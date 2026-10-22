---
title: "Функции: atproto/repo"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/repo
---


# Функции: atproto/repo


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_lexicon.md)

- [Следующая директория](atproto_syntax.md)


---


## Меню по файлам


- 📄 [atproto/repo/car.go](#atprotorepocargo)

- 📄 [atproto/repo/cbor_gen.go](#atprotorepocbor_gengo)

- 📄 [atproto/repo/cmd/repo-tool/firehose.go](#atprotorepocmdrepo-toolfirehosego)

- 📄 [atproto/repo/cmd/repo-tool/main.go](#atprotorepocmdrepo-toolmaingo)

- 📄 [atproto/repo/commit.go](#atprotorepocommitgo)

- 📄 [atproto/repo/mst/cbor_gen.go](#atprotorepomstcbor_gengo)

- 📄 [atproto/repo/mst/debug.go](#atprotorepomstdebuggo)

- 📄 [atproto/repo/mst/encoding.go](#atprotorepomstencodinggo)

- 📄 [atproto/repo/mst/node.go](#atprotorepomstnodego)

- 📄 [atproto/repo/mst/node_insert.go](#atprotorepomstnode_insertgo)

- 📄 [atproto/repo/mst/node_remove.go](#atprotorepomstnode_removego)

- 📄 [atproto/repo/mst/tree.go](#atprotorepomsttreego)

- 📄 [atproto/repo/mst/util.go](#atprotorepomstutilgo)

- 📄 [atproto/repo/mst/verify.go](#atprotorepomstverifygo)

- 📄 [atproto/repo/operation.go](#atprotorepooperationgo)

- 📄 [atproto/repo/repo.go](#atprotoreporepogo)

- 📄 [atproto/repo/sync.go](#atprotoreposyncgo)

- 📄 [atproto/repo/tiny_blockstore.go](#atprotorepotiny_blockstorego)


---


## atproto/repo/car.go


📄 Исходный файл: `atproto/repo/car.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [LoadCommitFromCAR](#loadcommitfromcar-atprotorepocargo82) `:82`

- 🔗 [LoadRepoFromCAR](#loadrepofromcar-atprotorepocargo21) `:21`


</details>


[function] name: LoadCommitFromCAR file: atproto/repo/car.go:82 returns_error: да description: LoadCommitFromCAR is like LoadRepoFromCAR() but filters to only return the commit object.
Also returns the commit CID.


### LoadCommitFromCAR (atproto/repo/car.go:82)


LoadCommitFromCAR is like LoadRepoFromCAR() but filters to only return the commit object.
Also returns the commit CID.


```go
func LoadCommitFromCAR((*Commit, *cid.Cid, error)) (*Commit, *cid.Cid, error)
```


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Commit`, `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/car.go:82`



---


[function] name: LoadRepoFromCAR file: atproto/repo/car.go:21 returns_error: да description: —


### LoadRepoFromCAR (atproto/repo/car.go:21)


LoadRepoFromCAR is a function that performs operations based on the provided parameters and may return an error.


```go
func LoadRepoFromCAR((*Commit, *Repo, error)) (*Commit, *Repo, error)
```


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип запроса:** Repo


```json
{
  "sc": {},
  "cst": {},
  "bs": {},
  "repoCid": {},
  "mst": null,
  "dirty": false,
  "clk": null
}
```


*Определено в:* `repo/repo.go`


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** Repo


```json
{
  "sc": {},
  "cst": {},
  "bs": {},
  "repoCid": {},
  "mst": null,
  "dirty": false,
  "clk": null
}
```


*Определено в:* `repo/repo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Commit`, `*Repo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/car.go:21`




## atproto/repo/cbor_gen.go


📄 Исходный файл: `atproto/repo/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-atprotorepocbor_gengo21) `:21`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotorepocbor_gengo182) `:182`


</details>


[function] name: MarshalCBOR file: atproto/repo/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (atproto/repo/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *Commit) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `atproto/repo/cbor_gen.go:21`



---


[function] name: UnmarshalCBOR file: atproto/repo/cbor_gen.go:182 returns_error: да description: —


### UnmarshalCBOR (atproto/repo/cbor_gen.go:182)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *Commit) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `atproto/repo/cbor_gen.go:182`




## atproto/repo/cmd/repo-tool/firehose.go


📄 Исходный файл: `atproto/repo/cmd/repo-tool/firehose.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [handleCommitEvent](#handlecommitevent-atprotorepocmdrepo-toolfirehosego61) `:61`

- 🔗 [runVerifyFirehose](#runverifyfirehose-atprotorepocmdrepo-toolfirehosego25) `:25`


</details>


[function] name: handleCommitEvent file: atproto/repo/cmd/repo-tool/firehose.go:61 returns_error: нет description: —


### handleCommitEvent (atproto/repo/cmd/repo-tool/firehose.go:61)


handleCommitEvent is a function that performs operations based on the provided parameters and returns (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit).


```go
func handleCommitEvent((ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)) (ctx context.Context, evt *comatproto.SyncSubscribeRepos_Commit)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** evt


```json
{
  "Flags": 0,
  "Kind": 0,
  "Seq": 0,
  "Usr": {},
  "Len": 0
}
```


*Определено в:* `events/diskpersist/diskpersist.go`


**Тип ответа:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `atproto/repo/cmd/repo-tool/firehose.go:61`



---


[function] name: runVerifyFirehose file: atproto/repo/cmd/repo-tool/firehose.go:25 returns_error: нет description: —


### runVerifyFirehose (atproto/repo/cmd/repo-tool/firehose.go:25)


runVerifyFirehose is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runVerifyFirehose((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/repo/cmd/repo-tool/firehose.go:25`




## atproto/repo/cmd/repo-tool/main.go


📄 Исходный файл: `atproto/repo/cmd/repo-tool/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [configLogger](#configlogger-atprotorepocmdrepo-toolmaingo65) `:65`

- 🔗 [main](#main-atprotorepocmdrepo-toolmaingo18) `:18`

- 🔗 [runVerifyCarMst](#runverifycarmst-atprotorepocmdrepo-toolmaingo86) `:86`

- 🔗 [runVerifyCarSignature](#runverifycarsignature-atprotorepocmdrepo-toolmaingo115) `:115`


</details>


[function] name: configLogger file: atproto/repo/cmd/repo-tool/main.go:65 returns_error: нет description: —


### configLogger (atproto/repo/cmd/repo-tool/main.go:65)


configLogger is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command, writer io.Writer).


```go
func configLogger((ctx context.Context, cmd *cli.Command, writer io.Writer)) (ctx context.Context, cmd *cli.Command, writer io.Writer)
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


**Тип ответа:** writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/repo/cmd/repo-tool/main.go:65`



---


[function] name: main file: atproto/repo/cmd/repo-tool/main.go:18 returns_error: нет description: —


### main (atproto/repo/cmd/repo-tool/main.go:18)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `atproto/repo/cmd/repo-tool/main.go:18`



---


[function] name: runVerifyCarMst file: atproto/repo/cmd/repo-tool/main.go:86 returns_error: нет description: —


### runVerifyCarMst (atproto/repo/cmd/repo-tool/main.go:86)


runVerifyCarMst is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runVerifyCarMst((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/repo/cmd/repo-tool/main.go:86`



---


[function] name: runVerifyCarSignature file: atproto/repo/cmd/repo-tool/main.go:115 returns_error: нет description: —


### runVerifyCarSignature (atproto/repo/cmd/repo-tool/main.go:115)


runVerifyCarSignature is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runVerifyCarSignature((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/repo/cmd/repo-tool/main.go:115`




## atproto/repo/commit.go


📄 Исходный файл: `atproto/repo/commit.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [AsData](#asdata-atprotorepocommitgo44) `:44`

- 🔗 [Sign](#sign-atprotorepocommitgo83) `:83`

- 🔗 [UnsignedBytes](#unsignedbytes-atprotorepocommitgo61) `:61`

- 🔗 [VerifySignature](#verifysignature-atprotorepocommitgo97) `:97`

- 🔗 [VerifyStructure](#verifystructure-atprotorepocommitgo25) `:25`


</details>


[function] name: AsData file: atproto/repo/commit.go:44 returns_error: нет description: returns a representation of the commit object as atproto data (eg, for JSON serialization)


### AsData (atproto/repo/commit.go:44)


returns a representation of the commit object as atproto data (eg, for JSON serialization)


```go
func (c *Commit) AsData(()) ()
```


📍 *Расположение:* `atproto/repo/commit.go:44`



---


[function] name: Sign file: atproto/repo/commit.go:83 returns_error: нет description: Signs the commit, storing the signature in the `Sig` field


### Sign (atproto/repo/commit.go:83)


Signs the commit, storing the signature in the `Sig` field


```go
func (c *Commit) Sign((privkey atcrypto.PrivateKey)) (privkey atcrypto.PrivateKey)
```


**Тип ответа:** privkey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atcrypto.PrivateKey


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


📍 *Расположение:* `atproto/repo/commit.go:83`



---


[function] name: UnsignedBytes file: atproto/repo/commit.go:61 returns_error: да description: Encodes the commit object as DAG-CBOR, without the signature field. Used for signing or validating signatures.


### UnsignedBytes (atproto/repo/commit.go:61)


Encodes the commit object as DAG-CBOR, without the signature field. Used for signing or validating signatures.


```go
func (c *Commit) UnsignedBytes(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/commit.go:61`



---


[function] name: VerifySignature file: atproto/repo/commit.go:97 returns_error: нет description: Verifies `Sig` field using the provided key. Returns `nil` if signature is valid.


### VerifySignature (atproto/repo/commit.go:97)


Verifies `Sig` field using the provided key. Returns `nil` if signature is valid.


```go
func (c *Commit) VerifySignature((pubkey atcrypto.PublicKey)) (pubkey atcrypto.PublicKey)
```


**Тип ответа:** pubkey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** atcrypto.PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


📍 *Расположение:* `atproto/repo/commit.go:97`



---


[function] name: VerifyStructure file: atproto/repo/commit.go:25 returns_error: нет description: does basic checks that field values and syntax are correct


### VerifyStructure (atproto/repo/commit.go:25)


does basic checks that field values and syntax are correct


```go
func (c *Commit) VerifyStructure(()) ()
```


📍 *Расположение:* `atproto/repo/commit.go:25`




## atproto/repo/mst/cbor_gen.go


📄 Исходный файл: `atproto/repo/mst/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-atprotorepomstcbor_gengo21) `:21`

- 🔗 [MarshalCBOR](#marshalcbor-atprotorepomstcbor_gengo198) `:198`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotorepomstcbor_gengo84) `:84`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-atprotorepomstcbor_gengo297) `:297`


</details>


[function] name: MarshalCBOR file: atproto/repo/mst/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (atproto/repo/mst/cbor_gen.go:21)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *NodeData) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `atproto/repo/mst/cbor_gen.go:21`



---


[function] name: MarshalCBOR file: atproto/repo/mst/cbor_gen.go:198 returns_error: нет description: —


### MarshalCBOR (atproto/repo/mst/cbor_gen.go:198)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EntryData) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `atproto/repo/mst/cbor_gen.go:198`



---


[function] name: UnmarshalCBOR file: atproto/repo/mst/cbor_gen.go:84 returns_error: да description: —


### UnmarshalCBOR (atproto/repo/mst/cbor_gen.go:84)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *NodeData) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `atproto/repo/mst/cbor_gen.go:84`



---


[function] name: UnmarshalCBOR file: atproto/repo/mst/cbor_gen.go:297 returns_error: да description: —


### UnmarshalCBOR (atproto/repo/mst/cbor_gen.go:297)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EntryData) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `atproto/repo/mst/cbor_gen.go:297`




## atproto/repo/mst/debug.go


📄 Исходный файл: `atproto/repo/mst/debug.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [DebugPrintTree](#debugprinttree-atprotorepomstdebuggo24) `:24`

- 🔗 [debugCountEntries](#debugcountentries-atprotorepomstdebuggo63) `:63`

- 🔗 [debugPrintChildPointers](#debugprintchildpointers-atprotorepomstdebuggo91) `:91`

- 🔗 [debugPrintMap](#debugprintmap-atprotorepomstdebuggo10) `:10`

- 🔗 [debugPrintNodePointers](#debugprintnodepointers-atprotorepomstdebuggo79) `:79`

- 🔗 [debugSiblingChild](#debugsiblingchild-atprotorepomstdebuggo103) `:103`


</details>


[function] name: DebugPrintTree file: atproto/repo/mst/debug.go:24 returns_error: нет description: This function is not very well implemented or correct. Should probably switch to Devin's `goat repo mst` code.


### DebugPrintTree (atproto/repo/mst/debug.go:24)


This function is not very well implemented or correct. Should probably switch to Devin's `goat repo mst` code.


```go
func DebugPrintTree((n *Node, depth int)) (n *Node, depth int)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** n


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


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** depth


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/repo/mst/debug.go:24`



---


[function] name: debugCountEntries file: atproto/repo/mst/debug.go:63 returns_error: нет description: —


### debugCountEntries (atproto/repo/mst/debug.go:63)


debugCountEntries is a function that performs operations based on the provided parameters and returns (n *Node).


```go
func debugCountEntries((n *Node)) (n *Node)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** n


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


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


📍 *Расположение:* `atproto/repo/mst/debug.go:63`



---


[function] name: debugPrintChildPointers file: atproto/repo/mst/debug.go:91 returns_error: нет description: —


### debugPrintChildPointers (atproto/repo/mst/debug.go:91)


debugPrintChildPointers is a function that performs operations based on the provided parameters and returns (n *Node).


```go
func debugPrintChildPointers((n *Node)) (n *Node)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** n


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


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


📍 *Расположение:* `atproto/repo/mst/debug.go:91`



---


[function] name: debugPrintMap file: atproto/repo/mst/debug.go:10 returns_error: нет description: —


### debugPrintMap (atproto/repo/mst/debug.go:10)


debugPrintMap is a function that performs operations based on the provided parameters and returns (m map[string]cid.Cid).


```go
func debugPrintMap((m map[string]cid.Cid)) (m map[string]cid.Cid)
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


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `atproto/repo/mst/debug.go:10`



---


[function] name: debugPrintNodePointers file: atproto/repo/mst/debug.go:79 returns_error: нет description: —


### debugPrintNodePointers (atproto/repo/mst/debug.go:79)


debugPrintNodePointers is a function that performs operations based on the provided parameters and returns (n *Node).


```go
func debugPrintNodePointers((n *Node)) (n *Node)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** n


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


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


📍 *Расположение:* `atproto/repo/mst/debug.go:79`



---


[function] name: debugSiblingChild file: atproto/repo/mst/debug.go:103 returns_error: нет description: —


### debugSiblingChild (atproto/repo/mst/debug.go:103)


debugSiblingChild is a function that performs operations based on the provided parameters and returns (n *Node).


```go
func debugSiblingChild((n *Node)) (n *Node)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** n


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


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


📍 *Расположение:* `atproto/repo/mst/debug.go:103`




## atproto/repo/mst/encoding.go


📄 Исходный файл: `atproto/repo/mst/encoding.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Bytes](#bytes-atprotorepomstencodinggo31) `:31`

- 🔗 [Node](#node-atprotorepomstencodinggo93) `:93`

- 🔗 [NodeData](#nodedata-atprotorepomstencodinggo58) `:58`

- 🔗 [NodeDataFromCBOR](#nodedatafromcbor-atprotorepomstencodinggo46) `:46`

- 🔗 [ensureHeights](#ensureheights-atprotorepomstencodinggo133) `:133`

- 🔗 [loadNodeFromStore](#loadnodefromstore-atprotorepomstencodinggo202) `:202`

- 🔗 [writeBlocks](#writeblocks-atprotorepomstencodinggo153) `:153`


</details>


[function] name: Bytes file: atproto/repo/mst/encoding.go:31 returns_error: да description: Encodes a single `NodeData` struct as CBOR bytes. Does not recursively encode or update children.


### Bytes (atproto/repo/mst/encoding.go:31)


Encodes a single `NodeData` struct as CBOR bytes. Does not recursively encode or update children.


```go
func (d *NodeData) Bytes(([]byte, *cid.Cid, error)) ([]byte, *cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/encoding.go:31`



---


[function] name: Node file: atproto/repo/mst/encoding.go:93 returns_error: нет description: Tansforms an encoded `NodeData` to `Node` data structure format.

c: optional CID argument for the CID of the CBOR repre


### Node (atproto/repo/mst/encoding.go:93)


Tansforms an encoded `NodeData` to `Node` data structure format.

c: optional CID argument for the CID of the CBOR representation of the NodeData


```go
func (d *NodeData) Node((c *cid.Cid)) (c *cid.Cid)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


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


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `atproto/repo/mst/encoding.go:93`



---


[function] name: NodeData file: atproto/repo/mst/encoding.go:58 returns_error: нет description: Transforms `Node` struct to `NodeData`, which is the format used for encoding to CBOR.

Will panic if any entries are mi


### NodeData (atproto/repo/mst/encoding.go:58)


Transforms `Node` struct to `NodeData`, which is the format used for encoding to CBOR.

Will panic if any entries are missing a CID (must compute those first)


```go
func (n *Node) NodeData(()) ()
```


📍 *Расположение:* `atproto/repo/mst/encoding.go:58`



---


[function] name: NodeDataFromCBOR file: atproto/repo/mst/encoding.go:46 returns_error: да description: Parses CBOR bytes in to `NodeData` struct


### NodeDataFromCBOR (atproto/repo/mst/encoding.go:46)


Parses CBOR bytes in to `NodeData` struct


```go
func NodeDataFromCBOR((*NodeData, error)) (*NodeData, error)
```


**Тип запроса:** NodeData


```json
{
  "Left": null,
  "Entries": []
}
```


*Определено в:* `atproto/repo/mst/encoding.go`


**Тип ответа:** NodeData


```json
{
  "Left": null,
  "Entries": []
}
```


*Определено в:* `atproto/repo/mst/encoding.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NodeData`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/encoding.go:46`



---


[function] name: ensureHeights file: atproto/repo/mst/encoding.go:133 returns_error: нет description: TODO: this feels like a hack, and easy to forget


### ensureHeights (atproto/repo/mst/encoding.go:133)


TODO: this feels like a hack, and easy to forget


```go
func (n *Node) ensureHeights(()) ()
```


📍 *Расположение:* `atproto/repo/mst/encoding.go:133`



---


[function] name: loadNodeFromStore file: atproto/repo/mst/encoding.go:202 returns_error: да description: —


### loadNodeFromStore (atproto/repo/mst/encoding.go:202)


loadNodeFromStore is a function that performs operations based on the provided parameters and may return an error.


```go
func loadNodeFromStore((*Node, error)) (*Node, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/encoding.go:202`



---


[function] name: writeBlocks file: atproto/repo/mst/encoding.go:153 returns_error: да description: Recursively encodes sub-tree, optionally writing to blockstore. Returns root CID.

This method will not error if tree is


### writeBlocks (atproto/repo/mst/encoding.go:153)


Recursively encodes sub-tree, optionally writing to blockstore. Returns root CID.

This method will not error if tree is partial.

bs: is an optional blockstore; if it is nil, blocks will not be written.
onlyDirty: is an optional blockstore; if it is nil, blocks will not be written.


```go
func (n *Node) writeBlocks((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/encoding.go:153`




## atproto/repo/mst/node.go


📄 Исходный файл: `atproto/repo/mst/node.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [IsChild](#ischild-atprotorepomstnodego69) `:69`

- 🔗 [IsEmpty](#isempty-atprotorepomstnodego40) `:40`

- 🔗 [IsPartial](#ispartial-atprotorepomstnodego45) `:45`

- 🔗 [IsValue](#isvalue-atprotorepomstnodego61) `:61`

- 🔗 [compareKey](#comparekey-atprotorepomstnodego181) `:181`

- 🔗 [deepCopy](#deepcopy-atprotorepomstnodego77) `:77`

- 🔗 [findExistingChild](#findexistingchild-atprotorepomstnodego114) `:114`

- 🔗 [findExistingEntry](#findexistingentry-atprotorepomstnodego101) `:101`

- 🔗 [findInsertionIndex](#findinsertionindex-atprotorepomstnodego136) `:136`

- 🔗 [getCID](#getcid-atprotorepomstnodego318) `:318`

- 🔗 [proveMutation](#provemutation-atprotorepomstnodego237) `:237`

- 🔗 [walk](#walk-atprotorepomstnodego294) `:294`

- 🔗 [writeToMap](#writetomap-atprotorepomstnodego274) `:274`


</details>


[function] name: IsChild file: atproto/repo/mst/node.go:69 returns_error: нет description: Returns true if this entry points to a node on a lower level


### IsChild (atproto/repo/mst/node.go:69)


Returns true if this entry points to a node on a lower level


```go
func (e *NodeEntry) IsChild(()) ()
```


📍 *Расположение:* `atproto/repo/mst/node.go:69`



---


[function] name: IsEmpty file: atproto/repo/mst/node.go:40 returns_error: нет description: —


### IsEmpty (atproto/repo/mst/node.go:40)


IsEmpty is a method that performs operations based on the provided parameters and returns ().


```go
func (n *Node) IsEmpty(()) ()
```


📍 *Расположение:* `atproto/repo/mst/node.go:40`



---


[function] name: IsPartial file: atproto/repo/mst/node.go:45 returns_error: нет description: Checks if the sub-tree (this node, or any children, recursively) contains any CID references to nodes which are not pres


### IsPartial (atproto/repo/mst/node.go:45)


Checks if the sub-tree (this node, or any children, recursively) contains any CID references to nodes which are not present.


```go
func (n *Node) IsPartial(()) ()
```


📍 *Расположение:* `atproto/repo/mst/node.go:45`



---


[function] name: IsValue file: atproto/repo/mst/node.go:61 returns_error: нет description: Returns true if this entry is a key/value at the current node


### IsValue (atproto/repo/mst/node.go:61)


Returns true if this entry is a key/value at the current node


```go
func (e *NodeEntry) IsValue(()) ()
```


📍 *Расположение:* `atproto/repo/mst/node.go:61`



---


[function] name: compareKey file: atproto/repo/mst/node.go:181 returns_error: да description: Compares a provided `key` against the overall range of keys represented by a `Node`. Returns -1 if the key sorts lower t


### compareKey (atproto/repo/mst/node.go:181)


Compares a provided `key` against the overall range of keys represented by a `Node`. Returns -1 if the key sorts lower than all keys (recursively) covered by the Node; 1 if higher, and 0 if the key falls within Node's key range.

If the `markDirty` flag is true, then this method will set the Dirty flag on this node, and any child nodes which were needed to "prove" the key order. This can be used to mark nodes for inclusion in invertible MST diffs.


```go
func (n *Node) compareKey((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node.go:181`



---


[function] name: deepCopy file: atproto/repo/mst/node.go:77 returns_error: нет description: creates a deep/recursive copy of the sub-tree


### deepCopy (atproto/repo/mst/node.go:77)


creates a deep/recursive copy of the sub-tree


```go
func (n *Node) deepCopy(()) ()
```


📍 *Расположение:* `atproto/repo/mst/node.go:77`



---


[function] name: findExistingChild file: atproto/repo/mst/node.go:114 returns_error: нет description: Looks for a "child" entry which the key would live under.

Returns -1 if not found.


### findExistingChild (atproto/repo/mst/node.go:114)


Looks for a "child" entry which the key would live under.

Returns -1 if not found.


```go
func (n *Node) findExistingChild((key []byte)) (key []byte)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/repo/mst/node.go:114`



---


[function] name: findExistingEntry file: atproto/repo/mst/node.go:101 returns_error: нет description: Looks for a "value" entry in the node with the exact key.
Returns entry index if a matching entry is found; or -1 if not


### findExistingEntry (atproto/repo/mst/node.go:101)


Looks for a "value" entry in the node with the exact key.
Returns entry index if a matching entry is found; or -1 if not found


```go
func (n *Node) findExistingEntry((key []byte)) (key []byte)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/repo/mst/node.go:101`



---


[function] name: findInsertionIndex file: atproto/repo/mst/node.go:136 returns_error: да description: Determines index where a new entry (child or value) would be inserted, relevant to the given key.

If the key would "spl


### findInsertionIndex (atproto/repo/mst/node.go:136)


Determines index where a new entry (child or value) would be inserted, relevant to the given key.

If the key would "split" an existing child entry, the index of that entry is returned, and a flag set

If the entry would be appended, then the index returned will be one higher that the current largest index.


```go
func (n *Node) findInsertionIndex((idx int, split bool, retErr error)) (idx int, split bool, retErr error)
```


**Тип ответа:** idx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** split


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** retErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `idx int`, `split bool`, `retErr error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node.go:136`



---


[function] name: getCID file: atproto/repo/mst/node.go:318 returns_error: да description: Reads the value (CID) corresponding to the key. If key is not in the tree, returns (nil, nil).

n: Node at top of sub-tr


### getCID (atproto/repo/mst/node.go:318)


Reads the value (CID) corresponding to the key. If key is not in the tree, returns (nil, nil).

n: Node at top of sub-tree to operate on. Must not be nil.
key: key or path being inserted. must not be empty/nil
height: tree height corresponding to key. if a negative value is provided, will be computed; use -1 instead of 0 if height is not known


```go
func (n *Node) getCID((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node.go:318`



---


[function] name: proveMutation file: atproto/repo/mst/node.go:237 returns_error: нет description: helper to mark nodes as "dirty" if they are needed to "prove" something about the key. used to generate invertable opera


### proveMutation (atproto/repo/mst/node.go:237)


helper to mark nodes as "dirty" if they are needed to "prove" something about the key. used to generate invertable operation diffs.


```go
func proveMutation((n *Node, key []byte)) (n *Node, key []byte)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** n


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


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/repo/mst/node.go:237`



---


[function] name: walk file: atproto/repo/mst/node.go:294 returns_error: да description: —


### walk (atproto/repo/mst/node.go:294)


walk is a method that performs operations based on the provided parameters and may return an error.


```go
func (n *Node) walk((f func(key []byte, val cid.Cid) error)) (f func(key []byte, val cid.Cid) error)
```


**Тип ответа:** f


```json
{
  "Logger": null,
  "PLCHost": "string",
  "PLCRateLimit": 0,
  "RedisURL": "string",
  "Bind": "string",
  "DisableRefresh": false
}
```


*Определено в:* `cmd/bluepages/server.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** val


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `f func(key []byte`, `val cid.Cid) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node.go:294`



---


[function] name: writeToMap file: atproto/repo/mst/node.go:274 returns_error: нет description: helper function, mostly for testing or development, which redusively inserts key/CID pairs into a `map[string]cid.Cid


### writeToMap (atproto/repo/mst/node.go:274)


helper function, mostly for testing or development, which redusively inserts key/CID pairs into a `map[string]cid.Cid


```go
func (n *Node) writeToMap((m map[string]cid.Cid)) (m map[string]cid.Cid)
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


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `atproto/repo/mst/node.go:274`




## atproto/repo/mst/node_insert.go


📄 Исходный файл: `atproto/repo/mst/node_insert.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [insert](#insert-atprotorepomstnode_insertgo19) `:19`

- 🔗 [insertChild](#insertchild-atprotorepomstnode_insertgo187) `:187`

- 🔗 [insertParent](#insertparent-atprotorepomstnode_insertgo163) `:163`

- 🔗 [split](#split-atprotorepomstnode_insertgo123) `:123`

- 🔗 [splitEntries](#splitentries-atprotorepomstnode_insertgo102) `:102`


</details>


[function] name: insert file: atproto/repo/mst/node_insert.go:19 returns_error: да description: Adds a key/CID entry to a sub-tree defined by a Node. If a previous value existed, returns it.

If the insert is a no-op


### insert (atproto/repo/mst/node_insert.go:19)


Adds a key/CID entry to a sub-tree defined by a Node. If a previous value existed, returns it.

If the insert is a no-op (the key already existed with exact value), then the operation is a no-op, the tree is not marked dirty, and the val is returned as the 'prev' value.

n: Node at top of sub-tree to operate on
key: key or path being inserted. must not be empty/nil
val: CID value being inserted
height: tree height to insert at, derived from key. if a negative value is provided, will be computed; use -1 instead of 0 if height is not known


```go
func (n *Node) insert((*Node, *cid.Cid, error)) (*Node, *cid.Cid, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node_insert.go:19`



---


[function] name: insertChild file: atproto/repo/mst/node_insert.go:187 returns_error: да description: inserts a node "below" this node in tree; either creating a new child entry or re-using an existing one


### insertChild (atproto/repo/mst/node_insert.go:187)


inserts a node "below" this node in tree; either creating a new child entry or re-using an existing one


```go
func (n *Node) insertChild((*Node, *cid.Cid, error)) (*Node, *cid.Cid, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node_insert.go:187`



---


[function] name: insertParent file: atproto/repo/mst/node_insert.go:163 returns_error: да description: inserts a node "above" this node in tree, possibly splitting the current node


### insertParent (atproto/repo/mst/node_insert.go:163)


inserts a node "above" this node in tree, possibly splitting the current node


```go
func (n *Node) insertParent((*Node, *cid.Cid, error)) (*Node, *cid.Cid, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node_insert.go:163`



---


[function] name: split file: atproto/repo/mst/node_insert.go:123 returns_error: да description: —


### split (atproto/repo/mst/node_insert.go:123)


split is a method that performs operations based on the provided parameters and may return an error.


```go
func (n *Node) split((*Node, *Node, error)) (*Node, *Node, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `*Node`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node_insert.go:123`



---


[function] name: splitEntries file: atproto/repo/mst/node_insert.go:102 returns_error: да description: —


### splitEntries (atproto/repo/mst/node_insert.go:102)


splitEntries is a method that performs operations based on the provided parameters and may return an error.


```go
func (n *Node) splitEntries((*Node, *Node, error)) (*Node, *Node, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `*Node`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node_insert.go:102`




## atproto/repo/mst/node_remove.go


📄 Исходный файл: `atproto/repo/mst/node_remove.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [mergeNodes](#mergenodes-atprotorepomstnode_removego94) `:94`

- 🔗 [remove](#remove-atprotorepomstnode_removego16) `:16`

- 🔗 [removeChild](#removechild-atprotorepomstnode_removego119) `:119`


</details>


[function] name: mergeNodes file: atproto/repo/mst/node_remove.go:94 returns_error: да description: —


### mergeNodes (atproto/repo/mst/node_remove.go:94)


mergeNodes is a function that performs operations based on the provided parameters and may return an error.


```go
func mergeNodes((*Node, error)) (*Node, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node_remove.go:94`



---


[function] name: remove file: atproto/repo/mst/node_remove.go:16 returns_error: да description: Removes key/value from the sub-tree provided, returning a new tree, and the previous CID value. If key is not found, ret


### remove (atproto/repo/mst/node_remove.go:16)


Removes key/value from the sub-tree provided, returning a new tree, and the previous CID value. If key is not found, returns unmodified subtree, and nil for the returned CID.

n: Node at top of sub-tree to operate on. Must not be nil.
key: key or path being inserted. must not be empty/nil
height: tree height corresponding to key. if a negative value is provided, will be computed; use -1 instead of 0 if height is not known


```go
func (n *Node) remove((*Node, *cid.Cid, error)) (*Node, *cid.Cid, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node_remove.go:16`



---


[function] name: removeChild file: atproto/repo/mst/node_remove.go:119 returns_error: да description: internal helper


### removeChild (atproto/repo/mst/node_remove.go:119)


internal helper


```go
func (n *Node) removeChild((*Node, *cid.Cid, error)) (*Node, *cid.Cid, error)
```


**Тип запроса:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** Node


```json
{
  "Entries": [],
  "Height": 0,
  "Dirty": false,
  "CID": null,
  "Stub": false
}
```


*Определено в:* `atproto/repo/mst/node.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Node`, `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/node_remove.go:119`




## atproto/repo/mst/tree.go


📄 Исходный файл: `atproto/repo/mst/tree.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [Copy](#copy-atprotorepomsttreego146) `:146`

- 🔗 [Get](#get-atprotorepomsttreego76) `:76`

- 🔗 [Insert](#insert-atprotorepomsttreego44) `:44`

- 🔗 [IsEmpty](#isempty-atprotorepomsttreego130) `:130`

- 🔗 [IsPartial](#ispartial-atprotorepomsttreego138) `:138`

- 🔗 [LoadTreeFromMap](#loadtreefrommap-atprotorepomsttreego89) `:89`

- 🔗 [LoadTreeFromStore](#loadtreefromstore-atprotorepomsttreego152) `:152`

- 🔗 [NewEmptyTree](#newemptytree-atprotorepomsttreego29) `:29`

- 🔗 [Remove](#remove-atprotorepomsttreego59) `:59`

- 🔗 [RootCID](#rootcid-atprotorepomsttreego122) `:122`

- 🔗 [Walk](#walk-atprotorepomsttreego84) `:84`

- 🔗 [WriteDiffBlocks](#writediffblocks-atprotorepomsttreego169) `:169`

- 🔗 [WriteToMap](#writetomap-atprotorepomsttreego107) `:107`


</details>


[function] name: Copy file: atproto/repo/mst/tree.go:146 returns_error: нет description: Creates a deep copy of MST


### Copy (atproto/repo/mst/tree.go:146)


Creates a deep copy of MST


```go
func (t *Tree) Copy(()) ()
```


📍 *Расположение:* `atproto/repo/mst/tree.go:146`



---


[function] name: Get file: atproto/repo/mst/tree.go:76 returns_error: да description: Reads the value (CID) corresponding to the key.

If key is not in the tree, returns nil, not an error.

key: key or path


### Get (atproto/repo/mst/tree.go:76)


Reads the value (CID) corresponding to the key.

If key is not in the tree, returns nil, not an error.

key: key or path being inserted. must not be empty/nil


```go
func (t *Tree) Get((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/tree.go:76`



---


[function] name: Insert file: atproto/repo/mst/tree.go:44 returns_error: да description: Adds a key/value to the tree, and returns any previously existing value (CID).

Caller can inspect the previous value to


### Insert (atproto/repo/mst/tree.go:44)


Adds a key/value to the tree, and returns any previously existing value (CID).

Caller can inspect the previous value to determine if the behavior was a "creation" (key didn't exist), an "update" (key existed with a different value), or no-op (key existed with current value).

key: key or path being inserted. must not be empty/nil
val: CID value being inserted


```go
func (t *Tree) Insert((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/tree.go:44`



---


[function] name: IsEmpty file: atproto/repo/mst/tree.go:130 returns_error: нет description: If the tree contains no key/value pairs, returns true.


### IsEmpty (atproto/repo/mst/tree.go:130)


If the tree contains no key/value pairs, returns true.


```go
func (t *Tree) IsEmpty(()) ()
```


📍 *Расположение:* `atproto/repo/mst/tree.go:130`



---


[function] name: IsPartial file: atproto/repo/mst/tree.go:138 returns_error: нет description: Returns false if all nodes in the tree are available in-memory in decoded format; otherwise returns true. Does not consi


### IsPartial (atproto/repo/mst/tree.go:138)


Returns false if all nodes in the tree are available in-memory in decoded format; otherwise returns true. Does not consider record data, only MST nodes.


```go
func (t *Tree) IsPartial(()) ()
```


📍 *Расположение:* `atproto/repo/mst/tree.go:138`



---


[function] name: LoadTreeFromMap file: atproto/repo/mst/tree.go:89 returns_error: да description: Creates a new Tree by loading key/value pairs from a map.


### LoadTreeFromMap (atproto/repo/mst/tree.go:89)


Creates a new Tree by loading key/value pairs from a map.


```go
func LoadTreeFromMap((*Tree, error)) (*Tree, error)
```


**Тип запроса:** Tree


```json
{
  "Root": null
}
```


*Определено в:* `atproto/repo/mst/tree.go`


**Тип ответа:** Tree


```json
{
  "Root": null
}
```


*Определено в:* `atproto/repo/mst/tree.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Tree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/tree.go:89`



---


[function] name: LoadTreeFromStore file: atproto/repo/mst/tree.go:152 returns_error: да description: —


### LoadTreeFromStore (atproto/repo/mst/tree.go:152)


LoadTreeFromStore is a function that performs operations based on the provided parameters and may return an error.


```go
func LoadTreeFromStore((*Tree, error)) (*Tree, error)
```


**Тип запроса:** Tree


```json
{
  "Root": null
}
```


*Определено в:* `atproto/repo/mst/tree.go`


**Тип ответа:** Tree


```json
{
  "Root": null
}
```


*Определено в:* `atproto/repo/mst/tree.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Tree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/tree.go:152`



---


[function] name: NewEmptyTree file: atproto/repo/mst/tree.go:29 returns_error: нет description: —


### NewEmptyTree (atproto/repo/mst/tree.go:29)


NewEmptyTree is a function that performs operations based on the provided parameters and returns ().


```go
func NewEmptyTree(()) ()
```


📍 *Расположение:* `atproto/repo/mst/tree.go:29`



---


[function] name: Remove file: atproto/repo/mst/tree.go:59 returns_error: да description: Removes key/value from the sub-tree provided. Return the previous CID value, if any. If key was not found, returns nil (


### Remove (atproto/repo/mst/tree.go:59)


Removes key/value from the sub-tree provided. Return the previous CID value, if any. If key was not found, returns nil (which is not an error).

key: key or path being inserted. must not be empty/nil


```go
func (t *Tree) Remove((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/tree.go:59`



---


[function] name: RootCID file: atproto/repo/mst/tree.go:122 returns_error: да description: Returns the overall root-node CID for the MST.

If possible, lazily returned a known value. If necessary, recursively en


### RootCID (atproto/repo/mst/tree.go:122)


Returns the overall root-node CID for the MST.

If possible, lazily returned a known value. If necessary, recursively encodes tree nodes to compute CIDs.

NOTE: will mark the tree "clean" (clear any dirty flags).


```go
func (t *Tree) RootCID((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/tree.go:122`



---


[function] name: Walk file: atproto/repo/mst/tree.go:84 returns_error: да description: Walks the Tree, invoking the callback function on each key/value pair.


### Walk (atproto/repo/mst/tree.go:84)


Walks the Tree, invoking the callback function on each key/value pair.


```go
func (t *Tree) Walk((f func(key []byte, val cid.Cid) error)) (f func(key []byte, val cid.Cid) error)
```


**Тип ответа:** f


```json
{
  "Logger": null,
  "PLCHost": "string",
  "PLCRateLimit": 0,
  "RedisURL": "string",
  "Bind": "string",
  "DisableRefresh": false
}
```


*Определено в:* `cmd/bluepages/server.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** val


```json
{
  "db": null,
  "lk": {},
  "lastCommitCache": {},
  "log": null
}
```


*Определено в:* `carstore/nonarchive.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `f func(key []byte`, `val cid.Cid) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/tree.go:84`



---


[function] name: WriteDiffBlocks file: atproto/repo/mst/tree.go:169 returns_error: да description: Walks the tree, encodes any "dirty" nodes as CBOR data, and writes that data as blocks to the provided blockstore. Retur


### WriteDiffBlocks (atproto/repo/mst/tree.go:169)


Walks the tree, encodes any "dirty" nodes as CBOR data, and writes that data as blocks to the provided blockstore. Returns root CID.


```go
func (t *Tree) WriteDiffBlocks((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/mst/tree.go:169`



---


[function] name: WriteToMap file: atproto/repo/mst/tree.go:107 returns_error: нет description: Recursively walks the tree and writes key/value pairs to map `m`

The map (`m`) is mutated in place (by reference); the 


### WriteToMap (atproto/repo/mst/tree.go:107)


Recursively walks the tree and writes key/value pairs to map `m`

The map (`m`) is mutated in place (by reference); the map must be initialized before calling.


```go
func (t *Tree) WriteToMap((m map[string]cid.Cid)) (m map[string]cid.Cid)
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


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `atproto/repo/mst/tree.go:107`




## atproto/repo/mst/util.go


📄 Исходный файл: `atproto/repo/mst/util.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [CountPrefixLen](#countprefixlen-atprotorepomstutilgo41) `:41`

- 🔗 [HeightForKey](#heightforkey-atprotorepomstutilgo15) `:15`

- 🔗 [IsValidKey](#isvalidkey-atprotorepomstutilgo52) `:52`


</details>


[function] name: CountPrefixLen file: atproto/repo/mst/util.go:41 returns_error: нет description: Computes the common prefix length between two bytestrings.

Used when compacting node entry lists for encoding.


### CountPrefixLen (atproto/repo/mst/util.go:41)


Computes the common prefix length between two bytestrings.

Used when compacting node entry lists for encoding.


```go
func CountPrefixLen((a, b []byte)) (a, b []byte)
```


**Тип ответа:** a


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


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


📍 *Расположение:* `atproto/repo/mst/util.go:41`



---


[function] name: HeightForKey file: atproto/repo/mst/util.go:15 returns_error: нет description: Computes the MST "height" for a key (bytestring). Layers are counted from the "bottom" of the tree, starting with zero.



### HeightForKey (atproto/repo/mst/util.go:15)


Computes the MST "height" for a key (bytestring). Layers are counted from the "bottom" of the tree, starting with zero.

For atproto repository v3, uses SHA-256 as the hashing function and counts two bits at a time, for an MST "fanout" value of 16.


```go
func HeightForKey((height int)) (height int)
```


**Тип ответа:** height


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/repo/mst/util.go:15`



---


[function] name: IsValidKey file: atproto/repo/mst/util.go:52 returns_error: нет description: —


### IsValidKey (atproto/repo/mst/util.go:52)


IsValidKey is a function that performs operations based on the provided parameters and returns (key []byte).


```go
func IsValidKey((key []byte)) (key []byte)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/repo/mst/util.go:52`




## atproto/repo/mst/verify.go


📄 Исходный файл: `atproto/repo/mst/verify.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Verify](#verify-atprotorepomstverifygo8) `:8`

- 🔗 [verifyStructure](#verifystructure-atprotorepomstverifygo15) `:15`


</details>


[function] name: Verify file: atproto/repo/mst/verify.go:8 returns_error: нет description: —


### Verify (atproto/repo/mst/verify.go:8)


Verify is a method that performs operations based on the provided parameters and returns ().


```go
func (t *Tree) Verify(()) ()
```


📍 *Расположение:* `atproto/repo/mst/verify.go:8`



---


[function] name: verifyStructure file: atproto/repo/mst/verify.go:15 returns_error: нет description: —


### verifyStructure (atproto/repo/mst/verify.go:15)


verifyStructure is a method that performs operations based on the provided parameters and returns (height int, key []byte).


```go
func (n *Node) verifyStructure((height int, key []byte)) (height int, key []byte)
```


**Тип ответа:** height


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `atproto/repo/mst/verify.go:15`




## atproto/repo/operation.go


📄 Исходный файл: `atproto/repo/operation.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [ApplyOp](#applyop-atprotorepooperationgo46) `:46`

- 🔗 [CheckOp](#checkop-atprotorepooperationgo73) `:73`

- 🔗 [InvertOp](#invertop-atprotorepooperationgo94) `:94`

- 🔗 [IsCreate](#iscreate-atprotorepooperationgo24) `:24`

- 🔗 [IsDelete](#isdelete-atprotorepooperationgo38) `:38`

- 🔗 [IsUpdate](#isupdate-atprotorepooperationgo31) `:31`

- 🔗 [Len](#len-atprotorepooperationgo130) `:130`

- 🔗 [Less](#less-atprotorepooperationgo133) `:133`

- 🔗 [NormalizeOps](#normalizeops-atprotorepooperationgo145) `:145`

- 🔗 [Swap](#swap-atprotorepooperationgo131) `:131`


</details>


[function] name: ApplyOp file: atproto/repo/operation.go:46 returns_error: да description: Mutates the tree, returning a full `Operation`


### ApplyOp (atproto/repo/operation.go:46)


Mutates the tree, returning a full `Operation`


```go
func ApplyOp((*Operation, error)) (*Operation, error)
```


**Тип запроса:** Operation


```json
{
  "op": 0,
  "sub": null,
  "evt": null
}
```


*Определено в:* `events/events.go`


**Тип ответа:** Operation


```json
{
  "op": 0,
  "sub": null,
  "evt": null
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Operation`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/operation.go:46`



---


[function] name: CheckOp file: atproto/repo/operation.go:73 returns_error: нет description: Does a simple "forwards" (not inversion) check of operation


### CheckOp (atproto/repo/operation.go:73)


Does a simple "forwards" (not inversion) check of operation


```go
func CheckOp((tree *mst.Tree, op *Operation)) (tree *mst.Tree, op *Operation)
```


**Тип запроса:** mst.Tree


```json
{
  "Root": null
}
```


*Определено в:* `atproto/repo/mst/tree.go`


**Тип запроса:** Operation


```json
{
  "op": 0,
  "sub": null,
  "evt": null
}
```


*Определено в:* `events/events.go`


**Тип ответа:** tree


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mst.Tree


```json
{
  "Root": null
}
```


*Определено в:* `atproto/repo/mst/tree.go`


**Тип ответа:** op


```json
{
  "HTTPMethod": "string",
  "TargetURI": "string",
  "AccessTokenHash": "string",
  "Nonce": "string"
}
```


*Определено в:* `atproto/auth/oauth/oauth.go`


**Тип ответа:** Operation


```json
{
  "op": 0,
  "sub": null,
  "evt": null
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `atproto/repo/operation.go:73`



---


[function] name: InvertOp file: atproto/repo/operation.go:94 returns_error: нет description: Applies the inversion of the `op` to the `tree`. This mutates the tree.


### InvertOp (atproto/repo/operation.go:94)


Applies the inversion of the `op` to the `tree`. This mutates the tree.


```go
func InvertOp((tree *mst.Tree, op *Operation)) (tree *mst.Tree, op *Operation)
```


**Тип запроса:** mst.Tree


```json
{
  "Root": null
}
```


*Определено в:* `atproto/repo/mst/tree.go`


**Тип запроса:** Operation


```json
{
  "op": 0,
  "sub": null,
  "evt": null
}
```


*Определено в:* `events/events.go`


**Тип ответа:** tree


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mst.Tree


```json
{
  "Root": null
}
```


*Определено в:* `atproto/repo/mst/tree.go`


**Тип ответа:** op


```json
{
  "HTTPMethod": "string",
  "TargetURI": "string",
  "AccessTokenHash": "string",
  "Nonce": "string"
}
```


*Определено в:* `atproto/auth/oauth/oauth.go`


**Тип ответа:** Operation


```json
{
  "op": 0,
  "sub": null,
  "evt": null
}
```


*Определено в:* `events/events.go`


📍 *Расположение:* `atproto/repo/operation.go:94`



---


[function] name: IsCreate file: atproto/repo/operation.go:24 returns_error: нет description: —


### IsCreate (atproto/repo/operation.go:24)


IsCreate is a method that performs operations based on the provided parameters and returns ().


```go
func (op *Operation) IsCreate(()) ()
```


📍 *Расположение:* `atproto/repo/operation.go:24`



---


[function] name: IsDelete file: atproto/repo/operation.go:38 returns_error: нет description: —


### IsDelete (atproto/repo/operation.go:38)


IsDelete is a method that performs operations based on the provided parameters and returns ().


```go
func (op *Operation) IsDelete(()) ()
```


📍 *Расположение:* `atproto/repo/operation.go:38`



---


[function] name: IsUpdate file: atproto/repo/operation.go:31 returns_error: нет description: —


### IsUpdate (atproto/repo/operation.go:31)


IsUpdate is a method that performs operations based on the provided parameters and returns ().


```go
func (op *Operation) IsUpdate(()) ()
```


📍 *Расположение:* `atproto/repo/operation.go:31`



---


[function] name: Len file: atproto/repo/operation.go:130 returns_error: нет description: —


### Len (atproto/repo/operation.go:130)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (a opByPath) Len(()) ()
```


📍 *Расположение:* `atproto/repo/operation.go:130`



---


[function] name: Less file: atproto/repo/operation.go:133 returns_error: нет description: —


### Less (atproto/repo/operation.go:133)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (a opByPath) Less((i, j int)) (i, j int)
```


**Тип ответа:** i


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** j


```json
{
  "Link": "string"
}
```


*Определено в:* `atproto/atdata/cidlink.go`


📍 *Расположение:* `atproto/repo/operation.go:133`



---


[function] name: NormalizeOps file: atproto/repo/operation.go:145 returns_error: да description: re-orders operation list, and checks for duplicates


### NormalizeOps (atproto/repo/operation.go:145)


re-orders operation list, and checks for duplicates


```go
func NormalizeOps(([]Operation, error)) ([]Operation, error)
```


**Тип ответа:** Operation


```json
{
  "op": 0,
  "sub": null,
  "evt": null
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]Operation`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/operation.go:145`



---


[function] name: Swap file: atproto/repo/operation.go:131 returns_error: нет description: —


### Swap (atproto/repo/operation.go:131)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (a opByPath) Swap((i, j int)) (i, j int)
```


**Тип ответа:** i


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** j


```json
{
  "Link": "string"
}
```


*Определено в:* `atproto/atdata/cidlink.go`


📍 *Расположение:* `atproto/repo/operation.go:131`




## atproto/repo/repo.go


📄 Исходный файл: `atproto/repo/repo.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Commit](#commit-atprotoreporepogo69) `:69`

- 🔗 [GetRecordBytes](#getrecordbytes-atprotoreporepogo55) `:55`

- 🔗 [GetRecordCID](#getrecordcid-atprotoreporepogo43) `:43`


</details>


[function] name: Commit file: atproto/repo/repo.go:69 returns_error: да description: Snapshots the current state of the repository, resulting in a new (unsigned) `Commit` struct.


### Commit (atproto/repo/repo.go:69)


Snapshots the current state of the repository, resulting in a new (unsigned) `Commit` struct.


```go
func (repo *Repo) Commit((*Commit, error)) (*Commit, error)
```


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Commit`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/repo.go:69`



---


[function] name: GetRecordBytes file: atproto/repo/repo.go:55 returns_error: да description: —


### GetRecordBytes (atproto/repo/repo.go:55)


GetRecordBytes is a method that retrieves data based on the provided parameters and may return an error.


```go
func (repo *Repo) GetRecordBytes(([]byte, *cid.Cid, error)) ([]byte, *cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/repo.go:55`



---


[function] name: GetRecordCID file: atproto/repo/repo.go:43 returns_error: да description: func NewEmptyRepo(did syntax.DID) Repo {
clk := syntax.NewTIDClock(0)
return Repo{
DID:         did,
Clock:       &clk,



### GetRecordCID (atproto/repo/repo.go:43)


func NewEmptyRepo(did syntax.DID) Repo {
clk := syntax.NewTIDClock(0)
return Repo{
DID:         did,
Clock:       &clk,
RecordStore: blockstore.NewBlockstore(datastore.NewMapDatastore()),
MST:         mst.NewEmptyTree(),
}
}


```go
func (repo *Repo) GetRecordCID((*cid.Cid, error)) (*cid.Cid, error)
```


**Тип запроса:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/repo.go:43`




## atproto/repo/sync.go


📄 Исходный файл: `atproto/repo/sync.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [VerifyCommitMessage](#verifycommitmessage-atprotoreposyncgo19) `:19`

- 🔗 [VerifyCommitSignature](#verifycommitsignature-atprotoreposyncgo174) `:174`

- 🔗 [VerifyCommitSignatureFromCar](#verifycommitsignaturefromcar-atprotoreposyncgo179) `:179`

- 🔗 [VerifySyncMessage](#verifysyncmessage-atprotoreposyncgo167) `:167`

- 🔗 [parseCommitOps](#parsecommitops-atprotoreposyncgo125) `:125`


</details>


[function] name: VerifyCommitMessage file: atproto/repo/sync.go:19 returns_error: да description: temporary/experimental method to parse and verify a firehose commit message.

TODO: move to a separate 'sync' package? b


### VerifyCommitMessage (atproto/repo/sync.go:19)


temporary/experimental method to parse and verify a firehose commit message.

TODO: move to a separate 'sync' package? break up in to smaller components?


```go
func VerifyCommitMessage((*Repo, error)) (*Repo, error)
```


**Тип запроса:** Repo


```json
{
  "sc": {},
  "cst": {},
  "bs": {},
  "repoCid": {},
  "mst": null,
  "dirty": false,
  "clk": null
}
```


*Определено в:* `repo/repo.go`


**Тип ответа:** Repo


```json
{
  "sc": {},
  "cst": {},
  "bs": {},
  "repoCid": {},
  "mst": null,
  "dirty": false,
  "clk": null
}
```


*Определено в:* `repo/repo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Repo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/sync.go:19`



---


[function] name: VerifyCommitSignature file: atproto/repo/sync.go:174 returns_error: нет description: temporary/experimental code showing how to verify a commit signature from firehose

TODO: in real implementation, will w


### VerifyCommitSignature (atproto/repo/sync.go:174)


temporary/experimental code showing how to verify a commit signature from firehose

TODO: in real implementation, will want to merge this code with `VerifyCommitMessage` above, and have it hanging off some service struct with a configured `identity.Directory`


```go
func VerifyCommitSignature((ctx context.Context, dir identity.Directory, msg *comatproto.SyncSubscribeRepos_Commit)) (ctx context.Context, dir identity.Directory, msg *comatproto.SyncSubscribeRepos_Commit)
```


**Тип запроса:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


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


**Тип ответа:** dir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** identity.Directory


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


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** comatproto.SyncSubscribeRepos_Commit


```json
{
  "blobs": [],
  "blocks": {},
  "commit": {},
  "ops": [],
  "prevData": null,
  "rebase": false,
  "repo": "string",
  "rev": "string",
  "seq": 0,
  "since": "string",
  "time": "string",
  "tooBig": false
}
```


*Определено в:* `api/atproto/syncsubscribeRepos.go`


📍 *Расположение:* `atproto/repo/sync.go:174`



---


[function] name: VerifyCommitSignatureFromCar file: atproto/repo/sync.go:179 returns_error: да description: —


### VerifyCommitSignatureFromCar (atproto/repo/sync.go:179)


VerifyCommitSignatureFromCar is a function that performs operations based on the provided parameters and may return an error.


```go
func VerifyCommitSignatureFromCar((*Commit, error)) (*Commit, error)
```


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Commit`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/sync.go:179`



---


[function] name: VerifySyncMessage file: atproto/repo/sync.go:167 returns_error: да description: —


### VerifySyncMessage (atproto/repo/sync.go:167)


VerifySyncMessage is a function that performs operations based on the provided parameters and may return an error.


```go
func VerifySyncMessage((*Commit, error)) (*Commit, error)
```


**Тип запроса:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Тип ответа:** Commit


```json
{
  "did": "string",
  "version": 0,
  "prev": null,
  "data": {},
  "sig": [],
  "rev": "string"
}
```


*Определено в:* `atproto/repo/commit.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Commit`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/sync.go:167`



---


[function] name: parseCommitOps file: atproto/repo/sync.go:125 returns_error: да description: —


### parseCommitOps (atproto/repo/sync.go:125)


parseCommitOps is a function that performs operations based on the provided parameters and may return an error.


```go
func parseCommitOps(([]Operation, error)) ([]Operation, error)
```


**Тип ответа:** Operation


```json
{
  "op": 0,
  "sub": null,
  "evt": null
}
```


*Определено в:* `events/events.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]Operation`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/sync.go:125`




## atproto/repo/tiny_blockstore.go


📄 Исходный файл: `atproto/repo/tiny_blockstore.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Get](#get-atprotorepotiny_blockstorego26) `:26`

- 🔗 [NewTinyBlockstore](#newtinyblockstore-atprotorepotiny_blockstorego15) `:15`

- 🔗 [Put](#put-atprotorepotiny_blockstorego19) `:19`


</details>


[function] name: Get file: atproto/repo/tiny_blockstore.go:26 returns_error: да description: —


### Get (atproto/repo/tiny_blockstore.go:26)


Get is a method that retrieves data based on the provided parameters and may return an error.


```go
func (tb *TinyBlockstore) Get((blocks.Block, error)) (blocks.Block, error)
```


**Тип ответа:** blocks.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `blocks.Block`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/repo/tiny_blockstore.go:26`



---


[function] name: NewTinyBlockstore file: atproto/repo/tiny_blockstore.go:15 returns_error: нет description: —


### NewTinyBlockstore (atproto/repo/tiny_blockstore.go:15)


NewTinyBlockstore is a function that performs operations based on the provided parameters and returns ().


```go
func NewTinyBlockstore(()) ()
```


📍 *Расположение:* `atproto/repo/tiny_blockstore.go:15`



---


[function] name: Put file: atproto/repo/tiny_blockstore.go:19 returns_error: нет description: —


### Put (atproto/repo/tiny_blockstore.go:19)


Put is a method that performs operations based on the provided parameters and returns (_ context.Context, block blocks.Block).


```go
func (tb *TinyBlockstore) Put((_ context.Context, block blocks.Block)) (_ context.Context, block blocks.Block)
```


**Тип ответа:** _


```json
{
  "Response": {}
}
```


*Определено в:* `automod/visual/hiveai_client.go`


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


**Тип ответа:** block


```json
{
  "ID": 0,
  "Cid": {},
  "Shard": 0,
  "Offset": 0
}
```


*Определено в:* `carstore/meta_gorm.go`


**Тип ответа:** blocks.Block


```json
{
  "blocks": {}
}
```


*Определено в:* `atproto/repo/tiny_blockstore.go`


📍 *Расположение:* `atproto/repo/tiny_blockstore.go:19`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_lexicon.md)

- [Следующая директория](atproto_syntax.md)


---

