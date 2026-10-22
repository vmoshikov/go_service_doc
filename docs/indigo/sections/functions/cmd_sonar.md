---
title: "Функции: cmd/sonar"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/sonar
---


# Функции: cmd/sonar


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_relay.md)

- [Следующая директория](cmd_stress.md)


---


## Меню по файлам


- 📄 [cmd/sonar/main.go](#cmdsonarmaingo)

- 📄 [cmd/sonar/sonar.go](#cmdsonarsonargo)


---


## cmd/sonar/main.go


📄 Исходный файл: `cmd/sonar/main.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [main](#main-cmdsonarmaingo27) `:27`

- 🔗 [runSonar](#runsonar-cmdsonarmaingo73) `:73`


</details>


[function] name: main file: cmd/sonar/main.go:27 returns_error: нет description: —


### main (cmd/sonar/main.go:27)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/sonar/main.go:27`



---


[function] name: runSonar file: cmd/sonar/main.go:73 returns_error: нет description: —


### runSonar (cmd/sonar/main.go:73)


runSonar is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runSonar((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/sonar/main.go:73`




## cmd/sonar/sonar.go


📄 Исходный файл: `cmd/sonar/sonar.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [HandleRepoCommit](#handlerepocommit-cmdsonarsonargo144) `:144`

- 🔗 [HandleStreamEvent](#handlestreamevent-cmdsonarsonargo103) `:103`

- 🔗 [NewSonar](#newsonar-cmdsonarsonargo74) `:74`

- 🔗 [ReadCursorFile](#readcursorfile-cmdsonarsonargo56) `:56`

- 🔗 [WriteCursorFile](#writecursorfile-cmdsonarsonargo38) `:38`


</details>


[function] name: HandleRepoCommit file: cmd/sonar/sonar.go:144 returns_error: нет description: —


### HandleRepoCommit (cmd/sonar/sonar.go:144)


HandleRepoCommit is a method that handles or processes requests based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit).


```go
func (s *Sonar) HandleRepoCommit((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)
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


📍 *Расположение:* `cmd/sonar/sonar.go:144`



---


[function] name: HandleStreamEvent file: cmd/sonar/sonar.go:103 returns_error: нет description: —


### HandleStreamEvent (cmd/sonar/sonar.go:103)


HandleStreamEvent is a method that handles or processes requests based on the provided parameters and returns (ctx context.Context, xe *events.XRPCStreamEvent).


```go
func (s *Sonar) HandleStreamEvent((ctx context.Context, xe *events.XRPCStreamEvent)) (ctx context.Context, xe *events.XRPCStreamEvent)
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


**Тип ответа:** xe


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "db": null,
  "relayhost": "string",
  "relayXRPC": null,
  "dir": {},
  "echo": null,
  "logger": null,
  "bfs": null,
  "bf": null,
  "enableRepoDiscovery": false,
  "indexLimiter": null,
  "profileQueue": {},
  "postQueue": {},
  "pagerankQueue": {}
}
```


*Определено в:* `search/indexing.go`


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


📍 *Расположение:* `cmd/sonar/sonar.go:103`



---


[function] name: NewSonar file: cmd/sonar/sonar.go:74 returns_error: да description: —


### NewSonar (cmd/sonar/sonar.go:74)


NewSonar is a function that performs operations based on the provided parameters and may return an error.


```go
func NewSonar((*Sonar, error)) (*Sonar, error)
```


**Тип запроса:** Sonar


```json
{
  "SocketURL": "string",
  "Progress": null,
  "ProgMux": {},
  "Logger": null,
  "CursorFile": "string"
}
```


*Определено в:* `cmd/sonar/sonar.go`


**Тип ответа:** Sonar


```json
{
  "SocketURL": "string",
  "Progress": null,
  "ProgMux": {},
  "Logger": null,
  "CursorFile": "string"
}
```


*Определено в:* `cmd/sonar/sonar.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Sonar`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/sonar/sonar.go:74`



---


[function] name: ReadCursorFile file: cmd/sonar/sonar.go:56 returns_error: нет description: —


### ReadCursorFile (cmd/sonar/sonar.go:56)


ReadCursorFile is a method that performs operations based on the provided parameters and returns ().


```go
func (s *Sonar) ReadCursorFile(()) ()
```


📍 *Расположение:* `cmd/sonar/sonar.go:56`



---


[function] name: WriteCursorFile file: cmd/sonar/sonar.go:38 returns_error: нет description: —


### WriteCursorFile (cmd/sonar/sonar.go:38)


WriteCursorFile is a method that performs operations based on the provided parameters and returns ().


```go
func (s *Sonar) WriteCursorFile(()) ()
```


📍 *Расположение:* `cmd/sonar/sonar.go:38`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_relay.md)

- [Следующая директория](cmd_stress.md)


---

