---
title: "Функции: cmd/gosky"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/gosky
---


# Функции: cmd/gosky


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_fakermaker.md)

- [Следующая директория](cmd_hepa.md)


---


## Меню по файлам


- 📄 [cmd/gosky/bsky.go](#cmdgoskybskygo)

- 📄 [cmd/gosky/debug.go](#cmdgoskydebuggo)

- 📄 [cmd/gosky/main.go](#cmdgoskymaingo)

- 📄 [cmd/gosky/streamdiff.go](#cmdgoskystreamdiffgo)


---


## cmd/gosky/bsky.go


📄 Исходный файл: `cmd/gosky/bsky.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [prettyPrintPost](#prettyprintpost-cmdgoskybskygo130) `:130`


</details>


[function] name: prettyPrintPost file: cmd/gosky/bsky.go:130 returns_error: нет description: —


### prettyPrintPost (cmd/gosky/bsky.go:130)


prettyPrintPost is a function that performs operations based on the provided parameters and returns (p *appbsky.FeedDefs_FeedViewPost, uris bool).


```go
func prettyPrintPost((p *appbsky.FeedDefs_FeedViewPost, uris bool)) (p *appbsky.FeedDefs_FeedViewPost, uris bool)
```


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


**Тип ответа:** p


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


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


**Тип ответа:** uris


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/gosky/bsky.go:130`




## cmd/gosky/debug.go


📄 Исходный файл: `cmd/gosky/debug.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [cidStr](#cidstr-cmdgoskydebuggo170) `:170`

- 🔗 [loadCache](#loadcache-cmdgoskydebuggo726) `:726`

- 🔗 [saveCache](#savecache-cmdgoskydebuggo752) `:752`


</details>


[function] name: cidStr file: cmd/gosky/debug.go:170 returns_error: нет description: —


### cidStr (cmd/gosky/debug.go:170)


cidStr is a function that performs operations based on the provided parameters and returns (c *lexutil.LexLink).


```go
func cidStr((c *lexutil.LexLink)) (c *lexutil.LexLink)
```


**Тип запроса:** lexutil.LexLink


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** lexutil.LexLink


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/gosky/debug.go:170`



---


[function] name: loadCache file: cmd/gosky/debug.go:726 returns_error: да description: —


### loadCache (cmd/gosky/debug.go:726)


loadCache is a function that performs operations based on the provided parameters and may return an error.


```go
func loadCache((map[string]*bsky.FeedDefs_PostView, error)) (map[string]*bsky.FeedDefs_PostView, error)
```


**Тип запроса:** bsky.FeedDefs_PostView


```json
{
  "$type": "string",
  "author": null,
  "bookmarkCount": 0,
  "cid": "string",
  "debug": null,
  "embed": null,
  "indexedAt": "string",
  "labels": [],
  "likeCount": 0,
  "quoteCount": 0,
  "record": null,
  "replyCount": 0,
  "repostCount": 0,
  "threadgate": null,
  "uri": "string",
  "viewer": null
}
```


*Определено в:* `api/bsky/feeddefs.go`


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bsky.FeedDefs_PostView


```json
{
  "$type": "string",
  "author": null,
  "bookmarkCount": 0,
  "cid": "string",
  "debug": null,
  "embed": null,
  "indexedAt": "string",
  "labels": [],
  "likeCount": 0,
  "quoteCount": 0,
  "record": null,
  "replyCount": 0,
  "repostCount": 0,
  "threadgate": null,
  "uri": "string",
  "viewer": null
}
```


*Определено в:* `api/bsky/feeddefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]*bsky.FeedDefs_PostView`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/gosky/debug.go:726`



---


[function] name: saveCache file: cmd/gosky/debug.go:752 returns_error: нет description: —


### saveCache (cmd/gosky/debug.go:752)


saveCache is a function that performs operations based on the provided parameters and returns (filename string, data map[string]*bsky.FeedDefs_PostView).


```go
func saveCache((filename string, data map[string]*bsky.FeedDefs_PostView)) (filename string, data map[string]*bsky.FeedDefs_PostView)
```


**Тип запроса:** bsky.FeedDefs_PostView


```json
{
  "$type": "string",
  "author": null,
  "bookmarkCount": 0,
  "cid": "string",
  "debug": null,
  "embed": null,
  "indexedAt": "string",
  "labels": [],
  "likeCount": 0,
  "quoteCount": 0,
  "record": null,
  "replyCount": 0,
  "repostCount": 0,
  "threadgate": null,
  "uri": "string",
  "viewer": null
}
```


*Определено в:* `api/bsky/feeddefs.go`


**Тип ответа:** filename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** data


```json
{
  "AuthorizationServers": []
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bsky.FeedDefs_PostView


```json
{
  "$type": "string",
  "author": null,
  "bookmarkCount": 0,
  "cid": "string",
  "debug": null,
  "embed": null,
  "indexedAt": "string",
  "labels": [],
  "likeCount": 0,
  "quoteCount": 0,
  "record": null,
  "replyCount": 0,
  "repostCount": 0,
  "threadgate": null,
  "uri": "string",
  "viewer": null
}
```


*Определено в:* `api/bsky/feeddefs.go`


📍 *Расположение:* `cmd/gosky/debug.go:752`




## cmd/gosky/main.go


📄 Исходный файл: `cmd/gosky/main.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [cborToJson](#cbortojson-cmdgoskymaingo117) `:117`

- 🔗 [configLogger](#configlogger-cmdgoskymaingo845) `:845`

- 🔗 [jsonPrint](#jsonprint-cmdgoskymaingo108) `:108`

- 🔗 [main](#main-cmdgoskymaingo47) `:47`

- 🔗 [needArgs](#needargs-cmdgoskymaingo524) `:524`

- 🔗 [readDids](#readdids-cmdgoskymaingo507) `:507`

- 🔗 [run](#run-cmdgoskymaingo51) `:51`

- 🔗 [unpackRecords](#unpackrecords-cmdgoskymaingo323) `:323`


</details>


[function] name: cborToJson file: cmd/gosky/main.go:117 returns_error: да description: —


### cborToJson (cmd/gosky/main.go:117)


cborToJson is a function that performs operations based on the provided parameters and may return an error.


```go
func cborToJson(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/gosky/main.go:117`



---


[function] name: configLogger file: cmd/gosky/main.go:845 returns_error: нет description: —


### configLogger (cmd/gosky/main.go:845)


configLogger is a function that performs operations based on the provided parameters and returns (cmd *cli.Context, writer *os.File).


```go
func configLogger((cmd *cli.Context, writer *os.File)) (cmd *cli.Context, writer *os.File)
```


**Тип запроса:** cli.Context


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


**Тип запроса:** os.File


```json
{
  "Path": "string",
  "Archived": false,
  "SeqStart": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** cmd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cli.Context


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


**Тип ответа:** writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** os.File


```json
{
  "Path": "string",
  "Archived": false,
  "SeqStart": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


📍 *Расположение:* `cmd/gosky/main.go:845`



---


[function] name: jsonPrint file: cmd/gosky/main.go:108 returns_error: нет description: —


### jsonPrint (cmd/gosky/main.go:108)


jsonPrint is a function that performs operations based on the provided parameters and returns (i any).


```go
func jsonPrint((i any)) (i any)
```


**Тип ответа:** i


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/gosky/main.go:108`



---


[function] name: main file: cmd/gosky/main.go:47 returns_error: нет description: —


### main (cmd/gosky/main.go:47)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/gosky/main.go:47`



---


[function] name: needArgs file: cmd/gosky/main.go:524 returns_error: да description: —


### needArgs (cmd/gosky/main.go:524)


needArgs is a function that performs operations based on the provided parameters and may return an error.


```go
func needArgs(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/gosky/main.go:524`



---


[function] name: readDids file: cmd/gosky/main.go:507 returns_error: да description: —


### readDids (cmd/gosky/main.go:507)


readDids is a function that performs operations based on the provided parameters and may return an error.


```go
func readDids(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/gosky/main.go:507`



---


[function] name: run file: cmd/gosky/main.go:51 returns_error: нет description: —


### run (cmd/gosky/main.go:51)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/gosky/main.go:51`



---


[function] name: unpackRecords file: cmd/gosky/main.go:323 returns_error: да description: —


### unpackRecords (cmd/gosky/main.go:323)


unpackRecords is a function that performs operations based on the provided parameters and may return an error.


```go
func unpackRecords(([]any, error)) ([]any, error)
```


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/gosky/main.go:323`




## cmd/gosky/streamdiff.go


📄 Исходный файл: `cmd/gosky/streamdiff.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [PushA](#pusha-cmdgoskystreamdiffgo103) `:103`

- 🔗 [PushB](#pushb-cmdgoskystreamdiffgo123) `:123`

- 🔗 [evtOp](#evtop-cmdgoskystreamdiffgo127) `:127`

- 🔗 [findEvt](#findevt-cmdgoskystreamdiffgo146) `:146`

- 🔗 [sameCommit](#samecommit-cmdgoskystreamdiffgo142) `:142`


</details>


[function] name: PushA file: cmd/gosky/streamdiff.go:103 returns_error: нет description: —


### PushA (cmd/gosky/streamdiff.go:103)


PushA is a method that performs operations based on the provided parameters and returns (evt *events.XRPCStreamEvent).


```go
func (sd *streamDiffer) PushA((evt *events.XRPCStreamEvent)) (evt *events.XRPCStreamEvent)
```


**Тип запроса:** events.XRPCStreamEvent


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


**Тип ответа:** events.XRPCStreamEvent


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


📍 *Расположение:* `cmd/gosky/streamdiff.go:103`



---


[function] name: PushB file: cmd/gosky/streamdiff.go:123 returns_error: нет description: —


### PushB (cmd/gosky/streamdiff.go:123)


PushB is a method that performs operations based on the provided parameters and returns (evt *events.XRPCStreamEvent).


```go
func (sd *streamDiffer) PushB((evt *events.XRPCStreamEvent)) (evt *events.XRPCStreamEvent)
```


**Тип запроса:** events.XRPCStreamEvent


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


**Тип ответа:** events.XRPCStreamEvent


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


📍 *Расположение:* `cmd/gosky/streamdiff.go:123`



---


[function] name: evtOp file: cmd/gosky/streamdiff.go:127 returns_error: нет description: —


### evtOp (cmd/gosky/streamdiff.go:127)


evtOp is a function that performs operations based on the provided parameters and returns (evt *events.XRPCStreamEvent).


```go
func evtOp((evt *events.XRPCStreamEvent)) (evt *events.XRPCStreamEvent)
```


**Тип запроса:** events.XRPCStreamEvent


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


**Тип ответа:** events.XRPCStreamEvent


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


📍 *Расположение:* `cmd/gosky/streamdiff.go:127`



---


[function] name: findEvt file: cmd/gosky/streamdiff.go:146 returns_error: нет description: —


### findEvt (cmd/gosky/streamdiff.go:146)


findEvt is a function that performs operations based on the provided parameters and returns (evt *events.XRPCStreamEvent, list []*events.XRPCStreamEvent).


```go
func findEvt((evt *events.XRPCStreamEvent, list []*events.XRPCStreamEvent)) (evt *events.XRPCStreamEvent, list []*events.XRPCStreamEvent)
```


**Тип запроса:** events.XRPCStreamEvent


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


**Тип запроса:** events.XRPCStreamEvent


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


**Тип ответа:** events.XRPCStreamEvent


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


**Тип ответа:** list


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** events.XRPCStreamEvent


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


📍 *Расположение:* `cmd/gosky/streamdiff.go:146`



---


[function] name: sameCommit file: cmd/gosky/streamdiff.go:142 returns_error: нет description: —


### sameCommit (cmd/gosky/streamdiff.go:142)


sameCommit is a function that performs operations based on the provided parameters and returns (a, b *comatproto.SyncSubscribeRepos_Commit).


```go
func sameCommit((a, b *comatproto.SyncSubscribeRepos_Commit)) (a, b *comatproto.SyncSubscribeRepos_Commit)
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


📍 *Расположение:* `cmd/gosky/streamdiff.go:142`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_fakermaker.md)

- [Следующая директория](cmd_hepa.md)


---

