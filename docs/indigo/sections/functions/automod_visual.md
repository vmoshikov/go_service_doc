---
title: "Функции: automod/visual"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/visual
---


# Функции: automod/visual


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_setstore.md)

- [Следующая директория](backfill.md)


---


## Меню по файлам


- 📄 [automod/visual/abyss_api.go](#automodvisualabyss_apigo)

- 📄 [automod/visual/abyss_client.go](#automodvisualabyss_clientgo)

- 📄 [automod/visual/abyss_rule.go](#automodvisualabyss_rulego)

- 📄 [automod/visual/hiveai_client.go](#automodvisualhiveai_clientgo)

- 📄 [automod/visual/hiveai_rule.go](#automodvisualhiveai_rulego)

- 📄 [automod/visual/prescreen.go](#automodvisualprescreengo)


---


## automod/visual/abyss_api.go


📄 Исходный файл: `automod/visual/abyss_api.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IsAbuseMatch](#isabusematch-automodvisualabyss_apigo35) `:35`


</details>


[function] name: IsAbuseMatch file: automod/visual/abyss_api.go:35 returns_error: нет description: —


### IsAbuseMatch (automod/visual/abyss_api.go:35)


IsAbuseMatch is a method that performs operations based on the provided parameters and returns ().


```go
func (amr *AbyssMatchResult) IsAbuseMatch(()) ()
```


📍 *Расположение:* `automod/visual/abyss_api.go:35`




## automod/visual/abyss_client.go


📄 Исходный файл: `automod/visual/abyss_client.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [NewAbyssClient](#newabyssclient-automodvisualabyss_clientgo26) `:26`

- 🔗 [ScanBlob](#scanblob-automodvisualabyss_clientgo35) `:35`


</details>


[function] name: NewAbyssClient file: automod/visual/abyss_client.go:26 returns_error: нет description: —


### NewAbyssClient (automod/visual/abyss_client.go:26)


NewAbyssClient is a function that performs operations based on the provided parameters and returns (host, password, ratelimitBypass string).


```go
func NewAbyssClient((host, password, ratelimitBypass string)) (host, password, ratelimitBypass string)
```


**Тип ответа:** host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Host": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HasActiveConnection": false,
  "EventsSeenSinceStartup": 0,
  "PerSecondEventRate": {},
  "PerHourEventRate": {},
  "PerDayEventRate": {},
  "UserCount": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


**Тип ответа:** password


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ratelimitBypass


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/visual/abyss_client.go:26`



---


[function] name: ScanBlob file: automod/visual/abyss_client.go:35 returns_error: да description: —


### ScanBlob (automod/visual/abyss_client.go:35)


ScanBlob is a method that performs operations based on the provided parameters and may return an error.


```go
func (ac *AbyssClient) ScanBlob((*AbyssScanResp, error)) (*AbyssScanResp, error)
```


**Тип запроса:** AbyssScanResp


```json
{
  "Blob": null,
  "Match": null,
  "Classify": null,
  "Review": null
}
```


*Определено в:* `automod/visual/abyss_api.go`


**Тип ответа:** AbyssScanResp


```json
{
  "Blob": null,
  "Match": null,
  "Classify": null,
  "Review": null
}
```


*Определено в:* `automod/visual/abyss_api.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AbyssScanResp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/visual/abyss_client.go:35`




## automod/visual/abyss_rule.go


📄 Исходный файл: `automod/visual/abyss_rule.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AbyssScanBlobRule](#abyssscanblobrule-automodvisualabyss_rulego10) `:10`


</details>


[function] name: AbyssScanBlobRule file: automod/visual/abyss_rule.go:10 returns_error: нет description: —


### AbyssScanBlobRule (automod/visual/abyss_rule.go:10)


AbyssScanBlobRule is a method that performs operations based on the provided parameters and returns (c *automod.RecordContext, blob lexutil.LexBlob, data []byte).


```go
func (ac *AbyssClient) AbyssScanBlobRule((c *automod.RecordContext, blob lexutil.LexBlob, data []byte)) (c *automod.RecordContext, blob lexutil.LexBlob, data []byte)
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


📍 *Расположение:* `automod/visual/abyss_rule.go:10`




## automod/visual/hiveai_client.go


📄 Исходный файл: `automod/visual/hiveai_client.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [LabelBlob](#labelblob-automodvisualhiveai_clientgo173) `:173`

- 🔗 [NewHiveAIClient](#newhiveaiclient-automodvisualhiveai_clientgo50) `:50`

- 🔗 [SummarizeLabels](#summarizelabels-automodvisualhiveai_clientgo153) `:153`

- 🔗 [summarizeSexualLabels](#summarizesexuallabels-automodvisualhiveai_clientgo87) `:87`

- 🔗 [summarizeSimpleLabels](#summarizesimplelabels-automodvisualhiveai_clientgo60) `:60`


</details>


[function] name: LabelBlob file: automod/visual/hiveai_client.go:173 returns_error: да description: —


### LabelBlob (automod/visual/hiveai_client.go:173)


LabelBlob is a method that performs operations based on the provided parameters and may return an error.


```go
func (hal *HiveAIClient) LabelBlob(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/visual/hiveai_client.go:173`



---


[function] name: NewHiveAIClient file: automod/visual/hiveai_client.go:50 returns_error: нет description: —


### NewHiveAIClient (automod/visual/hiveai_client.go:50)


NewHiveAIClient is a function that performs operations based on the provided parameters and returns (token string).


```go
func NewHiveAIClient((token string)) (token string)
```


**Тип ответа:** token


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/visual/hiveai_client.go:50`



---


[function] name: SummarizeLabels file: automod/visual/hiveai_client.go:153 returns_error: нет description: —


### SummarizeLabels (automod/visual/hiveai_client.go:153)


SummarizeLabels is a method that performs operations based on the provided parameters and returns ().


```go
func (resp *HiveAIResp) SummarizeLabels(()) ()
```


📍 *Расположение:* `automod/visual/hiveai_client.go:153`



---


[function] name: summarizeSexualLabels file: automod/visual/hiveai_client.go:87 returns_error: нет description: Matches only one (or none) of: porn, sexual, nudity

porn: sexual and nudity. including both explicit activity or full-f


### summarizeSexualLabels (automod/visual/hiveai_client.go:87)


Matches only one (or none) of: porn, sexual, nudity

porn: sexual and nudity. including both explicit activity or full-frontal and suggestive/intent
sexual: sexually suggestive, not explicit; may include some forms of nudity
nudity: non-sexual nudity (eg, artistic, possibly some photographic)

hive docs/definitions: https://docs.thehive.ai/docs/sexual-content


```go
func summarizeSexualLabels((cl []HiveAIResp_Class)) (cl []HiveAIResp_Class)
```


**Тип ответа:** cl


```json
{
  "HTTPMethod": "string",
  "TargetURI": "string",
  "AccessTokenHash": "string",
  "Nonce": "string"
}
```


*Определено в:* `atproto/auth/oauth/oauth.go`


**Тип ответа:** HiveAIResp_Class


```json
{
  "Class": "string",
  "Score": 0.0
}
```


*Определено в:* `automod/visual/hiveai_client.go`


📍 *Расположение:* `automod/visual/hiveai_client.go:87`



---


[function] name: summarizeSimpleLabels file: automod/visual/hiveai_client.go:60 returns_error: нет description: Simple direct mappings from individual classes to to labels

hive gore and violence: https://docs.thehive.ai/docs/class-


### summarizeSimpleLabels (automod/visual/hiveai_client.go:60)


Simple direct mappings from individual classes to to labels

hive gore and violence: https://docs.thehive.ai/docs/class-descriptions-violence-gore


```go
func summarizeSimpleLabels((cl []HiveAIResp_Class)) (cl []HiveAIResp_Class)
```


**Тип ответа:** cl


```json
{
  "HTTPMethod": "string",
  "TargetURI": "string",
  "AccessTokenHash": "string",
  "Nonce": "string"
}
```


*Определено в:* `atproto/auth/oauth/oauth.go`


**Тип ответа:** HiveAIResp_Class


```json
{
  "Class": "string",
  "Score": 0.0
}
```


*Определено в:* `automod/visual/hiveai_client.go`


📍 *Расположение:* `automod/visual/hiveai_client.go:60`




## automod/visual/hiveai_rule.go


📄 Исходный файл: `automod/visual/hiveai_rule.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [HiveLabelBlobRule](#hivelabelblobrule-automodvisualhiveai_rulego12) `:12`


</details>


[function] name: HiveLabelBlobRule file: automod/visual/hiveai_rule.go:12 returns_error: нет description: —


### HiveLabelBlobRule (automod/visual/hiveai_rule.go:12)


HiveLabelBlobRule is a method that performs operations based on the provided parameters and returns (c *automod.RecordContext, blob lexutil.LexBlob, data []byte).


```go
func (hal *HiveAIClient) HiveLabelBlobRule((c *automod.RecordContext, blob lexutil.LexBlob, data []byte)) (c *automod.RecordContext, blob lexutil.LexBlob, data []byte)
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


📍 *Расположение:* `automod/visual/hiveai_rule.go:12`




## automod/visual/prescreen.go


📄 Исходный файл: `automod/visual/prescreen.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [NewPreScreenClient](#newprescreenclient-automodvisualprescreengo27) `:27`

- 🔗 [PreScreenImage](#prescreenimage-automodvisualprescreengo72) `:72`

- 🔗 [available](#available-automodvisualprescreengo39) `:39`

- 🔗 [checkImage](#checkimage-automodvisualprescreengo91) `:91`

- 🔗 [recordCallResult](#recordcallresult-automodvisualprescreengo54) `:54`


</details>


[function] name: NewPreScreenClient file: automod/visual/prescreen.go:27 returns_error: нет description: —


### NewPreScreenClient (automod/visual/prescreen.go:27)


NewPreScreenClient is a function that performs operations based on the provided parameters and returns (host, token string).


```go
func NewPreScreenClient((host, token string)) (host, token string)
```


**Тип ответа:** host


```json
{
  "ID": 0,
  "CreatedAt": {},
  "Host": "string",
  "SSL": false,
  "Cursor": 0,
  "Registered": false,
  "Blocked": false,
  "CrawlRateLimit": 0.0,
  "RepoCount": 0,
  "RepoLimit": 0,
  "HasActiveConnection": false,
  "EventsSeenSinceStartup": 0,
  "PerSecondEventRate": {},
  "PerHourEventRate": {},
  "PerDayEventRate": {},
  "UserCount": 0
}
```


*Определено в:* `cmd/relay/handlers_admin.go`


**Тип ответа:** token


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/visual/prescreen.go:27`



---


[function] name: PreScreenImage file: automod/visual/prescreen.go:72 returns_error: да description: —


### PreScreenImage (automod/visual/prescreen.go:72)


PreScreenImage is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *PreScreenClient) PreScreenImage((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/visual/prescreen.go:72`



---


[function] name: available file: automod/visual/prescreen.go:39 returns_error: нет description: —


### available (automod/visual/prescreen.go:39)


available is a method that performs operations based on the provided parameters and returns ().


```go
func (c *PreScreenClient) available(()) ()
```


📍 *Расположение:* `automod/visual/prescreen.go:39`



---


[function] name: checkImage file: automod/visual/prescreen.go:91 returns_error: да description: —


### checkImage (automod/visual/prescreen.go:91)


checkImage is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *PreScreenClient) checkImage((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `automod/visual/prescreen.go:91`



---


[function] name: recordCallResult file: automod/visual/prescreen.go:54 returns_error: нет description: —


### recordCallResult (automod/visual/prescreen.go:54)


recordCallResult is a method that performs operations based on the provided parameters and returns (success bool).


```go
func (c *PreScreenClient) recordCallResult((success bool)) (success bool)
```


**Тип ответа:** success


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/visual/prescreen.go:54`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_setstore.md)

- [Следующая директория](backfill.md)


---

