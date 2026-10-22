---
title: Спецификация API
type: api
repo: indigo
language: ru
chunk_boundary: h4
---


# Спецификация API


## Навигация


- [К оглавлению документации](../README.md)

- [Диаграммы](../diagrams/)

- [Импорты](imports.md)

- [Структуры и типы](structures.md)

- [Функции](functions.md)

- [Спецификация API](api.md)

- [Тестирование](tests.md)

- [Используемые библиотеки](libraries.md)


---


## Меню по файлам


- 📄 [atproto/auth/oauth/cmd/oauth-web-demo/main.go](#atprotoauthoauthcmdoauth-web-demomaingo)

- 📄 [atproto/auth/oauth/doc.go](#atprotoauthoauthdocgo)

- 📄 [cmd/bluepages/server.go](#cmdbluepagesservergo)

- 📄 [cmd/collectiondir/serve.go](#cmdcollectiondirservego)

- 📄 [cmd/hepa/server.go](#cmdhepaservergo)

- 📄 [cmd/relay/service.go](#cmdrelayservicego)

- 📄 [cmd/relay/testing/producer.go](#cmdrelaytestingproducergo)

- 📄 [cmd/relay/testing/runner.go](#cmdrelaytestingrunnergo)

- 📄 [cmd/tap/main.go](#cmdtapmaingo)

- 📄 [repomgr/repomgr.go](#repomgrrepomgrgo)

- 📄 [search/server.go](#searchservergo)

- 📄 [splitter/splitter.go](#splittersplittergo)


---


## gRPC методы


### repomgr/repomgr.go


📄 Исходный файл: `repomgr/repomgr.go`


<details open>
<summary><b>Методы в этом файле (1)</b></summary>


- 🔗 [processNewRepo](#processnewrepo)


</details>



---


[grpc] method: processNewRepo request: string response: e file: repomgr/repomgr.go


#### processNewRepo


processNewRepo is a gRPC method that accepts string and returns e.


**Тип запроса:** `string`


*Определение типа не найдено в проекте.*



**Тип ответа:** `e`


*Тип ответа определён в:* `cmd/netsync/main.go`



**Ответ (JSON):**

```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


📍 *Обработчик определён в: `repomgr/repomgr.go`*


## REST эндпоинты


### atproto/auth/oauth/cmd/oauth-web-demo/main.go


📄 Исходный файл: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`


<details open>
<summary><b>Эндпоинты в этом файле (10)</b></summary>


- 🔗 [HandleFunc GET /](#handlefunc-get)

- 🔗 [HandleFunc GET /bsky/post](#handlefunc-get-bskypost)

- 🔗 [HandleFunc GET /oauth/callback](#handlefunc-get-oauthcallback)

- 🔗 [HandleFunc GET /oauth/client-metadata.json](#handlefunc-get-oauthclient-metadatajson)

- 🔗 [HandleFunc GET /oauth/jwks.json](#handlefunc-get-oauthjwksjson)

- 🔗 [HandleFunc GET /oauth/login](#handlefunc-get-oauthlogin)

- 🔗 [HandleFunc GET /oauth/logout](#handlefunc-get-oauthlogout)

- 🔗 [HandleFunc GET /oauth/refresh](#handlefunc-get-oauthrefresh)

- 🔗 [HandleFunc POST /bsky/post](#handlefunc-post-bskypost)

- 🔗 [HandleFunc POST /oauth/login](#handlefunc-post-oauthlogin)


</details>



---


[rest] method: HandleFunc path: GET / handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc GET /


HandleFunc GET / endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: GET /bsky/post handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc GET /bsky/post


HandleFunc GET /bsky/post endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: GET /oauth/callback handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc GET /oauth/callback


HandleFunc GET /oauth/callback endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: GET /oauth/client-metadata.json handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc GET /oauth/client-metadata.json


HandleFunc GET /oauth/client-metadata.json endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: GET /oauth/jwks.json handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc GET /oauth/jwks.json


HandleFunc GET /oauth/jwks.json endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: GET /oauth/login handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc GET /oauth/login


HandleFunc GET /oauth/login endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: GET /oauth/logout handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc GET /oauth/logout


HandleFunc GET /oauth/logout endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: GET /oauth/refresh handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc GET /oauth/refresh


HandleFunc GET /oauth/refresh endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: POST /bsky/post handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc POST /bsky/post


HandleFunc POST /bsky/post endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*



---


[rest] method: HandleFunc path: POST /oauth/login handler: srv file: atproto/auth/oauth/cmd/oauth-web-demo/main.go


#### HandleFunc POST /oauth/login


HandleFunc POST /oauth/login endpoint handled by srv.


**Handler:** `srv`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/cmd/oauth-web-demo/main.go`*


### atproto/auth/oauth/doc.go


📄 Исходный файл: `atproto/auth/oauth/doc.go`


<details open>
<summary><b>Эндпоинты в этом файле (3)</b></summary>


- 🔗 [HandleFunc GET /client-metadata.json](#handlefunc-get-client-metadatajson)

- 🔗 [HandleFunc GET /oauth/callback](#handlefunc-get-oauthcallback)

- 🔗 [HandleFunc GET /oauth/login](#handlefunc-get-oauthlogin)


</details>



---


[rest] method: HandleFunc path: GET /client-metadata.json handler: HandleClientMetadata file: atproto/auth/oauth/doc.go


#### HandleFunc GET /client-metadata.json


HandleFunc GET /client-metadata.json endpoint handled by HandleClientMetadata.


**Handler:** `HandleClientMetadata`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/doc.go`*



---


[rest] method: HandleFunc path: GET /oauth/callback handler: HandleOAuthCallback file: atproto/auth/oauth/doc.go


#### HandleFunc GET /oauth/callback


HandleFunc GET /oauth/callback endpoint handled by HandleOAuthCallback.


**Handler:** `HandleOAuthCallback`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/doc.go`*



---


[rest] method: HandleFunc path: GET /oauth/login handler: HandleLogin file: atproto/auth/oauth/doc.go


#### HandleFunc GET /oauth/login


HandleFunc GET /oauth/login endpoint handled by HandleLogin.


**Handler:** `HandleLogin`

**Router:** net/http


📍 *Определено в: `atproto/auth/oauth/doc.go`*


### cmd/bluepages/server.go


📄 Исходный файл: `cmd/bluepages/server.go`


<details open>
<summary><b>Эндпоинты в этом файле (6)</b></summary>


- 🔗 [GET /](#get)

- 🔗 [GET /_health](#get-_health)

- 🔗 [GET /xrpc/com.atproto.identity.resolveDid](#get-xrpccomatprotoidentityresolvedid)

- 🔗 [GET /xrpc/com.atproto.identity.resolveHandle](#get-xrpccomatprotoidentityresolvehandle)

- 🔗 [GET /xrpc/com.atproto.identity.resolveIdentity](#get-xrpccomatprotoidentityresolveidentity)

- 🔗 [POST /xrpc/com.atproto.identity.refreshIdentity](#post-xrpccomatprotoidentityrefreshidentity)


</details>



---


[rest] method: GET path: / handler: srv file: cmd/bluepages/server.go


#### GET /


GET / endpoint handled by srv. Retrieves data from the server.


**Handler:** `srv`

**Router:** echo


📍 *Определено в: `cmd/bluepages/server.go`*



---


[rest] method: GET path: /_health handler: srv file: cmd/bluepages/server.go


#### GET /_health


GET /_health endpoint handled by srv. Retrieves data from the server.


**Handler:** `srv`

**Router:** echo


📍 *Определено в: `cmd/bluepages/server.go`*



---


[rest] method: GET path: /xrpc/com.atproto.identity.resolveDid handler: srv file: cmd/bluepages/server.go


#### GET /xrpc/com.atproto.identity.resolveDid


GET /xrpc/com.atproto.identity.resolveDid endpoint handled by srv. Retrieves data from the server.


**Handler:** `srv`

**Router:** echo


📍 *Определено в: `cmd/bluepages/server.go`*



---


[rest] method: GET path: /xrpc/com.atproto.identity.resolveHandle handler: srv file: cmd/bluepages/server.go


#### GET /xrpc/com.atproto.identity.resolveHandle


GET /xrpc/com.atproto.identity.resolveHandle endpoint handled by srv. Retrieves data from the server.


**Handler:** `srv`

**Router:** echo


📍 *Определено в: `cmd/bluepages/server.go`*



---


[rest] method: GET path: /xrpc/com.atproto.identity.resolveIdentity handler: srv file: cmd/bluepages/server.go


#### GET /xrpc/com.atproto.identity.resolveIdentity


GET /xrpc/com.atproto.identity.resolveIdentity endpoint handled by srv. Retrieves data from the server.


**Handler:** `srv`

**Router:** echo


📍 *Определено в: `cmd/bluepages/server.go`*



---


[rest] method: POST path: /xrpc/com.atproto.identity.refreshIdentity handler: srv file: cmd/bluepages/server.go


#### POST /xrpc/com.atproto.identity.refreshIdentity


POST /xrpc/com.atproto.identity.refreshIdentity endpoint handled by srv. Creates new resources.


**Handler:** `srv`

**Router:** echo


📍 *Определено в: `cmd/bluepages/server.go`*


### cmd/collectiondir/serve.go


📄 Исходный файл: `cmd/collectiondir/serve.go`


<details open>
<summary><b>Эндпоинты в этом файле (9)</b></summary>


- 🔗 [GET /_health](#get-_health)

- 🔗 [GET /admin/crawlStatus](#get-admincrawlstatus)

- 🔗 [GET /metrics](#get-metrics)

- 🔗 [GET /v1/getDidsForCollection](#get-v1getdidsforcollection)

- 🔗 [GET /v1/listCollections](#get-v1listcollections)

- 🔗 [GET /xrpc/com.atproto.sync.listReposByCollection](#get-xrpccomatprotosynclistreposbycollection)

- 🔗 [GET /xrpc/com.atproto.sync.requestCrawl](#get-xrpccomatprotosyncrequestcrawl)

- 🔗 [POST /admin/pds/requestCrawl](#post-adminpdsrequestcrawl)

- 🔗 [POST /xrpc/com.atproto.sync.requestCrawl](#post-xrpccomatprotosyncrequestcrawl)


</details>



---


[rest] method: GET path: /_health handler: cs file: cmd/collectiondir/serve.go


#### GET /_health


GET /_health endpoint handled by cs. Retrieves data from the server.


**Handler:** `cs`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*



---


[rest] method: GET path: /admin/crawlStatus handler: cs file: cmd/collectiondir/serve.go


#### GET /admin/crawlStatus


GET /admin/crawlStatus endpoint handled by cs. Retrieves data from the server.


**Handler:** `cs`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*



---


[rest] method: GET path: /metrics handler: echo file: cmd/collectiondir/serve.go


#### GET /metrics


GET /metrics endpoint handled by echo. Retrieves data from the server.


**Handler:** `echo`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*



---


[rest] method: GET path: /v1/getDidsForCollection handler: cs file: cmd/collectiondir/serve.go


#### GET /v1/getDidsForCollection


GET /v1/getDidsForCollection endpoint handled by cs. Retrieves data from the server.


**Handler:** `cs`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*



---


[rest] method: GET path: /v1/listCollections handler: cs file: cmd/collectiondir/serve.go


#### GET /v1/listCollections


GET /v1/listCollections endpoint handled by cs. Retrieves data from the server.


**Handler:** `cs`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.listReposByCollection handler: cs file: cmd/collectiondir/serve.go


#### GET /xrpc/com.atproto.sync.listReposByCollection


GET /xrpc/com.atproto.sync.listReposByCollection endpoint handled by cs. Retrieves data from the server.


**Handler:** `cs`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.requestCrawl handler: cs file: cmd/collectiondir/serve.go


#### GET /xrpc/com.atproto.sync.requestCrawl


GET /xrpc/com.atproto.sync.requestCrawl endpoint handled by cs. Retrieves data from the server.


**Handler:** `cs`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*



---


[rest] method: POST path: /admin/pds/requestCrawl handler: cs file: cmd/collectiondir/serve.go


#### POST /admin/pds/requestCrawl


POST /admin/pds/requestCrawl endpoint handled by cs. Creates new resources.


**Handler:** `cs`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*



---


[rest] method: POST path: /xrpc/com.atproto.sync.requestCrawl handler: cs file: cmd/collectiondir/serve.go


#### POST /xrpc/com.atproto.sync.requestCrawl


POST /xrpc/com.atproto.sync.requestCrawl endpoint handled by cs. Creates new resources.


**Handler:** `cs`

**Router:** echo


📍 *Определено в: `cmd/collectiondir/serve.go`*


### cmd/hepa/server.go


📄 Исходный файл: `cmd/hepa/server.go`


<details open>
<summary><b>Эндпоинты в этом файле (1)</b></summary>


- 🔗 [Handle /metrics](#handle-metrics)


</details>



---


[rest] method: Handle path: /metrics handler: promhttp file: cmd/hepa/server.go


#### Handle /metrics


Handle /metrics endpoint handled by promhttp.


**Handler:** `promhttp`

**Router:** net/http


📍 *Определено в: `cmd/hepa/server.go`*


### cmd/relay/service.go


📄 Исходный файл: `cmd/relay/service.go`


<details open>
<summary><b>Эндпоинты в этом файле (12)</b></summary>


- 🔗 [GET /](#get)

- 🔗 [GET /_health](#get-_health)

- 🔗 [GET /xrpc/_health](#get-xrpc_health)

- 🔗 [GET /xrpc/com.atproto.sync.getHostStatus](#get-xrpccomatprotosyncgethoststatus)

- 🔗 [GET /xrpc/com.atproto.sync.getLatestCommit](#get-xrpccomatprotosyncgetlatestcommit)

- 🔗 [GET /xrpc/com.atproto.sync.getRepo](#get-xrpccomatprotosyncgetrepo)

- 🔗 [GET /xrpc/com.atproto.sync.getRepoStatus](#get-xrpccomatprotosyncgetrepostatus)

- 🔗 [GET /xrpc/com.atproto.sync.listHosts](#get-xrpccomatprotosynclisthosts)

- 🔗 [GET /xrpc/com.atproto.sync.listRepos](#get-xrpccomatprotosynclistrepos)

- 🔗 [GET /xrpc/com.atproto.sync.subscribeRepos](#get-xrpccomatprotosyncsubscriberepos)

- 🔗 [Handle /metrics](#handle-metrics)

- 🔗 [POST /xrpc/com.atproto.sync.requestCrawl](#post-xrpccomatprotosyncrequestcrawl)


</details>



---


[rest] method: GET path: / handler: svc file: cmd/relay/service.go


#### GET /


GET / endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /_health handler: svc file: cmd/relay/service.go


#### GET /_health


GET /_health endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /xrpc/_health handler: svc file: cmd/relay/service.go


#### GET /xrpc/_health


GET /xrpc/_health endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.getHostStatus handler: svc file: cmd/relay/service.go


#### GET /xrpc/com.atproto.sync.getHostStatus


GET /xrpc/com.atproto.sync.getHostStatus endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.getLatestCommit handler: svc file: cmd/relay/service.go


#### GET /xrpc/com.atproto.sync.getLatestCommit


GET /xrpc/com.atproto.sync.getLatestCommit endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.getRepo handler: svc file: cmd/relay/service.go


#### GET /xrpc/com.atproto.sync.getRepo


GET /xrpc/com.atproto.sync.getRepo endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.getRepoStatus handler: svc file: cmd/relay/service.go


#### GET /xrpc/com.atproto.sync.getRepoStatus


GET /xrpc/com.atproto.sync.getRepoStatus endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.listHosts handler: svc file: cmd/relay/service.go


#### GET /xrpc/com.atproto.sync.listHosts


GET /xrpc/com.atproto.sync.listHosts endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.listRepos handler: svc file: cmd/relay/service.go


#### GET /xrpc/com.atproto.sync.listRepos


GET /xrpc/com.atproto.sync.listRepos endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.subscribeRepos handler: svc file: cmd/relay/service.go


#### GET /xrpc/com.atproto.sync.subscribeRepos


GET /xrpc/com.atproto.sync.subscribeRepos endpoint handled by svc. Retrieves data from the server.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: Handle path: /metrics handler: promhttp file: cmd/relay/service.go


#### Handle /metrics


Handle /metrics endpoint handled by promhttp.


**Handler:** `promhttp`

**Router:** net/http


📍 *Определено в: `cmd/relay/service.go`*



---


[rest] method: POST path: /xrpc/com.atproto.sync.requestCrawl handler: svc file: cmd/relay/service.go


#### POST /xrpc/com.atproto.sync.requestCrawl


POST /xrpc/com.atproto.sync.requestCrawl endpoint handled by svc. Creates new resources.


**Handler:** `svc`

**Router:** echo


📍 *Определено в: `cmd/relay/service.go`*


### cmd/relay/testing/producer.go


📄 Исходный файл: `cmd/relay/testing/producer.go`


<details open>
<summary><b>Эндпоинты в этом файле (1)</b></summary>


- 🔗 [GET GET /xrpc/com.atproto.sync.subscribeRepos](#get-get-xrpccomatprotosyncsubscriberepos)


</details>



---


[rest] method: GET path: GET /xrpc/com.atproto.sync.subscribeRepos handler: p file: cmd/relay/testing/producer.go


#### GET GET /xrpc/com.atproto.sync.subscribeRepos


GET GET /xrpc/com.atproto.sync.subscribeRepos endpoint handled by p. Retrieves data from the server.


**Handler:** `p`

**Router:** mux


📍 *Определено в: `cmd/relay/testing/producer.go`*


### cmd/relay/testing/runner.go


📄 Исходный файл: `cmd/relay/testing/runner.go`


<details open>
<summary><b>Эндпоинты в этом файле (1)</b></summary>


- 🔗 [GET GET /xrpc/com.atproto.sync.subscribeRepos](#get-get-xrpccomatprotosyncsubscriberepos)


</details>



---


[rest] method: GET path: GET /xrpc/com.atproto.sync.subscribeRepos handler: sr file: cmd/relay/testing/runner.go


#### GET GET /xrpc/com.atproto.sync.subscribeRepos


GET GET /xrpc/com.atproto.sync.subscribeRepos endpoint handled by sr. Retrieves data from the server.


**Handler:** `sr`

**Router:** mux


📍 *Определено в: `cmd/relay/testing/runner.go`*


### cmd/tap/main.go


📄 Исходный файл: `cmd/tap/main.go`


<details open>
<summary><b>Эндпоинты в этом файле (1)</b></summary>


- 🔗 [Handle /metrics](#handle-metrics)


</details>



---


[rest] method: Handle path: /metrics handler: promhttp file: cmd/tap/main.go


#### Handle /metrics


Handle /metrics endpoint handled by promhttp.


**Handler:** `promhttp`

**Router:** net/http


📍 *Определено в: `cmd/tap/main.go`*


### search/server.go


📄 Исходный файл: `search/server.go`


<details open>
<summary><b>Эндпоинты в этом файле (6)</b></summary>


- 🔗 [GET /](#get)

- 🔗 [GET /_health](#get-_health)

- 🔗 [GET /metrics](#get-metrics)

- 🔗 [GET /xrpc/app.bsky.unspecced.searchActorsSkeleton](#get-xrpcappbskyunspeccedsearchactorsskeleton)

- 🔗 [GET /xrpc/app.bsky.unspecced.searchPostsSkeleton](#get-xrpcappbskyunspeccedsearchpostsskeleton)

- 🔗 [Handle /metrics](#handle-metrics)


</details>



---


[rest] method: GET path: / handler: s file: search/server.go


#### GET /


GET / endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `search/server.go`*



---


[rest] method: GET path: /_health handler: s file: search/server.go


#### GET /_health


GET /_health endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `search/server.go`*



---


[rest] method: GET path: /metrics handler: echo file: search/server.go


#### GET /metrics


GET /metrics endpoint handled by echo. Retrieves data from the server.


**Handler:** `echo`

**Router:** echo


📍 *Определено в: `search/server.go`*



---


[rest] method: GET path: /xrpc/app.bsky.unspecced.searchActorsSkeleton handler: s file: search/server.go


#### GET /xrpc/app.bsky.unspecced.searchActorsSkeleton


GET /xrpc/app.bsky.unspecced.searchActorsSkeleton endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `search/server.go`*



---


[rest] method: GET path: /xrpc/app.bsky.unspecced.searchPostsSkeleton handler: s file: search/server.go


#### GET /xrpc/app.bsky.unspecced.searchPostsSkeleton


GET /xrpc/app.bsky.unspecced.searchPostsSkeleton endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `search/server.go`*



---


[rest] method: Handle path: /metrics handler: promhttp file: search/server.go


#### Handle /metrics


Handle /metrics endpoint handled by promhttp.


**Handler:** `promhttp`

**Router:** net/http


📍 *Определено в: `search/server.go`*


### splitter/splitter.go


📄 Исходный файл: `splitter/splitter.go`


<details open>
<summary><b>Эндпоинты в этом файле (31)</b></summary>


- 🔗 [GET /](#get)

- 🔗 [GET /_health](#get-_health)

- 🔗 [GET /admin/consumers/list](#get-adminconsumerslist)

- 🔗 [GET /admin/pds/list](#get-adminpdslist)

- 🔗 [GET /admin/subs/getEnabled](#get-adminsubsgetenabled)

- 🔗 [GET /admin/subs/getUpstreamConns](#get-adminsubsgetupstreamconns)

- 🔗 [GET /admin/subs/listDomainBans](#get-adminsubslistdomainbans)

- 🔗 [GET /admin/subs/perDayLimit](#get-adminsubsperdaylimit)

- 🔗 [GET /xrpc/_health](#get-xrpc_health)

- 🔗 [GET /xrpc/com.atproto.sync.getHostStatus](#get-xrpccomatprotosyncgethoststatus)

- 🔗 [GET /xrpc/com.atproto.sync.getLatestCommit](#get-xrpccomatprotosyncgetlatestcommit)

- 🔗 [GET /xrpc/com.atproto.sync.getRepo](#get-xrpccomatprotosyncgetrepo)

- 🔗 [GET /xrpc/com.atproto.sync.getRepoStatus](#get-xrpccomatprotosyncgetrepostatus)

- 🔗 [GET /xrpc/com.atproto.sync.listHosts](#get-xrpccomatprotosynclisthosts)

- 🔗 [GET /xrpc/com.atproto.sync.listRepos](#get-xrpccomatprotosynclistrepos)

- 🔗 [GET /xrpc/com.atproto.sync.listReposByCollection](#get-xrpccomatprotosynclistreposbycollection)

- 🔗 [GET /xrpc/com.atproto.sync.subscribeRepos](#get-xrpccomatprotosyncsubscriberepos)

- 🔗 [Handle /metrics](#handle-metrics)

- 🔗 [POST /admin/pds/block](#post-adminpdsblock)

- 🔗 [POST /admin/pds/changeLimits](#post-adminpdschangelimits)

- 🔗 [POST /admin/pds/requestCrawl](#post-adminpdsrequestcrawl)

- 🔗 [POST /admin/pds/unblock](#post-adminpdsunblock)

- 🔗 [POST /admin/repo/reverseTakedown](#post-adminreporeversetakedown)

- 🔗 [POST /admin/repo/takeDown](#post-adminrepotakedown)

- 🔗 [POST /admin/subs/banDomain](#post-adminsubsbandomain)

- 🔗 [POST /admin/subs/killUpstream](#post-adminsubskillupstream)

- 🔗 [POST /admin/subs/setEnabled](#post-adminsubssetenabled)

- 🔗 [POST /admin/subs/setPerDayLimit](#post-adminsubssetperdaylimit)

- 🔗 [POST /admin/subs/unbanDomain](#post-adminsubsunbandomain)

- 🔗 [POST /xrpc/com.atproto.sync.requestCrawl](#post-xrpccomatprotosyncrequestcrawl)

- 🔗 [POST /xrpc/com.atproto.sync.requestCrawl](#post-xrpccomatprotosyncrequestcrawl)


</details>



---


[rest] method: GET path: / handler: s file: splitter/splitter.go


#### GET /


GET / endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /_health handler: s file: splitter/splitter.go


#### GET /_health


GET /_health endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /admin/consumers/list handler: s file: splitter/splitter.go


#### GET /admin/consumers/list


GET /admin/consumers/list endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /admin/pds/list handler: s file: splitter/splitter.go


#### GET /admin/pds/list


GET /admin/pds/list endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /admin/subs/getEnabled handler: s file: splitter/splitter.go


#### GET /admin/subs/getEnabled


GET /admin/subs/getEnabled endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /admin/subs/getUpstreamConns handler: s file: splitter/splitter.go


#### GET /admin/subs/getUpstreamConns


GET /admin/subs/getUpstreamConns endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /admin/subs/listDomainBans handler: s file: splitter/splitter.go


#### GET /admin/subs/listDomainBans


GET /admin/subs/listDomainBans endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /admin/subs/perDayLimit handler: s file: splitter/splitter.go


#### GET /admin/subs/perDayLimit


GET /admin/subs/perDayLimit endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/_health handler: s file: splitter/splitter.go


#### GET /xrpc/_health


GET /xrpc/_health endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.getHostStatus handler: s file: splitter/splitter.go


#### GET /xrpc/com.atproto.sync.getHostStatus


GET /xrpc/com.atproto.sync.getHostStatus endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.getLatestCommit handler: s file: splitter/splitter.go


#### GET /xrpc/com.atproto.sync.getLatestCommit


GET /xrpc/com.atproto.sync.getLatestCommit endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.getRepo handler: s file: splitter/splitter.go


#### GET /xrpc/com.atproto.sync.getRepo


GET /xrpc/com.atproto.sync.getRepo endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.getRepoStatus handler: s file: splitter/splitter.go


#### GET /xrpc/com.atproto.sync.getRepoStatus


GET /xrpc/com.atproto.sync.getRepoStatus endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.listHosts handler: s file: splitter/splitter.go


#### GET /xrpc/com.atproto.sync.listHosts


GET /xrpc/com.atproto.sync.listHosts endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.listRepos handler: s file: splitter/splitter.go


#### GET /xrpc/com.atproto.sync.listRepos


GET /xrpc/com.atproto.sync.listRepos endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.listReposByCollection handler: s file: splitter/splitter.go


#### GET /xrpc/com.atproto.sync.listReposByCollection


GET /xrpc/com.atproto.sync.listReposByCollection endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: GET path: /xrpc/com.atproto.sync.subscribeRepos handler: s file: splitter/splitter.go


#### GET /xrpc/com.atproto.sync.subscribeRepos


GET /xrpc/com.atproto.sync.subscribeRepos endpoint handled by s. Retrieves data from the server.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: Handle path: /metrics handler: promhttp file: splitter/splitter.go


#### Handle /metrics


Handle /metrics endpoint handled by promhttp.


**Handler:** `promhttp`

**Router:** net/http


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/pds/block handler: s file: splitter/splitter.go


#### POST /admin/pds/block


POST /admin/pds/block endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/pds/changeLimits handler: s file: splitter/splitter.go


#### POST /admin/pds/changeLimits


POST /admin/pds/changeLimits endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/pds/requestCrawl handler: s file: splitter/splitter.go


#### POST /admin/pds/requestCrawl


POST /admin/pds/requestCrawl endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/pds/unblock handler: s file: splitter/splitter.go


#### POST /admin/pds/unblock


POST /admin/pds/unblock endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/repo/reverseTakedown handler: s file: splitter/splitter.go


#### POST /admin/repo/reverseTakedown


POST /admin/repo/reverseTakedown endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/repo/takeDown handler: s file: splitter/splitter.go


#### POST /admin/repo/takeDown


POST /admin/repo/takeDown endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/subs/banDomain handler: s file: splitter/splitter.go


#### POST /admin/subs/banDomain


POST /admin/subs/banDomain endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/subs/killUpstream handler: s file: splitter/splitter.go


#### POST /admin/subs/killUpstream


POST /admin/subs/killUpstream endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/subs/setEnabled handler: s file: splitter/splitter.go


#### POST /admin/subs/setEnabled


POST /admin/subs/setEnabled endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/subs/setPerDayLimit handler: s file: splitter/splitter.go


#### POST /admin/subs/setPerDayLimit


POST /admin/subs/setPerDayLimit endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /admin/subs/unbanDomain handler: s file: splitter/splitter.go


#### POST /admin/subs/unbanDomain


POST /admin/subs/unbanDomain endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /xrpc/com.atproto.sync.requestCrawl handler: s file: splitter/splitter.go


#### POST /xrpc/com.atproto.sync.requestCrawl


POST /xrpc/com.atproto.sync.requestCrawl endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


[rest] method: POST path: /xrpc/com.atproto.sync.requestCrawl handler: s file: splitter/splitter.go


#### POST /xrpc/com.atproto.sync.requestCrawl


POST /xrpc/com.atproto.sync.requestCrawl endpoint handled by s. Creates new resources.


**Handler:** `s`

**Router:** echo


📍 *Определено в: `splitter/splitter.go`*



---


## Навигация


- [К оглавлению документации](../README.md)

- [Диаграммы](../diagrams/)

- [Импорты](imports.md)

- [Структуры и типы](structures.md)

- [Функции](functions.md)

- [Спецификация API](api.md)

- [Тестирование](tests.md)

- [Используемые библиотеки](libraries.md)


---

