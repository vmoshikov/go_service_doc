---
title: "Функции: cmd/cloud-controller-manager"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/cloud-controller-manager
---


# Функции: cmd/cloud-controller-manager


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_clicheck.md)

- [Следующая директория](cmd_dependencycheck.md)


---


## Меню по файлам


- 📄 [cmd/cloud-controller-manager/main.go](#cmdcloud-controller-managermaingo)

- 📄 [cmd/cloud-controller-manager/nodeipamcontroller.go](#cmdcloud-controller-managernodeipamcontrollergo)


---


## cmd/cloud-controller-manager/main.go


📄 Исходный файл: `cmd/cloud-controller-manager/main.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [cloudInitializer](#cloudinitializer-cmdcloud-controller-managermaingo82) `:82`

- 🔗 [main](#main-cmdcloud-controller-managermaingo46) `:46`


</details>


[function] name: cloudInitializer file: cmd/cloud-controller-manager/main.go:82 returns_error: нет description: —


### cloudInitializer (cmd/cloud-controller-manager/main.go:82)


cloudInitializer is a function that performs operations based on the provided parameters and returns (config *cloudcontrollerconfig.CompletedConfig).


```go
func cloudInitializer((config *cloudcontrollerconfig.CompletedConfig)) (config *cloudcontrollerconfig.CompletedConfig)
```


**Тип запроса:** cloudcontrollerconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** cloudcontrollerconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/cloud-controller-manager/main.go:82`



---


[function] name: main file: cmd/cloud-controller-manager/main.go:46 returns_error: нет description: —


### main (cmd/cloud-controller-manager/main.go:46)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/cloud-controller-manager/main.go:46`




## cmd/cloud-controller-manager/nodeipamcontroller.go


📄 Исходный файл: `cmd/cloud-controller-manager/nodeipamcontroller.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [StartNodeIpamControllerWrapper](#startnodeipamcontrollerwrapper-cmdcloud-controller-managernodeipamcontrollergo54) `:54`

- 🔗 [processCIDRs](#processcidrs-cmdcloud-controller-managernodeipamcontrollergo150) `:150`

- 🔗 [setNodeCIDRMaskSizes](#setnodecidrmasksizes-cmdcloud-controller-managernodeipamcontrollergo168) `:168`

- 🔗 [startNodeIpamController](#startnodeipamcontroller-cmdcloud-controller-managernodeipamcontrollergo66) `:66`


</details>


[function] name: StartNodeIpamControllerWrapper file: cmd/cloud-controller-manager/nodeipamcontroller.go:54 returns_error: нет description: —


### StartNodeIpamControllerWrapper (cmd/cloud-controller-manager/nodeipamcontroller.go:54)


StartNodeIpamControllerWrapper is a method that performs operations based on the provided parameters and returns (initContext app.ControllerInitContext, completedConfig *cloudcontrollerconfig.CompletedConfig, cloud cloudprovider.Interface).


```go
func (nodeIpamController *nodeIPAMController) StartNodeIpamControllerWrapper((initContext app.ControllerInitContext, completedConfig *cloudcontrollerconfig.CompletedConfig, cloud cloudprovider.Interface)) (initContext app.ControllerInitContext, completedConfig *cloudcontrollerconfig.CompletedConfig, cloud cloudprovider.Interface)
```


**Тип запроса:** cloudcontrollerconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** initContext


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** app.ControllerInitContext


```json
{
  "ClientName": "string"
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/controllermanager.go`


**Тип ответа:** completedConfig


```json
{
  "Options": {},
  "Aggregator": {},
  "ControlPlane": {},
  "APIExtensions": {}
}
```


*Определено в:* `pkg/controlplane/apiserver/samples/generic/server/config.go`


**Тип ответа:** cloudcontrollerconfig.CompletedConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cloud


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cloudprovider.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `cmd/cloud-controller-manager/nodeipamcontroller.go:54`



---


[function] name: processCIDRs file: cmd/cloud-controller-manager/nodeipamcontroller.go:150 returns_error: да description: processCIDRs is a helper function that works on a comma separated cidrs and returns
a list of typed cidrs
a flag if cidr


### processCIDRs (cmd/cloud-controller-manager/nodeipamcontroller.go:150)


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


📍 *Расположение:* `cmd/cloud-controller-manager/nodeipamcontroller.go:150`



---


[function] name: setNodeCIDRMaskSizes file: cmd/cloud-controller-manager/nodeipamcontroller.go:168 returns_error: да description: setNodeCIDRMaskSizes returns the IPv4 and IPv6 node cidr mask sizes to the value provided
for --node-cidr-mask-size-ipv4


### setNodeCIDRMaskSizes (cmd/cloud-controller-manager/nodeipamcontroller.go:168)


setNodeCIDRMaskSizes returns the IPv4 and IPv6 node cidr mask sizes to the value provided
for --node-cidr-mask-size-ipv4 and --node-cidr-mask-size-ipv6 respectively. If value not provided,
then it will return default IPv4 and IPv6 cidr mask sizes.


```go
func setNodeCIDRMaskSizes(([]int, error)) ([]int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/cloud-controller-manager/nodeipamcontroller.go:168`



---


[function] name: startNodeIpamController file: cmd/cloud-controller-manager/nodeipamcontroller.go:66 returns_error: да description: —


### startNodeIpamController (cmd/cloud-controller-manager/nodeipamcontroller.go:66)


startNodeIpamController is a function that performs operations based on the provided parameters and may return an error.


```go
func startNodeIpamController((controller.Interface, bool, error)) (controller.Interface, bool, error)
```


**Тип ответа:** controller.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `controller.Interface`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/cloud-controller-manager/nodeipamcontroller.go:66`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_clicheck.md)

- [Следующая директория](cmd_dependencycheck.md)


---

