---
title: "Функции: pkg/fieldpath"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/fieldpath
---


# Функции: pkg/fieldpath


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_features.md)

- [Следующая директория](pkg_generated.md)


---


## Меню по файлам


- 📄 [pkg/fieldpath/fieldpath.go](#pkgfieldpathfieldpathgo)


---


## pkg/fieldpath/fieldpath.go


📄 Исходный файл: `pkg/fieldpath/fieldpath.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [ExtractFieldPathAsString](#extractfieldpathasstring-pkgfieldpathfieldpathgo56) `:56`

- 🔗 [FormatMap](#formatmap-pkgfieldpathfieldpathgo30) `:30`

- 🔗 [SplitMaybeSubscriptedPath](#splitmaybesubscriptedpath-pkgfieldpathfieldpathgo107) `:107`


</details>


[function] name: ExtractFieldPathAsString file: pkg/fieldpath/fieldpath.go:56 returns_error: да description: ExtractFieldPathAsString extracts the field from the given object
and returns it as a string.  The object must be a poin


### ExtractFieldPathAsString (pkg/fieldpath/fieldpath.go:56)


ExtractFieldPathAsString extracts the field from the given object
and returns it as a string.  The object must be a pointer to an
API type.


```go
func ExtractFieldPathAsString((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/fieldpath/fieldpath.go:56`



---


[function] name: FormatMap file: pkg/fieldpath/fieldpath.go:30 returns_error: нет description: FormatMap formats map[string]string to a string.


### FormatMap (pkg/fieldpath/fieldpath.go:30)


FormatMap formats map[string]string to a string.


```go
func FormatMap((fmtStr string)) (fmtStr string)
```


**Тип ответа:** fmtStr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/fieldpath/fieldpath.go:30`



---


[function] name: SplitMaybeSubscriptedPath file: pkg/fieldpath/fieldpath.go:107 returns_error: нет description: SplitMaybeSubscriptedPath checks whether the specified fieldPath is
subscripted, and
- if yes, this function splits the 


### SplitMaybeSubscriptedPath (pkg/fieldpath/fieldpath.go:107)


SplitMaybeSubscriptedPath checks whether the specified fieldPath is
subscripted, and
- if yes, this function splits the fieldPath into path and subscript, and
returns (path, subscript, true).
- if no, this function returns (fieldPath, "", false).

Example inputs and outputs:

"metadata.annotations['myKey']" --> ("metadata.annotations", "myKey", true)
"metadata.annotations['a[b]c']" --> ("metadata.annotations", "a[b]c", true)
"metadata.labels['']"           --> ("metadata.labels", "", true)
"metadata.labels"               --> ("metadata.labels", "", false)


```go
func SplitMaybeSubscriptedPath((string, string, bool)) (string, string, bool)
```


📍 *Расположение:* `pkg/fieldpath/fieldpath.go:107`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_features.md)

- [Следующая директория](pkg_generated.md)


---

