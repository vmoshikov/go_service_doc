---
title: "Функции: pkg/security"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/security
---


# Функции: pkg/security


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_scheduler.md)

- [Следующая директория](pkg_securitycontext.md)


---


## Меню по файлам


- 📄 [pkg/security/apparmor/helpers.go](#pkgsecurityapparmorhelpersgo)

- 📄 [pkg/security/apparmor/validate.go](#pkgsecurityapparmorvalidatego)

- 📄 [pkg/security/apparmor/validate_disabled.go](#pkgsecurityapparmorvalidate_disabledgo)


---


## pkg/security/apparmor/helpers.go


📄 Исходный файл: `pkg/security/apparmor/helpers.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [GetProfile](#getprofile-pkgsecurityapparmorhelpersgo54) `:54`

- 🔗 [getProfileFromPodAnnotations](#getprofilefrompodannotations-pkgsecurityapparmorhelpersgo74) `:74`

- 🔗 [isRequired](#isrequired-pkgsecurityapparmorhelpersgo28) `:28`


</details>


[function] name: GetProfile file: pkg/security/apparmor/helpers.go:54 returns_error: нет description: GetProfileName returns the name of the profile to use with the container.


### GetProfile (pkg/security/apparmor/helpers.go:54)


GetProfileName returns the name of the profile to use with the container.


```go
func GetProfile((pod *v1.Pod, container *v1.Container)) (pod *v1.Pod, container *v1.Container)
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


📍 *Расположение:* `pkg/security/apparmor/helpers.go:54`



---


[function] name: getProfileFromPodAnnotations file: pkg/security/apparmor/helpers.go:74 returns_error: нет description: getProfileFromPodAnnotations gets the AppArmor profile to use with container from
(deprecated) pod annotations.


### getProfileFromPodAnnotations (pkg/security/apparmor/helpers.go:74)


getProfileFromPodAnnotations gets the AppArmor profile to use with container from
(deprecated) pod annotations.


```go
func getProfileFromPodAnnotations((annotations map[string]string, containerName string)) (annotations map[string]string, containerName string)
```


**Тип ответа:** annotations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** containerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/security/apparmor/helpers.go:74`



---


[function] name: isRequired file: pkg/security/apparmor/helpers.go:28 returns_error: нет description: Checks whether app armor is required for the pod to run. AppArmor is considered required if any
non-unconfined profiles 


### isRequired (pkg/security/apparmor/helpers.go:28)


Checks whether app armor is required for the pod to run. AppArmor is considered required if any
non-unconfined profiles are specified.


```go
func isRequired((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `pkg/security/apparmor/helpers.go:28`




## pkg/security/apparmor/validate.go


📄 Исходный файл: `pkg/security/apparmor/validate.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [NewValidator](#newvalidator-pkgsecurityapparmorvalidatego40) `:40`

- 🔗 [Validate](#validate-pkgsecurityapparmorvalidatego51) `:51`

- 🔗 [ValidateHost](#validatehost-pkgsecurityapparmorvalidatego84) `:84`

- 🔗 [validateHost](#validatehost-pkgsecurityapparmorvalidatego89) `:89`


</details>


[function] name: NewValidator file: pkg/security/apparmor/validate.go:40 returns_error: нет description: NewValidator is in order to find AppArmor FS


### NewValidator (pkg/security/apparmor/validate.go:40)


NewValidator is in order to find AppArmor FS


```go
func NewValidator(()) ()
```


📍 *Расположение:* `pkg/security/apparmor/validate.go:40`



---


[function] name: Validate file: pkg/security/apparmor/validate.go:51 returns_error: нет description: —


### Validate (pkg/security/apparmor/validate.go:51)


Validate is a method that performs operations based on the provided parameters and returns (pod *v1.Pod).


```go
func (v *validator) Validate((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `pkg/security/apparmor/validate.go:51`



---


[function] name: ValidateHost file: pkg/security/apparmor/validate.go:84 returns_error: нет description: ValidateHost verifies that the host and runtime is capable of enforcing AppArmor profiles.
Note, this is intentionally o


### ValidateHost (pkg/security/apparmor/validate.go:84)


ValidateHost verifies that the host and runtime is capable of enforcing AppArmor profiles.
Note, this is intentionally only check the host at kubelet startup and never re-evaluates the host
as the expectation is that the kubelet restart will be needed to enable or disable AppArmor support.


```go
func (v *validator) ValidateHost(()) ()
```


📍 *Расположение:* `pkg/security/apparmor/validate.go:84`



---


[function] name: validateHost file: pkg/security/apparmor/validate.go:89 returns_error: нет description: validateHost verifies that the host and runtime is capable of enforcing AppArmor profiles.


### validateHost (pkg/security/apparmor/validate.go:89)


validateHost verifies that the host and runtime is capable of enforcing AppArmor profiles.


```go
func validateHost(()) ()
```


📍 *Расположение:* `pkg/security/apparmor/validate.go:89`




## pkg/security/apparmor/validate_disabled.go


📄 Исходный файл: `pkg/security/apparmor/validate_disabled.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-pkgsecurityapparmorvalidate_disabledgo21) `:21`


</details>


[function] name: init file: pkg/security/apparmor/validate_disabled.go:21 returns_error: нет description: —


### init (pkg/security/apparmor/validate_disabled.go:21)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/security/apparmor/validate_disabled.go:21`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_scheduler.md)

- [Следующая директория](pkg_securitycontext.md)


---

