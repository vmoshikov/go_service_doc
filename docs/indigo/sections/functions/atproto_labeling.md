---
title: "Функции: atproto/labeling"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/labeling
---


# Функции: atproto/labeling


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_identity.md)

- [Следующая директория](atproto_lexicon.md)


---


## Меню по файлам


- 📄 [atproto/labeling/cbor_gen.go](#atprotolabelingcbor_gengo)

- 📄 [atproto/labeling/label.go](#atprotolabelinglabelgo)


---


## atproto/labeling/cbor_gen.go


📄 Исходный файл: `atproto/labeling/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-atprotolabelingcbor_gengo21) `:21`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotolabelingcbor_gengo284) `:284`


</details>


[function] name: MarshalCBOR file: atproto/labeling/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (atproto/labeling/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *Label) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `atproto/labeling/cbor_gen.go:21`



---


[function] name: UnmarshalCBOR file: atproto/labeling/cbor_gen.go:284 returns_error: да description: —


### UnmarshalCBOR (atproto/labeling/cbor_gen.go:284)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *Label) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `atproto/labeling/cbor_gen.go:284`




## atproto/labeling/label.go


📄 Исходный файл: `atproto/labeling/label.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Data](#data-atprotolabelinglabelgo29) `:29`

- 🔗 [FromLexicon](#fromlexicon-atprotolabelinglabelgo152) `:152`

- 🔗 [Sign](#sign-atprotolabelinglabelgo113) `:113`

- 🔗 [ToLexicon](#tolexicon-atprotolabelinglabelgo138) `:138`

- 🔗 [UnsignedBytes](#unsignedbytes-atprotolabelinglabelgo88) `:88`

- 🔗 [VerifySignature](#verifysignature-atprotolabelinglabelgo127) `:127`

- 🔗 [VerifySyntax](#verifysyntax-atprotolabelinglabelgo54) `:54`


</details>


[function] name: Data file: atproto/labeling/label.go:29 returns_error: нет description: converts to map[string]any for printing as JSON


### Data (atproto/labeling/label.go:29)


converts to map[string]any for printing as JSON


```go
func (l *Label) Data(()) ()
```


📍 *Расположение:* `atproto/labeling/label.go:29`



---


[function] name: FromLexicon file: atproto/labeling/label.go:152 returns_error: нет description: —


### FromLexicon (atproto/labeling/label.go:152)


FromLexicon is a function that performs operations based on the provided parameters and returns (l *comatproto.LabelDefs_Label).


```go
func FromLexicon((l *comatproto.LabelDefs_Label)) (l *comatproto.LabelDefs_Label)
```


**Тип запроса:** comatproto.LabelDefs_Label


```json
{
  "cid": "string",
  "cts": "string",
  "exp": "string",
  "neg": false,
  "sig": {},
  "src": "string",
  "uri": "string",
  "val": "string",
  "ver": 0
}
```


*Определено в:* `api/atproto/labeldefs.go`


**Тип ответа:** l


```json
{
  "Inner": {},
  "ErrTTL": {},
  "HitTTL": {},
  "InvalidHandleTTL": {},
  "Logger": null,
  "handleCache": null,
  "didCache": null,
  "didResolveChans": {},
  "handleResolveChans": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** comatproto.LabelDefs_Label


```json
{
  "cid": "string",
  "cts": "string",
  "exp": "string",
  "neg": false,
  "sig": {},
  "src": "string",
  "uri": "string",
  "val": "string",
  "ver": 0
}
```


*Определено в:* `api/atproto/labeldefs.go`


📍 *Расположение:* `atproto/labeling/label.go:152`



---


[function] name: Sign file: atproto/labeling/label.go:113 returns_error: нет description: Signs the commit, storing the signature in the `Sig` field


### Sign (atproto/labeling/label.go:113)


Signs the commit, storing the signature in the `Sig` field


```go
func (l *Label) Sign((privkey atcrypto.PrivateKey)) (privkey atcrypto.PrivateKey)
```


**Тип ответа:** privkey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atcrypto.PrivateKey


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


📍 *Расположение:* `atproto/labeling/label.go:113`



---


[function] name: ToLexicon file: atproto/labeling/label.go:138 returns_error: нет description: —


### ToLexicon (atproto/labeling/label.go:138)


ToLexicon is a method that performs operations based on the provided parameters and returns ().


```go
func (l *Label) ToLexicon(()) ()
```


📍 *Расположение:* `atproto/labeling/label.go:138`



---


[function] name: UnsignedBytes file: atproto/labeling/label.go:88 returns_error: да description: —


### UnsignedBytes (atproto/labeling/label.go:88)


UnsignedBytes is a method that performs operations based on the provided parameters and may return an error.


```go
func (l *Label) UnsignedBytes(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/labeling/label.go:88`



---


[function] name: VerifySignature file: atproto/labeling/label.go:127 returns_error: нет description: Verifies `Sig` field using the provided key. Returns `nil` if signature is valid.


### VerifySignature (atproto/labeling/label.go:127)


Verifies `Sig` field using the provided key. Returns `nil` if signature is valid.


```go
func (l *Label) VerifySignature((pubkey atcrypto.PublicKey)) (pubkey atcrypto.PublicKey)
```


**Тип ответа:** pubkey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atcrypto.PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


📍 *Расположение:* `atproto/labeling/label.go:127`



---


[function] name: VerifySyntax file: atproto/labeling/label.go:54 returns_error: нет description: does basic checks on syntax and structure


### VerifySyntax (atproto/labeling/label.go:54)


does basic checks on syntax and structure


```go
func (l *Label) VerifySyntax(()) ()
```


📍 *Расположение:* `atproto/labeling/label.go:54`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_identity.md)

- [Следующая директория](atproto_lexicon.md)


---

