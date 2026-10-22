---
title: "Функции: lex/lexgen"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: lex/lexgen
---


# Функции: lex/lexgen


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](lex.md)

- [Следующая директория](lex_lexlint.md)


---


## Меню по файлам


- 📄 [lex/lexgen/codegen.go](#lexlexgencodegengo)

- 📄 [lex/lexgen/flatten.go](#lexlexgenflattengo)

- 📄 [lex/lexgen/util.go](#lexlexgenutilgo)


---


## lex/lexgen/codegen.go


📄 Исходный файл: `lex/lexgen/codegen.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [FileName](#filename-lexlexgencodegengo93) `:93`

- 🔗 [LegacyConfig](#legacyconfig-lexlexgencodegengo31) `:31`

- 🔗 [NewGenConfig](#newgenconfig-lexlexgencodegengo24) `:24`

- 🔗 [PkgName](#pkgname-lexlexgencodegengo71) `:71`

- 🔗 [WriteLexicon](#writelexicon-lexlexgencodegengo49) `:49`

- 🔗 [WriteType](#writetype-lexlexgencodegengo126) `:126`

- 🔗 [baseName](#basename-lexlexgencodegengo88) `:88`

- 🔗 [deps](#deps-lexlexgencodegengo97) `:97`

- 🔗 [externalRefType](#externalreftype-lexlexgencodegengo304) `:304`

- 🔗 [fieldType](#fieldtype-lexlexgencodegengo183) `:183`

- 🔗 [isRequired](#isrequired-lexlexgencodegengo174) `:174`

- 🔗 [writeEndpoint](#writeendpoint-lexlexgencodegengo626) `:626`

- 🔗 [writeStruct](#writestruct-lexlexgencodegengo341) `:341`

- 🔗 [writeUnion](#writeunion-lexlexgencodegengo480) `:480`


</details>


[function] name: FileName file: lex/lexgen/codegen.go:93 returns_error: нет description: —


### FileName (lex/lexgen/codegen.go:93)


FileName is a method that performs operations based on the provided parameters and returns ().


```go
func (gen *CodeGenerator) FileName(()) ()
```


📍 *Расположение:* `lex/lexgen/codegen.go:93`



---


[function] name: LegacyConfig file: lex/lexgen/codegen.go:31 returns_error: нет description: —


### LegacyConfig (lex/lexgen/codegen.go:31)


LegacyConfig is a function that performs operations based on the provided parameters and returns ().


```go
func LegacyConfig(()) ()
```


📍 *Расположение:* `lex/lexgen/codegen.go:31`



---


[function] name: NewGenConfig file: lex/lexgen/codegen.go:24 returns_error: нет description: —


### NewGenConfig (lex/lexgen/codegen.go:24)


NewGenConfig is a function that performs operations based on the provided parameters and returns ().


```go
func NewGenConfig(()) ()
```


📍 *Расположение:* `lex/lexgen/codegen.go:24`



---


[function] name: PkgName file: lex/lexgen/codegen.go:71 returns_error: нет description: —


### PkgName (lex/lexgen/codegen.go:71)


PkgName is a method that performs operations based on the provided parameters and returns ().


```go
func (gen *CodeGenerator) PkgName(()) ()
```


📍 *Расположение:* `lex/lexgen/codegen.go:71`



---


[function] name: WriteLexicon file: lex/lexgen/codegen.go:49 returns_error: нет description: Outputs Go source code to the "Out" [io.Writer].


### WriteLexicon (lex/lexgen/codegen.go:49)


Outputs Go source code to the "Out" [io.Writer].


```go
func (gen *CodeGenerator) WriteLexicon(()) ()
```


📍 *Расположение:* `lex/lexgen/codegen.go:49`



---


[function] name: WriteType file: lex/lexgen/codegen.go:126 returns_error: нет description: —


### WriteType (lex/lexgen/codegen.go:126)


WriteType is a method that performs operations based on the provided parameters and returns (ft *FlatType).


```go
func (gen *CodeGenerator) WriteType((ft *FlatType)) (ft *FlatType)
```


**Тип запроса:** FlatType


```json
{
  "DefName": "string",
  "Path": [],
  "Type": "string",
  "Schema": null
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип ответа:** ft


```json
{
  "langs": [],
  "postgateEmbeddingRules": [],
  "posts": [],
  "threadgateAllow": []
}
```


*Определено в:* `api/bsky/draftdefs.go`


**Тип ответа:** FlatType


```json
{
  "DefName": "string",
  "Path": [],
  "Type": "string",
  "Schema": null
}
```


*Определено в:* `lex/lexgen/flatten.go`


📍 *Расположение:* `lex/lexgen/codegen.go:126`



---


[function] name: baseName file: lex/lexgen/codegen.go:88 returns_error: нет description: —


### baseName (lex/lexgen/codegen.go:88)


baseName is a method that performs operations based on the provided parameters and returns ().


```go
func (gen *CodeGenerator) baseName(()) ()
```


📍 *Расположение:* `lex/lexgen/codegen.go:88`



---


[function] name: deps file: lex/lexgen/codegen.go:97 returns_error: нет description: —


### deps (lex/lexgen/codegen.go:97)


deps is a method that performs operations based on the provided parameters and returns ().


```go
func (gen *CodeGenerator) deps(()) ()
```


📍 *Расположение:* `lex/lexgen/codegen.go:97`



---


[function] name: externalRefType file: lex/lexgen/codegen.go:304 returns_error: да description: —


### externalRefType (lex/lexgen/codegen.go:304)


externalRefType is a method that performs operations based on the provided parameters and may return an error.


```go
func (gen *CodeGenerator) externalRefType((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/lexgen/codegen.go:304`



---


[function] name: fieldType file: lex/lexgen/codegen.go:183 returns_error: да description: —


### fieldType (lex/lexgen/codegen.go:183)


fieldType is a method that performs operations based on the provided parameters and may return an error.


```go
func (gen *CodeGenerator) fieldType((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/lexgen/codegen.go:183`



---


[function] name: isRequired file: lex/lexgen/codegen.go:174 returns_error: нет description: —


### isRequired (lex/lexgen/codegen.go:174)


isRequired is a function that performs operations based on the provided parameters and returns (required []string, fname string).


```go
func isRequired((required []string, fname string)) (required []string, fname string)
```


**Тип ответа:** required


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/lexgen/codegen.go:174`



---


[function] name: writeEndpoint file: lex/lexgen/codegen.go:626 returns_error: нет description: —


### writeEndpoint (lex/lexgen/codegen.go:626)


writeEndpoint is a method that performs operations based on the provided parameters and returns (ft *FlatType, desc string, params *lexicon.SchemaParams, output, input *lexicon.SchemaBody, isProcedure bool).


```go
func (gen *CodeGenerator) writeEndpoint((ft *FlatType, desc string, params *lexicon.SchemaParams, output, input *lexicon.SchemaBody, isProcedure bool)) (ft *FlatType, desc string, params *lexicon.SchemaParams, output, input *lexicon.SchemaBody, isProcedure bool)
```


**Тип запроса:** FlatType


```json
{
  "DefName": "string",
  "Path": [],
  "Type": "string",
  "Schema": null
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип запроса:** lexicon.SchemaParams


```json
{
  "Type": "string",
  "Description": "string",
  "Properties": {},
  "Required": []
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип запроса:** lexicon.SchemaBody


```json
{
  "Description": "string",
  "Encoding": "string",
  "Schema": null
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** ft


```json
{
  "langs": [],
  "postgateEmbeddingRules": [],
  "posts": [],
  "threadgateAllow": []
}
```


*Определено в:* `api/bsky/draftdefs.go`


**Тип ответа:** FlatType


```json
{
  "DefName": "string",
  "Path": [],
  "Type": "string",
  "Schema": null
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип ответа:** desc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** params


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaParams


```json
{
  "Type": "string",
  "Description": "string",
  "Properties": {},
  "Required": []
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** output


```json
{
  "Name": "string",
  "Type": null,
  "NeedsCbor": false,
  "NeedsType": false
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaBody


```json
{
  "Description": "string",
  "Encoding": "string",
  "Schema": null
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** isProcedure


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/lexgen/codegen.go:626`



---


[function] name: writeStruct file: lex/lexgen/codegen.go:341 returns_error: нет description: —


### writeStruct (lex/lexgen/codegen.go:341)


writeStruct is a method that performs operations based on the provided parameters and returns (ft *FlatType, obj *lexicon.SchemaObject).


```go
func (gen *CodeGenerator) writeStruct((ft *FlatType, obj *lexicon.SchemaObject)) (ft *FlatType, obj *lexicon.SchemaObject)
```


**Тип запроса:** FlatType


```json
{
  "DefName": "string",
  "Path": [],
  "Type": "string",
  "Schema": null
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип запроса:** lexicon.SchemaObject


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


**Тип ответа:** ft


```json
{
  "langs": [],
  "postgateEmbeddingRules": [],
  "posts": [],
  "threadgateAllow": []
}
```


*Определено в:* `api/bsky/draftdefs.go`


**Тип ответа:** FlatType


```json
{
  "DefName": "string",
  "Path": [],
  "Type": "string",
  "Schema": null
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaObject


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


📍 *Расположение:* `lex/lexgen/codegen.go:341`



---


[function] name: writeUnion file: lex/lexgen/codegen.go:480 returns_error: нет description: —


### writeUnion (lex/lexgen/codegen.go:480)


writeUnion is a method that performs operations based on the provided parameters and returns (ft *FlatType, union *lexicon.SchemaUnion).


```go
func (gen *CodeGenerator) writeUnion((ft *FlatType, union *lexicon.SchemaUnion)) (ft *FlatType, union *lexicon.SchemaUnion)
```


**Тип запроса:** FlatType


```json
{
  "DefName": "string",
  "Path": [],
  "Type": "string",
  "Schema": null
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип запроса:** lexicon.SchemaUnion


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


**Тип ответа:** ft


```json
{
  "langs": [],
  "postgateEmbeddingRules": [],
  "posts": [],
  "threadgateAllow": []
}
```


*Определено в:* `api/bsky/draftdefs.go`


**Тип ответа:** FlatType


```json
{
  "DefName": "string",
  "Path": [],
  "Type": "string",
  "Schema": null
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип ответа:** union


```json
{
  "FieldName": "string",
  "TypeName": "string",
  "LexName": "string"
}
```


*Определено в:* `lex/lexgen/codegen.go`


**Тип ответа:** lexicon.SchemaUnion


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


📍 *Расположение:* `lex/lexgen/codegen.go:480`




## lex/lexgen/flatten.go


📄 Исходный файл: `lex/lexgen/flatten.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [FlattenSchemaFile](#flattenschemafile-lexlexgenflattengo37) `:37`

- 🔗 [MainType](#maintype-lexlexgenflattengo234) `:234`

- 🔗 [flattenDef](#flattendef-lexlexgenflattengo76) `:76`

- 🔗 [flattenObject](#flattenobject-lexlexgenflattengo191) `:191`

- 🔗 [flattenType](#flattentype-lexlexgenflattengo92) `:92`


</details>


[function] name: FlattenSchemaFile file: lex/lexgen/flatten.go:37 returns_error: да description: —


### FlattenSchemaFile (lex/lexgen/flatten.go:37)


FlattenSchemaFile is a function that performs operations based on the provided parameters and may return an error.


```go
func FlattenSchemaFile((*FlatLexicon, error)) (*FlatLexicon, error)
```


**Тип запроса:** FlatLexicon


```json
{
  "NSID": {},
  "Description": "string",
  "ExternalRefs": {},
  "Defs": {},
  "Types": []
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип ответа:** FlatLexicon


```json
{
  "NSID": {},
  "Description": "string",
  "ExternalRefs": {},
  "Defs": {},
  "Types": []
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FlatLexicon`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/lexgen/flatten.go:37`



---


[function] name: MainType file: lex/lexgen/flatten.go:234 returns_error: нет description: Returns the type of any "#main" definition in this file (or else an empty string)


### MainType (lex/lexgen/flatten.go:234)


Returns the type of any "#main" definition in this file (or else an empty string)


```go
func (fl *FlatLexicon) MainType(()) ()
```


📍 *Расположение:* `lex/lexgen/flatten.go:234`



---


[function] name: flattenDef file: lex/lexgen/flatten.go:76 returns_error: нет description: —


### flattenDef (lex/lexgen/flatten.go:76)


flattenDef is a method that performs operations based on the provided parameters and returns (name string, def *lexicon.SchemaDef).


```go
func (fl *FlatLexicon) flattenDef((name string, def *lexicon.SchemaDef)) (name string, def *lexicon.SchemaDef)
```


**Тип запроса:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** name


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


📍 *Расположение:* `lex/lexgen/flatten.go:76`



---


[function] name: flattenObject file: lex/lexgen/flatten.go:191 returns_error: нет description: —


### flattenObject (lex/lexgen/flatten.go:191)


flattenObject is a method that performs operations based on the provided parameters and returns (fd *FlatDef, tpath []string, obj *lexicon.SchemaObject).


```go
func (fl *FlatLexicon) flattenObject((fd *FlatDef, tpath []string, obj *lexicon.SchemaObject)) (fd *FlatDef, tpath []string, obj *lexicon.SchemaObject)
```


**Тип запроса:** FlatDef


```json
{
  "Name": "string",
  "Type": "string"
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип запроса:** lexicon.SchemaObject


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


**Тип ответа:** fd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** FlatDef


```json
{
  "Name": "string",
  "Type": "string"
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип ответа:** tpath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** obj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaObject


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


📍 *Расположение:* `lex/lexgen/flatten.go:191`



---


[function] name: flattenType file: lex/lexgen/flatten.go:92 returns_error: нет description: —


### flattenType (lex/lexgen/flatten.go:92)


flattenType is a method that performs operations based on the provided parameters and returns (fd *FlatDef, tpath []string, def *lexicon.SchemaDef).


```go
func (fl *FlatLexicon) flattenType((fd *FlatDef, tpath []string, def *lexicon.SchemaDef)) (fd *FlatDef, tpath []string, def *lexicon.SchemaDef)
```


**Тип запроса:** FlatDef


```json
{
  "Name": "string",
  "Type": "string"
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип запроса:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** fd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** FlatDef


```json
{
  "Name": "string",
  "Type": "string"
}
```


*Определено в:* `lex/lexgen/flatten.go`


**Тип ответа:** tpath


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


📍 *Расположение:* `lex/lexgen/flatten.go:92`




## lex/lexgen/util.go


📄 Исходный файл: `lex/lexgen/util.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [defDescription](#defdescription-lexlexgenutilgo59) `:59`

- 🔗 [defType](#deftype-lexlexgenutilgo14) `:14`

- 🔗 [isCompoundDef](#iscompounddef-lexlexgenutilgo108) `:108`

- 🔗 [nsidBaseName](#nsidbasename-lexlexgenutilgo129) `:129`

- 🔗 [nsidFileName](#nsidfilename-lexlexgenutilgo145) `:145`

- 🔗 [nsidPkgName](#nsidpkgname-lexlexgenutilgo117) `:117`


</details>


[function] name: defDescription file: lex/lexgen/util.go:59 returns_error: нет description: —


### defDescription (lex/lexgen/util.go:59)


defDescription is a function that performs operations based on the provided parameters and returns (sd *lexicon.SchemaDef).


```go
func defDescription((sd *lexicon.SchemaDef)) (sd *lexicon.SchemaDef)
```


**Тип запроса:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** sd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


📍 *Расположение:* `lex/lexgen/util.go:59`



---


[function] name: defType file: lex/lexgen/util.go:14 returns_error: да description: —


### defType (lex/lexgen/util.go:14)


defType is a function that performs operations based on the provided parameters and may return an error.


```go
func defType((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/lexgen/util.go:14`



---


[function] name: isCompoundDef file: lex/lexgen/util.go:108 returns_error: нет description: —


### isCompoundDef (lex/lexgen/util.go:108)


isCompoundDef is a function that performs operations based on the provided parameters and returns (sd *lexicon.SchemaDef).


```go
func isCompoundDef((sd *lexicon.SchemaDef)) (sd *lexicon.SchemaDef)
```


**Тип запроса:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


**Тип ответа:** sd


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexicon.SchemaDef


```json
{
  "Inner": {}
}
```


*Определено в:* `atproto/lexicon/language.go`


📍 *Расположение:* `lex/lexgen/util.go:108`



---


[function] name: nsidBaseName file: lex/lexgen/util.go:129 returns_error: нет description: —


### nsidBaseName (lex/lexgen/util.go:129)


nsidBaseName is a function that performs operations based on the provided parameters and returns (nsid syntax.NSID).


```go
func nsidBaseName((nsid syntax.NSID)) (nsid syntax.NSID)
```


**Тип ответа:** nsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/lexgen/util.go:129`



---


[function] name: nsidFileName file: lex/lexgen/util.go:145 returns_error: нет description: —


### nsidFileName (lex/lexgen/util.go:145)


nsidFileName is a function that performs operations based on the provided parameters and returns (nsid syntax.NSID).


```go
func nsidFileName((nsid syntax.NSID)) (nsid syntax.NSID)
```


**Тип ответа:** nsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/lexgen/util.go:145`



---


[function] name: nsidPkgName file: lex/lexgen/util.go:117 returns_error: нет description: —


### nsidPkgName (lex/lexgen/util.go:117)


nsidPkgName is a function that performs operations based on the provided parameters and returns (nsid syntax.NSID).


```go
func nsidPkgName((nsid syntax.NSID)) (nsid syntax.NSID)
```


**Тип ответа:** nsid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syntax.NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/lexgen/util.go:117`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](lex.md)

- [Следующая директория](lex_lexlint.md)


---

