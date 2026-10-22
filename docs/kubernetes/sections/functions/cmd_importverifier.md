---
title: "Функции: cmd/importverifier"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: cmd/importverifier
---


# Функции: cmd/importverifier


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_import-boss.md)

- [Следующая директория](cmd_kube-apiserver.md)


---


## Меню по файлам


- 📄 [cmd/importverifier/importverifier.go](#cmdimportverifierimportverifiergo)


---


## cmd/importverifier/importverifier.go


📄 Исходный файл: `cmd/importverifier/importverifier.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [ForbiddenImportsFor](#forbiddenimportsfor-cmdimportverifierimportverifiergo64) `:64`

- 🔗 [decodePackages](#decodepackages-cmdimportverifierimportverifiergo251) `:251`

- 🔗 [forbiddenImportsFor](#forbiddenimportsfor-cmdimportverifierimportverifiergo121) `:121`

- 🔗 [isForbidden](#isforbidden-cmdimportverifierimportverifiergo145) `:145`

- 🔗 [isPathUnder](#ispathunder-cmdimportverifierimportverifiergo98) `:98`

- 🔗 [isRestrictedDir](#isrestricteddir-cmdimportverifierimportverifiergo79) `:79`

- 🔗 [loadImportRestrictions](#loadimportrestrictions-cmdimportverifierimportverifiergo214) `:214`

- 🔗 [logForbiddenPackages](#logforbiddenpackages-cmdimportverifierimportverifiergo270) `:270`

- 🔗 [main](#main-cmdimportverifierimportverifiergo160) `:160`

- 🔗 [resolvePackageTree](#resolvepackagetree-cmdimportverifierimportverifiergo228) `:228`


</details>


[function] name: ForbiddenImportsFor file: cmd/importverifier/importverifier.go:64 returns_error: да description: ForbiddenImportsFor determines all of the forbidden
imports for a package given the import restrictions


### ForbiddenImportsFor (cmd/importverifier/importverifier.go:64)


ForbiddenImportsFor determines all of the forbidden
imports for a package given the import restrictions


```go
func (i *ImportRestriction) ForbiddenImportsFor(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/importverifier/importverifier.go:64`



---


[function] name: decodePackages file: cmd/importverifier/importverifier.go:251 returns_error: да description: —


### decodePackages (cmd/importverifier/importverifier.go:251)


decodePackages is a function that performs operations based on the provided parameters and may return an error.


```go
func decodePackages(([]Package, error)) ([]Package, error)
```


**Тип ответа:** Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]Package`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/importverifier/importverifier.go:251`



---


[function] name: forbiddenImportsFor file: cmd/importverifier/importverifier.go:121 returns_error: нет description: forbiddenImportsFor determines all of the forbidden
imports for a package given the import restrictions
and returns a de


### forbiddenImportsFor (cmd/importverifier/importverifier.go:121)


forbiddenImportsFor determines all of the forbidden
imports for a package given the import restrictions
and returns a deduplicated list of them


```go
func (i *ImportRestriction) forbiddenImportsFor((pkg Package)) (pkg Package)
```


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `cmd/importverifier/importverifier.go:121`



---


[function] name: isForbidden file: cmd/importverifier/importverifier.go:145 returns_error: нет description: isForbidden determines if an import is forbidden,
which is true when the import is:
- of a package under the rootPackage


### isForbidden (cmd/importverifier/importverifier.go:145)


isForbidden determines if an import is forbidden,
which is true when the import is:
- of a package under the rootPackage
- is not of the base import path or a sub-package of it
- is not of an allowed path or a sub-package of one


```go
func (i *ImportRestriction) isForbidden((imp string)) (imp string)
```


**Тип ответа:** imp


```json
{
  "impersonate": {},
  "delegate": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


📍 *Расположение:* `cmd/importverifier/importverifier.go:145`



---


[function] name: isPathUnder file: cmd/importverifier/importverifier.go:98 returns_error: да description: isPathUnder determines if path is under base


### isPathUnder (cmd/importverifier/importverifier.go:98)


isPathUnder determines if path is under base


```go
func isPathUnder((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/importverifier/importverifier.go:98`



---


[function] name: isRestrictedDir file: cmd/importverifier/importverifier.go:79 returns_error: да description: isRestrictedDir determines if the source directory has
any restrictions placed on it by this configuration.
A path will 


### isRestrictedDir (cmd/importverifier/importverifier.go:79)


isRestrictedDir determines if the source directory has
any restrictions placed on it by this configuration.
A path will be restricted if:
- it falls under the base import path
- it does not fall under any of the ignored sub-trees


```go
func (i *ImportRestriction) isRestrictedDir((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/importverifier/importverifier.go:79`



---


[function] name: loadImportRestrictions file: cmd/importverifier/importverifier.go:214 returns_error: да description: —


### loadImportRestrictions (cmd/importverifier/importverifier.go:214)


loadImportRestrictions is a function that performs operations based on the provided parameters and may return an error.


```go
func loadImportRestrictions(([]ImportRestriction, error)) ([]ImportRestriction, error)
```


**Тип ответа:** ImportRestriction


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]ImportRestriction`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/importverifier/importverifier.go:214`



---


[function] name: logForbiddenPackages file: cmd/importverifier/importverifier.go:270 returns_error: нет description: —


### logForbiddenPackages (cmd/importverifier/importverifier.go:270)


logForbiddenPackages is a function that performs operations based on the provided parameters and returns (base string, forbidden []string).


```go
func logForbiddenPackages((base string, forbidden []string)) (base string, forbidden []string)
```


**Тип ответа:** base


```json
{
  "w": {},
  "handlerHeaders": {},
  "mu": {},
  "timedOut": false,
  "wroteHeader": false,
  "hijacked": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


**Тип ответа:** forbidden


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `cmd/importverifier/importverifier.go:270`



---


[function] name: main file: cmd/importverifier/importverifier.go:160 returns_error: нет description: —


### main (cmd/importverifier/importverifier.go:160)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `cmd/importverifier/importverifier.go:160`



---


[function] name: resolvePackageTree file: cmd/importverifier/importverifier.go:228 returns_error: да description: —


### resolvePackageTree (cmd/importverifier/importverifier.go:228)


resolvePackageTree is a function that performs operations based on the provided parameters and may return an error.


```go
func resolvePackageTree(([]Package, error)) ([]Package, error)
```


**Тип ответа:** Package


```json
{
  "Dir": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]Package`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `cmd/importverifier/importverifier.go:228`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](cmd_import-boss.md)

- [Следующая директория](cmd_kube-apiserver.md)


---

