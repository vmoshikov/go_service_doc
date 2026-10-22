---
title: "Функции: xrpc"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: xrpc
---


# Функции: xrpc


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_tracing.md)


---


## Меню по файлам


- 📄 [xrpc/xrpc.go](#xrpcxrpcgo)


---


## xrpc/xrpc.go


📄 Исходный файл: `xrpc/xrpc.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [Do](#do-xrpcxrpcgo135) `:135`

- 🔗 [Error](#error-xrpcxrpcgo55) `:55`

- 🔗 [Error](#error-xrpcxrpcgo65) `:65`

- 🔗 [IsThrottled](#isthrottled-xrpcxrpcgo84) `:84`

- 🔗 [LexDo](#lexdo-xrpcxrpcgo230) `:230`

- 🔗 [Unwrap](#unwrap-xrpcxrpcgo77) `:77`

- 🔗 [errorFromHTTPResponse](#errorfromhttpresponse-xrpcxrpcgo88) `:88`

- 🔗 [getClient](#getclient-xrpcxrpcgo31) `:31`

- 🔗 [makeParams](#makeparams-xrpcxrpcgo120) `:120`


</details>


[function] name: Do file: xrpc/xrpc.go:135 returns_error: нет description: —


### Do (xrpc/xrpc.go:135)


Do is a method that performs operations based on the provided parameters and returns (ctx context.Context, kind string, inpenc string, method string, params map[string]interface{}, bodyobj interface{}, out interface{}).


```go
func (c *Client) Do((ctx context.Context, kind string, inpenc string, method string, params map[string]interface{}, bodyobj interface{}, out interface{})) (ctx context.Context, kind string, inpenc string, method string, params map[string]interface{}, bodyobj interface{}, out interface{})
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "Ctx": {},
  "Err": {},
  "Logger": null,
  "engine": null,
  "effects": null
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** kind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** inpenc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** method


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bodyobj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** out


```json
{
  "Name": "string",
  "Type": null,
  "NeedsCbor": false,
  "NeedsType": false
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `xrpc/xrpc.go:135`



---


[function] name: Error file: xrpc/xrpc.go:55 returns_error: нет description: —


### Error (xrpc/xrpc.go:55)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (xe *XRPCError) Error(()) ()
```


📍 *Расположение:* `xrpc/xrpc.go:55`



---


[function] name: Error file: xrpc/xrpc.go:65 returns_error: нет description: —


### Error (xrpc/xrpc.go:65)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e *Error) Error(()) ()
```


📍 *Расположение:* `xrpc/xrpc.go:65`



---


[function] name: IsThrottled file: xrpc/xrpc.go:84 returns_error: нет description: —


### IsThrottled (xrpc/xrpc.go:84)


IsThrottled is a method that performs operations based on the provided parameters and returns ().


```go
func (e *Error) IsThrottled(()) ()
```


📍 *Расположение:* `xrpc/xrpc.go:84`



---


[function] name: LexDo file: xrpc/xrpc.go:230 returns_error: нет description: —


### LexDo (xrpc/xrpc.go:230)


LexDo is a method that performs operations based on the provided parameters and returns (ctx context.Context, method string, inputEncoding string, endpoint string, params map[string]any, bodyData any, out any).


```go
func (c *Client) LexDo((ctx context.Context, method string, inputEncoding string, endpoint string, params map[string]any, bodyData any, out any)) (ctx context.Context, method string, inputEncoding string, endpoint string, params map[string]any, bodyData any, out any)
```


**Тип ответа:** ctx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** context.Context


```json
{
  "Ctx": {},
  "Err": {},
  "Logger": null,
  "engine": null,
  "effects": null
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** method


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** inputEncoding


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bodyData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** out


```json
{
  "Name": "string",
  "Type": null,
  "NeedsCbor": false,
  "NeedsType": false
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `xrpc/xrpc.go:230`



---


[function] name: Unwrap file: xrpc/xrpc.go:77 returns_error: нет description: —


### Unwrap (xrpc/xrpc.go:77)


Unwrap is a method that performs operations based on the provided parameters and returns ().


```go
func (e *Error) Unwrap(()) ()
```


📍 *Расположение:* `xrpc/xrpc.go:77`



---


[function] name: errorFromHTTPResponse file: xrpc/xrpc.go:88 returns_error: да description: —


### errorFromHTTPResponse (xrpc/xrpc.go:88)


errorFromHTTPResponse is a function that performs operations based on the provided parameters and may return an error.


```go
func errorFromHTTPResponse((resp *http.Response, err error)) (resp *http.Response, err error)
```


**Тип запроса:** http.Response


```json
{
  "Collections": {},
  "Cursor": "string"
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** resp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.Response


```json
{
  "Collections": {},
  "Cursor": "string"
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


*Типы возврата:* `resp *http.Response`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `xrpc/xrpc.go:88`



---


[function] name: getClient file: xrpc/xrpc.go:31 returns_error: нет description: —


### getClient (xrpc/xrpc.go:31)


getClient is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Client) getClient(()) ()
```


📍 *Расположение:* `xrpc/xrpc.go:31`



---


[function] name: makeParams file: xrpc/xrpc.go:120 returns_error: нет description: makeParams converts a map of string keys and any values into a URL-encoded string.
If a value is a slice of strings, it 


### makeParams (xrpc/xrpc.go:120)


makeParams converts a map of string keys and any values into a URL-encoded string.
If a value is a slice of strings, it will be joined with commas.
Generally the values will be strings, numbers, booleans, or slices of strings


```go
func makeParams((p map[string]any)) (p map[string]any)
```


**Тип ответа:** p


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `xrpc/xrpc.go:120`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_tracing.md)


---

