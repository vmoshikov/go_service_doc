---
title: "Функции: atproto/auth"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/auth
---


# Функции: atproto/auth


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_atdata.md)

- [Следующая директория](atproto_identity.md)


---


## Меню по файлам


- 📄 [atproto/auth/http.go](#atprotoauthhttpgo)

- 📄 [atproto/auth/jwt.go](#atprotoauthjwtgo)

- 📄 [atproto/auth/jwt_signing.go](#atprotoauthjwt_signinggo)

- 📄 [atproto/auth/oauth/cmd/oauth-web-demo/main.go](#atprotoauthoauthcmdoauth-web-demomaingo)

- 📄 [atproto/auth/oauth/jwt_signing.go](#atprotoauthoauthjwt_signinggo)

- 📄 [atproto/auth/oauth/memstore.go](#atprotoauthoauthmemstorego)

- 📄 [atproto/auth/oauth/oauth.go](#atprotoauthoauthoauthgo)

- 📄 [atproto/auth/oauth/resolver.go](#atprotoauthoauthresolvergo)

- 📄 [atproto/auth/oauth/session.go](#atprotoauthoauthsessiongo)

- 📄 [atproto/auth/oauth/types.go](#atprotoauthoauthtypesgo)

- 📄 [atproto/auth/oauth/util.go](#atprotoauthoauthutilgo)

- 📄 [atproto/auth/oauthscope.go](#atprotoauthoauthscopego)

- 📄 [atproto/auth/permission.go](#atprotoauthpermissiongo)

- 📄 [atproto/auth/permission_util.go](#atprotoauthpermission_utilgo)


---


## atproto/auth/http.go


📄 Исходный файл: `atproto/auth/http.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [AdminAuthMiddleware](#adminauthmiddleware-atprotoauthhttpgo19) `:19`

- 🔗 [Middleware](#middleware-atprotoauthhttpgo43) `:43`


</details>


[function] name: AdminAuthMiddleware file: atproto/auth/http.go:19 returns_error: нет description: HTTP Middleware for atproto admin auth, which is HTTP Basic auth with the username "admin".

This supports multiple admi


### AdminAuthMiddleware (atproto/auth/http.go:19)


HTTP Middleware for atproto admin auth, which is HTTP Basic auth with the username "admin".

This supports multiple admin passwords, which makes it easier to rotate service secrets.

This can be used with `echo.WrapMiddleware` (part of the echo web framework)


```go
func AdminAuthMiddleware((handler http.HandlerFunc, adminPasswords []string)) (handler http.HandlerFunc, adminPasswords []string)
```


**Тип ответа:** handler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.HandlerFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adminPasswords


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/http.go:19`



---


[function] name: Middleware file: atproto/auth/http.go:43 returns_error: нет description: HTTP Middleware for inter-service auth, which is HTTP Bearer with JWT.

'mandatory' indicates whether valid inter-servic


### Middleware (atproto/auth/http.go:43)


HTTP Middleware for inter-service auth, which is HTTP Bearer with JWT.

'mandatory' indicates whether valid inter-service auth must be present, or just optional.


```go
func (v *ServiceAuthValidator) Middleware((handler http.HandlerFunc, mandatory bool)) (handler http.HandlerFunc, mandatory bool)
```


**Тип ответа:** handler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.HandlerFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mandatory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/http.go:43`




## atproto/auth/jwt.go


📄 Исходный файл: `atproto/auth/jwt.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [SignServiceAuth](#signserviceauth-atprotoauthjwtgo125) `:125`

- 🔗 [Validate](#validate-atprotoauthjwtgo34) `:34`

- 🔗 [fetchIssuerKeyFunc](#fetchissuerkeyfunc-atprotoauthjwtgo96) `:96`

- 🔗 [randomNonce](#randomnonce-atprotoauthjwtgo119) `:119`


</details>


[function] name: SignServiceAuth file: atproto/auth/jwt.go:125 returns_error: да description: —


### SignServiceAuth (atproto/auth/jwt.go:125)


SignServiceAuth is a function that performs operations based on the provided parameters and may return an error.


```go
func SignServiceAuth((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/jwt.go:125`



---


[function] name: Validate file: atproto/auth/jwt.go:34 returns_error: да description: —


### Validate (atproto/auth/jwt.go:34)


Validate is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *ServiceAuthValidator) Validate((syntax.DID, error)) (syntax.DID, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `syntax.DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/jwt.go:34`



---


[function] name: fetchIssuerKeyFunc file: atproto/auth/jwt.go:96 returns_error: нет description: resolves public key from identity directory


### fetchIssuerKeyFunc (atproto/auth/jwt.go:96)


resolves public key from identity directory


```go
func (s *ServiceAuthValidator) fetchIssuerKeyFunc((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `atproto/auth/jwt.go:96`



---


[function] name: randomNonce file: atproto/auth/jwt.go:119 returns_error: нет description: —


### randomNonce (atproto/auth/jwt.go:119)


randomNonce is a function that performs operations based on the provided parameters and returns ().


```go
func randomNonce(()) ()
```


📍 *Расположение:* `atproto/auth/jwt.go:119`




## atproto/auth/jwt_signing.go


📄 Исходный файл: `atproto/auth/jwt_signing.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Alg](#alg-atprotoauthjwt_signinggo78) `:78`

- 🔗 [Sign](#sign-atprotoauthjwt_signinggo69) `:69`

- 🔗 [Verify](#verify-atprotoauthjwt_signinggo51) `:51`

- 🔗 [init](#init-atprotoauthjwt_signinggo26) `:26`

- 🔗 [toES256](#toes256-atprotoauthjwt_signinggo86) `:86`

- 🔗 [toES256K](#toes256k-atprotoauthjwt_signinggo82) `:82`


</details>


[function] name: Alg file: atproto/auth/jwt_signing.go:78 returns_error: нет description: —


### Alg (atproto/auth/jwt_signing.go:78)


Alg is a method that performs operations based on the provided parameters and returns ().


```go
func (sm *signingMethodAtproto) Alg(()) ()
```


📍 *Расположение:* `atproto/auth/jwt_signing.go:78`



---


[function] name: Sign file: atproto/auth/jwt_signing.go:69 returns_error: да description: —


### Sign (atproto/auth/jwt_signing.go:69)


Sign is a method that performs operations based on the provided parameters and may return an error.


```go
func (sm *signingMethodAtproto) Sign(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/jwt_signing.go:69`



---


[function] name: Verify file: atproto/auth/jwt_signing.go:51 returns_error: нет description: —


### Verify (atproto/auth/jwt_signing.go:51)


Verify is a method that performs operations based on the provided parameters and returns (signingString string, sig []byte, key interface{}).


```go
func (sm *signingMethodAtproto) Verify((signingString string, sig []byte, key interface{})) (signingString string, sig []byte, key interface{})
```


**Тип ответа:** signingString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sig


```json
{
  "cid": "string",
  "cts": "string",
  "exp": "string",
  "neg": false,
  "src": "string",
  "uri": "string",
  "val": "string",
  "ver": 0
}
```


*Определено в:* `util/labels/labels.go`


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/jwt_signing.go:51`



---


[function] name: init file: atproto/auth/jwt_signing.go:26 returns_error: нет description: —


### init (atproto/auth/jwt_signing.go:26)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `atproto/auth/jwt_signing.go:26`



---


[function] name: toES256 file: atproto/auth/jwt_signing.go:86 returns_error: нет description: —


### toES256 (atproto/auth/jwt_signing.go:86)


toES256 is a function that performs operations based on the provided parameters and returns (sig []byte).


```go
func toES256((sig []byte)) (sig []byte)
```


**Тип ответа:** sig


```json
{
  "cid": "string",
  "cts": "string",
  "exp": "string",
  "neg": false,
  "src": "string",
  "uri": "string",
  "val": "string",
  "ver": 0
}
```


*Определено в:* `util/labels/labels.go`


📍 *Расположение:* `atproto/auth/jwt_signing.go:86`



---


[function] name: toES256K file: atproto/auth/jwt_signing.go:82 returns_error: нет description: —


### toES256K (atproto/auth/jwt_signing.go:82)


toES256K is a function that performs operations based on the provided parameters and returns (sig []byte).


```go
func toES256K((sig []byte)) (sig []byte)
```


**Тип ответа:** sig


```json
{
  "cid": "string",
  "cts": "string",
  "exp": "string",
  "neg": false,
  "src": "string",
  "uri": "string",
  "val": "string",
  "ver": 0
}
```


*Определено в:* `util/labels/labels.go`


📍 *Расположение:* `atproto/auth/jwt_signing.go:82`




## atproto/auth/oauth/cmd/oauth-web-demo/main.go


📄 Исходный файл: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [ClientMetadata](#clientmetadata-atprotoauthoauthcmdoauth-web-demomaingo166) `:166`

- 🔗 [Homepage](#homepage-atprotoauthoauthcmdoauth-web-demomaingo199) `:199`

- 🔗 [JWKS](#jwks-atprotoauthoauthcmdoauth-web-demomaingo190) `:190`

- 🔗 [OAuthCallback](#oauthcallback-atprotoauthoauthcmdoauth-web-demomaingo244) `:244`

- 🔗 [OAuthLogin](#oauthlogin-atprotoauthoauthcmdoauth-web-demomaingo217) `:217`

- 🔗 [OAuthLogout](#oauthlogout-atprotoauthoauthcmdoauth-web-demomaingo299) `:299`

- 🔗 [OAuthRefresh](#oauthrefresh-atprotoauthoauthcmdoauth-web-demomaingo273) `:273`

- 🔗 [Post](#post-atprotoauthoauthcmdoauth-web-demomaingo322) `:322`

- 🔗 [currentSessionDID](#currentsessiondid-atprotoauthoauthcmdoauth-web-demomaingo144) `:144`

- 🔗 [main](#main-atprotoauthoauthcmdoauth-web-demomaingo25) `:25`

- 🔗 [runServer](#runserver-atprotoauthoauthcmdoauth-web-demomaingo84) `:84`

- 🔗 [strPtr](#strptr-atprotoauthoauthcmdoauth-web-demomaingo162) `:162`


</details>


[function] name: ClientMetadata file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:166 returns_error: нет description: —


### ClientMetadata (atproto/auth/oauth/cmd/oauth-web-demo/main.go:166)


ClientMetadata is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (s *Server) ClientMetadata((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:166`



---


[function] name: Homepage file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:199 returns_error: нет description: —


### Homepage (atproto/auth/oauth/cmd/oauth-web-demo/main.go:199)


Homepage is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (s *Server) Homepage((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:199`



---


[function] name: JWKS file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:190 returns_error: нет description: —


### JWKS (atproto/auth/oauth/cmd/oauth-web-demo/main.go:190)


JWKS is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (s *Server) JWKS((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:190`



---


[function] name: OAuthCallback file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:244 returns_error: нет description: —


### OAuthCallback (atproto/auth/oauth/cmd/oauth-web-demo/main.go:244)


OAuthCallback is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (s *Server) OAuthCallback((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:244`



---


[function] name: OAuthLogin file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:217 returns_error: нет description: —


### OAuthLogin (atproto/auth/oauth/cmd/oauth-web-demo/main.go:217)


OAuthLogin is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (s *Server) OAuthLogin((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:217`



---


[function] name: OAuthLogout file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:299 returns_error: нет description: —


### OAuthLogout (atproto/auth/oauth/cmd/oauth-web-demo/main.go:299)


OAuthLogout is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (s *Server) OAuthLogout((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:299`



---


[function] name: OAuthRefresh file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:273 returns_error: нет description: —


### OAuthRefresh (atproto/auth/oauth/cmd/oauth-web-demo/main.go:273)


OAuthRefresh is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (s *Server) OAuthRefresh((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:273`



---


[function] name: Post file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:322 returns_error: нет description: —


### Post (atproto/auth/oauth/cmd/oauth-web-demo/main.go:322)


Post is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (s *Server) Post((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


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


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:322`



---


[function] name: currentSessionDID file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:144 returns_error: нет description: —


### currentSessionDID (atproto/auth/oauth/cmd/oauth-web-demo/main.go:144)


currentSessionDID is a method that performs operations based on the provided parameters and returns (*syntax.DID, string).


```go
func (s *Server) currentSessionDID((*syntax.DID, string)) (*syntax.DID, string)
```


**Тип запроса:** syntax.DID


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


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:144`



---


[function] name: main file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:25 returns_error: нет description: —


### main (atproto/auth/oauth/cmd/oauth-web-demo/main.go:25)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:25`



---


[function] name: runServer file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:84 returns_error: нет description: —


### runServer (atproto/auth/oauth/cmd/oauth-web-demo/main.go:84)


runServer is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runServer((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:84`



---


[function] name: strPtr file: atproto/auth/oauth/cmd/oauth-web-demo/main.go:162 returns_error: нет description: —


### strPtr (atproto/auth/oauth/cmd/oauth-web-demo/main.go:162)


strPtr is a function that performs operations based on the provided parameters and returns (raw string).


```go
func strPtr((raw string)) (raw string)
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


📍 *Расположение:* `atproto/auth/oauth/cmd/oauth-web-demo/main.go:162`




## atproto/auth/oauth/jwt_signing.go


📄 Исходный файл: `atproto/auth/oauth/jwt_signing.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Alg](#alg-atprotoauthoauthjwt_signinggo71) `:71`

- 🔗 [Sign](#sign-atprotoauthoauthjwt_signinggo62) `:62`

- 🔗 [Verify](#verify-atprotoauthoauthjwt_signinggo44) `:44`

- 🔗 [init](#init-atprotoauthoauthjwt_signinggo28) `:28`

- 🔗 [keySigningMethod](#keysigningmethod-atprotoauthoauthjwt_signinggo79) `:79`

- 🔗 [toES256](#toes256-atprotoauthoauthjwt_signinggo75) `:75`


</details>


[function] name: Alg file: atproto/auth/oauth/jwt_signing.go:71 returns_error: нет description: —


### Alg (atproto/auth/oauth/jwt_signing.go:71)


Alg is a method that performs operations based on the provided parameters and returns ().


```go
func (sm *signingMethodAtproto) Alg(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/jwt_signing.go:71`



---


[function] name: Sign file: atproto/auth/oauth/jwt_signing.go:62 returns_error: да description: —


### Sign (atproto/auth/oauth/jwt_signing.go:62)


Sign is a method that performs operations based on the provided parameters and may return an error.


```go
func (sm *signingMethodAtproto) Sign(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/jwt_signing.go:62`



---


[function] name: Verify file: atproto/auth/oauth/jwt_signing.go:44 returns_error: нет description: —


### Verify (atproto/auth/oauth/jwt_signing.go:44)


Verify is a method that performs operations based on the provided parameters and returns (signingString string, sig []byte, key interface{}).


```go
func (sm *signingMethodAtproto) Verify((signingString string, sig []byte, key interface{})) (signingString string, sig []byte, key interface{})
```


**Тип ответа:** signingString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sig


```json
{
  "cid": "string",
  "cts": "string",
  "exp": "string",
  "neg": false,
  "src": "string",
  "uri": "string",
  "val": "string",
  "ver": 0
}
```


*Определено в:* `util/labels/labels.go`


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/jwt_signing.go:44`



---


[function] name: init file: atproto/auth/oauth/jwt_signing.go:28 returns_error: нет description: —


### init (atproto/auth/oauth/jwt_signing.go:28)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/jwt_signing.go:28`



---


[function] name: keySigningMethod file: atproto/auth/oauth/jwt_signing.go:79 returns_error: да description: —


### keySigningMethod (atproto/auth/oauth/jwt_signing.go:79)


keySigningMethod is a function that performs operations based on the provided parameters and may return an error.


```go
func keySigningMethod((jwt.SigningMethod, error)) (jwt.SigningMethod, error)
```


**Тип ответа:** jwt.SigningMethod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `jwt.SigningMethod`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/jwt_signing.go:79`



---


[function] name: toES256 file: atproto/auth/oauth/jwt_signing.go:75 returns_error: нет description: —


### toES256 (atproto/auth/oauth/jwt_signing.go:75)


toES256 is a function that performs operations based on the provided parameters and returns (sig []byte).


```go
func toES256((sig []byte)) (sig []byte)
```


**Тип ответа:** sig


```json
{
  "cid": "string",
  "cts": "string",
  "exp": "string",
  "neg": false,
  "src": "string",
  "uri": "string",
  "val": "string",
  "ver": 0
}
```


*Определено в:* `util/labels/labels.go`


📍 *Расположение:* `atproto/auth/oauth/jwt_signing.go:75`




## atproto/auth/oauth/memstore.go


📄 Исходный файл: `atproto/auth/oauth/memstore.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [DeleteAuthRequestInfo](#deleteauthrequestinfo-atprotoauthoauthmemstorego86) `:86`

- 🔗 [DeleteSession](#deletesession-atprotoauthoauthmemstorego53) `:53`

- 🔗 [GetAuthRequestInfo](#getauthrequestinfo-atprotoauthoauthmemstorego61) `:61`

- 🔗 [GetSession](#getsession-atprotoauthoauthmemstorego34) `:34`

- 🔗 [NewMemStore](#newmemstore-atprotoauthoauthmemstorego23) `:23`

- 🔗 [SaveAuthRequestInfo](#saveauthrequestinfo-atprotoauthoauthmemstorego73) `:73`

- 🔗 [SaveSession](#savesession-atprotoauthoauthmemstorego45) `:45`

- 🔗 [memKey](#memkey-atprotoauthoauthmemstorego30) `:30`


</details>


[function] name: DeleteAuthRequestInfo file: atproto/auth/oauth/memstore.go:86 returns_error: нет description: —


### DeleteAuthRequestInfo (atproto/auth/oauth/memstore.go:86)


DeleteAuthRequestInfo is a method that deletes data based on the provided parameters and returns (ctx context.Context, state string).


```go
func (m *MemStore) DeleteAuthRequestInfo((ctx context.Context, state string)) (ctx context.Context, state string)
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


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/memstore.go:86`



---


[function] name: DeleteSession file: atproto/auth/oauth/memstore.go:53 returns_error: нет description: —


### DeleteSession (atproto/auth/oauth/memstore.go:53)


DeleteSession is a method that deletes data based on the provided parameters and returns (ctx context.Context, did syntax.DID, sessionID string).


```go
func (m *MemStore) DeleteSession((ctx context.Context, did syntax.DID, sessionID string)) (ctx context.Context, did syntax.DID, sessionID string)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


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


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/memstore.go:53`



---


[function] name: GetAuthRequestInfo file: atproto/auth/oauth/memstore.go:61 returns_error: да description: —


### GetAuthRequestInfo (atproto/auth/oauth/memstore.go:61)


GetAuthRequestInfo is a method that retrieves data based on the provided parameters and may return an error.


```go
func (m *MemStore) GetAuthRequestInfo((*AuthRequestData, error)) (*AuthRequestData, error)
```


**Тип запроса:** AuthRequestData


```json
{
  "State": "string",
  "AuthServerURL": "string",
  "AccountDID": null,
  "Scopes": [],
  "RequestURI": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "PKCEVerifier": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Тип ответа:** AuthRequestData


```json
{
  "State": "string",
  "AuthServerURL": "string",
  "AccountDID": null,
  "Scopes": [],
  "RequestURI": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "PKCEVerifier": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AuthRequestData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/memstore.go:61`



---


[function] name: GetSession file: atproto/auth/oauth/memstore.go:34 returns_error: да description: —


### GetSession (atproto/auth/oauth/memstore.go:34)


GetSession is a method that retrieves data based on the provided parameters and may return an error.


```go
func (m *MemStore) GetSession((*ClientSessionData, error)) (*ClientSessionData, error)
```


**Тип запроса:** ClientSessionData


```json
{
  "AccountDID": {},
  "SessionID": "string",
  "HostURL": "string",
  "AuthServerURL": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "Scopes": [],
  "AccessToken": "string",
  "RefreshToken": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPHostNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/session.go`


**Тип ответа:** ClientSessionData


```json
{
  "AccountDID": {},
  "SessionID": "string",
  "HostURL": "string",
  "AuthServerURL": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "Scopes": [],
  "AccessToken": "string",
  "RefreshToken": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPHostNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ClientSessionData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/memstore.go:34`



---


[function] name: NewMemStore file: atproto/auth/oauth/memstore.go:23 returns_error: нет description: —


### NewMemStore (atproto/auth/oauth/memstore.go:23)


NewMemStore is a function that performs operations based on the provided parameters and returns ().


```go
func NewMemStore(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/memstore.go:23`



---


[function] name: SaveAuthRequestInfo file: atproto/auth/oauth/memstore.go:73 returns_error: нет description: —


### SaveAuthRequestInfo (atproto/auth/oauth/memstore.go:73)


SaveAuthRequestInfo is a method that performs operations based on the provided parameters and returns (ctx context.Context, info AuthRequestData).


```go
func (m *MemStore) SaveAuthRequestInfo((ctx context.Context, info AuthRequestData)) (ctx context.Context, info AuthRequestData)
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


**Тип ответа:** info


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AuthRequestData


```json
{
  "State": "string",
  "AuthServerURL": "string",
  "AccountDID": null,
  "Scopes": [],
  "RequestURI": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "PKCEVerifier": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


📍 *Расположение:* `atproto/auth/oauth/memstore.go:73`



---


[function] name: SaveSession file: atproto/auth/oauth/memstore.go:45 returns_error: нет description: —


### SaveSession (atproto/auth/oauth/memstore.go:45)


SaveSession is a method that performs operations based on the provided parameters and returns (ctx context.Context, sess ClientSessionData).


```go
func (m *MemStore) SaveSession((ctx context.Context, sess ClientSessionData)) (ctx context.Context, sess ClientSessionData)
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


**Тип ответа:** sess


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ClientSessionData


```json
{
  "AccountDID": {},
  "SessionID": "string",
  "HostURL": "string",
  "AuthServerURL": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "Scopes": [],
  "AccessToken": "string",
  "RefreshToken": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPHostNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/session.go`


📍 *Расположение:* `atproto/auth/oauth/memstore.go:45`



---


[function] name: memKey file: atproto/auth/oauth/memstore.go:30 returns_error: нет description: —


### memKey (atproto/auth/oauth/memstore.go:30)


memKey is a function that performs operations based on the provided parameters and returns (did syntax.DID, sessionID string).


```go
func memKey((did syntax.DID, sessionID string)) (did syntax.DID, sessionID string)
```


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


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


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/memstore.go:30`




## atproto/auth/oauth/oauth.go


📄 Исходный файл: `atproto/auth/oauth/oauth.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [ClientMetadata](#clientmetadata-atprotoauthoauthoauthgo168) `:168`

- 🔗 [IsConfidential](#isconfidential-atprotoauthoauthoauthgo111) `:111`

- 🔗 [Logout](#logout-atprotoauthoauthoauthgo701) `:701`

- 🔗 [NewAuthDPoP](#newauthdpop-atprotoauthoauthoauthgo272) `:272`

- 🔗 [NewClientApp](#newclientapp-atprotoauthoauthoauthgo53) `:53`

- 🔗 [NewClientAssertion](#newclientassertion-atprotoauthoauthoauthgo244) `:244`

- 🔗 [NewLocalhostConfig](#newlocalhostconfig-atprotoauthoauthoauthgo97) `:97`

- 🔗 [NewPublicConfig](#newpublicconfig-atprotoauthoauthoauthgo84) `:84`

- 🔗 [ProcessCallback](#processcallback-atprotoauthoauthoauthgo588) `:588`

- 🔗 [PublicJWKS](#publicjwks-atprotoauthoauthoauthgo137) `:137`

- 🔗 [ResumeSession](#resumesession-atprotoauthoauthoauthgo192) `:192`

- 🔗 [SendAuthRequest](#sendauthrequest-atprotoauthoauthoauthgo321) `:321`

- 🔗 [SendInitialTokenRequest](#sendinitialtokenrequest-atprotoauthoauthoauthgo436) `:436`

- 🔗 [SetClientSecret](#setclientsecret-atprotoauthoauthoauthgo120) `:120`

- 🔗 [StartAuthFlow](#startauthflow-atprotoauthoauthoauthgo528) `:528`

- 🔗 [parseAuthErrorReason](#parseautherrorreason-atprotoauthoauthoauthgo309) `:309`

- 🔗 [scopeStr](#scopestr-atprotoauthoauthoauthgo161) `:161`


</details>


[function] name: ClientMetadata file: atproto/auth/oauth/oauth.go:168 returns_error: нет description: Returns a [ClientMetadata] struct with the required fields populated based on this client configuration. Clients may wan


### ClientMetadata (atproto/auth/oauth/oauth.go:168)


Returns a [ClientMetadata] struct with the required fields populated based on this client configuration. Clients may want to populate additional metadata fields on top of this response.

NOTE: confidential clients currently must provide JWKSURI after the fact


```go
func (config *ClientConfig) ClientMetadata(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/oauth.go:168`



---


[function] name: IsConfidential file: atproto/auth/oauth/oauth.go:111 returns_error: нет description: Whether this is a "confidential" OAuth client (with configured client attestation key), versus "public" client.


### IsConfidential (atproto/auth/oauth/oauth.go:111)


Whether this is a "confidential" OAuth client (with configured client attestation key), versus "public" client.


```go
func (config *ClientConfig) IsConfidential(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/oauth.go:111`



---


[function] name: Logout file: atproto/auth/oauth/oauth.go:701 returns_error: нет description: High-level helper to delete a session, including revoking access/refresh tokens if supported by the AS


### Logout (atproto/auth/oauth/oauth.go:701)


High-level helper to delete a session, including revoking access/refresh tokens if supported by the AS


```go
func (app *ClientApp) Logout((ctx context.Context, did syntax.DID, sessionID string)) (ctx context.Context, did syntax.DID, sessionID string)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


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


**Тип ответа:** sessionID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/oauth.go:701`



---


[function] name: NewAuthDPoP file: atproto/auth/oauth/oauth.go:272 returns_error: да description: Creates a DPoP token (JWT) for use with an OAuth Auth Server (not to be used with Resource Server). The returned JWT is 


### NewAuthDPoP (atproto/auth/oauth/oauth.go:272)


Creates a DPoP token (JWT) for use with an OAuth Auth Server (not to be used with Resource Server). The returned JWT is not bound to an Access Token (no 'ath'), and does not indicate an issuer ('iss').

This is used during initial auth request (PAR), initial token request, and subsequent refresh token requests. Note that a full [ClientSession] is not available in several of these circumstances, so this is a stand-alone function.


```go
func NewAuthDPoP((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/oauth.go:272`



---


[function] name: NewClientApp file: atproto/auth/oauth/oauth.go:53 returns_error: нет description: Constructs a [ClientApp] based on configuration.


### NewClientApp (atproto/auth/oauth/oauth.go:53)


Constructs a [ClientApp] based on configuration.


```go
func NewClientApp((config *ClientConfig, store ClientAuthStore)) (config *ClientConfig, store ClientAuthStore)
```


**Тип запроса:** ClientConfig


```json
{
  "ClientID": "string",
  "CallbackURL": "string",
  "Scopes": [],
  "UserAgent": "string",
  "PrivateKey": {},
  "KeyID": "string"
}
```


*Определено в:* `atproto/auth/oauth/oauth.go`


**Тип ответа:** config


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ClientConfig


```json
{
  "ClientID": "string",
  "CallbackURL": "string",
  "Scopes": [],
  "UserAgent": "string",
  "PrivateKey": {},
  "KeyID": "string"
}
```


*Определено в:* `atproto/auth/oauth/oauth.go`


**Тип ответа:** store


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** ClientAuthStore


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/oauth.go:53`



---


[function] name: NewClientAssertion file: atproto/auth/oauth/oauth.go:244 returns_error: да description: Low-level helper to generate and sign an OAuth confidential client assertion token (JWT).


### NewClientAssertion (atproto/auth/oauth/oauth.go:244)


Low-level helper to generate and sign an OAuth confidential client assertion token (JWT).


```go
func (cfg *ClientConfig) NewClientAssertion((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/oauth.go:244`



---


[function] name: NewLocalhostConfig file: atproto/auth/oauth/oauth.go:97 returns_error: нет description: Creates a basic [ClientConfig] for use with localhost developmnet. Such a client is always public (non-confidential).

T


### NewLocalhostConfig (atproto/auth/oauth/oauth.go:97)


Creates a basic [ClientConfig] for use with localhost developmnet. Such a client is always public (non-confidential).

The "scopes" array must include "atproto".


```go
func NewLocalhostConfig((callbackURL string, scopes []string)) (callbackURL string, scopes []string)
```


**Тип ответа:** callbackURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** scopes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/oauth.go:97`



---


[function] name: NewPublicConfig file: atproto/auth/oauth/oauth.go:84 returns_error: нет description: Creates a basic [ClientConfig] for use as a public (non-confidential) client. To upgrade to a confidential client, use t


### NewPublicConfig (atproto/auth/oauth/oauth.go:84)


Creates a basic [ClientConfig] for use as a public (non-confidential) client. To upgrade to a confidential client, use this method and then [ClientConfig.SetClientSecret].

The "scopes" array must include "atproto".


```go
func NewPublicConfig((clientID, callbackURL string, scopes []string)) (clientID, callbackURL string, scopes []string)
```


**Тип ответа:** clientID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** callbackURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** scopes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/oauth.go:84`



---


[function] name: ProcessCallback file: atproto/auth/oauth/oauth.go:588 returns_error: да description: High-level helper for completing auth flow: verifies callback query parameters against persisted auth request info, make


### ProcessCallback (atproto/auth/oauth/oauth.go:588)


High-level helper for completing auth flow: verifies callback query parameters against persisted auth request info, makes initial token request to the auth server, validates account identifier, and persists session data.


```go
func (app *ClientApp) ProcessCallback((*ClientSessionData, error)) (*ClientSessionData, error)
```


**Тип запроса:** ClientSessionData


```json
{
  "AccountDID": {},
  "SessionID": "string",
  "HostURL": "string",
  "AuthServerURL": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "Scopes": [],
  "AccessToken": "string",
  "RefreshToken": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPHostNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/session.go`


**Тип ответа:** ClientSessionData


```json
{
  "AccountDID": {},
  "SessionID": "string",
  "HostURL": "string",
  "AuthServerURL": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "Scopes": [],
  "AccessToken": "string",
  "RefreshToken": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPHostNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ClientSessionData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/oauth.go:588`



---


[function] name: PublicJWKS file: atproto/auth/oauth/oauth.go:137 returns_error: нет description: Returns a "JWKS" representation of public keys for the client. This can be returned as JSON, as part of client metadata.


### PublicJWKS (atproto/auth/oauth/oauth.go:137)


Returns a "JWKS" representation of public keys for the client. This can be returned as JSON, as part of client metadata.

If the client does not have any keys (eg, public client), returns an empty set.


```go
func (config *ClientConfig) PublicJWKS(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/oauth.go:137`



---


[function] name: ResumeSession file: atproto/auth/oauth/oauth.go:192 returns_error: да description: High-level helper for fetching session data from store, based on account DID and session identifier.


### ResumeSession (atproto/auth/oauth/oauth.go:192)


High-level helper for fetching session data from store, based on account DID and session identifier.


```go
func (app *ClientApp) ResumeSession((*ClientSession, error)) (*ClientSession, error)
```


**Тип запроса:** ClientSession


```json
{
  "Client": null,
  "Config": null,
  "Data": null,
  "DPoPPrivateKey": {},
  "PersistSessionCallback": {},
  "lk": {}
}
```


*Определено в:* `atproto/auth/oauth/session.go`


**Тип ответа:** ClientSession


```json
{
  "Client": null,
  "Config": null,
  "Data": null,
  "DPoPPrivateKey": {},
  "PersistSessionCallback": {},
  "lk": {}
}
```


*Определено в:* `atproto/auth/oauth/session.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ClientSession`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/oauth.go:192`



---


[function] name: SendAuthRequest file: atproto/auth/oauth/oauth.go:321 returns_error: да description: Low-level helper to send PAR request to auth server, which involves starting PKCE and DPoP.


### SendAuthRequest (atproto/auth/oauth/oauth.go:321)


Low-level helper to send PAR request to auth server, which involves starting PKCE and DPoP.


```go
func (app *ClientApp) SendAuthRequest((*AuthRequestData, error)) (*AuthRequestData, error)
```


**Тип запроса:** AuthRequestData


```json
{
  "State": "string",
  "AuthServerURL": "string",
  "AccountDID": null,
  "Scopes": [],
  "RequestURI": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "PKCEVerifier": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Тип ответа:** AuthRequestData


```json
{
  "State": "string",
  "AuthServerURL": "string",
  "AccountDID": null,
  "Scopes": [],
  "RequestURI": "string",
  "AuthServerTokenEndpoint": "string",
  "AuthServerRevocationEndpoint": "string",
  "PKCEVerifier": "string",
  "DPoPAuthServerNonce": "string",
  "DPoPPrivateKeyMultibase": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AuthRequestData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/oauth.go:321`



---


[function] name: SendInitialTokenRequest file: atproto/auth/oauth/oauth.go:436 returns_error: да description: Lower-level helper. This is usually invoked as part of [ClientApp.ProcessCallback].


### SendInitialTokenRequest (atproto/auth/oauth/oauth.go:436)


Lower-level helper. This is usually invoked as part of [ClientApp.ProcessCallback].


```go
func (app *ClientApp) SendInitialTokenRequest((*TokenResponse, error)) (*TokenResponse, error)
```


**Тип запроса:** TokenResponse


```json
{
  "Subject": "string",
  "Scope": "string",
  "AccessToken": "string",
  "RefreshToken": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Тип ответа:** TokenResponse


```json
{
  "Subject": "string",
  "Scope": "string",
  "AccessToken": "string",
  "RefreshToken": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TokenResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/oauth.go:436`



---


[function] name: SetClientSecret file: atproto/auth/oauth/oauth.go:120 returns_error: нет description: Set the secret key used for client assertions (for confidential clients).

The corresponding public key (with matching k


### SetClientSecret (atproto/auth/oauth/oauth.go:120)


Set the secret key used for client assertions (for confidential clients).

The corresponding public key (with matching key ID) must be present in the JWK list referenced by the client metadata document.

Key IDs may be arbitrary strings such as UUIDs, stringified sequence numbers, or human-readable identifiers.


```go
func (config *ClientConfig) SetClientSecret((priv atcrypto.PrivateKey, keyID string)) (priv atcrypto.PrivateKey, keyID string)
```


**Тип ответа:** priv


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atcrypto.PrivateKey


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Тип ответа:** keyID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/oauth.go:120`



---


[function] name: StartAuthFlow file: atproto/auth/oauth/oauth.go:528 returns_error: да description: High-level helper for starting a new session. Resolves identifier to resource server and auth server metadata, sends PAR


### StartAuthFlow (atproto/auth/oauth/oauth.go:528)


High-level helper for starting a new session. Resolves identifier to resource server and auth server metadata, sends PAR request, persists request info to store, and returns a redirect URL.

The `identifier` argument can be an atproto account identifier (handle or DID), or can be a URL to the account's auth server.

The returned sting will be a web URL that the user should be redirected to (in browser) to approve the auth flow.


```go
func (app *ClientApp) StartAuthFlow((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/oauth.go:528`



---


[function] name: parseAuthErrorReason file: atproto/auth/oauth/oauth.go:309 returns_error: нет description: attempts to read an HTTP response body as JSON, and determine an error reason. always closes the response body


### parseAuthErrorReason (atproto/auth/oauth/oauth.go:309)


attempts to read an HTTP response body as JSON, and determine an error reason. always closes the response body


```go
func parseAuthErrorReason((resp *http.Response, reqType string)) (resp *http.Response, reqType string)
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


**Тип ответа:** reqType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/oauth.go:309`



---


[function] name: scopeStr file: atproto/auth/oauth/oauth.go:161 returns_error: нет description: helper to turn a list of scope strings in to a single space-separated scope string


### scopeStr (atproto/auth/oauth/oauth.go:161)


helper to turn a list of scope strings in to a single space-separated scope string


```go
func scopeStr((scopes []string)) (scopes []string)
```


**Тип ответа:** scopes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/oauth.go:161`




## atproto/auth/oauth/resolver.go


📄 Исходный файл: `atproto/auth/oauth/resolver.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [NewResolver](#newresolver-atprotoauthoauthresolvergo22) `:22`

- 🔗 [ResolveAuthServerMetadata](#resolveauthservermetadata-atprotoauthoauthresolvergo87) `:87`

- 🔗 [ResolveAuthServerURL](#resolveauthserverurl-atprotoauthoauthresolvergo36) `:36`

- 🔗 [ResolveClientMetadata](#resolveclientmetadata-atprotoauthoauthresolvergo131) `:131`


</details>


[function] name: NewResolver file: atproto/auth/oauth/resolver.go:22 returns_error: нет description: —


### NewResolver (atproto/auth/oauth/resolver.go:22)


NewResolver is a function that performs operations based on the provided parameters and returns ().


```go
func NewResolver(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/resolver.go:22`



---


[function] name: ResolveAuthServerMetadata file: atproto/auth/oauth/resolver.go:87 returns_error: да description: Resolves an Auth Server URL to server metadata. Validates metadata before returning.


### ResolveAuthServerMetadata (atproto/auth/oauth/resolver.go:87)


Resolves an Auth Server URL to server metadata. Validates metadata before returning.


```go
func (r *Resolver) ResolveAuthServerMetadata((*AuthServerMetadata, error)) (*AuthServerMetadata, error)
```


**Тип запроса:** AuthServerMetadata


```json
{
  "Issuer": "string",
  "AuthorizationEndpoint": "string",
  "TokenEndpoint": "string",
  "ResponseTypesSupported": [],
  "GrantTypesSupported": [],
  "CodeChallengeMethodsSupported": [],
  "TokenEndpointAuthMethodsSupoorted": [],
  "TokenEndpointAuthSigningAlgValuesSupported": [],
  "ScopesSupported": [],
  "AuthorizationReponseISSParameterSupported": false,
  "RequirePushedAuthorizationRequests": false,
  "PushedAuthorizationRequestEndpoint": "string",
  "DPoPSigningAlgValuesSupported": [],
  "RequireRequestURIRegistration": false,
  "ClientIDMetadataDocumentSupported": false,
  "RevocationEndpoint": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Тип ответа:** AuthServerMetadata


```json
{
  "Issuer": "string",
  "AuthorizationEndpoint": "string",
  "TokenEndpoint": "string",
  "ResponseTypesSupported": [],
  "GrantTypesSupported": [],
  "CodeChallengeMethodsSupported": [],
  "TokenEndpointAuthMethodsSupoorted": [],
  "TokenEndpointAuthSigningAlgValuesSupported": [],
  "ScopesSupported": [],
  "AuthorizationReponseISSParameterSupported": false,
  "RequirePushedAuthorizationRequests": false,
  "PushedAuthorizationRequestEndpoint": "string",
  "DPoPSigningAlgValuesSupported": [],
  "RequireRequestURIRegistration": false,
  "ClientIDMetadataDocumentSupported": false,
  "RevocationEndpoint": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AuthServerMetadata`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/resolver.go:87`



---


[function] name: ResolveAuthServerURL file: atproto/auth/oauth/resolver.go:36 returns_error: да description: Resolves a Resource Server URL (eg, an atproto account's registered PDS service URL) to an auth server URL (eg, entryway


### ResolveAuthServerURL (atproto/auth/oauth/resolver.go:36)


Resolves a Resource Server URL (eg, an atproto account's registered PDS service URL) to an auth server URL (eg, entryway URL). They might be the same server!

Ensures that the returned URL is valid (eg, parses as a URL).


```go
func (r *Resolver) ResolveAuthServerURL((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/resolver.go:36`



---


[function] name: ResolveClientMetadata file: atproto/auth/oauth/resolver.go:131 returns_error: да description: Fetches and validates OAuth client metadata document based on identifier in URL format.


### ResolveClientMetadata (atproto/auth/oauth/resolver.go:131)


Fetches and validates OAuth client metadata document based on identifier in URL format.


```go
func (r *Resolver) ResolveClientMetadata((*ClientMetadata, error)) (*ClientMetadata, error)
```


**Тип запроса:** ClientMetadata


```json
{
  "ClientID": "string",
  "ApplicationType": "string",
  "GrantTypes": [],
  "Scope": "string",
  "ResponseTypes": [],
  "RedirectURIs": [],
  "TokenEndpointAuthMethod": "string",
  "TokenEndpointAuthSigningAlg": "string",
  "DPoPBoundAccessTokens": false,
  "JWKS": null,
  "JWKSURI": "string",
  "ClientName": "string",
  "ClientURI": "string",
  "LogoURI": "string",
  "TosURI": "string",
  "PolicyURI": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Тип ответа:** ClientMetadata


```json
{
  "ClientID": "string",
  "ApplicationType": "string",
  "GrantTypes": [],
  "Scope": "string",
  "ResponseTypes": [],
  "RedirectURIs": [],
  "TokenEndpointAuthMethod": "string",
  "TokenEndpointAuthSigningAlg": "string",
  "DPoPBoundAccessTokens": false,
  "JWKS": null,
  "JWKSURI": "string",
  "ClientName": "string",
  "ClientURI": "string",
  "LogoURI": "string",
  "TosURI": "string",
  "PolicyURI": "string"
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ClientMetadata`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/resolver.go:131`




## atproto/auth/oauth/session.go


📄 Исходный файл: `atproto/auth/oauth/session.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [APIClient](#apiclient-atprotoauthoauthsessiongo401) `:401`

- 🔗 [DoWithAuth](#dowithauth-atprotoauthoauthsessiongo321) `:321`

- 🔗 [GetHostAccessData](#gethostaccessdata-atprotoauthoauthsessiongo298) `:298`

- 🔗 [NewHostDPoP](#newhostdpop-atprotoauthoauthsessiongo232) `:232`

- 🔗 [RefreshTokens](#refreshtokens-atprotoauthoauthsessiongo150) `:150`

- 🔗 [RevokeSession](#revokesession-atprotoauthoauthsessiongo192) `:192`

- 🔗 [UpdateHostDPoPNonce](#updatehostdpopnonce-atprotoauthoauthsessiongo305) `:305`

- 🔗 [dpopURL](#dpopurl-atprotoauthoauthsessiongo274) `:274`

- 🔗 [isExpiredAccessTokenHeader](#isexpiredaccesstokenheader-atprotoauthoauthsessiongo291) `:291`

- 🔗 [isNonceUpdateHeader](#isnonceupdateheader-atprotoauthoauthsessiongo284) `:284`

- 🔗 [postToAuthServer](#posttoauthserver-atprotoauthoauthsessiongo88) `:88`


</details>


[function] name: APIClient file: atproto/auth/oauth/session.go:401 returns_error: нет description: Creates a new [atclient.APIClient] which wraps this session for auth.


### APIClient (atproto/auth/oauth/session.go:401)


Creates a new [atclient.APIClient] which wraps this session for auth.


```go
func (sess *ClientSession) APIClient(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/session.go:401`



---


[function] name: DoWithAuth file: atproto/auth/oauth/session.go:321 returns_error: да description: Sends API request to OAuth Resource Server (PDS), using access token and DPoP.

Automatically handles DPoP nonce updates


### DoWithAuth (atproto/auth/oauth/session.go:321)


Sends API request to OAuth Resource Server (PDS), using access token and DPoP.

Automatically handles DPoP nonce updates and token refresh as needed, based on the response status code and `WWW-Authenticate` header.


```go
func (sess *ClientSession) DoWithAuth((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `atproto/auth/oauth/session.go:321`



---


[function] name: GetHostAccessData file: atproto/auth/oauth/session.go:298 returns_error: нет description: —


### GetHostAccessData (atproto/auth/oauth/session.go:298)


GetHostAccessData is a method that retrieves data based on the provided parameters and returns (accessToken string, dpopHostNonce string).


```go
func (sess *ClientSession) GetHostAccessData((accessToken string, dpopHostNonce string)) (accessToken string, dpopHostNonce string)
```


**Тип ответа:** accessToken


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dpopHostNonce


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/session.go:298`



---


[function] name: NewHostDPoP file: atproto/auth/oauth/session.go:232 returns_error: да description: Constructs and signs a DPoP JWT to include in request header to Host (aka Resource Server, aka PDS). These tokens are di


### NewHostDPoP (atproto/auth/oauth/session.go:232)


Constructs and signs a DPoP JWT to include in request header to Host (aka Resource Server, aka PDS). These tokens are different from those used with Auth Server token endpoints (even if the PDS is filling both roles)


```go
func (sess *ClientSession) NewHostDPoP((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/session.go:232`



---


[function] name: RefreshTokens file: atproto/auth/oauth/session.go:150 returns_error: да description: Requests new tokens from auth server, and returns the new access token on success.

Internally takes a lock on session d


### RefreshTokens (atproto/auth/oauth/session.go:150)


Requests new tokens from auth server, and returns the new access token on success.

Internally takes a lock on session data around the entire refresh process, including retries. Persists data using [PersistSessionCallback] if configured.


```go
func (sess *ClientSession) RefreshTokens((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauth/session.go:150`



---


[function] name: RevokeSession file: atproto/auth/oauth/session.go:192 returns_error: нет description: If supported by the AS, use the revocation endpoint to revoke both the access token and the refresh token.
This method a


### RevokeSession (atproto/auth/oauth/session.go:192)


If supported by the AS, use the revocation endpoint to revoke both the access token and the refresh token.
This method always succeeds - any errors during revocation are logged but not returned.


```go
func (sess *ClientSession) RevokeSession((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `atproto/auth/oauth/session.go:192`



---


[function] name: UpdateHostDPoPNonce file: atproto/auth/oauth/session.go:305 returns_error: нет description: —


### UpdateHostDPoPNonce (atproto/auth/oauth/session.go:305)


UpdateHostDPoPNonce is a method that updates data based on the provided parameters and returns (ctx context.Context, nonce string).


```go
func (sess *ClientSession) UpdateHostDPoPNonce((ctx context.Context, nonce string)) (ctx context.Context, nonce string)
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


**Тип ответа:** nonce


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/session.go:305`



---


[function] name: dpopURL file: atproto/auth/oauth/session.go:274 returns_error: нет description: copy a request URL and strip query params and fragment, for DPoP


### dpopURL (atproto/auth/oauth/session.go:274)


copy a request URL and strip query params and fragment, for DPoP


```go
func dpopURL((u *url.URL)) (u *url.URL)
```


**Тип запроса:** url.URL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** u


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** url.URL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/session.go:274`



---


[function] name: isExpiredAccessTokenHeader file: atproto/auth/oauth/session.go:291 returns_error: нет description: Parses a WWW-Authenticate response header to see if access token has expired (needs refresh)


### isExpiredAccessTokenHeader (atproto/auth/oauth/session.go:291)


Parses a WWW-Authenticate response header to see if access token has expired (needs refresh)


```go
func isExpiredAccessTokenHeader((hdr string)) (hdr string)
```


**Тип ответа:** hdr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/session.go:291`



---


[function] name: isNonceUpdateHeader file: atproto/auth/oauth/session.go:284 returns_error: нет description: Parses a WWW-Authenticate response header to see if DPoP nonce update is indicated


### isNonceUpdateHeader (atproto/auth/oauth/session.go:284)


Parses a WWW-Authenticate response header to see if DPoP nonce update is indicated


```go
func isNonceUpdateHeader((hdr string)) (hdr string)
```


**Тип ответа:** hdr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/session.go:284`



---


[function] name: postToAuthServer file: atproto/auth/oauth/session.go:88 returns_error: да description: Helper method to handle DPoP retries and client assertions (if the client is confidential)
body object will be url-encod


### postToAuthServer (atproto/auth/oauth/session.go:88)


Helper method to handle DPoP retries and client assertions (if the client is confidential)
body object will be url-encoded (expected to be either RefreshTokenRequest or RevocationRequest)
expects sess.lk to be held by caller
if a non-nil *http.Response is returned, the caller is responsible for closing the response body


```go
func (sess *ClientSession) postToAuthServer((*http.Response, error)) (*http.Response, error)
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


📍 *Расположение:* `atproto/auth/oauth/session.go:88`




## atproto/auth/oauth/types.go


📄 Исходный файл: `atproto/auth/oauth/types.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Error](#error-atprotoauthoauthtypesgo446) `:446`

- 🔗 [IsConfidential](#isconfidential-atprotoauthoauthtypesgo84) `:84`

- 🔗 [Validate](#validate-atprotoauthoauthtypesgo92) `:92`

- 🔗 [Validate](#validate-atprotoauthoauthtypesgo205) `:205`


</details>


[function] name: Error file: atproto/auth/oauth/types.go:446 returns_error: нет description: —


### Error (atproto/auth/oauth/types.go:446)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e *AuthRequestCallbackError) Error(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/types.go:446`



---


[function] name: IsConfidential file: atproto/auth/oauth/types.go:84 returns_error: нет description: returns 'true' if client metadata indicates that this is a confidential client


### IsConfidential (atproto/auth/oauth/types.go:84)


returns 'true' if client metadata indicates that this is a confidential client


```go
func (m *ClientMetadata) IsConfidential(()) ()
```


📍 *Расположение:* `atproto/auth/oauth/types.go:84`



---


[function] name: Validate file: atproto/auth/oauth/types.go:92 returns_error: нет description: —


### Validate (atproto/auth/oauth/types.go:92)


Validate is a method that performs operations based on the provided parameters and returns (clientID string).


```go
func (m *ClientMetadata) Validate((clientID string)) (clientID string)
```


**Тип ответа:** clientID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/types.go:92`



---


[function] name: Validate file: atproto/auth/oauth/types.go:205 returns_error: нет description: —


### Validate (atproto/auth/oauth/types.go:205)


Validate is a method that performs operations based on the provided parameters and returns (serverURL string).


```go
func (m *AuthServerMetadata) Validate((serverURL string)) (serverURL string)
```


**Тип ответа:** serverURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/types.go:205`




## atproto/auth/oauth/util.go


📄 Исходный файл: `atproto/auth/oauth/util.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [S256CodeChallenge](#s256codechallenge-atprotoauthoauthutilgo17) `:17`

- 🔗 [secureRandomBase64](#securerandombase64-atprotoauthoauthutilgo10) `:10`

- 🔗 [strPtr](#strptr-atprotoauthoauthutilgo22) `:22`


</details>


[function] name: S256CodeChallenge file: atproto/auth/oauth/util.go:17 returns_error: нет description: Computes an SHA-256 base64url-encoded challenge string, as used for PKCE.


### S256CodeChallenge (atproto/auth/oauth/util.go:17)


Computes an SHA-256 base64url-encoded challenge string, as used for PKCE.


```go
func S256CodeChallenge((raw string)) (raw string)
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


📍 *Расположение:* `atproto/auth/oauth/util.go:17`



---


[function] name: secureRandomBase64 file: atproto/auth/oauth/util.go:10 returns_error: нет description: This is used both for PKCE challenges, and for pseudo-unique nonces to prevent token (JWT) replay.


### secureRandomBase64 (atproto/auth/oauth/util.go:10)


This is used both for PKCE challenges, and for pseudo-unique nonces to prevent token (JWT) replay.


```go
func secureRandomBase64((sizeBytes uint)) (sizeBytes uint)
```


**Тип ответа:** sizeBytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/oauth/util.go:10`



---


[function] name: strPtr file: atproto/auth/oauth/util.go:22 returns_error: нет description: —


### strPtr (atproto/auth/oauth/util.go:22)


strPtr is a function that performs operations based on the provided parameters and returns (raw string).


```go
func strPtr((raw string)) (raw string)
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


📍 *Расположение:* `atproto/auth/oauth/util.go:22`




## atproto/auth/oauthscope.go


📄 Исходный файл: `atproto/auth/oauthscope.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ParseOAuthScope](#parseoauthscope-atprotoauthoauthscopego11) `:11`


</details>


[function] name: ParseOAuthScope file: atproto/auth/oauthscope.go:11 returns_error: да description: High-level helper for parsing a space-delimited OAuth scope string in to a set of permissions.

If the 'atproto' scope i


### ParseOAuthScope (atproto/auth/oauthscope.go:11)


High-level helper for parsing a space-delimited OAuth scope string in to a set of permissions.

If the 'atproto' scope is not included, this will return an error. Otherwise invalid permission scope strings are simply ignored.


```go
func ParseOAuthScope(([]Permission, error)) ([]Permission, error)
```


**Тип ответа:** Permission


```json
{
  "Type": "string",
  "Resource": "string",
  "Accept": [],
  "Action": [],
  "Attribute": "string",
  "Audience": "string",
  "InheritAud": false,
  "Collection": [],
  "Endpoint": [],
  "NSID": "string"
}
```


*Определено в:* `atproto/auth/permission.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]Permission`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/oauthscope.go:11`




## atproto/auth/permission.go


📄 Исходный файл: `atproto/auth/permission.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ParsePermissionString](#parsepermissionstring-atprotoauthpermissiongo103) `:103`

- 🔗 [ScopeString](#scopestring-atprotoauthpermissiongo38) `:38`


</details>


[function] name: ParsePermissionString file: atproto/auth/permission.go:103 returns_error: да description: Parses a permission scope string (as would be found as a component of an OAuth scope string) into a [Permission].

This 


### ParsePermissionString (atproto/auth/permission.go:103)


Parses a permission scope string (as would be found as a component of an OAuth scope string) into a [Permission].

This function is strict: it is case sensitive, verifies field syntax, and will throw an error on unknown parameters/fields. Note that calling code is usually supposed to simply skip any permission which cause such errors, not reject entire requests.


```go
func ParsePermissionString((*Permission, error)) (*Permission, error)
```


**Тип запроса:** Permission


```json
{
  "Type": "string",
  "Resource": "string",
  "Accept": [],
  "Action": [],
  "Attribute": "string",
  "Audience": "string",
  "InheritAud": false,
  "Collection": [],
  "Endpoint": [],
  "NSID": "string"
}
```


*Определено в:* `atproto/auth/permission.go`


**Тип ответа:** Permission


```json
{
  "Type": "string",
  "Resource": "string",
  "Accept": [],
  "Action": [],
  "Attribute": "string",
  "Audience": "string",
  "InheritAud": false,
  "Collection": [],
  "Endpoint": [],
  "NSID": "string"
}
```


*Определено в:* `atproto/auth/permission.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Permission`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/permission.go:103`



---


[function] name: ScopeString file: atproto/auth/permission.go:38 returns_error: нет description: Renders a permission as a permission scope string.

If the permission contains information which only makes sense in the


### ScopeString (atproto/auth/permission.go:38)


Renders a permission as a permission scope string.

If the permission contains information which only makes sense in the context of a permission-set (eg, the inheritAud flag), it will be silently dropped.


```go
func (p *Permission) ScopeString(()) ()
```


📍 *Расположение:* `atproto/auth/permission.go:38`




## atproto/auth/permission_util.go


📄 Исходный файл: `atproto/auth/permission_util.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [ParseGenericScope](#parsegenericscope-atprotoauthpermission_utilgo19) `:19`

- 🔗 [ScopeString](#scopestring-atprotoauthpermission_utilgo43) `:43`

- 🔗 [isASCII](#isascii-atprotoauthpermission_utilgo88) `:88`

- 🔗 [validBlobAccept](#validblobaccept-atprotoauthpermission_utilgo55) `:55`

- 🔗 [validServiceRef](#validserviceref-atprotoauthpermission_utilgo73) `:73`


</details>


[function] name: ParseGenericScope file: atproto/auth/permission_util.go:19 returns_error: да description: —


### ParseGenericScope (atproto/auth/permission_util.go:19)


ParseGenericScope is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseGenericScope((*GenericPermission, error)) (*GenericPermission, error)
```


**Тип запроса:** GenericPermission


```json
{
  "Resource": "string",
  "Positional": "string",
  "Params": {}
}
```


*Определено в:* `atproto/auth/permission_util.go`


**Тип ответа:** GenericPermission


```json
{
  "Resource": "string",
  "Positional": "string",
  "Params": {}
}
```


*Определено в:* `atproto/auth/permission_util.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GenericPermission`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/auth/permission_util.go:19`



---


[function] name: ScopeString file: atproto/auth/permission_util.go:43 returns_error: нет description: —


### ScopeString (atproto/auth/permission_util.go:43)


ScopeString is a method that performs operations based on the provided parameters and returns ().


```go
func (p *GenericPermission) ScopeString(()) ()
```


📍 *Расположение:* `atproto/auth/permission_util.go:43`



---


[function] name: isASCII file: atproto/auth/permission_util.go:88 returns_error: нет description: —


### isASCII (atproto/auth/permission_util.go:88)


isASCII is a function that performs operations based on the provided parameters and returns (s string).


```go
func isASCII((s string)) (s string)
```


**Тип ответа:** s


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


📍 *Расположение:* `atproto/auth/permission_util.go:88`



---


[function] name: validBlobAccept file: atproto/auth/permission_util.go:55 returns_error: нет description: TODO: replace with helper in syntax pkg


### validBlobAccept (atproto/auth/permission_util.go:55)


TODO: replace with helper in syntax pkg


```go
func validBlobAccept((accept string)) (accept string)
```


**Тип ответа:** accept


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/permission_util.go:55`



---


[function] name: validServiceRef file: atproto/auth/permission_util.go:73 returns_error: нет description: TODO: replace with helper in syntax pkg


### validServiceRef (atproto/auth/permission_util.go:73)


TODO: replace with helper in syntax pkg


```go
func validServiceRef((accept string)) (accept string)
```


**Тип ответа:** accept


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/auth/permission_util.go:73`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_atdata.md)

- [Следующая директория](atproto_identity.md)


---

