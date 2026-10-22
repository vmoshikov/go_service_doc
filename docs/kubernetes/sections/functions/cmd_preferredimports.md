---
title: "Функции: cmd/preferredimports"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/preferredimports
---


# Функции: cmd/preferredimports


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kubemark.md)

- [Следующая директория](cmd_prune-junit-xml.md)


---


## Меню по файлам


- 📄 [cmd/preferredimports/preferredimports.go](#cmdpreferredimportspreferredimportsgo)


---


## cmd/preferredimports/preferredimports.go


📄 Исходный файл: `cmd/preferredimports/preferredimports.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [collect](#collect-cmdpreferredimportspreferredimportsgo70) `:70`

- 🔗 [filterFiles](#filterfiles-cmdpreferredimportspreferredimportsgo180) `:180`

- 🔗 [handlePath](#handlepath-cmdpreferredimportspreferredimportsgo196) `:196`

- 🔗 [main](#main-cmdpreferredimportspreferredimportsgo222) `:222`

- 🔗 [newAnalyzer](#newanalyzer-cmdpreferredimportspreferredimportsgo56) `:56`

- 🔗 [renameImportUsages](#renameimportusages-cmdpreferredimportspreferredimportsgo152) `:152`


</details>


[function] name: collect file: cmd/preferredimports/preferredimports.go:70 returns_error: нет description: collect extracts test metadata from a file.


### collect (cmd/preferredimports/preferredimports.go:70)


collect extracts test metadata from a file.


```go
func (a *analyzer) collect((dir string)) (dir string)
```


**Тип ответа:** dir


```json
{
  "name": "string",
  "goRestfulContainer": null,
  "nonGoRestfulMux": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/handler.go`


📍 *Расположение:* `cmd/preferredimports/preferredimports.go:70`



---


[function] name: filterFiles file: cmd/preferredimports/preferredimports.go:180 returns_error: нет description: —


### filterFiles (cmd/preferredimports/preferredimports.go:180)


filterFiles is a method that performs operations based on the provided parameters and returns (fs map[string]*ast.File).


```go
func (a *analyzer) filterFiles((fs map[string]*ast.File)) (fs map[string]*ast.File)
```


**Тип запроса:** ast.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип ответа:** fs


```json
{
  "EndpointsName": "string",
  "Path": "string",
  "ReadOnly": false
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/glusterfsvolumesource.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ast.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


📍 *Расположение:* `cmd/preferredimports/preferredimports.go:180`



---


[function] name: handlePath file: cmd/preferredimports/preferredimports.go:196 returns_error: да description: handlePath walks the filesystem recursively, collecting directories,
ignoring some unneeded directories (hidden/vendored


### handlePath (cmd/preferredimports/preferredimports.go:196)


handlePath walks the filesystem recursively, collecting directories,
ignoring some unneeded directories (hidden/vendored) that are handled
specially later.


```go
func (c *collector) handlePath((path string, info os.FileInfo, err error)) (path string, info os.FileInfo, err error)
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


**Тип ответа:** info


```json
{
  "lister": {}
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/admission/pods.go`


**Тип ответа:** os.FileInfo


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


*Типы возврата:* `path string`, `info os.FileInfo`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/preferredimports/preferredimports.go:196`



---


[function] name: main file: cmd/preferredimports/preferredimports.go:222 returns_error: нет description: —


### main (cmd/preferredimports/preferredimports.go:222)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/preferredimports/preferredimports.go:222`



---


[function] name: newAnalyzer file: cmd/preferredimports/preferredimports.go:56 returns_error: нет description: —


### newAnalyzer (cmd/preferredimports/preferredimports.go:56)


newAnalyzer is a function that performs operations based on the provided parameters and returns ().


```go
func newAnalyzer(()) ()
```


📍 *Расположение:* `cmd/preferredimports/preferredimports.go:56`



---


[function] name: renameImportUsages file: cmd/preferredimports/preferredimports.go:152 returns_error: нет description: —


### renameImportUsages (cmd/preferredimports/preferredimports.go:152)


renameImportUsages is a function that performs operations based on the provided parameters and returns (f *ast.File, old, new string).


```go
func renameImportUsages((f *ast.File, old, new string)) (f *ast.File, old, new string)
```


**Тип запроса:** ast.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


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


**Тип ответа:** ast.File


```json
{
  "KubeConfigPath": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип ответа:** old


```json
{
  "Dial": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/config.go`


**Тип ответа:** new


```json
{
  "cfgPath": "string",
  "kubeconfigPath": "string",
  "cfg": {}
}
```


*Определено в:* `cmd/kubeadm/app/cmd/certs.go`


📍 *Расположение:* `cmd/preferredimports/preferredimports.go:152`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_kubemark.md)

- [Следующая директория](cmd_prune-junit-xml.md)


---

