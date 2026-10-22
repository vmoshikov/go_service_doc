---
title: "Функции: atproto/syntax"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/syntax
---


# Функции: atproto/syntax


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_repo.md)

- [Следующая директория](automod_cachestore.md)


---


## Меню по файлам


- 📄 [atproto/syntax/atidentifier.go](#atprotosyntaxatidentifiergo)

- 📄 [atproto/syntax/aturi.go](#atprotosyntaxaturigo)

- 📄 [atproto/syntax/cid.go](#atprotosyntaxcidgo)

- 📄 [atproto/syntax/cmd/atp-syntax/main.go](#atprotosyntaxcmdatp-syntaxmaingo)

- 📄 [atproto/syntax/datetime.go](#atprotosyntaxdatetimego)

- 📄 [atproto/syntax/did.go](#atprotosyntaxdidgo)

- 📄 [atproto/syntax/handle.go](#atprotosyntaxhandlego)

- 📄 [atproto/syntax/language.go](#atprotosyntaxlanguagego)

- 📄 [atproto/syntax/nsid.go](#atprotosyntaxnsidgo)

- 📄 [atproto/syntax/path.go](#atprotosyntaxpathgo)

- 📄 [atproto/syntax/recordkey.go](#atprotosyntaxrecordkeygo)

- 📄 [atproto/syntax/tid.go](#atprotosyntaxtidgo)

- 📄 [atproto/syntax/uri.go](#atprotosyntaxurigo)


---


## atproto/syntax/atidentifier.go


📄 Исходный файл: `atproto/syntax/atidentifier.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [AsDID](#asdid-atprotosyntaxatidentifiergo50) `:50`

- 🔗 [AsHandle](#ashandle-atprotosyntaxatidentifiergo32) `:32`

- 🔗 [DID](#did-atprotosyntaxatidentifiergo57) `:57`

- 🔗 [Handle](#handle-atprotosyntaxatidentifiergo39) `:39`

- 🔗 [IsDID](#isdid-atprotosyntaxatidentifiergo46) `:46`

- 🔗 [IsHandle](#ishandle-atprotosyntaxatidentifiergo28) `:28`

- 🔗 [MarshalText](#marshaltext-atprotosyntaxatidentifiergo75) `:75`

- 🔗 [Normalize](#normalize-atprotosyntaxatidentifiergo64) `:64`

- 🔗 [ParseAtIdentifier](#parseatidentifier-atprotosyntaxatidentifiergo10) `:10`

- 🔗 [String](#string-atprotosyntaxatidentifiergo71) `:71`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxatidentifiergo79) `:79`


</details>


[function] name: AsDID file: atproto/syntax/atidentifier.go:50 returns_error: да description: —


### AsDID (atproto/syntax/atidentifier.go:50)


AsDID is a method that performs operations based on the provided parameters and may return an error.


```go
func (n AtIdentifier) AsDID((DID, error)) (DID, error)
```


**Тип ответа:** DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/atidentifier.go:50`



---


[function] name: AsHandle file: atproto/syntax/atidentifier.go:32 returns_error: да description: —


### AsHandle (atproto/syntax/atidentifier.go:32)


AsHandle is a method that performs operations based on the provided parameters and may return an error.


```go
func (n AtIdentifier) AsHandle((Handle, error)) (Handle, error)
```


**Тип ответа:** Handle


```json
{
  "Handle": "string",
  "Valid": {}
}
```


*Определено в:* `cmd/gosky/main.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Handle`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/atidentifier.go:32`



---


[function] name: DID file: atproto/syntax/atidentifier.go:57 returns_error: нет description: —


### DID (atproto/syntax/atidentifier.go:57)


DID is a method that performs operations based on the provided parameters and returns ().


```go
func (n AtIdentifier) DID(()) ()
```


📍 *Расположение:* `atproto/syntax/atidentifier.go:57`



---


[function] name: Handle file: atproto/syntax/atidentifier.go:39 returns_error: нет description: —


### Handle (atproto/syntax/atidentifier.go:39)


Handle is a method that handles or processes requests based on the provided parameters and returns ().


```go
func (n AtIdentifier) Handle(()) ()
```


📍 *Расположение:* `atproto/syntax/atidentifier.go:39`



---


[function] name: IsDID file: atproto/syntax/atidentifier.go:46 returns_error: нет description: —


### IsDID (atproto/syntax/atidentifier.go:46)


IsDID is a method that performs operations based on the provided parameters and returns ().


```go
func (n AtIdentifier) IsDID(()) ()
```


📍 *Расположение:* `atproto/syntax/atidentifier.go:46`



---


[function] name: IsHandle file: atproto/syntax/atidentifier.go:28 returns_error: нет description: —


### IsHandle (atproto/syntax/atidentifier.go:28)


IsHandle is a method that performs operations based on the provided parameters and returns ().


```go
func (n AtIdentifier) IsHandle(()) ()
```


📍 *Расположение:* `atproto/syntax/atidentifier.go:28`



---


[function] name: MarshalText file: atproto/syntax/atidentifier.go:75 returns_error: да description: —


### MarshalText (atproto/syntax/atidentifier.go:75)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (a AtIdentifier) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/atidentifier.go:75`



---


[function] name: Normalize file: atproto/syntax/atidentifier.go:64 returns_error: нет description: —


### Normalize (atproto/syntax/atidentifier.go:64)


Normalize is a method that performs operations based on the provided parameters and returns ().


```go
func (n AtIdentifier) Normalize(()) ()
```


📍 *Расположение:* `atproto/syntax/atidentifier.go:64`



---


[function] name: ParseAtIdentifier file: atproto/syntax/atidentifier.go:10 returns_error: да description: —


### ParseAtIdentifier (atproto/syntax/atidentifier.go:10)


ParseAtIdentifier is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseAtIdentifier((AtIdentifier, error)) (AtIdentifier, error)
```


**Тип ответа:** AtIdentifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `AtIdentifier`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/atidentifier.go:10`



---


[function] name: String file: atproto/syntax/atidentifier.go:71 returns_error: нет description: —


### String (atproto/syntax/atidentifier.go:71)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (n AtIdentifier) String(()) ()
```


📍 *Расположение:* `atproto/syntax/atidentifier.go:71`



---


[function] name: UnmarshalText file: atproto/syntax/atidentifier.go:79 returns_error: нет description: —


### UnmarshalText (atproto/syntax/atidentifier.go:79)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (a *AtIdentifier) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/atidentifier.go:79`




## atproto/syntax/aturi.go


📄 Исходный файл: `atproto/syntax/aturi.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [Authority](#authority-atprotosyntaxaturigo50) `:50`

- 🔗 [Collection](#collection-atprotosyntaxaturigo77) `:77`

- 🔗 [MarshalText](#marshaltext-atprotosyntaxaturigo124) `:124`

- 🔗 [Normalize](#normalize-atprotosyntaxaturigo103) `:103`

- 🔗 [ParseATURI](#parseaturi-atprotosyntaxaturigo19) `:19`

- 🔗 [Path](#path-atprotosyntaxaturigo64) `:64`

- 🔗 [RecordKey](#recordkey-atprotosyntaxaturigo90) `:90`

- 🔗 [String](#string-atprotosyntaxaturigo120) `:120`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxaturigo128) `:128`


</details>


[function] name: Authority file: atproto/syntax/aturi.go:50 returns_error: нет description: Every valid ATURI has a valid AtIdentifier in the authority position.

If this ATURI is malformed, returns empty


### Authority (atproto/syntax/aturi.go:50)


Every valid ATURI has a valid AtIdentifier in the authority position.

If this ATURI is malformed, returns empty


```go
func (n ATURI) Authority(()) ()
```


📍 *Расположение:* `atproto/syntax/aturi.go:50`



---


[function] name: Collection file: atproto/syntax/aturi.go:77 returns_error: нет description: Returns a valid NSID if there is one in the appropriate part of the path, otherwise empty.


### Collection (atproto/syntax/aturi.go:77)


Returns a valid NSID if there is one in the appropriate part of the path, otherwise empty.


```go
func (n ATURI) Collection(()) ()
```


📍 *Расположение:* `atproto/syntax/aturi.go:77`



---


[function] name: MarshalText file: atproto/syntax/aturi.go:124 returns_error: да description: —


### MarshalText (atproto/syntax/aturi.go:124)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (a ATURI) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/aturi.go:124`



---


[function] name: Normalize file: atproto/syntax/aturi.go:103 returns_error: нет description: —


### Normalize (atproto/syntax/aturi.go:103)


Normalize is a method that performs operations based on the provided parameters and returns ().


```go
func (n ATURI) Normalize(()) ()
```


📍 *Расположение:* `atproto/syntax/aturi.go:103`



---


[function] name: ParseATURI file: atproto/syntax/aturi.go:19 returns_error: да description: —


### ParseATURI (atproto/syntax/aturi.go:19)


ParseATURI is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseATURI((ATURI, error)) (ATURI, error)
```


**Тип ответа:** ATURI


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `ATURI`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/aturi.go:19`



---


[function] name: Path file: atproto/syntax/aturi.go:64 returns_error: нет description: Returns path segment, without leading slash, as would be used in an atproto repository key. Or empty string if there is 


### Path (atproto/syntax/aturi.go:64)


Returns path segment, without leading slash, as would be used in an atproto repository key. Or empty string if there is no path.


```go
func (n ATURI) Path(()) ()
```


📍 *Расположение:* `atproto/syntax/aturi.go:64`



---


[function] name: RecordKey file: atproto/syntax/aturi.go:90 returns_error: нет description: —


### RecordKey (atproto/syntax/aturi.go:90)


RecordKey is a method that performs operations based on the provided parameters and returns ().


```go
func (n ATURI) RecordKey(()) ()
```


📍 *Расположение:* `atproto/syntax/aturi.go:90`



---


[function] name: String file: atproto/syntax/aturi.go:120 returns_error: нет description: —


### String (atproto/syntax/aturi.go:120)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (n ATURI) String(()) ()
```


📍 *Расположение:* `atproto/syntax/aturi.go:120`



---


[function] name: UnmarshalText file: atproto/syntax/aturi.go:128 returns_error: нет description: —


### UnmarshalText (atproto/syntax/aturi.go:128)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (a *ATURI) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/aturi.go:128`




## atproto/syntax/cid.go


📄 Исходный файл: `atproto/syntax/cid.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalText](#marshaltext-atprotosyntaxcidgo42) `:42`

- 🔗 [ParseCID](#parsecid-atprotosyntaxcidgo18) `:18`

- 🔗 [String](#string-atprotosyntaxcidgo38) `:38`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxcidgo46) `:46`


</details>


[function] name: MarshalText file: atproto/syntax/cid.go:42 returns_error: да description: —


### MarshalText (atproto/syntax/cid.go:42)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (c CID) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/cid.go:42`



---


[function] name: ParseCID file: atproto/syntax/cid.go:18 returns_error: да description: —


### ParseCID (atproto/syntax/cid.go:18)


ParseCID is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseCID((CID, error)) (CID, error)
```


**Тип ответа:** CID


```json
{
  "CID": {}
}
```


*Определено в:* `models/dbcid.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `CID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/cid.go:18`



---


[function] name: String file: atproto/syntax/cid.go:38 returns_error: нет description: —


### String (atproto/syntax/cid.go:38)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (c CID) String(()) ()
```


📍 *Расположение:* `atproto/syntax/cid.go:38`



---


[function] name: UnmarshalText file: atproto/syntax/cid.go:46 returns_error: нет description: —


### UnmarshalText (atproto/syntax/cid.go:46)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (c *CID) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/cid.go:46`




## atproto/syntax/cmd/atp-syntax/main.go


📄 Исходный файл: `atproto/syntax/cmd/atp-syntax/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [main](#main-atprotosyntaxcmdatp-syntaxmaingo14) `:14`

- 🔗 [runParseDID](#runparsedid-atprotosyntaxcmdatp-syntaxmaingo57) `:57`

- 🔗 [runParseTID](#runparsetid-atprotosyntaxcmdatp-syntaxmaingo41) `:41`


</details>


[function] name: main file: atproto/syntax/cmd/atp-syntax/main.go:14 returns_error: нет description: —


### main (atproto/syntax/cmd/atp-syntax/main.go:14)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `atproto/syntax/cmd/atp-syntax/main.go:14`



---


[function] name: runParseDID file: atproto/syntax/cmd/atp-syntax/main.go:57 returns_error: нет description: —


### runParseDID (atproto/syntax/cmd/atp-syntax/main.go:57)


runParseDID is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runParseDID((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/syntax/cmd/atp-syntax/main.go:57`



---


[function] name: runParseTID file: atproto/syntax/cmd/atp-syntax/main.go:41 returns_error: нет description: —


### runParseTID (atproto/syntax/cmd/atp-syntax/main.go:41)


runParseTID is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runParseTID((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/syntax/cmd/atp-syntax/main.go:41`




## atproto/syntax/datetime.go


📄 Исходный файл: `atproto/syntax/datetime.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [DatetimeNow](#datetimenow-atprotosyntaxdatetimego110) `:110`

- 🔗 [MarshalText](#marshaltext-atprotosyntaxdatetimego119) `:119`

- 🔗 [ParseDatetime](#parsedatetime-atprotosyntaxdatetimego28) `:28`

- 🔗 [ParseDatetimeLenient](#parsedatetimelenient-atprotosyntaxdatetimego69) `:69`

- 🔗 [ParseDatetimeTime](#parsedatetimetime-atprotosyntaxdatetimego55) `:55`

- 🔗 [String](#string-atprotosyntaxdatetimego115) `:115`

- 🔗 [Time](#time-atprotosyntaxdatetimego100) `:100`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxdatetimego123) `:123`


</details>


[function] name: DatetimeNow file: atproto/syntax/datetime.go:110 returns_error: нет description: Creates a new valid Datetime string matching the current time, in preferred syntax.


### DatetimeNow (atproto/syntax/datetime.go:110)


Creates a new valid Datetime string matching the current time, in preferred syntax.


```go
func DatetimeNow(()) ()
```


📍 *Расположение:* `atproto/syntax/datetime.go:110`



---


[function] name: MarshalText file: atproto/syntax/datetime.go:119 returns_error: да description: —


### MarshalText (atproto/syntax/datetime.go:119)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (d Datetime) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/datetime.go:119`



---


[function] name: ParseDatetime file: atproto/syntax/datetime.go:28 returns_error: да description: —


### ParseDatetime (atproto/syntax/datetime.go:28)


ParseDatetime is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseDatetime((Datetime, error)) (Datetime, error)
```


**Тип ответа:** Datetime


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Datetime`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/datetime.go:28`



---


[function] name: ParseDatetimeLenient file: atproto/syntax/datetime.go:69 returns_error: да description: —


### ParseDatetimeLenient (atproto/syntax/datetime.go:69)


ParseDatetimeLenient is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseDatetimeLenient((Datetime, error)) (Datetime, error)
```


**Тип ответа:** Datetime


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Datetime`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/datetime.go:69`



---


[function] name: ParseDatetimeTime file: atproto/syntax/datetime.go:55 returns_error: да description: Validates and converts a string to a golang [time.Time] in a single step.


### ParseDatetimeTime (atproto/syntax/datetime.go:55)


Validates and converts a string to a golang [time.Time] in a single step.


```go
func ParseDatetimeTime((time.Time, error)) (time.Time, error)
```


**Тип ответа:** time.Time


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `time.Time`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/datetime.go:55`



---


[function] name: String file: atproto/syntax/datetime.go:115 returns_error: нет description: —


### String (atproto/syntax/datetime.go:115)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (d Datetime) String(()) ()
```


📍 *Расположение:* `atproto/syntax/datetime.go:115`



---


[function] name: Time file: atproto/syntax/datetime.go:100 returns_error: нет description: Parses the Datetime string in to a golang [time.Time].

This method assumes that [ParseDatetime] was used to create the 


### Time (atproto/syntax/datetime.go:100)


Parses the Datetime string in to a golang [time.Time].

This method assumes that [ParseDatetime] was used to create the Datetime, which already verified parsing, and thus that [time.Parse] will always succeed. In the event of an error, zero/nil will be returned.


```go
func (d Datetime) Time(()) ()
```


📍 *Расположение:* `atproto/syntax/datetime.go:100`



---


[function] name: UnmarshalText file: atproto/syntax/datetime.go:123 returns_error: нет description: —


### UnmarshalText (atproto/syntax/datetime.go:123)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (d *Datetime) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/datetime.go:123`




## atproto/syntax/did.go


📄 Исходный файл: `atproto/syntax/did.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [AtIdentifier](#atidentifier-atprotosyntaxdidgo74) `:74`

- 🔗 [Identifier](#identifier-atprotosyntaxdidgo64) `:64`

- 🔗 [MarshalText](#marshaltext-atprotosyntaxdidgo82) `:82`

- 🔗 [Method](#method-atprotosyntaxdidgo53) `:53`

- 🔗 [ParseDID](#parsedid-atprotosyntaxdidgo25) `:25`

- 🔗 [String](#string-atprotosyntaxdidgo78) `:78`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxdidgo86) `:86`

- 🔗 [isASCIIAlphaNum](#isasciialphanum-atprotosyntaxdidgo18) `:18`


</details>


[function] name: AtIdentifier file: atproto/syntax/did.go:74 returns_error: нет description: —


### AtIdentifier (atproto/syntax/did.go:74)


AtIdentifier is a method that performs operations based on the provided parameters and returns ().


```go
func (d DID) AtIdentifier(()) ()
```


📍 *Расположение:* `atproto/syntax/did.go:74`



---


[function] name: Identifier file: atproto/syntax/did.go:64 returns_error: нет description: The final "identifier" segment of the DID


### Identifier (atproto/syntax/did.go:64)


The final "identifier" segment of the DID


```go
func (d DID) Identifier(()) ()
```


📍 *Расположение:* `atproto/syntax/did.go:64`



---


[function] name: MarshalText file: atproto/syntax/did.go:82 returns_error: да description: —


### MarshalText (atproto/syntax/did.go:82)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (d DID) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/did.go:82`



---


[function] name: Method file: atproto/syntax/did.go:53 returns_error: нет description: The "method" part of the DID, between the 'did:' prefix and the final identifier segment, normalized to lower-case.


### Method (atproto/syntax/did.go:53)


The "method" part of the DID, between the 'did:' prefix and the final identifier segment, normalized to lower-case.


```go
func (d DID) Method(()) ()
```


📍 *Расположение:* `atproto/syntax/did.go:53`



---


[function] name: ParseDID file: atproto/syntax/did.go:25 returns_error: да description: —


### ParseDID (atproto/syntax/did.go:25)


ParseDID is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseDID((DID, error)) (DID, error)
```


**Тип ответа:** DID


```json
{
  "outbox": null,
  "ctx": {},
  "did": "string",
  "notifChan": {},
  "pendingEvts": [],
  "inFlightSentAt": {},
  "blockedOnLive": false,
  "running": false,
  "mu": {}
}
```


*Определено в:* `cmd/tap/outbox.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `DID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/did.go:25`



---


[function] name: String file: atproto/syntax/did.go:78 returns_error: нет description: —


### String (atproto/syntax/did.go:78)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (d DID) String(()) ()
```


📍 *Расположение:* `atproto/syntax/did.go:78`



---


[function] name: UnmarshalText file: atproto/syntax/did.go:86 returns_error: нет description: —


### UnmarshalText (atproto/syntax/did.go:86)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (d *DID) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/did.go:86`



---


[function] name: isASCIIAlphaNum file: atproto/syntax/did.go:18 returns_error: нет description: —


### isASCIIAlphaNum (atproto/syntax/did.go:18)


isASCIIAlphaNum is a function that performs operations based on the provided parameters and returns (c rune).


```go
func isASCIIAlphaNum((c rune)) (c rune)
```


**Тип ответа:** c


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


📍 *Расположение:* `atproto/syntax/did.go:18`




## atproto/syntax/handle.go


📄 Исходный файл: `atproto/syntax/handle.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [AllowedTLD](#allowedtld-atprotosyntaxhandlego40) `:40`

- 🔗 [AtIdentifier](#atidentifier-atprotosyntaxhandlego69) `:69`

- 🔗 [IsInvalidHandle](#isinvalidhandle-atprotosyntaxhandlego61) `:61`

- 🔗 [MarshalText](#marshaltext-atprotosyntaxhandlego77) `:77`

- 🔗 [Normalize](#normalize-atprotosyntaxhandlego65) `:65`

- 🔗 [ParseHandle](#parsehandle-atprotosyntaxhandlego24) `:24`

- 🔗 [String](#string-atprotosyntaxhandlego73) `:73`

- 🔗 [TLD](#tld-atprotosyntaxhandlego55) `:55`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxhandlego81) `:81`


</details>


[function] name: AllowedTLD file: atproto/syntax/handle.go:40 returns_error: нет description: Some top-level domains (TLDs) are disallowed for registration across the atproto ecosystem. The *syntax* is valid, but t


### AllowedTLD (atproto/syntax/handle.go:40)


Some top-level domains (TLDs) are disallowed for registration across the atproto ecosystem. The *syntax* is valid, but these should never be considered acceptable handles for account registration or linking.

The reserved '.test' TLD is allowed, for testing and development. It is expected that '.test' domain resolution will fail in a real-world network.


```go
func (h Handle) AllowedTLD(()) ()
```


📍 *Расположение:* `atproto/syntax/handle.go:40`



---


[function] name: AtIdentifier file: atproto/syntax/handle.go:69 returns_error: нет description: —


### AtIdentifier (atproto/syntax/handle.go:69)


AtIdentifier is a method that performs operations based on the provided parameters and returns ().


```go
func (h Handle) AtIdentifier(()) ()
```


📍 *Расположение:* `atproto/syntax/handle.go:69`



---


[function] name: IsInvalidHandle file: atproto/syntax/handle.go:61 returns_error: нет description: Is this the special "handle.invalid" handle?


### IsInvalidHandle (atproto/syntax/handle.go:61)


Is this the special "handle.invalid" handle?


```go
func (h Handle) IsInvalidHandle(()) ()
```


📍 *Расположение:* `atproto/syntax/handle.go:61`



---


[function] name: MarshalText file: atproto/syntax/handle.go:77 returns_error: да description: —


### MarshalText (atproto/syntax/handle.go:77)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (h Handle) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/handle.go:77`



---


[function] name: Normalize file: atproto/syntax/handle.go:65 returns_error: нет description: —


### Normalize (atproto/syntax/handle.go:65)


Normalize is a method that performs operations based on the provided parameters and returns ().


```go
func (h Handle) Normalize(()) ()
```


📍 *Расположение:* `atproto/syntax/handle.go:65`



---


[function] name: ParseHandle file: atproto/syntax/handle.go:24 returns_error: да description: —


### ParseHandle (atproto/syntax/handle.go:24)


ParseHandle is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseHandle((Handle, error)) (Handle, error)
```


**Тип ответа:** Handle


```json
{
  "Handle": "string",
  "Valid": {}
}
```


*Определено в:* `cmd/gosky/main.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Handle`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/handle.go:24`



---


[function] name: String file: atproto/syntax/handle.go:73 returns_error: нет description: —


### String (atproto/syntax/handle.go:73)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (h Handle) String(()) ()
```


📍 *Расположение:* `atproto/syntax/handle.go:73`



---


[function] name: TLD file: atproto/syntax/handle.go:55 returns_error: нет description: —


### TLD (atproto/syntax/handle.go:55)


TLD is a method that performs operations based on the provided parameters and returns ().


```go
func (h Handle) TLD(()) ()
```


📍 *Расположение:* `atproto/syntax/handle.go:55`



---


[function] name: UnmarshalText file: atproto/syntax/handle.go:81 returns_error: нет description: —


### UnmarshalText (atproto/syntax/handle.go:81)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (h *Handle) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/handle.go:81`




## atproto/syntax/language.go


📄 Исходный файл: `atproto/syntax/language.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalText](#marshaltext-atprotosyntaxlanguagego34) `:34`

- 🔗 [ParseLanguage](#parselanguage-atprotosyntaxlanguagego17) `:17`

- 🔗 [String](#string-atprotosyntaxlanguagego30) `:30`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxlanguagego38) `:38`


</details>


[function] name: MarshalText file: atproto/syntax/language.go:34 returns_error: да description: —


### MarshalText (atproto/syntax/language.go:34)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (l Language) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/language.go:34`



---


[function] name: ParseLanguage file: atproto/syntax/language.go:17 returns_error: да description: —


### ParseLanguage (atproto/syntax/language.go:17)


ParseLanguage is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseLanguage((Language, error)) (Language, error)
```


**Тип ответа:** Language


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Language`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/language.go:17`



---


[function] name: String file: atproto/syntax/language.go:30 returns_error: нет description: —


### String (atproto/syntax/language.go:30)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (l Language) String(()) ()
```


📍 *Расположение:* `atproto/syntax/language.go:30`



---


[function] name: UnmarshalText file: atproto/syntax/language.go:38 returns_error: нет description: —


### UnmarshalText (atproto/syntax/language.go:38)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (l *Language) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/language.go:38`




## atproto/syntax/nsid.go


📄 Исходный файл: `atproto/syntax/nsid.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Authority](#authority-atprotosyntaxnsidgo32) `:32`

- 🔗 [MarshalText](#marshaltext-atprotosyntaxnsidgo67) `:67`

- 🔗 [Name](#name-atprotosyntaxnsidgo47) `:47`

- 🔗 [Normalize](#normalize-atprotosyntaxnsidgo56) `:56`

- 🔗 [ParseNSID](#parsensid-atprotosyntaxnsidgo18) `:18`

- 🔗 [String](#string-atprotosyntaxnsidgo52) `:52`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxnsidgo71) `:71`


</details>


[function] name: Authority file: atproto/syntax/nsid.go:32 returns_error: нет description: Authority domain name, in regular DNS order, not reversed order, normalized to lower-case.


### Authority (atproto/syntax/nsid.go:32)


Authority domain name, in regular DNS order, not reversed order, normalized to lower-case.


```go
func (n NSID) Authority(()) ()
```


📍 *Расположение:* `atproto/syntax/nsid.go:32`



---


[function] name: MarshalText file: atproto/syntax/nsid.go:67 returns_error: да description: —


### MarshalText (atproto/syntax/nsid.go:67)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (n NSID) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/nsid.go:67`



---


[function] name: Name file: atproto/syntax/nsid.go:47 returns_error: нет description: —


### Name (atproto/syntax/nsid.go:47)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (n NSID) Name(()) ()
```


📍 *Расположение:* `atproto/syntax/nsid.go:47`



---


[function] name: Normalize file: atproto/syntax/nsid.go:56 returns_error: нет description: —


### Normalize (atproto/syntax/nsid.go:56)


Normalize is a method that performs operations based on the provided parameters and returns ().


```go
func (n NSID) Normalize(()) ()
```


📍 *Расположение:* `atproto/syntax/nsid.go:56`



---


[function] name: ParseNSID file: atproto/syntax/nsid.go:18 returns_error: да description: —


### ParseNSID (atproto/syntax/nsid.go:18)


ParseNSID is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseNSID((NSID, error)) (NSID, error)
```


**Тип ответа:** NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `NSID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/nsid.go:18`



---


[function] name: String file: atproto/syntax/nsid.go:52 returns_error: нет description: —


### String (atproto/syntax/nsid.go:52)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (n NSID) String(()) ()
```


📍 *Расположение:* `atproto/syntax/nsid.go:52`



---


[function] name: UnmarshalText file: atproto/syntax/nsid.go:71 returns_error: нет description: —


### UnmarshalText (atproto/syntax/nsid.go:71)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (n *NSID) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/nsid.go:71`




## atproto/syntax/path.go


📄 Исходный файл: `atproto/syntax/path.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ParseRepoPath](#parserepopath-atprotosyntaxpathgo12) `:12`


</details>


[function] name: ParseRepoPath file: atproto/syntax/path.go:12 returns_error: да description: Parses an atproto repo path string in to "collection" (NSID) and record key parts.

Does not return partial success: eit


### ParseRepoPath (atproto/syntax/path.go:12)


Parses an atproto repo path string in to "collection" (NSID) and record key parts.

Does not return partial success: either both collection and record key are complete (and error is nil), or both are empty string (and error is not nil)


```go
func ParseRepoPath((NSID, RecordKey, error)) (NSID, RecordKey, error)
```


**Тип ответа:** NSID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** RecordKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `NSID`, `RecordKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/path.go:12`




## atproto/syntax/recordkey.go


📄 Исходный файл: `atproto/syntax/recordkey.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalText](#marshaltext-atprotosyntaxrecordkeygo37) `:37`

- 🔗 [ParseRecordKey](#parserecordkey-atprotosyntaxrecordkeygo17) `:17`

- 🔗 [String](#string-atprotosyntaxrecordkeygo33) `:33`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxrecordkeygo41) `:41`


</details>


[function] name: MarshalText file: atproto/syntax/recordkey.go:37 returns_error: да description: —


### MarshalText (atproto/syntax/recordkey.go:37)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (r RecordKey) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/recordkey.go:37`



---


[function] name: ParseRecordKey file: atproto/syntax/recordkey.go:17 returns_error: да description: —


### ParseRecordKey (atproto/syntax/recordkey.go:17)


ParseRecordKey is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseRecordKey((RecordKey, error)) (RecordKey, error)
```


**Тип ответа:** RecordKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `RecordKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/recordkey.go:17`



---


[function] name: String file: atproto/syntax/recordkey.go:33 returns_error: нет description: —


### String (atproto/syntax/recordkey.go:33)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (r RecordKey) String(()) ()
```


📍 *Расположение:* `atproto/syntax/recordkey.go:33`



---


[function] name: UnmarshalText file: atproto/syntax/recordkey.go:41 returns_error: нет description: —


### UnmarshalText (atproto/syntax/recordkey.go:41)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (r *RecordKey) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/recordkey.go:41`




## atproto/syntax/tid.go


📄 Исходный файл: `atproto/syntax/tid.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [Base32Sort](#base32sort-atprotosyntaxtidgo16) `:16`

- 🔗 [ClockFromTID](#clockfromtid-atprotosyntaxtidgo132) `:132`

- 🔗 [ClockID](#clockid-atprotosyntaxtidgo95) `:95`

- 🔗 [Integer](#integer-atprotosyntaxtidgo71) `:71`

- 🔗 [MarshalText](#marshaltext-atprotosyntaxtidgo104) `:104`

- 🔗 [NewTID](#newtid-atprotosyntaxtidgo60) `:60`

- 🔗 [NewTIDClock](#newtidclock-atprotosyntaxtidgo126) `:126`

- 🔗 [NewTIDFromInteger](#newtidfrominteger-atprotosyntaxtidgo49) `:49`

- 🔗 [NewTIDFromTime](#newtidfromtime-atprotosyntaxtidgo66) `:66`

- 🔗 [NewTIDNow](#newtidnow-atprotosyntaxtidgo45) `:45`

- 🔗 [Next](#next-atprotosyntaxtidgo141) `:141`

- 🔗 [ParseTID](#parsetid-atprotosyntaxtidgo29) `:29`

- 🔗 [String](#string-atprotosyntaxtidgo100) `:100`

- 🔗 [Time](#time-atprotosyntaxtidgo88) `:88`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxtidgo108) `:108`


</details>


[function] name: Base32Sort file: atproto/syntax/tid.go:16 returns_error: нет description: —


### Base32Sort (atproto/syntax/tid.go:16)


Base32Sort is a function that performs operations based on the provided parameters and returns ().


```go
func Base32Sort(()) ()
```


📍 *Расположение:* `atproto/syntax/tid.go:16`



---


[function] name: ClockFromTID file: atproto/syntax/tid.go:132 returns_error: нет description: —


### ClockFromTID (atproto/syntax/tid.go:132)


ClockFromTID is a function that performs operations based on the provided parameters and returns (t TID).


```go
func ClockFromTID((t TID)) (t TID)
```


**Тип ответа:** t


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** TID


```json
{
  "ClockID": 0,
  "mtx": {},
  "lastUnixMicro": 0
}
```


*Определено в:* `atproto/syntax/tid.go`


📍 *Расположение:* `atproto/syntax/tid.go:132`



---


[function] name: ClockID file: atproto/syntax/tid.go:95 returns_error: нет description: Returns the clock ID part of this TID, as an unsigned integer


### ClockID (atproto/syntax/tid.go:95)


Returns the clock ID part of this TID, as an unsigned integer


```go
func (t TID) ClockID(()) ()
```


📍 *Расположение:* `atproto/syntax/tid.go:95`



---


[function] name: Integer file: atproto/syntax/tid.go:71 returns_error: нет description: Returns full integer representation of this TID (not used often)


### Integer (atproto/syntax/tid.go:71)


Returns full integer representation of this TID (not used often)


```go
func (t TID) Integer(()) ()
```


📍 *Расположение:* `atproto/syntax/tid.go:71`



---


[function] name: MarshalText file: atproto/syntax/tid.go:104 returns_error: да description: —


### MarshalText (atproto/syntax/tid.go:104)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (t TID) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/tid.go:104`



---


[function] name: NewTID file: atproto/syntax/tid.go:60 returns_error: нет description: Constructs a new TID from a UNIX timestamp (in milliseconds) and clock ID value.


### NewTID (atproto/syntax/tid.go:60)


Constructs a new TID from a UNIX timestamp (in milliseconds) and clock ID value.


```go
func NewTID((unixMicros int64, clockId uint)) (unixMicros int64, clockId uint)
```


**Тип ответа:** unixMicros


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clockId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/syntax/tid.go:60`



---


[function] name: NewTIDClock file: atproto/syntax/tid.go:126 returns_error: нет description: —


### NewTIDClock (atproto/syntax/tid.go:126)


NewTIDClock is a function that performs operations based on the provided parameters and returns (clockId uint).


```go
func NewTIDClock((clockId uint)) (clockId uint)
```


**Тип ответа:** clockId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/syntax/tid.go:126`



---


[function] name: NewTIDFromInteger file: atproto/syntax/tid.go:49 returns_error: нет description: —


### NewTIDFromInteger (atproto/syntax/tid.go:49)


NewTIDFromInteger is a function that performs operations based on the provided parameters and returns (v uint64).


```go
func NewTIDFromInteger((v uint64)) (v uint64)
```


**Тип ответа:** v


```json
{
  "escli": null,
  "postIndex": "string",
  "profileIndex": "string",
  "dir": {},
  "echo": null,
  "logger": null,
  "Indexer": null
}
```


*Определено в:* `search/server.go`


📍 *Расположение:* `atproto/syntax/tid.go:49`



---


[function] name: NewTIDFromTime file: atproto/syntax/tid.go:66 returns_error: нет description: Constructs a new TID from a [time.Time] and clock ID value


### NewTIDFromTime (atproto/syntax/tid.go:66)


Constructs a new TID from a [time.Time] and clock ID value


```go
func NewTIDFromTime((ts time.Time, clockId uint)) (ts time.Time, clockId uint)
```


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


**Тип ответа:** time.Time


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Тип ответа:** clockId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/syntax/tid.go:66`



---


[function] name: NewTIDNow file: atproto/syntax/tid.go:45 returns_error: нет description: Naive (unsafe) one-off TID generation with the current time.

You should usually use a [TIDClock] to ensure monotonic ou


### NewTIDNow (atproto/syntax/tid.go:45)


Naive (unsafe) one-off TID generation with the current time.

You should usually use a [TIDClock] to ensure monotonic output.


```go
func NewTIDNow((clockId uint)) (clockId uint)
```


**Тип ответа:** clockId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/syntax/tid.go:45`



---


[function] name: Next file: atproto/syntax/tid.go:141 returns_error: нет description: —


### Next (atproto/syntax/tid.go:141)


Next is a method that performs operations based on the provided parameters and returns ().


```go
func (c *TIDClock) Next(()) ()
```


📍 *Расположение:* `atproto/syntax/tid.go:141`



---


[function] name: ParseTID file: atproto/syntax/tid.go:29 returns_error: да description: —


### ParseTID (atproto/syntax/tid.go:29)


ParseTID is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseTID((TID, error)) (TID, error)
```


**Тип ответа:** TID


```json
{
  "ClockID": 0,
  "mtx": {},
  "lastUnixMicro": 0
}
```


*Определено в:* `atproto/syntax/tid.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `TID`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/tid.go:29`



---


[function] name: String file: atproto/syntax/tid.go:100 returns_error: нет description: —


### String (atproto/syntax/tid.go:100)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (t TID) String(()) ()
```


📍 *Расположение:* `atproto/syntax/tid.go:100`



---


[function] name: Time file: atproto/syntax/tid.go:88 returns_error: нет description: Returns the golang [time.Time] corresponding to this TID's timestamp.


### Time (atproto/syntax/tid.go:88)


Returns the golang [time.Time] corresponding to this TID's timestamp.


```go
func (t TID) Time(()) ()
```


📍 *Расположение:* `atproto/syntax/tid.go:88`



---


[function] name: UnmarshalText file: atproto/syntax/tid.go:108 returns_error: нет description: —


### UnmarshalText (atproto/syntax/tid.go:108)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (t *TID) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/tid.go:108`




## atproto/syntax/uri.go


📄 Исходный файл: `atproto/syntax/uri.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalText](#marshaltext-atprotosyntaxurigo33) `:33`

- 🔗 [ParseURI](#parseuri-atprotosyntaxurigo15) `:15`

- 🔗 [String](#string-atprotosyntaxurigo29) `:29`

- 🔗 [UnmarshalText](#unmarshaltext-atprotosyntaxurigo37) `:37`


</details>


[function] name: MarshalText file: atproto/syntax/uri.go:33 returns_error: да description: —


### MarshalText (atproto/syntax/uri.go:33)


MarshalText is a method that performs operations based on the provided parameters and may return an error.


```go
func (u URI) MarshalText(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/uri.go:33`



---


[function] name: ParseURI file: atproto/syntax/uri.go:15 returns_error: да description: —


### ParseURI (atproto/syntax/uri.go:15)


ParseURI is a function that performs operations based on the provided parameters and may return an error.


```go
func ParseURI((URI, error)) (URI, error)
```


**Тип ответа:** URI


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `URI`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/syntax/uri.go:15`



---


[function] name: String file: atproto/syntax/uri.go:29 returns_error: нет description: —


### String (atproto/syntax/uri.go:29)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (u URI) String(()) ()
```


📍 *Расположение:* `atproto/syntax/uri.go:29`



---


[function] name: UnmarshalText file: atproto/syntax/uri.go:37 returns_error: нет description: —


### UnmarshalText (atproto/syntax/uri.go:37)


UnmarshalText is a method that performs operations based on the provided parameters and returns (text []byte).


```go
func (u *URI) UnmarshalText((text []byte)) (text []byte)
```


**Тип ответа:** text


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


📍 *Расположение:* `atproto/syntax/uri.go:37`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_repo.md)

- [Следующая директория](automod_cachestore.md)


---

