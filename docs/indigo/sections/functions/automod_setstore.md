---
title: "Функции: automod/setstore"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/setstore
---


# Функции: automod/setstore


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_rules.md)

- [Следующая директория](automod_visual.md)


---


## Меню по файлам


- 📄 [automod/setstore/setstore.go](#automodsetstoresetstorego)


---


## automod/setstore/setstore.go


📄 Исходный файл: `automod/setstore/setstore.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [InSet](#inset-automodsetstoresetstorego25) `:25`

- 🔗 [LoadFromFileJSON](#loadfromfilejson-automodsetstoresetstorego35) `:35`

- 🔗 [NewMemSetStore](#newmemsetstore-automodsetstoresetstorego19) `:19`


</details>


[function] name: InSet file: automod/setstore/setstore.go:25 returns_error: да description: —


### InSet (automod/setstore/setstore.go:25)


InSet is a method that performs operations based on the provided parameters and may return an error.


```go
func (s MemSetStore) InSet((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/setstore/setstore.go:25`



---


[function] name: LoadFromFileJSON file: automod/setstore/setstore.go:35 returns_error: нет description: —


### LoadFromFileJSON (automod/setstore/setstore.go:35)


LoadFromFileJSON is a method that performs operations based on the provided parameters and returns (p string).


```go
func (s *MemSetStore) LoadFromFileJSON((p string)) (p string)
```


**Тип ответа:** p


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


📍 *Расположение:* `automod/setstore/setstore.go:35`



---


[function] name: NewMemSetStore file: automod/setstore/setstore.go:19 returns_error: нет description: —


### NewMemSetStore (automod/setstore/setstore.go:19)


NewMemSetStore is a function that performs operations based on the provided parameters and returns ().


```go
func NewMemSetStore(()) ()
```


📍 *Расположение:* `automod/setstore/setstore.go:19`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_rules.md)

- [Следующая директория](automod_visual.md)


---

