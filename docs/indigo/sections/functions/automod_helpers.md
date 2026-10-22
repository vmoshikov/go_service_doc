---
title: "Функции: automod/helpers"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/helpers
---


# Функции: automod/helpers


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_flagstore.md)

- [Следующая директория](automod_keyword.md)


---


## Меню по файлам


- 📄 [automod/helpers/account.go](#automodhelpersaccountgo)

- 📄 [automod/helpers/bsky.go](#automodhelpersbskygo)

- 📄 [automod/helpers/text.go](#automodhelperstextgo)


---


## automod/helpers/account.go


📄 Исходный файл: `automod/helpers/account.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AccountIsOlderThan](#accountisolderthan-automodhelpersaccountgo41) `:41`

- 🔗 [AccountIsYoungerThan](#accountisyoungerthan-automodhelpersaccountgo29) `:29`

- 🔗 [plausibleAccountCreation](#plausibleaccountcreation-automodhelpersaccountgo13) `:13`


</details>


[function] name: AccountIsOlderThan file: automod/helpers/account.go:41 returns_error: нет description: checks if account was *not* created recently, based on either public or private account metadata. if metadata isn't avai


### AccountIsOlderThan (automod/helpers/account.go:41)


checks if account was *not* created recently, based on either public or private account metadata. if metadata isn't available at all, or seems bogus, returns 'false'


```go
func AccountIsOlderThan((c *automod.AccountContext, age time.Duration)) (c *automod.AccountContext, age time.Duration)
```


**Тип запроса:** automod.AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


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


**Тип ответа:** automod.AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** age


```json
{
  "cs": {},
  "kmgr": {},
  "lklk": {},
  "userLocks": {},
  "events": {},
  "hydrateRecords": false,
  "log": null,
  "noArchive": false,
  "clk": null
}
```


*Определено в:* `repomgr/repomgr.go`


**Тип ответа:** time.Duration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/helpers/account.go:41`



---


[function] name: AccountIsYoungerThan file: automod/helpers/account.go:29 returns_error: нет description: checks if account was created recently, based on either public or private account metadata. if metadata isn't available 


### AccountIsYoungerThan (automod/helpers/account.go:29)


checks if account was created recently, based on either public or private account metadata. if metadata isn't available at all, or seems bogus, returns 'false'


```go
func AccountIsYoungerThan((c *automod.AccountContext, age time.Duration)) (c *automod.AccountContext, age time.Duration)
```


**Тип запроса:** automod.AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


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


**Тип ответа:** automod.AccountContext


```json
{
  "Index": 0,
  "AccountType": "string",
  "Email": "string",
  "Password": "string",
  "Auth": {}
}
```


*Определено в:* `fakedata/accounts.go`


**Тип ответа:** age


```json
{
  "cs": {},
  "kmgr": {},
  "lklk": {},
  "userLocks": {},
  "events": {},
  "hydrateRecords": false,
  "log": null,
  "noArchive": false,
  "clk": null
}
```


*Определено в:* `repomgr/repomgr.go`


**Тип ответа:** time.Duration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/helpers/account.go:29`



---


[function] name: plausibleAccountCreation file: automod/helpers/account.go:13 returns_error: нет description: returns true if account creation timestamp is plausible: not-nil, not in distant past, not in the future


### plausibleAccountCreation (automod/helpers/account.go:13)


returns true if account creation timestamp is plausible: not-nil, not in distant past, not in the future


```go
func plausibleAccountCreation((when *time.Time)) (when *time.Time)
```


**Тип запроса:** time.Time


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


**Тип ответа:** when


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Time


```json
{
  "Collection": "string",
  "Did": "string",
  "UnixMillis": 0
}
```


*Определено в:* `cmd/collectiondir/pebble.go`


📍 *Расположение:* `automod/helpers/account.go:13`




## automod/helpers/bsky.go


📄 Исходный файл: `automod/helpers/bsky.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [ExtractBlobCIDsProfile](#extractblobcidsprofile-automodhelpersbskygo91) `:91`

- 🔗 [ExtractFacets](#extractfacets-automodhelpersbskygo36) `:36`

- 🔗 [ExtractHashtagsPost](#extracthashtagspost-automodhelpersbskygo12) `:12`

- 🔗 [ExtractPostBlobCIDsPost](#extractpostblobcidspost-automodhelpersbskygo73) `:73`

- 🔗 [ExtractTextTokensPost](#extracttexttokenspost-automodhelpersbskygo102) `:102`

- 🔗 [ExtractTextTokensProfile](#extracttexttokensprofile-automodhelpersbskygo126) `:126`

- 🔗 [ExtractTextURLsProfile](#extracttexturlsprofile-automodhelpersbskygo137) `:137`

- 🔗 [IsSelfThread](#isselfthread-automodhelpersbskygo149) `:149`

- 🔗 [NormalizeHashtag](#normalizehashtag-automodhelpersbskygo25) `:25`

- 🔗 [ParentOrRootIsFollower](#parentorrootisfollower-automodhelpersbskygo169) `:169`

- 🔗 [PostMentionsAnyDid](#postmentionsanydid-automodhelpersbskygo259) `:259`

- 🔗 [PostMentionsDid](#postmentionsdid-automodhelpersbskygo244) `:244`

- 🔗 [PostParentOrRootIsAnyDid](#postparentorrootisanydid-automodhelpersbskygo230) `:230`

- 🔗 [PostParentOrRootIsDid](#postparentorrootisdid-automodhelpersbskygo212) `:212`


</details>


[function] name: ExtractBlobCIDsProfile file: automod/helpers/bsky.go:91 returns_error: нет description: —


### ExtractBlobCIDsProfile (automod/helpers/bsky.go:91)


ExtractBlobCIDsProfile is a function that performs operations based on the provided parameters and returns (profile *appbsky.ActorProfile).


```go
func ExtractBlobCIDsProfile((profile *appbsky.ActorProfile)) (profile *appbsky.ActorProfile)
```


**Тип запроса:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


**Тип ответа:** profile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


📍 *Расположение:* `automod/helpers/bsky.go:91`



---


[function] name: ExtractFacets file: automod/helpers/bsky.go:36 returns_error: да description: —


### ExtractFacets (automod/helpers/bsky.go:36)


ExtractFacets is a function that performs operations based on the provided parameters and may return an error.


```go
func ExtractFacets(([]PostFacet, error)) ([]PostFacet, error)
```


**Тип ответа:** PostFacet


```json
{
  "Text": "string",
  "URL": "string",
  "DID": "string",
  "Tag": "string"
}
```


*Определено в:* `automod/helpers/bsky.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]PostFacet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/helpers/bsky.go:36`



---


[function] name: ExtractHashtagsPost file: automod/helpers/bsky.go:12 returns_error: нет description: —


### ExtractHashtagsPost (automod/helpers/bsky.go:12)


ExtractHashtagsPost is a function that performs operations based on the provided parameters and returns (post *appbsky.FeedPost).


```go
func ExtractHashtagsPost((post *appbsky.FeedPost)) (post *appbsky.FeedPost)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


📍 *Расположение:* `automod/helpers/bsky.go:12`



---


[function] name: ExtractPostBlobCIDsPost file: automod/helpers/bsky.go:73 returns_error: нет description: —


### ExtractPostBlobCIDsPost (automod/helpers/bsky.go:73)


ExtractPostBlobCIDsPost is a function that performs operations based on the provided parameters and returns (post *appbsky.FeedPost).


```go
func ExtractPostBlobCIDsPost((post *appbsky.FeedPost)) (post *appbsky.FeedPost)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


📍 *Расположение:* `automod/helpers/bsky.go:73`



---


[function] name: ExtractTextTokensPost file: automod/helpers/bsky.go:102 returns_error: нет description: —


### ExtractTextTokensPost (automod/helpers/bsky.go:102)


ExtractTextTokensPost is a function that performs operations based on the provided parameters and returns (post *appbsky.FeedPost).


```go
func ExtractTextTokensPost((post *appbsky.FeedPost)) (post *appbsky.FeedPost)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


📍 *Расположение:* `automod/helpers/bsky.go:102`



---


[function] name: ExtractTextTokensProfile file: automod/helpers/bsky.go:126 returns_error: нет description: —


### ExtractTextTokensProfile (automod/helpers/bsky.go:126)


ExtractTextTokensProfile is a function that performs operations based on the provided parameters and returns (profile *appbsky.ActorProfile).


```go
func ExtractTextTokensProfile((profile *appbsky.ActorProfile)) (profile *appbsky.ActorProfile)
```


**Тип запроса:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


**Тип ответа:** profile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


📍 *Расположение:* `automod/helpers/bsky.go:126`



---


[function] name: ExtractTextURLsProfile file: automod/helpers/bsky.go:137 returns_error: нет description: —


### ExtractTextURLsProfile (automod/helpers/bsky.go:137)


ExtractTextURLsProfile is a function that performs operations based on the provided parameters and returns (profile *appbsky.ActorProfile).


```go
func ExtractTextURLsProfile((profile *appbsky.ActorProfile)) (profile *appbsky.ActorProfile)
```


**Тип запроса:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


**Тип ответа:** profile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** appbsky.ActorProfile


```json
{
  "$type": "string",
  "avatar": null,
  "banner": null,
  "createdAt": "string",
  "description": "string",
  "displayName": "string",
  "joinedViaStarterPack": null,
  "labels": null,
  "pinnedPost": null,
  "pronouns": "string",
  "website": "string"
}
```


*Определено в:* `api/bsky/actorprofile.go`


📍 *Расположение:* `automod/helpers/bsky.go:137`



---


[function] name: IsSelfThread file: automod/helpers/bsky.go:149 returns_error: нет description: checks if the post event is a reply post for which the author is replying to themselves, or author is the root author (O


### IsSelfThread (automod/helpers/bsky.go:149)


checks if the post event is a reply post for which the author is replying to themselves, or author is the root author (OP)


```go
func IsSelfThread((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


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


**Тип ответа:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


📍 *Расположение:* `automod/helpers/bsky.go:149`



---


[function] name: NormalizeHashtag file: automod/helpers/bsky.go:25 returns_error: нет description: —


### NormalizeHashtag (automod/helpers/bsky.go:25)


NormalizeHashtag is a function that performs operations based on the provided parameters and returns (raw string).


```go
func NormalizeHashtag((raw string)) (raw string)
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


📍 *Расположение:* `automod/helpers/bsky.go:25`



---


[function] name: ParentOrRootIsFollower file: automod/helpers/bsky.go:169 returns_error: нет description: —


### ParentOrRootIsFollower (automod/helpers/bsky.go:169)


ParentOrRootIsFollower is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func ParentOrRootIsFollower((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


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


**Тип ответа:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


📍 *Расположение:* `automod/helpers/bsky.go:169`



---


[function] name: PostMentionsAnyDid file: automod/helpers/bsky.go:259 returns_error: нет description: —


### PostMentionsAnyDid (automod/helpers/bsky.go:259)


PostMentionsAnyDid is a function that performs operations based on the provided parameters and returns (post *appbsky.FeedPost, dids []string).


```go
func PostMentionsAnyDid((post *appbsky.FeedPost, dids []string)) (post *appbsky.FeedPost, dids []string)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** dids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/helpers/bsky.go:259`



---


[function] name: PostMentionsDid file: automod/helpers/bsky.go:244 returns_error: нет description: —


### PostMentionsDid (automod/helpers/bsky.go:244)


PostMentionsDid is a function that performs operations based on the provided parameters and returns (post *appbsky.FeedPost, did string).


```go
func PostMentionsDid((post *appbsky.FeedPost, did string)) (post *appbsky.FeedPost, did string)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `automod/helpers/bsky.go:244`



---


[function] name: PostParentOrRootIsAnyDid file: automod/helpers/bsky.go:230 returns_error: нет description: —


### PostParentOrRootIsAnyDid (automod/helpers/bsky.go:230)


PostParentOrRootIsAnyDid is a function that performs operations based on the provided parameters and returns (post *appbsky.FeedPost, dids []string).


```go
func PostParentOrRootIsAnyDid((post *appbsky.FeedPost, dids []string)) (post *appbsky.FeedPost, dids []string)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** dids


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/helpers/bsky.go:230`



---


[function] name: PostParentOrRootIsDid file: automod/helpers/bsky.go:212 returns_error: нет description: —


### PostParentOrRootIsDid (automod/helpers/bsky.go:212)


PostParentOrRootIsDid is a function that performs operations based on the provided parameters and returns (post *appbsky.FeedPost, did string).


```go
func PostParentOrRootIsDid((post *appbsky.FeedPost, did string)) (post *appbsky.FeedPost, did string)
```


**Тип запроса:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** post


```json
{
  "ID": 0,
  "CreatedAt": {},
  "RecCreated": "string",
  "Post": 0,
  "Reposter": {},
  "Author": {},
  "RecCid": "string",
  "Rkey": "string"
}
```


*Определено в:* `models/models.go`


**Тип ответа:** appbsky.FeedPost


```json
{
  "$type": "string",
  "createdAt": "string",
  "embed": null,
  "entities": [],
  "facets": [],
  "labels": null,
  "langs": [],
  "reply": null,
  "tags": [],
  "text": "string"
}
```


*Определено в:* `api/bsky/feedpost.go`


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


📍 *Расположение:* `automod/helpers/bsky.go:212`




## automod/helpers/text.go


📄 Исходный файл: `automod/helpers/text.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DedupeStrings](#dedupestrings-automodhelperstextgo10) `:10`

- 🔗 [ExtractTextURLs](#extracttexturls-automodhelperstextgo33) `:33`

- 🔗 [HashOfString](#hashofstring-automodhelperstextgo25) `:25`


</details>


[function] name: DedupeStrings file: automod/helpers/text.go:10 returns_error: нет description: —


### DedupeStrings (automod/helpers/text.go:10)


DedupeStrings is a function that performs operations based on the provided parameters and returns (in []string).


```go
func DedupeStrings((in []string)) (in []string)
```


**Тип ответа:** in


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


📍 *Расположение:* `automod/helpers/text.go:10`



---


[function] name: ExtractTextURLs file: automod/helpers/text.go:33 returns_error: нет description: —


### ExtractTextURLs (automod/helpers/text.go:33)


ExtractTextURLs is a function that performs operations based on the provided parameters and returns (raw string).


```go
func ExtractTextURLs((raw string)) (raw string)
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


📍 *Расположение:* `automod/helpers/text.go:33`



---


[function] name: HashOfString file: automod/helpers/text.go:25 returns_error: нет description: returns a fast, compact hash of a string

current implementation uses murmur3, default seed, and hex encoding


### HashOfString (automod/helpers/text.go:25)


returns a fast, compact hash of a string

current implementation uses murmur3, default seed, and hex encoding


```go
func HashOfString((s string)) (s string)
```


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


📍 *Расположение:* `automod/helpers/text.go:25`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_flagstore.md)

- [Следующая директория](automod_keyword.md)


---

