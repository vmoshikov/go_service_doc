---
title: "Функции: pkg/securitycontext"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/securitycontext
---


# Функции: pkg/securitycontext


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_security.md)

- [Следующая директория](pkg_serviceaccount.md)


---


## Меню по файлам


- 📄 [pkg/securitycontext/accessors.go](#pkgsecuritycontextaccessorsgo)

- 📄 [pkg/securitycontext/fake.go](#pkgsecuritycontextfakego)

- 📄 [pkg/securitycontext/util.go](#pkgsecuritycontextutilgo)

- 📄 [pkg/securitycontext/util_darwin.go](#pkgsecuritycontextutil_darwingo)

- 📄 [pkg/securitycontext/util_linux.go](#pkgsecuritycontextutil_linuxgo)

- 📄 [pkg/securitycontext/util_windows.go](#pkgsecuritycontextutil_windowsgo)


---


## pkg/securitycontext/accessors.go


📄 Исходный файл: `pkg/securitycontext/accessors.go`


<details open>
<summary><b>Функции в этом файле (73)</b></summary>


- 🔗 [AllowPrivilegeEscalation](#allowprivilegeescalation-pkgsecuritycontextaccessorsgo425) `:425`

- 🔗 [AllowPrivilegeEscalation](#allowprivilegeescalation-pkgsecuritycontextaccessorsgo540) `:540`

- 🔗 [Capabilities](#capabilities-pkgsecuritycontextaccessorsgo310) `:310`

- 🔗 [Capabilities](#capabilities-pkgsecuritycontextaccessorsgo460) `:460`

- 🔗 [ContainerSecurityContext](#containersecuritycontext-pkgsecuritycontextaccessorsgo300) `:300`

- 🔗 [ContainerSecurityContext](#containersecuritycontext-pkgsecuritycontextaccessorsgo456) `:456`

- 🔗 [FSGroup](#fsgroup-pkgsecuritycontextaccessorsgo222) `:222`

- 🔗 [FSGroupChangePolicy](#fsgroupchangepolicy-pkgsecuritycontextaccessorsgo236) `:236`

- 🔗 [HostIPC](#hostipc-pkgsecuritycontextaccessorsgo114) `:114`

- 🔗 [HostNetwork](#hostnetwork-pkgsecuritycontextaccessorsgo88) `:88`

- 🔗 [HostPID](#hostpid-pkgsecuritycontextaccessorsgo101) `:101`

- 🔗 [HostUsers](#hostusers-pkgsecuritycontextaccessorsgo127) `:127`

- 🔗 [NewContainerSecurityContextAccessor](#newcontainersecuritycontextaccessor-pkgsecuritycontextaccessorsgo286) `:286`

- 🔗 [NewContainerSecurityContextMutator](#newcontainersecuritycontextmutator-pkgsecuritycontextaccessorsgo292) `:292`

- 🔗 [NewEffectiveContainerSecurityContextAccessor](#neweffectivecontainersecuritycontextaccessor-pkgsecuritycontextaccessorsgo441) `:441`

- 🔗 [NewEffectiveContainerSecurityContextMutator](#neweffectivecontainersecuritycontextmutator-pkgsecuritycontextaccessorsgo447) `:447`

- 🔗 [NewPodSecurityContextAccessor](#newpodsecuritycontextaccessor-pkgsecuritycontextaccessorsgo64) `:64`

- 🔗 [NewPodSecurityContextMutator](#newpodsecuritycontextmutator-pkgsecuritycontextaccessorsgo70) `:70`

- 🔗 [PodSecurityContext](#podsecuritycontext-pkgsecuritycontextaccessorsgo78) `:78`

- 🔗 [Privileged](#privileged-pkgsecuritycontextaccessorsgo323) `:323`

- 🔗 [Privileged](#privileged-pkgsecuritycontextaccessorsgo468) `:468`

- 🔗 [ProcMount](#procmount-pkgsecuritycontextaccessorsgo336) `:336`

- 🔗 [ProcMount](#procmount-pkgsecuritycontextaccessorsgo476) `:476`

- 🔗 [ReadOnlyRootFilesystem](#readonlyrootfilesystem-pkgsecuritycontextaccessorsgo398) `:398`

- 🔗 [ReadOnlyRootFilesystem](#readonlyrootfilesystem-pkgsecuritycontextaccessorsgo524) `:524`

- 🔗 [RunAsGroup](#runasgroup-pkgsecuritycontextaccessorsgo166) `:166`

- 🔗 [RunAsGroup](#runasgroup-pkgsecuritycontextaccessorsgo371) `:371`

- 🔗 [RunAsGroup](#runasgroup-pkgsecuritycontextaccessorsgo501) `:501`

- 🔗 [RunAsNonRoot](#runasnonroot-pkgsecuritycontextaccessorsgo180) `:180`

- 🔗 [RunAsNonRoot](#runasnonroot-pkgsecuritycontextaccessorsgo385) `:385`

- 🔗 [RunAsNonRoot](#runasnonroot-pkgsecuritycontextaccessorsgo513) `:513`

- 🔗 [RunAsUser](#runasuser-pkgsecuritycontextaccessorsgo153) `:153`

- 🔗 [RunAsUser](#runasuser-pkgsecuritycontextaccessorsgo358) `:358`

- 🔗 [RunAsUser](#runasuser-pkgsecuritycontextaccessorsgo490) `:490`

- 🔗 [SELinuxOptions](#selinuxoptions-pkgsecuritycontextaccessorsgo140) `:140`

- 🔗 [SELinuxOptions](#selinuxoptions-pkgsecuritycontextaccessorsgo345) `:345`

- 🔗 [SELinuxOptions](#selinuxoptions-pkgsecuritycontextaccessorsgo479) `:479`

- 🔗 [SeccompProfile](#seccompprofile-pkgsecuritycontextaccessorsgo193) `:193`

- 🔗 [SeccompProfile](#seccompprofile-pkgsecuritycontextaccessorsgo411) `:411`

- 🔗 [SeccompProfile](#seccompprofile-pkgsecuritycontextaccessorsgo532) `:532`

- 🔗 [SetAllowPrivilegeEscalation](#setallowprivilegeescalation-pkgsecuritycontextaccessorsgo431) `:431`

- 🔗 [SetAllowPrivilegeEscalation](#setallowprivilegeescalation-pkgsecuritycontextaccessorsgo543) `:543`

- 🔗 [SetCapabilities](#setcapabilities-pkgsecuritycontextaccessorsgo316) `:316`

- 🔗 [SetCapabilities](#setcapabilities-pkgsecuritycontextaccessorsgo463) `:463`

- 🔗 [SetFSGroup](#setfsgroup-pkgsecuritycontextaccessorsgo228) `:228`

- 🔗 [SetFSGroupChangePolicy](#setfsgroupchangepolicy-pkgsecuritycontextaccessorsgo244) `:244`

- 🔗 [SetHostIPC](#sethostipc-pkgsecuritycontextaccessorsgo120) `:120`

- 🔗 [SetHostNetwork](#sethostnetwork-pkgsecuritycontextaccessorsgo94) `:94`

- 🔗 [SetHostPID](#sethostpid-pkgsecuritycontextaccessorsgo107) `:107`

- 🔗 [SetHostUsers](#sethostusers-pkgsecuritycontextaccessorsgo133) `:133`

- 🔗 [SetPrivileged](#setprivileged-pkgsecuritycontextaccessorsgo329) `:329`

- 🔗 [SetPrivileged](#setprivileged-pkgsecuritycontextaccessorsgo471) `:471`

- 🔗 [SetReadOnlyRootFilesystem](#setreadonlyrootfilesystem-pkgsecuritycontextaccessorsgo404) `:404`

- 🔗 [SetReadOnlyRootFilesystem](#setreadonlyrootfilesystem-pkgsecuritycontextaccessorsgo527) `:527`

- 🔗 [SetRunAsGroup](#setrunasgroup-pkgsecuritycontextaccessorsgo172) `:172`

- 🔗 [SetRunAsGroup](#setrunasgroup-pkgsecuritycontextaccessorsgo377) `:377`

- 🔗 [SetRunAsGroup](#setrunasgroup-pkgsecuritycontextaccessorsgo507) `:507`

- 🔗 [SetRunAsNonRoot](#setrunasnonroot-pkgsecuritycontextaccessorsgo186) `:186`

- 🔗 [SetRunAsNonRoot](#setrunasnonroot-pkgsecuritycontextaccessorsgo391) `:391`

- 🔗 [SetRunAsNonRoot](#setrunasnonroot-pkgsecuritycontextaccessorsgo519) `:519`

- 🔗 [SetRunAsUser](#setrunasuser-pkgsecuritycontextaccessorsgo159) `:159`

- 🔗 [SetRunAsUser](#setrunasuser-pkgsecuritycontextaccessorsgo364) `:364`

- 🔗 [SetRunAsUser](#setrunasuser-pkgsecuritycontextaccessorsgo496) `:496`

- 🔗 [SetSELinuxOptions](#setselinuxoptions-pkgsecuritycontextaccessorsgo146) `:146`

- 🔗 [SetSELinuxOptions](#setselinuxoptions-pkgsecuritycontextaccessorsgo351) `:351`

- 🔗 [SetSELinuxOptions](#setselinuxoptions-pkgsecuritycontextaccessorsgo485) `:485`

- 🔗 [SetSeccompProfile](#setseccompprofile-pkgsecuritycontextaccessorsgo199) `:199`

- 🔗 [SetSeccompProfile](#setseccompprofile-pkgsecuritycontextaccessorsgo417) `:417`

- 🔗 [SetSeccompProfile](#setseccompprofile-pkgsecuritycontextaccessorsgo535) `:535`

- 🔗 [SetSupplementalGroups](#setsupplementalgroups-pkgsecuritycontextaccessorsgo212) `:212`

- 🔗 [SupplementalGroups](#supplementalgroups-pkgsecuritycontextaccessorsgo206) `:206`

- 🔗 [ensureContainerSC](#ensurecontainersc-pkgsecuritycontextaccessorsgo304) `:304`

- 🔗 [ensurePodSC](#ensurepodsc-pkgsecuritycontextaccessorsgo82) `:82`


</details>


[function] name: AllowPrivilegeEscalation file: pkg/securitycontext/accessors.go:425 returns_error: нет description: —


### AllowPrivilegeEscalation (pkg/securitycontext/accessors.go:425)


AllowPrivilegeEscalation is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) AllowPrivilegeEscalation(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:425`



---


[function] name: AllowPrivilegeEscalation file: pkg/securitycontext/accessors.go:540 returns_error: нет description: —


### AllowPrivilegeEscalation (pkg/securitycontext/accessors.go:540)


AllowPrivilegeEscalation is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) AllowPrivilegeEscalation(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:540`



---


[function] name: Capabilities file: pkg/securitycontext/accessors.go:310 returns_error: нет description: —


### Capabilities (pkg/securitycontext/accessors.go:310)


Capabilities is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) Capabilities(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:310`



---


[function] name: Capabilities file: pkg/securitycontext/accessors.go:460 returns_error: нет description: —


### Capabilities (pkg/securitycontext/accessors.go:460)


Capabilities is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) Capabilities(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:460`



---


[function] name: ContainerSecurityContext file: pkg/securitycontext/accessors.go:300 returns_error: нет description: —


### ContainerSecurityContext (pkg/securitycontext/accessors.go:300)


ContainerSecurityContext is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) ContainerSecurityContext(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:300`



---


[function] name: ContainerSecurityContext file: pkg/securitycontext/accessors.go:456 returns_error: нет description: —


### ContainerSecurityContext (pkg/securitycontext/accessors.go:456)


ContainerSecurityContext is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) ContainerSecurityContext(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:456`



---


[function] name: FSGroup file: pkg/securitycontext/accessors.go:222 returns_error: нет description: —


### FSGroup (pkg/securitycontext/accessors.go:222)


FSGroup is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) FSGroup(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:222`



---


[function] name: FSGroupChangePolicy file: pkg/securitycontext/accessors.go:236 returns_error: нет description: —


### FSGroupChangePolicy (pkg/securitycontext/accessors.go:236)


FSGroupChangePolicy is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) FSGroupChangePolicy(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:236`



---


[function] name: HostIPC file: pkg/securitycontext/accessors.go:114 returns_error: нет description: —


### HostIPC (pkg/securitycontext/accessors.go:114)


HostIPC is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) HostIPC(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:114`



---


[function] name: HostNetwork file: pkg/securitycontext/accessors.go:88 returns_error: нет description: —


### HostNetwork (pkg/securitycontext/accessors.go:88)


HostNetwork is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) HostNetwork(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:88`



---


[function] name: HostPID file: pkg/securitycontext/accessors.go:101 returns_error: нет description: —


### HostPID (pkg/securitycontext/accessors.go:101)


HostPID is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) HostPID(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:101`



---


[function] name: HostUsers file: pkg/securitycontext/accessors.go:127 returns_error: нет description: —


### HostUsers (pkg/securitycontext/accessors.go:127)


HostUsers is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) HostUsers(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:127`



---


[function] name: NewContainerSecurityContextAccessor file: pkg/securitycontext/accessors.go:286 returns_error: нет description: NewContainerSecurityContextAccessor returns an accessor for the provided container security context
May be initialized w


### NewContainerSecurityContextAccessor (pkg/securitycontext/accessors.go:286)


NewContainerSecurityContextAccessor returns an accessor for the provided container security context
May be initialized with a nil SecurityContext


```go
func NewContainerSecurityContextAccessor((containerSC *api.SecurityContext)) (containerSC *api.SecurityContext)
```


**Тип запроса:** api.SecurityContext


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


**Тип ответа:** containerSC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/securitycontext/accessors.go:286`



---


[function] name: NewContainerSecurityContextMutator file: pkg/securitycontext/accessors.go:292 returns_error: нет description: NewContainerSecurityContextMutator returns a mutator for the provided container security context
May be initialized with


### NewContainerSecurityContextMutator (pkg/securitycontext/accessors.go:292)


NewContainerSecurityContextMutator returns a mutator for the provided container security context
May be initialized with a nil SecurityContext


```go
func NewContainerSecurityContextMutator((containerSC *api.SecurityContext)) (containerSC *api.SecurityContext)
```


**Тип запроса:** api.SecurityContext


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


**Тип ответа:** containerSC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/securitycontext/accessors.go:292`



---


[function] name: NewEffectiveContainerSecurityContextAccessor file: pkg/securitycontext/accessors.go:441 returns_error: нет description: NewEffectiveContainerSecurityContextAccessor returns an accessor for reading effective values
for the provided pod secur


### NewEffectiveContainerSecurityContextAccessor (pkg/securitycontext/accessors.go:441)


NewEffectiveContainerSecurityContextAccessor returns an accessor for reading effective values
for the provided pod security context and container security context


```go
func NewEffectiveContainerSecurityContextAccessor((podSC PodSecurityContextAccessor, containerSC ContainerSecurityContextMutator)) (podSC PodSecurityContextAccessor, containerSC ContainerSecurityContextMutator)
```


**Тип ответа:** podSC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PodSecurityContextAccessor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** containerSC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerSecurityContextMutator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/securitycontext/accessors.go:441`



---


[function] name: NewEffectiveContainerSecurityContextMutator file: pkg/securitycontext/accessors.go:447 returns_error: нет description: NewEffectiveContainerSecurityContextMutator returns a mutator for reading and writing effective values
for the provided 


### NewEffectiveContainerSecurityContextMutator (pkg/securitycontext/accessors.go:447)


NewEffectiveContainerSecurityContextMutator returns a mutator for reading and writing effective values
for the provided pod security context and container security context


```go
func NewEffectiveContainerSecurityContextMutator((podSC PodSecurityContextAccessor, containerSC ContainerSecurityContextMutator)) (podSC PodSecurityContextAccessor, containerSC ContainerSecurityContextMutator)
```


**Тип ответа:** podSC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PodSecurityContextAccessor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** containerSC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContainerSecurityContextMutator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/securitycontext/accessors.go:447`



---


[function] name: NewPodSecurityContextAccessor file: pkg/securitycontext/accessors.go:64 returns_error: нет description: NewPodSecurityContextAccessor returns an accessor for the given pod security context.
May be initialized with a nil PodS


### NewPodSecurityContextAccessor (pkg/securitycontext/accessors.go:64)


NewPodSecurityContextAccessor returns an accessor for the given pod security context.
May be initialized with a nil PodSecurityContext.


```go
func NewPodSecurityContextAccessor((podSC *api.PodSecurityContext)) (podSC *api.PodSecurityContext)
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


**Тип ответа:** podSC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/securitycontext/accessors.go:64`



---


[function] name: NewPodSecurityContextMutator file: pkg/securitycontext/accessors.go:70 returns_error: нет description: NewPodSecurityContextMutator returns a mutator for the given pod security context.
May be initialized with a nil PodSecu


### NewPodSecurityContextMutator (pkg/securitycontext/accessors.go:70)


NewPodSecurityContextMutator returns a mutator for the given pod security context.
May be initialized with a nil PodSecurityContext.


```go
func NewPodSecurityContextMutator((podSC *api.PodSecurityContext)) (podSC *api.PodSecurityContext)
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


**Тип ответа:** podSC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/securitycontext/accessors.go:70`



---


[function] name: PodSecurityContext file: pkg/securitycontext/accessors.go:78 returns_error: нет description: —


### PodSecurityContext (pkg/securitycontext/accessors.go:78)


PodSecurityContext is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) PodSecurityContext(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:78`



---


[function] name: Privileged file: pkg/securitycontext/accessors.go:323 returns_error: нет description: —


### Privileged (pkg/securitycontext/accessors.go:323)


Privileged is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) Privileged(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:323`



---


[function] name: Privileged file: pkg/securitycontext/accessors.go:468 returns_error: нет description: —


### Privileged (pkg/securitycontext/accessors.go:468)


Privileged is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) Privileged(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:468`



---


[function] name: ProcMount file: pkg/securitycontext/accessors.go:336 returns_error: нет description: —


### ProcMount (pkg/securitycontext/accessors.go:336)


ProcMount is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) ProcMount(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:336`



---


[function] name: ProcMount file: pkg/securitycontext/accessors.go:476 returns_error: нет description: —


### ProcMount (pkg/securitycontext/accessors.go:476)


ProcMount is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) ProcMount(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:476`



---


[function] name: ReadOnlyRootFilesystem file: pkg/securitycontext/accessors.go:398 returns_error: нет description: —


### ReadOnlyRootFilesystem (pkg/securitycontext/accessors.go:398)


ReadOnlyRootFilesystem is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) ReadOnlyRootFilesystem(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:398`



---


[function] name: ReadOnlyRootFilesystem file: pkg/securitycontext/accessors.go:524 returns_error: нет description: —


### ReadOnlyRootFilesystem (pkg/securitycontext/accessors.go:524)


ReadOnlyRootFilesystem is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) ReadOnlyRootFilesystem(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:524`



---


[function] name: RunAsGroup file: pkg/securitycontext/accessors.go:166 returns_error: нет description: —


### RunAsGroup (pkg/securitycontext/accessors.go:166)


RunAsGroup is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) RunAsGroup(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:166`



---


[function] name: RunAsGroup file: pkg/securitycontext/accessors.go:371 returns_error: нет description: —


### RunAsGroup (pkg/securitycontext/accessors.go:371)


RunAsGroup is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) RunAsGroup(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:371`



---


[function] name: RunAsGroup file: pkg/securitycontext/accessors.go:501 returns_error: нет description: —


### RunAsGroup (pkg/securitycontext/accessors.go:501)


RunAsGroup is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) RunAsGroup(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:501`



---


[function] name: RunAsNonRoot file: pkg/securitycontext/accessors.go:180 returns_error: нет description: —


### RunAsNonRoot (pkg/securitycontext/accessors.go:180)


RunAsNonRoot is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) RunAsNonRoot(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:180`



---


[function] name: RunAsNonRoot file: pkg/securitycontext/accessors.go:385 returns_error: нет description: —


### RunAsNonRoot (pkg/securitycontext/accessors.go:385)


RunAsNonRoot is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) RunAsNonRoot(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:385`



---


[function] name: RunAsNonRoot file: pkg/securitycontext/accessors.go:513 returns_error: нет description: —


### RunAsNonRoot (pkg/securitycontext/accessors.go:513)


RunAsNonRoot is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) RunAsNonRoot(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:513`



---


[function] name: RunAsUser file: pkg/securitycontext/accessors.go:153 returns_error: нет description: —


### RunAsUser (pkg/securitycontext/accessors.go:153)


RunAsUser is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) RunAsUser(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:153`



---


[function] name: RunAsUser file: pkg/securitycontext/accessors.go:358 returns_error: нет description: —


### RunAsUser (pkg/securitycontext/accessors.go:358)


RunAsUser is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) RunAsUser(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:358`



---


[function] name: RunAsUser file: pkg/securitycontext/accessors.go:490 returns_error: нет description: —


### RunAsUser (pkg/securitycontext/accessors.go:490)


RunAsUser is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) RunAsUser(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:490`



---


[function] name: SELinuxOptions file: pkg/securitycontext/accessors.go:140 returns_error: нет description: —


### SELinuxOptions (pkg/securitycontext/accessors.go:140)


SELinuxOptions is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) SELinuxOptions(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:140`



---


[function] name: SELinuxOptions file: pkg/securitycontext/accessors.go:345 returns_error: нет description: —


### SELinuxOptions (pkg/securitycontext/accessors.go:345)


SELinuxOptions is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) SELinuxOptions(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:345`



---


[function] name: SELinuxOptions file: pkg/securitycontext/accessors.go:479 returns_error: нет description: —


### SELinuxOptions (pkg/securitycontext/accessors.go:479)


SELinuxOptions is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) SELinuxOptions(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:479`



---


[function] name: SeccompProfile file: pkg/securitycontext/accessors.go:193 returns_error: нет description: —


### SeccompProfile (pkg/securitycontext/accessors.go:193)


SeccompProfile is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) SeccompProfile(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:193`



---


[function] name: SeccompProfile file: pkg/securitycontext/accessors.go:411 returns_error: нет description: —


### SeccompProfile (pkg/securitycontext/accessors.go:411)


SeccompProfile is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) SeccompProfile(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:411`



---


[function] name: SeccompProfile file: pkg/securitycontext/accessors.go:532 returns_error: нет description: —


### SeccompProfile (pkg/securitycontext/accessors.go:532)


SeccompProfile is a method that performs operations based on the provided parameters and returns ().


```go
func (w *effectiveContainerSecurityContextWrapper) SeccompProfile(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:532`



---


[function] name: SetAllowPrivilegeEscalation file: pkg/securitycontext/accessors.go:431 returns_error: нет description: —


### SetAllowPrivilegeEscalation (pkg/securitycontext/accessors.go:431)


SetAllowPrivilegeEscalation is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *containerSecurityContextWrapper) SetAllowPrivilegeEscalation((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:431`



---


[function] name: SetAllowPrivilegeEscalation file: pkg/securitycontext/accessors.go:543 returns_error: нет description: —


### SetAllowPrivilegeEscalation (pkg/securitycontext/accessors.go:543)


SetAllowPrivilegeEscalation is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *effectiveContainerSecurityContextWrapper) SetAllowPrivilegeEscalation((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:543`



---


[function] name: SetCapabilities file: pkg/securitycontext/accessors.go:316 returns_error: нет description: —


### SetCapabilities (pkg/securitycontext/accessors.go:316)


SetCapabilities is a method that updates data based on the provided parameters and returns (v *api.Capabilities).


```go
func (w *containerSecurityContextWrapper) SetCapabilities((v *api.Capabilities)) (v *api.Capabilities)
```


**Тип запроса:** api.Capabilities


```json
{
  "AllowPrivileged": false,
  "PrivilegedSources": {},
  "PerConnectionBandwidthLimitBytesPerSec": 0
}
```


*Определено в:* `pkg/capabilities/capabilities.go`


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


**Тип ответа:** api.Capabilities


```json
{
  "AllowPrivileged": false,
  "PrivilegedSources": {},
  "PerConnectionBandwidthLimitBytesPerSec": 0
}
```


*Определено в:* `pkg/capabilities/capabilities.go`


📍 *Расположение:* `pkg/securitycontext/accessors.go:316`



---


[function] name: SetCapabilities file: pkg/securitycontext/accessors.go:463 returns_error: нет description: —


### SetCapabilities (pkg/securitycontext/accessors.go:463)


SetCapabilities is a method that updates data based on the provided parameters and returns (v *api.Capabilities).


```go
func (w *effectiveContainerSecurityContextWrapper) SetCapabilities((v *api.Capabilities)) (v *api.Capabilities)
```


**Тип запроса:** api.Capabilities


```json
{
  "AllowPrivileged": false,
  "PrivilegedSources": {},
  "PerConnectionBandwidthLimitBytesPerSec": 0
}
```


*Определено в:* `pkg/capabilities/capabilities.go`


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


**Тип ответа:** api.Capabilities


```json
{
  "AllowPrivileged": false,
  "PrivilegedSources": {},
  "PerConnectionBandwidthLimitBytesPerSec": 0
}
```


*Определено в:* `pkg/capabilities/capabilities.go`


📍 *Расположение:* `pkg/securitycontext/accessors.go:463`



---


[function] name: SetFSGroup file: pkg/securitycontext/accessors.go:228 returns_error: нет description: —


### SetFSGroup (pkg/securitycontext/accessors.go:228)


SetFSGroup is a method that updates data based on the provided parameters and returns (v *int64).


```go
func (w *podSecurityContextWrapper) SetFSGroup((v *int64)) (v *int64)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:228`



---


[function] name: SetFSGroupChangePolicy file: pkg/securitycontext/accessors.go:244 returns_error: нет description: —


### SetFSGroupChangePolicy (pkg/securitycontext/accessors.go:244)


SetFSGroupChangePolicy is a method that updates data based on the provided parameters and returns (v *api.PodFSGroupChangePolicy).


```go
func (w *podSecurityContextWrapper) SetFSGroupChangePolicy((v *api.PodFSGroupChangePolicy)) (v *api.PodFSGroupChangePolicy)
```


**Тип запроса:** api.PodFSGroupChangePolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** api.PodFSGroupChangePolicy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/securitycontext/accessors.go:244`



---


[function] name: SetHostIPC file: pkg/securitycontext/accessors.go:120 returns_error: нет description: —


### SetHostIPC (pkg/securitycontext/accessors.go:120)


SetHostIPC is a method that updates data based on the provided parameters and returns (v bool).


```go
func (w *podSecurityContextWrapper) SetHostIPC((v bool)) (v bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:120`



---


[function] name: SetHostNetwork file: pkg/securitycontext/accessors.go:94 returns_error: нет description: —


### SetHostNetwork (pkg/securitycontext/accessors.go:94)


SetHostNetwork is a method that updates data based on the provided parameters and returns (v bool).


```go
func (w *podSecurityContextWrapper) SetHostNetwork((v bool)) (v bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:94`



---


[function] name: SetHostPID file: pkg/securitycontext/accessors.go:107 returns_error: нет description: —


### SetHostPID (pkg/securitycontext/accessors.go:107)


SetHostPID is a method that updates data based on the provided parameters and returns (v bool).


```go
func (w *podSecurityContextWrapper) SetHostPID((v bool)) (v bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:107`



---


[function] name: SetHostUsers file: pkg/securitycontext/accessors.go:133 returns_error: нет description: —


### SetHostUsers (pkg/securitycontext/accessors.go:133)


SetHostUsers is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *podSecurityContextWrapper) SetHostUsers((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:133`



---


[function] name: SetPrivileged file: pkg/securitycontext/accessors.go:329 returns_error: нет description: —


### SetPrivileged (pkg/securitycontext/accessors.go:329)


SetPrivileged is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *containerSecurityContextWrapper) SetPrivileged((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:329`



---


[function] name: SetPrivileged file: pkg/securitycontext/accessors.go:471 returns_error: нет description: —


### SetPrivileged (pkg/securitycontext/accessors.go:471)


SetPrivileged is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *effectiveContainerSecurityContextWrapper) SetPrivileged((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:471`



---


[function] name: SetReadOnlyRootFilesystem file: pkg/securitycontext/accessors.go:404 returns_error: нет description: —


### SetReadOnlyRootFilesystem (pkg/securitycontext/accessors.go:404)


SetReadOnlyRootFilesystem is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *containerSecurityContextWrapper) SetReadOnlyRootFilesystem((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:404`



---


[function] name: SetReadOnlyRootFilesystem file: pkg/securitycontext/accessors.go:527 returns_error: нет description: —


### SetReadOnlyRootFilesystem (pkg/securitycontext/accessors.go:527)


SetReadOnlyRootFilesystem is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *effectiveContainerSecurityContextWrapper) SetReadOnlyRootFilesystem((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:527`



---


[function] name: SetRunAsGroup file: pkg/securitycontext/accessors.go:172 returns_error: нет description: —


### SetRunAsGroup (pkg/securitycontext/accessors.go:172)


SetRunAsGroup is a method that updates data based on the provided parameters and returns (v *int64).


```go
func (w *podSecurityContextWrapper) SetRunAsGroup((v *int64)) (v *int64)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:172`



---


[function] name: SetRunAsGroup file: pkg/securitycontext/accessors.go:377 returns_error: нет description: —


### SetRunAsGroup (pkg/securitycontext/accessors.go:377)


SetRunAsGroup is a method that updates data based on the provided parameters and returns (v *int64).


```go
func (w *containerSecurityContextWrapper) SetRunAsGroup((v *int64)) (v *int64)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:377`



---


[function] name: SetRunAsGroup file: pkg/securitycontext/accessors.go:507 returns_error: нет description: —


### SetRunAsGroup (pkg/securitycontext/accessors.go:507)


SetRunAsGroup is a method that updates data based on the provided parameters and returns (v *int64).


```go
func (w *effectiveContainerSecurityContextWrapper) SetRunAsGroup((v *int64)) (v *int64)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:507`



---


[function] name: SetRunAsNonRoot file: pkg/securitycontext/accessors.go:186 returns_error: нет description: —


### SetRunAsNonRoot (pkg/securitycontext/accessors.go:186)


SetRunAsNonRoot is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *podSecurityContextWrapper) SetRunAsNonRoot((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:186`



---


[function] name: SetRunAsNonRoot file: pkg/securitycontext/accessors.go:391 returns_error: нет description: —


### SetRunAsNonRoot (pkg/securitycontext/accessors.go:391)


SetRunAsNonRoot is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *containerSecurityContextWrapper) SetRunAsNonRoot((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:391`



---


[function] name: SetRunAsNonRoot file: pkg/securitycontext/accessors.go:519 returns_error: нет description: —


### SetRunAsNonRoot (pkg/securitycontext/accessors.go:519)


SetRunAsNonRoot is a method that updates data based on the provided parameters and returns (v *bool).


```go
func (w *effectiveContainerSecurityContextWrapper) SetRunAsNonRoot((v *bool)) (v *bool)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:519`



---


[function] name: SetRunAsUser file: pkg/securitycontext/accessors.go:159 returns_error: нет description: —


### SetRunAsUser (pkg/securitycontext/accessors.go:159)


SetRunAsUser is a method that updates data based on the provided parameters and returns (v *int64).


```go
func (w *podSecurityContextWrapper) SetRunAsUser((v *int64)) (v *int64)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:159`



---


[function] name: SetRunAsUser file: pkg/securitycontext/accessors.go:364 returns_error: нет description: —


### SetRunAsUser (pkg/securitycontext/accessors.go:364)


SetRunAsUser is a method that updates data based on the provided parameters and returns (v *int64).


```go
func (w *containerSecurityContextWrapper) SetRunAsUser((v *int64)) (v *int64)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:364`



---


[function] name: SetRunAsUser file: pkg/securitycontext/accessors.go:496 returns_error: нет description: —


### SetRunAsUser (pkg/securitycontext/accessors.go:496)


SetRunAsUser is a method that updates data based on the provided parameters and returns (v *int64).


```go
func (w *effectiveContainerSecurityContextWrapper) SetRunAsUser((v *int64)) (v *int64)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:496`



---


[function] name: SetSELinuxOptions file: pkg/securitycontext/accessors.go:146 returns_error: нет description: —


### SetSELinuxOptions (pkg/securitycontext/accessors.go:146)


SetSELinuxOptions is a method that updates data based on the provided parameters and returns (v *api.SELinuxOptions).


```go
func (w *podSecurityContextWrapper) SetSELinuxOptions((v *api.SELinuxOptions)) (v *api.SELinuxOptions)
```


**Тип запроса:** api.SELinuxOptions


```json
{
  "User": "string",
  "Role": "string",
  "Type": "string",
  "Level": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** api.SELinuxOptions


```json
{
  "User": "string",
  "Role": "string",
  "Type": "string",
  "Level": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/securitycontext/accessors.go:146`



---


[function] name: SetSELinuxOptions file: pkg/securitycontext/accessors.go:351 returns_error: нет description: —


### SetSELinuxOptions (pkg/securitycontext/accessors.go:351)


SetSELinuxOptions is a method that updates data based on the provided parameters and returns (v *api.SELinuxOptions).


```go
func (w *containerSecurityContextWrapper) SetSELinuxOptions((v *api.SELinuxOptions)) (v *api.SELinuxOptions)
```


**Тип запроса:** api.SELinuxOptions


```json
{
  "User": "string",
  "Role": "string",
  "Type": "string",
  "Level": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** api.SELinuxOptions


```json
{
  "User": "string",
  "Role": "string",
  "Type": "string",
  "Level": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/securitycontext/accessors.go:351`



---


[function] name: SetSELinuxOptions file: pkg/securitycontext/accessors.go:485 returns_error: нет description: —


### SetSELinuxOptions (pkg/securitycontext/accessors.go:485)


SetSELinuxOptions is a method that updates data based on the provided parameters and returns (v *api.SELinuxOptions).


```go
func (w *effectiveContainerSecurityContextWrapper) SetSELinuxOptions((v *api.SELinuxOptions)) (v *api.SELinuxOptions)
```


**Тип запроса:** api.SELinuxOptions


```json
{
  "User": "string",
  "Role": "string",
  "Type": "string",
  "Level": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


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


**Тип ответа:** api.SELinuxOptions


```json
{
  "User": "string",
  "Role": "string",
  "Type": "string",
  "Level": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/securitycontext/accessors.go:485`



---


[function] name: SetSeccompProfile file: pkg/securitycontext/accessors.go:199 returns_error: нет description: —


### SetSeccompProfile (pkg/securitycontext/accessors.go:199)


SetSeccompProfile is a method that updates data based on the provided parameters and returns (p *api.SeccompProfile).


```go
func (w *podSecurityContextWrapper) SetSeccompProfile((p *api.SeccompProfile)) (p *api.SeccompProfile)
```


**Тип запроса:** api.SeccompProfile


```json
{
  "Type": {},
  "LocalhostProfile": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** api.SeccompProfile


```json
{
  "Type": {},
  "LocalhostProfile": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/securitycontext/accessors.go:199`



---


[function] name: SetSeccompProfile file: pkg/securitycontext/accessors.go:417 returns_error: нет description: —


### SetSeccompProfile (pkg/securitycontext/accessors.go:417)


SetSeccompProfile is a method that updates data based on the provided parameters and returns (p *api.SeccompProfile).


```go
func (w *containerSecurityContextWrapper) SetSeccompProfile((p *api.SeccompProfile)) (p *api.SeccompProfile)
```


**Тип запроса:** api.SeccompProfile


```json
{
  "Type": {},
  "LocalhostProfile": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** api.SeccompProfile


```json
{
  "Type": {},
  "LocalhostProfile": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/securitycontext/accessors.go:417`



---


[function] name: SetSeccompProfile file: pkg/securitycontext/accessors.go:535 returns_error: нет description: —


### SetSeccompProfile (pkg/securitycontext/accessors.go:535)


SetSeccompProfile is a method that updates data based on the provided parameters and returns (p *api.SeccompProfile).


```go
func (w *effectiveContainerSecurityContextWrapper) SetSeccompProfile((p *api.SeccompProfile)) (p *api.SeccompProfile)
```


**Тип запроса:** api.SeccompProfile


```json
{
  "Type": {},
  "LocalhostProfile": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** api.SeccompProfile


```json
{
  "Type": {},
  "LocalhostProfile": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/securitycontext/accessors.go:535`



---


[function] name: SetSupplementalGroups file: pkg/securitycontext/accessors.go:212 returns_error: нет description: —


### SetSupplementalGroups (pkg/securitycontext/accessors.go:212)


SetSupplementalGroups is a method that updates data based on the provided parameters and returns (v []int64).


```go
func (w *podSecurityContextWrapper) SetSupplementalGroups((v []int64)) (v []int64)
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


📍 *Расположение:* `pkg/securitycontext/accessors.go:212`



---


[function] name: SupplementalGroups file: pkg/securitycontext/accessors.go:206 returns_error: нет description: —


### SupplementalGroups (pkg/securitycontext/accessors.go:206)


SupplementalGroups is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) SupplementalGroups(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:206`



---


[function] name: ensureContainerSC file: pkg/securitycontext/accessors.go:304 returns_error: нет description: —


### ensureContainerSC (pkg/securitycontext/accessors.go:304)


ensureContainerSC is a method that performs operations based on the provided parameters and returns ().


```go
func (w *containerSecurityContextWrapper) ensureContainerSC(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:304`



---


[function] name: ensurePodSC file: pkg/securitycontext/accessors.go:82 returns_error: нет description: —


### ensurePodSC (pkg/securitycontext/accessors.go:82)


ensurePodSC is a method that performs operations based on the provided parameters and returns ().


```go
func (w *podSecurityContextWrapper) ensurePodSC(()) ()
```


📍 *Расположение:* `pkg/securitycontext/accessors.go:82`




## pkg/securitycontext/fake.go


📄 Исходный файл: `pkg/securitycontext/fake.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ValidInternalSecurityContextWithContainerDefaults](#validinternalsecuritycontextwithcontainerdefaults-pkgsecuritycontextfakego38) `:38`

- 🔗 [ValidSecurityContextWithContainerDefaults](#validsecuritycontextwithcontainerdefaults-pkgsecuritycontextfakego26) `:26`


</details>


[function] name: ValidInternalSecurityContextWithContainerDefaults file: pkg/securitycontext/fake.go:38 returns_error: нет description: ValidInternalSecurityContextWithContainerDefaults creates a valid security context provider based on
empty container def


### ValidInternalSecurityContextWithContainerDefaults (pkg/securitycontext/fake.go:38)


ValidInternalSecurityContextWithContainerDefaults creates a valid security context provider based on
empty container defaults.  Used for testing.


```go
func ValidInternalSecurityContextWithContainerDefaults(()) ()
```


📍 *Расположение:* `pkg/securitycontext/fake.go:38`



---


[function] name: ValidSecurityContextWithContainerDefaults file: pkg/securitycontext/fake.go:26 returns_error: нет description: ValidSecurityContextWithContainerDefaults creates a valid security context provider based on
empty container defaults.  


### ValidSecurityContextWithContainerDefaults (pkg/securitycontext/fake.go:26)


ValidSecurityContextWithContainerDefaults creates a valid security context provider based on
empty container defaults.  Used for testing.


```go
func ValidSecurityContextWithContainerDefaults(()) ()
```


📍 *Расположение:* `pkg/securitycontext/fake.go:26`




## pkg/securitycontext/util.go


📄 Исходный файл: `pkg/securitycontext/util.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [AddNoNewPrivileges](#addnonewprivileges-pkgsecuritycontextutilgo179) `:179`

- 🔗 [ConvertToRuntimeMaskedPaths](#converttoruntimemaskedpaths-pkgsecuritycontextutilgo232) `:232`

- 🔗 [ConvertToRuntimeReadonlyPaths](#converttoruntimereadonlypaths-pkgsecuritycontextutilgo244) `:244`

- 🔗 [DetermineEffectiveRunAsUser](#determineeffectiverunasuser-pkgsecuritycontextutilgo127) `:127`

- 🔗 [DetermineEffectiveSecurityContext](#determineeffectivesecuritycontext-pkgsecuritycontextutilgo44) `:44`

- 🔗 [HasWindowsHostProcessRequest](#haswindowshostprocessrequest-pkgsecuritycontextutilgo29) `:29`

- 🔗 [securityContextFromPodSecurityContext](#securitycontextfrompodsecuritycontext-pkgsecuritycontextutilgo143) `:143`


</details>


[function] name: AddNoNewPrivileges file: pkg/securitycontext/util.go:179 returns_error: нет description: AddNoNewPrivileges returns if we should add the no_new_privs option.


### AddNoNewPrivileges (pkg/securitycontext/util.go:179)


AddNoNewPrivileges returns if we should add the no_new_privs option.


```go
func AddNoNewPrivileges((sc *v1.SecurityContext)) (sc *v1.SecurityContext)
```


**Тип запроса:** v1.SecurityContext


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


**Тип ответа:** v1.SecurityContext


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


📍 *Расположение:* `pkg/securitycontext/util.go:179`



---


[function] name: ConvertToRuntimeMaskedPaths file: pkg/securitycontext/util.go:232 returns_error: нет description: ConvertToRuntimeMaskedPaths converts the ProcMountType to the specified or default
masked paths.


### ConvertToRuntimeMaskedPaths (pkg/securitycontext/util.go:232)


ConvertToRuntimeMaskedPaths converts the ProcMountType to the specified or default
masked paths.


```go
func ConvertToRuntimeMaskedPaths((opt *v1.ProcMountType)) (opt *v1.ProcMountType)
```


**Тип запроса:** v1.ProcMountType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** v1.ProcMountType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/securitycontext/util.go:232`



---


[function] name: ConvertToRuntimeReadonlyPaths file: pkg/securitycontext/util.go:244 returns_error: нет description: ConvertToRuntimeReadonlyPaths converts the ProcMountType to the specified or default
readonly paths.


### ConvertToRuntimeReadonlyPaths (pkg/securitycontext/util.go:244)


ConvertToRuntimeReadonlyPaths converts the ProcMountType to the specified or default
readonly paths.


```go
func ConvertToRuntimeReadonlyPaths((opt *v1.ProcMountType)) (opt *v1.ProcMountType)
```


**Тип запроса:** v1.ProcMountType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** v1.ProcMountType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/securitycontext/util.go:244`



---


[function] name: DetermineEffectiveRunAsUser file: pkg/securitycontext/util.go:127 returns_error: нет description: DetermineEffectiveRunAsUser returns a pointer of UID from the provided pod's
and container's security context and a bool


### DetermineEffectiveRunAsUser (pkg/securitycontext/util.go:127)


DetermineEffectiveRunAsUser returns a pointer of UID from the provided pod's
and container's security context and a bool value to indicate if it is absent.
Container's runAsUser take precedence in cases where both are set.


```go
func DetermineEffectiveRunAsUser((*int64, bool)) (*int64, bool)
```


📍 *Расположение:* `pkg/securitycontext/util.go:127`



---


[function] name: DetermineEffectiveSecurityContext file: pkg/securitycontext/util.go:44 returns_error: нет description: DetermineEffectiveSecurityContext returns a synthesized SecurityContext for reading effective configurations
from the pr


### DetermineEffectiveSecurityContext (pkg/securitycontext/util.go:44)


DetermineEffectiveSecurityContext returns a synthesized SecurityContext for reading effective configurations
from the provided pod's and container's security context. Container's fields take precedence in cases where both
are set


```go
func DetermineEffectiveSecurityContext((pod *v1.Pod, container *v1.Container)) (pod *v1.Pod, container *v1.Container)
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


📍 *Расположение:* `pkg/securitycontext/util.go:44`



---


[function] name: HasWindowsHostProcessRequest file: pkg/securitycontext/util.go:29 returns_error: нет description: HasWindowsHostProcessRequest returns true if container should run as HostProcess container,
taking into account nils


### HasWindowsHostProcessRequest (pkg/securitycontext/util.go:29)


HasWindowsHostProcessRequest returns true if container should run as HostProcess container,
taking into account nils


```go
func HasWindowsHostProcessRequest((pod *v1.Pod, container *v1.Container)) (pod *v1.Pod, container *v1.Container)
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


📍 *Расположение:* `pkg/securitycontext/util.go:29`



---


[function] name: securityContextFromPodSecurityContext file: pkg/securitycontext/util.go:143 returns_error: нет description: —


### securityContextFromPodSecurityContext (pkg/securitycontext/util.go:143)


securityContextFromPodSecurityContext is a function that performs operations based on the provided parameters and returns (pod *v1.Pod).


```go
func securityContextFromPodSecurityContext((pod *v1.Pod)) (pod *v1.Pod)
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


📍 *Расположение:* `pkg/securitycontext/util.go:143`




## pkg/securitycontext/util_darwin.go


📄 Исходный файл: `pkg/securitycontext/util_darwin.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [possibleCPUs](#possiblecpus-pkgsecuritycontextutil_darwingo19) `:19`


</details>


[function] name: possibleCPUs file: pkg/securitycontext/util_darwin.go:19 returns_error: нет description: —


### possibleCPUs (pkg/securitycontext/util_darwin.go:19)


possibleCPUs is a function that performs operations based on the provided parameters and returns ().


```go
func possibleCPUs(()) ()
```


📍 *Расположение:* `pkg/securitycontext/util_darwin.go:19`




## pkg/securitycontext/util_linux.go


📄 Исходный файл: `pkg/securitycontext/util_linux.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [possibleCPUs](#possiblecpus-pkgsecuritycontextutil_linuxgo28) `:28`


</details>


[function] name: possibleCPUs file: pkg/securitycontext/util_linux.go:28 returns_error: нет description: possibleCPUs returns the number of possible CPUs on this host.


### possibleCPUs (pkg/securitycontext/util_linux.go:28)


possibleCPUs returns the number of possible CPUs on this host.


```go
func possibleCPUs((cpus []int)) (cpus []int)
```


**Тип ответа:** cpus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/securitycontext/util_linux.go:28`




## pkg/securitycontext/util_windows.go


📄 Исходный файл: `pkg/securitycontext/util_windows.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [possibleCPUs](#possiblecpus-pkgsecuritycontextutil_windowsgo19) `:19`


</details>


[function] name: possibleCPUs file: pkg/securitycontext/util_windows.go:19 returns_error: нет description: —


### possibleCPUs (pkg/securitycontext/util_windows.go:19)


possibleCPUs is a function that performs operations based on the provided parameters and returns ().


```go
func possibleCPUs(()) ()
```


📍 *Расположение:* `pkg/securitycontext/util_windows.go:19`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_security.md)

- [Следующая директория](pkg_serviceaccount.md)


---

