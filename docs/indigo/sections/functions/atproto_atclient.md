---
title: "Функции: atproto/atclient"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/atclient
---


# Функции: atproto/atclient


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_ozone.md)

- [Следующая директория](atproto_atcrypto.md)


---


## Меню по файлам


- 📄 [atproto/atclient/admin_auth.go](#atprotoatclientadmin_authgo)

- 📄 [atproto/atclient/apiclient.go](#atprotoatclientapiclientgo)

- 📄 [atproto/atclient/apierror.go](#atprotoatclientapierrorgo)

- 📄 [atproto/atclient/apirequest.go](#atprotoatclientapirequestgo)

- 📄 [atproto/atclient/cmd/atp-client-demo/main.go](#atprotoatclientcmdatp-client-demomaingo)

- 📄 [atproto/atclient/lexclient.go](#atprotoatclientlexclientgo)

- 📄 [atproto/atclient/params.go](#atprotoatclientparamsgo)

- 📄 [atproto/atclient/password_auth.go](#atprotoatclientpassword_authgo)


---


## atproto/atclient/admin_auth.go


📄 Исходный файл: `atproto/atclient/admin_auth.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [DoWithAuth](#dowithauth-atprotoatclientadmin_authgo14) `:14`

- 🔗 [NewAdminClient](#newadminclient-atprotoatclientadmin_authgo19) `:19`


</details>


[function] name: DoWithAuth file: atproto/atclient/admin_auth.go:14 returns_error: да description: —


### DoWithAuth (atproto/atclient/admin_auth.go:14)


DoWithAuth is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *AdminAuth) DoWithAuth((*http.Response, error)) (*http.Response, error)
```


**Тип запроса:** http.Response


```json
{
  "Collections": {},
  "Cursor": "string"
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** http.Response


```json
{
  "Collections": {},
  "Cursor": "string"
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Response`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atclient/admin_auth.go:14`



---


[function] name: NewAdminClient file: atproto/atclient/admin_auth.go:19 returns_error: нет description: —


### NewAdminClient (atproto/atclient/admin_auth.go:19)


NewAdminClient is a function that performs operations based on the provided parameters and returns (host, password string).


```go
func NewAdminClient((host, password string)) (host, password string)
```


**Тип ответа:** host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Host": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HasActiveConnection": false,
  "EventsSeenSinceStartup": 0,
  "PerSecondEventRate": {},
  "PerHourEventRate": {},
  "PerDayEventRate": {},
  "UserCount": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


**Тип ответа:** password


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/admin_auth.go:19`




## atproto/atclient/apiclient.go


📄 Исходный файл: `atproto/atclient/apiclient.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Do](#do-atprotoatclientapiclientgo139) `:139`

- 🔗 [Get](#get-atprotoatclientapiclientgo56) `:56`

- 🔗 [NewAPIClient](#newapiclient-atprotoatclientapiclientgo41) `:41`

- 🔗 [Post](#post-atprotoatclientapiclientgo100) `:100`

- 🔗 [SetLabelers](#setlabelers-atprotoatclientapiclientgo181) `:181`

- 🔗 [WithService](#withservice-atprotoatclientapiclientgo165) `:165`

- 🔗 [encodeLabelerHeader](#encodelabelerheader-atprotoatclientapiclientgo185) `:185`


</details>


[function] name: Do file: atproto/atclient/apiclient.go:139 returns_error: да description: Full-featured method for atproto API requests.

TODO: this does not currently parse API error response JSON body to [API


### Do (atproto/atclient/apiclient.go:139)


Full-featured method for atproto API requests.

TODO: this does not currently parse API error response JSON body to [APIError], thought it might in the future.


```go
func (c *APIClient) Do((*http.Response, error)) (*http.Response, error)
```


**Тип запроса:** http.Response


```json
{
  "Collections": {},
  "Cursor": "string"
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** http.Response


```json
{
  "Collections": {},
  "Cursor": "string"
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Response`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atclient/apiclient.go:139`



---


[function] name: Get file: atproto/atclient/apiclient.go:56 returns_error: нет description: High-level helper for simple JSON "Query" API calls.

This method automatically parses non-successful responses to [APIE


### Get (atproto/atclient/apiclient.go:56)


High-level helper for simple JSON "Query" API calls.

This method automatically parses non-successful responses to [APIError].

For Query endpoints which return non-JSON data, or other situations needing complete configuration of the request and response, use the [APIClient.Do] method.


```go
func (c *APIClient) Get((ctx context.Context, endpoint syntax.NSID, params map[string]any, out any)) (ctx context.Context, endpoint syntax.NSID, params map[string]any, out any)
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


**Тип ответа:** endpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


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


📍 *Расположение:* `atproto/atclient/apiclient.go:56`



---


[function] name: NewAPIClient file: atproto/atclient/apiclient.go:41 returns_error: нет description: Creates a simple APIClient for the provided host. This is appropriate for use with unauthenticated ("public") atproto AP


### NewAPIClient (atproto/atclient/apiclient.go:41)


Creates a simple APIClient for the provided host. This is appropriate for use with unauthenticated ("public") atproto API endpoints, or to use as a base client to add authentication.

Uses [http.DefaultClient], and sets a default User-Agent.


```go
func NewAPIClient((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Host": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HasActiveConnection": false,
  "EventsSeenSinceStartup": 0,
  "PerSecondEventRate": {},
  "PerHourEventRate": {},
  "PerDayEventRate": {},
  "UserCount": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


📍 *Расположение:* `atproto/atclient/apiclient.go:41`



---


[function] name: Post file: atproto/atclient/apiclient.go:100 returns_error: нет description: High-level helper for simple JSON-to-JSON "Procedure" API calls, with no query params.

This method automatically parses


### Post (atproto/atclient/apiclient.go:100)


High-level helper for simple JSON-to-JSON "Procedure" API calls, with no query params.

This method automatically parses non-successful responses to [APIError].

For Query endpoints which expect non-JSON request bodies; return non-JSON responses; direct use of [io.Reader] for the request body; or other situations needing complete configuration of the request and response, use the [APIClient.Do] method.


```go
func (c *APIClient) Post((ctx context.Context, endpoint syntax.NSID, body any, out any)) (ctx context.Context, endpoint syntax.NSID, body any, out any)
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


**Тип ответа:** endpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** body


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


📍 *Расположение:* `atproto/atclient/apiclient.go:100`



---


[function] name: SetLabelers file: atproto/atclient/apiclient.go:181 returns_error: нет description: Configures labeler header ('Atproto-Accept-Labelers') with the indicated "redact" level labelers, and regular labelers.



### SetLabelers (atproto/atclient/apiclient.go:181)


Configures labeler header ('Atproto-Accept-Labelers') with the indicated "redact" level labelers, and regular labelers.

Overwrites any existing client-level header value.


```go
func (c *APIClient) SetLabelers((redact, other []syntax.DID)) (redact, other []syntax.DID)
```


**Тип ответа:** redact


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** other


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


📍 *Расположение:* `atproto/atclient/apiclient.go:181`



---


[function] name: WithService file: atproto/atclient/apiclient.go:165 returns_error: нет description: Returns a shallow copy of the APIClient with the provided service ref configured as a proxy header.

To configure servic


### WithService (atproto/atclient/apiclient.go:165)


Returns a shallow copy of the APIClient with the provided service ref configured as a proxy header.

To configure service proxying without creating a copy, simply set the 'Atproto-Proxy' header.


```go
func (c *APIClient) WithService((ref string)) (ref string)
```


**Тип ответа:** ref


```json
{
  "accessJwt": "string",
  "active": false,
  "did": "string",
  "refreshJwt": "string",
  "status": "string"
}
```


*Определено в:* `atproto/atclient/password_auth.go`


📍 *Расположение:* `atproto/atclient/apiclient.go:165`



---


[function] name: encodeLabelerHeader file: atproto/atclient/apiclient.go:185 returns_error: нет description: —


### encodeLabelerHeader (atproto/atclient/apiclient.go:185)


encodeLabelerHeader is a function that performs operations based on the provided parameters and returns (redact, other []syntax.DID).


```go
func encodeLabelerHeader((redact, other []syntax.DID)) (redact, other []syntax.DID)
```


**Тип ответа:** redact


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** other


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


📍 *Расположение:* `atproto/atclient/apiclient.go:185`




## atproto/atclient/apierror.go


📄 Исходный файл: `atproto/atclient/apierror.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [APIError](#apierror-atprotoatclientapierrorgo30) `:30`

- 🔗 [Error](#error-atprotoatclientapierrorgo13) `:13`


</details>


[function] name: APIError file: atproto/atclient/apierror.go:30 returns_error: нет description: —


### APIError (atproto/atclient/apierror.go:30)


APIError is a method that performs operations based on the provided parameters and returns (statusCode int).


```go
func (eb *ErrorBody) APIError((statusCode int)) (statusCode int)
```


**Тип ответа:** statusCode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/apierror.go:30`



---


[function] name: Error file: atproto/atclient/apierror.go:13 returns_error: нет description: —


### Error (atproto/atclient/apierror.go:13)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (ae *APIError) Error(()) ()
```


📍 *Расположение:* `atproto/atclient/apierror.go:13`




## atproto/atclient/apirequest.go


📄 Исходный файл: `atproto/atclient/apirequest.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [HTTPRequest](#httprequest-atprotoatclientapirequestgo74) `:74`

- 🔗 [NewAPIRequest](#newapirequest-atprotoatclientapirequestgo44) `:44`


</details>


[function] name: HTTPRequest file: atproto/atclient/apirequest.go:74 returns_error: да description: Creates an [http.Request] for this API request.

`host` parameter should be a URL prefix: schema, hostname, port (requir


### HTTPRequest (atproto/atclient/apirequest.go:74)


Creates an [http.Request] for this API request.

`host` parameter should be a URL prefix: schema, hostname, port (required)

`clientHeaders`, if provided, is treated as client-level defaults. Only a single value is allowed per key ("Set" behavior), and will be clobbered by any request-level header values. (optional; may be nil)


```go
func (r *APIRequest) HTTPRequest((*http.Request, error)) (*http.Request, error)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Request`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atclient/apirequest.go:74`



---


[function] name: NewAPIRequest file: atproto/atclient/apirequest.go:44 returns_error: нет description: Initializes a new request struct. Initializes Headers and QueryParams so they can be manipulated immediately.

If body i


### NewAPIRequest (atproto/atclient/apirequest.go:44)


Initializes a new request struct. Initializes Headers and QueryParams so they can be manipulated immediately.

If body is provided (it can be nil), will try to turn it in to the most retry-able form (and wrap as [io.ReadCloser]).


```go
func NewAPIRequest((method string, endpoint syntax.NSID, body io.Reader)) (method string, endpoint syntax.NSID, body io.Reader)
```


**Тип ответа:** method


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** body


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `atproto/atclient/apirequest.go:44`




## atproto/atclient/cmd/atp-client-demo/main.go


📄 Исходный файл: `atproto/atclient/cmd/atp-client-demo/main.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [getFeed](#getfeed-atprotoatclientcmdatp-client-demomaingo126) `:126`

- 🔗 [listRecords](#listrecords-atprotoatclientcmdatp-client-demomaingo147) `:147`

- 🔗 [main](#main-atprotoatclientcmdatp-client-demomaingo18) `:18`

- 🔗 [runGetFeedAuth](#rungetfeedauth-atprotoatclientcmdatp-client-demomaingo208) `:208`

- 🔗 [runGetFeedPublic](#rungetfeedpublic-atprotoatclientcmdatp-client-demomaingo162) `:162`

- 🔗 [runListRecordsPublic](#runlistrecordspublic-atprotoatclientcmdatp-client-demomaingo171) `:171`

- 🔗 [runLoginAuth](#runloginauth-atprotoatclientcmdatp-client-demomaingo180) `:180`

- 🔗 [runLookupAdmin](#runlookupadmin-atprotoatclientcmdatp-client-demomaingo226) `:226`


</details>


[function] name: getFeed file: atproto/atclient/cmd/atp-client-demo/main.go:126 returns_error: нет description: —


### getFeed (atproto/atclient/cmd/atp-client-demo/main.go:126)


getFeed is a function that performs operations based on the provided parameters and returns (ctx context.Context, c *atclient.APIClient).


```go
func getFeed((ctx context.Context, c *atclient.APIClient)) (ctx context.Context, c *atclient.APIClient)
```


**Тип запроса:** atclient.APIClient


```json
{
  "Client": null,
  "Host": "string",
  "Auth": {},
  "Headers": {},
  "AccountDID": null
}
```


*Определено в:* `atproto/atclient/apiclient.go`


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


**Тип ответа:** c


```json
{
  "EnqueuedRepos": {},
  "FinishedRepos": {},
  "StatePath": "string",
  "CheckoutPath": "string",
  "outDir": "string",
  "magicHeaderKey": "string",
  "magicHeaderVal": "string",
  "logger": null,
  "lk": {},
  "wg": {},
  "exit": {},
  "limiter": null,
  "workerCount": 0,
  "client": null
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** atclient.APIClient


```json
{
  "Client": null,
  "Host": "string",
  "Auth": {},
  "Headers": {},
  "AccountDID": null
}
```


*Определено в:* `atproto/atclient/apiclient.go`


📍 *Расположение:* `atproto/atclient/cmd/atp-client-demo/main.go:126`



---


[function] name: listRecords file: atproto/atclient/cmd/atp-client-demo/main.go:147 returns_error: нет description: —


### listRecords (atproto/atclient/cmd/atp-client-demo/main.go:147)


listRecords is a function that performs operations based on the provided parameters and returns (ctx context.Context, c *atclient.APIClient).


```go
func listRecords((ctx context.Context, c *atclient.APIClient)) (ctx context.Context, c *atclient.APIClient)
```


**Тип запроса:** atclient.APIClient


```json
{
  "Client": null,
  "Host": "string",
  "Auth": {},
  "Headers": {},
  "AccountDID": null
}
```


*Определено в:* `atproto/atclient/apiclient.go`


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


**Тип ответа:** c


```json
{
  "EnqueuedRepos": {},
  "FinishedRepos": {},
  "StatePath": "string",
  "CheckoutPath": "string",
  "outDir": "string",
  "magicHeaderKey": "string",
  "magicHeaderVal": "string",
  "logger": null,
  "lk": {},
  "wg": {},
  "exit": {},
  "limiter": null,
  "workerCount": 0,
  "client": null
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** atclient.APIClient


```json
{
  "Client": null,
  "Host": "string",
  "Auth": {},
  "Headers": {},
  "AccountDID": null
}
```


*Определено в:* `atproto/atclient/apiclient.go`


📍 *Расположение:* `atproto/atclient/cmd/atp-client-demo/main.go:147`



---


[function] name: main file: atproto/atclient/cmd/atp-client-demo/main.go:18 returns_error: нет description: —


### main (atproto/atclient/cmd/atp-client-demo/main.go:18)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `atproto/atclient/cmd/atp-client-demo/main.go:18`



---


[function] name: runGetFeedAuth file: atproto/atclient/cmd/atp-client-demo/main.go:208 returns_error: нет description: —


### runGetFeedAuth (atproto/atclient/cmd/atp-client-demo/main.go:208)


runGetFeedAuth is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runGetFeedAuth((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/cmd/atp-client-demo/main.go:208`



---


[function] name: runGetFeedPublic file: atproto/atclient/cmd/atp-client-demo/main.go:162 returns_error: нет description: —


### runGetFeedPublic (atproto/atclient/cmd/atp-client-demo/main.go:162)


runGetFeedPublic is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runGetFeedPublic((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/cmd/atp-client-demo/main.go:162`



---


[function] name: runListRecordsPublic file: atproto/atclient/cmd/atp-client-demo/main.go:171 returns_error: нет description: —


### runListRecordsPublic (atproto/atclient/cmd/atp-client-demo/main.go:171)


runListRecordsPublic is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runListRecordsPublic((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/cmd/atp-client-demo/main.go:171`



---


[function] name: runLoginAuth file: atproto/atclient/cmd/atp-client-demo/main.go:180 returns_error: нет description: —


### runLoginAuth (atproto/atclient/cmd/atp-client-demo/main.go:180)


runLoginAuth is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runLoginAuth((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/cmd/atp-client-demo/main.go:180`



---


[function] name: runLookupAdmin file: atproto/atclient/cmd/atp-client-demo/main.go:226 returns_error: нет description: —


### runLookupAdmin (atproto/atclient/cmd/atp-client-demo/main.go:226)


runLookupAdmin is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runLookupAdmin((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/cmd/atp-client-demo/main.go:226`




## atproto/atclient/lexclient.go


📄 Исходный файл: `atproto/atclient/lexclient.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [LexDo](#lexdo-atprotoatclientlexclientgo14) `:14`


</details>


[function] name: LexDo file: atproto/atclient/lexclient.go:14 returns_error: нет description: Implements the [github.com/bluesky-social/indigo/lex/util.LexClient] interface, for use with code-generated API helpers.


### LexDo (atproto/atclient/lexclient.go:14)


Implements the [github.com/bluesky-social/indigo/lex/util.LexClient] interface, for use with code-generated API helpers.


```go
func (c *APIClient) LexDo((ctx context.Context, method string, inputEncoding string, endpoint string, params map[string]any, bodyData any, out any)) (ctx context.Context, method string, inputEncoding string, endpoint string, params map[string]any, bodyData any, out any)
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


📍 *Расположение:* `atproto/atclient/lexclient.go:14`




## atproto/atclient/params.go


📄 Исходный файл: `atproto/atclient/params.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ParseParams](#parseparams-atprotoatclientparamsgo11) `:11`


</details>


[function] name: ParseParams file: atproto/atclient/params.go:11 returns_error: да description: Flexibly parses an input map to URL query params (strings)


### ParseParams (atproto/atclient/params.go:11)


Flexibly parses an input map to URL query params (strings)


```go
func ParseParams((url.Values, error)) (url.Values, error)
```


**Тип ответа:** url.Values


```json
{
  "cursor": "string",
  "set": null,
  "values": []
}
```


*Определено в:* `api/ozone/setgetValues.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `url.Values`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atclient/params.go:11`




## atproto/atclient/password_auth.go


📄 Исходный файл: `atproto/atclient/password_auth.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [Clone](#clone-atprotoatclientpassword_authgo42) `:42`

- 🔗 [DoWithAuth](#dowithauth-atprotoatclientpassword_authgo80) `:80`

- 🔗 [GetTokens](#gettokens-atprotoatclientpassword_authgo128) `:128`

- 🔗 [LoginWithPassword](#loginwithpassword-atprotoatclientpassword_authgo224) `:224`

- 🔗 [LoginWithPasswordHost](#loginwithpasswordhost-atprotoatclientpassword_authgo253) `:253`

- 🔗 [Logout](#logout-atprotoatclientpassword_authgo189) `:189`

- 🔗 [Refresh](#refresh-atprotoatclientpassword_authgo137) `:137`

- 🔗 [ResumePasswordSession](#resumepasswordsession-atprotoatclientpassword_authgo295) `:295`


</details>


[function] name: Clone file: atproto/atclient/password_auth.go:42 returns_error: нет description: Creates a deep copy of the session data.


### Clone (atproto/atclient/password_auth.go:42)


Creates a deep copy of the session data.


```go
func (sd *PasswordSessionData) Clone(()) ()
```


📍 *Расположение:* `atproto/atclient/password_auth.go:42`



---


[function] name: DoWithAuth file: atproto/atclient/password_auth.go:80 returns_error: да description: —


### DoWithAuth (atproto/atclient/password_auth.go:80)


DoWithAuth is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *PasswordAuth) DoWithAuth((*http.Response, error)) (*http.Response, error)
```


**Тип запроса:** http.Response


```json
{
  "Collections": {},
  "Cursor": "string"
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** http.Response


```json
{
  "Collections": {},
  "Cursor": "string"
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Response`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atclient/password_auth.go:80`



---


[function] name: GetTokens file: atproto/atclient/password_auth.go:128 returns_error: нет description: Returns current access and refresh tokens (take a read-lock on session data)


### GetTokens (atproto/atclient/password_auth.go:128)


Returns current access and refresh tokens (take a read-lock on session data)


```go
func (a *PasswordAuth) GetTokens((string, string)) (string, string)
```


📍 *Расположение:* `atproto/atclient/password_auth.go:128`



---


[function] name: LoginWithPassword file: atproto/atclient/password_auth.go:224 returns_error: да description: Creates a new [APIClient] with [PasswordAuth] for the provided user. The provided identity directory is used to resolve 


### LoginWithPassword (atproto/atclient/password_auth.go:224)


Creates a new [APIClient] with [PasswordAuth] for the provided user. The provided identity directory is used to resolve the PDS host for the account.

`authToken` is optional; is used when multi-factor authentication is enabled for the account.

`cb` is an optional callback which will be called with updated session data after any token refresh.


```go
func LoginWithPassword((*APIClient, error)) (*APIClient, error)
```


**Тип запроса:** APIClient


```json
{
  "Client": null,
  "Host": "string",
  "Auth": {},
  "Headers": {},
  "AccountDID": null
}
```


*Определено в:* `atproto/atclient/apiclient.go`


**Тип ответа:** APIClient


```json
{
  "Client": null,
  "Host": "string",
  "Auth": {},
  "Headers": {},
  "AccountDID": null
}
```


*Определено в:* `atproto/atclient/apiclient.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*APIClient`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atclient/password_auth.go:224`



---


[function] name: LoginWithPasswordHost file: atproto/atclient/password_auth.go:253 returns_error: да description: Creates a new [APIClient] with [PasswordAuth], based on a login to the provided host. Note that with some PDS implementa


### LoginWithPasswordHost (atproto/atclient/password_auth.go:253)


Creates a new [APIClient] with [PasswordAuth], based on a login to the provided host. Note that with some PDS implementations, 'username' could be an email address. This login method also works in situations where an account's network identity does not resolve to this specific host.

`authToken` is optional; is used when multi-factor authentication is enabled for the account.

`cb` is an optional callback which will be called with updated session data after any token refresh.


```go
func LoginWithPasswordHost((*APIClient, error)) (*APIClient, error)
```


**Тип запроса:** APIClient


```json
{
  "Client": null,
  "Host": "string",
  "Auth": {},
  "Headers": {},
  "AccountDID": null
}
```


*Определено в:* `atproto/atclient/apiclient.go`


**Тип ответа:** APIClient


```json
{
  "Client": null,
  "Host": "string",
  "Auth": {},
  "Headers": {},
  "AccountDID": null
}
```


*Определено в:* `atproto/atclient/apiclient.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*APIClient`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atclient/password_auth.go:253`



---


[function] name: Logout file: atproto/atclient/password_auth.go:189 returns_error: нет description: —


### Logout (atproto/atclient/password_auth.go:189)


Logout is a method that performs operations based on the provided parameters and returns (ctx context.Context, c *http.Client).


```go
func (a *PasswordAuth) Logout((ctx context.Context, c *http.Client)) (ctx context.Context, c *http.Client)
```


**Тип запроса:** http.Client


```json
{
  "Client": null,
  "Auth": null,
  "AdminToken": "string",
  "Host": "string",
  "UserAgent": "string",
  "Headers": {}
}
```


*Определено в:* `xrpc/xrpc.go`


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


**Тип ответа:** c


```json
{
  "EnqueuedRepos": {},
  "FinishedRepos": {},
  "StatePath": "string",
  "CheckoutPath": "string",
  "outDir": "string",
  "magicHeaderKey": "string",
  "magicHeaderVal": "string",
  "logger": null,
  "lk": {},
  "wg": {},
  "exit": {},
  "limiter": null,
  "workerCount": 0,
  "client": null
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** http.Client


```json
{
  "Client": null,
  "Auth": null,
  "AdminToken": "string",
  "Host": "string",
  "UserAgent": "string",
  "Headers": {}
}
```


*Определено в:* `xrpc/xrpc.go`


📍 *Расположение:* `atproto/atclient/password_auth.go:189`



---


[function] name: Refresh file: atproto/atclient/password_auth.go:137 returns_error: нет description: Refreshes auth tokens (takes a write-lock on session data).

`priorRefreshToken` argument is used to check if a concurre


### Refresh (atproto/atclient/password_auth.go:137)


Refreshes auth tokens (takes a write-lock on session data).

`priorRefreshToken` argument is used to check if a concurrent refresh already took place.


```go
func (a *PasswordAuth) Refresh((ctx context.Context, c *http.Client, priorRefreshToken string)) (ctx context.Context, c *http.Client, priorRefreshToken string)
```


**Тип запроса:** http.Client


```json
{
  "Client": null,
  "Auth": null,
  "AdminToken": "string",
  "Host": "string",
  "UserAgent": "string",
  "Headers": {}
}
```


*Определено в:* `xrpc/xrpc.go`


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


**Тип ответа:** c


```json
{
  "EnqueuedRepos": {},
  "FinishedRepos": {},
  "StatePath": "string",
  "CheckoutPath": "string",
  "outDir": "string",
  "magicHeaderKey": "string",
  "magicHeaderVal": "string",
  "logger": null,
  "lk": {},
  "wg": {},
  "exit": {},
  "limiter": null,
  "workerCount": 0,
  "client": null
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** http.Client


```json
{
  "Client": null,
  "Auth": null,
  "AdminToken": "string",
  "Host": "string",
  "UserAgent": "string",
  "Headers": {}
}
```


*Определено в:* `xrpc/xrpc.go`


**Тип ответа:** priorRefreshToken


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/password_auth.go:137`



---


[function] name: ResumePasswordSession file: atproto/atclient/password_auth.go:295 returns_error: нет description: Creates an [APIClient] using [PasswordAuth], based on existing session data.

`cb` is an optional callback which will be


### ResumePasswordSession (atproto/atclient/password_auth.go:295)


Creates an [APIClient] using [PasswordAuth], based on existing session data.

`cb` is an optional callback which will be called with updated session data after any token refresh.


```go
func ResumePasswordSession((data PasswordSessionData, cb RefreshCallback)) (data PasswordSessionData, cb RefreshCallback)
```


**Тип ответа:** data


```json
{
  "AuthorizationServers": []
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Тип ответа:** PasswordSessionData


```json
{
  "AccessToken": "string",
  "RefreshToken": "string",
  "AccountDID": {},
  "Host": "string"
}
```


*Определено в:* `atproto/atclient/password_auth.go`


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RefreshCallback


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/atclient/password_auth.go:295`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_ozone.md)

- [Следующая директория](atproto_atcrypto.md)


---

