---
title: "Функции: cmd/lexgen"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: cmd/lexgen
---


# Функции: cmd/lexgen


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_hepa.md)

- [Следующая директория](cmd_netsync.md)


---


## Меню по файлам


- 📄 [cmd/lexgen/main.go](#cmdlexgenmaingo)


---


## cmd/lexgen/main.go


📄 Исходный файл: `cmd/lexgen/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [expandArgs](#expandargs-cmdlexgenmaingo40) `:40`

- 🔗 [findSchemas](#findschemas-cmdlexgenmaingo15) `:15`

- 🔗 [main](#main-cmdlexgenmaingo60) `:60`


</details>


[function] name: expandArgs file: cmd/lexgen/main.go:40 returns_error: да description: for direct .json lexicon files or directories containing lexicon .json files, get one flat list of all paths to .json fi


### expandArgs (cmd/lexgen/main.go:40)


for direct .json lexicon files or directories containing lexicon .json files, get one flat list of all paths to .json files


```go
func expandArgs(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/lexgen/main.go:40`



---


[function] name: findSchemas file: cmd/lexgen/main.go:15 returns_error: да description: —


### findSchemas (cmd/lexgen/main.go:15)


findSchemas is a function that performs operations based on the provided parameters and may return an error.


```go
func findSchemas(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/lexgen/main.go:15`



---


[function] name: main file: cmd/lexgen/main.go:60 returns_error: нет description: —


### main (cmd/lexgen/main.go:60)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/lexgen/main.go:60`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_hepa.md)

- [Следующая директория](cmd_netsync.md)


---

