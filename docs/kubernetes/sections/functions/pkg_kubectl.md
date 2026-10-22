---
title: "Функции: pkg/kubectl"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/kubectl
---


# Функции: pkg/kubectl


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_kubeapiserver.md)

- [Следующая директория](pkg_kubelet.md)


---


## Меню по файлам


- 📄 [pkg/kubectl/cmd/convert/convert.go](#pkgkubectlcmdconvertconvertgo)


---


## pkg/kubectl/cmd/convert/convert.go


📄 Исходный файл: `pkg/kubectl/cmd/convert/convert.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Complete](#complete-pkgkubectlcmdconvertconvertgo115) `:115`

- 🔗 [NewCmdConvert](#newcmdconvert-pkgkubectlcmdconvertconvertgo90) `:90`

- 🔗 [NewConvertOptions](#newconvertoptions-pkgkubectlcmdconvertconvertgo80) `:80`

- 🔗 [RunConvert](#runconvert-pkgkubectlcmdconvertconvertgo141) `:141`

- 🔗 [asVersionedObject](#asversionedobject-pkgkubectlcmdconvertconvertgo196) `:196`

- 🔗 [asVersionedObjects](#asversionedobjects-pkgkubectlcmdconvertconvertgo234) `:234`

- 🔗 [tryConvert](#tryconvert-pkgkubectlcmdconvertconvertgo284) `:284`


</details>


[function] name: Complete file: pkg/kubectl/cmd/convert/convert.go:115 returns_error: да description: Complete collects information required to run Convert command from command line.


### Complete (pkg/kubectl/cmd/convert/convert.go:115)


Complete collects information required to run Convert command from command line.


```go
func (o *ConvertOptions) Complete((err error)) (err error)
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


📍 *Расположение:* `pkg/kubectl/cmd/convert/convert.go:115`



---


[function] name: NewCmdConvert file: pkg/kubectl/cmd/convert/convert.go:90 returns_error: нет description: NewCmdConvert creates a command object for the generic "convert" action, which
translates the config file into a given v


### NewCmdConvert (pkg/kubectl/cmd/convert/convert.go:90)


NewCmdConvert creates a command object for the generic "convert" action, which
translates the config file into a given version.


```go
func NewCmdConvert((f cmdutil.Factory, ioStreams genericiooptions.IOStreams)) (f cmdutil.Factory, ioStreams genericiooptions.IOStreams)
```


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


**Тип ответа:** cmdutil.Factory


```json
{
  "client": {},
  "namespace": "string",
  "tweakListOptions": {},
  "lock": {},
  "defaultResync": {},
  "customResync": {},
  "transform": {},
  "informerName": null,
  "informers": {},
  "startedInformers": {},
  "wg": {},
  "shuttingDown": false
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/factory.go`


**Тип ответа:** ioStreams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genericiooptions.IOStreams


```json
{
  "In": {},
  "Out": {},
  "ErrOut": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/genericiooptions/io_options.go`


📍 *Расположение:* `pkg/kubectl/cmd/convert/convert.go:90`



---


[function] name: NewConvertOptions file: pkg/kubectl/cmd/convert/convert.go:80 returns_error: нет description: —


### NewConvertOptions (pkg/kubectl/cmd/convert/convert.go:80)


NewConvertOptions is a function that performs operations based on the provided parameters and returns (ioStreams genericiooptions.IOStreams).


```go
func NewConvertOptions((ioStreams genericiooptions.IOStreams)) (ioStreams genericiooptions.IOStreams)
```


**Тип ответа:** ioStreams


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genericiooptions.IOStreams


```json
{
  "In": {},
  "Out": {},
  "ErrOut": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/genericiooptions/io_options.go`


📍 *Расположение:* `pkg/kubectl/cmd/convert/convert.go:80`



---


[function] name: RunConvert file: pkg/kubectl/cmd/convert/convert.go:141 returns_error: нет description: RunConvert implements the generic Convert command


### RunConvert (pkg/kubectl/cmd/convert/convert.go:141)


RunConvert implements the generic Convert command


```go
func (o *ConvertOptions) RunConvert(()) ()
```


📍 *Расположение:* `pkg/kubectl/cmd/convert/convert.go:141`



---


[function] name: asVersionedObject file: pkg/kubectl/cmd/convert/convert.go:196 returns_error: да description: asVersionedObject converts a list of infos into a single object - either a List containing
the objects as children, or i


### asVersionedObject (pkg/kubectl/cmd/convert/convert.go:196)


asVersionedObject converts a list of infos into a single object - either a List containing
the objects as children, or if only a single Object is present, as that object. The provided
version will be preferred as the conversion target, but the Object's mapping version will be
used if that version is not present.


```go
func asVersionedObject((runtime.Object, error)) (runtime.Object, error)
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


📍 *Расположение:* `pkg/kubectl/cmd/convert/convert.go:196`



---


[function] name: asVersionedObjects file: pkg/kubectl/cmd/convert/convert.go:234 returns_error: да description: asVersionedObjects converts a list of infos into versioned objects. The provided
version will be preferred as the conver


### asVersionedObjects (pkg/kubectl/cmd/convert/convert.go:234)


asVersionedObjects converts a list of infos into versioned objects. The provided
version will be preferred as the conversion target, but the Object's mapping version will be
used if that version is not present.


```go
func asVersionedObjects(([]runtime.Object, error)) ([]runtime.Object, error)
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


*Типы возврата:* `[]runtime.Object`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/kubectl/cmd/convert/convert.go:234`



---


[function] name: tryConvert file: pkg/kubectl/cmd/convert/convert.go:284 returns_error: да description: tryConvert attempts to convert the given object to the provided versions in order. This function assumes
the object is i


### tryConvert (pkg/kubectl/cmd/convert/convert.go:284)


tryConvert attempts to convert the given object to the provided versions in order. This function assumes
the object is in internal version.


```go
func tryConvert((runtime.Object, error)) (runtime.Object, error)
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


📍 *Расположение:* `pkg/kubectl/cmd/convert/convert.go:284`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_kubeapiserver.md)

- [Следующая директория](pkg_kubelet.md)


---

