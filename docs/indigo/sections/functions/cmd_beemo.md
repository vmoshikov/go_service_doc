---
title: "Функции: cmd/beemo"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/beemo
---


# Функции: cmd/beemo


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](carstore.md)

- [Следующая директория](cmd_bluepages.md)


---


## Меню по файлам


- 📄 [cmd/beemo/firehose_consumer.go](#cmdbeemofirehose_consumergo)

- 📄 [cmd/beemo/main.go](#cmdbeemomaingo)

- 📄 [cmd/beemo/notify_mentions.go](#cmdbeemonotify_mentionsgo)

- 📄 [cmd/beemo/notify_reports.go](#cmdbeemonotify_reportsgo)

- 📄 [cmd/beemo/slack.go](#cmdbeemoslackgo)


---


## cmd/beemo/firehose_consumer.go


📄 Исходный файл: `cmd/beemo/firehose_consumer.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [HandleRepoCommit](#handlerepocommit-cmdbeemofirehose_consumergo63) `:63`

- 🔗 [RunFirehoseConsumer](#runfirehoseconsumer-cmdbeemofirehose_consumergo24) `:24`


</details>


[function] name: HandleRepoCommit file: cmd/beemo/firehose_consumer.go:63 returns_error: да description: NOTE: for now, this function basically never errors, just logs and returns nil. Should think through error processing be


### HandleRepoCommit (cmd/beemo/firehose_consumer.go:63)


NOTE: for now, this function basically never errors, just logs and returns nil. Should think through error processing better.


```go
func HandleRepoCommit((ctx context.Context, logger *slog.Logger, evt *comatproto.SyncSubscribeRepos_Commit, postCallback func(context.Context, syntax.DID, syntax.RecordKey, appbsky.FeedPost) error)) (ctx context.Context, logger *slog.Logger, evt *comatproto.SyncSubscribeRepos_Commit, postCallback func(context.Context, syntax.DID, syntax.RecordKey, appbsky.FeedPost) error)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** postCallback


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


**Тип ответа:** syntax.RecordKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `logger *slog.Logger`, `evt *comatproto.SyncSubscribeRepos_Commit`, `postCallback func(context.Context`, `syntax.DID`, `syntax.RecordKey`, `appbsky.FeedPost) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/beemo/firehose_consumer.go:63`



---


[function] name: RunFirehoseConsumer file: cmd/beemo/firehose_consumer.go:24 returns_error: да description: —


### RunFirehoseConsumer (cmd/beemo/firehose_consumer.go:24)


RunFirehoseConsumer is a function that performs operations based on the provided parameters and may return an error.


```go
func RunFirehoseConsumer((ctx context.Context, logger *slog.Logger, relayHost string, postCallback func(context.Context, syntax.DID, syntax.RecordKey, appbsky.FeedPost) error)) (ctx context.Context, logger *slog.Logger, relayHost string, postCallback func(context.Context, syntax.DID, syntax.RecordKey, appbsky.FeedPost) error)
```


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


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** relayHost


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** postCallback


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


**Тип ответа:** syntax.RecordKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ctx context.Context`, `logger *slog.Logger`, `relayHost string`, `postCallback func(context.Context`, `syntax.DID`, `syntax.RecordKey`, `appbsky.FeedPost) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/beemo/firehose_consumer.go:24`




## cmd/beemo/main.go


📄 Исходный файл: `cmd/beemo/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [configLogger](#configlogger-cmdbeemomaingo122) `:122`

- 🔗 [main](#main-cmdbeemomaingo20) `:20`

- 🔗 [run](#run-cmdbeemomaingo27) `:27`


</details>


[function] name: configLogger file: cmd/beemo/main.go:122 returns_error: нет description: —


### configLogger (cmd/beemo/main.go:122)


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


📍 *Расположение:* `cmd/beemo/main.go:122`



---


[function] name: main file: cmd/beemo/main.go:20 returns_error: нет description: —


### main (cmd/beemo/main.go:20)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/beemo/main.go:20`



---


[function] name: run file: cmd/beemo/main.go:27 returns_error: нет description: —


### run (cmd/beemo/main.go:27)


run is a function that performs operations based on the provided parameters and returns (args []string).


```go
func run((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/beemo/main.go:27`




## cmd/beemo/notify_mentions.go


📄 Исходный файл: `cmd/beemo/notify_mentions.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ProcessPost](#processpost-cmdbeemonotify_mentionsgo25) `:25`

- 🔗 [notifyMentions](#notifymentions-cmdbeemonotify_mentionsgo64) `:64`


</details>


[function] name: ProcessPost file: cmd/beemo/notify_mentions.go:25 returns_error: нет description: —


### ProcessPost (cmd/beemo/notify_mentions.go:25)


ProcessPost is a method that handles or processes requests based on the provided parameters and returns (ctx context.Context, did syntax.DID, rkey syntax.RecordKey, post appbsky.FeedPost).


```go
func (mc *MentionChecker) ProcessPost((ctx context.Context, did syntax.DID, rkey syntax.RecordKey, post appbsky.FeedPost)) (ctx context.Context, did syntax.DID, rkey syntax.RecordKey, post appbsky.FeedPost)
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


**Тип ответа:** rkey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.RecordKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


📍 *Расположение:* `cmd/beemo/notify_mentions.go:25`



---


[function] name: notifyMentions file: cmd/beemo/notify_mentions.go:64 returns_error: нет description: —


### notifyMentions (cmd/beemo/notify_mentions.go:64)


notifyMentions is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func notifyMentions((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/beemo/notify_mentions.go:64`




## cmd/beemo/notify_reports.go


📄 Исходный файл: `cmd/beemo/notify_reports.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [pollNewReports](#pollnewreports-cmdbeemonotify_reportsgo18) `:18`


</details>


[function] name: pollNewReports file: cmd/beemo/notify_reports.go:18 returns_error: нет description: —


### pollNewReports (cmd/beemo/notify_reports.go:18)


pollNewReports is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func pollNewReports((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/beemo/notify_reports.go:18`




## cmd/beemo/slack.go


📄 Исходный файл: `cmd/beemo/slack.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [sendSlackMsg](#sendslackmsg-cmdbeemoslackgo19) `:19`


</details>


[function] name: sendSlackMsg file: cmd/beemo/slack.go:19 returns_error: нет description: sends a simple slack message to a channel via "incoming webhook"
The slack incoming webhook must be already configured i


### sendSlackMsg (cmd/beemo/slack.go:19)


sends a simple slack message to a channel via "incoming webhook"
The slack incoming webhook must be already configured in the slack workplace.


```go
func sendSlackMsg((ctx context.Context, msg, webhookURL string)) (ctx context.Context, msg, webhookURL string)
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


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** webhookURL


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/beemo/slack.go:19`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](carstore.md)

- [Следующая директория](cmd_bluepages.md)


---

