---
title: "Функции: events/schedulers"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: events/schedulers
---


# Функции: events/schedulers


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_pebblepersist.md)

- [Следующая директория](events_yolopersist.md)


---


## Меню по файлам


- 📄 [events/schedulers/autoscaling/autoscaling.go](#eventsschedulersautoscalingautoscalinggo)

- 📄 [events/schedulers/autoscaling/throughput.go](#eventsschedulersautoscalingthroughputgo)

- 📄 [events/schedulers/parallel/parallel.go](#eventsschedulersparallelparallelgo)

- 📄 [events/schedulers/sequential/sequential.go](#eventsschedulerssequentialsequentialgo)


---


## events/schedulers/autoscaling/autoscaling.go


📄 Исходный файл: `events/schedulers/autoscaling/autoscaling.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [AddWork](#addwork-eventsschedulersautoscalingautoscalinggo171) `:171`

- 🔗 [DefaultAutoscaleSettings](#defaultautoscalesettings-eventsschedulersautoscalingautoscalinggo63) `:63`

- 🔗 [NewScheduler](#newscheduler-eventsschedulersautoscalingautoscalinggo74) `:74`

- 🔗 [Shutdown](#shutdown-eventsschedulersautoscalingautoscalinggo115) `:115`

- 🔗 [autoscale](#autoscale-eventsschedulersautoscalingautoscalinggo141) `:141`

- 🔗 [worker](#worker-eventsschedulersautoscalingautoscalinggo201) `:201`


</details>


[function] name: AddWork file: events/schedulers/autoscaling/autoscaling.go:171 returns_error: нет description: —


### AddWork (events/schedulers/autoscaling/autoscaling.go:171)


AddWork is a method that creates new data based on the provided parameters and returns (ctx context.Context, repo string, val *events.XRPCStreamEvent).


```go
func (p *Scheduler) AddWork((ctx context.Context, repo string, val *events.XRPCStreamEvent)) (ctx context.Context, repo string, val *events.XRPCStreamEvent)
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


📍 *Расположение:* `events/schedulers/autoscaling/autoscaling.go:171`



---


[function] name: DefaultAutoscaleSettings file: events/schedulers/autoscaling/autoscaling.go:63 returns_error: нет description: DefaultAutoscaleSettings returns the default autoscale settings.
Concurrency is the number of workers to start with.
Max


### DefaultAutoscaleSettings (events/schedulers/autoscaling/autoscaling.go:63)


DefaultAutoscaleSettings returns the default autoscale settings.
Concurrency is the number of workers to start with.
MaxConcurrency is the maximum number of workers to scale up to.
AutoscaleFrequency is the frequency to check the average throughput.
ThroughputBucketCount is the number of buckets to use to calculate the average throughput.
ThroughputBucketDuration is the duration of each bucket.
By default we check the average throughput over the last 60 seconds with 1 second buckets
We make an autoscaling decision every 5 seconds.
We start with 1 worker and scale up to 32 workers.


```go
func DefaultAutoscaleSettings(()) ()
```


📍 *Расположение:* `events/schedulers/autoscaling/autoscaling.go:63`



---


[function] name: NewScheduler file: events/schedulers/autoscaling/autoscaling.go:74 returns_error: да description: —


### NewScheduler (events/schedulers/autoscaling/autoscaling.go:74)


NewScheduler is a function that performs operations based on the provided parameters and may return an error.


```go
func NewScheduler((autoscaleSettings AutoscaleSettings, ident string, do func(context.Context, *events.XRPCStreamEvent) error)) (autoscaleSettings AutoscaleSettings, ident string, do func(context.Context, *events.XRPCStreamEvent) error)
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


**Тип ответа:** autoscaleSettings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AutoscaleSettings


```json
{
  "Concurrency": 0,
  "MaxConcurrency": 0,
  "AutoscaleFrequency": {},
  "ThroughputBucketCount": 0,
  "ThroughputBucketDuration": {},
  "MaximumBufferedItemsPerRepo": 0
}
```


*Определено в:* `events/schedulers/autoscaling/autoscaling.go`


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `autoscaleSettings AutoscaleSettings`, `ident string`, `do func(context.Context`, `*events.XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/schedulers/autoscaling/autoscaling.go:74`



---


[function] name: Shutdown file: events/schedulers/autoscaling/autoscaling.go:115 returns_error: нет description: —


### Shutdown (events/schedulers/autoscaling/autoscaling.go:115)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) Shutdown(()) ()
```


📍 *Расположение:* `events/schedulers/autoscaling/autoscaling.go:115`



---


[function] name: autoscale file: events/schedulers/autoscaling/autoscaling.go:141 returns_error: нет description: Add autoscaling function


### autoscale (events/schedulers/autoscaling/autoscaling.go:141)


Add autoscaling function


```go
func (p *Scheduler) autoscale(()) ()
```


📍 *Расположение:* `events/schedulers/autoscaling/autoscaling.go:141`



---


[function] name: worker file: events/schedulers/autoscaling/autoscaling.go:201 returns_error: нет description: —


### worker (events/schedulers/autoscaling/autoscaling.go:201)


worker is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) worker(()) ()
```


📍 *Расположение:* `events/schedulers/autoscaling/autoscaling.go:201`




## events/schedulers/autoscaling/throughput.go


📄 Исходный файл: `events/schedulers/autoscaling/throughput.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Add](#add-eventsschedulersautoscalingthroughputgo32) `:32`

- 🔗 [AvgThroughput](#avgthroughput-eventsschedulersautoscalingthroughputgo43) `:43`

- 🔗 [NewThroughputManager](#newthroughputmanager-eventsschedulersautoscalingthroughputgo21) `:21`

- 🔗 [Start](#start-eventsschedulersautoscalingthroughputgo72) `:72`

- 🔗 [Stop](#stop-eventsschedulersautoscalingthroughputgo76) `:76`

- 🔗 [shift](#shift-eventsschedulersautoscalingthroughputgo51) `:51`


</details>


[function] name: Add file: events/schedulers/autoscaling/throughput.go:32 returns_error: нет description: Add increments the count of tasks processed in the current bucket


### Add (events/schedulers/autoscaling/throughput.go:32)


Add increments the count of tasks processed in the current bucket


```go
func (m *ThroughputManager) Add((n int)) (n int)
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


📍 *Расположение:* `events/schedulers/autoscaling/throughput.go:32`



---


[function] name: AvgThroughput file: events/schedulers/autoscaling/throughput.go:43 returns_error: нет description: AvgThroughput returns the average number of tasks processed per
bucketDuration over the past bucketCount buckets.


### AvgThroughput (events/schedulers/autoscaling/throughput.go:43)


AvgThroughput returns the average number of tasks processed per
bucketDuration over the past bucketCount buckets.


```go
func (m *ThroughputManager) AvgThroughput(()) ()
```


📍 *Расположение:* `events/schedulers/autoscaling/throughput.go:43`



---


[function] name: NewThroughputManager file: events/schedulers/autoscaling/throughput.go:21 returns_error: нет description: NewThroughputManager creates a new ThroughputManager with the specified interval.


### NewThroughputManager (events/schedulers/autoscaling/throughput.go:21)


NewThroughputManager creates a new ThroughputManager with the specified interval.


```go
func NewThroughputManager((bucketCount int, bucketDuration time.Duration)) (bucketCount int, bucketDuration time.Duration)
```


**Тип ответа:** bucketCount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bucketDuration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `events/schedulers/autoscaling/throughput.go:21`



---


[function] name: Start file: events/schedulers/autoscaling/throughput.go:72 returns_error: нет description: Start starts the ThroughputManager
It ticks every bucketDuration, shifting the position in the circular buffer.


### Start (events/schedulers/autoscaling/throughput.go:72)


Start starts the ThroughputManager
It ticks every bucketDuration, shifting the position in the circular buffer.


```go
func (m *ThroughputManager) Start(()) ()
```


📍 *Расположение:* `events/schedulers/autoscaling/throughput.go:72`



---


[function] name: Stop file: events/schedulers/autoscaling/throughput.go:76 returns_error: нет description: —


### Stop (events/schedulers/autoscaling/throughput.go:76)


Stop is a method that performs operations based on the provided parameters and returns ().


```go
func (m *ThroughputManager) Stop(()) ()
```


📍 *Расположение:* `events/schedulers/autoscaling/throughput.go:76`



---


[function] name: shift file: events/schedulers/autoscaling/throughput.go:51 returns_error: нет description: shift shifts the position in the circular buffer every bucketDuration, resetting the old value.


### shift (events/schedulers/autoscaling/throughput.go:51)


shift shifts the position in the circular buffer every bucketDuration, resetting the old value.


```go
func (m *ThroughputManager) shift(()) ()
```


📍 *Расположение:* `events/schedulers/autoscaling/throughput.go:51`




## events/schedulers/parallel/parallel.go


📄 Исходный файл: `events/schedulers/parallel/parallel.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [AddWork](#addwork-eventsschedulersparallelparallelgo94) `:94`

- 🔗 [NewScheduler](#newscheduler-eventsschedulersparallelparallelgo40) `:40`

- 🔗 [Shutdown](#shutdown-eventsschedulersparallelparallelgo70) `:70`

- 🔗 [worker](#worker-eventsschedulersparallelparallelgo120) `:120`


</details>


[function] name: AddWork file: events/schedulers/parallel/parallel.go:94 returns_error: нет description: —


### AddWork (events/schedulers/parallel/parallel.go:94)


AddWork is a method that creates new data based on the provided parameters and returns (ctx context.Context, repo string, val *events.XRPCStreamEvent).


```go
func (p *Scheduler) AddWork((ctx context.Context, repo string, val *events.XRPCStreamEvent)) (ctx context.Context, repo string, val *events.XRPCStreamEvent)
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


📍 *Расположение:* `events/schedulers/parallel/parallel.go:94`



---


[function] name: NewScheduler file: events/schedulers/parallel/parallel.go:40 returns_error: да description: —


### NewScheduler (events/schedulers/parallel/parallel.go:40)


NewScheduler is a function that performs operations based on the provided parameters and may return an error.


```go
func NewScheduler((maxC, maxQ int, ident string, do func(context.Context, *events.XRPCStreamEvent) error)) (maxC, maxQ int, ident string, do func(context.Context, *events.XRPCStreamEvent) error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `maxC`, `maxQ int`, `ident string`, `do func(context.Context`, `*events.XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/schedulers/parallel/parallel.go:40`



---


[function] name: Shutdown file: events/schedulers/parallel/parallel.go:70 returns_error: нет description: —


### Shutdown (events/schedulers/parallel/parallel.go:70)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) Shutdown(()) ()
```


📍 *Расположение:* `events/schedulers/parallel/parallel.go:70`



---


[function] name: worker file: events/schedulers/parallel/parallel.go:120 returns_error: нет description: —


### worker (events/schedulers/parallel/parallel.go:120)


worker is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) worker(()) ()
```


📍 *Расположение:* `events/schedulers/parallel/parallel.go:120`




## events/schedulers/sequential/sequential.go


📄 Исходный файл: `events/schedulers/sequential/sequential.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddWork](#addwork-eventsschedulerssequentialsequentialgo46) `:46`

- 🔗 [NewScheduler](#newscheduler-eventsschedulerssequentialsequentialgo25) `:25`

- 🔗 [Shutdown](#shutdown-eventsschedulerssequentialsequentialgo42) `:42`


</details>


[function] name: AddWork file: events/schedulers/sequential/sequential.go:46 returns_error: нет description: —


### AddWork (events/schedulers/sequential/sequential.go:46)


AddWork is a method that creates new data based on the provided parameters and returns (ctx context.Context, repo string, val *events.XRPCStreamEvent).


```go
func (s *Scheduler) AddWork((ctx context.Context, repo string, val *events.XRPCStreamEvent)) (ctx context.Context, repo string, val *events.XRPCStreamEvent)
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


📍 *Расположение:* `events/schedulers/sequential/sequential.go:46`



---


[function] name: NewScheduler file: events/schedulers/sequential/sequential.go:25 returns_error: да description: —


### NewScheduler (events/schedulers/sequential/sequential.go:25)


NewScheduler is a function that performs operations based on the provided parameters and may return an error.


```go
func NewScheduler((ident string, do func(context.Context, *events.XRPCStreamEvent) error)) (ident string, do func(context.Context, *events.XRPCStreamEvent) error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ident string`, `do func(context.Context`, `*events.XRPCStreamEvent) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `events/schedulers/sequential/sequential.go:25`



---


[function] name: Shutdown file: events/schedulers/sequential/sequential.go:42 returns_error: нет description: —


### Shutdown (events/schedulers/sequential/sequential.go:42)


Shutdown is a method that performs operations based on the provided parameters and returns ().


```go
func (p *Scheduler) Shutdown(()) ()
```


📍 *Расположение:* `events/schedulers/sequential/sequential.go:42`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](events_pebblepersist.md)

- [Следующая директория](events_yolopersist.md)


---

