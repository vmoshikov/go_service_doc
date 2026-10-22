---
title: "Функции: atproto/atcrypto"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: atproto/atcrypto
---


# Функции: atproto/atcrypto


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_atclient.md)

- [Следующая директория](atproto_atdata.md)


---


## Меню по файлам


- 📄 [atproto/atcrypto/cmd/atp-crypto/main.go](#atprotoatcryptocmdatp-cryptomaingo)

- 📄 [atproto/atcrypto/jwk.go](#atprotoatcryptojwkgo)

- 📄 [atproto/atcrypto/k256.go](#atprotoatcryptok256go)

- 📄 [atproto/atcrypto/keys.go](#atprotoatcryptokeysgo)

- 📄 [atproto/atcrypto/p256.go](#atprotoatcryptop256go)

- 📄 [atproto/atcrypto/p256_lowS.go](#atprotoatcryptop256_lowsgo)


---


## atproto/atcrypto/cmd/atp-crypto/main.go


📄 Исходный файл: `atproto/atcrypto/cmd/atp-crypto/main.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [main](#main-atprotoatcryptocmdatp-cryptomaingo14) `:14`

- 🔗 [runGenerate](#rungenerate-atprotoatcryptocmdatp-cryptomaingo45) `:45`


</details>


[function] name: main file: atproto/atcrypto/cmd/atp-crypto/main.go:14 returns_error: нет description: —


### main (atproto/atcrypto/cmd/atp-crypto/main.go:14)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `atproto/atcrypto/cmd/atp-crypto/main.go:14`



---


[function] name: runGenerate file: atproto/atcrypto/cmd/atp-crypto/main.go:45 returns_error: нет description: —


### runGenerate (atproto/atcrypto/cmd/atp-crypto/main.go:45)


runGenerate is a function that performs operations based on the provided parameters and returns (ctx context.Context, cmd *cli.Command).


```go
func runGenerate((ctx context.Context, cmd *cli.Command)) (ctx context.Context, cmd *cli.Command)
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


📍 *Расположение:* `atproto/atcrypto/cmd/atp-crypto/main.go:45`




## atproto/atcrypto/jwk.go


📄 Исходный файл: `atproto/atcrypto/jwk.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [JWK](#jwk-atprotoatcryptojwkgo100) `:100`

- 🔗 [JWK](#jwk-atprotoatcryptojwkgo110) `:110`

- 🔗 [ParsePublicJWK](#parsepublicjwk-atprotoatcryptojwkgo37) `:37`

- 🔗 [ParsePublicJWKBytes](#parsepublicjwkbytes-atprotoatcryptojwkgo28) `:28`


</details>


[function] name: JWK file: atproto/atcrypto/jwk.go:100 returns_error: да description: —


### JWK (atproto/atcrypto/jwk.go:100)


JWK is a method that performs operations based on the provided parameters and may return an error.


```go
func (k *PublicKeyP256) JWK((*JWK, error)) (*JWK, error)
```


**Тип запроса:** JWK


```json
{
  "KeyType": "string",
  "Curve": "string",
  "X": "string",
  "Y": "string",
  "Use": "string",
  "KeyID": "string"
}
```


*Определено в:* `atproto/atcrypto/jwk.go`


**Тип ответа:** JWK


```json
{
  "KeyType": "string",
  "Curve": "string",
  "X": "string",
  "Y": "string",
  "Use": "string",
  "KeyID": "string"
}
```


*Определено в:* `atproto/atcrypto/jwk.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*JWK`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/jwk.go:100`



---


[function] name: JWK file: atproto/atcrypto/jwk.go:110 returns_error: да description: —


### JWK (atproto/atcrypto/jwk.go:110)


JWK is a method that performs operations based on the provided parameters and may return an error.


```go
func (k *PublicKeyK256) JWK((*JWK, error)) (*JWK, error)
```


**Тип запроса:** JWK


```json
{
  "KeyType": "string",
  "Curve": "string",
  "X": "string",
  "Y": "string",
  "Use": "string",
  "KeyID": "string"
}
```


*Определено в:* `atproto/atcrypto/jwk.go`


**Тип ответа:** JWK


```json
{
  "KeyType": "string",
  "Curve": "string",
  "X": "string",
  "Y": "string",
  "Use": "string",
  "KeyID": "string"
}
```


*Определено в:* `atproto/atcrypto/jwk.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*JWK`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/jwk.go:110`



---


[function] name: ParsePublicJWK file: atproto/atcrypto/jwk.go:37 returns_error: да description: Loads a [PublicKey] from JWK struct.


### ParsePublicJWK (atproto/atcrypto/jwk.go:37)


Loads a [PublicKey] from JWK struct.


```go
func ParsePublicJWK((PublicKey, error)) (PublicKey, error)
```


**Тип ответа:** PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PublicKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/jwk.go:37`



---


[function] name: ParsePublicJWKBytes file: atproto/atcrypto/jwk.go:28 returns_error: да description: Loads a [PublicKey] from JWK (serialized as JSON bytes)


### ParsePublicJWKBytes (atproto/atcrypto/jwk.go:28)


Loads a [PublicKey] from JWK (serialized as JSON bytes)


```go
func ParsePublicJWKBytes((PublicKey, error)) (PublicKey, error)
```


**Тип ответа:** PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PublicKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/jwk.go:28`




## atproto/atcrypto/k256.go


📄 Исходный файл: `atproto/atcrypto/k256.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [Bytes](#bytes-atprotoatcryptok256go80) `:80`

- 🔗 [Bytes](#bytes-atprotoatcryptok256go179) `:179`

- 🔗 [DIDKey](#didkey-atprotoatcryptok256go225) `:225`

- 🔗 [Equal](#equal-atprotoatcryptok256go69) `:69`

- 🔗 [Equal](#equal-atprotoatcryptok256go155) `:155`

- 🔗 [GeneratePrivateKeyK256](#generateprivatekeyk256-atprotoatcryptok256go49) `:49`

- 🔗 [HashAndSign](#hashandsign-atprotoatcryptok256go109) `:109`

- 🔗 [HashAndVerify](#hashandverify-atprotoatcryptok256go191) `:191`

- 🔗 [HashAndVerifyLenient](#hashandverifylenient-atprotoatcryptok256go202) `:202`

- 🔗 [Multibase](#multibase-atprotoatcryptok256go85) `:85`

- 🔗 [Multibase](#multibase-atprotoatcryptok256go211) `:211`

- 🔗 [ParsePrivateBytesK256](#parseprivatebytesk256-atprotoatcryptok256go60) `:60`

- 🔗 [ParsePublicBytesK256](#parsepublicbytesk256-atprotoatcryptok256go117) `:117`

- 🔗 [ParsePublicUncompressedBytesK256](#parsepublicuncompressedbytesk256-atprotoatcryptok256go141) `:141`

- 🔗 [PublicKey](#publickey-atprotoatcryptok256go93) `:93`

- 🔗 [UncompressedBytes](#uncompressedbytes-atprotoatcryptok256go173) `:173`

- 🔗 [ensureBytes](#ensurebytes-atprotoatcryptok256go164) `:164`


</details>


[function] name: Bytes file: atproto/atcrypto/k256.go:80 returns_error: нет description: Serializes the secret key material in to a raw binary format, which can be parsed by [ParsePrivateBytesK256].

For K-256


### Bytes (atproto/atcrypto/k256.go:80)


Serializes the secret key material in to a raw binary format, which can be parsed by [ParsePrivateBytesK256].

For K-256, this is the "compact" encoding and is 32 bytes long. There is no ASN.1 or other enclosing structure.


```go
func (k PrivateKeyK256) Bytes(()) ()
```


📍 *Расположение:* `atproto/atcrypto/k256.go:80`



---


[function] name: Bytes file: atproto/atcrypto/k256.go:179 returns_error: нет description: Serializes the key in to "compressed" binary format.


### Bytes (atproto/atcrypto/k256.go:179)


Serializes the key in to "compressed" binary format.


```go
func (k *PublicKeyK256) Bytes(()) ()
```


📍 *Расположение:* `atproto/atcrypto/k256.go:179`



---


[function] name: DIDKey file: atproto/atcrypto/k256.go:225 returns_error: нет description: Returns a did:key string encoding of the public key, as would be encoded in a DID PLC operation:

- compressed / compact


### DIDKey (atproto/atcrypto/k256.go:225)


Returns a did:key string encoding of the public key, as would be encoded in a DID PLC operation:

- compressed / compacted binary representation
- prefix with appropriate curve multicodec bytes
- encode bytes with base58btc
- add "z" prefix to indicate encoding
- add "did:key:" prefix


```go
func (k *PublicKeyK256) DIDKey(()) ()
```


📍 *Расположение:* `atproto/atcrypto/k256.go:225`



---


[function] name: Equal file: atproto/atcrypto/k256.go:69 returns_error: нет description: Checks if the two private keys are the same. Note that the naive == operator does not work for most equality checks.


### Equal (atproto/atcrypto/k256.go:69)


Checks if the two private keys are the same. Note that the naive == operator does not work for most equality checks.


```go
func (k *PrivateKeyK256) Equal((other PrivateKey)) (other PrivateKey)
```


**Тип ответа:** other


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PrivateKey


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


📍 *Расположение:* `atproto/atcrypto/k256.go:69`



---


[function] name: Equal file: atproto/atcrypto/k256.go:155 returns_error: нет description: Checks if the two public keys are the same. Note that the naive == operator does not work for most equality checks.


### Equal (atproto/atcrypto/k256.go:155)


Checks if the two public keys are the same. Note that the naive == operator does not work for most equality checks.


```go
func (k *PublicKeyK256) Equal((other PublicKey)) (other PublicKey)
```


**Тип ответа:** other


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


📍 *Расположение:* `atproto/atcrypto/k256.go:155`



---


[function] name: GeneratePrivateKeyK256 file: atproto/atcrypto/k256.go:49 returns_error: да description: Creates a secure new cryptographic key from scratch, with the indicated curve type.


### GeneratePrivateKeyK256 (atproto/atcrypto/k256.go:49)


Creates a secure new cryptographic key from scratch, with the indicated curve type.


```go
func GeneratePrivateKeyK256((*PrivateKeyK256, error)) (*PrivateKeyK256, error)
```


**Тип запроса:** PrivateKeyK256


```json
{
  "privK256": null
}
```


*Определено в:* `atproto/atcrypto/k256.go`


**Тип ответа:** PrivateKeyK256


```json
{
  "privK256": null
}
```


*Определено в:* `atproto/atcrypto/k256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PrivateKeyK256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/k256.go:49`



---


[function] name: HashAndSign file: atproto/atcrypto/k256.go:109 returns_error: да description: First hashes the raw bytes, then signs the digest, returning a binary signature.

SHA-256 is the hash algorithm used, as


### HashAndSign (atproto/atcrypto/k256.go:109)


First hashes the raw bytes, then signs the digest, returning a binary signature.

SHA-256 is the hash algorithm used, as specified by atproto. Signing digests is the norm for ECDSA, and required by some backend implementations. This method does not "double hash", it simply has name which clarifies that hashing is happening.

Calling code is responsible for any string encoding of signatures (eg, hex or base64). For K-256, the signature is 64 bytes long.

NIST ECDSA signatures can have a "malleability" issue, meaning that there are multiple valid signatures for the same content with the same signing key. This method always returns a "low-S" signature, as required by atproto.


```go
func (k PrivateKeyK256) HashAndSign(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/k256.go:109`



---


[function] name: HashAndVerify file: atproto/atcrypto/k256.go:191 returns_error: нет description: First hashes the raw bytes, then verifies the digest, returning `nil` for valid signatures, or an error for any failure.


### HashAndVerify (atproto/atcrypto/k256.go:191)


First hashes the raw bytes, then verifies the digest, returning `nil` for valid signatures, or an error for any failure.

SHA-256 is the hash algorithm used, as specified by atproto. Signing digests is the norm for ECDSA, and required by some backend implementations. This method does not "double hash", it simply has name which clarifies that hashing is happening.

Calling code is responsible for any string decoding of signatures (eg, hex or base64) before calling this function.

This method requires a "low-S" signature, as specified by atproto.


```go
func (k *PublicKeyK256) HashAndVerify((content, sig []byte)) (content, sig []byte)
```


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `atproto/atcrypto/k256.go:191`



---


[function] name: HashAndVerifyLenient file: atproto/atcrypto/k256.go:202 returns_error: нет description: Same as HashAndVerify(), only does not require "low-S" signature.

Used for, eg, JWT validation.


### HashAndVerifyLenient (atproto/atcrypto/k256.go:202)


Same as HashAndVerify(), only does not require "low-S" signature.

Used for, eg, JWT validation.


```go
func (k *PublicKeyK256) HashAndVerifyLenient((content, sig []byte)) (content, sig []byte)
```


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `atproto/atcrypto/k256.go:202`



---


[function] name: Multibase file: atproto/atcrypto/k256.go:85 returns_error: нет description: Multibase string encoding of the private key, including a multicodec indicator


### Multibase (atproto/atcrypto/k256.go:85)


Multibase string encoding of the private key, including a multicodec indicator


```go
func (k *PrivateKeyK256) Multibase(()) ()
```


📍 *Расположение:* `atproto/atcrypto/k256.go:85`



---


[function] name: Multibase file: atproto/atcrypto/k256.go:211 returns_error: нет description: Returns a multibased string encoding of the public key, including a multicodec indicator and compressed curve bytes seri


### Multibase (atproto/atcrypto/k256.go:211)


Returns a multibased string encoding of the public key, including a multicodec indicator and compressed curve bytes serialization


```go
func (k *PublicKeyK256) Multibase(()) ()
```


📍 *Расположение:* `atproto/atcrypto/k256.go:211`



---


[function] name: ParsePrivateBytesK256 file: atproto/atcrypto/k256.go:60 returns_error: да description: Loads a [PrivateKeyK256] from raw bytes, as exported by the PrivateKey.Bytes method.

Calling code needs to know the key


### ParsePrivateBytesK256 (atproto/atcrypto/k256.go:60)


Loads a [PrivateKeyK256] from raw bytes, as exported by the PrivateKey.Bytes method.

Calling code needs to know the key type ahead of time, and must remove any string encoding (hex encoding, base64, etc) before calling this function.


```go
func ParsePrivateBytesK256((*PrivateKeyK256, error)) (*PrivateKeyK256, error)
```


**Тип запроса:** PrivateKeyK256


```json
{
  "privK256": null
}
```


*Определено в:* `atproto/atcrypto/k256.go`


**Тип ответа:** PrivateKeyK256


```json
{
  "privK256": null
}
```


*Определено в:* `atproto/atcrypto/k256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PrivateKeyK256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/k256.go:60`



---


[function] name: ParsePublicBytesK256 file: atproto/atcrypto/k256.go:117 returns_error: да description: Loads a [PublicKeyK256] raw bytes, as exported by the PublicKey.Bytes method. This is the "compressed" curve format.

Ca


### ParsePublicBytesK256 (atproto/atcrypto/k256.go:117)


Loads a [PublicKeyK256] raw bytes, as exported by the PublicKey.Bytes method. This is the "compressed" curve format.

Calling code needs to know the key type ahead of time, and must remove any string encoding (hex encoding, base64, etc) before calling this function.


```go
func ParsePublicBytesK256((*PublicKeyK256, error)) (*PublicKeyK256, error)
```


**Тип запроса:** PublicKeyK256


```json
{
  "pubK256": null
}
```


*Определено в:* `atproto/atcrypto/k256.go`


**Тип ответа:** PublicKeyK256


```json
{
  "pubK256": null
}
```


*Определено в:* `atproto/atcrypto/k256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PublicKeyK256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/k256.go:117`



---


[function] name: ParsePublicUncompressedBytesK256 file: atproto/atcrypto/k256.go:141 returns_error: да description: Loads a [PublicKeyK256] from raw bytes, as exported by the PublicKey.UncompressedBytes method.

Calling code needs to kn


### ParsePublicUncompressedBytesK256 (atproto/atcrypto/k256.go:141)


Loads a [PublicKeyK256] from raw bytes, as exported by the PublicKey.UncompressedBytes method.

Calling code needs to know the key type ahead of time, and must remove any string encoding (hex encoding, base64, etc) before calling this function.


```go
func ParsePublicUncompressedBytesK256((*PublicKeyK256, error)) (*PublicKeyK256, error)
```


**Тип запроса:** PublicKeyK256


```json
{
  "pubK256": null
}
```


*Определено в:* `atproto/atcrypto/k256.go`


**Тип ответа:** PublicKeyK256


```json
{
  "pubK256": null
}
```


*Определено в:* `atproto/atcrypto/k256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PublicKeyK256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/k256.go:141`



---


[function] name: PublicKey file: atproto/atcrypto/k256.go:93 returns_error: да description: Outputs the [PublicKey] corresponding to this [PrivateKeyK256]; it will be a [PublicKeyK256].


### PublicKey (atproto/atcrypto/k256.go:93)


Outputs the [PublicKey] corresponding to this [PrivateKeyK256]; it will be a [PublicKeyK256].


```go
func (k PrivateKeyK256) PublicKey((PublicKey, error)) (PublicKey, error)
```


**Тип ответа:** PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PublicKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/k256.go:93`



---


[function] name: UncompressedBytes file: atproto/atcrypto/k256.go:173 returns_error: нет description: Serializes the key in to "uncompressed" binary format.


### UncompressedBytes (atproto/atcrypto/k256.go:173)


Serializes the key in to "uncompressed" binary format.


```go
func (k *PublicKeyK256) UncompressedBytes(()) ()
```


📍 *Расположение:* `atproto/atcrypto/k256.go:173`



---


[function] name: ensureBytes file: atproto/atcrypto/k256.go:164 returns_error: нет description: verifies that this public key is safe to export as bytes later on


### ensureBytes (atproto/atcrypto/k256.go:164)


verifies that this public key is safe to export as bytes later on


```go
func (k *PublicKeyK256) ensureBytes(()) ()
```


📍 *Расположение:* `atproto/atcrypto/k256.go:164`




## atproto/atcrypto/keys.go


📄 Исходный файл: `atproto/atcrypto/keys.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [ParsePrivateMultibase](#parseprivatemultibase-atprotoatcryptokeysgo88) `:88`

- 🔗 [ParsePublicDIDKey](#parsepublicdidkey-atprotoatcryptokeysgo136) `:136`

- 🔗 [ParsePublicMultibase](#parsepublicmultibase-atprotoatcryptokeysgo111) `:111`


</details>


[function] name: ParsePrivateMultibase file: atproto/atcrypto/keys.go:88 returns_error: да description: Loads a private key from multibase string encoding, with multicodec indicating the key type.


### ParsePrivateMultibase (atproto/atcrypto/keys.go:88)


Loads a private key from multibase string encoding, with multicodec indicating the key type.


```go
func ParsePrivateMultibase((PrivateKeyExportable, error)) (PrivateKeyExportable, error)
```


**Тип ответа:** PrivateKeyExportable


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PrivateKeyExportable`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/keys.go:88`



---


[function] name: ParsePublicDIDKey file: atproto/atcrypto/keys.go:136 returns_error: да description: Loads a [PublicKey] from did:key string serialization.

The did:key format encodes the key type.


### ParsePublicDIDKey (atproto/atcrypto/keys.go:136)


Loads a [PublicKey] from did:key string serialization.

The did:key format encodes the key type.


```go
func ParsePublicDIDKey((PublicKey, error)) (PublicKey, error)
```


**Тип ответа:** PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PublicKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/keys.go:136`



---


[function] name: ParsePublicMultibase file: atproto/atcrypto/keys.go:111 returns_error: да description: Loads a public key from multibase string encoding, with multicodec indicating the key type.


### ParsePublicMultibase (atproto/atcrypto/keys.go:111)


Loads a public key from multibase string encoding, with multicodec indicating the key type.


```go
func ParsePublicMultibase((PublicKey, error)) (PublicKey, error)
```


**Тип ответа:** PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PublicKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/keys.go:111`




## atproto/atcrypto/p256.go


📄 Исходный файл: `atproto/atcrypto/p256.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [Bytes](#bytes-atprotoatcryptop256go82) `:82`

- 🔗 [Bytes](#bytes-atprotoatcryptop256go195) `:195`

- 🔗 [DIDKey](#didkey-atprotoatcryptop256go265) `:265`

- 🔗 [Equal](#equal-atprotoatcryptop256go71) `:71`

- 🔗 [Equal](#equal-atprotoatcryptop256go174) `:174`

- 🔗 [GeneratePrivateKeyP256](#generateprivatekeyp256-atprotoatcryptop256go33) `:33`

- 🔗 [HashAndSign](#hashandsign-atprotoatcryptop256go110) `:110`

- 🔗 [HashAndVerify](#hashandverify-atprotoatcryptop256go206) `:206`

- 🔗 [HashAndVerifyLenient](#hashandverifylenient-atprotoatcryptop256go232) `:232`

- 🔗 [Multibase](#multibase-atprotoatcryptop256go87) `:87`

- 🔗 [Multibase](#multibase-atprotoatcryptop256go251) `:251`

- 🔗 [ParsePrivateBytesP256](#parseprivatebytesp256-atprotoatcryptop256go48) `:48`

- 🔗 [ParsePublicBytesP256](#parsepublicbytesp256-atprotoatcryptop256go126) `:126`

- 🔗 [ParsePublicUncompressedBytesP256](#parsepublicuncompressedbytesp256-atprotoatcryptop256go151) `:151`

- 🔗 [PublicKey](#publickey-atprotoatcryptop256go95) `:95`

- 🔗 [UncompressedBytes](#uncompressedbytes-atprotoatcryptop256go190) `:190`

- 🔗 [checkCurve](#checkcurve-atprotoatcryptop256go182) `:182`


</details>


[function] name: Bytes file: atproto/atcrypto/p256.go:82 returns_error: нет description: Serializes the secret key material in to a raw binary format, which can be parsed by [ParsePrivateBytesP256].

For P-256


### Bytes (atproto/atcrypto/p256.go:82)


Serializes the secret key material in to a raw binary format, which can be parsed by [ParsePrivateBytesP256].

For P-256, this is the "compact" encoding and is 32 bytes long. There is no ASN.1 or other enclosing structure.


```go
func (k *PrivateKeyP256) Bytes(()) ()
```


📍 *Расположение:* `atproto/atcrypto/p256.go:82`



---


[function] name: Bytes file: atproto/atcrypto/p256.go:195 returns_error: нет description: Serializes the key in to "compressed" binary format.


### Bytes (atproto/atcrypto/p256.go:195)


Serializes the key in to "compressed" binary format.


```go
func (k *PublicKeyP256) Bytes(()) ()
```


📍 *Расположение:* `atproto/atcrypto/p256.go:195`



---


[function] name: DIDKey file: atproto/atcrypto/p256.go:265 returns_error: нет description: did:key string encoding of the public key, as would be encoded in a DID PLC operation:

- compressed / compacted binary 


### DIDKey (atproto/atcrypto/p256.go:265)


did:key string encoding of the public key, as would be encoded in a DID PLC operation:

- compressed / compacted binary representation
- prefix with appropriate curve multicodec bytes
- encode bytes with base58btc
- add "z" prefix to indicate encoding
- add "did:key:" prefix


```go
func (k *PublicKeyP256) DIDKey(()) ()
```


📍 *Расположение:* `atproto/atcrypto/p256.go:265`



---


[function] name: Equal file: atproto/atcrypto/p256.go:71 returns_error: нет description: Checks if the two private keys are the same. Note that the naive == operator does not work for most equality checks.


### Equal (atproto/atcrypto/p256.go:71)


Checks if the two private keys are the same. Note that the naive == operator does not work for most equality checks.


```go
func (k *PrivateKeyP256) Equal((other PrivateKey)) (other PrivateKey)
```


**Тип ответа:** other


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PrivateKey


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


📍 *Расположение:* `atproto/atcrypto/p256.go:71`



---


[function] name: Equal file: atproto/atcrypto/p256.go:174 returns_error: нет description: Checks if the two public keys are the same. Note that the naive == operator does not work for most equality checks.


### Equal (atproto/atcrypto/p256.go:174)


Checks if the two public keys are the same. Note that the naive == operator does not work for most equality checks.


```go
func (k *PublicKeyP256) Equal((other PublicKey)) (other PublicKey)
```


**Тип ответа:** other


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


📍 *Расположение:* `atproto/atcrypto/p256.go:174`



---


[function] name: GeneratePrivateKeyP256 file: atproto/atcrypto/p256.go:33 returns_error: да description: Creates a secure new cryptographic key from scratch.


### GeneratePrivateKeyP256 (atproto/atcrypto/p256.go:33)


Creates a secure new cryptographic key from scratch.


```go
func GeneratePrivateKeyP256((*PrivateKeyP256, error)) (*PrivateKeyP256, error)
```


**Тип запроса:** PrivateKeyP256


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Тип ответа:** PrivateKeyP256


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PrivateKeyP256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/p256.go:33`



---


[function] name: HashAndSign file: atproto/atcrypto/p256.go:110 returns_error: да description: First hashes the raw bytes, then signs the digest, returning a binary signature.

SHA-256 is the hash algorithm used, as


### HashAndSign (atproto/atcrypto/p256.go:110)


First hashes the raw bytes, then signs the digest, returning a binary signature.

SHA-256 is the hash algorithm used, as specified by atproto. Signing digests is the norm for ECDSA, and required by some backend implementations. This method does not "double hash", it simply has name which clarifies that hashing is happening.

Calling code is responsible for any string encoding of signatures (eg, hex or base64). For P-256, the signature is 64 bytes long.

NIST ECDSA signatures can have a "malleability" issue, meaning that there are multiple valid signatures for the same content with the same signing key. This method always returns a "low-S" signature, as required by atproto.


```go
func (k *PrivateKeyP256) HashAndSign(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/p256.go:110`



---


[function] name: HashAndVerify file: atproto/atcrypto/p256.go:206 returns_error: нет description: Hashes the raw bytes using SHA-256, then verifies the signature against the digest bytes.

Signing digests is the norm f


### HashAndVerify (atproto/atcrypto/p256.go:206)


Hashes the raw bytes using SHA-256, then verifies the signature against the digest bytes.

Signing digests is the norm for ECDSA, and required by some backend implementations. This method does not "double hash", it simply has name which clarifies that hashing is happening.

Calling code is responsible for any string decoding of signatures (eg, hex or base64) before calling this function.

This method requires a "low-S" signature, as specified by atproto.


```go
func (k *PublicKeyP256) HashAndVerify((content, sig []byte)) (content, sig []byte)
```


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `atproto/atcrypto/p256.go:206`



---


[function] name: HashAndVerifyLenient file: atproto/atcrypto/p256.go:232 returns_error: нет description: Same as HashAndVerify(), only does not require "low-S" signature.

Used for, eg, JWT validation.


### HashAndVerifyLenient (atproto/atcrypto/p256.go:232)


Same as HashAndVerify(), only does not require "low-S" signature.

Used for, eg, JWT validation.


```go
func (k *PublicKeyP256) HashAndVerifyLenient((content, sig []byte)) (content, sig []byte)
```


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `atproto/atcrypto/p256.go:232`



---


[function] name: Multibase file: atproto/atcrypto/p256.go:87 returns_error: нет description: Multibase string encoding of the private key, including a multicodec indicator


### Multibase (atproto/atcrypto/p256.go:87)


Multibase string encoding of the private key, including a multicodec indicator


```go
func (k *PrivateKeyP256) Multibase(()) ()
```


📍 *Расположение:* `atproto/atcrypto/p256.go:87`



---


[function] name: Multibase file: atproto/atcrypto/p256.go:251 returns_error: нет description: Multibase string encoding of the public key, including a multicodec indicator and compressed curve bytes serialization


### Multibase (atproto/atcrypto/p256.go:251)


Multibase string encoding of the public key, including a multicodec indicator and compressed curve bytes serialization


```go
func (k *PublicKeyP256) Multibase(()) ()
```


📍 *Расположение:* `atproto/atcrypto/p256.go:251`



---


[function] name: ParsePrivateBytesP256 file: atproto/atcrypto/p256.go:48 returns_error: да description: Loads a [PrivateKeyP256] from raw bytes, as exported by the PrivateKeyP256.Bytes method.

Calling code needs to know the


### ParsePrivateBytesP256 (atproto/atcrypto/p256.go:48)


Loads a [PrivateKeyP256] from raw bytes, as exported by the PrivateKeyP256.Bytes method.

Calling code needs to know the key type ahead of time, and must remove any string encoding (hex encoding, base64, etc) before calling this function.


```go
func ParsePrivateBytesP256((*PrivateKeyP256, error)) (*PrivateKeyP256, error)
```


**Тип запроса:** PrivateKeyP256


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Тип ответа:** PrivateKeyP256


```json
{
  "privP256ecdh": null,
  "privP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PrivateKeyP256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/p256.go:48`



---


[function] name: ParsePublicBytesP256 file: atproto/atcrypto/p256.go:126 returns_error: да description: Loads a [PublicKeyP256] raw bytes, as exported by the PublicKey.Bytes method. This is the "compressed" curve format.

Ca


### ParsePublicBytesP256 (atproto/atcrypto/p256.go:126)


Loads a [PublicKeyP256] raw bytes, as exported by the PublicKey.Bytes method. This is the "compressed" curve format.

Calling code needs to know the key type ahead of time, and must remove any string encoding (hex encoding, base64, etc) before calling this function.


```go
func ParsePublicBytesP256((*PublicKeyP256, error)) (*PublicKeyP256, error)
```


**Тип запроса:** PublicKeyP256


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Тип ответа:** PublicKeyP256


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PublicKeyP256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/p256.go:126`



---


[function] name: ParsePublicUncompressedBytesP256 file: atproto/atcrypto/p256.go:151 returns_error: да description: Loads a [PublicKeyP256] from raw bytes, as exported by the PublicKey.UncompressedBytes method.

Calling code needs to kn


### ParsePublicUncompressedBytesP256 (atproto/atcrypto/p256.go:151)


Loads a [PublicKeyP256] from raw bytes, as exported by the PublicKey.UncompressedBytes method.

Calling code needs to know the key type ahead of time, and must remove any string encoding (hex encoding, base64, etc) before calling this function.


```go
func ParsePublicUncompressedBytesP256((*PublicKeyP256, error)) (*PublicKeyP256, error)
```


**Тип запроса:** PublicKeyP256


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Тип ответа:** PublicKeyP256


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*PublicKeyP256`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/p256.go:151`



---


[function] name: PublicKey file: atproto/atcrypto/p256.go:95 returns_error: да description: Outputs the [PublicKey] corresponding to this [PrivateKeyP256]; it will be a [PublicKeyP256].


### PublicKey (atproto/atcrypto/p256.go:95)


Outputs the [PublicKey] corresponding to this [PrivateKeyP256]; it will be a [PublicKeyP256].


```go
func (k *PrivateKeyP256) PublicKey((PublicKey, error)) (PublicKey, error)
```


**Тип ответа:** PublicKey


```json
{
  "pubP256": {}
}
```


*Определено в:* `atproto/atcrypto/p256.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PublicKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `atproto/atcrypto/p256.go:95`



---


[function] name: UncompressedBytes file: atproto/atcrypto/p256.go:190 returns_error: нет description: Serializes the key in to "uncompressed" binary format.


### UncompressedBytes (atproto/atcrypto/p256.go:190)


Serializes the key in to "uncompressed" binary format.


```go
func (k *PublicKeyP256) UncompressedBytes(()) ()
```


📍 *Расположение:* `atproto/atcrypto/p256.go:190`



---


[function] name: checkCurve file: atproto/atcrypto/p256.go:182 returns_error: нет description: —


### checkCurve (atproto/atcrypto/p256.go:182)


checkCurve is a method that performs operations based on the provided parameters and returns ().


```go
func (k *PublicKeyP256) checkCurve(()) ()
```


📍 *Расположение:* `atproto/atcrypto/p256.go:182`




## atproto/atcrypto/p256_lowS.go


📄 Исходный файл: `atproto/atcrypto/p256_lowS.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [sigSIsLowS_P256](#sigsislows_p256-atprotoatcryptop256_lowsgo13) `:13`

- 🔗 [sigSToLowS_P256](#sigstolows_p256-atprotoatcryptop256_lowsgo19) `:19`


</details>


[function] name: sigSIsLowS_P256 file: atproto/atcrypto/p256_lowS.go:13 returns_error: нет description: Checks if 'S' value from a P-256 signature is "low-S".
un-reviewed, un-safe code from: https://github.com/golang/go/issu


### sigSIsLowS_P256 (atproto/atcrypto/p256_lowS.go:13)


Checks if 'S' value from a P-256 signature is "low-S".
un-reviewed, un-safe code from: https://github.com/golang/go/issues/54549


```go
func sigSIsLowS_P256((s *big.Int)) (s *big.Int)
```


**Тип запроса:** big.Int


```json
{
  "Type": "string",
  "Description": "string",
  "Minimum": 0,
  "Maximum": 0,
  "Enum": [],
  "Default": 0,
  "Const": 0
}
```


*Определено в:* `atproto/lexicon/language.go`


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


**Тип ответа:** big.Int


```json
{
  "Type": "string",
  "Description": "string",
  "Minimum": 0,
  "Maximum": 0,
  "Enum": [],
  "Default": 0,
  "Const": 0
}
```


*Определено в:* `atproto/lexicon/language.go`


📍 *Расположение:* `atproto/atcrypto/p256_lowS.go:13`



---


[function] name: sigSToLowS_P256 file: atproto/atcrypto/p256_lowS.go:19 returns_error: нет description: Ensures that 'S' value from a P-256 signature is "low-S" variant.
un-reviewed, un-safe code from: https://github.com/gol


### sigSToLowS_P256 (atproto/atcrypto/p256_lowS.go:19)


Ensures that 'S' value from a P-256 signature is "low-S" variant.
un-reviewed, un-safe code from: https://github.com/golang/go/issues/54549


```go
func sigSToLowS_P256((s *big.Int)) (s *big.Int)
```


**Тип запроса:** big.Int


```json
{
  "Type": "string",
  "Description": "string",
  "Minimum": 0,
  "Maximum": 0,
  "Enum": [],
  "Default": 0,
  "Const": 0
}
```


*Определено в:* `atproto/lexicon/language.go`


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


**Тип ответа:** big.Int


```json
{
  "Type": "string",
  "Description": "string",
  "Minimum": 0,
  "Maximum": 0,
  "Enum": [],
  "Default": 0,
  "Const": 0
}
```


*Определено в:* `atproto/lexicon/language.go`


📍 *Расположение:* `atproto/atcrypto/p256_lowS.go:19`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](atproto_atclient.md)

- [Следующая директория](atproto_atdata.md)


---

