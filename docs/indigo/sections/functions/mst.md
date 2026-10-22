---
title: "Функции: mst"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: mst
---


# Функции: mst


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](models.md)

- [Следующая директория](repo.md)


---


## Меню по файлам


- 📄 [mst/cbor_gen.go](#mstcbor_gengo)

- 📄 [mst/diff.go](#mstdiffgo)

- 📄 [mst/mst.go](#mstmstgo)

- 📄 [mst/mst_util.go](#mstmst_utilgo)


---


## mst/cbor_gen.go


📄 Исходный файл: `mst/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-mstcbor_gengo21) `:21`

- 🔗 [MarshalCBOR](#marshalcbor-mstcbor_gengo198) `:198`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-mstcbor_gengo84) `:84`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-mstcbor_gengo297) `:297`


</details>


[function] name: MarshalCBOR file: mst/cbor_gen.go:21 returns_error: нет description: —


### MarshalCBOR (mst/cbor_gen.go:21)


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


📍 *Расположение:* `mst/cbor_gen.go:21`



---


[function] name: MarshalCBOR file: mst/cbor_gen.go:198 returns_error: нет description: —


### MarshalCBOR (mst/cbor_gen.go:198)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *TreeEntry) MarshalCBOR((w io.Writer)) (w io.Writer)
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


📍 *Расположение:* `mst/cbor_gen.go:198`



---


[function] name: UnmarshalCBOR file: mst/cbor_gen.go:84 returns_error: да description: —


### UnmarshalCBOR (mst/cbor_gen.go:84)


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


📍 *Расположение:* `mst/cbor_gen.go:84`



---


[function] name: UnmarshalCBOR file: mst/cbor_gen.go:297 returns_error: да description: —


### UnmarshalCBOR (mst/cbor_gen.go:297)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *TreeEntry) UnmarshalCBOR((err error)) (err error)
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


📍 *Расположение:* `mst/cbor_gen.go:297`




## mst/diff.go


📄 Исходный файл: `mst/diff.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [DiffTrees](#difftrees-mstdiffgo21) `:21`

- 🔗 [identityDiff](#identitydiff-mstdiffgo188) `:188`

- 🔗 [nodeEntriesEqual](#nodeentriesequal-mstdiffgo172) `:172`


</details>


[function] name: DiffTrees file: mst/diff.go:21 returns_error: да description: TODO: this code isn't great, should be rewritten on top of the baseline datastructures once functional and correct


### DiffTrees (mst/diff.go:21)


TODO: this code isn't great, should be rewritten on top of the baseline datastructures once functional and correct


```go
func DiffTrees(([]*DiffOp, error)) ([]*DiffOp, error)
```


**Тип запроса:** DiffOp


```json
{
  "Depth": 0,
  "Op": "string",
  "Rpath": "string",
  "OldCid": {},
  "NewCid": {}
}
```


*Определено в:* `mst/diff.go`


**Тип ответа:** DiffOp


```json
{
  "Depth": 0,
  "Op": "string",
  "Rpath": "string",
  "OldCid": {},
  "NewCid": {}
}
```


*Определено в:* `mst/diff.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*DiffOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/diff.go:21`



---


[function] name: identityDiff file: mst/diff.go:188 returns_error: да description: —


### identityDiff (mst/diff.go:188)


identityDiff is a function that performs operations based on the provided parameters and may return an error.


```go
func identityDiff(([]*DiffOp, error)) ([]*DiffOp, error)
```


**Тип запроса:** DiffOp


```json
{
  "Depth": 0,
  "Op": "string",
  "Rpath": "string",
  "OldCid": {},
  "NewCid": {}
}
```


*Определено в:* `mst/diff.go`


**Тип ответа:** DiffOp


```json
{
  "Depth": 0,
  "Op": "string",
  "Rpath": "string",
  "OldCid": {},
  "NewCid": {}
}
```


*Определено в:* `mst/diff.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*DiffOp`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/diff.go:188`



---


[function] name: nodeEntriesEqual file: mst/diff.go:172 returns_error: нет description: —


### nodeEntriesEqual (mst/diff.go:172)


nodeEntriesEqual is a function that performs operations based on the provided parameters and returns (a, b *nodeEntry).


```go
func nodeEntriesEqual((a, b *nodeEntry)) (a, b *nodeEntry)
```


**Тип запроса:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


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


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


📍 *Расположение:* `mst/diff.go:172`




## mst/mst.go


📄 Исходный файл: `mst/mst.go`


<details open>
<summary><b>Функции в этом файле (37)</b></summary>


- 🔗 [Add](#add-mstmstgo324) `:324`

- 🔗 [CBORTypes](#cbortypes-mstmstgo106) `:106`

- 🔗 [Delete](#delete-mstmstgo567) `:567`

- 🔗 [Get](#get-mstmstgo488) `:488`

- 🔗 [GetPointer](#getpointer-mstmstgo231) `:231`

- 🔗 [LoadMST](#loadmst-mstmstgo164) `:164`

- 🔗 [NewEmptyMST](#newemptymst-mstmstgo143) `:143`

- 🔗 [Update](#update-mstmstgo517) `:517`

- 🔗 [WalkLeavesFrom](#walkleavesfrom-mstmstgo941) `:941`

- 🔗 [WalkLeavesFromNocache](#walkleavesfromnocache-mstmstgo948) `:948`

- 🔗 [append](#append-mstmstgo676) `:676`

- 🔗 [appendMerge](#appendmerge-mstmstgo853) `:853`

- 🔗 [atIndex](#atindex-mstmstgo707) `:707`

- 🔗 [attemptGetLayer](#attemptgetlayer-mstmstgo284) `:284`

- 🔗 [checkTreeInvariant](#checktreeinvariant-mstmstgo96) `:96`

- 🔗 [createChild](#createchild-mstmstgo895) `:895`

- 🔗 [createMST](#createmst-mstmstgo148) `:148`

- 🔗 [createParent](#createparent-mstmstgo904) `:904`

- 🔗 [deleteRecurse](#deleterecurse-mstmstgo576) `:576`

- 🔗 [entriesFromNodeData](#entriesfromnodedata-mstmstgo213) `:213`

- 🔗 [entryCount](#entrycount-mstmstgo843) `:843`

- 🔗 [findGtOrEqualLeafIndex](#findgtorequalleafindex-mstmstgo917) `:917`

- 🔗 [getEntries](#getentries-mstmstgo183) `:183`

- 🔗 [getLayer](#getlayer-mstmstgo270) `:270`

- 🔗 [isLeaf](#isleaf-mstmstgo87) `:87`

- 🔗 [isTree](#istree-mstmstgo83) `:83`

- 🔗 [isUndefined](#isundefined-mstmstgo91) `:91`

- 🔗 [mkTreeEntry](#mktreeentry-mstmstgo76) `:76`

- 🔗 [newTree](#newtree-mstmstgo172) `:172`

- 🔗 [prepend](#prepend-mstmstgo691) `:691`

- 🔗 [removeEntry](#removeentry-mstmstgo661) `:661`

- 🔗 [replaceWithSplit](#replacewithsplit-mstmstgo740) `:740`

- 🔗 [spliceIn](#splicein-mstmstgo724) `:724`

- 🔗 [splitAround](#splitaround-mstmstgo787) `:787`

- 🔗 [trimTop](#trimtop-mstmstgo772) `:772`

- 🔗 [updateEntry](#updateentry-mstmstgo645) `:645`

- 🔗 [walkLeavesFrom](#walkleavesfrom-mstmstgo952) `:952`


</details>


[function] name: Add file: mst/mst.go:324 returns_error: да description: "Adds a new leaf for the given key/value pair. Throws if a leaf with that key already exists"
Typescript: MST.add(key, v


### Add (mst/mst.go:324)


"Adds a new leaf for the given key/value pair. Throws if a leaf with that key already exists"
Typescript: MST.add(key, value, knownZeros?) -> MST


```go
func (mst *MerkleSearchTree) Add((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:324`



---


[function] name: CBORTypes file: mst/mst.go:106 returns_error: нет description: CBORTypes returns the types in this package that need to be registered with
the CBOR codec.


### CBORTypes (mst/mst.go:106)


CBORTypes returns the types in this package that need to be registered with
the CBOR codec.


```go
func CBORTypes(()) ()
```


📍 *Расположение:* `mst/mst.go:106`



---


[function] name: Delete file: mst/mst.go:567 returns_error: да description: "Deletes the value at the given key"
Typescript: MST.delete(key) -> MST


### Delete (mst/mst.go:567)


"Deletes the value at the given key"
Typescript: MST.delete(key) -> MST


```go
func (mst *MerkleSearchTree) Delete((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:567`



---


[function] name: Get file: mst/mst.go:488 returns_error: да description: "Gets the value at the given key"
Typescript: MST.get(key) -> (CID|null)


### Get (mst/mst.go:488)


"Gets the value at the given key"
Typescript: MST.get(key) -> (CID|null)


```go
func (mst *MerkleSearchTree) Get((cid.Cid, error)) (cid.Cid, error)
```


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:488`



---


[function] name: GetPointer file: mst/mst.go:231 returns_error: да description: "We don't hash the node on every mutation for performance reasons. Instead we keep track of whether the pointer is outda


### GetPointer (mst/mst.go:231)


"We don't hash the node on every mutation for performance reasons. Instead we keep track of whether the pointer is outdated and only (recursively) calculate when needed"
Typescript: MST.getPointer() -> CID


```go
func (mst *MerkleSearchTree) GetPointer((cid.Cid, error)) (cid.Cid, error)
```


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:231`



---


[function] name: LoadMST file: mst/mst.go:164 returns_error: нет description: This is poorly named in both implementations, because it is lazy
Typescript: MST.load(storage, cid, layer=null, fanout) 


### LoadMST (mst/mst.go:164)


This is poorly named in both implementations, because it is lazy
Typescript: MST.load(storage, cid, layer=null, fanout) -> MST


```go
func LoadMST((cst cbor.IpldStore, root cid.Cid)) (cst cbor.IpldStore, root cid.Cid)
```


**Тип ответа:** cst


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cbor.IpldStore


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** root


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


📍 *Расположение:* `mst/mst.go:164`



---


[function] name: NewEmptyMST file: mst/mst.go:143 returns_error: нет description: NewEmptyMST reports a new empty MST using cst as its storage.


### NewEmptyMST (mst/mst.go:143)


NewEmptyMST reports a new empty MST using cst as its storage.


```go
func NewEmptyMST((cst cbor.IpldStore)) (cst cbor.IpldStore)
```


**Тип ответа:** cst


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cbor.IpldStore


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `mst/mst.go:143`



---


[function] name: Update file: mst/mst.go:517 returns_error: да description: "Edits the value at the given key. Throws if the given key does not exist"
Typescript: MST.update(key, value) -> MST


### Update (mst/mst.go:517)


"Edits the value at the given key. Throws if the given key does not exist"
Typescript: MST.update(key, value) -> MST


```go
func (mst *MerkleSearchTree) Update((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:517`



---


[function] name: WalkLeavesFrom file: mst/mst.go:941 returns_error: да description: WalkLeavesFrom walks the leaves of the tree, calling the cb callback on each
key that's greater than or equal to the pro


### WalkLeavesFrom (mst/mst.go:941)


WalkLeavesFrom walks the leaves of the tree, calling the cb callback on each
key that's greater than or equal to the provided from key.
If cb returns an error, the walk is aborted and the error is returned.
NB: this method caches the tree structure in memory to make subsequent tree
operations significantly faster


```go
func (mst *MerkleSearchTree) WalkLeavesFrom((ctx context.Context, from string, cb func(key string, val cid.Cid) error)) (ctx context.Context, from string, cb func(key string, val cid.Cid) error)
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


**Тип ответа:** from


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `ctx context.Context`, `from string`, `cb func(key string`, `val cid.Cid) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:941`



---


[function] name: WalkLeavesFromNocache file: mst/mst.go:948 returns_error: да description: WalkLeavesFromNocache works the same as WalkLeavesFrom but does not cache
internal tree structure, intended for "once th


### WalkLeavesFromNocache (mst/mst.go:948)


WalkLeavesFromNocache works the same as WalkLeavesFrom but does not cache
internal tree structure, intended for "once through" passes of MSTs,
especially in streaming contexts


```go
func (mst *MerkleSearchTree) WalkLeavesFromNocache((ctx context.Context, from string, cb func(key string, val cid.Cid) error)) (ctx context.Context, from string, cb func(key string, val cid.Cid) error)
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


**Тип ответа:** from


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `ctx context.Context`, `from string`, `cb func(key string`, `val cid.Cid) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:948`



---


[function] name: append file: mst/mst.go:676 returns_error: да description: "append entry to end of the node"


### append (mst/mst.go:676)


"append entry to end of the node"


```go
func (mst *MerkleSearchTree) append((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:676`



---


[function] name: appendMerge file: mst/mst.go:853 returns_error: да description: "The simple merge case where every key in the right tree is greater than every key in the left tree (used primarily for 


### appendMerge (mst/mst.go:853)


"The simple merge case where every key in the right tree is greater than every key in the left tree (used primarily for deletes)"


```go
func (mst *MerkleSearchTree) appendMerge((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:853`



---


[function] name: atIndex file: mst/mst.go:707 returns_error: да description: "returns entry at index"
Apparently returns null if nothing at index, which seems brittle


### atIndex (mst/mst.go:707)


"returns entry at index"
Apparently returns null if nothing at index, which seems brittle


```go
func (mst *MerkleSearchTree) atIndex((nodeEntry, error)) (nodeEntry, error)
```


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `nodeEntry`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:707`



---


[function] name: attemptGetLayer file: mst/mst.go:284 returns_error: да description: Typescript: MST.attemptGetLayer() -> number


### attemptGetLayer (mst/mst.go:284)


Typescript: MST.attemptGetLayer() -> number


```go
func (mst *MerkleSearchTree) attemptGetLayer((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:284`



---


[function] name: checkTreeInvariant file: mst/mst.go:96 returns_error: нет description: golang-specific helper to sanity check nodeEntry semantics


### checkTreeInvariant (mst/mst.go:96)


golang-specific helper to sanity check nodeEntry semantics


```go
func checkTreeInvariant((ents []nodeEntry)) (ents []nodeEntry)
```


**Тип ответа:** ents


```json
{
  "cursor": "string",
  "limit": 0,
  "patternType": "string",
  "sortDirection": "string",
  "urls": []
}
```


*Определено в:* `api/ozone/safelinkqueryEvents.go`


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


📍 *Расположение:* `mst/mst.go:96`



---


[function] name: createChild file: mst/mst.go:895 returns_error: да description: === "Create relatives" ===


### createChild (mst/mst.go:895)


=== "Create relatives" ===


```go
func (mst *MerkleSearchTree) createChild((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:895`



---


[function] name: createMST file: mst/mst.go:148 returns_error: нет description: Typescript: MST.create(storage, entries, layer, fanout) -> MST


### createMST (mst/mst.go:148)


Typescript: MST.create(storage, entries, layer, fanout) -> MST


```go
func createMST((cst cbor.IpldStore, ptr cid.Cid, entries []nodeEntry, layer int)) (cst cbor.IpldStore, ptr cid.Cid, entries []nodeEntry, layer int)
```


**Тип ответа:** cst


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cbor.IpldStore


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ptr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Тип ответа:** entries


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** layer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `mst/mst.go:148`



---


[function] name: createParent file: mst/mst.go:904 returns_error: да description: —


### createParent (mst/mst.go:904)


createParent is a method that performs operations based on the provided parameters and may return an error.


```go
func (mst *MerkleSearchTree) createParent((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:904`



---


[function] name: deleteRecurse file: mst/mst.go:576 returns_error: да description: Typescript: MST.deleteRecurse(key) -> MST


### deleteRecurse (mst/mst.go:576)


Typescript: MST.deleteRecurse(key) -> MST


```go
func (mst *MerkleSearchTree) deleteRecurse((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:576`



---


[function] name: entriesFromNodeData file: mst/mst.go:213 returns_error: да description: golang-specific helper that calls in to deserializeNodeData


### entriesFromNodeData (mst/mst.go:213)


golang-specific helper that calls in to deserializeNodeData


```go
func entriesFromNodeData(([]nodeEntry, error)) ([]nodeEntry, error)
```


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]nodeEntry`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:213`



---


[function] name: entryCount file: mst/mst.go:843 returns_error: нет description: —


### entryCount (mst/mst.go:843)


entryCount is a method that performs operations based on the provided parameters and returns ().


```go
func (mst *MerkleSearchTree) entryCount(()) ()
```


📍 *Расположение:* `mst/mst.go:843`



---


[function] name: findGtOrEqualLeafIndex file: mst/mst.go:917 returns_error: да description: NOTE(@why): this smells inefficient
"finds index of first leaf node that is greater than or equal to the value"


### findGtOrEqualLeafIndex (mst/mst.go:917)


NOTE(@why): this smells inefficient
"finds index of first leaf node that is greater than or equal to the value"


```go
func (mst *MerkleSearchTree) findGtOrEqualLeafIndex((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:917`



---


[function] name: getEntries file: mst/mst.go:183 returns_error: да description: "We don't want to load entries of every subtree, just the ones we need"
Typescript: MST.getEntries() -> nodeEntry[]


### getEntries (mst/mst.go:183)


"We don't want to load entries of every subtree, just the ones we need"
Typescript: MST.getEntries() -> nodeEntry[]


```go
func (mst *MerkleSearchTree) getEntries(([]nodeEntry, error)) ([]nodeEntry, error)
```


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]nodeEntry`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:183`



---


[function] name: getLayer file: mst/mst.go:270 returns_error: да description: "In most cases, we get the layer of a node from a hint on creation"
"In the case of the topmost node in the tree, we loo


### getLayer (mst/mst.go:270)


"In most cases, we get the layer of a node from a hint on creation"
"In the case of the topmost node in the tree, we look for a key in the node & determine the layer"
"In the case where we don't find one, we recurse down until we do."
"If we still can't find one, then we have an empty tree and the node is layer 0"
Typescript: MST.getLayer() -> number


```go
func (mst *MerkleSearchTree) getLayer((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:270`



---


[function] name: isLeaf file: mst/mst.go:87 returns_error: нет description: —


### isLeaf (mst/mst.go:87)


isLeaf is a method that performs operations based on the provided parameters and returns ().


```go
func (ne nodeEntry) isLeaf(()) ()
```


📍 *Расположение:* `mst/mst.go:87`



---


[function] name: isTree file: mst/mst.go:83 returns_error: нет description: —


### isTree (mst/mst.go:83)


isTree is a method that performs operations based on the provided parameters and returns ().


```go
func (ne nodeEntry) isTree(()) ()
```


📍 *Расположение:* `mst/mst.go:83`



---


[function] name: isUndefined file: mst/mst.go:91 returns_error: нет description: —


### isUndefined (mst/mst.go:91)


isUndefined is a method that performs operations based on the provided parameters and returns ().


```go
func (ne nodeEntry) isUndefined(()) ()
```


📍 *Расположение:* `mst/mst.go:91`



---


[function] name: mkTreeEntry file: mst/mst.go:76 returns_error: нет description: —


### mkTreeEntry (mst/mst.go:76)


mkTreeEntry is a function that performs operations based on the provided parameters and returns (t *MerkleSearchTree).


```go
func mkTreeEntry((t *MerkleSearchTree)) (t *MerkleSearchTree)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** t


```json
{
  "Repo": "string",
  "State": "string",
  "FinishedAt": {}
}
```


*Определено в:* `cmd/netsync/main.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


📍 *Расположение:* `mst/mst.go:76`



---


[function] name: newTree file: mst/mst.go:172 returns_error: нет description: "We never mutate an MST, we just return a new MST with updated values"
Typescript: MST.newTree(entries) -> MST


### newTree (mst/mst.go:172)


"We never mutate an MST, we just return a new MST with updated values"
Typescript: MST.newTree(entries) -> MST


```go
func (mst *MerkleSearchTree) newTree((entries []nodeEntry)) (entries []nodeEntry)
```


**Тип ответа:** entries


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


📍 *Расположение:* `mst/mst.go:172`



---


[function] name: prepend file: mst/mst.go:691 returns_error: да description: "prepend entry to start of the node"


### prepend (mst/mst.go:691)


"prepend entry to start of the node"


```go
func (mst *MerkleSearchTree) prepend((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:691`



---


[function] name: removeEntry file: mst/mst.go:661 returns_error: да description: "remove entry at index"


### removeEntry (mst/mst.go:661)


"remove entry at index"


```go
func (mst *MerkleSearchTree) removeEntry((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:661`



---


[function] name: replaceWithSplit file: mst/mst.go:740 returns_error: да description: "replaces an entry with [ Maybe(tree), Leaf, Maybe(tree) ]"


### replaceWithSplit (mst/mst.go:740)


"replaces an entry with [ Maybe(tree), Leaf, Maybe(tree) ]"


```go
func (mst *MerkleSearchTree) replaceWithSplit((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:740`



---


[function] name: spliceIn file: mst/mst.go:724 returns_error: да description: "inserts entry at index"


### spliceIn (mst/mst.go:724)


"inserts entry at index"


```go
func (mst *MerkleSearchTree) spliceIn((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:724`



---


[function] name: splitAround file: mst/mst.go:787 returns_error: да description: "Recursively splits a sub tree around a given key"


### splitAround (mst/mst.go:787)


"Recursively splits a sub tree around a given key"


```go
func (mst *MerkleSearchTree) splitAround((*MerkleSearchTree, *MerkleSearchTree, error)) (*MerkleSearchTree, *MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:787`



---


[function] name: trimTop file: mst/mst.go:772 returns_error: да description: "if the topmost node in the tree only points to another tree, trim the top and return the subtree"


### trimTop (mst/mst.go:772)


"if the topmost node in the tree only points to another tree, trim the top and return the subtree"


```go
func (mst *MerkleSearchTree) trimTop((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:772`



---


[function] name: updateEntry file: mst/mst.go:645 returns_error: да description: "update entry in place"
Typescript: MST.updateEntry(index, entry) -> MST


### updateEntry (mst/mst.go:645)


"update entry in place"
Typescript: MST.updateEntry(index, entry) -> MST


```go
func (mst *MerkleSearchTree) updateEntry((*MerkleSearchTree, error)) (*MerkleSearchTree, error)
```


**Тип запроса:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Тип ответа:** MerkleSearchTree


```json
{
  "cst": {},
  "entries": [],
  "layer": 0,
  "pointer": {},
  "validPtr": false
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*MerkleSearchTree`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:645`



---


[function] name: walkLeavesFrom file: mst/mst.go:952 returns_error: да description: —


### walkLeavesFrom (mst/mst.go:952)


walkLeavesFrom is a method that performs operations based on the provided parameters and may return an error.


```go
func (mst *MerkleSearchTree) walkLeavesFrom((ctx context.Context, from string, nocache bool, cb func(key string, val cid.Cid) error)) (ctx context.Context, from string, nocache bool, cb func(key string, val cid.Cid) error)
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


**Тип ответа:** from


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nocache


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cb


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `ctx context.Context`, `from string`, `nocache bool`, `cb func(key string`, `val cid.Cid) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst.go:952`




## mst/mst_util.go


📄 Исходный файл: `mst/mst_util.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [cidForEntries](#cidforentries-mstmst_utilgo190) `:190`

- 🔗 [countPrefixLen](#countprefixlen-mstmst_utilgo175) `:175`

- 🔗 [deserializeNodeData](#deserializenodedata-mstmst_utilgo69) `:69`

- 🔗 [ensureValidMstKey](#ensurevalidmstkey-mstmst_utilgo235) `:235`

- 🔗 [isValidMstKey](#isvalidmstkey-mstmst_utilgo224) `:224`

- 🔗 [keyHasAllValidChars](#keyhasallvalidchars-mstmst_utilgo202) `:202`

- 🔗 [layerForEntries](#layerforentries-mstmst_utilgo52) `:52`

- 🔗 [leadingZerosOnHash](#leadingzerosonhash-mstmst_utilgo20) `:20`

- 🔗 [leadingZerosOnHashBytes](#leadingzerosonhashbytes-mstmst_utilgo28) `:28`

- 🔗 [serializeNodeData](#serializenodedata-mstmst_utilgo114) `:114`


</details>


[function] name: cidForEntries file: mst/mst_util.go:190 returns_error: да description: both computes *and* persists a tree entry; this is different from typescript
implementation
Typescript: cidForEntries(en


### cidForEntries (mst/mst_util.go:190)


both computes *and* persists a tree entry; this is different from typescript
implementation
Typescript: cidForEntries(entries) -> CID


```go
func cidForEntries((cid.Cid, error)) (cid.Cid, error)
```


**Тип ответа:** cid.Cid


```json
{
  "ActionId": 0,
  "Cid": "string"
}
```


*Определено в:* `models/moderation.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `cid.Cid`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst_util.go:190`



---


[function] name: countPrefixLen file: mst/mst_util.go:175 returns_error: нет description: how many leading bytes are identical between the two strings?
Typescript: countPrefixLen(a: string, b: string) -> number


### countPrefixLen (mst/mst_util.go:175)


how many leading bytes are identical between the two strings?
Typescript: countPrefixLen(a: string, b: string) -> number


```go
func countPrefixLen((a, b string)) (a, b string)
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


📍 *Расположение:* `mst/mst_util.go:175`



---


[function] name: deserializeNodeData file: mst/mst_util.go:69 returns_error: да description: Typescript: deserializeNodeData(storage, data, layer)


### deserializeNodeData (mst/mst_util.go:69)


Typescript: deserializeNodeData(storage, data, layer)


```go
func deserializeNodeData(([]nodeEntry, error)) ([]nodeEntry, error)
```


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]nodeEntry`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `mst/mst_util.go:69`



---


[function] name: ensureValidMstKey file: mst/mst_util.go:235 returns_error: нет description: Typescript: ensureValidMstKey(str)


### ensureValidMstKey (mst/mst_util.go:235)


Typescript: ensureValidMstKey(str)


```go
func ensureValidMstKey((s string)) (s string)
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


📍 *Расположение:* `mst/mst_util.go:235`



---


[function] name: isValidMstKey file: mst/mst_util.go:224 returns_error: нет description: Typescript: isValidMstKey(str)


### isValidMstKey (mst/mst_util.go:224)


Typescript: isValidMstKey(str)


```go
func isValidMstKey((s string)) (s string)
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


📍 *Расположение:* `mst/mst_util.go:224`



---


[function] name: keyHasAllValidChars file: mst/mst_util.go:202 returns_error: нет description: keyHasAllValidChars reports whether s matches
the regexp /^[a-zA-Z0-9_:.~-]+$/ without using regexp,
which is slower.


### keyHasAllValidChars (mst/mst_util.go:202)


keyHasAllValidChars reports whether s matches
the regexp /^[a-zA-Z0-9_:.~-]+$/ without using regexp,
which is slower.


```go
func keyHasAllValidChars((s string)) (s string)
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


📍 *Расположение:* `mst/mst_util.go:202`



---


[function] name: layerForEntries file: mst/mst_util.go:52 returns_error: нет description: Typescript: layerForEntries(entries, fanout) -> (number?)


### layerForEntries (mst/mst_util.go:52)


Typescript: layerForEntries(entries, fanout) -> (number?)


```go
func layerForEntries((entries []nodeEntry)) (entries []nodeEntry)
```


**Тип ответа:** entries


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeEntry


```json
{
  "Kind": {},
  "Key": "string",
  "Val": {},
  "Tree": null
}
```


*Определено в:* `mst/mst.go`


📍 *Расположение:* `mst/mst_util.go:52`



---


[function] name: leadingZerosOnHash file: mst/mst_util.go:20 returns_error: нет description: Used to determine the "depth" of keys in an MST.
For atproto, repo v2, the "fanout" is always 4, so we count "zeros" in



### leadingZerosOnHash (mst/mst_util.go:20)


Used to determine the "depth" of keys in an MST.
For atproto, repo v2, the "fanout" is always 4, so we count "zeros" in
chunks of 2-bits. Eg, a leading 0x00 byte is 4 "zeros".
Typescript: leadingZerosOnHash(key, fanout) -> number


```go
func leadingZerosOnHash((key string)) (key string)
```


**Тип ответа:** key


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `mst/mst_util.go:20`



---


[function] name: leadingZerosOnHashBytes file: mst/mst_util.go:28 returns_error: нет description: —


### leadingZerosOnHashBytes (mst/mst_util.go:28)


leadingZerosOnHashBytes is a function that performs operations based on the provided parameters and returns (total int).


```go
func leadingZerosOnHashBytes((total int)) (total int)
```


**Тип ответа:** total


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `mst/mst_util.go:28`



---


[function] name: serializeNodeData file: mst/mst_util.go:114 returns_error: да description: Typescript: serializeNodeData(entries) -> NodeData


### serializeNodeData (mst/mst_util.go:114)


Typescript: serializeNodeData(entries) -> NodeData


```go
func serializeNodeData((*NodeData, error)) (*NodeData, error)
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


📍 *Расположение:* `mst/mst_util.go:114`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](models.md)

- [Следующая директория](repo.md)


---

