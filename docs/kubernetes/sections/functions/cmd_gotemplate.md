---
title: "Функции: cmd/gotemplate"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/gotemplate
---


# Функции: cmd/gotemplate


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genyaml.md)

- [Следующая директория](cmd_import-boss.md)


---


## Меню по файлам


- 📄 [cmd/gotemplate/gotemplate.go](#cmdgotemplategotemplatego)


---


## cmd/gotemplate/gotemplate.go


📄 Исходный файл: `cmd/gotemplate/gotemplate.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [generate](#generate-cmdgotemplategotemplatego56) `:56`

- 🔗 [include](#include-cmdgotemplategotemplatego79) `:79`

- 🔗 [indent](#indent-cmdgotemplategotemplatego87) `:87`

- 🔗 [main](#main-cmdgotemplategotemplatego38) `:38`

- 🔗 [trim](#trim-cmdgotemplategotemplatego95) `:95`


</details>


[function] name: generate file: cmd/gotemplate/gotemplate.go:56 returns_error: нет description: —


### generate (cmd/gotemplate/gotemplate.go:56)


generate is a function that performs operations based on the provided parameters and returns (in io.Reader, out io.Writer, data interface{}).


```go
func generate((in io.Reader, out io.Writer, data interface{})) (in io.Reader, out io.Writer, data interface{})
```


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** io.Reader


```json
{
  "logger": {},
  "err": {},
  "r": {},
  "ping": false,
  "timeout": {},
  "protocols": {},
  "selectedProtocol": "string",
  "handleCrash": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/stream.go`


**Тип ответа:** out


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


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `cmd/gotemplate/gotemplate.go:56`



---


[function] name: include file: cmd/gotemplate/gotemplate.go:79 returns_error: да description: —


### include (cmd/gotemplate/gotemplate.go:79)


include is a function that performs operations based on the provided parameters and may return an error.


```go
func include((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/gotemplate/gotemplate.go:79`



---


[function] name: indent file: cmd/gotemplate/gotemplate.go:87 returns_error: нет description: —


### indent (cmd/gotemplate/gotemplate.go:87)


indent is a function that performs operations based on the provided parameters and returns (numSpaces int, content string).


```go
func indent((numSpaces int, content string)) (numSpaces int, content string)
```


**Тип ответа:** numSpaces


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/gotemplate/gotemplate.go:87`



---


[function] name: main file: cmd/gotemplate/gotemplate.go:38 returns_error: нет description: gotemplate is a simple CLI for text/template. It reads from stdin and writes to stdout.
Optional arguments are <key>=<va


### main (cmd/gotemplate/gotemplate.go:38)


gotemplate is a simple CLI for text/template. It reads from stdin and writes to stdout.
Optional arguments are <key>=<value> pairs which can be used as {{.<key>}} to inject
the <value> for that key.

Besides the default functions (https://pkg.go.dev/text/template#hdr-Functions),
gotemplate also implements:
- include <filename>: returns the content of that file as string
- indent <number of spaces> <string>: replace each newline with "newline + spaces", indent the newline at the end
- trim <string>: strip leading and trailing whitespace


```go
func main(()) ()
```


📍 *Расположение:* `cmd/gotemplate/gotemplate.go:38`



---


[function] name: trim file: cmd/gotemplate/gotemplate.go:95 returns_error: нет description: —


### trim (cmd/gotemplate/gotemplate.go:95)


trim is a function that performs operations based on the provided parameters and returns (content string).


```go
func trim((content string)) (content string)
```


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/gotemplate/gotemplate.go:95`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genyaml.md)

- [Следующая директория](cmd_import-boss.md)


---

