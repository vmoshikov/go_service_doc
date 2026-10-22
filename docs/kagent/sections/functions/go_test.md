---
title: "Функции: go/test"
type: functions
repo: kagent
language: ru
chunk_boundary: h3
group: go/test
---


# Функции: go/test


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](go_pkg.md)


---


## Меню по файлам


- 📄 [go/test/e2e/mocks/mock_sts_server.go](#goteste2emocksmock_sts_servergo)


---


## go/test/e2e/mocks/mock_sts_server.go


📄 Исходный файл: `go/test/e2e/mocks/mock_sts_server.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [ClearRequests](#clearrequests-goteste2emocksmock_sts_servergo90) `:90`

- 🔗 [Close](#close-goteste2emocksmock_sts_servergo80) `:80`

- 🔗 [GetRequests](#getrequests-goteste2emocksmock_sts_servergo85) `:85`

- 🔗 [NewMockSTSServer](#newmockstsserver-goteste2emocksmock_sts_servergo46) `:46`

- 🔗 [SetK8sURL](#setk8surl-goteste2emocksmock_sts_servergo65) `:65`

- 🔗 [URL](#url-goteste2emocksmock_sts_servergo70) `:70`

- 🔗 [WellKnownURL](#wellknownurl-goteste2emocksmock_sts_servergo75) `:75`

- 🔗 [extractClaimFromJWT](#extractclaimfromjwt-goteste2emocksmock_sts_servergo250) `:250`

- 🔗 [extractMayActFromJWT](#extractmayactfromjwt-goteste2emocksmock_sts_servergo242) `:242`

- 🔗 [extractSubjectFromJWT](#extractsubjectfromjwt-goteste2emocksmock_sts_servergo234) `:234`

- 🔗 [generateMockAccessToken](#generatemockaccesstoken-goteste2emocksmock_sts_servergo203) `:203`

- 🔗 [handleRequest](#handlerequest-goteste2emocksmock_sts_servergo94) `:94`

- 🔗 [handleTokenExchange](#handletokenexchange-goteste2emocksmock_sts_servergo124) `:124`

- 🔗 [handleWellKnown](#handlewellknown-goteste2emocksmock_sts_servergo105) `:105`


</details>


[function] name: ClearRequests file: go/test/e2e/mocks/mock_sts_server.go:90 returns_error: нет description: ClearRequests clears the request history


### ClearRequests (go/test/e2e/mocks/mock_sts_server.go:90)


ClearRequests clears the request history


```go
func (m *MockSTSServer) ClearRequests(()) ()
```


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:90`



---


[function] name: Close file: go/test/e2e/mocks/mock_sts_server.go:80 returns_error: нет description: Close stops the mock server


### Close (go/test/e2e/mocks/mock_sts_server.go:80)


Close stops the mock server


```go
func (m *MockSTSServer) Close(()) ()
```


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:80`



---


[function] name: GetRequests file: go/test/e2e/mocks/mock_sts_server.go:85 returns_error: нет description: GetRequests returns all token exchange requests received


### GetRequests (go/test/e2e/mocks/mock_sts_server.go:85)


GetRequests returns all token exchange requests received


```go
func (m *MockSTSServer) GetRequests(()) ()
```


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:85`



---


[function] name: NewMockSTSServer file: go/test/e2e/mocks/mock_sts_server.go:46 returns_error: нет description: NewMockSTSServer creates a new mock STS server


### NewMockSTSServer (go/test/e2e/mocks/mock_sts_server.go:46)


NewMockSTSServer creates a new mock STS server


```go
func NewMockSTSServer((agentServiceAccount string, port uint16)) (agentServiceAccount string, port uint16)
```


**Тип ответа:** agentServiceAccount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** port


```json
{
  "base": {},
  "headers": {}
}
```


*Определено в:* `contrib/go-adk/pkg/models/openai.go`


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:46`



---


[function] name: SetK8sURL file: go/test/e2e/mocks/mock_sts_server.go:65 returns_error: нет description: SetK8sURL sets the Kubernetes-accessible URL for the server


### SetK8sURL (go/test/e2e/mocks/mock_sts_server.go:65)


SetK8sURL sets the Kubernetes-accessible URL for the server


```go
func (m *MockSTSServer) SetK8sURL((k8sURL string)) (k8sURL string)
```


**Тип ответа:** k8sURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:65`



---


[function] name: URL file: go/test/e2e/mocks/mock_sts_server.go:70 returns_error: нет description: URL returns the base URL of the mock server


### URL (go/test/e2e/mocks/mock_sts_server.go:70)


URL returns the base URL of the mock server


```go
func (m *MockSTSServer) URL(()) ()
```


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:70`



---


[function] name: WellKnownURL file: go/test/e2e/mocks/mock_sts_server.go:75 returns_error: нет description: WellKnownURL returns the well-known configuration URL


### WellKnownURL (go/test/e2e/mocks/mock_sts_server.go:75)


WellKnownURL returns the well-known configuration URL


```go
func (m *MockSTSServer) WellKnownURL(()) ()
```


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:75`



---


[function] name: extractClaimFromJWT file: go/test/e2e/mocks/mock_sts_server.go:250 returns_error: да description: —


### extractClaimFromJWT (go/test/e2e/mocks/mock_sts_server.go:250)


extractClaimFromJWT is a function that performs operations based on the provided parameters and may return an error.


```go
func extractClaimFromJWT((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:250`



---


[function] name: extractMayActFromJWT file: go/test/e2e/mocks/mock_sts_server.go:242 returns_error: да description: —


### extractMayActFromJWT (go/test/e2e/mocks/mock_sts_server.go:242)


extractMayActFromJWT is a function that performs operations based on the provided parameters and may return an error.


```go
func extractMayActFromJWT((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:242`



---


[function] name: extractSubjectFromJWT file: go/test/e2e/mocks/mock_sts_server.go:234 returns_error: да description: extractSubjectFromJWT extracts the subject claim from a JWT token


### extractSubjectFromJWT (go/test/e2e/mocks/mock_sts_server.go:234)


extractSubjectFromJWT extracts the subject claim from a JWT token


```go
func extractSubjectFromJWT((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:234`



---


[function] name: generateMockAccessToken file: go/test/e2e/mocks/mock_sts_server.go:203 returns_error: да description: —


### generateMockAccessToken (go/test/e2e/mocks/mock_sts_server.go:203)


generateMockAccessToken is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *MockSTSServer) generateMockAccessToken((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:203`



---


[function] name: handleRequest file: go/test/e2e/mocks/mock_sts_server.go:94 returns_error: нет description: —


### handleRequest (go/test/e2e/mocks/mock_sts_server.go:94)


handleRequest is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (m *MockSTSServer) handleRequest((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:94`



---


[function] name: handleTokenExchange file: go/test/e2e/mocks/mock_sts_server.go:124 returns_error: нет description: —


### handleTokenExchange (go/test/e2e/mocks/mock_sts_server.go:124)


handleTokenExchange is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (m *MockSTSServer) handleTokenExchange((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


**Тип ответа:** r


```json
{
  "server": null,
  "requests": [],
  "k8sURL": "string",
  "agentServiceAccount": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


**Тип ответа:** http.Request


```json
{
  "GrantType": "string",
  "SubjectToken": "string",
  "SubjectTokenType": "string",
  "ActorToken": "string",
  "ActorTokenType": "string",
  "Resource": "string",
  "Audience": "string",
  "Scope": "string",
  "RequestedTokenType": "string"
}
```


*Определено в:* `go/test/e2e/mocks/mock_sts_server.go`


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:124`



---


[function] name: handleWellKnown file: go/test/e2e/mocks/mock_sts_server.go:105 returns_error: нет description: —


### handleWellKnown (go/test/e2e/mocks/mock_sts_server.go:105)


handleWellKnown is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter).


```go
func (m *MockSTSServer) handleWellKnown((w http.ResponseWriter)) (w http.ResponseWriter)
```


**Тип ответа:** w


```json
{
  "ThreadID": "string",
  "MethodName": "string",
  "StateData": {}
}
```


*Определено в:* `go/internal/httpserver/handlers/crewai.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "request": null
}
```


*Определено в:* `go/internal/httpserver/middleware_error.go`


📍 *Расположение:* `go/test/e2e/mocks/mock_sts_server.go:105`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](go_pkg.md)


---

