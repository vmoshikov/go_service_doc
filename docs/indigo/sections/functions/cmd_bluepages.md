---
title: "Функции: cmd/bluepages"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/bluepages
---


# Функции: cmd/bluepages


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_beemo.md)

- [Следующая директория](cmd_collectiondir.md)


---


## Меню по файлам


- 📄 [cmd/bluepages/firehose.go](#cmdbluepagesfirehosego)

- 📄 [cmd/bluepages/handlers.go](#cmdbluepageshandlersgo)

- 📄 [cmd/bluepages/main.go](#cmdbluepagesmaingo)

- 📄 [cmd/bluepages/resolver.go](#cmdbluepagesresolvergo)

- 📄 [cmd/bluepages/server.go](#cmdbluepagesservergo)


---


## cmd/bluepages/firehose.go


📄 Исходный файл: `cmd/bluepages/firehose.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [PersistCursor](#persistcursor-cmdbluepagesfirehosego109) `:109`

- 🔗 [ReadLastCursor](#readlastcursor-cmdbluepagesfirehosego91) `:91`

- 🔗 [RunFirehoseConsumer](#runfirehoseconsumer-cmdbluepagesfirehosego23) `:23`

- 🔗 [RunPersistCursor](#runpersistcursor-cmdbluepagesfirehosego123) `:123`


</details>


[function] name: PersistCursor file: cmd/bluepages/firehose.go:109 returns_error: нет description: —


### PersistCursor (cmd/bluepages/firehose.go:109)


PersistCursor is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (srv *Server) PersistCursor((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/bluepages/firehose.go:109`



---


[function] name: ReadLastCursor file: cmd/bluepages/firehose.go:91 returns_error: да description: —


### ReadLastCursor (cmd/bluepages/firehose.go:91)


ReadLastCursor is a method that performs operations based on the provided parameters and may return an error.


```go
func (srv *Server) ReadLastCursor((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/bluepages/firehose.go:91`



---


[function] name: RunFirehoseConsumer file: cmd/bluepages/firehose.go:23 returns_error: нет description: —


### RunFirehoseConsumer (cmd/bluepages/firehose.go:23)


RunFirehoseConsumer is a method that performs operations based on the provided parameters and returns (ctx context.Context, host string, parallelism int).


```go
func (srv *Server) RunFirehoseConsumer((ctx context.Context, host string, parallelism int)) (ctx context.Context, host string, parallelism int)
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


**Тип ответа:** parallelism


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/bluepages/firehose.go:23`



---


[function] name: RunPersistCursor file: cmd/bluepages/firehose.go:123 returns_error: нет description: this method runs in a loop, persisting the current cursor state every 5 seconds


### RunPersistCursor (cmd/bluepages/firehose.go:123)


this method runs in a loop, persisting the current cursor state every 5 seconds


```go
func (srv *Server) RunPersistCursor((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/bluepages/firehose.go:123`




## cmd/bluepages/handlers.go


📄 Исходный файл: `cmd/bluepages/handlers.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [HandleHealthCheck](#handlehealthcheck-cmdbluepageshandlersgo241) `:241`

- 🔗 [RefreshIdentity](#refreshidentity-cmdbluepageshandlersgo198) `:198`

- 🔗 [ResolveDid](#resolvedid-cmdbluepageshandlersgo45) `:45`

- 🔗 [ResolveHandle](#resolvehandle-cmdbluepageshandlersgo16) `:16`

- 🔗 [ResolveIdentity](#resolveidentity-cmdbluepageshandlersgo176) `:176`

- 🔗 [WebHome](#webhome-cmdbluepageshandlersgo245) `:245`

- 🔗 [resolveIdentityFromDID](#resolveidentityfromdid-cmdbluepageshandlersgo132) `:132`

- 🔗 [resolveIdentityFromHandle](#resolveidentityfromhandle-cmdbluepageshandlersgo74) `:74`


</details>


[function] name: HandleHealthCheck file: cmd/bluepages/handlers.go:241 returns_error: нет description: —


### HandleHealthCheck (cmd/bluepages/handlers.go:241)


HandleHealthCheck is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Server) HandleHealthCheck((c echo.Context)) (c echo.Context)
```


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `cmd/bluepages/handlers.go:241`



---


[function] name: RefreshIdentity file: cmd/bluepages/handlers.go:198 returns_error: нет description: POST /xrpc/com.atproto.identity.refreshIdentity


### RefreshIdentity (cmd/bluepages/handlers.go:198)


POST /xrpc/com.atproto.identity.refreshIdentity


```go
func (srv *Server) RefreshIdentity((c echo.Context)) (c echo.Context)
```


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `cmd/bluepages/handlers.go:198`



---


[function] name: ResolveDid file: cmd/bluepages/handlers.go:45 returns_error: нет description: GET /xrpc/com.atproto.identity.resolveDid


### ResolveDid (cmd/bluepages/handlers.go:45)


GET /xrpc/com.atproto.identity.resolveDid


```go
func (srv *Server) ResolveDid((c echo.Context)) (c echo.Context)
```


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `cmd/bluepages/handlers.go:45`



---


[function] name: ResolveHandle file: cmd/bluepages/handlers.go:16 returns_error: нет description: GET /xrpc/com.atproto.identity.resolveHandle


### ResolveHandle (cmd/bluepages/handlers.go:16)


GET /xrpc/com.atproto.identity.resolveHandle


```go
func (srv *Server) ResolveHandle((c echo.Context)) (c echo.Context)
```


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `cmd/bluepages/handlers.go:16`



---


[function] name: ResolveIdentity file: cmd/bluepages/handlers.go:176 returns_error: нет description: GET /xrpc/com.atproto.identity.resolveIdentity


### ResolveIdentity (cmd/bluepages/handlers.go:176)


GET /xrpc/com.atproto.identity.resolveIdentity


```go
func (srv *Server) ResolveIdentity((c echo.Context)) (c echo.Context)
```


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `cmd/bluepages/handlers.go:176`



---


[function] name: WebHome file: cmd/bluepages/handlers.go:245 returns_error: нет description: —


### WebHome (cmd/bluepages/handlers.go:245)


WebHome is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (srv *Server) WebHome((c echo.Context)) (c echo.Context)
```


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `cmd/bluepages/handlers.go:245`



---


[function] name: resolveIdentityFromDID file: cmd/bluepages/handlers.go:132 returns_error: нет description: helper for resolveIdentity


### resolveIdentityFromDID (cmd/bluepages/handlers.go:132)


helper for resolveIdentity


```go
func (srv *Server) resolveIdentityFromDID((c echo.Context, did syntax.DID)) (c echo.Context, did syntax.DID)
```


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


**Тип ответа:** echo.Context


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


📍 *Расположение:* `cmd/bluepages/handlers.go:132`



---


[function] name: resolveIdentityFromHandle file: cmd/bluepages/handlers.go:74 returns_error: нет description: helper for resolveIdentity


### resolveIdentityFromHandle (cmd/bluepages/handlers.go:74)


helper for resolveIdentity


```go
func (srv *Server) resolveIdentityFromHandle((c echo.Context, handle syntax.Handle)) (c echo.Context, handle syntax.Handle)
```


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


**Тип ответа:** echo.Context


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


**Тип ответа:** handle


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** syntax.Handle


```json
{
  "Handle": "string",
  "Valid": {}
}
```


*Определено в:* `cmd/gosky/main.go`


📍 *Расположение:* `cmd/bluepages/handlers.go:74`




## cmd/bluepages/main.go


📄 Исходный файл: `cmd/bluepages/main.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [configClient](#configclient-cmdbluepagesmaingo194) `:194`

- 🔗 [configLogger](#configlogger-cmdbluepagesmaingo168) `:168`

- 🔗 [main](#main-cmdbluepagesmaingo25) `:25`

- 🔗 [run](#run-cmdbluepagesmaingo32) `:32`

- 🔗 [runLookupCmd](#runlookupcmd-cmdbluepagesmaingo290) `:290`

- 🔗 [runRefreshCmd](#runrefreshcmd-cmdbluepagesmaingo315) `:315`

- 🔗 [runResolveDIDCmd](#runresolvedidcmd-cmdbluepagesmaingo266) `:266`

- 🔗 [runResolveHandleCmd](#runresolvehandlecmd-cmdbluepagesmaingo246) `:246`

- 🔗 [runServeCmd](#runservecmd-cmdbluepagesmaingo198) `:198`


</details>


[function] name: configClient file: cmd/bluepages/main.go:194 returns_error: нет description: —


### configClient (cmd/bluepages/main.go:194)


configClient is a function that performs operations based on the provided parameters and returns (cmd *cli.Command).


```go
func configClient((cmd *cli.Command)) (cmd *cli.Command)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/bluepages/main.go:194`



---


[function] name: configLogger file: cmd/bluepages/main.go:168 returns_error: нет description: —


### configLogger (cmd/bluepages/main.go:168)


configLogger is a function that performs operations based on the provided parameters and returns (cmd *cli.Command, writer io.Writer).


```go
func configLogger((cmd *cli.Command, writer io.Writer)) (cmd *cli.Command, writer io.Writer)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/bluepages/main.go:168`



---


[function] name: main file: cmd/bluepages/main.go:25 returns_error: нет description: —


### main (cmd/bluepages/main.go:25)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/bluepages/main.go:25`



---


[function] name: run file: cmd/bluepages/main.go:32 returns_error: нет description: —


### run (cmd/bluepages/main.go:32)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/bluepages/main.go:32`



---


[function] name: runLookupCmd file: cmd/bluepages/main.go:290 returns_error: нет description: —


### runLookupCmd (cmd/bluepages/main.go:290)


runLookupCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runLookupCmd((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/bluepages/main.go:290`



---


[function] name: runRefreshCmd file: cmd/bluepages/main.go:315 returns_error: нет description: —


### runRefreshCmd (cmd/bluepages/main.go:315)


runRefreshCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runRefreshCmd((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/bluepages/main.go:315`



---


[function] name: runResolveDIDCmd file: cmd/bluepages/main.go:266 returns_error: нет description: —


### runResolveDIDCmd (cmd/bluepages/main.go:266)


runResolveDIDCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runResolveDIDCmd((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/bluepages/main.go:266`



---


[function] name: runResolveHandleCmd file: cmd/bluepages/main.go:246 returns_error: нет description: —


### runResolveHandleCmd (cmd/bluepages/main.go:246)


runResolveHandleCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runResolveHandleCmd((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/bluepages/main.go:246`



---


[function] name: runServeCmd file: cmd/bluepages/main.go:198 returns_error: нет description: —


### runServeCmd (cmd/bluepages/main.go:198)


runServeCmd is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runServeCmd((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/bluepages/main.go:198`




## cmd/bluepages/resolver.go


📄 Исходный файл: `cmd/bluepages/resolver.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [NewRedisResolver](#newredisresolver-cmdbluepagesresolvergo59) `:59`

- 🔗 [PurgeDID](#purgedid-cmdbluepagesresolvergo313) `:313`

- 🔗 [PurgeHandle](#purgehandle-cmdbluepagesresolvergo304) `:304`

- 🔗 [ResolveDID](#resolvedid-cmdbluepagesresolvergo288) `:288`

- 🔗 [ResolveDIDRaw](#resolvedidraw-cmdbluepagesresolvergo238) `:238`

- 🔗 [ResolveHandle](#resolvehandle-cmdbluepagesresolvergo172) `:172`

- 🔗 [isDIDStale](#isdidstale-cmdbluepagesresolvergo95) `:95`

- 🔗 [isHandleStale](#ishandlestale-cmdbluepagesresolvergo88) `:88`

- 🔗 [refreshDID](#refreshdid-cmdbluepagesresolvergo136) `:136`

- 🔗 [refreshHandle](#refreshhandle-cmdbluepagesresolvergo102) `:102`


</details>


[function] name: NewRedisResolver file: cmd/bluepages/resolver.go:59 returns_error: да description: Creates a new caching `identity.Resolver` wrapper around an existing directory, using Redis and in-process LRU for cachi


### NewRedisResolver (cmd/bluepages/resolver.go:59)


Creates a new caching `identity.Resolver` wrapper around an existing directory, using Redis and in-process LRU for caching.

`redisURL` contains all the redis connection config options.
`hitTTL` and `errTTL` define how long successful and errored identity metadata should be cached (respectively). errTTL is expected to be shorted than hitTTL.
`lruSize` is the size of the in-process cache, for each of the handle and identity caches. 10000 is a reasonable default.

NOTE: Errors returned may be inconsistent with the base directory, or between calls. This is because cached errors are serialized/deserialized and that may break equality checks.


```go
func NewRedisResolver((*RedisResolver, error)) (*RedisResolver, error)
```


**Тип запроса:** RedisResolver


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


**Тип ответа:** RedisResolver


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RedisResolver`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/bluepages/resolver.go:59`



---


[function] name: PurgeDID file: cmd/bluepages/resolver.go:313 returns_error: нет description: —


### PurgeDID (cmd/bluepages/resolver.go:313)


PurgeDID is a method that performs operations based on the provided parameters and returns (ctx context.Context, did syntax.DID).


```go
func (d *RedisResolver) PurgeDID((ctx context.Context, did syntax.DID)) (ctx context.Context, did syntax.DID)
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


📍 *Расположение:* `cmd/bluepages/resolver.go:313`



---


[function] name: PurgeHandle file: cmd/bluepages/resolver.go:304 returns_error: нет description: —


### PurgeHandle (cmd/bluepages/resolver.go:304)


PurgeHandle is a method that performs operations based on the provided parameters and returns (ctx context.Context, handle syntax.Handle).


```go
func (d *RedisResolver) PurgeHandle((ctx context.Context, handle syntax.Handle)) (ctx context.Context, handle syntax.Handle)
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


**Тип ответа:** handle


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** syntax.Handle


```json
{
  "Handle": "string",
  "Valid": {}
}
```


*Определено в:* `cmd/gosky/main.go`


📍 *Расположение:* `cmd/bluepages/resolver.go:304`



---


[function] name: ResolveDID file: cmd/bluepages/resolver.go:288 returns_error: да description: —


### ResolveDID (cmd/bluepages/resolver.go:288)


ResolveDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisResolver) ResolveDID((*identity.DIDDocument, error)) (*identity.DIDDocument, error)
```


**Тип запроса:** identity.DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Тип ответа:** identity.DIDDocument


```json
{
  "DID": {},
  "AlsoKnownAs": [],
  "VerificationMethod": [],
  "Service": []
}
```


*Определено в:* `atproto/identity/diddoc.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*identity.DIDDocument`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/bluepages/resolver.go:288`



---


[function] name: ResolveDIDRaw file: cmd/bluepages/resolver.go:238 returns_error: да description: —


### ResolveDIDRaw (cmd/bluepages/resolver.go:238)


ResolveDIDRaw is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisResolver) ResolveDIDRaw((json.RawMessage, error)) (json.RawMessage, error)
```


**Тип ответа:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `json.RawMessage`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/bluepages/resolver.go:238`



---


[function] name: ResolveHandle file: cmd/bluepages/resolver.go:172 returns_error: да description: —


### ResolveHandle (cmd/bluepages/resolver.go:172)


ResolveHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (d *RedisResolver) ResolveHandle((syntax.DID, error)) (syntax.DID, error)
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


📍 *Расположение:* `cmd/bluepages/resolver.go:172`



---


[function] name: isDIDStale file: cmd/bluepages/resolver.go:95 returns_error: нет description: —


### isDIDStale (cmd/bluepages/resolver.go:95)


isDIDStale is a method that performs operations based on the provided parameters and returns (e *didEntry).


```go
func (d *RedisResolver) isDIDStale((e *didEntry)) (e *didEntry)
```


**Тип запроса:** didEntry


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** didEntry


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `cmd/bluepages/resolver.go:95`



---


[function] name: isHandleStale file: cmd/bluepages/resolver.go:88 returns_error: нет description: —


### isHandleStale (cmd/bluepages/resolver.go:88)


isHandleStale is a method that performs operations based on the provided parameters and returns (e *handleEntry).


```go
func (d *RedisResolver) isHandleStale((e *handleEntry)) (e *handleEntry)
```


**Тип запроса:** handleEntry


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** e


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** handleEntry


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


📍 *Расположение:* `cmd/bluepages/resolver.go:88`



---


[function] name: refreshDID file: cmd/bluepages/resolver.go:136 returns_error: нет description: —


### refreshDID (cmd/bluepages/resolver.go:136)


refreshDID is a method that performs operations based on the provided parameters and returns (ctx context.Context, did syntax.DID).


```go
func (d *RedisResolver) refreshDID((ctx context.Context, did syntax.DID)) (ctx context.Context, did syntax.DID)
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


📍 *Расположение:* `cmd/bluepages/resolver.go:136`



---


[function] name: refreshHandle file: cmd/bluepages/resolver.go:102 returns_error: нет description: —


### refreshHandle (cmd/bluepages/resolver.go:102)


refreshHandle is a method that performs operations based on the provided parameters and returns (ctx context.Context, h syntax.Handle).


```go
func (d *RedisResolver) refreshHandle((ctx context.Context, h syntax.Handle)) (ctx context.Context, h syntax.Handle)
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


**Тип ответа:** h


```json
{
  "Updated": {},
  "DID": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** syntax.Handle


```json
{
  "Handle": "string",
  "Valid": {}
}
```


*Определено в:* `cmd/gosky/main.go`


📍 *Расположение:* `cmd/bluepages/resolver.go:102`




## cmd/bluepages/server.go


📄 Исходный файл: `cmd/bluepages/server.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [NewServer](#newserver-cmdbluepagesservergo50) `:50`

- 🔗 [RunAPI](#runapi-cmdbluepagesservergo153) `:153`

- 🔗 [RunMetrics](#runmetrics-cmdbluepagesservergo185) `:185`

- 🔗 [ServeHTTP](#servehttp-cmdbluepagesservergo149) `:149`

- 🔗 [Shutdown](#shutdown-cmdbluepagesservergo192) `:192`

- 🔗 [errorHandler](#errorhandler-cmdbluepagesservergo206) `:206`


</details>


[function] name: NewServer file: cmd/bluepages/server.go:50 returns_error: да description: —


### NewServer (cmd/bluepages/server.go:50)


NewServer is a function that performs operations based on the provided parameters and may return an error.


```go
func NewServer((*Server, error)) (*Server, error)
```


**Тип запроса:** Server


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


**Тип ответа:** Server


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Server`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/bluepages/server.go:50`



---


[function] name: RunAPI file: cmd/bluepages/server.go:153 returns_error: нет description: —


### RunAPI (cmd/bluepages/server.go:153)


RunAPI is a method that performs operations based on the provided parameters and returns ().


```go
func (srv *Server) RunAPI(()) ()
```


📍 *Расположение:* `cmd/bluepages/server.go:153`



---


[function] name: RunMetrics file: cmd/bluepages/server.go:185 returns_error: нет description: —


### RunMetrics (cmd/bluepages/server.go:185)


RunMetrics is a method that performs operations based on the provided parameters and returns (bind string).


```go
func (srv *Server) RunMetrics((bind string)) (bind string)
```


**Тип ответа:** bind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/bluepages/server.go:185`



---


[function] name: ServeHTTP file: cmd/bluepages/server.go:149 returns_error: нет description: —


### ServeHTTP (cmd/bluepages/server.go:149)


ServeHTTP is a method that performs operations based on the provided parameters and returns (rw http.ResponseWriter, req *http.Request).


```go
func (srv *Server) ServeHTTP((rw http.ResponseWriter, req *http.Request)) (rw http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** rw


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.ResponseWriter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** req


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


📍 *Расположение:* `cmd/bluepages/server.go:149`



---


[function] name: Shutdown file: cmd/bluepages/server.go:192 returns_error: нет description: —


### Shutdown (cmd/bluepages/server.go:192)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (srv *Server) Shutdown(()) ()
```


📍 *Расположение:* `cmd/bluepages/server.go:192`



---


[function] name: errorHandler file: cmd/bluepages/server.go:206 returns_error: да description: —


### errorHandler (cmd/bluepages/server.go:206)


errorHandler is a method that performs operations based on the provided parameters and may return an error.


```go
func (srv *Server) errorHandler((err error, c echo.Context)) (err error, c echo.Context)
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


**Тип ответа:** echo.Context


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`, `c echo.Context`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/bluepages/server.go:206`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_beemo.md)

- [Следующая директория](cmd_collectiondir.md)


---

