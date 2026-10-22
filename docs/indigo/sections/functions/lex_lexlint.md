---
title: "Функции: lex/lexlint"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: lex/lexlint
---


# Функции: lex/lexlint


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](lex_lexgen.md)

- [Следующая директория](lex_util.md)


---


## Меню по файлам


- 📄 [lex/lexlint/breaking.go](#lexlexlintbreakinggo)

- 📄 [lex/lexlint/lint.go](#lexlexlintlintgo)

- 📄 [lex/lexlint/syntax.go](#lexlexlintsyntaxgo)


---


## lex/lexlint/breaking.go


📄 Исходный файл: `lex/lexlint/breaking.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [BreakingChanges](#breakingchanges-lexlexlintbreakinggo13) `:13`

- 🔗 [breakingDefs](#breakingdefs-lexlexlintbreakinggo54) `:54`

- 🔗 [breakingMaps](#breakingmaps-lexlexlintbreakinggo17) `:17`

- 🔗 [eqOptBool](#eqoptbool-lexlexlintbreakinggo354) `:354`

- 🔗 [eqOptInt](#eqoptint-lexlexlintbreakinggo344) `:344`

- 🔗 [eqOptString](#eqoptstring-lexlexlintbreakinggo364) `:364`


</details>


[function] name: BreakingChanges file: lex/lexlint/breaking.go:13 returns_error: нет description: —


### BreakingChanges (lex/lexlint/breaking.go:13)


BreakingChanges is a function that performs operations based on the provided parameters and returns (before, after *lexicon.SchemaFile).


```go
func BreakingChanges((before, after *lexicon.SchemaFile)) (before, after *lexicon.SchemaFile)
```


**Тип запроса:** lexicon.SchemaFile


```json
{
  "Type": "string",
  "Lexicon": 0,
  "ID": "string",
  "Description": "string",
  "Defs": {}
}
```


*Определено в:* `atproto/lexicon/schemafile.go`


**Тип ответа:** before


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** after


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaFile


```json
{
  "Type": "string",
  "Lexicon": 0,
  "ID": "string",
  "Description": "string",
  "Defs": {}
}
```


*Определено в:* `atproto/lexicon/schemafile.go`


📍 *Расположение:* `lex/lexlint/breaking.go:13`



---


[function] name: breakingDefs file: lex/lexlint/breaking.go:54 returns_error: нет description: —


### breakingDefs (lex/lexlint/breaking.go:54)


breakingDefs is a function that performs operations based on the provided parameters and returns (nsid syntax.NSID, name string, local, remote lexicon.SchemaDef).


```go
func breakingDefs((nsid syntax.NSID, name string, local, remote lexicon.SchemaDef)) (nsid syntax.NSID, name string, local, remote lexicon.SchemaDef)
```


**Тип ответа:** nsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** local


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** remote


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


📍 *Расположение:* `lex/lexlint/breaking.go:54`



---


[function] name: breakingMaps file: lex/lexlint/breaking.go:17 returns_error: нет description: —


### breakingMaps (lex/lexlint/breaking.go:17)


breakingMaps is a function that performs operations based on the provided parameters and returns (nsid syntax.NSID, localMap, remoteMap map[string]lexicon.SchemaDef).


```go
func breakingMaps((nsid syntax.NSID, localMap, remoteMap map[string]lexicon.SchemaDef)) (nsid syntax.NSID, localMap, remoteMap map[string]lexicon.SchemaDef)
```


**Тип ответа:** nsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** localMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** remoteMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


📍 *Расположение:* `lex/lexlint/breaking.go:17`



---


[function] name: eqOptBool file: lex/lexlint/breaking.go:354 returns_error: нет description: —


### eqOptBool (lex/lexlint/breaking.go:354)


eqOptBool is a function that performs operations based on the provided parameters and returns (a, b *bool).


```go
func eqOptBool((a, b *bool)) (a, b *bool)
```


**Тип ответа:** a


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


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


📍 *Расположение:* `lex/lexlint/breaking.go:354`



---


[function] name: eqOptInt file: lex/lexlint/breaking.go:344 returns_error: нет description: helper to check if two optional (pointer) integers are equal/consistent


### eqOptInt (lex/lexlint/breaking.go:344)


helper to check if two optional (pointer) integers are equal/consistent


```go
func eqOptInt((a, b *int)) (a, b *int)
```


**Тип ответа:** a


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


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


📍 *Расположение:* `lex/lexlint/breaking.go:344`



---


[function] name: eqOptString file: lex/lexlint/breaking.go:364 returns_error: нет description: —


### eqOptString (lex/lexlint/breaking.go:364)


eqOptString is a function that performs operations based on the provided parameters and returns (a, b *string).


```go
func eqOptString((a, b *string)) (a, b *string)
```


**Тип ответа:** a


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


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


📍 *Расположение:* `lex/lexlint/breaking.go:364`




## lex/lexlint/lint.go


📄 Исходный файл: `lex/lexlint/lint.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [LintSchemaFile](#lintschemafile-lexlexlintlintgo22) `:22`

- 🔗 [lintSchemaDef](#lintschemadef-lexlexlintlintgo59) `:59`

- 🔗 [lintSchemaRecursive](#lintschemarecursive-lexlexlintlintgo242) `:242`


</details>


[function] name: LintSchemaFile file: lex/lexlint/lint.go:22 returns_error: нет description: —


### LintSchemaFile (lex/lexlint/lint.go:22)


LintSchemaFile is a function that performs operations based on the provided parameters and returns (sf *lexicon.SchemaFile).


```go
func LintSchemaFile((sf *lexicon.SchemaFile)) (sf *lexicon.SchemaFile)
```


**Тип запроса:** lexicon.SchemaFile


```json
{
  "Type": "string",
  "Lexicon": 0,
  "ID": "string",
  "Description": "string",
  "Defs": {}
}
```


*Определено в:* `atproto/lexicon/schemafile.go`


**Тип ответа:** sf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaFile


```json
{
  "Type": "string",
  "Lexicon": 0,
  "ID": "string",
  "Description": "string",
  "Defs": {}
}
```


*Определено в:* `atproto/lexicon/schemafile.go`


📍 *Расположение:* `lex/lexlint/lint.go:22`



---


[function] name: lintSchemaDef file: lex/lexlint/lint.go:59 returns_error: нет description: —


### lintSchemaDef (lex/lexlint/lint.go:59)


lintSchemaDef is a function that performs operations based on the provided parameters and returns (nsid syntax.NSID, defname string, def lexicon.SchemaDef).


```go
func lintSchemaDef((nsid syntax.NSID, defname string, def lexicon.SchemaDef)) (nsid syntax.NSID, defname string, def lexicon.SchemaDef)
```


**Тип ответа:** nsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** defname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** def


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


📍 *Расположение:* `lex/lexlint/lint.go:59`



---


[function] name: lintSchemaRecursive file: lex/lexlint/lint.go:242 returns_error: нет description: —


### lintSchemaRecursive (lex/lexlint/lint.go:242)


lintSchemaRecursive is a function that performs operations based on the provided parameters and returns (nsid syntax.NSID, def lexicon.SchemaDef).


```go
func lintSchemaRecursive((nsid syntax.NSID, def lexicon.SchemaDef)) (nsid syntax.NSID, def lexicon.SchemaDef)
```


**Тип ответа:** nsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** def


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


📍 *Расположение:* `lex/lexlint/lint.go:242`




## lex/lexlint/syntax.go


📄 Исходный файл: `lex/lexlint/syntax.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CheckSchemaName](#checkschemaname-lexlexlintsyntaxgo10) `:10`


</details>


[function] name: CheckSchemaName file: lex/lexlint/syntax.go:10 returns_error: нет description: —


### CheckSchemaName (lex/lexlint/syntax.go:10)


CheckSchemaName is a function that performs operations based on the provided parameters and returns (raw string).


```go
func CheckSchemaName((raw string)) (raw string)
```


**Тип ответа:** raw


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


📍 *Расположение:* `lex/lexlint/syntax.go:10`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](lex_lexgen.md)

- [Следующая директория](lex_util.md)


---

