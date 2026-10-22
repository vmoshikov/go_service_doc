---
title: "Функции: test/fuzz"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/fuzz
---


# Функции: test/fuzz


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_fixtures.md)

- [Следующая директория](test_images.md)


---


## Меню по файлам


- 📄 [test/fuzz/cbor/cbor.go](#testfuzzcborcborgo)

- 📄 [test/fuzz/json/json.go](#testfuzzjsonjsongo)

- 📄 [test/fuzz/yaml/yaml.go](#testfuzzyamlyamlgo)


---


## test/fuzz/cbor/cbor.go


📄 Исходный файл: `test/fuzz/cbor/cbor.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FuzzDecodeAllocations](#fuzzdecodeallocations-testfuzzcborcborgo39) `:39`


</details>


[function] name: FuzzDecodeAllocations file: test/fuzz/cbor/cbor.go:39 returns_error: нет description: FuzzDecodeAllocations is a go-fuzz target that panics on inputs that cause an unreasonably large
number of bytes to be a


### FuzzDecodeAllocations (test/fuzz/cbor/cbor.go:39)


FuzzDecodeAllocations is a go-fuzz target that panics on inputs that cause an unreasonably large
number of bytes to be allocated at decode time.


```go
func FuzzDecodeAllocations((result int)) (result int)
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


📍 *Расположение:* `test/fuzz/cbor/cbor.go:39`




## test/fuzz/json/json.go


📄 Исходный файл: `test/fuzz/json/json.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [FuzzNonStrictDecode](#fuzznonstrictdecode-testfuzzjsonjsongo117) `:117`

- 🔗 [FuzzStrictDecode](#fuzzstrictdecode-testfuzzjsonjsongo47) `:47`


</details>


[function] name: FuzzNonStrictDecode file: test/fuzz/json/json.go:117 returns_error: нет description: FuzzNonStrictDecode is a fuzz target for "k8s.io/apimachinery/pkg/runtime/serializer/json" non-strict decoding.


### FuzzNonStrictDecode (test/fuzz/json/json.go:117)


FuzzNonStrictDecode is a fuzz target for "k8s.io/apimachinery/pkg/runtime/serializer/json" non-strict decoding.


```go
func FuzzNonStrictDecode((data []byte)) (data []byte)
```


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


📍 *Расположение:* `test/fuzz/json/json.go:117`



---


[function] name: FuzzStrictDecode file: test/fuzz/json/json.go:47 returns_error: нет description: FuzzStrictDecode is a fuzz target for "k8s.io/apimachinery/pkg/runtime/serializer/json" strict decoding.


### FuzzStrictDecode (test/fuzz/json/json.go:47)


FuzzStrictDecode is a fuzz target for "k8s.io/apimachinery/pkg/runtime/serializer/json" strict decoding.


```go
func FuzzStrictDecode((data []byte)) (data []byte)
```


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


📍 *Расположение:* `test/fuzz/json/json.go:47`




## test/fuzz/yaml/yaml.go


📄 Исходный файл: `test/fuzz/yaml/yaml.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [FuzzDurationStrict](#fuzzdurationstrict-testfuzzyamlyamlgo34) `:34`

- 🔗 [FuzzMicroTimeStrict](#fuzzmicrotimestrict-testfuzzyamlyamlgo58) `:58`

- 🔗 [FuzzSigYaml](#fuzzsigyaml-testfuzzyamlyamlgo86) `:86`

- 🔗 [FuzzTimeStrict](#fuzztimestrict-testfuzzyamlyamlgo102) `:102`

- 🔗 [FuzzYamlV2](#fuzzyamlv2-testfuzzyamlyamlgo130) `:130`


</details>


[function] name: FuzzDurationStrict file: test/fuzz/yaml/yaml.go:34 returns_error: нет description: FuzzDurationStrict is a fuzz target for strict-unmarshaling Duration defined
in "k8s.io/apimachinery/pkg/apis/meta/v1". 


### FuzzDurationStrict (test/fuzz/yaml/yaml.go:34)


FuzzDurationStrict is a fuzz target for strict-unmarshaling Duration defined
in "k8s.io/apimachinery/pkg/apis/meta/v1". This target also checks that the
unmarshaled result can be marshaled back to the input.


```go
func FuzzDurationStrict((b []byte)) (b []byte)
```


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


📍 *Расположение:* `test/fuzz/yaml/yaml.go:34`



---


[function] name: FuzzMicroTimeStrict file: test/fuzz/yaml/yaml.go:58 returns_error: нет description: FuzzMicroTimeStrict is a fuzz target for strict-unmarshaling MicroTime
defined in "k8s.io/apimachinery/pkg/apis/meta/v1"


### FuzzMicroTimeStrict (test/fuzz/yaml/yaml.go:58)


FuzzMicroTimeStrict is a fuzz target for strict-unmarshaling MicroTime
defined in "k8s.io/apimachinery/pkg/apis/meta/v1". This target also checks
that the unmarshaled result can be marshaled back to the input.


```go
func FuzzMicroTimeStrict((b []byte)) (b []byte)
```


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


📍 *Расположение:* `test/fuzz/yaml/yaml.go:58`



---


[function] name: FuzzSigYaml file: test/fuzz/yaml/yaml.go:86 returns_error: нет description: FuzzSigYaml is a fuzz target for "sigs.k8s.io/yaml" unmarshaling.


### FuzzSigYaml (test/fuzz/yaml/yaml.go:86)


FuzzSigYaml is a fuzz target for "sigs.k8s.io/yaml" unmarshaling.


```go
func FuzzSigYaml((b []byte)) (b []byte)
```


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


📍 *Расположение:* `test/fuzz/yaml/yaml.go:86`



---


[function] name: FuzzTimeStrict file: test/fuzz/yaml/yaml.go:102 returns_error: нет description: FuzzTimeStrict is a fuzz target for strict-unmarshaling Time defined in
"k8s.io/apimachinery/pkg/apis/meta/v1". This tar


### FuzzTimeStrict (test/fuzz/yaml/yaml.go:102)


FuzzTimeStrict is a fuzz target for strict-unmarshaling Time defined in
"k8s.io/apimachinery/pkg/apis/meta/v1". This target also checks that the
unmarshaled result can be marshaled back to the input.


```go
func FuzzTimeStrict((b []byte)) (b []byte)
```


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


📍 *Расположение:* `test/fuzz/yaml/yaml.go:102`



---


[function] name: FuzzYamlV2 file: test/fuzz/yaml/yaml.go:130 returns_error: нет description: FuzzYamlV2 is a fuzz target for "go.yaml.in/yaml/v2" unmarshaling.


### FuzzYamlV2 (test/fuzz/yaml/yaml.go:130)


FuzzYamlV2 is a fuzz target for "go.yaml.in/yaml/v2" unmarshaling.


```go
func FuzzYamlV2((b []byte)) (b []byte)
```


**Тип ответа:** b


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


📍 *Расположение:* `test/fuzz/yaml/yaml.go:130`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_fixtures.md)

- [Следующая директория](test_images.md)


---

