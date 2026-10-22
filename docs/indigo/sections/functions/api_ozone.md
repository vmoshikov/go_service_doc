---
title: "Функции: api/ozone"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: api/ozone
---


# Функции: api/ozone


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_chat.md)

- [Следующая директория](atproto_atclient.md)


---


## Меню по файлам


- 📄 [api/ozone/communicationcreateTemplate.go](#apiozonecommunicationcreatetemplatego)

- 📄 [api/ozone/communicationdeleteTemplate.go](#apiozonecommunicationdeletetemplatego)

- 📄 [api/ozone/communicationlistTemplates.go](#apiozonecommunicationlisttemplatesgo)

- 📄 [api/ozone/communicationupdateTemplate.go](#apiozonecommunicationupdatetemplatego)

- 📄 [api/ozone/hostinggetAccountHistory.go](#apiozonehostinggetaccounthistorygo)

- 📄 [api/ozone/moderationcancelScheduledActions.go](#apiozonemoderationcancelscheduledactionsgo)

- 📄 [api/ozone/moderationdefs.go](#apiozonemoderationdefsgo)

- 📄 [api/ozone/moderationemitEvent.go](#apiozonemoderationemiteventgo)

- 📄 [api/ozone/moderationgetAccountTimeline.go](#apiozonemoderationgetaccounttimelinego)

- 📄 [api/ozone/moderationgetEvent.go](#apiozonemoderationgeteventgo)

- 📄 [api/ozone/moderationgetRecord.go](#apiozonemoderationgetrecordgo)

- 📄 [api/ozone/moderationgetRecords.go](#apiozonemoderationgetrecordsgo)

- 📄 [api/ozone/moderationgetRepo.go](#apiozonemoderationgetrepogo)

- 📄 [api/ozone/moderationgetReporterStats.go](#apiozonemoderationgetreporterstatsgo)

- 📄 [api/ozone/moderationgetRepos.go](#apiozonemoderationgetreposgo)

- 📄 [api/ozone/moderationgetSubjects.go](#apiozonemoderationgetsubjectsgo)

- 📄 [api/ozone/moderationlistScheduledActions.go](#apiozonemoderationlistscheduledactionsgo)

- 📄 [api/ozone/moderationqueryEvents.go](#apiozonemoderationqueryeventsgo)

- 📄 [api/ozone/moderationqueryStatuses.go](#apiozonemoderationquerystatusesgo)

- 📄 [api/ozone/moderationscheduleAction.go](#apiozonemoderationscheduleactiongo)

- 📄 [api/ozone/moderationsearchRepos.go](#apiozonemoderationsearchreposgo)

- 📄 [api/ozone/safelinkaddRule.go](#apiozonesafelinkaddrulego)

- 📄 [api/ozone/safelinkqueryEvents.go](#apiozonesafelinkqueryeventsgo)

- 📄 [api/ozone/safelinkqueryRules.go](#apiozonesafelinkqueryrulesgo)

- 📄 [api/ozone/safelinkremoveRule.go](#apiozonesafelinkremoverulego)

- 📄 [api/ozone/safelinkupdateRule.go](#apiozonesafelinkupdaterulego)

- 📄 [api/ozone/servergetConfig.go](#apiozoneservergetconfiggo)

- 📄 [api/ozone/setaddValues.go](#apiozonesetaddvaluesgo)

- 📄 [api/ozone/setdeleteSet.go](#apiozonesetdeletesetgo)

- 📄 [api/ozone/setdeleteValues.go](#apiozonesetdeletevaluesgo)

- 📄 [api/ozone/setgetValues.go](#apiozonesetgetvaluesgo)

- 📄 [api/ozone/setquerySets.go](#apiozonesetquerysetsgo)

- 📄 [api/ozone/settinglistOptions.go](#apiozonesettinglistoptionsgo)

- 📄 [api/ozone/settingremoveOptions.go](#apiozonesettingremoveoptionsgo)

- 📄 [api/ozone/settingupsertOption.go](#apiozonesettingupsertoptiongo)

- 📄 [api/ozone/setupsertSet.go](#apiozonesetupsertsetgo)

- 📄 [api/ozone/signaturefindCorrelation.go](#apiozonesignaturefindcorrelationgo)

- 📄 [api/ozone/signaturefindRelatedAccounts.go](#apiozonesignaturefindrelatedaccountsgo)

- 📄 [api/ozone/signaturesearchAccounts.go](#apiozonesignaturesearchaccountsgo)

- 📄 [api/ozone/teamaddMember.go](#apiozoneteamaddmembergo)

- 📄 [api/ozone/teamdeleteMember.go](#apiozoneteamdeletemembergo)

- 📄 [api/ozone/teamlistMembers.go](#apiozoneteamlistmembersgo)

- 📄 [api/ozone/teamupdateMember.go](#apiozoneteamupdatemembergo)

- 📄 [api/ozone/verificationdefs.go](#apiozoneverificationdefsgo)

- 📄 [api/ozone/verificationgrantVerifications.go](#apiozoneverificationgrantverificationsgo)

- 📄 [api/ozone/verificationlistVerifications.go](#apiozoneverificationlistverificationsgo)

- 📄 [api/ozone/verificationrevokeVerifications.go](#apiozoneverificationrevokeverificationsgo)


---


## api/ozone/communicationcreateTemplate.go


📄 Исходный файл: `api/ozone/communicationcreateTemplate.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CommunicationCreateTemplate](#communicationcreatetemplate-apiozonecommunicationcreatetemplatego28) `:28`


</details>


[function] name: CommunicationCreateTemplate file: api/ozone/communicationcreateTemplate.go:28 returns_error: да description: CommunicationCreateTemplate calls the XRPC method "tools.ozone.communication.createTemplate".


### CommunicationCreateTemplate (api/ozone/communicationcreateTemplate.go:28)


CommunicationCreateTemplate calls the XRPC method "tools.ozone.communication.createTemplate".


```go
func CommunicationCreateTemplate((*CommunicationDefs_TemplateView, error)) (*CommunicationDefs_TemplateView, error)
```


**Тип запроса:** CommunicationDefs_TemplateView


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


**Тип ответа:** CommunicationDefs_TemplateView


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CommunicationDefs_TemplateView`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/communicationcreateTemplate.go:28`




## api/ozone/communicationdeleteTemplate.go


📄 Исходный файл: `api/ozone/communicationdeleteTemplate.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CommunicationDeleteTemplate](#communicationdeletetemplate-apiozonecommunicationdeletetemplatego19) `:19`


</details>


[function] name: CommunicationDeleteTemplate file: api/ozone/communicationdeleteTemplate.go:19 returns_error: нет description: CommunicationDeleteTemplate calls the XRPC method "tools.ozone.communication.deleteTemplate".


### CommunicationDeleteTemplate (api/ozone/communicationdeleteTemplate.go:19)


CommunicationDeleteTemplate calls the XRPC method "tools.ozone.communication.deleteTemplate".


```go
func CommunicationDeleteTemplate((ctx context.Context, c lexutil.LexClient, input *CommunicationDeleteTemplate_Input)) (ctx context.Context, c lexutil.LexClient, input *CommunicationDeleteTemplate_Input)
```


**Тип запроса:** CommunicationDeleteTemplate_Input


```json
{
  "id": "string"
}
```


*Определено в:* `api/ozone/communicationdeleteTemplate.go`


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


**Тип ответа:** CommunicationDeleteTemplate_Input


```json
{
  "id": "string"
}
```


*Определено в:* `api/ozone/communicationdeleteTemplate.go`


📍 *Расположение:* `api/ozone/communicationdeleteTemplate.go:19`




## api/ozone/communicationlistTemplates.go


📄 Исходный файл: `api/ozone/communicationlistTemplates.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CommunicationListTemplates](#communicationlisttemplates-apiozonecommunicationlisttemplatesgo19) `:19`


</details>


[function] name: CommunicationListTemplates file: api/ozone/communicationlistTemplates.go:19 returns_error: да description: CommunicationListTemplates calls the XRPC method "tools.ozone.communication.listTemplates".


### CommunicationListTemplates (api/ozone/communicationlistTemplates.go:19)


CommunicationListTemplates calls the XRPC method "tools.ozone.communication.listTemplates".


```go
func CommunicationListTemplates((*CommunicationListTemplates_Output, error)) (*CommunicationListTemplates_Output, error)
```


**Тип запроса:** CommunicationListTemplates_Output


```json
{
  "communicationTemplates": []
}
```


*Определено в:* `api/ozone/communicationlistTemplates.go`


**Тип ответа:** CommunicationListTemplates_Output


```json
{
  "communicationTemplates": []
}
```


*Определено в:* `api/ozone/communicationlistTemplates.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CommunicationListTemplates_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/communicationlistTemplates.go:19`




## api/ozone/communicationupdateTemplate.go


📄 Исходный файл: `api/ozone/communicationupdateTemplate.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CommunicationUpdateTemplate](#communicationupdatetemplate-apiozonecommunicationupdatetemplatego31) `:31`


</details>


[function] name: CommunicationUpdateTemplate file: api/ozone/communicationupdateTemplate.go:31 returns_error: да description: CommunicationUpdateTemplate calls the XRPC method "tools.ozone.communication.updateTemplate".


### CommunicationUpdateTemplate (api/ozone/communicationupdateTemplate.go:31)


CommunicationUpdateTemplate calls the XRPC method "tools.ozone.communication.updateTemplate".


```go
func CommunicationUpdateTemplate((*CommunicationDefs_TemplateView, error)) (*CommunicationDefs_TemplateView, error)
```


**Тип запроса:** CommunicationDefs_TemplateView


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


**Тип ответа:** CommunicationDefs_TemplateView


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*CommunicationDefs_TemplateView`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/communicationupdateTemplate.go:31`




## api/ozone/hostinggetAccountHistory.go


📄 Исходный файл: `api/ozone/hostinggetAccountHistory.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [HostingGetAccountHistory](#hostinggetaccounthistory-apiozonehostinggetaccounthistorygo118) `:118`

- 🔗 [MarshalJSON](#marshaljson-apiozonehostinggetaccounthistorygo49) `:49`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonehostinggetaccounthistorygo73) `:73`


</details>


[function] name: HostingGetAccountHistory file: api/ozone/hostinggetAccountHistory.go:118 returns_error: да description: HostingGetAccountHistory calls the XRPC method "tools.ozone.hosting.getAccountHistory".


### HostingGetAccountHistory (api/ozone/hostinggetAccountHistory.go:118)


HostingGetAccountHistory calls the XRPC method "tools.ozone.hosting.getAccountHistory".


```go
func HostingGetAccountHistory((*HostingGetAccountHistory_Output, error)) (*HostingGetAccountHistory_Output, error)
```


**Тип запроса:** HostingGetAccountHistory_Output


```json
{
  "cursor": "string",
  "events": []
}
```


*Определено в:* `api/ozone/hostinggetAccountHistory.go`


**Тип ответа:** HostingGetAccountHistory_Output


```json
{
  "cursor": "string",
  "events": []
}
```


*Определено в:* `api/ozone/hostinggetAccountHistory.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*HostingGetAccountHistory_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/hostinggetAccountHistory.go:118`



---


[function] name: MarshalJSON file: api/ozone/hostinggetAccountHistory.go:49 returns_error: да description: —


### MarshalJSON (api/ozone/hostinggetAccountHistory.go:49)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *HostingGetAccountHistory_Event_Details) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/hostinggetAccountHistory.go:49`



---


[function] name: UnmarshalJSON file: api/ozone/hostinggetAccountHistory.go:73 returns_error: нет description: —


### UnmarshalJSON (api/ozone/hostinggetAccountHistory.go:73)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *HostingGetAccountHistory_Event_Details) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/hostinggetAccountHistory.go:73`




## api/ozone/moderationcancelScheduledActions.go


📄 Исходный файл: `api/ozone/moderationcancelScheduledActions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationCancelScheduledActions](#moderationcancelscheduledactions-apiozonemoderationcancelscheduledactionsgo37) `:37`


</details>


[function] name: ModerationCancelScheduledActions file: api/ozone/moderationcancelScheduledActions.go:37 returns_error: да description: ModerationCancelScheduledActions calls the XRPC method "tools.ozone.moderation.cancelScheduledActions".


### ModerationCancelScheduledActions (api/ozone/moderationcancelScheduledActions.go:37)


ModerationCancelScheduledActions calls the XRPC method "tools.ozone.moderation.cancelScheduledActions".


```go
func ModerationCancelScheduledActions((*ModerationCancelScheduledActions_CancellationResults, error)) (*ModerationCancelScheduledActions_CancellationResults, error)
```


**Тип запроса:** ModerationCancelScheduledActions_CancellationResults


```json
{
  "failed": [],
  "succeeded": []
}
```


*Определено в:* `api/ozone/moderationcancelScheduledActions.go`


**Тип ответа:** ModerationCancelScheduledActions_CancellationResults


```json
{
  "failed": [],
  "succeeded": []
}
```


*Определено в:* `api/ozone/moderationcancelScheduledActions.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationCancelScheduledActions_CancellationResults`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationcancelScheduledActions.go:37`




## api/ozone/moderationdefs.go


📄 Исходный файл: `api/ozone/moderationdefs.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationdefsgo122) `:122`

- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationdefsgo414) `:414`

- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationdefsgo605) `:605`

- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationdefsgo676) `:676`

- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationdefsgo866) `:866`

- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationdefsgo1159) `:1159`

- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationdefsgo1195) `:1195`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationdefsgo134) `:134`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationdefsgo514) `:514`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationdefsgo625) `:625`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationdefsgo776) `:776`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationdefsgo882) `:882`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationdefsgo1171) `:1171`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationdefsgo1211) `:1211`


</details>


[function] name: MarshalJSON file: api/ozone/moderationdefs.go:122 returns_error: да description: —


### MarshalJSON (api/ozone/moderationdefs.go:122)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationDefs_BlobView_Details) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationdefs.go:122`



---


[function] name: MarshalJSON file: api/ozone/moderationdefs.go:414 returns_error: да description: —


### MarshalJSON (api/ozone/moderationdefs.go:414)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationDefs_ModEventViewDetail_Event) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationdefs.go:414`



---


[function] name: MarshalJSON file: api/ozone/moderationdefs.go:605 returns_error: да description: —


### MarshalJSON (api/ozone/moderationdefs.go:605)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationDefs_ModEventViewDetail_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationdefs.go:605`



---


[function] name: MarshalJSON file: api/ozone/moderationdefs.go:676 returns_error: да description: —


### MarshalJSON (api/ozone/moderationdefs.go:676)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationDefs_ModEventView_Event) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationdefs.go:676`



---


[function] name: MarshalJSON file: api/ozone/moderationdefs.go:866 returns_error: да description: —


### MarshalJSON (api/ozone/moderationdefs.go:866)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationDefs_ModEventView_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationdefs.go:866`



---


[function] name: MarshalJSON file: api/ozone/moderationdefs.go:1159 returns_error: да description: —


### MarshalJSON (api/ozone/moderationdefs.go:1159)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationDefs_SubjectStatusView_Hosting) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationdefs.go:1159`



---


[function] name: MarshalJSON file: api/ozone/moderationdefs.go:1195 returns_error: да description: —


### MarshalJSON (api/ozone/moderationdefs.go:1195)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationDefs_SubjectStatusView_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationdefs.go:1195`



---


[function] name: UnmarshalJSON file: api/ozone/moderationdefs.go:134 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationdefs.go:134)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationDefs_BlobView_Details) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationdefs.go:134`



---


[function] name: UnmarshalJSON file: api/ozone/moderationdefs.go:514 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationdefs.go:514)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationDefs_ModEventViewDetail_Event) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationdefs.go:514`



---


[function] name: UnmarshalJSON file: api/ozone/moderationdefs.go:625 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationdefs.go:625)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationDefs_ModEventViewDetail_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationdefs.go:625`



---


[function] name: UnmarshalJSON file: api/ozone/moderationdefs.go:776 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationdefs.go:776)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationDefs_ModEventView_Event) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationdefs.go:776`



---


[function] name: UnmarshalJSON file: api/ozone/moderationdefs.go:882 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationdefs.go:882)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationDefs_ModEventView_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationdefs.go:882`



---


[function] name: UnmarshalJSON file: api/ozone/moderationdefs.go:1171 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationdefs.go:1171)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationDefs_SubjectStatusView_Hosting) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationdefs.go:1171`



---


[function] name: UnmarshalJSON file: api/ozone/moderationdefs.go:1211 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationdefs.go:1211)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationDefs_SubjectStatusView_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationdefs.go:1211`




## api/ozone/moderationemitEvent.go


📄 Исходный файл: `api/ozone/moderationemitEvent.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationemiteventgo54) `:54`

- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationemiteventgo243) `:243`

- 🔗 [ModerationEmitEvent](#moderationemitevent-apiozonemoderationemiteventgo274) `:274`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationemiteventgo154) `:154`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationemiteventgo255) `:255`


</details>


[function] name: MarshalJSON file: api/ozone/moderationemitEvent.go:54 returns_error: да description: —


### MarshalJSON (api/ozone/moderationemitEvent.go:54)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationEmitEvent_Input_Event) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationemitEvent.go:54`



---


[function] name: MarshalJSON file: api/ozone/moderationemitEvent.go:243 returns_error: да description: —


### MarshalJSON (api/ozone/moderationemitEvent.go:243)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationEmitEvent_Input_Subject) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationemitEvent.go:243`



---


[function] name: ModerationEmitEvent file: api/ozone/moderationemitEvent.go:274 returns_error: да description: ModerationEmitEvent calls the XRPC method "tools.ozone.moderation.emitEvent".


### ModerationEmitEvent (api/ozone/moderationemitEvent.go:274)


ModerationEmitEvent calls the XRPC method "tools.ozone.moderation.emitEvent".


```go
func ModerationEmitEvent((*ModerationDefs_ModEventView, error)) (*ModerationDefs_ModEventView, error)
```


**Тип запроса:** ModerationDefs_ModEventView


```json
{
  "createdAt": "string",
  "createdBy": "string",
  "creatorHandle": "string",
  "event": null,
  "id": 0,
  "modTool": null,
  "subject": null,
  "subjectBlobCids": [],
  "subjectHandle": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Тип ответа:** ModerationDefs_ModEventView


```json
{
  "createdAt": "string",
  "createdBy": "string",
  "creatorHandle": "string",
  "event": null,
  "id": 0,
  "modTool": null,
  "subject": null,
  "subjectBlobCids": [],
  "subjectHandle": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationDefs_ModEventView`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationemitEvent.go:274`



---


[function] name: UnmarshalJSON file: api/ozone/moderationemitEvent.go:154 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationemitEvent.go:154)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationEmitEvent_Input_Event) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationemitEvent.go:154`



---


[function] name: UnmarshalJSON file: api/ozone/moderationemitEvent.go:255 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationemitEvent.go:255)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationEmitEvent_Input_Subject) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationemitEvent.go:255`




## api/ozone/moderationgetAccountTimeline.go


📄 Исходный файл: `api/ozone/moderationgetAccountTimeline.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationGetAccountTimeline](#moderationgetaccounttimeline-apiozonemoderationgetaccounttimelinego32) `:32`


</details>


[function] name: ModerationGetAccountTimeline file: api/ozone/moderationgetAccountTimeline.go:32 returns_error: да description: ModerationGetAccountTimeline calls the XRPC method "tools.ozone.moderation.getAccountTimeline".


### ModerationGetAccountTimeline (api/ozone/moderationgetAccountTimeline.go:32)


ModerationGetAccountTimeline calls the XRPC method "tools.ozone.moderation.getAccountTimeline".


```go
func ModerationGetAccountTimeline((*ModerationGetAccountTimeline_Output, error)) (*ModerationGetAccountTimeline_Output, error)
```


**Тип запроса:** ModerationGetAccountTimeline_Output


```json
{
  "timeline": []
}
```


*Определено в:* `api/ozone/moderationgetAccountTimeline.go`


**Тип ответа:** ModerationGetAccountTimeline_Output


```json
{
  "timeline": []
}
```


*Определено в:* `api/ozone/moderationgetAccountTimeline.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationGetAccountTimeline_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetAccountTimeline.go:32`




## api/ozone/moderationgetEvent.go


📄 Исходный файл: `api/ozone/moderationgetEvent.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationGetEvent](#moderationgetevent-apiozonemoderationgeteventgo14) `:14`


</details>


[function] name: ModerationGetEvent file: api/ozone/moderationgetEvent.go:14 returns_error: да description: ModerationGetEvent calls the XRPC method "tools.ozone.moderation.getEvent".


### ModerationGetEvent (api/ozone/moderationgetEvent.go:14)


ModerationGetEvent calls the XRPC method "tools.ozone.moderation.getEvent".


```go
func ModerationGetEvent((*ModerationDefs_ModEventViewDetail, error)) (*ModerationDefs_ModEventViewDetail, error)
```


**Тип запроса:** ModerationDefs_ModEventViewDetail


```json
{
  "createdAt": "string",
  "createdBy": "string",
  "event": null,
  "id": 0,
  "modTool": null,
  "subject": null,
  "subjectBlobs": []
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Тип ответа:** ModerationDefs_ModEventViewDetail


```json
{
  "createdAt": "string",
  "createdBy": "string",
  "event": null,
  "id": 0,
  "modTool": null,
  "subject": null,
  "subjectBlobs": []
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationDefs_ModEventViewDetail`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetEvent.go:14`




## api/ozone/moderationgetRecord.go


📄 Исходный файл: `api/ozone/moderationgetRecord.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationGetRecord](#moderationgetrecord-apiozonemoderationgetrecordgo14) `:14`


</details>


[function] name: ModerationGetRecord file: api/ozone/moderationgetRecord.go:14 returns_error: да description: ModerationGetRecord calls the XRPC method "tools.ozone.moderation.getRecord".


### ModerationGetRecord (api/ozone/moderationgetRecord.go:14)


ModerationGetRecord calls the XRPC method "tools.ozone.moderation.getRecord".


```go
func ModerationGetRecord((*ModerationDefs_RecordViewDetail, error)) (*ModerationDefs_RecordViewDetail, error)
```


**Тип запроса:** ModerationDefs_RecordViewDetail


```json
{
  "$type": "string",
  "blobs": [],
  "cid": "string",
  "indexedAt": "string",
  "labels": [],
  "moderation": null,
  "repo": null,
  "uri": "string",
  "value": null
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Тип ответа:** ModerationDefs_RecordViewDetail


```json
{
  "$type": "string",
  "blobs": [],
  "cid": "string",
  "indexedAt": "string",
  "labels": [],
  "moderation": null,
  "repo": null,
  "uri": "string",
  "value": null
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationDefs_RecordViewDetail`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetRecord.go:14`




## api/ozone/moderationgetRecords.go


📄 Исходный файл: `api/ozone/moderationgetRecords.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationgetrecordsgo25) `:25`

- 🔗 [ModerationGetRecords](#moderationgetrecords-apiozonemoderationgetrecordsgo56) `:56`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationgetrecordsgo37) `:37`


</details>


[function] name: MarshalJSON file: api/ozone/moderationgetRecords.go:25 returns_error: да description: —


### MarshalJSON (api/ozone/moderationgetRecords.go:25)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationGetRecords_Output_Records_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetRecords.go:25`



---


[function] name: ModerationGetRecords file: api/ozone/moderationgetRecords.go:56 returns_error: да description: ModerationGetRecords calls the XRPC method "tools.ozone.moderation.getRecords".


### ModerationGetRecords (api/ozone/moderationgetRecords.go:56)


ModerationGetRecords calls the XRPC method "tools.ozone.moderation.getRecords".


```go
func ModerationGetRecords((*ModerationGetRecords_Output, error)) (*ModerationGetRecords_Output, error)
```


**Тип запроса:** ModerationGetRecords_Output


```json
{
  "records": []
}
```


*Определено в:* `api/ozone/moderationgetRecords.go`


**Тип ответа:** ModerationGetRecords_Output


```json
{
  "records": []
}
```


*Определено в:* `api/ozone/moderationgetRecords.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationGetRecords_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetRecords.go:56`



---


[function] name: UnmarshalJSON file: api/ozone/moderationgetRecords.go:37 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationgetRecords.go:37)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationGetRecords_Output_Records_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationgetRecords.go:37`




## api/ozone/moderationgetRepo.go


📄 Исходный файл: `api/ozone/moderationgetRepo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationGetRepo](#moderationgetrepo-apiozonemoderationgetrepogo14) `:14`


</details>


[function] name: ModerationGetRepo file: api/ozone/moderationgetRepo.go:14 returns_error: да description: ModerationGetRepo calls the XRPC method "tools.ozone.moderation.getRepo".


### ModerationGetRepo (api/ozone/moderationgetRepo.go:14)


ModerationGetRepo calls the XRPC method "tools.ozone.moderation.getRepo".


```go
func ModerationGetRepo((*ModerationDefs_RepoViewDetail, error)) (*ModerationDefs_RepoViewDetail, error)
```


**Тип запроса:** ModerationDefs_RepoViewDetail


```json
{
  "$type": "string",
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
  "labels": [],
  "moderation": null,
  "relatedRecords": [],
  "threatSignatures": []
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Тип ответа:** ModerationDefs_RepoViewDetail


```json
{
  "$type": "string",
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
  "labels": [],
  "moderation": null,
  "relatedRecords": [],
  "threatSignatures": []
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationDefs_RepoViewDetail`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetRepo.go:14`




## api/ozone/moderationgetReporterStats.go


📄 Исходный файл: `api/ozone/moderationgetReporterStats.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationGetReporterStats](#moderationgetreporterstats-apiozonemoderationgetreporterstatsgo19) `:19`


</details>


[function] name: ModerationGetReporterStats file: api/ozone/moderationgetReporterStats.go:19 returns_error: да description: ModerationGetReporterStats calls the XRPC method "tools.ozone.moderation.getReporterStats".


### ModerationGetReporterStats (api/ozone/moderationgetReporterStats.go:19)


ModerationGetReporterStats calls the XRPC method "tools.ozone.moderation.getReporterStats".


```go
func ModerationGetReporterStats((*ModerationGetReporterStats_Output, error)) (*ModerationGetReporterStats_Output, error)
```


**Тип запроса:** ModerationGetReporterStats_Output


```json
{
  "stats": []
}
```


*Определено в:* `api/ozone/moderationgetReporterStats.go`


**Тип ответа:** ModerationGetReporterStats_Output


```json
{
  "stats": []
}
```


*Определено в:* `api/ozone/moderationgetReporterStats.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationGetReporterStats_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetReporterStats.go:19`




## api/ozone/moderationgetRepos.go


📄 Исходный файл: `api/ozone/moderationgetRepos.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationgetreposgo25) `:25`

- 🔗 [ModerationGetRepos](#moderationgetrepos-apiozonemoderationgetreposgo56) `:56`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationgetreposgo37) `:37`


</details>


[function] name: MarshalJSON file: api/ozone/moderationgetRepos.go:25 returns_error: да description: —


### MarshalJSON (api/ozone/moderationgetRepos.go:25)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationGetRepos_Output_Repos_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetRepos.go:25`



---


[function] name: ModerationGetRepos file: api/ozone/moderationgetRepos.go:56 returns_error: да description: ModerationGetRepos calls the XRPC method "tools.ozone.moderation.getRepos".


### ModerationGetRepos (api/ozone/moderationgetRepos.go:56)


ModerationGetRepos calls the XRPC method "tools.ozone.moderation.getRepos".


```go
func ModerationGetRepos((*ModerationGetRepos_Output, error)) (*ModerationGetRepos_Output, error)
```


**Тип запроса:** ModerationGetRepos_Output


```json
{
  "repos": []
}
```


*Определено в:* `api/ozone/moderationgetRepos.go`


**Тип ответа:** ModerationGetRepos_Output


```json
{
  "repos": []
}
```


*Определено в:* `api/ozone/moderationgetRepos.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationGetRepos_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetRepos.go:56`



---


[function] name: UnmarshalJSON file: api/ozone/moderationgetRepos.go:37 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationgetRepos.go:37)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationGetRepos_Output_Repos_Elem) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationgetRepos.go:37`




## api/ozone/moderationgetSubjects.go


📄 Исходный файл: `api/ozone/moderationgetSubjects.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationGetSubjects](#moderationgetsubjects-apiozonemoderationgetsubjectsgo19) `:19`


</details>


[function] name: ModerationGetSubjects file: api/ozone/moderationgetSubjects.go:19 returns_error: да description: ModerationGetSubjects calls the XRPC method "tools.ozone.moderation.getSubjects".


### ModerationGetSubjects (api/ozone/moderationgetSubjects.go:19)


ModerationGetSubjects calls the XRPC method "tools.ozone.moderation.getSubjects".


```go
func ModerationGetSubjects((*ModerationGetSubjects_Output, error)) (*ModerationGetSubjects_Output, error)
```


**Тип запроса:** ModerationGetSubjects_Output


```json
{
  "subjects": []
}
```


*Определено в:* `api/ozone/moderationgetSubjects.go`


**Тип ответа:** ModerationGetSubjects_Output


```json
{
  "subjects": []
}
```


*Определено в:* `api/ozone/moderationgetSubjects.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationGetSubjects_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationgetSubjects.go:19`




## api/ozone/moderationlistScheduledActions.go


📄 Исходный файл: `api/ozone/moderationlistScheduledActions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationListScheduledActions](#moderationlistscheduledactions-apiozonemoderationlistscheduledactionsgo37) `:37`


</details>


[function] name: ModerationListScheduledActions file: api/ozone/moderationlistScheduledActions.go:37 returns_error: да description: ModerationListScheduledActions calls the XRPC method "tools.ozone.moderation.listScheduledActions".


### ModerationListScheduledActions (api/ozone/moderationlistScheduledActions.go:37)


ModerationListScheduledActions calls the XRPC method "tools.ozone.moderation.listScheduledActions".


```go
func ModerationListScheduledActions((*ModerationListScheduledActions_Output, error)) (*ModerationListScheduledActions_Output, error)
```


**Тип запроса:** ModerationListScheduledActions_Output


```json
{
  "actions": [],
  "cursor": "string"
}
```


*Определено в:* `api/ozone/moderationlistScheduledActions.go`


**Тип ответа:** ModerationListScheduledActions_Output


```json
{
  "actions": [],
  "cursor": "string"
}
```


*Определено в:* `api/ozone/moderationlistScheduledActions.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationListScheduledActions_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationlistScheduledActions.go:37`




## api/ozone/moderationqueryEvents.go


📄 Исходный файл: `api/ozone/moderationqueryEvents.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationQueryEvents](#moderationqueryevents-apiozonemoderationqueryeventsgo38) `:38`


</details>


[function] name: ModerationQueryEvents file: api/ozone/moderationqueryEvents.go:38 returns_error: да description: ModerationQueryEvents calls the XRPC method "tools.ozone.moderation.queryEvents".

addedLabels: If specified, only event


### ModerationQueryEvents (api/ozone/moderationqueryEvents.go:38)


ModerationQueryEvents calls the XRPC method "tools.ozone.moderation.queryEvents".

addedLabels: If specified, only events where all of these labels were added are returned
addedTags: If specified, only events where all of these tags were added are returned
ageAssuranceState: If specified, only events where the age assurance state matches the given value are returned
batchId: If specified, only events where the batchId matches the given value are returned
collections: If specified, only events where the subject belongs to the given collections will be returned. When subjectType is set to 'account', this will be ignored.
comment: If specified, only events with comments containing the keyword are returned. Apply || separator to use multiple keywords and match using OR condition.
createdAfter: Retrieve events created after a given timestamp
createdBefore: Retrieve events created before a given timestamp
hasComment: If true, only events with comments are returned
includeAllUserRecords: If true, events on all record types (posts, lists, profile etc.) or records from given 'collections' param, owned by the did are returned.
modTool: If specified, only events where the modTool name matches any of the given values are returned
removedLabels: If specified, only events where all of these labels were removed are returned
removedTags: If specified, only events where all of these tags were removed are returned
sortDirection: Sort direction for the events. Defaults to descending order of created at timestamp.
subjectType: If specified, only events where the subject is of the given type (account or record) will be returned. When this is set to 'account' the 'collections' parameter will be ignored. When includeAllUserRecords or subject is set, this will be ignored.
types: The types of events (fully qualified string in the format of tools.ozone.moderation.defs#modEvent<name>) to filter by. If not specified, all events are returned.
withStrike: If specified, only events where strikeCount value is set are returned.


```go
func ModerationQueryEvents((*ModerationQueryEvents_Output, error)) (*ModerationQueryEvents_Output, error)
```


**Тип запроса:** ModerationQueryEvents_Output


```json
{
  "cursor": "string",
  "events": []
}
```


*Определено в:* `api/ozone/moderationqueryEvents.go`


**Тип ответа:** ModerationQueryEvents_Output


```json
{
  "cursor": "string",
  "events": []
}
```


*Определено в:* `api/ozone/moderationqueryEvents.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationQueryEvents_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationqueryEvents.go:38`




## api/ozone/moderationqueryStatuses.go


📄 Исходный файл: `api/ozone/moderationqueryStatuses.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationQueryStatuses](#moderationquerystatuses-apiozonemoderationquerystatusesgo50) `:50`


</details>


[function] name: ModerationQueryStatuses file: api/ozone/moderationqueryStatuses.go:50 returns_error: да description: ModerationQueryStatuses calls the XRPC method "tools.ozone.moderation.queryStatuses".

ageAssuranceState: If specified, 


### ModerationQueryStatuses (api/ozone/moderationqueryStatuses.go:50)


ModerationQueryStatuses calls the XRPC method "tools.ozone.moderation.queryStatuses".

ageAssuranceState: If specified, only subjects with the given age assurance state will be returned.
appealed: Get subjects in unresolved appealed status
collections: If specified, subjects belonging to the given collections will be returned. When subjectType is set to 'account', this will be ignored.
comment: Search subjects by keyword from comments
hostingDeletedAfter: Search subjects where the associated record/account was deleted after a given timestamp
hostingDeletedBefore: Search subjects where the associated record/account was deleted before a given timestamp
hostingStatuses: Search subjects by the status of the associated record/account
hostingUpdatedAfter: Search subjects where the associated record/account was updated after a given timestamp
hostingUpdatedBefore: Search subjects where the associated record/account was updated before a given timestamp
includeAllUserRecords: All subjects, or subjects from given 'collections' param, belonging to the account specified in the 'subject' param will be returned.
includeMuted: By default, we don't include muted subjects in the results. Set this to true to include them.
lastReviewedBy: Get all subject statuses that were reviewed by a specific moderator
minAccountSuspendCount: If specified, only subjects that belong to an account that has at least this many suspensions will be returned.
minPriorityScore: If specified, only subjects that have priority score value above the given value will be returned.
minReportedRecordsCount: If specified, only subjects that belong to an account that has at least this many reported records will be returned.
minStrikeCount: If specified, only subjects that belong to an account that has at least this many active strikes will be returned.
minTakendownRecordsCount: If specified, only subjects that belong to an account that has at least this many taken down records will be returned.
onlyMuted: When set to true, only muted subjects and reporters will be returned.
queueCount: Number of queues being used by moderators. Subjects will be split among all queues.
queueIndex: Index of the queue to fetch subjects from. Works only when queueCount value is specified.
queueSeed: A seeder to shuffle/balance the queue items.
reportedAfter: Search subjects reported after a given timestamp
reportedBefore: Search subjects reported before a given timestamp
reviewState: Specify when fetching subjects in a certain state
reviewedAfter: Search subjects reviewed after a given timestamp
reviewedBefore: Search subjects reviewed before a given timestamp
subject: The subject to get the status for.
subjectType: If specified, subjects of the given type (account or record) will be returned. When this is set to 'account' the 'collections' parameter will be ignored. When includeAllUserRecords or subject is set, this will be ignored.
takendown: Get subjects that were taken down


```go
func ModerationQueryStatuses((*ModerationQueryStatuses_Output, error)) (*ModerationQueryStatuses_Output, error)
```


**Тип запроса:** ModerationQueryStatuses_Output


```json
{
  "cursor": "string",
  "subjectStatuses": []
}
```


*Определено в:* `api/ozone/moderationqueryStatuses.go`


**Тип ответа:** ModerationQueryStatuses_Output


```json
{
  "cursor": "string",
  "subjectStatuses": []
}
```


*Определено в:* `api/ozone/moderationqueryStatuses.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationQueryStatuses_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationqueryStatuses.go:50`




## api/ozone/moderationscheduleAction.go


📄 Исходный файл: `api/ozone/moderationscheduleAction.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiozonemoderationscheduleactiongo37) `:37`

- 🔗 [ModerationScheduleAction](#moderationscheduleaction-apiozonemoderationscheduleactiongo103) `:103`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozonemoderationscheduleactiongo45) `:45`


</details>


[function] name: MarshalJSON file: api/ozone/moderationscheduleAction.go:37 returns_error: да description: —


### MarshalJSON (api/ozone/moderationscheduleAction.go:37)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ModerationScheduleAction_Input_Action) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationscheduleAction.go:37`



---


[function] name: ModerationScheduleAction file: api/ozone/moderationscheduleAction.go:103 returns_error: да description: ModerationScheduleAction calls the XRPC method "tools.ozone.moderation.scheduleAction".


### ModerationScheduleAction (api/ozone/moderationscheduleAction.go:103)


ModerationScheduleAction calls the XRPC method "tools.ozone.moderation.scheduleAction".


```go
func ModerationScheduleAction((*ModerationScheduleAction_ScheduledActionResults, error)) (*ModerationScheduleAction_ScheduledActionResults, error)
```


**Тип запроса:** ModerationScheduleAction_ScheduledActionResults


```json
{
  "failed": [],
  "succeeded": []
}
```


*Определено в:* `api/ozone/moderationscheduleAction.go`


**Тип ответа:** ModerationScheduleAction_ScheduledActionResults


```json
{
  "failed": [],
  "succeeded": []
}
```


*Определено в:* `api/ozone/moderationscheduleAction.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationScheduleAction_ScheduledActionResults`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationscheduleAction.go:103`



---


[function] name: UnmarshalJSON file: api/ozone/moderationscheduleAction.go:45 returns_error: нет description: —


### UnmarshalJSON (api/ozone/moderationscheduleAction.go:45)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ModerationScheduleAction_Input_Action) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/moderationscheduleAction.go:45`




## api/ozone/moderationsearchRepos.go


📄 Исходный файл: `api/ozone/moderationsearchRepos.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ModerationSearchRepos](#moderationsearchrepos-apiozonemoderationsearchreposgo22) `:22`


</details>


[function] name: ModerationSearchRepos file: api/ozone/moderationsearchRepos.go:22 returns_error: да description: ModerationSearchRepos calls the XRPC method "tools.ozone.moderation.searchRepos".

term: DEPRECATED: use 'q' instead


### ModerationSearchRepos (api/ozone/moderationsearchRepos.go:22)


ModerationSearchRepos calls the XRPC method "tools.ozone.moderation.searchRepos".

term: DEPRECATED: use 'q' instead


```go
func ModerationSearchRepos((*ModerationSearchRepos_Output, error)) (*ModerationSearchRepos_Output, error)
```


**Тип запроса:** ModerationSearchRepos_Output


```json
{
  "cursor": "string",
  "repos": []
}
```


*Определено в:* `api/ozone/moderationsearchRepos.go`


**Тип ответа:** ModerationSearchRepos_Output


```json
{
  "cursor": "string",
  "repos": []
}
```


*Определено в:* `api/ozone/moderationsearchRepos.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ModerationSearchRepos_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/moderationsearchRepos.go:22`




## api/ozone/safelinkaddRule.go


📄 Исходный файл: `api/ozone/safelinkaddRule.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SafelinkAddRule](#safelinkaddrule-apiozonesafelinkaddrulego27) `:27`


</details>


[function] name: SafelinkAddRule file: api/ozone/safelinkaddRule.go:27 returns_error: да description: SafelinkAddRule calls the XRPC method "tools.ozone.safelink.addRule".


### SafelinkAddRule (api/ozone/safelinkaddRule.go:27)


SafelinkAddRule calls the XRPC method "tools.ozone.safelink.addRule".


```go
func SafelinkAddRule((*SafelinkDefs_Event, error)) (*SafelinkDefs_Event, error)
```


**Тип запроса:** SafelinkDefs_Event


```json
{
  "action": "string",
  "comment": "string",
  "createdAt": "string",
  "createdBy": "string",
  "eventType": "string",
  "id": 0,
  "pattern": "string",
  "reason": "string",
  "url": "string"
}
```


*Определено в:* `api/ozone/safelinkdefs.go`


**Тип ответа:** SafelinkDefs_Event


```json
{
  "action": "string",
  "comment": "string",
  "createdAt": "string",
  "createdBy": "string",
  "eventType": "string",
  "id": 0,
  "pattern": "string",
  "reason": "string",
  "url": "string"
}
```


*Определено в:* `api/ozone/safelinkdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SafelinkDefs_Event`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/safelinkaddRule.go:27`




## api/ozone/safelinkqueryEvents.go


📄 Исходный файл: `api/ozone/safelinkqueryEvents.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SafelinkQueryEvents](#safelinkqueryevents-apiozonesafelinkqueryeventsgo35) `:35`


</details>


[function] name: SafelinkQueryEvents file: api/ozone/safelinkqueryEvents.go:35 returns_error: да description: SafelinkQueryEvents calls the XRPC method "tools.ozone.safelink.queryEvents".


### SafelinkQueryEvents (api/ozone/safelinkqueryEvents.go:35)


SafelinkQueryEvents calls the XRPC method "tools.ozone.safelink.queryEvents".


```go
func SafelinkQueryEvents((*SafelinkQueryEvents_Output, error)) (*SafelinkQueryEvents_Output, error)
```


**Тип запроса:** SafelinkQueryEvents_Output


```json
{
  "cursor": "string",
  "events": []
}
```


*Определено в:* `api/ozone/safelinkqueryEvents.go`


**Тип ответа:** SafelinkQueryEvents_Output


```json
{
  "cursor": "string",
  "events": []
}
```


*Определено в:* `api/ozone/safelinkqueryEvents.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SafelinkQueryEvents_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/safelinkqueryEvents.go:35`




## api/ozone/safelinkqueryRules.go


📄 Исходный файл: `api/ozone/safelinkqueryRules.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SafelinkQueryRules](#safelinkqueryrules-apiozonesafelinkqueryrulesgo41) `:41`


</details>


[function] name: SafelinkQueryRules file: api/ozone/safelinkqueryRules.go:41 returns_error: да description: SafelinkQueryRules calls the XRPC method "tools.ozone.safelink.queryRules".


### SafelinkQueryRules (api/ozone/safelinkqueryRules.go:41)


SafelinkQueryRules calls the XRPC method "tools.ozone.safelink.queryRules".


```go
func SafelinkQueryRules((*SafelinkQueryRules_Output, error)) (*SafelinkQueryRules_Output, error)
```


**Тип запроса:** SafelinkQueryRules_Output


```json
{
  "cursor": "string",
  "rules": []
}
```


*Определено в:* `api/ozone/safelinkqueryRules.go`


**Тип ответа:** SafelinkQueryRules_Output


```json
{
  "cursor": "string",
  "rules": []
}
```


*Определено в:* `api/ozone/safelinkqueryRules.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SafelinkQueryRules_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/safelinkqueryRules.go:41`




## api/ozone/safelinkremoveRule.go


📄 Исходный файл: `api/ozone/safelinkremoveRule.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SafelinkRemoveRule](#safelinkremoverule-apiozonesafelinkremoverulego25) `:25`


</details>


[function] name: SafelinkRemoveRule file: api/ozone/safelinkremoveRule.go:25 returns_error: да description: SafelinkRemoveRule calls the XRPC method "tools.ozone.safelink.removeRule".


### SafelinkRemoveRule (api/ozone/safelinkremoveRule.go:25)


SafelinkRemoveRule calls the XRPC method "tools.ozone.safelink.removeRule".


```go
func SafelinkRemoveRule((*SafelinkDefs_Event, error)) (*SafelinkDefs_Event, error)
```


**Тип запроса:** SafelinkDefs_Event


```json
{
  "action": "string",
  "comment": "string",
  "createdAt": "string",
  "createdBy": "string",
  "eventType": "string",
  "id": 0,
  "pattern": "string",
  "reason": "string",
  "url": "string"
}
```


*Определено в:* `api/ozone/safelinkdefs.go`


**Тип ответа:** SafelinkDefs_Event


```json
{
  "action": "string",
  "comment": "string",
  "createdAt": "string",
  "createdBy": "string",
  "eventType": "string",
  "id": 0,
  "pattern": "string",
  "reason": "string",
  "url": "string"
}
```


*Определено в:* `api/ozone/safelinkdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SafelinkDefs_Event`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/safelinkremoveRule.go:25`




## api/ozone/safelinkupdateRule.go


📄 Исходный файл: `api/ozone/safelinkupdateRule.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SafelinkUpdateRule](#safelinkupdaterule-apiozonesafelinkupdaterulego27) `:27`


</details>


[function] name: SafelinkUpdateRule file: api/ozone/safelinkupdateRule.go:27 returns_error: да description: SafelinkUpdateRule calls the XRPC method "tools.ozone.safelink.updateRule".


### SafelinkUpdateRule (api/ozone/safelinkupdateRule.go:27)


SafelinkUpdateRule calls the XRPC method "tools.ozone.safelink.updateRule".


```go
func SafelinkUpdateRule((*SafelinkDefs_Event, error)) (*SafelinkDefs_Event, error)
```


**Тип запроса:** SafelinkDefs_Event


```json
{
  "action": "string",
  "comment": "string",
  "createdAt": "string",
  "createdBy": "string",
  "eventType": "string",
  "id": 0,
  "pattern": "string",
  "reason": "string",
  "url": "string"
}
```


*Определено в:* `api/ozone/safelinkdefs.go`


**Тип ответа:** SafelinkDefs_Event


```json
{
  "action": "string",
  "comment": "string",
  "createdAt": "string",
  "createdBy": "string",
  "eventType": "string",
  "id": 0,
  "pattern": "string",
  "reason": "string",
  "url": "string"
}
```


*Определено в:* `api/ozone/safelinkdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SafelinkDefs_Event`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/safelinkupdateRule.go:27`




## api/ozone/servergetConfig.go


📄 Исходный файл: `api/ozone/servergetConfig.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ServerGetConfig](#servergetconfig-apiozoneservergetconfiggo35) `:35`


</details>


[function] name: ServerGetConfig file: api/ozone/servergetConfig.go:35 returns_error: да description: ServerGetConfig calls the XRPC method "tools.ozone.server.getConfig".


### ServerGetConfig (api/ozone/servergetConfig.go:35)


ServerGetConfig calls the XRPC method "tools.ozone.server.getConfig".


```go
func ServerGetConfig((*ServerGetConfig_Output, error)) (*ServerGetConfig_Output, error)
```


**Тип запроса:** ServerGetConfig_Output


```json
{
  "appview": null,
  "blobDivert": null,
  "chat": null,
  "pds": null,
  "verifierDid": "string",
  "viewer": null
}
```


*Определено в:* `api/ozone/servergetConfig.go`


**Тип ответа:** ServerGetConfig_Output


```json
{
  "appview": null,
  "blobDivert": null,
  "chat": null,
  "pds": null,
  "verifierDid": "string",
  "viewer": null
}
```


*Определено в:* `api/ozone/servergetConfig.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ServerGetConfig_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/servergetConfig.go:35`




## api/ozone/setaddValues.go


📄 Исходный файл: `api/ozone/setaddValues.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetAddValues](#setaddvalues-apiozonesetaddvaluesgo22) `:22`


</details>


[function] name: SetAddValues file: api/ozone/setaddValues.go:22 returns_error: нет description: SetAddValues calls the XRPC method "tools.ozone.set.addValues".


### SetAddValues (api/ozone/setaddValues.go:22)


SetAddValues calls the XRPC method "tools.ozone.set.addValues".


```go
func SetAddValues((ctx context.Context, c lexutil.LexClient, input *SetAddValues_Input)) (ctx context.Context, c lexutil.LexClient, input *SetAddValues_Input)
```


**Тип запроса:** SetAddValues_Input


```json
{
  "name": "string",
  "values": []
}
```


*Определено в:* `api/ozone/setaddValues.go`


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


**Тип ответа:** SetAddValues_Input


```json
{
  "name": "string",
  "values": []
}
```


*Определено в:* `api/ozone/setaddValues.go`


📍 *Расположение:* `api/ozone/setaddValues.go:22`




## api/ozone/setdeleteSet.go


📄 Исходный файл: `api/ozone/setdeleteSet.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetDeleteSet](#setdeleteset-apiozonesetdeletesetgo24) `:24`


</details>


[function] name: SetDeleteSet file: api/ozone/setdeleteSet.go:24 returns_error: да description: SetDeleteSet calls the XRPC method "tools.ozone.set.deleteSet".


### SetDeleteSet (api/ozone/setdeleteSet.go:24)


SetDeleteSet calls the XRPC method "tools.ozone.set.deleteSet".


```go
func SetDeleteSet((*SetDeleteSet_Output, error)) (*SetDeleteSet_Output, error)
```


**Тип запроса:** SetDeleteSet_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SetDeleteSet_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SetDeleteSet_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/setdeleteSet.go:24`




## api/ozone/setdeleteValues.go


📄 Исходный файл: `api/ozone/setdeleteValues.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetDeleteValues](#setdeletevalues-apiozonesetdeletevaluesgo22) `:22`


</details>


[function] name: SetDeleteValues file: api/ozone/setdeleteValues.go:22 returns_error: нет description: SetDeleteValues calls the XRPC method "tools.ozone.set.deleteValues".


### SetDeleteValues (api/ozone/setdeleteValues.go:22)


SetDeleteValues calls the XRPC method "tools.ozone.set.deleteValues".


```go
func SetDeleteValues((ctx context.Context, c lexutil.LexClient, input *SetDeleteValues_Input)) (ctx context.Context, c lexutil.LexClient, input *SetDeleteValues_Input)
```


**Тип запроса:** SetDeleteValues_Input


```json
{
  "name": "string",
  "values": []
}
```


*Определено в:* `api/ozone/setdeleteValues.go`


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


**Тип ответа:** SetDeleteValues_Input


```json
{
  "name": "string",
  "values": []
}
```


*Определено в:* `api/ozone/setdeleteValues.go`


📍 *Расположение:* `api/ozone/setdeleteValues.go:22`




## api/ozone/setgetValues.go


📄 Исходный файл: `api/ozone/setgetValues.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetGetValues](#setgetvalues-apiozonesetgetvaluesgo21) `:21`


</details>


[function] name: SetGetValues file: api/ozone/setgetValues.go:21 returns_error: да description: SetGetValues calls the XRPC method "tools.ozone.set.getValues".


### SetGetValues (api/ozone/setgetValues.go:21)


SetGetValues calls the XRPC method "tools.ozone.set.getValues".


```go
func SetGetValues((*SetGetValues_Output, error)) (*SetGetValues_Output, error)
```


**Тип запроса:** SetGetValues_Output


```json
{
  "cursor": "string",
  "set": null,
  "values": []
}
```


*Определено в:* `api/ozone/setgetValues.go`


**Тип ответа:** SetGetValues_Output


```json
{
  "cursor": "string",
  "set": null,
  "values": []
}
```


*Определено в:* `api/ozone/setgetValues.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SetGetValues_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/setgetValues.go:21`




## api/ozone/setquerySets.go


📄 Исходный файл: `api/ozone/setquerySets.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetQuerySets](#setquerysets-apiozonesetquerysetsgo22) `:22`


</details>


[function] name: SetQuerySets file: api/ozone/setquerySets.go:22 returns_error: да description: SetQuerySets calls the XRPC method "tools.ozone.set.querySets".

sortDirection: Defaults to ascending order of name fiel


### SetQuerySets (api/ozone/setquerySets.go:22)


SetQuerySets calls the XRPC method "tools.ozone.set.querySets".

sortDirection: Defaults to ascending order of name field.


```go
func SetQuerySets((*SetQuerySets_Output, error)) (*SetQuerySets_Output, error)
```


**Тип запроса:** SetQuerySets_Output


```json
{
  "cursor": "string",
  "sets": []
}
```


*Определено в:* `api/ozone/setquerySets.go`


**Тип ответа:** SetQuerySets_Output


```json
{
  "cursor": "string",
  "sets": []
}
```


*Определено в:* `api/ozone/setquerySets.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SetQuerySets_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/setquerySets.go:22`




## api/ozone/settinglistOptions.go


📄 Исходный файл: `api/ozone/settinglistOptions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SettingListOptions](#settinglistoptions-apiozonesettinglistoptionsgo23) `:23`


</details>


[function] name: SettingListOptions file: api/ozone/settinglistOptions.go:23 returns_error: да description: SettingListOptions calls the XRPC method "tools.ozone.setting.listOptions".

keys: Filter for only the specified keys. I


### SettingListOptions (api/ozone/settinglistOptions.go:23)


SettingListOptions calls the XRPC method "tools.ozone.setting.listOptions".

keys: Filter for only the specified keys. Ignored if prefix is provided
prefix: Filter keys by prefix


```go
func SettingListOptions((*SettingListOptions_Output, error)) (*SettingListOptions_Output, error)
```


**Тип запроса:** SettingListOptions_Output


```json
{
  "cursor": "string",
  "options": []
}
```


*Определено в:* `api/ozone/settinglistOptions.go`


**Тип ответа:** SettingListOptions_Output


```json
{
  "cursor": "string",
  "options": []
}
```


*Определено в:* `api/ozone/settinglistOptions.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SettingListOptions_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/settinglistOptions.go:23`




## api/ozone/settingremoveOptions.go


📄 Исходный файл: `api/ozone/settingremoveOptions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SettingRemoveOptions](#settingremoveoptions-apiozonesettingremoveoptionsgo24) `:24`


</details>


[function] name: SettingRemoveOptions file: api/ozone/settingremoveOptions.go:24 returns_error: да description: SettingRemoveOptions calls the XRPC method "tools.ozone.setting.removeOptions".


### SettingRemoveOptions (api/ozone/settingremoveOptions.go:24)


SettingRemoveOptions calls the XRPC method "tools.ozone.setting.removeOptions".


```go
func SettingRemoveOptions((*SettingRemoveOptions_Output, error)) (*SettingRemoveOptions_Output, error)
```


**Тип запроса:** SettingRemoveOptions_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** SettingRemoveOptions_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SettingRemoveOptions_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/settingremoveOptions.go:24`




## api/ozone/settingupsertOption.go


📄 Исходный файл: `api/ozone/settingupsertOption.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SettingUpsertOption](#settingupsertoption-apiozonesettingupsertoptiongo28) `:28`


</details>


[function] name: SettingUpsertOption file: api/ozone/settingupsertOption.go:28 returns_error: да description: SettingUpsertOption calls the XRPC method "tools.ozone.setting.upsertOption".


### SettingUpsertOption (api/ozone/settingupsertOption.go:28)


SettingUpsertOption calls the XRPC method "tools.ozone.setting.upsertOption".


```go
func SettingUpsertOption((*SettingUpsertOption_Output, error)) (*SettingUpsertOption_Output, error)
```


**Тип запроса:** SettingUpsertOption_Output


```json
{
  "option": null
}
```


*Определено в:* `api/ozone/settingupsertOption.go`


**Тип ответа:** SettingUpsertOption_Output


```json
{
  "option": null
}
```


*Определено в:* `api/ozone/settingupsertOption.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SettingUpsertOption_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/settingupsertOption.go:28`




## api/ozone/setupsertSet.go


📄 Исходный файл: `api/ozone/setupsertSet.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SetUpsertSet](#setupsertset-apiozonesetupsertsetgo14) `:14`


</details>


[function] name: SetUpsertSet file: api/ozone/setupsertSet.go:14 returns_error: да description: SetUpsertSet calls the XRPC method "tools.ozone.set.upsertSet".


### SetUpsertSet (api/ozone/setupsertSet.go:14)


SetUpsertSet calls the XRPC method "tools.ozone.set.upsertSet".


```go
func SetUpsertSet((*SetDefs_SetView, error)) (*SetDefs_SetView, error)
```


**Тип запроса:** SetDefs_SetView


```json
{
  "createdAt": "string",
  "description": "string",
  "name": "string",
  "setSize": 0,
  "updatedAt": "string"
}
```


*Определено в:* `api/ozone/setdefs.go`


**Тип ответа:** SetDefs_SetView


```json
{
  "createdAt": "string",
  "description": "string",
  "name": "string",
  "setSize": 0,
  "updatedAt": "string"
}
```


*Определено в:* `api/ozone/setdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SetDefs_SetView`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/setupsertSet.go:14`




## api/ozone/signaturefindCorrelation.go


📄 Исходный файл: `api/ozone/signaturefindCorrelation.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SignatureFindCorrelation](#signaturefindcorrelation-apiozonesignaturefindcorrelationgo19) `:19`


</details>


[function] name: SignatureFindCorrelation file: api/ozone/signaturefindCorrelation.go:19 returns_error: да description: SignatureFindCorrelation calls the XRPC method "tools.ozone.signature.findCorrelation".


### SignatureFindCorrelation (api/ozone/signaturefindCorrelation.go:19)


SignatureFindCorrelation calls the XRPC method "tools.ozone.signature.findCorrelation".


```go
func SignatureFindCorrelation((*SignatureFindCorrelation_Output, error)) (*SignatureFindCorrelation_Output, error)
```


**Тип запроса:** SignatureFindCorrelation_Output


```json
{
  "details": []
}
```


*Определено в:* `api/ozone/signaturefindCorrelation.go`


**Тип ответа:** SignatureFindCorrelation_Output


```json
{
  "details": []
}
```


*Определено в:* `api/ozone/signaturefindCorrelation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SignatureFindCorrelation_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/signaturefindCorrelation.go:19`




## api/ozone/signaturefindRelatedAccounts.go


📄 Исходный файл: `api/ozone/signaturefindRelatedAccounts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SignatureFindRelatedAccounts](#signaturefindrelatedaccounts-apiozonesignaturefindrelatedaccountsgo27) `:27`


</details>


[function] name: SignatureFindRelatedAccounts file: api/ozone/signaturefindRelatedAccounts.go:27 returns_error: да description: SignatureFindRelatedAccounts calls the XRPC method "tools.ozone.signature.findRelatedAccounts".


### SignatureFindRelatedAccounts (api/ozone/signaturefindRelatedAccounts.go:27)


SignatureFindRelatedAccounts calls the XRPC method "tools.ozone.signature.findRelatedAccounts".


```go
func SignatureFindRelatedAccounts((*SignatureFindRelatedAccounts_Output, error)) (*SignatureFindRelatedAccounts_Output, error)
```


**Тип запроса:** SignatureFindRelatedAccounts_Output


```json
{
  "accounts": [],
  "cursor": "string"
}
```


*Определено в:* `api/ozone/signaturefindRelatedAccounts.go`


**Тип ответа:** SignatureFindRelatedAccounts_Output


```json
{
  "accounts": [],
  "cursor": "string"
}
```


*Определено в:* `api/ozone/signaturefindRelatedAccounts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SignatureFindRelatedAccounts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/signaturefindRelatedAccounts.go:27`




## api/ozone/signaturesearchAccounts.go


📄 Исходный файл: `api/ozone/signaturesearchAccounts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [SignatureSearchAccounts](#signaturesearchaccounts-apiozonesignaturesearchaccountsgo21) `:21`


</details>


[function] name: SignatureSearchAccounts file: api/ozone/signaturesearchAccounts.go:21 returns_error: да description: SignatureSearchAccounts calls the XRPC method "tools.ozone.signature.searchAccounts".


### SignatureSearchAccounts (api/ozone/signaturesearchAccounts.go:21)


SignatureSearchAccounts calls the XRPC method "tools.ozone.signature.searchAccounts".


```go
func SignatureSearchAccounts((*SignatureSearchAccounts_Output, error)) (*SignatureSearchAccounts_Output, error)
```


**Тип запроса:** SignatureSearchAccounts_Output


```json
{
  "accounts": [],
  "cursor": "string"
}
```


*Определено в:* `api/ozone/signaturesearchAccounts.go`


**Тип ответа:** SignatureSearchAccounts_Output


```json
{
  "accounts": [],
  "cursor": "string"
}
```


*Определено в:* `api/ozone/signaturesearchAccounts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*SignatureSearchAccounts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/signaturesearchAccounts.go:21`




## api/ozone/teamaddMember.go


📄 Исходный файл: `api/ozone/teamaddMember.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TeamAddMember](#teamaddmember-apiozoneteamaddmembergo20) `:20`


</details>


[function] name: TeamAddMember file: api/ozone/teamaddMember.go:20 returns_error: да description: TeamAddMember calls the XRPC method "tools.ozone.team.addMember".


### TeamAddMember (api/ozone/teamaddMember.go:20)


TeamAddMember calls the XRPC method "tools.ozone.team.addMember".


```go
func TeamAddMember((*TeamDefs_Member, error)) (*TeamDefs_Member, error)
```


**Тип запроса:** TeamDefs_Member


```json
{
  "createdAt": "string",
  "did": "string",
  "disabled": false,
  "lastUpdatedBy": "string",
  "profile": null,
  "role": "string",
  "updatedAt": "string"
}
```


*Определено в:* `api/ozone/teamdefs.go`


**Тип ответа:** TeamDefs_Member


```json
{
  "createdAt": "string",
  "did": "string",
  "disabled": false,
  "lastUpdatedBy": "string",
  "profile": null,
  "role": "string",
  "updatedAt": "string"
}
```


*Определено в:* `api/ozone/teamdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TeamDefs_Member`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/teamaddMember.go:20`




## api/ozone/teamdeleteMember.go


📄 Исходный файл: `api/ozone/teamdeleteMember.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TeamDeleteMember](#teamdeletemember-apiozoneteamdeletemembergo19) `:19`


</details>


[function] name: TeamDeleteMember file: api/ozone/teamdeleteMember.go:19 returns_error: нет description: TeamDeleteMember calls the XRPC method "tools.ozone.team.deleteMember".


### TeamDeleteMember (api/ozone/teamdeleteMember.go:19)


TeamDeleteMember calls the XRPC method "tools.ozone.team.deleteMember".


```go
func TeamDeleteMember((ctx context.Context, c lexutil.LexClient, input *TeamDeleteMember_Input)) (ctx context.Context, c lexutil.LexClient, input *TeamDeleteMember_Input)
```


**Тип запроса:** TeamDeleteMember_Input


```json
{
  "did": "string"
}
```


*Определено в:* `api/ozone/teamdeleteMember.go`


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


**Тип ответа:** TeamDeleteMember_Input


```json
{
  "did": "string"
}
```


*Определено в:* `api/ozone/teamdeleteMember.go`


📍 *Расположение:* `api/ozone/teamdeleteMember.go:19`




## api/ozone/teamlistMembers.go


📄 Исходный файл: `api/ozone/teamlistMembers.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TeamListMembers](#teamlistmembers-apiozoneteamlistmembersgo20) `:20`


</details>


[function] name: TeamListMembers file: api/ozone/teamlistMembers.go:20 returns_error: да description: TeamListMembers calls the XRPC method "tools.ozone.team.listMembers".


### TeamListMembers (api/ozone/teamlistMembers.go:20)


TeamListMembers calls the XRPC method "tools.ozone.team.listMembers".


```go
func TeamListMembers((*TeamListMembers_Output, error)) (*TeamListMembers_Output, error)
```


**Тип запроса:** TeamListMembers_Output


```json
{
  "cursor": "string",
  "members": []
}
```


*Определено в:* `api/ozone/teamlistMembers.go`


**Тип ответа:** TeamListMembers_Output


```json
{
  "cursor": "string",
  "members": []
}
```


*Определено в:* `api/ozone/teamlistMembers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TeamListMembers_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/teamlistMembers.go:20`




## api/ozone/teamupdateMember.go


📄 Исходный файл: `api/ozone/teamupdateMember.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TeamUpdateMember](#teamupdatemember-apiozoneteamupdatemembergo21) `:21`


</details>


[function] name: TeamUpdateMember file: api/ozone/teamupdateMember.go:21 returns_error: да description: TeamUpdateMember calls the XRPC method "tools.ozone.team.updateMember".


### TeamUpdateMember (api/ozone/teamupdateMember.go:21)


TeamUpdateMember calls the XRPC method "tools.ozone.team.updateMember".


```go
func TeamUpdateMember((*TeamDefs_Member, error)) (*TeamDefs_Member, error)
```


**Тип запроса:** TeamDefs_Member


```json
{
  "createdAt": "string",
  "did": "string",
  "disabled": false,
  "lastUpdatedBy": "string",
  "profile": null,
  "role": "string",
  "updatedAt": "string"
}
```


*Определено в:* `api/ozone/teamdefs.go`


**Тип ответа:** TeamDefs_Member


```json
{
  "createdAt": "string",
  "did": "string",
  "disabled": false,
  "lastUpdatedBy": "string",
  "profile": null,
  "role": "string",
  "updatedAt": "string"
}
```


*Определено в:* `api/ozone/teamdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*TeamDefs_Member`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/teamupdateMember.go:21`




## api/ozone/verificationdefs.go


📄 Исходный файл: `api/ozone/verificationdefs.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apiozoneverificationdefsgo47) `:47`

- 🔗 [MarshalJSON](#marshaljson-apiozoneverificationdefsgo82) `:82`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozoneverificationdefsgo59) `:59`

- 🔗 [UnmarshalJSON](#unmarshaljson-apiozoneverificationdefsgo94) `:94`


</details>


[function] name: MarshalJSON file: api/ozone/verificationdefs.go:47 returns_error: да description: —


### MarshalJSON (api/ozone/verificationdefs.go:47)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *VerificationDefs_VerificationView_IssuerRepo) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/verificationdefs.go:47`



---


[function] name: MarshalJSON file: api/ozone/verificationdefs.go:82 returns_error: да description: —


### MarshalJSON (api/ozone/verificationdefs.go:82)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *VerificationDefs_VerificationView_SubjectRepo) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/verificationdefs.go:82`



---


[function] name: UnmarshalJSON file: api/ozone/verificationdefs.go:59 returns_error: нет description: —


### UnmarshalJSON (api/ozone/verificationdefs.go:59)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *VerificationDefs_VerificationView_IssuerRepo) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/verificationdefs.go:59`



---


[function] name: UnmarshalJSON file: api/ozone/verificationdefs.go:94 returns_error: нет description: —


### UnmarshalJSON (api/ozone/verificationdefs.go:94)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *VerificationDefs_VerificationView_SubjectRepo) UnmarshalJSON((b []byte)) (b []byte)
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


📍 *Расположение:* `api/ozone/verificationdefs.go:94`




## api/ozone/verificationgrantVerifications.go


📄 Исходный файл: `api/ozone/verificationgrantVerifications.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [VerificationGrantVerifications](#verificationgrantverifications-apiozoneverificationgrantverificationsgo48) `:48`


</details>


[function] name: VerificationGrantVerifications file: api/ozone/verificationgrantVerifications.go:48 returns_error: да description: VerificationGrantVerifications calls the XRPC method "tools.ozone.verification.grantVerifications".


### VerificationGrantVerifications (api/ozone/verificationgrantVerifications.go:48)


VerificationGrantVerifications calls the XRPC method "tools.ozone.verification.grantVerifications".


```go
func VerificationGrantVerifications((*VerificationGrantVerifications_Output, error)) (*VerificationGrantVerifications_Output, error)
```


**Тип запроса:** VerificationGrantVerifications_Output


```json
{
  "failedVerifications": [],
  "verifications": []
}
```


*Определено в:* `api/ozone/verificationgrantVerifications.go`


**Тип ответа:** VerificationGrantVerifications_Output


```json
{
  "failedVerifications": [],
  "verifications": []
}
```


*Определено в:* `api/ozone/verificationgrantVerifications.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VerificationGrantVerifications_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/verificationgrantVerifications.go:48`




## api/ozone/verificationlistVerifications.go


📄 Исходный файл: `api/ozone/verificationlistVerifications.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [VerificationListVerifications](#verificationlistverifications-apiozoneverificationlistverificationsgo29) `:29`


</details>


[function] name: VerificationListVerifications file: api/ozone/verificationlistVerifications.go:29 returns_error: да description: VerificationListVerifications calls the XRPC method "tools.ozone.verification.listVerifications".

createdAfter: Filter 


### VerificationListVerifications (api/ozone/verificationlistVerifications.go:29)


VerificationListVerifications calls the XRPC method "tools.ozone.verification.listVerifications".

createdAfter: Filter to verifications created after this timestamp
createdBefore: Filter to verifications created before this timestamp
cursor: Pagination cursor
isRevoked: Filter to verifications that are revoked or not. By default, includes both.
issuers: Filter to verifications from specific issuers
limit: Maximum number of results to return
sortDirection: Sort direction for creation date
subjects: Filter to specific verified DIDs


```go
func VerificationListVerifications((*VerificationListVerifications_Output, error)) (*VerificationListVerifications_Output, error)
```


**Тип запроса:** VerificationListVerifications_Output


```json
{
  "cursor": "string",
  "verifications": []
}
```


*Определено в:* `api/ozone/verificationlistVerifications.go`


**Тип ответа:** VerificationListVerifications_Output


```json
{
  "cursor": "string",
  "verifications": []
}
```


*Определено в:* `api/ozone/verificationlistVerifications.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VerificationListVerifications_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/verificationlistVerifications.go:29`




## api/ozone/verificationrevokeVerifications.go


📄 Исходный файл: `api/ozone/verificationrevokeVerifications.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [VerificationRevokeVerifications](#verificationrevokeverifications-apiozoneverificationrevokeverificationsgo40) `:40`


</details>


[function] name: VerificationRevokeVerifications file: api/ozone/verificationrevokeVerifications.go:40 returns_error: да description: VerificationRevokeVerifications calls the XRPC method "tools.ozone.verification.revokeVerifications".


### VerificationRevokeVerifications (api/ozone/verificationrevokeVerifications.go:40)


VerificationRevokeVerifications calls the XRPC method "tools.ozone.verification.revokeVerifications".


```go
func VerificationRevokeVerifications((*VerificationRevokeVerifications_Output, error)) (*VerificationRevokeVerifications_Output, error)
```


**Тип запроса:** VerificationRevokeVerifications_Output


```json
{
  "failedRevocations": [],
  "revokedVerifications": []
}
```


*Определено в:* `api/ozone/verificationrevokeVerifications.go`


**Тип ответа:** VerificationRevokeVerifications_Output


```json
{
  "failedRevocations": [],
  "revokedVerifications": []
}
```


*Определено в:* `api/ozone/verificationrevokeVerifications.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VerificationRevokeVerifications_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/ozone/verificationrevokeVerifications.go:40`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_chat.md)

- [Следующая директория](atproto_atclient.md)


---

