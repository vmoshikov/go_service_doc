---
title: "Функции: api/atproto"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: api/atproto
---


# Функции: api/atproto


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_agnostic.md)

- [Следующая директория](api_bsky.md)


---


## Меню по файлам


- 📄 [api/atproto/admindeleteAccount.go](#apiatprotoadmindeleteaccountgo)

- 📄 [api/atproto/admindisableAccountInvites.go](#apiatprotoadmindisableaccountinvitesgo)

- 📄 [api/atproto/admindisableInviteCodes.go](#apiatprotoadmindisableinvitecodesgo)

- 📄 [api/atproto/adminenableAccountInvites.go](#apiatprotoadminenableaccountinvitesgo)

- 📄 [api/atproto/admingetAccountInfo.go](#apiatprotoadmingetaccountinfogo)

- 📄 [api/atproto/admingetAccountInfos.go](#apiatprotoadmingetaccountinfosgo)

- 📄 [api/atproto/admingetInviteCodes.go](#apiatprotoadmingetinvitecodesgo)

- 📄 [api/atproto/admingetSubjectStatus.go](#apiatprotoadmingetsubjectstatusgo)

- 📄 [api/atproto/adminsearchAccounts.go](#apiatprotoadminsearchaccountsgo)

- 📄 [api/atproto/adminsendEmail.go](#apiatprotoadminsendemailgo)

- 📄 [api/atproto/adminupdateAccountEmail.go](#apiatprotoadminupdateaccountemailgo)

- 📄 [api/atproto/adminupdateAccountHandle.go](#apiatprotoadminupdateaccounthandlego)

- 📄 [api/atproto/adminupdateAccountPassword.go](#apiatprotoadminupdateaccountpasswordgo)

- 📄 [api/atproto/adminupdateAccountSigningKey.go](#apiatprotoadminupdateaccountsigningkeygo)

- 📄 [api/atproto/adminupdateSubjectStatus.go](#apiatprotoadminupdatesubjectstatusgo)

- 📄 [api/atproto/cbor_gen.go](#apiatprotocbor_gengo)

- 📄 [api/atproto/identitygetRecommendedDidCredentials.go](#apiatprotoidentitygetrecommendeddidcredentialsgo)

- 📄 [api/atproto/identityrefreshIdentity.go](#apiatprotoidentityrefreshidentitygo)

- 📄 [api/atproto/identityrequestPlcOperationSignature.go](#apiatprotoidentityrequestplcoperationsignaturego)

- 📄 [api/atproto/identityresolveDid.go](#apiatprotoidentityresolvedidgo)

- 📄 [api/atproto/identityresolveHandle.go](#apiatprotoidentityresolvehandlego)

- 📄 [api/atproto/identityresolveIdentity.go](#apiatprotoidentityresolveidentitygo)

- 📄 [api/atproto/identitysignPlcOperation.go](#apiatprotoidentitysignplcoperationgo)

- 📄 [api/atproto/identitysubmitPlcOperation.go](#apiatprotoidentitysubmitplcoperationgo)

- 📄 [api/atproto/identityupdateHandle.go](#apiatprotoidentityupdatehandlego)

- 📄 [api/atproto/labelqueryLabels.go](#apiatprotolabelquerylabelsgo)

- 📄 [api/atproto/lexiconschema.go](#apiatprotolexiconschemago)

- 📄 [api/atproto/moderationcreateReport.go](#apiatprotomoderationcreatereportgo)

- 📄 [api/atproto/repoapplyWrites.go](#apiatprotorepoapplywritesgo)

- 📄 [api/atproto/repocreateRecord.go](#apiatprotorepocreaterecordgo)

- 📄 [api/atproto/repodeleteRecord.go](#apiatprotorepodeleterecordgo)

- 📄 [api/atproto/repodescribeRepo.go](#apiatprotorepodescriberepogo)

- 📄 [api/atproto/repogetRecord.go](#apiatprotorepogetrecordgo)

- 📄 [api/atproto/repoimportRepo.go](#apiatprotorepoimportrepogo)

- 📄 [api/atproto/repolistMissingBlobs.go](#apiatprotorepolistmissingblobsgo)

- 📄 [api/atproto/repolistRecords.go](#apiatprotorepolistrecordsgo)

- 📄 [api/atproto/repoputRecord.go](#apiatprotorepoputrecordgo)

- 📄 [api/atproto/repostrongRef.go](#apiatprotorepostrongrefgo)

- 📄 [api/atproto/repouploadBlob.go](#apiatprotorepouploadblobgo)

- 📄 [api/atproto/serveractivateAccount.go](#apiatprotoserveractivateaccountgo)

- 📄 [api/atproto/servercheckAccountStatus.go](#apiatprotoservercheckaccountstatusgo)

- 📄 [api/atproto/serverconfirmEmail.go](#apiatprotoserverconfirmemailgo)

- 📄 [api/atproto/servercreateAccount.go](#apiatprotoservercreateaccountgo)

- 📄 [api/atproto/servercreateAppPassword.go](#apiatprotoservercreateapppasswordgo)

- 📄 [api/atproto/servercreateInviteCode.go](#apiatprotoservercreateinvitecodego)

- 📄 [api/atproto/servercreateInviteCodes.go](#apiatprotoservercreateinvitecodesgo)

- 📄 [api/atproto/servercreateSession.go](#apiatprotoservercreatesessiongo)

- 📄 [api/atproto/serverdeactivateAccount.go](#apiatprotoserverdeactivateaccountgo)

- 📄 [api/atproto/serverdeleteAccount.go](#apiatprotoserverdeleteaccountgo)

- 📄 [api/atproto/serverdeleteSession.go](#apiatprotoserverdeletesessiongo)

- 📄 [api/atproto/serverdescribeServer.go](#apiatprotoserverdescribeservergo)

- 📄 [api/atproto/servergetAccountInviteCodes.go](#apiatprotoservergetaccountinvitecodesgo)

- 📄 [api/atproto/servergetServiceAuth.go](#apiatprotoservergetserviceauthgo)

- 📄 [api/atproto/servergetSession.go](#apiatprotoservergetsessiongo)

- 📄 [api/atproto/serverlistAppPasswords.go](#apiatprotoserverlistapppasswordsgo)

- 📄 [api/atproto/serverrefreshSession.go](#apiatprotoserverrefreshsessiongo)

- 📄 [api/atproto/serverrequestAccountDelete.go](#apiatprotoserverrequestaccountdeletego)

- 📄 [api/atproto/serverrequestEmailConfirmation.go](#apiatprotoserverrequestemailconfirmationgo)

- 📄 [api/atproto/serverrequestEmailUpdate.go](#apiatprotoserverrequestemailupdatego)

- 📄 [api/atproto/serverrequestPasswordReset.go](#apiatprotoserverrequestpasswordresetgo)

- 📄 [api/atproto/serverreserveSigningKey.go](#apiatprotoserverreservesigningkeygo)

- 📄 [api/atproto/serverresetPassword.go](#apiatprotoserverresetpasswordgo)

- 📄 [api/atproto/serverrevokeAppPassword.go](#apiatprotoserverrevokeapppasswordgo)

- 📄 [api/atproto/serverupdateEmail.go](#apiatprotoserverupdateemailgo)

- 📄 [api/atproto/syncgetBlob.go](#apiatprotosyncgetblobgo)

- 📄 [api/atproto/syncgetBlocks.go](#apiatprotosyncgetblocksgo)

- 📄 [api/atproto/syncgetCheckout.go](#apiatprotosyncgetcheckoutgo)

- 📄 [api/atproto/syncgetHead.go](#apiatprotosyncgetheadgo)

- 📄 [api/atproto/syncgetHostStatus.go](#apiatprotosyncgethoststatusgo)

- 📄 [api/atproto/syncgetLatestCommit.go](#apiatprotosyncgetlatestcommitgo)

- 📄 [api/atproto/syncgetRecord.go](#apiatprotosyncgetrecordgo)

- 📄 [api/atproto/syncgetRepo.go](#apiatprotosyncgetrepogo)

- 📄 [api/atproto/syncgetRepoStatus.go](#apiatprotosyncgetrepostatusgo)

- 📄 [api/atproto/synclistBlobs.go](#apiatprotosynclistblobsgo)

- 📄 [api/atproto/synclistHosts.go](#apiatprotosynclisthostsgo)

- 📄 [api/atproto/synclistRepos.go](#apiatprotosynclistreposgo)

- 📄 [api/atproto/synclistReposByCollection.go](#apiatprotosynclistreposbycollectiongo)

- 📄 [api/atproto/syncnotifyOfUpdate.go](#apiatprotosyncnotifyofupdatego)

- 📄 [api/atproto/syncrequestCrawl.go](#apiatprotosyncrequestcrawlgo)

- 📄 [api/atproto/tempaddReservedHandle.go](#apiatprototempaddreservedhandlego)

- 📄 [api/atproto/tempcheckHandleAvailability.go](#apiatprototempcheckhandleavailabilitygo)

- 📄 [api/atproto/tempcheckSignupQueue.go](#apiatprototempchecksignupqueuego)

- 📄 [api/atproto/tempdereferenceScope.go](#apiatprototempdereferencescopego)

- 📄 [api/atproto/tempfetchLabels.go](#apiatprototempfetchlabelsgo)

- 📄 [api/atproto/temprequestPhoneVerification.go](#apiatprototemprequestphoneverificationgo)

- 📄 [api/atproto/temprevokeAccountCredentials.go](#apiatprototemprevokeaccountcredentialsgo)


---


## api/atproto/admindeleteAccount.go


📄 Исходный файл: `api/atproto/admindeleteAccount.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminDeleteAccount](#admindeleteaccount-apiatprotoadmindeleteaccountgo19) `:19`


</details>


[function] name: AdminDeleteAccount file: api/atproto/admindeleteAccount.go:19 returns_error: нет description: AdminDeleteAccount calls the XRPC method "com.atproto.admin.deleteAccount".


### AdminDeleteAccount (api/atproto/admindeleteAccount.go:19)


AdminDeleteAccount calls the XRPC method "com.atproto.admin.deleteAccount".


```go
func AdminDeleteAccount((ctx context.Context, c lexutil.LexClient, input *AdminDeleteAccount_Input)) (ctx context.Context, c lexutil.LexClient, input *AdminDeleteAccount_Input)
```


**Тип запроса:** AdminDeleteAccount_Input


```json
{
  "did": "string"
}
```


*Определено в:* `api/atproto/admindeleteAccount.go`


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


**Тип ответа:** AdminDeleteAccount_Input


```json
{
  "did": "string"
}
```


*Определено в:* `api/atproto/admindeleteAccount.go`


📍 *Расположение:* `api/atproto/admindeleteAccount.go:19`




## api/atproto/admindisableAccountInvites.go


📄 Исходный файл: `api/atproto/admindisableAccountInvites.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminDisableAccountInvites](#admindisableaccountinvites-apiatprotoadmindisableaccountinvitesgo21) `:21`


</details>


[function] name: AdminDisableAccountInvites file: api/atproto/admindisableAccountInvites.go:21 returns_error: нет description: AdminDisableAccountInvites calls the XRPC method "com.atproto.admin.disableAccountInvites".


### AdminDisableAccountInvites (api/atproto/admindisableAccountInvites.go:21)


AdminDisableAccountInvites calls the XRPC method "com.atproto.admin.disableAccountInvites".


```go
func AdminDisableAccountInvites((ctx context.Context, c lexutil.LexClient, input *AdminDisableAccountInvites_Input)) (ctx context.Context, c lexutil.LexClient, input *AdminDisableAccountInvites_Input)
```


**Тип запроса:** AdminDisableAccountInvites_Input


```json
{
  "account": "string",
  "note": "string"
}
```


*Определено в:* `api/atproto/admindisableAccountInvites.go`


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


**Тип ответа:** AdminDisableAccountInvites_Input


```json
{
  "account": "string",
  "note": "string"
}
```


*Определено в:* `api/atproto/admindisableAccountInvites.go`


📍 *Расположение:* `api/atproto/admindisableAccountInvites.go:21`




## api/atproto/admindisableInviteCodes.go


📄 Исходный файл: `api/atproto/admindisableInviteCodes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminDisableInviteCodes](#admindisableinvitecodes-apiatprotoadmindisableinvitecodesgo20) `:20`


</details>


[function] name: AdminDisableInviteCodes file: api/atproto/admindisableInviteCodes.go:20 returns_error: нет description: AdminDisableInviteCodes calls the XRPC method "com.atproto.admin.disableInviteCodes".


### AdminDisableInviteCodes (api/atproto/admindisableInviteCodes.go:20)


AdminDisableInviteCodes calls the XRPC method "com.atproto.admin.disableInviteCodes".


```go
func AdminDisableInviteCodes((ctx context.Context, c lexutil.LexClient, input *AdminDisableInviteCodes_Input)) (ctx context.Context, c lexutil.LexClient, input *AdminDisableInviteCodes_Input)
```


**Тип запроса:** AdminDisableInviteCodes_Input


```json
{
  "accounts": [],
  "codes": []
}
```


*Определено в:* `api/atproto/admindisableInviteCodes.go`


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


**Тип ответа:** AdminDisableInviteCodes_Input


```json
{
  "accounts": [],
  "codes": []
}
```


*Определено в:* `api/atproto/admindisableInviteCodes.go`


📍 *Расположение:* `api/atproto/admindisableInviteCodes.go:20`




## api/atproto/adminenableAccountInvites.go


📄 Исходный файл: `api/atproto/adminenableAccountInvites.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminEnableAccountInvites](#adminenableaccountinvites-apiatprotoadminenableaccountinvitesgo21) `:21`


</details>


[function] name: AdminEnableAccountInvites file: api/atproto/adminenableAccountInvites.go:21 returns_error: нет description: AdminEnableAccountInvites calls the XRPC method "com.atproto.admin.enableAccountInvites".


### AdminEnableAccountInvites (api/atproto/adminenableAccountInvites.go:21)


AdminEnableAccountInvites calls the XRPC method "com.atproto.admin.enableAccountInvites".


```go
func AdminEnableAccountInvites((ctx context.Context, c lexutil.LexClient, input *AdminEnableAccountInvites_Input)) (ctx context.Context, c lexutil.LexClient, input *AdminEnableAccountInvites_Input)
```


**Тип запроса:** AdminEnableAccountInvites_Input


```json
{
  "account": "string",
  "note": "string"
}
```


*Определено в:* `api/atproto/adminenableAccountInvites.go`


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


**Тип ответа:** AdminEnableAccountInvites_Input


```json
{
  "account": "string",
  "note": "string"
}
```


*Определено в:* `api/atproto/adminenableAccountInvites.go`


📍 *Расположение:* `api/atproto/adminenableAccountInvites.go:21`




## api/atproto/admingetAccountInfo.go


📄 Исходный файл: `api/atproto/admingetAccountInfo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminGetAccountInfo](#admingetaccountinfo-apiatprotoadmingetaccountinfogo14) `:14`


</details>


[function] name: AdminGetAccountInfo file: api/atproto/admingetAccountInfo.go:14 returns_error: да description: AdminGetAccountInfo calls the XRPC method "com.atproto.admin.getAccountInfo".


### AdminGetAccountInfo (api/atproto/admingetAccountInfo.go:14)


AdminGetAccountInfo calls the XRPC method "com.atproto.admin.getAccountInfo".


```go
func AdminGetAccountInfo((*AdminDefs_AccountView, error)) (*AdminDefs_AccountView, error)
```


**Тип запроса:** AdminDefs_AccountView


```json
{
  "deactivatedAt": "string",
  "did": "string",
  "email": "string",
  "emailConfirmedAt": "string",
  "handle": "string",
  "indexedAt": "string",
  "inviteNote": "string",
  "invitedBy": null,
  "invites": [],
  "invitesDisabled": false,
  "relatedRecords": [],
  "threatSignatures": []
}
```


*Определено в:* `api/atproto/admindefs.go`


**Тип ответа:** AdminDefs_AccountView


```json
{
  "deactivatedAt": "string",
  "did": "string",
  "email": "string",
  "emailConfirmedAt": "string",
  "handle": "string",
  "indexedAt": "string",
  "inviteNote": "string",
  "invitedBy": null,
  "invites": [],
  "invitesDisabled": false,
  "relatedRecords": [],
  "threatSignatures": []
}
```


*Определено в:* `api/atproto/admindefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AdminDefs_AccountView`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/admingetAccountInfo.go:14`




## api/atproto/admingetAccountInfos.go


📄 Исходный файл: `api/atproto/admingetAccountInfos.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminGetAccountInfos](#admingetaccountinfos-apiatprotoadmingetaccountinfosgo19) `:19`


</details>


[function] name: AdminGetAccountInfos file: api/atproto/admingetAccountInfos.go:19 returns_error: да description: AdminGetAccountInfos calls the XRPC method "com.atproto.admin.getAccountInfos".


### AdminGetAccountInfos (api/atproto/admingetAccountInfos.go:19)


AdminGetAccountInfos calls the XRPC method "com.atproto.admin.getAccountInfos".


```go
func AdminGetAccountInfos((*AdminGetAccountInfos_Output, error)) (*AdminGetAccountInfos_Output, error)
```


**Тип запроса:** AdminGetAccountInfos_Output


```json
{
  "infos": []
}
```


*Определено в:* `api/atproto/admingetAccountInfos.go`


**Тип ответа:** AdminGetAccountInfos_Output


```json
{
  "infos": []
}
```


*Определено в:* `api/atproto/admingetAccountInfos.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AdminGetAccountInfos_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/admingetAccountInfos.go:19`




## api/atproto/admingetInviteCodes.go


📄 Исходный файл: `api/atproto/admingetInviteCodes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminGetInviteCodes](#admingetinvitecodes-apiatprotoadmingetinvitecodesgo20) `:20`


</details>


[function] name: AdminGetInviteCodes file: api/atproto/admingetInviteCodes.go:20 returns_error: да description: AdminGetInviteCodes calls the XRPC method "com.atproto.admin.getInviteCodes".


### AdminGetInviteCodes (api/atproto/admingetInviteCodes.go:20)


AdminGetInviteCodes calls the XRPC method "com.atproto.admin.getInviteCodes".


```go
func AdminGetInviteCodes((*AdminGetInviteCodes_Output, error)) (*AdminGetInviteCodes_Output, error)
```


**Тип запроса:** AdminGetInviteCodes_Output


```json
{
  "codes": [],
  "cursor": "string"
}
```


*Определено в:* `api/atproto/admingetInviteCodes.go`


**Тип ответа:** AdminGetInviteCodes_Output


```json
{
  "codes": [],
  "cursor": "string"
}
```


*Определено в:* `api/atproto/admingetInviteCodes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AdminGetInviteCodes_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/admingetInviteCodes.go:20`




## api/atproto/admingetSubjectStatus.go


📄 Исходный файл: `api/atproto/admingetSubjectStatus.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AdminGetSubjectStatus](#admingetsubjectstatus-apiatprotoadmingetsubjectstatusgo66) `:66`

- 🔗 [MarshalJSON](#marshaljson-apiatprotoadmingetsubjectstatusgo28) `:28`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiatprotoadmingetsubjectstatusgo44) `:44`


</details>


[function] name: AdminGetSubjectStatus file: api/atproto/admingetSubjectStatus.go:66 returns_error: да description: AdminGetSubjectStatus calls the XRPC method "com.atproto.admin.getSubjectStatus".


### AdminGetSubjectStatus (api/atproto/admingetSubjectStatus.go:66)


AdminGetSubjectStatus calls the XRPC method "com.atproto.admin.getSubjectStatus".


```go
func AdminGetSubjectStatus((*AdminGetSubjectStatus_Output, error)) (*AdminGetSubjectStatus_Output, error)
```


**Тип запроса:** AdminGetSubjectStatus_Output


```json
{
  "deactivated": null,
  "subject": null,
  "takedown": null
}
```


*Определено в:* `api/atproto/admingetSubjectStatus.go`


**Тип ответа:** AdminGetSubjectStatus_Output


```json
{
  "deactivated": null,
  "subject": null,
  "takedown": null
}
```


*Определено в:* `api/atproto/admingetSubjectStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AdminGetSubjectStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/admingetSubjectStatus.go:66`



---


[function] name: MarshalJSON file: api/atproto/admingetSubjectStatus.go:28 returns_error: да description: —


### MarshalJSON (api/atproto/admingetSubjectStatus.go:28)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *AdminGetSubjectStatus_Output_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/admingetSubjectStatus.go:28`



---


[function] name: UnmarshalJSON file: api/atproto/admingetSubjectStatus.go:44 returns_error: нет description: —


### UnmarshalJSON (api/atproto/admingetSubjectStatus.go:44)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *AdminGetSubjectStatus_Output_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/atproto/admingetSubjectStatus.go:44`




## api/atproto/adminsearchAccounts.go


📄 Исходный файл: `api/atproto/adminsearchAccounts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminSearchAccounts](#adminsearchaccounts-apiatprotoadminsearchaccountsgo20) `:20`


</details>


[function] name: AdminSearchAccounts file: api/atproto/adminsearchAccounts.go:20 returns_error: да description: AdminSearchAccounts calls the XRPC method "com.atproto.admin.searchAccounts".


### AdminSearchAccounts (api/atproto/adminsearchAccounts.go:20)


AdminSearchAccounts calls the XRPC method "com.atproto.admin.searchAccounts".


```go
func AdminSearchAccounts((*AdminSearchAccounts_Output, error)) (*AdminSearchAccounts_Output, error)
```


**Тип запроса:** AdminSearchAccounts_Output


```json
{
  "accounts": [],
  "cursor": "string"
}
```


*Определено в:* `api/atproto/adminsearchAccounts.go`


**Тип ответа:** AdminSearchAccounts_Output


```json
{
  "accounts": [],
  "cursor": "string"
}
```


*Определено в:* `api/atproto/adminsearchAccounts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AdminSearchAccounts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/adminsearchAccounts.go:20`




## api/atproto/adminsendEmail.go


📄 Исходный файл: `api/atproto/adminsendEmail.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminSendEmail](#adminsendemail-apiatprotoadminsendemailgo29) `:29`


</details>


[function] name: AdminSendEmail file: api/atproto/adminsendEmail.go:29 returns_error: да description: AdminSendEmail calls the XRPC method "com.atproto.admin.sendEmail".


### AdminSendEmail (api/atproto/adminsendEmail.go:29)


AdminSendEmail calls the XRPC method "com.atproto.admin.sendEmail".


```go
func AdminSendEmail((*AdminSendEmail_Output, error)) (*AdminSendEmail_Output, error)
```


**Тип запроса:** AdminSendEmail_Output


```json
{
  "sent": false
}
```


*Определено в:* `api/atproto/adminsendEmail.go`


**Тип ответа:** AdminSendEmail_Output


```json
{
  "sent": false
}
```


*Определено в:* `api/atproto/adminsendEmail.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AdminSendEmail_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/adminsendEmail.go:29`




## api/atproto/adminupdateAccountEmail.go


📄 Исходный файл: `api/atproto/adminupdateAccountEmail.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminUpdateAccountEmail](#adminupdateaccountemail-apiatprotoadminupdateaccountemailgo21) `:21`


</details>


[function] name: AdminUpdateAccountEmail file: api/atproto/adminupdateAccountEmail.go:21 returns_error: нет description: AdminUpdateAccountEmail calls the XRPC method "com.atproto.admin.updateAccountEmail".


### AdminUpdateAccountEmail (api/atproto/adminupdateAccountEmail.go:21)


AdminUpdateAccountEmail calls the XRPC method "com.atproto.admin.updateAccountEmail".


```go
func AdminUpdateAccountEmail((ctx context.Context, c lexutil.LexClient, input *AdminUpdateAccountEmail_Input)) (ctx context.Context, c lexutil.LexClient, input *AdminUpdateAccountEmail_Input)
```


**Тип запроса:** AdminUpdateAccountEmail_Input


```json
{
  "account": "string",
  "email": "string"
}
```


*Определено в:* `api/atproto/adminupdateAccountEmail.go`


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


**Тип ответа:** AdminUpdateAccountEmail_Input


```json
{
  "account": "string",
  "email": "string"
}
```


*Определено в:* `api/atproto/adminupdateAccountEmail.go`


📍 *Расположение:* `api/atproto/adminupdateAccountEmail.go:21`




## api/atproto/adminupdateAccountHandle.go


📄 Исходный файл: `api/atproto/adminupdateAccountHandle.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminUpdateAccountHandle](#adminupdateaccounthandle-apiatprotoadminupdateaccounthandlego20) `:20`


</details>


[function] name: AdminUpdateAccountHandle file: api/atproto/adminupdateAccountHandle.go:20 returns_error: нет description: AdminUpdateAccountHandle calls the XRPC method "com.atproto.admin.updateAccountHandle".


### AdminUpdateAccountHandle (api/atproto/adminupdateAccountHandle.go:20)


AdminUpdateAccountHandle calls the XRPC method "com.atproto.admin.updateAccountHandle".


```go
func AdminUpdateAccountHandle((ctx context.Context, c lexutil.LexClient, input *AdminUpdateAccountHandle_Input)) (ctx context.Context, c lexutil.LexClient, input *AdminUpdateAccountHandle_Input)
```


**Тип запроса:** AdminUpdateAccountHandle_Input


```json
{
  "did": "string",
  "handle": "string"
}
```


*Определено в:* `api/atproto/adminupdateAccountHandle.go`


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


**Тип ответа:** AdminUpdateAccountHandle_Input


```json
{
  "did": "string",
  "handle": "string"
}
```


*Определено в:* `api/atproto/adminupdateAccountHandle.go`


📍 *Расположение:* `api/atproto/adminupdateAccountHandle.go:20`




## api/atproto/adminupdateAccountPassword.go


📄 Исходный файл: `api/atproto/adminupdateAccountPassword.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminUpdateAccountPassword](#adminupdateaccountpassword-apiatprotoadminupdateaccountpasswordgo20) `:20`


</details>


[function] name: AdminUpdateAccountPassword file: api/atproto/adminupdateAccountPassword.go:20 returns_error: нет description: AdminUpdateAccountPassword calls the XRPC method "com.atproto.admin.updateAccountPassword".


### AdminUpdateAccountPassword (api/atproto/adminupdateAccountPassword.go:20)


AdminUpdateAccountPassword calls the XRPC method "com.atproto.admin.updateAccountPassword".


```go
func AdminUpdateAccountPassword((ctx context.Context, c lexutil.LexClient, input *AdminUpdateAccountPassword_Input)) (ctx context.Context, c lexutil.LexClient, input *AdminUpdateAccountPassword_Input)
```


**Тип запроса:** AdminUpdateAccountPassword_Input


```json
{
  "did": "string",
  "password": "string"
}
```


*Определено в:* `api/atproto/adminupdateAccountPassword.go`


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


**Тип ответа:** AdminUpdateAccountPassword_Input


```json
{
  "did": "string",
  "password": "string"
}
```


*Определено в:* `api/atproto/adminupdateAccountPassword.go`


📍 *Расположение:* `api/atproto/adminupdateAccountPassword.go:20`




## api/atproto/adminupdateAccountSigningKey.go


📄 Исходный файл: `api/atproto/adminupdateAccountSigningKey.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AdminUpdateAccountSigningKey](#adminupdateaccountsigningkey-apiatprotoadminupdateaccountsigningkeygo21) `:21`


</details>


[function] name: AdminUpdateAccountSigningKey file: api/atproto/adminupdateAccountSigningKey.go:21 returns_error: нет description: AdminUpdateAccountSigningKey calls the XRPC method "com.atproto.admin.updateAccountSigningKey".


### AdminUpdateAccountSigningKey (api/atproto/adminupdateAccountSigningKey.go:21)


AdminUpdateAccountSigningKey calls the XRPC method "com.atproto.admin.updateAccountSigningKey".


```go
func AdminUpdateAccountSigningKey((ctx context.Context, c lexutil.LexClient, input *AdminUpdateAccountSigningKey_Input)) (ctx context.Context, c lexutil.LexClient, input *AdminUpdateAccountSigningKey_Input)
```


**Тип запроса:** AdminUpdateAccountSigningKey_Input


```json
{
  "did": "string",
  "signingKey": "string"
}
```


*Определено в:* `api/atproto/adminupdateAccountSigningKey.go`


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


**Тип ответа:** AdminUpdateAccountSigningKey_Input


```json
{
  "did": "string",
  "signingKey": "string"
}
```


*Определено в:* `api/atproto/adminupdateAccountSigningKey.go`


📍 *Расположение:* `api/atproto/adminupdateAccountSigningKey.go:21`




## api/atproto/adminupdateSubjectStatus.go


📄 Исходный файл: `api/atproto/adminupdateSubjectStatus.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [AdminUpdateSubjectStatus](#adminupdatesubjectstatus-apiatprotoadminupdatesubjectstatusgo115) `:115`

- 🔗 [MarshalJSON](#marshaljson-apiatprotoadminupdatesubjectstatusgo28) `:28`

- 🔗 [MarshalJSON](#marshaljson-apiatprotoadminupdatesubjectstatusgo77) `:77`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiatprotoadminupdatesubjectstatusgo44) `:44`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiatprotoadminupdatesubjectstatusgo93) `:93`


</details>


[function] name: AdminUpdateSubjectStatus file: api/atproto/adminupdateSubjectStatus.go:115 returns_error: да description: AdminUpdateSubjectStatus calls the XRPC method "com.atproto.admin.updateSubjectStatus".


### AdminUpdateSubjectStatus (api/atproto/adminupdateSubjectStatus.go:115)


AdminUpdateSubjectStatus calls the XRPC method "com.atproto.admin.updateSubjectStatus".


```go
func AdminUpdateSubjectStatus((*AdminUpdateSubjectStatus_Output, error)) (*AdminUpdateSubjectStatus_Output, error)
```


**Тип запроса:** AdminUpdateSubjectStatus_Output


```json
{
  "subject": null,
  "takedown": null
}
```


*Определено в:* `api/atproto/adminupdateSubjectStatus.go`


**Тип ответа:** AdminUpdateSubjectStatus_Output


```json
{
  "subject": null,
  "takedown": null
}
```


*Определено в:* `api/atproto/adminupdateSubjectStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AdminUpdateSubjectStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/adminupdateSubjectStatus.go:115`



---


[function] name: MarshalJSON file: api/atproto/adminupdateSubjectStatus.go:28 returns_error: да description: —


### MarshalJSON (api/atproto/adminupdateSubjectStatus.go:28)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *AdminUpdateSubjectStatus_Input_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/adminupdateSubjectStatus.go:28`



---


[function] name: MarshalJSON file: api/atproto/adminupdateSubjectStatus.go:77 returns_error: да description: —


### MarshalJSON (api/atproto/adminupdateSubjectStatus.go:77)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *AdminUpdateSubjectStatus_Output_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/adminupdateSubjectStatus.go:77`



---


[function] name: UnmarshalJSON file: api/atproto/adminupdateSubjectStatus.go:44 returns_error: нет description: —


### UnmarshalJSON (api/atproto/adminupdateSubjectStatus.go:44)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *AdminUpdateSubjectStatus_Input_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/atproto/adminupdateSubjectStatus.go:44`



---


[function] name: UnmarshalJSON file: api/atproto/adminupdateSubjectStatus.go:93 returns_error: нет description: —


### UnmarshalJSON (api/atproto/adminupdateSubjectStatus.go:93)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *AdminUpdateSubjectStatus_Output_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/atproto/adminupdateSubjectStatus.go:93`




## api/atproto/cbor_gen.go


📄 Исходный файл: `api/atproto/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (30)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo22) `:22`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo167) `:167`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo339) `:339`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo938) `:938`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo1209) `:1209`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo1449) `:1449`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo1723) `:1723`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo1881) `:1881`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo2095) `:2095`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo2286) `:2286`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo2386) `:2386`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo2892) `:2892`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo3081) `:3081`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo3239) `:3239`

- 🔗 [MarshalCBOR](#marshalcbor-apiatprotocbor_gengo3602) `:3602`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo78) `:78`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo254) `:254`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo629) `:629`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo1076) `:1076`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo1328) `:1328`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo1584) `:1584`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo1797) `:1797`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo1981) `:1981`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo2163) `:2163`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo2323) `:2323`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo2662) `:2662`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo2954) `:2954`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo3155) `:3155`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo3414) `:3414`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apiatprotocbor_gengo3685) `:3685`


</details>


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:22 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:22)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LexiconSchema) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:22`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:167 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:167)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *RepoStrongRef) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:167`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:339 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:339)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *SyncSubscribeRepos_Commit) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:339`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:938 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:938)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *SyncSubscribeRepos_Sync) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:938`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:1209 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:1209)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *SyncSubscribeRepos_Identity) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1209`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:1449 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:1449)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *SyncSubscribeRepos_Account) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1449`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:1723 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:1723)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *SyncSubscribeRepos_Info) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1723`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:1881 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:1881)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *SyncSubscribeRepos_RepoOp) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1881`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:2095 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:2095)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelDefs_SelfLabels) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:2095`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:2286 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:2286)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelDefs_SelfLabel) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:2286`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:2386 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:2386)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelDefs_Label) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:2386`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:2892 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:2892)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelSubscribeLabels_Labels) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:2892`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:3081 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:3081)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelSubscribeLabels_Info) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:3081`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:3239 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:3239)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelDefs_LabelValueDefinition) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:3239`



---


[function] name: MarshalCBOR file: api/atproto/cbor_gen.go:3602 returns_error: нет description: —


### MarshalCBOR (api/atproto/cbor_gen.go:3602)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelDefs_LabelValueDefinitionStrings) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:3602`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:78 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:78)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LexiconSchema) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:78`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:254 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:254)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RepoStrongRef) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:254`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:629 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:629)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *SyncSubscribeRepos_Commit) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:629`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:1076 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:1076)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *SyncSubscribeRepos_Sync) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1076`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:1328 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:1328)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *SyncSubscribeRepos_Identity) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1328`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:1584 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:1584)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *SyncSubscribeRepos_Account) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1584`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:1797 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:1797)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *SyncSubscribeRepos_Info) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1797`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:1981 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:1981)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *SyncSubscribeRepos_RepoOp) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:1981`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:2163 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:2163)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelDefs_SelfLabels) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:2163`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:2323 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:2323)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelDefs_SelfLabel) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:2323`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:2662 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:2662)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelDefs_Label) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:2662`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:2954 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:2954)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelSubscribeLabels_Labels) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:2954`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:3155 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:3155)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelSubscribeLabels_Info) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:3155`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:3414 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:3414)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelDefs_LabelValueDefinition) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:3414`



---


[function] name: UnmarshalCBOR file: api/atproto/cbor_gen.go:3685 returns_error: да description: —


### UnmarshalCBOR (api/atproto/cbor_gen.go:3685)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelDefs_LabelValueDefinitionStrings) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `api/atproto/cbor_gen.go:3685`




## api/atproto/identitygetRecommendedDidCredentials.go


📄 Исходный файл: `api/atproto/identitygetRecommendedDidCredentials.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentityGetRecommendedDidCredentials](#identitygetrecommendeddidcredentials-apiatprotoidentitygetrecommendeddidcredentialsgo23) `:23`


</details>


[function] name: IdentityGetRecommendedDidCredentials file: api/atproto/identitygetRecommendedDidCredentials.go:23 returns_error: да description: IdentityGetRecommendedDidCredentials calls the XRPC method "com.atproto.identity.getRecommendedDidCredentials".


### IdentityGetRecommendedDidCredentials (api/atproto/identitygetRecommendedDidCredentials.go:23)


IdentityGetRecommendedDidCredentials calls the XRPC method "com.atproto.identity.getRecommendedDidCredentials".


```go
func IdentityGetRecommendedDidCredentials((*IdentityGetRecommendedDidCredentials_Output, error)) (*IdentityGetRecommendedDidCredentials_Output, error)
```


**Тип запроса:** IdentityGetRecommendedDidCredentials_Output


```json
{
  "alsoKnownAs": [],
  "rotationKeys": [],
  "services": null,
  "verificationMethods": null
}
```


*Определено в:* `api/atproto/identitygetRecommendedDidCredentials.go`


**Тип ответа:** IdentityGetRecommendedDidCredentials_Output


```json
{
  "alsoKnownAs": [],
  "rotationKeys": [],
  "services": null,
  "verificationMethods": null
}
```


*Определено в:* `api/atproto/identitygetRecommendedDidCredentials.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*IdentityGetRecommendedDidCredentials_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/identitygetRecommendedDidCredentials.go:23`




## api/atproto/identityrefreshIdentity.go


📄 Исходный файл: `api/atproto/identityrefreshIdentity.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentityRefreshIdentity](#identityrefreshidentity-apiatprotoidentityrefreshidentitygo19) `:19`


</details>


[function] name: IdentityRefreshIdentity file: api/atproto/identityrefreshIdentity.go:19 returns_error: да description: IdentityRefreshIdentity calls the XRPC method "com.atproto.identity.refreshIdentity".


### IdentityRefreshIdentity (api/atproto/identityrefreshIdentity.go:19)


IdentityRefreshIdentity calls the XRPC method "com.atproto.identity.refreshIdentity".


```go
func IdentityRefreshIdentity((*IdentityDefs_IdentityInfo, error)) (*IdentityDefs_IdentityInfo, error)
```


**Тип запроса:** IdentityDefs_IdentityInfo


```json
{
  "did": "string",
  "didDoc": {},
  "handle": "string"
}
```


*Определено в:* `api/atproto/identitydefs.go`


**Тип ответа:** IdentityDefs_IdentityInfo


```json
{
  "did": "string",
  "didDoc": {},
  "handle": "string"
}
```


*Определено в:* `api/atproto/identitydefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*IdentityDefs_IdentityInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/identityrefreshIdentity.go:19`




## api/atproto/identityrequestPlcOperationSignature.go


📄 Исходный файл: `api/atproto/identityrequestPlcOperationSignature.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentityRequestPlcOperationSignature](#identityrequestplcoperationsignature-apiatprotoidentityrequestplcoperationsignaturego14) `:14`


</details>


[function] name: IdentityRequestPlcOperationSignature file: api/atproto/identityrequestPlcOperationSignature.go:14 returns_error: нет description: IdentityRequestPlcOperationSignature calls the XRPC method "com.atproto.identity.requestPlcOperationSignature".


### IdentityRequestPlcOperationSignature (api/atproto/identityrequestPlcOperationSignature.go:14)


IdentityRequestPlcOperationSignature calls the XRPC method "com.atproto.identity.requestPlcOperationSignature".


```go
func IdentityRequestPlcOperationSignature((ctx context.Context, c lexutil.LexClient)) (ctx context.Context, c lexutil.LexClient)
```


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


📍 *Расположение:* `api/atproto/identityrequestPlcOperationSignature.go:14`




## api/atproto/identityresolveDid.go


📄 Исходный файл: `api/atproto/identityresolveDid.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentityResolveDid](#identityresolvedid-apiatprotoidentityresolvedidgo22) `:22`


</details>


[function] name: IdentityResolveDid file: api/atproto/identityresolveDid.go:22 returns_error: да description: IdentityResolveDid calls the XRPC method "com.atproto.identity.resolveDid".

did: DID to resolve.


### IdentityResolveDid (api/atproto/identityresolveDid.go:22)


IdentityResolveDid calls the XRPC method "com.atproto.identity.resolveDid".

did: DID to resolve.


```go
func IdentityResolveDid((*IdentityResolveDid_Output, error)) (*IdentityResolveDid_Output, error)
```


**Тип запроса:** IdentityResolveDid_Output


```json
{
  "didDoc": {}
}
```


*Определено в:* `api/atproto/identityresolveDid.go`


**Тип ответа:** IdentityResolveDid_Output


```json
{
  "didDoc": {}
}
```


*Определено в:* `api/atproto/identityresolveDid.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*IdentityResolveDid_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/identityresolveDid.go:22`




## api/atproto/identityresolveHandle.go


📄 Исходный файл: `api/atproto/identityresolveHandle.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentityResolveHandle](#identityresolvehandle-apiatprotoidentityresolvehandlego21) `:21`


</details>


[function] name: IdentityResolveHandle file: api/atproto/identityresolveHandle.go:21 returns_error: да description: IdentityResolveHandle calls the XRPC method "com.atproto.identity.resolveHandle".

handle: The handle to resolve.


### IdentityResolveHandle (api/atproto/identityresolveHandle.go:21)


IdentityResolveHandle calls the XRPC method "com.atproto.identity.resolveHandle".

handle: The handle to resolve.


```go
func IdentityResolveHandle((*IdentityResolveHandle_Output, error)) (*IdentityResolveHandle_Output, error)
```


**Тип запроса:** IdentityResolveHandle_Output


```json
{
  "did": "string"
}
```


*Определено в:* `api/atproto/identityresolveHandle.go`


**Тип ответа:** IdentityResolveHandle_Output


```json
{
  "did": "string"
}
```


*Определено в:* `api/atproto/identityresolveHandle.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*IdentityResolveHandle_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/identityresolveHandle.go:21`




## api/atproto/identityresolveIdentity.go


📄 Исходный файл: `api/atproto/identityresolveIdentity.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentityResolveIdentity](#identityresolveidentity-apiatprotoidentityresolveidentitygo16) `:16`


</details>


[function] name: IdentityResolveIdentity file: api/atproto/identityresolveIdentity.go:16 returns_error: да description: IdentityResolveIdentity calls the XRPC method "com.atproto.identity.resolveIdentity".

identifier: Handle or DID to reso


### IdentityResolveIdentity (api/atproto/identityresolveIdentity.go:16)


IdentityResolveIdentity calls the XRPC method "com.atproto.identity.resolveIdentity".

identifier: Handle or DID to resolve.


```go
func IdentityResolveIdentity((*IdentityDefs_IdentityInfo, error)) (*IdentityDefs_IdentityInfo, error)
```


**Тип запроса:** IdentityDefs_IdentityInfo


```json
{
  "did": "string",
  "didDoc": {},
  "handle": "string"
}
```


*Определено в:* `api/atproto/identitydefs.go`


**Тип ответа:** IdentityDefs_IdentityInfo


```json
{
  "did": "string",
  "didDoc": {},
  "handle": "string"
}
```


*Определено в:* `api/atproto/identitydefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*IdentityDefs_IdentityInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/identityresolveIdentity.go:16`




## api/atproto/identitysignPlcOperation.go


📄 Исходный файл: `api/atproto/identitysignPlcOperation.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentitySignPlcOperation](#identitysignplcoperation-apiatprotoidentitysignplcoperationgo30) `:30`


</details>


[function] name: IdentitySignPlcOperation file: api/atproto/identitysignPlcOperation.go:30 returns_error: да description: IdentitySignPlcOperation calls the XRPC method "com.atproto.identity.signPlcOperation".


### IdentitySignPlcOperation (api/atproto/identitysignPlcOperation.go:30)


IdentitySignPlcOperation calls the XRPC method "com.atproto.identity.signPlcOperation".


```go
func IdentitySignPlcOperation((*IdentitySignPlcOperation_Output, error)) (*IdentitySignPlcOperation_Output, error)
```


**Тип запроса:** IdentitySignPlcOperation_Output


```json
{
  "operation": null
}
```


*Определено в:* `api/agnostic/identitysignPlcOperation.go`


**Тип ответа:** IdentitySignPlcOperation_Output


```json
{
  "operation": null
}
```


*Определено в:* `api/agnostic/identitysignPlcOperation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*IdentitySignPlcOperation_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/identitysignPlcOperation.go:30`




## api/atproto/identitysubmitPlcOperation.go


📄 Исходный файл: `api/atproto/identitysubmitPlcOperation.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentitySubmitPlcOperation](#identitysubmitplcoperation-apiatprotoidentitysubmitplcoperationgo19) `:19`


</details>


[function] name: IdentitySubmitPlcOperation file: api/atproto/identitysubmitPlcOperation.go:19 returns_error: нет description: IdentitySubmitPlcOperation calls the XRPC method "com.atproto.identity.submitPlcOperation".


### IdentitySubmitPlcOperation (api/atproto/identitysubmitPlcOperation.go:19)


IdentitySubmitPlcOperation calls the XRPC method "com.atproto.identity.submitPlcOperation".


```go
func IdentitySubmitPlcOperation((ctx context.Context, c lexutil.LexClient, input *IdentitySubmitPlcOperation_Input)) (ctx context.Context, c lexutil.LexClient, input *IdentitySubmitPlcOperation_Input)
```


**Тип запроса:** IdentitySubmitPlcOperation_Input


```json
{
  "operation": null
}
```


*Определено в:* `api/agnostic/identitysubmitPlcOperation.go`


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


**Тип ответа:** IdentitySubmitPlcOperation_Input


```json
{
  "operation": null
}
```


*Определено в:* `api/agnostic/identitysubmitPlcOperation.go`


📍 *Расположение:* `api/atproto/identitysubmitPlcOperation.go:19`




## api/atproto/identityupdateHandle.go


📄 Исходный файл: `api/atproto/identityupdateHandle.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IdentityUpdateHandle](#identityupdatehandle-apiatprotoidentityupdatehandlego20) `:20`


</details>


[function] name: IdentityUpdateHandle file: api/atproto/identityupdateHandle.go:20 returns_error: нет description: IdentityUpdateHandle calls the XRPC method "com.atproto.identity.updateHandle".


### IdentityUpdateHandle (api/atproto/identityupdateHandle.go:20)


IdentityUpdateHandle calls the XRPC method "com.atproto.identity.updateHandle".


```go
func IdentityUpdateHandle((ctx context.Context, c lexutil.LexClient, input *IdentityUpdateHandle_Input)) (ctx context.Context, c lexutil.LexClient, input *IdentityUpdateHandle_Input)
```


**Тип запроса:** IdentityUpdateHandle_Input


```json
{
  "handle": "string"
}
```


*Определено в:* `api/atproto/identityupdateHandle.go`


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


**Тип ответа:** IdentityUpdateHandle_Input


```json
{
  "handle": "string"
}
```


*Определено в:* `api/atproto/identityupdateHandle.go`


📍 *Расположение:* `api/atproto/identityupdateHandle.go:20`




## api/atproto/labelqueryLabels.go


📄 Исходный файл: `api/atproto/labelqueryLabels.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [LabelQueryLabels](#labelquerylabels-apiatprotolabelquerylabelsgo23) `:23`


</details>


[function] name: LabelQueryLabels file: api/atproto/labelqueryLabels.go:23 returns_error: да description: LabelQueryLabels calls the XRPC method "com.atproto.label.queryLabels".

sources: Optional list of label sources (DIDs) 


### LabelQueryLabels (api/atproto/labelqueryLabels.go:23)


LabelQueryLabels calls the XRPC method "com.atproto.label.queryLabels".

sources: Optional list of label sources (DIDs) to filter on.
uriPatterns: List of AT URI patterns to match (boolean 'OR'). Each may be a prefix (ending with '*'; will match inclusive of the string leading to '*'), or a full URI.


```go
func LabelQueryLabels((*LabelQueryLabels_Output, error)) (*LabelQueryLabels_Output, error)
```


**Тип запроса:** LabelQueryLabels_Output


```json
{
  "cursor": "string",
  "labels": []
}
```


*Определено в:* `api/atproto/labelqueryLabels.go`


**Тип ответа:** LabelQueryLabels_Output


```json
{
  "cursor": "string",
  "labels": []
}
```


*Определено в:* `api/atproto/labelqueryLabels.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*LabelQueryLabels_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/labelqueryLabels.go:23`




## api/atproto/lexiconschema.go


📄 Исходный файл: `api/atproto/lexiconschema.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apiatprotolexiconschemago11) `:11`


</details>


[function] name: init file: api/atproto/lexiconschema.go:11 returns_error: нет description: —


### init (api/atproto/lexiconschema.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/atproto/lexiconschema.go:11`




## api/atproto/moderationcreateReport.go


📄 Исходный файл: `api/atproto/moderationcreateReport.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiatprotomoderationcreatereportgo30) `:30`

- 🔗 [MarshalJSON](#marshaljson-apiatprotomoderationcreatereportgo85) `:85`

- 🔗 [ModerationCreateReport](#moderationcreatereport-apiatprotomoderationcreatereportgo116) `:116`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiatprotomoderationcreatereportgo42) `:42`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiatprotomoderationcreatereportgo97) `:97`


</details>


[function] name: MarshalJSON file: api/atproto/moderationcreateReport.go:30 returns_error: да description: —


### MarshalJSON (api/atproto/moderationcreateReport.go:30)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationCreateReport_Input_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/moderationcreateReport.go:30`



---


[function] name: MarshalJSON file: api/atproto/moderationcreateReport.go:85 returns_error: да description: —


### MarshalJSON (api/atproto/moderationcreateReport.go:85)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationCreateReport_Output_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/moderationcreateReport.go:85`



---


[function] name: ModerationCreateReport file: api/atproto/moderationcreateReport.go:116 returns_error: да description: ModerationCreateReport calls the XRPC method "com.atproto.moderation.createReport".


### ModerationCreateReport (api/atproto/moderationcreateReport.go:116)


ModerationCreateReport calls the XRPC method "com.atproto.moderation.createReport".


```go
func ModerationCreateReport((*ModerationCreateReport_Output, error)) (*ModerationCreateReport_Output, error)
```


**Тип запроса:** ModerationCreateReport_Output


```json
{
  "createdAt": "string",
  "id": 0,
  "reason": "string",
  "reasonType": "string",
  "reportedBy": "string",
  "subject": null
}
```


*Определено в:* `api/atproto/moderationcreateReport.go`


**Тип ответа:** ModerationCreateReport_Output


```json
{
  "createdAt": "string",
  "id": 0,
  "reason": "string",
  "reasonType": "string",
  "reportedBy": "string",
  "subject": null
}
```


*Определено в:* `api/atproto/moderationcreateReport.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationCreateReport_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/moderationcreateReport.go:116`



---


[function] name: UnmarshalJSON file: api/atproto/moderationcreateReport.go:42 returns_error: нет description: —


### UnmarshalJSON (api/atproto/moderationcreateReport.go:42)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationCreateReport_Input_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/atproto/moderationcreateReport.go:42`



---


[function] name: UnmarshalJSON file: api/atproto/moderationcreateReport.go:97 returns_error: нет description: —


### UnmarshalJSON (api/atproto/moderationcreateReport.go:97)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationCreateReport_Output_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/atproto/moderationcreateReport.go:97`




## api/atproto/repoapplyWrites.go


📄 Исходный файл: `api/atproto/repoapplyWrites.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiatprotorepoapplywritesgo65) `:65`

- 🔗 [MarshalJSON](#marshaljson-apiatprotorepoapplywritesgo114) `:114`

- 🔗 [RepoApplyWrites](#repoapplywrites-apiatprotorepoapplywritesgo170) `:170`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiatprotorepoapplywritesgo81) `:81`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiatprotorepoapplywritesgo130) `:130`


</details>


[function] name: MarshalJSON file: api/atproto/repoapplyWrites.go:65 returns_error: да description: —


### MarshalJSON (api/atproto/repoapplyWrites.go:65)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RepoApplyWrites_Input_Writes_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repoapplyWrites.go:65`



---


[function] name: MarshalJSON file: api/atproto/repoapplyWrites.go:114 returns_error: да description: —


### MarshalJSON (api/atproto/repoapplyWrites.go:114)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RepoApplyWrites_Output_Results_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repoapplyWrites.go:114`



---


[function] name: RepoApplyWrites file: api/atproto/repoapplyWrites.go:170 returns_error: да description: RepoApplyWrites calls the XRPC method "com.atproto.repo.applyWrites".


### RepoApplyWrites (api/atproto/repoapplyWrites.go:170)


RepoApplyWrites calls the XRPC method "com.atproto.repo.applyWrites".


```go
func RepoApplyWrites((*RepoApplyWrites_Output, error)) (*RepoApplyWrites_Output, error)
```


**Тип запроса:** RepoApplyWrites_Output


```json
{
  "commit": null,
  "results": []
}
```


*Определено в:* `api/agnostic/repoapplyWrites.go`


**Тип ответа:** RepoApplyWrites_Output


```json
{
  "commit": null,
  "results": []
}
```


*Определено в:* `api/agnostic/repoapplyWrites.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoApplyWrites_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repoapplyWrites.go:170`



---


[function] name: UnmarshalJSON file: api/atproto/repoapplyWrites.go:81 returns_error: нет description: —


### UnmarshalJSON (api/atproto/repoapplyWrites.go:81)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *RepoApplyWrites_Input_Writes_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/atproto/repoapplyWrites.go:81`



---


[function] name: UnmarshalJSON file: api/atproto/repoapplyWrites.go:130 returns_error: нет description: —


### UnmarshalJSON (api/atproto/repoapplyWrites.go:130)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *RepoApplyWrites_Output_Results_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/atproto/repoapplyWrites.go:130`




## api/atproto/repocreateRecord.go


📄 Исходный файл: `api/atproto/repocreateRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoCreateRecord](#repocreaterecord-apiatprotorepocreaterecordgo38) `:38`


</details>


[function] name: RepoCreateRecord file: api/atproto/repocreateRecord.go:38 returns_error: да description: RepoCreateRecord calls the XRPC method "com.atproto.repo.createRecord".


### RepoCreateRecord (api/atproto/repocreateRecord.go:38)


RepoCreateRecord calls the XRPC method "com.atproto.repo.createRecord".


```go
func RepoCreateRecord((*RepoCreateRecord_Output, error)) (*RepoCreateRecord_Output, error)
```


**Тип запроса:** RepoCreateRecord_Output


```json
{
  "cid": "string",
  "commit": null,
  "uri": "string",
  "validationStatus": "string"
}
```


*Определено в:* `api/agnostic/repocreateRecord.go`


**Тип ответа:** RepoCreateRecord_Output


```json
{
  "cid": "string",
  "commit": null,
  "uri": "string",
  "validationStatus": "string"
}
```


*Определено в:* `api/agnostic/repocreateRecord.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoCreateRecord_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repocreateRecord.go:38`




## api/atproto/repodeleteRecord.go


📄 Исходный файл: `api/atproto/repodeleteRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoDeleteRecord](#repodeleterecord-apiatprotorepodeleterecordgo33) `:33`


</details>


[function] name: RepoDeleteRecord file: api/atproto/repodeleteRecord.go:33 returns_error: да description: RepoDeleteRecord calls the XRPC method "com.atproto.repo.deleteRecord".


### RepoDeleteRecord (api/atproto/repodeleteRecord.go:33)


RepoDeleteRecord calls the XRPC method "com.atproto.repo.deleteRecord".


```go
func RepoDeleteRecord((*RepoDeleteRecord_Output, error)) (*RepoDeleteRecord_Output, error)
```


**Тип запроса:** RepoDeleteRecord_Output


```json
{
  "commit": null
}
```


*Определено в:* `api/atproto/repodeleteRecord.go`


**Тип ответа:** RepoDeleteRecord_Output


```json
{
  "commit": null
}
```


*Определено в:* `api/atproto/repodeleteRecord.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoDeleteRecord_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repodeleteRecord.go:33`




## api/atproto/repodescribeRepo.go


📄 Исходный файл: `api/atproto/repodescribeRepo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoDescribeRepo](#repodescriberepo-apiatprotorepodescriberepogo28) `:28`


</details>


[function] name: RepoDescribeRepo file: api/atproto/repodescribeRepo.go:28 returns_error: да description: RepoDescribeRepo calls the XRPC method "com.atproto.repo.describeRepo".

repo: The handle or DID of the repo.


### RepoDescribeRepo (api/atproto/repodescribeRepo.go:28)


RepoDescribeRepo calls the XRPC method "com.atproto.repo.describeRepo".

repo: The handle or DID of the repo.


```go
func RepoDescribeRepo((*RepoDescribeRepo_Output, error)) (*RepoDescribeRepo_Output, error)
```


**Тип запроса:** RepoDescribeRepo_Output


```json
{
  "collections": [],
  "did": "string",
  "didDoc": {},
  "handle": "string",
  "handleIsCorrect": false
}
```


*Определено в:* `api/atproto/repodescribeRepo.go`


**Тип ответа:** RepoDescribeRepo_Output


```json
{
  "collections": [],
  "did": "string",
  "didDoc": {},
  "handle": "string",
  "handleIsCorrect": false
}
```


*Определено в:* `api/atproto/repodescribeRepo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoDescribeRepo_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repodescribeRepo.go:28`




## api/atproto/repogetRecord.go


📄 Исходный файл: `api/atproto/repogetRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoGetRecord](#repogetrecord-apiatprotorepogetrecordgo26) `:26`


</details>


[function] name: RepoGetRecord file: api/atproto/repogetRecord.go:26 returns_error: да description: RepoGetRecord calls the XRPC method "com.atproto.repo.getRecord".

cid: The CID of the version of the record. If not spe


### RepoGetRecord (api/atproto/repogetRecord.go:26)


RepoGetRecord calls the XRPC method "com.atproto.repo.getRecord".

cid: The CID of the version of the record. If not specified, then return the most recent version.
collection: The NSID of the record collection.
repo: The handle or DID of the repo.
rkey: The Record Key.


```go
func RepoGetRecord((*RepoGetRecord_Output, error)) (*RepoGetRecord_Output, error)
```


**Тип запроса:** RepoGetRecord_Output


```json
{
  "cid": "string",
  "uri": "string",
  "value": null
}
```


*Определено в:* `api/agnostic/repogetRecord.go`


**Тип ответа:** RepoGetRecord_Output


```json
{
  "cid": "string",
  "uri": "string",
  "value": null
}
```


*Определено в:* `api/agnostic/repogetRecord.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoGetRecord_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repogetRecord.go:26`




## api/atproto/repoimportRepo.go


📄 Исходный файл: `api/atproto/repoimportRepo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoImportRepo](#repoimportrepo-apiatprotorepoimportrepogo15) `:15`


</details>


[function] name: RepoImportRepo file: api/atproto/repoimportRepo.go:15 returns_error: нет description: RepoImportRepo calls the XRPC method "com.atproto.repo.importRepo".


### RepoImportRepo (api/atproto/repoimportRepo.go:15)


RepoImportRepo calls the XRPC method "com.atproto.repo.importRepo".


```go
func RepoImportRepo((ctx context.Context, c lexutil.LexClient, input io.Reader)) (ctx context.Context, c lexutil.LexClient, input io.Reader)
```


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


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/atproto/repoimportRepo.go:15`




## api/atproto/repolistMissingBlobs.go


📄 Исходный файл: `api/atproto/repolistMissingBlobs.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoListMissingBlobs](#repolistmissingblobs-apiatprotorepolistmissingblobsgo26) `:26`


</details>


[function] name: RepoListMissingBlobs file: api/atproto/repolistMissingBlobs.go:26 returns_error: да description: RepoListMissingBlobs calls the XRPC method "com.atproto.repo.listMissingBlobs".


### RepoListMissingBlobs (api/atproto/repolistMissingBlobs.go:26)


RepoListMissingBlobs calls the XRPC method "com.atproto.repo.listMissingBlobs".


```go
func RepoListMissingBlobs((*RepoListMissingBlobs_Output, error)) (*RepoListMissingBlobs_Output, error)
```


**Тип запроса:** RepoListMissingBlobs_Output


```json
{
  "blobs": [],
  "cursor": "string"
}
```


*Определено в:* `api/atproto/repolistMissingBlobs.go`


**Тип ответа:** RepoListMissingBlobs_Output


```json
{
  "blobs": [],
  "cursor": "string"
}
```


*Определено в:* `api/atproto/repolistMissingBlobs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoListMissingBlobs_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repolistMissingBlobs.go:26`




## api/atproto/repolistRecords.go


📄 Исходный файл: `api/atproto/repolistRecords.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoListRecords](#repolistrecords-apiatprotorepolistrecordsgo32) `:32`


</details>


[function] name: RepoListRecords file: api/atproto/repolistRecords.go:32 returns_error: да description: RepoListRecords calls the XRPC method "com.atproto.repo.listRecords".

collection: The NSID of the record type.
limit: T


### RepoListRecords (api/atproto/repolistRecords.go:32)


RepoListRecords calls the XRPC method "com.atproto.repo.listRecords".

collection: The NSID of the record type.
limit: The number of records to return.
repo: The handle or DID of the repo.
reverse: Flag to reverse the order of the returned records.


```go
func RepoListRecords((*RepoListRecords_Output, error)) (*RepoListRecords_Output, error)
```


**Тип запроса:** RepoListRecords_Output


```json
{
  "cursor": "string",
  "records": []
}
```


*Определено в:* `api/agnostic/repolistRecords.go`


**Тип ответа:** RepoListRecords_Output


```json
{
  "cursor": "string",
  "records": []
}
```


*Определено в:* `api/agnostic/repolistRecords.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoListRecords_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repolistRecords.go:32`




## api/atproto/repoputRecord.go


📄 Исходный файл: `api/atproto/repoputRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoPutRecord](#repoputrecord-apiatprotorepoputrecordgo40) `:40`


</details>


[function] name: RepoPutRecord file: api/atproto/repoputRecord.go:40 returns_error: да description: RepoPutRecord calls the XRPC method "com.atproto.repo.putRecord".


### RepoPutRecord (api/atproto/repoputRecord.go:40)


RepoPutRecord calls the XRPC method "com.atproto.repo.putRecord".


```go
func RepoPutRecord((*RepoPutRecord_Output, error)) (*RepoPutRecord_Output, error)
```


**Тип запроса:** RepoPutRecord_Output


```json
{
  "cid": "string",
  "commit": null,
  "uri": "string",
  "validationStatus": "string"
}
```


*Определено в:* `api/agnostic/repoputRecord.go`


**Тип ответа:** RepoPutRecord_Output


```json
{
  "cid": "string",
  "commit": null,
  "uri": "string",
  "validationStatus": "string"
}
```


*Определено в:* `api/agnostic/repoputRecord.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoPutRecord_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repoputRecord.go:40`




## api/atproto/repostrongRef.go


📄 Исходный файл: `api/atproto/repostrongRef.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apiatprotorepostrongrefgo11) `:11`


</details>


[function] name: init file: api/atproto/repostrongRef.go:11 returns_error: нет description: —


### init (api/atproto/repostrongRef.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/atproto/repostrongRef.go:11`




## api/atproto/repouploadBlob.go


📄 Исходный файл: `api/atproto/repouploadBlob.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RepoUploadBlob](#repouploadblob-apiatprotorepouploadblobgo20) `:20`


</details>


[function] name: RepoUploadBlob file: api/atproto/repouploadBlob.go:20 returns_error: да description: RepoUploadBlob calls the XRPC method "com.atproto.repo.uploadBlob".


### RepoUploadBlob (api/atproto/repouploadBlob.go:20)


RepoUploadBlob calls the XRPC method "com.atproto.repo.uploadBlob".


```go
func RepoUploadBlob((*RepoUploadBlob_Output, error)) (*RepoUploadBlob_Output, error)
```


**Тип запроса:** RepoUploadBlob_Output


```json
{
  "blob": null
}
```


*Определено в:* `api/atproto/repouploadBlob.go`


**Тип ответа:** RepoUploadBlob_Output


```json
{
  "blob": null
}
```


*Определено в:* `api/atproto/repouploadBlob.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RepoUploadBlob_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/repouploadBlob.go:20`




## api/atproto/serveractivateAccount.go


📄 Исходный файл: `api/atproto/serveractivateAccount.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerActivateAccount](#serveractivateaccount-apiatprotoserveractivateaccountgo14) `:14`


</details>


[function] name: ServerActivateAccount file: api/atproto/serveractivateAccount.go:14 returns_error: нет description: ServerActivateAccount calls the XRPC method "com.atproto.server.activateAccount".


### ServerActivateAccount (api/atproto/serveractivateAccount.go:14)


ServerActivateAccount calls the XRPC method "com.atproto.server.activateAccount".


```go
func ServerActivateAccount((ctx context.Context, c lexutil.LexClient)) (ctx context.Context, c lexutil.LexClient)
```


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


📍 *Расположение:* `api/atproto/serveractivateAccount.go:14`




## api/atproto/servercheckAccountStatus.go


📄 Исходный файл: `api/atproto/servercheckAccountStatus.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerCheckAccountStatus](#servercheckaccountstatus-apiatprotoservercheckaccountstatusgo27) `:27`


</details>


[function] name: ServerCheckAccountStatus file: api/atproto/servercheckAccountStatus.go:27 returns_error: да description: ServerCheckAccountStatus calls the XRPC method "com.atproto.server.checkAccountStatus".


### ServerCheckAccountStatus (api/atproto/servercheckAccountStatus.go:27)


ServerCheckAccountStatus calls the XRPC method "com.atproto.server.checkAccountStatus".


```go
func ServerCheckAccountStatus((*ServerCheckAccountStatus_Output, error)) (*ServerCheckAccountStatus_Output, error)
```


**Тип запроса:** ServerCheckAccountStatus_Output


```json
{
  "activated": false,
  "expectedBlobs": 0,
  "importedBlobs": 0,
  "indexedRecords": 0,
  "privateStateValues": 0,
  "repoBlocks": 0,
  "repoCommit": "string",
  "repoRev": "string",
  "validDid": false
}
```


*Определено в:* `api/atproto/servercheckAccountStatus.go`


**Тип ответа:** ServerCheckAccountStatus_Output


```json
{
  "activated": false,
  "expectedBlobs": 0,
  "importedBlobs": 0,
  "indexedRecords": 0,
  "privateStateValues": 0,
  "repoBlocks": 0,
  "repoCommit": "string",
  "repoRev": "string",
  "validDid": false
}
```


*Определено в:* `api/atproto/servercheckAccountStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerCheckAccountStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servercheckAccountStatus.go:27`




## api/atproto/serverconfirmEmail.go


📄 Исходный файл: `api/atproto/serverconfirmEmail.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerConfirmEmail](#serverconfirmemail-apiatprotoserverconfirmemailgo20) `:20`


</details>


[function] name: ServerConfirmEmail file: api/atproto/serverconfirmEmail.go:20 returns_error: нет description: ServerConfirmEmail calls the XRPC method "com.atproto.server.confirmEmail".


### ServerConfirmEmail (api/atproto/serverconfirmEmail.go:20)


ServerConfirmEmail calls the XRPC method "com.atproto.server.confirmEmail".


```go
func ServerConfirmEmail((ctx context.Context, c lexutil.LexClient, input *ServerConfirmEmail_Input)) (ctx context.Context, c lexutil.LexClient, input *ServerConfirmEmail_Input)
```


**Тип запроса:** ServerConfirmEmail_Input


```json
{
  "email": "string",
  "token": "string"
}
```


*Определено в:* `api/atproto/serverconfirmEmail.go`


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


**Тип ответа:** ServerConfirmEmail_Input


```json
{
  "email": "string",
  "token": "string"
}
```


*Определено в:* `api/atproto/serverconfirmEmail.go`


📍 *Расположение:* `api/atproto/serverconfirmEmail.go:20`




## api/atproto/servercreateAccount.go


📄 Исходный файл: `api/atproto/servercreateAccount.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerCreateAccount](#servercreateaccount-apiatprotoservercreateaccountgo45) `:45`


</details>


[function] name: ServerCreateAccount file: api/atproto/servercreateAccount.go:45 returns_error: да description: ServerCreateAccount calls the XRPC method "com.atproto.server.createAccount".


### ServerCreateAccount (api/atproto/servercreateAccount.go:45)


ServerCreateAccount calls the XRPC method "com.atproto.server.createAccount".


```go
func ServerCreateAccount((*ServerCreateAccount_Output, error)) (*ServerCreateAccount_Output, error)
```


**Тип запроса:** ServerCreateAccount_Output


```json
{
  "accessJwt": "string",
  "did": "string",
  "didDoc": null,
  "handle": "string",
  "refreshJwt": "string"
}
```


*Определено в:* `api/atproto/servercreateAccount.go`


**Тип ответа:** ServerCreateAccount_Output


```json
{
  "accessJwt": "string",
  "did": "string",
  "didDoc": null,
  "handle": "string",
  "refreshJwt": "string"
}
```


*Определено в:* `api/atproto/servercreateAccount.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerCreateAccount_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servercreateAccount.go:45`




## api/atproto/servercreateAppPassword.go


📄 Исходный файл: `api/atproto/servercreateAppPassword.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerCreateAppPassword](#servercreateapppassword-apiatprotoservercreateapppasswordgo30) `:30`


</details>


[function] name: ServerCreateAppPassword file: api/atproto/servercreateAppPassword.go:30 returns_error: да description: ServerCreateAppPassword calls the XRPC method "com.atproto.server.createAppPassword".


### ServerCreateAppPassword (api/atproto/servercreateAppPassword.go:30)


ServerCreateAppPassword calls the XRPC method "com.atproto.server.createAppPassword".


```go
func ServerCreateAppPassword((*ServerCreateAppPassword_AppPassword, error)) (*ServerCreateAppPassword_AppPassword, error)
```


**Тип запроса:** ServerCreateAppPassword_AppPassword


```json
{
  "createdAt": "string",
  "name": "string",
  "password": "string",
  "privileged": false
}
```


*Определено в:* `api/atproto/servercreateAppPassword.go`


**Тип ответа:** ServerCreateAppPassword_AppPassword


```json
{
  "createdAt": "string",
  "name": "string",
  "password": "string",
  "privileged": false
}
```


*Определено в:* `api/atproto/servercreateAppPassword.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerCreateAppPassword_AppPassword`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servercreateAppPassword.go:30`




## api/atproto/servercreateInviteCode.go


📄 Исходный файл: `api/atproto/servercreateInviteCode.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerCreateInviteCode](#servercreateinvitecode-apiatprotoservercreateinvitecodego25) `:25`


</details>


[function] name: ServerCreateInviteCode file: api/atproto/servercreateInviteCode.go:25 returns_error: да description: ServerCreateInviteCode calls the XRPC method "com.atproto.server.createInviteCode".


### ServerCreateInviteCode (api/atproto/servercreateInviteCode.go:25)


ServerCreateInviteCode calls the XRPC method "com.atproto.server.createInviteCode".


```go
func ServerCreateInviteCode((*ServerCreateInviteCode_Output, error)) (*ServerCreateInviteCode_Output, error)
```


**Тип запроса:** ServerCreateInviteCode_Output


```json
{
  "code": "string"
}
```


*Определено в:* `api/atproto/servercreateInviteCode.go`


**Тип ответа:** ServerCreateInviteCode_Output


```json
{
  "code": "string"
}
```


*Определено в:* `api/atproto/servercreateInviteCode.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerCreateInviteCode_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servercreateInviteCode.go:25`




## api/atproto/servercreateInviteCodes.go


📄 Исходный файл: `api/atproto/servercreateInviteCodes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerCreateInviteCodes](#servercreateinvitecodes-apiatprotoservercreateinvitecodesgo32) `:32`


</details>


[function] name: ServerCreateInviteCodes file: api/atproto/servercreateInviteCodes.go:32 returns_error: да description: ServerCreateInviteCodes calls the XRPC method "com.atproto.server.createInviteCodes".


### ServerCreateInviteCodes (api/atproto/servercreateInviteCodes.go:32)


ServerCreateInviteCodes calls the XRPC method "com.atproto.server.createInviteCodes".


```go
func ServerCreateInviteCodes((*ServerCreateInviteCodes_Output, error)) (*ServerCreateInviteCodes_Output, error)
```


**Тип запроса:** ServerCreateInviteCodes_Output


```json
{
  "codes": []
}
```


*Определено в:* `api/atproto/servercreateInviteCodes.go`


**Тип ответа:** ServerCreateInviteCodes_Output


```json
{
  "codes": []
}
```


*Определено в:* `api/atproto/servercreateInviteCodes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerCreateInviteCodes_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servercreateInviteCodes.go:32`




## api/atproto/servercreateSession.go


📄 Исходный файл: `api/atproto/servercreateSession.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerCreateSession](#servercreatesession-apiatprotoservercreatesessiongo39) `:39`


</details>


[function] name: ServerCreateSession file: api/atproto/servercreateSession.go:39 returns_error: да description: ServerCreateSession calls the XRPC method "com.atproto.server.createSession".


### ServerCreateSession (api/atproto/servercreateSession.go:39)


ServerCreateSession calls the XRPC method "com.atproto.server.createSession".


```go
func ServerCreateSession((*ServerCreateSession_Output, error)) (*ServerCreateSession_Output, error)
```


**Тип запроса:** ServerCreateSession_Output


```json
{
  "accessJwt": "string",
  "active": false,
  "did": "string",
  "didDoc": null,
  "email": "string",
  "emailAuthFactor": false,
  "emailConfirmed": false,
  "handle": "string",
  "refreshJwt": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/servercreateSession.go`


**Тип ответа:** ServerCreateSession_Output


```json
{
  "accessJwt": "string",
  "active": false,
  "did": "string",
  "didDoc": null,
  "email": "string",
  "emailAuthFactor": false,
  "emailConfirmed": false,
  "handle": "string",
  "refreshJwt": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/servercreateSession.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerCreateSession_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servercreateSession.go:39`




## api/atproto/serverdeactivateAccount.go


📄 Исходный файл: `api/atproto/serverdeactivateAccount.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerDeactivateAccount](#serverdeactivateaccount-apiatprotoserverdeactivateaccountgo20) `:20`


</details>


[function] name: ServerDeactivateAccount file: api/atproto/serverdeactivateAccount.go:20 returns_error: нет description: ServerDeactivateAccount calls the XRPC method "com.atproto.server.deactivateAccount".


### ServerDeactivateAccount (api/atproto/serverdeactivateAccount.go:20)


ServerDeactivateAccount calls the XRPC method "com.atproto.server.deactivateAccount".


```go
func ServerDeactivateAccount((ctx context.Context, c lexutil.LexClient, input *ServerDeactivateAccount_Input)) (ctx context.Context, c lexutil.LexClient, input *ServerDeactivateAccount_Input)
```


**Тип запроса:** ServerDeactivateAccount_Input


```json
{
  "deleteAfter": "string"
}
```


*Определено в:* `api/atproto/serverdeactivateAccount.go`


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


**Тип ответа:** ServerDeactivateAccount_Input


```json
{
  "deleteAfter": "string"
}
```


*Определено в:* `api/atproto/serverdeactivateAccount.go`


📍 *Расположение:* `api/atproto/serverdeactivateAccount.go:20`




## api/atproto/serverdeleteAccount.go


📄 Исходный файл: `api/atproto/serverdeleteAccount.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerDeleteAccount](#serverdeleteaccount-apiatprotoserverdeleteaccountgo21) `:21`


</details>


[function] name: ServerDeleteAccount file: api/atproto/serverdeleteAccount.go:21 returns_error: нет description: ServerDeleteAccount calls the XRPC method "com.atproto.server.deleteAccount".


### ServerDeleteAccount (api/atproto/serverdeleteAccount.go:21)


ServerDeleteAccount calls the XRPC method "com.atproto.server.deleteAccount".


```go
func ServerDeleteAccount((ctx context.Context, c lexutil.LexClient, input *ServerDeleteAccount_Input)) (ctx context.Context, c lexutil.LexClient, input *ServerDeleteAccount_Input)
```


**Тип запроса:** ServerDeleteAccount_Input


```json
{
  "did": "string",
  "password": "string",
  "token": "string"
}
```


*Определено в:* `api/atproto/serverdeleteAccount.go`


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


**Тип ответа:** ServerDeleteAccount_Input


```json
{
  "did": "string",
  "password": "string",
  "token": "string"
}
```


*Определено в:* `api/atproto/serverdeleteAccount.go`


📍 *Расположение:* `api/atproto/serverdeleteAccount.go:21`




## api/atproto/serverdeleteSession.go


📄 Исходный файл: `api/atproto/serverdeleteSession.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerDeleteSession](#serverdeletesession-apiatprotoserverdeletesessiongo14) `:14`


</details>


[function] name: ServerDeleteSession file: api/atproto/serverdeleteSession.go:14 returns_error: нет description: ServerDeleteSession calls the XRPC method "com.atproto.server.deleteSession".


### ServerDeleteSession (api/atproto/serverdeleteSession.go:14)


ServerDeleteSession calls the XRPC method "com.atproto.server.deleteSession".


```go
func ServerDeleteSession((ctx context.Context, c lexutil.LexClient)) (ctx context.Context, c lexutil.LexClient)
```


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


📍 *Расположение:* `api/atproto/serverdeleteSession.go:14`




## api/atproto/serverdescribeServer.go


📄 Исходный файл: `api/atproto/serverdescribeServer.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerDescribeServer](#serverdescribeserver-apiatprotoserverdescribeservergo40) `:40`


</details>


[function] name: ServerDescribeServer file: api/atproto/serverdescribeServer.go:40 returns_error: да description: ServerDescribeServer calls the XRPC method "com.atproto.server.describeServer".


### ServerDescribeServer (api/atproto/serverdescribeServer.go:40)


ServerDescribeServer calls the XRPC method "com.atproto.server.describeServer".


```go
func ServerDescribeServer((*ServerDescribeServer_Output, error)) (*ServerDescribeServer_Output, error)
```


**Тип запроса:** ServerDescribeServer_Output


```json
{
  "availableUserDomains": [],
  "contact": null,
  "did": "string",
  "inviteCodeRequired": false,
  "links": null,
  "phoneVerificationRequired": false
}
```


*Определено в:* `api/atproto/serverdescribeServer.go`


**Тип ответа:** ServerDescribeServer_Output


```json
{
  "availableUserDomains": [],
  "contact": null,
  "did": "string",
  "inviteCodeRequired": false,
  "links": null,
  "phoneVerificationRequired": false
}
```


*Определено в:* `api/atproto/serverdescribeServer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerDescribeServer_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/serverdescribeServer.go:40`




## api/atproto/servergetAccountInviteCodes.go


📄 Исходный файл: `api/atproto/servergetAccountInviteCodes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerGetAccountInviteCodes](#servergetaccountinvitecodes-apiatprotoservergetaccountinvitecodesgo21) `:21`


</details>


[function] name: ServerGetAccountInviteCodes file: api/atproto/servergetAccountInviteCodes.go:21 returns_error: да description: ServerGetAccountInviteCodes calls the XRPC method "com.atproto.server.getAccountInviteCodes".

createAvailable: Controls


### ServerGetAccountInviteCodes (api/atproto/servergetAccountInviteCodes.go:21)


ServerGetAccountInviteCodes calls the XRPC method "com.atproto.server.getAccountInviteCodes".

createAvailable: Controls whether any new 'earned' but not 'created' invites should be created.


```go
func ServerGetAccountInviteCodes((*ServerGetAccountInviteCodes_Output, error)) (*ServerGetAccountInviteCodes_Output, error)
```


**Тип запроса:** ServerGetAccountInviteCodes_Output


```json
{
  "codes": []
}
```


*Определено в:* `api/atproto/servergetAccountInviteCodes.go`


**Тип ответа:** ServerGetAccountInviteCodes_Output


```json
{
  "codes": []
}
```


*Определено в:* `api/atproto/servergetAccountInviteCodes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerGetAccountInviteCodes_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servergetAccountInviteCodes.go:21`




## api/atproto/servergetServiceAuth.go


📄 Исходный файл: `api/atproto/servergetServiceAuth.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerGetServiceAuth](#servergetserviceauth-apiatprotoservergetserviceauthgo23) `:23`


</details>


[function] name: ServerGetServiceAuth file: api/atproto/servergetServiceAuth.go:23 returns_error: да description: ServerGetServiceAuth calls the XRPC method "com.atproto.server.getServiceAuth".

aud: The DID of the service that the to


### ServerGetServiceAuth (api/atproto/servergetServiceAuth.go:23)


ServerGetServiceAuth calls the XRPC method "com.atproto.server.getServiceAuth".

aud: The DID of the service that the token will be used to authenticate with
exp: The time in Unix Epoch seconds that the JWT expires. Defaults to 60 seconds in the future. The service may enforce certain time bounds on tokens depending on the requested scope.
lxm: Lexicon (XRPC) method to bind the requested token to


```go
func ServerGetServiceAuth((*ServerGetServiceAuth_Output, error)) (*ServerGetServiceAuth_Output, error)
```


**Тип запроса:** ServerGetServiceAuth_Output


```json
{
  "token": "string"
}
```


*Определено в:* `api/atproto/servergetServiceAuth.go`


**Тип ответа:** ServerGetServiceAuth_Output


```json
{
  "token": "string"
}
```


*Определено в:* `api/atproto/servergetServiceAuth.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerGetServiceAuth_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servergetServiceAuth.go:23`




## api/atproto/servergetSession.go


📄 Исходный файл: `api/atproto/servergetSession.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerGetSession](#servergetsession-apiatprotoservergetsessiongo27) `:27`


</details>


[function] name: ServerGetSession file: api/atproto/servergetSession.go:27 returns_error: да description: ServerGetSession calls the XRPC method "com.atproto.server.getSession".


### ServerGetSession (api/atproto/servergetSession.go:27)


ServerGetSession calls the XRPC method "com.atproto.server.getSession".


```go
func ServerGetSession((*ServerGetSession_Output, error)) (*ServerGetSession_Output, error)
```


**Тип запроса:** ServerGetSession_Output


```json
{
  "active": false,
  "did": "string",
  "didDoc": null,
  "email": "string",
  "emailAuthFactor": false,
  "emailConfirmed": false,
  "handle": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/servergetSession.go`


**Тип ответа:** ServerGetSession_Output


```json
{
  "active": false,
  "did": "string",
  "didDoc": null,
  "email": "string",
  "emailAuthFactor": false,
  "emailConfirmed": false,
  "handle": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/servergetSession.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerGetSession_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/servergetSession.go:27`




## api/atproto/serverlistAppPasswords.go


📄 Исходный файл: `api/atproto/serverlistAppPasswords.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerListAppPasswords](#serverlistapppasswords-apiatprotoserverlistapppasswordsgo26) `:26`


</details>


[function] name: ServerListAppPasswords file: api/atproto/serverlistAppPasswords.go:26 returns_error: да description: ServerListAppPasswords calls the XRPC method "com.atproto.server.listAppPasswords".


### ServerListAppPasswords (api/atproto/serverlistAppPasswords.go:26)


ServerListAppPasswords calls the XRPC method "com.atproto.server.listAppPasswords".


```go
func ServerListAppPasswords((*ServerListAppPasswords_Output, error)) (*ServerListAppPasswords_Output, error)
```


**Тип запроса:** ServerListAppPasswords_Output


```json
{
  "passwords": []
}
```


*Определено в:* `api/atproto/serverlistAppPasswords.go`


**Тип ответа:** ServerListAppPasswords_Output


```json
{
  "passwords": []
}
```


*Определено в:* `api/atproto/serverlistAppPasswords.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerListAppPasswords_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/serverlistAppPasswords.go:26`




## api/atproto/serverrefreshSession.go


📄 Исходный файл: `api/atproto/serverrefreshSession.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerRefreshSession](#serverrefreshsession-apiatprotoserverrefreshsessiongo26) `:26`


</details>


[function] name: ServerRefreshSession file: api/atproto/serverrefreshSession.go:26 returns_error: да description: ServerRefreshSession calls the XRPC method "com.atproto.server.refreshSession".


### ServerRefreshSession (api/atproto/serverrefreshSession.go:26)


ServerRefreshSession calls the XRPC method "com.atproto.server.refreshSession".


```go
func ServerRefreshSession((*ServerRefreshSession_Output, error)) (*ServerRefreshSession_Output, error)
```


**Тип запроса:** ServerRefreshSession_Output


```json
{
  "accessJwt": "string",
  "active": false,
  "did": "string",
  "didDoc": null,
  "handle": "string",
  "refreshJwt": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/serverrefreshSession.go`


**Тип ответа:** ServerRefreshSession_Output


```json
{
  "accessJwt": "string",
  "active": false,
  "did": "string",
  "didDoc": null,
  "handle": "string",
  "refreshJwt": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/serverrefreshSession.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerRefreshSession_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/serverrefreshSession.go:26`




## api/atproto/serverrequestAccountDelete.go


📄 Исходный файл: `api/atproto/serverrequestAccountDelete.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerRequestAccountDelete](#serverrequestaccountdelete-apiatprotoserverrequestaccountdeletego14) `:14`


</details>


[function] name: ServerRequestAccountDelete file: api/atproto/serverrequestAccountDelete.go:14 returns_error: нет description: ServerRequestAccountDelete calls the XRPC method "com.atproto.server.requestAccountDelete".


### ServerRequestAccountDelete (api/atproto/serverrequestAccountDelete.go:14)


ServerRequestAccountDelete calls the XRPC method "com.atproto.server.requestAccountDelete".


```go
func ServerRequestAccountDelete((ctx context.Context, c lexutil.LexClient)) (ctx context.Context, c lexutil.LexClient)
```


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


📍 *Расположение:* `api/atproto/serverrequestAccountDelete.go:14`




## api/atproto/serverrequestEmailConfirmation.go


📄 Исходный файл: `api/atproto/serverrequestEmailConfirmation.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerRequestEmailConfirmation](#serverrequestemailconfirmation-apiatprotoserverrequestemailconfirmationgo14) `:14`


</details>


[function] name: ServerRequestEmailConfirmation file: api/atproto/serverrequestEmailConfirmation.go:14 returns_error: нет description: ServerRequestEmailConfirmation calls the XRPC method "com.atproto.server.requestEmailConfirmation".


### ServerRequestEmailConfirmation (api/atproto/serverrequestEmailConfirmation.go:14)


ServerRequestEmailConfirmation calls the XRPC method "com.atproto.server.requestEmailConfirmation".


```go
func ServerRequestEmailConfirmation((ctx context.Context, c lexutil.LexClient)) (ctx context.Context, c lexutil.LexClient)
```


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


📍 *Расположение:* `api/atproto/serverrequestEmailConfirmation.go:14`




## api/atproto/serverrequestEmailUpdate.go


📄 Исходный файл: `api/atproto/serverrequestEmailUpdate.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerRequestEmailUpdate](#serverrequestemailupdate-apiatprotoserverrequestemailupdatego19) `:19`


</details>


[function] name: ServerRequestEmailUpdate file: api/atproto/serverrequestEmailUpdate.go:19 returns_error: да description: ServerRequestEmailUpdate calls the XRPC method "com.atproto.server.requestEmailUpdate".


### ServerRequestEmailUpdate (api/atproto/serverrequestEmailUpdate.go:19)


ServerRequestEmailUpdate calls the XRPC method "com.atproto.server.requestEmailUpdate".


```go
func ServerRequestEmailUpdate((*ServerRequestEmailUpdate_Output, error)) (*ServerRequestEmailUpdate_Output, error)
```


**Тип запроса:** ServerRequestEmailUpdate_Output


```json
{
  "tokenRequired": false
}
```


*Определено в:* `api/atproto/serverrequestEmailUpdate.go`


**Тип ответа:** ServerRequestEmailUpdate_Output


```json
{
  "tokenRequired": false
}
```


*Определено в:* `api/atproto/serverrequestEmailUpdate.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerRequestEmailUpdate_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/serverrequestEmailUpdate.go:19`




## api/atproto/serverrequestPasswordReset.go


📄 Исходный файл: `api/atproto/serverrequestPasswordReset.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerRequestPasswordReset](#serverrequestpasswordreset-apiatprotoserverrequestpasswordresetgo19) `:19`


</details>


[function] name: ServerRequestPasswordReset file: api/atproto/serverrequestPasswordReset.go:19 returns_error: нет description: ServerRequestPasswordReset calls the XRPC method "com.atproto.server.requestPasswordReset".


### ServerRequestPasswordReset (api/atproto/serverrequestPasswordReset.go:19)


ServerRequestPasswordReset calls the XRPC method "com.atproto.server.requestPasswordReset".


```go
func ServerRequestPasswordReset((ctx context.Context, c lexutil.LexClient, input *ServerRequestPasswordReset_Input)) (ctx context.Context, c lexutil.LexClient, input *ServerRequestPasswordReset_Input)
```


**Тип запроса:** ServerRequestPasswordReset_Input


```json
{
  "email": "string"
}
```


*Определено в:* `api/atproto/serverrequestPasswordReset.go`


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


**Тип ответа:** ServerRequestPasswordReset_Input


```json
{
  "email": "string"
}
```


*Определено в:* `api/atproto/serverrequestPasswordReset.go`


📍 *Расположение:* `api/atproto/serverrequestPasswordReset.go:19`




## api/atproto/serverreserveSigningKey.go


📄 Исходный файл: `api/atproto/serverreserveSigningKey.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerReserveSigningKey](#serverreservesigningkey-apiatprotoserverreservesigningkeygo26) `:26`


</details>


[function] name: ServerReserveSigningKey file: api/atproto/serverreserveSigningKey.go:26 returns_error: да description: ServerReserveSigningKey calls the XRPC method "com.atproto.server.reserveSigningKey".


### ServerReserveSigningKey (api/atproto/serverreserveSigningKey.go:26)


ServerReserveSigningKey calls the XRPC method "com.atproto.server.reserveSigningKey".


```go
func ServerReserveSigningKey((*ServerReserveSigningKey_Output, error)) (*ServerReserveSigningKey_Output, error)
```


**Тип запроса:** ServerReserveSigningKey_Output


```json
{
  "signingKey": "string"
}
```


*Определено в:* `api/atproto/serverreserveSigningKey.go`


**Тип ответа:** ServerReserveSigningKey_Output


```json
{
  "signingKey": "string"
}
```


*Определено в:* `api/atproto/serverreserveSigningKey.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerReserveSigningKey_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/serverreserveSigningKey.go:26`




## api/atproto/serverresetPassword.go


📄 Исходный файл: `api/atproto/serverresetPassword.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerResetPassword](#serverresetpassword-apiatprotoserverresetpasswordgo20) `:20`


</details>


[function] name: ServerResetPassword file: api/atproto/serverresetPassword.go:20 returns_error: нет description: ServerResetPassword calls the XRPC method "com.atproto.server.resetPassword".


### ServerResetPassword (api/atproto/serverresetPassword.go:20)


ServerResetPassword calls the XRPC method "com.atproto.server.resetPassword".


```go
func ServerResetPassword((ctx context.Context, c lexutil.LexClient, input *ServerResetPassword_Input)) (ctx context.Context, c lexutil.LexClient, input *ServerResetPassword_Input)
```


**Тип запроса:** ServerResetPassword_Input


```json
{
  "password": "string",
  "token": "string"
}
```


*Определено в:* `api/atproto/serverresetPassword.go`


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


**Тип ответа:** ServerResetPassword_Input


```json
{
  "password": "string",
  "token": "string"
}
```


*Определено в:* `api/atproto/serverresetPassword.go`


📍 *Расположение:* `api/atproto/serverresetPassword.go:20`




## api/atproto/serverrevokeAppPassword.go


📄 Исходный файл: `api/atproto/serverrevokeAppPassword.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerRevokeAppPassword](#serverrevokeapppassword-apiatprotoserverrevokeapppasswordgo19) `:19`


</details>


[function] name: ServerRevokeAppPassword file: api/atproto/serverrevokeAppPassword.go:19 returns_error: нет description: ServerRevokeAppPassword calls the XRPC method "com.atproto.server.revokeAppPassword".


### ServerRevokeAppPassword (api/atproto/serverrevokeAppPassword.go:19)


ServerRevokeAppPassword calls the XRPC method "com.atproto.server.revokeAppPassword".


```go
func ServerRevokeAppPassword((ctx context.Context, c lexutil.LexClient, input *ServerRevokeAppPassword_Input)) (ctx context.Context, c lexutil.LexClient, input *ServerRevokeAppPassword_Input)
```


**Тип запроса:** ServerRevokeAppPassword_Input


```json
{
  "name": "string"
}
```


*Определено в:* `api/atproto/serverrevokeAppPassword.go`


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


**Тип ответа:** ServerRevokeAppPassword_Input


```json
{
  "name": "string"
}
```


*Определено в:* `api/atproto/serverrevokeAppPassword.go`


📍 *Расположение:* `api/atproto/serverrevokeAppPassword.go:19`




## api/atproto/serverupdateEmail.go


📄 Исходный файл: `api/atproto/serverupdateEmail.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerUpdateEmail](#serverupdateemail-apiatprotoserverupdateemailgo22) `:22`


</details>


[function] name: ServerUpdateEmail file: api/atproto/serverupdateEmail.go:22 returns_error: нет description: ServerUpdateEmail calls the XRPC method "com.atproto.server.updateEmail".


### ServerUpdateEmail (api/atproto/serverupdateEmail.go:22)


ServerUpdateEmail calls the XRPC method "com.atproto.server.updateEmail".


```go
func ServerUpdateEmail((ctx context.Context, c lexutil.LexClient, input *ServerUpdateEmail_Input)) (ctx context.Context, c lexutil.LexClient, input *ServerUpdateEmail_Input)
```


**Тип запроса:** ServerUpdateEmail_Input


```json
{
  "email": "string",
  "emailAuthFactor": false,
  "token": "string"
}
```


*Определено в:* `api/atproto/serverupdateEmail.go`


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


**Тип ответа:** ServerUpdateEmail_Input


```json
{
  "email": "string",
  "emailAuthFactor": false,
  "token": "string"
}
```


*Определено в:* `api/atproto/serverupdateEmail.go`


📍 *Расположение:* `api/atproto/serverupdateEmail.go:22`




## api/atproto/syncgetBlob.go


📄 Исходный файл: `api/atproto/syncgetBlob.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetBlob](#syncgetblob-apiatprotosyncgetblobgo18) `:18`


</details>


[function] name: SyncGetBlob file: api/atproto/syncgetBlob.go:18 returns_error: да description: SyncGetBlob calls the XRPC method "com.atproto.sync.getBlob".

cid: The CID of the blob to fetch
did: The DID of the acc


### SyncGetBlob (api/atproto/syncgetBlob.go:18)


SyncGetBlob calls the XRPC method "com.atproto.sync.getBlob".

cid: The CID of the blob to fetch
did: The DID of the account.


```go
func SyncGetBlob(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetBlob.go:18`




## api/atproto/syncgetBlocks.go


📄 Исходный файл: `api/atproto/syncgetBlocks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetBlocks](#syncgetblocks-apiatprotosyncgetblocksgo17) `:17`


</details>


[function] name: SyncGetBlocks file: api/atproto/syncgetBlocks.go:17 returns_error: да description: SyncGetBlocks calls the XRPC method "com.atproto.sync.getBlocks".

did: The DID of the repo.


### SyncGetBlocks (api/atproto/syncgetBlocks.go:17)


SyncGetBlocks calls the XRPC method "com.atproto.sync.getBlocks".

did: The DID of the repo.


```go
func SyncGetBlocks(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetBlocks.go:17`




## api/atproto/syncgetCheckout.go


📄 Исходный файл: `api/atproto/syncgetCheckout.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetCheckout](#syncgetcheckout-apiatprotosyncgetcheckoutgo17) `:17`


</details>


[function] name: SyncGetCheckout file: api/atproto/syncgetCheckout.go:17 returns_error: да description: SyncGetCheckout calls the XRPC method "com.atproto.sync.getCheckout".

did: The DID of the repo.


### SyncGetCheckout (api/atproto/syncgetCheckout.go:17)


SyncGetCheckout calls the XRPC method "com.atproto.sync.getCheckout".

did: The DID of the repo.


```go
func SyncGetCheckout(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetCheckout.go:17`




## api/atproto/syncgetHead.go


📄 Исходный файл: `api/atproto/syncgetHead.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetHead](#syncgethead-apiatprotosyncgetheadgo21) `:21`


</details>


[function] name: SyncGetHead file: api/atproto/syncgetHead.go:21 returns_error: да description: SyncGetHead calls the XRPC method "com.atproto.sync.getHead".

did: The DID of the repo.


### SyncGetHead (api/atproto/syncgetHead.go:21)


SyncGetHead calls the XRPC method "com.atproto.sync.getHead".

did: The DID of the repo.


```go
func SyncGetHead((*SyncGetHead_Output, error)) (*SyncGetHead_Output, error)
```


**Тип запроса:** SyncGetHead_Output


```json
{
  "root": "string"
}
```


*Определено в:* `api/atproto/syncgetHead.go`


**Тип ответа:** SyncGetHead_Output


```json
{
  "root": "string"
}
```


*Определено в:* `api/atproto/syncgetHead.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SyncGetHead_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetHead.go:21`




## api/atproto/syncgetHostStatus.go


📄 Исходный файл: `api/atproto/syncgetHostStatus.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetHostStatus](#syncgethoststatus-apiatprotosyncgethoststatusgo26) `:26`


</details>


[function] name: SyncGetHostStatus file: api/atproto/syncgetHostStatus.go:26 returns_error: да description: SyncGetHostStatus calls the XRPC method "com.atproto.sync.getHostStatus".

hostname: Hostname of the host (eg, PDS or re


### SyncGetHostStatus (api/atproto/syncgetHostStatus.go:26)


SyncGetHostStatus calls the XRPC method "com.atproto.sync.getHostStatus".

hostname: Hostname of the host (eg, PDS or relay) being queried.


```go
func SyncGetHostStatus((*SyncGetHostStatus_Output, error)) (*SyncGetHostStatus_Output, error)
```


**Тип запроса:** SyncGetHostStatus_Output


```json
{
  "accountCount": 0,
  "hostname": "string",
  "seq": 0,
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetHostStatus.go`


**Тип ответа:** SyncGetHostStatus_Output


```json
{
  "accountCount": 0,
  "hostname": "string",
  "seq": 0,
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetHostStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SyncGetHostStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetHostStatus.go:26`




## api/atproto/syncgetLatestCommit.go


📄 Исходный файл: `api/atproto/syncgetLatestCommit.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetLatestCommit](#syncgetlatestcommit-apiatprotosyncgetlatestcommitgo22) `:22`


</details>


[function] name: SyncGetLatestCommit file: api/atproto/syncgetLatestCommit.go:22 returns_error: да description: SyncGetLatestCommit calls the XRPC method "com.atproto.sync.getLatestCommit".

did: The DID of the repo.


### SyncGetLatestCommit (api/atproto/syncgetLatestCommit.go:22)


SyncGetLatestCommit calls the XRPC method "com.atproto.sync.getLatestCommit".

did: The DID of the repo.


```go
func SyncGetLatestCommit((*SyncGetLatestCommit_Output, error)) (*SyncGetLatestCommit_Output, error)
```


**Тип запроса:** SyncGetLatestCommit_Output


```json
{
  "cid": "string",
  "rev": "string"
}
```


*Определено в:* `api/atproto/syncgetLatestCommit.go`


**Тип ответа:** SyncGetLatestCommit_Output


```json
{
  "cid": "string",
  "rev": "string"
}
```


*Определено в:* `api/atproto/syncgetLatestCommit.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SyncGetLatestCommit_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetLatestCommit.go:22`




## api/atproto/syncgetRecord.go


📄 Исходный файл: `api/atproto/syncgetRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetRecord](#syncgetrecord-apiatprotosyncgetrecordgo18) `:18`


</details>


[function] name: SyncGetRecord file: api/atproto/syncgetRecord.go:18 returns_error: да description: SyncGetRecord calls the XRPC method "com.atproto.sync.getRecord".

did: The DID of the repo.
rkey: Record Key


### SyncGetRecord (api/atproto/syncgetRecord.go:18)


SyncGetRecord calls the XRPC method "com.atproto.sync.getRecord".

did: The DID of the repo.
rkey: Record Key


```go
func SyncGetRecord(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetRecord.go:18`




## api/atproto/syncgetRepo.go


📄 Исходный файл: `api/atproto/syncgetRepo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetRepo](#syncgetrepo-apiatprotosyncgetrepogo18) `:18`


</details>


[function] name: SyncGetRepo file: api/atproto/syncgetRepo.go:18 returns_error: да description: SyncGetRepo calls the XRPC method "com.atproto.sync.getRepo".

did: The DID of the repo.
since: The revision ('rev') of 


### SyncGetRepo (api/atproto/syncgetRepo.go:18)


SyncGetRepo calls the XRPC method "com.atproto.sync.getRepo".

did: The DID of the repo.
since: The revision ('rev') of the repo to create a diff from.


```go
func SyncGetRepo(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetRepo.go:18`




## api/atproto/syncgetRepoStatus.go


📄 Исходный файл: `api/atproto/syncgetRepoStatus.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncGetRepoStatus](#syncgetrepostatus-apiatprotosyncgetrepostatusgo26) `:26`


</details>


[function] name: SyncGetRepoStatus file: api/atproto/syncgetRepoStatus.go:26 returns_error: да description: SyncGetRepoStatus calls the XRPC method "com.atproto.sync.getRepoStatus".

did: The DID of the repo.


### SyncGetRepoStatus (api/atproto/syncgetRepoStatus.go:26)


SyncGetRepoStatus calls the XRPC method "com.atproto.sync.getRepoStatus".

did: The DID of the repo.


```go
func SyncGetRepoStatus((*SyncGetRepoStatus_Output, error)) (*SyncGetRepoStatus_Output, error)
```


**Тип запроса:** SyncGetRepoStatus_Output


```json
{
  "active": false,
  "did": "string",
  "rev": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetRepoStatus.go`


**Тип ответа:** SyncGetRepoStatus_Output


```json
{
  "active": false,
  "did": "string",
  "rev": "string",
  "status": "string"
}
```


*Определено в:* `api/atproto/syncgetRepoStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SyncGetRepoStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/syncgetRepoStatus.go:26`




## api/atproto/synclistBlobs.go


📄 Исходный файл: `api/atproto/synclistBlobs.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncListBlobs](#synclistblobs-apiatprotosynclistblobsgo23) `:23`


</details>


[function] name: SyncListBlobs file: api/atproto/synclistBlobs.go:23 returns_error: да description: SyncListBlobs calls the XRPC method "com.atproto.sync.listBlobs".

did: The DID of the repo.
since: Optional revision of


### SyncListBlobs (api/atproto/synclistBlobs.go:23)


SyncListBlobs calls the XRPC method "com.atproto.sync.listBlobs".

did: The DID of the repo.
since: Optional revision of the repo to list blobs since.


```go
func SyncListBlobs((*SyncListBlobs_Output, error)) (*SyncListBlobs_Output, error)
```


**Тип запроса:** SyncListBlobs_Output


```json
{
  "cids": [],
  "cursor": "string"
}
```


*Определено в:* `api/atproto/synclistBlobs.go`


**Тип ответа:** SyncListBlobs_Output


```json
{
  "cids": [],
  "cursor": "string"
}
```


*Определено в:* `api/atproto/synclistBlobs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SyncListBlobs_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/synclistBlobs.go:23`




## api/atproto/synclistHosts.go


📄 Исходный файл: `api/atproto/synclistHosts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncListHosts](#synclisthosts-apiatprotosynclisthostsgo31) `:31`


</details>


[function] name: SyncListHosts file: api/atproto/synclistHosts.go:31 returns_error: да description: SyncListHosts calls the XRPC method "com.atproto.sync.listHosts".


### SyncListHosts (api/atproto/synclistHosts.go:31)


SyncListHosts calls the XRPC method "com.atproto.sync.listHosts".


```go
func SyncListHosts((*SyncListHosts_Output, error)) (*SyncListHosts_Output, error)
```


**Тип запроса:** SyncListHosts_Output


```json
{
  "cursor": "string",
  "hosts": []
}
```


*Определено в:* `api/atproto/synclistHosts.go`


**Тип ответа:** SyncListHosts_Output


```json
{
  "cursor": "string",
  "hosts": []
}
```


*Определено в:* `api/atproto/synclistHosts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SyncListHosts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/synclistHosts.go:31`




## api/atproto/synclistRepos.go


📄 Исходный файл: `api/atproto/synclistRepos.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncListRepos](#synclistrepos-apiatprotosynclistreposgo31) `:31`


</details>


[function] name: SyncListRepos file: api/atproto/synclistRepos.go:31 returns_error: да description: SyncListRepos calls the XRPC method "com.atproto.sync.listRepos".


### SyncListRepos (api/atproto/synclistRepos.go:31)


SyncListRepos calls the XRPC method "com.atproto.sync.listRepos".


```go
func SyncListRepos((*SyncListRepos_Output, error)) (*SyncListRepos_Output, error)
```


**Тип запроса:** SyncListRepos_Output


```json
{
  "cursor": "string",
  "repos": []
}
```


*Определено в:* `api/atproto/synclistRepos.go`


**Тип ответа:** SyncListRepos_Output


```json
{
  "cursor": "string",
  "repos": []
}
```


*Определено в:* `api/atproto/synclistRepos.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SyncListRepos_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/synclistRepos.go:31`




## api/atproto/synclistReposByCollection.go


📄 Исходный файл: `api/atproto/synclistReposByCollection.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncListReposByCollection](#synclistreposbycollection-apiatprotosynclistreposbycollectiongo27) `:27`


</details>


[function] name: SyncListReposByCollection file: api/atproto/synclistReposByCollection.go:27 returns_error: да description: SyncListReposByCollection calls the XRPC method "com.atproto.sync.listReposByCollection".

limit: Maximum size of respon


### SyncListReposByCollection (api/atproto/synclistReposByCollection.go:27)


SyncListReposByCollection calls the XRPC method "com.atproto.sync.listReposByCollection".

limit: Maximum size of response set. Recommend setting a large maximum (1000+) when enumerating large DID lists.


```go
func SyncListReposByCollection((*SyncListReposByCollection_Output, error)) (*SyncListReposByCollection_Output, error)
```


**Тип запроса:** SyncListReposByCollection_Output


```json
{
  "cursor": "string",
  "repos": []
}
```


*Определено в:* `api/atproto/synclistReposByCollection.go`


**Тип ответа:** SyncListReposByCollection_Output


```json
{
  "cursor": "string",
  "repos": []
}
```


*Определено в:* `api/atproto/synclistReposByCollection.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SyncListReposByCollection_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/synclistReposByCollection.go:27`




## api/atproto/syncnotifyOfUpdate.go


📄 Исходный файл: `api/atproto/syncnotifyOfUpdate.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncNotifyOfUpdate](#syncnotifyofupdate-apiatprotosyncnotifyofupdatego20) `:20`


</details>


[function] name: SyncNotifyOfUpdate file: api/atproto/syncnotifyOfUpdate.go:20 returns_error: нет description: SyncNotifyOfUpdate calls the XRPC method "com.atproto.sync.notifyOfUpdate".


### SyncNotifyOfUpdate (api/atproto/syncnotifyOfUpdate.go:20)


SyncNotifyOfUpdate calls the XRPC method "com.atproto.sync.notifyOfUpdate".


```go
func SyncNotifyOfUpdate((ctx context.Context, c lexutil.LexClient, input *SyncNotifyOfUpdate_Input)) (ctx context.Context, c lexutil.LexClient, input *SyncNotifyOfUpdate_Input)
```


**Тип запроса:** SyncNotifyOfUpdate_Input


```json
{
  "hostname": "string"
}
```


*Определено в:* `api/atproto/syncnotifyOfUpdate.go`


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


**Тип ответа:** SyncNotifyOfUpdate_Input


```json
{
  "hostname": "string"
}
```


*Определено в:* `api/atproto/syncnotifyOfUpdate.go`


📍 *Расположение:* `api/atproto/syncnotifyOfUpdate.go:20`




## api/atproto/syncrequestCrawl.go


📄 Исходный файл: `api/atproto/syncrequestCrawl.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SyncRequestCrawl](#syncrequestcrawl-apiatprotosyncrequestcrawlgo20) `:20`


</details>


[function] name: SyncRequestCrawl file: api/atproto/syncrequestCrawl.go:20 returns_error: нет description: SyncRequestCrawl calls the XRPC method "com.atproto.sync.requestCrawl".


### SyncRequestCrawl (api/atproto/syncrequestCrawl.go:20)


SyncRequestCrawl calls the XRPC method "com.atproto.sync.requestCrawl".


```go
func SyncRequestCrawl((ctx context.Context, c lexutil.LexClient, input *SyncRequestCrawl_Input)) (ctx context.Context, c lexutil.LexClient, input *SyncRequestCrawl_Input)
```


**Тип запроса:** SyncRequestCrawl_Input


```json
{
  "hostname": "string"
}
```


*Определено в:* `api/atproto/syncrequestCrawl.go`


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


**Тип ответа:** SyncRequestCrawl_Input


```json
{
  "hostname": "string"
}
```


*Определено в:* `api/atproto/syncrequestCrawl.go`


📍 *Расположение:* `api/atproto/syncrequestCrawl.go:20`




## api/atproto/tempaddReservedHandle.go


📄 Исходный файл: `api/atproto/tempaddReservedHandle.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TempAddReservedHandle](#tempaddreservedhandle-apiatprototempaddreservedhandlego23) `:23`


</details>


[function] name: TempAddReservedHandle file: api/atproto/tempaddReservedHandle.go:23 returns_error: да description: TempAddReservedHandle calls the XRPC method "com.atproto.temp.addReservedHandle".


### TempAddReservedHandle (api/atproto/tempaddReservedHandle.go:23)


TempAddReservedHandle calls the XRPC method "com.atproto.temp.addReservedHandle".


```go
func TempAddReservedHandle((*TempAddReservedHandle_Output, error)) (*TempAddReservedHandle_Output, error)
```


**Тип запроса:** TempAddReservedHandle_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TempAddReservedHandle_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TempAddReservedHandle_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/tempaddReservedHandle.go:23`




## api/atproto/tempcheckHandleAvailability.go


📄 Исходный файл: `api/atproto/tempcheckHandleAvailability.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiatprototempcheckhandleavailabilitygo27) `:27`

- 🔗 [TempCheckHandleAvailability](#tempcheckhandleavailability-apiatprototempcheckhandleavailabilitygo85) `:85`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiatprototempcheckhandleavailabilitygo39) `:39`


</details>


[function] name: MarshalJSON file: api/atproto/tempcheckHandleAvailability.go:27 returns_error: да description: —


### MarshalJSON (api/atproto/tempcheckHandleAvailability.go:27)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *TempCheckHandleAvailability_Output_Result) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/tempcheckHandleAvailability.go:27`



---


[function] name: TempCheckHandleAvailability file: api/atproto/tempcheckHandleAvailability.go:85 returns_error: да description: TempCheckHandleAvailability calls the XRPC method "com.atproto.temp.checkHandleAvailability".

birthDate: User-provided 


### TempCheckHandleAvailability (api/atproto/tempcheckHandleAvailability.go:85)


TempCheckHandleAvailability calls the XRPC method "com.atproto.temp.checkHandleAvailability".

birthDate: User-provided birth date. Might be used to build handle suggestions.
email: User-provided email. Might be used to build handle suggestions.
handle: Tentative handle. Will be checked for availability or used to build handle suggestions.


```go
func TempCheckHandleAvailability((*TempCheckHandleAvailability_Output, error)) (*TempCheckHandleAvailability_Output, error)
```


**Тип запроса:** TempCheckHandleAvailability_Output


```json
{
  "handle": "string",
  "result": null
}
```


*Определено в:* `api/atproto/tempcheckHandleAvailability.go`


**Тип ответа:** TempCheckHandleAvailability_Output


```json
{
  "handle": "string",
  "result": null
}
```


*Определено в:* `api/atproto/tempcheckHandleAvailability.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TempCheckHandleAvailability_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/tempcheckHandleAvailability.go:85`



---


[function] name: UnmarshalJSON file: api/atproto/tempcheckHandleAvailability.go:39 returns_error: нет description: —


### UnmarshalJSON (api/atproto/tempcheckHandleAvailability.go:39)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *TempCheckHandleAvailability_Output_Result) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/atproto/tempcheckHandleAvailability.go:39`




## api/atproto/tempcheckSignupQueue.go


📄 Исходный файл: `api/atproto/tempcheckSignupQueue.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TempCheckSignupQueue](#tempchecksignupqueue-apiatprototempchecksignupqueuego21) `:21`


</details>


[function] name: TempCheckSignupQueue file: api/atproto/tempcheckSignupQueue.go:21 returns_error: да description: TempCheckSignupQueue calls the XRPC method "com.atproto.temp.checkSignupQueue".


### TempCheckSignupQueue (api/atproto/tempcheckSignupQueue.go:21)


TempCheckSignupQueue calls the XRPC method "com.atproto.temp.checkSignupQueue".


```go
func TempCheckSignupQueue((*TempCheckSignupQueue_Output, error)) (*TempCheckSignupQueue_Output, error)
```


**Тип запроса:** TempCheckSignupQueue_Output


```json
{
  "activated": false,
  "estimatedTimeMs": 0,
  "placeInQueue": 0
}
```


*Определено в:* `api/atproto/tempcheckSignupQueue.go`


**Тип ответа:** TempCheckSignupQueue_Output


```json
{
  "activated": false,
  "estimatedTimeMs": 0,
  "placeInQueue": 0
}
```


*Определено в:* `api/atproto/tempcheckSignupQueue.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TempCheckSignupQueue_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/tempcheckSignupQueue.go:21`




## api/atproto/tempdereferenceScope.go


📄 Исходный файл: `api/atproto/tempdereferenceScope.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TempDereferenceScope](#tempdereferencescope-apiatprototempdereferencescopego22) `:22`


</details>


[function] name: TempDereferenceScope file: api/atproto/tempdereferenceScope.go:22 returns_error: да description: TempDereferenceScope calls the XRPC method "com.atproto.temp.dereferenceScope".

scope: The scope reference (starts with


### TempDereferenceScope (api/atproto/tempdereferenceScope.go:22)


TempDereferenceScope calls the XRPC method "com.atproto.temp.dereferenceScope".

scope: The scope reference (starts with 'ref:')


```go
func TempDereferenceScope((*TempDereferenceScope_Output, error)) (*TempDereferenceScope_Output, error)
```


**Тип запроса:** TempDereferenceScope_Output


```json
{
  "scope": "string"
}
```


*Определено в:* `api/atproto/tempdereferenceScope.go`


**Тип ответа:** TempDereferenceScope_Output


```json
{
  "scope": "string"
}
```


*Определено в:* `api/atproto/tempdereferenceScope.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TempDereferenceScope_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/tempdereferenceScope.go:22`




## api/atproto/tempfetchLabels.go


📄 Исходный файл: `api/atproto/tempfetchLabels.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TempFetchLabels](#tempfetchlabels-apiatprototempfetchlabelsgo19) `:19`


</details>


[function] name: TempFetchLabels file: api/atproto/tempfetchLabels.go:19 returns_error: да description: TempFetchLabels calls the XRPC method "com.atproto.temp.fetchLabels".


### TempFetchLabels (api/atproto/tempfetchLabels.go:19)


TempFetchLabels calls the XRPC method "com.atproto.temp.fetchLabels".


```go
func TempFetchLabels((*TempFetchLabels_Output, error)) (*TempFetchLabels_Output, error)
```


**Тип запроса:** TempFetchLabels_Output


```json
{
  "labels": []
}
```


*Определено в:* `api/atproto/tempfetchLabels.go`


**Тип ответа:** TempFetchLabels_Output


```json
{
  "labels": []
}
```


*Определено в:* `api/atproto/tempfetchLabels.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TempFetchLabels_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/atproto/tempfetchLabels.go:19`




## api/atproto/temprequestPhoneVerification.go


📄 Исходный файл: `api/atproto/temprequestPhoneVerification.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TempRequestPhoneVerification](#temprequestphoneverification-apiatprototemprequestphoneverificationgo19) `:19`


</details>


[function] name: TempRequestPhoneVerification file: api/atproto/temprequestPhoneVerification.go:19 returns_error: нет description: TempRequestPhoneVerification calls the XRPC method "com.atproto.temp.requestPhoneVerification".


### TempRequestPhoneVerification (api/atproto/temprequestPhoneVerification.go:19)


TempRequestPhoneVerification calls the XRPC method "com.atproto.temp.requestPhoneVerification".


```go
func TempRequestPhoneVerification((ctx context.Context, c lexutil.LexClient, input *TempRequestPhoneVerification_Input)) (ctx context.Context, c lexutil.LexClient, input *TempRequestPhoneVerification_Input)
```


**Тип запроса:** TempRequestPhoneVerification_Input


```json
{
  "phoneNumber": "string"
}
```


*Определено в:* `api/atproto/temprequestPhoneVerification.go`


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


**Тип ответа:** TempRequestPhoneVerification_Input


```json
{
  "phoneNumber": "string"
}
```


*Определено в:* `api/atproto/temprequestPhoneVerification.go`


📍 *Расположение:* `api/atproto/temprequestPhoneVerification.go:19`




## api/atproto/temprevokeAccountCredentials.go


📄 Исходный файл: `api/atproto/temprevokeAccountCredentials.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TempRevokeAccountCredentials](#temprevokeaccountcredentials-apiatprototemprevokeaccountcredentialsgo19) `:19`


</details>


[function] name: TempRevokeAccountCredentials file: api/atproto/temprevokeAccountCredentials.go:19 returns_error: нет description: TempRevokeAccountCredentials calls the XRPC method "com.atproto.temp.revokeAccountCredentials".


### TempRevokeAccountCredentials (api/atproto/temprevokeAccountCredentials.go:19)


TempRevokeAccountCredentials calls the XRPC method "com.atproto.temp.revokeAccountCredentials".


```go
func TempRevokeAccountCredentials((ctx context.Context, c lexutil.LexClient, input *TempRevokeAccountCredentials_Input)) (ctx context.Context, c lexutil.LexClient, input *TempRevokeAccountCredentials_Input)
```


**Тип запроса:** TempRevokeAccountCredentials_Input


```json
{
  "account": "string"
}
```


*Определено в:* `api/atproto/temprevokeAccountCredentials.go`


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


**Тип ответа:** TempRevokeAccountCredentials_Input


```json
{
  "account": "string"
}
```


*Определено в:* `api/atproto/temprevokeAccountCredentials.go`


📍 *Расположение:* `api/atproto/temprevokeAccountCredentials.go:19`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_agnostic.md)

- [Следующая директория](api_bsky.md)


---

