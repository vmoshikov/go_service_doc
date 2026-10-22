---
title: "Функции: test/utils"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/utils
---


# Функции: test/utils


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_typecheck.md)


---


## Меню по файлам


- 📄 [test/utils/admission_webhook.go](#testutilsadmission_webhookgo)

- 📄 [test/utils/apiserver/testapiserver.go](#testutilsapiservertestapiservergo)

- 📄 [test/utils/audit.go](#testutilsauditgo)

- 📄 [test/utils/conditions.go](#testutilsconditionsgo)

- 📄 [test/utils/crd/crd_util.go](#testutilscrdcrd_utilgo)

- 📄 [test/utils/create_resources.go](#testutilscreate_resourcesgo)

- 📄 [test/utils/delete_resources.go](#testutilsdelete_resourcesgo)

- 📄 [test/utils/density_utils.go](#testutilsdensity_utilsgo)

- 📄 [test/utils/deployment.go](#testutilsdeploymentgo)

- 📄 [test/utils/fakedns/fakedns.go](#testutilsfakednsfakednsgo)

- 📄 [test/utils/format/format.go](#testutilsformatformatgo)

- 📄 [test/utils/harness/harness.go](#testutilsharnessharnessgo)

- 📄 [test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go](#testutilshermeticpodcertificatesignerhermeticpodcertificatesignergo)

- 📄 [test/utils/image/csi_manifest.go](#testutilsimagecsi_manifestgo)

- 📄 [test/utils/image/manifest.go](#testutilsimagemanifestgo)

- 📄 [test/utils/junit/junit.go](#testutilsjunitjunitgo)

- 📄 [test/utils/ktesting/assert.go](#testutilsktestingassertgo)

- 📄 [test/utils/ktesting/clientcontext.go](#testutilsktestingclientcontextgo)

- 📄 [test/utils/ktesting/contexthelper.go](#testutilsktestingcontexthelpergo)

- 📄 [test/utils/ktesting/errorcontext.go](#testutilsktestingerrorcontextgo)

- 📄 [test/utils/ktesting/initoption/initoption.go](#testutilsktestinginitoptioninitoptiongo)

- 📄 [test/utils/ktesting/klogcontext.go](#testutilsktestingklogcontextgo)

- 📄 [test/utils/ktesting/ktesting.go](#testutilsktestingktestinggo)

- 📄 [test/utils/ktesting/signals.go](#testutilsktestingsignalsgo)

- 📄 [test/utils/ktesting/stepcontext.go](#testutilsktestingstepcontextgo)

- 📄 [test/utils/ktesting/tcontext.go](#testutilsktestingtcontextgo)

- 📄 [test/utils/ktesting/withcontext.go](#testutilsktestingwithcontextgo)

- 📄 [test/utils/kubeconfig/kubeconfig.go](#testutilskubeconfigkubeconfiggo)

- 📄 [test/utils/localupcluster/cmd.go](#testutilslocalupclustercmdgo)

- 📄 [test/utils/localupcluster/localupcluster.go](#testutilslocalupclusterlocalupclustergo)

- 📄 [test/utils/node.go](#testutilsnodego)

- 📄 [test/utils/oidc/handlers/mocks.go](#testutilsoidchandlersmocksgo)

- 📄 [test/utils/oidc/testserver.go](#testutilsoidctestservergo)

- 📄 [test/utils/paths.go](#testutilspathsgo)

- 📄 [test/utils/pki_helpers.go](#testutilspki_helpersgo)

- 📄 [test/utils/pod_store.go](#testutilspod_storego)

- 📄 [test/utils/replicaset.go](#testutilsreplicasetgo)

- 📄 [test/utils/runners.go](#testutilsrunnersgo)

- 📄 [test/utils/tmpdir.go](#testutilstmpdirgo)

- 📄 [test/utils/update_resources.go](#testutilsupdate_resourcesgo)


---


## test/utils/admission_webhook.go


📄 Исходный файл: `test/utils/admission_webhook.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [AdmissionWebhookHandler](#admissionwebhookhandler-testutilsadmission_webhookgo55) `:55`

- 🔗 [NewAdmissionWebhookServer](#newadmissionwebhookserver-testutilsadmission_webhookgo34) `:34`


</details>


[function] name: AdmissionWebhookHandler file: test/utils/admission_webhook.go:55 returns_error: да description: AdmissionWebhookHandler creates a HandlerFunc that decodes/encodes AdmissionReview and performs
given admit function


### AdmissionWebhookHandler (test/utils/admission_webhook.go:55)


AdmissionWebhookHandler creates a HandlerFunc that decodes/encodes AdmissionReview and performs
given admit function


```go
func AdmissionWebhookHandler((t *testing.T, admit func(*v1beta1.AdmissionReview) error)) (t *testing.T, admit func(*v1beta1.AdmissionReview) error)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** v1beta1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


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


**Тип ответа:** admit


```json
{
  "v1beta1": {},
  "v1": {}
}
```


*Определено в:* `test/images/agnhost/webhook/main.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1beta1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `t *testing.T`, `admit func(*v1beta1.AdmissionReview) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/admission_webhook.go:55`



---


[function] name: NewAdmissionWebhookServer file: test/utils/admission_webhook.go:34 returns_error: да description: NewAdmissionWebhookServer sets up a webhook server with TLS enabled, returns URL and Close function
for the server


### NewAdmissionWebhookServer (test/utils/admission_webhook.go:34)


NewAdmissionWebhookServer sets up a webhook server with TLS enabled, returns URL and Close function
for the server


```go
func NewAdmissionWebhookServer((string, func(), error)) (string, func(), error)
```


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `func()`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/admission_webhook.go:34`




## test/utils/apiserver/testapiserver.go


📄 Исходный файл: `test/utils/apiserver/testapiserver.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [StartAPITestServer](#startapitestserver-testutilsapiservertestapiservergo49) `:49`

- 🔗 [writeKubeConfigForWardleServerToKASConnection](#writekubeconfigforwardleservertokasconnection-testutilsapiservertestapiservergo68) `:68`


</details>


[function] name: StartAPITestServer file: test/utils/apiserver/testapiserver.go:49 returns_error: нет description: StartAPIServer runs etcd and apiserver in the background in the same
process. All resources get released automatically w


### StartAPITestServer (test/utils/apiserver/testapiserver.go:49)


StartAPIServer runs etcd and apiserver in the background in the same
process. All resources get released automatically when the test
completes. If startup fails, the test gets aborted.


```go
func StartAPITestServer((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/utils/apiserver/testapiserver.go:49`



---


[function] name: writeKubeConfigForWardleServerToKASConnection file: test/utils/apiserver/testapiserver.go:68 returns_error: нет description: —


### writeKubeConfigForWardleServerToKASConnection (test/utils/apiserver/testapiserver.go:68)


writeKubeConfigForWardleServerToKASConnection is a function that performs operations based on the provided parameters and returns (t *testing.T, kubeClientConfig *rest.Config).


```go
func writeKubeConfigForWardleServerToKASConnection((t *testing.T, kubeClientConfig *rest.Config)) (t *testing.T, kubeClientConfig *rest.Config)
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


**Тип ответа:** kubeClientConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/utils/apiserver/testapiserver.go:68`




## test/utils/audit.go


📄 Исходный файл: `test/utils/audit.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [CheckAuditLines](#checkauditlines-testutilsauditgo86) `:86`

- 🔗 [CheckAuditLinesFiltered](#checkauditlinesfiltered-testutilsauditgo93) `:93`

- 🔗 [Mark](#mark-testutilsauditgo206) `:206`

- 🔗 [Missing](#missing-testutilsauditgo215) `:215`

- 🔗 [String](#string-testutilsauditgo73) `:73`

- 🔗 [newAuditEventTracker](#newauditeventtracker-testutilsauditgo196) `:196`

- 🔗 [testEventFromInternalFiltered](#testeventfrominternalfiltered-testutilsauditgo136) `:136`


</details>


[function] name: CheckAuditLines file: test/utils/audit.go:86 returns_error: да description: CheckAuditLines searches the audit log for the expected audit lines.


### CheckAuditLines (test/utils/audit.go:86)


CheckAuditLines searches the audit log for the expected audit lines.


```go
func CheckAuditLines((missingReport *MissingEventsReport, err error)) (missingReport *MissingEventsReport, err error)
```


**Тип запроса:** MissingEventsReport


```json
{
  "FirstEventChecked": null,
  "LastEventChecked": null,
  "NumEventsChecked": 0,
  "MissingEvents": [],
  "AllEvents": []
}
```


*Определено в:* `test/utils/audit.go`


**Тип ответа:** missingReport


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** MissingEventsReport


```json
{
  "FirstEventChecked": null,
  "LastEventChecked": null,
  "NumEventsChecked": 0,
  "MissingEvents": [],
  "AllEvents": []
}
```


*Определено в:* `test/utils/audit.go`


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


*Типы возврата:* `missingReport *MissingEventsReport`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/audit.go:86`



---


[function] name: CheckAuditLinesFiltered file: test/utils/audit.go:93 returns_error: да description: CheckAuditLinesFiltered searches the audit log for the expected audit lines, customAnnotationsFilter
controls which audi


### CheckAuditLinesFiltered (test/utils/audit.go:93)


CheckAuditLinesFiltered searches the audit log for the expected audit lines, customAnnotationsFilter
controls which audit annotations are added to AuditEvent.CustomAuditAnnotations.
If the customAnnotationsFilter is nil, AuditEvent.CustomAuditAnnotations will be empty.


```go
func CheckAuditLinesFiltered((missingReport *MissingEventsReport, err error)) (missingReport *MissingEventsReport, err error)
```


**Тип запроса:** MissingEventsReport


```json
{
  "FirstEventChecked": null,
  "LastEventChecked": null,
  "NumEventsChecked": 0,
  "MissingEvents": [],
  "AllEvents": []
}
```


*Определено в:* `test/utils/audit.go`


**Тип ответа:** missingReport


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** MissingEventsReport


```json
{
  "FirstEventChecked": null,
  "LastEventChecked": null,
  "NumEventsChecked": 0,
  "MissingEvents": [],
  "AllEvents": []
}
```


*Определено в:* `test/utils/audit.go`


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


*Типы возврата:* `missingReport *MissingEventsReport`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/audit.go:93`



---


[function] name: Mark file: test/utils/audit.go:206 returns_error: нет description: Mark marks the given event as found if it's expected


### Mark (test/utils/audit.go:206)


Mark marks the given event as found if it's expected


```go
func (t *auditEventTracker) Mark((event AuditEvent)) (event AuditEvent)
```


**Тип ответа:** event


```json
{
  "eventType": {},
  "obj": {},
  "oldObj": {},
  "gvr": {}
}
```


*Определено в:* `pkg/controller/resourcequota/resource_quota_monitor.go`


**Тип ответа:** AuditEvent


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


📍 *Расположение:* `test/utils/audit.go:206`



---


[function] name: Missing file: test/utils/audit.go:215 returns_error: нет description: Missing reports events that are expected but not found


### Missing (test/utils/audit.go:215)


Missing reports events that are expected but not found


```go
func (t *auditEventTracker) Missing(()) ()
```


📍 *Расположение:* `test/utils/audit.go:215`



---


[function] name: String file: test/utils/audit.go:73 returns_error: нет description: String returns a human readable string representation of the report


### String (test/utils/audit.go:73)


String returns a human readable string representation of the report


```go
func (m *MissingEventsReport) String(()) ()
```


📍 *Расположение:* `test/utils/audit.go:73`



---


[function] name: newAuditEventTracker file: test/utils/audit.go:196 returns_error: нет description: newAuditEventTracker creates a tracker that tracks whether expect events are found


### newAuditEventTracker (test/utils/audit.go:196)


newAuditEventTracker creates a tracker that tracks whether expect events are found


```go
func newAuditEventTracker((expected []AuditEvent)) (expected []AuditEvent)
```


**Тип ответа:** expected


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/errors/errors.go`


**Тип ответа:** AuditEvent


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


📍 *Расположение:* `test/utils/audit.go:196`



---


[function] name: testEventFromInternalFiltered file: test/utils/audit.go:136 returns_error: да description: testEventFromInternalFiltered takes an internal audit event and returns a test event, customAnnotationsFilter
controls w


### testEventFromInternalFiltered (test/utils/audit.go:136)


testEventFromInternalFiltered takes an internal audit event and returns a test event, customAnnotationsFilter
controls which audit annotations are added to AuditEvent.CustomAuditAnnotations.
If the customAnnotationsFilter is nil, AuditEvent.CustomAuditAnnotations will be empty.


```go
func testEventFromInternalFiltered((AuditEvent, error)) (AuditEvent, error)
```


**Тип ответа:** AuditEvent


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `AuditEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/audit.go:136`




## test/utils/conditions.go


📄 Исходный файл: `test/utils/conditions.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [FailedContainers](#failedcontainers-testutilsconditionsgo63) `:63`

- 🔗 [PodRunningReady](#podrunningready-testutilsconditionsgo33) `:33`

- 🔗 [PodRunningReadyOrSucceeded](#podrunningreadyorsucceeded-testutilsconditionsgo47) `:47`

- 🔗 [PodSucceeded](#podsucceeded-testutilsconditionsgo55) `:55`

- 🔗 [TerminatedContainers](#terminatedcontainers-testutilsconditionsgo93) `:93`


</details>


[function] name: FailedContainers file: test/utils/conditions.go:63 returns_error: нет description: FailedContainers inspects all containers in a pod and returns failure
information for containers that have failed or bee


### FailedContainers (test/utils/conditions.go:63)


FailedContainers inspects all containers in a pod and returns failure
information for containers that have failed or been restarted.
A map is returned where the key is the containerID and the value is a
struct containing the restart and failure information


```go
func FailedContainers((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `test/utils/conditions.go:63`



---


[function] name: PodRunningReady file: test/utils/conditions.go:33 returns_error: да description: PodRunningReady checks whether pod p's phase is running and it has a ready
condition of status true.


### PodRunningReady (test/utils/conditions.go:33)


PodRunningReady checks whether pod p's phase is running and it has a ready
condition of status true.


```go
func PodRunningReady((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/conditions.go:33`



---


[function] name: PodRunningReadyOrSucceeded file: test/utils/conditions.go:47 returns_error: да description: —


### PodRunningReadyOrSucceeded (test/utils/conditions.go:47)


PodRunningReadyOrSucceeded is a function that performs operations based on the provided parameters and may return an error.


```go
func PodRunningReadyOrSucceeded((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/conditions.go:47`



---


[function] name: PodSucceeded file: test/utils/conditions.go:55 returns_error: да description: —


### PodSucceeded (test/utils/conditions.go:55)


PodSucceeded is a function that performs operations based on the provided parameters and may return an error.


```go
func PodSucceeded((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/conditions.go:55`



---


[function] name: TerminatedContainers file: test/utils/conditions.go:93 returns_error: нет description: TerminatedContainers inspects all containers in a pod and returns a map
of "container name: termination reason", for all


### TerminatedContainers (test/utils/conditions.go:93)


TerminatedContainers inspects all containers in a pod and returns a map
of "container name: termination reason", for all currently terminated
containers.


```go
func TerminatedContainers((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `test/utils/conditions.go:93`




## test/utils/crd/crd_util.go


📄 Исходный файл: `test/utils/crd/crd_util.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [CreateMultiVersionTestCRD](#createmultiversiontestcrd-testutilscrdcrd_utilgo52) `:52`

- 🔗 [CreateTestCRD](#createtestcrd-testutilscrdcrd_utilgo150) `:150`

- 🔗 [genRandomCRD](#genrandomcrd-testutilscrdcrd_utilgo117) `:117`


</details>


[function] name: CreateMultiVersionTestCRD file: test/utils/crd/crd_util.go:52 returns_error: да description: CreateMultiVersionTestCRD creates a new CRD specifically for the calling test.


### CreateMultiVersionTestCRD (test/utils/crd/crd_util.go:52)


CreateMultiVersionTestCRD creates a new CRD specifically for the calling test.


```go
func CreateMultiVersionTestCRD((*TestCrd, error)) (*TestCrd, error)
```


**Тип запроса:** TestCrd


```json
{
  "APIExtensionClient": null,
  "Crd": null,
  "DynamicClients": {},
  "CleanUp": {}
}
```


*Определено в:* `test/utils/crd/crd_util.go`


**Тип ответа:** TestCrd


```json
{
  "APIExtensionClient": null,
  "Crd": null,
  "DynamicClients": {},
  "CleanUp": {}
}
```


*Определено в:* `test/utils/crd/crd_util.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TestCrd`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/crd/crd_util.go:52`



---


[function] name: CreateTestCRD file: test/utils/crd/crd_util.go:150 returns_error: да description: CreateTestCRD creates a new CRD specifically for the calling test.


### CreateTestCRD (test/utils/crd/crd_util.go:150)


CreateTestCRD creates a new CRD specifically for the calling test.


```go
func CreateTestCRD((*TestCrd, error)) (*TestCrd, error)
```


**Тип запроса:** TestCrd


```json
{
  "APIExtensionClient": null,
  "Crd": null,
  "DynamicClients": {},
  "CleanUp": {}
}
```


*Определено в:* `test/utils/crd/crd_util.go`


**Тип ответа:** TestCrd


```json
{
  "APIExtensionClient": null,
  "Crd": null,
  "DynamicClients": {},
  "CleanUp": {}
}
```


*Определено в:* `test/utils/crd/crd_util.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TestCrd`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/crd/crd_util.go:150`



---


[function] name: genRandomCRD file: test/utils/crd/crd_util.go:117 returns_error: нет description: genRandomCRD generates a random CRD name and kind based on the framework's base name and a random suffix.
It also sets t


### genRandomCRD (test/utils/crd/crd_util.go:117)


genRandomCRD generates a random CRD name and kind based on the framework's base name and a random suffix.
It also sets the group to the provided value and sets the scope to NamespaceScoped. If no versions are provided via
the opts, it will create a default version "v1" with an allow-all schema.


```go
func genRandomCRD((f *framework.Framework, group string, opts ...Option)) (f *framework.Framework, group string, opts ...Option)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** group


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/interface.go`


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Option


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `test/utils/crd/crd_util.go:117`




## test/utils/create_resources.go


📄 Исходный файл: `test/utils/create_resources.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [CreateDeploymentWithRetries](#createdeploymentwithretries-testutilscreate_resourcesgo104) `:104`

- 🔗 [CreatePersistentVolumeClaimWithRetries](#createpersistentvolumeclaimwithretries-testutilscreate_resourcesgo155) `:155`

- 🔗 [CreatePersistentVolumeWithRetries](#createpersistentvolumewithretries-testutilscreate_resourcesgo138) `:138`

- 🔗 [CreatePodWithRetries](#createpodwithretries-testutilscreate_resourcesgo53) `:53`

- 🔗 [CreateRCWithRetries](#creatercwithretries-testutilscreate_resourcesgo70) `:70`

- 🔗 [CreateReplicaSetWithRetries](#createreplicasetwithretries-testutilscreate_resourcesgo87) `:87`

- 🔗 [CreateServiceWithRetries](#createservicewithretries-testutilscreate_resourcesgo121) `:121`

- 🔗 [RetryWithExponentialBackOff](#retrywithexponentialbackoff-testutilscreate_resourcesgo43) `:43`

- 🔗 [isGenerateNameConflict](#isgeneratenameconflict-testutilscreate_resourcesgo173) `:173`


</details>


[function] name: CreateDeploymentWithRetries file: test/utils/create_resources.go:104 returns_error: нет description: —


### CreateDeploymentWithRetries (test/utils/create_resources.go:104)


CreateDeploymentWithRetries is a function that creates new data based on the provided parameters and returns (c clientset.Interface, namespace string, obj *apps.Deployment).


```go
func CreateDeploymentWithRetries((c clientset.Interface, namespace string, obj *apps.Deployment)) (c clientset.Interface, namespace string, obj *apps.Deployment)
```


**Тип запроса:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


📍 *Расположение:* `test/utils/create_resources.go:104`



---


[function] name: CreatePersistentVolumeClaimWithRetries file: test/utils/create_resources.go:155 returns_error: нет description: —


### CreatePersistentVolumeClaimWithRetries (test/utils/create_resources.go:155)


CreatePersistentVolumeClaimWithRetries is a function that creates new data based on the provided parameters and returns (c clientset.Interface, namespace string, obj *v1.PersistentVolumeClaim).


```go
func CreatePersistentVolumeClaimWithRetries((c clientset.Interface, namespace string, obj *v1.PersistentVolumeClaim)) (c clientset.Interface, namespace string, obj *v1.PersistentVolumeClaim)
```


**Тип запроса:** v1.PersistentVolumeClaim


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


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/utils/create_resources.go:155`



---


[function] name: CreatePersistentVolumeWithRetries file: test/utils/create_resources.go:138 returns_error: нет description: —


### CreatePersistentVolumeWithRetries (test/utils/create_resources.go:138)


CreatePersistentVolumeWithRetries is a function that creates new data based on the provided parameters and returns (c clientset.Interface, obj *v1.PersistentVolume).


```go
func CreatePersistentVolumeWithRetries((c clientset.Interface, obj *v1.PersistentVolume)) (c clientset.Interface, obj *v1.PersistentVolume)
```


**Тип запроса:** v1.PersistentVolume


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


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** v1.PersistentVolume


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/utils/create_resources.go:138`



---


[function] name: CreatePodWithRetries file: test/utils/create_resources.go:53 returns_error: нет description: —


### CreatePodWithRetries (test/utils/create_resources.go:53)


CreatePodWithRetries is a function that creates new data based on the provided parameters and returns (c clientset.Interface, namespace string, obj *v1.Pod).


```go
func CreatePodWithRetries((c clientset.Interface, namespace string, obj *v1.Pod)) (c clientset.Interface, namespace string, obj *v1.Pod)
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


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


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


📍 *Расположение:* `test/utils/create_resources.go:53`



---


[function] name: CreateRCWithRetries file: test/utils/create_resources.go:70 returns_error: нет description: —


### CreateRCWithRetries (test/utils/create_resources.go:70)


CreateRCWithRetries is a function that creates new data based on the provided parameters and returns (c clientset.Interface, namespace string, obj *v1.ReplicationController).


```go
func CreateRCWithRetries((c clientset.Interface, namespace string, obj *v1.ReplicationController)) (c clientset.Interface, namespace string, obj *v1.ReplicationController)
```


**Тип запроса:** v1.ReplicationController


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


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** v1.ReplicationController


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/utils/create_resources.go:70`



---


[function] name: CreateReplicaSetWithRetries file: test/utils/create_resources.go:87 returns_error: нет description: —


### CreateReplicaSetWithRetries (test/utils/create_resources.go:87)


CreateReplicaSetWithRetries is a function that creates new data based on the provided parameters and returns (c clientset.Interface, namespace string, obj *apps.ReplicaSet).


```go
func CreateReplicaSetWithRetries((c clientset.Interface, namespace string, obj *apps.ReplicaSet)) (c clientset.Interface, namespace string, obj *apps.ReplicaSet)
```


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


📍 *Расположение:* `test/utils/create_resources.go:87`



---


[function] name: CreateServiceWithRetries file: test/utils/create_resources.go:121 returns_error: нет description: —


### CreateServiceWithRetries (test/utils/create_resources.go:121)


CreateServiceWithRetries is a function that creates new data based on the provided parameters and returns (c clientset.Interface, namespace string, obj *v1.Service).


```go
func CreateServiceWithRetries((c clientset.Interface, namespace string, obj *v1.Service)) (c clientset.Interface, namespace string, obj *v1.Service)
```


**Тип запроса:** v1.Service


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


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/utils/create_resources.go:121`



---


[function] name: RetryWithExponentialBackOff file: test/utils/create_resources.go:43 returns_error: нет description: Utility for retrying the given function with exponential backoff.


### RetryWithExponentialBackOff (test/utils/create_resources.go:43)


Utility for retrying the given function with exponential backoff.


```go
func RetryWithExponentialBackOff((fn wait.ConditionFunc)) (fn wait.ConditionFunc)
```


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** wait.ConditionFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/create_resources.go:43`



---


[function] name: isGenerateNameConflict file: test/utils/create_resources.go:173 returns_error: да description: isGenerateNameConflict returns whether the error is generateName conflict or not.


### isGenerateNameConflict (test/utils/create_resources.go:173)


isGenerateNameConflict returns whether the error is generateName conflict or not.


```go
func isGenerateNameConflict((meta metav1.ObjectMeta, err error)) (meta metav1.ObjectMeta, err error)
```


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


*Типы возврата:* `meta metav1.ObjectMeta`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/create_resources.go:173`




## test/utils/delete_resources.go


📄 Исходный файл: `test/utils/delete_resources.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DeleteResource](#deleteresource-testutilsdelete_resourcesgo34) `:34`


</details>


[function] name: DeleteResource file: test/utils/delete_resources.go:34 returns_error: нет description: —


### DeleteResource (test/utils/delete_resources.go:34)


DeleteResource is a function that deletes data based on the provided parameters and returns (c clientset.Interface, kind schema.GroupKind, namespace, name string, options metav1.DeleteOptions).


```go
func DeleteResource((c clientset.Interface, kind schema.GroupKind, namespace, name string, options metav1.DeleteOptions)) (c clientset.Interface, kind schema.GroupKind, namespace, name string, options metav1.DeleteOptions)
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


**Тип ответа:** kind


```json
{
  "restMapping": null
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/apply/applyset.go`


**Тип ответа:** schema.GroupKind


```json
{
  "Group": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


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


**Тип ответа:** metav1.DeleteOptions


```json
{
  "gracePeriodSeconds": 0,
  "preconditions": null,
  "orphanDependents": false,
  "propagationPolicy": null,
  "dryRun": [],
  "ignoreStoreReadErrorWithClusterBreakingPotential": false
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


📍 *Расположение:* `test/utils/delete_resources.go:34`




## test/utils/density_utils.go


📄 Исходный файл: `test/utils/density_utils.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddLabelsToNode](#addlabelstonode-testutilsdensity_utilsgo38) `:38`

- 🔗 [RemoveLabelOffNode](#removelabeloffnode-testutilsdensity_utilsgo62) `:62`

- 🔗 [VerifyLabelsRemoved](#verifylabelsremoved-testutilsdensity_utilsgo96) `:96`


</details>


[function] name: AddLabelsToNode file: test/utils/density_utils.go:38 returns_error: нет description: —


### AddLabelsToNode (test/utils/density_utils.go:38)


AddLabelsToNode is a function that creates new data based on the provided parameters and returns (c clientset.Interface, nodeName string, labels map[string]string).


```go
func AddLabelsToNode((c clientset.Interface, nodeName string, labels map[string]string)) (c clientset.Interface, nodeName string, labels map[string]string)
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


**Тип ответа:** nodeName


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


📍 *Расположение:* `test/utils/density_utils.go:38`



---


[function] name: RemoveLabelOffNode file: test/utils/density_utils.go:62 returns_error: нет description: RemoveLabelOffNode is for cleaning up labels temporarily added to node,
won't fail if target label doesn't exist or has 


### RemoveLabelOffNode (test/utils/density_utils.go:62)


RemoveLabelOffNode is for cleaning up labels temporarily added to node,
won't fail if target label doesn't exist or has been removed.


```go
func RemoveLabelOffNode((c clientset.Interface, nodeName string, labelKeys []string)) (c clientset.Interface, nodeName string, labelKeys []string)
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


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelKeys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/density_utils.go:62`



---


[function] name: VerifyLabelsRemoved file: test/utils/density_utils.go:96 returns_error: нет description: VerifyLabelsRemoved checks if Node for given nodeName does not have any of labels from labelKeys.
Return non-nil error i


### VerifyLabelsRemoved (test/utils/density_utils.go:96)


VerifyLabelsRemoved checks if Node for given nodeName does not have any of labels from labelKeys.
Return non-nil error if it does.


```go
func VerifyLabelsRemoved((c clientset.Interface, nodeName string, labelKeys []string)) (c clientset.Interface, nodeName string, labelKeys []string)
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


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelKeys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/density_utils.go:96`




## test/utils/deployment.go


📄 Исходный файл: `test/utils/deployment.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [CheckDeploymentRevisionAndImage](#checkdeploymentrevisionandimage-testutilsdeploymentgo253) `:253`

- 🔗 [GetAllReplicaSets](#getallreplicasets-testutilsdeploymentgo158) `:158`

- 🔗 [GetNewReplicaSet](#getnewreplicaset-testutilsdeploymentgo181) `:181`

- 🔗 [GetOldReplicaSets](#getoldreplicasets-testutilsdeploymentgo170) `:170`

- 🔗 [LogPodsOfDeployment](#logpodsofdeployment-testutilsdeploymentgo52) `:52`

- 🔗 [LogReplicaSetsOfDeployment](#logreplicasetsofdeployment-testutilsdeploymentgo38) `:38`

- 🔗 [UpdateDeploymentWithRetries](#updatedeploymentwithretries-testutilsdeploymentgo303) `:303`

- 🔗 [WaitForDeploymentComplete](#waitfordeploymentcomplete-testutilsdeploymentgo199) `:199`

- 🔗 [WaitForDeploymentCompleteAndCheckRolling](#waitfordeploymentcompleteandcheckrolling-testutilsdeploymentgo191) `:191`

- 🔗 [WaitForDeploymentRevisionAndImage](#waitfordeploymentrevisionandimage-testutilsdeploymentgo206) `:206`

- 🔗 [WaitForDeploymentUpdatedReplicasGTE](#waitfordeploymentupdatedreplicasgte-testutilsdeploymentgo333) `:333`

- 🔗 [WaitForDeploymentWithCondition](#waitfordeploymentwithcondition-testutilsdeploymentgo349) `:349`

- 🔗 [WaitForObservedDeployment](#waitforobserveddeployment-testutilsdeploymentgo326) `:326`

- 🔗 [checkRevisionAndImage](#checkrevisionandimage-testutilsdeploymentgo267) `:267`

- 🔗 [checkRollingUpdateStatus](#checkrollingupdatestatus-testutilsdeploymentgo118) `:118`

- 🔗 [containsImage](#containsimage-testutilsdeploymentgo292) `:292`

- 🔗 [waitForDeploymentCompleteMaybeCheckRolling](#waitfordeploymentcompletemaybecheckrolling-testutilsdeploymentgo76) `:76`


</details>


[function] name: CheckDeploymentRevisionAndImage file: test/utils/deployment.go:253 returns_error: нет description: CheckDeploymentRevisionAndImage checks if the input deployment's and its new replica set's revision and image are as exp


### CheckDeploymentRevisionAndImage (test/utils/deployment.go:253)


CheckDeploymentRevisionAndImage checks if the input deployment's and its new replica set's revision and image are as expected.


```go
func CheckDeploymentRevisionAndImage((c clientset.Interface, ns, deploymentName, revision, image string)) (c clientset.Interface, ns, deploymentName, revision, image string)
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


**Тип ответа:** deploymentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/utils/deployment.go:253`



---


[function] name: GetAllReplicaSets file: test/utils/deployment.go:158 returns_error: да description: GetAllReplicaSets returns the old and new replica sets targeted by the given Deployment. It gets PodList and ReplicaSetL


### GetAllReplicaSets (test/utils/deployment.go:158)


GetAllReplicaSets returns the old and new replica sets targeted by the given Deployment. It gets PodList and ReplicaSetList from client interface.
Note that the first set of old replica sets doesn't include the ones with no pods, and the second set of old replica sets include all old replica sets.
The third returned value is the new replica set, and it may be nil if it doesn't exist yet.


```go
func GetAllReplicaSets(([]*apps.ReplicaSet, []*apps.ReplicaSet, *apps.ReplicaSet, error)) ([]*apps.ReplicaSet, []*apps.ReplicaSet, *apps.ReplicaSet, error)
```


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** apps.ReplicaSet


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


*Типы возврата:* `[]*apps.ReplicaSet`, `[]*apps.ReplicaSet`, `*apps.ReplicaSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/deployment.go:158`



---


[function] name: GetNewReplicaSet file: test/utils/deployment.go:181 returns_error: да description: GetNewReplicaSet returns a replica set that matches the intent of the given deployment; get ReplicaSetList from client i


### GetNewReplicaSet (test/utils/deployment.go:181)


GetNewReplicaSet returns a replica set that matches the intent of the given deployment; get ReplicaSetList from client interface.
Returns nil if the new replica set doesn't exist yet.


```go
func GetNewReplicaSet((*apps.ReplicaSet, error)) (*apps.ReplicaSet, error)
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


📍 *Расположение:* `test/utils/deployment.go:181`



---


[function] name: GetOldReplicaSets file: test/utils/deployment.go:170 returns_error: да description: GetOldReplicaSets returns the old replica sets targeted by the given Deployment; get PodList and ReplicaSetList from cli


### GetOldReplicaSets (test/utils/deployment.go:170)


GetOldReplicaSets returns the old replica sets targeted by the given Deployment; get PodList and ReplicaSetList from client interface.
Note that the first set of old replica sets doesn't include the ones with no pods, and the second set of old replica sets include all old replica sets.


```go
func GetOldReplicaSets(([]*apps.ReplicaSet, []*apps.ReplicaSet, error)) ([]*apps.ReplicaSet, []*apps.ReplicaSet, error)
```


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*apps.ReplicaSet`, `[]*apps.ReplicaSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/deployment.go:170`



---


[function] name: LogPodsOfDeployment file: test/utils/deployment.go:52 returns_error: нет description: —


### LogPodsOfDeployment (test/utils/deployment.go:52)


LogPodsOfDeployment is a function that performs operations based on the provided parameters and returns (c clientset.Interface, deployment *apps.Deployment, rsList []*apps.ReplicaSet, logf LogfFn).


```go
func LogPodsOfDeployment((c clientset.Interface, deployment *apps.Deployment, rsList []*apps.ReplicaSet, logf LogfFn)) (c clientset.Interface, deployment *apps.Deployment, rsList []*apps.ReplicaSet, logf LogfFn)
```


**Тип запроса:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** deployment


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/apps/v1beta1/deployment.go`


**Тип ответа:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** rsList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** logf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** LogfFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/deployment.go:52`



---


[function] name: LogReplicaSetsOfDeployment file: test/utils/deployment.go:38 returns_error: нет description: —


### LogReplicaSetsOfDeployment (test/utils/deployment.go:38)


LogReplicaSetsOfDeployment is a function that performs operations based on the provided parameters and returns (deployment *apps.Deployment, allOldRSs []*apps.ReplicaSet, newRS *apps.ReplicaSet, logf LogfFn).


```go
func LogReplicaSetsOfDeployment((deployment *apps.Deployment, allOldRSs []*apps.ReplicaSet, newRS *apps.ReplicaSet, logf LogfFn)) (deployment *apps.Deployment, allOldRSs []*apps.ReplicaSet, newRS *apps.ReplicaSet, logf LogfFn)
```


**Тип запроса:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** deployment


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/apps/v1beta1/deployment.go`


**Тип ответа:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** allOldRSs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** newRS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** logf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** LogfFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/deployment.go:38`



---


[function] name: UpdateDeploymentWithRetries file: test/utils/deployment.go:303 returns_error: да description: —


### UpdateDeploymentWithRetries (test/utils/deployment.go:303)


UpdateDeploymentWithRetries is a function that updates data based on the provided parameters and may return an error.


```go
func UpdateDeploymentWithRetries((*apps.Deployment, error)) (*apps.Deployment, error)
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


📍 *Расположение:* `test/utils/deployment.go:303`



---


[function] name: WaitForDeploymentComplete file: test/utils/deployment.go:199 returns_error: нет description: Waits for the deployment to complete, and don't check if rolling update strategy is broken.
Rolling update strategy is u


### WaitForDeploymentComplete (test/utils/deployment.go:199)


Waits for the deployment to complete, and don't check if rolling update strategy is broken.
Rolling update strategy is used only during a rolling update, and can be violated in other situations,
such as shortly after a scaling event or the deployment is just created.


```go
func WaitForDeploymentComplete((c clientset.Interface, d *apps.Deployment, logf LogfFn, pollInterval, pollTimeout time.Duration)) (c clientset.Interface, d *apps.Deployment, logf LogfFn, pollInterval, pollTimeout time.Duration)
```


**Тип запроса:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** logf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** LogfFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollTimeout


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


📍 *Расположение:* `test/utils/deployment.go:199`



---


[function] name: WaitForDeploymentCompleteAndCheckRolling file: test/utils/deployment.go:191 returns_error: нет description: Waits for the deployment to complete, and check rolling update strategy isn't broken at any times.
Rolling update strate


### WaitForDeploymentCompleteAndCheckRolling (test/utils/deployment.go:191)


Waits for the deployment to complete, and check rolling update strategy isn't broken at any times.
Rolling update strategy should not be broken during a rolling update.


```go
func WaitForDeploymentCompleteAndCheckRolling((c clientset.Interface, d *apps.Deployment, logf LogfFn, pollInterval, pollTimeout time.Duration)) (c clientset.Interface, d *apps.Deployment, logf LogfFn, pollInterval, pollTimeout time.Duration)
```


**Тип запроса:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** logf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** LogfFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollTimeout


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


📍 *Расположение:* `test/utils/deployment.go:191`



---


[function] name: WaitForDeploymentRevisionAndImage file: test/utils/deployment.go:206 returns_error: нет description: WaitForDeploymentRevisionAndImage waits for the deployment's and its new RS's revision and container image to match the 


### WaitForDeploymentRevisionAndImage (test/utils/deployment.go:206)


WaitForDeploymentRevisionAndImage waits for the deployment's and its new RS's revision and container image to match the given revision and image.
Note that deployment revision and its new RS revision should be updated shortly, so we only wait for 1 minute here to fail early.


```go
func WaitForDeploymentRevisionAndImage((c clientset.Interface, ns, deploymentName string, revision, image string, logf LogfFn, pollInterval, pollTimeout time.Duration)) (c clientset.Interface, ns, deploymentName string, revision, image string, logf LogfFn, pollInterval, pollTimeout time.Duration)
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


**Тип ответа:** deploymentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** logf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** LogfFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollTimeout


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


📍 *Расположение:* `test/utils/deployment.go:206`



---


[function] name: WaitForDeploymentUpdatedReplicasGTE file: test/utils/deployment.go:333 returns_error: нет description: WaitForDeploymentUpdatedReplicasGTE waits for given deployment to be observed by the controller and has at least a numbe


### WaitForDeploymentUpdatedReplicasGTE (test/utils/deployment.go:333)


WaitForDeploymentUpdatedReplicasGTE waits for given deployment to be observed by the controller and has at least a number of updatedReplicas


```go
func WaitForDeploymentUpdatedReplicasGTE((c clientset.Interface, ns, deploymentName string, minUpdatedReplicas int32, desiredGeneration int64, pollInterval, pollTimeout time.Duration)) (c clientset.Interface, ns, deploymentName string, minUpdatedReplicas int32, desiredGeneration int64, pollInterval, pollTimeout time.Duration)
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


**Тип ответа:** deploymentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** minUpdatedReplicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desiredGeneration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollTimeout


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


📍 *Расположение:* `test/utils/deployment.go:333`



---


[function] name: WaitForDeploymentWithCondition file: test/utils/deployment.go:349 returns_error: нет description: —


### WaitForDeploymentWithCondition (test/utils/deployment.go:349)


WaitForDeploymentWithCondition is a function that performs operations based on the provided parameters and returns (c clientset.Interface, ns, deploymentName, reason string, condType apps.DeploymentConditionType, logf LogfFn, pollInterval, pollTimeout time.Duration).


```go
func WaitForDeploymentWithCondition((c clientset.Interface, ns, deploymentName, reason string, condType apps.DeploymentConditionType, logf LogfFn, pollInterval, pollTimeout time.Duration)) (c clientset.Interface, ns, deploymentName, reason string, condType apps.DeploymentConditionType, logf LogfFn, pollInterval, pollTimeout time.Duration)
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


**Тип ответа:** deploymentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** condType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apps.DeploymentConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** LogfFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollTimeout


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


📍 *Расположение:* `test/utils/deployment.go:349`



---


[function] name: WaitForObservedDeployment file: test/utils/deployment.go:326 returns_error: нет description: —


### WaitForObservedDeployment (test/utils/deployment.go:326)


WaitForObservedDeployment is a function that performs operations based on the provided parameters and returns (c clientset.Interface, ns, deploymentName string, desiredGeneration int64).


```go
func WaitForObservedDeployment((c clientset.Interface, ns, deploymentName string, desiredGeneration int64)) (c clientset.Interface, ns, deploymentName string, desiredGeneration int64)
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


**Тип ответа:** deploymentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desiredGeneration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/deployment.go:326`



---


[function] name: checkRevisionAndImage file: test/utils/deployment.go:267 returns_error: нет description: —


### checkRevisionAndImage (test/utils/deployment.go:267)


checkRevisionAndImage is a function that performs operations based on the provided parameters and returns (deployment *apps.Deployment, newRS *apps.ReplicaSet, revision, image string).


```go
func checkRevisionAndImage((deployment *apps.Deployment, newRS *apps.ReplicaSet, revision, image string)) (deployment *apps.Deployment, newRS *apps.ReplicaSet, revision, image string)
```


**Тип запроса:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип запроса:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** deployment


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/apps/v1beta1/deployment.go`


**Тип ответа:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** newRS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


📍 *Расположение:* `test/utils/deployment.go:267`



---


[function] name: checkRollingUpdateStatus file: test/utils/deployment.go:118 returns_error: да description: —


### checkRollingUpdateStatus (test/utils/deployment.go:118)


checkRollingUpdateStatus is a function that performs operations based on the provided parameters and may return an error.


```go
func checkRollingUpdateStatus((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/deployment.go:118`



---


[function] name: containsImage file: test/utils/deployment.go:292 returns_error: нет description: —


### containsImage (test/utils/deployment.go:292)


containsImage is a function that performs operations based on the provided parameters and returns (containers []v1.Container, imageName string).


```go
func containsImage((containers []v1.Container, imageName string)) (containers []v1.Container, imageName string)
```


**Тип ответа:** containers


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


**Тип ответа:** imageName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/deployment.go:292`



---


[function] name: waitForDeploymentCompleteMaybeCheckRolling file: test/utils/deployment.go:76 returns_error: нет description: Waits for the deployment to complete.
If during a rolling update (rolling == true), returns an error if the deployment's


### waitForDeploymentCompleteMaybeCheckRolling (test/utils/deployment.go:76)


Waits for the deployment to complete.
If during a rolling update (rolling == true), returns an error if the deployment's
rolling update strategy (max unavailable or max surge) is broken at any times.
It's not seen as a rolling update if shortly after a scaling event or the deployment is just created.


```go
func waitForDeploymentCompleteMaybeCheckRolling((c clientset.Interface, d *apps.Deployment, rolling bool, logf LogfFn, pollInterval, pollTimeout time.Duration)) (c clientset.Interface, d *apps.Deployment, rolling bool, logf LogfFn, pollInterval, pollTimeout time.Duration)
```


**Тип запроса:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


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


**Тип ответа:** apps.Deployment


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** rolling


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** LogfFn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollTimeout


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


📍 *Расположение:* `test/utils/deployment.go:76`




## test/utils/fakedns/fakedns.go


📄 Исходный файл: `test/utils/fakedns/fakedns.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Hijack](#hijack-testutilsfakednsfakednsgo113) `:113`

- 🔗 [NewServer](#newserver-testutilsfakednsfakednsgo52) `:52`


</details>


[function] name: Hijack file: test/utils/fakedns/fakedns.go:113 returns_error: нет description: Hijack takes control of the net.DefaultResolver to redirect DNS queries
to the fake server. It uses t.Cleanup to automat


### Hijack (test/utils/fakedns/fakedns.go:113)


Hijack takes control of the net.DefaultResolver to redirect DNS queries
to the fake server. It uses t.Cleanup to automatically restore the original
resolver after the test.
This helper does not support running tests in parallel.

Example:

dnsServer, _ := fakedns.NewServer(hosts)
dnsServer.Hijack(t)


```go
func (s *Server) Hijack((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/utils/fakedns/fakedns.go:113`



---


[function] name: NewServer file: test/utils/fakedns/fakedns.go:52 returns_error: да description: NewServer creates a new fake DNS server. The hosts map should contain
domain names as keys and their corresponding IP ad


### NewServer (test/utils/fakedns/fakedns.go:52)


NewServer creates a new fake DNS server. The hosts map should contain
domain names as keys and their corresponding IP addresses as string values.
It returns an error if any of the IP addresses are invalid.


```go
func NewServer((*Server, error)) (*Server, error)
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


📍 *Расположение:* `test/utils/fakedns/fakedns.go:52`




## test/utils/format/format.go


📄 Исходный файл: `test/utils/format/format.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Object](#object-testutilsformatformatgo41) `:41`

- 🔗 [handleYAML](#handleyaml-testutilsformatformatgo51) `:51`

- 🔗 [init](#init-testutilsformatformatgo35) `:35`

- 🔗 [useYAML](#useyaml-testutilsformatformatgo65) `:65`


</details>


[function] name: Object file: test/utils/format/format.go:41 returns_error: нет description: Object makes Gomega's [format.Object] available without having to import that
package.


### Object (test/utils/format/format.go:41)


Object makes Gomega's [format.Object] available without having to import that
package.


```go
func Object((object interface{}, indentation uint)) (object interface{}, indentation uint)
```


**Тип ответа:** object


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


**Тип ответа:** indentation


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/format/format.go:41`



---


[function] name: handleYAML file: test/utils/format/format.go:51 returns_error: нет description: handleYAML formats all values as YAML where the result
is likely to look better as YAML:
- pointer to struct or struct w


### handleYAML (test/utils/format/format.go:51)


handleYAML formats all values as YAML where the result
is likely to look better as YAML:
- pointer to struct or struct where all fields
have `json` tags
- slices containing such a value
- maps where the key or value are such a value


```go
func handleYAML((string, bool)) (string, bool)
```


📍 *Расположение:* `test/utils/format/format.go:51`



---


[function] name: init file: test/utils/format/format.go:35 returns_error: нет description: —


### init (test/utils/format/format.go:35)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/utils/format/format.go:35`



---


[function] name: useYAML file: test/utils/format/format.go:65 returns_error: нет description: —


### useYAML (test/utils/format/format.go:65)


useYAML is a function that performs operations based on the provided parameters and returns (t reflect.Type).


```go
func useYAML((t reflect.Type)) (t reflect.Type)
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


**Тип ответа:** reflect.Type


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `test/utils/format/format.go:65`




## test/utils/harness/harness.go


📄 Исходный файл: `test/utils/harness/harness.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Close](#close-testutilsharnessharnessgo52) `:52`

- 🔗 [For](#for-testutilsharnessharnessgo46) `:46`

- 🔗 [TempDir](#tempdir-testutilsharnessharnessgo63) `:63`


</details>


[function] name: Close file: test/utils/harness/harness.go:52 returns_error: нет description: Close cleans up any owned resources, and should be called in a defer block after For


### Close (test/utils/harness/harness.go:52)


Close cleans up any owned resources, and should be called in a defer block after For


```go
func (h *Harness) Close(()) ()
```


📍 *Расположение:* `test/utils/harness/harness.go:52`



---


[function] name: For file: test/utils/harness/harness.go:46 returns_error: нет description: For creates a Harness from a testing.T
Callers must call Close on the Harness so that resources can be cleaned up


### For (test/utils/harness/harness.go:46)


For creates a Harness from a testing.T
Callers must call Close on the Harness so that resources can be cleaned up


```go
func For((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/utils/harness/harness.go:46`



---


[function] name: TempDir file: test/utils/harness/harness.go:63 returns_error: нет description: TempDir is a wrapper around os.MkdirTemp for tests.
It automatically fails the test if we can't create a temp file,
and 


### TempDir (test/utils/harness/harness.go:63)


TempDir is a wrapper around os.MkdirTemp for tests.
It automatically fails the test if we can't create a temp file,
and deletes the temp directory when Close is called on the Harness


```go
func (h *Harness) TempDir((baseDir string, prefix string)) (baseDir string, prefix string)
```


**Тип ответа:** baseDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


📍 *Расположение:* `test/utils/harness/harness.go:63`




## test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go


📄 Исходный файл: `test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [GenerateCAHierarchy](#generatecahierarchy-testutilshermeticpodcertificatesignerhermeticpodcertificatesignergo328) `:328`

- 🔗 [New](#new-testutilshermeticpodcertificatesignerhermeticpodcertificatesignergo65) `:65`

- 🔗 [Run](#run-testutilshermeticpodcertificatesignerhermeticpodcertificatesignergo110) `:110`

- 🔗 [ensureTrustBundle](#ensuretrustbundle-testutilshermeticpodcertificatesignerhermeticpodcertificatesignergo132) `:132`

- 🔗 [handlePCR](#handlepcr-testutilshermeticpodcertificatesignerhermeticpodcertificatesignergo213) `:213`

- 🔗 [processNextWorkItem](#processnextworkitem-testutilshermeticpodcertificatesignerhermeticpodcertificatesignergo178) `:178`

- 🔗 [runWorker](#runworker-testutilshermeticpodcertificatesignerhermeticpodcertificatesignergo173) `:173`


</details>


[function] name: GenerateCAHierarchy file: test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:328 returns_error: да description: GenerateCAHierarchy makes a CA hierarchy, possibly with intermediates.  The
outputs can be used with Controller.


### GenerateCAHierarchy (test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:328)


GenerateCAHierarchy makes a CA hierarchy, possibly with intermediates.  The
outputs can be used with Controller.


```go
func GenerateCAHierarchy(([]crypto.PrivateKey, [][]byte, error)) ([]crypto.PrivateKey, [][]byte, error)
```


**Тип ответа:** crypto.PrivateKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]crypto.PrivateKey`, `[][]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:328`



---


[function] name: New file: test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:65 returns_error: нет description: New creates a new Controller.


### New (test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:65)


New creates a new Controller.


```go
func New((clock clock.PassiveClock, signerName string, caKeys []crypto.PrivateKey, caCerts [][]byte, kc kubernetes.Interface)) (clock clock.PassiveClock, signerName string, caKeys []crypto.PrivateKey, caCerts [][]byte, kc kubernetes.Interface)
```


**Тип ответа:** clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clock.PassiveClock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** signerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** caKeys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** crypto.PrivateKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** caCerts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kc


```json
{
  "keyID": "string",
  "aead": {}
}
```


*Определено в:* `staging/src/k8s.io/kms/internal/plugins/_mock/pkcs11/pkcs11.go`


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:65`



---


[function] name: Run file: test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:110 returns_error: нет description: —


### Run (test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:110)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:110`



---


[function] name: ensureTrustBundle file: test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:132 returns_error: нет description: —


### ensureTrustBundle (test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:132)


ensureTrustBundle is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) ensureTrustBundle((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:132`



---


[function] name: handlePCR file: test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:213 returns_error: нет description: —


### handlePCR (test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:213)


handlePCR is a method that performs operations based on the provided parameters and returns (ctx context.Context, pcr *certsv1beta1.PodCertificateRequest).


```go
func (c *Controller) handlePCR((ctx context.Context, pcr *certsv1beta1.PodCertificateRequest)) (ctx context.Context, pcr *certsv1beta1.PodCertificateRequest)
```


**Тип запроса:** certsv1beta1.PodCertificateRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/certificates/types.go`


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


📍 *Расположение:* `test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:213`



---


[function] name: processNextWorkItem file: test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:178 returns_error: нет description: —


### processNextWorkItem (test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:178)


processNextWorkItem is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *Controller) processNextWorkItem((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:178`



---


[function] name: runWorker file: test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:173 returns_error: нет description: —


### runWorker (test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:173)


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


📍 *Расположение:* `test/utils/hermeticpodcertificatesigner/hermeticpodcertificatesigner.go:173`




## test/utils/image/csi_manifest.go


📄 Исходный файл: `test/utils/image/csi_manifest.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [appendCSIImageConfigs](#appendcsiimageconfigs-testutilsimagecsi_manifestgo36) `:36`

- 🔗 [findStrings](#findstrings-testutilsimagecsi_manifestgo112) `:112`


</details>


[function] name: appendCSIImageConfigs file: test/utils/image/csi_manifest.go:36 returns_error: нет description: appendCSIImageConfigs extracts image repo, name and version from
the YAML files under test/e2e/testing-manifests/storage


### appendCSIImageConfigs (test/utils/image/csi_manifest.go:36)


appendCSIImageConfigs extracts image repo, name and version from
the YAML files under test/e2e/testing-manifests/storage-csi and
creates new config entries  for them.


```go
func appendCSIImageConfigs((configs map[ImageID]Config)) (configs map[ImageID]Config)
```


**Тип ответа:** configs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/utils/image/csi_manifest.go:36`



---


[function] name: findStrings file: test/utils/image/csi_manifest.go:112 returns_error: нет description: findStrings recursively decends into an object along a certain path.  Path
elements are the named fields. If a field ref


### findStrings (test/utils/image/csi_manifest.go:112)


findStrings recursively decends into an object along a certain path.  Path
elements are the named fields. If a field references a list, each of the
list elements will be followed.

Conceptually this is similar to a JSON path.


```go
func findStrings((object interface{}, visit func(value string), path ...string)) (object interface{}, visit func(value string), path ...string)
```


**Тип ответа:** object


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


**Тип ответа:** visit


```json
{
  "a1": {},
  "a2": {},
  "typ": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/third_party/forked/golang/reflect/deep_equal.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


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


📍 *Расположение:* `test/utils/image/csi_manifest.go:112`




## test/utils/image/manifest.go


📄 Исходный файл: `test/utils/image/manifest.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [GetConfig](#getconfig-testutilsimagemanifestgo326) `:326`

- 🔗 [GetE2EImage](#gete2eimage-testutilsimagemanifestgo331) `:331`

- 🔗 [GetE2EImage](#gete2eimage-testutilsimagemanifestgo336) `:336`

- 🔗 [GetImageConfigs](#getimageconfigs-testutilsimagemanifestgo321) `:321`

- 🔗 [GetMappedImageConfigs](#getmappedimageconfigs-testutilsimagemanifestgo256) `:256`

- 🔗 [GetOriginalImageConfigs](#getoriginalimageconfigs-testutilsimagemanifestgo316) `:316`

- 🔗 [GetPauseImageName](#getpauseimagename-testutilsimagemanifestgo341) `:341`

- 🔗 [Init](#init-testutilsimagemanifestgo69) `:69`

- 🔗 [ReplaceRegistryInImageURL](#replaceregistryinimageurl-testutilsimagemanifestgo347) `:347`

- 🔗 [SetName](#setname-testutilsimagemanifestgo60) `:60`

- 🔗 [SetRegistry](#setregistry-testutilsimagemanifestgo55) `:55`

- 🔗 [SetVersion](#setversion-testutilsimagemanifestgo65) `:65`

- 🔗 [getRepositoryMappedConfig](#getrepositorymappedconfig-testutilsimagemanifestgo285) `:285`

- 🔗 [initImageConfigs](#initimageconfigs-testutilsimagemanifestgo209) `:209`

- 🔗 [readFromURL](#readfromurl-testutilsimagemanifestgo109) `:109`

- 🔗 [readRepoList](#readrepolist-testutilsimagemanifestgo73) `:73`

- 🔗 [replaceRegistryInImageURLWithList](#replaceregistryinimageurlwithlist-testutilsimagemanifestgo353) `:353`


</details>


[function] name: GetConfig file: test/utils/image/manifest.go:326 returns_error: нет description: GetConfig returns the Config object for an image


### GetConfig (test/utils/image/manifest.go:326)


GetConfig returns the Config object for an image


```go
func GetConfig((image ImageID)) (image ImageID)
```


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/image/manifest.go:326`



---


[function] name: GetE2EImage file: test/utils/image/manifest.go:331 returns_error: нет description: GetE2EImage returns the fully qualified URI to an image (including version)


### GetE2EImage (test/utils/image/manifest.go:331)


GetE2EImage returns the fully qualified URI to an image (including version)


```go
func GetE2EImage((image ImageID)) (image ImageID)
```


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/image/manifest.go:331`



---


[function] name: GetE2EImage file: test/utils/image/manifest.go:336 returns_error: нет description: GetE2EImage returns the fully qualified URI to an image (including version)


### GetE2EImage (test/utils/image/manifest.go:336)


GetE2EImage returns the fully qualified URI to an image (including version)


```go
func (i *Config) GetE2EImage(()) ()
```


📍 *Расположение:* `test/utils/image/manifest.go:336`



---


[function] name: GetImageConfigs file: test/utils/image/manifest.go:321 returns_error: нет description: GetImageConfigs returns the map of imageConfigs


### GetImageConfigs (test/utils/image/manifest.go:321)


GetImageConfigs returns the map of imageConfigs


```go
func GetImageConfigs(()) ()
```


📍 *Расположение:* `test/utils/image/manifest.go:321`



---


[function] name: GetMappedImageConfigs file: test/utils/image/manifest.go:256 returns_error: нет description: GetMappedImageConfigs returns the images if they were mapped to the provided
image repository.


### GetMappedImageConfigs (test/utils/image/manifest.go:256)


GetMappedImageConfigs returns the images if they were mapped to the provided
image repository.


```go
func GetMappedImageConfigs((originalImageConfigs map[ImageID]Config, repo string)) (originalImageConfigs map[ImageID]Config, repo string)
```


**Тип ответа:** originalImageConfigs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/image/manifest.go:256`



---


[function] name: GetOriginalImageConfigs file: test/utils/image/manifest.go:316 returns_error: нет description: GetOriginalImageConfigs returns the configuration before any mapping rules.


### GetOriginalImageConfigs (test/utils/image/manifest.go:316)


GetOriginalImageConfigs returns the configuration before any mapping rules.


```go
func GetOriginalImageConfigs(()) ()
```


📍 *Расположение:* `test/utils/image/manifest.go:316`



---


[function] name: GetPauseImageName file: test/utils/image/manifest.go:341 returns_error: нет description: GetPauseImageName returns the pause image name with proper version


### GetPauseImageName (test/utils/image/manifest.go:341)


GetPauseImageName returns the pause image name with proper version


```go
func GetPauseImageName(()) ()
```


📍 *Расположение:* `test/utils/image/manifest.go:341`



---


[function] name: Init file: test/utils/image/manifest.go:69 returns_error: нет description: —


### Init (test/utils/image/manifest.go:69)


Init is a function that performs operations based on the provided parameters and returns (repoList string).


```go
func Init((repoList string)) (repoList string)
```


**Тип ответа:** repoList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/image/manifest.go:69`



---


[function] name: ReplaceRegistryInImageURL file: test/utils/image/manifest.go:347 returns_error: да description: ReplaceRegistryInImageURL replaces the registry in the image URL with a custom one based
on the configured registries.


### ReplaceRegistryInImageURL (test/utils/image/manifest.go:347)


ReplaceRegistryInImageURL replaces the registry in the image URL with a custom one based
on the configured registries.


```go
func ReplaceRegistryInImageURL((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/image/manifest.go:347`



---


[function] name: SetName file: test/utils/image/manifest.go:60 returns_error: нет description: SetName sets an image name in a Config struct


### SetName (test/utils/image/manifest.go:60)


SetName sets an image name in a Config struct


```go
func (i *Config) SetName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/utils/image/manifest.go:60`



---


[function] name: SetRegistry file: test/utils/image/manifest.go:55 returns_error: нет description: SetRegistry sets an image registry in a Config struct


### SetRegistry (test/utils/image/manifest.go:55)


SetRegistry sets an image registry in a Config struct


```go
func (i *Config) SetRegistry((registry string)) (registry string)
```


**Тип ответа:** registry


```json
{
  "lock": {},
  "initialized": {},
  "tagValidators": {},
  "tagIndex": [],
  "typeValidators": [],
  "fieldValidators": []
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/registry.go`


📍 *Расположение:* `test/utils/image/manifest.go:55`



---


[function] name: SetVersion file: test/utils/image/manifest.go:65 returns_error: нет description: SetVersion sets an image version in a Config struct


### SetVersion (test/utils/image/manifest.go:65)


SetVersion sets an image version in a Config struct


```go
func (i *Config) SetVersion((version string)) (version string)
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


📍 *Расположение:* `test/utils/image/manifest.go:65`



---


[function] name: getRepositoryMappedConfig file: test/utils/image/manifest.go:285 returns_error: нет description: getRepositoryMappedConfig maps an existing image to the provided repo, generating a
tag that is unique with the input co


### getRepositoryMappedConfig (test/utils/image/manifest.go:285)


getRepositoryMappedConfig maps an existing image to the provided repo, generating a
tag that is unique with the input config. The tag will contain the imageID, a hash of
the image spec (to be unique) and shorten and make the pull spec "safe" so it will
fit in the tag to allow a human to recognize the value. If imageID is None, then no
imageID will be added to the tag.


```go
func getRepositoryMappedConfig((imageID ImageID, config Config, repo string)) (imageID ImageID, config Config, repo string)
```


**Тип ответа:** imageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/image/manifest.go:285`



---


[function] name: initImageConfigs file: test/utils/image/manifest.go:209 returns_error: нет description: —


### initImageConfigs (test/utils/image/manifest.go:209)


initImageConfigs is a function that performs operations based on the provided parameters and returns (map[ImageID]Config, map[ImageID]Config).


```go
func initImageConfigs((map[ImageID]Config, map[ImageID]Config)) (map[ImageID]Config, map[ImageID]Config)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/utils/image/manifest.go:209`



---


[function] name: readFromURL file: test/utils/image/manifest.go:109 returns_error: нет description: Essentially curl url | writer


### readFromURL (test/utils/image/manifest.go:109)


Essentially curl url | writer


```go
func readFromURL((url string, writer io.Writer)) (url string, writer io.Writer)
```


**Тип ответа:** url


```json
{
  "baseURL": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


**Тип ответа:** writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


📍 *Расположение:* `test/utils/image/manifest.go:109`



---


[function] name: readRepoList file: test/utils/image/manifest.go:73 returns_error: нет description: —


### readRepoList (test/utils/image/manifest.go:73)


readRepoList is a function that performs operations based on the provided parameters and returns (RegistryList, map[ImageID]Config, map[ImageID]Config).


```go
func readRepoList((RegistryList, map[ImageID]Config, map[ImageID]Config)) (RegistryList, map[ImageID]Config, map[ImageID]Config)
```


**Тип ответа:** RegistryList


```json
{
  "PromoterE2eRegistry": "string",
  "BuildImageRegistry": "string",
  "InvalidRegistry": "string",
  "GcEtcdRegistry": "string",
  "GcRegistry": "string",
  "SigStorageRegistry": "string",
  "PrivateRegistry": "string",
  "DockerLibraryRegistry": "string",
  "CloudProviderGcpRegistry": "string"
}
```


*Определено в:* `test/utils/image/manifest.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ImageID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/utils/image/manifest.go:73`



---


[function] name: replaceRegistryInImageURLWithList file: test/utils/image/manifest.go:353 returns_error: да description: replaceRegistryInImageURLWithList replaces the registry in the image URL with a custom one based
on the given registry l


### replaceRegistryInImageURLWithList (test/utils/image/manifest.go:353)


replaceRegistryInImageURLWithList replaces the registry in the image URL with a custom one based
on the given registry list.


```go
func replaceRegistryInImageURLWithList((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/image/manifest.go:353`




## test/utils/junit/junit.go


📄 Исходный файл: `test/utils/junit/junit.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Update](#update-testutilsjunitjunitgo51) `:51`


</details>


[function] name: Update file: test/utils/junit/junit.go:51 returns_error: нет description: Update iterates through the TestCases and updates Tests, Errors,
Failures, and Skipped top level attributes.


### Update (test/utils/junit/junit.go:51)


Update iterates through the TestCases and updates Tests, Errors,
Failures, and Skipped top level attributes.


```go
func (t *TestSuite) Update(()) ()
```


📍 *Расположение:* `test/utils/junit/junit.go:51`




## test/utils/ktesting/assert.go


📄 Исходный файл: `test/utils/ktesting/assert.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [AssertConsistently](#assertconsistently-testutilsktestingassertgo257) `:257`

- 🔗 [AssertEventually](#asserteventually-testutilsktestingassertgo243) `:243`

- 🔗 [AssertNoError](#assertnoerror-testutilsktestingassertgo114) `:114`

- 🔗 [Backtrace](#backtrace-testutilsktestingassertgo42) `:42`

- 🔗 [Consistently](#consistently-testutilsktestingassertgo250) `:250`

- 🔗 [Error](#error-testutilsktestingassertgo38) `:38`

- 🔗 [Eventually](#eventually-testutilsktestingassertgo236) `:236`

- 🔗 [ExpectNoError](#expectnoerror-testutilsktestingassertgo107) `:107`

- 🔗 [Fatalf](#fatalf-testutilsktestingassertgo78) `:78`

- 🔗 [Is](#is-testutilsktestingassertgo46) `:46`

- 🔗 [buildDescription](#builddescription-testutilsktestingassertgo155) `:155`

- 🔗 [gomegaAssertion](#gomegaassertion-testutilsktestingassertgo61) `:61`

- 🔗 [newAsyncAssertion](#newasyncassertion-testutilsktestingassertgo262) `:262`

- 🔗 [noError](#noerror-testutilsktestingassertgo119) `:119`


</details>


[function] name: AssertConsistently file: test/utils/ktesting/assert.go:257 returns_error: нет description: AssertConsistently is a variant of Consistently which merely records a failure
without stopping the test.


### AssertConsistently (test/utils/ktesting/assert.go:257)


AssertConsistently is a variant of Consistently which merely records a failure
without stopping the test.


```go
func (tCtx TContext) AssertConsistently((arg any)) (arg any)
```


**Тип ответа:** arg


```json
{
  "args": null
}
```


*Определено в:* `cmd/kubeadm/app/cmd/options/argslice.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/assert.go:257`



---


[function] name: AssertEventually file: test/utils/ktesting/assert.go:243 returns_error: нет description: AssertEventually is a variant of Eventually which merely records a failure
without stopping the test.


### AssertEventually (test/utils/ktesting/assert.go:243)


AssertEventually is a variant of Eventually which merely records a failure
without stopping the test.


```go
func (tCtx TContext) AssertEventually((arg any)) (arg any)
```


**Тип ответа:** arg


```json
{
  "args": null
}
```


*Определено в:* `cmd/kubeadm/app/cmd/options/argslice.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/assert.go:243`



---


[function] name: AssertNoError file: test/utils/ktesting/assert.go:114 returns_error: да description: AssertNoError is a variant of ExpectNoError which reports an unexpected
error without aborting the test. It returns true


### AssertNoError (test/utils/ktesting/assert.go:114)


AssertNoError is a variant of ExpectNoError which reports an unexpected
error without aborting the test. It returns true if there was no error.


```go
func (tCtx TContext) AssertNoError((err error, explain ...interface{})) (err error, explain ...interface{})
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


**Тип ответа:** explain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`, `explain ...interface{}`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/ktesting/assert.go:114`



---


[function] name: Backtrace file: test/utils/ktesting/assert.go:42 returns_error: нет description: —


### Backtrace (test/utils/ktesting/assert.go:42)


Backtrace is a method that performs operations based on the provided parameters and returns ().


```go
func (f FailureError) Backtrace(()) ()
```


📍 *Расположение:* `test/utils/ktesting/assert.go:42`



---


[function] name: Consistently file: test/utils/ktesting/assert.go:250 returns_error: нет description: Consistently wraps [gomega.Consistently] the same way as [Eventually] wraps
[gomega.Eventually].


### Consistently (test/utils/ktesting/assert.go:250)


Consistently wraps [gomega.Consistently] the same way as [Eventually] wraps
[gomega.Eventually].


```go
func (tCtx TContext) Consistently((arg any)) (arg any)
```


**Тип ответа:** arg


```json
{
  "args": null
}
```


*Определено в:* `cmd/kubeadm/app/cmd/options/argslice.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/assert.go:250`



---


[function] name: Error file: test/utils/ktesting/assert.go:38 returns_error: нет description: —


### Error (test/utils/ktesting/assert.go:38)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (f FailureError) Error(()) ()
```


📍 *Расположение:* `test/utils/ktesting/assert.go:38`



---


[function] name: Eventually file: test/utils/ktesting/assert.go:236 returns_error: нет description: Eventually wraps [gomega.Eventually]. Supported argument types are:
- A function with a `tCtx ktesting.TContext` or `ctx


### Eventually (test/utils/ktesting/assert.go:236)


Eventually wraps [gomega.Eventually]. Supported argument types are:
- A function with a `tCtx ktesting.TContext` or `ctx context.Context`
parameter plus additional parameters and arbitrary return values.
- A value which changes over time, usually a channel.

For functions, the context is provided by Eventually. Additional parameters
must be passed via WithParameters. The first return value is passed to the Gomega
matcher, all others (in particular an additional error) must be null.
As a special case, a function with `tCtx ktesting.TContext` and no return
values can be combined with gomega.Succeed as matcher.

In contrast to direct usage of [gomega.Eventually], making additional
assertions inside the callback function is okay in all cases as long as they
use the TContext that is passed in. An assertion failure is considered
temporary, so Eventually will continue to poll. This can be used to check a
value with multiple assertions instead of writing a custom matcher:

cb := func(tCtx ktesting.TContext) {
value, err := doSomething(...)
tCtx.ExpectNoError(err, "something failed")
tCtx.Assert(value.a).To(gomega.Equal(42), "the answer")
tCtx.Assert(value.b).To(gomega.Equal("the fish"), "thanks")
}
tCtx.Eventually(cb).Should(gomega.Succeed())

The test stops in case of a failure. To continue, use AssertEventually.

The default Gomega poll interval and timeout are used. Setting a specific
timeout may be useful:

tCtx.Eventually(cb).Timeout(5 * time.Second).Should(gomega.Succeed(), "foobar should succeed")

Canceling the context in the callback only affects code in the callback. The
context passed to Eventually is not getting canceled. To abort polling
immediately because the expected condition is known to not be reached
anymore, use [gomega.StopTrying]:

cb := func(func(tCtx ktesting.TContext) int {
value, err := doSomething(...)
if errors.Is(err, SomeFinalErr) {
// This message completely replaces the normal
// failure message and thus should include all
// relevant information.
//
// github.com/onsi/gomega/format is a good way
// to format arbitrary data. It uses indention
// and falls back to YAML for Kubernetes API
// structs for readability.
gomega.StopTrying("permanent failure, last value:\n%s", format.Object(value, 1 /* indent one level */)).
Wrap(err).Now()
}
tCtx.ExpectNoError(err, "something failed")
return value
}
tCtx.Eventually(cb).Should(gomega.Equal(42), "should be the answer to everything")

To poll again after some specific timeout, use [gomega.TryAgainAfter]. This is
particularly useful in [Consistently] to ignore some intermittent error.

cb := func(func(tCtx ktesting.TContext) int {
value, err := doSomething(...)
var intermittentErr SomeIntermittentError
if errors.As(err, &intermittentErr) {
gomega.TryAgainAfter(intermittentErr.RetryPeriod).Wrap(err).Now()
}
tCtx.ExpectNoError(err, "something failed")
return value
}
tCtx.Eventually(cb).Should(gomega.Equal(42), "should be the answer to everything")


```go
func (tCtx TContext) Eventually((arg any)) (arg any)
```


**Тип ответа:** arg


```json
{
  "args": null
}
```


*Определено в:* `cmd/kubeadm/app/cmd/options/argslice.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/assert.go:236`



---


[function] name: ExpectNoError file: test/utils/ktesting/assert.go:107 returns_error: да description: ExpectNoError asserts that no error has occurred and fails the test if it does.

As in [gomega], the optional explanatio


### ExpectNoError (test/utils/ktesting/assert.go:107)


ExpectNoError asserts that no error has occurred and fails the test if it does.

As in [gomega], the optional explanation can be:
- a [fmt.Sprintf] format string plus its arguments
- a function returning a string, which will be called
lazily to construct the explanation if needed

If an explanation is provided, then it replaces the default "Unexpected
error" in the failure message. It's combined with additional details by
adding a colon at the end, as when wrapping an error. Therefore it should
not end with a punctuation mark or line break.

Using ExpectNoError instead of the corresponding Gomega or testify
assertions has the advantage that the failure message is short (good for
aggregation in https://go.k8s.io/triage) with more details captured in the
test log output (good when investigating one particular failure).

Helper packages should return errors that are derived from [FailureError].
The test code then is forced to check for that error by the normal
linter and should provide additional context for the failure, just
as it would when printing or wrapping an error:

tCtx.ExpectNoError(somehelper.CreateSomething(tCtx, ...), "creating the first foobar")
tCtx.ExpectNoError(somehelper.CreateSomething(tCtx, ...), "creating the second foobar")


```go
func (tCtx TContext) ExpectNoError((err error, explain ...interface{})) (err error, explain ...interface{})
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


**Тип ответа:** explain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`, `explain ...interface{}`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/ktesting/assert.go:107`



---


[function] name: Fatalf file: test/utils/ktesting/assert.go:78 returns_error: нет description: —


### Fatalf (test/utils/ktesting/assert.go:78)


Fatalf is a method that performs operations based on the provided parameters and returns (format string, args ...any).


```go
func (a assertTestingT) Fatalf((format string, args ...any)) (format string, args ...any)
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


📍 *Расположение:* `test/utils/ktesting/assert.go:78`



---


[function] name: Is file: test/utils/ktesting/assert.go:46 returns_error: да description: —


### Is (test/utils/ktesting/assert.go:46)


Is is a method that performs operations based on the provided parameters and may return an error.


```go
func (f FailureError) Is((target error)) (target error)
```


**Тип ответа:** target


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `target error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `test/utils/ktesting/assert.go:46`



---


[function] name: buildDescription file: test/utils/ktesting/assert.go:155 returns_error: нет description: —


### buildDescription (test/utils/ktesting/assert.go:155)


buildDescription is a function that performs operations based on the provided parameters and returns (explain ...interface{}).


```go
func buildDescription((explain ...interface{})) (explain ...interface{})
```


**Тип ответа:** explain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/utils/ktesting/assert.go:155`



---


[function] name: gomegaAssertion file: test/utils/ktesting/assert.go:61 returns_error: нет description: —


### gomegaAssertion (test/utils/ktesting/assert.go:61)


gomegaAssertion is a function that performs operations based on the provided parameters and returns (tCtx TContext, fatal bool, actual interface{}, extra ...interface{}).


```go
func gomegaAssertion((tCtx TContext, fatal bool, actual interface{}, extra ...interface{})) (tCtx TContext, fatal bool, actual interface{}, extra ...interface{})
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TContext


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


**Тип ответа:** fatal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** actual


```json
{
  "socketFileToInfo": {}
}
```


*Определено в:* `pkg/kubelet/pluginmanager/cache/actual_state_of_world.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** extra


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/unstructured.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/utils/ktesting/assert.go:61`



---


[function] name: newAsyncAssertion file: test/utils/ktesting/assert.go:262 returns_error: нет description: —


### newAsyncAssertion (test/utils/ktesting/assert.go:262)


newAsyncAssertion is a method that performs operations based on the provided parameters and returns (eventuallyOrConsistently func(actualOrCtx any, args ...any) gomega.AsyncAssertion, arg any).


```go
func (tCtx TContext) newAsyncAssertion((eventuallyOrConsistently func(actualOrCtx any, args ...any) gomega.AsyncAssertion, arg any)) (eventuallyOrConsistently func(actualOrCtx any, args ...any) gomega.AsyncAssertion, arg any)
```


**Тип ответа:** eventuallyOrConsistently


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** actualOrCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gomega.AsyncAssertion


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** arg


```json
{
  "args": null
}
```


*Определено в:* `cmd/kubeadm/app/cmd/options/argslice.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/assert.go:262`



---


[function] name: noError file: test/utils/ktesting/assert.go:119 returns_error: да description: —


### noError (test/utils/ktesting/assert.go:119)


noError is a method that performs operations based on the provided parameters and may return an error.


```go
func (tCtx TContext) noError((failf func(format string, args ...any), err error, explain ...interface{})) (failf func(format string, args ...any), err error, explain ...interface{})
```


**Тип ответа:** failf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** err


```json
{
  "msg": {},
  "cause": {},
  "stack": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/errors/errors.go`


**Тип ответа:** explain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `failf func(format string`, `args ...any)`, `err error`, `explain ...interface{}`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/ktesting/assert.go:119`




## test/utils/ktesting/clientcontext.go


📄 Исходный файл: `test/utils/ktesting/clientcontext.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [WithClients](#withclients-testutilsktestingclientcontextgo46) `:46`

- 🔗 [WithRESTConfig](#withrestconfig-testutilsktestingclientcontextgo32) `:32`


</details>


[function] name: WithClients file: test/utils/ktesting/clientcontext.go:46 returns_error: нет description: WithClients uses an existing config and clients.


### WithClients (test/utils/ktesting/clientcontext.go:46)


WithClients uses an existing config and clients.


```go
func (tCtx TContext) WithClients((cfg *rest.Config, mapper *restmapper.DeferredDiscoveryRESTMapper, client clientset.Interface, dynamic dynamic.Interface, apiextensions apiextensions.Interface)) (cfg *rest.Config, mapper *restmapper.DeferredDiscoveryRESTMapper, client clientset.Interface, dynamic dynamic.Interface, apiextensions apiextensions.Interface)
```


**Тип запроса:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип запроса:** restmapper.DeferredDiscoveryRESTMapper


```json
{
  "initMu": {},
  "delegate": {},
  "cl": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/restmapper/discovery.go`


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** mapper


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** restmapper.DeferredDiscoveryRESTMapper


```json
{
  "initMu": {},
  "delegate": {},
  "cl": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/restmapper/discovery.go`


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


**Тип ответа:** dynamic


```json
{
  "client": null,
  "namespace": "string",
  "resource": {},
  "listKind": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/fake/simple.go`


**Тип ответа:** dynamic.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** apiextensions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiextensions.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `test/utils/ktesting/clientcontext.go:46`



---


[function] name: WithRESTConfig file: test/utils/ktesting/clientcontext.go:32 returns_error: нет description: WithRESTConfig initializes all client-go clients with new clients
created for the config. The current test name gets inc


### WithRESTConfig (test/utils/ktesting/clientcontext.go:32)


WithRESTConfig initializes all client-go clients with new clients
created for the config. The current test name gets included in the UserAgent.


```go
func (tCtx TContext) WithRESTConfig((cfg *rest.Config)) (cfg *rest.Config)
```


**Тип запроса:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/utils/ktesting/clientcontext.go:32`




## test/utils/ktesting/contexthelper.go


📄 Исходный файл: `test/utils/ktesting/contexthelper.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Deadline](#deadline-testutilsktestingcontexthelpergo103) `:103`

- 🔗 [Error](#error-testutilsktestingcontexthelpergo33) `:33`

- 🔗 [Is](#is-testutilsktestingcontexthelpergo35) `:35`

- 🔗 [cleanupErr](#cleanuperr-testutilsktestingcontexthelpergo27) `:27`

- 🔗 [withTimeout](#withtimeout-testutilsktestingcontexthelpergo43) `:43`


</details>


[function] name: Deadline file: test/utils/ktesting/contexthelper.go:103 returns_error: нет description: —


### Deadline (test/utils/ktesting/contexthelper.go:103)


Deadline is a method that performs operations based on the provided parameters and returns (time.Time, bool).


```go
func (d deadlineContext) Deadline((time.Time, bool)) (time.Time, bool)
```


**Тип ответа:** time.Time


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


📍 *Расположение:* `test/utils/ktesting/contexthelper.go:103`



---


[function] name: Error file: test/utils/ktesting/contexthelper.go:33 returns_error: нет description: —


### Error (test/utils/ktesting/contexthelper.go:33)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (c canceledError) Error(()) ()
```


📍 *Расположение:* `test/utils/ktesting/contexthelper.go:33`



---


[function] name: Is file: test/utils/ktesting/contexthelper.go:35 returns_error: да description: —


### Is (test/utils/ktesting/contexthelper.go:35)


Is is a method that performs operations based on the provided parameters and may return an error.


```go
func (c canceledError) Is((target error)) (target error)
```


**Тип ответа:** target


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `target error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `test/utils/ktesting/contexthelper.go:35`



---


[function] name: cleanupErr file: test/utils/ktesting/contexthelper.go:27 returns_error: нет description: cleanupErr creates a cause when canceling a context because the test has completed.
It is a context.Canceled error.


### cleanupErr (test/utils/ktesting/contexthelper.go:27)


cleanupErr creates a cause when canceling a context because the test has completed.
It is a context.Canceled error.


```go
func cleanupErr((testName string)) (testName string)
```


**Тип ответа:** testName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/contexthelper.go:27`



---


[function] name: withTimeout file: test/utils/ktesting/contexthelper.go:43 returns_error: нет description: withTimeout corresponds to [context.WithTimeout]. In contrast to
[context.WithTimeout], it automatically cancels during 


### withTimeout (test/utils/ktesting/contexthelper.go:43)


withTimeout corresponds to [context.WithTimeout]. In contrast to
[context.WithTimeout], it automatically cancels during test cleanup, provides
the given cause when the deadline is reached, and its cancel function
requires a cause.


```go
func withTimeout((context.Context, func(cause string))) (context.Context, func(cause string))
```


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


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cause


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/contexthelper.go:43`




## test/utils/ktesting/errorcontext.go


📄 Исходный файл: `test/utils/ktesting/errorcontext.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [Error](#error-testutilsktestingerrorcontextgo134) `:134`

- 🔗 [Errorf](#errorf-testutilsktestingerrorcontextgo156) `:156`

- 🔗 [Fail](#fail-testutilsktestingerrorcontextgo174) `:174`

- 🔗 [FailNow](#failnow-testutilsktestingerrorcontextgo186) `:186`

- 🔗 [Failed](#failed-testutilsktestingerrorcontextgo199) `:199`

- 🔗 [Fatal](#fatal-testutilsktestingerrorcontextgo210) `:210`

- 🔗 [Fatalf](#fatalf-testutilsktestingerrorcontextgo223) `:223`

- 🔗 [GomegaString](#gomegastring-testutilsktestingerrorcontextgo78) `:78`

- 🔗 [Log](#log-testutilsktestingerrorcontextgo120) `:120`

- 🔗 [Logf](#logf-testutilsktestingerrorcontextgo127) `:127`

- 🔗 [Skip](#skip-testutilsktestingerrorcontextgo106) `:106`

- 🔗 [Skipf](#skipf-testutilsktestingerrorcontextgo113) `:113`

- 🔗 [WithError](#witherror-testutilsktestingerrorcontextgo42) `:42`

- 🔗 [buildHeader](#buildheader-testutilsktestingerrorcontextgo87) `:87`

- 🔗 [finalize](#finalize-testutilsktestingerrorcontextgo60) `:60`

- 🔗 [indent](#indent-testutilsktestingerrorcontextgo98) `:98`


</details>


[function] name: Error file: test/utils/ktesting/errorcontext.go:134 returns_error: нет description: —


### Error (test/utils/ktesting/errorcontext.go:134)


Error is a method that performs operations based on the provided parameters and returns (args ...any).


```go
func (tCtx TContext) Error((args ...any)) (args ...any)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:134`



---


[function] name: Errorf file: test/utils/ktesting/errorcontext.go:156 returns_error: нет description: —


### Errorf (test/utils/ktesting/errorcontext.go:156)


Errorf is a method that performs operations based on the provided parameters and returns (format string, args ...any).


```go
func (tCtx TContext) Errorf((format string, args ...any)) (format string, args ...any)
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


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:156`



---


[function] name: Fail file: test/utils/ktesting/errorcontext.go:174 returns_error: нет description: —


### Fail (test/utils/ktesting/errorcontext.go:174)


Fail is a method that performs operations based on the provided parameters and returns ().


```go
func (tCtx TContext) Fail(()) ()
```


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:174`



---


[function] name: FailNow file: test/utils/ktesting/errorcontext.go:186 returns_error: нет description: —


### FailNow (test/utils/ktesting/errorcontext.go:186)


FailNow is a method that performs operations based on the provided parameters and returns ().


```go
func (tCtx TContext) FailNow(()) ()
```


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:186`



---


[function] name: Failed file: test/utils/ktesting/errorcontext.go:199 returns_error: нет description: —


### Failed (test/utils/ktesting/errorcontext.go:199)


Failed is a method that performs operations based on the provided parameters and returns ().


```go
func (tCtx TContext) Failed(()) ()
```


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:199`



---


[function] name: Fatal file: test/utils/ktesting/errorcontext.go:210 returns_error: нет description: —


### Fatal (test/utils/ktesting/errorcontext.go:210)


Fatal is a method that performs operations based on the provided parameters and returns (args ...any).


```go
func (tCtx TContext) Fatal((args ...any)) (args ...any)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:210`



---


[function] name: Fatalf file: test/utils/ktesting/errorcontext.go:223 returns_error: нет description: —


### Fatalf (test/utils/ktesting/errorcontext.go:223)


Fatalf is a method that performs operations based on the provided parameters and returns (format string, args ...any).


```go
func (tCtx TContext) Fatalf((format string, args ...any)) (format string, args ...any)
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


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:223`



---


[function] name: GomegaString file: test/utils/ktesting/errorcontext.go:78 returns_error: нет description: —


### GomegaString (test/utils/ktesting/errorcontext.go:78)


GomegaString is a method that performs operations based on the provided parameters and returns ().


```go
func (e failures) GomegaString(()) ()
```


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:78`



---


[function] name: Log file: test/utils/ktesting/errorcontext.go:120 returns_error: нет description: —


### Log (test/utils/ktesting/errorcontext.go:120)


Log is a method that performs operations based on the provided parameters and returns (args ...any).


```go
func (tCtx TContext) Log((args ...any)) (args ...any)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:120`



---


[function] name: Logf file: test/utils/ktesting/errorcontext.go:127 returns_error: нет description: —


### Logf (test/utils/ktesting/errorcontext.go:127)


Logf is a method that performs operations based on the provided parameters and returns (format string, args ...any).


```go
func (tCtx TContext) Logf((format string, args ...any)) (format string, args ...any)
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


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:127`



---


[function] name: Skip file: test/utils/ktesting/errorcontext.go:106 returns_error: нет description: —


### Skip (test/utils/ktesting/errorcontext.go:106)


Skip is a method that performs operations based on the provided parameters and returns (args ...any).


```go
func (tCtx TContext) Skip((args ...any)) (args ...any)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:106`



---


[function] name: Skipf file: test/utils/ktesting/errorcontext.go:113 returns_error: нет description: —


### Skipf (test/utils/ktesting/errorcontext.go:113)


Skipf is a method that performs operations based on the provided parameters and returns (format string, args ...any).


```go
func (tCtx TContext) Skipf((format string, args ...any)) (format string, args ...any)
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


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:113`



---


[function] name: WithError file: test/utils/ktesting/errorcontext.go:42 returns_error: нет description: WithError creates a context where test failures are collected and stored in
the provided error instance when the caller 


### WithError (test/utils/ktesting/errorcontext.go:42)


WithError creates a context where test failures are collected and stored in
the provided error instance when the caller is done. Use it like this:

func doSomething(tCtx ktesting.TContext) (finalErr error) {
tCtx, finalize := WithError(tCtx, &finalErr)
defer finalize()
...
tCtx.Fatal("some failure")

Any error already stored in the variable will get overwritten by finalize if
there were test failures, otherwise the variable is left unchanged.
If there were multiple test errors, then the error will wrap all of
them with errors.Join.

Test failures are not propagated to the parent context.
WithRESTConfig initializes all client-go clients with new clients
created for the config. The current test name gets included in the UserAgent.


```go
func (tCtx TContext) WithError((TContext, func())) (TContext, func())
```


**Тип ответа:** TContext


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


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:42`



---


[function] name: buildHeader file: test/utils/ktesting/errorcontext.go:87 returns_error: нет description: buildHeader handles:
- "ERROR:<non-empty prefix><optional header><suffix>" -> use both prefix and suffix when we have a 


### buildHeader (test/utils/ktesting/errorcontext.go:87)


buildHeader handles:
- "ERROR:<non-empty prefix><optional header><suffix>" -> use both prefix and suffix when we have a header, otherwise just the suffix
- "<empty prefix><optional header><suffix>" -> use suffix only if we have a header


```go
func (tCtx TContext) buildHeader((prefix, suffix string)) (prefix, suffix string)
```


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


**Тип ответа:** suffix


```json
{
  "decSuffixes": {},
  "binSuffixes": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/resource/suffix.go`


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:87`



---


[function] name: finalize file: test/utils/ktesting/errorcontext.go:60 returns_error: да description: —


### finalize (test/utils/ktesting/errorcontext.go:60)


finalize is a method that performs operations based on the provided parameters and may return an error.


```go
func (tCtx TContext) finalize((err *error)) (err *error)
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


*Типы возврата:* `err *error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:60`



---


[function] name: indent file: test/utils/ktesting/errorcontext.go:98 returns_error: нет description: indent either indents all follow-up lines or all lines including the first one.


### indent (test/utils/ktesting/errorcontext.go:98)


indent either indents all follow-up lines or all lines including the first one.


```go
func indent((msg string, all bool)) (msg string, all bool)
```


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** all


```json
{
  "ports": []
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/utils/ktesting/errorcontext.go:98`




## test/utils/ktesting/initoption/initoption.go


📄 Исходный файл: `test/utils/ktesting/initoption/initoption.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [BufferLogs](#bufferlogs-testutilsktestinginitoptioninitoptiongo36) `:36`

- 🔗 [PerTestOutput](#pertestoutput-testutilsktestinginitoptioninitoptiongo26) `:26`


</details>


[function] name: BufferLogs file: test/utils/ktesting/initoption/initoption.go:36 returns_error: нет description: BufferLogs controls whether log entries are captured in memory in addition
to being printed. Off by default. Unit tests 


### BufferLogs (test/utils/ktesting/initoption/initoption.go:36)


BufferLogs controls whether log entries are captured in memory in addition
to being printed. Off by default. Unit tests that want to verify that
log entries are emitted as expected can turn this on and then retrieve
the captured log through the Underlier LogSink interface.


```go
func BufferLogs((enabled bool)) (enabled bool)
```


**Тип ответа:** enabled


```json
{
  "value": "string",
  "register": false
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/generators/deepcopy.go`


📍 *Расположение:* `test/utils/ktesting/initoption/initoption.go:36`



---


[function] name: PerTestOutput file: test/utils/ktesting/initoption/initoption.go:26 returns_error: нет description: PerTestOutput controls whether a per-test logger gets
set up by Init. Has no effect in InitCtx.


### PerTestOutput (test/utils/ktesting/initoption/initoption.go:26)


PerTestOutput controls whether a per-test logger gets
set up by Init. Has no effect in InitCtx.


```go
func PerTestOutput((enabled bool)) (enabled bool)
```


**Тип ответа:** enabled


```json
{
  "value": "string",
  "register": false
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/generators/deepcopy.go`


📍 *Расположение:* `test/utils/ktesting/initoption/initoption.go:26`




## test/utils/ktesting/klogcontext.go


📄 Исходный файл: `test/utils/ktesting/klogcontext.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [klogHeader](#klogheader-testutilsktestingklogcontextgo26) `:26`


</details>


[function] name: klogHeader file: test/utils/ktesting/klogcontext.go:26 returns_error: нет description: —


### klogHeader (test/utils/ktesting/klogcontext.go:26)


klogHeader is a function that performs operations based on the provided parameters and returns ().


```go
func klogHeader(()) ()
```


📍 *Расположение:* `test/utils/ktesting/klogcontext.go:26`




## test/utils/ktesting/ktesting.go


📄 Исходный файл: `test/utils/ktesting/ktesting.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [NewTestContext](#newtestcontext-testutilsktestingktestinggo52) `:52`

- 🔗 [SetDefaultVerbosity](#setdefaultverbosity-testutilsktestingktestinggo42) `:42`


</details>


[function] name: NewTestContext file: test/utils/ktesting/ktesting.go:52 returns_error: нет description: NewTestContext is a drop-in replacement for ktesting.NewTestContext.

The result can be cast to a TContext and has the s


### NewTestContext (test/utils/ktesting/ktesting.go:52)


NewTestContext is a drop-in replacement for ktesting.NewTestContext.

The result can be cast to a TContext and has the same functionality
(for example, it gets cancelled at the end of the test).
It's returned as a context.Context to avoid breaking code which expects that type.


```go
func NewTestContext((klog.Logger, context.Context)) (klog.Logger, context.Context)
```


**Тип ответа:** klog.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


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


📍 *Расположение:* `test/utils/ktesting/ktesting.go:52`



---


[function] name: SetDefaultVerbosity file: test/utils/ktesting/ktesting.go:42 returns_error: нет description: SetDefaultVerbosity can be called during init to modify the default
log verbosity of the program.

Note that this immedi


### SetDefaultVerbosity (test/utils/ktesting/ktesting.go:42)


SetDefaultVerbosity can be called during init to modify the default
log verbosity of the program.

Note that this immediately reconfigures the klog verbosity, already before
flag parsing. If the verbosity is non-zero and SetDefaultVerbosity is called
during init, then other init functions might start logging where normally
they wouldn't log anything. Should this occur, then the right fix is to
remove those log calls because logging during init is discouraged. It leads
to unpredictable output (init order is not specified) and/or is useless
(logging not initialized during init and thus conditional log output gets
omitted).


```go
func SetDefaultVerbosity((v int)) (v int)
```


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


📍 *Расположение:* `test/utils/ktesting/ktesting.go:42`




## test/utils/ktesting/signals.go


📄 Исходный файл: `test/utils/ktesting/signals.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [AttachProgressReporter](#attachprogressreporter-testutilsktestingsignalsgo177) `:177`

- 🔗 [detachProgressReporter](#detachprogressreporter-testutilsktestingsignalsgo193) `:193`

- 🔗 [dumpProgress](#dumpprogress-testutilsktestingsignalsgo217) `:217`

- 🔗 [finalize](#finalize-testutilsktestingsignalsgo153) `:153`

- 🔗 [init](#init-testutilsktestingsignalsgo80) `:80`

- 🔗 [run](#run-testutilsktestingsignalsgo200) `:200`


</details>


[function] name: AttachProgressReporter file: test/utils/ktesting/signals.go:177 returns_error: нет description: AttachProgressReporter implements Gomega's contextWithAttachProgressReporter.


### AttachProgressReporter (test/utils/ktesting/signals.go:177)


AttachProgressReporter implements Gomega's contextWithAttachProgressReporter.


```go
func (p *progressReporter) AttachProgressReporter((reporter func() string)) (reporter func() string)
```


**Тип ответа:** reporter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/signals.go:177`



---


[function] name: detachProgressReporter file: test/utils/ktesting/signals.go:193 returns_error: нет description: —


### detachProgressReporter (test/utils/ktesting/signals.go:193)


detachProgressReporter is a method that performs operations based on the provided parameters and returns (id int64).


```go
func (p *progressReporter) detachProgressReporter((id int64)) (id int64)
```


**Тип ответа:** id


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/coordination/v1beta1/leasecandidate.go`


📍 *Расположение:* `test/utils/ktesting/signals.go:193`



---


[function] name: dumpProgress file: test/utils/ktesting/signals.go:217 returns_error: нет description: dumpProgress is less useful than the Ginkgo progress report. We can't fix
that we don't know which tests are currently r


### dumpProgress (test/utils/ktesting/signals.go:217)


dumpProgress is less useful than the Ginkgo progress report. We can't fix
that we don't know which tests are currently running and instead have to
rely on "go test -v" for that.

But perhaps dumping goroutines and their callstacks is useful anyway?  TODO:
look at how Ginkgo does it and replicate some of it.


```go
func (p *progressReporter) dumpProgress(()) ()
```


📍 *Расположение:* `test/utils/ktesting/signals.go:217`



---


[function] name: finalize file: test/utils/ktesting/signals.go:153 returns_error: нет description: —


### finalize (test/utils/ktesting/signals.go:153)


finalize is a method that performs operations based on the provided parameters and returns ().


```go
func (p *progressReporter) finalize(()) ()
```


📍 *Расположение:* `test/utils/ktesting/signals.go:153`



---


[function] name: init file: test/utils/ktesting/signals.go:80 returns_error: нет description: init is invoked by Init. It returns the context to be used for the
new TContext.

By default, that is just context.Backg


### init (test/utils/ktesting/signals.go:80)


init is invoked by Init. It returns the context to be used for the
new TContext.

By default, that is just context.Background. In a Go unit test, it
is a context connected to os.Interrupt.

Once activated like that in a Go unit test, the progressReporter implements
support for triggering a progress report in a running test when sending it a
USR1 signal, similar to the corresponding Ginkgo feature.

This support is active until the last test terminates.


```go
func (p *progressReporter) init((tb TB)) (tb TB)
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


**Тип ответа:** TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/signals.go:80`



---


[function] name: run file: test/utils/ktesting/signals.go:200 returns_error: нет description: —


### run (test/utils/ktesting/signals.go:200)


run is a method that performs operations based on the provided parameters and returns ().


```go
func (p *progressReporter) run(()) ()
```


📍 *Расположение:* `test/utils/ktesting/signals.go:200`




## test/utils/ktesting/stepcontext.go


📄 Исходный файл: `test/utils/ktesting/stepcontext.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [AttachProgressReporter](#attachprogressreporter-testutilsktestingstepcontextgo72) `:72`

- 🔗 [Step](#step-testutilsktestingstepcontextgo47) `:47`

- 🔗 [Value](#value-testutilsktestingstepcontextgo54) `:54`

- 🔗 [WithStep](#withstep-testutilsktestingstepcontextgo29) `:29`


</details>


[function] name: AttachProgressReporter file: test/utils/ktesting/stepcontext.go:72 returns_error: нет description: —


### AttachProgressReporter (test/utils/ktesting/stepcontext.go:72)


AttachProgressReporter is a method that performs operations based on the provided parameters and returns (reporter func() string).


```go
func (s *stepReporter) AttachProgressReporter((reporter func() string)) (reporter func() string)
```


**Тип ответа:** reporter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/stepcontext.go:72`



---


[function] name: Step file: test/utils/ktesting/stepcontext.go:47 returns_error: нет description: Step is useful when the context with the step information is
used more than once:

ktesting.Step(tCtx, "step 1", func(tC


### Step (test/utils/ktesting/stepcontext.go:47)


Step is useful when the context with the step information is
used more than once:

ktesting.Step(tCtx, "step 1", func(tCtx ktesting.TContext) {
tCtx.Log(...)
if (... ) {
tCtx.Failf(...)
}
)}

Inside the callback, the tCtx variable is the one where the step
has been added. This avoids the need to introduce multiple different
context variables and risk of using the wrong one.


```go
func (tCtx TContext) Step((step string, cb func(tCtx TContext))) (step string, cb func(tCtx TContext))
```


**Тип ответа:** step


```json
{
  "reporter": {},
  "steps": "string"
}
```


*Определено в:* `test/utils/ktesting/stepcontext.go`


**Тип ответа:** cb


```json
{
  "block": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/aes/aes.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TContext


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


📍 *Расположение:* `test/utils/ktesting/stepcontext.go:47`



---


[function] name: Value file: test/utils/ktesting/stepcontext.go:54 returns_error: нет description: Value intercepts a search for the special "GINKGO_SPEC_CONTEXT" and
wraps the underlying reporter so that the steps are 


### Value (test/utils/ktesting/stepcontext.go:54)


Value intercepts a search for the special "GINKGO_SPEC_CONTEXT" and
wraps the underlying reporter so that the steps are visible in the report.


```go
func (tCtx TContext) Value((key any)) (key any)
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


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/stepcontext.go:54`



---


[function] name: WithStep file: test/utils/ktesting/stepcontext.go:29 returns_error: нет description: WithStep creates a context where a prefix is added to all errors and log
messages, similar to how errors are wrapped. Th


### WithStep (test/utils/ktesting/stepcontext.go:29)


WithStep creates a context where a prefix is added to all errors and log
messages, similar to how errors are wrapped. This can be nested, leaving a
trail of "bread crumbs" that help figure out where in a test some problem
occurred or why some log output gets written:

ERROR: bake cake: set heat for baking: oven not found

The string should describe the operation that is about to happen ("starting
the controller", "list items") or what is being operated on ("HTTP server").
Multiple different prefixes get concatenated with a colon.


```go
func (tCtx TContext) WithStep((step string)) (step string)
```


**Тип ответа:** step


```json
{
  "reporter": {},
  "steps": "string"
}
```


*Определено в:* `test/utils/ktesting/stepcontext.go`


📍 *Расположение:* `test/utils/ktesting/stepcontext.go:29`




## test/utils/ktesting/tcontext.go


📄 Исходный файл: `test/utils/ktesting/tcontext.go`


<details open>
<summary><b>Функции в этом файле (26)</b></summary>


- 🔗 [APIExtensions](#apiextensions-testutilsktestingtcontextgo555) `:555`

- 🔗 [Assert](#assert-testutilsktestingtcontextgo577) `:577`

- 🔗 [Cancel](#cancel-testutilsktestingtcontextgo428) `:428`

- 🔗 [CleanupCtx](#cleanupctx-testutilsktestingtcontextgo450) `:450`

- 🔗 [Client](#client-testutilsktestingtcontextgo553) `:553`

- 🔗 [Dynamic](#dynamic-testutilsktestingtcontextgo554) `:554`

- 🔗 [Expect](#expect-testutilsktestingtcontextgo565) `:565`

- 🔗 [Init](#init-testutilsktestingtcontextgo122) `:122`

- 🔗 [InitCtx](#initctx-testutilsktestingtcontextgo218) `:218`

- 🔗 [IsSyncTest](#issynctest-testutilsktestingtcontextgo499) `:499`

- 🔗 [Logger](#logger-testutilsktestingtcontextgo540) `:540`

- 🔗 [Namespace](#namespace-testutilsktestingtcontextgo593) `:593`

- 🔗 [Parallel](#parallel-testutilsktestingtcontextgo413) `:413`

- 🔗 [RESTConfig](#restconfig-testutilsktestingtcontextgo548) `:548`

- 🔗 [RESTMapper](#restmapper-testutilsktestingtcontextgo552) `:552`

- 🔗 [Require](#require-testutilsktestingtcontextgo570) `:570`

- 🔗 [Run](#run-testutilsktestingtcontextgo477) `:477`

- 🔗 [SyncTest](#synctest-testutilsktestingtcontextgo486) `:486`

- 🔗 [TB](#tb-testutilsktestingtcontextgo528) `:528`

- 🔗 [Wait](#wait-testutilsktestingtcontextgo508) `:508`

- 🔗 [WithContext](#withcontext-testutilsktestingtcontextgo305) `:305`

- 🔗 [WithNamespace](#withnamespace-testutilsktestingtcontextgo582) `:582`

- 🔗 [WithValue](#withvalue-testutilsktestingtcontextgo316) `:316`

- 🔗 [newLogger](#newlogger-testutilsktestingtcontextgo171) `:171`

- 🔗 [run](#run-testutilsktestingtcontextgo253) `:253`

- 🔗 [withTB](#withtb-testutilsktestingtcontextgo241) `:241`


</details>


[function] name: APIExtensions file: test/utils/ktesting/tcontext.go:555 returns_error: нет description: —


### APIExtensions (test/utils/ktesting/tcontext.go:555)


APIExtensions is a method that performs operations based on the provided parameters and returns ().


```go
func (tCtx TContext) APIExtensions(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:555`



---


[function] name: Assert file: test/utils/ktesting/tcontext.go:577 returns_error: нет description: Assert also wraps [gomega.Expect], but in contrast to Expect = Require,
it reports a failure through [TContext.Error]. T


### Assert (test/utils/ktesting/tcontext.go:577)


Assert also wraps [gomega.Expect], but in contrast to Expect = Require,
it reports a failure through [TContext.Error]. This makes it possible
to test several different assertions.


```go
func (tCtx TContext) Assert((actual interface{}, extra ...interface{})) (actual interface{}, extra ...interface{})
```


**Тип ответа:** actual


```json
{
  "socketFileToInfo": {}
}
```


*Определено в:* `pkg/kubelet/pluginmanager/cache/actual_state_of_world.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** extra


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/unstructured.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/utils/ktesting/tcontext.go:577`



---


[function] name: Cancel file: test/utils/ktesting/tcontext.go:428 returns_error: нет description: Cancel can be invoked to cancel the context before the test is completed.
Tests which use the context to control gorouti


### Cancel (test/utils/ktesting/tcontext.go:428)


Cancel can be invoked to cancel the context before the test is completed.
Tests which use the context to control goroutines and then wait for
termination of those goroutines must call Cancel to avoid a deadlock.

The cause, if non-empty, is turned into an error which is equivalent
to context.Canceled. context.Cause will return that error for the
context.


```go
func (tCtx TContext) Cancel((cause string)) (cause string)
```


**Тип ответа:** cause


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/tcontext.go:428`



---


[function] name: CleanupCtx file: test/utils/ktesting/tcontext.go:450 returns_error: нет description: CleanupCtx registers a callback that will get invoked when the test
has finished. Callbacks get invoked in last-in-first


### CleanupCtx (test/utils/ktesting/tcontext.go:450)


CleanupCtx registers a callback that will get invoked when the test
has finished. Callbacks get invoked in last-in-first-out order (LIFO).

Using CleanupCtx is preferred because of the automatic context cancellation.
The following broken (!) cleanup code will use a canceled context,
which is not desirable:

// tCtx gets canceled when the test ends and before the callback runs.
tCtx.Cleanup(func() { /* do something with the test's tCtx */ })

A safer way to run cleanup code is:

tCtx.CleanupCtx(func (tCtx ktesting.TContext) { /* do something with the cleanup's tCtx */ })

The logger and clients are the same as in the TContext that CleanupCtx
is invoked on.


```go
func (tCtx TContext) CleanupCtx((cb func(TContext))) (cb func(TContext))
```


**Тип ответа:** cb


```json
{
  "block": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/aes/aes.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TContext


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


📍 *Расположение:* `test/utils/ktesting/tcontext.go:450`



---


[function] name: Client file: test/utils/ktesting/tcontext.go:553 returns_error: нет description: —


### Client (test/utils/ktesting/tcontext.go:553)


Client is a method that performs operations based on the provided parameters and returns ().


```go
func (tCtx TContext) Client(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:553`



---


[function] name: Dynamic file: test/utils/ktesting/tcontext.go:554 returns_error: нет description: —


### Dynamic (test/utils/ktesting/tcontext.go:554)


Dynamic is a method that performs operations based on the provided parameters and returns ().


```go
func (tCtx TContext) Dynamic(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:554`



---


[function] name: Expect file: test/utils/ktesting/tcontext.go:565 returns_error: нет description: Expect wraps [gomega.Expect] such that a failure will be reported via
[TContext.Fatal]. As with [gomega.Expect], additio


### Expect (test/utils/ktesting/tcontext.go:565)


Expect wraps [gomega.Expect] such that a failure will be reported via
[TContext.Fatal]. As with [gomega.Expect], additional values
may get passed. Those values then all must be nil for the assertion
to pass. This can be used with functions which return a value
plus error. The error gets checked automatically.

myAmazingThing := func(int, error) { ...}
tCtx.Expect(myAmazingThing()).Should(gomega.Equal(1))


```go
func (tCtx TContext) Expect((actual interface{}, extra ...interface{})) (actual interface{}, extra ...interface{})
```


**Тип ответа:** actual


```json
{
  "socketFileToInfo": {}
}
```


*Определено в:* `pkg/kubelet/pluginmanager/cache/actual_state_of_world.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** extra


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/unstructured.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/utils/ktesting/tcontext.go:565`



---


[function] name: Init file: test/utils/ktesting/tcontext.go:122 returns_error: нет description: Init can be called in a unit or integration test to create
a test context which:
- has a per-test logger with verbosity 


### Init (test/utils/ktesting/tcontext.go:122)


Init can be called in a unit or integration test to create
a test context which:
- has a per-test logger with verbosity derived from the -v command line flag
- gets canceled when the test finishes (via [TB.Cleanup])

Note that the test context supports the interfaces of [TB] and
[context.Context] and thus can be used like one of those where needed.
It also has additional methods for retrieving the logger and canceling
the context early, which can be useful in tests which want to wait
for goroutines to terminate after cancellation.

If the [TB] implementation also implements [ContextTB], then
[TContext.CleanupCtx] uses [ContextTB.CleanupCtx] and uses
the context passed into that callback. This can be used to let
Ginkgo create a fresh context for cleanup code.

Can be called more than once per test to get different contexts with
independent cancellation. The default behavior describe above can be
modified via optional functional options defined in [initoption].


```go
func Init((tb TB, opts ...InitOption)) (tb TB, opts ...InitOption)
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


**Тип ответа:** TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** InitOption


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/tcontext.go:122`



---


[function] name: InitCtx file: test/utils/ktesting/tcontext.go:218 returns_error: нет description: InitCtx is a variant of [Init] which uses an already existing context and
whatever logger and timeouts are stored there.


### InitCtx (test/utils/ktesting/tcontext.go:218)


InitCtx is a variant of [Init] which uses an already existing context and
whatever logger and timeouts are stored there.
Functional options are part of the API, but currently
there are none which have an effect.


```go
func InitCtx((ctx context.Context, tb TB, _ ...InitOption)) (ctx context.Context, tb TB, _ ...InitOption)
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


**Тип ответа:** TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** InitOption


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/tcontext.go:218`



---


[function] name: IsSyncTest file: test/utils/ktesting/tcontext.go:499 returns_error: нет description: IsSyncTest returns true if the context was created by SyncTest.

Inside such a context, Wait is usable. This can be used


### IsSyncTest (test/utils/ktesting/tcontext.go:499)


IsSyncTest returns true if the context was created by SyncTest.

Inside such a context, Wait is usable. This can be used in
code which runs inside synctest bubbles and outside:
- Inside a bubble, Wait can be used to block until
background activity has settled down (= "durably blocked").
Eventually and Consistently both call Wait and then check
the condition.
- Outside, polling or some synchronization mechanism has to be used.


```go
func (tCtx TContext) IsSyncTest(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:499`



---


[function] name: Logger file: test/utils/ktesting/tcontext.go:540 returns_error: нет description: Logger returns a logger for the current test. This is a shortcut
for calling klog.FromContext.

Output emitted via this 


### Logger (test/utils/ktesting/tcontext.go:540)


Logger returns a logger for the current test. This is a shortcut
for calling klog.FromContext.

Output emitted via this logger and the TB interface (like Logf)
is formatted consistently. The TB interface generates a single
message string, while Logger enables structured logging and can
be passed down into code which expects a logger.

To skip intermediate helper functions during stack unwinding,
TB.Helper can be called in those functions.


```go
func (tCtx TContext) Logger(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:540`



---


[function] name: Namespace file: test/utils/ktesting/tcontext.go:593 returns_error: нет description: Namespace returns the Kubernetes namespace name that was set previously
through WithNamespace and the empty string if no


### Namespace (test/utils/ktesting/tcontext.go:593)


Namespace returns the Kubernetes namespace name that was set previously
through WithNamespace and the empty string if none is available.

This namespace is the one to be used by tests which need to create namespace-scoped
objects. The name is guaranteed to be unique for the test context, so tests running
in parallel need to be set up so that each test has its own namespace.


```go
func (tCtx TContext) Namespace(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:593`



---


[function] name: Parallel file: test/utils/ktesting/tcontext.go:413 returns_error: нет description: Parallel signals that this test is to be run in parallel with (and
only with) other parallel tests. In other words, it n


### Parallel (test/utils/ktesting/tcontext.go:413)


Parallel signals that this test is to be run in parallel with (and
only with) other parallel tests. In other words, it needs to be
called in each test which is meant to run in parallel.

Only supported in Go unit tests, calling it elsewhere causes a test failure.

When a unit test is run multiple times due to use of -test.count or -test.cpu,
multiple instances of a single test never run in parallel with each other.


```go
func (tCtx TContext) Parallel(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:413`



---


[function] name: RESTConfig file: test/utils/ktesting/tcontext.go:548 returns_error: нет description: RESTConfig returns a copy of the config for a rest client with the UserAgent
set to include the current test name or nil


### RESTConfig (test/utils/ktesting/tcontext.go:548)


RESTConfig returns a copy of the config for a rest client with the UserAgent
set to include the current test name or nil if not available. Several typed
clients using this config are available through [Client], [Dynamic],
[APIExtensions].


```go
func (tCtx TContext) RESTConfig(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:548`



---


[function] name: RESTMapper file: test/utils/ktesting/tcontext.go:552 returns_error: нет description: —


### RESTMapper (test/utils/ktesting/tcontext.go:552)


RESTMapper is a method that performs operations based on the provided parameters and returns ().


```go
func (tCtx TContext) RESTMapper(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:552`



---


[function] name: Require file: test/utils/ktesting/tcontext.go:570 returns_error: нет description: Require is an alias for Expect.


### Require (test/utils/ktesting/tcontext.go:570)


Require is an alias for Expect.


```go
func (tCtx TContext) Require((actual interface{}, extra ...interface{})) (actual interface{}, extra ...interface{})
```


**Тип ответа:** actual


```json
{
  "socketFileToInfo": {}
}
```


*Определено в:* `pkg/kubelet/pluginmanager/cache/actual_state_of_world.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** extra


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/unstructured.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/utils/ktesting/tcontext.go:570`



---


[function] name: Run file: test/utils/ktesting/tcontext.go:477 returns_error: нет description: Run runs cb as a subtest called name. It blocks until cb returns or
calls t.Parallel to become a parallel test.

Only su


### Run (test/utils/ktesting/tcontext.go:477)


Run runs cb as a subtest called name. It blocks until cb returns or
calls t.Parallel to become a parallel test.

Only supported in Go unit tests or benchmarks. It fails the current
test when called elsewhere.


```go
func (tCtx TContext) Run((name string, cb func(tCtx TContext))) (name string, cb func(tCtx TContext))
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** cb


```json
{
  "block": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/aes/aes.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TContext


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


📍 *Расположение:* `test/utils/ktesting/tcontext.go:477`



---


[function] name: SyncTest file: test/utils/ktesting/tcontext.go:486 returns_error: нет description: SyncTest uses [synctest.Test] to execute the callback inside a bubble.
Creates a new subtest if the name is non-empty, o


### SyncTest (test/utils/ktesting/tcontext.go:486)


SyncTest uses [synctest.Test] to execute the callback inside a bubble.
Creates a new subtest if the name is non-empty, otherwise it creates
the bubble directly in the current test context.

Only works in Go unit tests.


```go
func (tCtx TContext) SyncTest((name string, cb func(tCtx TContext))) (name string, cb func(tCtx TContext))
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** cb


```json
{
  "block": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/aes/aes.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TContext


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


📍 *Расположение:* `test/utils/ktesting/tcontext.go:486`



---


[function] name: TB file: test/utils/ktesting/tcontext.go:528 returns_error: нет description: TB returns the underlying TB. This can be used to "break the glass"
and cast back into a testing.T or TB. Calling TB is 


### TB (test/utils/ktesting/tcontext.go:528)


TB returns the underlying TB. This can be used to "break the glass"
and cast back into a testing.T or TB. Calling TB is necessary
because TContext wraps the underlying TB.

For example, in benchmarks it is necessary to cast back to
a testing.B because not all benchmark-only methods are provided.
This examples uses separate functions again to ensure that
b isn't used unintentionally:

func BenchmarkSomething(b *testing.B) { benchmarkSomething(ktesting.Init(b) }
func benchmarkSomething(tCtx ktesting.TContext) {
... set up with tCtx ...
for tCtx.TB().(*testing.B).Loop() {
...
}
}


```go
func (tCtx TContext) TB(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:528`



---


[function] name: Wait file: test/utils/ktesting/tcontext.go:508 returns_error: нет description: Wait calls [synctest.Wait] and thus ensures that all background
activity has settled down (= "durably blocked").

Only w


### Wait (test/utils/ktesting/tcontext.go:508)


Wait calls [synctest.Wait] and thus ensures that all background
activity has settled down (= "durably blocked").

Only works inside a bubble started by SyncTest (can be checked with
IsSyncTest), panics elsewhere.


```go
func (tCtx TContext) Wait(()) ()
```


📍 *Расположение:* `test/utils/ktesting/tcontext.go:508`



---


[function] name: WithContext file: test/utils/ktesting/tcontext.go:305 returns_error: нет description: WithContext constructs a new TContext with a different Context instance.
This can be used in callbacks which receive a C


### WithContext (test/utils/ktesting/tcontext.go:305)


WithContext constructs a new TContext with a different Context instance.
This can be used in callbacks which receive a Context, for example
from Gomega:

gomega.Eventually(tCtx, func(ctx context.Context) {
tCtx := ktesting.WithContext(tCtx, ctx)
...

This is important because the Context in the callback could have
a different deadline than in the parent TContext.


```go
func (tCtx TContext) WithContext((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/utils/ktesting/tcontext.go:305`



---


[function] name: WithNamespace file: test/utils/ktesting/tcontext.go:582 returns_error: нет description: WithNamespace creates a new context with a Kubernetes namespace name for retrieval through [Namespace].


### WithNamespace (test/utils/ktesting/tcontext.go:582)


WithNamespace creates a new context with a Kubernetes namespace name for retrieval through [Namespace].


```go
func (tCtx TContext) WithNamespace((namespace string)) (namespace string)
```


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


📍 *Расположение:* `test/utils/ktesting/tcontext.go:582`



---


[function] name: WithValue file: test/utils/ktesting/tcontext.go:316 returns_error: нет description: WithValue wraps [context.WithValue] such that the result is again a TContext.


### WithValue (test/utils/ktesting/tcontext.go:316)


WithValue wraps [context.WithValue] such that the result is again a TContext.


```go
func (tCtx TContext) WithValue((key, val any)) (key, val any)
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


📍 *Расположение:* `test/utils/ktesting/tcontext.go:316`



---


[function] name: newLogger file: test/utils/ktesting/tcontext.go:171 returns_error: нет description: —


### newLogger (test/utils/ktesting/tcontext.go:171)


newLogger is a function that performs operations based on the provided parameters and returns (tb TB, bufferLogs bool).


```go
func newLogger((tb TB, bufferLogs bool)) (tb TB, bufferLogs bool)
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


**Тип ответа:** TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bufferLogs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/tcontext.go:171`



---


[function] name: run file: test/utils/ktesting/tcontext.go:253 returns_error: нет description: run implements the different Run and SyncTest methods. It's not an exported
method because tCtx.Run is more discoverable


### run (test/utils/ktesting/tcontext.go:253)


run implements the different Run and SyncTest methods. It's not an exported
method because tCtx.Run is more discoverable (same usage as
with normal Go).


```go
func run((tCtx TContext, name string, syncTest bool, cb func(tCtx TContext))) (tCtx TContext, name string, syncTest bool, cb func(tCtx TContext))
```


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TContext


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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** syncTest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cb


```json
{
  "block": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/aes/aes.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TContext


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


📍 *Расположение:* `test/utils/ktesting/tcontext.go:253`



---


[function] name: withTB file: test/utils/ktesting/tcontext.go:241 returns_error: нет description: withTB constructs a new TContext with a different TB instance.

This is used internally to set up some of the context, i


### withTB (test/utils/ktesting/tcontext.go:241)


withTB constructs a new TContext with a different TB instance.

This is used internally to set up some of the context, in particular
clients, in the root test and then run sub-tests:

func TestSomething(t *testing.T) {
tCtx := ktesting.Init(t)
...
tCtx = ktesting.WithRESTConfig(tCtx, config)

t.Run("sub", func (t *testing.T) {
tCtx := ktesting.WithTB(tCtx, t)
...
})

withTB sets up cancellation for the sub-test and uses per-test output.


```go
func (tCtx TContext) withTB((tb TB)) (tb TB)
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


**Тип ответа:** TB


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/tcontext.go:241`




## test/utils/ktesting/withcontext.go


📄 Исходный файл: `test/utils/ktesting/withcontext.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [WithCancel](#withcancel-testutilsktestingwithcontextgo29) `:29`

- 🔗 [WithLogger](#withlogger-testutilsktestingwithcontextgo68) `:68`

- 🔗 [WithTimeout](#withtimeout-testutilsktestingwithcontextgo59) `:59`

- 🔗 [WithoutCancel](#withoutcancel-testutilsktestingwithcontextgo46) `:46`


</details>


[function] name: WithCancel file: test/utils/ktesting/withcontext.go:29 returns_error: нет description: WithCancel sets up cancellation in a [TContext.Cleanup] callback and
constructs a new TContext where [TContext.Cancel] c


### WithCancel (test/utils/ktesting/withcontext.go:29)


WithCancel sets up cancellation in a [TContext.Cleanup] callback and
constructs a new TContext where [TContext.Cancel] cancels only the new
context.


```go
func (tCtx TContext) WithCancel(()) ()
```


📍 *Расположение:* `test/utils/ktesting/withcontext.go:29`



---


[function] name: WithLogger file: test/utils/ktesting/withcontext.go:68 returns_error: нет description: WithLogger constructs a new context with a different logger.


### WithLogger (test/utils/ktesting/withcontext.go:68)


WithLogger constructs a new context with a different logger.


```go
func (tCtx TContext) WithLogger((logger klog.Logger)) (logger klog.Logger)
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


📍 *Расположение:* `test/utils/ktesting/withcontext.go:68`



---


[function] name: WithTimeout file: test/utils/ktesting/withcontext.go:59 returns_error: нет description: WithTimeout sets up new context with a timeout. Canceling the timeout gets
registered in a cleanup callback. [TContext.C


### WithTimeout (test/utils/ktesting/withcontext.go:59)


WithTimeout sets up new context with a timeout. Canceling the timeout gets
registered in a cleanup callback. [TContext.Cancel] cancels only
the new context. The cause is used as reason why the context is canceled
once the timeout is reached. It may be empty, in which case the usual
"context canceled" error is used.


```go
func (tCtx TContext) WithTimeout((timeout time.Duration, timeoutCause string)) (timeout time.Duration, timeoutCause string)
```


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


**Тип ответа:** timeoutCause


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/ktesting/withcontext.go:59`



---


[function] name: WithoutCancel file: test/utils/ktesting/withcontext.go:46 returns_error: нет description: WithoutCancel causes the returned context to ignore cancellation of its parent.
Calling Cancel will not cancel the paren


### WithoutCancel (test/utils/ktesting/withcontext.go:46)


WithoutCancel causes the returned context to ignore cancellation of its parent.
Calling Cancel will not cancel the parent either.
This matches [context.WithoutCancel].


```go
func (tCtx TContext) WithoutCancel(()) ()
```


📍 *Расположение:* `test/utils/ktesting/withcontext.go:46`




## test/utils/kubeconfig/kubeconfig.go


📄 Исходный файл: `test/utils/kubeconfig/kubeconfig.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CreateKubeConfig](#createkubeconfig-testutilskubeconfigkubeconfiggo26) `:26`


</details>


[function] name: CreateKubeConfig file: test/utils/kubeconfig/kubeconfig.go:26 returns_error: нет description: CreateKubeConfig converts a [rest.Config] into a [clientcmdapi.Config]
which then can be written to a file with [clientc


### CreateKubeConfig (test/utils/kubeconfig/kubeconfig.go:26)


CreateKubeConfig converts a [rest.Config] into a [clientcmdapi.Config]
which then can be written to a file with [clientcmd.WriteToFile].


```go
func CreateKubeConfig((clientCfg *rest.Config)) (clientCfg *rest.Config)
```


**Тип запроса:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** clientCfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rest.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/utils/kubeconfig/kubeconfig.go:26`




## test/utils/localupcluster/cmd.go


📄 Исходный файл: `test/utils/localupcluster/cmd.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Output](#output-testutilslocalupclustercmdgo210) `:210`

- 🔗 [Running](#running-testutilslocalupclustercmdgo206) `:206`

- 🔗 [Start](#start-testutilslocalupclustercmdgo89) `:89`

- 🔗 [Stop](#stop-testutilslocalupclustercmdgo187) `:187`

- 🔗 [Wait](#wait-testutilslocalupclustercmdgo183) `:183`

- 🔗 [wait](#wait-testutilslocalupclustercmdgo197) `:197`


</details>


[function] name: Output file: test/utils/localupcluster/cmd.go:210 returns_error: нет description: —


### Output (test/utils/localupcluster/cmd.go:210)


Output is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (c *Cmd) Output((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
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


📍 *Расположение:* `test/utils/localupcluster/cmd.go:210`



---


[function] name: Running file: test/utils/localupcluster/cmd.go:206 returns_error: нет description: —


### Running (test/utils/localupcluster/cmd.go:206)


Running is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Cmd) Running(()) ()
```


📍 *Расположение:* `test/utils/localupcluster/cmd.go:206`



---


[function] name: Start file: test/utils/localupcluster/cmd.go:89 returns_error: нет description: —


### Start (test/utils/localupcluster/cmd.go:89)


Start is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (c *Cmd) Start((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
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


📍 *Расположение:* `test/utils/localupcluster/cmd.go:89`



---


[function] name: Stop file: test/utils/localupcluster/cmd.go:187 returns_error: нет description: —


### Stop (test/utils/localupcluster/cmd.go:187)


Stop is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, reason string).


```go
func (c *Cmd) Stop((tCtx ktesting.TContext, reason string)) (tCtx ktesting.TContext, reason string)
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


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/localupcluster/cmd.go:187`



---


[function] name: Wait file: test/utils/localupcluster/cmd.go:183 returns_error: нет description: —


### Wait (test/utils/localupcluster/cmd.go:183)


Wait is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func (c *Cmd) Wait((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
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


📍 *Расположение:* `test/utils/localupcluster/cmd.go:183`



---


[function] name: wait file: test/utils/localupcluster/cmd.go:197 returns_error: нет description: —


### wait (test/utils/localupcluster/cmd.go:197)


wait is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, killed bool).


```go
func (c *Cmd) wait((tCtx ktesting.TContext, killed bool)) (tCtx ktesting.TContext, killed bool)
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


**Тип ответа:** killed


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/localupcluster/cmd.go:197`




## test/utils/localupcluster/localupcluster.go


📄 Исходный файл: `test/utils/localupcluster/localupcluster.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [GetComponentFile](#getcomponentfile-testutilslocalupclusterlocalupclustergo352) `:352`

- 🔗 [GetSystemLogs](#getsystemlogs-testutilslocalupclusterlocalupclustergo303) `:303`

- 🔗 [GomegaString](#gomegastring-testutilslocalupclusterlocalupclustergo320) `:320`

- 🔗 [LoadConfig](#loadconfig-testutilslocalupclusterlocalupclustergo292) `:292`

- 🔗 [Modify](#modify-testutilslocalupclusterlocalupclustergo365) `:365`

- 🔗 [New](#new-testutilslocalupclusterlocalupclustergo92) `:92`

- 🔗 [Start](#start-testutilslocalupclusterlocalupclustergo127) `:127`

- 🔗 [Stop](#stop-testutilslocalupclusterlocalupclustergo279) `:279`

- 🔗 [String](#string-testutilslocalupclusterlocalupclustergo334) `:334`

- 🔗 [checkHealthz](#checkhealthz-testutilslocalupclusterlocalupclustergo484) `:484`

- 🔗 [checkReadiness](#checkreadiness-testutilslocalupclusterlocalupclustergo457) `:457`

- 🔗 [fromLocalUpClusterOutput](#fromlocalupclusteroutput-testutilslocalupclusterlocalupclustergo270) `:270`

- 🔗 [modifyComponent](#modifycomponent-testutilslocalupclusterlocalupclustergo383) `:383`

- 🔗 [processLocalUpClusterOutput](#processlocalupclusteroutput-testutilslocalupclusterlocalupclustergo199) `:199`

- 🔗 [repoRoot](#reporoot-testutilslocalupclusterlocalupclustergo78) `:78`

- 🔗 [runCmd](#runcmd-testutilslocalupclusterlocalupclustergo259) `:259`

- 🔗 [runComponentWithRetry](#runcomponentwithretry-testutilslocalupclusterlocalupclustergo425) `:425`

- 🔗 [runKubeComponent](#runkubecomponent-testutilslocalupclusterlocalupclustergo244) `:244`


</details>


[function] name: GetComponentFile file: test/utils/localupcluster/localupcluster.go:352 returns_error: нет description: —


### GetComponentFile (test/utils/localupcluster/localupcluster.go:352)


GetComponentFile is a method that retrieves data based on the provided parameters and returns (component KubeComponentName).


```go
func (m ModifyOptions) GetComponentFile((component KubeComponentName)) (component KubeComponentName)
```


**Тип ответа:** component


```json
{
  "name": "string",
  "args": [],
  "defaultAddr": "string",
  "defaultPort": "string",
  "endpoint": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/apiclient/wait.go`


**Тип ответа:** KubeComponentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:352`



---


[function] name: GetSystemLogs file: test/utils/localupcluster/localupcluster.go:303 returns_error: нет description: GetSystemLogs returns the output of the given component, the empty string and false if not started.


### GetSystemLogs (test/utils/localupcluster/localupcluster.go:303)


GetSystemLogs returns the output of the given component, the empty string and false if not started.


```go
func (c *Cluster) GetSystemLogs((GString, bool)) (GString, bool)
```


**Тип ответа:** GString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:303`



---


[function] name: GomegaString file: test/utils/localupcluster/localupcluster.go:320 returns_error: нет description: —


### GomegaString (test/utils/localupcluster/localupcluster.go:320)


GomegaString is a method that performs operations based on the provided parameters and returns ().


```go
func (gs GString) GomegaString(()) ()
```


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:320`



---


[function] name: LoadConfig file: test/utils/localupcluster/localupcluster.go:292 returns_error: нет description: LoadConfig returns the REST config for the running cluster.


### LoadConfig (test/utils/localupcluster/localupcluster.go:292)


LoadConfig returns the REST config for the running cluster.


```go
func (c *Cluster) LoadConfig((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
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


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:292`



---


[function] name: Modify file: test/utils/localupcluster/localupcluster.go:365 returns_error: нет description: Modify changes the cluster as described in the options.
It returns options that can be passed to Modify unchanged
to res


### Modify (test/utils/localupcluster/localupcluster.go:365)


Modify changes the cluster as described in the options.
It returns options that can be passed to Modify unchanged
to restore the original state.


```go
func (c *Cluster) Modify((tCtx ktesting.TContext, options ModifyOptions)) (tCtx ktesting.TContext, options ModifyOptions)
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


**Тип ответа:** ModifyOptions


```json
{
  "BinDir": "string",
  "FileByComponent": {},
  "Upgrade": false
}
```


*Определено в:* `test/utils/localupcluster/localupcluster.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:365`



---


[function] name: New file: test/utils/localupcluster/localupcluster.go:92 returns_error: нет description: —


### New (test/utils/localupcluster/localupcluster.go:92)


New is a function that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func New((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
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


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:92`



---


[function] name: Start file: test/utils/localupcluster/localupcluster.go:127 returns_error: нет description: Start brings up the cluster anew. If it was already running, it will be stopped first.

The cluster will be stopped auto


### Start (test/utils/localupcluster/localupcluster.go:127)


Start brings up the cluster anew. If it was already running, it will be stopped first.

The cluster will be stopped automatically at the end of the test.
If the ARTIFACTS env variable is set and the test failed,
log files of the kind cluster get dumped into
$ARTIFACTS/<test name>/kind/<cluster name> before stopping it.

The binary directory must contain kube-apiserver, kube-controller-manager,
kube-scheduler, kube-proxy, and kubelet. Those binaries can be from a previous
Kubernetes release. They will be invoked with parameters  as defined in the
*current* local-up-cluster.sh. This works as long as local-up-cluster.sh in its
default configuration doesn't depend on something which was added only recently.


```go
func (c *Cluster) Start((tCtx ktesting.TContext, bindir string, localUpClusterEnv map[string]string)) (tCtx ktesting.TContext, bindir string, localUpClusterEnv map[string]string)
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


**Тип ответа:** bindir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** localUpClusterEnv


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:127`



---


[function] name: Stop file: test/utils/localupcluster/localupcluster.go:279 returns_error: нет description: Stop ensures that the cluster is not running anymore.


### Stop (test/utils/localupcluster/localupcluster.go:279)


Stop ensures that the cluster is not running anymore.


```go
func (c *Cluster) Stop((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
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


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:279`



---


[function] name: String file: test/utils/localupcluster/localupcluster.go:334 returns_error: нет description: —


### String (test/utils/localupcluster/localupcluster.go:334)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (gs GString) String(()) ()
```


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:334`



---


[function] name: checkHealthz file: test/utils/localupcluster/localupcluster.go:484 returns_error: нет description: —


### checkHealthz (test/utils/localupcluster/localupcluster.go:484)


checkHealthz is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, cmd *Cmd, method, hostIP, port string).


```go
func (c *Cluster) checkHealthz((tCtx ktesting.TContext, cmd *Cmd, method, hostIP, port string)) (tCtx ktesting.TContext, cmd *Cmd, method, hostIP, port string)
```


**Тип запроса:** Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


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


**Тип ответа:** cmd


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


**Тип ответа:** method


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hostIP


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:484`



---


[function] name: checkReadiness file: test/utils/localupcluster/localupcluster.go:457 returns_error: нет description: —


### checkReadiness (test/utils/localupcluster/localupcluster.go:457)


checkReadiness is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, cmd *Cmd).


```go
func (c *Cluster) checkReadiness((tCtx ktesting.TContext, cmd *Cmd)) (tCtx ktesting.TContext, cmd *Cmd)
```


**Тип запроса:** Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


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


**Тип ответа:** cmd


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:457`



---


[function] name: fromLocalUpClusterOutput file: test/utils/localupcluster/localupcluster.go:270 returns_error: нет description: —


### fromLocalUpClusterOutput (test/utils/localupcluster/localupcluster.go:270)


fromLocalUpClusterOutput is a function that performs operations based on the provided parameters and returns (command string).


```go
func fromLocalUpClusterOutput((command string)) (command string)
```


**Тип ответа:** command


```json
{
  "PrintFlags": null,
  "Name": "string",
  "StructuredGenerator": {},
  "DryRunStrategy": {},
  "CreateAnnotation": false,
  "FieldManager": "string",
  "ValidationDirective": "string",
  "Namespace": "string",
  "EnforceNamespace": false,
  "Mapper": {},
  "DynamicClient": {},
  "PrintObj": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/create/create.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:270`



---


[function] name: modifyComponent file: test/utils/localupcluster/localupcluster.go:383 returns_error: нет description: —


### modifyComponent (test/utils/localupcluster/localupcluster.go:383)


modifyComponent is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, options ModifyOptions, component KubeComponentName, restore *ModifyOptions).


```go
func (c *Cluster) modifyComponent((tCtx ktesting.TContext, options ModifyOptions, component KubeComponentName, restore *ModifyOptions)) (tCtx ktesting.TContext, options ModifyOptions, component KubeComponentName, restore *ModifyOptions)
```


**Тип запроса:** ModifyOptions


```json
{
  "BinDir": "string",
  "FileByComponent": {},
  "Upgrade": false
}
```


*Определено в:* `test/utils/localupcluster/localupcluster.go`


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


**Тип ответа:** ModifyOptions


```json
{
  "BinDir": "string",
  "FileByComponent": {},
  "Upgrade": false
}
```


*Определено в:* `test/utils/localupcluster/localupcluster.go`


**Тип ответа:** component


```json
{
  "name": "string",
  "args": [],
  "defaultAddr": "string",
  "defaultPort": "string",
  "endpoint": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/apiclient/wait.go`


**Тип ответа:** KubeComponentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** restore


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModifyOptions


```json
{
  "BinDir": "string",
  "FileByComponent": {},
  "Upgrade": false
}
```


*Определено в:* `test/utils/localupcluster/localupcluster.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:383`



---


[function] name: processLocalUpClusterOutput file: test/utils/localupcluster/localupcluster.go:199 returns_error: нет description: —


### processLocalUpClusterOutput (test/utils/localupcluster/localupcluster.go:199)


processLocalUpClusterOutput is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, output Output).


```go
func (c *Cluster) processLocalUpClusterOutput((tCtx ktesting.TContext, output Output)) (tCtx ktesting.TContext, output Output)
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


**Тип ответа:** output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Output


```json
{
  "Line": "string",
  "EOF": false
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:199`



---


[function] name: repoRoot file: test/utils/localupcluster/localupcluster.go:78 returns_error: нет description: —


### repoRoot (test/utils/localupcluster/localupcluster.go:78)


repoRoot is a function that performs operations based on the provided parameters and returns (tCtx ktesting.TContext).


```go
func repoRoot((tCtx ktesting.TContext)) (tCtx ktesting.TContext)
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


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:78`



---


[function] name: runCmd file: test/utils/localupcluster/localupcluster.go:259 returns_error: нет description: —


### runCmd (test/utils/localupcluster/localupcluster.go:259)


runCmd is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, name, command string).


```go
func (c *Cluster) runCmd((tCtx ktesting.TContext, name, command string)) (tCtx ktesting.TContext, name, command string)
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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** command


```json
{
  "PrintFlags": null,
  "Name": "string",
  "StructuredGenerator": {},
  "DryRunStrategy": {},
  "CreateAnnotation": false,
  "FieldManager": "string",
  "ValidationDirective": "string",
  "Namespace": "string",
  "EnforceNamespace": false,
  "Mapper": {},
  "DynamicClient": {},
  "PrintObj": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/create/create.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:259`



---


[function] name: runComponentWithRetry file: test/utils/localupcluster/localupcluster.go:425 returns_error: нет description: —


### runComponentWithRetry (test/utils/localupcluster/localupcluster.go:425)


runComponentWithRetry is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, cmd *Cmd).


```go
func (c *Cluster) runComponentWithRetry((tCtx ktesting.TContext, cmd *Cmd)) (tCtx ktesting.TContext, cmd *Cmd)
```


**Тип запроса:** Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


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


**Тип ответа:** cmd


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:425`



---


[function] name: runKubeComponent file: test/utils/localupcluster/localupcluster.go:244 returns_error: нет description: —


### runKubeComponent (test/utils/localupcluster/localupcluster.go:244)


runKubeComponent is a method that performs operations based on the provided parameters and returns (tCtx ktesting.TContext, component KubeComponentName, command string).


```go
func (c *Cluster) runKubeComponent((tCtx ktesting.TContext, component KubeComponentName, command string)) (tCtx ktesting.TContext, component KubeComponentName, command string)
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


**Тип ответа:** component


```json
{
  "name": "string",
  "args": [],
  "defaultAddr": "string",
  "defaultPort": "string",
  "endpoint": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/apiclient/wait.go`


**Тип ответа:** KubeComponentName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** command


```json
{
  "PrintFlags": null,
  "Name": "string",
  "StructuredGenerator": {},
  "DryRunStrategy": {},
  "CreateAnnotation": false,
  "FieldManager": "string",
  "ValidationDirective": "string",
  "Namespace": "string",
  "EnforceNamespace": false,
  "Mapper": {},
  "DynamicClient": {},
  "PrintObj": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/create/create.go`


📍 *Расположение:* `test/utils/localupcluster/localupcluster.go:244`




## test/utils/node.go


📄 Исходный файл: `test/utils/node.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetNodeCondition](#getnodecondition-testutilsnodego23) `:23`


</details>


[function] name: GetNodeCondition file: test/utils/node.go:23 returns_error: нет description: GetNodeCondition extracts the provided condition from the given status and returns that.
Returns nil and -1 if the condi


### GetNodeCondition (test/utils/node.go:23)


GetNodeCondition extracts the provided condition from the given status and returns that.
Returns nil and -1 if the condition is not present, and the index of the located condition.


```go
func GetNodeCondition((int, *v1.NodeCondition)) (int, *v1.NodeCondition)
```


**Тип запроса:** v1.NodeCondition


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


📍 *Расположение:* `test/utils/node.go:23`




## test/utils/oidc/handlers/mocks.go


📄 Исходный файл: `test/utils/oidc/handlers/mocks.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [EXPECT](#expect-testutilsoidchandlersmocksgo51) `:51`

- 🔗 [EXPECT](#expect-testutilsoidchandlersmocksgo131) `:131`

- 🔗 [KeySet](#keyset-testutilsoidchandlersmocksgo136) `:136`

- 🔗 [KeySet](#keyset-testutilsoidchandlersmocksgo158) `:158`

- 🔗 [NewMockJWKsHandler](#newmockjwkshandler-testutilsoidchandlersmocksgo110) `:110`

- 🔗 [NewMockTokenHandler](#newmocktokenhandler-testutilsoidchandlersmocksgo30) `:30`

- 🔗 [Return](#return-testutilsoidchandlersmocksgo98) `:98`

- 🔗 [Return](#return-testutilsoidchandlersmocksgo169) `:169`

- 🔗 [Run](#run-testutilsoidchandlersmocksgo91) `:91`

- 🔗 [Run](#run-testutilsoidchandlersmocksgo162) `:162`

- 🔗 [RunAndReturn](#runandreturn-testutilsoidchandlersmocksgo103) `:103`

- 🔗 [RunAndReturn](#runandreturn-testutilsoidchandlersmocksgo174) `:174`

- 🔗 [Token](#token-testutilsoidchandlersmocksgo56) `:56`

- 🔗 [Token](#token-testutilsoidchandlersmocksgo87) `:87`


</details>


[function] name: EXPECT file: test/utils/oidc/handlers/mocks.go:51 returns_error: нет description: —


### EXPECT (test/utils/oidc/handlers/mocks.go:51)


EXPECT is a method that performs operations based on the provided parameters and returns ().


```go
func (_m *MockTokenHandler) EXPECT(()) ()
```


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:51`



---


[function] name: EXPECT file: test/utils/oidc/handlers/mocks.go:131 returns_error: нет description: —


### EXPECT (test/utils/oidc/handlers/mocks.go:131)


EXPECT is a method that performs operations based on the provided parameters and returns ().


```go
func (_m *MockJWKsHandler) EXPECT(()) ()
```


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:131`



---


[function] name: KeySet file: test/utils/oidc/handlers/mocks.go:136 returns_error: нет description: KeySet provides a mock function for the type MockJWKsHandler


### KeySet (test/utils/oidc/handlers/mocks.go:136)


KeySet provides a mock function for the type MockJWKsHandler


```go
func (_mock *MockJWKsHandler) KeySet(()) ()
```


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:136`



---


[function] name: KeySet file: test/utils/oidc/handlers/mocks.go:158 returns_error: нет description: KeySet is a helper method to define mock.On call


### KeySet (test/utils/oidc/handlers/mocks.go:158)


KeySet is a helper method to define mock.On call


```go
func (_e *MockJWKsHandler_Expecter) KeySet(()) ()
```


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:158`



---


[function] name: NewMockJWKsHandler file: test/utils/oidc/handlers/mocks.go:110 returns_error: нет description: NewMockJWKsHandler creates a new instance of MockJWKsHandler. It also registers a testing interface on the mock and a cl


### NewMockJWKsHandler (test/utils/oidc/handlers/mocks.go:110)


NewMockJWKsHandler creates a new instance of MockJWKsHandler. It also registers a testing interface on the mock and a cleanup function to assert the mocks expectations.
The first argument is typically a *testing.T value.


```go
func NewMockJWKsHandler((t interface {
	mock.TestingT
	Cleanup(func())
})) (t interface {
	mock.TestingT
	Cleanup(func())
})
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


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** mock.TestingT


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Cleanup


```json
{
  "itDescr": "string",
  "podCmd": "string"
}
```


*Определено в:* `test/e2e/node/kubelet.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:110`



---


[function] name: NewMockTokenHandler file: test/utils/oidc/handlers/mocks.go:30 returns_error: нет description: NewMockTokenHandler creates a new instance of MockTokenHandler. It also registers a testing interface on the mock and a 


### NewMockTokenHandler (test/utils/oidc/handlers/mocks.go:30)


NewMockTokenHandler creates a new instance of MockTokenHandler. It also registers a testing interface on the mock and a cleanup function to assert the mocks expectations.
The first argument is typically a *testing.T value.


```go
func NewMockTokenHandler((t interface {
	mock.TestingT
	Cleanup(func())
})) (t interface {
	mock.TestingT
	Cleanup(func())
})
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


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** mock.TestingT


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Cleanup


```json
{
  "itDescr": "string",
  "podCmd": "string"
}
```


*Определено в:* `test/e2e/node/kubelet.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:30`



---


[function] name: Return file: test/utils/oidc/handlers/mocks.go:98 returns_error: да description: —


### Return (test/utils/oidc/handlers/mocks.go:98)


Return is a method that performs operations based on the provided parameters and may return an error.


```go
func (_c *MockTokenHandler_Token_Call) Return((token Token, err error)) (token Token, err error)
```


**Тип ответа:** token


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** Token


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


*Типы возврата:* `token Token`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:98`



---


[function] name: Return file: test/utils/oidc/handlers/mocks.go:169 returns_error: нет description: —


### Return (test/utils/oidc/handlers/mocks.go:169)


Return is a method that performs operations based on the provided parameters and returns (jSONWebKeySet jose.JSONWebKeySet).


```go
func (_c *MockJWKsHandler_KeySet_Call) Return((jSONWebKeySet jose.JSONWebKeySet)) (jSONWebKeySet jose.JSONWebKeySet)
```


**Тип ответа:** jSONWebKeySet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** jose.JSONWebKeySet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:169`



---


[function] name: Run file: test/utils/oidc/handlers/mocks.go:91 returns_error: нет description: —


### Run (test/utils/oidc/handlers/mocks.go:91)


Run is a method that performs operations based on the provided parameters and returns (run func()).


```go
func (_c *MockTokenHandler_Token_Call) Run((run func())) (run func())
```


**Тип ответа:** run


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/node/v1alpha1/runtimeclass.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:91`



---


[function] name: Run file: test/utils/oidc/handlers/mocks.go:162 returns_error: нет description: —


### Run (test/utils/oidc/handlers/mocks.go:162)


Run is a method that performs operations based on the provided parameters and returns (run func()).


```go
func (_c *MockJWKsHandler_KeySet_Call) Run((run func())) (run func())
```


**Тип ответа:** run


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/node/v1alpha1/runtimeclass.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:162`



---


[function] name: RunAndReturn file: test/utils/oidc/handlers/mocks.go:103 returns_error: да description: —


### RunAndReturn (test/utils/oidc/handlers/mocks.go:103)


RunAndReturn is a method that performs operations based on the provided parameters and may return an error.


```go
func (_c *MockTokenHandler_Token_Call) RunAndReturn((run func() (Token, error))) (run func() (Token, error))
```


**Тип ответа:** run


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/node/v1alpha1/runtimeclass.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Token


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


*Типы возврата:* `run func() (Token`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:103`



---


[function] name: RunAndReturn file: test/utils/oidc/handlers/mocks.go:174 returns_error: нет description: —


### RunAndReturn (test/utils/oidc/handlers/mocks.go:174)


RunAndReturn is a method that performs operations based on the provided parameters and returns (run func() jose.JSONWebKeySet).


```go
func (_c *MockJWKsHandler_KeySet_Call) RunAndReturn((run func() jose.JSONWebKeySet)) (run func() jose.JSONWebKeySet)
```


**Тип ответа:** run


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/node/v1alpha1/runtimeclass.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** jose.JSONWebKeySet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:174`



---


[function] name: Token file: test/utils/oidc/handlers/mocks.go:56 returns_error: да description: Token provides a mock function for the type MockTokenHandler


### Token (test/utils/oidc/handlers/mocks.go:56)


Token provides a mock function for the type MockTokenHandler


```go
func (_mock *MockTokenHandler) Token((Token, error)) (Token, error)
```


**Тип ответа:** Token


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


*Типы возврата:* `Token`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:56`



---


[function] name: Token file: test/utils/oidc/handlers/mocks.go:87 returns_error: нет description: Token is a helper method to define mock.On call


### Token (test/utils/oidc/handlers/mocks.go:87)


Token is a helper method to define mock.On call


```go
func (_e *MockTokenHandler_Expecter) Token(()) ()
```


📍 *Расположение:* `test/utils/oidc/handlers/mocks.go:87`




## test/utils/oidc/testserver.go


📄 Исходный файл: `test/utils/oidc/testserver.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [BuildAndRunTestServer](#buildandruntestserver-testutilsoidctestservergo83) `:83`

- 🔗 [DefaultJwksHandlerBehavior](#defaultjwkshandlerbehavior-testutilsoidctestservergo230) `:230`

- 🔗 [GetSignatureAlgorithm](#getsignaturealgorithm-testutilsoidctestservergo248) `:248`

- 🔗 [JwksHandler](#jwkshandler-testutilsoidctestservergo58) `:58`

- 🔗 [TokenHandler](#tokenhandler-testutilsoidctestservergo63) `:63`

- 🔗 [TokenHandlerBehaviorReturningPredefinedJWT](#tokenhandlerbehaviorreturningpredefinedjwt-testutilsoidctestservergo197) `:197`

- 🔗 [TokenURL](#tokenurl-testutilsoidctestservergo73) `:73`

- 🔗 [URL](#url-testutilsoidctestservergo68) `:68`

- 🔗 [discoveryDocHandler](#discoverydochandler-testutilsoidctestservergo163) `:163`


</details>


[function] name: BuildAndRunTestServer file: test/utils/oidc/testserver.go:83 returns_error: нет description: BuildAndRunTestServer configures OIDC TLS server and its routing


### BuildAndRunTestServer (test/utils/oidc/testserver.go:83)


BuildAndRunTestServer configures OIDC TLS server and its routing


```go
func BuildAndRunTestServer((t *testing.T, caPath, caKeyPath, issuerOverride string)) (t *testing.T, caPath, caKeyPath, issuerOverride string)
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


**Тип ответа:** caPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** caKeyPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** issuerOverride


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/testserver.go:83`



---


[function] name: DefaultJwksHandlerBehavior file: test/utils/oidc/testserver.go:230 returns_error: нет description: DefaultJwksHandlerBehavior describes the scenario when JSON Web Key Set token is being returned.
This behavior should be


### DefaultJwksHandlerBehavior (test/utils/oidc/testserver.go:230)


DefaultJwksHandlerBehavior describes the scenario when JSON Web Key Set token is being returned.
This behavior should being applied to the MockJWKsHandler.


```go
func DefaultJwksHandlerBehavior((t *testing.T, verificationPublicKey K)) (t *testing.T, verificationPublicKey K)
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


**Тип ответа:** verificationPublicKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** K


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


📍 *Расположение:* `test/utils/oidc/testserver.go:230`



---


[function] name: GetSignatureAlgorithm file: test/utils/oidc/testserver.go:248 returns_error: нет description: —


### GetSignatureAlgorithm (test/utils/oidc/testserver.go:248)


GetSignatureAlgorithm is a function that retrieves data based on the provided parameters and returns (key K).


```go
func GetSignatureAlgorithm((key K)) (key K)
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


**Тип ответа:** K


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


📍 *Расположение:* `test/utils/oidc/testserver.go:248`



---


[function] name: JwksHandler file: test/utils/oidc/testserver.go:58 returns_error: нет description: JwksHandler is getter of JSON Web Key Sets handler


### JwksHandler (test/utils/oidc/testserver.go:58)


JwksHandler is getter of JSON Web Key Sets handler


```go
func (ts *TestServer) JwksHandler(()) ()
```


📍 *Расположение:* `test/utils/oidc/testserver.go:58`



---


[function] name: TokenHandler file: test/utils/oidc/testserver.go:63 returns_error: нет description: TokenHandler is getter of JWT token handler


### TokenHandler (test/utils/oidc/testserver.go:63)


TokenHandler is getter of JWT token handler


```go
func (ts *TestServer) TokenHandler(()) ()
```


📍 *Расположение:* `test/utils/oidc/testserver.go:63`



---


[function] name: TokenHandlerBehaviorReturningPredefinedJWT file: test/utils/oidc/testserver.go:197 returns_error: нет description: TokenHandlerBehaviorReturningPredefinedJWT describes the scenario when signed JWT token is being created.
This behavior 


### TokenHandlerBehaviorReturningPredefinedJWT (test/utils/oidc/testserver.go:197)


TokenHandlerBehaviorReturningPredefinedJWT describes the scenario when signed JWT token is being created.
This behavior should being applied to the MockTokenHandler.


```go
func TokenHandlerBehaviorReturningPredefinedJWT((
	t *testing.T,
	privateKey K,
	claims map[string]interface{}, accessToken, refreshToken string,
)) (
	t *testing.T,
	privateKey K,
	claims map[string]interface{}, accessToken, refreshToken string,
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


**Тип ответа:** privateKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** K


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


**Тип ответа:** claims


```json
{
  "Kubernetes": {}
}
```


*Определено в:* `test/images/agnhost/openidmetadata/openidmetadata.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** accessToken


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** refreshToken


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/testserver.go:197`



---


[function] name: TokenURL file: test/utils/oidc/testserver.go:73 returns_error: да description: TokenURL returns the public URL of JWT token endpoint


### TokenURL (test/utils/oidc/testserver.go:73)


TokenURL returns the public URL of JWT token endpoint


```go
func (ts *TestServer) TokenURL((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/oidc/testserver.go:73`



---


[function] name: URL file: test/utils/oidc/testserver.go:68 returns_error: нет description: URL returns the public URL of server


### URL (test/utils/oidc/testserver.go:68)


URL returns the public URL of server


```go
func (ts *TestServer) URL(()) ()
```


📍 *Расположение:* `test/utils/oidc/testserver.go:68`



---


[function] name: discoveryDocHandler file: test/utils/oidc/testserver.go:163 returns_error: нет description: —


### discoveryDocHandler (test/utils/oidc/testserver.go:163)


discoveryDocHandler is a function that performs operations based on the provided parameters and returns (t *testing.T, writer http.ResponseWriter, httpServerURL, issuer string).


```go
func discoveryDocHandler((t *testing.T, writer http.ResponseWriter, httpServerURL, issuer string)) (t *testing.T, writer http.ResponseWriter, httpServerURL, issuer string)
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


**Тип ответа:** writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** httpServerURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** issuer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/oidc/testserver.go:163`




## test/utils/paths.go


📄 Исходный файл: `test/utils/paths.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetCAdvisorRootDir](#getcadvisorrootdir-testutilspathsgo43) `:43`

- 🔗 [GetK8sBuildOutputDir](#getk8sbuildoutputdir-testutilspathsgo69) `:69`

- 🔗 [GetK8sRootDir](#getk8srootdir-testutilspathsgo29) `:29`

- 🔗 [RootDir](#rootdir-testutilspathsgo52) `:52`


</details>


[function] name: GetCAdvisorRootDir file: test/utils/paths.go:43 returns_error: да description: GetCAdvisorRootDir returns the root directory for cAdvisor, if present in the gopath.


### GetCAdvisorRootDir (test/utils/paths.go:43)


GetCAdvisorRootDir returns the root directory for cAdvisor, if present in the gopath.


```go
func GetCAdvisorRootDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/paths.go:43`



---


[function] name: GetK8sBuildOutputDir file: test/utils/paths.go:69 returns_error: да description: GetK8sBuildOutputDir returns the build output directory for k8s
For dockerized build, targetArch (eg: 'linux/arm64', 'li


### GetK8sBuildOutputDir (test/utils/paths.go:69)


GetK8sBuildOutputDir returns the build output directory for k8s
For dockerized build, targetArch (eg: 'linux/arm64', 'linux/amd64') must be explicitly specified
For non dockerized build, targetArch is ignored


```go
func GetK8sBuildOutputDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/paths.go:69`



---


[function] name: GetK8sRootDir file: test/utils/paths.go:29 returns_error: да description: GetK8sRootDir returns the root directory for kubernetes, if present in the gopath.


### GetK8sRootDir (test/utils/paths.go:29)


GetK8sRootDir returns the root directory for kubernetes, if present in the gopath.


```go
func GetK8sRootDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/paths.go:29`



---


[function] name: RootDir file: test/utils/paths.go:52 returns_error: да description: RootDir gets the on-disk kubernetes source directory, returning an error is none is found


### RootDir (test/utils/paths.go:52)


RootDir gets the on-disk kubernetes source directory, returning an error is none is found


```go
func RootDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/paths.go:52`




## test/utils/pki_helpers.go


📄 Исходный файл: `test/utils/pki_helpers.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [EncodeCertPEM](#encodecertpem-testutilspki_helpersgo46) `:46`

- 🔗 [NewPrivateKey](#newprivatekey-testutilspki_helpersgo41) `:41`

- 🔗 [NewSignedCert](#newsignedcert-testutilspki_helpersgo55) `:55`


</details>


[function] name: EncodeCertPEM file: test/utils/pki_helpers.go:46 returns_error: нет description: EncodeCertPEM returns PEM-endcoded certificate data


### EncodeCertPEM (test/utils/pki_helpers.go:46)


EncodeCertPEM returns PEM-endcoded certificate data


```go
func EncodeCertPEM((cert *x509.Certificate)) (cert *x509.Certificate)
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


**Тип ответа:** cert


```json
{
  "pkiDir": "string",
  "caBaseName": "string",
  "baseName": "string",
  "uxName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/certs.go`


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


📍 *Расположение:* `test/utils/pki_helpers.go:46`



---


[function] name: NewPrivateKey file: test/utils/pki_helpers.go:41 returns_error: да description: NewPrivateKey creates an RSA private key


### NewPrivateKey (test/utils/pki_helpers.go:41)


NewPrivateKey creates an RSA private key


```go
func NewPrivateKey((*rsa.PrivateKey, error)) (*rsa.PrivateKey, error)
```


**Тип запроса:** rsa.PrivateKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rsa.PrivateKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*rsa.PrivateKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/pki_helpers.go:41`



---


[function] name: NewSignedCert file: test/utils/pki_helpers.go:55 returns_error: да description: NewSignedCert creates a signed certificate using the given CA certificate and key


### NewSignedCert (test/utils/pki_helpers.go:55)


NewSignedCert creates a signed certificate using the given CA certificate and key


```go
func NewSignedCert((*x509.Certificate, error)) (*x509.Certificate, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*x509.Certificate`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/pki_helpers.go:55`




## test/utils/pod_store.go


📄 Исходный файл: `test/utils/pod_store.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [List](#list-testutilspod_storego71) `:71`

- 🔗 [NewPodStore](#newpodstore-testutilspod_storego41) `:41`

- 🔗 [Stop](#stop-testutilspod_storego80) `:80`


</details>


[function] name: List file: test/utils/pod_store.go:71 returns_error: нет description: —


### List (test/utils/pod_store.go:71)


List is a method that lists or finds data based on the provided parameters and returns ().


```go
func (s *PodStore) List(()) ()
```


📍 *Расположение:* `test/utils/pod_store.go:71`



---


[function] name: NewPodStore file: test/utils/pod_store.go:41 returns_error: да description: —


### NewPodStore (test/utils/pod_store.go:41)


NewPodStore is a function that performs operations based on the provided parameters and may return an error.


```go
func NewPodStore((*PodStore, error)) (*PodStore, error)
```


**Тип запроса:** PodStore


```json
{
  "stopCh": {},
  "Reflector": null
}
```


*Определено в:* `test/utils/pod_store.go`


**Тип ответа:** PodStore


```json
{
  "stopCh": {},
  "Reflector": null
}
```


*Определено в:* `test/utils/pod_store.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PodStore`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/pod_store.go:41`



---


[function] name: Stop file: test/utils/pod_store.go:80 returns_error: нет description: —


### Stop (test/utils/pod_store.go:80)


Stop is a method that performs operations based on the provided parameters and returns ().


```go
func (s *PodStore) Stop(()) ()
```


📍 *Расположение:* `test/utils/pod_store.go:80`




## test/utils/replicaset.go


📄 Исходный файл: `test/utils/replicaset.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [UpdateReplicaSetWithRetries](#updatereplicasetwithretries-testutilsreplicasetgo33) `:33`

- 🔗 [WaitRSStable](#waitrsstable-testutilsreplicasetgo57) `:57`


</details>


[function] name: UpdateReplicaSetWithRetries file: test/utils/replicaset.go:33 returns_error: да description: —


### UpdateReplicaSetWithRetries (test/utils/replicaset.go:33)


UpdateReplicaSetWithRetries is a function that updates data based on the provided parameters and may return an error.


```go
func UpdateReplicaSetWithRetries((*apps.ReplicaSet, error)) (*apps.ReplicaSet, error)
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


📍 *Расположение:* `test/utils/replicaset.go:33`



---


[function] name: WaitRSStable file: test/utils/replicaset.go:57 returns_error: нет description: Verify .Status.Replicas is equal to .Spec.Replicas


### WaitRSStable (test/utils/replicaset.go:57)


Verify .Status.Replicas is equal to .Spec.Replicas


```go
func WaitRSStable((t *testing.T, clientSet clientset.Interface, rs *apps.ReplicaSet, pollInterval, pollTimeout time.Duration)) (t *testing.T, clientSet clientset.Interface, rs *apps.ReplicaSet, pollInterval, pollTimeout time.Duration)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип запроса:** apps.ReplicaSet


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


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** apps.ReplicaSet


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/apps/types.go`


**Тип ответа:** pollInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pollTimeout


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


📍 *Расположение:* `test/utils/replicaset.go:57`




## test/utils/runners.go


📄 Исходный файл: `test/utils/runners.go`


<details open>
<summary><b>Функции в этом файле (57)</b></summary>


- 🔗 [AddStrategy](#addstrategy-testutilsrunnersgo1103) `:1103`

- 🔗 [CleanupDependentObjects](#cleanupdependentobjects-testutilsrunnersgo827) `:827`

- 🔗 [CleanupDependentObjects](#cleanupdependentobjects-testutilsrunnersgo868) `:868`

- 🔗 [CleanupDependentObjects](#cleanupdependentobjects-testutilsrunnersgo991) `:991`

- 🔗 [CleanupDependentObjects](#cleanupdependentobjects-testutilsrunnersgo1041) `:1041`

- 🔗 [CleanupNode](#cleanupnode-testutilsrunnersgo818) `:818`

- 🔗 [CleanupNode](#cleanupnode-testutilsrunnersgo856) `:856`

- 🔗 [CleanupNode](#cleanupnode-testutilsrunnersgo916) `:916`

- 🔗 [CleanupNode](#cleanupnode-testutilsrunnersgo1029) `:1029`

- 🔗 [CreatePod](#createpod-testutilsrunnersgo1159) `:1159`

- 🔗 [CreatePodWithPersistentVolume](#createpodwithpersistentvolume-testutilsrunnersgo1189) `:1189`

- 🔗 [CreatePods](#createpods-testutilsrunnersgo1121) `:1121`

- 🔗 [DeletedPods](#deletedpods-testutilsrunnersgo250) `:250`

- 🔗 [DoPrepareNode](#dopreparenode-testutilsrunnersgo1045) `:1045`

- 🔗 [GetPodTemplate](#getpodtemplate-testutilsrunnersgo1318) `:1318`

- 🔗 [MakePodSpec](#makepodspec-testutilsrunnersgo1132) `:1132`

- 🔗 [NewCreatePodWithPersistentVolumeStrategy](#newcreatepodwithpersistentvolumestrategy-testutilsrunnersgo1322) `:1322`

- 🔗 [NewCustomCreatePodStrategy](#newcustomcreatepodstrategy-testutilsrunnersgo1288) `:1288`

- 🔗 [NewLabelNodePrepareStrategy](#newlabelnodepreparestrategy-testutilsrunnersgo839) `:839`

- 🔗 [NewNodeAllocatableStrategy](#newnodeallocatablestrategy-testutilsrunnersgo886) `:886`

- 🔗 [NewTestPodCreator](#newtestpodcreator-testutilsrunnersgo1114) `:1114`

- 🔗 [NewTestPodCreatorConfig](#newtestpodcreatorconfig-testutilsrunnersgo1088) `:1088`

- 🔗 [NewUniqueNodeLabelStrategy](#newuniquenodelabelstrategy-testutilsrunnersgo1017) `:1017`

- 🔗 [PrepareDependentObjects](#preparedependentobjects-testutilsrunnersgo823) `:823`

- 🔗 [PrepareDependentObjects](#preparedependentobjects-testutilsrunnersgo864) `:864`

- 🔗 [PrepareDependentObjects](#preparedependentobjects-testutilsrunnersgo980) `:980`

- 🔗 [PrepareDependentObjects](#preparedependentobjects-testutilsrunnersgo1037) `:1037`

- 🔗 [PreparePatch](#preparepatch-testutilsrunnersgo814) `:814`

- 🔗 [PreparePatch](#preparepatch-testutilsrunnersgo846) `:846`

- 🔗 [PreparePatch](#preparepatch-testutilsrunnersgo894) `:894`

- 🔗 [PreparePatch](#preparepatch-testutilsrunnersgo1023) `:1023`

- 🔗 [RCConfigLog](#rcconfiglog-testutilsrunnersgo182) `:182`

- 🔗 [RunDeployment](#rundeployment-testutilsrunnersgo284) `:284`

- 🔗 [RunPodAndGetNodeName](#runpodandgetnodename-testutilsrunnersgo74) `:74`

- 🔗 [RunRC](#runrc-testutilsrunnersgo430) `:430`

- 🔗 [RunReplicaSet](#runreplicaset-testutilsrunnersgo359) `:359`

- 🔗 [StartPods](#startpods-testutilsrunnersgo730) `:730`

- 🔗 [StaticPodTemplate](#staticpodtemplate-testutilsrunnersgo1310) `:1310`

- 🔗 [String](#string-testutilsrunnersgo213) `:213`

- 🔗 [String](#string-testutilsrunnersgo579) `:579`

- 🔗 [WaitForEnoughPodsWithLabelRunning](#waitforenoughpodswithlabelrunning-testutilsrunnersgo766) `:766`

- 🔗 [WaitForPodsWithLabelRunning](#waitforpodswithlabelrunning-testutilsrunnersgo760) `:760`

- 🔗 [applyTo](#applyto-testutilsrunnersgo506) `:506`

- 🔗 [attachConfigMaps](#attachconfigmaps-testutilsrunnersgo1352) `:1352`

- 🔗 [attachSecrets](#attachsecrets-testutilsrunnersgo1329) `:1329`

- 🔗 [attachServiceAccountTokenProjection](#attachserviceaccounttokenprojection-testutilsrunnersgo1383) `:1383`

- 🔗 [computeRCStartupStatus](#computercstartupstatus-testutilsrunnersgo584) `:584`

- 🔗 [create](#create-testutilsrunnersgo292) `:292`

- 🔗 [create](#create-testutilsrunnersgo367) `:367`

- 🔗 [create](#create-testutilsrunnersgo438) `:438`

- 🔗 [createCSINode](#createcsinode-testutilsrunnersgo924) `:924`

- 🔗 [diff](#diff-testutilsrunnersgo261) `:261`

- 🔗 [getTerminationGracePeriodSeconds](#getterminationgraceperiodseconds-testutilsrunnersgo1376) `:1376`

- 🔗 [makeCreatePod](#makecreatepod-testutilsrunnersgo1152) `:1152`

- 🔗 [start](#start-testutilsrunnersgo633) `:633`

- 🔗 [updateCSINode](#updatecsinode-testutilsrunnersgo955) `:955`

- 🔗 [waitUntilPodIsScheduled](#waituntilpodisscheduled-testutilsrunnersgo56) `:56`


</details>


[function] name: AddStrategy file: test/utils/runners.go:1103 returns_error: нет description: —


### AddStrategy (test/utils/runners.go:1103)


AddStrategy is a method that creates new data based on the provided parameters and returns (
	namespace string, podCount int, strategy TestPodCreateStrategy).


```go
func (c *TestPodCreatorConfig) AddStrategy((
	namespace string, podCount int, strategy TestPodCreateStrategy)) (
	namespace string, podCount int, strategy TestPodCreateStrategy)
```


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podCount


```json
{
  "podName": "string",
  "podCount": 0
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/admission/admission.go`


**Тип ответа:** strategy


```json
{
  "alwaysAutoUpdateSpec": false,
  "name": "string"
}
```


*Определено в:* `pkg/registry/flowcontrol/ensurer/strategy.go`


**Тип ответа:** TestPodCreateStrategy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:1103`



---


[function] name: CleanupDependentObjects file: test/utils/runners.go:827 returns_error: нет description: —


### CleanupDependentObjects (test/utils/runners.go:827)


CleanupDependentObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, nodeName string, client clientset.Interface).


```go
func (*TrivialNodePrepareStrategy) CleanupDependentObjects((ctx context.Context, nodeName string, client clientset.Interface)) (ctx context.Context, nodeName string, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:827`



---


[function] name: CleanupDependentObjects file: test/utils/runners.go:868 returns_error: нет description: —


### CleanupDependentObjects (test/utils/runners.go:868)


CleanupDependentObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, nodeName string, client clientset.Interface).


```go
func (*LabelNodePrepareStrategy) CleanupDependentObjects((ctx context.Context, nodeName string, client clientset.Interface)) (ctx context.Context, nodeName string, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:868`



---


[function] name: CleanupDependentObjects file: test/utils/runners.go:991 returns_error: нет description: —


### CleanupDependentObjects (test/utils/runners.go:991)


CleanupDependentObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, nodeName string, client clientset.Interface).


```go
func (s *NodeAllocatableStrategy) CleanupDependentObjects((ctx context.Context, nodeName string, client clientset.Interface)) (ctx context.Context, nodeName string, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:991`



---


[function] name: CleanupDependentObjects file: test/utils/runners.go:1041 returns_error: нет description: —


### CleanupDependentObjects (test/utils/runners.go:1041)


CleanupDependentObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, nodeName string, client clientset.Interface).


```go
func (*UniqueNodeLabelStrategy) CleanupDependentObjects((ctx context.Context, nodeName string, client clientset.Interface)) (ctx context.Context, nodeName string, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:1041`



---


[function] name: CleanupNode file: test/utils/runners.go:818 returns_error: нет description: —


### CleanupNode (test/utils/runners.go:818)


CleanupNode is a method that performs operations based on the provided parameters and returns (ctx context.Context, node *v1.Node).


```go
func (*TrivialNodePrepareStrategy) CleanupNode((ctx context.Context, node *v1.Node)) (ctx context.Context, node *v1.Node)
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


📍 *Расположение:* `test/utils/runners.go:818`



---


[function] name: CleanupNode file: test/utils/runners.go:856 returns_error: нет description: —


### CleanupNode (test/utils/runners.go:856)


CleanupNode is a method that performs operations based on the provided parameters and returns (ctx context.Context, node *v1.Node).


```go
func (s *LabelNodePrepareStrategy) CleanupNode((ctx context.Context, node *v1.Node)) (ctx context.Context, node *v1.Node)
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


📍 *Расположение:* `test/utils/runners.go:856`



---


[function] name: CleanupNode file: test/utils/runners.go:916 returns_error: нет description: —


### CleanupNode (test/utils/runners.go:916)


CleanupNode is a method that performs operations based on the provided parameters and returns (ctx context.Context, node *v1.Node).


```go
func (s *NodeAllocatableStrategy) CleanupNode((ctx context.Context, node *v1.Node)) (ctx context.Context, node *v1.Node)
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


📍 *Расположение:* `test/utils/runners.go:916`



---


[function] name: CleanupNode file: test/utils/runners.go:1029 returns_error: нет description: —


### CleanupNode (test/utils/runners.go:1029)


CleanupNode is a method that performs operations based on the provided parameters and returns (ctx context.Context, node *v1.Node).


```go
func (s *UniqueNodeLabelStrategy) CleanupNode((ctx context.Context, node *v1.Node)) (ctx context.Context, node *v1.Node)
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


📍 *Расположение:* `test/utils/runners.go:1029`



---


[function] name: CreatePod file: test/utils/runners.go:1159 returns_error: нет description: —


### CreatePod (test/utils/runners.go:1159)


CreatePod is a function that creates new data based on the provided parameters and returns (ctx context.Context, client clientset.Interface, namespace string, podCount int, podTemplate PodTemplate).


```go
func CreatePod((ctx context.Context, client clientset.Interface, namespace string, podCount int, podTemplate PodTemplate)) (ctx context.Context, client clientset.Interface, namespace string, podCount int, podTemplate PodTemplate)
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


**Тип ответа:** podCount


```json
{
  "podName": "string",
  "podCount": 0
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/admission/admission.go`


**Тип ответа:** podTemplate


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/podtemplate.go`


**Тип ответа:** PodTemplate


```json
{
  "Template": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/utils/runners.go:1159`



---


[function] name: CreatePodWithPersistentVolume file: test/utils/runners.go:1189 returns_error: нет description: —


### CreatePodWithPersistentVolume (test/utils/runners.go:1189)


CreatePodWithPersistentVolume is a function that creates new data based on the provided parameters and returns (ctx context.Context, client clientset.Interface, namespace string, claimTemplate *v1.PersistentVolumeClaim, factory volumeFactory, podTemplate PodTemplate, count int, bindVolume bool).


```go
func CreatePodWithPersistentVolume((ctx context.Context, client clientset.Interface, namespace string, claimTemplate *v1.PersistentVolumeClaim, factory volumeFactory, podTemplate PodTemplate, count int, bindVolume bool)) (ctx context.Context, client clientset.Interface, namespace string, claimTemplate *v1.PersistentVolumeClaim, factory volumeFactory, podTemplate PodTemplate, count int, bindVolume bool)
```


**Тип запроса:** v1.PersistentVolumeClaim


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


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** claimTemplate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** volumeFactory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podTemplate


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/podtemplate.go`


**Тип ответа:** PodTemplate


```json
{
  "Template": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** count


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** bindVolume


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:1189`



---


[function] name: CreatePods file: test/utils/runners.go:1121 returns_error: нет description: —


### CreatePods (test/utils/runners.go:1121)


CreatePods is a method that creates new data based on the provided parameters and returns (ctx context.Context).


```go
func (c *TestPodCreator) CreatePods((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/utils/runners.go:1121`



---


[function] name: DeletedPods file: test/utils/runners.go:250 returns_error: нет description: DeletedPods returns a slice of pods that were present at the beginning
and then disappeared.


### DeletedPods (test/utils/runners.go:250)


DeletedPods returns a slice of pods that were present at the beginning
and then disappeared.


```go
func (p podDiff) DeletedPods(()) ()
```


📍 *Расположение:* `test/utils/runners.go:250`



---


[function] name: DoPrepareNode file: test/utils/runners.go:1045 returns_error: нет description: —


### DoPrepareNode (test/utils/runners.go:1045)


DoPrepareNode is a function that performs operations based on the provided parameters and returns (ctx context.Context, client clientset.Interface, node *v1.Node, strategy PrepareNodeStrategy).


```go
func DoPrepareNode((ctx context.Context, client clientset.Interface, node *v1.Node, strategy PrepareNodeStrategy)) (ctx context.Context, client clientset.Interface, node *v1.Node, strategy PrepareNodeStrategy)
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


**Тип ответа:** strategy


```json
{
  "alwaysAutoUpdateSpec": false,
  "name": "string"
}
```


*Определено в:* `pkg/registry/flowcontrol/ensurer/strategy.go`


**Тип ответа:** PrepareNodeStrategy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:1045`



---


[function] name: GetPodTemplate file: test/utils/runners.go:1318 returns_error: да description: GetPodTemplate implements [PodTemplate.GetPodTemplate] by returning the same pod
for each call.


### GetPodTemplate (test/utils/runners.go:1318)


GetPodTemplate implements [PodTemplate.GetPodTemplate] by returning the same pod
for each call.


```go
func (s *staticPodTemplate) GetPodTemplate((*v1.Pod, error)) (*v1.Pod, error)
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


📍 *Расположение:* `test/utils/runners.go:1318`



---


[function] name: MakePodSpec file: test/utils/runners.go:1132 returns_error: нет description: —


### MakePodSpec (test/utils/runners.go:1132)


MakePodSpec is a function that performs operations based on the provided parameters and returns ().


```go
func MakePodSpec(()) ()
```


📍 *Расположение:* `test/utils/runners.go:1132`



---


[function] name: NewCreatePodWithPersistentVolumeStrategy file: test/utils/runners.go:1322 returns_error: нет description: —


### NewCreatePodWithPersistentVolumeStrategy (test/utils/runners.go:1322)


NewCreatePodWithPersistentVolumeStrategy is a function that performs operations based on the provided parameters and returns (claimTemplate *v1.PersistentVolumeClaim, factory volumeFactory, podTemplate PodTemplate).


```go
func NewCreatePodWithPersistentVolumeStrategy((claimTemplate *v1.PersistentVolumeClaim, factory volumeFactory, podTemplate PodTemplate)) (claimTemplate *v1.PersistentVolumeClaim, factory volumeFactory, podTemplate PodTemplate)
```


**Тип запроса:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** claimTemplate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.PersistentVolumeClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** volumeFactory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podTemplate


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/podtemplate.go`


**Тип ответа:** PodTemplate


```json
{
  "Template": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/utils/runners.go:1322`



---


[function] name: NewCustomCreatePodStrategy file: test/utils/runners.go:1288 returns_error: нет description: —


### NewCustomCreatePodStrategy (test/utils/runners.go:1288)


NewCustomCreatePodStrategy is a function that performs operations based on the provided parameters and returns (podTemplate PodTemplate).


```go
func NewCustomCreatePodStrategy((podTemplate PodTemplate)) (podTemplate PodTemplate)
```


**Тип ответа:** podTemplate


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/podtemplate.go`


**Тип ответа:** PodTemplate


```json
{
  "Template": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/utils/runners.go:1288`



---


[function] name: NewLabelNodePrepareStrategy file: test/utils/runners.go:839 returns_error: нет description: —


### NewLabelNodePrepareStrategy (test/utils/runners.go:839)


NewLabelNodePrepareStrategy is a function that performs operations based on the provided parameters and returns (labelKey string, labelValues ...string).


```go
func NewLabelNodePrepareStrategy((labelKey string, labelValues ...string)) (labelKey string, labelValues ...string)
```


**Тип ответа:** labelKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelValues


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/utils/runners.go:839`



---


[function] name: NewNodeAllocatableStrategy file: test/utils/runners.go:886 returns_error: нет description: —


### NewNodeAllocatableStrategy (test/utils/runners.go:886)


NewNodeAllocatableStrategy is a function that performs operations based on the provided parameters and returns (nodeAllocatable map[v1.ResourceName]string, csiNodeAllocatable map[string]*storagev1.VolumeNodeResources, migratedPlugins []string).


```go
func NewNodeAllocatableStrategy((nodeAllocatable map[v1.ResourceName]string, csiNodeAllocatable map[string]*storagev1.VolumeNodeResources, migratedPlugins []string)) (nodeAllocatable map[v1.ResourceName]string, csiNodeAllocatable map[string]*storagev1.VolumeNodeResources, migratedPlugins []string)
```


**Тип запроса:** storagev1.VolumeNodeResources


```json
{
  "Count": 0
}
```


*Определено в:* `pkg/apis/storage/types.go`


**Тип ответа:** nodeAllocatable


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** v1.ResourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** csiNodeAllocatable


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** storagev1.VolumeNodeResources


```json
{
  "Count": 0
}
```


*Определено в:* `pkg/apis/storage/types.go`


**Тип ответа:** migratedPlugins


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:886`



---


[function] name: NewTestPodCreator file: test/utils/runners.go:1114 returns_error: нет description: —


### NewTestPodCreator (test/utils/runners.go:1114)


NewTestPodCreator is a function that performs operations based on the provided parameters and returns (client clientset.Interface, config *TestPodCreatorConfig).


```go
func NewTestPodCreator((client clientset.Interface, config *TestPodCreatorConfig)) (client clientset.Interface, config *TestPodCreatorConfig)
```


**Тип запроса:** TestPodCreatorConfig


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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** TestPodCreatorConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:1114`



---


[function] name: NewTestPodCreatorConfig file: test/utils/runners.go:1088 returns_error: нет description: —


### NewTestPodCreatorConfig (test/utils/runners.go:1088)


NewTestPodCreatorConfig is a function that performs operations based on the provided parameters and returns ().


```go
func NewTestPodCreatorConfig(()) ()
```


📍 *Расположение:* `test/utils/runners.go:1088`



---


[function] name: NewUniqueNodeLabelStrategy file: test/utils/runners.go:1017 returns_error: нет description: —


### NewUniqueNodeLabelStrategy (test/utils/runners.go:1017)


NewUniqueNodeLabelStrategy is a function that performs operations based on the provided parameters and returns (labelKey string).


```go
func NewUniqueNodeLabelStrategy((labelKey string)) (labelKey string)
```


**Тип ответа:** labelKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:1017`



---


[function] name: PrepareDependentObjects file: test/utils/runners.go:823 returns_error: нет description: —


### PrepareDependentObjects (test/utils/runners.go:823)


PrepareDependentObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, node *v1.Node, client clientset.Interface).


```go
func (*TrivialNodePrepareStrategy) PrepareDependentObjects((ctx context.Context, node *v1.Node, client clientset.Interface)) (ctx context.Context, node *v1.Node, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:823`



---


[function] name: PrepareDependentObjects file: test/utils/runners.go:864 returns_error: нет description: —


### PrepareDependentObjects (test/utils/runners.go:864)


PrepareDependentObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, node *v1.Node, client clientset.Interface).


```go
func (*LabelNodePrepareStrategy) PrepareDependentObjects((ctx context.Context, node *v1.Node, client clientset.Interface)) (ctx context.Context, node *v1.Node, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:864`



---


[function] name: PrepareDependentObjects file: test/utils/runners.go:980 returns_error: нет description: —


### PrepareDependentObjects (test/utils/runners.go:980)


PrepareDependentObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, node *v1.Node, client clientset.Interface).


```go
func (s *NodeAllocatableStrategy) PrepareDependentObjects((ctx context.Context, node *v1.Node, client clientset.Interface)) (ctx context.Context, node *v1.Node, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:980`



---


[function] name: PrepareDependentObjects file: test/utils/runners.go:1037 returns_error: нет description: —


### PrepareDependentObjects (test/utils/runners.go:1037)


PrepareDependentObjects is a method that performs operations based on the provided parameters and returns (ctx context.Context, node *v1.Node, client clientset.Interface).


```go
func (*UniqueNodeLabelStrategy) PrepareDependentObjects((ctx context.Context, node *v1.Node, client clientset.Interface)) (ctx context.Context, node *v1.Node, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:1037`



---


[function] name: PreparePatch file: test/utils/runners.go:814 returns_error: нет description: —


### PreparePatch (test/utils/runners.go:814)


PreparePatch is a method that performs operations based on the provided parameters and returns (*v1.Node).


```go
func (*TrivialNodePrepareStrategy) PreparePatch((*v1.Node)) (*v1.Node)
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


📍 *Расположение:* `test/utils/runners.go:814`



---


[function] name: PreparePatch file: test/utils/runners.go:846 returns_error: нет description: —


### PreparePatch (test/utils/runners.go:846)


PreparePatch is a method that performs operations based on the provided parameters and returns (*v1.Node).


```go
func (s *LabelNodePrepareStrategy) PreparePatch((*v1.Node)) (*v1.Node)
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


📍 *Расположение:* `test/utils/runners.go:846`



---


[function] name: PreparePatch file: test/utils/runners.go:894 returns_error: нет description: —


### PreparePatch (test/utils/runners.go:894)


PreparePatch is a method that performs operations based on the provided parameters and returns (node *v1.Node).


```go
func (s *NodeAllocatableStrategy) PreparePatch((node *v1.Node)) (node *v1.Node)
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


📍 *Расположение:* `test/utils/runners.go:894`



---


[function] name: PreparePatch file: test/utils/runners.go:1023 returns_error: нет description: —


### PreparePatch (test/utils/runners.go:1023)


PreparePatch is a method that performs operations based on the provided parameters and returns (*v1.Node).


```go
func (s *UniqueNodeLabelStrategy) PreparePatch((*v1.Node)) (*v1.Node)
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


📍 *Расположение:* `test/utils/runners.go:1023`



---


[function] name: RCConfigLog file: test/utils/runners.go:182 returns_error: нет description: —


### RCConfigLog (test/utils/runners.go:182)


RCConfigLog is a method that performs operations based on the provided parameters and returns (fmt string, args ...interface{}).


```go
func (rc *RCConfig) RCConfigLog((fmt string, args ...interface{})) (fmt string, args ...interface{})
```


**Тип ответа:** fmt


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/utils/runners.go:182`



---


[function] name: RunDeployment file: test/utils/runners.go:284 returns_error: нет description: RunDeployment Launches (and verifies correctness) of a Deployment
and will wait for all pods it spawns to become "Runnin


### RunDeployment (test/utils/runners.go:284)


RunDeployment Launches (and verifies correctness) of a Deployment
and will wait for all pods it spawns to become "Running".
It's the caller's responsibility to clean up externally (i.e. use the
namespace lifecycle for handling Cleanup).


```go
func RunDeployment((ctx context.Context, config DeploymentConfig)) (ctx context.Context, config DeploymentConfig)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** DeploymentConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:284`



---


[function] name: RunPodAndGetNodeName file: test/utils/runners.go:74 returns_error: да description: —


### RunPodAndGetNodeName (test/utils/runners.go:74)


RunPodAndGetNodeName is a function that performs operations based on the provided parameters and may return an error.


```go
func RunPodAndGetNodeName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/utils/runners.go:74`



---


[function] name: RunRC file: test/utils/runners.go:430 returns_error: нет description: RunRC Launches (and verifies correctness) of a Replication Controller
and will wait for all pods it spawns to become "Ru


### RunRC (test/utils/runners.go:430)


RunRC Launches (and verifies correctness) of a Replication Controller
and will wait for all pods it spawns to become "Running".
It's the caller's responsibility to clean up externally (i.e. use the
namespace lifecycle for handling Cleanup).


```go
func RunRC((ctx context.Context, config RCConfig)) (ctx context.Context, config RCConfig)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** RCConfig


```json
{
  "Affinity": null,
  "Client": {},
  "ScalesGetter": {},
  "Image": "string",
  "Command": [],
  "Name": "string",
  "Namespace": "string",
  "PollInterval": {},
  "Timeout": {},
  "PodStatusFile": null,
  "Replicas": 0,
  "CPURequest": 0,
  "CPULimit": 0,
  "MemRequest": 0,
  "MemLimit": 0,
  "GpuLimit": 0,
  "PodResources": null,
  "ReadinessProbe": null,
  "DNSPolicy": null,
  "PriorityClassName": "string",
  "TerminationGracePeriodSeconds": 0,
  "Lifecycle": null,
  "SchedulerName": "string",
  "Env": {},
  "Labels": {},
  "Annotations": {},
  "NodeSelector": {},
  "Tolerations": [],
  "Ports": {},
  "HostPorts": {},
  "Volumes": [],
  "VolumeMounts": [],
  "CreatedPods": null,
  "MaxContainerFailures": 0,
  "MaxAllowedPodDeletions": 0,
  "Silent": false,
  "LogFunc": {},
  "NodeDumpFunc": {},
  "ContainerDumpFunc": {},
  "SecretNames": [],
  "ConfigMapNames": [],
  "ServiceAccountTokenProjections": 0,
  "AdditionalContainers": [],
  "SecurityContext": null
}
```


*Определено в:* `test/utils/runners.go`


📍 *Расположение:* `test/utils/runners.go:430`



---


[function] name: RunReplicaSet file: test/utils/runners.go:359 returns_error: нет description: RunReplicaSet launches (and verifies correctness) of a ReplicaSet
and waits until all the pods it launches to reach the 


### RunReplicaSet (test/utils/runners.go:359)


RunReplicaSet launches (and verifies correctness) of a ReplicaSet
and waits until all the pods it launches to reach the "Running" state.
It's the caller's responsibility to clean up externally (i.e. use the
namespace lifecycle for handling Cleanup).


```go
func RunReplicaSet((ctx context.Context, config ReplicaSetConfig)) (ctx context.Context, config ReplicaSetConfig)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** ReplicaSetConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:359`



---


[function] name: StartPods file: test/utils/runners.go:730 returns_error: нет description: Simplified version of RunRC, that does not create RC, but creates plain Pods.
Optionally waits for pods to start running


### StartPods (test/utils/runners.go:730)


Simplified version of RunRC, that does not create RC, but creates plain Pods.
Optionally waits for pods to start running (if waitForRunning == true).
The number of replicas must be non-zero.


```go
func StartPods((c clientset.Interface, replicas int, namespace string, podNamePrefix string,
	pod v1.Pod, waitForRunning bool, logFunc func(fmt string, args ...interface{}))) (c clientset.Interface, replicas int, namespace string, podNamePrefix string,
	pod v1.Pod, waitForRunning bool, logFunc func(fmt string, args ...interface{}))
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


**Тип ответа:** replicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podNamePrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** waitForRunning


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fmt


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/utils/runners.go:730`



---


[function] name: StaticPodTemplate file: test/utils/runners.go:1310 returns_error: нет description: StaticPodTemplate returns an implementation of PodTemplate for a fixed pod that is the same regardless of the index.


### StaticPodTemplate (test/utils/runners.go:1310)


StaticPodTemplate returns an implementation of PodTemplate for a fixed pod that is the same regardless of the index.


```go
func StaticPodTemplate((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `test/utils/runners.go:1310`



---


[function] name: String file: test/utils/runners.go:213 returns_error: нет description: Print formats and prints the give podDiff.


### String (test/utils/runners.go:213)


Print formats and prints the give podDiff.


```go
func (p podDiff) String((ignorePhases sets.String)) (ignorePhases sets.String)
```


**Тип ответа:** ignorePhases


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.String


```json
{
  "ID": "string",
  "Secret": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/bootstraptoken/v1/types.go`


📍 *Расположение:* `test/utils/runners.go:213`



---


[function] name: String file: test/utils/runners.go:579 returns_error: нет description: —


### String (test/utils/runners.go:579)


String is a method that performs operations based on the provided parameters and returns (name string).


```go
func (s *RCStartupStatus) String((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/utils/runners.go:579`



---


[function] name: WaitForEnoughPodsWithLabelRunning file: test/utils/runners.go:766 returns_error: нет description: Wait up to 10 minutes for at least 'replicas' many pods to be Running and at least
one matching pod exists. If 'replicas


### WaitForEnoughPodsWithLabelRunning (test/utils/runners.go:766)


Wait up to 10 minutes for at least 'replicas' many pods to be Running and at least
one matching pod exists. If 'replicas' is < 0, wait for all matching pods running.


```go
func WaitForEnoughPodsWithLabelRunning((c clientset.Interface, ns string, label labels.Selector, replicas int)) (c clientset.Interface, ns string, label labels.Selector, replicas int)
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


**Тип ответа:** label


```json
{
  "parts": [],
  "explanation": "string",
  "alphaBetaLevel": "string",
  "offByDefault": false
}
```


*Определено в:* `test/e2e/framework/ginkgowrapper.go`


**Тип ответа:** labels.Selector


```json
{
  "Client": {},
  "Mapping": null,
  "Namespace": "string",
  "LabelSelector": "string",
  "FieldSelector": "string",
  "LimitChunks": 0
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/selector.go`


**Тип ответа:** replicas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:766`



---


[function] name: WaitForPodsWithLabelRunning file: test/utils/runners.go:760 returns_error: нет description: Wait up to 10 minutes for all matching pods to become Running and at least one
matching pod exists.


### WaitForPodsWithLabelRunning (test/utils/runners.go:760)


Wait up to 10 minutes for all matching pods to become Running and at least one
matching pod exists.


```go
func WaitForPodsWithLabelRunning((c clientset.Interface, ns string, label labels.Selector)) (c clientset.Interface, ns string, label labels.Selector)
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


**Тип ответа:** label


```json
{
  "parts": [],
  "explanation": "string",
  "alphaBetaLevel": "string",
  "offByDefault": false
}
```


*Определено в:* `test/e2e/framework/ginkgowrapper.go`


**Тип ответа:** labels.Selector


```json
{
  "Client": {},
  "Mapping": null,
  "Namespace": "string",
  "LabelSelector": "string",
  "FieldSelector": "string",
  "LimitChunks": 0
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/selector.go`


📍 *Расположение:* `test/utils/runners.go:760`



---


[function] name: applyTo file: test/utils/runners.go:506 returns_error: нет description: —


### applyTo (test/utils/runners.go:506)


applyTo is a method that performs operations based on the provided parameters and returns (template *v1.PodTemplateSpec).


```go
func (config *RCConfig) applyTo((template *v1.PodTemplateSpec)) (template *v1.PodTemplateSpec)
```


**Тип запроса:** v1.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** template


```json
{
  "UsageTemplate": "string",
  "HelpTemplate": "string",
  "RootCmd": null,
  "Filtered": []
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/util/templates/templater.go`


**Тип ответа:** v1.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `test/utils/runners.go:506`



---


[function] name: attachConfigMaps file: test/utils/runners.go:1352 returns_error: нет description: TODO: attach configmaps using different possibilities: env vars.


### attachConfigMaps (test/utils/runners.go:1352)


TODO: attach configmaps using different possibilities: env vars.


```go
func attachConfigMaps((template *v1.PodTemplateSpec, configMapNames []string)) (template *v1.PodTemplateSpec, configMapNames []string)
```


**Тип запроса:** v1.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** template


```json
{
  "UsageTemplate": "string",
  "HelpTemplate": "string",
  "RootCmd": null,
  "Filtered": []
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/util/templates/templater.go`


**Тип ответа:** v1.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** configMapNames


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:1352`



---


[function] name: attachSecrets file: test/utils/runners.go:1329 returns_error: нет description: TODO: attach secrets using different possibilities: env vars, image pull secrets.


### attachSecrets (test/utils/runners.go:1329)


TODO: attach secrets using different possibilities: env vars, image pull secrets.


```go
func attachSecrets((template *v1.PodTemplateSpec, secretNames []string)) (template *v1.PodTemplateSpec, secretNames []string)
```


**Тип запроса:** v1.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** template


```json
{
  "UsageTemplate": "string",
  "HelpTemplate": "string",
  "RootCmd": null,
  "Filtered": []
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/util/templates/templater.go`


**Тип ответа:** v1.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** secretNames


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:1329`



---


[function] name: attachServiceAccountTokenProjection file: test/utils/runners.go:1383 returns_error: нет description: —


### attachServiceAccountTokenProjection (test/utils/runners.go:1383)


attachServiceAccountTokenProjection is a function that performs operations based on the provided parameters and returns (template *v1.PodTemplateSpec, name string).


```go
func attachServiceAccountTokenProjection((template *v1.PodTemplateSpec, name string)) (template *v1.PodTemplateSpec, name string)
```


**Тип запроса:** v1.PodTemplateSpec


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** template


```json
{
  "UsageTemplate": "string",
  "HelpTemplate": "string",
  "RootCmd": null,
  "Filtered": []
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/util/templates/templater.go`


**Тип ответа:** v1.PodTemplateSpec


```json
{
  "Spec": {}
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


📍 *Расположение:* `test/utils/runners.go:1383`



---


[function] name: computeRCStartupStatus file: test/utils/runners.go:584 returns_error: нет description: —


### computeRCStartupStatus (test/utils/runners.go:584)


computeRCStartupStatus is a function that performs operations based on the provided parameters and returns (pods []*v1.Pod, expected int).


```go
func computeRCStartupStatus((pods []*v1.Pod, expected int)) (pods []*v1.Pod, expected int)
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


**Тип ответа:** expected


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/errors/errors.go`


📍 *Расположение:* `test/utils/runners.go:584`



---


[function] name: create file: test/utils/runners.go:292 returns_error: нет description: —


### create (test/utils/runners.go:292)


create is a method that performs operations based on the provided parameters and returns ().


```go
func (config *DeploymentConfig) create(()) ()
```


📍 *Расположение:* `test/utils/runners.go:292`



---


[function] name: create file: test/utils/runners.go:367 returns_error: нет description: —


### create (test/utils/runners.go:367)


create is a method that performs operations based on the provided parameters and returns ().


```go
func (config *ReplicaSetConfig) create(()) ()
```


📍 *Расположение:* `test/utils/runners.go:367`



---


[function] name: create file: test/utils/runners.go:438 returns_error: нет description: —


### create (test/utils/runners.go:438)


create is a method that performs operations based on the provided parameters and returns ().


```go
func (config *RCConfig) create(()) ()
```


📍 *Расположение:* `test/utils/runners.go:438`



---


[function] name: createCSINode file: test/utils/runners.go:924 returns_error: нет description: —


### createCSINode (test/utils/runners.go:924)


createCSINode is a method that performs operations based on the provided parameters and returns (ctx context.Context, nodeName string, client clientset.Interface).


```go
func (s *NodeAllocatableStrategy) createCSINode((ctx context.Context, nodeName string, client clientset.Interface)) (ctx context.Context, nodeName string, client clientset.Interface)
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


📍 *Расположение:* `test/utils/runners.go:924`



---


[function] name: diff file: test/utils/runners.go:261 returns_error: нет description: diff computes a podDiff given 2 lists of pods.


### diff (test/utils/runners.go:261)


diff computes a podDiff given 2 lists of pods.


```go
func diff((oldPods []*v1.Pod, curPods []*v1.Pod)) (oldPods []*v1.Pod, curPods []*v1.Pod)
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


**Тип ответа:** oldPods


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


**Тип ответа:** curPods


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


📍 *Расположение:* `test/utils/runners.go:261`



---


[function] name: getTerminationGracePeriodSeconds file: test/utils/runners.go:1376 returns_error: нет description: —


### getTerminationGracePeriodSeconds (test/utils/runners.go:1376)


getTerminationGracePeriodSeconds is a method that performs operations based on the provided parameters and returns (defaultGrace *int64).


```go
func (config *RCConfig) getTerminationGracePeriodSeconds((defaultGrace *int64)) (defaultGrace *int64)
```


**Тип ответа:** defaultGrace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/runners.go:1376`



---


[function] name: makeCreatePod file: test/utils/runners.go:1152 returns_error: нет description: —


### makeCreatePod (test/utils/runners.go:1152)


makeCreatePod is a function that performs operations based on the provided parameters and returns (client clientset.Interface, namespace string, podTemplate *v1.Pod).


```go
func makeCreatePod((client clientset.Interface, namespace string, podTemplate *v1.Pod)) (client clientset.Interface, namespace string, podTemplate *v1.Pod)
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


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podTemplate


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/podtemplate.go`


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


📍 *Расположение:* `test/utils/runners.go:1152`



---


[function] name: start file: test/utils/runners.go:633 returns_error: нет description: —


### start (test/utils/runners.go:633)


start is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (config *RCConfig) start((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/utils/runners.go:633`



---


[function] name: updateCSINode file: test/utils/runners.go:955 returns_error: нет description: —


### updateCSINode (test/utils/runners.go:955)


updateCSINode is a method that performs operations based on the provided parameters and returns (ctx context.Context, csiNode *storagev1.CSINode, client clientset.Interface).


```go
func (s *NodeAllocatableStrategy) updateCSINode((ctx context.Context, csiNode *storagev1.CSINode, client clientset.Interface)) (ctx context.Context, csiNode *storagev1.CSINode, client clientset.Interface)
```


**Тип запроса:** storagev1.CSINode


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/storage/types.go`


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


**Тип ответа:** csiNode


```json
{
  "csiNodeLister": {}
}
```


*Определено в:* `pkg/scheduler/framework/plugins/nodevolumelimits/csi_manager.go`


**Тип ответа:** storagev1.CSINode


```json
{
  "Spec": {}
}
```


*Определено в:* `pkg/apis/storage/types.go`


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


📍 *Расположение:* `test/utils/runners.go:955`



---


[function] name: waitUntilPodIsScheduled file: test/utils/runners.go:56 returns_error: да description: —


### waitUntilPodIsScheduled (test/utils/runners.go:56)


waitUntilPodIsScheduled is a function that performs operations based on the provided parameters and may return an error.


```go
func waitUntilPodIsScheduled((*v1.Pod, error)) (*v1.Pod, error)
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


📍 *Расположение:* `test/utils/runners.go:56`




## test/utils/tmpdir.go


📄 Исходный файл: `test/utils/tmpdir.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [MakeTempDirOrDie](#maketempdirordie-testutilstmpdirgo25) `:25`


</details>


[function] name: MakeTempDirOrDie file: test/utils/tmpdir.go:25 returns_error: нет description: —


### MakeTempDirOrDie (test/utils/tmpdir.go:25)


MakeTempDirOrDie is a function that performs operations based on the provided parameters and returns (prefix string, baseDir string).


```go
func MakeTempDirOrDie((prefix string, baseDir string)) (prefix string, baseDir string)
```


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


**Тип ответа:** baseDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/tmpdir.go:25`




## test/utils/update_resources.go


📄 Исходный файл: `test/utils/update_resources.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [RetryErrorCondition](#retryerrorcondition-testutilsupdate_resourcesgo39) `:39`

- 🔗 [ScaleResourceWithRetries](#scaleresourcewithretries-testutilsupdate_resourcesgo46) `:46`


</details>


[function] name: RetryErrorCondition file: test/utils/update_resources.go:39 returns_error: нет description: —


### RetryErrorCondition (test/utils/update_resources.go:39)


RetryErrorCondition is a function that performs operations based on the provided parameters and returns (condition wait.ConditionWithContextFunc).


```go
func RetryErrorCondition((condition wait.ConditionWithContextFunc)) (condition wait.ConditionWithContextFunc)
```


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** wait.ConditionWithContextFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/utils/update_resources.go:39`



---


[function] name: ScaleResourceWithRetries file: test/utils/update_resources.go:46 returns_error: нет description: —


### ScaleResourceWithRetries (test/utils/update_resources.go:46)


ScaleResourceWithRetries is a function that performs operations based on the provided parameters and returns (scalesGetter scaleclient.ScalesGetter, namespace, name string, size uint, gvr schema.GroupVersionResource).


```go
func ScaleResourceWithRetries((scalesGetter scaleclient.ScalesGetter, namespace, name string, size uint, gvr schema.GroupVersionResource)) (scalesGetter scaleclient.ScalesGetter, namespace, name string, size uint, gvr schema.GroupVersionResource)
```


**Тип ответа:** scalesGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** scaleclient.ScalesGetter


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


**Тип ответа:** size


```json
{
  "ResourceName": null,
  "RestartPolicy": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/containerresizepolicy.go`


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


📍 *Расположение:* `test/utils/update_resources.go:46`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_typecheck.md)


---

