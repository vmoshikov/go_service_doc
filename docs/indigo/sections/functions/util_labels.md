---
title: "Функции: util/labels"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: util/labels
---


# Функции: util/labels


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_cliutil.md)

- [Следующая директория](util_ssrf.md)


---


## Меню по файлам


- 📄 [util/labels/cbor_gen.go](#utillabelscbor_gengo)

- 📄 [util/labels/labels.go](#utillabelslabelsgo)


---


## util/labels/cbor_gen.go


📄 Исходный файл: `util/labels/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-utillabelscbor_gengo21) `:21`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-utillabelscbor_gengo265) `:265`


</details>


[function] name: MarshalCBOR file: util/labels/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (util/labels/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *UnsignedLabel) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `util/labels/cbor_gen.go:21`



---


[function] name: UnmarshalCBOR file: util/labels/cbor_gen.go:265 returns_error: да description: —


### UnmarshalCBOR (util/labels/cbor_gen.go:265)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *UnsignedLabel) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `util/labels/cbor_gen.go:265`




## util/labels/labels.go


📄 Исходный файл: `util/labels/labels.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [BytesForSigning](#bytesforsigning-utillabelslabelsgo33) `:33`


</details>


[function] name: BytesForSigning file: util/labels/labels.go:33 returns_error: да description: BytesForSigning returns bytes of the DAG-CBOR representation of object


### BytesForSigning (util/labels/labels.go:33)


BytesForSigning returns bytes of the DAG-CBOR representation of object


```go
func (ul *UnsignedLabel) BytesForSigning(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `util/labels/labels.go:33`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_cliutil.md)

- [Следующая директория](util_ssrf.md)


---

