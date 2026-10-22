---
title: "Функции: util/ssrf"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: util/ssrf
---


# Функции: util/ssrf


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_labels.md)

- [Следующая директория](util_svcutil.md)


---


## Меню по файлам


- 📄 [util/ssrf/ssrf.go](#utilssrfssrfgo)


---


## util/ssrf/ssrf.go


📄 Исходный файл: `util/ssrf/ssrf.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [IsPublicIPAddress](#ispublicipaddress-utilssrfssrfgo69) `:69`

- 🔗 [PublicOnlyControl](#publiconlycontrol-utilssrfssrfgo78) `:78`

- 🔗 [PublicOnlyDialer](#publiconlydialer-utilssrfssrfgo105) `:105`

- 🔗 [PublicOnlyTransport](#publiconlytransport-utilssrfssrfgo117) `:117`

- 🔗 [ipv4Net](#ipv4net-utilssrfssrfgo26) `:26`

- 🔗 [isIPv4Reserved](#isipv4reserved-utilssrfssrfgo60) `:60`

- 🔗 [isIPv6GlobalUnicast](#isipv6globalunicast-utilssrfssrfgo56) `:56`


</details>


[function] name: IsPublicIPAddress file: util/ssrf/ssrf.go:69 returns_error: нет description: —


### IsPublicIPAddress (util/ssrf/ssrf.go:69)


IsPublicIPAddress is a function that performs operations based on the provided parameters and returns (address net.IP).


```go
func IsPublicIPAddress((address net.IP)) (address net.IP)
```


**Тип ответа:** address


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IP


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/ssrf/ssrf.go:69`



---


[function] name: PublicOnlyControl file: util/ssrf/ssrf.go:78 returns_error: нет description: Implementation of [net.Dialer] `Control` field (a function) which avoids some SSRF attacks by rejecting local IPv4 and I


### PublicOnlyControl (util/ssrf/ssrf.go:78)


Implementation of [net.Dialer] `Control` field (a function) which avoids some SSRF attacks by rejecting local IPv4 and IPv6 address ranges, and only allowing ports 80 or 443.


```go
func PublicOnlyControl((network string, address string, conn syscall.RawConn)) (network string, address string, conn syscall.RawConn)
```


**Тип ответа:** network


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** address


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** conn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** syscall.RawConn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/ssrf/ssrf.go:78`



---


[function] name: PublicOnlyDialer file: util/ssrf/ssrf.go:105 returns_error: нет description: [net.Dialer] with [PublicOnlyControl] for `Control` function (for SSRF protection). Other fields are same default values


### PublicOnlyDialer (util/ssrf/ssrf.go:105)


[net.Dialer] with [PublicOnlyControl] for `Control` function (for SSRF protection). Other fields are same default values as standard library.


```go
func PublicOnlyDialer(()) ()
```


📍 *Расположение:* `util/ssrf/ssrf.go:105`



---


[function] name: PublicOnlyTransport file: util/ssrf/ssrf.go:117 returns_error: нет description: [http.Transport] with [PublicOnlyDialer] for `DialContext` field (for SSRF protection). Other fields are same default va


### PublicOnlyTransport (util/ssrf/ssrf.go:117)


[http.Transport] with [PublicOnlyDialer] for `DialContext` field (for SSRF protection). Other fields are same default values as standard library.

Use this in an [http.Client] like: `c := http.Client{ Transport: PublicOnlyTransport() }`


```go
func PublicOnlyTransport(()) ()
```


📍 *Расположение:* `util/ssrf/ssrf.go:117`



---


[function] name: ipv4Net file: util/ssrf/ssrf.go:26 returns_error: нет description: —


### ipv4Net (util/ssrf/ssrf.go:26)


ipv4Net is a function that performs operations based on the provided parameters and returns (a, b, c, d byte, subnetPrefixLen int).


```go
func ipv4Net((a, b, c, d byte, subnetPrefixLen int)) (a, b, c, d byte, subnetPrefixLen int)
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


**Тип ответа:** d


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** subnetPrefixLen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/ssrf/ssrf.go:26`



---


[function] name: isIPv4Reserved file: util/ssrf/ssrf.go:60 returns_error: нет description: —


### isIPv4Reserved (util/ssrf/ssrf.go:60)


isIPv4Reserved is a function that performs operations based on the provided parameters and returns (address net.IP).


```go
func isIPv4Reserved((address net.IP)) (address net.IP)
```


**Тип ответа:** address


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IP


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/ssrf/ssrf.go:60`



---


[function] name: isIPv6GlobalUnicast file: util/ssrf/ssrf.go:56 returns_error: нет description: —


### isIPv6GlobalUnicast (util/ssrf/ssrf.go:56)


isIPv6GlobalUnicast is a function that performs operations based on the provided parameters and returns (address net.IP).


```go
func isIPv6GlobalUnicast((address net.IP)) (address net.IP)
```


**Тип ответа:** address


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IP


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `util/ssrf/ssrf.go:56`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](util_labels.md)

- [Следующая директория](util_svcutil.md)


---

