---
title: "Функции: cmd/netsync"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/netsync
---


# Функции: cmd/netsync


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_lexgen.md)

- [Следующая директория](cmd_palomar.md)


---


## Меню по файлам


- 📄 [cmd/netsync/main.go](#cmdnetsyncmaingo)


---


## cmd/netsync/main.go


📄 Исходный файл: `cmd/netsync/main.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Close](#close-cmdnetsyncmaingo168) `:168`

- 🔗 [Dequeue](#dequeue-cmdnetsyncmaingo226) `:226`

- 🔗 [Finish](#finish-cmdnetsyncmaingo247) `:247`

- 🔗 [Netsync](#netsync-cmdnetsyncmaingo262) `:262`

- 🔗 [Read](#read-cmdnetsyncmaingo162) `:162`

- 🔗 [Resume](#resume-cmdnetsyncmaingo202) `:202`

- 🔗 [Save](#save-cmdnetsyncmaingo183) `:183`

- 🔗 [cloneRepo](#clonerepo-cmdnetsyncmaingo474) `:474`

- 🔗 [main](#main-cmdnetsyncmaingo36) `:36`

- 🔗 [worker](#worker-cmdnetsyncmaingo430) `:430`


</details>


[function] name: Close file: cmd/netsync/main.go:168 returns_error: нет description: —


### Close (cmd/netsync/main.go:168)


Close is a method that performs operations based on the provided parameters and returns ().


```go
func (r instrumentedReader) Close(()) ()
```


📍 *Расположение:* `cmd/netsync/main.go:168`



---


[function] name: Dequeue file: cmd/netsync/main.go:226 returns_error: нет description: —


### Dequeue (cmd/netsync/main.go:226)


Dequeue is a method that performs operations based on the provided parameters and returns ().


```go
func (s *NetsyncState) Dequeue(()) ()
```


📍 *Расположение:* `cmd/netsync/main.go:226`



---


[function] name: Finish file: cmd/netsync/main.go:247 returns_error: нет description: —


### Finish (cmd/netsync/main.go:247)


Finish is a method that performs operations based on the provided parameters and returns (repo string, state string).


```go
func (s *NetsyncState) Finish((repo string, state string)) (repo string, state string)
```


**Тип ответа:** repo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** state


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/netsync/main.go:247`



---


[function] name: Netsync file: cmd/netsync/main.go:262 returns_error: нет description: —


### Netsync (cmd/netsync/main.go:262)


Netsync is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func Netsync((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `cmd/netsync/main.go:262`



---


[function] name: Read file: cmd/netsync/main.go:162 returns_error: да description: —


### Read (cmd/netsync/main.go:162)


Read is a method that performs operations based on the provided parameters and may return an error.


```go
func (r instrumentedReader) Read((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/netsync/main.go:162`



---


[function] name: Resume file: cmd/netsync/main.go:202 returns_error: нет description: —


### Resume (cmd/netsync/main.go:202)


Resume is a method that performs operations based on the provided parameters and returns ().


```go
func (s *NetsyncState) Resume(()) ()
```


📍 *Расположение:* `cmd/netsync/main.go:202`



---


[function] name: Save file: cmd/netsync/main.go:183 returns_error: нет description: —


### Save (cmd/netsync/main.go:183)


Save is a method that performs operations based on the provided parameters and returns ().


```go
func (s *NetsyncState) Save(()) ()
```


📍 *Расположение:* `cmd/netsync/main.go:183`



---


[function] name: cloneRepo file: cmd/netsync/main.go:474 returns_error: да description: —


### cloneRepo (cmd/netsync/main.go:474)


cloneRepo is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *NetsyncState) cloneRepo((cloneState string, err error)) (cloneState string, err error)
```


**Тип ответа:** cloneState


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


*Типы возврата:* `cloneState string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/netsync/main.go:474`



---


[function] name: main file: cmd/netsync/main.go:36 returns_error: нет description: —


### main (cmd/netsync/main.go:36)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/netsync/main.go:36`



---


[function] name: worker file: cmd/netsync/main.go:430 returns_error: нет description: —


### worker (cmd/netsync/main.go:430)


worker is a method that performs operations based on the provided parameters and returns (id int).


```go
func (s *NetsyncState) worker((id int)) (id int)
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


📍 *Расположение:* `cmd/netsync/main.go:430`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_lexgen.md)

- [Следующая директория](cmd_palomar.md)


---

