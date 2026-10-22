---
title: "Функции: models"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: models
---


# Функции: models


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](lex_util.md)

- [Следующая директория](mst.md)


---


## Меню по файлам


- 📄 [models/dbcid.go](#modelsdbcidgo)

- 📄 [models/models.go](#modelsmodelsgo)


---


## models/dbcid.go


📄 Исходный файл: `models/dbcid.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GormDataType](#gormdatatype-modelsdbcidgo61) `:61`

- 🔗 [MarshalJSON](#marshaljson-modelsdbcidgo42) `:42`

- 🔗 [Scan](#scan-modelsdbcidgo16) `:16`

- 🔗 [UnmarshalJSON](#unmarshaljson-modelsdbcidgo46) `:46`

- 🔗 [Value](#value-modelsdbcidgo35) `:35`


</details>


[function] name: GormDataType file: models/dbcid.go:61 returns_error: нет description: —


### GormDataType (models/dbcid.go:61)


GormDataType is a method that performs operations based on the provided parameters and returns ().


```go
func (dbc *DbCID) GormDataType(()) ()
```


📍 *Расположение:* `models/dbcid.go:61`



---


[function] name: MarshalJSON file: models/dbcid.go:42 returns_error: да description: —


### MarshalJSON (models/dbcid.go:42)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (dbc DbCID) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `models/dbcid.go:42`



---


[function] name: Scan file: models/dbcid.go:16 returns_error: нет description: —


### Scan (models/dbcid.go:16)


Scan is a method that performs operations based on the provided parameters and returns (v interface{}).


```go
func (dbc *DbCID) Scan((v interface{})) (v interface{})
```


**Тип ответа:** v


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


**Тип ответа:** interface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `models/dbcid.go:16`



---


[function] name: UnmarshalJSON file: models/dbcid.go:46 returns_error: нет description: —


### UnmarshalJSON (models/dbcid.go:46)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (dbc *DbCID) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `models/dbcid.go:46`



---


[function] name: Value file: models/dbcid.go:35 returns_error: да description: —


### Value (models/dbcid.go:35)


Value is a method that performs operations based on the provided parameters and may return an error.


```go
func (dbc DbCID) Value((driver.Value, error)) (driver.Value, error)
```


**Тип ответа:** driver.Value


```json
{
  "cursor": "string",
  "set": null,
  "values": []
}
```


*Определено в:* `api/ozone/setgetValues.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `driver.Value`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `models/dbcid.go:35`




## models/models.go


📄 Исходный файл: `models/models.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [ActorRef](#actorref-modelsmodelsgo51) `:51`

- 🔗 [ActorView](#actorview-modelsmodelsgo60) `:60`

- 🔗 [ClientForPds](#clientforpds-modelsmodelsgo124) `:124`

- 🔗 [String](#string-modelsmodelsgo70) `:70`


</details>


[function] name: ActorRef file: models/models.go:51 returns_error: нет description: —


### ActorRef (models/models.go:51)


ActorRef is a method that performs operations based on the provided parameters and returns ().


```go
func (ai *ActorInfo) ActorRef(()) ()
```


📍 *Расположение:* `models/models.go:51`



---


[function] name: ActorView file: models/models.go:60 returns_error: нет description: TODO: this is just s stub; needs to populate more info


### ActorView (models/models.go:60)


TODO: this is just s stub; needs to populate more info


```go
func (ai *ActorInfo) ActorView(()) ()
```


📍 *Расположение:* `models/models.go:60`



---


[function] name: ClientForPds file: models/models.go:124 returns_error: нет description: —


### ClientForPds (models/models.go:124)


ClientForPds is a function that performs operations based on the provided parameters and returns (pds *PDS).


```go
func ClientForPds((pds *PDS)) (pds *PDS)
```


**Тип запроса:** PDS


```json
{
  "Host": "string",
  "Did": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "RateLimit": 0.0,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HourlyEventLimit": 0,
  "DailyEventLimit": 0
}
```


*Определено в:* `models/models.go`


**Тип ответа:** pds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PDS


```json
{
  "Host": "string",
  "Did": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "RateLimit": 0.0,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HourlyEventLimit": 0,
  "DailyEventLimit": 0
}
```


*Определено в:* `models/models.go`


📍 *Расположение:* `models/models.go:124`



---


[function] name: String file: models/models.go:70 returns_error: нет description: —


### String (models/models.go:70)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (vd VoteDir) String(()) ()
```


📍 *Расположение:* `models/models.go:70`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](lex_util.md)

- [Следующая директория](mst.md)


---

