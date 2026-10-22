---
title: "Функции: atproto/lexicon"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/lexicon
---


# Функции: atproto/lexicon


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_labeling.md)

- [Следующая директория](atproto_repo.md)


---


## Меню по файлам


- 📄 [atproto/lexicon/catalog.go](#atprotolexiconcataloggo)

- 📄 [atproto/lexicon/cmd/lextool/main.go](#atprotolexiconcmdlextoolmaingo)

- 📄 [atproto/lexicon/cmd/lextool/net.go](#atprotolexiconcmdlextoolnetgo)

- 📄 [atproto/lexicon/extract_type.go](#atprotolexiconextract_typego)

- 📄 [atproto/lexicon/language.go](#atprotolexiconlanguagego)

- 📄 [atproto/lexicon/mimetype.go](#atprotolexiconmimetypego)

- 📄 [atproto/lexicon/resolve.go](#atprotolexiconresolvego)

- 📄 [atproto/lexicon/resolving_catalog.go](#atprotolexiconresolving_cataloggo)

- 📄 [atproto/lexicon/schemafile.go](#atprotolexiconschemafilego)

- 📄 [atproto/lexicon/validation.go](#atprotolexiconvalidationgo)


---


## atproto/lexicon/catalog.go


📄 Исходный файл: `atproto/lexicon/catalog.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [AddSchemaFile](#addschemafile-atprotolexiconcataloggo52) `:52`

- 🔗 [LoadDirectory](#loaddirectory-atprotolexiconcataloggo90) `:90`

- 🔗 [LoadEmbedFS](#loadembedfs-atprotolexiconcataloggo118) `:118`

- 🔗 [NewBaseCatalog](#newbasecatalog-atprotolexiconcataloggo27) `:27`

- 🔗 [Resolve](#resolve-atprotolexiconcataloggo36) `:36`

- 🔗 [addSchemaFromBytes](#addschemafrombytes-atprotolexiconcataloggo78) `:78`


</details>


[function] name: AddSchemaFile file: atproto/lexicon/catalog.go:52 returns_error: нет description: Inserts a schema loaded from a JSON file in to the catalog.


### AddSchemaFile (atproto/lexicon/catalog.go:52)


Inserts a schema loaded from a JSON file in to the catalog.


```go
func (c *BaseCatalog) AddSchemaFile((sf SchemaFile)) (sf SchemaFile)
```


**Тип ответа:** sf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SchemaFile


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


📍 *Расположение:* `atproto/lexicon/catalog.go:52`



---


[function] name: LoadDirectory file: atproto/lexicon/catalog.go:90 returns_error: нет description: Recursively loads all '.json' files from a directory in to the catalog.


### LoadDirectory (atproto/lexicon/catalog.go:90)


Recursively loads all '.json' files from a directory in to the catalog.


```go
func (c *BaseCatalog) LoadDirectory((dirPath string)) (dirPath string)
```


**Тип ответа:** dirPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/catalog.go:90`



---


[function] name: LoadEmbedFS file: atproto/lexicon/catalog.go:118 returns_error: нет description: Recursively loads all '.json' files from an embed.FS


### LoadEmbedFS (atproto/lexicon/catalog.go:118)


Recursively loads all '.json' files from an embed.FS


```go
func (c *BaseCatalog) LoadEmbedFS((efs embed.FS)) (efs embed.FS)
```


**Тип ответа:** efs


```json
{
  "contentMarkdown": "string",
  "createdAt": "string",
  "disabled": false,
  "id": "string",
  "lang": "string",
  "lastUpdatedBy": "string",
  "name": "string",
  "subject": "string",
  "updatedAt": "string"
}
```


*Определено в:* `api/ozone/communicationdefs.go`


**Тип ответа:** embed.FS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/catalog.go:118`



---


[function] name: NewBaseCatalog file: atproto/lexicon/catalog.go:27 returns_error: нет description: Creates a new empty BaseCatalog


### NewBaseCatalog (atproto/lexicon/catalog.go:27)


Creates a new empty BaseCatalog


```go
func NewBaseCatalog(()) ()
```


📍 *Расположение:* `atproto/lexicon/catalog.go:27`



---


[function] name: Resolve file: atproto/lexicon/catalog.go:36 returns_error: да description: Returns a scheman definition (`Schema` struct) for a Lexicon reference.

A Lexicon ref string is an NSID with an optiona


### Resolve (atproto/lexicon/catalog.go:36)


Returns a scheman definition (`Schema` struct) for a Lexicon reference.

A Lexicon ref string is an NSID with an optional #-separated fragment. If the fragment isn't specified, '#main' is used by default.


```go
func (c *BaseCatalog) Resolve((*Schema, error)) (*Schema, error)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Schema`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/lexicon/catalog.go:36`



---


[function] name: addSchemaFromBytes file: atproto/lexicon/catalog.go:78 returns_error: нет description: internal helper for loading JSON files from bytes


### addSchemaFromBytes (atproto/lexicon/catalog.go:78)


internal helper for loading JSON files from bytes


```go
func (c *BaseCatalog) addSchemaFromBytes((b []byte)) (b []byte)
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


📍 *Расположение:* `atproto/lexicon/catalog.go:78`




## atproto/lexicon/cmd/lextool/main.go


📄 Исходный файл: `atproto/lexicon/cmd/lextool/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [main](#main-atprotolexiconcmdlextoolmaingo16) `:16`

- 🔗 [runLoadDirectory](#runloaddirectory-atprotolexiconcmdlextoolmaingo80) `:80`

- 🔗 [runParseSchema](#runparseschema-atprotolexiconcmdlextoolmaingo51) `:51`

- 🔗 [runResolve](#runresolve-atprotolexiconcmdlextoolmaingo96) `:96`


</details>


[function] name: main file: atproto/lexicon/cmd/lextool/main.go:16 returns_error: нет description: —


### main (atproto/lexicon/cmd/lextool/main.go:16)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `atproto/lexicon/cmd/lextool/main.go:16`



---


[function] name: runLoadDirectory file: atproto/lexicon/cmd/lextool/main.go:80 returns_error: нет description: —


### runLoadDirectory (atproto/lexicon/cmd/lextool/main.go:80)


runLoadDirectory is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runLoadDirectory((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/lexicon/cmd/lextool/main.go:80`



---


[function] name: runParseSchema file: atproto/lexicon/cmd/lextool/main.go:51 returns_error: нет description: —


### runParseSchema (atproto/lexicon/cmd/lextool/main.go:51)


runParseSchema is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runParseSchema((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/lexicon/cmd/lextool/main.go:51`



---


[function] name: runResolve file: atproto/lexicon/cmd/lextool/main.go:96 returns_error: нет description: —


### runResolve (atproto/lexicon/cmd/lextool/main.go:96)


runResolve is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runResolve((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/lexicon/cmd/lextool/main.go:96`




## atproto/lexicon/cmd/lextool/net.go


📄 Исходный файл: `atproto/lexicon/cmd/lextool/net.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [runValidateRecord](#runvalidaterecord-atprotolexiconcmdlextoolnetgo18) `:18`


</details>


[function] name: runValidateRecord file: atproto/lexicon/cmd/lextool/net.go:18 returns_error: нет description: —


### runValidateRecord (atproto/lexicon/cmd/lextool/net.go:18)


runValidateRecord is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runValidateRecord((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/lexicon/cmd/lextool/net.go:18`




## atproto/lexicon/extract_type.go


📄 Исходный файл: `atproto/lexicon/extract_type.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ExtractTypeJSON](#extracttypejson-atprotolexiconextract_typego13) `:13`


</details>


[function] name: ExtractTypeJSON file: atproto/lexicon/extract_type.go:13 returns_error: да description: Parses the top-level $type field from generic atproto JSON data


### ExtractTypeJSON (atproto/lexicon/extract_type.go:13)


Parses the top-level $type field from generic atproto JSON data


```go
func ExtractTypeJSON((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/lexicon/extract_type.go:13`




## atproto/lexicon/language.go


📄 Исходный файл: `atproto/lexicon/language.go`


<details open>
<summary><b>Функции в этом файле (40)</b></summary>


- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego21) `:21`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego342) `:342`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego367) `:367`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego398) `:398`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego432) `:432`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego457) `:457`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego493) `:493`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego553) `:553`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego574) `:574`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego583) `:583`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego608) `:608`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego639) `:639`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego694) `:694`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego819) `:819`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego849) `:849`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego872) `:872`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego897) `:897`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego945) `:945`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego989) `:989`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego1031) `:1031`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego1053) `:1053`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego1076) `:1076`

- 🔗 [CheckSchema](#checkschema-atprotolexiconlanguagego1101) `:1101`

- 🔗 [IsConcrete](#isconcrete-atprotolexiconlanguagego75) `:75`

- 🔗 [IsDefinable](#isdefinable-atprotolexiconlanguagego84) `:84`

- 🔗 [IsFieldType](#isfieldtype-atprotolexiconlanguagego93) `:93`

- 🔗 [IsNullable](#isnullable-atprotolexiconlanguagego929) `:929`

- 🔗 [IsPrimary](#isprimary-atprotolexiconlanguagego67) `:67`

- 🔗 [MarshalJSON](#marshaljson-atprotolexiconlanguagego186) `:186`

- 🔗 [UnmarshalJSON](#unmarshaljson-atprotolexiconlanguagego190) `:190`

- 🔗 [Validate](#validate-atprotolexiconlanguagego586) `:586`

- 🔗 [Validate](#validate-atprotolexiconlanguagego618) `:618`

- 🔗 [Validate](#validate-atprotolexiconlanguagego653) `:653`

- 🔗 [Validate](#validate-atprotolexiconlanguagego725) `:725`

- 🔗 [Validate](#validate-atprotolexiconlanguagego833) `:833`

- 🔗 [Validate](#validate-atprotolexiconlanguagego856) `:856`

- 🔗 [Validate](#validate-atprotolexiconlanguagego956) `:956`

- 🔗 [Validate](#validate-atprotolexiconlanguagego1041) `:1041`

- 🔗 [Validate](#validate-atprotolexiconlanguagego1108) `:1108`

- 🔗 [setBase](#setbase-atprotolexiconlanguagego105) `:105`


</details>


[function] name: CheckSchema file: atproto/lexicon/language.go:21 returns_error: нет description: Checks that the schema definition itself is valid (recursively).


### CheckSchema (atproto/lexicon/language.go:21)


Checks that the schema definition itself is valid (recursively).


```go
func (s *SchemaDef) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:21`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:342 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:342)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaRecord) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:342`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:367 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:367)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaQuery) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:367`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:398 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:398)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaProcedure) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:398`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:432 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:432)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaSubscription) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:432`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:457 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:457)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaPermissionSet) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:457`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:493 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:493)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaPermission) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:493`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:553 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:553)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaBody) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:553`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:574 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:574)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaMessage) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:574`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:583 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:583)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaError) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:583`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:608 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:608)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaBoolean) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:608`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:639 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:639)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaInteger) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:639`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:694 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:694)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaString) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:694`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:819 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:819)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaBytes) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:819`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:849 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:849)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaCIDLink) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:849`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:872 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:872)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaArray) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:872`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:897 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:897)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaObject) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:897`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:945 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:945)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaBlob) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:945`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:989 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:989)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaParams) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:989`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:1031 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:1031)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaToken) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:1031`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:1053 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:1053)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaRef) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:1053`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:1076 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:1076)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaUnion) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:1076`



---


[function] name: CheckSchema file: atproto/lexicon/language.go:1101 returns_error: нет description: —


### CheckSchema (atproto/lexicon/language.go:1101)


CheckSchema is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaUnknown) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:1101`



---


[function] name: IsConcrete file: atproto/lexicon/language.go:75 returns_error: нет description: —


### IsConcrete (atproto/lexicon/language.go:75)


IsConcrete is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SchemaDef) IsConcrete(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:75`



---


[function] name: IsDefinable file: atproto/lexicon/language.go:84 returns_error: нет description: Checks if type can be a top-level "named" definition


### IsDefinable (atproto/lexicon/language.go:84)


Checks if type can be a top-level "named" definition


```go
func (s *SchemaDef) IsDefinable(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:84`



---


[function] name: IsFieldType file: atproto/lexicon/language.go:93 returns_error: нет description: Checks if the type is allowed to be included in object fields.


### IsFieldType (atproto/lexicon/language.go:93)


Checks if the type is allowed to be included in object fields.


```go
func (s *SchemaDef) IsFieldType(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:93`



---


[function] name: IsNullable file: atproto/lexicon/language.go:929 returns_error: нет description: Checks if a field name 'k' is one of the Nullable fields for this object


### IsNullable (atproto/lexicon/language.go:929)


Checks if a field name 'k' is one of the Nullable fields for this object


```go
func (s *SchemaObject) IsNullable((k string)) (k string)
```


**Тип ответа:** k


```json
{
  "logger": null,
  "webhookURL": "string",
  "adminPassword": "string",
  "httpClient": null
}
```


*Определено в:* `cmd/tap/webhook_client.go`


📍 *Расположение:* `atproto/lexicon/language.go:929`



---


[function] name: IsPrimary file: atproto/lexicon/language.go:67 returns_error: нет description: Checks if def is of "parimary" type


### IsPrimary (atproto/lexicon/language.go:67)


Checks if def is of "parimary" type


```go
func (s *SchemaDef) IsPrimary(()) ()
```


📍 *Расположение:* `atproto/lexicon/language.go:67`



---


[function] name: MarshalJSON file: atproto/lexicon/language.go:186 returns_error: да description: —


### MarshalJSON (atproto/lexicon/language.go:186)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (s SchemaDef) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/lexicon/language.go:186`



---


[function] name: UnmarshalJSON file: atproto/lexicon/language.go:190 returns_error: нет description: —


### UnmarshalJSON (atproto/lexicon/language.go:190)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (s *SchemaDef) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `atproto/lexicon/language.go:190`



---


[function] name: Validate file: atproto/lexicon/language.go:586 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:586)


Validate is a method that performs operations based on the provided parameters and returns (d any).


```go
func (s *SchemaError) Validate((d any)) (d any)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:586`



---


[function] name: Validate file: atproto/lexicon/language.go:618 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:618)


Validate is a method that performs operations based on the provided parameters and returns (d any).


```go
func (s *SchemaBoolean) Validate((d any)) (d any)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:618`



---


[function] name: Validate file: atproto/lexicon/language.go:653 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:653)


Validate is a method that performs operations based on the provided parameters and returns (d any).


```go
func (s *SchemaInteger) Validate((d any)) (d any)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:653`



---


[function] name: Validate file: atproto/lexicon/language.go:725 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:725)


Validate is a method that performs operations based on the provided parameters and returns (d any, flags ValidateFlags).


```go
func (s *SchemaString) Validate((d any, flags ValidateFlags)) (d any, flags ValidateFlags)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:725`



---


[function] name: Validate file: atproto/lexicon/language.go:833 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:833)


Validate is a method that performs operations based on the provided parameters and returns (d any).


```go
func (s *SchemaBytes) Validate((d any)) (d any)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:833`



---


[function] name: Validate file: atproto/lexicon/language.go:856 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:856)


Validate is a method that performs operations based on the provided parameters and returns (d any).


```go
func (s *SchemaCIDLink) Validate((d any)) (d any)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:856`



---


[function] name: Validate file: atproto/lexicon/language.go:956 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:956)


Validate is a method that performs operations based on the provided parameters and returns (d any, flags ValidateFlags).


```go
func (s *SchemaBlob) Validate((d any, flags ValidateFlags)) (d any, flags ValidateFlags)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:956`



---


[function] name: Validate file: atproto/lexicon/language.go:1041 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:1041)


Validate is a method that performs operations based on the provided parameters and returns (d any).


```go
func (s *SchemaToken) Validate((d any)) (d any)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:1041`



---


[function] name: Validate file: atproto/lexicon/language.go:1108 returns_error: нет description: —


### Validate (atproto/lexicon/language.go:1108)


Validate is a method that performs operations based on the provided parameters and returns (d any).


```go
func (s *SchemaUnknown) Validate((d any)) (d any)
```


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:1108`



---


[function] name: setBase file: atproto/lexicon/language.go:105 returns_error: нет description: Helper to recurse down the definition tree and set full references on any sub-schemas which need to embed that metadata


### setBase (atproto/lexicon/language.go:105)


Helper to recurse down the definition tree and set full references on any sub-schemas which need to embed that metadata


```go
func (s *SchemaDef) setBase((base string)) (base string)
```


**Тип ответа:** base


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/language.go:105`




## atproto/lexicon/mimetype.go


📄 Исходный файл: `atproto/lexicon/mimetype.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [acceptableMimeType](#acceptablemimetype-atprotolexiconmimetypego8) `:8`


</details>


[function] name: acceptableMimeType file: atproto/lexicon/mimetype.go:8 returns_error: нет description: checks if val matches pattern, with optional trailing glob on pattern. case-sensitive.


### acceptableMimeType (atproto/lexicon/mimetype.go:8)


checks if val matches pattern, with optional trailing glob on pattern. case-sensitive.


```go
func acceptableMimeType((pattern, val string)) (pattern, val string)
```


**Тип ответа:** pattern


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** val


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


📍 *Расположение:* `atproto/lexicon/mimetype.go:8`




## atproto/lexicon/resolve.go


📄 Исходный файл: `atproto/lexicon/resolve.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [ResolveLexiconData](#resolvelexicondata-atprotolexiconresolvego21) `:21`

- 🔗 [ResolveLexiconSchemaFile](#resolvelexiconschemafile-atprotolexiconresolvego38) `:38`

- 🔗 [fetchRecordJSON](#fetchrecordjson-atprotolexiconresolvego73) `:73`

- 🔗 [resolveLexiconJSON](#resolvelexiconjson-atprotolexiconresolvego52) `:52`


</details>


[function] name: ResolveLexiconData file: atproto/lexicon/resolve.go:21 returns_error: да description: Low-level routine for resolving an NSID to full Lexicon data record (as stored in a repository).

The current implementa


### ResolveLexiconData (atproto/lexicon/resolve.go:21)


Low-level routine for resolving an NSID to full Lexicon data record (as stored in a repository).

The current implementation uses a naive 'getRepo' fetch to the relevant PDS instance, without validating MST proof chain.

Calling code should usually use ResolvingCatalog, which handles basic caching and validation of the Lexicon language itself.


```go
func ResolveLexiconData((map[string]any, error)) (map[string]any, error)
```


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]any`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/lexicon/resolve.go:21`



---


[function] name: ResolveLexiconSchemaFile file: atproto/lexicon/resolve.go:38 returns_error: да description: Low-level routine for resolving an NSID to `SchemaFile`.

Same as `ResolveLexiconData`, but returns a parsed `SchemaFile


### ResolveLexiconSchemaFile (atproto/lexicon/resolve.go:38)


Low-level routine for resolving an NSID to `SchemaFile`.

Same as `ResolveLexiconData`, but returns a parsed `SchemaFile` struct.


```go
func ResolveLexiconSchemaFile((*SchemaFile, error)) (*SchemaFile, error)
```


**Тип запроса:** SchemaFile


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


**Тип ответа:** SchemaFile


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SchemaFile`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/lexicon/resolve.go:38`



---


[function] name: fetchRecordJSON file: atproto/lexicon/resolve.go:73 returns_error: да description: —


### fetchRecordJSON (atproto/lexicon/resolve.go:73)


fetchRecordJSON is a function that performs operations based on the provided parameters and may return an error.


```go
func fetchRecordJSON((*json.RawMessage, error)) (*json.RawMessage, error)
```


**Тип запроса:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*json.RawMessage`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/lexicon/resolve.go:73`



---


[function] name: resolveLexiconJSON file: atproto/lexicon/resolve.go:52 returns_error: да description: internal helper for fetching lexicon record as JSON bytes


### resolveLexiconJSON (atproto/lexicon/resolve.go:52)


internal helper for fetching lexicon record as JSON bytes


```go
func resolveLexiconJSON((*json.RawMessage, error)) (*json.RawMessage, error)
```


**Тип запроса:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** json.RawMessage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*json.RawMessage`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/lexicon/resolve.go:52`




## atproto/lexicon/resolving_catalog.go


📄 Исходный файл: `atproto/lexicon/resolving_catalog.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [NewResolvingCatalog](#newresolvingcatalog-atprotolexiconresolving_cataloggo19) `:19`

- 🔗 [Resolve](#resolve-atprotolexiconresolving_cataloggo26) `:26`


</details>


[function] name: NewResolvingCatalog file: atproto/lexicon/resolving_catalog.go:19 returns_error: нет description: —


### NewResolvingCatalog (atproto/lexicon/resolving_catalog.go:19)


NewResolvingCatalog is a function that performs operations based on the provided parameters and returns ().


```go
func NewResolvingCatalog(()) ()
```


📍 *Расположение:* `atproto/lexicon/resolving_catalog.go:19`



---


[function] name: Resolve file: atproto/lexicon/resolving_catalog.go:26 returns_error: да description: —


### Resolve (atproto/lexicon/resolving_catalog.go:26)


Resolve is a method that performs operations based on the provided parameters and may return an error.


```go
func (rc *ResolvingCatalog) Resolve((*Schema, error)) (*Schema, error)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Schema`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/lexicon/resolving_catalog.go:26`




## atproto/lexicon/schemafile.go


📄 Исходный файл: `atproto/lexicon/schemafile.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [CheckSchema](#checkschema-atprotolexiconschemafilego49) `:49`

- 🔗 [FinishParse](#finishparse-atprotolexiconschemafilego25) `:25`


</details>


[function] name: CheckSchema file: atproto/lexicon/schemafile.go:49 returns_error: нет description: Calls [SchemaDef.CheckSchema] recursively over all defs


### CheckSchema (atproto/lexicon/schemafile.go:49)


Calls [SchemaDef.CheckSchema] recursively over all defs


```go
func (sf *SchemaFile) CheckSchema(()) ()
```


📍 *Расположение:* `atproto/lexicon/schemafile.go:49`



---


[function] name: FinishParse file: atproto/lexicon/schemafile.go:25 returns_error: нет description: Helper method which should always be called after parsing a schema file (eg, from JSON).

Does some very basic validatio


### FinishParse (atproto/lexicon/schemafile.go:25)


Helper method which should always be called after parsing a schema file (eg, from JSON).

Does some very basic validation (eg, lexicon language version), and fills in
internal references (for example full name of tokens).


```go
func (sf *SchemaFile) FinishParse(()) ()
```


📍 *Расположение:* `atproto/lexicon/schemafile.go:25`




## atproto/lexicon/validation.go


📄 Исходный файл: `atproto/lexicon/validation.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [ValidateRecord](#validaterecord-atprotolexiconvalidationgo34) `:34`

- 🔗 [validateArray](#validatearray-atprotolexiconvalidationgo122) `:122`

- 🔗 [validateData](#validatedata-atprotolexiconvalidationgo58) `:58`

- 🔗 [validateObject](#validateobject-atprotolexiconvalidationgo102) `:102`

- 🔗 [validateRecordConfig](#validaterecordconfig-atprotolexiconvalidationgo38) `:38`

- 🔗 [validateUnion](#validateunion-atprotolexiconvalidationgo135) `:135`


</details>


[function] name: ValidateRecord file: atproto/lexicon/validation.go:34 returns_error: нет description: Checks Lexicon schema (fetched from the catalog) for the given record, with optional flags tweaking default validation r


### ValidateRecord (atproto/lexicon/validation.go:34)


Checks Lexicon schema (fetched from the catalog) for the given record, with optional flags tweaking default validation rules.

'recordData' is typed as 'any', but is expected to be 'map[string]any'
'ref' is a reference to the schema type, as an NSID with optional fragment. For records, the '$type' must match 'ref'
'flags' are parameters tweaking Lexicon validation rules. Zero value is default.


```go
func ValidateRecord((cat Catalog, recordData any, ref string, flags ValidateFlags)) (cat Catalog, recordData any, ref string, flags ValidateFlags)
```


**Тип ответа:** cat


```json
{
  "Type": "string",
  "PublicKeyMultibase": "string"
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** Catalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** recordData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ref


```json
{
  "accessJwt": "string",
  "active": false,
  "did": "string",
  "refreshJwt": "string",
  "status": "string"
}
```


*Определено в:* `atproto/atclient/password_auth.go`


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/validation.go:34`



---


[function] name: validateArray file: atproto/lexicon/validation.go:122 returns_error: нет description: —


### validateArray (atproto/lexicon/validation.go:122)


validateArray is a function that performs operations based on the provided parameters and returns (cat Catalog, s SchemaArray, arr []any, flags ValidateFlags).


```go
func validateArray((cat Catalog, s SchemaArray, arr []any, flags ValidateFlags)) (cat Catalog, s SchemaArray, arr []any, flags ValidateFlags)
```


**Тип ответа:** cat


```json
{
  "Type": "string",
  "PublicKeyMultibase": "string"
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** Catalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** s


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


**Тип ответа:** SchemaArray


```json
{
  "Type": "string",
  "Description": "string",
  "Items": {},
  "MinLength": 0,
  "MaxLength": 0
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** arr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/validation.go:122`



---


[function] name: validateData file: atproto/lexicon/validation.go:58 returns_error: нет description: —


### validateData (atproto/lexicon/validation.go:58)


validateData is a function that performs operations based on the provided parameters and returns (cat Catalog, def any, d any, flags ValidateFlags).


```go
func validateData((cat Catalog, def any, d any, flags ValidateFlags)) (cat Catalog, def any, d any, flags ValidateFlags)
```


**Тип ответа:** cat


```json
{
  "Type": "string",
  "PublicKeyMultibase": "string"
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** Catalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** def


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/validation.go:58`



---


[function] name: validateObject file: atproto/lexicon/validation.go:102 returns_error: нет description: —


### validateObject (atproto/lexicon/validation.go:102)


validateObject is a function that performs operations based on the provided parameters and returns (cat Catalog, s SchemaObject, d map[string]any, flags ValidateFlags).


```go
func validateObject((cat Catalog, s SchemaObject, d map[string]any, flags ValidateFlags)) (cat Catalog, s SchemaObject, d map[string]any, flags ValidateFlags)
```


**Тип ответа:** cat


```json
{
  "Type": "string",
  "PublicKeyMultibase": "string"
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** Catalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** s


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


**Тип ответа:** SchemaObject


```json
{
  "Type": "string",
  "Description": "string",
  "Properties": {},
  "Required": [],
  "Nullable": []
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/validation.go:102`



---


[function] name: validateRecordConfig file: atproto/lexicon/validation.go:38 returns_error: нет description: —


### validateRecordConfig (atproto/lexicon/validation.go:38)


validateRecordConfig is a function that performs operations based on the provided parameters and returns (cat Catalog, recordData any, ref string, flags ValidateFlags).


```go
func validateRecordConfig((cat Catalog, recordData any, ref string, flags ValidateFlags)) (cat Catalog, recordData any, ref string, flags ValidateFlags)
```


**Тип ответа:** cat


```json
{
  "Type": "string",
  "PublicKeyMultibase": "string"
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** Catalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** recordData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ref


```json
{
  "accessJwt": "string",
  "active": false,
  "did": "string",
  "refreshJwt": "string",
  "status": "string"
}
```


*Определено в:* `atproto/atclient/password_auth.go`


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/validation.go:38`



---


[function] name: validateUnion file: atproto/lexicon/validation.go:135 returns_error: нет description: —


### validateUnion (atproto/lexicon/validation.go:135)


validateUnion is a function that performs operations based on the provided parameters and returns (cat Catalog, s SchemaUnion, d any, flags ValidateFlags).


```go
func validateUnion((cat Catalog, s SchemaUnion, d any, flags ValidateFlags)) (cat Catalog, s SchemaUnion, d any, flags ValidateFlags)
```


**Тип ответа:** cat


```json
{
  "Type": "string",
  "PublicKeyMultibase": "string"
}
```


*Определено в:* `atproto/identity/identity.go`


**Тип ответа:** Catalog


```json
{
  "Celebs": [],
  "Regulars": []
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** s


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


**Тип ответа:** SchemaUnion


```json
{
  "Type": "string",
  "Description": "string",
  "Refs": [],
  "Closed": false,
  "fullRefs": []
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ValidateFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/lexicon/validation.go:135`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_labeling.md)

- [Следующая директория](atproto_repo.md)


---

