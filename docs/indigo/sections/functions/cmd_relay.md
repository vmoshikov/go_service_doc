---
title: "Функции: cmd/relay"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/relay
---


# Функции: cmd/relay


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_rainbow.md)

- [Следующая директория](cmd_sonar.md)


---


## Меню по файлам


- 📄 [cmd/relay/forward.go](#cmdrelayforwardgo)

- 📄 [cmd/relay/handlers.go](#cmdrelayhandlersgo)

- 📄 [cmd/relay/handlers_admin.go](#cmdrelayhandlers_admingo)

- 📄 [cmd/relay/main.go](#cmdrelaymaingo)

- 📄 [cmd/relay/otel.go](#cmdrelayotelgo)

- 📄 [cmd/relay/pull.go](#cmdrelaypullgo)

- 📄 [cmd/relay/relay/account.go](#cmdrelayrelayaccountgo)

- 📄 [cmd/relay/relay/broadcast.go](#cmdrelayrelaybroadcastgo)

- 📄 [cmd/relay/relay/crawl.go](#cmdrelayrelaycrawlgo)

- 📄 [cmd/relay/relay/domain_ban.go](#cmdrelayrelaydomain_bango)

- 📄 [cmd/relay/relay/host.go](#cmdrelayrelayhostgo)

- 📄 [cmd/relay/relay/host_checker.go](#cmdrelayrelayhost_checkergo)

- 📄 [cmd/relay/relay/ingest.go](#cmdrelayrelayingestgo)

- 📄 [cmd/relay/relay/models/joins.go](#cmdrelayrelaymodelsjoinsgo)

- 📄 [cmd/relay/relay/models/methods.go](#cmdrelayrelaymodelsmethodsgo)

- 📄 [cmd/relay/relay/models/models.go](#cmdrelayrelaymodelsmodelsgo)

- 📄 [cmd/relay/relay/relay.go](#cmdrelayrelayrelaygo)

- 📄 [cmd/relay/relay/slurper.go](#cmdrelayrelayslurpergo)

- 📄 [cmd/relay/relay/util.go](#cmdrelayrelayutilgo)

- 📄 [cmd/relay/relay/verify.go](#cmdrelayrelayverifygo)

- 📄 [cmd/relay/service.go](#cmdrelayservicego)

- 📄 [cmd/relay/stream/cbor_gen.go](#cmdrelaystreamcbor_gengo)

- 📄 [cmd/relay/stream/consumer.go](#cmdrelaystreamconsumergo)

- 📄 [cmd/relay/stream/eventmgr/event_manager.go](#cmdrelaystreameventmgrevent_managergo)

- 📄 [cmd/relay/stream/events.go](#cmdrelaystreameventsgo)

- 📄 [cmd/relay/stream/persist/diskpersist/diskpersist.go](#cmdrelaystreampersistdiskpersistdiskpersistgo)

- 📄 [cmd/relay/stream/schedulers/parallel/parallel.go](#cmdrelaystreamschedulersparallelparallelgo)

- 📄 [cmd/relay/stream/schedulers/sequential/sequential.go](#cmdrelaystreamschedulerssequentialsequentialgo)

- 📄 [cmd/relay/stubs.go](#cmdrelaystubsgo)

- 📄 [cmd/relay/testing/consumer.go](#cmdrelaytestingconsumergo)

- 📄 [cmd/relay/testing/producer.go](#cmdrelaytestingproducergo)

- 📄 [cmd/relay/testing/runner.go](#cmdrelaytestingrunnergo)

- 📄 [cmd/relay/testing/scenario.go](#cmdrelaytestingscenariogo)


---


## cmd/relay/forward.go


📄 Исходный файл: `cmd/relay/forward.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ForwardSiblingRequest](#forwardsiblingrequest-cmdrelayforwardgo17) `:17`


</details>


[function] name: ForwardSiblingRequest file: cmd/relay/forward.go:17 returns_error: нет description: Forwards HTTP request on to sibling relay instances, if they are configured.

This method expects to be run "in the back


### ForwardSiblingRequest (cmd/relay/forward.go:17)


Forwards HTTP request on to sibling relay instances, if they are configured.

This method expects to be run "in the background" as a goroutine, so it doesn't take a `context.Context`, and does not return an `error`. It logs both success and failure. The `echo.Context` request has presumably been read, so any body is passed separately. The `echo.Context` response is presumably being returned or already finalized concurrently.


```go
func (s *Service) ForwardSiblingRequest((c echo.Context, body []byte)) (c echo.Context, body []byte)
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


**Тип ответа:** body


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/forward.go:17`




## cmd/relay/handlers.go


📄 Исходный файл: `cmd/relay/handlers.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [HandleHealthCheck](#handlehealthcheck-cmdrelayhandlersgo245) `:245`

- 🔗 [HandleHomeMessage](#handlehomemessage-cmdrelayhandlersgo269) `:269`

- 🔗 [handleComAtprotoSyncGetHostStatus](#handlecomatprotosyncgethoststatus-cmdrelayhandlersgo108) `:108`

- 🔗 [handleComAtprotoSyncGetLatestCommit](#handlecomatprotosyncgetlatestcommit-cmdrelayhandlersgo201) `:201`

- 🔗 [handleComAtprotoSyncGetRepoStatus](#handlecomatprotosyncgetrepostatus-cmdrelayhandlersgo170) `:170`

- 🔗 [handleComAtprotoSyncListHosts](#handlecomatprotosynclisthosts-cmdrelayhandlersgo71) `:71`

- 🔗 [handleComAtprotoSyncListRepos](#handlecomatprotosynclistrepos-cmdrelayhandlersgo130) `:130`

- 🔗 [handleComAtprotoSyncRequestCrawl](#handlecomatprotosyncrequestcrawl-cmdrelayhandlersgo19) `:19`


</details>


[function] name: HandleHealthCheck file: cmd/relay/handlers.go:245 returns_error: нет description: —


### HandleHealthCheck (cmd/relay/handlers.go:245)


HandleHealthCheck is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (svc *Service) HandleHealthCheck((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers.go:245`



---


[function] name: HandleHomeMessage file: cmd/relay/handlers.go:269 returns_error: нет description: —


### HandleHomeMessage (cmd/relay/handlers.go:269)


HandleHomeMessage is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (svc *Service) HandleHomeMessage((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers.go:269`



---


[function] name: handleComAtprotoSyncGetHostStatus file: cmd/relay/handlers.go:108 returns_error: да description: —


### handleComAtprotoSyncGetHostStatus (cmd/relay/handlers.go:108)


handleComAtprotoSyncGetHostStatus is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Service) handleComAtprotoSyncGetHostStatus((*comatproto.SyncGetHostStatus_Output, error)) (*comatproto.SyncGetHostStatus_Output, error)
```


**Тип запроса:** comatproto.SyncGetHostStatus_Output


```json
{
  "accountCount": 0,
  "hostname": "string",
  "seq": 0,
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetHostStatus.go`


**Тип ответа:** comatproto.SyncGetHostStatus_Output


```json
{
  "accountCount": 0,
  "hostname": "string",
  "seq": 0,
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetHostStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*comatproto.SyncGetHostStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/handlers.go:108`



---


[function] name: handleComAtprotoSyncGetLatestCommit file: cmd/relay/handlers.go:201 returns_error: да description: —


### handleComAtprotoSyncGetLatestCommit (cmd/relay/handlers.go:201)


handleComAtprotoSyncGetLatestCommit is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Service) handleComAtprotoSyncGetLatestCommit((*comatproto.SyncGetLatestCommit_Output, error)) (*comatproto.SyncGetLatestCommit_Output, error)
```


**Тип запроса:** comatproto.SyncGetLatestCommit_Output


```json
{
  "cid": "string",
  "rev": "string"
}
```


*Определено в:* `api/atproto/syncgetLatestCommit.go`


**Тип ответа:** comatproto.SyncGetLatestCommit_Output


```json
{
  "cid": "string",
  "rev": "string"
}
```


*Определено в:* `api/atproto/syncgetLatestCommit.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*comatproto.SyncGetLatestCommit_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/handlers.go:201`



---


[function] name: handleComAtprotoSyncGetRepoStatus file: cmd/relay/handlers.go:170 returns_error: да description: —


### handleComAtprotoSyncGetRepoStatus (cmd/relay/handlers.go:170)


handleComAtprotoSyncGetRepoStatus is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Service) handleComAtprotoSyncGetRepoStatus((*comatproto.SyncGetRepoStatus_Output, error)) (*comatproto.SyncGetRepoStatus_Output, error)
```


**Тип запроса:** comatproto.SyncGetRepoStatus_Output


```json
{
  "active": false,
  "did": "string",
  "rev": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetRepoStatus.go`


**Тип ответа:** comatproto.SyncGetRepoStatus_Output


```json
{
  "active": false,
  "did": "string",
  "rev": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetRepoStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*comatproto.SyncGetRepoStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/handlers.go:170`



---


[function] name: handleComAtprotoSyncListHosts file: cmd/relay/handlers.go:71 returns_error: да description: —


### handleComAtprotoSyncListHosts (cmd/relay/handlers.go:71)


handleComAtprotoSyncListHosts is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Service) handleComAtprotoSyncListHosts((*comatproto.SyncListHosts_Output, error)) (*comatproto.SyncListHosts_Output, error)
```


**Тип запроса:** comatproto.SyncListHosts_Output


```json
{
  "cursor": "string",
  "hosts": []
}
```


*Определено в:* `api/atproto/synclistHosts.go`


**Тип ответа:** comatproto.SyncListHosts_Output


```json
{
  "cursor": "string",
  "hosts": []
}
```


*Определено в:* `api/atproto/synclistHosts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*comatproto.SyncListHosts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/handlers.go:71`



---


[function] name: handleComAtprotoSyncListRepos file: cmd/relay/handlers.go:130 returns_error: да description: —


### handleComAtprotoSyncListRepos (cmd/relay/handlers.go:130)


handleComAtprotoSyncListRepos is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *Service) handleComAtprotoSyncListRepos((*comatproto.SyncListRepos_Output, error)) (*comatproto.SyncListRepos_Output, error)
```


**Тип запроса:** comatproto.SyncListRepos_Output


```json
{
  "cursor": "string",
  "repos": []
}
```


*Определено в:* `api/atproto/synclistRepos.go`


**Тип ответа:** comatproto.SyncListRepos_Output


```json
{
  "cursor": "string",
  "repos": []
}
```


*Определено в:* `api/atproto/synclistRepos.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*comatproto.SyncListRepos_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/handlers.go:130`



---


[function] name: handleComAtprotoSyncRequestCrawl file: cmd/relay/handlers.go:19 returns_error: нет description: —


### handleComAtprotoSyncRequestCrawl (cmd/relay/handlers.go:19)


handleComAtprotoSyncRequestCrawl is a method that performs operations based on the provided parameters and returns (c echo.Context, body *comatproto.SyncRequestCrawl_Input, admin bool).


```go
func (s *Service) handleComAtprotoSyncRequestCrawl((c echo.Context, body *comatproto.SyncRequestCrawl_Input, admin bool)) (c echo.Context, body *comatproto.SyncRequestCrawl_Input, admin bool)
```


**Тип запроса:** comatproto.SyncRequestCrawl_Input


```json
{
  "hostname": "string"
}
```


*Определено в:* `api/atproto/syncrequestCrawl.go`


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


**Тип ответа:** body


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** comatproto.SyncRequestCrawl_Input


```json
{
  "hostname": "string"
}
```


*Определено в:* `api/atproto/syncrequestCrawl.go`


**Тип ответа:** admin


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/handlers.go:19`




## cmd/relay/handlers_admin.go


📄 Исходный файл: `cmd/relay/handlers_admin.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [handleAdminBanDomain](#handleadminbandomain-cmdrelayhandlers_admingo422) `:422`

- 🔗 [handleAdminChangeHostRateLimits](#handleadminchangehostratelimits-cmdrelayhandlers_admingo477) `:477`

- 🔗 [handleAdminGetNewHostPerDayRateLimit](#handleadmingetnewhostperdayratelimit-cmdrelayhandlers_admingo48) `:48`

- 🔗 [handleAdminGetSubsEnabled](#handleadmingetsubsenabled-cmdrelayhandlers_admingo42) `:42`

- 🔗 [handleAdminGetUpstreamConns](#handleadmingetupstreamconns-cmdrelayhandlers_admingo194) `:194`

- 🔗 [handleAdminKillUpstreamConn](#handleadminkillupstreamconn-cmdrelayhandlers_admingo297) `:297`

- 🔗 [handleAdminListConsumers](#handleadminlistconsumers-cmdrelayhandlers_admingo293) `:293`

- 🔗 [handleAdminListDomainBans](#handleadminlistdomainbans-cmdrelayhandlers_admingo399) `:399`

- 🔗 [handleAdminListRepoTakeDowns](#handleadminlistrepotakedowns-cmdrelayhandlers_admingo162) `:162`

- 🔗 [handleAdminRequestCrawl](#handleadminrequestcrawl-cmdrelayhandlers_admingo22) `:22`

- 🔗 [handleAdminReverseTakedown](#handleadminreversetakedown-cmdrelayhandlers_admingo113) `:113`

- 🔗 [handleAdminSetNewHostPerDayRateLimit](#handleadminsetnewhostperdayratelimit-cmdrelayhandlers_admingo54) `:54`

- 🔗 [handleAdminSetSubsEnabled](#handleadminsetsubsenabled-cmdrelayhandlers_admingo31) `:31`

- 🔗 [handleAdminTakeDownRepo](#handleadmintakedownrepo-cmdrelayhandlers_admingo69) `:69`

- 🔗 [handleAdminUnbanDomain](#handleadminunbandomain-cmdrelayhandlers_admingo447) `:447`

- 🔗 [handleBlockHost](#handleblockhost-cmdrelayhandlers_admingo330) `:330`

- 🔗 [handleListHosts](#handlelisthosts-cmdrelayhandlers_admingo224) `:224`

- 🔗 [handleUnblockHost](#handleunblockhost-cmdrelayhandlers_admingo364) `:364`


</details>


[function] name: handleAdminBanDomain file: cmd/relay/handlers_admin.go:422 returns_error: нет description: —


### handleAdminBanDomain (cmd/relay/handlers_admin.go:422)


handleAdminBanDomain is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminBanDomain((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:422`



---


[function] name: handleAdminChangeHostRateLimits file: cmd/relay/handlers_admin.go:477 returns_error: нет description: —


### handleAdminChangeHostRateLimits (cmd/relay/handlers_admin.go:477)


handleAdminChangeHostRateLimits is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminChangeHostRateLimits((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:477`



---


[function] name: handleAdminGetNewHostPerDayRateLimit file: cmd/relay/handlers_admin.go:48 returns_error: нет description: —


### handleAdminGetNewHostPerDayRateLimit (cmd/relay/handlers_admin.go:48)


handleAdminGetNewHostPerDayRateLimit is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminGetNewHostPerDayRateLimit((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:48`



---


[function] name: handleAdminGetSubsEnabled file: cmd/relay/handlers_admin.go:42 returns_error: нет description: —


### handleAdminGetSubsEnabled (cmd/relay/handlers_admin.go:42)


handleAdminGetSubsEnabled is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminGetSubsEnabled((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:42`



---


[function] name: handleAdminGetUpstreamConns file: cmd/relay/handlers_admin.go:194 returns_error: нет description: —


### handleAdminGetUpstreamConns (cmd/relay/handlers_admin.go:194)


handleAdminGetUpstreamConns is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminGetUpstreamConns((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:194`



---


[function] name: handleAdminKillUpstreamConn file: cmd/relay/handlers_admin.go:297 returns_error: нет description: —


### handleAdminKillUpstreamConn (cmd/relay/handlers_admin.go:297)


handleAdminKillUpstreamConn is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminKillUpstreamConn((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:297`



---


[function] name: handleAdminListConsumers file: cmd/relay/handlers_admin.go:293 returns_error: нет description: —


### handleAdminListConsumers (cmd/relay/handlers_admin.go:293)


handleAdminListConsumers is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminListConsumers((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:293`



---


[function] name: handleAdminListDomainBans file: cmd/relay/handlers_admin.go:399 returns_error: нет description: —


### handleAdminListDomainBans (cmd/relay/handlers_admin.go:399)


handleAdminListDomainBans is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminListDomainBans((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:399`



---


[function] name: handleAdminListRepoTakeDowns file: cmd/relay/handlers_admin.go:162 returns_error: нет description: —


### handleAdminListRepoTakeDowns (cmd/relay/handlers_admin.go:162)


handleAdminListRepoTakeDowns is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminListRepoTakeDowns((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:162`



---


[function] name: handleAdminRequestCrawl file: cmd/relay/handlers_admin.go:22 returns_error: нет description: This endpoint is basically the same as the regular com.atproto.sync.requestCrawl endpoint, except it sets a flag to bypa


### handleAdminRequestCrawl (cmd/relay/handlers_admin.go:22)


This endpoint is basically the same as the regular com.atproto.sync.requestCrawl endpoint, except it sets a flag to bypass configuration checks.


```go
func (s *Service) handleAdminRequestCrawl((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:22`



---


[function] name: handleAdminReverseTakedown file: cmd/relay/handlers_admin.go:113 returns_error: нет description: —


### handleAdminReverseTakedown (cmd/relay/handlers_admin.go:113)


handleAdminReverseTakedown is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminReverseTakedown((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:113`



---


[function] name: handleAdminSetNewHostPerDayRateLimit file: cmd/relay/handlers_admin.go:54 returns_error: нет description: —


### handleAdminSetNewHostPerDayRateLimit (cmd/relay/handlers_admin.go:54)


handleAdminSetNewHostPerDayRateLimit is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminSetNewHostPerDayRateLimit((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:54`



---


[function] name: handleAdminSetSubsEnabled file: cmd/relay/handlers_admin.go:31 returns_error: нет description: —


### handleAdminSetSubsEnabled (cmd/relay/handlers_admin.go:31)


handleAdminSetSubsEnabled is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminSetSubsEnabled((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:31`



---


[function] name: handleAdminTakeDownRepo file: cmd/relay/handlers_admin.go:69 returns_error: нет description: —


### handleAdminTakeDownRepo (cmd/relay/handlers_admin.go:69)


handleAdminTakeDownRepo is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminTakeDownRepo((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:69`



---


[function] name: handleAdminUnbanDomain file: cmd/relay/handlers_admin.go:447 returns_error: нет description: —


### handleAdminUnbanDomain (cmd/relay/handlers_admin.go:447)


handleAdminUnbanDomain is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleAdminUnbanDomain((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:447`



---


[function] name: handleBlockHost file: cmd/relay/handlers_admin.go:330 returns_error: нет description: —


### handleBlockHost (cmd/relay/handlers_admin.go:330)


handleBlockHost is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleBlockHost((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:330`



---


[function] name: handleListHosts file: cmd/relay/handlers_admin.go:224 returns_error: нет description: —


### handleListHosts (cmd/relay/handlers_admin.go:224)


handleListHosts is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleListHosts((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:224`



---


[function] name: handleUnblockHost file: cmd/relay/handlers_admin.go:364 returns_error: нет description: —


### handleUnblockHost (cmd/relay/handlers_admin.go:364)


handleUnblockHost is a method that performs operations based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) handleUnblockHost((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/handlers_admin.go:364`




## cmd/relay/main.go


📄 Исходный файл: `cmd/relay/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [configLogger](#configlogger-cmdrelaymaingo191) `:191`

- 🔗 [main](#main-cmdrelaymaingo32) `:32`

- 🔗 [run](#run-cmdrelaymaingo39) `:39`

- 🔗 [runRelay](#runrelay-cmdrelaymaingo212) `:212`


</details>


[function] name: configLogger file: cmd/relay/main.go:191 returns_error: нет description: —


### configLogger (cmd/relay/main.go:191)


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


📍 *Расположение:* `cmd/relay/main.go:191`



---


[function] name: main file: cmd/relay/main.go:32 returns_error: нет description: —


### main (cmd/relay/main.go:32)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/relay/main.go:32`



---


[function] name: run file: cmd/relay/main.go:39 returns_error: нет description: —


### run (cmd/relay/main.go:39)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/main.go:39`



---


[function] name: runRelay file: cmd/relay/main.go:212 returns_error: нет description: —


### runRelay (cmd/relay/main.go:212)


runRelay is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runRelay((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/relay/main.go:212`




## cmd/relay/otel.go


📄 Исходный файл: `cmd/relay/otel.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [setupOTEL](#setupotel-cmdrelayotelgo19) `:19`


</details>


[function] name: setupOTEL file: cmd/relay/otel.go:19 returns_error: нет description: —


### setupOTEL (cmd/relay/otel.go:19)


setupOTEL is a function that performs operations based on the provided parameters and returns (cmd *cli.Command).


```go
func setupOTEL((cmd *cli.Command)) (cmd *cli.Command)
```


**Тип запроса:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Command


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/otel.go:19`




## cmd/relay/pull.go


📄 Исходный файл: `cmd/relay/pull.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [runPullHosts](#runpullhosts-cmdrelaypullgo61) `:61`


</details>


[function] name: runPullHosts file: cmd/relay/pull.go:61 returns_error: нет description: —


### runPullHosts (cmd/relay/pull.go:61)


runPullHosts is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runPullHosts((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/relay/pull.go:61`




## cmd/relay/relay/account.go


📄 Исходный файл: `cmd/relay/relay/account.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [CreateAccountHost](#createaccounthost-cmdrelayrelayaccountgo59) `:59`

- 🔗 [DidToUid](#didtouid-cmdrelayrelayaccountgo325) `:325`

- 🔗 [EnsureAccountActive](#ensureaccountactive-cmdrelayrelayaccountgo197) `:197`

- 🔗 [EnsureAccountHost](#ensureaccounthost-cmdrelayrelayaccountgo127) `:127`

- 🔗 [GetAccount](#getaccount-cmdrelayrelayaccountgo17) `:17`

- 🔗 [GetAccountRepo](#getaccountrepo-cmdrelayrelayaccountgo45) `:45`

- 🔗 [ListAccountTakedowns](#listaccounttakedowns-cmdrelayrelayaccountgo311) `:311`

- 🔗 [ListAccounts](#listaccounts-cmdrelayrelayaccountgo288) `:288`

- 🔗 [ListAccountsDetailed](#listaccountsdetailed-cmdrelayrelayaccountgo295) `:295`

- 🔗 [NormalizeDID](#normalizedid-cmdrelayrelayaccountgo338) `:338`

- 🔗 [UpdateAccountLocalStatus](#updateaccountlocalstatus-cmdrelayrelayaccountgo252) `:252`

- 🔗 [UpdateAccountUpstreamStatus](#updateaccountupstreamstatus-cmdrelayrelayaccountgo237) `:237`

- 🔗 [UpsertAccountRepo](#upsertaccountrepo-cmdrelayrelayaccountgo320) `:320`


</details>


[function] name: CreateAccountHost file: cmd/relay/relay/account.go:59 returns_error: да description: Attempts creation of a new account associated with the given host, presumably because the account was discovered on that


### CreateAccountHost (cmd/relay/relay/account.go:59)


Attempts creation of a new account associated with the given host, presumably because the account was discovered on that host's stream.

If the account's identity doesn't match the host, this will fail. We only create accounts associated with hosts we already know of, not remote hosts (aka, no spidering).


```go
func (r *Relay) CreateAccountHost((*models.Account, error)) (*models.Account, error)
```


**Тип запроса:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.Account`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/account.go:59`



---


[function] name: DidToUid file: cmd/relay/relay/account.go:325 returns_error: да description: This implements the `diskpersist.UidSource` interface


### DidToUid (cmd/relay/relay/account.go:325)


This implements the `diskpersist.UidSource` interface


```go
func (r *Relay) DidToUid((uint64, error)) (uint64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `uint64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/account.go:325`



---


[function] name: EnsureAccountActive file: cmd/relay/relay/account.go:197 returns_error: нет description: Checks that account is active. If it is not active upstream, double-checks with the host and updates status if needed; o


### EnsureAccountActive (cmd/relay/relay/account.go:197)


Checks that account is active. If it is not active upstream, double-checks with the host and updates status if needed; otherwise returns an error.


```go
func (r *Relay) EnsureAccountActive((ctx context.Context, acc *models.Account)) (ctx context.Context, acc *models.Account)
```


**Тип запроса:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


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


**Тип ответа:** acc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


📍 *Расположение:* `cmd/relay/relay/account.go:197`



---


[function] name: EnsureAccountHost file: cmd/relay/relay/account.go:127 returns_error: нет description: Checks if account matches provided hostID, and in the fast pass returns successfully. If not, checks if the account shou


### EnsureAccountHost (cmd/relay/relay/account.go:127)


Checks if account matches provided hostID, and in the fast pass returns successfully. If not, checks if the account should be updated. If the account is now on the indicated host, it is updated, both in the database and struct via pointer. Otherwise, if the account is not associated with this host, an error is returned.

TODO: could also update to another known host, if doesn't match this hostID?


```go
func (r *Relay) EnsureAccountHost((ctx context.Context, acc *models.Account, hostID uint64, hostname string)) (ctx context.Context, acc *models.Account, hostID uint64, hostname string)
```


**Тип запроса:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


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


**Тип ответа:** acc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** hostID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/account.go:127`



---


[function] name: GetAccount file: cmd/relay/relay/account.go:17 returns_error: да description: —


### GetAccount (cmd/relay/relay/account.go:17)


GetAccount is a method that retrieves data based on the provided parameters and may return an error.


```go
func (r *Relay) GetAccount((*models.Account, error)) (*models.Account, error)
```


**Тип запроса:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.Account`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/account.go:17`



---


[function] name: GetAccountRepo file: cmd/relay/relay/account.go:45 returns_error: да description: —


### GetAccountRepo (cmd/relay/relay/account.go:45)


GetAccountRepo is a method that retrieves data based on the provided parameters and may return an error.


```go
func (r *Relay) GetAccountRepo((*models.AccountRepo, error)) (*models.AccountRepo, error)
```


**Тип запроса:** models.AccountRepo


```json
{
  "UID": 0,
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.AccountRepo


```json
{
  "UID": 0,
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.AccountRepo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/account.go:45`



---


[function] name: ListAccountTakedowns file: cmd/relay/relay/account.go:311 returns_error: да description: —


### ListAccountTakedowns (cmd/relay/relay/account.go:311)


ListAccountTakedowns is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (r *Relay) ListAccountTakedowns(([]*models.Account, error)) ([]*models.Account, error)
```


**Тип запроса:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*models.Account`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/account.go:311`



---


[function] name: ListAccounts file: cmd/relay/relay/account.go:288 returns_error: да description: Returns the of active accounts (based on local and upstream status). The sort order is by UID, ascending.


### ListAccounts (cmd/relay/relay/account.go:288)


Returns the of active accounts (based on local and upstream status). The sort order is by UID, ascending.


```go
func (r *Relay) ListAccounts(([]*models.Account, error)) ([]*models.Account, error)
```


**Тип запроса:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*models.Account`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/account.go:288`



---


[function] name: ListAccountsDetailed file: cmd/relay/relay/account.go:295 returns_error: да description: —


### ListAccountsDetailed (cmd/relay/relay/account.go:295)


ListAccountsDetailed is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (r *Relay) ListAccountsDetailed(([]*models.AccountDetailed, error)) ([]*models.AccountDetailed, error)
```


**Тип запроса:** models.AccountDetailed


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {},
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/joins.go`


**Тип ответа:** models.AccountDetailed


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {},
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/joins.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*models.AccountDetailed`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/account.go:295`



---


[function] name: NormalizeDID file: cmd/relay/relay/account.go:338 returns_error: нет description: In the general case, DIDs are case-sensitive. But PLC and did:web should not be, and should normalize to lower-case.


### NormalizeDID (cmd/relay/relay/account.go:338)


In the general case, DIDs are case-sensitive. But PLC and did:web should not be, and should normalize to lower-case.


```go
func NormalizeDID((orig syntax.DID)) (orig syntax.DID)
```


**Тип ответа:** orig


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


📍 *Расположение:* `cmd/relay/relay/account.go:338`



---


[function] name: UpdateAccountLocalStatus file: cmd/relay/relay/account.go:252 returns_error: нет description: This method updates the "local" account status (as opposed to "upstream" status, eg at the account's PDS).

If the `emit


### UpdateAccountLocalStatus (cmd/relay/relay/account.go:252)


This method updates the "local" account status (as opposed to "upstream" status, eg at the account's PDS).

If the `emitEvent` flag is set true, a `#account` event is broadcast. This should be used for account-level takedowns.


```go
func (r *Relay) UpdateAccountLocalStatus((ctx context.Context, did syntax.DID, status models.AccountStatus, emitEvent bool)) (ctx context.Context, did syntax.DID, status models.AccountStatus, emitEvent bool)
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


**Тип ответа:** status


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.AccountStatus


```json
{
  "activated": false,
  "expectedBlobs": 0,
  "importedBlobs": 0,
  "indexedRecords": 0,
  "privateStateValues": 0,
  "repoBlocks": 0,
  "repoCommit": "string",
  "repoRev": "string",
  "validDid": false
}
```


*Определено в:* `api/atproto/servercheckAccountStatus.go`


**Тип ответа:** emitEvent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/account.go:252`



---


[function] name: UpdateAccountUpstreamStatus file: cmd/relay/relay/account.go:237 returns_error: нет description: This updates the account's "upstream" status (eg, at the account's PDS). Usually this is called in response to an `#acco


### UpdateAccountUpstreamStatus (cmd/relay/relay/account.go:237)


This updates the account's "upstream" status (eg, at the account's PDS). Usually this is called in response to an `#account` event.

The DID and UID are both required, and *must* match; it is assumed that calling code has already done an account lookup.


```go
func (r *Relay) UpdateAccountUpstreamStatus((ctx context.Context, did syntax.DID, uid uint64, status models.AccountStatus)) (ctx context.Context, did syntax.DID, uid uint64, status models.AccountStatus)
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


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** status


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.AccountStatus


```json
{
  "activated": false,
  "expectedBlobs": 0,
  "importedBlobs": 0,
  "indexedRecords": 0,
  "privateStateValues": 0,
  "repoBlocks": 0,
  "repoCommit": "string",
  "repoRev": "string",
  "validDid": false
}
```


*Определено в:* `api/atproto/servercheckAccountStatus.go`


📍 *Расположение:* `cmd/relay/relay/account.go:237`



---


[function] name: UpsertAccountRepo file: cmd/relay/relay/account.go:320 returns_error: нет description: —


### UpsertAccountRepo (cmd/relay/relay/account.go:320)


UpsertAccountRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid uint64, rev syntax.TID, commitCID, commitDataCID string).


```go
func (r *Relay) UpsertAccountRepo((ctx context.Context, uid uint64, rev syntax.TID, commitCID, commitDataCID string)) (ctx context.Context, uid uint64, rev syntax.TID, commitCID, commitDataCID string)
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


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** rev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.TID


```json
{
  "ClockID": 0,
  "mtx": {},
  "lastUnixMicro": 0
}
```


*Определено в:* `atproto/syntax/tid.go`


**Тип ответа:** commitCID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** commitDataCID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/account.go:320`




## cmd/relay/relay/broadcast.go


📄 Исходный файл: `cmd/relay/relay/broadcast.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [HandleSubscribeRepos](#handlesubscriberepos-cmdrelayrelaybroadcastgo63) `:63`

- 🔗 [ListConsumers](#listconsumers-cmdrelayrelaybroadcastgo206) `:206`

- 🔗 [cleanupConsumer](#cleanupconsumer-cmdrelayrelaybroadcastgo37) `:37`

- 🔗 [registerConsumer](#registerconsumer-cmdrelayrelaybroadcastgo25) `:25`


</details>


[function] name: HandleSubscribeRepos file: cmd/relay/relay/broadcast.go:63 returns_error: нет description: Main HTTP request handler for clients connecting to the firehose (com.atproto.sync.subscribeRepos)


### HandleSubscribeRepos (cmd/relay/relay/broadcast.go:63)


Main HTTP request handler for clients connecting to the firehose (com.atproto.sync.subscribeRepos)


```go
func (r *Relay) HandleSubscribeRepos((resp http.ResponseWriter, req *http.Request, since *int64, realIP string)) (resp http.ResponseWriter, req *http.Request, since *int64, realIP string)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** resp


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


**Тип ответа:** since


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** realIP


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/broadcast.go:63`



---


[function] name: ListConsumers file: cmd/relay/relay/broadcast.go:206 returns_error: нет description: —


### ListConsumers (cmd/relay/relay/broadcast.go:206)


ListConsumers is a method that lists or finds data based on the provided parameters and returns ().


```go
func (r *Relay) ListConsumers(()) ()
```


📍 *Расположение:* `cmd/relay/relay/broadcast.go:206`



---


[function] name: cleanupConsumer file: cmd/relay/relay/broadcast.go:37 returns_error: нет description: —


### cleanupConsumer (cmd/relay/relay/broadcast.go:37)


cleanupConsumer is a method that performs operations based on the provided parameters and returns (id uint64).


```go
func (r *Relay) cleanupConsumer((id uint64)) (id uint64)
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


📍 *Расположение:* `cmd/relay/relay/broadcast.go:37`



---


[function] name: registerConsumer file: cmd/relay/relay/broadcast.go:25 returns_error: нет description: —


### registerConsumer (cmd/relay/relay/broadcast.go:25)


registerConsumer is a method that performs operations based on the provided parameters and returns (c *SocketConsumer).


```go
func (r *Relay) registerConsumer((c *SocketConsumer)) (c *SocketConsumer)
```


**Тип запроса:** SocketConsumer


```json
{
  "UserAgent": "string",
  "RemoteAddr": "string",
  "ConnectedAt": {},
  "EventsSent": {}
}
```


*Определено в:* `splitter/firehose.go`


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


**Тип ответа:** SocketConsumer


```json
{
  "UserAgent": "string",
  "RemoteAddr": "string",
  "ConnectedAt": {},
  "EventsSent": {}
}
```


*Определено в:* `splitter/firehose.go`


📍 *Расположение:* `cmd/relay/relay/broadcast.go:25`




## cmd/relay/relay/crawl.go


📄 Исходный файл: `cmd/relay/relay/crawl.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ResubscribeAllHosts](#resubscribeallhosts-cmdrelayrelaycrawlgo59) `:59`

- 🔗 [SubscribeToHost](#subscribetohost-cmdrelayrelaycrawlgo11) `:11`


</details>


[function] name: ResubscribeAllHosts file: cmd/relay/relay/crawl.go:59 returns_error: нет description: This function expects to be run when starting up, to re-connect to known active hosts


### ResubscribeAllHosts (cmd/relay/relay/crawl.go:59)


This function expects to be run when starting up, to re-connect to known active hosts


```go
func (r *Relay) ResubscribeAllHosts((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/relay/crawl.go:59`



---


[function] name: SubscribeToHost file: cmd/relay/relay/crawl.go:11 returns_error: нет description: —


### SubscribeToHost (cmd/relay/relay/crawl.go:11)


SubscribeToHost is a method that performs operations based on the provided parameters and returns (ctx context.Context, hostname string, noSSL, adminForce bool).


```go
func (r *Relay) SubscribeToHost((ctx context.Context, hostname string, noSSL, adminForce bool)) (ctx context.Context, hostname string, noSSL, adminForce bool)
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


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** noSSL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** adminForce


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/crawl.go:11`




## cmd/relay/relay/domain_ban.go


📄 Исходный файл: `cmd/relay/relay/domain_ban.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [CreateDomainBan](#createdomainban-cmdrelayrelaydomain_bango57) `:57`

- 🔗 [DomainIsBanned](#domainisbanned-cmdrelayrelaydomain_bango19) `:19`

- 🔗 [ListDomainBans](#listdomainbans-cmdrelayrelaydomain_bango67) `:67`

- 🔗 [RemoveDomainBan](#removedomainban-cmdrelayrelaydomain_bango62) `:62`

- 🔗 [findDomainBan](#finddomainban-cmdrelayrelaydomain_bango46) `:46`


</details>


[function] name: CreateDomainBan file: cmd/relay/relay/domain_ban.go:57 returns_error: нет description: —


### CreateDomainBan (cmd/relay/relay/domain_ban.go:57)


CreateDomainBan is a method that creates new data based on the provided parameters and returns (ctx context.Context, domain string).


```go
func (r *Relay) CreateDomainBan((ctx context.Context, domain string)) (ctx context.Context, domain string)
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


**Тип ответа:** domain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/domain_ban.go:57`



---


[function] name: DomainIsBanned file: cmd/relay/relay/domain_ban.go:19 returns_error: да description: DomainIsBanned checks if the given hostname is banned. It checks all domain suffixs.

Hostname is assumed to have been p


### DomainIsBanned (cmd/relay/relay/domain_ban.go:19)


DomainIsBanned checks if the given hostname is banned. It checks all domain suffixs.

Hostname is assumed to have been parsed/normalized (eg, lower-case).


```go
func (r *Relay) DomainIsBanned((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/domain_ban.go:19`



---


[function] name: ListDomainBans file: cmd/relay/relay/domain_ban.go:67 returns_error: да description: returns all domain bans


### ListDomainBans (cmd/relay/relay/domain_ban.go:67)


returns all domain bans


```go
func (r *Relay) ListDomainBans(([]models.DomainBan, error)) ([]models.DomainBan, error)
```


**Тип ответа:** models.DomainBan


```json
{
  "Domain": "string"
}
```


*Определено в:* `models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]models.DomainBan`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/domain_ban.go:67`



---


[function] name: RemoveDomainBan file: cmd/relay/relay/domain_ban.go:62 returns_error: нет description: —


### RemoveDomainBan (cmd/relay/relay/domain_ban.go:62)


RemoveDomainBan is a method that deletes data based on the provided parameters and returns (ctx context.Context, domain string).


```go
func (r *Relay) RemoveDomainBan((ctx context.Context, domain string)) (ctx context.Context, domain string)
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


**Тип ответа:** domain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/domain_ban.go:62`



---


[function] name: findDomainBan file: cmd/relay/relay/domain_ban.go:46 returns_error: да description: —


### findDomainBan (cmd/relay/relay/domain_ban.go:46)


findDomainBan is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Relay) findDomainBan((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/domain_ban.go:46`




## cmd/relay/relay/host.go


📄 Исходный файл: `cmd/relay/relay/host.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [GetHost](#gethost-cmdrelayrelayhostgo16) `:16`

- 🔗 [GetHostByID](#gethostbyid-cmdrelayrelayhostgo36) `:36`

- 🔗 [IsTrustedHostname](#istrustedhostname-cmdrelayrelayhostgo192) `:192`

- 🔗 [ListHosts](#listhosts-cmdrelayrelayhostgo57) `:57`

- 🔗 [ParseHostname](#parsehostname-cmdrelayrelayhostgo143) `:143`

- 🔗 [PersistHostCursors](#persisthostcursors-cmdrelayrelayhostgo127) `:127`

- 🔗 [UpdateHostAccountLimit](#updatehostaccountlimit-cmdrelayrelayhostgo78) `:78`

- 🔗 [UpdateHostStatus](#updatehoststatus-cmdrelayrelayhostgo74) `:74`


</details>


[function] name: GetHost file: cmd/relay/relay/host.go:16 returns_error: да description: —


### GetHost (cmd/relay/relay/host.go:16)


GetHost is a method that retrieves data based on the provided parameters and may return an error.


```go
func (r *Relay) GetHost((*models.Host, error)) (*models.Host, error)
```


**Тип запроса:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.Host`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/host.go:16`



---


[function] name: GetHostByID file: cmd/relay/relay/host.go:36 returns_error: да description: —


### GetHostByID (cmd/relay/relay/host.go:36)


GetHostByID is a method that retrieves data based on the provided parameters and may return an error.


```go
func (r *Relay) GetHostByID((*models.Host, error)) (*models.Host, error)
```


**Тип запроса:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.Host`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/host.go:36`



---


[function] name: IsTrustedHostname file: cmd/relay/relay/host.go:192 returns_error: нет description: —


### IsTrustedHostname (cmd/relay/relay/host.go:192)


IsTrustedHostname is a function that performs operations based on the provided parameters and returns (hostname string, domains []string).


```go
func IsTrustedHostname((hostname string, domains []string)) (hostname string, domains []string)
```


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** domains


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/host.go:192`



---


[function] name: ListHosts file: cmd/relay/relay/host.go:57 returns_error: да description: If `everActive` flag is true, then only hosts which have ever had a message received (seq > 0) are returned.


### ListHosts (cmd/relay/relay/host.go:57)


If `everActive` flag is true, then only hosts which have ever had a message received (seq > 0) are returned.


```go
func (r *Relay) ListHosts(([]*models.Host, error)) ([]*models.Host, error)
```


**Тип запроса:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*models.Host`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/host.go:57`



---


[function] name: ParseHostname file: cmd/relay/relay/host.go:143 returns_error: да description: parses, normalizes, and validates a raw URL (HTTP or WebSocket) in to a hostname for subscriptions

Hostnames must be DN


### ParseHostname (cmd/relay/relay/host.go:143)


parses, normalizes, and validates a raw URL (HTTP or WebSocket) in to a hostname for subscriptions

Hostnames must be DNS names, not IP addresses.


```go
func ParseHostname((hostname string, noSSL bool, err error)) (hostname string, noSSL bool, err error)
```


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** noSSL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `hostname string`, `noSSL bool`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/host.go:143`



---


[function] name: PersistHostCursors file: cmd/relay/relay/host.go:127 returns_error: нет description: Persists all the host cursors in a single database transaction. Also updates status to "active" for hosts which have a p


### PersistHostCursors (cmd/relay/relay/host.go:127)


Persists all the host cursors in a single database transaction. Also updates status to "active" for hosts which have a positive cursor.

Note that in some situations this may have partial success.


```go
func (r *Relay) PersistHostCursors((ctx context.Context, cursors *[]HostCursor)) (ctx context.Context, cursors *[]HostCursor)
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


**Тип ответа:** cursors


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** HostCursor


```json
{
  "HostID": 0,
  "LastSeq": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


📍 *Расположение:* `cmd/relay/relay/host.go:127`



---


[function] name: UpdateHostAccountLimit file: cmd/relay/relay/host.go:78 returns_error: нет description: —


### UpdateHostAccountLimit (cmd/relay/relay/host.go:78)


UpdateHostAccountLimit is a method that updates data based on the provided parameters and returns (ctx context.Context, hostID uint64, accountLimit int64).


```go
func (r *Relay) UpdateHostAccountLimit((ctx context.Context, hostID uint64, accountLimit int64)) (ctx context.Context, hostID uint64, accountLimit int64)
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


**Тип ответа:** hostID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** accountLimit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/host.go:78`



---


[function] name: UpdateHostStatus file: cmd/relay/relay/host.go:74 returns_error: нет description: —


### UpdateHostStatus (cmd/relay/relay/host.go:74)


UpdateHostStatus is a method that updates data based on the provided parameters and returns (ctx context.Context, hostID uint64, status models.HostStatus).


```go
func (r *Relay) UpdateHostStatus((ctx context.Context, hostID uint64, status models.HostStatus)) (ctx context.Context, hostID uint64, status models.HostStatus)
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


**Тип ответа:** hostID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** status


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.HostStatus


```json
{
  "accountCount": 0,
  "hostname": "string",
  "seq": 0,
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetHostStatus.go`


📍 *Расположение:* `cmd/relay/relay/host.go:74`




## cmd/relay/relay/host_checker.go


📄 Исходный файл: `cmd/relay/relay/host_checker.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [CheckHost](#checkhost-cmdrelayrelayhost_checkergo57) `:57`

- 🔗 [CheckHost](#checkhost-cmdrelayrelayhost_checkergo105) `:105`

- 🔗 [FetchAccountStatus](#fetchaccountstatus-cmdrelayrelayhost_checkergo67) `:67`

- 🔗 [FetchAccountStatus](#fetchaccountstatus-cmdrelayrelayhost_checkergo113) `:113`

- 🔗 [NewHostClient](#newhostclient-cmdrelayrelayhost_checkergo32) `:32`

- 🔗 [NewMockHostChecker](#newmockhostchecker-cmdrelayrelayhost_checkergo98) `:98`

- 🔗 [apiClient](#apiclient-cmdrelayrelayhost_checkergo46) `:46`


</details>


[function] name: CheckHost file: cmd/relay/relay/host_checker.go:57 returns_error: нет description: —


### CheckHost (cmd/relay/relay/host_checker.go:57)


CheckHost is a method that performs operations based on the provided parameters and returns (ctx context.Context, host string).


```go
func (hc *HostClient) CheckHost((ctx context.Context, host string)) (ctx context.Context, host string)
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


📍 *Расположение:* `cmd/relay/relay/host_checker.go:57`



---


[function] name: CheckHost file: cmd/relay/relay/host_checker.go:105 returns_error: нет description: —


### CheckHost (cmd/relay/relay/host_checker.go:105)


CheckHost is a method that performs operations based on the provided parameters and returns (ctx context.Context, host string).


```go
func (hc *MockHostChecker) CheckHost((ctx context.Context, host string)) (ctx context.Context, host string)
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


📍 *Расположение:* `cmd/relay/relay/host_checker.go:105`



---


[function] name: FetchAccountStatus file: cmd/relay/relay/host_checker.go:67 returns_error: да description: —


### FetchAccountStatus (cmd/relay/relay/host_checker.go:67)


FetchAccountStatus is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hc *HostClient) FetchAccountStatus((models.AccountStatus, error)) (models.AccountStatus, error)
```


**Тип ответа:** models.AccountStatus


```json
{
  "activated": false,
  "expectedBlobs": 0,
  "importedBlobs": 0,
  "indexedRecords": 0,
  "privateStateValues": 0,
  "repoBlocks": 0,
  "repoCommit": "string",
  "repoRev": "string",
  "validDid": false
}
```


*Определено в:* `api/atproto/servercheckAccountStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `models.AccountStatus`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/host_checker.go:67`



---


[function] name: FetchAccountStatus file: cmd/relay/relay/host_checker.go:113 returns_error: да description: —


### FetchAccountStatus (cmd/relay/relay/host_checker.go:113)


FetchAccountStatus is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hc *MockHostChecker) FetchAccountStatus((models.AccountStatus, error)) (models.AccountStatus, error)
```


**Тип ответа:** models.AccountStatus


```json
{
  "activated": false,
  "expectedBlobs": 0,
  "importedBlobs": 0,
  "indexedRecords": 0,
  "privateStateValues": 0,
  "repoBlocks": 0,
  "repoCommit": "string",
  "repoRev": "string",
  "validDid": false
}
```


*Определено в:* `api/atproto/servercheckAccountStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `models.AccountStatus`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/host_checker.go:113`



---


[function] name: NewHostClient file: cmd/relay/relay/host_checker.go:32 returns_error: нет description: —


### NewHostClient (cmd/relay/relay/host_checker.go:32)


NewHostClient is a function that performs operations based on the provided parameters and returns (userAgent string).


```go
func NewHostClient((userAgent string)) (userAgent string)
```


**Тип ответа:** userAgent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/host_checker.go:32`



---


[function] name: NewMockHostChecker file: cmd/relay/relay/host_checker.go:98 returns_error: нет description: —


### NewMockHostChecker (cmd/relay/relay/host_checker.go:98)


NewMockHostChecker is a function that performs operations based on the provided parameters and returns ().


```go
func NewMockHostChecker(()) ()
```


📍 *Расположение:* `cmd/relay/relay/host_checker.go:98`



---


[function] name: apiClient file: cmd/relay/relay/host_checker.go:46 returns_error: нет description: —


### apiClient (cmd/relay/relay/host_checker.go:46)


apiClient is a method that performs operations based on the provided parameters and returns (host string).


```go
func (hc *HostClient) apiClient((host string)) (host string)
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


📍 *Расположение:* `cmd/relay/relay/host_checker.go:46`




## cmd/relay/relay/ingest.go


📄 Исходный файл: `cmd/relay/relay/ingest.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [preProcessEvent](#preprocessevent-cmdrelayrelayingestgo54) `:54`

- 🔗 [processAccountEvent](#processaccountevent-cmdrelayrelayingestgo243) `:243`

- 🔗 [processCommitEvent](#processcommitevent-cmdrelayrelayingestgo88) `:88`

- 🔗 [processIdentityEvent](#processidentityevent-cmdrelayrelayingestgo194) `:194`

- 🔗 [processRepoEvent](#processrepoevent-cmdrelayrelayingestgo22) `:22`

- 🔗 [processSyncEvent](#processsyncevent-cmdrelayrelayingestgo149) `:149`


</details>


[function] name: preProcessEvent file: cmd/relay/relay/ingest.go:54 returns_error: да description: Implements the shared part of event processing: that the account existing, is associated with this host, etc.

If there 


### preProcessEvent (cmd/relay/relay/ingest.go:54)


Implements the shared part of event processing: that the account existing, is associated with this host, etc.

If there is no error, the returned account is always non-nil, but the identity may be nil (if there was a resolution error).


```go
func (r *Relay) preProcessEvent((*models.Account, *identity.Identity, error)) (*models.Account, *identity.Identity, error)
```


**Тип запроса:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип запроса:** identity.Identity


```json
{
  "DID": {},
  "Handle": {},
  "AlsoKnownAs": [],
  "Services": {},
  "Keys": {}
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** models.Account


```json
{
  "UID": 0,
  "DID": "string",
  "HostID": 0,
  "Status": {},
  "UpstreamStatus": {}
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** identity.Identity


```json
{
  "DID": {},
  "Handle": {},
  "AlsoKnownAs": [],
  "Services": {},
  "Keys": {}
}
```


*Определено в:* `atproto/identity/identity.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.Account`, `*identity.Identity`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/ingest.go:54`



---


[function] name: processAccountEvent file: cmd/relay/relay/ingest.go:243 returns_error: нет description: —


### processAccountEvent (cmd/relay/relay/ingest.go:243)


processAccountEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Account, hostname string, hostID uint64).


```go
func (r *Relay) processAccountEvent((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Account, hostname string, hostID uint64)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Account, hostname string, hostID uint64)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Account


```json
{
  "active": false,
  "did": "string",
  "seq": 0,
  "status": "string",
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** comatproto.SyncSubscribeRepos_Account


```json
{
  "active": false,
  "did": "string",
  "seq": 0,
  "status": "string",
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hostID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/ingest.go:243`



---


[function] name: processCommitEvent file: cmd/relay/relay/ingest.go:88 returns_error: нет description: —


### processCommitEvent (cmd/relay/relay/ingest.go:88)


processCommitEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit, hostname string, hostID uint64).


```go
func (r *Relay) processCommitEvent((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit, hostname string, hostID uint64)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit, hostname string, hostID uint64)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hostID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/ingest.go:88`



---


[function] name: processIdentityEvent file: cmd/relay/relay/ingest.go:194 returns_error: нет description: —


### processIdentityEvent (cmd/relay/relay/ingest.go:194)


processIdentityEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Identity, hostname string, hostID uint64).


```go
func (r *Relay) processIdentityEvent((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Identity, hostname string, hostID uint64)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Identity, hostname string, hostID uint64)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Identity


```json
{
  "did": "string",
  "handle": "string",
  "seq": 0,
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** comatproto.SyncSubscribeRepos_Identity


```json
{
  "did": "string",
  "handle": "string",
  "seq": 0,
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hostID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/ingest.go:194`



---


[function] name: processRepoEvent file: cmd/relay/relay/ingest.go:22 returns_error: нет description: This callback function gets called by Slurper on every upstream repo stream message from any host.

Messages are process


### processRepoEvent (cmd/relay/relay/ingest.go:22)


This callback function gets called by Slurper on every upstream repo stream message from any host.

Messages are processed in-order for a single account on a single host; but may be concurrent or out-of-order for the same account *across* hosts (eg, during account migration or a conflict)


```go
func (r *Relay) processRepoEvent((ctx context.Context, evt *stream.XRPCStreamEvent, hostname string, hostID uint64)) (ctx context.Context, evt *stream.XRPCStreamEvent, hostname string, hostID uint64)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hostID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/ingest.go:22`



---


[function] name: processSyncEvent file: cmd/relay/relay/ingest.go:149 returns_error: нет description: —


### processSyncEvent (cmd/relay/relay/ingest.go:149)


processSyncEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Sync, hostname string, hostID uint64).


```go
func (r *Relay) processSyncEvent((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Sync, hostname string, hostID uint64)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Sync, hostname string, hostID uint64)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Sync


```json
{
  "blocks": {},
  "did": "string",
  "rev": "string",
  "seq": 0,
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** comatproto.SyncSubscribeRepos_Sync


```json
{
  "blocks": {},
  "did": "string",
  "rev": "string",
  "seq": 0,
  "time": "string"
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hostID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/ingest.go:149`




## cmd/relay/relay/models/joins.go


📄 Исходный файл: `cmd/relay/relay/models/joins.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AccountStatus](#accountstatus-cmdrelayrelaymodelsjoinsgo14) `:14`

- 🔗 [IsActive](#isactive-cmdrelayrelaymodelsjoinsgo35) `:35`

- 🔗 [StatusField](#statusfield-cmdrelayrelaymodelsjoinsgo27) `:27`


</details>


[function] name: AccountStatus file: cmd/relay/relay/models/joins.go:14 returns_error: нет description: —


### AccountStatus (cmd/relay/relay/models/joins.go:14)


AccountStatus is a method that performs operations based on the provided parameters and returns ().


```go
func (a *AccountDetailed) AccountStatus(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/joins.go:14`



---


[function] name: IsActive file: cmd/relay/relay/models/joins.go:35 returns_error: нет description: —


### IsActive (cmd/relay/relay/models/joins.go:35)


IsActive is a method that performs operations based on the provided parameters and returns ().


```go
func (a *AccountDetailed) IsActive(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/joins.go:35`



---


[function] name: StatusField file: cmd/relay/relay/models/joins.go:27 returns_error: нет description: Returns a pointer to a copy of status string; or nil if status is active.

Helpful for account info responses which have


### StatusField (cmd/relay/relay/models/joins.go:27)


Returns a pointer to a copy of status string; or nil if status is active.

Helpful for account info responses which have a boolean 'active' and optional 'status' field (like the #account message)


```go
func (a *AccountDetailed) StatusField(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/joins.go:27`




## cmd/relay/relay/models/methods.go


📄 Исходный файл: `cmd/relay/relay/models/methods.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [AccountStatus](#accountstatus-cmdrelayrelaymodelsmethodsgo25) `:25`

- 🔗 [BaseURL](#baseurl-cmdrelayrelaymodelsmethodsgo8) `:8`

- 🔗 [IsActive](#isactive-cmdrelayrelaymodelsmethodsgo46) `:46`

- 🔗 [StatusField](#statusfield-cmdrelayrelaymodelsmethodsgo38) `:38`

- 🔗 [SubscribeReposURL](#subscribereposurl-cmdrelayrelaymodelsmethodsgo17) `:17`


</details>


[function] name: AccountStatus file: cmd/relay/relay/models/methods.go:25 returns_error: нет description: —


### AccountStatus (cmd/relay/relay/models/methods.go:25)


AccountStatus is a method that performs operations based on the provided parameters and returns ().


```go
func (a *Account) AccountStatus(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/methods.go:25`



---


[function] name: BaseURL file: cmd/relay/relay/models/methods.go:8 returns_error: нет description: returns base HTTP URL for the host: scheme, hostname, optional port, no path segment


### BaseURL (cmd/relay/relay/models/methods.go:8)


returns base HTTP URL for the host: scheme, hostname, optional port, no path segment


```go
func (h *Host) BaseURL(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/methods.go:8`



---


[function] name: IsActive file: cmd/relay/relay/models/methods.go:46 returns_error: нет description: —


### IsActive (cmd/relay/relay/models/methods.go:46)


IsActive is a method that performs operations based on the provided parameters and returns ().


```go
func (a *Account) IsActive(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/methods.go:46`



---


[function] name: StatusField file: cmd/relay/relay/models/methods.go:38 returns_error: нет description: Returns a pointer to a copy of status string; or nil if status is active.

Helpful for account info responses which have


### StatusField (cmd/relay/relay/models/methods.go:38)


Returns a pointer to a copy of status string; or nil if status is active.

Helpful for account info responses which have a boolean 'active' and optional 'status' field (like the #account message)


```go
func (a *Account) StatusField(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/methods.go:38`



---


[function] name: SubscribeReposURL file: cmd/relay/relay/models/methods.go:17 returns_error: нет description: returns websocket URL for the host: scheme, hostname, optional port, and path.


### SubscribeReposURL (cmd/relay/relay/models/methods.go:17)


returns websocket URL for the host: scheme, hostname, optional port, and path.


```go
func (h *Host) SubscribeReposURL(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/methods.go:17`




## cmd/relay/relay/models/models.go


📄 Исходный файл: `cmd/relay/relay/models/models.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [TableName](#tablename-cmdrelayrelaymodelsmodelsgo53) `:53`

- 🔗 [TableName](#tablename-cmdrelayrelaymodelsmodelsgo85) `:85`

- 🔗 [TableName](#tablename-cmdrelayrelaymodelsmodelsgo103) `:103`


</details>


[function] name: TableName file: cmd/relay/relay/models/models.go:53 returns_error: нет description: —


### TableName (cmd/relay/relay/models/models.go:53)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (Host) TableName(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/models.go:53`



---


[function] name: TableName file: cmd/relay/relay/models/models.go:85 returns_error: нет description: —


### TableName (cmd/relay/relay/models/models.go:85)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (Account) TableName(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/models.go:85`



---


[function] name: TableName file: cmd/relay/relay/models/models.go:103 returns_error: нет description: —


### TableName (cmd/relay/relay/models/models.go:103)


TableName is a method that performs operations based on the provided parameters and returns ().


```go
func (AccountRepo) TableName(()) ()
```


📍 *Расположение:* `cmd/relay/relay/models/models.go:103`




## cmd/relay/relay/relay.go


📄 Исходный файл: `cmd/relay/relay/relay.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [DefaultRelayConfig](#defaultrelayconfig-cmdrelayrelayrelaygo53) `:53`

- 🔗 [Healthcheck](#healthcheck-cmdrelayrelayrelaygo128) `:128`

- 🔗 [MigrateDatabase](#migratedatabase-cmdrelayrelayrelaygo111) `:111`

- 🔗 [NewRelay](#newrelay-cmdrelayrelayrelaygo64) `:64`


</details>


[function] name: DefaultRelayConfig file: cmd/relay/relay/relay.go:53 returns_error: нет description: —


### DefaultRelayConfig (cmd/relay/relay/relay.go:53)


DefaultRelayConfig is a function that performs operations based on the provided parameters and returns ().


```go
func DefaultRelayConfig(()) ()
```


📍 *Расположение:* `cmd/relay/relay/relay.go:53`



---


[function] name: Healthcheck file: cmd/relay/relay/relay.go:128 returns_error: нет description: simple check of connection to database


### Healthcheck (cmd/relay/relay/relay.go:128)


simple check of connection to database


```go
func (r *Relay) Healthcheck((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/relay/relay.go:128`



---


[function] name: MigrateDatabase file: cmd/relay/relay/relay.go:111 returns_error: нет description: —


### MigrateDatabase (cmd/relay/relay/relay.go:111)


MigrateDatabase is a method that performs operations based on the provided parameters and returns ().


```go
func (r *Relay) MigrateDatabase(()) ()
```


📍 *Расположение:* `cmd/relay/relay/relay.go:111`



---


[function] name: NewRelay file: cmd/relay/relay/relay.go:64 returns_error: да description: —


### NewRelay (cmd/relay/relay/relay.go:64)


NewRelay is a function that performs operations based on the provided parameters and may return an error.


```go
func NewRelay((*Relay, error)) (*Relay, error)
```


**Тип запроса:** Relay


```json
{
  "db": null,
  "Dir": {},
  "Logger": null,
  "Slurper": null,
  "Events": null,
  "HostChecker": {},
  "Config": {},
  "consumersLk": {},
  "nextConsumerID": 0,
  "consumers": {},
  "accountCache": null,
  "HostPerDayLimiter": null
}
```


*Определено в:* `cmd/relay/relay/relay.go`


**Тип ответа:** Relay


```json
{
  "db": null,
  "Dir": {},
  "Logger": null,
  "Slurper": null,
  "Events": null,
  "HostChecker": {},
  "Config": {},
  "consumersLk": {},
  "nextConsumerID": 0,
  "consumers": {},
  "accountCache": null,
  "HostPerDayLimiter": null
}
```


*Определено в:* `cmd/relay/relay/relay.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Relay`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/relay.go:64`




## cmd/relay/relay/slurper.go


📄 Исходный файл: `cmd/relay/relay/slurper.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [CheckIfSubscribed](#checkifsubscribed-cmdrelayrelayslurpergo237) `:237`

- 🔗 [ComputeLimiterCounts](#computelimitercounts-cmdrelayrelayslurpergo178) `:178`

- 🔗 [Counts](#counts-cmdrelayrelayslurpergo130) `:130`

- 🔗 [DefaultSlurperConfig](#defaultslurperconfig-cmdrelayrelayslurpergo65) `:65`

- 🔗 [GetActiveSubHostnames](#getactivesubhostnames-cmdrelayrelayslurpergo508) `:508`

- 🔗 [GetLimits](#getlimits-cmdrelayrelayslurpergo212) `:212`

- 🔗 [HostCursor](#hostcursor-cmdrelayrelayslurpergo111) `:111`

- 🔗 [KillUpstreamConnection](#killupstreamconnection-cmdrelayrelayslurpergo519) `:519`

- 🔗 [NewSlurper](#newslurper-cmdrelayrelayslurpergo138) `:138`

- 🔗 [Shutdown](#shutdown-cmdrelayrelayslurpergo226) `:226`

- 🔗 [Subscribe](#subscribe-cmdrelayrelayslurpergo248) `:248`

- 🔗 [UpdateLimiters](#updatelimiters-cmdrelayrelayslurpergo193) `:193`

- 🔗 [UpdateSeq](#updateseq-cmdrelayrelayslurpergo100) `:100`

- 🔗 [handleConnection](#handleconnection-cmdrelayrelayslurpergo393) `:393`

- 🔗 [persistCursors](#persistcursors-cmdrelayrelayslurpergo484) `:484`

- 🔗 [sleepForBackoff](#sleepforbackoff-cmdrelayrelayslurpergo380) `:380`

- 🔗 [subscribeWithRedialer](#subscribewithredialer-cmdrelayrelayslurpergo286) `:286`

- 🔗 [windowFunc](#windowfunc-cmdrelayrelayslurpergo174) `:174`


</details>


[function] name: CheckIfSubscribed file: cmd/relay/relay/slurper.go:237 returns_error: нет description: —


### CheckIfSubscribed (cmd/relay/relay/slurper.go:237)


CheckIfSubscribed is a method that performs operations based on the provided parameters and returns (hostname string).


```go
func (s *Slurper) CheckIfSubscribed((hostname string)) (hostname string)
```


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/slurper.go:237`



---


[function] name: ComputeLimiterCounts file: cmd/relay/relay/slurper.go:178 returns_error: нет description: —


### ComputeLimiterCounts (cmd/relay/relay/slurper.go:178)


ComputeLimiterCounts is a method that performs operations based on the provided parameters and returns (accountLimit int64, trusted bool).


```go
func (s *Slurper) ComputeLimiterCounts((accountLimit int64, trusted bool)) (accountLimit int64, trusted bool)
```


**Тип ответа:** accountLimit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** trusted


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/slurper.go:178`



---


[function] name: Counts file: cmd/relay/relay/slurper.go:130 returns_error: нет description: —


### Counts (cmd/relay/relay/slurper.go:130)


Counts is a method that performs operations based on the provided parameters and returns ().


```go
func (sl *StreamLimiters) Counts(()) ()
```


📍 *Расположение:* `cmd/relay/relay/slurper.go:130`



---


[function] name: DefaultSlurperConfig file: cmd/relay/relay/slurper.go:65 returns_error: нет description: —


### DefaultSlurperConfig (cmd/relay/relay/slurper.go:65)


DefaultSlurperConfig is a function that performs operations based on the provided parameters and returns ().


```go
func DefaultSlurperConfig(()) ()
```


📍 *Расположение:* `cmd/relay/relay/slurper.go:65`



---


[function] name: GetActiveSubHostnames file: cmd/relay/relay/slurper.go:508 returns_error: нет description: gets a snapshot of current subscription hostnames


### GetActiveSubHostnames (cmd/relay/relay/slurper.go:508)


gets a snapshot of current subscription hostnames


```go
func (s *Slurper) GetActiveSubHostnames(()) ()
```


📍 *Расположение:* `cmd/relay/relay/slurper.go:508`



---


[function] name: GetLimits file: cmd/relay/relay/slurper.go:212 returns_error: да description: —


### GetLimits (cmd/relay/relay/slurper.go:212)


GetLimits is a method that retrieves data based on the provided parameters and may return an error.


```go
func (s *Slurper) GetLimits((*StreamLimiterCounts, error)) (*StreamLimiterCounts, error)
```


**Тип запроса:** StreamLimiterCounts


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


**Тип ответа:** StreamLimiterCounts


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*StreamLimiterCounts`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/slurper.go:212`



---


[function] name: HostCursor file: cmd/relay/relay/slurper.go:111 returns_error: нет description: —


### HostCursor (cmd/relay/relay/slurper.go:111)


HostCursor is a method that performs operations based on the provided parameters and returns ().


```go
func (sub *Subscription) HostCursor(()) ()
```


📍 *Расположение:* `cmd/relay/relay/slurper.go:111`



---


[function] name: KillUpstreamConnection file: cmd/relay/relay/slurper.go:519 returns_error: нет description: —


### KillUpstreamConnection (cmd/relay/relay/slurper.go:519)


KillUpstreamConnection is a method that performs operations based on the provided parameters and returns (ctx context.Context, hostname string, ban bool).


```go
func (s *Slurper) KillUpstreamConnection((ctx context.Context, hostname string, ban bool)) (ctx context.Context, hostname string, ban bool)
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


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ban


```json
{
  "BannedDomains": []
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


📍 *Расположение:* `cmd/relay/relay/slurper.go:519`



---


[function] name: NewSlurper file: cmd/relay/relay/slurper.go:138 returns_error: да description: —


### NewSlurper (cmd/relay/relay/slurper.go:138)


NewSlurper is a function that performs operations based on the provided parameters and may return an error.


```go
func NewSlurper((*Slurper, error)) (*Slurper, error)
```


**Тип запроса:** Slurper


```json
{
  "processCallback": {},
  "Config": null,
  "subsLk": {},
  "subs": {},
  "shutdownChan": {},
  "shutdownResult": {},
  "logger": null
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


**Тип ответа:** Slurper


```json
{
  "processCallback": {},
  "Config": null,
  "subsLk": {},
  "subs": {},
  "shutdownChan": {},
  "shutdownResult": {},
  "logger": null
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Slurper`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/slurper.go:138`



---


[function] name: Shutdown file: cmd/relay/relay/slurper.go:226 returns_error: нет description: Shutdown shuts down the entire Slurper (all subscriptions)


### Shutdown (cmd/relay/relay/slurper.go:226)


Shutdown shuts down the entire Slurper (all subscriptions)


```go
func (s *Slurper) Shutdown(()) ()
```


📍 *Расположение:* `cmd/relay/relay/slurper.go:226`



---


[function] name: Subscribe file: cmd/relay/relay/slurper.go:248 returns_error: нет description: high-level entry point for opening a subscription (websocket connection). This might be called when adding a new host, o


### Subscribe (cmd/relay/relay/slurper.go:248)


high-level entry point for opening a subscription (websocket connection). This might be called when adding a new host, or when re-connecting to a previously subscribed host.

NOTE: the `host` parameter (a database row) contains metadata about the host at a point in time. Subsequent changes to the database aren't reflected in that struct, and changes to the struct don't get persisted to database.


```go
func (s *Slurper) Subscribe((host *models.Host)) (host *models.Host)
```


**Тип запроса:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


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


**Тип ответа:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


📍 *Расположение:* `cmd/relay/relay/slurper.go:248`



---


[function] name: UpdateLimiters file: cmd/relay/relay/slurper.go:193 returns_error: нет description: —


### UpdateLimiters (cmd/relay/relay/slurper.go:193)


UpdateLimiters is a method that updates data based on the provided parameters and returns (hostname string, accountLimit int64, trusted bool).


```go
func (s *Slurper) UpdateLimiters((hostname string, accountLimit int64, trusted bool)) (hostname string, accountLimit int64, trusted bool)
```


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** accountLimit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** trusted


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/slurper.go:193`



---


[function] name: UpdateSeq file: cmd/relay/relay/slurper.go:100 returns_error: нет description: pulls lastSeq from underlying scheduler in to this Subscription


### UpdateSeq (cmd/relay/relay/slurper.go:100)


pulls lastSeq from underlying scheduler in to this Subscription


```go
func (sub *Subscription) UpdateSeq(()) ()
```


📍 *Расположение:* `cmd/relay/relay/slurper.go:100`



---


[function] name: handleConnection file: cmd/relay/relay/slurper.go:393 returns_error: нет description: Configures event processing for a websocket connection, using the parallel schedule helper library, with all events proc


### handleConnection (cmd/relay/relay/slurper.go:393)


Configures event processing for a websocket connection, using the parallel schedule helper library, with all events processed using the configured callback function.


```go
func (s *Slurper) handleConnection((ctx context.Context, conn *websocket.Conn, sub *Subscription)) (ctx context.Context, conn *websocket.Conn, sub *Subscription)
```


**Тип запроса:** websocket.Conn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** Subscription


```json
{
  "Hostname": "string",
  "HostID": 0,
  "LastSeq": {},
  "Limiters": null,
  "scheduler": null,
  "lk": {},
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


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


**Тип ответа:** conn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** websocket.Conn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sub


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Subscription


```json
{
  "Hostname": "string",
  "HostID": 0,
  "LastSeq": {},
  "Limiters": null,
  "scheduler": null,
  "lk": {},
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


📍 *Расположение:* `cmd/relay/relay/slurper.go:393`



---


[function] name: persistCursors file: cmd/relay/relay/slurper.go:484 returns_error: нет description: persistCursors sends all cursors to callback to be persisted in database (if registered)


### persistCursors (cmd/relay/relay/slurper.go:484)


persistCursors sends all cursors to callback to be persisted in database (if registered)


```go
func (s *Slurper) persistCursors((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/relay/slurper.go:484`



---


[function] name: sleepForBackoff file: cmd/relay/relay/slurper.go:380 returns_error: нет description: —


### sleepForBackoff (cmd/relay/relay/slurper.go:380)


sleepForBackoff is a function that performs operations based on the provided parameters and returns (b int).


```go
func sleepForBackoff((b int)) (b int)
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


📍 *Расположение:* `cmd/relay/relay/slurper.go:380`



---


[function] name: subscribeWithRedialer file: cmd/relay/relay/slurper.go:286 returns_error: нет description: Main event-loop for a subscription (websocket connection to upstream host), expected to be called as a goroutine.

On co


### subscribeWithRedialer (cmd/relay/relay/slurper.go:286)


Main event-loop for a subscription (websocket connection to upstream host), expected to be called as a goroutine.

On connection failure (drop or failed initial connection), will attempt re-connects, with backoff.


```go
func (s *Slurper) subscribeWithRedialer((ctx context.Context, host *models.Host, sub *Subscription)) (ctx context.Context, host *models.Host, sub *Subscription)
```


**Тип запроса:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип запроса:** Subscription


```json
{
  "Hostname": "string",
  "HostID": 0,
  "LastSeq": {},
  "Limiters": null,
  "scheduler": null,
  "lk": {},
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


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


**Тип ответа:** models.Host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "UpdatedAt": {},
  "Hostname": "string",
  "NoSSL": false,
  "AccountLimit": 0,
  "Trusted": false,
  "Status": {},
  "LastSeq": 0,
  "AccountCount": 0
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** sub


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Subscription


```json
{
  "Hostname": "string",
  "HostID": 0,
  "LastSeq": {},
  "Limiters": null,
  "scheduler": null,
  "lk": {},
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


📍 *Расположение:* `cmd/relay/relay/slurper.go:286`



---


[function] name: windowFunc file: cmd/relay/relay/slurper.go:174 returns_error: нет description: —


### windowFunc (cmd/relay/relay/slurper.go:174)


windowFunc is a function that performs operations based on the provided parameters and returns (slidingwindow.Window, slidingwindow.StopFunc).


```go
func windowFunc((slidingwindow.Window, slidingwindow.StopFunc)) (slidingwindow.Window, slidingwindow.StopFunc)
```


**Тип ответа:** slidingwindow.Window


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slidingwindow.StopFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/slurper.go:174`




## cmd/relay/relay/util.go


📄 Исходный файл: `cmd/relay/relay/util.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [perDayLimiter](#perdaylimiter-cmdrelayrelayutilgo9) `:9`


</details>


[function] name: perDayLimiter file: cmd/relay/relay/util.go:9 returns_error: нет description: —


### perDayLimiter (cmd/relay/relay/util.go:9)


perDayLimiter is a function that performs operations based on the provided parameters and returns (count int64).


```go
func perDayLimiter((count int64)) (count int64)
```


**Тип ответа:** count


```json
{
  "Identity": {},
  "Status": "string"
}
```


*Определено в:* `cmd/relay/testing/scenario.go`


📍 *Расположение:* `cmd/relay/relay/util.go:9`




## cmd/relay/relay/verify.go


📄 Исходный файл: `cmd/relay/relay/verify.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [VerifyCommitMessageStrict](#verifycommitmessagestrict-cmdrelayrelayverifygo119) `:119`

- 🔗 [VerifyCommitObject](#verifycommitobject-cmdrelayrelayverifygo85) `:85`

- 🔗 [VerifyRepoCommit](#verifyrepocommit-cmdrelayrelayverifygo38) `:38`

- 🔗 [VerifyRepoSync](#verifyreposync-cmdrelayrelayverifygo177) `:177`


</details>


[function] name: VerifyCommitMessageStrict file: cmd/relay/relay/verify.go:119 returns_error: нет description: —


### VerifyCommitMessageStrict (cmd/relay/relay/verify.go:119)


VerifyCommitMessageStrict is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit, commit *repo.Commit, prevRepo *models.AccountRepo, hostname string).


```go
func (r *Relay) VerifyCommitMessageStrict((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit, commit *repo.Commit, prevRepo *models.AccountRepo, hostname string)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit, commit *repo.Commit, prevRepo *models.AccountRepo, hostname string)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


**Тип запроса:** repo.Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип запроса:** models.AccountRepo


```json
{
  "UID": 0,
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


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


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


**Тип ответа:** commit


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** repo.Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** prevRepo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** models.AccountRepo


```json
{
  "UID": 0,
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/verify.go:119`



---


[function] name: VerifyCommitObject file: cmd/relay/relay/verify.go:85 returns_error: нет description: the parts of basic verification which are common between #commit and #sync messages


### VerifyCommitObject (cmd/relay/relay/verify.go:85)


the parts of basic verification which are common between #commit and #sync messages


```go
func (r *Relay) VerifyCommitObject((ctx context.Context, commit *repo.Commit, ident *identity.Identity, hostname string)) (ctx context.Context, commit *repo.Commit, ident *identity.Identity, hostname string)
```


**Тип запроса:** repo.Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип запроса:** identity.Identity


```json
{
  "DID": {},
  "Handle": {},
  "AlsoKnownAs": [],
  "Services": {},
  "Keys": {}
}
```


*Определено в:* `atproto/identity/identity.go`


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


**Тип ответа:** commit


```json
{
  "ID": 0,
  "Uid": {},
  "Rev": "string",
  "Root": {}
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** repo.Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** ident


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** identity.Identity


```json
{
  "DID": {},
  "Handle": {},
  "AlsoKnownAs": [],
  "Services": {},
  "Keys": {}
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/relay/verify.go:85`



---


[function] name: VerifyRepoCommit file: cmd/relay/relay/verify.go:38 returns_error: да description: High-level entrypoint for verifying #commit messages.

Always verifies: loading commit and repo; field syntax; commit si


### VerifyRepoCommit (cmd/relay/relay/verify.go:38)


High-level entrypoint for verifying #commit messages.

Always verifies: loading commit and repo; field syntax; commit signature; future rev

Strict verification: use of deprecated fields; MST inversion; all ops present in blocks

Does not check: account/host matching; host-level sequence; account-level rev ordering; DID syntax

`ident` arg may be nil (if resolution failed)
`prevRepo` arg represents previous state, and is optional/nullable.
`hostname` arg is piped through just for logging, not for validating account/host match
returns an AccountRepo with empty UID, containing metadata about *this* commit


```go
func (r *Relay) VerifyRepoCommit((*models.AccountRepo, error)) (*models.AccountRepo, error)
```


**Тип запроса:** models.AccountRepo


```json
{
  "UID": 0,
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.AccountRepo


```json
{
  "UID": 0,
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.AccountRepo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/verify.go:38`



---


[function] name: VerifyRepoSync file: cmd/relay/relay/verify.go:177 returns_error: да description: High-level entrypoint for verifying #sync messages.

Always verifies: loading commit and repo; field syntax; commit sign


### VerifyRepoSync (cmd/relay/relay/verify.go:177)


High-level entrypoint for verifying #sync messages.

Always verifies: loading commit and repo; field syntax; commit signature; future rev

Does not check: account/host matching; host-level sequence; account-level rev ordering; DID syntax

`ident` arg may be nil (if resolution failed)
`hostname` arg is piped through just for logging, not for validating account/host match
returns an AccountRepo with empty UID, containing metadata about *this* commit


```go
func (r *Relay) VerifyRepoSync((*models.AccountRepo, error)) (*models.AccountRepo, error)
```


**Тип запроса:** models.AccountRepo


```json
{
  "UID": 0,
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Тип ответа:** models.AccountRepo


```json
{
  "UID": 0,
  "Rev": "string",
  "CommitCID": "string",
  "CommitDataCID": "string"
}
```


*Определено в:* `cmd/relay/relay/models/models.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*models.AccountRepo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/relay/verify.go:177`




## cmd/relay/service.go


📄 Исходный файл: `cmd/relay/service.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [DefaultServiceConfig](#defaultserviceconfig-cmdrelayservicego46) `:46`

- 🔗 [NewService](#newservice-cmdrelayservicego52) `:52`

- 🔗 [Shutdown](#shutdown-cmdrelayservicego197) `:197`

- 🔗 [StartAPI](#startapi-cmdrelayservicego75) `:75`

- 🔗 [StartMetrics](#startmetrics-cmdrelayservicego70) `:70`

- 🔗 [checkAdminAuth](#checkadminauth-cmdrelayservicego210) `:210`

- 🔗 [startWithListener](#startwithlistener-cmdrelayservicego87) `:87`


</details>


[function] name: DefaultServiceConfig file: cmd/relay/service.go:46 returns_error: нет description: —


### DefaultServiceConfig (cmd/relay/service.go:46)


DefaultServiceConfig is a function that performs operations based on the provided parameters and returns ().


```go
func DefaultServiceConfig(()) ()
```


📍 *Расположение:* `cmd/relay/service.go:46`



---


[function] name: NewService file: cmd/relay/service.go:52 returns_error: да description: —


### NewService (cmd/relay/service.go:52)


NewService is a function that performs operations based on the provided parameters and may return an error.


```go
func NewService((*Service, error)) (*Service, error)
```


**Тип запроса:** Service


```json
{
  "logger": null,
  "relay": null,
  "config": {},
  "siblingClient": {}
}
```


*Определено в:* `cmd/relay/service.go`


**Тип ответа:** Service


```json
{
  "logger": null,
  "relay": null,
  "config": {},
  "siblingClient": {}
}
```


*Определено в:* `cmd/relay/service.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Service`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/service.go:52`



---


[function] name: Shutdown file: cmd/relay/service.go:197 returns_error: нет description: —


### Shutdown (cmd/relay/service.go:197)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (svc *Service) Shutdown(()) ()
```


📍 *Расположение:* `cmd/relay/service.go:197`



---


[function] name: StartAPI file: cmd/relay/service.go:75 returns_error: нет description: —


### StartAPI (cmd/relay/service.go:75)


StartAPI is a method that performs operations based on the provided parameters and returns (bind string).


```go
func (svc *Service) StartAPI((bind string)) (bind string)
```


**Тип ответа:** bind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/service.go:75`



---


[function] name: StartMetrics file: cmd/relay/service.go:70 returns_error: нет description: —


### StartMetrics (cmd/relay/service.go:70)


StartMetrics is a method that performs operations based on the provided parameters and returns (listen string).


```go
func (svc *Service) StartMetrics((listen string)) (listen string)
```


**Тип ответа:** listen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/service.go:70`



---


[function] name: checkAdminAuth file: cmd/relay/service.go:210 returns_error: нет description: —


### checkAdminAuth (cmd/relay/service.go:210)


checkAdminAuth is a method that performs operations based on the provided parameters and returns (next echo.HandlerFunc).


```go
func (svc *Service) checkAdminAuth((next echo.HandlerFunc)) (next echo.HandlerFunc)
```


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** echo.HandlerFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/service.go:210`



---


[function] name: startWithListener file: cmd/relay/service.go:87 returns_error: нет description: —


### startWithListener (cmd/relay/service.go:87)


startWithListener is a method that performs operations based on the provided parameters and returns (listen net.Listener).


```go
func (svc *Service) startWithListener((listen net.Listener)) (listen net.Listener)
```


**Тип ответа:** listen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.Listener


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/service.go:87`




## cmd/relay/stream/cbor_gen.go


📄 Исходный файл: `cmd/relay/stream/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-cmdrelaystreamcbor_gengo21) `:21`

- 🔗 [MarshalCBOR](#marshalcbor-cmdrelaystreamcbor_gengo170) `:170`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-cmdrelaystreamcbor_gengo81) `:81`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-cmdrelaystreamcbor_gengo230) `:230`


</details>


[function] name: MarshalCBOR file: cmd/relay/stream/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (cmd/relay/stream/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EventHeader) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `cmd/relay/stream/cbor_gen.go:21`



---


[function] name: MarshalCBOR file: cmd/relay/stream/cbor_gen.go:170 returns_error: нет description: —


### MarshalCBOR (cmd/relay/stream/cbor_gen.go:170)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *ErrorFrame) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `cmd/relay/stream/cbor_gen.go:170`



---


[function] name: UnmarshalCBOR file: cmd/relay/stream/cbor_gen.go:81 returns_error: да description: —


### UnmarshalCBOR (cmd/relay/stream/cbor_gen.go:81)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EventHeader) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `cmd/relay/stream/cbor_gen.go:81`



---


[function] name: UnmarshalCBOR file: cmd/relay/stream/cbor_gen.go:230 returns_error: да description: —


### UnmarshalCBOR (cmd/relay/stream/cbor_gen.go:230)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ErrorFrame) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `cmd/relay/stream/cbor_gen.go:230`




## cmd/relay/stream/consumer.go


📄 Исходный файл: `cmd/relay/stream/consumer.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [EventHandler](#eventhandler-cmdrelaystreamconsumergo31) `:31`

- 🔗 [EventHandler](#eventhandler-cmdrelaystreamconsumergo86) `:86`

- 🔗 [HandleRepoStream](#handlerepostream-cmdrelaystreamconsumergo112) `:112`

- 🔗 [NewInstrumentedRepoStreamCallbacks](#newinstrumentedrepostreamcallbacks-cmdrelaystreamconsumergo59) `:59`

- 🔗 [Read](#read-cmdrelaystreamconsumergo102) `:102`

- 🔗 [waitForLimiter](#waitforlimiter-cmdrelaystreamconsumergo66) `:66`


</details>


[function] name: EventHandler file: cmd/relay/stream/consumer.go:31 returns_error: нет description: —


### EventHandler (cmd/relay/stream/consumer.go:31)


EventHandler is a method that performs operations based on the provided parameters and returns (ctx context.Context, xev *XRPCStreamEvent).


```go
func (rsc *RepoStreamCallbacks) EventHandler((ctx context.Context, xev *XRPCStreamEvent)) (ctx context.Context, xev *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** xev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/consumer.go:31`



---


[function] name: EventHandler file: cmd/relay/stream/consumer.go:86 returns_error: нет description: —


### EventHandler (cmd/relay/stream/consumer.go:86)


EventHandler is a method that performs operations based on the provided parameters and returns (ctx context.Context, xev *XRPCStreamEvent).


```go
func (rsc *InstrumentedRepoStreamCallbacks) EventHandler((ctx context.Context, xev *XRPCStreamEvent)) (ctx context.Context, xev *XRPCStreamEvent)
```


**Тип запроса:** XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** xev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/consumer.go:86`



---


[function] name: HandleRepoStream file: cmd/relay/stream/consumer.go:112 returns_error: нет description: HandleRepoStream
con is source of events
sched gets AddWork for each event
logger may be nil for default logger


### HandleRepoStream (cmd/relay/stream/consumer.go:112)


HandleRepoStream
con is source of events
sched gets AddWork for each event
logger may be nil for default logger


```go
func HandleRepoStream((ctx context.Context, con *websocket.Conn, sched Scheduler, logger *slog.Logger)) (ctx context.Context, con *websocket.Conn, sched Scheduler, logger *slog.Logger)
```


**Тип запроса:** websocket.Conn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип запроса:** slog.Logger


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


**Тип ответа:** con


```json
{
  "repo": "string",
  "val": null,
  "signal": "string",
  "wg": null
}
```


*Определено в:* `events/schedulers/autoscaling/autoscaling.go`


**Тип ответа:** websocket.Conn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sched


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Scheduler


```json
{
  "concurrency": 0,
  "maxConcurrency": 0,
  "do": {},
  "feeder": {},
  "workerGroup": {},
  "lk": {},
  "active": {},
  "maxActive": 0,
  "ident": "string",
  "itemsAdded": {},
  "itemsProcessed": {},
  "itemsActive": {},
  "workersActive": {},
  "throughputManager": null,
  "autoscaleFrequency": {},
  "autoscalerIn": {},
  "autoscalerOut": {},
  "log": null
}
```


*Определено в:* `events/schedulers/autoscaling/autoscaling.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/stream/consumer.go:112`



---


[function] name: NewInstrumentedRepoStreamCallbacks file: cmd/relay/stream/consumer.go:59 returns_error: да description: —


### NewInstrumentedRepoStreamCallbacks (cmd/relay/stream/consumer.go:59)


NewInstrumentedRepoStreamCallbacks is a function that performs operations based on the provided parameters and may return an error.


```go
func NewInstrumentedRepoStreamCallbacks((limiters []*slidingwindow.Limiter, next func(ctx context.Context, xev *XRPCStreamEvent) error)) (limiters []*slidingwindow.Limiter, next func(ctx context.Context, xev *XRPCStreamEvent) error)
```


**Тип запроса:** slidingwindow.Limiter


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


**Тип запроса:** XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** limiters


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slidingwindow.Limiter


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


**Тип ответа:** next


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


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


**Тип ответа:** xev


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `limiters []*slidingwindow.Limiter`, `next func(ctx context.Context`, `xev *XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/consumer.go:59`



---


[function] name: Read file: cmd/relay/stream/consumer.go:102 returns_error: да description: —


### Read (cmd/relay/stream/consumer.go:102)


Read is a method that performs operations based on the provided parameters and may return an error.


```go
func (sr *instrumentedReader) Read((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/consumer.go:102`



---


[function] name: waitForLimiter file: cmd/relay/stream/consumer.go:66 returns_error: нет description: —


### waitForLimiter (cmd/relay/stream/consumer.go:66)


waitForLimiter is a function that performs operations based on the provided parameters and returns (ctx context.Context, lim *slidingwindow.Limiter).


```go
func waitForLimiter((ctx context.Context, lim *slidingwindow.Limiter)) (ctx context.Context, lim *slidingwindow.Limiter)
```


**Тип запроса:** slidingwindow.Limiter


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


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


**Тип ответа:** lim


```json
{
  "Limit": 0,
  "Remaining": 0,
  "Policy": "string",
  "Reset": {}
}
```


*Определено в:* `xrpc/xrpc.go`


**Тип ответа:** slidingwindow.Limiter


```json
{
  "PerSecond": 0,
  "PerHour": 0,
  "PerDay": 0
}
```


*Определено в:* `cmd/relay/relay/slurper.go`


📍 *Расположение:* `cmd/relay/stream/consumer.go:66`




## cmd/relay/stream/eventmgr/event_manager.go


📄 Исходный файл: `cmd/relay/stream/eventmgr/event_manager.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [AddEvent](#addevent-cmdrelaystreameventmgrevent_managergo109) `:109`

- 🔗 [NewEventManager](#neweventmanager-cmdrelaystreameventmgrevent_managergo28) `:28`

- 🔗 [SequenceForEvent](#sequenceforevent-cmdrelaystreameventmgrevent_managergo245) `:245`

- 🔗 [Shutdown](#shutdown-cmdrelaystreameventmgrevent_managergo41) `:41`

- 🔗 [Subscribe](#subscribe-cmdrelaystreameventmgrevent_managergo117) `:117`

- 🔗 [TakeDownRepo](#takedownrepo-cmdrelaystreameventmgrevent_managergo240) `:240`

- 🔗 [addSubscriber](#addsubscriber-cmdrelaystreameventmgrevent_managergo233) `:233`

- 🔗 [broadcastEvent](#broadcastevent-cmdrelaystreameventmgrevent_managergo46) `:46`

- 🔗 [persistAndSendEvent](#persistandsendevent-cmdrelaystreameventmgrevent_managergo100) `:100`

- 🔗 [rmSubscriber](#rmsubscriber-cmdrelaystreameventmgrevent_managergo220) `:220`


</details>


[function] name: AddEvent file: cmd/relay/stream/eventmgr/event_manager.go:109 returns_error: нет description: —


### AddEvent (cmd/relay/stream/eventmgr/event_manager.go:109)


AddEvent is a method that creates new data based on the provided parameters and returns (ctx context.Context, ev *stream.XRPCStreamEvent).


```go
func (em *EventManager) AddEvent((ctx context.Context, ev *stream.XRPCStreamEvent)) (ctx context.Context, ev *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** ev


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:109`



---


[function] name: NewEventManager file: cmd/relay/stream/eventmgr/event_manager.go:28 returns_error: нет description: —


### NewEventManager (cmd/relay/stream/eventmgr/event_manager.go:28)


NewEventManager is a function that performs operations based on the provided parameters and returns (persister persist.EventPersistence).


```go
func NewEventManager((persister persist.EventPersistence)) (persister persist.EventPersistence)
```


**Тип ответа:** persister


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** persist.EventPersistence


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:28`



---


[function] name: SequenceForEvent file: cmd/relay/stream/eventmgr/event_manager.go:245 returns_error: нет description: TODO: remove this?


### SequenceForEvent (cmd/relay/stream/eventmgr/event_manager.go:245)


TODO: remove this?


```go
func SequenceForEvent((evt *stream.XRPCStreamEvent)) (evt *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:245`



---


[function] name: Shutdown file: cmd/relay/stream/eventmgr/event_manager.go:41 returns_error: нет description: —


### Shutdown (cmd/relay/stream/eventmgr/event_manager.go:41)


Shutdown is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (em *EventManager) Shutdown((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:41`



---


[function] name: Subscribe file: cmd/relay/stream/eventmgr/event_manager.go:117 returns_error: да description: —


### Subscribe (cmd/relay/stream/eventmgr/event_manager.go:117)


Subscribe is a method that performs operations based on the provided parameters and may return an error.


```go
func (em *EventManager) Subscribe((<-chan *stream.XRPCStreamEvent, func(), error)) (<-chan *stream.XRPCStreamEvent, func(), error)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `<-chan *stream.XRPCStreamEvent`, `func()`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:117`



---


[function] name: TakeDownRepo file: cmd/relay/stream/eventmgr/event_manager.go:240 returns_error: нет description: —


### TakeDownRepo (cmd/relay/stream/eventmgr/event_manager.go:240)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid uint64).


```go
func (em *EventManager) TakeDownRepo((ctx context.Context, uid uint64)) (ctx context.Context, uid uint64)
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


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:240`



---


[function] name: addSubscriber file: cmd/relay/stream/eventmgr/event_manager.go:233 returns_error: нет description: —


### addSubscriber (cmd/relay/stream/eventmgr/event_manager.go:233)


addSubscriber is a method that performs operations based on the provided parameters and returns (sub *Subscriber).


```go
func (em *EventManager) addSubscriber((sub *Subscriber)) (sub *Subscriber)
```


**Тип запроса:** Subscriber


```json
{
  "outgoing": {},
  "filter": {},
  "done": {},
  "cleanup": {},
  "lk": {},
  "cleanedUp": false,
  "ident": "string",
  "enqueuedCounter": {},
  "broadcastCounter": {}
}
```


*Определено в:* `events/events.go`


**Тип ответа:** sub


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Subscriber


```json
{
  "outgoing": {},
  "filter": {},
  "done": {},
  "cleanup": {},
  "lk": {},
  "cleanedUp": false,
  "ident": "string",
  "enqueuedCounter": {},
  "broadcastCounter": {}
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:233`



---


[function] name: broadcastEvent file: cmd/relay/stream/eventmgr/event_manager.go:46 returns_error: нет description: broadcastEvent is the target for EventPersistence.SetEventBroadcaster()


### broadcastEvent (cmd/relay/stream/eventmgr/event_manager.go:46)


broadcastEvent is the target for EventPersistence.SetEventBroadcaster()


```go
func (em *EventManager) broadcastEvent((evt *stream.XRPCStreamEvent)) (evt *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:46`



---


[function] name: persistAndSendEvent file: cmd/relay/stream/eventmgr/event_manager.go:100 returns_error: нет description: —


### persistAndSendEvent (cmd/relay/stream/eventmgr/event_manager.go:100)


persistAndSendEvent is a method that performs operations based on the provided parameters and returns (ctx context.Context, evt *stream.XRPCStreamEvent).


```go
func (em *EventManager) persistAndSendEvent((ctx context.Context, evt *stream.XRPCStreamEvent)) (ctx context.Context, evt *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:100`



---


[function] name: rmSubscriber file: cmd/relay/stream/eventmgr/event_manager.go:220 returns_error: нет description: —


### rmSubscriber (cmd/relay/stream/eventmgr/event_manager.go:220)


rmSubscriber is a method that performs operations based on the provided parameters and returns (sub *Subscriber).


```go
func (em *EventManager) rmSubscriber((sub *Subscriber)) (sub *Subscriber)
```


**Тип запроса:** Subscriber


```json
{
  "outgoing": {},
  "filter": {},
  "done": {},
  "cleanup": {},
  "lk": {},
  "cleanedUp": false,
  "ident": "string",
  "enqueuedCounter": {},
  "broadcastCounter": {}
}
```


*Определено в:* `events/events.go`


**Тип ответа:** sub


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Subscriber


```json
{
  "outgoing": {},
  "filter": {},
  "done": {},
  "cleanup": {},
  "lk": {},
  "cleanedUp": false,
  "ident": "string",
  "enqueuedCounter": {},
  "broadcastCounter": {}
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/eventmgr/event_manager.go:220`




## cmd/relay/stream/events.go


📄 Исходный файл: `cmd/relay/stream/events.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Deserialize](#deserialize-cmdrelaystreameventsgo76) `:76`

- 🔗 [GetSequence](#getsequence-cmdrelaystreameventsgo176) `:176`

- 🔗 [Preserialize](#preserialize-cmdrelaystreameventsgo137) `:137`

- 🔗 [Sequence](#sequence-cmdrelaystreameventsgo155) `:155`

- 🔗 [Serialize](#serialize-cmdrelaystreameventsgo42) `:42`


</details>


[function] name: Deserialize file: cmd/relay/stream/events.go:76 returns_error: нет description: —


### Deserialize (cmd/relay/stream/events.go:76)


Deserialize is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (xevt *XRPCStreamEvent) Deserialize((r io.Reader)) (r io.Reader)
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


📍 *Расположение:* `cmd/relay/stream/events.go:76`



---


[function] name: GetSequence file: cmd/relay/stream/events.go:176 returns_error: нет description: —


### GetSequence (cmd/relay/stream/events.go:176)


GetSequence is a method that retrieves data based on the provided parameters and returns (int64, bool).


```go
func (evt *XRPCStreamEvent) GetSequence((int64, bool)) (int64, bool)
```


📍 *Расположение:* `cmd/relay/stream/events.go:176`



---


[function] name: Preserialize file: cmd/relay/stream/events.go:137 returns_error: нет description: serialize content into Preserialized cache


### Preserialize (cmd/relay/stream/events.go:137)


serialize content into Preserialized cache


```go
func (evt *XRPCStreamEvent) Preserialize(()) ()
```


📍 *Расположение:* `cmd/relay/stream/events.go:137`



---


[function] name: Sequence file: cmd/relay/stream/events.go:155 returns_error: нет description: —


### Sequence (cmd/relay/stream/events.go:155)


Sequence is a method that performs operations based on the provided parameters and returns ().


```go
func (evt *XRPCStreamEvent) Sequence(()) ()
```


📍 *Расположение:* `cmd/relay/stream/events.go:155`



---


[function] name: Serialize file: cmd/relay/stream/events.go:42 returns_error: нет description: —


### Serialize (cmd/relay/stream/events.go:42)


Serialize is a method that performs operations based on the provided parameters and returns (wc io.Writer).


```go
func (evt *XRPCStreamEvent) Serialize((wc io.Writer)) (wc io.Writer)
```


**Тип ответа:** wc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/stream/events.go:42`




## cmd/relay/stream/persist/diskpersist/diskpersist.go


📄 Исходный файл: `cmd/relay/stream/persist/diskpersist/diskpersist.go`


<details open>
<summary><b>Функции в этом файле (31)</b></summary>


- 🔗 [DefaultDiskPersistOptions](#defaultdiskpersistoptions-cmdrelaystreampersistdiskpersistdiskpersistgo88) `:88`

- 🔗 [Flush](#flush-cmdrelaystreampersistdiskpersistdiskpersistgo979) `:979`

- 🔗 [Len64](#len64-cmdrelaystreampersistdiskpersistdiskpersistgo622) `:622`

- 🔗 [NewDiskPersistence](#newdiskpersistence-cmdrelaystreampersistdiskpersistdiskpersistgo103) `:103`

- 🔗 [Persist](#persist-cmdrelaystreampersistdiskpersistdiskpersistgo548) `:548`

- 🔗 [Playback](#playback-cmdrelaystreampersistdiskpersistdiskpersistgo691) `:691`

- 🔗 [PlaybackLogfiles](#playbacklogfiles-cmdrelaystreampersistdiskpersistdiskpersistgo732) `:732`

- 🔗 [Read](#read-cmdrelaystreampersistdiskpersistdiskpersistgo912) `:912`

- 🔗 [SetEventBroadcaster](#seteventbroadcaster-cmdrelaystreampersistdiskpersistdiskpersistgo997) `:997`

- 🔗 [SetUidSource](#setuidsource-cmdrelaystreampersistdiskpersistdiskpersistgo177) `:177`

- 🔗 [Shutdown](#shutdown-cmdrelaystreampersistdiskpersistdiskpersistgo988) `:988`

- 🔗 [TakeDownRepo](#takedownrepo-cmdrelaystreampersistdiskpersistdiskpersistgo857) `:857`

- 🔗 [addJobToQueue](#addjobtoqueue-cmdrelaystreampersistdiskpersistdiskpersistgo334) `:334`

- 🔗 [deleteEventsForUser](#deleteeventsforuser-cmdrelaystreampersistdiskpersistdiskpersistgo919) `:919`

- 🔗 [doPersist](#dopersist-cmdrelaystreampersistdiskpersistdiskpersistgo498) `:498`

- 🔗 [flushLog](#flushlog-cmdrelaystreampersistdiskpersistdiskpersistgo371) `:371`

- 🔗 [flushRoutine](#flushroutine-cmdrelaystreampersistdiskpersistdiskpersistgo352) `:352`

- 🔗 [forEachShardWithUserEvents](#foreachshardwithuserevents-cmdrelaystreampersistdiskpersistdiskpersistgo876) `:876`

- 🔗 [garbageCollect](#garbagecollect-cmdrelaystreampersistdiskpersistdiskpersistgo440) `:440`

- 🔗 [garbageCollectRoutine](#garbagecollectroutine-cmdrelaystreampersistdiskpersistdiskpersistgo396) `:396`

- 🔗 [initLogFile](#initlogfile-cmdrelaystreampersistdiskpersistdiskpersistgo229) `:229`

- 🔗 [mutateUserEventsInLog](#mutateusereventsinlog-cmdrelaystreampersistdiskpersistdiskpersistgo923) `:923`

- 🔗 [postDoNotEmit](#postdonotemit-cmdrelaystreampersistdiskpersistdiskpersistgo750) `:750`

- 🔗 [readEventsFrom](#readeventsfrom-cmdrelaystreampersistdiskpersistdiskpersistgo758) `:758`

- 🔗 [readHeader](#readheader-cmdrelaystreampersistdiskpersistdiskpersistgo628) `:628`

- 🔗 [refMaybeHasUserEvents](#refmaybehasuserevents-cmdrelaystreampersistdiskpersistdiskpersistgo905) `:905`

- 🔗 [resumeLog](#resumelog-cmdrelaystreampersistdiskpersistdiskpersistgo181) `:181`

- 🔗 [scanForLastSeq](#scanforlastseq-cmdrelaystreampersistdiskpersistdiskpersistgo279) `:279`

- 🔗 [swapLog](#swaplog-cmdrelaystreampersistdiskpersistdiskpersistgo255) `:255`

- 🔗 [uidForDid](#uidfordid-cmdrelaystreampersistdiskpersistdiskpersistgo673) `:673`

- 🔗 [writeHeader](#writeheader-cmdrelaystreampersistdiskpersistdiskpersistgo654) `:654`


</details>


[function] name: DefaultDiskPersistOptions file: cmd/relay/stream/persist/diskpersist/diskpersist.go:88 returns_error: нет description: —


### DefaultDiskPersistOptions (cmd/relay/stream/persist/diskpersist/diskpersist.go:88)


DefaultDiskPersistOptions is a function that performs operations based on the provided parameters and returns ().


```go
func DefaultDiskPersistOptions(()) ()
```


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:88`



---


[function] name: Flush file: cmd/relay/stream/persist/diskpersist/diskpersist.go:979 returns_error: нет description: —


### Flush (cmd/relay/stream/persist/diskpersist/diskpersist.go:979)


Flush is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (dp *DiskPersistence) Flush((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:979`



---


[function] name: Len64 file: cmd/relay/stream/persist/diskpersist/diskpersist.go:622 returns_error: нет description: —


### Len64 (cmd/relay/stream/persist/diskpersist/diskpersist.go:622)


Len64 is a method that performs operations based on the provided parameters and returns ().


```go
func (eh *evtHeader) Len64(()) ()
```


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:622`



---


[function] name: NewDiskPersistence file: cmd/relay/stream/persist/diskpersist/diskpersist.go:103 returns_error: да description: —


### NewDiskPersistence (cmd/relay/stream/persist/diskpersist/diskpersist.go:103)


NewDiskPersistence is a function that performs operations based on the provided parameters and may return an error.


```go
func NewDiskPersistence((*DiskPersistence, error)) (*DiskPersistence, error)
```


**Тип запроса:** DiskPersistence


```json
{
  "primaryDir": "string",
  "archiveDir": "string",
  "eventsPerFile": 0,
  "writeBufferSize": 0,
  "retention": {},
  "meta": null,
  "broadcast": {},
  "logfi": null,
  "curSeq": 0,
  "uidCache": null,
  "didCache": null,
  "writers": null,
  "buffers": null,
  "scratch": [],
  "outbuf": null,
  "evtbuf": [],
  "shutdown": {},
  "lk": {}
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** DiskPersistence


```json
{
  "primaryDir": "string",
  "archiveDir": "string",
  "eventsPerFile": 0,
  "writeBufferSize": 0,
  "retention": {},
  "meta": null,
  "broadcast": {},
  "logfi": null,
  "curSeq": 0,
  "uidCache": null,
  "didCache": null,
  "writers": null,
  "buffers": null,
  "scratch": [],
  "outbuf": null,
  "evtbuf": [],
  "shutdown": {},
  "lk": {}
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DiskPersistence`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:103`



---


[function] name: Persist file: cmd/relay/stream/persist/diskpersist/diskpersist.go:548 returns_error: нет description: Persist implements persist.EventPersistence
Persist may mutate contents of xevt and what it points to


### Persist (cmd/relay/stream/persist/diskpersist/diskpersist.go:548)


Persist implements persist.EventPersistence
Persist may mutate contents of xevt and what it points to


```go
func (dp *DiskPersistence) Persist((ctx context.Context, xevt *stream.XRPCStreamEvent)) (ctx context.Context, xevt *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** xevt


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:548`



---


[function] name: Playback file: cmd/relay/stream/persist/diskpersist/diskpersist.go:691 returns_error: да description: —


### Playback (cmd/relay/stream/persist/diskpersist/diskpersist.go:691)


Playback is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) Playback((ctx context.Context, since int64, cb func(*stream.XRPCStreamEvent) error)) (ctx context.Context, since int64, cb func(*stream.XRPCStreamEvent) error)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** since


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `since int64`, `cb func(*stream.XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:691`



---


[function] name: PlaybackLogfiles file: cmd/relay/stream/persist/diskpersist/diskpersist.go:732 returns_error: да description: —


### PlaybackLogfiles (cmd/relay/stream/persist/diskpersist/diskpersist.go:732)


PlaybackLogfiles is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) PlaybackLogfiles((*int64, error)) (*int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:732`



---


[function] name: Read file: cmd/relay/stream/persist/diskpersist/diskpersist.go:912 returns_error: да description: —


### Read (cmd/relay/stream/persist/diskpersist/diskpersist.go:912)


Read is a method that performs operations based on the provided parameters and may return an error.


```go
func (zr *zeroReader) Read((n int, err error)) (n int, err error)
```


**Тип ответа:** n


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


*Типы возврата:* `n int`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:912`



---


[function] name: SetEventBroadcaster file: cmd/relay/stream/persist/diskpersist/diskpersist.go:997 returns_error: нет description: —


### SetEventBroadcaster (cmd/relay/stream/persist/diskpersist/diskpersist.go:997)


SetEventBroadcaster is a method that updates data based on the provided parameters and returns (f func(*stream.XRPCStreamEvent)).


```go
func (dp *DiskPersistence) SetEventBroadcaster((f func(*stream.XRPCStreamEvent))) (f func(*stream.XRPCStreamEvent))
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** f


```json
{
  "Logger": null,
  "PLCHost": "string",
  "PLCRateLimit": 0,
  "RedisURL": "string",
  "Bind": "string",
  "DisableRefresh": false
}
```


*Определено в:* `cmd/bluepages/server.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:997`



---


[function] name: SetUidSource file: cmd/relay/stream/persist/diskpersist/diskpersist.go:177 returns_error: нет description: —


### SetUidSource (cmd/relay/stream/persist/diskpersist/diskpersist.go:177)


SetUidSource is a method that updates data based on the provided parameters and returns (uids UidSource).


```go
func (dp *DiskPersistence) SetUidSource((uids UidSource)) (uids UidSource)
```


**Тип ответа:** uids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** UidSource


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:177`



---


[function] name: Shutdown file: cmd/relay/stream/persist/diskpersist/diskpersist.go:988 returns_error: нет description: —


### Shutdown (cmd/relay/stream/persist/diskpersist/diskpersist.go:988)


Shutdown is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (dp *DiskPersistence) Shutdown((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:988`



---


[function] name: TakeDownRepo file: cmd/relay/stream/persist/diskpersist/diskpersist.go:857 returns_error: нет description: —


### TakeDownRepo (cmd/relay/stream/persist/diskpersist/diskpersist.go:857)


TakeDownRepo is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid uint64).


```go
func (dp *DiskPersistence) TakeDownRepo((ctx context.Context, uid uint64)) (ctx context.Context, uid uint64)
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


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:857`



---


[function] name: addJobToQueue file: cmd/relay/stream/persist/diskpersist/diskpersist.go:334 returns_error: нет description: —


### addJobToQueue (cmd/relay/stream/persist/diskpersist/diskpersist.go:334)


addJobToQueue is a method that performs operations based on the provided parameters and returns (ctx context.Context, job persistJob).


```go
func (dp *DiskPersistence) addJobToQueue((ctx context.Context, job persistJob)) (ctx context.Context, job persistJob)
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


**Тип ответа:** job


```json
{
  "repo": "string",
  "state": "string",
  "rev": "string",
  "lk": {},
  "bufferedOps": [],
  "dbj": null,
  "db": null,
  "createdAt": {},
  "updatedAt": {},
  "retryCount": 0,
  "retryAfter": "2023-01-01T00:00:00Z"
}
```


*Определено в:* `backfill/gormstore.go`


**Тип ответа:** persistJob


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:334`



---


[function] name: deleteEventsForUser file: cmd/relay/stream/persist/diskpersist/diskpersist.go:919 returns_error: нет description: —


### deleteEventsForUser (cmd/relay/stream/persist/diskpersist/diskpersist.go:919)


deleteEventsForUser is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid uint64, fn string).


```go
func (dp *DiskPersistence) deleteEventsForUser((ctx context.Context, uid uint64, fn string)) (ctx context.Context, uid uint64, fn string)
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


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:919`



---


[function] name: doPersist file: cmd/relay/stream/persist/diskpersist/diskpersist.go:498 returns_error: нет description: —


### doPersist (cmd/relay/stream/persist/diskpersist/diskpersist.go:498)


doPersist is a method that performs operations based on the provided parameters and returns (ctx context.Context, pjob persistJob).


```go
func (dp *DiskPersistence) doPersist((ctx context.Context, pjob persistJob)) (ctx context.Context, pjob persistJob)
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


**Тип ответа:** pjob


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** persistJob


```json
{
  "Bytes": [],
  "Evt": null,
  "Buffer": null
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:498`



---


[function] name: flushLog file: cmd/relay/stream/persist/diskpersist/diskpersist.go:371 returns_error: нет description: —


### flushLog (cmd/relay/stream/persist/diskpersist/diskpersist.go:371)


flushLog is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (dp *DiskPersistence) flushLog((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:371`



---


[function] name: flushRoutine file: cmd/relay/stream/persist/diskpersist/diskpersist.go:352 returns_error: нет description: —


### flushRoutine (cmd/relay/stream/persist/diskpersist/diskpersist.go:352)


flushRoutine is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DiskPersistence) flushRoutine(()) ()
```


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:352`



---


[function] name: forEachShardWithUserEvents file: cmd/relay/stream/persist/diskpersist/diskpersist.go:876 returns_error: да description: —


### forEachShardWithUserEvents (cmd/relay/stream/persist/diskpersist/diskpersist.go:876)


forEachShardWithUserEvents is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) forEachShardWithUserEvents((ctx context.Context, uid uint64, cb func(context.Context, string) error)) (ctx context.Context, uid uint64, cb func(context.Context, string) error)
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


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `uid uint64`, `cb func(context.Context`, `string) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:876`



---


[function] name: garbageCollect file: cmd/relay/stream/persist/diskpersist/diskpersist.go:440 returns_error: нет description: —


### garbageCollect (cmd/relay/stream/persist/diskpersist/diskpersist.go:440)


garbageCollect is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (dp *DiskPersistence) garbageCollect((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:440`



---


[function] name: garbageCollectRoutine file: cmd/relay/stream/persist/diskpersist/diskpersist.go:396 returns_error: нет description: —


### garbageCollectRoutine (cmd/relay/stream/persist/diskpersist/diskpersist.go:396)


garbageCollectRoutine is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DiskPersistence) garbageCollectRoutine(()) ()
```


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:396`



---


[function] name: initLogFile file: cmd/relay/stream/persist/diskpersist/diskpersist.go:229 returns_error: нет description: —


### initLogFile (cmd/relay/stream/persist/diskpersist/diskpersist.go:229)


initLogFile is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DiskPersistence) initLogFile(()) ()
```


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:229`



---


[function] name: mutateUserEventsInLog file: cmd/relay/stream/persist/diskpersist/diskpersist.go:923 returns_error: нет description: —


### mutateUserEventsInLog (cmd/relay/stream/persist/diskpersist/diskpersist.go:923)


mutateUserEventsInLog is a method that performs operations based on the provided parameters and returns (ctx context.Context, uid uint64, fn string, flag uint32, zeroEvts bool).


```go
func (dp *DiskPersistence) mutateUserEventsInLog((ctx context.Context, uid uint64, fn string, flag uint32, zeroEvts bool)) (ctx context.Context, uid uint64, fn string, flag uint32, zeroEvts bool)
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


**Тип ответа:** uid


```json
{
  "guide": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flag


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** zeroEvts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:923`



---


[function] name: postDoNotEmit file: cmd/relay/stream/persist/diskpersist/diskpersist.go:750 returns_error: нет description: —


### postDoNotEmit (cmd/relay/stream/persist/diskpersist/diskpersist.go:750)


postDoNotEmit is a function that performs operations based on the provided parameters and returns (flags uint32).


```go
func postDoNotEmit((flags uint32)) (flags uint32)
```


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:750`



---


[function] name: readEventsFrom file: cmd/relay/stream/persist/diskpersist/diskpersist.go:758 returns_error: да description: —


### readEventsFrom (cmd/relay/stream/persist/diskpersist/diskpersist.go:758)


readEventsFrom is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) readEventsFrom((*int64, error)) (*int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:758`



---


[function] name: readHeader file: cmd/relay/stream/persist/diskpersist/diskpersist.go:628 returns_error: да description: —


### readHeader (cmd/relay/stream/persist/diskpersist/diskpersist.go:628)


readHeader is a function that performs operations based on the provided parameters and may return an error.


```go
func readHeader((*evtHeader, error)) (*evtHeader, error)
```


**Тип запроса:** evtHeader


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** evtHeader


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*evtHeader`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:628`



---


[function] name: refMaybeHasUserEvents file: cmd/relay/stream/persist/diskpersist/diskpersist.go:905 returns_error: да description: —


### refMaybeHasUserEvents (cmd/relay/stream/persist/diskpersist/diskpersist.go:905)


refMaybeHasUserEvents is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) refMaybeHasUserEvents((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:905`



---


[function] name: resumeLog file: cmd/relay/stream/persist/diskpersist/diskpersist.go:181 returns_error: нет description: —


### resumeLog (cmd/relay/stream/persist/diskpersist/diskpersist.go:181)


resumeLog is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DiskPersistence) resumeLog(()) ()
```


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:181`



---


[function] name: scanForLastSeq file: cmd/relay/stream/persist/diskpersist/diskpersist.go:279 returns_error: да description: —


### scanForLastSeq (cmd/relay/stream/persist/diskpersist/diskpersist.go:279)


scanForLastSeq is a function that performs operations based on the provided parameters and may return an error.


```go
func scanForLastSeq((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:279`



---


[function] name: swapLog file: cmd/relay/stream/persist/diskpersist/diskpersist.go:255 returns_error: нет description: swapLog swaps the current log file out for a new empty one
must only be called while holding dp.lk


### swapLog (cmd/relay/stream/persist/diskpersist/diskpersist.go:255)


swapLog swaps the current log file out for a new empty one
must only be called while holding dp.lk


```go
func (dp *DiskPersistence) swapLog((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:255`



---


[function] name: uidForDid file: cmd/relay/stream/persist/diskpersist/diskpersist.go:673 returns_error: да description: —


### uidForDid (cmd/relay/stream/persist/diskpersist/diskpersist.go:673)


uidForDid is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DiskPersistence) uidForDid((uint64, error)) (uint64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `uint64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:673`



---


[function] name: writeHeader file: cmd/relay/stream/persist/diskpersist/diskpersist.go:654 returns_error: нет description: —


### writeHeader (cmd/relay/stream/persist/diskpersist/diskpersist.go:654)


writeHeader is a method that performs operations based on the provided parameters and returns (ctx context.Context, flags uint32, kind uint32, l uint32, usr uint64, seq int64).


```go
func (dp *DiskPersistence) writeHeader((ctx context.Context, flags uint32, kind uint32, l uint32, usr uint64, seq int64)) (ctx context.Context, flags uint32, kind uint32, l uint32, usr uint64, seq int64)
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


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** usr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** seq


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/stream/persist/diskpersist/diskpersist.go:654`




## cmd/relay/stream/schedulers/parallel/parallel.go


📄 Исходный файл: `cmd/relay/stream/schedulers/parallel/parallel.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [AddWork](#addwork-cmdrelaystreamschedulersparallelparallelgo98) `:98`

- 🔗 [LastSeq](#lastseq-cmdrelaystreamschedulersparallelparallelgo181) `:181`

- 🔗 [NewScheduler](#newscheduler-cmdrelaystreamschedulersparallelparallelgo43) `:43`

- 🔗 [Shutdown](#shutdown-cmdrelaystreamschedulersparallelparallelgo74) `:74`

- 🔗 [worker](#worker-cmdrelaystreamschedulersparallelparallelgo130) `:130`


</details>


[function] name: AddWork file: cmd/relay/stream/schedulers/parallel/parallel.go:98 returns_error: нет description: —


### AddWork (cmd/relay/stream/schedulers/parallel/parallel.go:98)


AddWork is a method that creates new data based on the provided parameters and returns (ctx context.Context, repo string, val *stream.XRPCStreamEvent).


```go
func (p *Scheduler) AddWork((ctx context.Context, repo string, val *stream.XRPCStreamEvent)) (ctx context.Context, repo string, val *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/schedulers/parallel/parallel.go:98`



---


[function] name: LastSeq file: cmd/relay/stream/schedulers/parallel/parallel.go:181 returns_error: нет description: —


### LastSeq (cmd/relay/stream/schedulers/parallel/parallel.go:181)


LastSeq is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) LastSeq(()) ()
```


📍 *Расположение:* `cmd/relay/stream/schedulers/parallel/parallel.go:181`



---


[function] name: NewScheduler file: cmd/relay/stream/schedulers/parallel/parallel.go:43 returns_error: да description: —


### NewScheduler (cmd/relay/stream/schedulers/parallel/parallel.go:43)


NewScheduler is a function that performs operations based on the provided parameters and may return an error.


```go
func NewScheduler((maxC, maxQ int, ident string, do func(context.Context, *stream.XRPCStreamEvent) error)) (maxC, maxQ int, ident string, do func(context.Context, *stream.XRPCStreamEvent) error)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** maxC


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxQ


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ident


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** do


```json
{
  "DIDs": [],
  "Cursor": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


**Тип ответа:** func


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


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `maxC`, `maxQ int`, `ident string`, `do func(context.Context`, `*stream.XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/schedulers/parallel/parallel.go:43`



---


[function] name: Shutdown file: cmd/relay/stream/schedulers/parallel/parallel.go:74 returns_error: нет description: —


### Shutdown (cmd/relay/stream/schedulers/parallel/parallel.go:74)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) Shutdown(()) ()
```


📍 *Расположение:* `cmd/relay/stream/schedulers/parallel/parallel.go:74`



---


[function] name: worker file: cmd/relay/stream/schedulers/parallel/parallel.go:130 returns_error: нет description: —


### worker (cmd/relay/stream/schedulers/parallel/parallel.go:130)


worker is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) worker(()) ()
```


📍 *Расположение:* `cmd/relay/stream/schedulers/parallel/parallel.go:130`




## cmd/relay/stream/schedulers/sequential/sequential.go


📄 Исходный файл: `cmd/relay/stream/schedulers/sequential/sequential.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddWork](#addwork-cmdrelaystreamschedulerssequentialsequentialgo48) `:48`

- 🔗 [NewScheduler](#newscheduler-cmdrelaystreamschedulerssequentialsequentialgo27) `:27`

- 🔗 [Shutdown](#shutdown-cmdrelaystreamschedulerssequentialsequentialgo44) `:44`


</details>


[function] name: AddWork file: cmd/relay/stream/schedulers/sequential/sequential.go:48 returns_error: нет description: —


### AddWork (cmd/relay/stream/schedulers/sequential/sequential.go:48)


AddWork is a method that creates new data based on the provided parameters and returns (ctx context.Context, repo string, val *stream.XRPCStreamEvent).


```go
func (s *Scheduler) AddWork((ctx context.Context, repo string, val *stream.XRPCStreamEvent)) (ctx context.Context, repo string, val *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


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


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/stream/schedulers/sequential/sequential.go:48`



---


[function] name: NewScheduler file: cmd/relay/stream/schedulers/sequential/sequential.go:27 returns_error: да description: —


### NewScheduler (cmd/relay/stream/schedulers/sequential/sequential.go:27)


NewScheduler is a function that performs operations based on the provided parameters and may return an error.


```go
func NewScheduler((ident string, do func(context.Context, *stream.XRPCStreamEvent) error)) (ident string, do func(context.Context, *stream.XRPCStreamEvent) error)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** ident


```json
{
  "Updated": {},
  "Identity": null,
  "Err": {}
}
```


*Определено в:* `atproto/identity/redisdir/redis_directory.go`


**Тип ответа:** do


```json
{
  "DIDs": [],
  "Cursor": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


**Тип ответа:** func


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


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ident string`, `do func(context.Context`, `*stream.XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/stream/schedulers/sequential/sequential.go:27`



---


[function] name: Shutdown file: cmd/relay/stream/schedulers/sequential/sequential.go:44 returns_error: нет description: —


### Shutdown (cmd/relay/stream/schedulers/sequential/sequential.go:44)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) Shutdown(()) ()
```


📍 *Расположение:* `cmd/relay/stream/schedulers/sequential/sequential.go:44`




## cmd/relay/stubs.go


📄 Исходный файл: `cmd/relay/stubs.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [HandleComAtprotoSyncGetHostStatus](#handlecomatprotosyncgethoststatus-cmdrelaystubsgo80) `:80`

- 🔗 [HandleComAtprotoSyncGetLatestCommit](#handlecomatprotosyncgetlatestcommit-cmdrelaystubsgo178) `:178`

- 🔗 [HandleComAtprotoSyncGetRepo](#handlecomatprotosyncgetrepo-cmdrelaystubsgo128) `:128`

- 🔗 [HandleComAtprotoSyncGetRepoStatus](#handlecomatprotosyncgetrepostatus-cmdrelaystubsgo160) `:160`

- 🔗 [HandleComAtprotoSyncListHosts](#handlecomatprotosynclisthosts-cmdrelaystubsgo47) `:47`

- 🔗 [HandleComAtprotoSyncListRepos](#handlecomatprotosynclistrepos-cmdrelaystubsgo93) `:93`

- 🔗 [HandleComAtprotoSyncRequestCrawl](#handlecomatprotosyncrequestcrawl-cmdrelaystubsgo34) `:34`

- 🔗 [HandleComAtprotoSyncSubscribeRepos](#handlecomatprotosyncsubscriberepos-cmdrelaystubsgo17) `:17`


</details>


[function] name: HandleComAtprotoSyncGetHostStatus file: cmd/relay/stubs.go:80 returns_error: нет description: —


### HandleComAtprotoSyncGetHostStatus (cmd/relay/stubs.go:80)


HandleComAtprotoSyncGetHostStatus is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) HandleComAtprotoSyncGetHostStatus((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/stubs.go:80`



---


[function] name: HandleComAtprotoSyncGetLatestCommit file: cmd/relay/stubs.go:178 returns_error: нет description: —


### HandleComAtprotoSyncGetLatestCommit (cmd/relay/stubs.go:178)


HandleComAtprotoSyncGetLatestCommit is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) HandleComAtprotoSyncGetLatestCommit((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/stubs.go:178`



---


[function] name: HandleComAtprotoSyncGetRepo file: cmd/relay/stubs.go:128 returns_error: нет description: does a simple HTTP redirect to getRepo on the account's PDS.

NOTE: currently does not check account status locally; a t


### HandleComAtprotoSyncGetRepo (cmd/relay/stubs.go:128)


does a simple HTTP redirect to getRepo on the account's PDS.

NOTE: currently does not check account status locally; a takendown account will still redirect. this saves a database lookup.


```go
func (s *Service) HandleComAtprotoSyncGetRepo((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/stubs.go:128`



---


[function] name: HandleComAtprotoSyncGetRepoStatus file: cmd/relay/stubs.go:160 returns_error: нет description: —


### HandleComAtprotoSyncGetRepoStatus (cmd/relay/stubs.go:160)


HandleComAtprotoSyncGetRepoStatus is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) HandleComAtprotoSyncGetRepoStatus((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/stubs.go:160`



---


[function] name: HandleComAtprotoSyncListHosts file: cmd/relay/stubs.go:47 returns_error: нет description: —


### HandleComAtprotoSyncListHosts (cmd/relay/stubs.go:47)


HandleComAtprotoSyncListHosts is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) HandleComAtprotoSyncListHosts((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/stubs.go:47`



---


[function] name: HandleComAtprotoSyncListRepos file: cmd/relay/stubs.go:93 returns_error: нет description: —


### HandleComAtprotoSyncListRepos (cmd/relay/stubs.go:93)


HandleComAtprotoSyncListRepos is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) HandleComAtprotoSyncListRepos((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/stubs.go:93`



---


[function] name: HandleComAtprotoSyncRequestCrawl file: cmd/relay/stubs.go:34 returns_error: нет description: —


### HandleComAtprotoSyncRequestCrawl (cmd/relay/stubs.go:34)


HandleComAtprotoSyncRequestCrawl is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) HandleComAtprotoSyncRequestCrawl((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/stubs.go:34`



---


[function] name: HandleComAtprotoSyncSubscribeRepos file: cmd/relay/stubs.go:17 returns_error: нет description: —


### HandleComAtprotoSyncSubscribeRepos (cmd/relay/stubs.go:17)


HandleComAtprotoSyncSubscribeRepos is a method that handles or processes requests based on the provided parameters and returns (c echo.Context).


```go
func (s *Service) HandleComAtprotoSyncSubscribeRepos((c echo.Context)) (c echo.Context)
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


📍 *Расположение:* `cmd/relay/stubs.go:17`




## cmd/relay/testing/consumer.go


📄 Исходный файл: `cmd/relay/testing/consumer.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Clear](#clear-cmdrelaytestingconsumergo111) `:111`

- 🔗 [Connect](#connect-cmdrelaytestingconsumergo69) `:69`

- 🔗 [ConsumeEvents](#consumeevents-cmdrelaytestingconsumergo126) `:126`

- 🔗 [Count](#count-cmdrelaytestingconsumergo105) `:105`

- 🔗 [NewConsumer](#newconsumer-cmdrelaytestingconsumergo27) `:27`

- 🔗 [Shutdown](#shutdown-cmdrelaytestingconsumergo117) `:117`

- 🔗 [eventCallbacks](#eventcallbacks-cmdrelaytestingconsumergo35) `:35`


</details>


[function] name: Clear file: cmd/relay/testing/consumer.go:111 returns_error: нет description: —


### Clear (cmd/relay/testing/consumer.go:111)


Clear is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Consumer) Clear(()) ()
```


📍 *Расположение:* `cmd/relay/testing/consumer.go:111`



---


[function] name: Connect file: cmd/relay/testing/consumer.go:69 returns_error: нет description: —


### Connect (cmd/relay/testing/consumer.go:69)


Connect is a method that performs operations based on the provided parameters and returns (ctx context.Context, cursor int).


```go
func (c *Consumer) Connect((ctx context.Context, cursor int)) (ctx context.Context, cursor int)
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


**Тип ответа:** cursor


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/testing/consumer.go:69`



---


[function] name: ConsumeEvents file: cmd/relay/testing/consumer.go:126 returns_error: да description: connects to host and consumes 'count' events, then returns them. will try up to 'c.Timeout', and error if not enough eve


### ConsumeEvents (cmd/relay/testing/consumer.go:126)


connects to host and consumes 'count' events, then returns them. will try up to 'c.Timeout', and error if not enough events are seen

cursor: pass -1 to consume from current


```go
func (c *Consumer) ConsumeEvents(([]*stream.XRPCStreamEvent, error)) ([]*stream.XRPCStreamEvent, error)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*stream.XRPCStreamEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/testing/consumer.go:126`



---


[function] name: Count file: cmd/relay/testing/consumer.go:105 returns_error: нет description: —


### Count (cmd/relay/testing/consumer.go:105)


Count is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Consumer) Count(()) ()
```


📍 *Расположение:* `cmd/relay/testing/consumer.go:105`



---


[function] name: NewConsumer file: cmd/relay/testing/consumer.go:27 returns_error: нет description: —


### NewConsumer (cmd/relay/testing/consumer.go:27)


NewConsumer is a function that performs operations based on the provided parameters and returns (host string).


```go
func NewConsumer((host string)) (host string)
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


📍 *Расположение:* `cmd/relay/testing/consumer.go:27`



---


[function] name: Shutdown file: cmd/relay/testing/consumer.go:117 returns_error: нет description: —


### Shutdown (cmd/relay/testing/consumer.go:117)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Consumer) Shutdown(()) ()
```


📍 *Расположение:* `cmd/relay/testing/consumer.go:117`



---


[function] name: eventCallbacks file: cmd/relay/testing/consumer.go:35 returns_error: нет description: —


### eventCallbacks (cmd/relay/testing/consumer.go:35)


eventCallbacks is a method that performs operations based on the provided parameters and returns ().


```go
func (c *Consumer) eventCallbacks(()) ()
```


📍 *Расположение:* `cmd/relay/testing/consumer.go:35`




## cmd/relay/testing/producer.go


📄 Исходный файл: `cmd/relay/testing/producer.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [AddSubscriber](#addsubscriber-cmdrelaytestingproducergo136) `:136`

- 🔗 [Emit](#emit-cmdrelaytestingproducergo150) `:150`

- 🔗 [ListenRandom](#listenrandom-cmdrelaytestingproducergo108) `:108`

- 🔗 [NewProducer](#newproducer-cmdrelaytestingproducergo29) `:29`

- 🔗 [Shutdown](#shutdown-cmdrelaytestingproducergo127) `:127`

- 🔗 [handleSubscribeRepos](#handlesubscriberepos-cmdrelaytestingproducergo44) `:44`


</details>


[function] name: AddSubscriber file: cmd/relay/testing/producer.go:136 returns_error: да description: —


### AddSubscriber (cmd/relay/testing/producer.go:136)


AddSubscriber is a method that creates new data based on the provided parameters and may return an error.


```go
func (p *Producer) AddSubscriber((<-chan *stream.XRPCStreamEvent, error)) (<-chan *stream.XRPCStreamEvent, error)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** chan


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `<-chan *stream.XRPCStreamEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/testing/producer.go:136`



---


[function] name: Emit file: cmd/relay/testing/producer.go:150 returns_error: нет description: —


### Emit (cmd/relay/testing/producer.go:150)


Emit is a method that performs operations based on the provided parameters and returns (evt *stream.XRPCStreamEvent).


```go
func (p *Producer) Emit((evt *stream.XRPCStreamEvent)) (evt *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/testing/producer.go:150`



---


[function] name: ListenRandom file: cmd/relay/testing/producer.go:108 returns_error: нет description: —


### ListenRandom (cmd/relay/testing/producer.go:108)


ListenRandom is a method that lists or finds data based on the provided parameters and returns ().


```go
func (p *Producer) ListenRandom(()) ()
```


📍 *Расположение:* `cmd/relay/testing/producer.go:108`



---


[function] name: NewProducer file: cmd/relay/testing/producer.go:29 returns_error: нет description: —


### NewProducer (cmd/relay/testing/producer.go:29)


NewProducer is a function that performs operations based on the provided parameters and returns ().


```go
func NewProducer(()) ()
```


📍 *Расположение:* `cmd/relay/testing/producer.go:29`



---


[function] name: Shutdown file: cmd/relay/testing/producer.go:127 returns_error: нет description: —


### Shutdown (cmd/relay/testing/producer.go:127)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Producer) Shutdown(()) ()
```


📍 *Расположение:* `cmd/relay/testing/producer.go:127`



---


[function] name: handleSubscribeRepos file: cmd/relay/testing/producer.go:44 returns_error: нет description: —


### handleSubscribeRepos (cmd/relay/testing/producer.go:44)


handleSubscribeRepos is a method that performs operations based on the provided parameters and returns (resp http.ResponseWriter, req *http.Request).


```go
func (p *Producer) handleSubscribeRepos((resp http.ResponseWriter, req *http.Request)) (resp http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Host": "string",
  "Hosts": []
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** resp


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


📍 *Расположение:* `cmd/relay/testing/producer.go:44`




## cmd/relay/testing/runner.go


📄 Исходный файл: `cmd/relay/testing/runner.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [EqualEvents](#equalevents-cmdrelaytestingrunnergo180) `:180`

- 🔗 [LoadAndRunScenario](#loadandrunscenario-cmdrelaytestingrunnergo84) `:84`

- 🔗 [LoadScenario](#loadscenario-cmdrelaytestingrunnergo93) `:93`

- 🔗 [MustSimpleRelay](#mustsimplerelay-cmdrelaytestingrunnergo33) `:33`

- 🔗 [RunScenario](#runscenario-cmdrelaytestingrunnergo115) `:115`

- 🔗 [handleSubscribeRepos](#handlesubscriberepos-cmdrelaytestingrunnergo26) `:26`


</details>


[function] name: EqualEvents file: cmd/relay/testing/runner.go:180 returns_error: нет description: checks if two XRPCStreamEvent are equal, ignoring sequence numbers and timestamps


### EqualEvents (cmd/relay/testing/runner.go:180)


checks if two XRPCStreamEvent are equal, ignoring sequence numbers and timestamps


```go
func EqualEvents((a, b *stream.XRPCStreamEvent)) (a, b *stream.XRPCStreamEvent)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** a


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


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


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `cmd/relay/testing/runner.go:180`



---


[function] name: LoadAndRunScenario file: cmd/relay/testing/runner.go:84 returns_error: нет description: —


### LoadAndRunScenario (cmd/relay/testing/runner.go:84)


LoadAndRunScenario is a function that performs operations based on the provided parameters and returns (ctx context.Context, fpath string).


```go
func LoadAndRunScenario((ctx context.Context, fpath string)) (ctx context.Context, fpath string)
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


**Тип ответа:** fpath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/testing/runner.go:84`



---


[function] name: LoadScenario file: cmd/relay/testing/runner.go:93 returns_error: да description: —


### LoadScenario (cmd/relay/testing/runner.go:93)


LoadScenario is a function that performs operations based on the provided parameters and may return an error.


```go
func LoadScenario((*Scenario, error)) (*Scenario, error)
```


**Тип запроса:** Scenario


```json
{
  "Description": "string",
  "Lenient": false,
  "Accounts": [],
  "Messages": []
}
```


*Определено в:* `cmd/relay/testing/scenario.go`


**Тип ответа:** Scenario


```json
{
  "Description": "string",
  "Lenient": false,
  "Accounts": [],
  "Messages": []
}
```


*Определено в:* `cmd/relay/testing/scenario.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Scenario`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/testing/runner.go:93`



---


[function] name: MustSimpleRelay file: cmd/relay/testing/runner.go:33 returns_error: нет description: —


### MustSimpleRelay (cmd/relay/testing/runner.go:33)


MustSimpleRelay is a function that performs operations based on the provided parameters and returns (dir identity.Directory, tmpd string, lenient bool).


```go
func MustSimpleRelay((dir identity.Directory, tmpd string, lenient bool)) (dir identity.Directory, tmpd string, lenient bool)
```


**Тип ответа:** dir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** identity.Directory


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


**Тип ответа:** tmpd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lenient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/relay/testing/runner.go:33`



---


[function] name: RunScenario file: cmd/relay/testing/runner.go:115 returns_error: нет description: —


### RunScenario (cmd/relay/testing/runner.go:115)


RunScenario is a function that performs operations based on the provided parameters and returns (ctx context.Context, s *Scenario).


```go
func RunScenario((ctx context.Context, s *Scenario)) (ctx context.Context, s *Scenario)
```


**Тип запроса:** Scenario


```json
{
  "Description": "string",
  "Lenient": false,
  "Accounts": [],
  "Messages": []
}
```


*Определено в:* `cmd/relay/testing/scenario.go`


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


**Тип ответа:** Scenario


```json
{
  "Description": "string",
  "Lenient": false,
  "Accounts": [],
  "Messages": []
}
```


*Определено в:* `cmd/relay/testing/scenario.go`


📍 *Расположение:* `cmd/relay/testing/runner.go:115`



---


[function] name: handleSubscribeRepos file: cmd/relay/testing/runner.go:26 returns_error: нет description: —


### handleSubscribeRepos (cmd/relay/testing/runner.go:26)


handleSubscribeRepos is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func (sr *SimpleRelay) handleSubscribeRepos((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
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


📍 *Расположение:* `cmd/relay/testing/runner.go:26`




## cmd/relay/testing/scenario.go


📄 Исходный файл: `cmd/relay/testing/scenario.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [XRPCStreamEvent](#xrpcstreamevent-cmdrelaytestingscenariogo45) `:45`


</details>


[function] name: XRPCStreamEvent file: cmd/relay/testing/scenario.go:45 returns_error: да description: —


### XRPCStreamEvent (cmd/relay/testing/scenario.go:45)


XRPCStreamEvent is a method that performs operations based on the provided parameters and may return an error.


```go
func (re *RepoEventFrame) XRPCStreamEvent((*stream.XRPCStreamEvent, error)) (*stream.XRPCStreamEvent, error)
```


**Тип запроса:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Тип ответа:** stream.XRPCStreamEvent


```json
{
  "Error": null,
  "RepoCommit": null,
  "RepoSync": null,
  "RepoIdentity": null,
  "RepoInfo": null,
  "RepoAccount": null,
  "LabelLabels": null,
  "LabelInfo": null,
  "PrivUid": {},
  "PrivPdsId": 0,
  "PrivRelevantPds": [],
  "Preserialized": []
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*stream.XRPCStreamEvent`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/relay/testing/scenario.go:45`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_rainbow.md)

- [Следующая директория](cmd_sonar.md)


---

