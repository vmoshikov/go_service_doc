---
title: "Функции: pkg/capabilities"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/capabilities
---


# Функции: pkg/capabilities


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_auth.md)

- [Следующая директория](pkg_certauthorization.md)


---


## Меню по файлам


- 📄 [pkg/capabilities/capabilities.go](#pkgcapabilitiescapabilitiesgo)


---


## pkg/capabilities/capabilities.go


📄 Исходный файл: `pkg/capabilities/capabilities.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Get](#get-pkgcapabilitiescapabilitiesgo81) `:81`

- 🔗 [Initialize](#initialize-pkgcapabilitiescapabilitiesgo56) `:56`

- 🔗 [ResetForTest](#resetfortest-pkgcapabilitiescapabilitiesgo73) `:73`

- 🔗 [Setup](#setup-pkgcapabilitiescapabilitiesgo64) `:64`


</details>


[function] name: Get file: pkg/capabilities/capabilities.go:81 returns_error: нет description: Get returns a read-only copy of the system capabilities.


### Get (pkg/capabilities/capabilities.go:81)


Get returns a read-only copy of the system capabilities.


```go
func Get(()) ()
```


📍 *Расположение:* `pkg/capabilities/capabilities.go:81`



---


[function] name: Initialize file: pkg/capabilities/capabilities.go:56 returns_error: нет description: Initialize the capability set.  This can only be done once per binary, subsequent calls are ignored.


### Initialize (pkg/capabilities/capabilities.go:56)


Initialize the capability set.  This can only be done once per binary, subsequent calls are ignored.


```go
func Initialize((c Capabilities)) (c Capabilities)
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


**Тип ответа:** Capabilities


```json
{
  "AllowPrivileged": false,
  "PrivilegedSources": {},
  "PerConnectionBandwidthLimitBytesPerSec": 0
}
```


*Определено в:* `pkg/capabilities/capabilities.go`


📍 *Расположение:* `pkg/capabilities/capabilities.go:56`



---


[function] name: ResetForTest file: pkg/capabilities/capabilities.go:73 returns_error: нет description: ResetForTest resets the capabilities to a given state for testing purposes.
This function should only be called from tes


### ResetForTest (pkg/capabilities/capabilities.go:73)


ResetForTest resets the capabilities to a given state for testing purposes.
This function should only be called from tests.


```go
func ResetForTest(()) ()
```


📍 *Расположение:* `pkg/capabilities/capabilities.go:73`



---


[function] name: Setup file: pkg/capabilities/capabilities.go:64 returns_error: нет description: Setup the capability set.  It wraps Initialize for improving usability.


### Setup (pkg/capabilities/capabilities.go:64)


Setup the capability set.  It wraps Initialize for improving usability.


```go
func Setup((allowPrivileged bool, perConnectionBytesPerSec int64)) (allowPrivileged bool, perConnectionBytesPerSec int64)
```


**Тип ответа:** allowPrivileged


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** perConnectionBytesPerSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/capabilities/capabilities.go:64`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_auth.md)

- [Следующая директория](pkg_certauthorization.md)


---

