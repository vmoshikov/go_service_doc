---
title: "Функции: lex/util"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: lex/util
---


# Функции: lex/util


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](lex_lexlint.md)

- [Следующая директория](models.md)


---


## Меню по файлам


- 📄 [lex/util/cbor_gen.go](#lexutilcbor_gengo)

- 📄 [lex/util/decoder.go](#lexutildecodergo)

- 📄 [lex/util/lex_types.go](#lexutillex_typesgo)

- 📄 [lex/util/util.go](#lexutilutilgo)


---


## lex/util/cbor_gen.go


📄 Исходный файл: `lex/util/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-lexutilcbor_gengo21) `:21`

- 🔗 [MarshalCBOR](#marshalcbor-lexutilcbor_gengo121) `:121`

- 🔗 [MarshalCBOR](#marshalcbor-lexutilcbor_gengo255) `:255`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-lexutilcbor_gengo58) `:58`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-lexutilcbor_gengo181) `:181`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-lexutilcbor_gengo349) `:349`


</details>


[function] name: MarshalCBOR file: lex/util/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (lex/util/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *CborChecker) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `lex/util/cbor_gen.go:21`



---


[function] name: MarshalCBOR file: lex/util/cbor_gen.go:121 returns_error: нет description: —


### MarshalCBOR (lex/util/cbor_gen.go:121)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LegacyBlob) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `lex/util/cbor_gen.go:121`



---


[function] name: MarshalCBOR file: lex/util/cbor_gen.go:255 returns_error: нет description: —


### MarshalCBOR (lex/util/cbor_gen.go:255)


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


📍 *Расположение:* `lex/util/cbor_gen.go:255`



---


[function] name: UnmarshalCBOR file: lex/util/cbor_gen.go:58 returns_error: да description: —


### UnmarshalCBOR (lex/util/cbor_gen.go:58)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *CborChecker) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `lex/util/cbor_gen.go:58`



---


[function] name: UnmarshalCBOR file: lex/util/cbor_gen.go:181 returns_error: да description: —


### UnmarshalCBOR (lex/util/cbor_gen.go:181)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LegacyBlob) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `lex/util/cbor_gen.go:181`



---


[function] name: UnmarshalCBOR file: lex/util/cbor_gen.go:349 returns_error: да description: —


### UnmarshalCBOR (lex/util/cbor_gen.go:349)


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


📍 *Расположение:* `lex/util/cbor_gen.go:349`




## lex/util/decoder.go


📄 Исходный файл: `lex/util/decoder.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [CborDecodeValue](#cbordecodevalue-lexutildecodergo71) `:71`

- 🔗 [JsonDecodeValue](#jsondecodevalue-lexutildecodergo43) `:43`

- 🔗 [MarshalJSON](#marshaljson-lexutildecodergo111) `:111`

- 🔗 [NewFromType](#newfromtype-lexutildecodergo34) `:34`

- 🔗 [RegisterType](#registertype-lexutildecodergo20) `:20`

- 🔗 [UnmarshalJSON](#unmarshaljson-lexutildecodergo100) `:100`

- 🔗 [init](#init-lexutildecodergo15) `:15`


</details>


[function] name: CborDecodeValue file: lex/util/decoder.go:71 returns_error: да description: —


### CborDecodeValue (lex/util/decoder.go:71)


CborDecodeValue is a function that performs operations based on the provided parameters and may return an error.


```go
func CborDecodeValue((CBOR, error)) (CBOR, error)
```


**Тип ответа:** CBOR


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CBOR`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/decoder.go:71`



---


[function] name: JsonDecodeValue file: lex/util/decoder.go:43 returns_error: да description: —


### JsonDecodeValue (lex/util/decoder.go:43)


JsonDecodeValue is a function that performs operations based on the provided parameters and may return an error.


```go
func JsonDecodeValue((any, error)) (any, error)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/decoder.go:43`



---


[function] name: MarshalJSON file: lex/util/decoder.go:111 returns_error: да description: —


### MarshalJSON (lex/util/decoder.go:111)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (ltd *LexiconTypeDecoder) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/decoder.go:111`



---


[function] name: NewFromType file: lex/util/decoder.go:34 returns_error: да description: —


### NewFromType (lex/util/decoder.go:34)


NewFromType is a function that performs operations based on the provided parameters and may return an error.


```go
func NewFromType((interface{}, error)) (interface{}, error)
```


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `interface{}`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/decoder.go:34`



---


[function] name: RegisterType file: lex/util/decoder.go:20 returns_error: нет description: —


### RegisterType (lex/util/decoder.go:20)


RegisterType is a function that performs operations based on the provided parameters and returns (id string, val cbg.CBORMarshaler).


```go
func RegisterType((id string, val cbg.CBORMarshaler)) (id string, val cbg.CBORMarshaler)
```


**Тип ответа:** id


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** val


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** cbg.CBORMarshaler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/util/decoder.go:20`



---


[function] name: UnmarshalJSON file: lex/util/decoder.go:100 returns_error: нет description: —


### UnmarshalJSON (lex/util/decoder.go:100)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (ltd *LexiconTypeDecoder) UnmarshalJSON((b []byte)) (b []byte)
```


**Тип ответа:** b


```json
{
  "db": null,
  "collections": {},
  "collectionNames": {},
  "maxCollectionId": 0,
  "collectionsLock": {},
  "log": null
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


📍 *Расположение:* `lex/util/decoder.go:100`



---


[function] name: init file: lex/util/decoder.go:15 returns_error: нет description: —


### init (lex/util/decoder.go:15)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `lex/util/decoder.go:15`




## lex/util/lex_types.go


📄 Исходный файл: `lex/util/lex_types.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [Defined](#defined-lexutillex_typesgo33) `:33`

- 🔗 [MarshalCBOR](#marshalcbor-lexutillex_typesgo61) `:61`

- 🔗 [MarshalCBOR](#marshalcbor-lexutillex_typesgo116) `:116`

- 🔗 [MarshalCBOR](#marshalcbor-lexutillex_typesgo212) `:212`

- 🔗 [MarshalJSON](#marshaljson-lexutillex_typesgo37) `:37`

- 🔗 [MarshalJSON](#marshaljson-lexutillex_typesgo92) `:92`

- 🔗 [MarshalJSON](#marshaljson-lexutillex_typesgo159) `:159`

- 🔗 [String](#string-lexutillex_typesgo28) `:28`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-lexutillex_typesgo76) `:76`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-lexutillex_typesgo128) `:128`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-lexutillex_typesgo234) `:234`

- 🔗 [UnmarshalJSON](#unmarshaljson-lexutillex_typesgo47) `:47`

- 🔗 [UnmarshalJSON](#unmarshaljson-lexutillex_typesgo102) `:102`

- 🔗 [UnmarshalJSON](#unmarshaljson-lexutillex_typesgo177) `:177`


</details>


[function] name: Defined file: lex/util/lex_types.go:33 returns_error: нет description: convenience helper


### Defined (lex/util/lex_types.go:33)


convenience helper


```go
func (ll LexLink) Defined(()) ()
```


📍 *Расположение:* `lex/util/lex_types.go:33`



---


[function] name: MarshalCBOR file: lex/util/lex_types.go:61 returns_error: нет description: —


### MarshalCBOR (lex/util/lex_types.go:61)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (ll *LexLink) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `lex/util/lex_types.go:61`



---


[function] name: MarshalCBOR file: lex/util/lex_types.go:116 returns_error: нет description: —


### MarshalCBOR (lex/util/lex_types.go:116)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (lb *LexBytes) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `lex/util/lex_types.go:116`



---


[function] name: MarshalCBOR file: lex/util/lex_types.go:212 returns_error: нет description: —


### MarshalCBOR (lex/util/lex_types.go:212)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (b *LexBlob) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `lex/util/lex_types.go:212`



---


[function] name: MarshalJSON file: lex/util/lex_types.go:37 returns_error: да description: —


### MarshalJSON (lex/util/lex_types.go:37)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (ll LexLink) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/lex_types.go:37`



---


[function] name: MarshalJSON file: lex/util/lex_types.go:92 returns_error: да description: —


### MarshalJSON (lex/util/lex_types.go:92)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (lb LexBytes) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/lex_types.go:92`



---


[function] name: MarshalJSON file: lex/util/lex_types.go:159 returns_error: да description: —


### MarshalJSON (lex/util/lex_types.go:159)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (b LexBlob) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/lex_types.go:159`



---


[function] name: String file: lex/util/lex_types.go:28 returns_error: нет description: convenience helper


### String (lex/util/lex_types.go:28)


convenience helper


```go
func (ll LexLink) String(()) ()
```


📍 *Расположение:* `lex/util/lex_types.go:28`



---


[function] name: UnmarshalCBOR file: lex/util/lex_types.go:76 returns_error: нет description: —


### UnmarshalCBOR (lex/util/lex_types.go:76)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (ll *LexLink) UnmarshalCBOR((r io.Reader)) (r io.Reader)
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


📍 *Расположение:* `lex/util/lex_types.go:76`



---


[function] name: UnmarshalCBOR file: lex/util/lex_types.go:128 returns_error: нет description: —


### UnmarshalCBOR (lex/util/lex_types.go:128)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (lb *LexBytes) UnmarshalCBOR((r io.Reader)) (r io.Reader)
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


📍 *Расположение:* `lex/util/lex_types.go:128`



---


[function] name: UnmarshalCBOR file: lex/util/lex_types.go:234 returns_error: нет description: —


### UnmarshalCBOR (lex/util/lex_types.go:234)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (lb *LexBlob) UnmarshalCBOR((r io.Reader)) (r io.Reader)
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


📍 *Расположение:* `lex/util/lex_types.go:234`



---


[function] name: UnmarshalJSON file: lex/util/lex_types.go:47 returns_error: нет description: —


### UnmarshalJSON (lex/util/lex_types.go:47)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (raw []byte).


```go
func (ll *LexLink) UnmarshalJSON((raw []byte)) (raw []byte)
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


📍 *Расположение:* `lex/util/lex_types.go:47`



---


[function] name: UnmarshalJSON file: lex/util/lex_types.go:102 returns_error: нет description: —


### UnmarshalJSON (lex/util/lex_types.go:102)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (raw []byte).


```go
func (lb *LexBytes) UnmarshalJSON((raw []byte)) (raw []byte)
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


📍 *Расположение:* `lex/util/lex_types.go:102`



---


[function] name: UnmarshalJSON file: lex/util/lex_types.go:177 returns_error: нет description: —


### UnmarshalJSON (lex/util/lex_types.go:177)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (raw []byte).


```go
func (b *LexBlob) UnmarshalJSON((raw []byte)) (raw []byte)
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


📍 *Расположение:* `lex/util/lex_types.go:177`




## lex/util/util.go


📄 Исходный файл: `lex/util/util.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [CborTypeExtract](#cbortypeextract-lexutilutilgo27) `:27`

- 🔗 [CborTypeExtractReader](#cbortypeextractreader-lexutilutilgo37) `:37`

- 🔗 [TypeExtract](#typeextract-lexutilutilgo14) `:14`


</details>


[function] name: CborTypeExtract file: lex/util/util.go:27 returns_error: да description: —


### CborTypeExtract (lex/util/util.go:27)


CborTypeExtract is a function that performs operations based on the provided parameters and may return an error.


```go
func CborTypeExtract((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/util.go:27`



---


[function] name: CborTypeExtractReader file: lex/util/util.go:37 returns_error: да description: —


### CborTypeExtractReader (lex/util/util.go:37)


CborTypeExtractReader is a function that performs operations based on the provided parameters and may return an error.


```go
func CborTypeExtractReader((string, []byte, error)) (string, []byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/util.go:37`



---


[function] name: TypeExtract file: lex/util/util.go:14 returns_error: да description: —


### TypeExtract (lex/util/util.go:14)


TypeExtract is a function that performs operations based on the provided parameters and may return an error.


```go
func TypeExtract((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/util/util.go:14`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](lex_lexlint.md)

- [Следующая директория](models.md)


---

