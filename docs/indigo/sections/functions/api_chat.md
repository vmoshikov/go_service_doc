---
title: "Функции: api/chat"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: api/chat
---


# Функции: api/chat


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_bsky.md)

- [Следующая директория](api_ozone.md)


---


## Меню по файлам


- 📄 [api/chat/actordeclaration.go](#apichatactordeclarationgo)

- 📄 [api/chat/actordeleteAccount.go](#apichatactordeleteaccountgo)

- 📄 [api/chat/actorexportAccountData.go](#apichatactorexportaccountdatago)

- 📄 [api/chat/cbor_gen.go](#apichatcbor_gengo)

- 📄 [api/chat/convoacceptConvo.go](#apichatconvoacceptconvogo)

- 📄 [api/chat/convoaddReaction.go](#apichatconvoaddreactiongo)

- 📄 [api/chat/convodefs.go](#apichatconvodefsgo)

- 📄 [api/chat/convodeleteMessageForSelf.go](#apichatconvodeletemessageforselfgo)

- 📄 [api/chat/convogetConvo.go](#apichatconvogetconvogo)

- 📄 [api/chat/convogetConvoAvailability.go](#apichatconvogetconvoavailabilitygo)

- 📄 [api/chat/convogetConvoForMembers.go](#apichatconvogetconvoformembersgo)

- 📄 [api/chat/convogetLog.go](#apichatconvogetloggo)

- 📄 [api/chat/convogetMessages.go](#apichatconvogetmessagesgo)

- 📄 [api/chat/convoleaveConvo.go](#apichatconvoleaveconvogo)

- 📄 [api/chat/convolistConvos.go](#apichatconvolistconvosgo)

- 📄 [api/chat/convomuteConvo.go](#apichatconvomuteconvogo)

- 📄 [api/chat/convoremoveReaction.go](#apichatconvoremovereactiongo)

- 📄 [api/chat/convosendMessage.go](#apichatconvosendmessagego)

- 📄 [api/chat/convosendMessageBatch.go](#apichatconvosendmessagebatchgo)

- 📄 [api/chat/convounmuteConvo.go](#apichatconvounmuteconvogo)

- 📄 [api/chat/convoupdateAllRead.go](#apichatconvoupdateallreadgo)

- 📄 [api/chat/convoupdateRead.go](#apichatconvoupdatereadgo)

- 📄 [api/chat/moderationgetActorMetadata.go](#apichatmoderationgetactormetadatago)

- 📄 [api/chat/moderationgetMessageContext.go](#apichatmoderationgetmessagecontextgo)

- 📄 [api/chat/moderationupdateActorAccess.go](#apichatmoderationupdateactoraccessgo)


---


## api/chat/actordeclaration.go


📄 Исходный файл: `api/chat/actordeclaration.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apichatactordeclarationgo11) `:11`


</details>


[function] name: init file: api/chat/actordeclaration.go:11 returns_error: нет description: —


### init (api/chat/actordeclaration.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/chat/actordeclaration.go:11`




## api/chat/actordeleteAccount.go


📄 Исходный файл: `api/chat/actordeleteAccount.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorDeleteAccount](#actordeleteaccount-apichatactordeleteaccountgo18) `:18`


</details>


[function] name: ActorDeleteAccount file: api/chat/actordeleteAccount.go:18 returns_error: да description: ActorDeleteAccount calls the XRPC method "chat.bsky.actor.deleteAccount".


### ActorDeleteAccount (api/chat/actordeleteAccount.go:18)


ActorDeleteAccount calls the XRPC method "chat.bsky.actor.deleteAccount".


```go
func ActorDeleteAccount((*ActorDeleteAccount_Output, error)) (*ActorDeleteAccount_Output, error)
```


**Тип запроса:** ActorDeleteAccount_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ActorDeleteAccount_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ActorDeleteAccount_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/actordeleteAccount.go:18`




## api/chat/actorexportAccountData.go


📄 Исходный файл: `api/chat/actorexportAccountData.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorExportAccountData](#actorexportaccountdata-apichatactorexportaccountdatago15) `:15`


</details>


[function] name: ActorExportAccountData file: api/chat/actorexportAccountData.go:15 returns_error: да description: ActorExportAccountData calls the XRPC method "chat.bsky.actor.exportAccountData".


### ActorExportAccountData (api/chat/actorexportAccountData.go:15)


ActorExportAccountData calls the XRPC method "chat.bsky.actor.exportAccountData".


```go
func ActorExportAccountData(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/actorexportAccountData.go:15`




## api/chat/cbor_gen.go


📄 Исходный файл: `api/chat/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apichatcbor_gengo21) `:21`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apichatcbor_gengo77) `:77`


</details>


[function] name: MarshalCBOR file: api/chat/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (api/chat/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *ActorDeclaration) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/chat/cbor_gen.go:21`



---


[function] name: UnmarshalCBOR file: api/chat/cbor_gen.go:77 returns_error: да description: —


### UnmarshalCBOR (api/chat/cbor_gen.go:77)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorDeclaration) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/chat/cbor_gen.go:77`




## api/chat/convoacceptConvo.go


📄 Исходный файл: `api/chat/convoacceptConvo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoAcceptConvo](#convoacceptconvo-apichatconvoacceptconvogo25) `:25`


</details>


[function] name: ConvoAcceptConvo file: api/chat/convoacceptConvo.go:25 returns_error: да description: ConvoAcceptConvo calls the XRPC method "chat.bsky.convo.acceptConvo".


### ConvoAcceptConvo (api/chat/convoacceptConvo.go:25)


ConvoAcceptConvo calls the XRPC method "chat.bsky.convo.acceptConvo".


```go
func ConvoAcceptConvo((*ConvoAcceptConvo_Output, error)) (*ConvoAcceptConvo_Output, error)
```


**Тип запроса:** ConvoAcceptConvo_Output


```json
{
  "rev": "string"
}
```


*Определено в:* `api/chat/convoacceptConvo.go`


**Тип ответа:** ConvoAcceptConvo_Output


```json
{
  "rev": "string"
}
```


*Определено в:* `api/chat/convoacceptConvo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoAcceptConvo_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convoacceptConvo.go:25`




## api/chat/convoaddReaction.go


📄 Исходный файл: `api/chat/convoaddReaction.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoAddReaction](#convoaddreaction-apichatconvoaddreactiongo26) `:26`


</details>


[function] name: ConvoAddReaction file: api/chat/convoaddReaction.go:26 returns_error: да description: ConvoAddReaction calls the XRPC method "chat.bsky.convo.addReaction".


### ConvoAddReaction (api/chat/convoaddReaction.go:26)


ConvoAddReaction calls the XRPC method "chat.bsky.convo.addReaction".


```go
func ConvoAddReaction((*ConvoAddReaction_Output, error)) (*ConvoAddReaction_Output, error)
```


**Тип запроса:** ConvoAddReaction_Output


```json
{
  "message": null
}
```


*Определено в:* `api/chat/convoaddReaction.go`


**Тип ответа:** ConvoAddReaction_Output


```json
{
  "message": null
}
```


*Определено в:* `api/chat/convoaddReaction.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoAddReaction_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convoaddReaction.go:26`




## api/chat/convodefs.go


📄 Исходный файл: `api/chat/convodefs.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo32) `:32`

- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo66) `:66`

- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo119) `:119`

- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo169) `:169`

- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo212) `:212`

- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo269) `:269`

- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo313) `:313`

- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo369) `:369`

- 🔗 [MarshalJSON](#marshaljson-apichatconvodefsgo424) `:424`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo44) `:44`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo74) `:74`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo131) `:131`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo181) `:181`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo224) `:224`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo281) `:281`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo325) `:325`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo377) `:377`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvodefsgo432) `:432`


</details>


[function] name: MarshalJSON file: api/chat/convodefs.go:32 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:32)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_ConvoView_LastMessage) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:32`



---


[function] name: MarshalJSON file: api/chat/convodefs.go:66 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:66)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_ConvoView_LastReaction) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:66`



---


[function] name: MarshalJSON file: api/chat/convodefs.go:119 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:119)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_LogAddReaction_Message) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:119`



---


[function] name: MarshalJSON file: api/chat/convodefs.go:169 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:169)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_LogCreateMessage_Message) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:169`



---


[function] name: MarshalJSON file: api/chat/convodefs.go:212 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:212)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_LogDeleteMessage_Message) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:212`



---


[function] name: MarshalJSON file: api/chat/convodefs.go:269 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:269)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_LogReadMessage_Message) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:269`



---


[function] name: MarshalJSON file: api/chat/convodefs.go:313 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:313)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_LogRemoveReaction_Message) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:313`



---


[function] name: MarshalJSON file: api/chat/convodefs.go:369 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:369)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_MessageInput_Embed) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:369`



---


[function] name: MarshalJSON file: api/chat/convodefs.go:424 returns_error: да description: —


### MarshalJSON (api/chat/convodefs.go:424)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoDefs_MessageView_Embed) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodefs.go:424`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:44 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:44)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_ConvoView_LastMessage) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:44`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:74 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:74)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_ConvoView_LastReaction) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:74`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:131 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:131)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_LogAddReaction_Message) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:131`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:181 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:181)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_LogCreateMessage_Message) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:181`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:224 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:224)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_LogDeleteMessage_Message) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:224`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:281 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:281)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_LogReadMessage_Message) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:281`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:325 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:325)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_LogRemoveReaction_Message) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:325`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:377 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:377)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_MessageInput_Embed) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:377`



---


[function] name: UnmarshalJSON file: api/chat/convodefs.go:432 returns_error: нет description: —


### UnmarshalJSON (api/chat/convodefs.go:432)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoDefs_MessageView_Embed) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convodefs.go:432`




## api/chat/convodeleteMessageForSelf.go


📄 Исходный файл: `api/chat/convodeleteMessageForSelf.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoDeleteMessageForSelf](#convodeletemessageforself-apichatconvodeletemessageforselfgo20) `:20`


</details>


[function] name: ConvoDeleteMessageForSelf file: api/chat/convodeleteMessageForSelf.go:20 returns_error: да description: ConvoDeleteMessageForSelf calls the XRPC method "chat.bsky.convo.deleteMessageForSelf".


### ConvoDeleteMessageForSelf (api/chat/convodeleteMessageForSelf.go:20)


ConvoDeleteMessageForSelf calls the XRPC method "chat.bsky.convo.deleteMessageForSelf".


```go
func ConvoDeleteMessageForSelf((*ConvoDefs_DeletedMessageView, error)) (*ConvoDefs_DeletedMessageView, error)
```


**Тип запроса:** ConvoDefs_DeletedMessageView


```json
{
  "$type": "string",
  "id": "string",
  "rev": "string",
  "sender": null,
  "sentAt": "string"
}
```


*Определено в:* `api/chat/convodefs.go`


**Тип ответа:** ConvoDefs_DeletedMessageView


```json
{
  "$type": "string",
  "id": "string",
  "rev": "string",
  "sender": null,
  "sentAt": "string"
}
```


*Определено в:* `api/chat/convodefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoDefs_DeletedMessageView`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convodeleteMessageForSelf.go:20`




## api/chat/convogetConvo.go


📄 Исходный файл: `api/chat/convogetConvo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoGetConvo](#convogetconvo-apichatconvogetconvogo19) `:19`


</details>


[function] name: ConvoGetConvo file: api/chat/convogetConvo.go:19 returns_error: да description: ConvoGetConvo calls the XRPC method "chat.bsky.convo.getConvo".


### ConvoGetConvo (api/chat/convogetConvo.go:19)


ConvoGetConvo calls the XRPC method "chat.bsky.convo.getConvo".


```go
func ConvoGetConvo((*ConvoGetConvo_Output, error)) (*ConvoGetConvo_Output, error)
```


**Тип запроса:** ConvoGetConvo_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convogetConvo.go`


**Тип ответа:** ConvoGetConvo_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convogetConvo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoGetConvo_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convogetConvo.go:19`




## api/chat/convogetConvoAvailability.go


📄 Исходный файл: `api/chat/convogetConvoAvailability.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoGetConvoAvailability](#convogetconvoavailability-apichatconvogetconvoavailabilitygo20) `:20`


</details>


[function] name: ConvoGetConvoAvailability file: api/chat/convogetConvoAvailability.go:20 returns_error: да description: ConvoGetConvoAvailability calls the XRPC method "chat.bsky.convo.getConvoAvailability".


### ConvoGetConvoAvailability (api/chat/convogetConvoAvailability.go:20)


ConvoGetConvoAvailability calls the XRPC method "chat.bsky.convo.getConvoAvailability".


```go
func ConvoGetConvoAvailability((*ConvoGetConvoAvailability_Output, error)) (*ConvoGetConvoAvailability_Output, error)
```


**Тип запроса:** ConvoGetConvoAvailability_Output


```json
{
  "canChat": false,
  "convo": null
}
```


*Определено в:* `api/chat/convogetConvoAvailability.go`


**Тип ответа:** ConvoGetConvoAvailability_Output


```json
{
  "canChat": false,
  "convo": null
}
```


*Определено в:* `api/chat/convogetConvoAvailability.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoGetConvoAvailability_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convogetConvoAvailability.go:20`




## api/chat/convogetConvoForMembers.go


📄 Исходный файл: `api/chat/convogetConvoForMembers.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoGetConvoForMembers](#convogetconvoformembers-apichatconvogetconvoformembersgo19) `:19`


</details>


[function] name: ConvoGetConvoForMembers file: api/chat/convogetConvoForMembers.go:19 returns_error: да description: ConvoGetConvoForMembers calls the XRPC method "chat.bsky.convo.getConvoForMembers".


### ConvoGetConvoForMembers (api/chat/convogetConvoForMembers.go:19)


ConvoGetConvoForMembers calls the XRPC method "chat.bsky.convo.getConvoForMembers".


```go
func ConvoGetConvoForMembers((*ConvoGetConvoForMembers_Output, error)) (*ConvoGetConvoForMembers_Output, error)
```


**Тип запроса:** ConvoGetConvoForMembers_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convogetConvoForMembers.go`


**Тип ответа:** ConvoGetConvoForMembers_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convogetConvoForMembers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoGetConvoForMembers_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convogetConvoForMembers.go:19`




## api/chat/convogetLog.go


📄 Исходный файл: `api/chat/convogetLog.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [ConvoGetLog](#convogetlog-apichatconvogetloggo121) `:121`

- 🔗 [MarshalJSON](#marshaljson-apichatconvogetloggo34) `:34`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvogetloggo78) `:78`


</details>


[function] name: ConvoGetLog file: api/chat/convogetLog.go:121 returns_error: да description: ConvoGetLog calls the XRPC method "chat.bsky.convo.getLog".


### ConvoGetLog (api/chat/convogetLog.go:121)


ConvoGetLog calls the XRPC method "chat.bsky.convo.getLog".


```go
func ConvoGetLog((*ConvoGetLog_Output, error)) (*ConvoGetLog_Output, error)
```


**Тип запроса:** ConvoGetLog_Output


```json
{
  "cursor": "string",
  "logs": []
}
```


*Определено в:* `api/chat/convogetLog.go`


**Тип ответа:** ConvoGetLog_Output


```json
{
  "cursor": "string",
  "logs": []
}
```


*Определено в:* `api/chat/convogetLog.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoGetLog_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convogetLog.go:121`



---


[function] name: MarshalJSON file: api/chat/convogetLog.go:34 returns_error: да description: —


### MarshalJSON (api/chat/convogetLog.go:34)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoGetLog_Output_Logs_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convogetLog.go:34`



---


[function] name: UnmarshalJSON file: api/chat/convogetLog.go:78 returns_error: нет description: —


### UnmarshalJSON (api/chat/convogetLog.go:78)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoGetLog_Output_Logs_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convogetLog.go:78`




## api/chat/convogetMessages.go


📄 Исходный файл: `api/chat/convogetMessages.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [ConvoGetMessages](#convogetmessages-apichatconvogetmessagesgo57) `:57`

- 🔗 [MarshalJSON](#marshaljson-apichatconvogetmessagesgo26) `:26`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatconvogetmessagesgo38) `:38`


</details>


[function] name: ConvoGetMessages file: api/chat/convogetMessages.go:57 returns_error: да description: ConvoGetMessages calls the XRPC method "chat.bsky.convo.getMessages".


### ConvoGetMessages (api/chat/convogetMessages.go:57)


ConvoGetMessages calls the XRPC method "chat.bsky.convo.getMessages".


```go
func ConvoGetMessages((*ConvoGetMessages_Output, error)) (*ConvoGetMessages_Output, error)
```


**Тип запроса:** ConvoGetMessages_Output


```json
{
  "cursor": "string",
  "messages": []
}
```


*Определено в:* `api/chat/convogetMessages.go`


**Тип ответа:** ConvoGetMessages_Output


```json
{
  "cursor": "string",
  "messages": []
}
```


*Определено в:* `api/chat/convogetMessages.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoGetMessages_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convogetMessages.go:57`



---


[function] name: MarshalJSON file: api/chat/convogetMessages.go:26 returns_error: да description: —


### MarshalJSON (api/chat/convogetMessages.go:26)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ConvoGetMessages_Output_Messages_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convogetMessages.go:26`



---


[function] name: UnmarshalJSON file: api/chat/convogetMessages.go:38 returns_error: нет description: —


### UnmarshalJSON (api/chat/convogetMessages.go:38)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ConvoGetMessages_Output_Messages_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/convogetMessages.go:38`




## api/chat/convoleaveConvo.go


📄 Исходный файл: `api/chat/convoleaveConvo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoLeaveConvo](#convoleaveconvo-apichatconvoleaveconvogo25) `:25`


</details>


[function] name: ConvoLeaveConvo file: api/chat/convoleaveConvo.go:25 returns_error: да description: ConvoLeaveConvo calls the XRPC method "chat.bsky.convo.leaveConvo".


### ConvoLeaveConvo (api/chat/convoleaveConvo.go:25)


ConvoLeaveConvo calls the XRPC method "chat.bsky.convo.leaveConvo".


```go
func ConvoLeaveConvo((*ConvoLeaveConvo_Output, error)) (*ConvoLeaveConvo_Output, error)
```


**Тип запроса:** ConvoLeaveConvo_Output


```json
{
  "convoId": "string",
  "rev": "string"
}
```


*Определено в:* `api/chat/convoleaveConvo.go`


**Тип ответа:** ConvoLeaveConvo_Output


```json
{
  "convoId": "string",
  "rev": "string"
}
```


*Определено в:* `api/chat/convoleaveConvo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoLeaveConvo_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convoleaveConvo.go:25`




## api/chat/convolistConvos.go


📄 Исходный файл: `api/chat/convolistConvos.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoListConvos](#convolistconvos-apichatconvolistconvosgo20) `:20`


</details>


[function] name: ConvoListConvos file: api/chat/convolistConvos.go:20 returns_error: да description: ConvoListConvos calls the XRPC method "chat.bsky.convo.listConvos".


### ConvoListConvos (api/chat/convolistConvos.go:20)


ConvoListConvos calls the XRPC method "chat.bsky.convo.listConvos".


```go
func ConvoListConvos((*ConvoListConvos_Output, error)) (*ConvoListConvos_Output, error)
```


**Тип запроса:** ConvoListConvos_Output


```json
{
  "convos": [],
  "cursor": "string"
}
```


*Определено в:* `api/chat/convolistConvos.go`


**Тип ответа:** ConvoListConvos_Output


```json
{
  "convos": [],
  "cursor": "string"
}
```


*Определено в:* `api/chat/convolistConvos.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoListConvos_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convolistConvos.go:20`




## api/chat/convomuteConvo.go


📄 Исходный файл: `api/chat/convomuteConvo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoMuteConvo](#convomuteconvo-apichatconvomuteconvogo24) `:24`


</details>


[function] name: ConvoMuteConvo file: api/chat/convomuteConvo.go:24 returns_error: да description: ConvoMuteConvo calls the XRPC method "chat.bsky.convo.muteConvo".


### ConvoMuteConvo (api/chat/convomuteConvo.go:24)


ConvoMuteConvo calls the XRPC method "chat.bsky.convo.muteConvo".


```go
func ConvoMuteConvo((*ConvoMuteConvo_Output, error)) (*ConvoMuteConvo_Output, error)
```


**Тип запроса:** ConvoMuteConvo_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convomuteConvo.go`


**Тип ответа:** ConvoMuteConvo_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convomuteConvo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoMuteConvo_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convomuteConvo.go:24`




## api/chat/convoremoveReaction.go


📄 Исходный файл: `api/chat/convoremoveReaction.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoRemoveReaction](#convoremovereaction-apichatconvoremovereactiongo26) `:26`


</details>


[function] name: ConvoRemoveReaction file: api/chat/convoremoveReaction.go:26 returns_error: да description: ConvoRemoveReaction calls the XRPC method "chat.bsky.convo.removeReaction".


### ConvoRemoveReaction (api/chat/convoremoveReaction.go:26)


ConvoRemoveReaction calls the XRPC method "chat.bsky.convo.removeReaction".


```go
func ConvoRemoveReaction((*ConvoRemoveReaction_Output, error)) (*ConvoRemoveReaction_Output, error)
```


**Тип запроса:** ConvoRemoveReaction_Output


```json
{
  "message": null
}
```


*Определено в:* `api/chat/convoremoveReaction.go`


**Тип ответа:** ConvoRemoveReaction_Output


```json
{
  "message": null
}
```


*Определено в:* `api/chat/convoremoveReaction.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoRemoveReaction_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convoremoveReaction.go:26`




## api/chat/convosendMessage.go


📄 Исходный файл: `api/chat/convosendMessage.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoSendMessage](#convosendmessage-apichatconvosendmessagego20) `:20`


</details>


[function] name: ConvoSendMessage file: api/chat/convosendMessage.go:20 returns_error: да description: ConvoSendMessage calls the XRPC method "chat.bsky.convo.sendMessage".


### ConvoSendMessage (api/chat/convosendMessage.go:20)


ConvoSendMessage calls the XRPC method "chat.bsky.convo.sendMessage".


```go
func ConvoSendMessage((*ConvoDefs_MessageView, error)) (*ConvoDefs_MessageView, error)
```


**Тип запроса:** ConvoDefs_MessageView


```json
{
  "$type": "string",
  "embed": null,
  "facets": [],
  "id": "string",
  "reactions": [],
  "rev": "string",
  "sender": null,
  "sentAt": "string",
  "text": "string"
}
```


*Определено в:* `api/chat/convodefs.go`


**Тип ответа:** ConvoDefs_MessageView


```json
{
  "$type": "string",
  "embed": null,
  "facets": [],
  "id": "string",
  "reactions": [],
  "rev": "string",
  "sender": null,
  "sentAt": "string",
  "text": "string"
}
```


*Определено в:* `api/chat/convodefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoDefs_MessageView`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convosendMessage.go:20`




## api/chat/convosendMessageBatch.go


📄 Исходный файл: `api/chat/convosendMessageBatch.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoSendMessageBatch](#convosendmessagebatch-apichatconvosendmessagebatchgo30) `:30`


</details>


[function] name: ConvoSendMessageBatch file: api/chat/convosendMessageBatch.go:30 returns_error: да description: ConvoSendMessageBatch calls the XRPC method "chat.bsky.convo.sendMessageBatch".


### ConvoSendMessageBatch (api/chat/convosendMessageBatch.go:30)


ConvoSendMessageBatch calls the XRPC method "chat.bsky.convo.sendMessageBatch".


```go
func ConvoSendMessageBatch((*ConvoSendMessageBatch_Output, error)) (*ConvoSendMessageBatch_Output, error)
```


**Тип запроса:** ConvoSendMessageBatch_Output


```json
{
  "items": []
}
```


*Определено в:* `api/chat/convosendMessageBatch.go`


**Тип ответа:** ConvoSendMessageBatch_Output


```json
{
  "items": []
}
```


*Определено в:* `api/chat/convosendMessageBatch.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoSendMessageBatch_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convosendMessageBatch.go:30`




## api/chat/convounmuteConvo.go


📄 Исходный файл: `api/chat/convounmuteConvo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoUnmuteConvo](#convounmuteconvo-apichatconvounmuteconvogo24) `:24`


</details>


[function] name: ConvoUnmuteConvo file: api/chat/convounmuteConvo.go:24 returns_error: да description: ConvoUnmuteConvo calls the XRPC method "chat.bsky.convo.unmuteConvo".


### ConvoUnmuteConvo (api/chat/convounmuteConvo.go:24)


ConvoUnmuteConvo calls the XRPC method "chat.bsky.convo.unmuteConvo".


```go
func ConvoUnmuteConvo((*ConvoUnmuteConvo_Output, error)) (*ConvoUnmuteConvo_Output, error)
```


**Тип запроса:** ConvoUnmuteConvo_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convounmuteConvo.go`


**Тип ответа:** ConvoUnmuteConvo_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convounmuteConvo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoUnmuteConvo_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convounmuteConvo.go:24`




## api/chat/convoupdateAllRead.go


📄 Исходный файл: `api/chat/convoupdateAllRead.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoUpdateAllRead](#convoupdateallread-apichatconvoupdateallreadgo25) `:25`


</details>


[function] name: ConvoUpdateAllRead file: api/chat/convoupdateAllRead.go:25 returns_error: да description: ConvoUpdateAllRead calls the XRPC method "chat.bsky.convo.updateAllRead".


### ConvoUpdateAllRead (api/chat/convoupdateAllRead.go:25)


ConvoUpdateAllRead calls the XRPC method "chat.bsky.convo.updateAllRead".


```go
func ConvoUpdateAllRead((*ConvoUpdateAllRead_Output, error)) (*ConvoUpdateAllRead_Output, error)
```


**Тип запроса:** ConvoUpdateAllRead_Output


```json
{
  "updatedCount": 0
}
```


*Определено в:* `api/chat/convoupdateAllRead.go`


**Тип ответа:** ConvoUpdateAllRead_Output


```json
{
  "updatedCount": 0
}
```


*Определено в:* `api/chat/convoupdateAllRead.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoUpdateAllRead_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convoupdateAllRead.go:25`




## api/chat/convoupdateRead.go


📄 Исходный файл: `api/chat/convoupdateRead.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvoUpdateRead](#convoupdateread-apichatconvoupdatereadgo25) `:25`


</details>


[function] name: ConvoUpdateRead file: api/chat/convoupdateRead.go:25 returns_error: да description: ConvoUpdateRead calls the XRPC method "chat.bsky.convo.updateRead".


### ConvoUpdateRead (api/chat/convoupdateRead.go:25)


ConvoUpdateRead calls the XRPC method "chat.bsky.convo.updateRead".


```go
func ConvoUpdateRead((*ConvoUpdateRead_Output, error)) (*ConvoUpdateRead_Output, error)
```


**Тип запроса:** ConvoUpdateRead_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convoupdateRead.go`


**Тип ответа:** ConvoUpdateRead_Output


```json
{
  "convo": null
}
```


*Определено в:* `api/chat/convoupdateRead.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ConvoUpdateRead_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/convoupdateRead.go:25`




## api/chat/moderationgetActorMetadata.go


📄 Исходный файл: `api/chat/moderationgetActorMetadata.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationGetActorMetadata](#moderationgetactormetadata-apichatmoderationgetactormetadatago29) `:29`


</details>


[function] name: ModerationGetActorMetadata file: api/chat/moderationgetActorMetadata.go:29 returns_error: да description: ModerationGetActorMetadata calls the XRPC method "chat.bsky.moderation.getActorMetadata".


### ModerationGetActorMetadata (api/chat/moderationgetActorMetadata.go:29)


ModerationGetActorMetadata calls the XRPC method "chat.bsky.moderation.getActorMetadata".


```go
func ModerationGetActorMetadata((*ModerationGetActorMetadata_Output, error)) (*ModerationGetActorMetadata_Output, error)
```


**Тип запроса:** ModerationGetActorMetadata_Output


```json
{
  "all": null,
  "day": null,
  "month": null
}
```


*Определено в:* `api/chat/moderationgetActorMetadata.go`


**Тип ответа:** ModerationGetActorMetadata_Output


```json
{
  "all": null,
  "day": null,
  "month": null
}
```


*Определено в:* `api/chat/moderationgetActorMetadata.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationGetActorMetadata_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/moderationgetActorMetadata.go:29`




## api/chat/moderationgetMessageContext.go


📄 Исходный файл: `api/chat/moderationgetMessageContext.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apichatmoderationgetmessagecontextgo25) `:25`

- 🔗 [ModerationGetMessageContext](#moderationgetmessagecontext-apichatmoderationgetmessagecontextgo58) `:58`

- 🔗 [UnmarshalJSON](#unmarshaljson-apichatmoderationgetmessagecontextgo37) `:37`


</details>


[function] name: MarshalJSON file: api/chat/moderationgetMessageContext.go:25 returns_error: да description: —


### MarshalJSON (api/chat/moderationgetMessageContext.go:25)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationGetMessageContext_Output_Messages_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/moderationgetMessageContext.go:25`



---


[function] name: ModerationGetMessageContext file: api/chat/moderationgetMessageContext.go:58 returns_error: да description: ModerationGetMessageContext calls the XRPC method "chat.bsky.moderation.getMessageContext".

convoId: Conversation that 


### ModerationGetMessageContext (api/chat/moderationgetMessageContext.go:58)


ModerationGetMessageContext calls the XRPC method "chat.bsky.moderation.getMessageContext".

convoId: Conversation that the message is from. NOTE: this field will eventually be required.


```go
func ModerationGetMessageContext((*ModerationGetMessageContext_Output, error)) (*ModerationGetMessageContext_Output, error)
```


**Тип запроса:** ModerationGetMessageContext_Output


```json
{
  "messages": []
}
```


*Определено в:* `api/chat/moderationgetMessageContext.go`


**Тип ответа:** ModerationGetMessageContext_Output


```json
{
  "messages": []
}
```


*Определено в:* `api/chat/moderationgetMessageContext.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationGetMessageContext_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/chat/moderationgetMessageContext.go:58`



---


[function] name: UnmarshalJSON file: api/chat/moderationgetMessageContext.go:37 returns_error: нет description: —


### UnmarshalJSON (api/chat/moderationgetMessageContext.go:37)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationGetMessageContext_Output_Messages_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/chat/moderationgetMessageContext.go:37`




## api/chat/moderationupdateActorAccess.go


📄 Исходный файл: `api/chat/moderationupdateActorAccess.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationUpdateActorAccess](#moderationupdateactoraccess-apichatmoderationupdateactoraccessgo21) `:21`


</details>


[function] name: ModerationUpdateActorAccess file: api/chat/moderationupdateActorAccess.go:21 returns_error: нет description: ModerationUpdateActorAccess calls the XRPC method "chat.bsky.moderation.updateActorAccess".


### ModerationUpdateActorAccess (api/chat/moderationupdateActorAccess.go:21)


ModerationUpdateActorAccess calls the XRPC method "chat.bsky.moderation.updateActorAccess".


```go
func ModerationUpdateActorAccess((ctx context.Context, c lexutil.LexClient, input *ModerationUpdateActorAccess_Input)) (ctx context.Context, c lexutil.LexClient, input *ModerationUpdateActorAccess_Input)
```


**Тип запроса:** ModerationUpdateActorAccess_Input


```json
{
  "actor": "string",
  "allowAccess": false,
  "ref": "string"
}
```


*Определено в:* `api/chat/moderationupdateActorAccess.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ModerationUpdateActorAccess_Input


```json
{
  "actor": "string",
  "allowAccess": false,
  "ref": "string"
}
```


*Определено в:* `api/chat/moderationupdateActorAccess.go`


📍 *Расположение:* `api/chat/moderationupdateActorAccess.go:21`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_bsky.md)

- [Следующая директория](api_ozone.md)


---

