---
title: "Функции: lex"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: lex
---


# Функции: lex


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](gen.md)

- [Следующая директория](lex_lexgen.md)


---


## Меню по файлам


- 📄 [lex/gen.go](#lexgengo)

- 📄 [lex/schema.go](#lexschemago)

- 📄 [lex/type_schema.go](#lextype_schemago)


---


## lex/gen.go


📄 Исходный файл: `lex/gen.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [BuildExtDefMap](#buildextdefmap-lexgengo37) `:37`

- 🔗 [CreateHandlerStub](#createhandlerstub-lexgengo281) `:281`

- 🔗 [FixRecordReferences](#fixrecordreferences-lexgengo73) `:73`

- 🔗 [GenCodeForSchema](#gencodeforschema-lexgengo111) `:111`

- 🔗 [ParsePackages](#parsepackages-lexgengo461) `:461`

- 🔗 [Run](#run-lexgengo470) `:470`

- 🔗 [WriteServerHandlers](#writeserverhandlers-lexgengo314) `:314`

- 🔗 [WriteXrpcServer](#writexrpcserver-lexgengo356) `:356`

- 🔗 [idToTitle](#idtotitle-lexgengo445) `:445`

- 🔗 [importNameForPrefix](#importnameforprefix-lexgengo310) `:310`

- 🔗 [nameFromID](#namefromid-lexgengo254) `:254`

- 🔗 [orderedMapIter](#orderedmapiter-lexgengo265) `:265`

- 🔗 [printerf](#printerf-lexgengo105) `:105`

- 🔗 [writeCodeFile](#writecodefile-lexgengo204) `:204`

- 🔗 [writeDecoderRegister](#writedecoderregister-lexgengo180) `:180`

- 🔗 [writeMethods](#writemethods-lexgengo221) `:221`


</details>


[function] name: BuildExtDefMap file: lex/gen.go:37 returns_error: нет description: Build total map of all types defined inside schemas.
Return map from fully qualified type name to its *TypeSchema


### BuildExtDefMap (lex/gen.go:37)


Build total map of all types defined inside schemas.
Return map from fully qualified type name to its *TypeSchema


```go
func BuildExtDefMap((ss []*Schema, packages []Package)) (ss []*Schema, packages []Package)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** ss


```json
{
  "logger": null,
  "db": null,
  "events": null,
  "repos": null,
  "relayUrl": "string",
  "fullNetworkMode": false,
  "signalCollection": "string",
  "collectionFilters": [],
  "parallelism": 0,
  "cursorSaveInterval": {},
  "lastSeq": {}
}
```


*Определено в:* `cmd/tap/firehose.go`


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** packages


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Package


```json
{
  "GoPackage": "string",
  "Prefix": "string",
  "Outdir": "string",
  "Import": "string"
}
```


*Определено в:* `lex/gen.go`


📍 *Расположение:* `lex/gen.go:37`



---


[function] name: CreateHandlerStub file: lex/gen.go:281 returns_error: нет description: —


### CreateHandlerStub (lex/gen.go:281)


CreateHandlerStub is a function that creates new data based on the provided parameters and returns (pkg string, impmap map[string]string, dir string, schemas []*Schema, handlers bool).


```go
func CreateHandlerStub((pkg string, impmap map[string]string, dir string, schemas []*Schema, handlers bool)) (pkg string, impmap map[string]string, dir string, schemas []*Schema, handlers bool)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** impmap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** schemas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** handlers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:281`



---


[function] name: FixRecordReferences file: lex/gen.go:73 returns_error: нет description: TODO: this method is necessary because in lexicon there is no way to know if
a type needs to be marshaled with a "$type"


### FixRecordReferences (lex/gen.go:73)


TODO: this method is necessary because in lexicon there is no way to know if
a type needs to be marshaled with a "$type" field up front, you can only
know for sure by seeing where the type is used.


```go
func FixRecordReferences((schemas []*Schema, defmap map[string]*ExtDef, prefix string)) (schemas []*Schema, defmap map[string]*ExtDef, prefix string)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип запроса:** ExtDef


```json
{
  "Type": null
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** schemas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** defmap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ExtDef


```json
{
  "Type": null
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** prefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:73`



---


[function] name: GenCodeForSchema file: lex/gen.go:111 returns_error: нет description: —


### GenCodeForSchema (lex/gen.go:111)


GenCodeForSchema is a function that performs operations based on the provided parameters and returns (pkg Package, reqcode bool, s *Schema, packages []Package, defmap map[string]*ExtDef).


```go
func GenCodeForSchema((pkg Package, reqcode bool, s *Schema, packages []Package, defmap map[string]*ExtDef)) (pkg Package, reqcode bool, s *Schema, packages []Package, defmap map[string]*ExtDef)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип запроса:** ExtDef


```json
{
  "Type": null
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Package


```json
{
  "GoPackage": "string",
  "Prefix": "string",
  "Outdir": "string",
  "Import": "string"
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** reqcode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** packages


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Package


```json
{
  "GoPackage": "string",
  "Prefix": "string",
  "Outdir": "string",
  "Import": "string"
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** defmap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ExtDef


```json
{
  "Type": null
}
```


*Определено в:* `lex/gen.go`


📍 *Расположение:* `lex/gen.go:111`



---


[function] name: ParsePackages file: lex/gen.go:461 returns_error: да description: ParsePackages reads a json blob which should be an array of Package{} objects.


### ParsePackages (lex/gen.go:461)


ParsePackages reads a json blob which should be an array of Package{} objects.


```go
func ParsePackages(([]Package, error)) ([]Package, error)
```


**Тип ответа:** Package


```json
{
  "GoPackage": "string",
  "Prefix": "string",
  "Outdir": "string",
  "Import": "string"
}
```


*Определено в:* `lex/gen.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]Package`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/gen.go:461`



---


[function] name: Run file: lex/gen.go:470 returns_error: нет description: —


### Run (lex/gen.go:470)


Run is a function that performs operations based on the provided parameters and returns (schemas []*Schema, externalSchemas []*Schema, packages []Package).


```go
func Run((schemas []*Schema, externalSchemas []*Schema, packages []Package)) (schemas []*Schema, externalSchemas []*Schema, packages []Package)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** schemas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** externalSchemas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** packages


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Package


```json
{
  "GoPackage": "string",
  "Prefix": "string",
  "Outdir": "string",
  "Import": "string"
}
```


*Определено в:* `lex/gen.go`


📍 *Расположение:* `lex/gen.go:470`



---


[function] name: WriteServerHandlers file: lex/gen.go:314 returns_error: нет description: —


### WriteServerHandlers (lex/gen.go:314)


WriteServerHandlers is a function that performs operations based on the provided parameters and returns (w io.Writer, schemas []*Schema, pkg string, impmap map[string]string).


```go
func WriteServerHandlers((w io.Writer, schemas []*Schema, pkg string, impmap map[string]string)) (w io.Writer, schemas []*Schema, pkg string, impmap map[string]string)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** schemas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** impmap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:314`



---


[function] name: WriteXrpcServer file: lex/gen.go:356 returns_error: нет description: —


### WriteXrpcServer (lex/gen.go:356)


WriteXrpcServer is a function that performs operations based on the provided parameters and returns (w io.Writer, schemas []*Schema, pkg string, impmap map[string]string).


```go
func WriteXrpcServer((w io.Writer, schemas []*Schema, pkg string, impmap map[string]string)) (w io.Writer, schemas []*Schema, pkg string, impmap map[string]string)
```


**Тип запроса:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** schemas


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Schema


```json
{
  "ID": "string",
  "Def": {}
}
```


*Определено в:* `atproto/lexicon/validation.go`


**Тип ответа:** pkg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** impmap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:356`



---


[function] name: idToTitle file: lex/gen.go:445 returns_error: нет description: —


### idToTitle (lex/gen.go:445)


idToTitle is a function that performs operations based on the provided parameters and returns (id string).


```go
func idToTitle((id string)) (id string)
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


📍 *Расположение:* `lex/gen.go:445`



---


[function] name: importNameForPrefix file: lex/gen.go:310 returns_error: нет description: —


### importNameForPrefix (lex/gen.go:310)


importNameForPrefix is a function that performs operations based on the provided parameters and returns (prefix string).


```go
func importNameForPrefix((prefix string)) (prefix string)
```


**Тип ответа:** prefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:310`



---


[function] name: nameFromID file: lex/gen.go:254 returns_error: нет description: —


### nameFromID (lex/gen.go:254)


nameFromID is a function that performs operations based on the provided parameters and returns (id, prefix string).


```go
func nameFromID((id, prefix string)) (id, prefix string)
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


**Тип ответа:** prefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:254`



---


[function] name: orderedMapIter file: lex/gen.go:265 returns_error: да description: —


### orderedMapIter (lex/gen.go:265)


orderedMapIter is a function that performs operations based on the provided parameters and may return an error.


```go
func orderedMapIter((m map[string]T, cb func(string, T) error)) (m map[string]T, cb func(string, T) error)
```


**Тип ответа:** m


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


**Тип ответа:** T


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** T


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `m map[string]T`, `cb func(string`, `T) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/gen.go:265`



---


[function] name: printerf file: lex/gen.go:105 returns_error: нет description: —


### printerf (lex/gen.go:105)


printerf is a function that performs operations based on the provided parameters and returns (w io.Writer).


```go
func printerf((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:105`



---


[function] name: writeCodeFile file: lex/gen.go:204 returns_error: нет description: —


### writeCodeFile (lex/gen.go:204)


writeCodeFile is a function that performs operations based on the provided parameters and returns (b []byte, fname string).


```go
func writeCodeFile((b []byte, fname string)) (b []byte, fname string)
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


**Тип ответа:** fname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:204`



---


[function] name: writeDecoderRegister file: lex/gen.go:180 returns_error: нет description: —


### writeDecoderRegister (lex/gen.go:180)


writeDecoderRegister is a function that performs operations based on the provided parameters and returns (w io.Writer, tps []outputType).


```go
func writeDecoderRegister((w io.Writer, tps []outputType)) (w io.Writer, tps []outputType)
```


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tps


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** outputType


```json
{
  "Name": "string",
  "Type": null,
  "NeedsCbor": false,
  "NeedsType": false
}
```


*Определено в:* `lex/gen.go`


📍 *Расположение:* `lex/gen.go:180`



---


[function] name: writeMethods file: lex/gen.go:221 returns_error: нет description: —


### writeMethods (lex/gen.go:221)


writeMethods is a function that performs operations based on the provided parameters and returns (typename string, ts *TypeSchema, w io.Writer).


```go
func writeMethods((typename string, ts *TypeSchema, w io.Writer)) (typename string, ts *TypeSchema, w io.Writer)
```


**Тип запроса:** TypeSchema


```json
{
  "prefix": "string",
  "id": "string",
  "defName": "string",
  "defMap": {},
  "needsCbor": false,
  "needsType": false,
  "Type": "string",
  "Key": "string",
  "Description": "string",
  "Parameters": null,
  "Input": null,
  "Output": null,
  "Record": null,
  "Ref": "string",
  "Refs": [],
  "Required": [],
  "Nullable": [],
  "Properties": {},
  "MaxLength": 0,
  "Items": null,
  "Const": {},
  "Enum": [],
  "Closed": false,
  "Default": {},
  "Minimum": {},
  "Maximum": {}
}
```


*Определено в:* `lex/type_schema.go`


**Тип ответа:** typename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ts


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


**Тип ответа:** TypeSchema


```json
{
  "prefix": "string",
  "id": "string",
  "defName": "string",
  "defMap": {},
  "needsCbor": false,
  "needsType": false,
  "Type": "string",
  "Key": "string",
  "Description": "string",
  "Parameters": null,
  "Input": null,
  "Output": null,
  "Record": null,
  "Ref": "string",
  "Refs": [],
  "Required": [],
  "Nullable": [],
  "Properties": {},
  "MaxLength": 0,
  "Items": null,
  "Const": {},
  "Enum": [],
  "Closed": false,
  "Default": {},
  "Minimum": {},
  "Maximum": {}
}
```


*Определено в:* `lex/type_schema.go`


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/gen.go:221`




## lex/schema.go


📄 Исходный файл: `lex/schema.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AllTypes](#alltypes-lexschemago47) `:47`

- 🔗 [Name](#name-lexschemago42) `:42`

- 🔗 [ReadSchema](#readschema-lexschemago26) `:26`


</details>


[function] name: AllTypes file: lex/schema.go:47 returns_error: нет description: —


### AllTypes (lex/schema.go:47)


AllTypes is a method that performs operations based on the provided parameters and returns (prefix string, defMap map[string]*ExtDef).


```go
func (s *Schema) AllTypes((prefix string, defMap map[string]*ExtDef)) (prefix string, defMap map[string]*ExtDef)
```


**Тип запроса:** ExtDef


```json
{
  "Type": null
}
```


*Определено в:* `lex/gen.go`


**Тип ответа:** prefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** defMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ExtDef


```json
{
  "Type": null
}
```


*Определено в:* `lex/gen.go`


📍 *Расположение:* `lex/schema.go:47`



---


[function] name: Name file: lex/schema.go:42 returns_error: нет description: —


### Name (lex/schema.go:42)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (s *Schema) Name(()) ()
```


📍 *Расположение:* `lex/schema.go:42`



---


[function] name: ReadSchema file: lex/schema.go:26 returns_error: да description: —


### ReadSchema (lex/schema.go:26)


ReadSchema is a function that performs operations based on the provided parameters and may return an error.


```go
func ReadSchema((*Schema, error)) (*Schema, error)
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


📍 *Расположение:* `lex/schema.go:26`




## lex/type_schema.go


📄 Исходный файл: `lex/type_schema.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [TypeName](#typename-lextype_schemago505) `:505`

- 🔗 [WriteHandlerStub](#writehandlerstub-lextype_schemago192) `:192`

- 🔗 [WriteRPC](#writerpc-lextype_schemago54) `:54`

- 🔗 [WriteRPCHandler](#writerpchandler-lextype_schemago259) `:259`

- 🔗 [WriteType](#writetype-lextype_schemago601) `:601`

- 🔗 [lookupRef](#lookupref-lextype_schemago584) `:584`

- 🔗 [namesFromRef](#namesfromref-lextype_schemago470) `:470`

- 🔗 [typeNameForField](#typenameforfield-lextype_schemago531) `:531`

- 🔗 [writeCborMarshalerEnum](#writecbormarshalerenum-lextype_schemago861) `:861`

- 🔗 [writeCborUnmarshalerEnum](#writecborunmarshalerenum-lextype_schemago881) `:881`

- 🔗 [writeJsonMarshalerEnum](#writejsonmarshalerenum-lextype_schemago801) `:801`

- 🔗 [writeJsonMarshalerObject](#writejsonmarshalerobject-lextype_schemago797) `:797`

- 🔗 [writeJsonUnmarshalerEnum](#writejsonunmarshalerenum-lextype_schemago826) `:826`

- 🔗 [writeJsonUnmarshalerObject](#writejsonunmarshalerobject-lextype_schemago820) `:820`

- 🔗 [writeTypeDefinition](#writetypedefinition-lextype_schemago616) `:616`

- 🔗 [writeTypeMethods](#writetypemethods-lextype_schemago745) `:745`


</details>


[function] name: TypeName file: lex/type_schema.go:505 returns_error: нет description: —


### TypeName (lex/type_schema.go:505)


TypeName is a method that performs operations based on the provided parameters and returns ().


```go
func (s *TypeSchema) TypeName(()) ()
```


📍 *Расположение:* `lex/type_schema.go:505`



---


[function] name: WriteHandlerStub file: lex/type_schema.go:192 returns_error: нет description: —


### WriteHandlerStub (lex/type_schema.go:192)


WriteHandlerStub is a method that performs operations based on the provided parameters and returns (w io.Writer, fname, shortname, impname string).


```go
func (s *TypeSchema) WriteHandlerStub((w io.Writer, fname, shortname, impname string)) (w io.Writer, fname, shortname, impname string)
```


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shortname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** impname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:192`



---


[function] name: WriteRPC file: lex/type_schema.go:54 returns_error: нет description: —


### WriteRPC (lex/type_schema.go:54)


WriteRPC is a method that performs operations based on the provided parameters and returns (w io.Writer, typename, inputname string).


```go
func (s *TypeSchema) WriteRPC((w io.Writer, typename, inputname string)) (w io.Writer, typename, inputname string)
```


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** typename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** inputname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:54`



---


[function] name: WriteRPCHandler file: lex/type_schema.go:259 returns_error: нет description: —


### WriteRPCHandler (lex/type_schema.go:259)


WriteRPCHandler is a method that performs operations based on the provided parameters and returns (w io.Writer, fname, shortname, impname string).


```go
func (s *TypeSchema) WriteRPCHandler((w io.Writer, fname, shortname, impname string)) (w io.Writer, fname, shortname, impname string)
```


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** fname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shortname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** impname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:259`



---


[function] name: WriteType file: lex/type_schema.go:601 returns_error: нет description: name is the top level type name from outputType
WriteType is only called on a top level TypeSchema


### WriteType (lex/type_schema.go:601)


name is the top level type name from outputType
WriteType is only called on a top level TypeSchema


```go
func (ts *TypeSchema) WriteType((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:601`



---


[function] name: lookupRef file: lex/type_schema.go:584 returns_error: да description: —


### lookupRef (lex/type_schema.go:584)


lookupRef is a method that performs operations based on the provided parameters and may return an error.


```go
func (ts *TypeSchema) lookupRef((*TypeSchema, error)) (*TypeSchema, error)
```


**Тип запроса:** TypeSchema


```json
{
  "prefix": "string",
  "id": "string",
  "defName": "string",
  "defMap": {},
  "needsCbor": false,
  "needsType": false,
  "Type": "string",
  "Key": "string",
  "Description": "string",
  "Parameters": null,
  "Input": null,
  "Output": null,
  "Record": null,
  "Ref": "string",
  "Refs": [],
  "Required": [],
  "Nullable": [],
  "Properties": {},
  "MaxLength": 0,
  "Items": null,
  "Const": {},
  "Enum": [],
  "Closed": false,
  "Default": {},
  "Minimum": {},
  "Maximum": {}
}
```


*Определено в:* `lex/type_schema.go`


**Тип ответа:** TypeSchema


```json
{
  "prefix": "string",
  "id": "string",
  "defName": "string",
  "defMap": {},
  "needsCbor": false,
  "needsType": false,
  "Type": "string",
  "Key": "string",
  "Description": "string",
  "Parameters": null,
  "Input": null,
  "Output": null,
  "Record": null,
  "Ref": "string",
  "Refs": [],
  "Required": [],
  "Nullable": [],
  "Properties": {},
  "MaxLength": 0,
  "Items": null,
  "Const": {},
  "Enum": [],
  "Closed": false,
  "Default": {},
  "Minimum": {},
  "Maximum": {}
}
```


*Определено в:* `lex/type_schema.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TypeSchema`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/type_schema.go:584`



---


[function] name: namesFromRef file: lex/type_schema.go:470 returns_error: нет description: —


### namesFromRef (lex/type_schema.go:470)


namesFromRef is a method that performs operations based on the provided parameters and returns (string, string).


```go
func (s *TypeSchema) namesFromRef((string, string)) (string, string)
```


📍 *Расположение:* `lex/type_schema.go:470`



---


[function] name: typeNameForField file: lex/type_schema.go:531 returns_error: да description: name: enclosing type name
k: field name
v: field TypeSchema


### typeNameForField (lex/type_schema.go:531)


name: enclosing type name
k: field name
v: field TypeSchema


```go
func (s *TypeSchema) typeNameForField((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `lex/type_schema.go:531`



---


[function] name: writeCborMarshalerEnum file: lex/type_schema.go:861 returns_error: нет description: —


### writeCborMarshalerEnum (lex/type_schema.go:861)


writeCborMarshalerEnum is a method that performs operations based on the provided parameters and returns (name string, w io.Writer).


```go
func (ts *TypeSchema) writeCborMarshalerEnum((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:861`



---


[function] name: writeCborUnmarshalerEnum file: lex/type_schema.go:881 returns_error: нет description: —


### writeCborUnmarshalerEnum (lex/type_schema.go:881)


writeCborUnmarshalerEnum is a method that performs operations based on the provided parameters and returns (name string, w io.Writer).


```go
func (ts *TypeSchema) writeCborUnmarshalerEnum((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:881`



---


[function] name: writeJsonMarshalerEnum file: lex/type_schema.go:801 returns_error: нет description: —


### writeJsonMarshalerEnum (lex/type_schema.go:801)


writeJsonMarshalerEnum is a method that performs operations based on the provided parameters and returns (name string, w io.Writer).


```go
func (ts *TypeSchema) writeJsonMarshalerEnum((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:801`



---


[function] name: writeJsonMarshalerObject file: lex/type_schema.go:797 returns_error: нет description: —


### writeJsonMarshalerObject (lex/type_schema.go:797)


writeJsonMarshalerObject is a method that performs operations based on the provided parameters and returns (name string, w io.Writer).


```go
func (ts *TypeSchema) writeJsonMarshalerObject((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:797`



---


[function] name: writeJsonUnmarshalerEnum file: lex/type_schema.go:826 returns_error: нет description: —


### writeJsonUnmarshalerEnum (lex/type_schema.go:826)


writeJsonUnmarshalerEnum is a method that performs operations based on the provided parameters and returns (name string, w io.Writer).


```go
func (ts *TypeSchema) writeJsonUnmarshalerEnum((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:826`



---


[function] name: writeJsonUnmarshalerObject file: lex/type_schema.go:820 returns_error: нет description: —


### writeJsonUnmarshalerObject (lex/type_schema.go:820)


writeJsonUnmarshalerObject is a method that performs operations based on the provided parameters and returns (name string, w io.Writer).


```go
func (s *TypeSchema) writeJsonUnmarshalerObject((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:820`



---


[function] name: writeTypeDefinition file: lex/type_schema.go:616 returns_error: нет description: name is the top level type name from outputType
writeTypeDefinition is not called recursively, but only on a top level T


### writeTypeDefinition (lex/type_schema.go:616)


name is the top level type name from outputType
writeTypeDefinition is not called recursively, but only on a top level TypeSchema


```go
func (ts *TypeSchema) writeTypeDefinition((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:616`



---


[function] name: writeTypeMethods file: lex/type_schema.go:745 returns_error: нет description: —


### writeTypeMethods (lex/type_schema.go:745)


writeTypeMethods is a method that performs operations based on the provided parameters and returns (name string, w io.Writer).


```go
func (ts *TypeSchema) writeTypeMethods((name string, w io.Writer)) (name string, w io.Writer)
```


**Тип ответа:** name


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** w


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


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `lex/type_schema.go:745`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](gen.md)

- [Следующая директория](lex_lexgen.md)


---

