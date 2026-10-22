---
title: "Функции: pkg/serviceaccount"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/serviceaccount
---


# Функции: pkg/serviceaccount


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_securitycontext.md)

- [Следующая директория](pkg_util.md)


---


## Меню по файлам


- 📄 [pkg/serviceaccount/claims.go](#pkgserviceaccountclaimsgo)

- 📄 [pkg/serviceaccount/externaljwt/metrics/metrics.go](#pkgserviceaccountexternaljwtmetricsmetricsgo)

- 📄 [pkg/serviceaccount/externaljwt/plugin/keycache.go](#pkgserviceaccountexternaljwtpluginkeycachego)

- 📄 [pkg/serviceaccount/externaljwt/plugin/plugin.go](#pkgserviceaccountexternaljwtpluginplugingo)

- 📄 [pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go](#pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo)

- 📄 [pkg/serviceaccount/jwt.go](#pkgserviceaccountjwtgo)

- 📄 [pkg/serviceaccount/legacy.go](#pkgserviceaccountlegacygo)

- 📄 [pkg/serviceaccount/metrics.go](#pkgserviceaccountmetricsgo)

- 📄 [pkg/serviceaccount/openidmetadata.go](#pkgserviceaccountopenidmetadatago)


---


## pkg/serviceaccount/claims.go


📄 Исходный файл: `pkg/serviceaccount/claims.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Claims](#claims-pkgserviceaccountclaimsgo70) `:70`

- 🔗 [NewValidator](#newvalidator-pkgserviceaccountclaimsgo132) `:132`

- 🔗 [Validate](#validate-pkgserviceaccountclaimsgo144) `:144`


</details>


[function] name: Claims file: pkg/serviceaccount/claims.go:70 returns_error: да description: —


### Claims (pkg/serviceaccount/claims.go:70)


Claims is a function that performs operations based on the provided parameters and may return an error.


```go
func Claims((*jwt.Claims, interface{}, error)) (*jwt.Claims, interface{}, error)
```


**Тип запроса:** jwt.Claims


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/core/v1/fake/fake_persistentvolumeclaim.go`


**Тип ответа:** jwt.Claims


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/core/v1/fake/fake_persistentvolumeclaim.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*jwt.Claims`, `interface{}`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/claims.go:70`



---


[function] name: NewValidator file: pkg/serviceaccount/claims.go:132 returns_error: нет description: —


### NewValidator (pkg/serviceaccount/claims.go:132)


NewValidator is a function that performs operations based on the provided parameters and returns (getter ServiceAccountTokenGetter).


```go
func NewValidator((getter ServiceAccountTokenGetter)) (getter ServiceAccountTokenGetter)
```


**Тип ответа:** getter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ServiceAccountTokenGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/claims.go:132`



---


[function] name: Validate file: pkg/serviceaccount/claims.go:144 returns_error: да description: —


### Validate (pkg/serviceaccount/claims.go:144)


Validate is a method that performs operations based on the provided parameters and may return an error.


```go
func (v *validator) Validate((*apiserverserviceaccount.ServiceAccountInfo, error)) (*apiserverserviceaccount.ServiceAccountInfo, error)
```


**Тип запроса:** apiserverserviceaccount.ServiceAccountInfo


```json
{
  "Name": "string",
  "PodName": "string",
  "CredentialID": "string",
  "NodeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/serviceaccount/util.go`


**Тип ответа:** apiserverserviceaccount.ServiceAccountInfo


```json
{
  "Name": "string",
  "PodName": "string",
  "CredentialID": "string",
  "NodeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/serviceaccount/util.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apiserverserviceaccount.ServiceAccountInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/claims.go:144`




## pkg/serviceaccount/externaljwt/metrics/metrics.go


📄 Исходный файл: `pkg/serviceaccount/externaljwt/metrics/metrics.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [OuboundRequestMetricsInterceptor](#ouboundrequestmetricsinterceptor-pkgserviceaccountexternaljwtmetricsmetricsgo143) `:143`

- 🔗 [RecordFetchKeysAttempt](#recordfetchkeysattempt-pkgserviceaccountexternaljwtmetricsmetricsgo108) `:108`

- 🔗 [RecordKeyDataTimeStamp](#recordkeydatatimestamp-pkgserviceaccountexternaljwtmetricsmetricsgo119) `:119`

- 🔗 [RecordTokenGenAttempt](#recordtokengenattempt-pkgserviceaccountexternaljwtmetricsmetricsgo115) `:115`

- 🔗 [RegisterMetrics](#registermetrics-pkgserviceaccountexternaljwtmetricsmetricsgo98) `:98`

- 🔗 [getErrorCode](#geterrorcode-pkgserviceaccountexternaljwtmetricsmetricsgo127) `:127`


</details>


[function] name: OuboundRequestMetricsInterceptor file: pkg/serviceaccount/externaljwt/metrics/metrics.go:143 returns_error: нет description: —


### OuboundRequestMetricsInterceptor (pkg/serviceaccount/externaljwt/metrics/metrics.go:143)


OuboundRequestMetricsInterceptor is a function that performs operations based on the provided parameters and returns (ctx context.Context, method string, req, reply any, cc *grpc.ClientConn, invoker grpc.UnaryInvoker, opts ...grpc.CallOption).


```go
func OuboundRequestMetricsInterceptor((ctx context.Context, method string, req, reply any, cc *grpc.ClientConn, invoker grpc.UnaryInvoker, opts ...grpc.CallOption)) (ctx context.Context, method string, req, reply any, cc *grpc.ClientConn, invoker grpc.UnaryInvoker, opts ...grpc.CallOption)
```


**Тип запроса:** grpc.ClientConn


```json
{
  "Kubeconfig": "string",
  "AcceptContentTypes": "string",
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0
}
```


*Определено в:* `staging/src/k8s.io/component-base/config/v1alpha1/types.go`


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


**Тип ответа:** method


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** req


```json
{
  "RequestHeaders": {},
  "RequestVerb": "string",
  "RequestURL": "string",
  "ResponseStatus": "string",
  "ResponseHeaders": {},
  "ResponseErr": {},
  "muTrace": {},
  "DNSLookup": {},
  "Dialing": {},
  "GetConnection": {},
  "TLSHandshake": {},
  "ServerProcessing": {},
  "ConnectionReused": false,
  "Duration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/round_trippers.go`


**Тип ответа:** reply


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** any


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cc


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** grpc.ClientConn


```json
{
  "Kubeconfig": "string",
  "AcceptContentTypes": "string",
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0
}
```


*Определено в:* `staging/src/k8s.io/component-base/config/v1alpha1/types.go`


**Тип ответа:** invoker


```json
{
  "t": null,
  "admission": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/testing/helpers.go`


**Тип ответа:** grpc.UnaryInvoker


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** grpc.CallOption


```json
{
  "OnFinish": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-scheduler/framework/api_dispatcher.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/metrics/metrics.go:143`



---


[function] name: RecordFetchKeysAttempt file: pkg/serviceaccount/externaljwt/metrics/metrics.go:108 returns_error: да description: —


### RecordFetchKeysAttempt (pkg/serviceaccount/externaljwt/metrics/metrics.go:108)


RecordFetchKeysAttempt is a function that performs operations based on the provided parameters and may return an error.


```go
func RecordFetchKeysAttempt((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "msg": {},
  "cause": {},
  "stack": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/errors/errors.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/serviceaccount/externaljwt/metrics/metrics.go:108`



---


[function] name: RecordKeyDataTimeStamp file: pkg/serviceaccount/externaljwt/metrics/metrics.go:119 returns_error: нет description: —


### RecordKeyDataTimeStamp (pkg/serviceaccount/externaljwt/metrics/metrics.go:119)


RecordKeyDataTimeStamp is a function that performs operations based on the provided parameters and returns (timestamp float64).


```go
func RecordKeyDataTimeStamp((timestamp float64)) (timestamp float64)
```


**Тип ответа:** timestamp


```json
{
  "lastUpdatedAt": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/request/object_count_tracker.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/metrics/metrics.go:119`



---


[function] name: RecordTokenGenAttempt file: pkg/serviceaccount/externaljwt/metrics/metrics.go:115 returns_error: да description: —


### RecordTokenGenAttempt (pkg/serviceaccount/externaljwt/metrics/metrics.go:115)


RecordTokenGenAttempt is a function that performs operations based on the provided parameters and may return an error.


```go
func RecordTokenGenAttempt((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "msg": {},
  "cause": {},
  "stack": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/errors/errors.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/serviceaccount/externaljwt/metrics/metrics.go:115`



---


[function] name: RegisterMetrics file: pkg/serviceaccount/externaljwt/metrics/metrics.go:98 returns_error: нет description: —


### RegisterMetrics (pkg/serviceaccount/externaljwt/metrics/metrics.go:98)


RegisterMetrics is a function that performs operations based on the provided parameters and returns ().


```go
func RegisterMetrics(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/metrics/metrics.go:98`



---


[function] name: getErrorCode file: pkg/serviceaccount/externaljwt/metrics/metrics.go:127 returns_error: да description: —


### getErrorCode (pkg/serviceaccount/externaljwt/metrics/metrics.go:127)


getErrorCode is a function that performs operations based on the provided parameters and may return an error.


```go
func getErrorCode((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "msg": {},
  "cause": {},
  "stack": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/errors/errors.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/serviceaccount/externaljwt/metrics/metrics.go:127`




## pkg/serviceaccount/externaljwt/plugin/keycache.go


📄 Исходный файл: `pkg/serviceaccount/externaljwt/plugin/keycache.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [AddListener](#addlistener-pkgserviceaccountexternaljwtpluginkeycachego88) `:88`

- 🔗 [GetCacheAgeMaxSeconds](#getcacheagemaxseconds-pkgserviceaccountexternaljwtpluginkeycachego95) `:95`

- 🔗 [GetPublicKeys](#getpublickeys-pkgserviceaccountexternaljwtpluginkeycachego105) `:105`

- 🔗 [broadcastUpdate](#broadcastupdate-pkgserviceaccountexternaljwtpluginkeycachego193) `:193`

- 🔗 [findKeyForKeyID](#findkeyforkeyid-pkgserviceaccountexternaljwtpluginkeycachego127) `:127`

- 🔗 [getTokenVerificationKeys](#gettokenverificationkeys-pkgserviceaccountexternaljwtpluginkeycachego205) `:205`

- 🔗 [initialFill](#initialfill-pkgserviceaccountexternaljwtpluginkeycachego58) `:58`

- 🔗 [keysChanged](#keyschanged-pkgserviceaccountexternaljwtpluginkeycachego171) `:171`

- 🔗 [newKeyCache](#newkeycache-pkgserviceaccountexternaljwtpluginkeycachego48) `:48`

- 🔗 [scheduleSync](#schedulesync-pkgserviceaccountexternaljwtpluginkeycachego65) `:65`

- 🔗 [syncKeys](#synckeys-pkgserviceaccountexternaljwtpluginkeycachego149) `:149`


</details>


[function] name: AddListener file: pkg/serviceaccount/externaljwt/plugin/keycache.go:88 returns_error: нет description: —


### AddListener (pkg/serviceaccount/externaljwt/plugin/keycache.go:88)


AddListener is a method that creates new data based on the provided parameters and returns (listener serviceaccount.Listener).


```go
func (p *keyCache) AddListener((listener serviceaccount.Listener)) (listener serviceaccount.Listener)
```


**Тип ответа:** listener


```json
{
  "addr": {},
  "ctx": {},
  "cancel": {},
  "mutex": {},
  "connections": {}
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


**Тип ответа:** serviceaccount.Listener


```json
{
  "logger": {},
  "nextCh": {},
  "addCh": {},
  "done": {},
  "handler": {},
  "syncTracker": null,
  "upstreamHasSynced": {},
  "pendingNotifications": {},
  "requestedResyncPeriod": {},
  "resyncPeriod": {},
  "nextResync": {},
  "resyncLock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/shared_informer.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:88`



---


[function] name: GetCacheAgeMaxSeconds file: pkg/serviceaccount/externaljwt/plugin/keycache.go:95 returns_error: нет description: —


### GetCacheAgeMaxSeconds (pkg/serviceaccount/externaljwt/plugin/keycache.go:95)


GetCacheAgeMaxSeconds is a method that retrieves data based on the provided parameters and returns ().


```go
func (p *keyCache) GetCacheAgeMaxSeconds(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:95`



---


[function] name: GetPublicKeys file: pkg/serviceaccount/externaljwt/plugin/keycache.go:105 returns_error: нет description: GetPublicKeys returns the public key corresponding to requested keyID.
Getter is expected to return All keys for keyID "


### GetPublicKeys (pkg/serviceaccount/externaljwt/plugin/keycache.go:105)


GetPublicKeys returns the public key corresponding to requested keyID.
Getter is expected to return All keys for keyID ""


```go
func (p *keyCache) GetPublicKeys((ctx context.Context, keyID string)) (ctx context.Context, keyID string)
```


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


**Тип ответа:** keyID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:105`



---


[function] name: broadcastUpdate file: pkg/serviceaccount/externaljwt/plugin/keycache.go:193 returns_error: нет description: —


### broadcastUpdate (pkg/serviceaccount/externaljwt/plugin/keycache.go:193)


broadcastUpdate is a method that performs operations based on the provided parameters and returns ().


```go
func (p *keyCache) broadcastUpdate(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:193`



---


[function] name: findKeyForKeyID file: pkg/serviceaccount/externaljwt/plugin/keycache.go:127 returns_error: нет description: —


### findKeyForKeyID (pkg/serviceaccount/externaljwt/plugin/keycache.go:127)


findKeyForKeyID is a method that performs operations based on the provided parameters and returns ([]serviceaccount.PublicKey, bool).


```go
func (p *keyCache) findKeyForKeyID(([]serviceaccount.PublicKey, bool)) ([]serviceaccount.PublicKey, bool)
```


**Тип ответа:** serviceaccount.PublicKey


```json
{
  "KeyID": "string",
  "PublicKey": {},
  "ExcludeFromOIDCDiscovery": false
}
```


*Определено в:* `pkg/serviceaccount/jwt.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:127`



---


[function] name: getTokenVerificationKeys file: pkg/serviceaccount/externaljwt/plugin/keycache.go:205 returns_error: да description: GetTokenVerificationKeys returns a map of supported external keyIDs to keys
the keys are PKIX-serialized. It calls exter


### getTokenVerificationKeys (pkg/serviceaccount/externaljwt/plugin/keycache.go:205)


GetTokenVerificationKeys returns a map of supported external keyIDs to keys
the keys are PKIX-serialized. It calls external-jwt-signer with a timeout of keySyncTimeoutSec.


```go
func (p *keyCache) getTokenVerificationKeys((*VerificationKeys, error)) (*VerificationKeys, error)
```


**Тип запроса:** VerificationKeys


```json
{
  "Keys": [],
  "DataTimestamp": {},
  "NextRefreshHint": {}
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Тип ответа:** VerificationKeys


```json
{
  "Keys": [],
  "DataTimestamp": {},
  "NextRefreshHint": {}
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VerificationKeys`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:205`



---


[function] name: initialFill file: pkg/serviceaccount/externaljwt/plugin/keycache.go:58 returns_error: нет description: InitialFill can be used to perform an initial fetch for keys get the
refresh interval as recommended by external signer.


### initialFill (pkg/serviceaccount/externaljwt/plugin/keycache.go:58)


InitialFill can be used to perform an initial fetch for keys get the
refresh interval as recommended by external signer.


```go
func (p *keyCache) initialFill((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:58`



---


[function] name: keysChanged file: pkg/serviceaccount/externaljwt/plugin/keycache.go:171 returns_error: нет description: keysChanged returns true if the data timestamp, key count, order of key ids or excludeFromOIDCDiscovery indicators


### keysChanged (pkg/serviceaccount/externaljwt/plugin/keycache.go:171)


keysChanged returns true if the data timestamp, key count, order of key ids or excludeFromOIDCDiscovery indicators


```go
func keysChanged((oldPublicKeys, newPublicKeys *VerificationKeys)) (oldPublicKeys, newPublicKeys *VerificationKeys)
```


**Тип запроса:** VerificationKeys


```json
{
  "Keys": [],
  "DataTimestamp": {},
  "NextRefreshHint": {}
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Тип ответа:** oldPublicKeys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newPublicKeys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** VerificationKeys


```json
{
  "Keys": [],
  "DataTimestamp": {},
  "NextRefreshHint": {}
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:171`



---


[function] name: newKeyCache file: pkg/serviceaccount/externaljwt/plugin/keycache.go:48 returns_error: нет description: newKeyCache constructs an implementation of KeyCache.


### newKeyCache (pkg/serviceaccount/externaljwt/plugin/keycache.go:48)


newKeyCache constructs an implementation of KeyCache.


```go
func newKeyCache((client externaljwtv1.ExternalJWTSignerClient)) (client externaljwtv1.ExternalJWTSignerClient)
```


**Тип ответа:** client


```json
{
  "mutex": {},
  "resource": "string",
  "socket": "string",
  "grpc": null,
  "handler": {},
  "client": {}
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/plugin/v1beta1/client.go`


**Тип ответа:** externaljwtv1.ExternalJWTSignerClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:48`



---


[function] name: scheduleSync file: pkg/serviceaccount/externaljwt/plugin/keycache.go:65 returns_error: нет description: —


### scheduleSync (pkg/serviceaccount/externaljwt/plugin/keycache.go:65)


scheduleSync is a method that performs operations based on the provided parameters and returns (ctx context.Context, keySyncTimeout time.Duration).


```go
func (p *keyCache) scheduleSync((ctx context.Context, keySyncTimeout time.Duration)) (ctx context.Context, keySyncTimeout time.Duration)
```


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


**Тип ответа:** keySyncTimeout


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** time.Duration


```json
{
  "Name": "string",
  "Webhooks": [],
  "InitContext": false,
  "IsDryRun": false,
  "ExpectedDurationSum": {},
  "ExpectedDurationMax": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:65`



---


[function] name: syncKeys file: pkg/serviceaccount/externaljwt/plugin/keycache.go:149 returns_error: нет description: sync supported external keys.
completely re-writes the set of supported keys.


### syncKeys (pkg/serviceaccount/externaljwt/plugin/keycache.go:149)


sync supported external keys.
completely re-writes the set of supported keys.


```go
func (p *keyCache) syncKeys((ctx context.Context)) (ctx context.Context)
```


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/keycache.go:149`




## pkg/serviceaccount/externaljwt/plugin/plugin.go


📄 Исходный файл: `pkg/serviceaccount/externaljwt/plugin/plugin.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [GenerateToken](#generatetoken-pkgserviceaccountexternaljwtpluginplugingo107) `:107`

- 🔗 [GetServiceMetadata](#getservicemetadata-pkgserviceaccountexternaljwtpluginplugingo143) `:143`

- 🔗 [New](#new-pkgserviceaccountexternaljwtpluginplugingo52) `:52`

- 🔗 [Options](#options-pkgserviceaccountexternaljwtpluginplugingo218) `:218`

- 🔗 [Sign](#sign-pkgserviceaccountexternaljwtpluginplugingo213) `:213`

- 🔗 [init](#init-pkgserviceaccountexternaljwtpluginplugingo38) `:38`

- 🔗 [mergeClaims](#mergeclaims-pkgserviceaccountexternaljwtpluginplugingo199) `:199`

- 🔗 [newPlugin](#newplugin-pkgserviceaccountexternaljwtpluginplugingo94) `:94`

- 🔗 [signAndAssembleJWT](#signandassemblejwt-pkgserviceaccountexternaljwtpluginplugingo113) `:113`

- 🔗 [validateJWTHeader](#validatejwtheader-pkgserviceaccountexternaljwtpluginplugingo148) `:148`


</details>


[function] name: GenerateToken file: pkg/serviceaccount/externaljwt/plugin/plugin.go:107 returns_error: да description: GenerateToken creates a service account token with the provided claims by
calling out to the external signer binary.


### GenerateToken (pkg/serviceaccount/externaljwt/plugin/plugin.go:107)


GenerateToken creates a service account token with the provided claims by
calling out to the external signer binary.


```go
func (p *Plugin) GenerateToken((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:107`



---


[function] name: GetServiceMetadata file: pkg/serviceaccount/externaljwt/plugin/plugin.go:143 returns_error: да description: GetServiceMetadata returns metadata associated with externalJWTSigner
It Includes details like max token lifetime suppor


### GetServiceMetadata (pkg/serviceaccount/externaljwt/plugin/plugin.go:143)


GetServiceMetadata returns metadata associated with externalJWTSigner
It Includes details like max token lifetime supported by externalJWTSigner, etc.


```go
func (p *Plugin) GetServiceMetadata((*externaljwtv1.MetadataResponse, error)) (*externaljwtv1.MetadataResponse, error)
```


**Тип запроса:** externaljwtv1.MetadataResponse


```json
{
  "state": {},
  "maxTokenExpirationSeconds": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Тип ответа:** externaljwtv1.MetadataResponse


```json
{
  "state": {},
  "maxTokenExpirationSeconds": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*externaljwtv1.MetadataResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:143`



---


[function] name: New file: pkg/serviceaccount/externaljwt/plugin/plugin.go:52 returns_error: да description: New calls external signer to fill out supported keys.
It also starts a periodic sync of external keys.
In order for the 


### New (pkg/serviceaccount/externaljwt/plugin/plugin.go:52)


New calls external signer to fill out supported keys.
It also starts a periodic sync of external keys.
In order for the key cache and external signing to work correctly, pass a context that will live as
long as the dependent process; is used to maintain the lifetime of the connection to external signer.


```go
func New((*Plugin, *keyCache, error)) (*Plugin, *keyCache, error)
```


**Тип запроса:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Тип запроса:** keyCache


```json
{
  "client": {},
  "syncGroup": {},
  "listenersLock": {},
  "listeners": [],
  "verificationKeys": {}
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/keycache.go`


**Тип ответа:** Plugin


```json
{
  "iss": "string",
  "client": {},
  "keyCache": null,
  "allowSigningWithNonOIDCKeys": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/plugin.go`


**Тип ответа:** keyCache


```json
{
  "client": {},
  "syncGroup": {},
  "listenersLock": {},
  "listeners": [],
  "verificationKeys": {}
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/keycache.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Plugin`, `*keyCache`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:52`



---


[function] name: Options file: pkg/serviceaccount/externaljwt/plugin/plugin.go:218 returns_error: нет description: —


### Options (pkg/serviceaccount/externaljwt/plugin/plugin.go:218)


Options is a method that performs operations based on the provided parameters and returns ().


```go
func (p payloadGrabber) Options(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:218`



---


[function] name: Sign file: pkg/serviceaccount/externaljwt/plugin/plugin.go:213 returns_error: да description: —


### Sign (pkg/serviceaccount/externaljwt/plugin/plugin.go:213)


Sign is a method that performs operations based on the provided parameters and may return an error.


```go
func (p payloadGrabber) Sign((*jose.JSONWebSignature, error)) (*jose.JSONWebSignature, error)
```


**Тип запроса:** jose.JSONWebSignature


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** jose.JSONWebSignature


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*jose.JSONWebSignature`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:213`



---


[function] name: init file: pkg/serviceaccount/externaljwt/plugin/plugin.go:38 returns_error: нет description: —


### init (pkg/serviceaccount/externaljwt/plugin/plugin.go:38)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:38`



---


[function] name: mergeClaims file: pkg/serviceaccount/externaljwt/plugin/plugin.go:199 returns_error: да description: —


### mergeClaims (pkg/serviceaccount/externaljwt/plugin/plugin.go:199)


mergeClaims is a function that performs operations based on the provided parameters and may return an error.


```go
func mergeClaims(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:199`



---


[function] name: newPlugin file: pkg/serviceaccount/externaljwt/plugin/plugin.go:94 returns_error: нет description: newPlugin constructs an implementation of external JWT signer plugin.


### newPlugin (pkg/serviceaccount/externaljwt/plugin/plugin.go:94)


newPlugin constructs an implementation of external JWT signer plugin.


```go
func newPlugin((iss string, conn *grpc.ClientConn, allowSigningWithNonOIDCKeys bool)) (iss string, conn *grpc.ClientConn, allowSigningWithNonOIDCKeys bool)
```


**Тип запроса:** grpc.ClientConn


```json
{
  "Kubeconfig": "string",
  "AcceptContentTypes": "string",
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0
}
```


*Определено в:* `staging/src/k8s.io/component-base/config/v1alpha1/types.go`


**Тип ответа:** iss


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/admissionregistration/v1alpha1/validatingadmissionpolicybinding.go`


**Тип ответа:** conn


```json
{
  "conn": {},
  "stdinStream": {},
  "stdoutStream": {},
  "stderrStream": {},
  "writeStatus": {},
  "resizeStream": {},
  "resizeChan": {},
  "tty": false
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/cri/streaming/remotecommand/httpstream.go`


**Тип ответа:** grpc.ClientConn


```json
{
  "Kubeconfig": "string",
  "AcceptContentTypes": "string",
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0
}
```


*Определено в:* `staging/src/k8s.io/component-base/config/v1alpha1/types.go`


**Тип ответа:** allowSigningWithNonOIDCKeys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:94`



---


[function] name: signAndAssembleJWT file: pkg/serviceaccount/externaljwt/plugin/plugin.go:113 returns_error: да description: —


### signAndAssembleJWT (pkg/serviceaccount/externaljwt/plugin/plugin.go:113)


signAndAssembleJWT is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *Plugin) signAndAssembleJWT((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:113`



---


[function] name: validateJWTHeader file: pkg/serviceaccount/externaljwt/plugin/plugin.go:148 returns_error: нет description: —


### validateJWTHeader (pkg/serviceaccount/externaljwt/plugin/plugin.go:148)


validateJWTHeader is a method that performs operations based on the provided parameters and returns (ctx context.Context, response *externaljwtv1.SignJWTResponse).


```go
func (p *Plugin) validateJWTHeader((ctx context.Context, response *externaljwtv1.SignJWTResponse)) (ctx context.Context, response *externaljwtv1.SignJWTResponse)
```


**Тип запроса:** externaljwtv1.SignJWTResponse


```json
{
  "state": {},
  "Header": "string",
  "Signature": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


**Тип ответа:** response


```json
{
  "podName": "string",
  "response": "string"
}
```


*Определено в:* `test/e2e/framework/pod/wait.go`


**Тип ответа:** externaljwtv1.SignJWTResponse


```json
{
  "state": {},
  "Header": "string",
  "Signature": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/plugin.go:148`




## pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go


📄 Исходный файл: `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [CleanUp](#cleanup-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo270) `:270`

- 🔗 [FetchKeys](#fetchkeys-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo146) `:146`

- 🔗 [GetSupportedKeys](#getsupportedkeys-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo98) `:98`

- 🔗 [Metadata](#metadata-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo174) `:174`

- 🔗 [NewMockSigner](#newmocksigner-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo71) `:71`

- 🔗 [Reset](#reset-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo186) `:186`

- 🔗 [SetSupportedKeys](#setsupportedkeys-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo103) `:103`

- 🔗 [Sign](#sign-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo114) `:114`

- 🔗 [WaitForSupportedKeysFetch](#waitforsupportedkeysfetch-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo108) `:108`

- 🔗 [generateKeyPair](#generatekeypair-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo276) `:276`

- 🔗 [hashBytes](#hashbytes-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo294) `:294`

- 🔗 [start](#start-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo222) `:222`

- 🔗 [waitForMockServerToStart](#waitformockservertostart-pkgserviceaccountexternaljwtplugintestingv1externalsigner_mockgo243) `:243`


</details>


[function] name: CleanUp file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:270 returns_error: нет description: CleanUp stops gRPC server and the underlying listener.


### CleanUp (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:270)


CleanUp stops gRPC server and the underlying listener.


```go
func (m *MockSigner) CleanUp(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:270`



---


[function] name: FetchKeys file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:146 returns_error: да description: —


### FetchKeys (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:146)


FetchKeys is a method that retrieves data based on the provided parameters and may return an error.


```go
func (m *MockSigner) FetchKeys((*v1.FetchKeysResponse, error)) (*v1.FetchKeysResponse, error)
```


**Тип запроса:** v1.FetchKeysResponse


```json
{
  "state": {},
  "Keys": [],
  "dataTimestamp": null,
  "refreshHintSeconds": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Тип ответа:** v1.FetchKeysResponse


```json
{
  "state": {},
  "Keys": [],
  "dataTimestamp": null,
  "refreshHintSeconds": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.FetchKeysResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:146`



---


[function] name: GetSupportedKeys file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:98 returns_error: нет description: —


### GetSupportedKeys (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:98)


GetSupportedKeys is a method that retrieves data based on the provided parameters and returns ().


```go
func (m *MockSigner) GetSupportedKeys(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:98`



---


[function] name: Metadata file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:174 returns_error: да description: —


### Metadata (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:174)


Metadata is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *MockSigner) Metadata((*v1.MetadataResponse, error)) (*v1.MetadataResponse, error)
```


**Тип запроса:** v1.MetadataResponse


```json
{
  "state": {},
  "maxTokenExpirationSeconds": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Тип ответа:** v1.MetadataResponse


```json
{
  "state": {},
  "maxTokenExpirationSeconds": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.MetadataResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:174`



---


[function] name: NewMockSigner file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:71 returns_error: нет description: NewMockSigner starts and returns a new MockSigner
It servers on the provided socket.


### NewMockSigner (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:71)


NewMockSigner starts and returns a new MockSigner
It servers on the provided socket.


```go
func NewMockSigner((t *testing.T, socketPath string)) (t *testing.T, socketPath string)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** t


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** socketPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:71`



---


[function] name: Reset file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:186 returns_error: нет description: Reset genrate and adds signing/supported keys to MockSigner instance.


### Reset (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:186)


Reset genrate and adds signing/supported keys to MockSigner instance.


```go
func (m *MockSigner) Reset(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:186`



---


[function] name: SetSupportedKeys file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:103 returns_error: нет description: —


### SetSupportedKeys (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:103)


SetSupportedKeys is a method that updates data based on the provided parameters and returns (keys map[string]KeyT).


```go
func (m *MockSigner) SetSupportedKeys((keys map[string]KeyT)) (keys map[string]KeyT)
```


**Тип ответа:** keys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** KeyT


```json
{
  "Key": [],
  "ExcludeFromOidcDiscovery": false
}
```


*Определено в:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:103`



---


[function] name: Sign file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:114 returns_error: да description: —


### Sign (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:114)


Sign is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *MockSigner) Sign((*v1.SignJWTResponse, error)) (*v1.SignJWTResponse, error)
```


**Тип запроса:** v1.SignJWTResponse


```json
{
  "state": {},
  "Header": "string",
  "Signature": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Тип ответа:** v1.SignJWTResponse


```json
{
  "state": {},
  "Header": "string",
  "Signature": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/externaljwt/apis/v1alpha1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*v1.SignJWTResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:114`



---


[function] name: WaitForSupportedKeysFetch file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:108 returns_error: нет description: —


### WaitForSupportedKeysFetch (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:108)


WaitForSupportedKeysFetch is a method that performs operations based on the provided parameters and returns ().


```go
func (m *MockSigner) WaitForSupportedKeysFetch(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:108`



---


[function] name: generateKeyPair file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:276 returns_error: да description: —


### generateKeyPair (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:276)


generateKeyPair is a function that performs operations based on the provided parameters and may return an error.


```go
func generateKeyPair((*rsa.PrivateKey, []byte, error)) (*rsa.PrivateKey, []byte, error)
```


**Тип запроса:** rsa.PrivateKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rsa.PrivateKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*rsa.PrivateKey`, `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:276`



---


[function] name: hashBytes file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:294 returns_error: нет description: —


### hashBytes (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:294)


hashBytes is a function that performs operations based on the provided parameters and returns (bytes []byte).


```go
func hashBytes((bytes []byte)) (bytes []byte)
```


**Тип ответа:** bytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:294`



---


[function] name: start file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:222 returns_error: нет description: start makes the gRpc MockServer listen on unix socket.


### start (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:222)


start makes the gRpc MockServer listen on unix socket.


```go
func (m *MockSigner) start((t *testing.T)) (t *testing.T)
```


**Тип запроса:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


**Тип ответа:** t


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** testing.T


```json
{
  "TypeMeta": 0,
  "S": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/doc.go`


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:222`



---


[function] name: waitForMockServerToStart file: pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:243 returns_error: нет description: waitForMockServerToStart waits until Mock signer is ready to server.
waits for a max of 30s before failing.


### waitForMockServerToStart (pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:243)


waitForMockServerToStart waits until Mock signer is ready to server.
waits for a max of 30s before failing.


```go
func (m *MockSigner) waitForMockServerToStart(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/externaljwt/plugin/testing/v1/externalsigner_mock.go:243`




## pkg/serviceaccount/jwt.go


📄 Исходный файл: `pkg/serviceaccount/jwt.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [AddListener](#addlistener-pkgserviceaccountjwtgo300) `:300`

- 🔗 [AuthenticateToken](#authenticatetoken-pkgserviceaccountjwtgo334) `:334`

- 🔗 [GenerateToken](#generatetoken-pkgserviceaccountjwtgo220) `:220`

- 🔗 [GenerateToken](#generatetoken-pkgserviceaccountjwtgo443) `:443`

- 🔗 [GetCacheAgeMaxSeconds](#getcacheagemaxseconds-pkgserviceaccountjwtgo304) `:304`

- 🔗 [GetPublicKeys](#getpublickeys-pkgserviceaccountjwtgo309) `:309`

- 🔗 [JWTTokenAuthenticator](#jwttokenauthenticator-pkgserviceaccountjwtgo227) `:227`

- 🔗 [JWTTokenGenerator](#jwttokengenerator-pkgserviceaccountjwtgo61) `:61`

- 🔗 [StaticPublicKeysGetter](#staticpublickeysgetter-pkgserviceaccountjwtgo277) `:277`

- 🔗 [hasCorrectIssuer](#hascorrectissuer-pkgserviceaccountjwtgo420) `:420`

- 🔗 [keyIDFromPublicKey](#keyidfrompublickey-pkgserviceaccountjwtgo99) `:99`

- 🔗 [signerFromECDSAPrivateKey](#signerfromecdsaprivatekey-pkgserviceaccountjwtgo148) `:148`

- 🔗 [signerFromOpaqueSigner](#signerfromopaquesigner-pkgserviceaccountjwtgo193) `:193`

- 🔗 [signerFromRSAPrivateKey](#signerfromrsaprivatekey-pkgserviceaccountjwtgo114) `:114`


</details>


[function] name: AddListener file: pkg/serviceaccount/jwt.go:300 returns_error: нет description: —


### AddListener (pkg/serviceaccount/jwt.go:300)


AddListener is a method that creates new data based on the provided parameters and returns (listener Listener).


```go
func (s staticPublicKeysGetter) AddListener((listener Listener)) (listener Listener)
```


**Тип ответа:** listener


```json
{
  "addr": {},
  "ctx": {},
  "cancel": {},
  "mutex": {},
  "connections": {}
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


**Тип ответа:** Listener


```json
{
  "logger": {},
  "nextCh": {},
  "addCh": {},
  "done": {},
  "handler": {},
  "syncTracker": null,
  "upstreamHasSynced": {},
  "pendingNotifications": {},
  "requestedResyncPeriod": {},
  "resyncPeriod": {},
  "nextResync": {},
  "resyncLock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/shared_informer.go`


📍 *Расположение:* `pkg/serviceaccount/jwt.go:300`



---


[function] name: AuthenticateToken file: pkg/serviceaccount/jwt.go:334 returns_error: да description: —


### AuthenticateToken (pkg/serviceaccount/jwt.go:334)


AuthenticateToken is a method that performs operations based on the provided parameters and may return an error.


```go
func (j *jwtTokenAuthenticator[PrivateClaims]) AuthenticateToken((*authenticator.Response, bool, error)) (*authenticator.Response, bool, error)
```


**Тип запроса:** authenticator.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Тип ответа:** authenticator.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*authenticator.Response`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:334`



---


[function] name: GenerateToken file: pkg/serviceaccount/jwt.go:220 returns_error: да description: —


### GenerateToken (pkg/serviceaccount/jwt.go:220)


GenerateToken is a method that performs operations based on the provided parameters and may return an error.


```go
func (j *jwtTokenGenerator) GenerateToken((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:220`



---


[function] name: GenerateToken file: pkg/serviceaccount/jwt.go:443 returns_error: да description: GenerateToken is shared between internal and external signer code to ensure that claim merging logic remains consistent 


### GenerateToken (pkg/serviceaccount/jwt.go:443)


GenerateToken is shared between internal and external signer code to ensure that claim merging logic remains consistent between them.


```go
func GenerateToken((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:443`



---


[function] name: GetCacheAgeMaxSeconds file: pkg/serviceaccount/jwt.go:304 returns_error: нет description: —


### GetCacheAgeMaxSeconds (pkg/serviceaccount/jwt.go:304)


GetCacheAgeMaxSeconds is a method that retrieves data based on the provided parameters and returns ().


```go
func (s staticPublicKeysGetter) GetCacheAgeMaxSeconds(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/jwt.go:304`



---


[function] name: GetPublicKeys file: pkg/serviceaccount/jwt.go:309 returns_error: нет description: —


### GetPublicKeys (pkg/serviceaccount/jwt.go:309)


GetPublicKeys is a method that retrieves data based on the provided parameters and returns (ctx context.Context, keyID string).


```go
func (s staticPublicKeysGetter) GetPublicKeys((ctx context.Context, keyID string)) (ctx context.Context, keyID string)
```


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


**Тип ответа:** keyID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/jwt.go:309`



---


[function] name: JWTTokenAuthenticator file: pkg/serviceaccount/jwt.go:227 returns_error: нет description: JWTTokenAuthenticator authenticates tokens as JWT tokens produced by JWTTokenGenerator
Token signatures are verified usi


### JWTTokenAuthenticator (pkg/serviceaccount/jwt.go:227)


JWTTokenAuthenticator authenticates tokens as JWT tokens produced by JWTTokenGenerator
Token signatures are verified using each of the given public keys until one works (allowing key rotation)
If lookup is true, the service account and secret referenced as claims inside the token are retrieved and verified with the provided ServiceAccountTokenGetter


```go
func JWTTokenAuthenticator((issuers []string, publicKeysGetter PublicKeysGetter, implicitAuds authenticator.Audiences, validator Validator[PrivateClaims])) (issuers []string, publicKeysGetter PublicKeysGetter, implicitAuds authenticator.Audiences, validator Validator[PrivateClaims])
```


**Тип ответа:** issuers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** publicKeysGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PublicKeysGetter


```json
{
  "allPublicKeys": [],
  "publicKeysByID": {}
}
```


*Определено в:* `pkg/serviceaccount/jwt.go`


**Тип ответа:** implicitAuds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** authenticator.Audiences


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** validator


```json
{
  "getter": {}
}
```


*Определено в:* `pkg/serviceaccount/claims.go`


**Тип ответа:** Validator


```json
{
  "Items": null,
  "Properties": {},
  "AllOfValidators": [],
  "AdditionalProperties": null,
  "Schema": null,
  "uncompiledRules": [],
  "compiledRules": [],
  "compilationErr": {},
  "isResourceRoot": false,
  "celActivationFactory": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/validation.go`


**Тип ответа:** PrivateClaims


```json
{
  "ServiceAccountName": "string",
  "ServiceAccountUID": "string",
  "SecretName": "string",
  "Namespace": "string"
}
```


*Определено в:* `pkg/serviceaccount/legacy.go`


📍 *Расположение:* `pkg/serviceaccount/jwt.go:227`



---


[function] name: JWTTokenGenerator file: pkg/serviceaccount/jwt.go:61 returns_error: да description: JWTTokenGenerator returns a TokenGenerator that generates signed JWT tokens, using the given privateKey.
privateKey is a


### JWTTokenGenerator (pkg/serviceaccount/jwt.go:61)


JWTTokenGenerator returns a TokenGenerator that generates signed JWT tokens, using the given privateKey.
privateKey is a PEM-encoded byte array of a private RSA key.


```go
func JWTTokenGenerator((TokenGenerator, error)) (TokenGenerator, error)
```


**Тип ответа:** TokenGenerator


```json
{
  "iss": "string",
  "signer": {}
}
```


*Определено в:* `pkg/serviceaccount/jwt.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `TokenGenerator`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:61`



---


[function] name: StaticPublicKeysGetter file: pkg/serviceaccount/jwt.go:277 returns_error: да description: StaticPublicKeysGetter constructs an implementation of PublicKeysGetter
which returns all public keys when key id is uns


### StaticPublicKeysGetter (pkg/serviceaccount/jwt.go:277)


StaticPublicKeysGetter constructs an implementation of PublicKeysGetter
which returns all public keys when key id is unspecified, and returns
the public keys matching the keyIDFromPublicKey-derived key id when
a key id is specified.


```go
func StaticPublicKeysGetter((PublicKeysGetter, error)) (PublicKeysGetter, error)
```


**Тип ответа:** PublicKeysGetter


```json
{
  "allPublicKeys": [],
  "publicKeysByID": {}
}
```


*Определено в:* `pkg/serviceaccount/jwt.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `PublicKeysGetter`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:277`



---


[function] name: hasCorrectIssuer file: pkg/serviceaccount/jwt.go:420 returns_error: нет description: hasCorrectIssuer returns true if tokenData is a valid JWT in compact
serialization format and the "iss" claim matches th


### hasCorrectIssuer (pkg/serviceaccount/jwt.go:420)


hasCorrectIssuer returns true if tokenData is a valid JWT in compact
serialization format and the "iss" claim matches the iss field of this token
authenticator, and otherwise returns false.

Note: go-jose currently does not allow access to unverified JWS payloads.
See https://github.com/square/go-jose/issues/169


```go
func (j *jwtTokenAuthenticator[PrivateClaims]) hasCorrectIssuer((tokenData string)) (tokenData string)
```


**Тип ответа:** tokenData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/jwt.go:420`



---


[function] name: keyIDFromPublicKey file: pkg/serviceaccount/jwt.go:99 returns_error: да description: keyIDFromPublicKey derives a key ID non-reversibly from a public key.

The Key ID is field on a given on JWTs and JWKs t


### keyIDFromPublicKey (pkg/serviceaccount/jwt.go:99)


keyIDFromPublicKey derives a key ID non-reversibly from a public key.

The Key ID is field on a given on JWTs and JWKs that help relying parties
pick the correct key for verification when the identity party advertises
multiple keys.

Making the derivation non-reversible makes it impossible for someone to
accidentally obtain the real key from the key ID and use it for token
validation.


```go
func keyIDFromPublicKey((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:99`



---


[function] name: signerFromECDSAPrivateKey file: pkg/serviceaccount/jwt.go:148 returns_error: да description: —


### signerFromECDSAPrivateKey (pkg/serviceaccount/jwt.go:148)


signerFromECDSAPrivateKey is a function that performs operations based on the provided parameters and may return an error.


```go
func signerFromECDSAPrivateKey((jose.Signer, error)) (jose.Signer, error)
```


**Тип ответа:** jose.Signer


```json
{
  "client": {},
  "configMapKey": "string",
  "configMapName": "string",
  "configMapNamespace": "string",
  "secretNamespace": "string",
  "syncQueue": {},
  "secretLister": {},
  "secretSynced": {},
  "configMapLister": {},
  "configMapSynced": {}
}
```


*Определено в:* `pkg/controller/bootstrap/bootstrapsigner.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `jose.Signer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:148`



---


[function] name: signerFromOpaqueSigner file: pkg/serviceaccount/jwt.go:193 returns_error: да description: —


### signerFromOpaqueSigner (pkg/serviceaccount/jwt.go:193)


signerFromOpaqueSigner is a function that performs operations based on the provided parameters and may return an error.


```go
func signerFromOpaqueSigner((jose.Signer, error)) (jose.Signer, error)
```


**Тип ответа:** jose.Signer


```json
{
  "client": {},
  "configMapKey": "string",
  "configMapName": "string",
  "configMapNamespace": "string",
  "secretNamespace": "string",
  "syncQueue": {},
  "secretLister": {},
  "secretSynced": {},
  "configMapLister": {},
  "configMapSynced": {}
}
```


*Определено в:* `pkg/controller/bootstrap/bootstrapsigner.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `jose.Signer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:193`



---


[function] name: signerFromRSAPrivateKey file: pkg/serviceaccount/jwt.go:114 returns_error: да description: —


### signerFromRSAPrivateKey (pkg/serviceaccount/jwt.go:114)


signerFromRSAPrivateKey is a function that performs operations based on the provided parameters and may return an error.


```go
func signerFromRSAPrivateKey((jose.Signer, error)) (jose.Signer, error)
```


**Тип ответа:** jose.Signer


```json
{
  "client": {},
  "configMapKey": "string",
  "configMapName": "string",
  "configMapNamespace": "string",
  "secretNamespace": "string",
  "syncQueue": {},
  "secretLister": {},
  "secretSynced": {},
  "configMapLister": {},
  "configMapSynced": {}
}
```


*Определено в:* `pkg/controller/bootstrap/bootstrapsigner.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `jose.Signer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/jwt.go:114`




## pkg/serviceaccount/legacy.go


📄 Исходный файл: `pkg/serviceaccount/legacy.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [LegacyClaims](#legacyclaims-pkgserviceaccountlegacygo42) `:42`

- 🔗 [NewLegacyValidator](#newlegacyvalidator-pkgserviceaccountlegacygo65) `:65`

- 🔗 [Validate](#validate-pkgserviceaccountlegacygo87) `:87`

- 🔗 [patchSecretWithLastUsedDate](#patchsecretwithlastuseddate-pkgserviceaccountlegacygo183) `:183`


</details>


[function] name: LegacyClaims file: pkg/serviceaccount/legacy.go:42 returns_error: нет description: —


### LegacyClaims (pkg/serviceaccount/legacy.go:42)


LegacyClaims is a function that performs operations based on the provided parameters and returns (*jwt.Claims, interface{}).


```go
func LegacyClaims((*jwt.Claims, interface{})) (*jwt.Claims, interface{})
```


**Тип запроса:** jwt.Claims


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/core/v1/fake/fake_persistentvolumeclaim.go`


**Тип ответа:** jwt.Claims


```json
{
  "Fake": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/kubernetes/typed/core/v1/fake/fake_persistentvolumeclaim.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/serviceaccount/legacy.go:42`



---


[function] name: NewLegacyValidator file: pkg/serviceaccount/legacy.go:65 returns_error: да description: —


### NewLegacyValidator (pkg/serviceaccount/legacy.go:65)


NewLegacyValidator is a function that performs operations based on the provided parameters and may return an error.


```go
func NewLegacyValidator((Validator[legacyPrivateClaims], error)) (Validator[legacyPrivateClaims], error)
```


**Тип ответа:** Validator


```json
{
  "Items": null,
  "Properties": {},
  "AllOfValidators": [],
  "AdditionalProperties": null,
  "Schema": null,
  "uncompiledRules": [],
  "compiledRules": [],
  "compilationErr": {},
  "isResourceRoot": false,
  "celActivationFactory": {}
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/validation.go`


**Тип ответа:** legacyPrivateClaims


```json
{
  "ServiceAccountName": "string",
  "ServiceAccountUID": "string",
  "SecretName": "string",
  "Namespace": "string"
}
```


*Определено в:* `pkg/serviceaccount/legacy.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Validator[legacyPrivateClaims]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/legacy.go:65`



---


[function] name: Validate file: pkg/serviceaccount/legacy.go:87 returns_error: да description: —


### Validate (pkg/serviceaccount/legacy.go:87)


Validate is a method that performs operations based on the provided parameters and may return an error.


```go
func (v *legacyValidator) Validate((*apiserverserviceaccount.ServiceAccountInfo, error)) (*apiserverserviceaccount.ServiceAccountInfo, error)
```


**Тип запроса:** apiserverserviceaccount.ServiceAccountInfo


```json
{
  "Name": "string",
  "PodName": "string",
  "CredentialID": "string",
  "NodeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/serviceaccount/util.go`


**Тип ответа:** apiserverserviceaccount.ServiceAccountInfo


```json
{
  "Name": "string",
  "PodName": "string",
  "CredentialID": "string",
  "NodeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/serviceaccount/util.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*apiserverserviceaccount.ServiceAccountInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/legacy.go:87`



---


[function] name: patchSecretWithLastUsedDate file: pkg/serviceaccount/legacy.go:183 returns_error: нет description: —


### patchSecretWithLastUsedDate (pkg/serviceaccount/legacy.go:183)


patchSecretWithLastUsedDate is a method that performs operations based on the provided parameters and returns (ctx context.Context, secret *v1.Secret).


```go
func (v *legacyValidator) patchSecretWithLastUsedDate((ctx context.Context, secret *v1.Secret)) (ctx context.Context, secret *v1.Secret)
```


**Тип запроса:** v1.Secret


```json
{
  "Immutable": false,
  "Data": {},
  "Type": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** ctx


```json
{
  "ctx": {},
  "cancel": {}
}
```


*Определено в:* `test/e2e/apimachinery/coordinatedleaderelection.go`


**Тип ответа:** context.Context


```json
{
  "Scope": {},
  "Type": null,
  "Path": null,
  "Member": null,
  "ListSelector": [],
  "ParentPath": null,
  "Constants": [],
  "StabilityLevel": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/validators.go`


**Тип ответа:** secret


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/secret.go`


**Тип ответа:** v1.Secret


```json
{
  "Immutable": false,
  "Data": {},
  "Type": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/serviceaccount/legacy.go:183`




## pkg/serviceaccount/metrics.go


📄 Исходный файл: `pkg/serviceaccount/metrics.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [RegisterMetrics](#registermetrics-pkgserviceaccountmetricsgo93) `:93`


</details>


[function] name: RegisterMetrics file: pkg/serviceaccount/metrics.go:93 returns_error: нет description: —


### RegisterMetrics (pkg/serviceaccount/metrics.go:93)


RegisterMetrics is a function that performs operations based on the provided parameters and returns ().


```go
func RegisterMetrics(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/metrics.go:93`




## pkg/serviceaccount/openidmetadata.go


📄 Исходный файл: `pkg/serviceaccount/openidmetadata.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [Enqueue](#enqueue-pkgserviceaccountopenidmetadatago72) `:72`

- 🔗 [GetConfigJSON](#getconfigjson-pkgserviceaccountopenidmetadatago66) `:66`

- 🔗 [GetKeysetJSON](#getkeysetjson-pkgserviceaccountopenidmetadatago69) `:69`

- 🔗 [NewOpenIDMetadataProvider](#newopenidmetadataprovider-pkgserviceaccountopenidmetadatago113) `:113`

- 🔗 [Update](#update-pkgserviceaccountopenidmetadatago78) `:78`

- 🔗 [algorithmFromPublicKey](#algorithmfrompublickey-pkgserviceaccountopenidmetadatago311) `:311`

- 🔗 [getAlgs](#getalgs-pkgserviceaccountopenidmetadatago253) `:253`

- 🔗 [jwkFromPublicKey](#jwkfrompublickey-pkgserviceaccountopenidmetadatago291) `:291`

- 🔗 [openIDConfigJSON](#openidconfigjson-pkgserviceaccountopenidmetadatago215) `:215`

- 🔗 [openIDKeysetJSON](#openidkeysetjson-pkgserviceaccountopenidmetadatago239) `:239`

- 🔗 [publicJWKSFromKeys](#publicjwksfromkeys-pkgserviceaccountopenidmetadatago268) `:268`


</details>


[function] name: Enqueue file: pkg/serviceaccount/openidmetadata.go:72 returns_error: нет description: —


### Enqueue (pkg/serviceaccount/openidmetadata.go:72)


Enqueue is a method that performs operations based on the provided parameters and returns ().


```go
func (p *openidConfigProvider) Enqueue(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:72`



---


[function] name: GetConfigJSON file: pkg/serviceaccount/openidmetadata.go:66 returns_error: нет description: —


### GetConfigJSON (pkg/serviceaccount/openidmetadata.go:66)


GetConfigJSON is a method that retrieves data based on the provided parameters and returns ([]byte, int).


```go
func (p *openidConfigProvider) GetConfigJSON(([]byte, int)) ([]byte, int)
```


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:66`



---


[function] name: GetKeysetJSON file: pkg/serviceaccount/openidmetadata.go:69 returns_error: нет description: —


### GetKeysetJSON (pkg/serviceaccount/openidmetadata.go:69)


GetKeysetJSON is a method that retrieves data based on the provided parameters and returns ([]byte, int).


```go
func (p *openidConfigProvider) GetKeysetJSON(([]byte, int)) ([]byte, int)
```


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:69`



---


[function] name: NewOpenIDMetadataProvider file: pkg/serviceaccount/openidmetadata.go:113 returns_error: да description: NewOpenIDMetadataProvider returns a provider for the OIDC discovery
endpoints, or an error if they could not be construc


### NewOpenIDMetadataProvider (pkg/serviceaccount/openidmetadata.go:113)


NewOpenIDMetadataProvider returns a provider for the OIDC discovery
endpoints, or an error if they could not be constructed. Callers should note
that this function may perform additional validation on inputs that is not
backwards-compatible with all command-line validation. The recommendation is
to log the error and skip installing the OIDC discovery endpoints.


```go
func NewOpenIDMetadataProvider((OpenIDMetadataProvider, error)) (OpenIDMetadataProvider, error)
```


**Тип ответа:** OpenIDMetadataProvider


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `OpenIDMetadataProvider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:113`



---


[function] name: Update file: pkg/serviceaccount/openidmetadata.go:78 returns_error: нет description: —


### Update (pkg/serviceaccount/openidmetadata.go:78)


Update is a method that updates data based on the provided parameters and returns ().


```go
func (p *openidConfigProvider) Update(()) ()
```


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:78`



---


[function] name: algorithmFromPublicKey file: pkg/serviceaccount/openidmetadata.go:311 returns_error: да description: —


### algorithmFromPublicKey (pkg/serviceaccount/openidmetadata.go:311)


algorithmFromPublicKey is a function that performs operations based on the provided parameters and may return an error.


```go
func algorithmFromPublicKey((jose.SignatureAlgorithm, error)) (jose.SignatureAlgorithm, error)
```


**Тип ответа:** jose.SignatureAlgorithm


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `jose.SignatureAlgorithm`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:311`



---


[function] name: getAlgs file: pkg/serviceaccount/openidmetadata.go:253 returns_error: нет description: —


### getAlgs (pkg/serviceaccount/openidmetadata.go:253)


getAlgs is a function that performs operations based on the provided parameters and returns (keys *jose.JSONWebKeySet).


```go
func getAlgs((keys *jose.JSONWebKeySet)) (keys *jose.JSONWebKeySet)
```


**Тип запроса:** jose.JSONWebKeySet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** keys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** jose.JSONWebKeySet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:253`



---


[function] name: jwkFromPublicKey file: pkg/serviceaccount/openidmetadata.go:291 returns_error: да description: —


### jwkFromPublicKey (pkg/serviceaccount/openidmetadata.go:291)


jwkFromPublicKey is a function that performs operations based on the provided parameters and may return an error.


```go
func jwkFromPublicKey((*jose.JSONWebKey, error)) (*jose.JSONWebKey, error)
```


**Тип запроса:** jose.JSONWebKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** jose.JSONWebKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*jose.JSONWebKey`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:291`



---


[function] name: openIDConfigJSON file: pkg/serviceaccount/openidmetadata.go:215 returns_error: да description: openIDConfigJSON returns the JSON OIDC Discovery Doc for the service
account issuer.


### openIDConfigJSON (pkg/serviceaccount/openidmetadata.go:215)


openIDConfigJSON returns the JSON OIDC Discovery Doc for the service
account issuer.


```go
func openIDConfigJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:215`



---


[function] name: openIDKeysetJSON file: pkg/serviceaccount/openidmetadata.go:239 returns_error: да description: openIDKeysetJSON returns the JSON Web Key Set for the service account
issuer's keys.


### openIDKeysetJSON (pkg/serviceaccount/openidmetadata.go:239)


openIDKeysetJSON returns the JSON Web Key Set for the service account
issuer's keys.


```go
func openIDKeysetJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:239`



---


[function] name: publicJWKSFromKeys file: pkg/serviceaccount/openidmetadata.go:268 returns_error: нет description: publicJWKSFromKeys constructs a JSONWebKeySet from a list of keys. The key
set will only contain the public keys associa


### publicJWKSFromKeys (pkg/serviceaccount/openidmetadata.go:268)


publicJWKSFromKeys constructs a JSONWebKeySet from a list of keys. The key
set will only contain the public keys associated with the input keys.


```go
func publicJWKSFromKeys((*jose.JSONWebKeySet, errors.Aggregate)) (*jose.JSONWebKeySet, errors.Aggregate)
```


**Тип запроса:** jose.JSONWebKeySet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** jose.JSONWebKeySet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errors.Aggregate


```json
{
  "Allowed": false,
  "ForbiddenReasons": [],
  "ForbiddenDetails": []
}
```


*Определено в:* `staging/src/k8s.io/pod-security-admission/policy/checks.go`


📍 *Расположение:* `pkg/serviceaccount/openidmetadata.go:268`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_securitycontext.md)

- [Следующая директория](pkg_util.md)


---

