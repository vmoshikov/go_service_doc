---
title: "Функции: pkg/kubemark"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/kubemark
---


# Функции: pkg/kubemark


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_kubelet.md)

- [Следующая директория](pkg_printers.md)


---


## Меню по файлам


- 📄 [pkg/kubemark/controller.go](#pkgkubemarkcontrollergo)

- 📄 [pkg/kubemark/hollow_kubelet.go](#pkgkubemarkhollow_kubeletgo)


---


## pkg/kubemark/controller.go


📄 Исходный файл: `pkg/kubemark/controller.go`


<details open>
<summary><b>Функции в этом файле (20)</b></summary>


- 🔗 [GetNodeGroupForNode](#getnodegroupfornode-pkgkubemarkcontrollergo210) `:210`

- 🔗 [GetNodeGroupSize](#getnodegroupsize-pkgkubemarkcontrollergo151) `:151`

- 🔗 [GetNodeGroupTargetSize](#getnodegrouptargetsize-pkgkubemarkcontrollergo162) `:162`

- 🔗 [GetNodeNamesForNodeGroup](#getnodenamesfornodegroup-pkgkubemarkcontrollergo137) `:137`

- 🔗 [NewKubemarkController](#newkubemarkcontroller-pkgkubemarkcontrollergo83) `:83`

- 🔗 [RemoveNodeFromNodeGroup](#removenodefromnodegroup-pkgkubemarkcontrollergo239) `:239`

- 🔗 [Run](#run-pkgkubemarkcontrollergo125) `:125`

- 🔗 [SetNodeGroupSize](#setnodegroupsize-pkgkubemarkcontrollergo173) `:173`

- 🔗 [WaitForCacheSync](#waitforcachesync-pkgkubemarkcontrollergo116) `:116`

- 🔗 [addNodeToNodeGroup](#addnodetonodegroup-pkgkubemarkcontrollergo222) `:222`

- 🔗 [getHollowNodeName](#gethollownodename-pkgkubemarkcontrollergo353) `:353`

- 🔗 [getNodeNameForPod](#getnodenameforpod-pkgkubemarkcontrollergo293) `:293`

- 🔗 [getNodeTemplate](#getnodetemplate-pkgkubemarkcontrollergo309) `:309`

- 🔗 [getPodByName](#getpodbyname-pkgkubemarkcontrollergo280) `:280`

- 🔗 [getReplicationControllerByName](#getreplicationcontrollerbyname-pkgkubemarkcontrollergo267) `:267`

- 🔗 [markNodeForDeletion](#marknodefordeletion-pkgkubemarkcontrollergo387) `:387`

- 🔗 [newPodInformer](#newpodinformer-pkgkubemarkcontrollergo398) `:398`

- 🔗 [newReplicationControllerInformer](#newreplicationcontrollerinformer-pkgkubemarkcontrollergo393) `:393`

- 🔗 [removeUnneededNodes](#removeunneedednodes-pkgkubemarkcontrollergo365) `:365`

- 🔗 [runNodeCreation](#runnodecreation-pkgkubemarkcontrollergo335) `:335`


</details>


[function] name: GetNodeGroupForNode file: pkg/kubemark/controller.go:210 returns_error: да description: GetNodeGroupForNode returns the name of the node group to which the node
belongs.


### GetNodeGroupForNode (pkg/kubemark/controller.go:210)


GetNodeGroupForNode returns the name of the node group to which the node
belongs.


```go
func (kubemarkController *KubemarkController) GetNodeGroupForNode((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubemark/controller.go:210`



---


[function] name: GetNodeGroupSize file: pkg/kubemark/controller.go:151 returns_error: да description: GetNodeGroupSize returns the current size for the node group as observed.


### GetNodeGroupSize (pkg/kubemark/controller.go:151)


GetNodeGroupSize returns the current size for the node group as observed.


```go
func (kubemarkController *KubemarkController) GetNodeGroupSize((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubemark/controller.go:151`



---


[function] name: GetNodeGroupTargetSize file: pkg/kubemark/controller.go:162 returns_error: да description: GetNodeGroupTargetSize returns the size of the node group as a sum of current
observed size and number of upcoming nodes


### GetNodeGroupTargetSize (pkg/kubemark/controller.go:162)


GetNodeGroupTargetSize returns the size of the node group as a sum of current
observed size and number of upcoming nodes.


```go
func (kubemarkController *KubemarkController) GetNodeGroupTargetSize((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubemark/controller.go:162`



---


[function] name: GetNodeNamesForNodeGroup file: pkg/kubemark/controller.go:137 returns_error: да description: GetNodeNamesForNodeGroup returns list of the nodes in the node group.


### GetNodeNamesForNodeGroup (pkg/kubemark/controller.go:137)


GetNodeNamesForNodeGroup returns list of the nodes in the node group.


```go
func (kubemarkController *KubemarkController) GetNodeNamesForNodeGroup(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubemark/controller.go:137`



---


[function] name: NewKubemarkController file: pkg/kubemark/controller.go:83 returns_error: да description: NewKubemarkController creates KubemarkController using the provided clients to talk to external
and kubemark clusters.


### NewKubemarkController (pkg/kubemark/controller.go:83)


NewKubemarkController creates KubemarkController using the provided clients to talk to external
and kubemark clusters.


```go
func NewKubemarkController((*KubemarkController, error)) (*KubemarkController, error)
```


**Тип запроса:** KubemarkController


```json
{
  "nodeTemplate": null,
  "externalCluster": {},
  "kubemarkCluster": {},
  "rand": null,
  "createNodeQueue": {},
  "nodeGroupQueueSize": {},
  "nodeGroupQueueSizeLock": {}
}
```


*Определено в:* `pkg/kubemark/controller.go`


**Тип ответа:** KubemarkController


```json
{
  "nodeTemplate": null,
  "externalCluster": {},
  "kubemarkCluster": {},
  "rand": null,
  "createNodeQueue": {},
  "nodeGroupQueueSize": {},
  "nodeGroupQueueSizeLock": {}
}
```


*Определено в:* `pkg/kubemark/controller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*KubemarkController`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubemark/controller.go:83`



---


[function] name: RemoveNodeFromNodeGroup file: pkg/kubemark/controller.go:239 returns_error: нет description: —


### RemoveNodeFromNodeGroup (pkg/kubemark/controller.go:239)


RemoveNodeFromNodeGroup is a method that deletes data based on the provided parameters and returns (nodeGroup string, node string).


```go
func (kubemarkController *KubemarkController) RemoveNodeFromNodeGroup((nodeGroup string, node string)) (nodeGroup string, node string)
```


**Тип ответа:** nodeGroup


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


📍 *Расположение:* `pkg/kubemark/controller.go:239`



---


[function] name: Run file: pkg/kubemark/controller.go:125 returns_error: нет description: Run populates the node template needed for creation of kubemark nodes and
starts the worker routine for creating new nod


### Run (pkg/kubemark/controller.go:125)


Run populates the node template needed for creation of kubemark nodes and
starts the worker routine for creating new nodes.


```go
func (kubemarkController *KubemarkController) Run((stopCh chan struct{})) (stopCh chan struct{})
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


📍 *Расположение:* `pkg/kubemark/controller.go:125`



---


[function] name: SetNodeGroupSize file: pkg/kubemark/controller.go:173 returns_error: нет description: SetNodeGroupSize changes the size of node group by adding or removing nodes.


### SetNodeGroupSize (pkg/kubemark/controller.go:173)


SetNodeGroupSize changes the size of node group by adding or removing nodes.


```go
func (kubemarkController *KubemarkController) SetNodeGroupSize((nodeGroup string, size int)) (nodeGroup string, size int)
```


**Тип ответа:** nodeGroup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** size


```json
{
  "ResourceName": null,
  "RestartPolicy": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/containerresizepolicy.go`


📍 *Расположение:* `pkg/kubemark/controller.go:173`



---


[function] name: WaitForCacheSync file: pkg/kubemark/controller.go:116 returns_error: нет description: WaitForCacheSync waits until all caches in the controller are populated.


### WaitForCacheSync (pkg/kubemark/controller.go:116)


WaitForCacheSync waits until all caches in the controller are populated.


```go
func (kubemarkController *KubemarkController) WaitForCacheSync((stopCh chan struct{})) (stopCh chan struct{})
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


📍 *Расположение:* `pkg/kubemark/controller.go:116`



---


[function] name: addNodeToNodeGroup file: pkg/kubemark/controller.go:222 returns_error: нет description: —


### addNodeToNodeGroup (pkg/kubemark/controller.go:222)


addNodeToNodeGroup is a method that performs operations based on the provided parameters and returns (nodeGroup string).


```go
func (kubemarkController *KubemarkController) addNodeToNodeGroup((nodeGroup string)) (nodeGroup string)
```


**Тип ответа:** nodeGroup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/kubemark/controller.go:222`



---


[function] name: getHollowNodeName file: pkg/kubemark/controller.go:353 returns_error: да description: —


### getHollowNodeName (pkg/kubemark/controller.go:353)


getHollowNodeName is a method that performs operations based on the provided parameters and may return an error.


```go
func (kubemarkCluster *kubemarkCluster) getHollowNodeName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubemark/controller.go:353`



---


[function] name: getNodeNameForPod file: pkg/kubemark/controller.go:293 returns_error: да description: —


### getNodeNameForPod (pkg/kubemark/controller.go:293)


getNodeNameForPod is a method that performs operations based on the provided parameters and may return an error.


```go
func (kubemarkController *KubemarkController) getNodeNameForPod((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubemark/controller.go:293`



---


[function] name: getNodeTemplate file: pkg/kubemark/controller.go:309 returns_error: да description: getNodeTemplate returns the template for hollow node replication controllers
by looking for an existing hollow node spec


### getNodeTemplate (pkg/kubemark/controller.go:309)


getNodeTemplate returns the template for hollow node replication controllers
by looking for an existing hollow node specification. This requires at least
one kubemark node to be present on startup.


```go
func (kubemarkController *KubemarkController) getNodeTemplate((*apiv1.ReplicationController, error)) (*apiv1.ReplicationController, error)
```


**Тип запроса:** apiv1.ReplicationController


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** apiv1.ReplicationController


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apiv1.ReplicationController`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubemark/controller.go:309`



---


[function] name: getPodByName file: pkg/kubemark/controller.go:280 returns_error: нет description: —


### getPodByName (pkg/kubemark/controller.go:280)


getPodByName is a method that performs operations based on the provided parameters and returns (name string).


```go
func (kubemarkController *KubemarkController) getPodByName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/kubemark/controller.go:280`



---


[function] name: getReplicationControllerByName file: pkg/kubemark/controller.go:267 returns_error: нет description: —


### getReplicationControllerByName (pkg/kubemark/controller.go:267)


getReplicationControllerByName is a method that performs operations based on the provided parameters and returns (name string).


```go
func (kubemarkController *KubemarkController) getReplicationControllerByName((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/kubemark/controller.go:267`



---


[function] name: markNodeForDeletion file: pkg/kubemark/controller.go:387 returns_error: нет description: —


### markNodeForDeletion (pkg/kubemark/controller.go:387)


markNodeForDeletion is a method that performs operations based on the provided parameters and returns (name string).


```go
func (kubemarkCluster *kubemarkCluster) markNodeForDeletion((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/kubemark/controller.go:387`



---


[function] name: newPodInformer file: pkg/kubemark/controller.go:398 returns_error: нет description: —


### newPodInformer (pkg/kubemark/controller.go:398)


newPodInformer is a function that performs operations based on the provided parameters and returns (kubeClient kubeclient.Interface, resyncPeriod time.Duration).


```go
func newPodInformer((kubeClient kubeclient.Interface, resyncPeriod time.Duration)) (kubeClient kubeclient.Interface, resyncPeriod time.Duration)
```


**Тип ответа:** kubeClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeclient.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `pkg/kubemark/controller.go:398`



---


[function] name: newReplicationControllerInformer file: pkg/kubemark/controller.go:393 returns_error: нет description: —


### newReplicationControllerInformer (pkg/kubemark/controller.go:393)


newReplicationControllerInformer is a function that performs operations based on the provided parameters and returns (kubeClient kubeclient.Interface, resyncPeriod time.Duration).


```go
func newReplicationControllerInformer((kubeClient kubeclient.Interface, resyncPeriod time.Duration)) (kubeClient kubeclient.Interface, resyncPeriod time.Duration)
```


**Тип ответа:** kubeClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeclient.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `pkg/kubemark/controller.go:393`



---


[function] name: removeUnneededNodes file: pkg/kubemark/controller.go:365 returns_error: нет description: —


### removeUnneededNodes (pkg/kubemark/controller.go:365)


removeUnneededNodes is a method that performs operations based on the provided parameters and returns (oldObj interface{}, newObj interface{}).


```go
func (kubemarkCluster *kubemarkCluster) removeUnneededNodes((oldObj interface{}, newObj interface{})) (oldObj interface{}, newObj interface{})
```


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** newObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/kubemark/controller.go:365`



---


[function] name: runNodeCreation file: pkg/kubemark/controller.go:335 returns_error: нет description: —


### runNodeCreation (pkg/kubemark/controller.go:335)


runNodeCreation is a method that performs operations based on the provided parameters and returns (stop <-chan struct{}).


```go
func (kubemarkController *KubemarkController) runNodeCreation((stop <-chan struct{})) (stop <-chan struct{})
```


**Тип ответа:** stop


```json
{
  "Opcode": {}
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


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


📍 *Расположение:* `pkg/kubemark/controller.go:335`




## pkg/kubemark/hollow_kubelet.go


📄 Исходный файл: `pkg/kubemark/hollow_kubelet.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [GetHollowKubeletConfig](#gethollowkubeletconfig-pkgkubemarkhollow_kubeletgo146) `:146`

- 🔗 [NewHollowKubelet](#newhollowkubelet-pkgkubemarkhollow_kubeletgo85) `:85`

- 🔗 [Run](#run-pkgkubemarkhollow_kubeletgo123) `:123`

- 🔗 [volumePlugins](#volumeplugins-pkgkubemarkhollow_kubeletgo68) `:68`


</details>


[function] name: GetHollowKubeletConfig file: pkg/kubemark/hollow_kubelet.go:146 returns_error: нет description: Builds a KubeletConfiguration for the HollowKubelet, ensuring that the
usual defaults are applied for fields we do not o


### GetHollowKubeletConfig (pkg/kubemark/hollow_kubelet.go:146)


Builds a KubeletConfiguration for the HollowKubelet, ensuring that the
usual defaults are applied for fields we do not override.


```go
func GetHollowKubeletConfig((*options.KubeletFlags, *kubeletconfig.KubeletConfiguration)) (*options.KubeletFlags, *kubeletconfig.KubeletConfiguration)
```


**Тип запроса:** options.KubeletFlags


```json
{
  "KubeConfig": "string",
  "BootstrapKubeconfig": "string",
  "HostnameOverride": "string",
  "NodeIP": "string",
  "CertDirectory": "string",
  "CloudProvider": "string",
  "CloudConfigFile": "string",
  "RootDirectory": "string",
  "KubeletConfigFile": "string",
  "KubeletDropinConfigDirectory": "string",
  "WindowsService": false,
  "WindowsPriorityClass": "string",
  "ExperimentalMounterPath": "string",
  "ExperimentalNodeAllocatableIgnoreEvictionThreshold": false,
  "NodeLabels": {},
  "LockFilePath": "string",
  "ExitOnLockContention": false,
  "MinimumGCAge": {},
  "MaxPerPodContainerCount": 0,
  "MaxContainerCount": 0,
  "SeccompDefault": false
}
```


*Определено в:* `cmd/kubelet/app/options/options.go`


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** options.KubeletFlags


```json
{
  "KubeConfig": "string",
  "BootstrapKubeconfig": "string",
  "HostnameOverride": "string",
  "NodeIP": "string",
  "CertDirectory": "string",
  "CloudProvider": "string",
  "CloudConfigFile": "string",
  "RootDirectory": "string",
  "KubeletConfigFile": "string",
  "KubeletDropinConfigDirectory": "string",
  "WindowsService": false,
  "WindowsPriorityClass": "string",
  "ExperimentalMounterPath": "string",
  "ExperimentalNodeAllocatableIgnoreEvictionThreshold": false,
  "NodeLabels": {},
  "LockFilePath": "string",
  "ExitOnLockContention": false,
  "MinimumGCAge": {},
  "MaxPerPodContainerCount": 0,
  "MaxContainerCount": 0,
  "SeccompDefault": false
}
```


*Определено в:* `cmd/kubelet/app/options/options.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


📍 *Расположение:* `pkg/kubemark/hollow_kubelet.go:146`



---


[function] name: NewHollowKubelet file: pkg/kubemark/hollow_kubelet.go:85 returns_error: нет description: —


### NewHollowKubelet (pkg/kubemark/hollow_kubelet.go:85)


NewHollowKubelet is a function that performs operations based on the provided parameters and returns (
	flags *options.KubeletFlags,
	config *kubeletconfig.KubeletConfiguration,
	client *clientset.Clientset,
	heartbeatClient *clientset.Clientset,
	cadvisorInterface cadvisor.Interface,
	imageService internalapi.ImageManagerService,
	runtimeService internalapi.RuntimeService,
	containerManager cm.ContainerManager).


```go
func NewHollowKubelet((
	flags *options.KubeletFlags,
	config *kubeletconfig.KubeletConfiguration,
	client *clientset.Clientset,
	heartbeatClient *clientset.Clientset,
	cadvisorInterface cadvisor.Interface,
	imageService internalapi.ImageManagerService,
	runtimeService internalapi.RuntimeService,
	containerManager cm.ContainerManager)) (
	flags *options.KubeletFlags,
	config *kubeletconfig.KubeletConfiguration,
	client *clientset.Clientset,
	heartbeatClient *clientset.Clientset,
	cadvisorInterface cadvisor.Interface,
	imageService internalapi.ImageManagerService,
	runtimeService internalapi.RuntimeService,
	containerManager cm.ContainerManager)
```


**Тип запроса:** options.KubeletFlags


```json
{
  "KubeConfig": "string",
  "BootstrapKubeconfig": "string",
  "HostnameOverride": "string",
  "NodeIP": "string",
  "CertDirectory": "string",
  "CloudProvider": "string",
  "CloudConfigFile": "string",
  "RootDirectory": "string",
  "KubeletConfigFile": "string",
  "KubeletDropinConfigDirectory": "string",
  "WindowsService": false,
  "WindowsPriorityClass": "string",
  "ExperimentalMounterPath": "string",
  "ExperimentalNodeAllocatableIgnoreEvictionThreshold": false,
  "NodeLabels": {},
  "LockFilePath": "string",
  "ExitOnLockContention": false,
  "MinimumGCAge": {},
  "MaxPerPodContainerCount": 0,
  "MaxContainerCount": 0,
  "SeccompDefault": false
}
```


*Определено в:* `cmd/kubelet/app/options/options.go`


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип запроса:** clientset.Clientset


```json
{
  "discovery": null,
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/clientset/versioned/fake/clientset_generated.go`


**Тип запроса:** clientset.Clientset


```json
{
  "discovery": null,
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/clientset/versioned/fake/clientset_generated.go`


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options.KubeletFlags


```json
{
  "KubeConfig": "string",
  "BootstrapKubeconfig": "string",
  "HostnameOverride": "string",
  "NodeIP": "string",
  "CertDirectory": "string",
  "CloudProvider": "string",
  "CloudConfigFile": "string",
  "RootDirectory": "string",
  "KubeletConfigFile": "string",
  "KubeletDropinConfigDirectory": "string",
  "WindowsService": false,
  "WindowsPriorityClass": "string",
  "ExperimentalMounterPath": "string",
  "ExperimentalNodeAllocatableIgnoreEvictionThreshold": false,
  "NodeLabels": {},
  "LockFilePath": "string",
  "ExitOnLockContention": false,
  "MinimumGCAge": {},
  "MaxPerPodContainerCount": 0,
  "MaxContainerCount": 0,
  "SeccompDefault": false
}
```


*Определено в:* `cmd/kubelet/app/options/options.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


**Тип ответа:** clientset.Clientset


```json
{
  "discovery": null,
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/clientset/versioned/fake/clientset_generated.go`


**Тип ответа:** heartbeatClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientset.Clientset


```json
{
  "discovery": null,
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/clientset/versioned/fake/clientset_generated.go`


**Тип ответа:** cadvisorInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cadvisor.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** imageService


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


**Тип ответа:** internalapi.ImageManagerService


```json
{
  "service": {}
}
```


*Определено в:* `pkg/kubelet/kuberuntime/instrumented_services.go`


**Тип ответа:** runtimeService


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


**Тип ответа:** internalapi.RuntimeService


```json
{
  "Called": [],
  "Errors": {},
  "FakeStatus": null,
  "Containers": {},
  "Sandboxes": {},
  "FakeContainerStats": {},
  "FakePodSandboxStats": {},
  "FakePodSandboxMetrics": {},
  "FakeMetricDescriptors": {},
  "FakeContainerMetrics": {},
  "FakeLinuxConfiguration": null,
  "ErrorOnSandboxCreate": false
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/testing/fake_runtime_service.go`


**Тип ответа:** containerManager


```json
{
  "cadvisorInterface": {},
  "mountUtil": {},
  "status": {},
  "systemContainers": [],
  "periodicTasks": [],
  "subsystems": null,
  "nodeInfo": null,
  "cgroupManager": {},
  "capacity": {},
  "internalCapacity": {},
  "cgroupRoot": {},
  "recorder": {},
  "qosContainerManager": {},
  "deviceManager": {},
  "cpuManager": {},
  "memoryManager": {},
  "topologyManager": {},
  "draManager": null,
  "kubeClient": {},
  "resourceUpdates": {}
}
```


*Определено в:* `pkg/kubelet/cm/container_manager_linux.go`


**Тип ответа:** cm.ContainerManager


```json
{
  "qosContainersInfo": {},
  "subsystems": null,
  "cgroupManager": {},
  "activePods": {},
  "getNodeAllocatable": {},
  "cgroupRoot": {},
  "qosReserved": {}
}
```


*Определено в:* `pkg/kubelet/cm/qos_container_manager_linux.go`


📍 *Расположение:* `pkg/kubemark/hollow_kubelet.go:85`



---


[function] name: Run file: pkg/kubemark/hollow_kubelet.go:123 returns_error: нет description: Starts this HollowKubelet and blocks.


### Run (pkg/kubemark/hollow_kubelet.go:123)


Starts this HollowKubelet and blocks.


```go
func (hk *HollowKubelet) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/kubemark/hollow_kubelet.go:123`



---


[function] name: volumePlugins file: pkg/kubemark/hollow_kubelet.go:68 returns_error: нет description: —


### volumePlugins (pkg/kubemark/hollow_kubelet.go:68)


volumePlugins is a function that performs operations based on the provided parameters and returns ().


```go
func volumePlugins(()) ()
```


📍 *Расположение:* `pkg/kubemark/hollow_kubelet.go:68`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_kubelet.md)

- [Следующая директория](pkg_printers.md)


---

