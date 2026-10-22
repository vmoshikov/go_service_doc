---
title: "Функции: pkg/credentialprovider"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/credentialprovider
---


# Функции: pkg/credentialprovider


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_controlplane.md)

- [Следующая директория](pkg_features.md)


---


## Меню по файлам


- 📄 [pkg/credentialprovider/config.go](#pkgcredentialproviderconfiggo)

- 📄 [pkg/credentialprovider/keyring.go](#pkgcredentialproviderkeyringgo)

- 📄 [pkg/credentialprovider/plugin/config.go](#pkgcredentialproviderpluginconfiggo)

- 📄 [pkg/credentialprovider/plugin/metrics.go](#pkgcredentialproviderpluginmetricsgo)

- 📄 [pkg/credentialprovider/plugin/plugin.go](#pkgcredentialproviderpluginplugingo)

- 📄 [pkg/credentialprovider/plugin/plugins.go](#pkgcredentialproviderpluginpluginsgo)

- 📄 [pkg/credentialprovider/provider.go](#pkgcredentialproviderprovidergo)

- 📄 [pkg/credentialprovider/secrets/secrets.go](#pkgcredentialprovidersecretssecretsgo)


---


## pkg/credentialprovider/config.go


📄 Исходный файл: `pkg/credentialprovider/config.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [DefaultDockerConfigJSONPaths](#defaultdockerconfigjsonpaths-pkgcredentialproviderconfiggo92) `:92`

- 🔗 [DefaultDockercfgPaths](#defaultdockercfgpaths-pkgcredentialproviderconfiggo87) `:87`

- 🔗 [Error](#error-pkgcredentialproviderconfiggo184) `:184`

- 🔗 [GetPreferredDockercfgPath](#getpreferreddockercfgpath-pkgcredentialproviderconfiggo80) `:80`

- 🔗 [MarshalJSON](#marshaljson-pkgcredentialproviderconfiggo276) `:276`

- 🔗 [ReadDockerConfigFile](#readdockerconfigfile-pkgcredentialproviderconfiggo169) `:169`

- 🔗 [ReadDockerConfigFileFromBytes](#readdockerconfigfilefrombytes-pkgcredentialproviderconfiggo226) `:226`

- 🔗 [ReadDockerConfigJSONFile](#readdockerconfigjsonfile-pkgcredentialproviderconfiggo133) `:133`

- 🔗 [ReadDockercfgFile](#readdockercfgfile-pkgcredentialproviderconfiggo98) `:98`

- 🔗 [ReadSpecificDockerConfigJSONFile](#readspecificdockerconfigjsonfile-pkgcredentialproviderconfiggo159) `:159`

- 🔗 [ReadURL](#readurl-pkgcredentialproviderconfiggo190) `:190`

- 🔗 [SetPreferredDockercfgPath](#setpreferreddockercfgpath-pkgcredentialproviderconfiggo73) `:73`

- 🔗 [UnmarshalJSON](#unmarshaljson-pkgcredentialproviderconfiggo256) `:256`

- 🔗 [decodeDockerConfigFieldAuth](#decodedockerconfigfieldauth-pkgcredentialproviderconfiggo285) `:285`

- 🔗 [encodeDockerConfigFieldAuth](#encodedockerconfigfieldauth-pkgcredentialproviderconfiggo315) `:315`

- 🔗 [readDockerConfigJSONFileFromBytes](#readdockerconfigjsonfilefrombytes-pkgcredentialproviderconfiggo233) `:233`


</details>


[function] name: DefaultDockerConfigJSONPaths file: pkg/credentialprovider/config.go:92 returns_error: нет description: DefaultDockerConfigJSONPaths returns default search paths of .docker/config.json


### DefaultDockerConfigJSONPaths (pkg/credentialprovider/config.go:92)


DefaultDockerConfigJSONPaths returns default search paths of .docker/config.json


```go
func DefaultDockerConfigJSONPaths(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/config.go:92`



---


[function] name: DefaultDockercfgPaths file: pkg/credentialprovider/config.go:87 returns_error: нет description: DefaultDockercfgPaths returns default search paths of .dockercfg


### DefaultDockercfgPaths (pkg/credentialprovider/config.go:87)


DefaultDockercfgPaths returns default search paths of .dockercfg


```go
func DefaultDockercfgPaths(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/config.go:87`



---


[function] name: Error file: pkg/credentialprovider/config.go:184 returns_error: нет description: Error implements error


### Error (pkg/credentialprovider/config.go:184)


Error implements error


```go
func (he *HTTPError) Error(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/config.go:184`



---


[function] name: GetPreferredDockercfgPath file: pkg/credentialprovider/config.go:80 returns_error: нет description: GetPreferredDockercfgPath get preferred docker config path


### GetPreferredDockercfgPath (pkg/credentialprovider/config.go:80)


GetPreferredDockercfgPath get preferred docker config path


```go
func GetPreferredDockercfgPath(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/config.go:80`



---


[function] name: MarshalJSON file: pkg/credentialprovider/config.go:276 returns_error: да description: MarshalJSON implements the json.Marshaler interface.


### MarshalJSON (pkg/credentialprovider/config.go:276)


MarshalJSON implements the json.Marshaler interface.


```go
func (ident DockerConfigEntry) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:276`



---


[function] name: ReadDockerConfigFile file: pkg/credentialprovider/config.go:169 returns_error: да description: ReadDockerConfigFile read a docker config file from default path


### ReadDockerConfigFile (pkg/credentialprovider/config.go:169)


ReadDockerConfigFile read a docker config file from default path


```go
func ReadDockerConfigFile((cfg DockerConfig, err error)) (cfg DockerConfig, err error)
```


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


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


*Типы возврата:* `cfg DockerConfig`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:169`



---


[function] name: ReadDockerConfigFileFromBytes file: pkg/credentialprovider/config.go:226 returns_error: да description: ReadDockerConfigFileFromBytes read a docker config file from the given bytes


### ReadDockerConfigFileFromBytes (pkg/credentialprovider/config.go:226)


ReadDockerConfigFileFromBytes read a docker config file from the given bytes


```go
func ReadDockerConfigFileFromBytes((cfg DockerConfig, err error)) (cfg DockerConfig, err error)
```


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


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


*Типы возврата:* `cfg DockerConfig`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:226`



---


[function] name: ReadDockerConfigJSONFile file: pkg/credentialprovider/config.go:133 returns_error: да description: ReadDockerConfigJSONFile attempts to read a docker config.json file from the given paths.
if searchPaths is empty, the d


### ReadDockerConfigJSONFile (pkg/credentialprovider/config.go:133)


ReadDockerConfigJSONFile attempts to read a docker config.json file from the given paths.
if searchPaths is empty, the default paths are used.


```go
func ReadDockerConfigJSONFile((cfg DockerConfig, err error)) (cfg DockerConfig, err error)
```


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


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


*Типы возврата:* `cfg DockerConfig`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:133`



---


[function] name: ReadDockercfgFile file: pkg/credentialprovider/config.go:98 returns_error: да description: ReadDockercfgFile attempts to read a legacy dockercfg file from the given paths.
if searchPaths is empty, the default pa


### ReadDockercfgFile (pkg/credentialprovider/config.go:98)


ReadDockercfgFile attempts to read a legacy dockercfg file from the given paths.
if searchPaths is empty, the default paths are used.


```go
func ReadDockercfgFile((cfg DockerConfig, err error)) (cfg DockerConfig, err error)
```


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


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


*Типы возврата:* `cfg DockerConfig`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:98`



---


[function] name: ReadSpecificDockerConfigJSONFile file: pkg/credentialprovider/config.go:159 returns_error: да description: ReadSpecificDockerConfigJSONFile attempts to read docker configJSON from a given file path.


### ReadSpecificDockerConfigJSONFile (pkg/credentialprovider/config.go:159)


ReadSpecificDockerConfigJSONFile attempts to read docker configJSON from a given file path.


```go
func ReadSpecificDockerConfigJSONFile((cfg DockerConfig, err error)) (cfg DockerConfig, err error)
```


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


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


*Типы возврата:* `cfg DockerConfig`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:159`



---


[function] name: ReadURL file: pkg/credentialprovider/config.go:190 returns_error: да description: ReadURL read contents from given url


### ReadURL (pkg/credentialprovider/config.go:190)


ReadURL read contents from given url


```go
func ReadURL((body []byte, err error)) (body []byte, err error)
```


**Тип ответа:** body


```json
{
  "locator": {},
  "localPackage": {},
  "omitGogo": false,
  "omitFieldTypes": {},
  "t": null
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/go-to-protobuf/protobuf/generator.go`


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


*Типы возврата:* `body []byte`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:190`



---


[function] name: SetPreferredDockercfgPath file: pkg/credentialprovider/config.go:73 returns_error: нет description: SetPreferredDockercfgPath set preferred docker config path


### SetPreferredDockercfgPath (pkg/credentialprovider/config.go:73)


SetPreferredDockercfgPath set preferred docker config path


```go
func SetPreferredDockercfgPath((path string)) (path string)
```


**Тип ответа:** path


```json
{
  "muxName": "string",
  "pathToHandler": {},
  "prefixHandlers": [],
  "notFoundHandler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


📍 *Расположение:* `pkg/credentialprovider/config.go:73`



---


[function] name: UnmarshalJSON file: pkg/credentialprovider/config.go:256 returns_error: нет description: UnmarshalJSON implements the json.Unmarshaler interface.


### UnmarshalJSON (pkg/credentialprovider/config.go:256)


UnmarshalJSON implements the json.Unmarshaler interface.


```go
func (ident *DockerConfigEntry) UnmarshalJSON((data []byte)) (data []byte)
```


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


📍 *Расположение:* `pkg/credentialprovider/config.go:256`



---


[function] name: decodeDockerConfigFieldAuth file: pkg/credentialprovider/config.go:285 returns_error: да description: decodeDockerConfigFieldAuth deserializes the "auth" field from dockercfg into a
username and a password. The format of t


### decodeDockerConfigFieldAuth (pkg/credentialprovider/config.go:285)


decodeDockerConfigFieldAuth deserializes the "auth" field from dockercfg into a
username and a password. The format of the auth field is base64(<username>:<password>).


```go
func decodeDockerConfigFieldAuth((username, password string, err error)) (username, password string, err error)
```


**Тип ответа:** username


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** password


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


*Типы возврата:* `username`, `password string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:285`



---


[function] name: encodeDockerConfigFieldAuth file: pkg/credentialprovider/config.go:315 returns_error: нет description: —


### encodeDockerConfigFieldAuth (pkg/credentialprovider/config.go:315)


encodeDockerConfigFieldAuth is a function that performs operations based on the provided parameters and returns (username, password string).


```go
func encodeDockerConfigFieldAuth((username, password string)) (username, password string)
```


**Тип ответа:** username


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** password


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/credentialprovider/config.go:315`



---


[function] name: readDockerConfigJSONFileFromBytes file: pkg/credentialprovider/config.go:233 returns_error: да description: —


### readDockerConfigJSONFileFromBytes (pkg/credentialprovider/config.go:233)


readDockerConfigJSONFileFromBytes is a function that performs operations based on the provided parameters and may return an error.


```go
func readDockerConfigJSONFileFromBytes((cfg DockerConfig, err error)) (cfg DockerConfig, err error)
```


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


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


*Типы возврата:* `cfg DockerConfig`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/config.go:233`




## pkg/credentialprovider/keyring.go


📄 Исходный файл: `pkg/credentialprovider/keyring.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Add](#add-pkgcredentialproviderkeyringgo131) `:131`

- 🔗 [Lookup](#lookup-pkgcredentialproviderkeyringgo295) `:295`

- 🔗 [Lookup](#lookup-pkgcredentialproviderkeyringgo322) `:322`

- 🔗 [Lookup](#lookup-pkgcredentialproviderkeyringgo340) `:340`

- 🔗 [Lookup](#lookup-pkgcredentialproviderkeyringgo349) `:349`

- 🔗 [NewTrackedAuthConfig](#newtrackedauthconfig-pkgcredentialproviderkeyringgo73) `:73`

- 🔗 [ParseSchemelessURL](#parseschemelessurl-pkgcredentialproviderkeyringgo220) `:220`

- 🔗 [SplitURL](#spliturl-pkgcredentialproviderkeyringgo231) `:231`

- 🔗 [URLsMatch](#urlsmatch-pkgcredentialproviderkeyringgo262) `:262`

- 🔗 [URLsMatchStr](#urlsmatchstr-pkgcredentialproviderkeyringgo241) `:241`

- 🔗 [hashAuthConfig](#hashauthconfig-pkgcredentialproviderkeyringgo363) `:363`

- 🔗 [isDefaultRegistryMatch](#isdefaultregistrymatch-pkgcredentialproviderkeyringgo193) `:193`


</details>


[function] name: Add file: pkg/credentialprovider/keyring.go:131 returns_error: нет description: Add inserts the docker config `cfg` into the basic docker keyring. It attaches
the `src` information that describes wher


### Add (pkg/credentialprovider/keyring.go:131)


Add inserts the docker config `cfg` into the basic docker keyring. It attaches
the `src` information that describes where the docker config `cfg` comes from.
`src` is nil if the docker config is globally available on the node.


```go
func (dk *BasicDockerKeyring) Add((src *CredentialSource, cfg DockerConfig)) (src *CredentialSource, cfg DockerConfig)
```


**Тип запроса:** CredentialSource


```json
{
  "Secret": null,
  "ServiceAccount": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CredentialSource


```json
{
  "Secret": null,
  "ServiceAccount": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Тип ответа:** cfg


```json
{
  "cfgCtlr": null,
  "newPLStates": {},
  "shareSum": 0.0,
  "haveExemptPL": false,
  "fsStatusUpdates": [],
  "maxWaitingRequests": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`


**Тип ответа:** DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:131`



---


[function] name: Lookup file: pkg/credentialprovider/keyring.go:295 returns_error: нет description: Lookup implements the DockerKeyring method for fetching credentials based on image name.
Multiple credentials may be ret


### Lookup (pkg/credentialprovider/keyring.go:295)


Lookup implements the DockerKeyring method for fetching credentials based on image name.
Multiple credentials may be returned if there are multiple potentially valid credentials
available.  This allows for rotation.


```go
func (dk *BasicDockerKeyring) Lookup(([]TrackedAuthConfig, bool)) ([]TrackedAuthConfig, bool)
```


**Тип ответа:** TrackedAuthConfig


```json
{
  "AuthConfigHash": "string",
  "Source": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:295`



---


[function] name: Lookup file: pkg/credentialprovider/keyring.go:322 returns_error: нет description: Lookup implements the DockerKeyring method for fetching credentials
based on image name.


### Lookup (pkg/credentialprovider/keyring.go:322)


Lookup implements the DockerKeyring method for fetching credentials
based on image name.


```go
func (dk *providersDockerKeyring) Lookup(([]TrackedAuthConfig, bool)) ([]TrackedAuthConfig, bool)
```


**Тип ответа:** TrackedAuthConfig


```json
{
  "AuthConfigHash": "string",
  "Source": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:322`



---


[function] name: Lookup file: pkg/credentialprovider/keyring.go:340 returns_error: нет description: Lookup implements the DockerKeyring method for fetching credentials based on image name
return fake auth and ok


### Lookup (pkg/credentialprovider/keyring.go:340)


Lookup implements the DockerKeyring method for fetching credentials based on image name
return fake auth and ok


```go
func (f *FakeKeyring) Lookup(([]TrackedAuthConfig, bool)) ([]TrackedAuthConfig, bool)
```


**Тип ответа:** TrackedAuthConfig


```json
{
  "AuthConfigHash": "string",
  "Source": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:340`



---


[function] name: Lookup file: pkg/credentialprovider/keyring.go:349 returns_error: нет description: Lookup implements the DockerKeyring method for fetching credentials based on image name.
return each credentials


### Lookup (pkg/credentialprovider/keyring.go:349)


Lookup implements the DockerKeyring method for fetching credentials based on image name.
return each credentials


```go
func (k UnionDockerKeyring) Lookup(([]TrackedAuthConfig, bool)) ([]TrackedAuthConfig, bool)
```


**Тип ответа:** TrackedAuthConfig


```json
{
  "AuthConfigHash": "string",
  "Source": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:349`



---


[function] name: NewTrackedAuthConfig file: pkg/credentialprovider/keyring.go:73 returns_error: нет description: NewTrackedAuthConfig initializes the TrackedAuthConfig structure by adding
the source information to the supplied AuthCo


### NewTrackedAuthConfig (pkg/credentialprovider/keyring.go:73)


NewTrackedAuthConfig initializes the TrackedAuthConfig structure by adding
the source information to the supplied AuthConfig. It also counts a hash of the
AuthConfig and keeps it in the returned structure.

The supplied CredentialSource is only used when the "KubeletEnsureSecretPulledImages"
is enabled, the same applies for counting the hash.


```go
func NewTrackedAuthConfig((c *AuthConfig, src *CredentialSource)) (c *AuthConfig, src *CredentialSource)
```


**Тип запроса:** AuthConfig


```json
{
  "Username": "string",
  "Password": "string",
  "Auth": "string",
  "Email": "string",
  "ServerAddress": "string",
  "IdentityToken": "string",
  "RegistryToken": "string"
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Тип запроса:** CredentialSource


```json
{
  "Secret": null,
  "ServiceAccount": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Тип ответа:** c


```json
{
  "Name": "string",
  "ImportPath": "string",
  "Imports": [],
  "TestImports": [],
  "XTestImports": []
}
```


*Определено в:* `cmd/dependencycheck/dependencycheck.go`


**Тип ответа:** AuthConfig


```json
{
  "Username": "string",
  "Password": "string",
  "Auth": "string",
  "Email": "string",
  "ServerAddress": "string",
  "IdentityToken": "string",
  "RegistryToken": "string"
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** CredentialSource


```json
{
  "Secret": null,
  "ServiceAccount": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:73`



---


[function] name: ParseSchemelessURL file: pkg/credentialprovider/keyring.go:220 returns_error: да description: ParseSchemelessURL parses a schemeless url and returns a url.URL
url.Parse require a scheme, but ours don't have schemes


### ParseSchemelessURL (pkg/credentialprovider/keyring.go:220)


ParseSchemelessURL parses a schemeless url and returns a url.URL
url.Parse require a scheme, but ours don't have schemes.  Adding a
scheme to make url.Parse happy, then clear out the resulting scheme.


```go
func ParseSchemelessURL((*url.URL, error)) (*url.URL, error)
```


**Тип запроса:** url.URL


```json
{
  "Backoff": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/rest/urlbackoff.go`


**Тип ответа:** url.URL


```json
{
  "Backoff": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/rest/urlbackoff.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*url.URL`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/keyring.go:220`



---


[function] name: SplitURL file: pkg/credentialprovider/keyring.go:231 returns_error: нет description: SplitURL splits the host name into parts, as well as the port


### SplitURL (pkg/credentialprovider/keyring.go:231)


SplitURL splits the host name into parts, as well as the port


```go
func SplitURL((parts []string, port string)) (parts []string, port string)
```


**Тип ответа:** parts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** port


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:231`



---


[function] name: URLsMatch file: pkg/credentialprovider/keyring.go:262 returns_error: да description: URLsMatch checks whether the given target url matches the glob url, which may have
glob wild cards in the host name.

Ex


### URLsMatch (pkg/credentialprovider/keyring.go:262)


URLsMatch checks whether the given target url matches the glob url, which may have
glob wild cards in the host name.

Examples:

globURL=*.docker.io, targetURL=blah.docker.io => match
globURL=*.docker.io, targetURL=not.right.io   => no match

Note that we don't support wildcards in ports and paths yet.


```go
func URLsMatch((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/keyring.go:262`



---


[function] name: URLsMatchStr file: pkg/credentialprovider/keyring.go:241 returns_error: да description: URLsMatchStr is wrapper for URLsMatch, operating on strings instead of URLs.


### URLsMatchStr (pkg/credentialprovider/keyring.go:241)


URLsMatchStr is wrapper for URLsMatch, operating on strings instead of URLs.


```go
func URLsMatchStr((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/keyring.go:241`



---


[function] name: hashAuthConfig file: pkg/credentialprovider/keyring.go:363 returns_error: нет description: —


### hashAuthConfig (pkg/credentialprovider/keyring.go:363)


hashAuthConfig is a function that performs operations based on the provided parameters and returns (creds *AuthConfig).


```go
func hashAuthConfig((creds *AuthConfig)) (creds *AuthConfig)
```


**Тип запроса:** AuthConfig


```json
{
  "Username": "string",
  "Password": "string",
  "Auth": "string",
  "Email": "string",
  "ServerAddress": "string",
  "IdentityToken": "string",
  "RegistryToken": "string"
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Тип ответа:** creds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** AuthConfig


```json
{
  "Username": "string",
  "Password": "string",
  "Auth": "string",
  "Email": "string",
  "ServerAddress": "string",
  "IdentityToken": "string",
  "RegistryToken": "string"
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:363`



---


[function] name: isDefaultRegistryMatch file: pkg/credentialprovider/keyring.go:193 returns_error: нет description: isDefaultRegistryMatch determines whether the given image will
pull from the default registry (DockerHub) based on the
c


### isDefaultRegistryMatch (pkg/credentialprovider/keyring.go:193)


isDefaultRegistryMatch determines whether the given image will
pull from the default registry (DockerHub) based on the
characteristics of its name.


```go
func isDefaultRegistryMatch((image string)) (image string)
```


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `pkg/credentialprovider/keyring.go:193`




## pkg/credentialprovider/plugin/config.go


📄 Исходный файл: `pkg/credentialprovider/plugin/config.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [decode](#decode-pkgcredentialproviderpluginconfiggo124) `:124`

- 🔗 [readCredentialProviderConfig](#readcredentialproviderconfig-pkgcredentialproviderpluginconfiggo50) `:50`

- 🔗 [validateCredentialProviderConfig](#validatecredentialproviderconfig-pkgcredentialproviderpluginconfiggo146) `:146`

- 🔗 [validateServiceAccountAnnotationKeys](#validateserviceaccountannotationkeys-pkgcredentialproviderpluginconfiggo246) `:246`


</details>


[function] name: decode file: pkg/credentialprovider/plugin/config.go:124 returns_error: да description: decode decodes data into the internal CredentialProviderConfig type.


### decode (pkg/credentialprovider/plugin/config.go:124)


decode decodes data into the internal CredentialProviderConfig type.


```go
func decode((*kubeletconfig.CredentialProviderConfig, error)) (*kubeletconfig.CredentialProviderConfig, error)
```


**Тип запроса:** kubeletconfig.CredentialProviderConfig


```json
{
  "Providers": []
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfig.CredentialProviderConfig


```json
{
  "Providers": []
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfig.CredentialProviderConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/config.go:124`



---


[function] name: readCredentialProviderConfig file: pkg/credentialprovider/plugin/config.go:50 returns_error: да description: readCredentialProviderConfig receives a path to a config file or directory.
If the path is a directory, it reads all "*.


### readCredentialProviderConfig (pkg/credentialprovider/plugin/config.go:50)


readCredentialProviderConfig receives a path to a config file or directory.
If the path is a directory, it reads all "*.json", "*.yaml" and "*.yml" files in lexicographic order,
decodes them, and merges their entries into a single CredentialProviderConfig object.
If the path is a file, it decodes the file into a CredentialProviderConfig object directly.
It also returns the SHA256 hash of all the raw file content. This hash is exposed via metrics
as an external API to allow monitoring of configuration changes.
The hash format follows container digest conventions (sha256:hexstring) for consistency.


```go
func readCredentialProviderConfig((*kubeletconfig.CredentialProviderConfig, string, error)) (*kubeletconfig.CredentialProviderConfig, string, error)
```


**Тип запроса:** kubeletconfig.CredentialProviderConfig


```json
{
  "Providers": []
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfig.CredentialProviderConfig


```json
{
  "Providers": []
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfig.CredentialProviderConfig`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/config.go:50`



---


[function] name: validateCredentialProviderConfig file: pkg/credentialprovider/plugin/config.go:146 returns_error: нет description: validateCredentialProviderConfig validates CredentialProviderConfig.


### validateCredentialProviderConfig (pkg/credentialprovider/plugin/config.go:146)


validateCredentialProviderConfig validates CredentialProviderConfig.


```go
func validateCredentialProviderConfig((config *kubeletconfig.CredentialProviderConfig, saTokenForCredentialProviders bool)) (config *kubeletconfig.CredentialProviderConfig, saTokenForCredentialProviders bool)
```


**Тип запроса:** kubeletconfig.CredentialProviderConfig


```json
{
  "Providers": []
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeletconfig.CredentialProviderConfig


```json
{
  "Providers": []
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** saTokenForCredentialProviders


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/credentialprovider/plugin/config.go:146`



---


[function] name: validateServiceAccountAnnotationKeys file: pkg/credentialprovider/plugin/config.go:246 returns_error: нет description: validateServiceAccountAnnotationKeys validates the service account annotation keys.


### validateServiceAccountAnnotationKeys (pkg/credentialprovider/plugin/config.go:246)


validateServiceAccountAnnotationKeys validates the service account annotation keys.


```go
func validateServiceAccountAnnotationKeys((fldPath *field.Path, keys []string)) (fldPath *field.Path, keys []string)
```


**Тип запроса:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** fldPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** field.Path


```json
{
  "name": "string",
  "index": "string",
  "parent": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/validation/field/path.go`


**Тип ответа:** keys


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/credentialprovider/plugin/config.go:246`




## pkg/credentialprovider/plugin/metrics.go


📄 Исходный файл: `pkg/credentialprovider/plugin/metrics.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [recordCredentialProviderConfigHash](#recordcredentialproviderconfighash-pkgcredentialproviderpluginmetricsgo80) `:80`

- 🔗 [registerMetrics](#registermetrics-pkgcredentialproviderpluginmetricsgo71) `:71`


</details>


[function] name: recordCredentialProviderConfigHash file: pkg/credentialprovider/plugin/metrics.go:80 returns_error: нет description: recordCredentialProviderConfigHash records the hash of the credential provider configuration


### recordCredentialProviderConfigHash (pkg/credentialprovider/plugin/metrics.go:80)


recordCredentialProviderConfigHash records the hash of the credential provider configuration


```go
func recordCredentialProviderConfigHash((configHash string)) (configHash string)
```


**Тип ответа:** configHash


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/credentialprovider/plugin/metrics.go:80`



---


[function] name: registerMetrics file: pkg/credentialprovider/plugin/metrics.go:71 returns_error: нет description: registerMetrics registers credential provider metrics.


### registerMetrics (pkg/credentialprovider/plugin/metrics.go:71)


registerMetrics registers credential provider metrics.


```go
func registerMetrics(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/plugin/metrics.go:71`




## pkg/credentialprovider/plugin/plugin.go


📄 Исходный файл: `pkg/credentialprovider/plugin/plugin.go`


<details open>
<summary><b>Функции в этом файле (29)</b></summary>


- 🔗 [Error](#error-pkgcredentialproviderpluginplugingo298) `:298`

- 🔗 [ExecPlugin](#execplugin-pkgcredentialproviderpluginplugingo686) `:686`

- 🔗 [IsExpired](#isexpired-pkgcredentialproviderpluginplugingo385) `:385`

- 🔗 [RegisterCredentialProviderPlugins](#registercredentialproviderplugins-pkgcredentialproviderpluginplugingo143) `:143`

- 🔗 [addAnnotations](#addannotations-pkgcredentialproviderpluginplugingo111) `:111`

- 🔗 [addString](#addstring-pkgcredentialproviderpluginplugingo104) `:104`

- 🔗 [build](#build-pkgcredentialproviderpluginplugingo125) `:125`

- 🔗 [cacheKeyFunc](#cachekeyfunc-pkgcredentialproviderpluginplugingo373) `:373`

- 🔗 [decodeResponse](#decoderesponse-pkgcredentialproviderpluginplugingo773) `:773`

- 🔗 [encodeRequest](#encoderequest-pkgcredentialproviderpluginplugingo763) `:763`

- 🔗 [generateCacheKey](#generatecachekey-pkgcredentialproviderpluginplugingo823) `:823`

- 🔗 [generateServiceAccountCacheKey](#generateserviceaccountcachekey-pkgcredentialproviderpluginplugingo809) `:809`

- 🔗 [generateSingleFlightKey](#generatesingleflightkey-pkgcredentialproviderpluginplugingo831) `:831`

- 🔗 [getCachedCredentials](#getcachedcredentials-pkgcredentialproviderpluginplugingo614) `:614`

- 🔗 [getHashIfNotEmpty](#gethashifnotempty-pkgcredentialproviderpluginplugingo841) `:841`

- 🔗 [getServiceAccountData](#getserviceaccountdata-pkgcredentialproviderpluginplugingo316) `:316`

- 🔗 [getServiceAccountToken](#getserviceaccounttoken-pkgcredentialproviderpluginplugingo341) `:341`

- 🔗 [init](#init-pkgcredentialproviderpluginplugingo133) `:133`

- 🔗 [isImageAllowed](#isimageallowed-pkgcredentialproviderpluginplugingo603) `:603`

- 🔗 [isRequiredAnnotationNotFoundError](#isrequiredannotationnotfounderror-pkgcredentialproviderpluginplugingo302) `:302`

- 🔗 [lookupCredentialsInCache](#lookupcredentialsincache-pkgcredentialproviderpluginplugingo643) `:643`

- 🔗 [mergeEnvVars](#mergeenvvars-pkgcredentialproviderpluginplugingo803) `:803`

- 🔗 [newCacheKeyBuilder](#newcachekeybuilder-pkgcredentialproviderpluginplugingo100) `:100`

- 🔗 [newPluginProvider](#newpluginprovider-pkgcredentialproviderpluginplugingo196) `:196`

- 🔗 [newServiceAccountProvider](#newserviceaccountprovider-pkgcredentialproviderpluginplugingo273) `:273`

- 🔗 [parseRegistry](#parseregistry-pkgcredentialproviderpluginplugingo795) `:795`

- 🔗 [provide](#provide-pkgcredentialproviderpluginplugingo429) `:429`

- 🔗 [provideWithCoordinates](#providewithcoordinates-pkgcredentialproviderpluginplugingo408) `:408`

- 🔗 [runPlugin](#runplugin-pkgcredentialproviderpluginplugingo744) `:744`


</details>


[function] name: Error file: pkg/credentialprovider/plugin/plugin.go:298 returns_error: нет description: —


### Error (pkg/credentialprovider/plugin/plugin.go:298)


Error is a method that performs operations based on the provided parameters and returns ().


```go
func (e requiredAnnotationNotFoundError) Error(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:298`



---


[function] name: ExecPlugin file: pkg/credentialprovider/plugin/plugin.go:686 returns_error: да description: ExecPlugin executes the plugin binary with arguments and environment variables specified in CredentialProviderConfig:

$


### ExecPlugin (pkg/credentialprovider/plugin/plugin.go:686)


ExecPlugin executes the plugin binary with arguments and environment variables specified in CredentialProviderConfig:

$ ENV_NAME=ENV_VALUE <plugin-name> args[0] args[1] <<<request

The plugin is expected to receive the CredentialProviderRequest API via stdin from the kubelet and
return CredentialProviderResponse via stdout.


```go
func (e *execPlugin) ExecPlugin((*credentialproviderapi.CredentialProviderResponse, error)) (*credentialproviderapi.CredentialProviderResponse, error)
```


**Тип запроса:** credentialproviderapi.CredentialProviderResponse


```json
{
  "CacheKeyType": {},
  "CacheDuration": null,
  "Auth": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/credentialprovider/v1alpha1/types.go`


**Тип ответа:** credentialproviderapi.CredentialProviderResponse


```json
{
  "CacheKeyType": {},
  "CacheDuration": null,
  "Auth": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/credentialprovider/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*credentialproviderapi.CredentialProviderResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:686`



---


[function] name: IsExpired file: pkg/credentialprovider/plugin/plugin.go:385 returns_error: нет description: IsExpired returns true if the current time is after cacheEntry.expiresAt, which is determined by the
cache duration retu


### IsExpired (pkg/credentialprovider/plugin/plugin.go:385)


IsExpired returns true if the current time is after cacheEntry.expiresAt, which is determined by the
cache duration returned from the credential provider plugin response.


```go
func (c *cacheExpirationPolicy) IsExpired((entry *cache.TimestampedEntry)) (entry *cache.TimestampedEntry)
```


**Тип запроса:** cache.TimestampedEntry


```json
{
  "Obj": {},
  "Timestamp": {},
  "key": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/expiration_cache.go`


**Тип ответа:** entry


```json
{
  "val": {},
  "expiry": {},
  "generation": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/cache/expiring.go`


**Тип ответа:** cache.TimestampedEntry


```json
{
  "Obj": {},
  "Timestamp": {},
  "key": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/expiration_cache.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:385`



---


[function] name: RegisterCredentialProviderPlugins file: pkg/credentialprovider/plugin/plugin.go:143 returns_error: нет description: RegisterCredentialProviderPlugins is called from kubelet to register external credential provider
plugins according to t


### RegisterCredentialProviderPlugins (pkg/credentialprovider/plugin/plugin.go:143)


RegisterCredentialProviderPlugins is called from kubelet to register external credential provider
plugins according to the CredentialProviderConfig config file.


```go
func RegisterCredentialProviderPlugins((pluginConfigPath, pluginBinDir string,
	getServiceAccountToken getServiceAccountTokenFunc,
	getServiceAccount GetServiceAccountFunc,
)) (pluginConfigPath, pluginBinDir string,
	getServiceAccountToken getServiceAccountTokenFunc,
	getServiceAccount GetServiceAccountFunc,
)
```


**Тип ответа:** pluginConfigPath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pluginBinDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** getServiceAccountToken


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** getServiceAccountTokenFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** getServiceAccount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GetServiceAccountFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:143`



---


[function] name: addAnnotations file: pkg/credentialprovider/plugin/plugin.go:111 returns_error: нет description: —


### addAnnotations (pkg/credentialprovider/plugin/plugin.go:111)


addAnnotations is a method that performs operations based on the provided parameters and returns (annotations map[string]string).


```go
func (c *cacheKeyBuilder) addAnnotations((annotations map[string]string)) (annotations map[string]string)
```


**Тип ответа:** annotations


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:111`



---


[function] name: addString file: pkg/credentialprovider/plugin/plugin.go:104 returns_error: нет description: —


### addString (pkg/credentialprovider/plugin/plugin.go:104)


addString is a method that performs operations based on the provided parameters and returns (value string).


```go
func (c *cacheKeyBuilder) addString((value string)) (value string)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:104`



---


[function] name: build file: pkg/credentialprovider/plugin/plugin.go:125 returns_error: да description: —


### build (pkg/credentialprovider/plugin/plugin.go:125)


build is a method that performs operations based on the provided parameters and may return an error.


```go
func (c *cacheKeyBuilder) build((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:125`



---


[function] name: cacheKeyFunc file: pkg/credentialprovider/plugin/plugin.go:373 returns_error: да description: cacheKeyFunc extracts AuthEntry.MatchKey as the cache key function for the plugin provider.


### cacheKeyFunc (pkg/credentialprovider/plugin/plugin.go:373)


cacheKeyFunc extracts AuthEntry.MatchKey as the cache key function for the plugin provider.


```go
func cacheKeyFunc((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:373`



---


[function] name: decodeResponse file: pkg/credentialprovider/plugin/plugin.go:773 returns_error: да description: decodeResponse decodes data into the internal CredentialProviderResponse type


### decodeResponse (pkg/credentialprovider/plugin/plugin.go:773)


decodeResponse decodes data into the internal CredentialProviderResponse type


```go
func (e *execPlugin) decodeResponse((*credentialproviderapi.CredentialProviderResponse, error)) (*credentialproviderapi.CredentialProviderResponse, error)
```


**Тип запроса:** credentialproviderapi.CredentialProviderResponse


```json
{
  "CacheKeyType": {},
  "CacheDuration": null,
  "Auth": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/credentialprovider/v1alpha1/types.go`


**Тип ответа:** credentialproviderapi.CredentialProviderResponse


```json
{
  "CacheKeyType": {},
  "CacheDuration": null,
  "Auth": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/credentialprovider/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*credentialproviderapi.CredentialProviderResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:773`



---


[function] name: encodeRequest file: pkg/credentialprovider/plugin/plugin.go:763 returns_error: да description: encodeRequest encodes the internal CredentialProviderRequest type into the v1alpha1 version in json


### encodeRequest (pkg/credentialprovider/plugin/plugin.go:763)


encodeRequest encodes the internal CredentialProviderRequest type into the v1alpha1 version in json


```go
func (e *execPlugin) encodeRequest(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:763`



---


[function] name: generateCacheKey file: pkg/credentialprovider/plugin/plugin.go:823 returns_error: да description: —


### generateCacheKey (pkg/credentialprovider/plugin/plugin.go:823)


generateCacheKey is a function that performs operations based on the provided parameters and may return an error.


```go
func generateCacheKey((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:823`



---


[function] name: generateServiceAccountCacheKey file: pkg/credentialprovider/plugin/plugin.go:809 returns_error: да description: —


### generateServiceAccountCacheKey (pkg/credentialprovider/plugin/plugin.go:809)


generateServiceAccountCacheKey is a function that performs operations based on the provided parameters and may return an error.


```go
func generateServiceAccountCacheKey((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:809`



---


[function] name: generateSingleFlightKey file: pkg/credentialprovider/plugin/plugin.go:831 returns_error: да description: —


### generateSingleFlightKey (pkg/credentialprovider/plugin/plugin.go:831)


generateSingleFlightKey is a function that performs operations based on the provided parameters and may return an error.


```go
func generateSingleFlightKey((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:831`



---


[function] name: getCachedCredentials file: pkg/credentialprovider/plugin/plugin.go:614 returns_error: да description: getCachedCredentials returns a credentialprovider.DockerConfig if cached from the plugin.


### getCachedCredentials (pkg/credentialprovider/plugin/plugin.go:614)


getCachedCredentials returns a credentialprovider.DockerConfig if cached from the plugin.


```go
func (p *pluginProvider) getCachedCredentials((credentialprovider.DockerConfig, bool, error)) (credentialprovider.DockerConfig, bool, error)
```


**Тип ответа:** credentialprovider.DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `credentialprovider.DockerConfig`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:614`



---


[function] name: getHashIfNotEmpty file: pkg/credentialprovider/plugin/plugin.go:841 returns_error: нет description: getHashIfNotEmpty returns the sha256 hash of the data if it is not empty.


### getHashIfNotEmpty (pkg/credentialprovider/plugin/plugin.go:841)


getHashIfNotEmpty returns the sha256 hash of the data if it is not empty.


```go
func getHashIfNotEmpty((data string)) (data string)
```


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:841`



---


[function] name: getServiceAccountData file: pkg/credentialprovider/plugin/plugin.go:316 returns_error: да description: getServiceAccountData returns the service account UID and required annotations for the service account.
If the service a


### getServiceAccountData (pkg/credentialprovider/plugin/plugin.go:316)


getServiceAccountData returns the service account UID and required annotations for the service account.
If the service account does not exist, an error is returned.
saAnnotations is a map of annotation keys and values that the plugin requires to generate credentials
that's defined in the tokenAttributes in the credential provider config.
requiredServiceAccountAnnotationKeys are the keys that are required to be present in the service account.
If any of the keys defined in this list are not present in the service account, kubelet will not invoke the plugin
and will return an error.
optionalServiceAccountAnnotationKeys are the keys that are optional to be present in the service account.
If present, they will be added to the saAnnotations map.


```go
func (s *serviceAccountProvider) getServiceAccountData((types.UID, map[string]string, error)) (types.UID, map[string]string, error)
```


**Тип ответа:** types.UID


```json
{
  "key": "string"
}
```


*Определено в:* `pkg/controller/controller_utils.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `types.UID`, `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:316`



---


[function] name: getServiceAccountToken file: pkg/credentialprovider/plugin/plugin.go:341 returns_error: да description: getServiceAccountToken returns a service account token for the service account.


### getServiceAccountToken (pkg/credentialprovider/plugin/plugin.go:341)


getServiceAccountToken returns a service account token for the service account.


```go
func (s *serviceAccountProvider) getServiceAccountToken((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:341`



---


[function] name: init file: pkg/credentialprovider/plugin/plugin.go:133 returns_error: нет description: —


### init (pkg/credentialprovider/plugin/plugin.go:133)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:133`



---


[function] name: isImageAllowed file: pkg/credentialprovider/plugin/plugin.go:603 returns_error: нет description: isImageAllowed returns true if the image matches against the list of allowed matches by the plugin.


### isImageAllowed (pkg/credentialprovider/plugin/plugin.go:603)


isImageAllowed returns true if the image matches against the list of allowed matches by the plugin.


```go
func (p *pluginProvider) isImageAllowed((image string)) (image string)
```


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:603`



---


[function] name: isRequiredAnnotationNotFoundError file: pkg/credentialprovider/plugin/plugin.go:302 returns_error: да description: —


### isRequiredAnnotationNotFoundError (pkg/credentialprovider/plugin/plugin.go:302)


isRequiredAnnotationNotFoundError is a function that performs operations based on the provided parameters and may return an error.


```go
func isRequiredAnnotationNotFoundError((err error)) (err error)
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


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:302`



---


[function] name: lookupCredentialsInCache file: pkg/credentialprovider/plugin/plugin.go:643 returns_error: да description: lookupCredentialsInCache performs a single cache lookup for the given base key and service account cache key


### lookupCredentialsInCache (pkg/credentialprovider/plugin/plugin.go:643)


lookupCredentialsInCache performs a single cache lookup for the given base key and service account cache key


```go
func (p *pluginProvider) lookupCredentialsInCache((credentialprovider.DockerConfig, bool, error)) (credentialprovider.DockerConfig, bool, error)
```


**Тип ответа:** credentialprovider.DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `credentialprovider.DockerConfig`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:643`



---


[function] name: mergeEnvVars file: pkg/credentialprovider/plugin/plugin.go:803 returns_error: нет description: mergedEnvVars overlays system defined env vars with credential provider env vars,
it gives priority to the credential pr


### mergeEnvVars (pkg/credentialprovider/plugin/plugin.go:803)


mergedEnvVars overlays system defined env vars with credential provider env vars,
it gives priority to the credential provider vars allowing user to override system
env vars


```go
func mergeEnvVars((sysEnvVars, credProviderVars []string)) (sysEnvVars, credProviderVars []string)
```


**Тип ответа:** sysEnvVars


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** credProviderVars


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:803`



---


[function] name: newCacheKeyBuilder file: pkg/credentialprovider/plugin/plugin.go:100 returns_error: нет description: —


### newCacheKeyBuilder (pkg/credentialprovider/plugin/plugin.go:100)


newCacheKeyBuilder is a function that performs operations based on the provided parameters and returns ().


```go
func newCacheKeyBuilder(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:100`



---


[function] name: newPluginProvider file: pkg/credentialprovider/plugin/plugin.go:196 returns_error: да description: newPluginProvider returns a new pluginProvider based on the credential provider config.


### newPluginProvider (pkg/credentialprovider/plugin/plugin.go:196)


newPluginProvider returns a new pluginProvider based on the credential provider config.


```go
func newPluginProvider((*pluginProvider, error)) (*pluginProvider, error)
```


**Тип запроса:** pluginProvider


```json
{
  "name": "string",
  "clock": {},
  "group": {},
  "matchImages": [],
  "cache": {},
  "defaultCacheDuration": {},
  "plugin": {},
  "lastCachePurge": {},
  "serviceAccountProvider": null
}
```


*Определено в:* `pkg/credentialprovider/plugin/plugin.go`


**Тип ответа:** pluginProvider


```json
{
  "name": "string",
  "clock": {},
  "group": {},
  "matchImages": [],
  "cache": {},
  "defaultCacheDuration": {},
  "plugin": {},
  "lastCachePurge": {},
  "serviceAccountProvider": null
}
```


*Определено в:* `pkg/credentialprovider/plugin/plugin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*pluginProvider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:196`



---


[function] name: newServiceAccountProvider file: pkg/credentialprovider/plugin/plugin.go:273 returns_error: нет description: —


### newServiceAccountProvider (pkg/credentialprovider/plugin/plugin.go:273)


newServiceAccountProvider is a function that performs operations based on the provided parameters and returns (
	provider kubeletconfig.CredentialProvider,
	getServiceAccount GetServiceAccountFunc,
	getServiceAccountToken getServiceAccountTokenFunc,
).


```go
func newServiceAccountProvider((
	provider kubeletconfig.CredentialProvider,
	getServiceAccount GetServiceAccountFunc,
	getServiceAccountToken getServiceAccountTokenFunc,
)) (
	provider kubeletconfig.CredentialProvider,
	getServiceAccount GetServiceAccountFunc,
	getServiceAccountToken getServiceAccountTokenFunc,
)
```


**Тип ответа:** provider


```json
{
  "name": "string",
  "impl": null
}
```


*Определено в:* `pkg/credentialprovider/plugin/plugins.go`


**Тип ответа:** kubeletconfig.CredentialProvider


```json
{
  "Name": "string",
  "MatchImages": [],
  "DefaultCacheDuration": null,
  "APIVersion": "string",
  "Args": [],
  "Env": [],
  "TokenAttributes": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** getServiceAccount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GetServiceAccountFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** getServiceAccountToken


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** getServiceAccountTokenFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:273`



---


[function] name: parseRegistry file: pkg/credentialprovider/plugin/plugin.go:795 returns_error: нет description: parseRegistry extracts the registry hostname of an image (including port if specified).


### parseRegistry (pkg/credentialprovider/plugin/plugin.go:795)


parseRegistry extracts the registry hostname of an image (including port if specified).


```go
func parseRegistry((image string)) (image string)
```


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:795`



---


[function] name: provide file: pkg/credentialprovider/plugin/plugin.go:429 returns_error: да description: provide returns a credentialprovider.DockerConfig based on the credentials returned
from cache or the exec plugin. The r


### provide (pkg/credentialprovider/plugin/plugin.go:429)


provide returns a credentialprovider.DockerConfig based on the credentials returned
from cache or the exec plugin. The returned ServiceAccountCoordinates may be nil.
If ServiceAccountCoordinates is nil, it means no service account context was used
(e.g., the plugin is not operating in service account token mode or no service account
was provided for the request).


```go
func (p *pluginProvider) provide((credentialprovider.DockerConfig, *credentialprovider.ServiceAccountCoordinates, error)) (credentialprovider.DockerConfig, *credentialprovider.ServiceAccountCoordinates, error)
```


**Тип запроса:** credentialprovider.ServiceAccountCoordinates


```json
{
  "UID": "string",
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Тип ответа:** credentialprovider.DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


**Тип ответа:** credentialprovider.ServiceAccountCoordinates


```json
{
  "UID": "string",
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `credentialprovider.DockerConfig`, `*credentialprovider.ServiceAccountCoordinates`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:429`



---


[function] name: provideWithCoordinates file: pkg/credentialprovider/plugin/plugin.go:408 returns_error: нет description: provideWithCoordinates returns the DockerConfig and, if available, the ServiceAccountCoordinates
used for credential res


### provideWithCoordinates (pkg/credentialprovider/plugin/plugin.go:408)


provideWithCoordinates returns the DockerConfig and, if available, the ServiceAccountCoordinates
used for credential resolution. If ServiceAccountCoordinates is nil, it means no service account
context was used (e.g., the plugin is not operating in service account token mode or no service
account was provided for the request).


```go
func (p *perPodPluginProvider) provideWithCoordinates((credentialprovider.DockerConfig, *credentialprovider.ServiceAccountCoordinates)) (credentialprovider.DockerConfig, *credentialprovider.ServiceAccountCoordinates)
```


**Тип запроса:** credentialprovider.ServiceAccountCoordinates


```json
{
  "UID": "string",
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Тип ответа:** credentialprovider.DockerConfig


```json
{
  "Auths": {},
  "HTTPHeaders": {}
}
```


*Определено в:* `pkg/credentialprovider/config.go`


**Тип ответа:** credentialprovider.ServiceAccountCoordinates


```json
{
  "UID": "string",
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:408`



---


[function] name: runPlugin file: pkg/credentialprovider/plugin/plugin.go:744 returns_error: нет description: —


### runPlugin (pkg/credentialprovider/plugin/plugin.go:744)


runPlugin is a method that performs operations based on the provided parameters and returns (ctx context.Context, cmd *exec.Cmd, image string).


```go
func (e *execPlugin) runPlugin((ctx context.Context, cmd *exec.Cmd, image string)) (ctx context.Context, cmd *exec.Cmd, image string)
```


**Тип запроса:** exec.Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


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


**Тип ответа:** cmd


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** exec.Cmd


```json
{
  "Name": "string",
  "CommandLine": [],
  "AdditionalEnv": {},
  "LogOutput": false,
  "ProcessOutput": {},
  "GatherOutput": false,
  "LogFile": "string",
  "KeepRunning": false,
  "cancel": {},
  "cmd": null,
  "wg": {},
  "running": {},
  "result": {},
  "gathering": false,
  "mutex": {},
  "output": {}
}
```


*Определено в:* `test/utils/localupcluster/cmd.go`


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugin.go:744`




## pkg/credentialprovider/plugin/plugins.go


📄 Исходный файл: `pkg/credentialprovider/plugin/plugins.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Lookup](#lookup-pkgcredentialproviderpluginpluginsgo91) `:91`

- 🔗 [NewExternalCredentialProviderDockerKeyring](#newexternalcredentialproviderdockerkeyring-pkgcredentialproviderpluginpluginsgo62) `:62`

- 🔗 [registerCredentialProviderPlugin](#registercredentialproviderplugin-pkgcredentialproviderpluginpluginsgo45) `:45`


</details>


[function] name: Lookup file: pkg/credentialprovider/plugin/plugins.go:91 returns_error: нет description: —


### Lookup (pkg/credentialprovider/plugin/plugins.go:91)


Lookup is a method that performs operations based on the provided parameters and returns ([]credentialprovider.TrackedAuthConfig, bool).


```go
func (k *externalCredentialProviderKeyring) Lookup(([]credentialprovider.TrackedAuthConfig, bool)) ([]credentialprovider.TrackedAuthConfig, bool)
```


**Тип ответа:** credentialprovider.TrackedAuthConfig


```json
{
  "AuthConfigHash": "string",
  "Source": null
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugins.go:91`



---


[function] name: NewExternalCredentialProviderDockerKeyring file: pkg/credentialprovider/plugin/plugins.go:62 returns_error: нет description: —


### NewExternalCredentialProviderDockerKeyring (pkg/credentialprovider/plugin/plugins.go:62)


NewExternalCredentialProviderDockerKeyring is a function that performs operations based on the provided parameters and returns (podNamespace, podName, podUID, serviceAccountName string).


```go
func NewExternalCredentialProviderDockerKeyring((podNamespace, podName, podUID, serviceAccountName string)) (podNamespace, podName, podUID, serviceAccountName string)
```


**Тип ответа:** podNamespace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podUID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** serviceAccountName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/credentialprovider/plugin/plugins.go:62`



---


[function] name: registerCredentialProviderPlugin file: pkg/credentialprovider/plugin/plugins.go:45 returns_error: нет description: —


### registerCredentialProviderPlugin (pkg/credentialprovider/plugin/plugins.go:45)


registerCredentialProviderPlugin is a function that performs operations based on the provided parameters and returns (name string, p *pluginProvider).


```go
func registerCredentialProviderPlugin((name string, p *pluginProvider)) (name string, p *pluginProvider)
```


**Тип запроса:** pluginProvider


```json
{
  "name": "string",
  "clock": {},
  "group": {},
  "matchImages": [],
  "cache": {},
  "defaultCacheDuration": {},
  "plugin": {},
  "lastCachePurge": {},
  "serviceAccountProvider": null
}
```


*Определено в:* `pkg/credentialprovider/plugin/plugin.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** p


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** pluginProvider


```json
{
  "name": "string",
  "clock": {},
  "group": {},
  "matchImages": [],
  "cache": {},
  "defaultCacheDuration": {},
  "plugin": {},
  "lastCachePurge": {},
  "serviceAccountProvider": null
}
```


*Определено в:* `pkg/credentialprovider/plugin/plugin.go`


📍 *Расположение:* `pkg/credentialprovider/plugin/plugins.go:45`




## pkg/credentialprovider/provider.go


📄 Исходный файл: `pkg/credentialprovider/provider.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Enabled](#enabled-pkgcredentialproviderprovidergo63) `:63`

- 🔗 [Enabled](#enabled-pkgcredentialproviderprovidergo79) `:79`

- 🔗 [NewDefaultDockerKeyring](#newdefaultdockerkeyring-pkgcredentialproviderprovidergo104) `:104`

- 🔗 [Provide](#provide-pkgcredentialproviderprovidergo68) `:68`

- 🔗 [Provide](#provide-pkgcredentialproviderprovidergo84) `:84`


</details>


[function] name: Enabled file: pkg/credentialprovider/provider.go:63 returns_error: нет description: Enabled implements dockerConfigProvider


### Enabled (pkg/credentialprovider/provider.go:63)


Enabled implements dockerConfigProvider


```go
func (d *defaultDockerConfigProvider) Enabled(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/provider.go:63`



---


[function] name: Enabled file: pkg/credentialprovider/provider.go:79 returns_error: нет description: Enabled implements dockerConfigProvider


### Enabled (pkg/credentialprovider/provider.go:79)


Enabled implements dockerConfigProvider


```go
func (d *CachingDockerConfigProvider) Enabled(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/provider.go:79`



---


[function] name: NewDefaultDockerKeyring file: pkg/credentialprovider/provider.go:104 returns_error: нет description: NewDefaultDockerKeyring creates a DockerKeyring to use for resolving credentials,
which returns the default credentials 


### NewDefaultDockerKeyring (pkg/credentialprovider/provider.go:104)


NewDefaultDockerKeyring creates a DockerKeyring to use for resolving credentials,
which returns the default credentials from the .dockercfg file.


```go
func NewDefaultDockerKeyring(()) ()
```


📍 *Расположение:* `pkg/credentialprovider/provider.go:104`



---


[function] name: Provide file: pkg/credentialprovider/provider.go:68 returns_error: нет description: Provide implements dockerConfigProvider


### Provide (pkg/credentialprovider/provider.go:68)


Provide implements dockerConfigProvider


```go
func (d *defaultDockerConfigProvider) Provide((image string)) (image string)
```


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `pkg/credentialprovider/provider.go:68`



---


[function] name: Provide file: pkg/credentialprovider/provider.go:84 returns_error: нет description: Provide implements dockerConfigProvider


### Provide (pkg/credentialprovider/provider.go:84)


Provide implements dockerConfigProvider


```go
func (d *CachingDockerConfigProvider) Provide((image string)) (image string)
```


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `pkg/credentialprovider/provider.go:84`




## pkg/credentialprovider/secrets/secrets.go


📄 Исходный файл: `pkg/credentialprovider/secrets/secrets.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MakeDockerKeyring](#makedockerkeyring-pkgcredentialprovidersecretssecretsgo29) `:29`

- 🔗 [secretsToTrackedDockerConfigs](#secretstotrackeddockerconfigs-pkgcredentialprovidersecretssecretsgo42) `:42`


</details>


[function] name: MakeDockerKeyring file: pkg/credentialprovider/secrets/secrets.go:29 returns_error: да description: MakeDockerKeyring inspects the passedSecrets to see if they contain any DockerConfig secrets.  If they do,
then a Docker


### MakeDockerKeyring (pkg/credentialprovider/secrets/secrets.go:29)


MakeDockerKeyring inspects the passedSecrets to see if they contain any DockerConfig secrets.  If they do,
then a DockerKeyring is built based on every hit and unioned with the defaultKeyring.
If they do not, then the default keyring is returned


```go
func MakeDockerKeyring((credentialprovider.DockerKeyring, error)) (credentialprovider.DockerKeyring, error)
```


**Тип ответа:** credentialprovider.DockerKeyring


```json
{
  "index": [],
  "creds": {}
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `credentialprovider.DockerKeyring`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/secrets/secrets.go:29`



---


[function] name: secretsToTrackedDockerConfigs file: pkg/credentialprovider/secrets/secrets.go:42 returns_error: да description: —


### secretsToTrackedDockerConfigs (pkg/credentialprovider/secrets/secrets.go:42)


secretsToTrackedDockerConfigs is a function that performs operations based on the provided parameters and may return an error.


```go
func secretsToTrackedDockerConfigs((credentialprovider.DockerKeyring, error)) (credentialprovider.DockerKeyring, error)
```


**Тип ответа:** credentialprovider.DockerKeyring


```json
{
  "index": [],
  "creds": {}
}
```


*Определено в:* `pkg/credentialprovider/keyring.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `credentialprovider.DockerKeyring`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/credentialprovider/secrets/secrets.go:42`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_controlplane.md)

- [Следующая директория](pkg_features.md)


---

