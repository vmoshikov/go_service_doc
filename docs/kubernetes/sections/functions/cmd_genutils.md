---
title: "Функции: cmd/genutils"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/genutils
---


# Функции: cmd/genutils


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genswaggertypedocs.md)

- [Следующая директория](cmd_genyaml.md)


---


## Меню по файлам


- 📄 [cmd/genutils/genutils.go](#cmdgenutilsgenutilsgo)


---


## cmd/genutils/genutils.go


📄 Исходный файл: `cmd/genutils/genutils.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [OutDir](#outdir-cmdgenutilsgenutilsgo27) `:27`


</details>


[function] name: OutDir file: cmd/genutils/genutils.go:27 returns_error: да description: OutDir creates the absolute path name from path and checks path exists.
Returns absolute path including trailing '/' or 


### OutDir (cmd/genutils/genutils.go:27)


OutDir creates the absolute path name from path and checks path exists.
Returns absolute path including trailing '/' or error if path does not exist.


```go
func OutDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/genutils/genutils.go:27`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_genswaggertypedocs.md)

- [Следующая директория](cmd_genyaml.md)


---

