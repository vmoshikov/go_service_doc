---
title: "Функции: repo/carutil"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: repo/carutil
---


# Функции: repo/carutil


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](repo.md)

- [Следующая директория](repomgr.md)


---


## Меню по файлам


- 📄 [repo/carutil/reader.go](#repocarutilreadergo)


---


## repo/carutil/reader.go


📄 Исходный файл: `repo/carutil/reader.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [BaseBuffer](#basebuffer-repocarutilreadergo131) `:131`

- 🔗 [Cid](#cid-repocarutilreadergo115) `:115`

- 🔗 [Loggable](#loggable-repocarutilreadergo125) `:125`

- 🔗 [NewBlockWithCid](#newblockwithcid-repocarutilreadergo105) `:105`

- 🔗 [NewReader](#newreader-repocarutilreadergo18) `:18`

- 🔗 [NextBlock](#nextblock-repocarutilreadergo39) `:39`

- 🔗 [NextBlockBuf](#nextblockbuf-repocarutilreadergo48) `:48`

- 🔗 [RawData](#rawdata-repocarutilreadergo110) `:110`

- 🔗 [String](#string-repocarutilreadergo120) `:120`

- 🔗 [ldRead](#ldread-repocarutilreadergo64) `:64`


</details>


[function] name: BaseBuffer file: repo/carutil/reader.go:131 returns_error: нет description: —


### BaseBuffer (repo/carutil/reader.go:131)


BaseBuffer is a method that performs operations based on the provided parameters and returns ().


```go
func (b *BasicBlock) BaseBuffer(()) ()
```


📍 *Расположение:* `repo/carutil/reader.go:131`



---


[function] name: Cid file: repo/carutil/reader.go:115 returns_error: нет description: Cid returns the content identifier of the block.


### Cid (repo/carutil/reader.go:115)


Cid returns the content identifier of the block.


```go
func (b *BasicBlock) Cid(()) ()
```


📍 *Расположение:* `repo/carutil/reader.go:115`



---


[function] name: Loggable file: repo/carutil/reader.go:125 returns_error: нет description: Loggable returns a go-log loggable item.


### Loggable (repo/carutil/reader.go:125)


Loggable returns a go-log loggable item.


```go
func (b *BasicBlock) Loggable(()) ()
```


📍 *Расположение:* `repo/carutil/reader.go:125`



---


[function] name: NewBlockWithCid file: repo/carutil/reader.go:105 returns_error: нет description: —


### NewBlockWithCid (repo/carutil/reader.go:105)


NewBlockWithCid is a function that performs operations based on the provided parameters and returns (data, base []byte, c cid.Cid).


```go
func NewBlockWithCid((data, base []byte, c cid.Cid)) (data, base []byte, c cid.Cid)
```


**Тип ответа:** data


```json
{
  "AuthorizationServers": []
}
```


*Определено в:* `atproto/auth/oauth/types.go`


**Тип ответа:** base


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


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `repo/carutil/reader.go:105`



---


[function] name: NewReader file: repo/carutil/reader.go:18 returns_error: да description: —


### NewReader (repo/carutil/reader.go:18)


NewReader is a function that performs operations based on the provided parameters and may return an error.


```go
func NewReader((*Reader, cid.Cid, error)) (*Reader, cid.Cid, error)
```


**Тип запроса:** Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


**Тип ответа:** Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Reader`, `cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/carutil/reader.go:18`



---


[function] name: NextBlock file: repo/carutil/reader.go:39 returns_error: да description: —


### NextBlock (repo/carutil/reader.go:39)


NextBlock is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Reader) NextBlock((*BasicBlock, error)) (*BasicBlock, error)
```


**Тип запроса:** BasicBlock


```json
{
  "cid": {},
  "data": [],
  "base": []
}
```


*Определено в:* `repo/carutil/reader.go`


**Тип ответа:** BasicBlock


```json
{
  "cid": {},
  "data": [],
  "base": []
}
```


*Определено в:* `repo/carutil/reader.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*BasicBlock`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/carutil/reader.go:39`



---


[function] name: NextBlockBuf file: repo/carutil/reader.go:48 returns_error: да description: —


### NextBlockBuf (repo/carutil/reader.go:48)


NextBlockBuf is a method that performs operations based on the provided parameters and may return an error.


```go
func (r *Reader) NextBlockBuf((*BasicBlock, bool, error)) (*BasicBlock, bool, error)
```


**Тип запроса:** BasicBlock


```json
{
  "cid": {},
  "data": [],
  "base": []
}
```


*Определено в:* `repo/carutil/reader.go`


**Тип ответа:** BasicBlock


```json
{
  "cid": {},
  "data": [],
  "base": []
}
```


*Определено в:* `repo/carutil/reader.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*BasicBlock`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/carutil/reader.go:48`



---


[function] name: RawData file: repo/carutil/reader.go:110 returns_error: нет description: RawData returns the block raw contents as a byte slice.


### RawData (repo/carutil/reader.go:110)


RawData returns the block raw contents as a byte slice.


```go
func (b *BasicBlock) RawData(()) ()
```


📍 *Расположение:* `repo/carutil/reader.go:110`



---


[function] name: String file: repo/carutil/reader.go:120 returns_error: нет description: String provides a human-readable representation of the block CID.


### String (repo/carutil/reader.go:120)


String provides a human-readable representation of the block CID.


```go
func (b *BasicBlock) String(()) ()
```


📍 *Расположение:* `repo/carutil/reader.go:120`



---


[function] name: ldRead file: repo/carutil/reader.go:64 returns_error: да description: reads a length delimited value off of the given reader into the the given buf if its big enough, otherwise allocates a n


### ldRead (repo/carutil/reader.go:64)


reads a length delimited value off of the given reader into the the given buf if its big enough, otherwise allocates a new buffer.
returns whether or not the passed in buffer was used


```go
func ldRead(([]byte, bool, error)) ([]byte, bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repo/carutil/reader.go:64`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](repo.md)

- [Следующая директория](repomgr.md)


---

