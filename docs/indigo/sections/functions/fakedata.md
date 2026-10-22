---
title: "Функции: fakedata"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: fakedata
---


# Функции: fakedata


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_yolopersist.md)

- [Следующая директория](gen.md)


---


## Меню по файлам


- 📄 [fakedata/accounts.go](#fakedataaccountsgo)

- 📄 [fakedata/generators.go](#fakedatageneratorsgo)


---


## fakedata/accounts.go


📄 Исходный файл: `fakedata/accounts.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AccountXrpcClient](#accountxrpcclient-fakedataaccountsgo75) `:75`

- 🔗 [Combined](#combined-fakedataaccountsgo21) `:21`

- 🔗 [ReadAccountCatalog](#readaccountcatalog-fakedataaccountsgo37) `:37`


</details>


[function] name: AccountXrpcClient file: fakedata/accounts.go:75 returns_error: да description: —


### AccountXrpcClient (fakedata/accounts.go:75)


AccountXrpcClient is a function that performs operations based on the provided parameters and may return an error.


```go
func AccountXrpcClient((*xrpc.Client, error)) (*xrpc.Client, error)
```


**Тип запроса:** xrpc.Client


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


**Тип ответа:** xrpc.Client


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*xrpc.Client`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `fakedata/accounts.go:75`



---


[function] name: Combined file: fakedata/accounts.go:21 returns_error: нет description: —


### Combined (fakedata/accounts.go:21)


Combined is a method that performs operations based on the provided parameters and returns ().


```go
func (ac *AccountCatalog) Combined(()) ()
```


📍 *Расположение:* `fakedata/accounts.go:21`



---


[function] name: ReadAccountCatalog file: fakedata/accounts.go:37 returns_error: да description: —


### ReadAccountCatalog (fakedata/accounts.go:37)


ReadAccountCatalog is a function that performs operations based on the provided parameters and may return an error.


```go
func ReadAccountCatalog((*AccountCatalog, error)) (*AccountCatalog, error)
```


**Тип запроса:** AccountCatalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** AccountCatalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AccountCatalog`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `fakedata/accounts.go:37`




## fakedata/generators.go


📄 Исходный файл: `fakedata/generators.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [BrowseAccount](#browseaccount-fakedatageneratorsgo390) `:390`

- 🔗 [CreateFollow](#createfollow-fakedatageneratorsgo217) `:217`

- 🔗 [CreateLike](#createlike-fakedatageneratorsgo230) `:230`

- 🔗 [CreateReply](#createreply-fakedatageneratorsgo264) `:264`

- 🔗 [CreateRepost](#createrepost-fakedatageneratorsgo248) `:248`

- 🔗 [GenAccount](#genaccount-fakedatageneratorsgo39) `:39`

- 🔗 [GenFollowsAndMutes](#genfollowsandmutes-fakedatageneratorsgo296) `:296`

- 🔗 [GenLikesRepostsReplies](#genlikesrepostsreplies-fakedatageneratorsgo354) `:354`

- 🔗 [GenPosts](#genposts-fakedatageneratorsgo132) `:132`

- 🔗 [GenProfile](#genprofile-fakedatageneratorsgo81) `:81`

- 🔗 [MeasureIterations](#measureiterations-fakedatageneratorsgo28) `:28`

- 🔗 [SetLogger](#setlogger-fakedatageneratorsgo24) `:24`


</details>


[function] name: BrowseAccount file: fakedata/generators.go:390 returns_error: нет description: —


### BrowseAccount (fakedata/generators.go:390)


BrowseAccount is a function that performs operations based on the provided parameters and returns (xrpcc *xrpc.Client, acc *AccountContext).


```go
func BrowseAccount((xrpcc *xrpc.Client, acc *AccountContext)) (xrpcc *xrpc.Client, acc *AccountContext)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** acc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


📍 *Расположение:* `fakedata/generators.go:390`



---


[function] name: CreateFollow file: fakedata/generators.go:217 returns_error: нет description: —


### CreateFollow (fakedata/generators.go:217)


CreateFollow is a function that creates new data based on the provided parameters and returns (xrpcc *xrpc.Client, tgt *AccountContext).


```go
func CreateFollow((xrpcc *xrpc.Client, tgt *AccountContext)) (xrpcc *xrpc.Client, tgt *AccountContext)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** tgt


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


📍 *Расположение:* `fakedata/generators.go:217`



---


[function] name: CreateLike file: fakedata/generators.go:230 returns_error: нет description: —


### CreateLike (fakedata/generators.go:230)


CreateLike is a function that creates new data based on the provided parameters and returns (xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost).


```go
func CreateLike((xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost)) (xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** appbsky.FeedDefs_FeedViewPost


```json
{
  "feedContext": "string",
  "post": null,
  "reason": null,
  "reply": null,
  "reqId": "string"
}
```


*Определено в:* `api/bsky/feeddefs.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** viewPost


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.FeedDefs_FeedViewPost


```json
{
  "feedContext": "string",
  "post": null,
  "reason": null,
  "reply": null,
  "reqId": "string"
}
```


*Определено в:* `api/bsky/feeddefs.go`


📍 *Расположение:* `fakedata/generators.go:230`



---


[function] name: CreateReply file: fakedata/generators.go:264 returns_error: нет description: —


### CreateReply (fakedata/generators.go:264)


CreateReply is a function that creates new data based on the provided parameters and returns (xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost).


```go
func CreateReply((xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost)) (xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** appbsky.FeedDefs_FeedViewPost


```json
{
  "feedContext": "string",
  "post": null,
  "reason": null,
  "reply": null,
  "reqId": "string"
}
```


*Определено в:* `api/bsky/feeddefs.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** viewPost


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.FeedDefs_FeedViewPost


```json
{
  "feedContext": "string",
  "post": null,
  "reason": null,
  "reply": null,
  "reqId": "string"
}
```


*Определено в:* `api/bsky/feeddefs.go`


📍 *Расположение:* `fakedata/generators.go:264`



---


[function] name: CreateRepost file: fakedata/generators.go:248 returns_error: нет description: —


### CreateRepost (fakedata/generators.go:248)


CreateRepost is a function that creates new data based on the provided parameters and returns (xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost).


```go
func CreateRepost((xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost)) (xrpcc *xrpc.Client, viewPost *appbsky.FeedDefs_FeedViewPost)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** appbsky.FeedDefs_FeedViewPost


```json
{
  "feedContext": "string",
  "post": null,
  "reason": null,
  "reply": null,
  "reqId": "string"
}
```


*Определено в:* `api/bsky/feeddefs.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** viewPost


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.FeedDefs_FeedViewPost


```json
{
  "feedContext": "string",
  "post": null,
  "reason": null,
  "reply": null,
  "reqId": "string"
}
```


*Определено в:* `api/bsky/feeddefs.go`


📍 *Расположение:* `fakedata/generators.go:248`



---


[function] name: GenAccount file: fakedata/generators.go:39 returns_error: да description: —


### GenAccount (fakedata/generators.go:39)


GenAccount is a function that performs operations based on the provided parameters and may return an error.


```go
func GenAccount((*AccountContext, error)) (*AccountContext, error)
```


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AccountContext`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `fakedata/generators.go:39`



---


[function] name: GenFollowsAndMutes file: fakedata/generators.go:296 returns_error: нет description: —


### GenFollowsAndMutes (fakedata/generators.go:296)


GenFollowsAndMutes is a function that performs operations based on the provided parameters and returns (xrpcc *xrpc.Client, catalog *AccountCatalog, acc *AccountContext, maxFollows int, maxMutes int).


```go
func GenFollowsAndMutes((xrpcc *xrpc.Client, catalog *AccountCatalog, acc *AccountContext, maxFollows int, maxMutes int)) (xrpcc *xrpc.Client, catalog *AccountCatalog, acc *AccountContext, maxFollows int, maxMutes int)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** AccountCatalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** catalog


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountCatalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** acc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** maxFollows


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxMutes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `fakedata/generators.go:296`



---


[function] name: GenLikesRepostsReplies file: fakedata/generators.go:354 returns_error: нет description: —


### GenLikesRepostsReplies (fakedata/generators.go:354)


GenLikesRepostsReplies is a function that performs operations based on the provided parameters and returns (xrpcc *xrpc.Client, acc *AccountContext, fracLike, fracRepost, fracReply float64).


```go
func GenLikesRepostsReplies((xrpcc *xrpc.Client, acc *AccountContext, fracLike, fracRepost, fracReply float64)) (xrpcc *xrpc.Client, acc *AccountContext, fracLike, fracRepost, fracReply float64)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** acc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** fracLike


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fracRepost


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fracReply


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `fakedata/generators.go:354`



---


[function] name: GenPosts file: fakedata/generators.go:132 returns_error: нет description: —


### GenPosts (fakedata/generators.go:132)


GenPosts is a function that performs operations based on the provided parameters and returns (xrpcc *xrpc.Client, catalog *AccountCatalog, acc *AccountContext, maxPosts int, fracImage float64, fracMention float64).


```go
func GenPosts((xrpcc *xrpc.Client, catalog *AccountCatalog, acc *AccountContext, maxPosts int, fracImage float64, fracMention float64)) (xrpcc *xrpc.Client, catalog *AccountCatalog, acc *AccountContext, maxPosts int, fracImage float64, fracMention float64)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** AccountCatalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** catalog


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountCatalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** acc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** maxPosts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fracImage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fracMention


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `fakedata/generators.go:132`



---


[function] name: GenProfile file: fakedata/generators.go:81 returns_error: нет description: —


### GenProfile (fakedata/generators.go:81)


GenProfile is a function that performs operations based on the provided parameters and returns (xrpcc *xrpc.Client, acc *AccountContext, genAvatar, genBanner bool).


```go
func GenProfile((xrpcc *xrpc.Client, acc *AccountContext, genAvatar, genBanner bool)) (xrpcc *xrpc.Client, acc *AccountContext, genAvatar, genBanner bool)
```


**Тип запроса:** xrpc.Client


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


**Тип запроса:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** xrpcc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** xrpc.Client


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


**Тип ответа:** acc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** genAvatar


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** genBanner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `fakedata/generators.go:81`



---


[function] name: MeasureIterations file: fakedata/generators.go:28 returns_error: нет description: —


### MeasureIterations (fakedata/generators.go:28)


MeasureIterations is a function that performs operations based on the provided parameters and returns (name string).


```go
func MeasureIterations((name string)) (name string)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `fakedata/generators.go:28`



---


[function] name: SetLogger file: fakedata/generators.go:24 returns_error: нет description: —


### SetLogger (fakedata/generators.go:24)


SetLogger is a function that updates data based on the provided parameters and returns (logger *slog.Logger).


```go
func SetLogger((logger *slog.Logger)) (logger *slog.Logger)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `fakedata/generators.go:24`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_yolopersist.md)

- [Следующая директория](gen.md)


---

