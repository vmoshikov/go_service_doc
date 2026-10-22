---
title: "Функции: atproto/atdata"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/atdata
---


# Функции: atproto/atdata


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_atcrypto.md)

- [Следующая директория](atproto_auth.md)


---


## Меню по файлам


- 📄 [atproto/atdata/blob.go](#atprotoatdatablobgo)

- 📄 [atproto/atdata/bytes.go](#atprotoatdatabytesgo)

- 📄 [atproto/atdata/cbor_gen.go](#atprotoatdatacbor_gengo)

- 📄 [atproto/atdata/cidlink.go](#atprotoatdatacidlinkgo)

- 📄 [atproto/atdata/data.go](#atprotoatdatadatago)

- 📄 [atproto/atdata/extract.go](#atprotoatdataextractgo)

- 📄 [atproto/atdata/parse.go](#atprotoatdataparsego)


---


## atproto/atdata/blob.go


📄 Исходный файл: `atproto/atdata/blob.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-atprotoatdatablobgo89) `:89`

- 🔗 [MarshalJSON](#marshaljson-atprotoatdatablobgo36) `:36`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotoatdatablobgo111) `:111`

- 🔗 [UnmarshalJSON](#unmarshaljson-atprotoatdatablobgo54) `:54`


</details>


[function] name: MarshalCBOR file: atproto/atdata/blob.go:89 returns_error: нет description: —


### MarshalCBOR (atproto/atdata/blob.go:89)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (b *Blob) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/blob.go:89`



---


[function] name: MarshalJSON file: atproto/atdata/blob.go:36 returns_error: да description: —


### MarshalJSON (atproto/atdata/blob.go:36)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (b Blob) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/blob.go:36`



---


[function] name: UnmarshalCBOR file: atproto/atdata/blob.go:111 returns_error: нет description: —


### UnmarshalCBOR (atproto/atdata/blob.go:111)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (lb *Blob) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `atproto/atdata/blob.go:111`



---


[function] name: UnmarshalJSON file: atproto/atdata/blob.go:54 returns_error: нет description: —


### UnmarshalJSON (atproto/atdata/blob.go:54)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (raw []byte).


```go
func (b *Blob) UnmarshalJSON((raw []byte)) (raw []byte)
```


**Тип ответа:** raw


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


📍 *Расположение:* `atproto/atdata/blob.go:54`




## atproto/atdata/bytes.go


📄 Исходный файл: `atproto/atdata/bytes.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-atprotoatdatabytesgo47) `:47`

- 🔗 [MarshalJSON](#marshaljson-atprotoatdatabytesgo23) `:23`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotoatdatabytesgo59) `:59`

- 🔗 [UnmarshalJSON](#unmarshaljson-atprotoatdatabytesgo33) `:33`


</details>


[function] name: MarshalCBOR file: atproto/atdata/bytes.go:47 returns_error: нет description: —


### MarshalCBOR (atproto/atdata/bytes.go:47)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (lb *Bytes) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/bytes.go:47`



---


[function] name: MarshalJSON file: atproto/atdata/bytes.go:23 returns_error: да description: —


### MarshalJSON (atproto/atdata/bytes.go:23)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (lb Bytes) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/bytes.go:23`



---


[function] name: UnmarshalCBOR file: atproto/atdata/bytes.go:59 returns_error: нет description: —


### UnmarshalCBOR (atproto/atdata/bytes.go:59)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (lb *Bytes) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `atproto/atdata/bytes.go:59`



---


[function] name: UnmarshalJSON file: atproto/atdata/bytes.go:33 returns_error: нет description: —


### UnmarshalJSON (atproto/atdata/bytes.go:33)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (raw []byte).


```go
func (lb *Bytes) UnmarshalJSON((raw []byte)) (raw []byte)
```


**Тип ответа:** raw


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


📍 *Расположение:* `atproto/atdata/bytes.go:33`




## atproto/atdata/cbor_gen.go


📄 Исходный файл: `atproto/atdata/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-atprotoatdatacbor_gengo21) `:21`

- 🔗 [MarshalCBOR](#marshalcbor-atprotoatdatacbor_gengo121) `:121`

- 🔗 [MarshalCBOR](#marshalcbor-atprotoatdatacbor_gengo255) `:255`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotoatdatacbor_gengo58) `:58`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotoatdatacbor_gengo181) `:181`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotoatdatacbor_gengo349) `:349`


</details>


[function] name: MarshalCBOR file: atproto/atdata/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (atproto/atdata/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GenericRecord) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/cbor_gen.go:21`



---


[function] name: MarshalCBOR file: atproto/atdata/cbor_gen.go:121 returns_error: нет description: —


### MarshalCBOR (atproto/atdata/cbor_gen.go:121)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LegacyBlobSchema) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/cbor_gen.go:121`



---


[function] name: MarshalCBOR file: atproto/atdata/cbor_gen.go:255 returns_error: нет description: —


### MarshalCBOR (atproto/atdata/cbor_gen.go:255)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *BlobSchema) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/cbor_gen.go:255`



---


[function] name: UnmarshalCBOR file: atproto/atdata/cbor_gen.go:58 returns_error: да description: —


### UnmarshalCBOR (atproto/atdata/cbor_gen.go:58)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GenericRecord) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `atproto/atdata/cbor_gen.go:58`



---


[function] name: UnmarshalCBOR file: atproto/atdata/cbor_gen.go:181 returns_error: да description: —


### UnmarshalCBOR (atproto/atdata/cbor_gen.go:181)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LegacyBlobSchema) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `atproto/atdata/cbor_gen.go:181`



---


[function] name: UnmarshalCBOR file: atproto/atdata/cbor_gen.go:349 returns_error: да description: —


### UnmarshalCBOR (atproto/atdata/cbor_gen.go:349)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *BlobSchema) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `atproto/atdata/cbor_gen.go:349`




## atproto/atdata/cidlink.go


📄 Исходный файл: `atproto/atdata/cidlink.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [CID](#cid-atprotoatdatacidlinkgo22) `:22`

- 🔗 [IsDefined](#isdefined-atprotoatdatacidlinkgo37) `:37`

- 🔗 [MarshalCBOR](#marshalcbor-atprotoatdatacidlinkgo65) `:65`

- 🔗 [MarshalJSON](#marshaljson-atprotoatdatacidlinkgo41) `:41`

- 🔗 [String](#string-atprotoatdatacidlinkgo29) `:29`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotoatdatacidlinkgo80) `:80`

- 🔗 [UnmarshalJSON](#unmarshaljson-atprotoatdatacidlinkgo51) `:51`


</details>


[function] name: CID file: atproto/atdata/cidlink.go:22 returns_error: нет description: Unwraps the inner cid.Cid type (github.com/ipfs/go-cid)


### CID (atproto/atdata/cidlink.go:22)


Unwraps the inner cid.Cid type (github.com/ipfs/go-cid)


```go
func (ll CIDLink) CID(()) ()
```


📍 *Расположение:* `atproto/atdata/cidlink.go:22`



---


[function] name: IsDefined file: atproto/atdata/cidlink.go:37 returns_error: нет description: Convenience helper, returns false if CID is "undefined" (golang zero value)


### IsDefined (atproto/atdata/cidlink.go:37)


Convenience helper, returns false if CID is "undefined" (golang zero value)


```go
func (ll CIDLink) IsDefined(()) ()
```


📍 *Расположение:* `atproto/atdata/cidlink.go:37`



---


[function] name: MarshalCBOR file: atproto/atdata/cidlink.go:65 returns_error: нет description: —


### MarshalCBOR (atproto/atdata/cidlink.go:65)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (ll *CIDLink) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/cidlink.go:65`



---


[function] name: MarshalJSON file: atproto/atdata/cidlink.go:41 returns_error: да description: —


### MarshalJSON (atproto/atdata/cidlink.go:41)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (ll CIDLink) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/cidlink.go:41`



---


[function] name: String file: atproto/atdata/cidlink.go:29 returns_error: нет description: Returns string representation.

If the CID is "undefined", returns an empty string (note that this is different from how


### String (atproto/atdata/cidlink.go:29)


Returns string representation.

If the CID is "undefined", returns an empty string (note that this is different from how cid.Cid works).


```go
func (ll CIDLink) String(()) ()
```


📍 *Расположение:* `atproto/atdata/cidlink.go:29`



---


[function] name: UnmarshalCBOR file: atproto/atdata/cidlink.go:80 returns_error: нет description: —


### UnmarshalCBOR (atproto/atdata/cidlink.go:80)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (ll *CIDLink) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `atproto/atdata/cidlink.go:80`



---


[function] name: UnmarshalJSON file: atproto/atdata/cidlink.go:51 returns_error: нет description: —


### UnmarshalJSON (atproto/atdata/cidlink.go:51)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (raw []byte).


```go
func (ll *CIDLink) UnmarshalJSON((raw []byte)) (raw []byte)
```


**Тип ответа:** raw


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


📍 *Расположение:* `atproto/atdata/cidlink.go:51`




## atproto/atdata/data.go


📄 Исходный файл: `atproto/atdata/data.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [ExtractBlobs](#extractblobs-atprotoatdatadatago58) `:58`

- 🔗 [MarshalCBOR](#marshalcbor-atprotoatdatadatago83) `:83`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotoatdatadatago39) `:39`

- 🔗 [UnmarshalJSON](#unmarshaljson-atprotoatdatadatago22) `:22`

- 🔗 [Validate](#validate-atprotoatdatadatago14) `:14`

- 🔗 [extractBlobsAtom](#extractblobsatom-atprotoatdatadatago62) `:62`

- 🔗 [forCBOR](#forcbor-atprotoatdatadatago88) `:88`

- 🔗 [forCBORArray](#forcborarray-atprotoatdatadatago120) `:120`


</details>


[function] name: ExtractBlobs file: atproto/atdata/data.go:58 returns_error: нет description: Recursively finds all the "blob" objects from generic atproto data (which has already been parsed).

Returns an array wi


### ExtractBlobs (atproto/atdata/data.go:58)


Recursively finds all the "blob" objects from generic atproto data (which has already been parsed).

Returns an array with all Blob instances; does not de-dupe.


```go
func ExtractBlobs((obj map[string]any)) (obj map[string]any)
```


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/data.go:58`



---


[function] name: MarshalCBOR file: atproto/atdata/data.go:83 returns_error: да description: Serializes generic atproto data (object) to DAG-CBOR bytes

Does not re-validate that data conforms to atproto data mode


### MarshalCBOR (atproto/atdata/data.go:83)


Serializes generic atproto data (object) to DAG-CBOR bytes

Does not re-validate that data conforms to atproto data model, but does handle Blob, Bytes, and CIDLink as expected.


```go
func MarshalCBOR(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/data.go:83`



---


[function] name: UnmarshalCBOR file: atproto/atdata/data.go:39 returns_error: да description: Parses generic data (object) in CBOR (specifically, IPLD dag-cbor), validating against the atproto data model at the sam


### UnmarshalCBOR (atproto/atdata/data.go:39)


Parses generic data (object) in CBOR (specifically, IPLD dag-cbor), validating against the atproto data model at the same time.


```go
func UnmarshalCBOR((map[string]any, error)) (map[string]any, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/data.go:39`



---


[function] name: UnmarshalJSON file: atproto/atdata/data.go:22 returns_error: да description: Parses generic data (object) in JSON, validating against the atproto data model at the same time.

The standard library'


### UnmarshalJSON (atproto/atdata/data.go:22)


Parses generic data (object) in JSON, validating against the atproto data model at the same time.

The standard library's MarshalJSON can be used to invert this function.


```go
func UnmarshalJSON((map[string]any, error)) (map[string]any, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/data.go:22`



---


[function] name: Validate file: atproto/atdata/data.go:14 returns_error: нет description: Checks that generic data (object) complies with the atproto data model.


### Validate (atproto/atdata/data.go:14)


Checks that generic data (object) complies with the atproto data model.


```go
func Validate((obj map[string]any)) (obj map[string]any)
```


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/data.go:14`



---


[function] name: extractBlobsAtom file: atproto/atdata/data.go:62 returns_error: нет description: —


### extractBlobsAtom (atproto/atdata/data.go:62)


extractBlobsAtom is a function that performs operations based on the provided parameters and returns (atom any).


```go
func extractBlobsAtom((atom any)) (atom any)
```


**Тип ответа:** atom


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/data.go:62`



---


[function] name: forCBOR file: atproto/atdata/data.go:88 returns_error: нет description: helper to get generic data in the correct "shape" for serialization with ipfs/go-ipld-cbor


### forCBOR (atproto/atdata/data.go:88)


helper to get generic data in the correct "shape" for serialization with ipfs/go-ipld-cbor


```go
func forCBOR((obj map[string]any)) (obj map[string]any)
```


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/data.go:88`



---


[function] name: forCBORArray file: atproto/atdata/data.go:120 returns_error: нет description: recursive helper for forCBOR


### forCBORArray (atproto/atdata/data.go:120)


recursive helper for forCBOR


```go
func forCBORArray((arr []any)) (arr []any)
```


**Тип ответа:** arr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atdata/data.go:120`




## atproto/atdata/extract.go


📄 Исходный файл: `atproto/atdata/extract.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [ExtractTypeCBOR](#extracttypecbor-atprotoatdataextractgo26) `:26`

- 🔗 [ExtractTypeCBORReader](#extracttypecborreader-atprotoatdataextractgo39) `:39`

- 🔗 [ExtractTypeJSON](#extracttypejson-atprotoatdataextractgo16) `:16`


</details>


[function] name: ExtractTypeCBOR file: atproto/atdata/extract.go:26 returns_error: да description: Parses the top-level $type field from generic atproto CBOR data


### ExtractTypeCBOR (atproto/atdata/extract.go:26)


Parses the top-level $type field from generic atproto CBOR data


```go
func ExtractTypeCBOR((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/extract.go:26`



---


[function] name: ExtractTypeCBORReader file: atproto/atdata/extract.go:39 returns_error: да description: Parses top-level $type field from generic atproto CBOR.

Returns that string field, and additional bytes (TODO: the pars


### ExtractTypeCBORReader (atproto/atdata/extract.go:39)


Parses top-level $type field from generic atproto CBOR.

Returns that string field, and additional bytes (TODO: the parsed bytes, or remaining bytes?)


```go
func ExtractTypeCBORReader((string, []byte, error)) (string, []byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/extract.go:39`



---


[function] name: ExtractTypeJSON file: atproto/atdata/extract.go:16 returns_error: да description: Parses the top-level $type field from generic atproto JSON data


### ExtractTypeJSON (atproto/atdata/extract.go:16)


Parses the top-level $type field from generic atproto JSON data


```go
func ExtractTypeJSON((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/extract.go:16`




## atproto/atdata/parse.go


📄 Исходный файл: `atproto/atdata/parse.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [parseArray](#parsearray-atprotoatdataparsego73) `:73`

- 🔗 [parseAtom](#parseatom-atprotoatdataparsego19) `:19`

- 🔗 [parseBlob](#parseblob-atprotoatdataparsego175) `:175`

- 🔗 [parseBytes](#parsebytes-atprotoatdataparsego159) `:159`

- 🔗 [parseFloat](#parsefloat-atprotoatdataparsego12) `:12`

- 🔗 [parseLegacyBlob](#parselegacyblob-atprotoatdataparsego228) `:228`

- 🔗 [parseLink](#parselink-atprotoatdataparsego140) `:140`

- 🔗 [parseMap](#parsemap-atprotoatdataparsego88) `:88`

- 🔗 [parseObject](#parseobject-atprotoatdataparsego252) `:252`


</details>


[function] name: parseArray file: atproto/atdata/parse.go:73 returns_error: да description: —


### parseArray (atproto/atdata/parse.go:73)


parseArray is a function that performs operations based on the provided parameters and may return an error.


```go
func parseArray(([]any, error)) ([]any, error)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:73`



---


[function] name: parseAtom file: atproto/atdata/parse.go:19 returns_error: да description: —


### parseAtom (atproto/atdata/parse.go:19)


parseAtom is a function that performs operations based on the provided parameters and may return an error.


```go
func parseAtom((any, error)) (any, error)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:19`



---


[function] name: parseBlob file: atproto/atdata/parse.go:175 returns_error: да description: NOTE: doesn't handle legacy blobs yet!


### parseBlob (atproto/atdata/parse.go:175)


NOTE: doesn't handle legacy blobs yet!


```go
func parseBlob((*Blob, error)) (*Blob, error)
```


**Тип запроса:** Blob


```json
{
  "Ref": {},
  "MimeType": "string",
  "Size": 0
}
```


*Определено в:* `atproto/atdata/blob.go`


**Тип ответа:** Blob


```json
{
  "Ref": {},
  "MimeType": "string",
  "Size": 0
}
```


*Определено в:* `atproto/atdata/blob.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Blob`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:175`



---


[function] name: parseBytes file: atproto/atdata/parse.go:159 returns_error: да description: —


### parseBytes (atproto/atdata/parse.go:159)


parseBytes is a function that performs operations based on the provided parameters and may return an error.


```go
func parseBytes((Bytes, error)) (Bytes, error)
```


**Тип ответа:** Bytes


```json
{
  "Bytes": "string"
}
```


*Определено в:* `atproto/atdata/bytes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Bytes`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:159`



---


[function] name: parseFloat file: atproto/atdata/parse.go:12 returns_error: да description: —


### parseFloat (atproto/atdata/parse.go:12)


parseFloat is a function that performs operations based on the provided parameters and may return an error.


```go
func parseFloat((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:12`



---


[function] name: parseLegacyBlob file: atproto/atdata/parse.go:228 returns_error: да description: —


### parseLegacyBlob (atproto/atdata/parse.go:228)


parseLegacyBlob is a function that performs operations based on the provided parameters and may return an error.


```go
func parseLegacyBlob((*Blob, error)) (*Blob, error)
```


**Тип запроса:** Blob


```json
{
  "Ref": {},
  "MimeType": "string",
  "Size": 0
}
```


*Определено в:* `atproto/atdata/blob.go`


**Тип ответа:** Blob


```json
{
  "Ref": {},
  "MimeType": "string",
  "Size": 0
}
```


*Определено в:* `atproto/atdata/blob.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Blob`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:228`



---


[function] name: parseLink file: atproto/atdata/parse.go:140 returns_error: да description: —


### parseLink (atproto/atdata/parse.go:140)


parseLink is a function that performs operations based on the provided parameters and may return an error.


```go
func parseLink((CIDLink, error)) (CIDLink, error)
```


**Тип ответа:** CIDLink


```json
{
  "Type": "string",
  "Description": "string"
}
```


*Определено в:* `atproto/lexicon/language.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CIDLink`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:140`



---


[function] name: parseMap file: atproto/atdata/parse.go:88 returns_error: да description: —


### parseMap (atproto/atdata/parse.go:88)


parseMap is a function that performs operations based on the provided parameters and may return an error.


```go
func parseMap((any, error)) (any, error)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:88`



---


[function] name: parseObject file: atproto/atdata/parse.go:252 returns_error: да description: —


### parseObject (atproto/atdata/parse.go:252)


parseObject is a function that performs operations based on the provided parameters and may return an error.


```go
func parseObject((map[string]any, error)) (map[string]any, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atdata/parse.go:252`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_atcrypto.md)

- [Следующая директория](atproto_auth.md)


---

