---
title: "Функции: cmd/kube-controller-manager"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/kube-controller-manager
---


# Функции: cmd/kube-controller-manager


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kube-apiserver.md)

- [Следующая директория](cmd_kube-proxy.md)


---


## Меню по файлам


- 📄 [cmd/kube-controller-manager/app/apps.go](#cmdkube-controller-managerappappsgo)

- 📄 [cmd/kube-controller-manager/app/autoscaling.go](#cmdkube-controller-managerappautoscalinggo)

- 📄 [cmd/kube-controller-manager/app/batch.go](#cmdkube-controller-managerappbatchgo)

- 📄 [cmd/kube-controller-manager/app/bootstrap.go](#cmdkube-controller-managerappbootstrapgo)

- 📄 [cmd/kube-controller-manager/app/certificates.go](#cmdkube-controller-managerappcertificatesgo)

- 📄 [cmd/kube-controller-manager/app/config/config.go](#cmdkube-controller-managerappconfigconfiggo)

- 📄 [cmd/kube-controller-manager/app/controller_descriptor.go](#cmdkube-controller-managerappcontroller_descriptorgo)

- 📄 [cmd/kube-controller-manager/app/controller_utils.go](#cmdkube-controller-managerappcontroller_utilsgo)

- 📄 [cmd/kube-controller-manager/app/controllermanager.go](#cmdkube-controller-managerappcontrollermanagergo)

- 📄 [cmd/kube-controller-manager/app/core.go](#cmdkube-controller-managerappcorego)

- 📄 [cmd/kube-controller-manager/app/discovery.go](#cmdkube-controller-managerappdiscoverygo)

- 📄 [cmd/kube-controller-manager/app/networking.go](#cmdkube-controller-managerappnetworkinggo)

- 📄 [cmd/kube-controller-manager/app/options/attachdetachcontroller.go](#cmdkube-controller-managerappoptionsattachdetachcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/cronjobcontroller.go](#cmdkube-controller-managerappoptionscronjobcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/csrsigningcontroller.go](#cmdkube-controller-managerappoptionscsrsigningcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/daemonsetcontroller.go](#cmdkube-controller-managerappoptionsdaemonsetcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/deploymentcontroller.go](#cmdkube-controller-managerappoptionsdeploymentcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/deprecatedcontroller.go](#cmdkube-controller-managerappoptionsdeprecatedcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go](#cmdkube-controller-managerappoptionsdevicetaintevictioncontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/endpointcontroller.go](#cmdkube-controller-managerappoptionsendpointcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/endpointslicecontroller.go](#cmdkube-controller-managerappoptionsendpointslicecontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go](#cmdkube-controller-managerappoptionsendpointslicemirroringcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/ephemeralcontroller.go](#cmdkube-controller-managerappoptionsephemeralcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go](#cmdkube-controller-managerappoptionsgarbagecollectorcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/hpacontroller.go](#cmdkube-controller-managerappoptionshpacontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/jobcontroller.go](#cmdkube-controller-managerappoptionsjobcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go](#cmdkube-controller-managerappoptionslegacyserviceaccounttokencleanergo)

- 📄 [cmd/kube-controller-manager/app/options/namespacecontroller.go](#cmdkube-controller-managerappoptionsnamespacecontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/nodeipamcontroller.go](#cmdkube-controller-managerappoptionsnodeipamcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go](#cmdkube-controller-managerappoptionsnodelifecyclecontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/options.go](#cmdkube-controller-managerappoptionsoptionsgo)

- 📄 [cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go](#cmdkube-controller-managerappoptionspersistentvolumebindercontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/podgccontroller.go](#cmdkube-controller-managerappoptionspodgccontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/replicasetcontroller.go](#cmdkube-controller-managerappoptionsreplicasetcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/replicationcontroller.go](#cmdkube-controller-managerappoptionsreplicationcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/resourceclaimcontroller.go](#cmdkube-controller-managerappoptionsresourceclaimcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/resourcequotacontroller.go](#cmdkube-controller-managerappoptionsresourcequotacontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/serviceaccountcontroller.go](#cmdkube-controller-managerappoptionsserviceaccountcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/statefulsetcontroller.go](#cmdkube-controller-managerappoptionsstatefulsetcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go](#cmdkube-controller-managerappoptionsttlafterfinishedcontrollergo)

- 📄 [cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go](#cmdkube-controller-managerappoptionsvalidatingadmissionpolicycontrollergo)

- 📄 [cmd/kube-controller-manager/app/plugins.go](#cmdkube-controller-managerapppluginsgo)

- 📄 [cmd/kube-controller-manager/app/policy.go](#cmdkube-controller-managerapppolicygo)

- 📄 [cmd/kube-controller-manager/app/rbac.go](#cmdkube-controller-managerapprbacgo)

- 📄 [cmd/kube-controller-manager/app/service_accounts.go](#cmdkube-controller-managerappservice_accountsgo)

- 📄 [cmd/kube-controller-manager/app/storageversionmigrator.go](#cmdkube-controller-managerappstorageversionmigratorgo)

- 📄 [cmd/kube-controller-manager/app/testing/testserver.go](#cmdkube-controller-managerapptestingtestservergo)

- 📄 [cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go](#cmdkube-controller-managerappvalidatingadmissionpolicystatusgo)

- 📄 [cmd/kube-controller-manager/controller-manager.go](#cmdkube-controller-managercontroller-managergo)


---


## cmd/kube-controller-manager/app/apps.go


📄 Исходный файл: `cmd/kube-controller-manager/app/apps.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [newDaemonSetController](#newdaemonsetcontroller-cmdkube-controller-managerappappsgo43) `:43`

- 🔗 [newDaemonSetControllerDescriptor](#newdaemonsetcontrollerdescriptor-cmdkube-controller-managerappappsgo35) `:35`

- 🔗 [newDeploymentController](#newdeploymentcontroller-cmdkube-controller-managerappappsgo128) `:128`

- 🔗 [newDeploymentControllerDescriptor](#newdeploymentcontrollerdescriptor-cmdkube-controller-managerappappsgo120) `:120`

- 🔗 [newReplicaSetController](#newreplicasetcontroller-cmdkube-controller-managerappappsgo102) `:102`

- 🔗 [newReplicaSetControllerDescriptor](#newreplicasetcontrollerdescriptor-cmdkube-controller-managerappappsgo94) `:94`

- 🔗 [newStatefulSetController](#newstatefulsetcontroller-cmdkube-controller-managerappappsgo75) `:75`

- 🔗 [newStatefulSetControllerDescriptor](#newstatefulsetcontrollerdescriptor-cmdkube-controller-managerappappsgo67) `:67`


</details>


[function] name: newDaemonSetController file: cmd/kube-controller-manager/app/apps.go:43 returns_error: да description: —


### newDaemonSetController (cmd/kube-controller-manager/app/apps.go:43)


newDaemonSetController is a function that performs operations based on the provided parameters and may return an error.


```go
func newDaemonSetController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/apps.go:43`



---


[function] name: newDaemonSetControllerDescriptor file: cmd/kube-controller-manager/app/apps.go:35 returns_error: нет description: —


### newDaemonSetControllerDescriptor (cmd/kube-controller-manager/app/apps.go:35)


newDaemonSetControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newDaemonSetControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/apps.go:35`



---


[function] name: newDeploymentController file: cmd/kube-controller-manager/app/apps.go:128 returns_error: да description: —


### newDeploymentController (cmd/kube-controller-manager/app/apps.go:128)


newDeploymentController is a function that performs operations based on the provided parameters and may return an error.


```go
func newDeploymentController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/apps.go:128`



---


[function] name: newDeploymentControllerDescriptor file: cmd/kube-controller-manager/app/apps.go:120 returns_error: нет description: —


### newDeploymentControllerDescriptor (cmd/kube-controller-manager/app/apps.go:120)


newDeploymentControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newDeploymentControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/apps.go:120`



---


[function] name: newReplicaSetController file: cmd/kube-controller-manager/app/apps.go:102 returns_error: да description: —


### newReplicaSetController (cmd/kube-controller-manager/app/apps.go:102)


newReplicaSetController is a function that performs operations based on the provided parameters and may return an error.


```go
func newReplicaSetController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/apps.go:102`



---


[function] name: newReplicaSetControllerDescriptor file: cmd/kube-controller-manager/app/apps.go:94 returns_error: нет description: —


### newReplicaSetControllerDescriptor (cmd/kube-controller-manager/app/apps.go:94)


newReplicaSetControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newReplicaSetControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/apps.go:94`



---


[function] name: newStatefulSetController file: cmd/kube-controller-manager/app/apps.go:75 returns_error: да description: —


### newStatefulSetController (cmd/kube-controller-manager/app/apps.go:75)


newStatefulSetController is a function that performs operations based on the provided parameters and may return an error.


```go
func newStatefulSetController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/apps.go:75`



---


[function] name: newStatefulSetControllerDescriptor file: cmd/kube-controller-manager/app/apps.go:67 returns_error: нет description: —


### newStatefulSetControllerDescriptor (cmd/kube-controller-manager/app/apps.go:67)


newStatefulSetControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newStatefulSetControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/apps.go:67`




## cmd/kube-controller-manager/app/autoscaling.go


📄 Исходный файл: `cmd/kube-controller-manager/app/autoscaling.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [newHorizontalPodAutoscalerController](#newhorizontalpodautoscalercontroller-cmdkube-controller-managerappautoscalinggo43) `:43`

- 🔗 [newHorizontalPodAutoscalerControllerDescriptor](#newhorizontalpodautoscalercontrollerdescriptor-cmdkube-controller-managerappautoscalinggo35) `:35`


</details>


[function] name: newHorizontalPodAutoscalerController file: cmd/kube-controller-manager/app/autoscaling.go:43 returns_error: да description: —


### newHorizontalPodAutoscalerController (cmd/kube-controller-manager/app/autoscaling.go:43)


newHorizontalPodAutoscalerController is a function that performs operations based on the provided parameters and may return an error.


```go
func newHorizontalPodAutoscalerController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/autoscaling.go:43`



---


[function] name: newHorizontalPodAutoscalerControllerDescriptor file: cmd/kube-controller-manager/app/autoscaling.go:35 returns_error: нет description: —


### newHorizontalPodAutoscalerControllerDescriptor (cmd/kube-controller-manager/app/autoscaling.go:35)


newHorizontalPodAutoscalerControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newHorizontalPodAutoscalerControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/autoscaling.go:35`




## cmd/kube-controller-manager/app/batch.go


📄 Исходный файл: `cmd/kube-controller-manager/app/batch.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [newCronJobController](#newcronjobcontroller-cmdkube-controller-managerappbatchgo68) `:68`

- 🔗 [newCronJobControllerDescriptor](#newcronjobcontrollerdescriptor-cmdkube-controller-managerappbatchgo60) `:60`

- 🔗 [newJobController](#newjobcontroller-cmdkube-controller-managerappbatchgo39) `:39`

- 🔗 [newJobControllerDescriptor](#newjobcontrollerdescriptor-cmdkube-controller-managerappbatchgo31) `:31`


</details>


[function] name: newCronJobController file: cmd/kube-controller-manager/app/batch.go:68 returns_error: да description: —


### newCronJobController (cmd/kube-controller-manager/app/batch.go:68)


newCronJobController is a function that performs operations based on the provided parameters and may return an error.


```go
func newCronJobController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/batch.go:68`



---


[function] name: newCronJobControllerDescriptor file: cmd/kube-controller-manager/app/batch.go:60 returns_error: нет description: —


### newCronJobControllerDescriptor (cmd/kube-controller-manager/app/batch.go:60)


newCronJobControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newCronJobControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/batch.go:60`



---


[function] name: newJobController file: cmd/kube-controller-manager/app/batch.go:39 returns_error: да description: —


### newJobController (cmd/kube-controller-manager/app/batch.go:39)


newJobController is a function that performs operations based on the provided parameters and may return an error.


```go
func newJobController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/batch.go:39`



---


[function] name: newJobControllerDescriptor file: cmd/kube-controller-manager/app/batch.go:31 returns_error: нет description: —


### newJobControllerDescriptor (cmd/kube-controller-manager/app/batch.go:31)


newJobControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newJobControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/batch.go:31`




## cmd/kube-controller-manager/app/bootstrap.go


📄 Исходный файл: `cmd/kube-controller-manager/app/bootstrap.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [newBootstrapSignerController](#newbootstrapsignercontroller-cmdkube-controller-managerappbootstrapgo36) `:36`

- 🔗 [newBootstrapSignerControllerDescriptor](#newbootstrapsignercontrollerdescriptor-cmdkube-controller-managerappbootstrapgo27) `:27`

- 🔗 [newTokenCleanerController](#newtokencleanercontroller-cmdkube-controller-managerappbootstrapgo64) `:64`

- 🔗 [newTokenCleanerControllerDescriptor](#newtokencleanercontrollerdescriptor-cmdkube-controller-managerappbootstrapgo55) `:55`


</details>


[function] name: newBootstrapSignerController file: cmd/kube-controller-manager/app/bootstrap.go:36 returns_error: да description: —


### newBootstrapSignerController (cmd/kube-controller-manager/app/bootstrap.go:36)


newBootstrapSignerController is a function that performs operations based on the provided parameters and may return an error.


```go
func newBootstrapSignerController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/bootstrap.go:36`



---


[function] name: newBootstrapSignerControllerDescriptor file: cmd/kube-controller-manager/app/bootstrap.go:27 returns_error: нет description: —


### newBootstrapSignerControllerDescriptor (cmd/kube-controller-manager/app/bootstrap.go:27)


newBootstrapSignerControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newBootstrapSignerControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/bootstrap.go:27`



---


[function] name: newTokenCleanerController file: cmd/kube-controller-manager/app/bootstrap.go:64 returns_error: да description: —


### newTokenCleanerController (cmd/kube-controller-manager/app/bootstrap.go:64)


newTokenCleanerController is a function that performs operations based on the provided parameters and may return an error.


```go
func newTokenCleanerController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/bootstrap.go:64`



---


[function] name: newTokenCleanerControllerDescriptor file: cmd/kube-controller-manager/app/bootstrap.go:55 returns_error: нет description: —


### newTokenCleanerControllerDescriptor (cmd/kube-controller-manager/app/bootstrap.go:55)


newTokenCleanerControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newTokenCleanerControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/bootstrap.go:55`




## cmd/kube-controller-manager/app/certificates.go


📄 Исходный файл: `cmd/kube-controller-manager/app/certificates.go`


<details open>
<summary><b>Функции в этом файле (23)</b></summary>


- 🔗 [anySpecificFilesSet](#anyspecificfilesset-cmdkube-controller-managerappcertificatesgo148) `:148`

- 🔗 [areKubeAPIServerClientSignerFilesSpecified](#arekubeapiserverclientsignerfilesspecified-cmdkube-controller-managerappcertificatesgo138) `:138`

- 🔗 [areKubeletClientSignerFilesSpecified](#arekubeletclientsignerfilesspecified-cmdkube-controller-managerappcertificatesgo133) `:133`

- 🔗 [areKubeletServingSignerFilesSpecified](#arekubeletservingsignerfilesspecified-cmdkube-controller-managerappcertificatesgo129) `:129`

- 🔗 [areLegacyUnknownSignerFilesSpecified](#arelegacyunknownsignerfilesspecified-cmdkube-controller-managerappcertificatesgo143) `:143`

- 🔗 [clusterTrustBundlesAvailable](#clustertrustbundlesavailable-cmdkube-controller-managerappcertificatesgo355) `:355`

- 🔗 [getKubeAPIServerCAFileContents](#getkubeapiservercafilecontents-cmdkube-controller-managerappcertificatesgo373) `:373`

- 🔗 [getKubeAPIServerClientSignerFiles](#getkubeapiserverclientsignerfiles-cmdkube-controller-managerappcertificatesgo171) `:171`

- 🔗 [getKubeletClientSignerFiles](#getkubeletclientsignerfiles-cmdkube-controller-managerappcertificatesgo163) `:163`

- 🔗 [getKubeletServingSignerFiles](#getkubeletservingsignerfiles-cmdkube-controller-managerappcertificatesgo155) `:155`

- 🔗 [getLegacyUnknownSignerFiles](#getlegacyunknownsignerfiles-cmdkube-controller-managerappcertificatesgo179) `:179`

- 🔗 [newCertificateSigningRequestApprovingController](#newcertificatesigningrequestapprovingcontroller-cmdkube-controller-managerappcertificatesgo194) `:194`

- 🔗 [newCertificateSigningRequestApprovingControllerDescriptor](#newcertificatesigningrequestapprovingcontrollerdescriptor-cmdkube-controller-managerappcertificatesgo187) `:187`

- 🔗 [newCertificateSigningRequestCleanerController](#newcertificatesigningrequestcleanercontroller-cmdkube-controller-managerappcertificatesgo217) `:217`

- 🔗 [newCertificateSigningRequestCleanerControllerDescriptor](#newcertificatesigningrequestcleanercontrollerdescriptor-cmdkube-controller-managerappcertificatesgo210) `:210`

- 🔗 [newCertificateSigningRequestSigningController](#newcertificatesigningrequestsigningcontroller-cmdkube-controller-managerappcertificatesgo54) `:54`

- 🔗 [newCertificateSigningRequestSigningControllerDescriptor](#newcertificatesigningrequestsigningcontrollerdescriptor-cmdkube-controller-managerappcertificatesgo46) `:46`

- 🔗 [newKubeAPIServerSignerClusterTrustBundledPublisherController](#newkubeapiserversignerclustertrustbundledpublishercontroller-cmdkube-controller-managerappcertificatesgo299) `:299`

- 🔗 [newKubeAPIServerSignerClusterTrustBundledPublisherDescriptor](#newkubeapiserversignerclustertrustbundledpublisherdescriptor-cmdkube-controller-managerappcertificatesgo289) `:289`

- 🔗 [newPodCertificateRequestCleanerController](#newpodcertificaterequestcleanercontroller-cmdkube-controller-managerappcertificatesgo242) `:242`

- 🔗 [newPodCertificateRequestCleanerControllerDescriptor](#newpodcertificaterequestcleanercontrollerdescriptor-cmdkube-controller-managerappcertificatesgo232) `:232`

- 🔗 [newRootCACertificatePublisherController](#newrootcacertificatepublishercontroller-cmdkube-controller-managerappcertificatesgo263) `:263`

- 🔗 [newRootCACertificatePublisherControllerDescriptor](#newrootcacertificatepublishercontrollerdescriptor-cmdkube-controller-managerappcertificatesgo255) `:255`


</details>


[function] name: anySpecificFilesSet file: cmd/kube-controller-manager/app/certificates.go:148 returns_error: нет description: —


### anySpecificFilesSet (cmd/kube-controller-manager/app/certificates.go:148)


anySpecificFilesSet is a function that performs operations based on the provided parameters and returns (config csrsigningconfig.CSRSigningControllerConfiguration).


```go
func anySpecificFilesSet((config csrsigningconfig.CSRSigningControllerConfiguration)) (config csrsigningconfig.CSRSigningControllerConfiguration)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** csrsigningconfig.CSRSigningControllerConfiguration


```json
{
  "ClusterSigningCertFile": "string",
  "ClusterSigningKeyFile": "string",
  "KubeletServingSignerConfiguration": {},
  "KubeletClientSignerConfiguration": {},
  "KubeAPIServerClientSignerConfiguration": {},
  "LegacyUnknownSignerConfiguration": {},
  "ClusterSigningDuration": {}
}
```


*Определено в:* `pkg/controller/certificates/signer/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:148`



---


[function] name: areKubeAPIServerClientSignerFilesSpecified file: cmd/kube-controller-manager/app/certificates.go:138 returns_error: нет description: —


### areKubeAPIServerClientSignerFilesSpecified (cmd/kube-controller-manager/app/certificates.go:138)


areKubeAPIServerClientSignerFilesSpecified is a function that performs operations based on the provided parameters and returns (config csrsigningconfig.CSRSigningControllerConfiguration).


```go
func areKubeAPIServerClientSignerFilesSpecified((config csrsigningconfig.CSRSigningControllerConfiguration)) (config csrsigningconfig.CSRSigningControllerConfiguration)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** csrsigningconfig.CSRSigningControllerConfiguration


```json
{
  "ClusterSigningCertFile": "string",
  "ClusterSigningKeyFile": "string",
  "KubeletServingSignerConfiguration": {},
  "KubeletClientSignerConfiguration": {},
  "KubeAPIServerClientSignerConfiguration": {},
  "LegacyUnknownSignerConfiguration": {},
  "ClusterSigningDuration": {}
}
```


*Определено в:* `pkg/controller/certificates/signer/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:138`



---


[function] name: areKubeletClientSignerFilesSpecified file: cmd/kube-controller-manager/app/certificates.go:133 returns_error: нет description: —


### areKubeletClientSignerFilesSpecified (cmd/kube-controller-manager/app/certificates.go:133)


areKubeletClientSignerFilesSpecified is a function that performs operations based on the provided parameters and returns (config csrsigningconfig.CSRSigningControllerConfiguration).


```go
func areKubeletClientSignerFilesSpecified((config csrsigningconfig.CSRSigningControllerConfiguration)) (config csrsigningconfig.CSRSigningControllerConfiguration)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** csrsigningconfig.CSRSigningControllerConfiguration


```json
{
  "ClusterSigningCertFile": "string",
  "ClusterSigningKeyFile": "string",
  "KubeletServingSignerConfiguration": {},
  "KubeletClientSignerConfiguration": {},
  "KubeAPIServerClientSignerConfiguration": {},
  "LegacyUnknownSignerConfiguration": {},
  "ClusterSigningDuration": {}
}
```


*Определено в:* `pkg/controller/certificates/signer/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:133`



---


[function] name: areKubeletServingSignerFilesSpecified file: cmd/kube-controller-manager/app/certificates.go:129 returns_error: нет description: —


### areKubeletServingSignerFilesSpecified (cmd/kube-controller-manager/app/certificates.go:129)


areKubeletServingSignerFilesSpecified is a function that performs operations based on the provided parameters and returns (config csrsigningconfig.CSRSigningControllerConfiguration).


```go
func areKubeletServingSignerFilesSpecified((config csrsigningconfig.CSRSigningControllerConfiguration)) (config csrsigningconfig.CSRSigningControllerConfiguration)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** csrsigningconfig.CSRSigningControllerConfiguration


```json
{
  "ClusterSigningCertFile": "string",
  "ClusterSigningKeyFile": "string",
  "KubeletServingSignerConfiguration": {},
  "KubeletClientSignerConfiguration": {},
  "KubeAPIServerClientSignerConfiguration": {},
  "LegacyUnknownSignerConfiguration": {},
  "ClusterSigningDuration": {}
}
```


*Определено в:* `pkg/controller/certificates/signer/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:129`



---


[function] name: areLegacyUnknownSignerFilesSpecified file: cmd/kube-controller-manager/app/certificates.go:143 returns_error: нет description: —


### areLegacyUnknownSignerFilesSpecified (cmd/kube-controller-manager/app/certificates.go:143)


areLegacyUnknownSignerFilesSpecified is a function that performs operations based on the provided parameters and returns (config csrsigningconfig.CSRSigningControllerConfiguration).


```go
func areLegacyUnknownSignerFilesSpecified((config csrsigningconfig.CSRSigningControllerConfiguration)) (config csrsigningconfig.CSRSigningControllerConfiguration)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** csrsigningconfig.CSRSigningControllerConfiguration


```json
{
  "ClusterSigningCertFile": "string",
  "ClusterSigningKeyFile": "string",
  "KubeletServingSignerConfiguration": {},
  "KubeletClientSignerConfiguration": {},
  "KubeAPIServerClientSignerConfiguration": {},
  "LegacyUnknownSignerConfiguration": {},
  "ClusterSigningDuration": {}
}
```


*Определено в:* `pkg/controller/certificates/signer/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:143`



---


[function] name: clusterTrustBundlesAvailable file: cmd/kube-controller-manager/app/certificates.go:355 returns_error: да description: —


### clusterTrustBundlesAvailable (cmd/kube-controller-manager/app/certificates.go:355)


clusterTrustBundlesAvailable is a function that performs operations based on the provided parameters and may return an error.


```go
func clusterTrustBundlesAvailable((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:355`



---


[function] name: getKubeAPIServerCAFileContents file: cmd/kube-controller-manager/app/certificates.go:373 returns_error: да description: —


### getKubeAPIServerCAFileContents (cmd/kube-controller-manager/app/certificates.go:373)


getKubeAPIServerCAFileContents is a function that performs operations based on the provided parameters and may return an error.


```go
func getKubeAPIServerCAFileContents(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:373`



---


[function] name: getKubeAPIServerClientSignerFiles file: cmd/kube-controller-manager/app/certificates.go:171 returns_error: нет description: —


### getKubeAPIServerClientSignerFiles (cmd/kube-controller-manager/app/certificates.go:171)


getKubeAPIServerClientSignerFiles is a function that performs operations based on the provided parameters and returns (string, string).


```go
func getKubeAPIServerClientSignerFiles((string, string)) (string, string)
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:171`



---


[function] name: getKubeletClientSignerFiles file: cmd/kube-controller-manager/app/certificates.go:163 returns_error: нет description: —


### getKubeletClientSignerFiles (cmd/kube-controller-manager/app/certificates.go:163)


getKubeletClientSignerFiles is a function that performs operations based on the provided parameters and returns (string, string).


```go
func getKubeletClientSignerFiles((string, string)) (string, string)
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:163`



---


[function] name: getKubeletServingSignerFiles file: cmd/kube-controller-manager/app/certificates.go:155 returns_error: нет description: —


### getKubeletServingSignerFiles (cmd/kube-controller-manager/app/certificates.go:155)


getKubeletServingSignerFiles is a function that performs operations based on the provided parameters and returns (string, string).


```go
func getKubeletServingSignerFiles((string, string)) (string, string)
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:155`



---


[function] name: getLegacyUnknownSignerFiles file: cmd/kube-controller-manager/app/certificates.go:179 returns_error: нет description: —


### getLegacyUnknownSignerFiles (cmd/kube-controller-manager/app/certificates.go:179)


getLegacyUnknownSignerFiles is a function that performs operations based on the provided parameters and returns (string, string).


```go
func getLegacyUnknownSignerFiles((string, string)) (string, string)
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:179`



---


[function] name: newCertificateSigningRequestApprovingController file: cmd/kube-controller-manager/app/certificates.go:194 returns_error: да description: —


### newCertificateSigningRequestApprovingController (cmd/kube-controller-manager/app/certificates.go:194)


newCertificateSigningRequestApprovingController is a function that performs operations based on the provided parameters and may return an error.


```go
func newCertificateSigningRequestApprovingController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:194`



---


[function] name: newCertificateSigningRequestApprovingControllerDescriptor file: cmd/kube-controller-manager/app/certificates.go:187 returns_error: нет description: —


### newCertificateSigningRequestApprovingControllerDescriptor (cmd/kube-controller-manager/app/certificates.go:187)


newCertificateSigningRequestApprovingControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newCertificateSigningRequestApprovingControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:187`



---


[function] name: newCertificateSigningRequestCleanerController file: cmd/kube-controller-manager/app/certificates.go:217 returns_error: да description: —


### newCertificateSigningRequestCleanerController (cmd/kube-controller-manager/app/certificates.go:217)


newCertificateSigningRequestCleanerController is a function that performs operations based on the provided parameters and may return an error.


```go
func newCertificateSigningRequestCleanerController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:217`



---


[function] name: newCertificateSigningRequestCleanerControllerDescriptor file: cmd/kube-controller-manager/app/certificates.go:210 returns_error: нет description: —


### newCertificateSigningRequestCleanerControllerDescriptor (cmd/kube-controller-manager/app/certificates.go:210)


newCertificateSigningRequestCleanerControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newCertificateSigningRequestCleanerControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:210`



---


[function] name: newCertificateSigningRequestSigningController file: cmd/kube-controller-manager/app/certificates.go:54 returns_error: да description: —


### newCertificateSigningRequestSigningController (cmd/kube-controller-manager/app/certificates.go:54)


newCertificateSigningRequestSigningController is a function that performs operations based on the provided parameters and may return an error.


```go
func newCertificateSigningRequestSigningController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:54`



---


[function] name: newCertificateSigningRequestSigningControllerDescriptor file: cmd/kube-controller-manager/app/certificates.go:46 returns_error: нет description: —


### newCertificateSigningRequestSigningControllerDescriptor (cmd/kube-controller-manager/app/certificates.go:46)


newCertificateSigningRequestSigningControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newCertificateSigningRequestSigningControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:46`



---


[function] name: newKubeAPIServerSignerClusterTrustBundledPublisherController file: cmd/kube-controller-manager/app/certificates.go:299 returns_error: да description: —


### newKubeAPIServerSignerClusterTrustBundledPublisherController (cmd/kube-controller-manager/app/certificates.go:299)


newKubeAPIServerSignerClusterTrustBundledPublisherController is a function that performs operations based on the provided parameters and may return an error.


```go
func newKubeAPIServerSignerClusterTrustBundledPublisherController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:299`



---


[function] name: newKubeAPIServerSignerClusterTrustBundledPublisherDescriptor file: cmd/kube-controller-manager/app/certificates.go:289 returns_error: нет description: —


### newKubeAPIServerSignerClusterTrustBundledPublisherDescriptor (cmd/kube-controller-manager/app/certificates.go:289)


newKubeAPIServerSignerClusterTrustBundledPublisherDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newKubeAPIServerSignerClusterTrustBundledPublisherDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:289`



---


[function] name: newPodCertificateRequestCleanerController file: cmd/kube-controller-manager/app/certificates.go:242 returns_error: да description: —


### newPodCertificateRequestCleanerController (cmd/kube-controller-manager/app/certificates.go:242)


newPodCertificateRequestCleanerController is a function that performs operations based on the provided parameters and may return an error.


```go
func newPodCertificateRequestCleanerController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:242`



---


[function] name: newPodCertificateRequestCleanerControllerDescriptor file: cmd/kube-controller-manager/app/certificates.go:232 returns_error: нет description: —


### newPodCertificateRequestCleanerControllerDescriptor (cmd/kube-controller-manager/app/certificates.go:232)


newPodCertificateRequestCleanerControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newPodCertificateRequestCleanerControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:232`



---


[function] name: newRootCACertificatePublisherController file: cmd/kube-controller-manager/app/certificates.go:263 returns_error: да description: —


### newRootCACertificatePublisherController (cmd/kube-controller-manager/app/certificates.go:263)


newRootCACertificatePublisherController is a function that performs operations based on the provided parameters and may return an error.


```go
func newRootCACertificatePublisherController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:263`



---


[function] name: newRootCACertificatePublisherControllerDescriptor file: cmd/kube-controller-manager/app/certificates.go:255 returns_error: нет description: —


### newRootCACertificatePublisherControllerDescriptor (cmd/kube-controller-manager/app/certificates.go:255)


newRootCACertificatePublisherControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newRootCACertificatePublisherControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/certificates.go:255`




## cmd/kube-controller-manager/app/config/config.go


📄 Исходный файл: `cmd/kube-controller-manager/app/config/config.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Complete](#complete-cmdkube-controller-managerappconfigconfiggo68) `:68`


</details>


[function] name: Complete file: cmd/kube-controller-manager/app/config/config.go:68 returns_error: нет description: Complete fills in any fields not set that are required to have valid data. It's mutating the receiver.


### Complete (cmd/kube-controller-manager/app/config/config.go:68)


Complete fills in any fields not set that are required to have valid data. It's mutating the receiver.


```go
func (c *Config) Complete(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/config/config.go:68`




## cmd/kube-controller-manager/app/controller_descriptor.go


📄 Исходный файл: `cmd/kube-controller-manager/app/controller_descriptor.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [BuildController](#buildcontroller-cmdkube-controller-managerappcontroller_descriptorgo93) `:93`

- 🔗 [ControllerAliases](#controlleraliases-cmdkube-controller-managerappcontroller_descriptorgo121) `:121`

- 🔗 [ControllersDisabledByDefault](#controllersdisabledbydefault-cmdkube-controller-managerappcontroller_descriptorgo131) `:131`

- 🔗 [GetAliases](#getaliases-cmdkube-controller-managerappcontroller_descriptorgo74) `:74`

- 🔗 [GetControllerConstructor](#getcontrollerconstructor-cmdkube-controller-managerappcontroller_descriptorgo64) `:64`

- 🔗 [GetRequiredFeatureGates](#getrequiredfeaturegates-cmdkube-controller-managerappcontroller_descriptorgo68) `:68`

- 🔗 [IsCloudProviderController](#iscloudprovidercontroller-cmdkube-controller-managerappcontroller_descriptorgo82) `:82`

- 🔗 [IsDisabledByDefault](#isdisabledbydefault-cmdkube-controller-managerappcontroller_descriptorgo78) `:78`

- 🔗 [KnownControllers](#knowncontrollers-cmdkube-controller-managerappcontroller_descriptorgo116) `:116`

- 🔗 [Name](#name-cmdkube-controller-managerappcontroller_descriptorgo60) `:60`

- 🔗 [NewControllerDescriptors](#newcontrollerdescriptors-cmdkube-controller-managerappcontroller_descriptorgo148) `:148`

- 🔗 [RequiresSpecialHandling](#requiresspecialhandling-cmdkube-controller-managerappcontroller_descriptorgo87) `:87`


</details>


[function] name: BuildController file: cmd/kube-controller-manager/app/controller_descriptor.go:93 returns_error: да description: BuildController creates a controller based on the given descriptor.
The associated controller's constructor is called at


### BuildController (cmd/kube-controller-manager/app/controller_descriptor.go:93)


BuildController creates a controller based on the given descriptor.
The associated controller's constructor is called at the end, so the same contract applies for the return values here.


```go
func (r *ControllerDescriptor) BuildController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:93`



---


[function] name: ControllerAliases file: cmd/kube-controller-manager/app/controller_descriptor.go:121 returns_error: нет description: ControllerAliases returns a mapping of aliases to canonical controller names


### ControllerAliases (cmd/kube-controller-manager/app/controller_descriptor.go:121)


ControllerAliases returns a mapping of aliases to canonical controller names


```go
func ControllerAliases(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:121`



---


[function] name: ControllersDisabledByDefault file: cmd/kube-controller-manager/app/controller_descriptor.go:131 returns_error: нет description: —


### ControllersDisabledByDefault (cmd/kube-controller-manager/app/controller_descriptor.go:131)


ControllersDisabledByDefault is a function that performs operations based on the provided parameters and returns ().


```go
func ControllersDisabledByDefault(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:131`



---


[function] name: GetAliases file: cmd/kube-controller-manager/app/controller_descriptor.go:74 returns_error: нет description: GetAliases returns aliases to ensure backwards compatibility and should never be removed!
Only addition of new aliases i


### GetAliases (cmd/kube-controller-manager/app/controller_descriptor.go:74)


GetAliases returns aliases to ensure backwards compatibility and should never be removed!
Only addition of new aliases is allowed, and only when a canonical name is changed (please see CHANGE POLICY of controller names)


```go
func (r *ControllerDescriptor) GetAliases(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:74`



---


[function] name: GetControllerConstructor file: cmd/kube-controller-manager/app/controller_descriptor.go:64 returns_error: нет description: —


### GetControllerConstructor (cmd/kube-controller-manager/app/controller_descriptor.go:64)


GetControllerConstructor is a method that retrieves data based on the provided parameters and returns ().


```go
func (r *ControllerDescriptor) GetControllerConstructor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:64`



---


[function] name: GetRequiredFeatureGates file: cmd/kube-controller-manager/app/controller_descriptor.go:68 returns_error: нет description: —


### GetRequiredFeatureGates (cmd/kube-controller-manager/app/controller_descriptor.go:68)


GetRequiredFeatureGates is a method that retrieves data based on the provided parameters and returns ().


```go
func (r *ControllerDescriptor) GetRequiredFeatureGates(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:68`



---


[function] name: IsCloudProviderController file: cmd/kube-controller-manager/app/controller_descriptor.go:82 returns_error: нет description: —


### IsCloudProviderController (cmd/kube-controller-manager/app/controller_descriptor.go:82)


IsCloudProviderController is a method that performs operations based on the provided parameters and returns ().


```go
func (r *ControllerDescriptor) IsCloudProviderController(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:82`



---


[function] name: IsDisabledByDefault file: cmd/kube-controller-manager/app/controller_descriptor.go:78 returns_error: нет description: —


### IsDisabledByDefault (cmd/kube-controller-manager/app/controller_descriptor.go:78)


IsDisabledByDefault is a method that performs operations based on the provided parameters and returns ().


```go
func (r *ControllerDescriptor) IsDisabledByDefault(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:78`



---


[function] name: KnownControllers file: cmd/kube-controller-manager/app/controller_descriptor.go:116 returns_error: нет description: KnownControllers returns all known controllers' name


### KnownControllers (cmd/kube-controller-manager/app/controller_descriptor.go:116)


KnownControllers returns all known controllers' name


```go
func KnownControllers(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:116`



---


[function] name: Name file: cmd/kube-controller-manager/app/controller_descriptor.go:60 returns_error: нет description: —


### Name (cmd/kube-controller-manager/app/controller_descriptor.go:60)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (r *ControllerDescriptor) Name(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:60`



---


[function] name: NewControllerDescriptors file: cmd/kube-controller-manager/app/controller_descriptor.go:148 returns_error: нет description: NewControllerDescriptors is a public map of named controller groups (you can start more than one in an init func)
paired


### NewControllerDescriptors (cmd/kube-controller-manager/app/controller_descriptor.go:148)


NewControllerDescriptors is a public map of named controller groups (you can start more than one in an init func)
paired to their ControllerDescriptor wrapper object that includes the associated controller constructor.
This allows for structured downstream composition and subdivision.


```go
func NewControllerDescriptors(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:148`



---


[function] name: RequiresSpecialHandling file: cmd/kube-controller-manager/app/controller_descriptor.go:87 returns_error: нет description: RequiresSpecialHandling should return true only in a special non-generic controllers like ServiceAccountTokenController


### RequiresSpecialHandling (cmd/kube-controller-manager/app/controller_descriptor.go:87)


RequiresSpecialHandling should return true only in a special non-generic controllers like ServiceAccountTokenController


```go
func (r *ControllerDescriptor) RequiresSpecialHandling(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_descriptor.go:87`




## cmd/kube-controller-manager/app/controller_utils.go


📄 Исходный файл: `cmd/kube-controller-manager/app/controller_utils.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Name](#name-cmdkube-controller-managerappcontroller_utilsgo61) `:61`

- 🔗 [Run](#run-cmdkube-controller-managerappcontroller_utilsgo31) `:31`

- 🔗 [Run](#run-cmdkube-controller-managerappcontroller_utilsgo65) `:65`

- 🔗 [concurrentRun](#concurrentrun-cmdkube-controller-managerappcontroller_utilsgo44) `:44`

- 🔗 [newControllerLoop](#newcontrollerloop-cmdkube-controller-managerappcontroller_utilsgo54) `:54`


</details>


[function] name: Name file: cmd/kube-controller-manager/app/controller_utils.go:61 returns_error: нет description: —


### Name (cmd/kube-controller-manager/app/controller_utils.go:61)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (loop *controllerLoop) Name(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_utils.go:61`



---


[function] name: Run file: cmd/kube-controller-manager/app/controller_utils.go:31 returns_error: нет description: —


### Run (cmd/kube-controller-manager/app/controller_utils.go:31)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (rx runFuncSlice) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_utils.go:31`



---


[function] name: Run file: cmd/kube-controller-manager/app/controller_utils.go:65 returns_error: нет description: —


### Run (cmd/kube-controller-manager/app/controller_utils.go:65)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (loop *controllerLoop) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_utils.go:65`



---


[function] name: concurrentRun file: cmd/kube-controller-manager/app/controller_utils.go:44 returns_error: нет description: concurrentRun returns a runFunc that wraps the given functions to run concurrently.


### concurrentRun (cmd/kube-controller-manager/app/controller_utils.go:44)


concurrentRun returns a runFunc that wraps the given functions to run concurrently.


```go
func concurrentRun((rx ...runFunc)) (rx ...runFunc)
```


**Тип ответа:** rx


```json
{
  "VolumeID": "string",
  "FSType": "string",
  "ReadOnly": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/portworxvolumesource.go`


**Тип ответа:** runFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_utils.go:44`



---


[function] name: newControllerLoop file: cmd/kube-controller-manager/app/controller_utils.go:54 returns_error: нет description: —


### newControllerLoop (cmd/kube-controller-manager/app/controller_utils.go:54)


newControllerLoop is a function that performs operations based on the provided parameters and returns (run runFunc, controllerName string).


```go
func newControllerLoop((run runFunc, controllerName string)) (run runFunc, controllerName string)
```


**Тип ответа:** run


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/node/v1alpha1/runtimeclass.go`


**Тип ответа:** runFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** controllerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-controller-manager/app/controller_utils.go:54`




## cmd/kube-controller-manager/app/controllermanager.go


📄 Исходный файл: `cmd/kube-controller-manager/app/controllermanager.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [BuildControllers](#buildcontrollers-cmdkube-controller-managerappcontrollermanagergo571) `:571`

- 🔗 [CreateControllerContext](#createcontrollercontext-cmdkube-controller-managerappcontrollermanagergo475) `:475`

- 🔗 [IsControllerEnabled](#iscontrollerenabled-cmdkube-controller-managerappcontrollermanagergo446) `:446`

- 🔗 [NewClient](#newclient-cmdkube-controller-managerappcontrollermanagergo464) `:464`

- 🔗 [NewClientConfig](#newclientconfig-cmdkube-controller-managerappcontrollermanagergo455) `:455`

- 🔗 [NewControllerManagerCommand](#newcontrollermanagercommand-cmdkube-controller-managerappcontrollermanagergo102) `:102`

- 🔗 [ResyncPeriod](#resyncperiod-cmdkube-controller-managerappcontrollermanagergo177) `:177`

- 🔗 [Run](#run-cmdkube-controller-managerappcontrollermanagergo185) `:185`

- 🔗 [RunControllers](#runcontrollers-cmdkube-controller-managerappcontrollermanagergo655) `:655`

- 🔗 [createClientBuilders](#createclientbuilders-cmdkube-controller-managerappcontrollermanagergo766) `:766`

- 🔗 [filteredControllerDescriptors](#filteredcontrollerdescriptors-cmdkube-controller-managerappcontrollermanagergo816) `:816`

- 🔗 [init](#init-cmdkube-controller-managerappcontrollermanagergo87) `:87`

- 🔗 [leaderElectAndRun](#leaderelectandrun-cmdkube-controller-managerappcontrollermanagergo785) `:785`

- 🔗 [readCA](#readca-cmdkube-controller-managerappcontrollermanagergo753) `:753`


</details>


[function] name: BuildControllers file: cmd/kube-controller-manager/app/controllermanager.go:571 returns_error: да description: BuildControllers builds all controllers in the given descriptor map. Disabled controllers are obviously skipped.

A heal


### BuildControllers (cmd/kube-controller-manager/app/controllermanager.go:571)


BuildControllers builds all controllers in the given descriptor map. Disabled controllers are obviously skipped.

A health check is registered for each controller using the controller name. The default check always passes.
If the controller implements controller.HealthCheckable, though, the given check is used.
The controller can also implement controller.Debuggable, in which case the debug handler is registered with the given mux.


```go
func BuildControllers(([]Controller, error)) ([]Controller, error)
```


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


*Типы возврата:* `[]Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:571`



---


[function] name: CreateControllerContext file: cmd/kube-controller-manager/app/controllermanager.go:475 returns_error: да description: CreateControllerContext creates a context struct containing references to resources needed by the
controllers such as th


### CreateControllerContext (cmd/kube-controller-manager/app/controllermanager.go:475)


CreateControllerContext creates a context struct containing references to resources needed by the
controllers such as the cloud provider and clientBuilder. rootClientBuilder is only used for
the shared-informers client and token controller.


```go
func CreateControllerContext((ControllerContext, error)) (ControllerContext, error)
```


**Тип ответа:** ControllerContext


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ControllerContext`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:475`



---


[function] name: IsControllerEnabled file: cmd/kube-controller-manager/app/controllermanager.go:446 returns_error: нет description: IsControllerEnabled checks if the context's controllers enabled or not


### IsControllerEnabled (cmd/kube-controller-manager/app/controllermanager.go:446)


IsControllerEnabled checks if the context's controllers enabled or not


```go
func (c ControllerContext) IsControllerEnabled((controllerDescriptor *ControllerDescriptor)) (controllerDescriptor *ControllerDescriptor)
```


**Тип запроса:** ControllerDescriptor


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


**Тип ответа:** controllerDescriptor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ControllerDescriptor


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


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:446`



---


[function] name: NewClient file: cmd/kube-controller-manager/app/controllermanager.go:464 returns_error: да description: NewClient is a shortcut for ClientBuilder.Client. It wraps the error with an additional message.


### NewClient (cmd/kube-controller-manager/app/controllermanager.go:464)


NewClient is a shortcut for ClientBuilder.Client. It wraps the error with an additional message.


```go
func (c ControllerContext) NewClient((kubernetes.Interface, error)) (kubernetes.Interface, error)
```


**Тип ответа:** kubernetes.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `kubernetes.Interface`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:464`



---


[function] name: NewClientConfig file: cmd/kube-controller-manager/app/controllermanager.go:455 returns_error: да description: NewClientConfig is a shortcut for ClientBuilder.Config. It wraps the error with an additional message.


### NewClientConfig (cmd/kube-controller-manager/app/controllermanager.go:455)


NewClientConfig is a shortcut for ClientBuilder.Config. It wraps the error with an additional message.


```go
func (c ControllerContext) NewClientConfig((*restclient.Config, error)) (*restclient.Config, error)
```


**Тип запроса:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** restclient.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*restclient.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:455`



---


[function] name: NewControllerManagerCommand file: cmd/kube-controller-manager/app/controllermanager.go:102 returns_error: нет description: NewControllerManagerCommand creates a *cobra.Command object with default parameters


### NewControllerManagerCommand (cmd/kube-controller-manager/app/controllermanager.go:102)


NewControllerManagerCommand creates a *cobra.Command object with default parameters


```go
func NewControllerManagerCommand(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:102`



---


[function] name: ResyncPeriod file: cmd/kube-controller-manager/app/controllermanager.go:177 returns_error: нет description: ResyncPeriod returns a function which generates a duration each time it is
invoked; this is because that multiple contro


### ResyncPeriod (cmd/kube-controller-manager/app/controllermanager.go:177)


ResyncPeriod returns a function which generates a duration each time it is
invoked; this is because that multiple controllers don't get into lock-step.


```go
func ResyncPeriod((c *config.CompletedConfig)) (c *config.CompletedConfig)
```


**Тип запроса:** config.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** config.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:177`



---


[function] name: Run file: cmd/kube-controller-manager/app/controllermanager.go:185 returns_error: нет description: Run runs the KubeControllerManagerOptions.


### Run (cmd/kube-controller-manager/app/controllermanager.go:185)


Run runs the KubeControllerManagerOptions.


```go
func Run((ctx context.Context, c *config.CompletedConfig)) (ctx context.Context, c *config.CompletedConfig)
```


**Тип запроса:** config.CompletedConfig


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


**Тип ответа:** config.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:185`



---


[function] name: RunControllers file: cmd/kube-controller-manager/app/controllermanager.go:655 returns_error: нет description: RunControllers runs all controllers concurrently and blocks until the context is cancelled and all controllers are termi


### RunControllers (cmd/kube-controller-manager/app/controllermanager.go:655)


RunControllers runs all controllers concurrently and blocks until the context is cancelled and all controllers are terminated.

Once the context is cancelled, RunControllers waits for shutdownTimeout for all controllers to terminate.
When the timeout is reached, the function unblocks and returns false.
Zero shutdown timeout means that there is no timeout.


```go
func RunControllers((ctx context.Context, controllerCtx ControllerContext, controllers []Controller,
	controllerStartJitterMaxFactor float64, shutdownTimeout time.Duration)) (ctx context.Context, controllerCtx ControllerContext, controllers []Controller,
	controllerStartJitterMaxFactor float64, shutdownTimeout time.Duration)
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


**Тип ответа:** controllerCtx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ControllerContext


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


**Тип ответа:** controllers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** controllerStartJitterMaxFactor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shutdownTimeout


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


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:655`



---


[function] name: createClientBuilders file: cmd/kube-controller-manager/app/controllermanager.go:766 returns_error: нет description: createClientBuilders creates clientBuilder and rootClientBuilder from the given configuration


### createClientBuilders (cmd/kube-controller-manager/app/controllermanager.go:766)


createClientBuilders creates clientBuilder and rootClientBuilder from the given configuration


```go
func createClientBuilders((clientBuilder clientbuilder.ControllerClientBuilder, rootClientBuilder clientbuilder.ControllerClientBuilder)) (clientBuilder clientbuilder.ControllerClientBuilder, rootClientBuilder clientbuilder.ControllerClientBuilder)
```


**Тип ответа:** clientBuilder


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientbuilder.ControllerClientBuilder


```json
{
  "ClientConfig": null
}
```


*Определено в:* `staging/src/k8s.io/controller-manager/pkg/clientbuilder/client_builder.go`


**Тип ответа:** rootClientBuilder


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientbuilder.ControllerClientBuilder


```json
{
  "ClientConfig": null
}
```


*Определено в:* `staging/src/k8s.io/controller-manager/pkg/clientbuilder/client_builder.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:766`



---


[function] name: filteredControllerDescriptors file: cmd/kube-controller-manager/app/controllermanager.go:816 returns_error: нет description: filteredControllerDescriptors returns all controllerDescriptors after filtering through filterFunc.


### filteredControllerDescriptors (cmd/kube-controller-manager/app/controllermanager.go:816)


filteredControllerDescriptors returns all controllerDescriptors after filtering through filterFunc.


```go
func filteredControllerDescriptors((controllerDescriptors map[string]*ControllerDescriptor, filterFunc leadermigration.FilterFunc, expected leadermigration.FilterResult)) (controllerDescriptors map[string]*ControllerDescriptor, filterFunc leadermigration.FilterFunc, expected leadermigration.FilterResult)
```


**Тип запроса:** ControllerDescriptor


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


**Тип ответа:** controllerDescriptors


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ControllerDescriptor


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


**Тип ответа:** filterFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** leadermigration.FilterFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** expected


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/errors/errors.go`


**Тип ответа:** leadermigration.FilterResult


```json
{
  "Nodes": null,
  "NodeNames": null,
  "FailedNodes": {},
  "FailedAndUnresolvableNodes": {},
  "Error": "string"
}
```


*Определено в:* `staging/src/k8s.io/kube-scheduler/extender/v1/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:816`



---


[function] name: init file: cmd/kube-controller-manager/app/controllermanager.go:87 returns_error: нет description: —


### init (cmd/kube-controller-manager/app/controllermanager.go:87)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:87`



---


[function] name: leaderElectAndRun file: cmd/kube-controller-manager/app/controllermanager.go:785 returns_error: нет description: leaderElectAndRun runs the leader election, and runs the callbacks once the leader lease is acquired.
TODO: extract this


### leaderElectAndRun (cmd/kube-controller-manager/app/controllermanager.go:785)


leaderElectAndRun runs the leader election, and runs the callbacks once the leader lease is acquired.
TODO: extract this function into staging/controller-manager


```go
func leaderElectAndRun((ctx context.Context, c *config.CompletedConfig, lockIdentity string, electionChecker *leaderelection.HealthzAdaptor, resourceLock string, leaseName string, callbacks leaderelection.LeaderCallbacks)) (ctx context.Context, c *config.CompletedConfig, lockIdentity string, electionChecker *leaderelection.HealthzAdaptor, resourceLock string, leaseName string, callbacks leaderelection.LeaderCallbacks)
```


**Тип запроса:** config.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** leaderelection.HealthzAdaptor


```json
{
  "pointerLock": {},
  "le": null,
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/leaderelection/healthzadaptor.go`


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


**Тип ответа:** config.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lockIdentity


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** electionChecker


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** leaderelection.HealthzAdaptor


```json
{
  "pointerLock": {},
  "le": null,
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/leaderelection/healthzadaptor.go`


**Тип ответа:** resourceLock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** leaseName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** callbacks


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** leaderelection.LeaderCallbacks


```json
{
  "OnStartedLeading": {},
  "OnStoppedLeading": {},
  "OnNewLeader": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/leaderelection/leaderelection.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:785`



---


[function] name: readCA file: cmd/kube-controller-manager/app/controllermanager.go:753 returns_error: да description: —


### readCA (cmd/kube-controller-manager/app/controllermanager.go:753)


readCA is a function that performs operations based on the provided parameters and may return an error.


```go
func readCA(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/controllermanager.go:753`




## cmd/kube-controller-manager/app/core.go


📄 Исходный файл: `cmd/kube-controller-manager/app/core.go`


<details open>
<summary><b>Функции в этом файле (57)</b></summary>


- 🔗 [Name](#name-cmdkube-controller-managerappcorego804) `:804`

- 🔗 [Run](#run-cmdkube-controller-managerappcorego808) `:808`

- 🔗 [newCloudNodeLifecycleControllerDescriptor](#newcloudnodelifecyclecontrollerdescriptor-cmdkube-controller-managerappcorego286) `:286`

- 🔗 [newDeviceTaintEvictionController](#newdevicetaintevictioncontroller-cmdkube-controller-managerappcorego263) `:263`

- 🔗 [newDeviceTaintEvictionControllerDescriptor](#newdevicetaintevictioncontrollerdescriptor-cmdkube-controller-managerappcorego251) `:251`

- 🔗 [newEndpointsController](#newendpointscontroller-cmdkube-controller-managerappcorego507) `:507`

- 🔗 [newEndpointsControllerDescriptor](#newendpointscontrollerdescriptor-cmdkube-controller-managerappcorego499) `:499`

- 🔗 [newEphemeralVolumeController](#newephemeralvolumecontroller-cmdkube-controller-managerappcorego443) `:443`

- 🔗 [newEphemeralVolumeControllerDescriptor](#newephemeralvolumecontrollerdescriptor-cmdkube-controller-managerappcorego435) `:435`

- 🔗 [newGarbageCollectorController](#newgarbagecollectorcontroller-cmdkube-controller-managerappcorego756) `:756`

- 🔗 [newGarbageCollectorControllerDescriptor](#newgarbagecollectorcontrollerdescriptor-cmdkube-controller-managerappcorego738) `:738`

- 🔗 [newLegacyServiceAccountTokenCleanerController](#newlegacyserviceaccounttokencleanercontroller-cmdkube-controller-managerappcorego940) `:940`

- 🔗 [newLegacyServiceAccountTokenCleanerControllerDescriptor](#newlegacyserviceaccounttokencleanercontrollerdescriptor-cmdkube-controller-managerappcorego932) `:932`

- 🔗 [newModifiedNamespaceController](#newmodifiednamespacecontroller-cmdkube-controller-managerappcorego658) `:658`

- 🔗 [newNamespaceController](#newnamespacecontroller-cmdkube-controller-managerappcorego638) `:638`

- 🔗 [newNamespaceControllerDescriptor](#newnamespacecontrollerdescriptor-cmdkube-controller-managerappcorego630) `:630`

- 🔗 [newNodeIpamController](#newnodeipamcontroller-cmdkube-controller-managerappcorego105) `:105`

- 🔗 [newNodeIpamControllerDescriptor](#newnodeipamcontrollerdescriptor-cmdkube-controller-managerappcorego97) `:97`

- 🔗 [newNodeLifecycleController](#newnodelifecyclecontroller-cmdkube-controller-managerappcorego189) `:189`

- 🔗 [newNodeLifecycleControllerDescriptor](#newnodelifecyclecontrollerdescriptor-cmdkube-controller-managerappcorego181) `:181`

- 🔗 [newNodeRouteControllerDescriptor](#newnoderoutecontrollerdescriptor-cmdkube-controller-managerappcorego299) `:299`

- 🔗 [newPersistentVolumeAttachDetachController](#newpersistentvolumeattachdetachcontroller-cmdkube-controller-managerappcorego359) `:359`

- 🔗 [newPersistentVolumeAttachDetachControllerDescriptor](#newpersistentvolumeattachdetachcontrollerdescriptor-cmdkube-controller-managerappcorego351) `:351`

- 🔗 [newPersistentVolumeBinderController](#newpersistentvolumebindercontroller-cmdkube-controller-managerappcorego320) `:320`

- 🔗 [newPersistentVolumeBinderControllerDescriptor](#newpersistentvolumebindercontrollerdescriptor-cmdkube-controller-managerappcorego312) `:312`

- 🔗 [newPersistentVolumeClaimProtectionController](#newpersistentvolumeclaimprotectioncontroller-cmdkube-controller-managerappcorego831) `:831`

- 🔗 [newPersistentVolumeClaimProtectionControllerDescriptor](#newpersistentvolumeclaimprotectioncontrollerdescriptor-cmdkube-controller-managerappcorego823) `:823`

- 🔗 [newPersistentVolumeExpanderController](#newpersistentvolumeexpandercontroller-cmdkube-controller-managerappcorego407) `:407`

- 🔗 [newPersistentVolumeExpanderControllerDescriptor](#newpersistentvolumeexpandercontrollerdescriptor-cmdkube-controller-managerappcorego399) `:399`

- 🔗 [newPersistentVolumeProtectionController](#newpersistentvolumeprotectioncontroller-cmdkube-controller-managerappcorego860) `:860`

- 🔗 [newPersistentVolumeProtectionControllerDescriptor](#newpersistentvolumeprotectioncontrollerdescriptor-cmdkube-controller-managerappcorego852) `:852`

- 🔗 [newPodGarbageCollectorController](#newpodgarbagecollectorcontroller-cmdkube-controller-managerappcorego561) `:561`

- 🔗 [newPodGarbageCollectorControllerDescriptor](#newpodgarbagecollectorcontrollerdescriptor-cmdkube-controller-managerappcorego553) `:553`

- 🔗 [newReplicationController](#newreplicationcontroller-cmdkube-controller-managerappcorego534) `:534`

- 🔗 [newReplicationControllerDescriptor](#newreplicationcontrollerdescriptor-cmdkube-controller-managerappcorego526) `:526`

- 🔗 [newResourceClaimController](#newresourceclaimcontroller-cmdkube-controller-managerappcorego474) `:474`

- 🔗 [newResourceClaimControllerDescriptor](#newresourceclaimcontrollerdescriptor-cmdkube-controller-managerappcorego463) `:463`

- 🔗 [newResourceQuotaController](#newresourcequotacontroller-cmdkube-controller-managerappcorego585) `:585`

- 🔗 [newResourceQuotaControllerDescriptor](#newresourcequotacontrollerdescriptor-cmdkube-controller-managerappcorego577) `:577`

- 🔗 [newSELinuxWarningController](#newselinuxwarningcontroller-cmdkube-controller-managerappcorego1119) `:1119`

- 🔗 [newSELinuxWarningControllerDescriptor](#newselinuxwarningcontrollerdescriptor-cmdkube-controller-managerappcorego1108) `:1108`

- 🔗 [newServiceAccountController](#newserviceaccountcontroller-cmdkube-controller-managerappcorego691) `:691`

- 🔗 [newServiceAccountControllerDescriptor](#newserviceaccountcontrollerdescriptor-cmdkube-controller-managerappcorego683) `:683`

- 🔗 [newServiceLBControllerDescriptor](#newservicelbcontrollerdescriptor-cmdkube-controller-managerappcorego84) `:84`

- 🔗 [newStorageVersionGarbageCollectorController](#newstorageversiongarbagecollectorcontroller-cmdkube-controller-managerappcorego1093) `:1093`

- 🔗 [newStorageVersionGarbageCollectorControllerDescriptor](#newstorageversiongarbagecollectorcontrollerdescriptor-cmdkube-controller-managerappcorego1081) `:1081`

- 🔗 [newTTLAfterFinishedController](#newttlafterfinishedcontroller-cmdkube-controller-managerappcorego916) `:916`

- 🔗 [newTTLAfterFinishedControllerDescriptor](#newttlafterfinishedcontrollerdescriptor-cmdkube-controller-managerappcorego908) `:908`

- 🔗 [newTTLController](#newttlcontroller-cmdkube-controller-managerappcorego722) `:722`

- 🔗 [newTTLControllerDescriptor](#newttlcontrollerdescriptor-cmdkube-controller-managerappcorego714) `:714`

- 🔗 [newTaintEvictionController](#newtaintevictioncontroller-cmdkube-controller-managerappcorego230) `:230`

- 🔗 [newTaintEvictionControllerDescriptor](#newtaintevictioncontrollerdescriptor-cmdkube-controller-managerappcorego220) `:220`

- 🔗 [newVolumeAttributesClassProtectionController](#newvolumeattributesclassprotectioncontroller-cmdkube-controller-managerappcorego886) `:886`

- 🔗 [newVolumeAttributesClassProtectionControllerDescriptor](#newvolumeattributesclassprotectioncontrollerdescriptor-cmdkube-controller-managerappcorego876) `:876`

- 🔗 [processCIDRs](#processcidrs-cmdkube-controller-managerappcorego992) `:992`

- 🔗 [setNodeCIDRMaskSizes](#setnodecidrmasksizes-cmdkube-controller-managerappcorego1010) `:1010`

- 🔗 [validateCIDRs](#validatecidrs-cmdkube-controller-managerappcorego968) `:968`


</details>


[function] name: Name file: cmd/kube-controller-manager/app/core.go:804 returns_error: нет description: Name must be implemented explicitly as it collides with the embedded controller.


### Name (cmd/kube-controller-manager/app/core.go:804)


Name must be implemented explicitly as it collides with the embedded controller.


```go
func (c *garbageCollectorController) Name(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:804`



---


[function] name: Run file: cmd/kube-controller-manager/app/core.go:808 returns_error: нет description: —


### Run (cmd/kube-controller-manager/app/core.go:808)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (c *garbageCollectorController) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:808`



---


[function] name: newCloudNodeLifecycleControllerDescriptor file: cmd/kube-controller-manager/app/core.go:286 returns_error: нет description: —


### newCloudNodeLifecycleControllerDescriptor (cmd/kube-controller-manager/app/core.go:286)


newCloudNodeLifecycleControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newCloudNodeLifecycleControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:286`



---


[function] name: newDeviceTaintEvictionController file: cmd/kube-controller-manager/app/core.go:263 returns_error: да description: —


### newDeviceTaintEvictionController (cmd/kube-controller-manager/app/core.go:263)


newDeviceTaintEvictionController is a function that performs operations based on the provided parameters and may return an error.


```go
func newDeviceTaintEvictionController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:263`



---


[function] name: newDeviceTaintEvictionControllerDescriptor file: cmd/kube-controller-manager/app/core.go:251 returns_error: нет description: —


### newDeviceTaintEvictionControllerDescriptor (cmd/kube-controller-manager/app/core.go:251)


newDeviceTaintEvictionControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newDeviceTaintEvictionControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:251`



---


[function] name: newEndpointsController file: cmd/kube-controller-manager/app/core.go:507 returns_error: да description: —


### newEndpointsController (cmd/kube-controller-manager/app/core.go:507)


newEndpointsController is a function that performs operations based on the provided parameters and may return an error.


```go
func newEndpointsController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:507`



---


[function] name: newEndpointsControllerDescriptor file: cmd/kube-controller-manager/app/core.go:499 returns_error: нет description: —


### newEndpointsControllerDescriptor (cmd/kube-controller-manager/app/core.go:499)


newEndpointsControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newEndpointsControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:499`



---


[function] name: newEphemeralVolumeController file: cmd/kube-controller-manager/app/core.go:443 returns_error: да description: —


### newEphemeralVolumeController (cmd/kube-controller-manager/app/core.go:443)


newEphemeralVolumeController is a function that performs operations based on the provided parameters and may return an error.


```go
func newEphemeralVolumeController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:443`



---


[function] name: newEphemeralVolumeControllerDescriptor file: cmd/kube-controller-manager/app/core.go:435 returns_error: нет description: —


### newEphemeralVolumeControllerDescriptor (cmd/kube-controller-manager/app/core.go:435)


newEphemeralVolumeControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newEphemeralVolumeControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:435`



---


[function] name: newGarbageCollectorController file: cmd/kube-controller-manager/app/core.go:756 returns_error: да description: —


### newGarbageCollectorController (cmd/kube-controller-manager/app/core.go:756)


newGarbageCollectorController is a function that performs operations based on the provided parameters and may return an error.


```go
func newGarbageCollectorController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:756`



---


[function] name: newGarbageCollectorControllerDescriptor file: cmd/kube-controller-manager/app/core.go:738 returns_error: нет description: —


### newGarbageCollectorControllerDescriptor (cmd/kube-controller-manager/app/core.go:738)


newGarbageCollectorControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newGarbageCollectorControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:738`



---


[function] name: newLegacyServiceAccountTokenCleanerController file: cmd/kube-controller-manager/app/core.go:940 returns_error: да description: —


### newLegacyServiceAccountTokenCleanerController (cmd/kube-controller-manager/app/core.go:940)


newLegacyServiceAccountTokenCleanerController is a function that performs operations based on the provided parameters and may return an error.


```go
func newLegacyServiceAccountTokenCleanerController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:940`



---


[function] name: newLegacyServiceAccountTokenCleanerControllerDescriptor file: cmd/kube-controller-manager/app/core.go:932 returns_error: нет description: —


### newLegacyServiceAccountTokenCleanerControllerDescriptor (cmd/kube-controller-manager/app/core.go:932)


newLegacyServiceAccountTokenCleanerControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newLegacyServiceAccountTokenCleanerControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:932`



---


[function] name: newModifiedNamespaceController file: cmd/kube-controller-manager/app/core.go:658 returns_error: да description: —


### newModifiedNamespaceController (cmd/kube-controller-manager/app/core.go:658)


newModifiedNamespaceController is a function that performs operations based on the provided parameters and may return an error.


```go
func newModifiedNamespaceController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:658`



---


[function] name: newNamespaceController file: cmd/kube-controller-manager/app/core.go:638 returns_error: да description: —


### newNamespaceController (cmd/kube-controller-manager/app/core.go:638)


newNamespaceController is a function that performs operations based on the provided parameters and may return an error.


```go
func newNamespaceController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:638`



---


[function] name: newNamespaceControllerDescriptor file: cmd/kube-controller-manager/app/core.go:630 returns_error: нет description: —


### newNamespaceControllerDescriptor (cmd/kube-controller-manager/app/core.go:630)


newNamespaceControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newNamespaceControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:630`



---


[function] name: newNodeIpamController file: cmd/kube-controller-manager/app/core.go:105 returns_error: да description: —


### newNodeIpamController (cmd/kube-controller-manager/app/core.go:105)


newNodeIpamController is a function that performs operations based on the provided parameters and may return an error.


```go
func newNodeIpamController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:105`



---


[function] name: newNodeIpamControllerDescriptor file: cmd/kube-controller-manager/app/core.go:97 returns_error: нет description: —


### newNodeIpamControllerDescriptor (cmd/kube-controller-manager/app/core.go:97)


newNodeIpamControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newNodeIpamControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:97`



---


[function] name: newNodeLifecycleController file: cmd/kube-controller-manager/app/core.go:189 returns_error: да description: —


### newNodeLifecycleController (cmd/kube-controller-manager/app/core.go:189)


newNodeLifecycleController is a function that performs operations based on the provided parameters and may return an error.


```go
func newNodeLifecycleController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:189`



---


[function] name: newNodeLifecycleControllerDescriptor file: cmd/kube-controller-manager/app/core.go:181 returns_error: нет description: —


### newNodeLifecycleControllerDescriptor (cmd/kube-controller-manager/app/core.go:181)


newNodeLifecycleControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newNodeLifecycleControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:181`



---


[function] name: newNodeRouteControllerDescriptor file: cmd/kube-controller-manager/app/core.go:299 returns_error: нет description: —


### newNodeRouteControllerDescriptor (cmd/kube-controller-manager/app/core.go:299)


newNodeRouteControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newNodeRouteControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:299`



---


[function] name: newPersistentVolumeAttachDetachController file: cmd/kube-controller-manager/app/core.go:359 returns_error: да description: —


### newPersistentVolumeAttachDetachController (cmd/kube-controller-manager/app/core.go:359)


newPersistentVolumeAttachDetachController is a function that performs operations based on the provided parameters and may return an error.


```go
func newPersistentVolumeAttachDetachController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:359`



---


[function] name: newPersistentVolumeAttachDetachControllerDescriptor file: cmd/kube-controller-manager/app/core.go:351 returns_error: нет description: —


### newPersistentVolumeAttachDetachControllerDescriptor (cmd/kube-controller-manager/app/core.go:351)


newPersistentVolumeAttachDetachControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newPersistentVolumeAttachDetachControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:351`



---


[function] name: newPersistentVolumeBinderController file: cmd/kube-controller-manager/app/core.go:320 returns_error: да description: —


### newPersistentVolumeBinderController (cmd/kube-controller-manager/app/core.go:320)


newPersistentVolumeBinderController is a function that performs operations based on the provided parameters and may return an error.


```go
func newPersistentVolumeBinderController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:320`



---


[function] name: newPersistentVolumeBinderControllerDescriptor file: cmd/kube-controller-manager/app/core.go:312 returns_error: нет description: —


### newPersistentVolumeBinderControllerDescriptor (cmd/kube-controller-manager/app/core.go:312)


newPersistentVolumeBinderControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newPersistentVolumeBinderControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:312`



---


[function] name: newPersistentVolumeClaimProtectionController file: cmd/kube-controller-manager/app/core.go:831 returns_error: да description: —


### newPersistentVolumeClaimProtectionController (cmd/kube-controller-manager/app/core.go:831)


newPersistentVolumeClaimProtectionController is a function that performs operations based on the provided parameters and may return an error.


```go
func newPersistentVolumeClaimProtectionController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:831`



---


[function] name: newPersistentVolumeClaimProtectionControllerDescriptor file: cmd/kube-controller-manager/app/core.go:823 returns_error: нет description: —


### newPersistentVolumeClaimProtectionControllerDescriptor (cmd/kube-controller-manager/app/core.go:823)


newPersistentVolumeClaimProtectionControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newPersistentVolumeClaimProtectionControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:823`



---


[function] name: newPersistentVolumeExpanderController file: cmd/kube-controller-manager/app/core.go:407 returns_error: да description: —


### newPersistentVolumeExpanderController (cmd/kube-controller-manager/app/core.go:407)


newPersistentVolumeExpanderController is a function that performs operations based on the provided parameters and may return an error.


```go
func newPersistentVolumeExpanderController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:407`



---


[function] name: newPersistentVolumeExpanderControllerDescriptor file: cmd/kube-controller-manager/app/core.go:399 returns_error: нет description: —


### newPersistentVolumeExpanderControllerDescriptor (cmd/kube-controller-manager/app/core.go:399)


newPersistentVolumeExpanderControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newPersistentVolumeExpanderControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:399`



---


[function] name: newPersistentVolumeProtectionController file: cmd/kube-controller-manager/app/core.go:860 returns_error: да description: —


### newPersistentVolumeProtectionController (cmd/kube-controller-manager/app/core.go:860)


newPersistentVolumeProtectionController is a function that performs operations based on the provided parameters and may return an error.


```go
func newPersistentVolumeProtectionController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:860`



---


[function] name: newPersistentVolumeProtectionControllerDescriptor file: cmd/kube-controller-manager/app/core.go:852 returns_error: нет description: —


### newPersistentVolumeProtectionControllerDescriptor (cmd/kube-controller-manager/app/core.go:852)


newPersistentVolumeProtectionControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newPersistentVolumeProtectionControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:852`



---


[function] name: newPodGarbageCollectorController file: cmd/kube-controller-manager/app/core.go:561 returns_error: да description: —


### newPodGarbageCollectorController (cmd/kube-controller-manager/app/core.go:561)


newPodGarbageCollectorController is a function that performs operations based on the provided parameters and may return an error.


```go
func newPodGarbageCollectorController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:561`



---


[function] name: newPodGarbageCollectorControllerDescriptor file: cmd/kube-controller-manager/app/core.go:553 returns_error: нет description: —


### newPodGarbageCollectorControllerDescriptor (cmd/kube-controller-manager/app/core.go:553)


newPodGarbageCollectorControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newPodGarbageCollectorControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:553`



---


[function] name: newReplicationController file: cmd/kube-controller-manager/app/core.go:534 returns_error: да description: —


### newReplicationController (cmd/kube-controller-manager/app/core.go:534)


newReplicationController is a function that performs operations based on the provided parameters and may return an error.


```go
func newReplicationController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:534`



---


[function] name: newReplicationControllerDescriptor file: cmd/kube-controller-manager/app/core.go:526 returns_error: нет description: —


### newReplicationControllerDescriptor (cmd/kube-controller-manager/app/core.go:526)


newReplicationControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newReplicationControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:526`



---


[function] name: newResourceClaimController file: cmd/kube-controller-manager/app/core.go:474 returns_error: да description: —


### newResourceClaimController (cmd/kube-controller-manager/app/core.go:474)


newResourceClaimController is a function that performs operations based on the provided parameters and may return an error.


```go
func newResourceClaimController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:474`



---


[function] name: newResourceClaimControllerDescriptor file: cmd/kube-controller-manager/app/core.go:463 returns_error: нет description: —


### newResourceClaimControllerDescriptor (cmd/kube-controller-manager/app/core.go:463)


newResourceClaimControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newResourceClaimControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:463`



---


[function] name: newResourceQuotaController file: cmd/kube-controller-manager/app/core.go:585 returns_error: да description: —


### newResourceQuotaController (cmd/kube-controller-manager/app/core.go:585)


newResourceQuotaController is a function that performs operations based on the provided parameters and may return an error.


```go
func newResourceQuotaController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:585`



---


[function] name: newResourceQuotaControllerDescriptor file: cmd/kube-controller-manager/app/core.go:577 returns_error: нет description: —


### newResourceQuotaControllerDescriptor (cmd/kube-controller-manager/app/core.go:577)


newResourceQuotaControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newResourceQuotaControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:577`



---


[function] name: newSELinuxWarningController file: cmd/kube-controller-manager/app/core.go:1119 returns_error: да description: —


### newSELinuxWarningController (cmd/kube-controller-manager/app/core.go:1119)


newSELinuxWarningController is a function that performs operations based on the provided parameters and may return an error.


```go
func newSELinuxWarningController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:1119`



---


[function] name: newSELinuxWarningControllerDescriptor file: cmd/kube-controller-manager/app/core.go:1108 returns_error: нет description: —


### newSELinuxWarningControllerDescriptor (cmd/kube-controller-manager/app/core.go:1108)


newSELinuxWarningControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newSELinuxWarningControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:1108`



---


[function] name: newServiceAccountController file: cmd/kube-controller-manager/app/core.go:691 returns_error: да description: —


### newServiceAccountController (cmd/kube-controller-manager/app/core.go:691)


newServiceAccountController is a function that performs operations based on the provided parameters and may return an error.


```go
func newServiceAccountController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:691`



---


[function] name: newServiceAccountControllerDescriptor file: cmd/kube-controller-manager/app/core.go:683 returns_error: нет description: —


### newServiceAccountControllerDescriptor (cmd/kube-controller-manager/app/core.go:683)


newServiceAccountControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newServiceAccountControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:683`



---


[function] name: newServiceLBControllerDescriptor file: cmd/kube-controller-manager/app/core.go:84 returns_error: нет description: —


### newServiceLBControllerDescriptor (cmd/kube-controller-manager/app/core.go:84)


newServiceLBControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newServiceLBControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:84`



---


[function] name: newStorageVersionGarbageCollectorController file: cmd/kube-controller-manager/app/core.go:1093 returns_error: да description: —


### newStorageVersionGarbageCollectorController (cmd/kube-controller-manager/app/core.go:1093)


newStorageVersionGarbageCollectorController is a function that performs operations based on the provided parameters and may return an error.


```go
func newStorageVersionGarbageCollectorController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:1093`



---


[function] name: newStorageVersionGarbageCollectorControllerDescriptor file: cmd/kube-controller-manager/app/core.go:1081 returns_error: нет description: —


### newStorageVersionGarbageCollectorControllerDescriptor (cmd/kube-controller-manager/app/core.go:1081)


newStorageVersionGarbageCollectorControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newStorageVersionGarbageCollectorControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:1081`



---


[function] name: newTTLAfterFinishedController file: cmd/kube-controller-manager/app/core.go:916 returns_error: да description: —


### newTTLAfterFinishedController (cmd/kube-controller-manager/app/core.go:916)


newTTLAfterFinishedController is a function that performs operations based on the provided parameters and may return an error.


```go
func newTTLAfterFinishedController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:916`



---


[function] name: newTTLAfterFinishedControllerDescriptor file: cmd/kube-controller-manager/app/core.go:908 returns_error: нет description: —


### newTTLAfterFinishedControllerDescriptor (cmd/kube-controller-manager/app/core.go:908)


newTTLAfterFinishedControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newTTLAfterFinishedControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:908`



---


[function] name: newTTLController file: cmd/kube-controller-manager/app/core.go:722 returns_error: да description: —


### newTTLController (cmd/kube-controller-manager/app/core.go:722)


newTTLController is a function that performs operations based on the provided parameters and may return an error.


```go
func newTTLController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:722`



---


[function] name: newTTLControllerDescriptor file: cmd/kube-controller-manager/app/core.go:714 returns_error: нет description: —


### newTTLControllerDescriptor (cmd/kube-controller-manager/app/core.go:714)


newTTLControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newTTLControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:714`



---


[function] name: newTaintEvictionController file: cmd/kube-controller-manager/app/core.go:230 returns_error: да description: —


### newTaintEvictionController (cmd/kube-controller-manager/app/core.go:230)


newTaintEvictionController is a function that performs operations based on the provided parameters and may return an error.


```go
func newTaintEvictionController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:230`



---


[function] name: newTaintEvictionControllerDescriptor file: cmd/kube-controller-manager/app/core.go:220 returns_error: нет description: —


### newTaintEvictionControllerDescriptor (cmd/kube-controller-manager/app/core.go:220)


newTaintEvictionControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newTaintEvictionControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:220`



---


[function] name: newVolumeAttributesClassProtectionController file: cmd/kube-controller-manager/app/core.go:886 returns_error: да description: —


### newVolumeAttributesClassProtectionController (cmd/kube-controller-manager/app/core.go:886)


newVolumeAttributesClassProtectionController is a function that performs operations based on the provided parameters and may return an error.


```go
func newVolumeAttributesClassProtectionController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:886`



---


[function] name: newVolumeAttributesClassProtectionControllerDescriptor file: cmd/kube-controller-manager/app/core.go:876 returns_error: нет description: —


### newVolumeAttributesClassProtectionControllerDescriptor (cmd/kube-controller-manager/app/core.go:876)


newVolumeAttributesClassProtectionControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newVolumeAttributesClassProtectionControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:876`



---


[function] name: processCIDRs file: cmd/kube-controller-manager/app/core.go:992 returns_error: да description: processCIDRs is a helper function that works on a comma separated cidrs and returns
a list of typed cidrs
a flag if cidr


### processCIDRs (cmd/kube-controller-manager/app/core.go:992)


processCIDRs is a helper function that works on a comma separated cidrs and returns
a list of typed cidrs
a flag if cidrs represents a dual stack
error if failed to parse any of the cidrs


```go
func processCIDRs(([]*net.IPNet, bool, error)) ([]*net.IPNet, bool, error)
```


**Тип запроса:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*net.IPNet`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:992`



---


[function] name: setNodeCIDRMaskSizes file: cmd/kube-controller-manager/app/core.go:1010 returns_error: да description: setNodeCIDRMaskSizes returns the IPv4 and IPv6 node cidr mask sizes to the value provided
for --node-cidr-mask-size-ipv4


### setNodeCIDRMaskSizes (cmd/kube-controller-manager/app/core.go:1010)


setNodeCIDRMaskSizes returns the IPv4 and IPv6 node cidr mask sizes to the value provided
for --node-cidr-mask-size-ipv4 and --node-cidr-mask-size-ipv6 respectively. If value not provided,
then it will return default IPv4 and IPv6 cidr mask sizes.


```go
func setNodeCIDRMaskSizes(([]int, error)) ([]int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:1010`



---


[function] name: validateCIDRs file: cmd/kube-controller-manager/app/core.go:968 returns_error: да description: processCIDRs is a helper function that works on a comma separated cidrs and returns
a list of typed cidrs
error if faile


### validateCIDRs (cmd/kube-controller-manager/app/core.go:968)


processCIDRs is a helper function that works on a comma separated cidrs and returns
a list of typed cidrs
error if failed to parse any of the cidrs or invalid length of cidrs


```go
func validateCIDRs(([]*net.IPNet, error)) ([]*net.IPNet, error)
```


**Тип запроса:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*net.IPNet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/core.go:968`




## cmd/kube-controller-manager/app/discovery.go


📄 Исходный файл: `cmd/kube-controller-manager/app/discovery.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [newEndpointSliceController](#newendpointslicecontroller-cmdkube-controller-managerappdiscoverygo38) `:38`

- 🔗 [newEndpointSliceControllerDescriptor](#newendpointslicecontrollerdescriptor-cmdkube-controller-managerappdiscoverygo30) `:30`

- 🔗 [newEndpointSliceMirroringController](#newendpointslicemirroringcontroller-cmdkube-controller-managerappdiscoverygo67) `:67`

- 🔗 [newEndpointSliceMirroringControllerDescriptor](#newendpointslicemirroringcontrollerdescriptor-cmdkube-controller-managerappdiscoverygo59) `:59`


</details>


[function] name: newEndpointSliceController file: cmd/kube-controller-manager/app/discovery.go:38 returns_error: да description: —


### newEndpointSliceController (cmd/kube-controller-manager/app/discovery.go:38)


newEndpointSliceController is a function that performs operations based on the provided parameters and may return an error.


```go
func newEndpointSliceController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/discovery.go:38`



---


[function] name: newEndpointSliceControllerDescriptor file: cmd/kube-controller-manager/app/discovery.go:30 returns_error: нет description: —


### newEndpointSliceControllerDescriptor (cmd/kube-controller-manager/app/discovery.go:30)


newEndpointSliceControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newEndpointSliceControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/discovery.go:30`



---


[function] name: newEndpointSliceMirroringController file: cmd/kube-controller-manager/app/discovery.go:67 returns_error: да description: —


### newEndpointSliceMirroringController (cmd/kube-controller-manager/app/discovery.go:67)


newEndpointSliceMirroringController is a function that performs operations based on the provided parameters and may return an error.


```go
func newEndpointSliceMirroringController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/discovery.go:67`



---


[function] name: newEndpointSliceMirroringControllerDescriptor file: cmd/kube-controller-manager/app/discovery.go:59 returns_error: нет description: —


### newEndpointSliceMirroringControllerDescriptor (cmd/kube-controller-manager/app/discovery.go:59)


newEndpointSliceMirroringControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newEndpointSliceMirroringControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/discovery.go:59`




## cmd/kube-controller-manager/app/networking.go


📄 Исходный файл: `cmd/kube-controller-manager/app/networking.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [newServiceCIDRsController](#newservicecidrscontroller-cmdkube-controller-managerappnetworkinggo41) `:41`

- 🔗 [newServiceCIDRsControllerDescriptor](#newservicecidrscontrollerdescriptor-cmdkube-controller-managerappnetworkinggo31) `:31`


</details>


[function] name: newServiceCIDRsController file: cmd/kube-controller-manager/app/networking.go:41 returns_error: да description: —


### newServiceCIDRsController (cmd/kube-controller-manager/app/networking.go:41)


newServiceCIDRsController is a function that performs operations based on the provided parameters and may return an error.


```go
func newServiceCIDRsController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/networking.go:41`



---


[function] name: newServiceCIDRsControllerDescriptor file: cmd/kube-controller-manager/app/networking.go:31 returns_error: нет description: —


### newServiceCIDRsControllerDescriptor (cmd/kube-controller-manager/app/networking.go:31)


newServiceCIDRsControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newServiceCIDRsControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/networking.go:31`




## cmd/kube-controller-manager/app/options/attachdetachcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/attachdetachcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsattachdetachcontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsattachdetachcontrollergo44) `:44`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsattachdetachcontrollergo57) `:57`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/attachdetachcontroller.go:33 returns_error: нет description: AddFlags adds flags related to AttachDetachController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/attachdetachcontroller.go:33)


AddFlags adds flags related to AttachDetachController for controller manager to the specified FlagSet.


```go
func (o *AttachDetachControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/attachdetachcontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/attachdetachcontroller.go:44 returns_error: нет description: ApplyTo fills up AttachDetachController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/attachdetachcontroller.go:44)


ApplyTo fills up AttachDetachController config with options.


```go
func (o *AttachDetachControllerOptions) ApplyTo((cfg *attachdetachconfig.AttachDetachControllerConfiguration)) (cfg *attachdetachconfig.AttachDetachControllerConfiguration)
```


**Тип запроса:** attachdetachconfig.AttachDetachControllerConfiguration


```json
{
  "DisableAttachDetachReconcilerSync": false,
  "ReconcilerSyncLoopPeriod": {},
  "DisableForceDetachOnTimeout": false
}
```


*Определено в:* `pkg/controller/volume/attachdetach/config/types.go`


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


**Тип ответа:** attachdetachconfig.AttachDetachControllerConfiguration


```json
{
  "DisableAttachDetachReconcilerSync": false,
  "ReconcilerSyncLoopPeriod": {},
  "DisableForceDetachOnTimeout": false
}
```


*Определено в:* `pkg/controller/volume/attachdetach/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/attachdetachcontroller.go:44`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/attachdetachcontroller.go:57 returns_error: нет description: Validate checks validation of AttachDetachControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/attachdetachcontroller.go:57)


Validate checks validation of AttachDetachControllerOptions.


```go
func (o *AttachDetachControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/attachdetachcontroller.go:57`




## cmd/kube-controller-manager/app/options/cronjobcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/cronjobcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionscronjobcontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionscronjobcontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionscronjobcontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/cronjobcontroller.go:33 returns_error: нет description: AddFlags adds flags related to JobController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/cronjobcontroller.go:33)


AddFlags adds flags related to JobController for controller manager to the specified FlagSet.


```go
func (o *CronJobControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/cronjobcontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/cronjobcontroller.go:42 returns_error: нет description: ApplyTo fills up JobController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/cronjobcontroller.go:42)


ApplyTo fills up JobController config with options.


```go
func (o *CronJobControllerOptions) ApplyTo((cfg *cronjobconfig.CronJobControllerConfiguration)) (cfg *cronjobconfig.CronJobControllerConfiguration)
```


**Тип запроса:** cronjobconfig.CronJobControllerConfiguration


```json
{
  "ConcurrentCronJobSyncs": 0
}
```


*Определено в:* `pkg/controller/cronjob/config/types.go`


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


**Тип ответа:** cronjobconfig.CronJobControllerConfiguration


```json
{
  "ConcurrentCronJobSyncs": 0
}
```


*Определено в:* `pkg/controller/cronjob/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/cronjobcontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/cronjobcontroller.go:53 returns_error: нет description: Validate checks validation of CronJobControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/cronjobcontroller.go:53)


Validate checks validation of CronJobControllerOptions.


```go
func (o *CronJobControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/cronjobcontroller.go:53`




## cmd/kube-controller-manager/app/options/csrsigningcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/csrsigningcontroller.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionscsrsigningcontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionscsrsigningcontrollergo52) `:52`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionscsrsigningcontrollergo69) `:69`

- 🔗 [csrSigningFilesValid](#csrsigningfilesvalid-cmdkube-controller-managerappoptionscsrsigningcontrollergo101) `:101`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/csrsigningcontroller.go:33 returns_error: нет description: AddFlags adds flags related to CSRSigningController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/csrsigningcontroller.go:33)


AddFlags adds flags related to CSRSigningController for controller manager to the specified FlagSet.


```go
func (o *CSRSigningControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/csrsigningcontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/csrsigningcontroller.go:52 returns_error: нет description: ApplyTo fills up CSRSigningController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/csrsigningcontroller.go:52)


ApplyTo fills up CSRSigningController config with options.


```go
func (o *CSRSigningControllerOptions) ApplyTo((cfg *csrsigningconfig.CSRSigningControllerConfiguration)) (cfg *csrsigningconfig.CSRSigningControllerConfiguration)
```


**Тип запроса:** csrsigningconfig.CSRSigningControllerConfiguration


```json
{
  "ClusterSigningCertFile": "string",
  "ClusterSigningKeyFile": "string",
  "KubeletServingSignerConfiguration": {},
  "KubeletClientSignerConfiguration": {},
  "KubeAPIServerClientSignerConfiguration": {},
  "LegacyUnknownSignerConfiguration": {},
  "ClusterSigningDuration": {}
}
```


*Определено в:* `pkg/controller/certificates/signer/config/types.go`


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


**Тип ответа:** csrsigningconfig.CSRSigningControllerConfiguration


```json
{
  "ClusterSigningCertFile": "string",
  "ClusterSigningKeyFile": "string",
  "KubeletServingSignerConfiguration": {},
  "KubeletClientSignerConfiguration": {},
  "KubeAPIServerClientSignerConfiguration": {},
  "LegacyUnknownSignerConfiguration": {},
  "ClusterSigningDuration": {}
}
```


*Определено в:* `pkg/controller/certificates/signer/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/csrsigningcontroller.go:52`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/csrsigningcontroller.go:69 returns_error: нет description: Validate checks validation of CSRSigningControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/csrsigningcontroller.go:69)


Validate checks validation of CSRSigningControllerOptions.


```go
func (o *CSRSigningControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/csrsigningcontroller.go:69`



---


[function] name: csrSigningFilesValid file: cmd/kube-controller-manager/app/options/csrsigningcontroller.go:101 returns_error: нет description: both must be specified or both must be empty


### csrSigningFilesValid (cmd/kube-controller-manager/app/options/csrsigningcontroller.go:101)


both must be specified or both must be empty


```go
func csrSigningFilesValid((config csrsigningconfig.CSRSigningConfiguration)) (config csrsigningconfig.CSRSigningConfiguration)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** csrsigningconfig.CSRSigningConfiguration


```json
{
  "CertFile": "string",
  "KeyFile": "string"
}
```


*Определено в:* `pkg/controller/certificates/signer/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/csrsigningcontroller.go:101`




## cmd/kube-controller-manager/app/options/daemonsetcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/daemonsetcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsdaemonsetcontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsdaemonsetcontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsdaemonsetcontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/daemonsetcontroller.go:33 returns_error: нет description: AddFlags adds flags related to DaemonSetController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/daemonsetcontroller.go:33)


AddFlags adds flags related to DaemonSetController for controller manager to the specified FlagSet.


```go
func (o *DaemonSetControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/daemonsetcontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/daemonsetcontroller.go:42 returns_error: нет description: ApplyTo fills up DaemonSetController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/daemonsetcontroller.go:42)


ApplyTo fills up DaemonSetController config with options.


```go
func (o *DaemonSetControllerOptions) ApplyTo((cfg *daemonconfig.DaemonSetControllerConfiguration)) (cfg *daemonconfig.DaemonSetControllerConfiguration)
```


**Тип запроса:** daemonconfig.DaemonSetControllerConfiguration


```json
{
  "ConcurrentDaemonSetSyncs": 0
}
```


*Определено в:* `pkg/controller/daemon/config/types.go`


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


**Тип ответа:** daemonconfig.DaemonSetControllerConfiguration


```json
{
  "ConcurrentDaemonSetSyncs": 0
}
```


*Определено в:* `pkg/controller/daemon/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/daemonsetcontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/daemonsetcontroller.go:53 returns_error: нет description: Validate checks validation of DaemonSetControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/daemonsetcontroller.go:53)


Validate checks validation of DaemonSetControllerOptions.


```go
func (o *DaemonSetControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/daemonsetcontroller.go:53`




## cmd/kube-controller-manager/app/options/deploymentcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/deploymentcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsdeploymentcontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsdeploymentcontrollergo40) `:40`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsdeploymentcontrollergo51) `:51`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/deploymentcontroller.go:31 returns_error: нет description: AddFlags adds flags related to DeploymentController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/deploymentcontroller.go:31)


AddFlags adds flags related to DeploymentController for controller manager to the specified FlagSet.


```go
func (o *DeploymentControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/deploymentcontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/deploymentcontroller.go:40 returns_error: нет description: ApplyTo fills up DeploymentController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/deploymentcontroller.go:40)


ApplyTo fills up DeploymentController config with options.


```go
func (o *DeploymentControllerOptions) ApplyTo((cfg *deploymentconfig.DeploymentControllerConfiguration)) (cfg *deploymentconfig.DeploymentControllerConfiguration)
```


**Тип запроса:** deploymentconfig.DeploymentControllerConfiguration


```json
{
  "ConcurrentDeploymentSyncs": 0
}
```


*Определено в:* `pkg/controller/deployment/config/types.go`


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


**Тип ответа:** deploymentconfig.DeploymentControllerConfiguration


```json
{
  "ConcurrentDeploymentSyncs": 0
}
```


*Определено в:* `pkg/controller/deployment/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/deploymentcontroller.go:40`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/deploymentcontroller.go:51 returns_error: нет description: Validate checks validation of DeploymentControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/deploymentcontroller.go:51)


Validate checks validation of DeploymentControllerOptions.


```go
func (o *DeploymentControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/deploymentcontroller.go:51`




## cmd/kube-controller-manager/app/options/deprecatedcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/deprecatedcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsdeprecatedcontrollergo32) `:32`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsdeprecatedcontrollergo39) `:39`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsdeprecatedcontrollergo48) `:48`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/deprecatedcontroller.go:32 returns_error: нет description: AddFlags adds flags related to DeprecatedController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/deprecatedcontroller.go:32)


AddFlags adds flags related to DeprecatedController for controller manager to the specified FlagSet.


```go
func (o *DeprecatedControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/deprecatedcontroller.go:32`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/deprecatedcontroller.go:39 returns_error: нет description: ApplyTo fills up DeprecatedController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/deprecatedcontroller.go:39)


ApplyTo fills up DeprecatedController config with options.


```go
func (o *DeprecatedControllerOptions) ApplyTo((cfg *kubectrlmgrconfig.DeprecatedControllerConfiguration)) (cfg *kubectrlmgrconfig.DeprecatedControllerConfiguration)
```


**Тип запроса:** kubectrlmgrconfig.DeprecatedControllerConfiguration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** kubectrlmgrconfig.DeprecatedControllerConfiguration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-controller-manager/app/options/deprecatedcontroller.go:39`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/deprecatedcontroller.go:48 returns_error: нет description: Validate checks validation of DeprecatedControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/deprecatedcontroller.go:48)


Validate checks validation of DeprecatedControllerOptions.


```go
func (o *DeprecatedControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/deprecatedcontroller.go:48`




## cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsdevicetaintevictioncontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsdevicetaintevictioncontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsdevicetaintevictioncontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:33 returns_error: нет description: AddFlags adds flags related to DeviceTaintEvictionController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:33)


AddFlags adds flags related to DeviceTaintEvictionController for controller manager to the specified FlagSet.


```go
func (o *DeviceTaintEvictionControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:42 returns_error: нет description: ApplyTo fills up DeviceTaintEvictionController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:42)


ApplyTo fills up DeviceTaintEvictionController config with options.


```go
func (o *DeviceTaintEvictionControllerOptions) ApplyTo((cfg *devicetaintevictionconfig.DeviceTaintEvictionControllerConfiguration)) (cfg *devicetaintevictionconfig.DeviceTaintEvictionControllerConfiguration)
```


**Тип запроса:** devicetaintevictionconfig.DeviceTaintEvictionControllerConfiguration


```json
{
  "ConcurrentSyncs": 0
}
```


*Определено в:* `pkg/controller/devicetainteviction/config/types.go`


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


**Тип ответа:** devicetaintevictionconfig.DeviceTaintEvictionControllerConfiguration


```json
{
  "ConcurrentSyncs": 0
}
```


*Определено в:* `pkg/controller/devicetainteviction/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:53 returns_error: нет description: Validate checks validation of DeviceTaintEvictionControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:53)


Validate checks validation of DeviceTaintEvictionControllerOptions.


```go
func (o *DeviceTaintEvictionControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/devicetaintevictioncontroller.go:53`




## cmd/kube-controller-manager/app/options/endpointcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/endpointcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsendpointcontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsendpointcontrollergo41) `:41`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsendpointcontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/endpointcontroller.go:31 returns_error: нет description: AddFlags adds flags related to EndPointController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/endpointcontroller.go:31)


AddFlags adds flags related to EndPointController for controller manager to the specified FlagSet.


```go
func (o *EndpointControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointcontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/endpointcontroller.go:41 returns_error: нет description: ApplyTo fills up EndPointController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/endpointcontroller.go:41)


ApplyTo fills up EndPointController config with options.


```go
func (o *EndpointControllerOptions) ApplyTo((cfg *endpointconfig.EndpointControllerConfiguration)) (cfg *endpointconfig.EndpointControllerConfiguration)
```


**Тип запроса:** endpointconfig.EndpointControllerConfiguration


```json
{
  "ConcurrentEndpointSyncs": 0,
  "EndpointUpdatesBatchPeriod": {}
}
```


*Определено в:* `pkg/controller/endpoint/config/types.go`


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


**Тип ответа:** endpointconfig.EndpointControllerConfiguration


```json
{
  "ConcurrentEndpointSyncs": 0,
  "EndpointUpdatesBatchPeriod": {}
}
```


*Определено в:* `pkg/controller/endpoint/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointcontroller.go:41`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/endpointcontroller.go:53 returns_error: нет description: Validate checks validation of EndpointControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/endpointcontroller.go:53)


Validate checks validation of EndpointControllerOptions.


```go
func (o *EndpointControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointcontroller.go:53`




## cmd/kube-controller-manager/app/options/endpointslicecontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/endpointslicecontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsendpointslicecontrollergo40) `:40`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsendpointslicecontrollergo51) `:51`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsendpointslicecontrollergo64) `:64`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/endpointslicecontroller.go:40 returns_error: нет description: AddFlags adds flags related to EndpointSliceController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/endpointslicecontroller.go:40)


AddFlags adds flags related to EndpointSliceController for controller manager to the specified FlagSet.


```go
func (o *EndpointSliceControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointslicecontroller.go:40`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/endpointslicecontroller.go:51 returns_error: нет description: ApplyTo fills up EndpointSliceController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/endpointslicecontroller.go:51)


ApplyTo fills up EndpointSliceController config with options.


```go
func (o *EndpointSliceControllerOptions) ApplyTo((cfg *endpointsliceconfig.EndpointSliceControllerConfiguration)) (cfg *endpointsliceconfig.EndpointSliceControllerConfiguration)
```


**Тип запроса:** endpointsliceconfig.EndpointSliceControllerConfiguration


```json
{
  "ConcurrentServiceEndpointSyncs": 0,
  "MaxEndpointsPerSlice": 0,
  "EndpointUpdatesBatchPeriod": {}
}
```


*Определено в:* `pkg/controller/endpointslice/config/types.go`


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


**Тип ответа:** endpointsliceconfig.EndpointSliceControllerConfiguration


```json
{
  "ConcurrentServiceEndpointSyncs": 0,
  "MaxEndpointsPerSlice": 0,
  "EndpointUpdatesBatchPeriod": {}
}
```


*Определено в:* `pkg/controller/endpointslice/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointslicecontroller.go:51`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/endpointslicecontroller.go:64 returns_error: нет description: Validate checks validation of EndpointSliceControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/endpointslicecontroller.go:64)


Validate checks validation of EndpointSliceControllerOptions.


```go
func (o *EndpointSliceControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointslicecontroller.go:64`




## cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsendpointslicemirroringcontrollergo43) `:43`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsendpointslicemirroringcontrollergo54) `:54`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsendpointslicemirroringcontrollergo67) `:67`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:43 returns_error: нет description: AddFlags adds flags related to EndpointSliceMirroringController for
controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:43)


AddFlags adds flags related to EndpointSliceMirroringController for
controller manager to the specified FlagSet.


```go
func (o *EndpointSliceMirroringControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:43`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:54 returns_error: нет description: ApplyTo fills up EndpointSliceMirroringController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:54)


ApplyTo fills up EndpointSliceMirroringController config with options.


```go
func (o *EndpointSliceMirroringControllerOptions) ApplyTo((cfg *endpointslicemirroringconfig.EndpointSliceMirroringControllerConfiguration)) (cfg *endpointslicemirroringconfig.EndpointSliceMirroringControllerConfiguration)
```


**Тип запроса:** endpointslicemirroringconfig.EndpointSliceMirroringControllerConfiguration


```json
{
  "MirroringConcurrentServiceEndpointSyncs": 0,
  "MirroringMaxEndpointsPerSubset": 0,
  "MirroringEndpointUpdatesBatchPeriod": {}
}
```


*Определено в:* `pkg/controller/endpointslicemirroring/config/types.go`


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


**Тип ответа:** endpointslicemirroringconfig.EndpointSliceMirroringControllerConfiguration


```json
{
  "MirroringConcurrentServiceEndpointSyncs": 0,
  "MirroringMaxEndpointsPerSubset": 0,
  "MirroringEndpointUpdatesBatchPeriod": {}
}
```


*Определено в:* `pkg/controller/endpointslicemirroring/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:54`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:67 returns_error: нет description: Validate checks validation of EndpointSliceMirroringControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:67)


Validate checks validation of EndpointSliceMirroringControllerOptions.


```go
func (o *EndpointSliceMirroringControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/endpointslicemirroringcontroller.go:67`




## cmd/kube-controller-manager/app/options/ephemeralcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/ephemeralcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsephemeralcontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsephemeralcontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsephemeralcontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/ephemeralcontroller.go:33 returns_error: нет description: AddFlags adds flags related to EphemeralVolumeController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/ephemeralcontroller.go:33)


AddFlags adds flags related to EphemeralVolumeController for controller manager to the specified FlagSet.


```go
func (o *EphemeralVolumeControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/ephemeralcontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/ephemeralcontroller.go:42 returns_error: нет description: ApplyTo fills up EphemeralVolumeController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/ephemeralcontroller.go:42)


ApplyTo fills up EphemeralVolumeController config with options.


```go
func (o *EphemeralVolumeControllerOptions) ApplyTo((cfg *ephemeralvolumeconfig.EphemeralVolumeControllerConfiguration)) (cfg *ephemeralvolumeconfig.EphemeralVolumeControllerConfiguration)
```


**Тип запроса:** ephemeralvolumeconfig.EphemeralVolumeControllerConfiguration


```json
{
  "ConcurrentEphemeralVolumeSyncs": 0
}
```


*Определено в:* `pkg/controller/volume/ephemeral/config/types.go`


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


**Тип ответа:** ephemeralvolumeconfig.EphemeralVolumeControllerConfiguration


```json
{
  "ConcurrentEphemeralVolumeSyncs": 0
}
```


*Определено в:* `pkg/controller/volume/ephemeral/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/ephemeralcontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/ephemeralcontroller.go:53 returns_error: нет description: Validate checks validation of EphemeralVolumeControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/ephemeralcontroller.go:53)


Validate checks validation of EphemeralVolumeControllerOptions.


```go
func (o *EphemeralVolumeControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/ephemeralcontroller.go:53`




## cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsgarbagecollectorcontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsgarbagecollectorcontrollergo41) `:41`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsgarbagecollectorcontrollergo54) `:54`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:31 returns_error: нет description: AddFlags adds flags related to GarbageCollectorController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:31)


AddFlags adds flags related to GarbageCollectorController for controller manager to the specified FlagSet.


```go
func (o *GarbageCollectorControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:41 returns_error: нет description: ApplyTo fills up GarbageCollectorController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:41)


ApplyTo fills up GarbageCollectorController config with options.


```go
func (o *GarbageCollectorControllerOptions) ApplyTo((cfg *garbagecollectorconfig.GarbageCollectorControllerConfiguration)) (cfg *garbagecollectorconfig.GarbageCollectorControllerConfiguration)
```


**Тип запроса:** garbagecollectorconfig.GarbageCollectorControllerConfiguration


```json
{
  "EnableGarbageCollector": false,
  "ConcurrentGCSyncs": 0,
  "GCIgnoredResources": []
}
```


*Определено в:* `pkg/controller/garbagecollector/config/types.go`


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


**Тип ответа:** garbagecollectorconfig.GarbageCollectorControllerConfiguration


```json
{
  "EnableGarbageCollector": false,
  "ConcurrentGCSyncs": 0,
  "GCIgnoredResources": []
}
```


*Определено в:* `pkg/controller/garbagecollector/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:41`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:54 returns_error: нет description: Validate checks validation of GarbageCollectorController.


### Validate (cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:54)


Validate checks validation of GarbageCollectorController.


```go
func (o *GarbageCollectorControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/garbagecollectorcontroller.go:54`




## cmd/kube-controller-manager/app/options/hpacontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/hpacontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionshpacontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionshpacontrollergo47) `:47`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionshpacontrollergo63) `:63`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/hpacontroller.go:33 returns_error: нет description: AddFlags adds flags related to HPAController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/hpacontroller.go:33)


AddFlags adds flags related to HPAController for controller manager to the specified FlagSet.


```go
func (o *HPAControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/hpacontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/hpacontroller.go:47 returns_error: нет description: ApplyTo fills up HPAController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/hpacontroller.go:47)


ApplyTo fills up HPAController config with options.


```go
func (o *HPAControllerOptions) ApplyTo((cfg *poautosclerconfig.HPAControllerConfiguration)) (cfg *poautosclerconfig.HPAControllerConfiguration)
```


**Тип запроса:** poautosclerconfig.HPAControllerConfiguration


```json
{
  "ConcurrentHorizontalPodAutoscalerSyncs": 0,
  "HorizontalPodAutoscalerSyncPeriod": {},
  "HorizontalPodAutoscalerDownscaleStabilizationWindow": {},
  "HorizontalPodAutoscalerTolerance": 0.0,
  "HorizontalPodAutoscalerCPUInitializationPeriod": {},
  "HorizontalPodAutoscalerInitialReadinessDelay": {}
}
```


*Определено в:* `pkg/controller/podautoscaler/config/types.go`


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


**Тип ответа:** poautosclerconfig.HPAControllerConfiguration


```json
{
  "ConcurrentHorizontalPodAutoscalerSyncs": 0,
  "HorizontalPodAutoscalerSyncPeriod": {},
  "HorizontalPodAutoscalerDownscaleStabilizationWindow": {},
  "HorizontalPodAutoscalerTolerance": 0.0,
  "HorizontalPodAutoscalerCPUInitializationPeriod": {},
  "HorizontalPodAutoscalerInitialReadinessDelay": {}
}
```


*Определено в:* `pkg/controller/podautoscaler/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/hpacontroller.go:47`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/hpacontroller.go:63 returns_error: нет description: Validate checks validation of HPAControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/hpacontroller.go:63)


Validate checks validation of HPAControllerOptions.


```go
func (o *HPAControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/hpacontroller.go:63`




## cmd/kube-controller-manager/app/options/jobcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/jobcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsjobcontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsjobcontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsjobcontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/jobcontroller.go:33 returns_error: нет description: AddFlags adds flags related to JobController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/jobcontroller.go:33)


AddFlags adds flags related to JobController for controller manager to the specified FlagSet.


```go
func (o *JobControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/jobcontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/jobcontroller.go:42 returns_error: нет description: ApplyTo fills up JobController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/jobcontroller.go:42)


ApplyTo fills up JobController config with options.


```go
func (o *JobControllerOptions) ApplyTo((cfg *jobconfig.JobControllerConfiguration)) (cfg *jobconfig.JobControllerConfiguration)
```


**Тип запроса:** jobconfig.JobControllerConfiguration


```json
{
  "ConcurrentJobSyncs": 0
}
```


*Определено в:* `pkg/controller/job/config/types.go`


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


**Тип ответа:** jobconfig.JobControllerConfiguration


```json
{
  "ConcurrentJobSyncs": 0
}
```


*Определено в:* `pkg/controller/job/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/jobcontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/jobcontroller.go:53 returns_error: нет description: Validate checks validation of JobControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/jobcontroller.go:53)


Validate checks validation of JobControllerOptions.


```go
func (o *JobControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/jobcontroller.go:53`




## cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionslegacyserviceaccounttokencleanergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionslegacyserviceaccounttokencleanergo40) `:40`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionslegacyserviceaccounttokencleanergo51) `:51`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:31 returns_error: нет description: AddFlags adds flags related to LegacySATokenCleaner for controller manager to the specified FlagSet


### AddFlags (cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:31)


AddFlags adds flags related to LegacySATokenCleaner for controller manager to the specified FlagSet


```go
func (o *LegacySATokenCleanerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:40 returns_error: нет description: ApplyTo fills up LegacySATokenCleaner config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:40)


ApplyTo fills up LegacySATokenCleaner config with options.


```go
func (o *LegacySATokenCleanerOptions) ApplyTo((cfg *serviceaccountconfig.LegacySATokenCleanerConfiguration)) (cfg *serviceaccountconfig.LegacySATokenCleanerConfiguration)
```


**Тип запроса:** serviceaccountconfig.LegacySATokenCleanerConfiguration


```json
{
  "CleanUpPeriod": {}
}
```


*Определено в:* `pkg/controller/serviceaccount/config/types.go`


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


**Тип ответа:** serviceaccountconfig.LegacySATokenCleanerConfiguration


```json
{
  "CleanUpPeriod": {}
}
```


*Определено в:* `pkg/controller/serviceaccount/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:40`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:51 returns_error: нет description: Validate checks validation of LegacySATokenCleanerOptions.


### Validate (cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:51)


Validate checks validation of LegacySATokenCleanerOptions.


```go
func (o *LegacySATokenCleanerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/legacyserviceaccounttokencleaner.go:51`




## cmd/kube-controller-manager/app/options/namespacecontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/namespacecontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsnamespacecontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsnamespacecontrollergo41) `:41`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsnamespacecontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/namespacecontroller.go:31 returns_error: нет description: AddFlags adds flags related to NamespaceController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/namespacecontroller.go:31)


AddFlags adds flags related to NamespaceController for controller manager to the specified FlagSet.


```go
func (o *NamespaceControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/namespacecontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/namespacecontroller.go:41 returns_error: нет description: ApplyTo fills up NamespaceController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/namespacecontroller.go:41)


ApplyTo fills up NamespaceController config with options.


```go
func (o *NamespaceControllerOptions) ApplyTo((cfg *namespaceconfig.NamespaceControllerConfiguration)) (cfg *namespaceconfig.NamespaceControllerConfiguration)
```


**Тип запроса:** namespaceconfig.NamespaceControllerConfiguration


```json
{
  "NamespaceSyncPeriod": {},
  "ConcurrentNamespaceSyncs": 0
}
```


*Определено в:* `pkg/controller/namespace/config/types.go`


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


**Тип ответа:** namespaceconfig.NamespaceControllerConfiguration


```json
{
  "NamespaceSyncPeriod": {},
  "ConcurrentNamespaceSyncs": 0
}
```


*Определено в:* `pkg/controller/namespace/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/namespacecontroller.go:41`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/namespacecontroller.go:53 returns_error: нет description: Validate checks validation of NamespaceControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/namespacecontroller.go:53)


Validate checks validation of NamespaceControllerOptions.


```go
func (o *NamespaceControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/namespacecontroller.go:53`




## cmd/kube-controller-manager/app/options/nodeipamcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/nodeipamcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsnodeipamcontrollergo34) `:34`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsnodeipamcontrollergo45) `:45`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsnodeipamcontrollergo67) `:67`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/nodeipamcontroller.go:34 returns_error: нет description: AddFlags adds flags related to NodeIpamController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/nodeipamcontroller.go:34)


AddFlags adds flags related to NodeIpamController for controller manager to the specified FlagSet.


```go
func (o *NodeIPAMControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/nodeipamcontroller.go:34`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/nodeipamcontroller.go:45 returns_error: нет description: ApplyTo fills up NodeIpamController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/nodeipamcontroller.go:45)


ApplyTo fills up NodeIpamController config with options.


```go
func (o *NodeIPAMControllerOptions) ApplyTo((cfg *nodeipamconfig.NodeIPAMControllerConfiguration)) (cfg *nodeipamconfig.NodeIPAMControllerConfiguration)
```


**Тип запроса:** nodeipamconfig.NodeIPAMControllerConfiguration


```json
{
  "ServiceCIDR": "string",
  "SecondaryServiceCIDR": "string",
  "NodeCIDRMaskSize": 0,
  "NodeCIDRMaskSizeIPv4": 0,
  "NodeCIDRMaskSizeIPv6": 0
}
```


*Определено в:* `pkg/controller/nodeipam/config/types.go`


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


**Тип ответа:** nodeipamconfig.NodeIPAMControllerConfiguration


```json
{
  "ServiceCIDR": "string",
  "SecondaryServiceCIDR": "string",
  "NodeCIDRMaskSize": 0,
  "NodeCIDRMaskSizeIPv4": 0,
  "NodeCIDRMaskSizeIPv6": 0
}
```


*Определено в:* `pkg/controller/nodeipam/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/nodeipamcontroller.go:45`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/nodeipamcontroller.go:67 returns_error: нет description: Validate checks validation of NodeIPAMControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/nodeipamcontroller.go:67)


Validate checks validation of NodeIPAMControllerOptions.


```go
func (o *NodeIPAMControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/nodeipamcontroller.go:67`




## cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsnodelifecyclecontrollergo34) `:34`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsnodelifecyclecontrollergo53) `:53`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsnodelifecyclecontrollergo69) `:69`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:34 returns_error: нет description: AddFlags adds flags related to NodeLifecycleController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:34)


AddFlags adds flags related to NodeLifecycleController for controller manager to the specified FlagSet.


```go
func (o *NodeLifecycleControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:34`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:53 returns_error: нет description: ApplyTo fills up NodeLifecycleController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:53)


ApplyTo fills up NodeLifecycleController config with options.


```go
func (o *NodeLifecycleControllerOptions) ApplyTo((cfg *nodelifecycleconfig.NodeLifecycleControllerConfiguration)) (cfg *nodelifecycleconfig.NodeLifecycleControllerConfiguration)
```


**Тип запроса:** nodelifecycleconfig.NodeLifecycleControllerConfiguration


```json
{
  "NodeEvictionRate": 0.0,
  "SecondaryNodeEvictionRate": 0.0,
  "NodeStartupGracePeriod": {},
  "NodeMonitorGracePeriod": {},
  "LargeClusterSizeThreshold": 0,
  "UnhealthyZoneThreshold": 0.0
}
```


*Определено в:* `pkg/controller/nodelifecycle/config/types.go`


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


**Тип ответа:** nodelifecycleconfig.NodeLifecycleControllerConfiguration


```json
{
  "NodeEvictionRate": 0.0,
  "SecondaryNodeEvictionRate": 0.0,
  "NodeStartupGracePeriod": {},
  "NodeMonitorGracePeriod": {},
  "LargeClusterSizeThreshold": 0,
  "UnhealthyZoneThreshold": 0.0
}
```


*Определено в:* `pkg/controller/nodelifecycle/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:53`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:69 returns_error: нет description: Validate checks validation of NodeLifecycleControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:69)


Validate checks validation of NodeLifecycleControllerOptions.


```go
func (o *NodeLifecycleControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/nodelifecyclecontroller.go:69`




## cmd/kube-controller-manager/app/options/options.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/options.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsoptionsgo322) `:322`

- 🔗 [Config](#config-cmdkube-controller-managerappoptionsoptionsgo494) `:494`

- 🔗 [Flags](#flags-cmdkube-controller-managerappoptionsoptionsgo267) `:267`

- 🔗 [NewDefaultComponentConfig](#newdefaultcomponentconfig-cmdkube-controller-managerappoptionsoptionsgo255) `:255`

- 🔗 [NewKubeControllerManagerOptions](#newkubecontrollermanageroptions-cmdkube-controller-managerappoptionsoptionsgo121) `:121`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsoptionsgo435) `:435`


</details>


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/options.go:322 returns_error: нет description: ApplyTo fills up controller manager config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/options.go:322)


ApplyTo fills up controller manager config with options.


```go
func (s *KubeControllerManagerOptions) ApplyTo((c *kubecontrollerconfig.Config, allControllers []string, disabledByDefaultControllers []string, controllerAliases map[string]string)) (c *kubecontrollerconfig.Config, allControllers []string, disabledByDefaultControllers []string, controllerAliases map[string]string)
```


**Тип запроса:** kubecontrollerconfig.Config


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


**Тип ответа:** kubecontrollerconfig.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** allControllers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** disabledByDefaultControllers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** controllerAliases


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/options.go:322`



---


[function] name: Config file: cmd/kube-controller-manager/app/options/options.go:494 returns_error: да description: Config return a controller manager config objective


### Config (cmd/kube-controller-manager/app/options/options.go:494)


Config return a controller manager config objective


```go
func (s KubeControllerManagerOptions) Config((*kubecontrollerconfig.Config, error)) (*kubecontrollerconfig.Config, error)
```


**Тип запроса:** kubecontrollerconfig.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** kubecontrollerconfig.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubecontrollerconfig.Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/options/options.go:494`



---


[function] name: Flags file: cmd/kube-controller-manager/app/options/options.go:267 returns_error: нет description: Flags returns flags for a specific KubeController by section name


### Flags (cmd/kube-controller-manager/app/options/options.go:267)


Flags returns flags for a specific KubeController by section name


```go
func (s *KubeControllerManagerOptions) Flags((allControllers []string, disabledByDefaultControllers []string, controllerAliases map[string]string)) (allControllers []string, disabledByDefaultControllers []string, controllerAliases map[string]string)
```


**Тип ответа:** allControllers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** disabledByDefaultControllers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** controllerAliases


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/options.go:267`



---


[function] name: NewDefaultComponentConfig file: cmd/kube-controller-manager/app/options/options.go:255 returns_error: да description: NewDefaultComponentConfig returns kube-controller manager configuration object.


### NewDefaultComponentConfig (cmd/kube-controller-manager/app/options/options.go:255)


NewDefaultComponentConfig returns kube-controller manager configuration object.


```go
func NewDefaultComponentConfig((kubectrlmgrconfig.KubeControllerManagerConfiguration, error)) (kubectrlmgrconfig.KubeControllerManagerConfiguration, error)
```


**Тип ответа:** kubectrlmgrconfig.KubeControllerManagerConfiguration


```json
{
  "Generic": {},
  "KubeCloudShared": {},
  "AttachDetachController": {},
  "CronJobController": {},
  "CSRSigningController": {},
  "DaemonSetController": {},
  "DeploymentController": {},
  "DeviceTaintEvictionController": {},
  "DeprecatedController": {},
  "EndpointController": {},
  "EndpointSliceController": {},
  "EndpointSliceMirroringController": {},
  "EphemeralVolumeController": {},
  "GarbageCollectorController": {},
  "HPAController": {},
  "JobController": {},
  "LegacySATokenCleaner": {},
  "NamespaceController": {},
  "NodeIPAMController": {},
  "NodeLifecycleController": {},
  "PersistentVolumeBinderController": {},
  "PodGCController": {},
  "ReplicaSetController": {},
  "ReplicationController": {},
  "ResourceQuotaController": {},
  "SAController": {},
  "ServiceController": {},
  "StatefulSetController": {},
  "TTLAfterFinishedController": {},
  "ValidatingAdmissionPolicyStatusController": {},
  "ResourceClaimController": {}
}
```


*Определено в:* `pkg/controller/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `kubectrlmgrconfig.KubeControllerManagerConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/options/options.go:255`



---


[function] name: NewKubeControllerManagerOptions file: cmd/kube-controller-manager/app/options/options.go:121 returns_error: да description: NewKubeControllerManagerOptions creates a new KubeControllerManagerOptions with a default config.


### NewKubeControllerManagerOptions (cmd/kube-controller-manager/app/options/options.go:121)


NewKubeControllerManagerOptions creates a new KubeControllerManagerOptions with a default config.


```go
func NewKubeControllerManagerOptions((*KubeControllerManagerOptions, error)) (*KubeControllerManagerOptions, error)
```


**Тип запроса:** KubeControllerManagerOptions


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


**Тип ответа:** KubeControllerManagerOptions


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*KubeControllerManagerOptions`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/options/options.go:121`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/options.go:435 returns_error: нет description: Validate is used to validate the options and config before launching the controller manager


### Validate (cmd/kube-controller-manager/app/options/options.go:435)


Validate is used to validate the options and config before launching the controller manager


```go
func (s *KubeControllerManagerOptions) Validate((allControllers []string, disabledByDefaultControllers []string, controllerAliases map[string]string)) (allControllers []string, disabledByDefaultControllers []string, controllerAliases map[string]string)
```


**Тип ответа:** allControllers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** disabledByDefaultControllers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** controllerAliases


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/options.go:435`




## cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionspersistentvolumebindercontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionspersistentvolumebindercontrollergo49) `:49`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionspersistentvolumebindercontrollergo61) `:61`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:31 returns_error: нет description: AddFlags adds flags related to PersistentVolumeBinderController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:31)


AddFlags adds flags related to PersistentVolumeBinderController for controller manager to the specified FlagSet.


```go
func (o *PersistentVolumeBinderControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:49 returns_error: нет description: ApplyTo fills up PersistentVolumeBinderController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:49)


ApplyTo fills up PersistentVolumeBinderController config with options.


```go
func (o *PersistentVolumeBinderControllerOptions) ApplyTo((cfg *persistentvolumeconfig.PersistentVolumeBinderControllerConfiguration)) (cfg *persistentvolumeconfig.PersistentVolumeBinderControllerConfiguration)
```


**Тип запроса:** persistentvolumeconfig.PersistentVolumeBinderControllerConfiguration


```json
{
  "PVClaimBinderSyncPeriod": {},
  "VolumeConfiguration": {}
}
```


*Определено в:* `pkg/controller/volume/persistentvolume/config/types.go`


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


**Тип ответа:** persistentvolumeconfig.PersistentVolumeBinderControllerConfiguration


```json
{
  "PVClaimBinderSyncPeriod": {},
  "VolumeConfiguration": {}
}
```


*Определено в:* `pkg/controller/volume/persistentvolume/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:49`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:61 returns_error: нет description: Validate checks validation of PersistentVolumeBinderControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:61)


Validate checks validation of PersistentVolumeBinderControllerOptions.


```go
func (o *PersistentVolumeBinderControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/persistentvolumebindercontroller.go:61`




## cmd/kube-controller-manager/app/options/podgccontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/podgccontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionspodgccontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionspodgccontrollergo40) `:40`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionspodgccontrollergo51) `:51`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/podgccontroller.go:31 returns_error: нет description: AddFlags adds flags related to PodGCController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/podgccontroller.go:31)


AddFlags adds flags related to PodGCController for controller manager to the specified FlagSet.


```go
func (o *PodGCControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/podgccontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/podgccontroller.go:40 returns_error: нет description: ApplyTo fills up PodGCController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/podgccontroller.go:40)


ApplyTo fills up PodGCController config with options.


```go
func (o *PodGCControllerOptions) ApplyTo((cfg *podgcconfig.PodGCControllerConfiguration)) (cfg *podgcconfig.PodGCControllerConfiguration)
```


**Тип запроса:** podgcconfig.PodGCControllerConfiguration


```json
{
  "TerminatedPodGCThreshold": 0
}
```


*Определено в:* `pkg/controller/podgc/config/types.go`


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


**Тип ответа:** podgcconfig.PodGCControllerConfiguration


```json
{
  "TerminatedPodGCThreshold": 0
}
```


*Определено в:* `pkg/controller/podgc/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/podgccontroller.go:40`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/podgccontroller.go:51 returns_error: нет description: Validate checks validation of PodGCControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/podgccontroller.go:51)


Validate checks validation of PodGCControllerOptions.


```go
func (o *PodGCControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/podgccontroller.go:51`




## cmd/kube-controller-manager/app/options/replicasetcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/replicasetcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsreplicasetcontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsreplicasetcontrollergo40) `:40`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsreplicasetcontrollergo51) `:51`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/replicasetcontroller.go:31 returns_error: нет description: AddFlags adds flags related to ReplicaSetController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/replicasetcontroller.go:31)


AddFlags adds flags related to ReplicaSetController for controller manager to the specified FlagSet.


```go
func (o *ReplicaSetControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/replicasetcontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/replicasetcontroller.go:40 returns_error: нет description: ApplyTo fills up ReplicaSetController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/replicasetcontroller.go:40)


ApplyTo fills up ReplicaSetController config with options.


```go
func (o *ReplicaSetControllerOptions) ApplyTo((cfg *replicasetconfig.ReplicaSetControllerConfiguration)) (cfg *replicasetconfig.ReplicaSetControllerConfiguration)
```


**Тип запроса:** replicasetconfig.ReplicaSetControllerConfiguration


```json
{
  "ConcurrentRSSyncs": 0
}
```


*Определено в:* `pkg/controller/replicaset/config/types.go`


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


**Тип ответа:** replicasetconfig.ReplicaSetControllerConfiguration


```json
{
  "ConcurrentRSSyncs": 0
}
```


*Определено в:* `pkg/controller/replicaset/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/replicasetcontroller.go:40`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/replicasetcontroller.go:51 returns_error: нет description: Validate checks validation of ReplicaSetControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/replicasetcontroller.go:51)


Validate checks validation of ReplicaSetControllerOptions.


```go
func (o *ReplicaSetControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/replicasetcontroller.go:51`




## cmd/kube-controller-manager/app/options/replicationcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/replicationcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsreplicationcontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsreplicationcontrollergo40) `:40`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsreplicationcontrollergo51) `:51`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/replicationcontroller.go:31 returns_error: нет description: AddFlags adds flags related to ReplicationController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/replicationcontroller.go:31)


AddFlags adds flags related to ReplicationController for controller manager to the specified FlagSet.


```go
func (o *ReplicationControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/replicationcontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/replicationcontroller.go:40 returns_error: нет description: ApplyTo fills up ReplicationController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/replicationcontroller.go:40)


ApplyTo fills up ReplicationController config with options.


```go
func (o *ReplicationControllerOptions) ApplyTo((cfg *replicationconfig.ReplicationControllerConfiguration)) (cfg *replicationconfig.ReplicationControllerConfiguration)
```


**Тип запроса:** replicationconfig.ReplicationControllerConfiguration


```json
{
  "ConcurrentRCSyncs": 0
}
```


*Определено в:* `pkg/controller/replication/config/types.go`


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


**Тип ответа:** replicationconfig.ReplicationControllerConfiguration


```json
{
  "ConcurrentRCSyncs": 0
}
```


*Определено в:* `pkg/controller/replication/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/replicationcontroller.go:40`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/replicationcontroller.go:51 returns_error: нет description: Validate checks validation of ReplicationControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/replicationcontroller.go:51)


Validate checks validation of ReplicationControllerOptions.


```go
func (o *ReplicationControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/replicationcontroller.go:51`




## cmd/kube-controller-manager/app/options/resourceclaimcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/resourceclaimcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsresourceclaimcontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsresourceclaimcontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsresourceclaimcontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:33 returns_error: нет description: AddFlags adds flags related to ResourceClaimController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:33)


AddFlags adds flags related to ResourceClaimController for controller manager to the specified FlagSet.


```go
func (o *ResourceClaimControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:42 returns_error: нет description: ApplyTo fills up ResourceClaimController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:42)


ApplyTo fills up ResourceClaimController config with options.


```go
func (o *ResourceClaimControllerOptions) ApplyTo((cfg *resourceclaimconfig.ResourceClaimControllerConfiguration)) (cfg *resourceclaimconfig.ResourceClaimControllerConfiguration)
```


**Тип запроса:** resourceclaimconfig.ResourceClaimControllerConfiguration


```json
{
  "ConcurrentSyncs": 0
}
```


*Определено в:* `pkg/controller/resourceclaim/config/types.go`


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


**Тип ответа:** resourceclaimconfig.ResourceClaimControllerConfiguration


```json
{
  "ConcurrentSyncs": 0
}
```


*Определено в:* `pkg/controller/resourceclaim/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:53 returns_error: нет description: Validate checks validation of ResourceClaimControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:53)


Validate checks validation of ResourceClaimControllerOptions.


```go
func (o *ResourceClaimControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/resourceclaimcontroller.go:53`




## cmd/kube-controller-manager/app/options/resourcequotacontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/resourcequotacontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsresourcequotacontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsresourcequotacontrollergo41) `:41`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsresourcequotacontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/resourcequotacontroller.go:31 returns_error: нет description: AddFlags adds flags related to ResourceQuotaController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/resourcequotacontroller.go:31)


AddFlags adds flags related to ResourceQuotaController for controller manager to the specified FlagSet.


```go
func (o *ResourceQuotaControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/resourcequotacontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/resourcequotacontroller.go:41 returns_error: нет description: ApplyTo fills up ResourceQuotaController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/resourcequotacontroller.go:41)


ApplyTo fills up ResourceQuotaController config with options.


```go
func (o *ResourceQuotaControllerOptions) ApplyTo((cfg *resourcequotaconfig.ResourceQuotaControllerConfiguration)) (cfg *resourcequotaconfig.ResourceQuotaControllerConfiguration)
```


**Тип запроса:** resourcequotaconfig.ResourceQuotaControllerConfiguration


```json
{
  "ResourceQuotaSyncPeriod": {},
  "ConcurrentResourceQuotaSyncs": 0
}
```


*Определено в:* `pkg/controller/resourcequota/config/types.go`


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


**Тип ответа:** resourcequotaconfig.ResourceQuotaControllerConfiguration


```json
{
  "ResourceQuotaSyncPeriod": {},
  "ConcurrentResourceQuotaSyncs": 0
}
```


*Определено в:* `pkg/controller/resourcequota/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/resourcequotacontroller.go:41`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/resourcequotacontroller.go:53 returns_error: нет description: Validate checks validation of ResourceQuotaControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/resourcequotacontroller.go:53)


Validate checks validation of ResourceQuotaControllerOptions.


```go
func (o *ResourceQuotaControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/resourcequotacontroller.go:53`




## cmd/kube-controller-manager/app/options/serviceaccountcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/serviceaccountcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsserviceaccountcontrollergo31) `:31`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsserviceaccountcontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsserviceaccountcontrollergo55) `:55`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:31 returns_error: нет description: AddFlags adds flags related to ServiceAccountController for controller manager to the specified FlagSet


### AddFlags (cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:31)


AddFlags adds flags related to ServiceAccountController for controller manager to the specified FlagSet


```go
func (o *SAControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:31`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:42 returns_error: нет description: ApplyTo fills up ServiceAccountController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:42)


ApplyTo fills up ServiceAccountController config with options.


```go
func (o *SAControllerOptions) ApplyTo((cfg *serviceaccountconfig.SAControllerConfiguration)) (cfg *serviceaccountconfig.SAControllerConfiguration)
```


**Тип запроса:** serviceaccountconfig.SAControllerConfiguration


```json
{
  "ServiceAccountKeyFile": "string",
  "ConcurrentSATokenSyncs": 0,
  "RootCAFile": "string"
}
```


*Определено в:* `pkg/controller/serviceaccount/config/types.go`


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


**Тип ответа:** serviceaccountconfig.SAControllerConfiguration


```json
{
  "ServiceAccountKeyFile": "string",
  "ConcurrentSATokenSyncs": 0,
  "RootCAFile": "string"
}
```


*Определено в:* `pkg/controller/serviceaccount/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:55 returns_error: нет description: Validate checks validation of ServiceAccountControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:55)


Validate checks validation of ServiceAccountControllerOptions.


```go
func (o *SAControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/serviceaccountcontroller.go:55`




## cmd/kube-controller-manager/app/options/statefulsetcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/statefulsetcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsstatefulsetcontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsstatefulsetcontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsstatefulsetcontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/statefulsetcontroller.go:33 returns_error: нет description: AddFlags adds flags related to StatefulSetController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/statefulsetcontroller.go:33)


AddFlags adds flags related to StatefulSetController for controller manager to the specified FlagSet.


```go
func (o *StatefulSetControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/statefulsetcontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/statefulsetcontroller.go:42 returns_error: нет description: ApplyTo fills up StatefulSetController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/statefulsetcontroller.go:42)


ApplyTo fills up StatefulSetController config with options.


```go
func (o *StatefulSetControllerOptions) ApplyTo((cfg *statefulsetconfig.StatefulSetControllerConfiguration)) (cfg *statefulsetconfig.StatefulSetControllerConfiguration)
```


**Тип запроса:** statefulsetconfig.StatefulSetControllerConfiguration


```json
{
  "ConcurrentStatefulSetSyncs": 0
}
```


*Определено в:* `pkg/controller/statefulset/config/types.go`


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


**Тип ответа:** statefulsetconfig.StatefulSetControllerConfiguration


```json
{
  "ConcurrentStatefulSetSyncs": 0
}
```


*Определено в:* `pkg/controller/statefulset/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/statefulsetcontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/statefulsetcontroller.go:53 returns_error: нет description: Validate checks validation of StatefulSetControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/statefulsetcontroller.go:53)


Validate checks validation of StatefulSetControllerOptions.


```go
func (o *StatefulSetControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/statefulsetcontroller.go:53`




## cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsttlafterfinishedcontrollergo34) `:34`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsttlafterfinishedcontrollergo43) `:43`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsttlafterfinishedcontrollergo54) `:54`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:34 returns_error: нет description: AddFlags adds flags related to TTLAfterFinishedController for controller manager to the specified FlagSet.


### AddFlags (cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:34)


AddFlags adds flags related to TTLAfterFinishedController for controller manager to the specified FlagSet.


```go
func (o *TTLAfterFinishedControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:34`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:43 returns_error: нет description: ApplyTo fills up TTLAfterFinishedController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:43)


ApplyTo fills up TTLAfterFinishedController config with options.


```go
func (o *TTLAfterFinishedControllerOptions) ApplyTo((cfg *ttlafterfinishedconfig.TTLAfterFinishedControllerConfiguration)) (cfg *ttlafterfinishedconfig.TTLAfterFinishedControllerConfiguration)
```


**Тип запроса:** ttlafterfinishedconfig.TTLAfterFinishedControllerConfiguration


```json
{
  "ConcurrentTTLSyncs": 0
}
```


*Определено в:* `pkg/controller/ttlafterfinished/config/types.go`


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


**Тип ответа:** ttlafterfinishedconfig.TTLAfterFinishedControllerConfiguration


```json
{
  "ConcurrentTTLSyncs": 0
}
```


*Определено в:* `pkg/controller/ttlafterfinished/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:43`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:54 returns_error: нет description: Validate checks validation of TTLAfterFinishedControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:54)


Validate checks validation of TTLAfterFinishedControllerOptions.


```go
func (o *TTLAfterFinishedControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/ttlafterfinishedcontroller.go:54`




## cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go


📄 Исходный файл: `cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddFlags](#addflags-cmdkube-controller-managerappoptionsvalidatingadmissionpolicycontrollergo33) `:33`

- 🔗 [ApplyTo](#applyto-cmdkube-controller-managerappoptionsvalidatingadmissionpolicycontrollergo42) `:42`

- 🔗 [Validate](#validate-cmdkube-controller-managerappoptionsvalidatingadmissionpolicycontrollergo53) `:53`


</details>


[function] name: AddFlags file: cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:33 returns_error: нет description: AddFlags adds flags related to ValidatingAdmissionPolicyStatusController for controller manager to the specified FlagSet


### AddFlags (cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:33)


AddFlags adds flags related to ValidatingAdmissionPolicyStatusController for controller manager to the specified FlagSet.


```go
func (o *ValidatingAdmissionPolicyStatusControllerOptions) AddFlags((fs *pflag.FlagSet)) (fs *pflag.FlagSet)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:33`



---


[function] name: ApplyTo file: cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:42 returns_error: нет description: ApplyTo fills up ValidatingAdmissionPolicyStatusController config with options.


### ApplyTo (cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:42)


ApplyTo fills up ValidatingAdmissionPolicyStatusController config with options.


```go
func (o *ValidatingAdmissionPolicyStatusControllerOptions) ApplyTo((cfg *validatingadmissionpolicystatusconfig.ValidatingAdmissionPolicyStatusControllerConfiguration)) (cfg *validatingadmissionpolicystatusconfig.ValidatingAdmissionPolicyStatusControllerConfiguration)
```


**Тип запроса:** validatingadmissionpolicystatusconfig.ValidatingAdmissionPolicyStatusControllerConfiguration


```json
{
  "ConcurrentPolicySyncs": 0
}
```


*Определено в:* `pkg/controller/validatingadmissionpolicystatus/config/types.go`


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


**Тип ответа:** validatingadmissionpolicystatusconfig.ValidatingAdmissionPolicyStatusControllerConfiguration


```json
{
  "ConcurrentPolicySyncs": 0
}
```


*Определено в:* `pkg/controller/validatingadmissionpolicystatus/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:42`



---


[function] name: Validate file: cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:53 returns_error: нет description: Validate checks validation of ValidatingAdmissionPolicyStatusControllerOptions.


### Validate (cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:53)


Validate checks validation of ValidatingAdmissionPolicyStatusControllerOptions.


```go
func (o *ValidatingAdmissionPolicyStatusControllerOptions) Validate(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/options/validatingadmissionpolicycontroller.go:53`




## cmd/kube-controller-manager/app/plugins.go


📄 Исходный файл: `cmd/kube-controller-manager/app/plugins.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [AttemptToLoadRecycler](#attempttoloadrecycler-cmdkube-controller-managerapppluginsgo143) `:143`

- 🔗 [GetDynamicPluginProber](#getdynamicpluginprober-cmdkube-controller-managerapppluginsgo54) `:54`

- 🔗 [ProbeAttachableVolumePlugins](#probeattachablevolumeplugins-cmdkube-controller-managerapppluginsgo44) `:44`

- 🔗 [ProbeExpandableVolumePlugins](#probeexpandablevolumeplugins-cmdkube-controller-managerapppluginsgo59) `:59`

- 🔗 [ProbePersistentVolumePlugins](#probepersistentvolumeplugins-cmdkube-controller-managerapppluginsgo82) `:82`

- 🔗 [ProbeProvisionableRecyclableVolumePlugins](#probeprovisionablerecyclablevolumeplugins-cmdkube-controller-managerapppluginsgo66) `:66`

- 🔗 [probeControllerVolumePlugins](#probecontrollervolumeplugins-cmdkube-controller-managerapppluginsgo88) `:88`


</details>


[function] name: AttemptToLoadRecycler file: cmd/kube-controller-manager/app/plugins.go:143 returns_error: нет description: AttemptToLoadRecycler tries decoding a pod from a filepath for use as a recycler for a volume.
If successful, this metho


### AttemptToLoadRecycler (cmd/kube-controller-manager/app/plugins.go:143)


AttemptToLoadRecycler tries decoding a pod from a filepath for use as a recycler for a volume.
If successful, this method will set the recycler on the config.
If unsuccessful, an error is returned. Function is exported for reuse downstream.


```go
func AttemptToLoadRecycler((path string, config *volume.VolumeConfig)) (path string, config *volume.VolumeConfig)
```


**Тип запроса:** volume.VolumeConfig


```json
{
  "RecyclerPodTemplate": null,
  "RecyclerMinimumTimeout": 0,
  "RecyclerTimeoutIncrement": 0,
  "PVName": "string",
  "OtherAttributes": {},
  "ProvisioningEnabled": false
}
```


*Определено в:* `pkg/volume/plugins.go`


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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** volume.VolumeConfig


```json
{
  "RecyclerPodTemplate": null,
  "RecyclerMinimumTimeout": 0,
  "RecyclerTimeoutIncrement": 0,
  "PVName": "string",
  "OtherAttributes": {},
  "ProvisioningEnabled": false
}
```


*Определено в:* `pkg/volume/plugins.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/plugins.go:143`



---


[function] name: GetDynamicPluginProber file: cmd/kube-controller-manager/app/plugins.go:54 returns_error: нет description: GetDynamicPluginProber gets the probers of dynamically discoverable plugins
for the attach/detach controller.
Currently 


### GetDynamicPluginProber (cmd/kube-controller-manager/app/plugins.go:54)


GetDynamicPluginProber gets the probers of dynamically discoverable plugins
for the attach/detach controller.
Currently only Flexvolume plugins are dynamically discoverable.


```go
func GetDynamicPluginProber((config persistentvolumeconfig.VolumeConfiguration)) (config persistentvolumeconfig.VolumeConfiguration)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** persistentvolumeconfig.VolumeConfiguration


```json
{
  "EnableHostPathProvisioning": false,
  "EnableDynamicProvisioning": false,
  "PersistentVolumeRecyclerConfiguration": {},
  "FlexVolumePluginDir": "string"
}
```


*Определено в:* `pkg/controller/volume/persistentvolume/config/types.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/plugins.go:54`



---


[function] name: ProbeAttachableVolumePlugins file: cmd/kube-controller-manager/app/plugins.go:44 returns_error: да description: ProbeAttachableVolumePlugins collects all volume plugins for the attach/
detach controller.


### ProbeAttachableVolumePlugins (cmd/kube-controller-manager/app/plugins.go:44)


ProbeAttachableVolumePlugins collects all volume plugins for the attach/
detach controller.


```go
func ProbeAttachableVolumePlugins(([]volume.VolumePlugin, error)) ([]volume.VolumePlugin, error)
```


**Тип ответа:** volume.VolumePlugin


```json
{
  "mutex": {},
  "plugins": {},
  "prober": {},
  "probedPlugins": {},
  "Host": {}
}
```


*Определено в:* `pkg/volume/plugins.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]volume.VolumePlugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/plugins.go:44`



---


[function] name: ProbeExpandableVolumePlugins file: cmd/kube-controller-manager/app/plugins.go:59 returns_error: да description: ProbeExpandableVolumePlugins returns volume plugins which are expandable


### ProbeExpandableVolumePlugins (cmd/kube-controller-manager/app/plugins.go:59)


ProbeExpandableVolumePlugins returns volume plugins which are expandable


```go
func ProbeExpandableVolumePlugins(([]volume.VolumePlugin, error)) ([]volume.VolumePlugin, error)
```


**Тип ответа:** volume.VolumePlugin


```json
{
  "mutex": {},
  "plugins": {},
  "prober": {},
  "probedPlugins": {},
  "Host": {}
}
```


*Определено в:* `pkg/volume/plugins.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]volume.VolumePlugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/plugins.go:59`



---


[function] name: ProbePersistentVolumePlugins file: cmd/kube-controller-manager/app/plugins.go:82 returns_error: да description: ProbePersistentVolumePlugins collects all volume plugins that are actually persistent.


### ProbePersistentVolumePlugins (cmd/kube-controller-manager/app/plugins.go:82)


ProbePersistentVolumePlugins collects all volume plugins that are actually persistent.


```go
func ProbePersistentVolumePlugins(([]volume.VolumePlugin, error)) ([]volume.VolumePlugin, error)
```


**Тип ответа:** volume.VolumePlugin


```json
{
  "mutex": {},
  "plugins": {},
  "prober": {},
  "probedPlugins": {},
  "Host": {}
}
```


*Определено в:* `pkg/volume/plugins.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]volume.VolumePlugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/plugins.go:82`



---


[function] name: ProbeProvisionableRecyclableVolumePlugins file: cmd/kube-controller-manager/app/plugins.go:66 returns_error: да description: —


### ProbeProvisionableRecyclableVolumePlugins (cmd/kube-controller-manager/app/plugins.go:66)


ProbeProvisionableRecyclableVolumePlugins is a function that performs operations based on the provided parameters and may return an error.


```go
func ProbeProvisionableRecyclableVolumePlugins(([]volume.VolumePlugin, error)) ([]volume.VolumePlugin, error)
```


**Тип ответа:** volume.VolumePlugin


```json
{
  "mutex": {},
  "plugins": {},
  "prober": {},
  "probedPlugins": {},
  "Host": {}
}
```


*Определено в:* `pkg/volume/plugins.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]volume.VolumePlugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/plugins.go:66`



---


[function] name: probeControllerVolumePlugins file: cmd/kube-controller-manager/app/plugins.go:88 returns_error: да description: probeControllerVolumePlugins collects all persistent volume plugins
used by KCM controllers into an easy to use list.


### probeControllerVolumePlugins (cmd/kube-controller-manager/app/plugins.go:88)


probeControllerVolumePlugins collects all persistent volume plugins
used by KCM controllers into an easy to use list.


```go
func probeControllerVolumePlugins(([]volume.VolumePlugin, error)) ([]volume.VolumePlugin, error)
```


**Тип ответа:** volume.VolumePlugin


```json
{
  "mutex": {},
  "plugins": {},
  "prober": {},
  "probedPlugins": {},
  "Host": {}
}
```


*Определено в:* `pkg/volume/plugins.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]volume.VolumePlugin`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/plugins.go:88`




## cmd/kube-controller-manager/app/policy.go


📄 Исходный файл: `cmd/kube-controller-manager/app/policy.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [newDisruptionController](#newdisruptioncontroller-cmdkube-controller-managerapppolicygo38) `:38`

- 🔗 [newDisruptionControllerDescriptor](#newdisruptioncontrollerdescriptor-cmdkube-controller-managerapppolicygo30) `:30`


</details>


[function] name: newDisruptionController file: cmd/kube-controller-manager/app/policy.go:38 returns_error: да description: —


### newDisruptionController (cmd/kube-controller-manager/app/policy.go:38)


newDisruptionController is a function that performs operations based on the provided parameters and may return an error.


```go
func newDisruptionController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/policy.go:38`



---


[function] name: newDisruptionControllerDescriptor file: cmd/kube-controller-manager/app/policy.go:30 returns_error: нет description: —


### newDisruptionControllerDescriptor (cmd/kube-controller-manager/app/policy.go:30)


newDisruptionControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newDisruptionControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/policy.go:30`




## cmd/kube-controller-manager/app/rbac.go


📄 Исходный файл: `cmd/kube-controller-manager/app/rbac.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [newClusterRoleAggregationController](#newclusterroleaggregationcontroller-cmdkube-controller-managerapprbacgo34) `:34`

- 🔗 [newClusterRoleAggregrationControllerDescriptor](#newclusterroleaggregrationcontrollerdescriptor-cmdkube-controller-managerapprbacgo26) `:26`


</details>


[function] name: newClusterRoleAggregationController file: cmd/kube-controller-manager/app/rbac.go:34 returns_error: да description: —


### newClusterRoleAggregationController (cmd/kube-controller-manager/app/rbac.go:34)


newClusterRoleAggregationController is a function that performs operations based on the provided parameters and may return an error.


```go
func newClusterRoleAggregationController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/rbac.go:34`



---


[function] name: newClusterRoleAggregrationControllerDescriptor file: cmd/kube-controller-manager/app/rbac.go:26 returns_error: нет description: —


### newClusterRoleAggregrationControllerDescriptor (cmd/kube-controller-manager/app/rbac.go:26)


newClusterRoleAggregrationControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newClusterRoleAggregrationControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/rbac.go:26`




## cmd/kube-controller-manager/app/service_accounts.go


📄 Исходный файл: `cmd/kube-controller-manager/app/service_accounts.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [newServiceAccountTokenController](#newserviceaccounttokencontroller-cmdkube-controller-managerappservice_accountsgo45) `:45`

- 🔗 [newServiceAccountTokenControllerDescriptor](#newserviceaccounttokencontrollerdescriptor-cmdkube-controller-managerappservice_accountsgo33) `:33`


</details>


[function] name: newServiceAccountTokenController file: cmd/kube-controller-manager/app/service_accounts.go:45 returns_error: да description: —


### newServiceAccountTokenController (cmd/kube-controller-manager/app/service_accounts.go:45)


newServiceAccountTokenController is a function that performs operations based on the provided parameters and may return an error.


```go
func newServiceAccountTokenController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/service_accounts.go:45`



---


[function] name: newServiceAccountTokenControllerDescriptor file: cmd/kube-controller-manager/app/service_accounts.go:33 returns_error: нет description: serviceAccountTokenController is special because it must run first to set up permissions for other controllers.
It canno


### newServiceAccountTokenControllerDescriptor (cmd/kube-controller-manager/app/service_accounts.go:33)


serviceAccountTokenController is special because it must run first to set up permissions for other controllers.
It cannot use the "normal" client builder, so it tracks its own.


```go
func newServiceAccountTokenControllerDescriptor((rootClientBuilder clientbuilder.ControllerClientBuilder)) (rootClientBuilder clientbuilder.ControllerClientBuilder)
```


**Тип ответа:** rootClientBuilder


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clientbuilder.ControllerClientBuilder


```json
{
  "ClientConfig": null
}
```


*Определено в:* `staging/src/k8s.io/controller-manager/pkg/clientbuilder/client_builder.go`


📍 *Расположение:* `cmd/kube-controller-manager/app/service_accounts.go:33`




## cmd/kube-controller-manager/app/storageversionmigrator.go


📄 Исходный файл: `cmd/kube-controller-manager/app/storageversionmigrator.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [newSVMController](#newsvmcontroller-cmdkube-controller-managerappstorageversionmigratorgo41) `:41`

- 🔗 [newStorageVersionMigratorControllerDescriptor](#newstorageversionmigratorcontrollerdescriptor-cmdkube-controller-managerappstorageversionmigratorgo33) `:33`


</details>


[function] name: newSVMController file: cmd/kube-controller-manager/app/storageversionmigrator.go:41 returns_error: да description: —


### newSVMController (cmd/kube-controller-manager/app/storageversionmigrator.go:41)


newSVMController is a function that performs operations based on the provided parameters and may return an error.


```go
func newSVMController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/storageversionmigrator.go:41`



---


[function] name: newStorageVersionMigratorControllerDescriptor file: cmd/kube-controller-manager/app/storageversionmigrator.go:33 returns_error: нет description: —


### newStorageVersionMigratorControllerDescriptor (cmd/kube-controller-manager/app/storageversionmigrator.go:33)


newStorageVersionMigratorControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newStorageVersionMigratorControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/storageversionmigrator.go:33`




## cmd/kube-controller-manager/app/testing/testserver.go


📄 Исходный файл: `cmd/kube-controller-manager/app/testing/testserver.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [StartTestServer](#starttestserver-cmdkube-controller-managerapptestingtestservergo66) `:66`

- 🔗 [StartTestServerOrDie](#starttestserverordie-cmdkube-controller-managerapptestingtestservergo192) `:192`

- 🔗 [createListenerOnFreePort](#createlisteneronfreeport-cmdkube-controller-managerapptestingtestservergo200) `:200`

- 🔗 [init](#init-cmdkube-controller-managerapptestingtestservergo42) `:42`


</details>


[function] name: StartTestServer file: cmd/kube-controller-manager/app/testing/testserver.go:66 returns_error: да description: StartTestServer starts a kube-controller-manager. A rest client config and a tear-down func,
and location of the tmpdir 


### StartTestServer (cmd/kube-controller-manager/app/testing/testserver.go:66)


StartTestServer starts a kube-controller-manager. A rest client config and a tear-down func,
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


📍 *Расположение:* `cmd/kube-controller-manager/app/testing/testserver.go:66`



---


[function] name: StartTestServerOrDie file: cmd/kube-controller-manager/app/testing/testserver.go:192 returns_error: нет description: StartTestServerOrDie calls StartTestServer t.Fatal if it does not succeed.


### StartTestServerOrDie (cmd/kube-controller-manager/app/testing/testserver.go:192)


StartTestServerOrDie calls StartTestServer t.Fatal if it does not succeed.


```go
func StartTestServerOrDie((t *testing.T, ctx context.Context, flags []string)) (t *testing.T, ctx context.Context, flags []string)
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


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/kube-controller-manager/app/testing/testserver.go:192`



---


[function] name: createListenerOnFreePort file: cmd/kube-controller-manager/app/testing/testserver.go:200 returns_error: да description: —


### createListenerOnFreePort (cmd/kube-controller-manager/app/testing/testserver.go:200)


createListenerOnFreePort is a function that performs operations based on the provided parameters and may return an error.


```go
func createListenerOnFreePort((net.Listener, int, error)) (net.Listener, int, error)
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


📍 *Расположение:* `cmd/kube-controller-manager/app/testing/testserver.go:200`



---


[function] name: init file: cmd/kube-controller-manager/app/testing/testserver.go:42 returns_error: нет description: —


### init (cmd/kube-controller-manager/app/testing/testserver.go:42)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/testing/testserver.go:42`




## cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go


📄 Исходный файл: `cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [newValidatingAdmissionPolicyStatusController](#newvalidatingadmissionpolicystatuscontroller-cmdkube-controller-managerappvalidatingadmissionpolicystatusgo41) `:41`

- 🔗 [newValidatingAdmissionPolicyStatusControllerDescriptor](#newvalidatingadmissionpolicystatuscontrollerdescriptor-cmdkube-controller-managerappvalidatingadmissionpolicystatusgo33) `:33`


</details>


[function] name: newValidatingAdmissionPolicyStatusController file: cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go:41 returns_error: да description: —


### newValidatingAdmissionPolicyStatusController (cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go:41)


newValidatingAdmissionPolicyStatusController is a function that performs operations based on the provided parameters and may return an error.


```go
func newValidatingAdmissionPolicyStatusController((Controller, error)) (Controller, error)
```


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


*Типы возврата:* `Controller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go:41`



---


[function] name: newValidatingAdmissionPolicyStatusControllerDescriptor file: cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go:33 returns_error: нет description: —


### newValidatingAdmissionPolicyStatusControllerDescriptor (cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go:33)


newValidatingAdmissionPolicyStatusControllerDescriptor is a function that performs operations based on the provided parameters and returns ().


```go
func newValidatingAdmissionPolicyStatusControllerDescriptor(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/app/validatingadmissionpolicystatus.go:33`




## cmd/kube-controller-manager/controller-manager.go


📄 Исходный файл: `cmd/kube-controller-manager/controller-manager.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-cmdkube-controller-managercontroller-managergo34) `:34`


</details>


[function] name: main file: cmd/kube-controller-manager/controller-manager.go:34 returns_error: нет description: —


### main (cmd/kube-controller-manager/controller-manager.go:34)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/kube-controller-manager/controller-manager.go:34`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kube-apiserver.md)

- [Следующая директория](cmd_kube-proxy.md)


---

