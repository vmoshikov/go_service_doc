---
title: "Функции: automod/keyword"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: automod/keyword
---


# Функции: automod/keyword


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_helpers.md)

- [Следующая директория](automod_rules.md)


---


## Меню по файлам


- 📄 [automod/keyword/cmd/kw-cli/main.go](#automodkeywordcmdkw-climaingo)

- 📄 [automod/keyword/keyword.go](#automodkeywordkeywordgo)

- 📄 [automod/keyword/slugify.go](#automodkeywordslugifygo)

- 📄 [automod/keyword/slur_regex.go](#automodkeywordslur_regexgo)

- 📄 [automod/keyword/tokenize.go](#automodkeywordtokenizego)


---


## automod/keyword/cmd/kw-cli/main.go


📄 Исходный файл: `automod/keyword/cmd/kw-cli/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [main](#main-automodkeywordcmdkw-climaingo16) `:16`

- 🔗 [runFuzzy](#runfuzzy-automodkeywordcmdkw-climaingo57) `:57`

- 🔗 [runTokens](#runtokens-automodkeywordcmdkw-climaingo69) `:69`


</details>


[function] name: main file: automod/keyword/cmd/kw-cli/main.go:16 returns_error: нет description: —


### main (automod/keyword/cmd/kw-cli/main.go:16)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `automod/keyword/cmd/kw-cli/main.go:16`



---


[function] name: runFuzzy file: automod/keyword/cmd/kw-cli/main.go:57 returns_error: нет description: —


### runFuzzy (automod/keyword/cmd/kw-cli/main.go:57)


runFuzzy is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runFuzzy((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `automod/keyword/cmd/kw-cli/main.go:57`



---


[function] name: runTokens file: automod/keyword/cmd/kw-cli/main.go:69 returns_error: нет description: —


### runTokens (automod/keyword/cmd/kw-cli/main.go:69)


runTokens is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runTokens((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `automod/keyword/cmd/kw-cli/main.go:69`




## automod/keyword/keyword.go


📄 Исходный файл: `automod/keyword/keyword.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [TokenInSet](#tokeninset-automodkeywordkeywordgo4) `:4`


</details>


[function] name: TokenInSet file: automod/keyword/keyword.go:4 returns_error: нет description: Helper to check a single token against a list of tokens


### TokenInSet (automod/keyword/keyword.go:4)


Helper to check a single token against a list of tokens


```go
func TokenInSet((tok string, set []string)) (tok string, set []string)
```


**Тип ответа:** tok


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** set


```json
{
  "email": "string"
}
```


*Определено в:* `api/atproto/serverrequestPasswordReset.go`


📍 *Расположение:* `automod/keyword/keyword.go:4`




## automod/keyword/slugify.go


📄 Исходный файл: `automod/keyword/slugify.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [Slugify](#slugify-automodkeywordslugifygo11) `:11`


</details>


[function] name: Slugify file: automod/keyword/slugify.go:11 returns_error: нет description: Takes an arbitrary string (eg, an identifier or free-form text) and returns a version with all non-letter, non-digit cha


### Slugify (automod/keyword/slugify.go:11)


Takes an arbitrary string (eg, an identifier or free-form text) and returns a version with all non-letter, non-digit characters removed, and all lower-case


```go
func Slugify((orig string)) (orig string)
```


**Тип ответа:** orig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/keyword/slugify.go:11`




## automod/keyword/slur_regex.go


📄 Исходный файл: `automod/keyword/slur_regex.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [SlugContainsExplicitSlur](#slugcontainsexplicitslur-automodkeywordslur_regexgo24) `:24`

- 🔗 [SlugIsExplicitSlur](#slugisexplicitslur-automodkeywordslur_regexgo34) `:34`


</details>


[function] name: SlugContainsExplicitSlur file: automod/keyword/slur_regex.go:24 returns_error: нет description: For a small set of frequently-abused explicit slurs, checks for a of permissive set of "l33t-speak" variations of the ke


### SlugContainsExplicitSlur (automod/keyword/slur_regex.go:24)


For a small set of frequently-abused explicit slurs, checks for a of permissive set of "l33t-speak" variations of the keyword. This is intended to be used with pre-processed "slugs", which are strings with all whitespace, punctuation, and other characters removed. These could be pre-processed identifiers (like handles or record keys), or pre-processed free-form text.

If there is a match, returns a plan-text version of the slur.

This is a loose port of the 'hasExplicitSlur' function from the `@atproto/pds` TypeScript package.


```go
func SlugContainsExplicitSlur((raw string)) (raw string)
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


📍 *Расположение:* `automod/keyword/slur_regex.go:24`



---


[function] name: SlugIsExplicitSlur file: automod/keyword/slur_regex.go:34 returns_error: нет description: Variant of `SlugContainsExplicitSlur` where the entire slug must match.


### SlugIsExplicitSlur (automod/keyword/slur_regex.go:34)


Variant of `SlugContainsExplicitSlur` where the entire slug must match.


```go
func SlugIsExplicitSlur((raw string)) (raw string)
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


📍 *Расположение:* `automod/keyword/slur_regex.go:34`




## automod/keyword/tokenize.go


📄 Исходный файл: `automod/keyword/tokenize.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [TokenizeIdentifier](#tokenizeidentifier-automodkeywordtokenizego51) `:51`

- 🔗 [TokenizeText](#tokenizetext-automodkeywordtokenizego36) `:36`

- 🔗 [TokenizeTextSkippingCensorChars](#tokenizetextskippingcensorchars-automodkeywordtokenizego40) `:40`

- 🔗 [TokenizeTextWithRegex](#tokenizetextwithregex-automodkeywordtokenizego23) `:23`

- 🔗 [splitIdentRune](#splitidentrune-automodkeywordtokenizego44) `:44`


</details>


[function] name: TokenizeIdentifier file: automod/keyword/tokenize.go:51 returns_error: нет description: Splits an identifier in to tokens. Removes any single-character tokens.

For example, the-handle.bsky.social would be sp


### TokenizeIdentifier (automod/keyword/tokenize.go:51)


Splits an identifier in to tokens. Removes any single-character tokens.

For example, the-handle.bsky.social would be split in to ["the", "handle", "bsky", "social"]


```go
func TokenizeIdentifier((orig string)) (orig string)
```


**Тип ответа:** orig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/keyword/tokenize.go:51`



---


[function] name: TokenizeText file: automod/keyword/tokenize.go:36 returns_error: нет description: —


### TokenizeText (automod/keyword/tokenize.go:36)


TokenizeText is a function that performs operations based on the provided parameters and returns (text string).


```go
func TokenizeText((text string)) (text string)
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


📍 *Расположение:* `automod/keyword/tokenize.go:36`



---


[function] name: TokenizeTextSkippingCensorChars file: automod/keyword/tokenize.go:40 returns_error: нет description: —


### TokenizeTextSkippingCensorChars (automod/keyword/tokenize.go:40)


TokenizeTextSkippingCensorChars is a function that performs operations based on the provided parameters and returns (text string).


```go
func TokenizeTextSkippingCensorChars((text string)) (text string)
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


📍 *Расположение:* `automod/keyword/tokenize.go:40`



---


[function] name: TokenizeTextWithRegex file: automod/keyword/tokenize.go:23 returns_error: нет description: Splits free-form text in to tokens, including lower-case, unicode normalization, and some unicode folding.

The intent i


### TokenizeTextWithRegex (automod/keyword/tokenize.go:23)


Splits free-form text in to tokens, including lower-case, unicode normalization, and some unicode folding.

The intent is for this to work similarly to an NLP tokenizer, as might be used in a fulltext search engine, and enable fast matching to a list of known tokens. It might eventually even do stemming, removing pluralization (trailing "s" for English), etc.


```go
func TokenizeTextWithRegex((text string, nonTokenCharsRegex *regexp.Regexp)) (text string, nonTokenCharsRegex *regexp.Regexp)
```


**Тип запроса:** regexp.Regexp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** nonTokenCharsRegex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** regexp.Regexp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `automod/keyword/tokenize.go:23`



---


[function] name: splitIdentRune file: automod/keyword/tokenize.go:44 returns_error: нет description: —


### splitIdentRune (automod/keyword/tokenize.go:44)


splitIdentRune is a function that performs operations based on the provided parameters and returns (c rune).


```go
func splitIdentRune((c rune)) (c rune)
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


📍 *Расположение:* `automod/keyword/tokenize.go:44`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](automod_helpers.md)

- [Следующая директория](automod_rules.md)


---

