---
title: "Функции: test/e2e_kubeadm"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/e2e_kubeadm
---


# Функции: test/e2e_kubeadm


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_e2e.md)

- [Следующая директория](test_e2e_node.md)


---


## Меню по файлам


- 📄 [test/e2e_kubeadm/framework.go](#teste2e_kubeadmframeworkgo)

- 📄 [test/e2e_kubeadm/util.go](#teste2e_kubeadmutilgo)


---


## test/e2e_kubeadm/framework.go


📄 Исходный файл: `test/e2e_kubeadm/framework.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Describe](#describe-teste2e_kubeadmframeworkgo22) `:22`


</details>


[function] name: Describe file: test/e2e_kubeadm/framework.go:22 returns_error: нет description: Describe annotates the test with the Kubeadm label.


### Describe (test/e2e_kubeadm/framework.go:22)


Describe annotates the test with the Kubeadm label.


```go
func Describe((text string, body func())) (text string, body func())
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


**Тип ответа:** body


```json
{
  "locator": {},
  "localPackage": {},
  "omitGogo": false,
  "omitFieldTypes": {},
  "t": null
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/go-to-protobuf/protobuf/generator.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_kubeadm/framework.go:22`




## test/e2e_kubeadm/util.go


📄 Исходный файл: `test/e2e_kubeadm/util.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [ExpectClusterRole](#expectclusterrole-teste2e_kubeadmutilgo117) `:117`

- 🔗 [ExpectClusterRoleBinding](#expectclusterrolebinding-teste2e_kubeadmutilgo125) `:125`

- 🔗 [ExpectClusterRoleBindingWithSubjectAndRole](#expectclusterrolebindingwithsubjectandrole-teste2e_kubeadmutilgo133) `:133`

- 🔗 [ExpectRole](#expectrole-teste2e_kubeadmutilgo101) `:101`

- 🔗 [ExpectRoleBinding](#expectrolebinding-teste2e_kubeadmutilgo109) `:109`

- 🔗 [ExpectService](#expectservice-teste2e_kubeadmutilgo69) `:69`

- 🔗 [ExpectServiceAccount](#expectserviceaccount-teste2e_kubeadmutilgo37) `:37`

- 🔗 [ExpectSubjectHasAccessToResource](#expectsubjecthasaccesstoresource-teste2e_kubeadmutilgo152) `:152`

- 🔗 [GetConfigMap](#getconfigmap-teste2e_kubeadmutilgo58) `:58`

- 🔗 [GetDaemonSet](#getdaemonset-teste2e_kubeadmutilgo90) `:90`

- 🔗 [GetDeployment](#getdeployment-teste2e_kubeadmutilgo79) `:79`

- 🔗 [GetSecret](#getsecret-teste2e_kubeadmutilgo47) `:47`

- 🔗 [subjectMatcher](#subjectmatcher-teste2e_kubeadmutilgo183) `:183`


</details>


[function] name: ExpectClusterRole file: test/e2e_kubeadm/util.go:117 returns_error: нет description: ExpectClusterRole expects to be able to get the ClusterRole with specific name


### ExpectClusterRole (test/e2e_kubeadm/util.go:117)


ExpectClusterRole expects to be able to get the ClusterRole with specific name


```go
func ExpectClusterRole((c clientset.Interface, name string)) (c clientset.Interface, name string)
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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/e2e_kubeadm/util.go:117`



---


[function] name: ExpectClusterRoleBinding file: test/e2e_kubeadm/util.go:125 returns_error: нет description: ExpectClusterRoleBinding expects to be able to get the ClusterRoleBinding with specific name


### ExpectClusterRoleBinding (test/e2e_kubeadm/util.go:125)


ExpectClusterRoleBinding expects to be able to get the ClusterRoleBinding with specific name


```go
func ExpectClusterRoleBinding((c clientset.Interface, name string)) (c clientset.Interface, name string)
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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/e2e_kubeadm/util.go:125`



---


[function] name: ExpectClusterRoleBindingWithSubjectAndRole file: test/e2e_kubeadm/util.go:133 returns_error: нет description: ExpectClusterRoleBindingWithSubjectAndRole expects to be able to get the ClusterRoleBinding with specific name, subject 


### ExpectClusterRoleBindingWithSubjectAndRole (test/e2e_kubeadm/util.go:133)


ExpectClusterRoleBindingWithSubjectAndRole expects to be able to get the ClusterRoleBinding with specific name, subject and role


```go
func ExpectClusterRoleBindingWithSubjectAndRole((c clientset.Interface, name, subjectKind, subject, role string)) (c clientset.Interface, name, subjectKind, subject, role string)
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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** subjectKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** subject


```json
{
  "client": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook.go`


**Тип ответа:** role


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/rbac/v1alpha1/role.go`


📍 *Расположение:* `test/e2e_kubeadm/util.go:133`



---


[function] name: ExpectRole file: test/e2e_kubeadm/util.go:101 returns_error: нет description: ExpectRole expects to be able to get the Role with specific name from the namespace


### ExpectRole (test/e2e_kubeadm/util.go:101)


ExpectRole expects to be able to get the Role with specific name from the namespace


```go
func ExpectRole((c clientset.Interface, namespace, name string)) (c clientset.Interface, namespace, name string)
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


📍 *Расположение:* `test/e2e_kubeadm/util.go:101`



---


[function] name: ExpectRoleBinding file: test/e2e_kubeadm/util.go:109 returns_error: нет description: ExpectRoleBinding expects to be able to get the RoleBinding with specific name from the namespace


### ExpectRoleBinding (test/e2e_kubeadm/util.go:109)


ExpectRoleBinding expects to be able to get the RoleBinding with specific name from the namespace


```go
func ExpectRoleBinding((c clientset.Interface, namespace, name string)) (c clientset.Interface, namespace, name string)
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


📍 *Расположение:* `test/e2e_kubeadm/util.go:109`



---


[function] name: ExpectService file: test/e2e_kubeadm/util.go:69 returns_error: нет description: ExpectService expects to be able to get the Service with specific name from the namespace


### ExpectService (test/e2e_kubeadm/util.go:69)


ExpectService expects to be able to get the Service with specific name from the namespace


```go
func ExpectService((c clientset.Interface, namespace, name string)) (c clientset.Interface, namespace, name string)
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


📍 *Расположение:* `test/e2e_kubeadm/util.go:69`



---


[function] name: ExpectServiceAccount file: test/e2e_kubeadm/util.go:37 returns_error: нет description: ExpectServiceAccount expects to be able to get the ServiceAccount with specific name from the namespace


### ExpectServiceAccount (test/e2e_kubeadm/util.go:37)


ExpectServiceAccount expects to be able to get the ServiceAccount with specific name from the namespace


```go
func ExpectServiceAccount((c clientset.Interface, namespace, name string)) (c clientset.Interface, namespace, name string)
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


📍 *Расположение:* `test/e2e_kubeadm/util.go:37`



---


[function] name: ExpectSubjectHasAccessToResource file: test/e2e_kubeadm/util.go:152 returns_error: нет description: ExpectSubjectHasAccessToResource expects that the subject has access to the target resource


### ExpectSubjectHasAccessToResource (test/e2e_kubeadm/util.go:152)


ExpectSubjectHasAccessToResource expects that the subject has access to the target resource


```go
func ExpectSubjectHasAccessToResource((c clientset.Interface, subjectKind, subject string, resource *authv1.ResourceAttributes)) (c clientset.Interface, subjectKind, subject string, resource *authv1.ResourceAttributes)
```


**Тип запроса:** authv1.ResourceAttributes


```json
{
  "Namespace": "string",
  "Verb": "string",
  "Group": "string",
  "Version": "string",
  "Resource": "string",
  "Subresource": "string",
  "Name": "string",
  "FieldSelector": null,
  "LabelSelector": null
}
```


*Определено в:* `pkg/apis/authorization/types.go`


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


**Тип ответа:** subjectKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** subject


```json
{
  "client": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook.go`


**Тип ответа:** resource


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/resourcequota.go`


**Тип ответа:** authv1.ResourceAttributes


```json
{
  "Namespace": "string",
  "Verb": "string",
  "Group": "string",
  "Version": "string",
  "Resource": "string",
  "Subresource": "string",
  "Name": "string",
  "FieldSelector": null,
  "LabelSelector": null
}
```


*Определено в:* `pkg/apis/authorization/types.go`


📍 *Расположение:* `test/e2e_kubeadm/util.go:152`



---


[function] name: GetConfigMap file: test/e2e_kubeadm/util.go:58 returns_error: нет description: GetConfigMap gets ConfigMap with specific name from the namespace


### GetConfigMap (test/e2e_kubeadm/util.go:58)


GetConfigMap gets ConfigMap with specific name from the namespace


```go
func GetConfigMap((c clientset.Interface, namespace, name string)) (c clientset.Interface, namespace, name string)
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


📍 *Расположение:* `test/e2e_kubeadm/util.go:58`



---


[function] name: GetDaemonSet file: test/e2e_kubeadm/util.go:90 returns_error: нет description: GetDaemonSet gets DaemonSet with specific name from the namespace


### GetDaemonSet (test/e2e_kubeadm/util.go:90)


GetDaemonSet gets DaemonSet with specific name from the namespace


```go
func GetDaemonSet((c clientset.Interface, namespace, name string)) (c clientset.Interface, namespace, name string)
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


📍 *Расположение:* `test/e2e_kubeadm/util.go:90`



---


[function] name: GetDeployment file: test/e2e_kubeadm/util.go:79 returns_error: нет description: GetDeployment gets Deployment with specific name from the namespace


### GetDeployment (test/e2e_kubeadm/util.go:79)


GetDeployment gets Deployment with specific name from the namespace


```go
func GetDeployment((c clientset.Interface, namespace, name string)) (c clientset.Interface, namespace, name string)
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


📍 *Расположение:* `test/e2e_kubeadm/util.go:79`



---


[function] name: GetSecret file: test/e2e_kubeadm/util.go:47 returns_error: нет description: GetSecret gets Secret with specific name from the namespace


### GetSecret (test/e2e_kubeadm/util.go:47)


GetSecret gets Secret with specific name from the namespace


```go
func GetSecret((c clientset.Interface, namespace, name string)) (c clientset.Interface, namespace, name string)
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


📍 *Расположение:* `test/e2e_kubeadm/util.go:47`



---


[function] name: subjectMatcher file: test/e2e_kubeadm/util.go:183 returns_error: нет description: matchers


### subjectMatcher (test/e2e_kubeadm/util.go:183)


matchers


```go
func subjectMatcher((name, kind string)) (name, kind string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** kind


```json
{
  "restMapping": null
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/apply/applyset.go`


📍 *Расположение:* `test/e2e_kubeadm/util.go:183`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_e2e.md)

- [Следующая директория](test_e2e_node.md)


---

