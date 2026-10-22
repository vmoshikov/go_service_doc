---
title: "Функции: testing"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: testing
---


# Функции: testing


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](splitter.md)

- [Следующая директория](util.md)


---


## Меню по файлам


- 📄 [testing/utils.go](#testingutilsgo)


---


## testing/utils.go


📄 Исходный файл: `testing/utils.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [GenerateFakeRepo](#generatefakerepo-testingutilsgo139) `:139`

- 🔗 [MakeRandomPost](#makerandompost-testingutilsgo41) `:41`

- 🔗 [RandAction](#randaction-testingutilsgo126) `:126`

- 🔗 [RandFakeAtUri](#randfakeaturi-testingutilsgo113) `:113`

- 🔗 [RandFakeCid](#randfakecid-testingutilsgo100) `:100`

- 🔗 [RandSentence](#randsentence-testingutilsgo79) `:79`

- 🔗 [ReadWords](#readwords-testingutilsgo91) `:91`


</details>


[function] name: GenerateFakeRepo file: testing/utils.go:139 returns_error: да description: —


### GenerateFakeRepo (testing/utils.go:139)


GenerateFakeRepo is a function that performs operations based on the provided parameters and may return an error.


```go
func GenerateFakeRepo((cid.Cid, error)) (cid.Cid, error)
```


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `testing/utils.go:139`



---


[function] name: MakeRandomPost file: testing/utils.go:41 returns_error: нет description: —


### MakeRandomPost (testing/utils.go:41)


MakeRandomPost is a function that performs operations based on the provided parameters and returns ().


```go
func MakeRandomPost(()) ()
```


📍 *Расположение:* `testing/utils.go:41`



---


[function] name: RandAction file: testing/utils.go:126 returns_error: нет description: —


### RandAction (testing/utils.go:126)


RandAction is a function that performs operations based on the provided parameters and returns ().


```go
func RandAction(()) ()
```


📍 *Расположение:* `testing/utils.go:126`



---


[function] name: RandFakeAtUri file: testing/utils.go:113 returns_error: нет description: —


### RandFakeAtUri (testing/utils.go:113)


RandFakeAtUri is a function that performs operations based on the provided parameters and returns (collection, rkey string).


```go
func RandFakeAtUri((collection, rkey string)) (collection, rkey string)
```


**Тип ответа:** collection


```json
{
  "ctx": {},
  "pcd": null,
  "dauDirectory": null,
  "dauDirectoryPath": "string",
  "dauDay": {},
  "dauTomorrow": {},
  "dauDirectoryDir": "string",
  "statsCache": null,
  "statsCacheWhen": {},
  "statsCacheLock": {},
  "statsCacheFresh": {},
  "statsCachePending": false,
  "ingestFirehose": {},
  "ingestCrawl": {},
  "log": null,
  "AdminToken": "string",
  "ExepctedAuthHeader": "string",
  "PerPDSCrawlQPS": 0.0,
  "activeCrawls": {},
  "activeCrawlsLock": {},
  "shutdown": {},
  "wg": {},
  "ratelimitHeader": "string",
  "apiServer": null,
  "metricsServer": null,
  "MinDidsForCollectionList": 0,
  "MaxDidCollections": 0,
  "didCollectionCounts": null,
  "badwords": {}
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** rkey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `testing/utils.go:113`



---


[function] name: RandFakeCid file: testing/utils.go:100 returns_error: нет description: —


### RandFakeCid (testing/utils.go:100)


RandFakeCid is a function that performs operations based on the provided parameters and returns ().


```go
func RandFakeCid(()) ()
```


📍 *Расположение:* `testing/utils.go:100`



---


[function] name: RandSentence file: testing/utils.go:79 returns_error: нет description: —


### RandSentence (testing/utils.go:79)


RandSentence is a function that performs operations based on the provided parameters and returns (words []string, maxl int).


```go
func RandSentence((words []string, maxl int)) (words []string, maxl int)
```


**Тип ответа:** words


```json
{
  "re": null
}
```


*Определено в:* `cmd/collectiondir/serve.go`


**Тип ответа:** maxl


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `testing/utils.go:79`



---


[function] name: ReadWords file: testing/utils.go:91 returns_error: да description: —


### ReadWords (testing/utils.go:91)


ReadWords is a function that performs operations based on the provided parameters and may return an error.


```go
func ReadWords(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `testing/utils.go:91`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](splitter.md)

- [Следующая директория](util.md)


---

