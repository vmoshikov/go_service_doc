---
title: "Функции: automod/consumer"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/consumer
---


# Функции: automod/consumer


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_capture.md)

- [Следующая директория](automod_countstore.md)


---


## Меню по файлам


- 📄 [automod/consumer/firehose.go](#automodconsumerfirehosego)

- 📄 [automod/consumer/ozone.go](#automodconsumerozonego)


---


## automod/consumer/firehose.go


📄 Исходный файл: `automod/consumer/firehose.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [HandleRepoCommit](#handlerepocommit-automodconsumerfirehosego123) `:123`

- 🔗 [PersistCursor](#persistcursor-automodconsumerfirehosego230) `:230`

- 🔗 [ReadLastCursor](#readlastcursor-automodconsumerfirehosego212) `:212`

- 🔗 [Run](#run-automodconsumerfirehosego48) `:48`

- 🔗 [RunPersistCursor](#runpersistcursor-automodconsumerfirehosego244) `:244`


</details>


[function] name: HandleRepoCommit file: automod/consumer/firehose.go:123 returns_error: нет description: NOTE: for now, this function basically never errors, just logs and returns nil. Should think through error processing be


### HandleRepoCommit (automod/consumer/firehose.go:123)


NOTE: for now, this function basically never errors, just logs and returns nil. Should think through error processing better.


```go
func (fc *FirehoseConsumer) HandleRepoCommit((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)
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


📍 *Расположение:* `automod/consumer/firehose.go:123`



---


[function] name: PersistCursor file: automod/consumer/firehose.go:230 returns_error: нет description: —


### PersistCursor (automod/consumer/firehose.go:230)


PersistCursor is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (fc *FirehoseConsumer) PersistCursor((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `automod/consumer/firehose.go:230`



---


[function] name: ReadLastCursor file: automod/consumer/firehose.go:212 returns_error: да description: —


### ReadLastCursor (automod/consumer/firehose.go:212)


ReadLastCursor is a method that performs operations based on the provided parameters and may return an error.


```go
func (fc *FirehoseConsumer) ReadLastCursor((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/consumer/firehose.go:212`



---


[function] name: Run file: automod/consumer/firehose.go:48 returns_error: нет description: —


### Run (automod/consumer/firehose.go:48)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (fc *FirehoseConsumer) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `automod/consumer/firehose.go:48`



---


[function] name: RunPersistCursor file: automod/consumer/firehose.go:244 returns_error: нет description: this method runs in a loop, persisting the current cursor state every 5 seconds


### RunPersistCursor (automod/consumer/firehose.go:244)


this method runs in a loop, persisting the current cursor state every 5 seconds


```go
func (fc *FirehoseConsumer) RunPersistCursor((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `automod/consumer/firehose.go:244`




## automod/consumer/ozone.go


📄 Исходный файл: `automod/consumer/ozone.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [HandleOzoneEvent](#handleozoneevent-automodconsumerozonego121) `:121`

- 🔗 [PersistCursor](#persistcursor-automodconsumerozonego149) `:149`

- 🔗 [ReadLastCursor](#readlastcursor-automodconsumerozonego131) `:131`

- 🔗 [Run](#run-automodconsumerozonego31) `:31`

- 🔗 [RunPersistCursor](#runpersistcursor-automodconsumerozonego163) `:163`


</details>


[function] name: HandleOzoneEvent file: automod/consumer/ozone.go:121 returns_error: нет description: —


### HandleOzoneEvent (automod/consumer/ozone.go:121)


HandleOzoneEvent is a method that handles or processes requests based on the provided parameters and returns (ctx context.Context, eventView *toolsozone.ModerationDefs_ModEventView).


```go
func (oc *OzoneConsumer) HandleOzoneEvent((ctx context.Context, eventView *toolsozone.ModerationDefs_ModEventView)) (ctx context.Context, eventView *toolsozone.ModerationDefs_ModEventView)
```


**Тип запроса:** toolsozone.ModerationDefs_ModEventView


```json
{
  "createdAt": "string",
  "createdBy": "string",
  "creatorHandle": "string",
  "event": null,
  "id": 0,
  "modTool": null,
  "subject": null,
  "subjectBlobCids": [],
  "subjectHandle": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


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


**Тип ответа:** eventView


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** toolsozone.ModerationDefs_ModEventView


```json
{
  "createdAt": "string",
  "createdBy": "string",
  "creatorHandle": "string",
  "event": null,
  "id": 0,
  "modTool": null,
  "subject": null,
  "subjectBlobCids": [],
  "subjectHandle": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


📍 *Расположение:* `automod/consumer/ozone.go:121`



---


[function] name: PersistCursor file: automod/consumer/ozone.go:149 returns_error: нет description: —


### PersistCursor (automod/consumer/ozone.go:149)


PersistCursor is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (oc *OzoneConsumer) PersistCursor((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `automod/consumer/ozone.go:149`



---


[function] name: ReadLastCursor file: automod/consumer/ozone.go:131 returns_error: да description: —


### ReadLastCursor (automod/consumer/ozone.go:131)


ReadLastCursor is a method that performs operations based on the provided parameters and may return an error.


```go
func (oc *OzoneConsumer) ReadLastCursor((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/consumer/ozone.go:131`



---


[function] name: Run file: automod/consumer/ozone.go:31 returns_error: нет description: —


### Run (automod/consumer/ozone.go:31)


Run is a method that performs operations based on the provided parameters and returns (ctx context.Context).


```go
func (oc *OzoneConsumer) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `automod/consumer/ozone.go:31`



---


[function] name: RunPersistCursor file: automod/consumer/ozone.go:163 returns_error: нет description: this method runs in a loop, persisting the current cursor state every 5 seconds


### RunPersistCursor (automod/consumer/ozone.go:163)


this method runs in a loop, persisting the current cursor state every 5 seconds


```go
func (oc *OzoneConsumer) RunPersistCursor((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `automod/consumer/ozone.go:163`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_capture.md)

- [Следующая директория](automod_countstore.md)


---

