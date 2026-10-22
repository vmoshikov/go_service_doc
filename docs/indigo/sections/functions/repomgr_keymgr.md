---
title: "Функции: repomgr/keymgr"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: repomgr/keymgr
---


# Функции: repomgr/keymgr


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](repomgr.md)

- [Следующая директория](search.md)


---


## Меню по файлам


- 📄 [repomgr/keymgr/keymgr.go](#repomgrkeymgrkeymgrgo)


---


## repomgr/keymgr/keymgr.go


📄 Исходный файл: `repomgr/keymgr/keymgr.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [NewKeyManager](#newkeymanager-repomgrkeymgrkeymgrgo25) `:25`

- 🔗 [SignForUser](#signforuser-repomgrkeymgrkeymgrgo68) `:68`

- 🔗 [VerifyUserSignature](#verifyusersignature-repomgrkeymgrkeymgrgo33) `:33`

- 🔗 [getKey](#getkey-repomgrkeymgrkeymgrgo49) `:49`


</details>


[function] name: NewKeyManager file: repomgr/keymgr/keymgr.go:25 returns_error: нет description: —


### NewKeyManager (repomgr/keymgr/keymgr.go:25)


NewKeyManager is a function that performs operations based on the provided parameters and returns (didr DidResolver, k *did.PrivKey).


```go
func NewKeyManager((didr DidResolver, k *did.PrivKey)) (didr DidResolver, k *did.PrivKey)
```


**Тип запроса:** did.PrivKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** didr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DidResolver


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** k


```json
{
  "logger": null,
  "webhookURL": "string",
  "adminPassword": "string",
  "httpClient": null
}
```


*Определено в:* `cmd/tap/webhook_client.go`


**Тип ответа:** did.PrivKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repomgr/keymgr/keymgr.go:25`



---


[function] name: SignForUser file: repomgr/keymgr/keymgr.go:68 returns_error: да description: —


### SignForUser (repomgr/keymgr/keymgr.go:68)


SignForUser is a method that performs operations based on the provided parameters and may return an error.


```go
func (km *KeyManager) SignForUser(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/keymgr/keymgr.go:68`



---


[function] name: VerifyUserSignature file: repomgr/keymgr/keymgr.go:33 returns_error: нет description: —


### VerifyUserSignature (repomgr/keymgr/keymgr.go:33)


VerifyUserSignature is a method that performs operations based on the provided parameters and returns (ctx context.Context, did string, sig []byte, msg []byte).


```go
func (km *KeyManager) VerifyUserSignature((ctx context.Context, did string, sig []byte, msg []byte)) (ctx context.Context, did string, sig []byte, msg []byte)
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


**Тип ответа:** did


```json
{
  "Updated": {},
  "RawDoc": {},
  "Err": {}
}
```


*Определено в:* `cmd/bluepages/resolver.go`


**Тип ответа:** sig


```json
{
  "cid": "string",
  "cts": "string",
  "exp": "string",
  "neg": false,
  "src": "string",
  "uri": "string",
  "val": "string",
  "ver": 0
}
```


*Определено в:* `util/labels/labels.go`


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `repomgr/keymgr/keymgr.go:33`



---


[function] name: getKey file: repomgr/keymgr/keymgr.go:49 returns_error: да description: —


### getKey (repomgr/keymgr/keymgr.go:49)


getKey is a method that performs operations based on the provided parameters and may return an error.


```go
func (km *KeyManager) getKey((*did.PubKey, error)) (*did.PubKey, error)
```


**Тип запроса:** did.PubKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** did.PubKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*did.PubKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `repomgr/keymgr/keymgr.go:49`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](repomgr.md)

- [Следующая директория](search.md)


---

