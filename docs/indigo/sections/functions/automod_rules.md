---
title: "Функции: automod/rules"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/rules
---


# Функции: automod/rules


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_keyword.md)

- [Следующая директория](automod_setstore.md)


---


## Меню по файлам


- 📄 [automod/rules/all.go](#automodrulesallgo)

- 📄 [automod/rules/blobs.go](#automodrulesblobsgo)

- 📄 [automod/rules/gtube.go](#automodrulesgtubego)

- 📄 [automod/rules/harassment.go](#automodrulesharassmentgo)

- 📄 [automod/rules/hashtags.go](#automodruleshashtagsgo)

- 📄 [automod/rules/identity.go](#automodrulesidentitygo)

- 📄 [automod/rules/interaction.go](#automodrulesinteractiongo)

- 📄 [automod/rules/keyword.go](#automodruleskeywordgo)

- 📄 [automod/rules/mentions.go](#automodrulesmentionsgo)

- 📄 [automod/rules/misleading.go](#automodrulesmisleadinggo)

- 📄 [automod/rules/misleading_unicode_reverse.go](#automodrulesmisleading_unicode_reversego)

- 📄 [automod/rules/nostr.go](#automodrulesnostrgo)

- 📄 [automod/rules/private.go](#automodrulesprivatego)

- 📄 [automod/rules/profile.go](#automodrulesprofilego)

- 📄 [automod/rules/promo.go](#automodrulespromogo)

- 📄 [automod/rules/quick.go](#automodrulesquickgo)

- 📄 [automod/rules/replies.go](#automodrulesrepliesgo)

- 📄 [automod/rules/reposts.go](#automodrulesrepostsgo)


---


## automod/rules/all.go


📄 Исходный файл: `automod/rules/all.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DefaultRules](#defaultrules-automodrulesallgo8) `:8`


</details>


[function] name: DefaultRules file: automod/rules/all.go:8 returns_error: нет description: IMPORTANT: reminder that these are the indigo-edition rules, not production rules


### DefaultRules (automod/rules/all.go:8)


IMPORTANT: reminder that these are the indigo-edition rules, not production rules


```go
func DefaultRules(()) ()
```


📍 *Расположение:* `automod/rules/all.go:8`




## automod/rules/blobs.go


📄 Исходный файл: `automod/rules/blobs.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [BlobVerifyRule](#blobverifyrule-automodrulesblobsgo10) `:10`


</details>


[function] name: BlobVerifyRule file: automod/rules/blobs.go:10 returns_error: нет description: —


### BlobVerifyRule (automod/rules/blobs.go:10)


BlobVerifyRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, blob lexutil.LexBlob, data []byte).


```go
func BlobVerifyRule((c *automod.RecordContext, blob lexutil.LexBlob, data []byte)) (c *automod.RecordContext, blob lexutil.LexBlob, data []byte)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


**Тип ответа:** blob


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lexutil.LexBlob


```json
{
  "Ref": {},
  "MimeType": "string",
  "Size": 0
}
```


*Определено в:* `lex/util/lex_types.go`


**Тип ответа:** data


```json
{
  "AuthorizationServers": []
}
```


*Определено в:* `atproto/auth/oauth/types.go`


📍 *Расположение:* `automod/rules/blobs.go:10`




## automod/rules/gtube.go


📄 Исходный файл: `automod/rules/gtube.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GtubePostRule](#gtubepostrule-automodrulesgtubego15) `:15`

- 🔗 [GtubeProfileRule](#gtubeprofilerule-automodrulesgtubego26) `:26`


</details>


[function] name: GtubePostRule file: automod/rules/gtube.go:15 returns_error: нет description: —


### GtubePostRule (automod/rules/gtube.go:15)


GtubePostRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func GtubePostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/gtube.go:15`



---


[function] name: GtubeProfileRule file: automod/rules/gtube.go:26 returns_error: нет description: —


### GtubeProfileRule (automod/rules/gtube.go:26)


GtubeProfileRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, profile *appbsky.ActorProfile).


```go
func GtubeProfileRule((c *automod.RecordContext, profile *appbsky.ActorProfile)) (c *automod.RecordContext, profile *appbsky.ActorProfile)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


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


📍 *Расположение:* `automod/rules/gtube.go:26`




## automod/rules/harassment.go


📄 Исходный файл: `automod/rules/harassment.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [HarassmentProtectionOzoneEventRule](#harassmentprotectionozoneeventrule-automodrulesharassmentgo143) `:143`

- 🔗 [HarassmentTargetInteractionPostRule](#harassmenttargetinteractionpostrule-automodrulesharassmentgo17) `:17`

- 🔗 [HarassmentTrivialPostRule](#harassmenttrivialpostrule-automodrulesharassmentgo117) `:117`


</details>


[function] name: HarassmentProtectionOzoneEventRule file: automod/rules/harassment.go:143 returns_error: нет description: looks for new harassment protection tags on accounts, and logs them


### HarassmentProtectionOzoneEventRule (automod/rules/harassment.go:143)


looks for new harassment protection tags on accounts, and logs them


```go
func HarassmentProtectionOzoneEventRule((c *automod.OzoneEventContext)) (c *automod.OzoneEventContext)
```


**Тип запроса:** automod.OzoneEventContext


```json
{
  "Event": {},
  "CreatorAccount": {},
  "SubjectRecord": null
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


**Тип ответа:** automod.OzoneEventContext


```json
{
  "Event": {},
  "CreatorAccount": {},
  "SubjectRecord": null
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/rules/harassment.go:143`



---


[function] name: HarassmentTargetInteractionPostRule file: automod/rules/harassment.go:17 returns_error: нет description: looks for new accounts, which interact with frequently-harassed accounts, and report them for review


### HarassmentTargetInteractionPostRule (automod/rules/harassment.go:17)


looks for new accounts, which interact with frequently-harassed accounts, and report them for review


```go
func HarassmentTargetInteractionPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/harassment.go:17`



---


[function] name: HarassmentTrivialPostRule file: automod/rules/harassment.go:117 returns_error: нет description: looks for new accounts, which frequently post the same type of content


### HarassmentTrivialPostRule (automod/rules/harassment.go:117)


looks for new accounts, which frequently post the same type of content


```go
func HarassmentTrivialPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/harassment.go:117`




## automod/rules/hashtags.go


📄 Исходный файл: `automod/rules/hashtags.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [BadHashtagsPostRule](#badhashtagspostrule-automodruleshashtagsgo13) `:13`

- 🔗 [TooManyHashtagsPostRule](#toomanyhashtagspostrule-automodruleshashtagsgo38) `:38`


</details>


[function] name: BadHashtagsPostRule file: automod/rules/hashtags.go:13 returns_error: нет description: looks for specific hashtags from known lists


### BadHashtagsPostRule (automod/rules/hashtags.go:13)


looks for specific hashtags from known lists


```go
func BadHashtagsPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/hashtags.go:13`



---


[function] name: TooManyHashtagsPostRule file: automod/rules/hashtags.go:38 returns_error: нет description: if a post is "almost all" hashtags, it might be a form of search spam


### TooManyHashtagsPostRule (automod/rules/hashtags.go:38)


if a post is "almost all" hashtags, it might be a form of search spam


```go
func TooManyHashtagsPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/hashtags.go:38`




## automod/rules/identity.go


📄 Исходный файл: `automod/rules/identity.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [CelebSpamIdentityRule](#celebspamidentityrule-automodrulesidentitygo47) `:47`

- 🔗 [NewAccountRule](#newaccountrule-automodrulesidentitygo14) `:14`


</details>


[function] name: CelebSpamIdentityRule file: automod/rules/identity.go:47 returns_error: нет description: —


### CelebSpamIdentityRule (automod/rules/identity.go:47)


CelebSpamIdentityRule is a function that performs operations based on the provided parameters and returns (c *automod.AccountContext).


```go
func CelebSpamIdentityRule((c *automod.AccountContext)) (c *automod.AccountContext)
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


📍 *Расположение:* `automod/rules/identity.go:47`



---


[function] name: NewAccountRule file: automod/rules/identity.go:14 returns_error: нет description: triggers on first identity event for an account (DID)


### NewAccountRule (automod/rules/identity.go:14)


triggers on first identity event for an account (DID)


```go
func NewAccountRule((c *automod.AccountContext)) (c *automod.AccountContext)
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


📍 *Расположение:* `automod/rules/identity.go:14`




## automod/rules/interaction.go


📄 Исходный файл: `automod/rules/interaction.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [DeleteInteractionRule](#deleteinteractionrule-automodrulesinteractiongo60) `:60`

- 🔗 [InteractionChurnRule](#interactionchurnrule-automodrulesinteractiongo16) `:16`


</details>


[function] name: DeleteInteractionRule file: automod/rules/interaction.go:60 returns_error: нет description: —


### DeleteInteractionRule (automod/rules/interaction.go:60)


DeleteInteractionRule is a function that deletes data based on the provided parameters and returns (c *automod.RecordContext).


```go
func DeleteInteractionRule((c *automod.RecordContext)) (c *automod.RecordContext)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/rules/interaction.go:60`



---


[function] name: InteractionChurnRule file: automod/rules/interaction.go:16 returns_error: нет description: looks for accounts which do frequent interaction churn, such as follow-unfollow.


### InteractionChurnRule (automod/rules/interaction.go:16)


looks for accounts which do frequent interaction churn, such as follow-unfollow.


```go
func InteractionChurnRule((c *automod.RecordContext)) (c *automod.RecordContext)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/rules/interaction.go:16`




## automod/rules/keyword.go


📄 Исходный файл: `automod/rules/keyword.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [BadWordDIDRule](#badworddidrule-automodruleskeywordgo210) `:210`

- 🔗 [BadWordHandleRule](#badwordhandlerule-automodruleskeywordgo186) `:186`

- 🔗 [BadWordOtherRecordRule](#badwordotherrecordrule-automodruleskeywordgo93) `:93`

- 🔗 [BadWordPostRule](#badwordpostrule-automodruleskeywordgo14) `:14`

- 🔗 [BadWordProfileRule](#badwordprofilerule-automodruleskeywordgo49) `:49`

- 🔗 [BadWordRecordKeyRule](#badwordrecordkeyrule-automodruleskeywordgo163) `:163`

- 🔗 [ReplySingleBadWordPostRule](#replysinglebadwordpostrule-automodruleskeywordgo74) `:74`


</details>


[function] name: BadWordDIDRule file: automod/rules/keyword.go:210 returns_error: нет description: —


### BadWordDIDRule (automod/rules/keyword.go:210)


BadWordDIDRule is a function that performs operations based on the provided parameters and returns (c *automod.AccountContext).


```go
func BadWordDIDRule((c *automod.AccountContext)) (c *automod.AccountContext)
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


📍 *Расположение:* `automod/rules/keyword.go:210`



---


[function] name: BadWordHandleRule file: automod/rules/keyword.go:186 returns_error: нет description: —


### BadWordHandleRule (automod/rules/keyword.go:186)


BadWordHandleRule is a function that performs operations based on the provided parameters and returns (c *automod.AccountContext).


```go
func BadWordHandleRule((c *automod.AccountContext)) (c *automod.AccountContext)
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


📍 *Расположение:* `automod/rules/keyword.go:186`



---


[function] name: BadWordOtherRecordRule file: automod/rules/keyword.go:93 returns_error: нет description: scans for bad keywords in records other than posts and profiles


### BadWordOtherRecordRule (automod/rules/keyword.go:93)


scans for bad keywords in records other than posts and profiles


```go
func BadWordOtherRecordRule((c *automod.RecordContext)) (c *automod.RecordContext)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/rules/keyword.go:93`



---


[function] name: BadWordPostRule file: automod/rules/keyword.go:14 returns_error: нет description: —


### BadWordPostRule (automod/rules/keyword.go:14)


BadWordPostRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func BadWordPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/keyword.go:14`



---


[function] name: BadWordProfileRule file: automod/rules/keyword.go:49 returns_error: нет description: —


### BadWordProfileRule (automod/rules/keyword.go:49)


BadWordProfileRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, profile *appbsky.ActorProfile).


```go
func BadWordProfileRule((c *automod.RecordContext, profile *appbsky.ActorProfile)) (c *automod.RecordContext, profile *appbsky.ActorProfile)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


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


📍 *Расположение:* `automod/rules/keyword.go:49`



---


[function] name: BadWordRecordKeyRule file: automod/rules/keyword.go:163 returns_error: нет description: scans the record-key for all records


### BadWordRecordKeyRule (automod/rules/keyword.go:163)


scans the record-key for all records


```go
func BadWordRecordKeyRule((c *automod.RecordContext)) (c *automod.RecordContext)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/rules/keyword.go:163`



---


[function] name: ReplySingleBadWordPostRule file: automod/rules/keyword.go:74 returns_error: нет description: looks for the specific harassment situation of a replay to another user with only a single word


### ReplySingleBadWordPostRule (automod/rules/keyword.go:74)


looks for the specific harassment situation of a replay to another user with only a single word


```go
func ReplySingleBadWordPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/keyword.go:74`




## automod/rules/mentions.go


📄 Исходный файл: `automod/rules/mentions.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [DistinctMentionsRule](#distinctmentionsrule-automodrulesmentionsgo19) `:19`

- 🔗 [YoungAccountDistinctMentionsRule](#youngaccountdistinctmentionsrule-automodrulesmentionsgo50) `:50`


</details>


[function] name: DistinctMentionsRule file: automod/rules/mentions.go:19 returns_error: нет description: DistinctMentionsRule looks for accounts which mention an unusually large number of distinct accounts per period.


### DistinctMentionsRule (automod/rules/mentions.go:19)


DistinctMentionsRule looks for accounts which mention an unusually large number of distinct accounts per period.


```go
func DistinctMentionsRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/mentions.go:19`



---


[function] name: YoungAccountDistinctMentionsRule file: automod/rules/mentions.go:50 returns_error: нет description: —


### YoungAccountDistinctMentionsRule (automod/rules/mentions.go:50)


YoungAccountDistinctMentionsRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func YoungAccountDistinctMentionsRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/mentions.go:50`




## automod/rules/misleading.go


📄 Исходный файл: `automod/rules/misleading.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MisleadingMentionPostRule](#misleadingmentionpostrule-automodrulesmisleadinggo108) `:108`

- 🔗 [MisleadingURLPostRule](#misleadingurlpostrule-automodrulesmisleadinggo83) `:83`

- 🔗 [isMisleadingURLFacet](#ismisleadingurlfacet-automodrulesmisleadinggo15) `:15`


</details>


[function] name: MisleadingMentionPostRule file: automod/rules/misleading.go:108 returns_error: нет description: —


### MisleadingMentionPostRule (automod/rules/misleading.go:108)


MisleadingMentionPostRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func MisleadingMentionPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/misleading.go:108`



---


[function] name: MisleadingURLPostRule file: automod/rules/misleading.go:83 returns_error: нет description: —


### MisleadingURLPostRule (automod/rules/misleading.go:83)


MisleadingURLPostRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func MisleadingURLPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/misleading.go:83`



---


[function] name: isMisleadingURLFacet file: automod/rules/misleading.go:15 returns_error: нет description: —


### isMisleadingURLFacet (automod/rules/misleading.go:15)


isMisleadingURLFacet is a function that performs operations based on the provided parameters and returns (facet helpers.PostFacet, logger *slog.Logger).


```go
func isMisleadingURLFacet((facet helpers.PostFacet, logger *slog.Logger)) (facet helpers.PostFacet, logger *slog.Logger)
```


**Тип запроса:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** facet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** helpers.PostFacet


```json
{
  "Text": "string",
  "URL": "string",
  "DID": "string",
  "Tag": "string"
}
```


*Определено в:* `automod/helpers/bsky.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slog.Logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/rules/misleading.go:15`




## automod/rules/misleading_unicode_reverse.go


📄 Исходный файл: `automod/rules/misleading_unicode_reverse.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [MisleadingLinkUnicodeReversalPostRule](#misleadinglinkunicodereversalpostrule-automodrulesmisleading_unicode_reversego10) `:10`


</details>


[function] name: MisleadingLinkUnicodeReversalPostRule file: automod/rules/misleading_unicode_reverse.go:10 returns_error: нет description: —


### MisleadingLinkUnicodeReversalPostRule (automod/rules/misleading_unicode_reverse.go:10)


MisleadingLinkUnicodeReversalPostRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func MisleadingLinkUnicodeReversalPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/misleading_unicode_reverse.go:10`




## automod/rules/nostr.go


📄 Исходный файл: `automod/rules/nostr.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NostrSpamPostRule](#nostrspampostrule-automodrulesnostrgo15) `:15`


</details>


[function] name: NostrSpamPostRule file: automod/rules/nostr.go:15 returns_error: нет description: looks for new accounts, which frequently post the same type of content


### NostrSpamPostRule (automod/rules/nostr.go:15)


looks for new accounts, which frequently post the same type of content


```go
func NostrSpamPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/nostr.go:15`




## automod/rules/private.go


📄 Исходный файл: `automod/rules/private.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AccountPrivateDemoPostRule](#accountprivatedemopostrule-automodrulesprivatego13) `:13`


</details>


[function] name: AccountPrivateDemoPostRule file: automod/rules/private.go:13 returns_error: нет description: dummy rule. this leaks PII (account email) in logs and should never be used in real life


### AccountPrivateDemoPostRule (automod/rules/private.go:13)


dummy rule. this leaks PII (account email) in logs and should never be used in real life


```go
func AccountPrivateDemoPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/private.go:13`




## automod/rules/profile.go


📄 Исходный файл: `automod/rules/profile.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [AccountDemoPostRule](#accountdemopostrule-automodrulesprofilego12) `:12`

- 🔗 [CelebSpamProfileRule](#celebspamprofilerule-automodrulesprofilego20) `:20`


</details>


[function] name: AccountDemoPostRule file: automod/rules/profile.go:12 returns_error: нет description: this is a dummy rule to demonstrate accessing account metadata (eg, profile) from within post handler


### AccountDemoPostRule (automod/rules/profile.go:12)


this is a dummy rule to demonstrate accessing account metadata (eg, profile) from within post handler


```go
func AccountDemoPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/profile.go:12`



---


[function] name: CelebSpamProfileRule file: automod/rules/profile.go:20 returns_error: нет description: —


### CelebSpamProfileRule (automod/rules/profile.go:20)


CelebSpamProfileRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, profile *appbsky.ActorProfile).


```go
func CelebSpamProfileRule((c *automod.RecordContext, profile *appbsky.ActorProfile)) (c *automod.RecordContext, profile *appbsky.ActorProfile)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


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


📍 *Расположение:* `automod/rules/profile.go:20`




## automod/rules/promo.go


📄 Исходный файл: `automod/rules/promo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AggressivePromotionRule](#aggressivepromotionrule-automodrulespromogo19) `:19`


</details>


[function] name: AggressivePromotionRule file: automod/rules/promo.go:19 returns_error: нет description: looks for new accounts, with a commercial or donation link in profile, which directly reply to several accounts

this ru


### AggressivePromotionRule (automod/rules/promo.go:19)


looks for new accounts, with a commercial or donation link in profile, which directly reply to several accounts

this rule depends on ReplyCountPostRule() to set counts


```go
func AggressivePromotionRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/promo.go:19`




## automod/rules/quick.go


📄 Исходный файл: `automod/rules/quick.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [BotLinkProfileRule](#botlinkprofilerule-automodrulesquickgo19) `:19`

- 🔗 [NewAccountBotEmailRule](#newaccountbotemailrule-automodrulesquickgo57) `:57`

- 🔗 [SimpleBotPostRule](#simplebotpostrule-automodrulesquickgo42) `:42`

- 🔗 [TrivialSpamPostRule](#trivialspampostrule-automodrulesquickgo76) `:76`


</details>


[function] name: BotLinkProfileRule file: automod/rules/quick.go:19 returns_error: нет description: —


### BotLinkProfileRule (automod/rules/quick.go:19)


BotLinkProfileRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, profile *appbsky.ActorProfile).


```go
func BotLinkProfileRule((c *automod.RecordContext, profile *appbsky.ActorProfile)) (c *automod.RecordContext, profile *appbsky.ActorProfile)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


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


📍 *Расположение:* `automod/rules/quick.go:19`



---


[function] name: NewAccountBotEmailRule file: automod/rules/quick.go:57 returns_error: нет description: —


### NewAccountBotEmailRule (automod/rules/quick.go:57)


NewAccountBotEmailRule is a function that performs operations based on the provided parameters and returns (c *automod.AccountContext).


```go
func NewAccountBotEmailRule((c *automod.AccountContext)) (c *automod.AccountContext)
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


📍 *Расположение:* `automod/rules/quick.go:57`



---


[function] name: SimpleBotPostRule file: automod/rules/quick.go:42 returns_error: нет description: —


### SimpleBotPostRule (automod/rules/quick.go:42)


SimpleBotPostRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func SimpleBotPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/quick.go:42`



---


[function] name: TrivialSpamPostRule file: automod/rules/quick.go:76 returns_error: нет description: looks for new accounts, which frequently post the same type of content


### TrivialSpamPostRule (automod/rules/quick.go:76)


looks for new accounts, which frequently post the same type of content


```go
func TrivialSpamPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/quick.go:76`




## automod/rules/replies.go


📄 Исходный файл: `automod/rules/replies.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [IdenticalReplyPostRule](#identicalreplypostrule-automodrulesrepliesgo50) `:50`

- 🔗 [IdenticalReplyPostSameParentRule](#identicalreplypostsameparentrule-automodrulesrepliesgo94) `:94`

- 🔗 [ReplyCountPostRule](#replycountpostrule-automodrulesrepliesgo18) `:18`

- 🔗 [YoungAccountDistinctRepliesRule](#youngaccountdistinctrepliesrule-automodrulesrepliesgo128) `:128`


</details>


[function] name: IdenticalReplyPostRule file: automod/rules/replies.go:50 returns_error: нет description: Looks for accounts posting the exact same text multiple times. Does not currently count the number of distinct accounts 


### IdenticalReplyPostRule (automod/rules/replies.go:50)


Looks for accounts posting the exact same text multiple times. Does not currently count the number of distinct accounts replied to, just counts replies at all.

There can be legitimate situations that trigger this rule, so in most situations should be a "report" not "label" action.


```go
func IdenticalReplyPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/replies.go:50`



---


[function] name: IdenticalReplyPostSameParentRule file: automod/rules/replies.go:94 returns_error: нет description: —


### IdenticalReplyPostSameParentRule (automod/rules/replies.go:94)


IdenticalReplyPostSameParentRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func IdenticalReplyPostSameParentRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/replies.go:94`



---


[function] name: ReplyCountPostRule file: automod/rules/replies.go:18 returns_error: нет description: does not count "self-replies" (direct to self, or in own post thread)


### ReplyCountPostRule (automod/rules/replies.go:18)


does not count "self-replies" (direct to self, or in own post thread)


```go
func ReplyCountPostRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/replies.go:18`



---


[function] name: YoungAccountDistinctRepliesRule file: automod/rules/replies.go:128 returns_error: нет description: —


### YoungAccountDistinctRepliesRule (automod/rules/replies.go:128)


YoungAccountDistinctRepliesRule is a function that performs operations based on the provided parameters and returns (c *automod.RecordContext, post *appbsky.FeedPost).


```go
func YoungAccountDistinctRepliesRule((c *automod.RecordContext, post *appbsky.FeedPost)) (c *automod.RecordContext, post *appbsky.FeedPost)
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


📍 *Расположение:* `automod/rules/replies.go:128`




## automod/rules/reposts.go


📄 Исходный файл: `automod/rules/reposts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TooManyRepostRule](#toomanyrepostrule-automodrulesrepostsgo20) `:20`


</details>


[function] name: TooManyRepostRule file: automod/rules/reposts.go:20 returns_error: нет description: looks for accounts which do frequent reposts


### TooManyRepostRule (automod/rules/reposts.go:20)


looks for accounts which do frequent reposts


```go
func TooManyRepostRule((c *automod.RecordContext)) (c *automod.RecordContext)
```


**Тип запроса:** automod.RecordContext


```json
{
  "RecordOp": {}
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


**Тип ответа:** automod.RecordContext


```json
{
  "RecordOp": {}
}
```


*Определено в:* `automod/engine/context.go`


📍 *Расположение:* `automod/rules/reposts.go:20`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_keyword.md)

- [Следующая директория](automod_setstore.md)


---

