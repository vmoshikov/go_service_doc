---
title: "Функции: pkg/proxy"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/proxy
---


# Функции: pkg/proxy


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_probe.md)

- [Следующая директория](pkg_quota.md)


---


## Меню по файлам


- 📄 [pkg/proxy/apis/config/fuzzer/fuzzer.go](#pkgproxyapisconfigfuzzerfuzzergo)

- 📄 [pkg/proxy/apis/config/register.go](#pkgproxyapisconfigregistergo)

- 📄 [pkg/proxy/apis/config/scheme/scheme.go](#pkgproxyapisconfigschemeschemego)

- 📄 [pkg/proxy/apis/config/types.go](#pkgproxyapisconfigtypesgo)

- 📄 [pkg/proxy/apis/config/v1alpha1/conversion.go](#pkgproxyapisconfigv1alpha1conversiongo)

- 📄 [pkg/proxy/apis/config/v1alpha1/defaults.go](#pkgproxyapisconfigv1alpha1defaultsgo)

- 📄 [pkg/proxy/apis/config/v1alpha1/register.go](#pkgproxyapisconfigv1alpha1registergo)

- 📄 [pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go](#pkgproxyapisconfigv1alpha1zz_generatedconversiongo)

- 📄 [pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go](#pkgproxyapisconfigv1alpha1zz_generateddefaultsgo)

- 📄 [pkg/proxy/apis/config/validation/validation.go](#pkgproxyapisconfigvalidationvalidationgo)

- 📄 [pkg/proxy/apis/config/zz_generated.deepcopy.go](#pkgproxyapisconfigzz_generateddeepcopygo)

- 📄 [pkg/proxy/config/config.go](#pkgproxyconfigconfiggo)

- 📄 [pkg/proxy/conntrack/cleanup.go](#pkgproxyconntrackcleanupgo)

- 📄 [pkg/proxy/conntrack/conntrack.go](#pkgproxyconntrackconntrackgo)

- 📄 [pkg/proxy/conntrack/fake.go](#pkgproxyconntrackfakego)

- 📄 [pkg/proxy/conntrack/filter.go](#pkgproxyconntrackfiltergo)

- 📄 [pkg/proxy/conntrack/sysctls.go](#pkgproxyconntracksysctlsgo)

- 📄 [pkg/proxy/endpoint.go](#pkgproxyendpointgo)

- 📄 [pkg/proxy/endpointschangetracker.go](#pkgproxyendpointschangetrackergo)

- 📄 [pkg/proxy/endpointslicecache.go](#pkgproxyendpointslicecachego)

- 📄 [pkg/proxy/healthcheck/common.go](#pkgproxyhealthcheckcommongo)

- 📄 [pkg/proxy/healthcheck/proxy_health.go](#pkgproxyhealthcheckproxy_healthgo)

- 📄 [pkg/proxy/healthcheck/service_health.go](#pkgproxyhealthcheckservice_healthgo)

- 📄 [pkg/proxy/iptables/cleanup.go](#pkgproxyiptablescleanupgo)

- 📄 [pkg/proxy/iptables/proxier.go](#pkgproxyiptablesproxiergo)

- 📄 [pkg/proxy/ipvs/cleanup.go](#pkgproxyipvscleanupgo)

- 📄 [pkg/proxy/ipvs/graceful_termination.go](#pkgproxyipvsgraceful_terminationgo)

- 📄 [pkg/proxy/ipvs/ipset.go](#pkgproxyipvsipsetgo)

- 📄 [pkg/proxy/ipvs/ipset/ipset.go](#pkgproxyipvsipsetipsetgo)

- 📄 [pkg/proxy/ipvs/ipset/testing/fake.go](#pkgproxyipvsipsettestingfakego)

- 📄 [pkg/proxy/ipvs/netlink_linux.go](#pkgproxyipvsnetlink_linuxgo)

- 📄 [pkg/proxy/ipvs/proxier.go](#pkgproxyipvsproxiergo)

- 📄 [pkg/proxy/ipvs/supported.go](#pkgproxyipvssupportedgo)

- 📄 [pkg/proxy/ipvs/testing/fake.go](#pkgproxyipvstestingfakego)

- 📄 [pkg/proxy/ipvs/util/ipvs.go](#pkgproxyipvsutilipvsgo)

- 📄 [pkg/proxy/ipvs/util/ipvs_linux.go](#pkgproxyipvsutilipvs_linuxgo)

- 📄 [pkg/proxy/ipvs/util/testing/fake.go](#pkgproxyipvsutiltestingfakego)

- 📄 [pkg/proxy/kubemark/hollow_proxy.go](#pkgproxykubemarkhollow_proxygo)

- 📄 [pkg/proxy/metaproxier/meta_proxier.go](#pkgproxymetaproxiermeta_proxiergo)

- 📄 [pkg/proxy/metrics/metrics.go](#pkgproxymetricsmetricsgo)

- 📄 [pkg/proxy/nftables/cleanup.go](#pkgproxynftablescleanupgo)

- 📄 [pkg/proxy/nftables/proxier.go](#pkgproxynftablesproxiergo)

- 📄 [pkg/proxy/nftables/supported.go](#pkgproxynftablessupportedgo)

- 📄 [pkg/proxy/node.go](#pkgproxynodego)

- 📄 [pkg/proxy/runner/bounded_frequency_runner.go](#pkgproxyrunnerbounded_frequency_runnergo)

- 📄 [pkg/proxy/servicechangetracker.go](#pkgproxyservicechangetrackergo)

- 📄 [pkg/proxy/serviceport.go](#pkgproxyserviceportgo)

- 📄 [pkg/proxy/topology.go](#pkgproxytopologygo)

- 📄 [pkg/proxy/types.go](#pkgproxytypesgo)

- 📄 [pkg/proxy/util/endpoints.go](#pkgproxyutilendpointsgo)

- 📄 [pkg/proxy/util/linebuffer.go](#pkgproxyutillinebuffergo)

- 📄 [pkg/proxy/util/localdetector.go](#pkgproxyutillocaldetectorgo)

- 📄 [pkg/proxy/util/network.go](#pkgproxyutilnetworkgo)

- 📄 [pkg/proxy/util/nfacct/handler.go](#pkgproxyutilnfaccthandlergo)

- 📄 [pkg/proxy/util/nfacct/nfacct_linux.go](#pkgproxyutilnfacctnfacct_linuxgo)

- 📄 [pkg/proxy/util/nfacct/nfacct_others.go](#pkgproxyutilnfacctnfacct_othersgo)

- 📄 [pkg/proxy/util/nodeport_addresses.go](#pkgproxyutilnodeport_addressesgo)

- 📄 [pkg/proxy/util/testing/fake.go](#pkgproxyutiltestingfakego)

- 📄 [pkg/proxy/util/utils.go](#pkgproxyutilutilsgo)

- 📄 [pkg/proxy/winkernel/hcnutils.go](#pkgproxywinkernelhcnutilsgo)

- 📄 [pkg/proxy/winkernel/hns.go](#pkgproxywinkernelhnsgo)

- 📄 [pkg/proxy/winkernel/proxier.go](#pkgproxywinkernelproxiergo)

- 📄 [pkg/proxy/winkernel/supported.go](#pkgproxywinkernelsupportedgo)

- 📄 [pkg/proxy/winkernel/testing/hcnutils_mock.go](#pkgproxywinkerneltestinghcnutils_mockgo)


---


## pkg/proxy/apis/config/fuzzer/fuzzer.go


📄 Исходный файл: `pkg/proxy/apis/config/fuzzer/fuzzer.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Funcs](#funcs-pkgproxyapisconfigfuzzerfuzzergo82) `:82`

- 🔗 [generateRandomCIDR](#generaterandomcidr-pkgproxyapisconfigfuzzerfuzzergo52) `:52`

- 🔗 [generateRandomIP](#generaterandomip-pkgproxyapisconfigfuzzerfuzzergo33) `:33`

- 🔗 [getRandomDualStackCIDR](#getrandomdualstackcidr-pkgproxyapisconfigfuzzerfuzzergo70) `:70`


</details>


[function] name: Funcs file: pkg/proxy/apis/config/fuzzer/fuzzer.go:82 returns_error: нет description: Funcs returns the fuzzer functions for the kube-proxy apis.


### Funcs (pkg/proxy/apis/config/fuzzer/fuzzer.go:82)


Funcs returns the fuzzer functions for the kube-proxy apis.


```go
func Funcs((codecs runtimeserializer.CodecFactory)) (codecs runtimeserializer.CodecFactory)
```


**Тип ответа:** codecs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** runtimeserializer.CodecFactory


```json
{
  "scheme": null,
  "universal": {},
  "accepts": [],
  "legacySerializer": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/codec_factory.go`


📍 *Расположение:* `pkg/proxy/apis/config/fuzzer/fuzzer.go:82`



---


[function] name: generateRandomCIDR file: pkg/proxy/apis/config/fuzzer/fuzzer.go:52 returns_error: нет description: generateRandomCIDR is copied from pkg/apis/networking/fuzzer/fuzzer.go


### generateRandomCIDR (pkg/proxy/apis/config/fuzzer/fuzzer.go:52)


generateRandomCIDR is copied from pkg/apis/networking/fuzzer/fuzzer.go


```go
func generateRandomCIDR((is6 bool, c randfill.Continue)) (is6 bool, c randfill.Continue)
```


**Тип ответа:** is6


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** randfill.Continue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/apis/config/fuzzer/fuzzer.go:52`



---


[function] name: generateRandomIP file: pkg/proxy/apis/config/fuzzer/fuzzer.go:33 returns_error: нет description: generateRandomIP is copied from pkg/apis/networking/fuzzer/fuzzer.go


### generateRandomIP (pkg/proxy/apis/config/fuzzer/fuzzer.go:33)


generateRandomIP is copied from pkg/apis/networking/fuzzer/fuzzer.go


```go
func generateRandomIP((is6 bool, c randfill.Continue)) (is6 bool, c randfill.Continue)
```


**Тип ответа:** is6


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** randfill.Continue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/apis/config/fuzzer/fuzzer.go:33`



---


[function] name: getRandomDualStackCIDR file: pkg/proxy/apis/config/fuzzer/fuzzer.go:70 returns_error: нет description: getRandomDualStackCIDR returns a random dual-stack CIDR.


### getRandomDualStackCIDR (pkg/proxy/apis/config/fuzzer/fuzzer.go:70)


getRandomDualStackCIDR returns a random dual-stack CIDR.


```go
func getRandomDualStackCIDR((c randfill.Continue)) (c randfill.Continue)
```


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


**Тип ответа:** randfill.Continue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/apis/config/fuzzer/fuzzer.go:70`




## pkg/proxy/apis/config/register.go


📄 Исходный файл: `pkg/proxy/apis/config/register.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [addKnownTypes](#addknowntypes-pkgproxyapisconfigregistergo38) `:38`


</details>


[function] name: addKnownTypes file: pkg/proxy/apis/config/register.go:38 returns_error: нет description: addKnownTypes registers known types to the given scheme


### addKnownTypes (pkg/proxy/apis/config/register.go:38)


addKnownTypes registers known types to the given scheme


```go
func addKnownTypes((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `pkg/proxy/apis/config/register.go:38`




## pkg/proxy/apis/config/scheme/scheme.go


📄 Исходный файл: `pkg/proxy/apis/config/scheme/scheme.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [AddToScheme](#addtoscheme-pkgproxyapisconfigschemeschemego40) `:40`

- 🔗 [init](#init-pkgproxyapisconfigschemeschemego35) `:35`


</details>


[function] name: AddToScheme file: pkg/proxy/apis/config/scheme/scheme.go:40 returns_error: нет description: AddToScheme adds the types of this group into the given scheme.


### AddToScheme (pkg/proxy/apis/config/scheme/scheme.go:40)


AddToScheme adds the types of this group into the given scheme.


```go
func AddToScheme((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `pkg/proxy/apis/config/scheme/scheme.go:40`



---


[function] name: init file: pkg/proxy/apis/config/scheme/scheme.go:35 returns_error: нет description: —


### init (pkg/proxy/apis/config/scheme/scheme.go:35)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/scheme/scheme.go:35`




## pkg/proxy/apis/config/types.go


📄 Исходный файл: `pkg/proxy/apis/config/types.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Set](#set-pkgproxyapisconfigtypesgo259) `:259`

- 🔗 [Set](#set-pkgproxyapisconfigtypesgo286) `:286`

- 🔗 [String](#string-pkgproxyapisconfigtypesgo264) `:264`

- 🔗 [String](#string-pkgproxyapisconfigtypesgo291) `:291`

- 🔗 [Type](#type-pkgproxyapisconfigtypesgo271) `:271`

- 🔗 [Type](#type-pkgproxyapisconfigtypesgo298) `:298`


</details>


[function] name: Set file: pkg/proxy/apis/config/types.go:259 returns_error: нет description: —


### Set (pkg/proxy/apis/config/types.go:259)


Set is a method that updates data based on the provided parameters and returns (s string).


```go
func (m *ProxyMode) Set((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/proxy/apis/config/types.go:259`



---


[function] name: Set file: pkg/proxy/apis/config/types.go:286 returns_error: нет description: —


### Set (pkg/proxy/apis/config/types.go:286)


Set is a method that updates data based on the provided parameters and returns (s string).


```go
func (m *LocalMode) Set((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/proxy/apis/config/types.go:286`



---


[function] name: String file: pkg/proxy/apis/config/types.go:264 returns_error: нет description: —


### String (pkg/proxy/apis/config/types.go:264)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (m *ProxyMode) String(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/types.go:264`



---


[function] name: String file: pkg/proxy/apis/config/types.go:291 returns_error: нет description: —


### String (pkg/proxy/apis/config/types.go:291)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (m *LocalMode) String(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/types.go:291`



---


[function] name: Type file: pkg/proxy/apis/config/types.go:271 returns_error: нет description: —


### Type (pkg/proxy/apis/config/types.go:271)


Type is a method that performs operations based on the provided parameters and returns ().


```go
func (m *ProxyMode) Type(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/types.go:271`



---


[function] name: Type file: pkg/proxy/apis/config/types.go:298 returns_error: нет description: —


### Type (pkg/proxy/apis/config/types.go:298)


Type is a method that performs operations based on the provided parameters and returns ().


```go
func (m *LocalMode) Type(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/types.go:298`




## pkg/proxy/apis/config/v1alpha1/conversion.go


📄 Исходный файл: `pkg/proxy/apis/config/v1alpha1/conversion.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Convert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration](#convert_config_detectlocalconfiguration_to_v1alpha1_detectlocalconfiguration-pkgproxyapisconfigv1alpha1conversiongo109) `:109`

- 🔗 [Convert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration](#convert_config_kubeproxyconfiguration_to_v1alpha1_kubeproxyconfiguration-pkgproxyapisconfigv1alpha1conversiongo28) `:28`

- 🔗 [Convert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration](#convert_v1alpha1_kubeproxyconfiguration_to_config_kubeproxyconfiguration-pkgproxyapisconfigv1alpha1conversiongo61) `:61`

- 🔗 [Convert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration](#convert_v1alpha1_kubeproxyiptablesconfiguration_to_config_kubeproxyiptablesconfiguration-pkgproxyapisconfigv1alpha1conversiongo94) `:94`

- 🔗 [Convert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration](#convert_v1alpha1_kubeproxyipvsconfiguration_to_config_kubeproxyipvsconfiguration-pkgproxyapisconfigv1alpha1conversiongo99) `:99`

- 🔗 [Convert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration](#convert_v1alpha1_kubeproxynftablesconfiguration_to_config_kubeproxynftablesconfiguration-pkgproxyapisconfigv1alpha1conversiongo104) `:104`


</details>


[function] name: Convert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration file: pkg/proxy/apis/config/v1alpha1/conversion.go:109 returns_error: нет description: Convert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration is defined here, because public conversion 


### Convert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration (pkg/proxy/apis/config/v1alpha1/conversion.go:109)


Convert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration is defined here, because public conversion is not auto-generated due to existing warnings.


```go
func Convert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration((in *config.DetectLocalConfiguration, out *v1alpha1.DetectLocalConfiguration, s conversion.Scope)) (in *config.DetectLocalConfiguration, out *v1alpha1.DetectLocalConfiguration, s conversion.Scope)
```


**Тип запроса:** config.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** v1alpha1.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** v1alpha1.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/conversion.go:109`



---


[function] name: Convert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration file: pkg/proxy/apis/config/v1alpha1/conversion.go:28 returns_error: нет description: Convert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration is defined here, because public conversion is n


### Convert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration (pkg/proxy/apis/config/v1alpha1/conversion.go:28)


Convert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration is defined here, because public conversion is not auto-generated due to existing warnings.


```go
func Convert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration((in *config.KubeProxyConfiguration, out *v1alpha1.KubeProxyConfiguration, scope conversion.Scope)) (in *config.KubeProxyConfiguration, out *v1alpha1.KubeProxyConfiguration, scope conversion.Scope)
```


**Тип запроса:** config.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** v1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** v1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** scope


```json
{
  "mutex": {},
  "name": "string",
  "podTopologyHints": {},
  "hintProviders": [],
  "policy": {},
  "podMap": {}
}
```


*Определено в:* `pkg/kubelet/cm/topologymanager/scope.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/conversion.go:28`



---


[function] name: Convert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration file: pkg/proxy/apis/config/v1alpha1/conversion.go:61 returns_error: нет description: Convert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration is defined here, because public conversion is n


### Convert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration (pkg/proxy/apis/config/v1alpha1/conversion.go:61)


Convert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration is defined here, because public conversion is not auto-generated due to existing warnings.


```go
func Convert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration((in *v1alpha1.KubeProxyConfiguration, out *config.KubeProxyConfiguration, scope conversion.Scope)) (in *v1alpha1.KubeProxyConfiguration, out *config.KubeProxyConfiguration, scope conversion.Scope)
```


**Тип запроса:** v1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** v1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** scope


```json
{
  "mutex": {},
  "name": "string",
  "podTopologyHints": {},
  "hintProviders": [],
  "policy": {},
  "podMap": {}
}
```


*Определено в:* `pkg/kubelet/cm/topologymanager/scope.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/conversion.go:61`



---


[function] name: Convert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration file: pkg/proxy/apis/config/v1alpha1/conversion.go:94 returns_error: нет description: Convert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration is defined here, because public


### Convert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration (pkg/proxy/apis/config/v1alpha1/conversion.go:94)


Convert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration is defined here, because public conversion is not auto-generated due to existing warnings.


```go
func Convert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration((in *v1alpha1.KubeProxyIPTablesConfiguration, out *config.KubeProxyIPTablesConfiguration, scope conversion.Scope)) (in *v1alpha1.KubeProxyIPTablesConfiguration, out *config.KubeProxyIPTablesConfiguration, scope conversion.Scope)
```


**Тип запроса:** v1alpha1.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** v1alpha1.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** scope


```json
{
  "mutex": {},
  "name": "string",
  "podTopologyHints": {},
  "hintProviders": [],
  "policy": {},
  "podMap": {}
}
```


*Определено в:* `pkg/kubelet/cm/topologymanager/scope.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/conversion.go:94`



---


[function] name: Convert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration file: pkg/proxy/apis/config/v1alpha1/conversion.go:99 returns_error: нет description: Convert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration is defined here, because public convers


### Convert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration (pkg/proxy/apis/config/v1alpha1/conversion.go:99)


Convert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration is defined here, because public conversion is not auto-generated due to existing warnings.


```go
func Convert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration((in *v1alpha1.KubeProxyIPVSConfiguration, out *config.KubeProxyIPVSConfiguration, scope conversion.Scope)) (in *v1alpha1.KubeProxyIPVSConfiguration, out *config.KubeProxyIPVSConfiguration, scope conversion.Scope)
```


**Тип запроса:** v1alpha1.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** v1alpha1.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** scope


```json
{
  "mutex": {},
  "name": "string",
  "podTopologyHints": {},
  "hintProviders": [],
  "policy": {},
  "podMap": {}
}
```


*Определено в:* `pkg/kubelet/cm/topologymanager/scope.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/conversion.go:99`



---


[function] name: Convert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration file: pkg/proxy/apis/config/v1alpha1/conversion.go:104 returns_error: нет description: Convert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration is defined here, because public


### Convert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration (pkg/proxy/apis/config/v1alpha1/conversion.go:104)


Convert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration is defined here, because public conversion is not auto-generated due to existing warnings.


```go
func Convert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration((in *v1alpha1.KubeProxyNFTablesConfiguration, out *config.KubeProxyNFTablesConfiguration, scope conversion.Scope)) (in *v1alpha1.KubeProxyNFTablesConfiguration, out *config.KubeProxyNFTablesConfiguration, scope conversion.Scope)
```


**Тип запроса:** v1alpha1.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** v1alpha1.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** scope


```json
{
  "mutex": {},
  "name": "string",
  "podTopologyHints": {},
  "hintProviders": [],
  "policy": {},
  "podMap": {}
}
```


*Определено в:* `pkg/kubelet/cm/topologymanager/scope.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/conversion.go:104`




## pkg/proxy/apis/config/v1alpha1/defaults.go


📄 Исходный файл: `pkg/proxy/apis/config/v1alpha1/defaults.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [SetDefaults_KubeProxyConfiguration](#setdefaults_kubeproxyconfiguration-pkgproxyapisconfigv1alpha1defaultsgo39) `:39`

- 🔗 [addDefaultingFuncs](#adddefaultingfuncs-pkgproxyapisconfigv1alpha1defaultsgo35) `:35`

- 🔗 [getDefaultAddresses](#getdefaultaddresses-pkgproxyapisconfigv1alpha1defaultsgo145) `:145`


</details>


[function] name: SetDefaults_KubeProxyConfiguration file: pkg/proxy/apis/config/v1alpha1/defaults.go:39 returns_error: нет description: —


### SetDefaults_KubeProxyConfiguration (pkg/proxy/apis/config/v1alpha1/defaults.go:39)


SetDefaults_KubeProxyConfiguration is a function that updates data based on the provided parameters and returns (obj *kubeproxyconfigv1alpha1.KubeProxyConfiguration).


```go
func SetDefaults_KubeProxyConfiguration((obj *kubeproxyconfigv1alpha1.KubeProxyConfiguration)) (obj *kubeproxyconfigv1alpha1.KubeProxyConfiguration)
```


**Тип запроса:** kubeproxyconfigv1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** kubeproxyconfigv1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/defaults.go:39`



---


[function] name: addDefaultingFuncs file: pkg/proxy/apis/config/v1alpha1/defaults.go:35 returns_error: нет description: —


### addDefaultingFuncs (pkg/proxy/apis/config/v1alpha1/defaults.go:35)


addDefaultingFuncs is a function that performs operations based on the provided parameters and returns (scheme *kruntime.Scheme).


```go
func addDefaultingFuncs((scheme *kruntime.Scheme)) (scheme *kruntime.Scheme)
```


**Тип запроса:** kruntime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** kruntime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/defaults.go:35`



---


[function] name: getDefaultAddresses file: pkg/proxy/apis/config/v1alpha1/defaults.go:145 returns_error: нет description: getDefaultAddresses returns default address of healthz and metrics server
based on the given bind address. IPv6 addresse


### getDefaultAddresses (pkg/proxy/apis/config/v1alpha1/defaults.go:145)


getDefaultAddresses returns default address of healthz and metrics server
based on the given bind address. IPv6 addresses are enclosed in square
brackets for appending port.


```go
func getDefaultAddresses((defaultHealthzAddress, defaultMetricsAddress string)) (defaultHealthzAddress, defaultMetricsAddress string)
```


**Тип ответа:** defaultHealthzAddress


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** defaultMetricsAddress


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/defaults.go:145`




## pkg/proxy/apis/config/v1alpha1/register.go


📄 Исходный файл: `pkg/proxy/apis/config/v1alpha1/register.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-pkgproxyapisconfigv1alpha1registergo38) `:38`


</details>


[function] name: init file: pkg/proxy/apis/config/v1alpha1/register.go:38 returns_error: нет description: —


### init (pkg/proxy/apis/config/v1alpha1/register.go:38)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/register.go:38`




## pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go


📄 Исходный файл: `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go`


<details open>
<summary><b>Функции в этом файле (24)</b></summary>


- 🔗 [Convert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration](#convert_config_kubeproxyconntrackconfiguration_to_v1alpha1_kubeproxyconntrackconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo240) `:240`

- 🔗 [Convert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration](#convert_config_kubeproxyiptablesconfiguration_to_v1alpha1_kubeproxyiptablesconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo260) `:260`

- 🔗 [Convert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration](#convert_config_kubeproxyipvsconfiguration_to_v1alpha1_kubeproxyipvsconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo287) `:287`

- 🔗 [Convert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration](#convert_config_kubeproxynftablesconfiguration_to_v1alpha1_kubeproxynftablesconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo305) `:305`

- 🔗 [Convert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration](#convert_config_kubeproxywinkernelconfiguration_to_v1alpha1_kubeproxywinkernelconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo333) `:333`

- 🔗 [Convert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration](#convert_v1alpha1_detectlocalconfiguration_to_config_detectlocalconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo122) `:122`

- 🔗 [Convert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration](#convert_v1alpha1_kubeproxyconntrackconfiguration_to_config_kubeproxyconntrackconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo224) `:224`

- 🔗 [Convert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration](#convert_v1alpha1_kubeproxywinkernelconfiguration_to_config_kubeproxywinkernelconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo319) `:319`

- 🔗 [RegisterConversions](#registerconversions-pkgproxyapisconfigv1alpha1zz_generatedconversiongo41) `:41`

- 🔗 [autoConvert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration](#autoconvert_config_detectlocalconfiguration_to_v1alpha1_detectlocalconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo126) `:126`

- 🔗 [autoConvert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration](#autoconvert_config_kubeproxyconfiguration_to_v1alpha1_kubeproxyconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo173) `:173`

- 🔗 [autoConvert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration](#autoconvert_config_kubeproxyconntrackconfiguration_to_v1alpha1_kubeproxyconntrackconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo228) `:228`

- 🔗 [autoConvert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration](#autoconvert_config_kubeproxyiptablesconfiguration_to_v1alpha1_kubeproxyiptablesconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo253) `:253`

- 🔗 [autoConvert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration](#autoconvert_config_kubeproxyipvsconfiguration_to_v1alpha1_kubeproxyipvsconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo276) `:276`

- 🔗 [autoConvert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration](#autoconvert_config_kubeproxynftablesconfiguration_to_v1alpha1_kubeproxynftablesconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo299) `:299`

- 🔗 [autoConvert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration](#autoconvert_config_kubeproxywinkernelconfiguration_to_v1alpha1_kubeproxywinkernelconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo323) `:323`

- 🔗 [autoConvert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration](#autoconvert_v1alpha1_detectlocalconfiguration_to_config_detectlocalconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo115) `:115`

- 🔗 [autoConvert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration](#autoconvert_v1alpha1_kubeproxyconfiguration_to_config_kubeproxyconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo133) `:133`

- 🔗 [autoConvert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration](#autoconvert_v1alpha1_kubeproxyconntrackconfiguration_to_config_kubeproxyconntrackconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo212) `:212`

- 🔗 [autoConvert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration](#autoconvert_v1alpha1_kubeproxyiptablesconfiguration_to_config_kubeproxyiptablesconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo244) `:244`

- 🔗 [autoConvert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration](#autoconvert_v1alpha1_kubeproxyipvsconfiguration_to_config_kubeproxyipvsconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo264) `:264`

- 🔗 [autoConvert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration](#autoconvert_v1alpha1_kubeproxynftablesconfiguration_to_config_kubeproxynftablesconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo291) `:291`

- 🔗 [autoConvert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration](#autoconvert_v1alpha1_kubeproxywinkernelconfiguration_to_config_kubeproxywinkernelconfiguration-pkgproxyapisconfigv1alpha1zz_generatedconversiongo309) `:309`

- 🔗 [init](#init-pkgproxyapisconfigv1alpha1zz_generatedconversiongo35) `:35`


</details>


[function] name: Convert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:240 returns_error: нет description: Convert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration is an autogenerated conversio


### Convert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:240)


Convert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration is an autogenerated conversion function.


```go
func Convert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration((in *config.KubeProxyConntrackConfiguration, out *configv1alpha1.KubeProxyConntrackConfiguration, s conversion.Scope)) (in *config.KubeProxyConntrackConfiguration, out *configv1alpha1.KubeProxyConntrackConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:240`



---


[function] name: Convert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:260 returns_error: нет description: Convert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration is an autogenerated conversion 


### Convert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:260)


Convert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration is an autogenerated conversion function.


```go
func Convert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration((in *config.KubeProxyIPTablesConfiguration, out *configv1alpha1.KubeProxyIPTablesConfiguration, s conversion.Scope)) (in *config.KubeProxyIPTablesConfiguration, out *configv1alpha1.KubeProxyIPTablesConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:260`



---


[function] name: Convert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:287 returns_error: нет description: Convert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration is an autogenerated conversion function


### Convert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:287)


Convert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration is an autogenerated conversion function.


```go
func Convert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration((in *config.KubeProxyIPVSConfiguration, out *configv1alpha1.KubeProxyIPVSConfiguration, s conversion.Scope)) (in *config.KubeProxyIPVSConfiguration, out *configv1alpha1.KubeProxyIPVSConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:287`



---


[function] name: Convert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:305 returns_error: нет description: Convert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration is an autogenerated conversion 


### Convert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:305)


Convert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration is an autogenerated conversion function.


```go
func Convert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration((in *config.KubeProxyNFTablesConfiguration, out *configv1alpha1.KubeProxyNFTablesConfiguration, s conversion.Scope)) (in *config.KubeProxyNFTablesConfiguration, out *configv1alpha1.KubeProxyNFTablesConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:305`



---


[function] name: Convert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:333 returns_error: нет description: Convert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration is an autogenerated conversio


### Convert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:333)


Convert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration is an autogenerated conversion function.


```go
func Convert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration((in *config.KubeProxyWinkernelConfiguration, out *configv1alpha1.KubeProxyWinkernelConfiguration, s conversion.Scope)) (in *config.KubeProxyWinkernelConfiguration, out *configv1alpha1.KubeProxyWinkernelConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:333`



---


[function] name: Convert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:122 returns_error: нет description: Convert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration is an autogenerated conversion function.


### Convert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:122)


Convert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration is an autogenerated conversion function.


```go
func Convert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration((in *configv1alpha1.DetectLocalConfiguration, out *config.DetectLocalConfiguration, s conversion.Scope)) (in *configv1alpha1.DetectLocalConfiguration, out *config.DetectLocalConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:122`



---


[function] name: Convert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:224 returns_error: нет description: Convert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration is an autogenerated conversio


### Convert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:224)


Convert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration is an autogenerated conversion function.


```go
func Convert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration((in *configv1alpha1.KubeProxyConntrackConfiguration, out *config.KubeProxyConntrackConfiguration, s conversion.Scope)) (in *configv1alpha1.KubeProxyConntrackConfiguration, out *config.KubeProxyConntrackConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:224`



---


[function] name: Convert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:319 returns_error: нет description: Convert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration is an autogenerated conversio


### Convert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:319)


Convert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration is an autogenerated conversion function.


```go
func Convert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration((in *configv1alpha1.KubeProxyWinkernelConfiguration, out *config.KubeProxyWinkernelConfiguration, s conversion.Scope)) (in *configv1alpha1.KubeProxyWinkernelConfiguration, out *config.KubeProxyWinkernelConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:319`



---


[function] name: RegisterConversions file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:41 returns_error: нет description: RegisterConversions adds conversion functions to the given scheme.
Public to allow building arbitrary schemes.


### RegisterConversions (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:41)


RegisterConversions adds conversion functions to the given scheme.
Public to allow building arbitrary schemes.


```go
func RegisterConversions((s *runtime.Scheme)) (s *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:41`



---


[function] name: autoConvert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:126 returns_error: нет description: —


### autoConvert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:126)


autoConvert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration is a function that performs operations based on the provided parameters and returns (in *config.DetectLocalConfiguration, out *configv1alpha1.DetectLocalConfiguration, s conversion.Scope).


```go
func autoConvert_config_DetectLocalConfiguration_To_v1alpha1_DetectLocalConfiguration((in *config.DetectLocalConfiguration, out *configv1alpha1.DetectLocalConfiguration, s conversion.Scope)) (in *config.DetectLocalConfiguration, out *configv1alpha1.DetectLocalConfiguration, s conversion.Scope)
```


**Тип запроса:** config.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:126`



---


[function] name: autoConvert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:173 returns_error: нет description: —


### autoConvert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:173)


autoConvert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration is a function that performs operations based on the provided parameters and returns (in *config.KubeProxyConfiguration, out *configv1alpha1.KubeProxyConfiguration, s conversion.Scope).


```go
func autoConvert_config_KubeProxyConfiguration_To_v1alpha1_KubeProxyConfiguration((in *config.KubeProxyConfiguration, out *configv1alpha1.KubeProxyConfiguration, s conversion.Scope)) (in *config.KubeProxyConfiguration, out *configv1alpha1.KubeProxyConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:173`



---


[function] name: autoConvert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:228 returns_error: нет description: —


### autoConvert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:228)


autoConvert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration is a function that performs operations based on the provided parameters and returns (in *config.KubeProxyConntrackConfiguration, out *configv1alpha1.KubeProxyConntrackConfiguration, s conversion.Scope).


```go
func autoConvert_config_KubeProxyConntrackConfiguration_To_v1alpha1_KubeProxyConntrackConfiguration((in *config.KubeProxyConntrackConfiguration, out *configv1alpha1.KubeProxyConntrackConfiguration, s conversion.Scope)) (in *config.KubeProxyConntrackConfiguration, out *configv1alpha1.KubeProxyConntrackConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:228`



---


[function] name: autoConvert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:253 returns_error: нет description: —


### autoConvert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:253)


autoConvert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration is a function that performs operations based on the provided parameters and returns (in *config.KubeProxyIPTablesConfiguration, out *configv1alpha1.KubeProxyIPTablesConfiguration, s conversion.Scope).


```go
func autoConvert_config_KubeProxyIPTablesConfiguration_To_v1alpha1_KubeProxyIPTablesConfiguration((in *config.KubeProxyIPTablesConfiguration, out *configv1alpha1.KubeProxyIPTablesConfiguration, s conversion.Scope)) (in *config.KubeProxyIPTablesConfiguration, out *configv1alpha1.KubeProxyIPTablesConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:253`



---


[function] name: autoConvert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:276 returns_error: нет description: —


### autoConvert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:276)


autoConvert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration is a function that performs operations based on the provided parameters and returns (in *config.KubeProxyIPVSConfiguration, out *configv1alpha1.KubeProxyIPVSConfiguration, s conversion.Scope).


```go
func autoConvert_config_KubeProxyIPVSConfiguration_To_v1alpha1_KubeProxyIPVSConfiguration((in *config.KubeProxyIPVSConfiguration, out *configv1alpha1.KubeProxyIPVSConfiguration, s conversion.Scope)) (in *config.KubeProxyIPVSConfiguration, out *configv1alpha1.KubeProxyIPVSConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:276`



---


[function] name: autoConvert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:299 returns_error: нет description: —


### autoConvert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:299)


autoConvert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration is a function that performs operations based on the provided parameters and returns (in *config.KubeProxyNFTablesConfiguration, out *configv1alpha1.KubeProxyNFTablesConfiguration, s conversion.Scope).


```go
func autoConvert_config_KubeProxyNFTablesConfiguration_To_v1alpha1_KubeProxyNFTablesConfiguration((in *config.KubeProxyNFTablesConfiguration, out *configv1alpha1.KubeProxyNFTablesConfiguration, s conversion.Scope)) (in *config.KubeProxyNFTablesConfiguration, out *configv1alpha1.KubeProxyNFTablesConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:299`



---


[function] name: autoConvert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:323 returns_error: нет description: —


### autoConvert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:323)


autoConvert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration is a function that performs operations based on the provided parameters and returns (in *config.KubeProxyWinkernelConfiguration, out *configv1alpha1.KubeProxyWinkernelConfiguration, s conversion.Scope).


```go
func autoConvert_config_KubeProxyWinkernelConfiguration_To_v1alpha1_KubeProxyWinkernelConfiguration((in *config.KubeProxyWinkernelConfiguration, out *configv1alpha1.KubeProxyWinkernelConfiguration, s conversion.Scope)) (in *config.KubeProxyWinkernelConfiguration, out *configv1alpha1.KubeProxyWinkernelConfiguration, s conversion.Scope)
```


**Тип запроса:** config.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** configv1alpha1.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** config.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** configv1alpha1.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:323`



---


[function] name: autoConvert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:115 returns_error: нет description: —


### autoConvert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:115)


autoConvert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration is a function that performs operations based on the provided parameters and returns (in *configv1alpha1.DetectLocalConfiguration, out *config.DetectLocalConfiguration, s conversion.Scope).


```go
func autoConvert_v1alpha1_DetectLocalConfiguration_To_config_DetectLocalConfiguration((in *configv1alpha1.DetectLocalConfiguration, out *config.DetectLocalConfiguration, s conversion.Scope)) (in *configv1alpha1.DetectLocalConfiguration, out *config.DetectLocalConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:115`



---


[function] name: autoConvert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:133 returns_error: нет description: —


### autoConvert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:133)


autoConvert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration is a function that performs operations based on the provided parameters and returns (in *configv1alpha1.KubeProxyConfiguration, out *config.KubeProxyConfiguration, s conversion.Scope).


```go
func autoConvert_v1alpha1_KubeProxyConfiguration_To_config_KubeProxyConfiguration((in *configv1alpha1.KubeProxyConfiguration, out *config.KubeProxyConfiguration, s conversion.Scope)) (in *configv1alpha1.KubeProxyConfiguration, out *config.KubeProxyConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:133`



---


[function] name: autoConvert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:212 returns_error: нет description: —


### autoConvert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:212)


autoConvert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration is a function that performs operations based on the provided parameters and returns (in *configv1alpha1.KubeProxyConntrackConfiguration, out *config.KubeProxyConntrackConfiguration, s conversion.Scope).


```go
func autoConvert_v1alpha1_KubeProxyConntrackConfiguration_To_config_KubeProxyConntrackConfiguration((in *configv1alpha1.KubeProxyConntrackConfiguration, out *config.KubeProxyConntrackConfiguration, s conversion.Scope)) (in *configv1alpha1.KubeProxyConntrackConfiguration, out *config.KubeProxyConntrackConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:212`



---


[function] name: autoConvert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:244 returns_error: нет description: —


### autoConvert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:244)


autoConvert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration is a function that performs operations based on the provided parameters and returns (in *configv1alpha1.KubeProxyIPTablesConfiguration, out *config.KubeProxyIPTablesConfiguration, s conversion.Scope).


```go
func autoConvert_v1alpha1_KubeProxyIPTablesConfiguration_To_config_KubeProxyIPTablesConfiguration((in *configv1alpha1.KubeProxyIPTablesConfiguration, out *config.KubeProxyIPTablesConfiguration, s conversion.Scope)) (in *configv1alpha1.KubeProxyIPTablesConfiguration, out *config.KubeProxyIPTablesConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:244`



---


[function] name: autoConvert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:264 returns_error: нет description: —


### autoConvert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:264)


autoConvert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration is a function that performs operations based on the provided parameters and returns (in *configv1alpha1.KubeProxyIPVSConfiguration, out *config.KubeProxyIPVSConfiguration, s conversion.Scope).


```go
func autoConvert_v1alpha1_KubeProxyIPVSConfiguration_To_config_KubeProxyIPVSConfiguration((in *configv1alpha1.KubeProxyIPVSConfiguration, out *config.KubeProxyIPVSConfiguration, s conversion.Scope)) (in *configv1alpha1.KubeProxyIPVSConfiguration, out *config.KubeProxyIPVSConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:264`



---


[function] name: autoConvert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:291 returns_error: нет description: —


### autoConvert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:291)


autoConvert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration is a function that performs operations based on the provided parameters and returns (in *configv1alpha1.KubeProxyNFTablesConfiguration, out *config.KubeProxyNFTablesConfiguration, s conversion.Scope).


```go
func autoConvert_v1alpha1_KubeProxyNFTablesConfiguration_To_config_KubeProxyNFTablesConfiguration((in *configv1alpha1.KubeProxyNFTablesConfiguration, out *config.KubeProxyNFTablesConfiguration, s conversion.Scope)) (in *configv1alpha1.KubeProxyNFTablesConfiguration, out *config.KubeProxyNFTablesConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:291`



---


[function] name: autoConvert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:309 returns_error: нет description: —


### autoConvert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:309)


autoConvert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration is a function that performs operations based on the provided parameters and returns (in *configv1alpha1.KubeProxyWinkernelConfiguration, out *config.KubeProxyWinkernelConfiguration, s conversion.Scope).


```go
func autoConvert_v1alpha1_KubeProxyWinkernelConfiguration_To_config_KubeProxyWinkernelConfiguration((in *configv1alpha1.KubeProxyWinkernelConfiguration, out *config.KubeProxyWinkernelConfiguration, s conversion.Scope)) (in *configv1alpha1.KubeProxyWinkernelConfiguration, out *config.KubeProxyWinkernelConfiguration, s conversion.Scope)
```


**Тип запроса:** configv1alpha1.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип запроса:** config.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** config.KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** conversion.Scope


```json
{
  "client": null
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/versioned_client.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:309`



---


[function] name: init file: pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:35 returns_error: нет description: —


### init (pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:35)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.conversion.go:35`




## pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go


📄 Исходный файл: `pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [RegisterDefaults](#registerdefaults-pkgproxyapisconfigv1alpha1zz_generateddefaultsgo32) `:32`

- 🔗 [SetObjectDefaults_KubeProxyConfiguration](#setobjectdefaults_kubeproxyconfiguration-pkgproxyapisconfigv1alpha1zz_generateddefaultsgo39) `:39`


</details>


[function] name: RegisterDefaults file: pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go:32 returns_error: нет description: RegisterDefaults adds defaulters functions to the given scheme.
Public to allow building arbitrary schemes.
All generate


### RegisterDefaults (pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go:32)


RegisterDefaults adds defaulters functions to the given scheme.
Public to allow building arbitrary schemes.
All generated defaulters are covering - they call all nested defaulters.


```go
func RegisterDefaults((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
```


**Тип запроса:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


**Тип ответа:** scheme


```json
{
  "scheme": null,
  "parser": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/runtimetypeconverter.go`


**Тип ответа:** runtime.Scheme


```json
{
  "gvkToType": {},
  "typeToGVK": {},
  "unversionedTypes": {},
  "unversionedKinds": {},
  "fieldLabelConversionFuncs": {},
  "defaulterFuncs": {},
  "validationFuncs": {},
  "converter": null,
  "versionPriority": {},
  "observedVersions": [],
  "schemeName": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go:32`



---


[function] name: SetObjectDefaults_KubeProxyConfiguration file: pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go:39 returns_error: нет description: —


### SetObjectDefaults_KubeProxyConfiguration (pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go:39)


SetObjectDefaults_KubeProxyConfiguration is a function that updates data based on the provided parameters and returns (in *configv1alpha1.KubeProxyConfiguration).


```go
func SetObjectDefaults_KubeProxyConfiguration((in *configv1alpha1.KubeProxyConfiguration)) (in *configv1alpha1.KubeProxyConfiguration)
```


**Тип запроса:** configv1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


**Тип ответа:** configv1alpha1.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/v1alpha1/zz_generated.defaults.go:39`




## pkg/proxy/apis/config/validation/validation.go


📄 Исходный файл: `pkg/proxy/apis/config/validation/validation.go`


<details open>
<summary><b>Функции в этом файле (19)</b></summary>


- 🔗 [Validate](#validate-pkgproxyapisconfigvalidationvalidationgo38) `:38`

- 🔗 [validateClientConnectionConfiguration](#validateclientconnectionconfiguration-pkgproxyapisconfigvalidationvalidationgo215) `:215`

- 🔗 [validateDetectLocalConfiguration](#validatedetectlocalconfiguration-pkgproxyapisconfigvalidationvalidationgo332) `:332`

- 🔗 [validateDetectLocalMode](#validatedetectlocalmode-pkgproxyapisconfigvalidationvalidationgo199) `:199`

- 🔗 [validateDualStackCIDRStrings](#validatedualstackcidrstrings-pkgproxyapisconfigvalidationvalidationgo309) `:309`

- 🔗 [validateHostPort](#validatehostport-pkgproxyapisconfigvalidationvalidationgo221) `:221`

- 🔗 [validateIPVSExcludeCIDRs](#validateipvsexcludecidrs-pkgproxyapisconfigvalidationvalidationgo280) `:280`

- 🔗 [validateIPVSTimeout](#validateipvstimeout-pkgproxyapisconfigvalidationvalidationgo262) `:262`

- 🔗 [validateInterface](#validateinterface-pkgproxyapisconfigvalidationvalidationgo301) `:301`

- 🔗 [validateKubeProxyConntrackConfiguration](#validatekubeproxyconntrackconfiguration-pkgproxyapisconfigvalidationvalidationgo131) `:131`

- 🔗 [validateKubeProxyIPTablesConfiguration](#validatekubeproxyiptablesconfiguration-pkgproxyapisconfigvalidationvalidationgo91) `:91`

- 🔗 [validateKubeProxyIPVSConfiguration](#validatekubeproxyipvsconfiguration-pkgproxyapisconfigvalidationvalidationgo100) `:100`

- 🔗 [validateKubeProxyLinuxConfiguration](#validatekubeproxylinuxconfiguration-pkgproxyapisconfigvalidationvalidationgo119) `:119`

- 🔗 [validateKubeProxyNFTablesConfiguration](#validatekubeproxynftablesconfiguration-pkgproxyapisconfigvalidationvalidationgo109) `:109`

- 🔗 [validateKubeProxyNodePortAddress](#validatekubeproxynodeportaddress-pkgproxyapisconfigvalidationvalidationgo243) `:243`

- 🔗 [validateProxyMode](#validateproxymode-pkgproxyapisconfigvalidationvalidationgo163) `:163`

- 🔗 [validateProxyModeLinux](#validateproxymodelinux-pkgproxyapisconfigvalidationvalidationgo171) `:171`

- 🔗 [validateProxyModeWindows](#validateproxymodewindows-pkgproxyapisconfigvalidationvalidationgo186) `:186`

- 🔗 [validateShowHiddenMetricsVersion](#validateshowhiddenmetricsversion-pkgproxyapisconfigvalidationvalidationgo291) `:291`


</details>


[function] name: Validate file: pkg/proxy/apis/config/validation/validation.go:38 returns_error: нет description: Validate validates the configuration of kube-proxy


### Validate (pkg/proxy/apis/config/validation/validation.go:38)


Validate validates the configuration of kube-proxy


```go
func Validate((config *kubeproxyconfig.KubeProxyConfiguration)) (config *kubeproxyconfig.KubeProxyConfiguration)
```


**Тип запроса:** kubeproxyconfig.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeproxyconfig.KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:38`



---


[function] name: validateClientConnectionConfiguration file: pkg/proxy/apis/config/validation/validation.go:215 returns_error: нет description: —


### validateClientConnectionConfiguration (pkg/proxy/apis/config/validation/validation.go:215)


validateClientConnectionConfiguration is a function that performs operations based on the provided parameters and returns (config componentbaseconfig.ClientConnectionConfiguration, fldPath *field.Path).


```go
func validateClientConnectionConfiguration((config componentbaseconfig.ClientConnectionConfiguration, fldPath *field.Path)) (config componentbaseconfig.ClientConnectionConfiguration, fldPath *field.Path)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** componentbaseconfig.ClientConnectionConfiguration


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:215`



---


[function] name: validateDetectLocalConfiguration file: pkg/proxy/apis/config/validation/validation.go:332 returns_error: нет description: —


### validateDetectLocalConfiguration (pkg/proxy/apis/config/validation/validation.go:332)


validateDetectLocalConfiguration is a function that performs operations based on the provided parameters and returns (mode kubeproxyconfig.LocalMode, config kubeproxyconfig.DetectLocalConfiguration, fldPath *field.Path).


```go
func validateDetectLocalConfiguration((mode kubeproxyconfig.LocalMode, config kubeproxyconfig.DetectLocalConfiguration, fldPath *field.Path)) (mode kubeproxyconfig.LocalMode, config kubeproxyconfig.DetectLocalConfiguration, fldPath *field.Path)
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


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** kubeproxyconfig.LocalMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeproxyconfig.DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:332`



---


[function] name: validateDetectLocalMode file: pkg/proxy/apis/config/validation/validation.go:199 returns_error: нет description: —


### validateDetectLocalMode (pkg/proxy/apis/config/validation/validation.go:199)


validateDetectLocalMode is a function that performs operations based on the provided parameters and returns (mode kubeproxyconfig.LocalMode, fldPath *field.Path).


```go
func validateDetectLocalMode((mode kubeproxyconfig.LocalMode, fldPath *field.Path)) (mode kubeproxyconfig.LocalMode, fldPath *field.Path)
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


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** kubeproxyconfig.LocalMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:199`



---


[function] name: validateDualStackCIDRStrings file: pkg/proxy/apis/config/validation/validation.go:309 returns_error: нет description: —


### validateDualStackCIDRStrings (pkg/proxy/apis/config/validation/validation.go:309)


validateDualStackCIDRStrings is a function that performs operations based on the provided parameters and returns (cidrStrings []string, fldPath *field.Path).


```go
func validateDualStackCIDRStrings((cidrStrings []string, fldPath *field.Path)) (cidrStrings []string, fldPath *field.Path)
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


**Тип ответа:** cidrStrings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:309`



---


[function] name: validateHostPort file: pkg/proxy/apis/config/validation/validation.go:221 returns_error: нет description: —


### validateHostPort (pkg/proxy/apis/config/validation/validation.go:221)


validateHostPort is a function that performs operations based on the provided parameters and returns (input string, fldPath *field.Path).


```go
func validateHostPort((input string, fldPath *field.Path)) (input string, fldPath *field.Path)
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


**Тип ответа:** input


```json
{
  "builder": null
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/client-gen/args/gvpackages.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:221`



---


[function] name: validateIPVSExcludeCIDRs file: pkg/proxy/apis/config/validation/validation.go:280 returns_error: нет description: —


### validateIPVSExcludeCIDRs (pkg/proxy/apis/config/validation/validation.go:280)


validateIPVSExcludeCIDRs is a function that performs operations based on the provided parameters and returns (excludeCIDRs []string, fldPath *field.Path).


```go
func validateIPVSExcludeCIDRs((excludeCIDRs []string, fldPath *field.Path)) (excludeCIDRs []string, fldPath *field.Path)
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


**Тип ответа:** excludeCIDRs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:280`



---


[function] name: validateIPVSTimeout file: pkg/proxy/apis/config/validation/validation.go:262 returns_error: нет description: —


### validateIPVSTimeout (pkg/proxy/apis/config/validation/validation.go:262)


validateIPVSTimeout is a function that performs operations based on the provided parameters and returns (config kubeproxyconfig.KubeProxyIPVSConfiguration, fldPath *field.Path).


```go
func validateIPVSTimeout((config kubeproxyconfig.KubeProxyIPVSConfiguration, fldPath *field.Path)) (config kubeproxyconfig.KubeProxyIPVSConfiguration, fldPath *field.Path)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeproxyconfig.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:262`



---


[function] name: validateInterface file: pkg/proxy/apis/config/validation/validation.go:301 returns_error: нет description: —


### validateInterface (pkg/proxy/apis/config/validation/validation.go:301)


validateInterface is a function that performs operations based on the provided parameters and returns (iface string, fldPath *field.Path).


```go
func validateInterface((iface string, fldPath *field.Path)) (iface string, fldPath *field.Path)
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


**Тип ответа:** iface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:301`



---


[function] name: validateKubeProxyConntrackConfiguration file: pkg/proxy/apis/config/validation/validation.go:131 returns_error: нет description: —


### validateKubeProxyConntrackConfiguration (pkg/proxy/apis/config/validation/validation.go:131)


validateKubeProxyConntrackConfiguration is a function that performs operations based on the provided parameters and returns (config kubeproxyconfig.KubeProxyConntrackConfiguration, fldPath *field.Path).


```go
func validateKubeProxyConntrackConfiguration((config kubeproxyconfig.KubeProxyConntrackConfiguration, fldPath *field.Path)) (config kubeproxyconfig.KubeProxyConntrackConfiguration, fldPath *field.Path)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeproxyconfig.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:131`



---


[function] name: validateKubeProxyIPTablesConfiguration file: pkg/proxy/apis/config/validation/validation.go:91 returns_error: нет description: —


### validateKubeProxyIPTablesConfiguration (pkg/proxy/apis/config/validation/validation.go:91)


validateKubeProxyIPTablesConfiguration is a function that performs operations based on the provided parameters and returns (config kubeproxyconfig.KubeProxyIPTablesConfiguration, fldPath *field.Path).


```go
func validateKubeProxyIPTablesConfiguration((config kubeproxyconfig.KubeProxyIPTablesConfiguration, fldPath *field.Path)) (config kubeproxyconfig.KubeProxyIPTablesConfiguration, fldPath *field.Path)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeproxyconfig.KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:91`



---


[function] name: validateKubeProxyIPVSConfiguration file: pkg/proxy/apis/config/validation/validation.go:100 returns_error: нет description: —


### validateKubeProxyIPVSConfiguration (pkg/proxy/apis/config/validation/validation.go:100)


validateKubeProxyIPVSConfiguration is a function that performs operations based on the provided parameters and returns (config kubeproxyconfig.KubeProxyIPVSConfiguration, fldPath *field.Path).


```go
func validateKubeProxyIPVSConfiguration((config kubeproxyconfig.KubeProxyIPVSConfiguration, fldPath *field.Path)) (config kubeproxyconfig.KubeProxyIPVSConfiguration, fldPath *field.Path)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeproxyconfig.KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:100`



---


[function] name: validateKubeProxyLinuxConfiguration file: pkg/proxy/apis/config/validation/validation.go:119 returns_error: нет description: —


### validateKubeProxyLinuxConfiguration (pkg/proxy/apis/config/validation/validation.go:119)


validateKubeProxyLinuxConfiguration is a function that performs operations based on the provided parameters and returns (config kubeproxyconfig.KubeProxyLinuxConfiguration, fldPath *field.Path).


```go
func validateKubeProxyLinuxConfiguration((config kubeproxyconfig.KubeProxyLinuxConfiguration, fldPath *field.Path)) (config kubeproxyconfig.KubeProxyLinuxConfiguration, fldPath *field.Path)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeproxyconfig.KubeProxyLinuxConfiguration


```json
{
  "Conntrack": {},
  "MasqueradeAll": false,
  "OOMScoreAdj": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:119`



---


[function] name: validateKubeProxyNFTablesConfiguration file: pkg/proxy/apis/config/validation/validation.go:109 returns_error: нет description: —


### validateKubeProxyNFTablesConfiguration (pkg/proxy/apis/config/validation/validation.go:109)


validateKubeProxyNFTablesConfiguration is a function that performs operations based on the provided parameters and returns (config kubeproxyconfig.KubeProxyNFTablesConfiguration, fldPath *field.Path).


```go
func validateKubeProxyNFTablesConfiguration((config kubeproxyconfig.KubeProxyNFTablesConfiguration, fldPath *field.Path)) (config kubeproxyconfig.KubeProxyNFTablesConfiguration, fldPath *field.Path)
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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** kubeproxyconfig.KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:109`



---


[function] name: validateKubeProxyNodePortAddress file: pkg/proxy/apis/config/validation/validation.go:243 returns_error: нет description: —


### validateKubeProxyNodePortAddress (pkg/proxy/apis/config/validation/validation.go:243)


validateKubeProxyNodePortAddress is a function that performs operations based on the provided parameters and returns (nodePortAddresses []string, fldPath *field.Path).


```go
func validateKubeProxyNodePortAddress((nodePortAddresses []string, fldPath *field.Path)) (nodePortAddresses []string, fldPath *field.Path)
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


**Тип ответа:** nodePortAddresses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:243`



---


[function] name: validateProxyMode file: pkg/proxy/apis/config/validation/validation.go:163 returns_error: нет description: —


### validateProxyMode (pkg/proxy/apis/config/validation/validation.go:163)


validateProxyMode is a function that performs operations based on the provided parameters and returns (mode kubeproxyconfig.ProxyMode, fldPath *field.Path).


```go
func validateProxyMode((mode kubeproxyconfig.ProxyMode, fldPath *field.Path)) (mode kubeproxyconfig.ProxyMode, fldPath *field.Path)
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


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** kubeproxyconfig.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:163`



---


[function] name: validateProxyModeLinux file: pkg/proxy/apis/config/validation/validation.go:171 returns_error: нет description: —


### validateProxyModeLinux (pkg/proxy/apis/config/validation/validation.go:171)


validateProxyModeLinux is a function that performs operations based on the provided parameters and returns (mode kubeproxyconfig.ProxyMode, fldPath *field.Path).


```go
func validateProxyModeLinux((mode kubeproxyconfig.ProxyMode, fldPath *field.Path)) (mode kubeproxyconfig.ProxyMode, fldPath *field.Path)
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


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** kubeproxyconfig.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:171`



---


[function] name: validateProxyModeWindows file: pkg/proxy/apis/config/validation/validation.go:186 returns_error: нет description: —


### validateProxyModeWindows (pkg/proxy/apis/config/validation/validation.go:186)


validateProxyModeWindows is a function that performs operations based on the provided parameters and returns (mode kubeproxyconfig.ProxyMode, fldPath *field.Path).


```go
func validateProxyModeWindows((mode kubeproxyconfig.ProxyMode, fldPath *field.Path)) (mode kubeproxyconfig.ProxyMode, fldPath *field.Path)
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


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** kubeproxyconfig.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:186`



---


[function] name: validateShowHiddenMetricsVersion file: pkg/proxy/apis/config/validation/validation.go:291 returns_error: нет description: —


### validateShowHiddenMetricsVersion (pkg/proxy/apis/config/validation/validation.go:291)


validateShowHiddenMetricsVersion is a function that performs operations based on the provided parameters and returns (version string, fldPath *field.Path).


```go
func validateShowHiddenMetricsVersion((version string, fldPath *field.Path)) (version string, fldPath *field.Path)
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


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


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


📍 *Расположение:* `pkg/proxy/apis/config/validation/validation.go:291`




## pkg/proxy/apis/config/zz_generated.deepcopy.go


📄 Исходный файл: `pkg/proxy/apis/config/zz_generated.deepcopy.go`


<details open>
<summary><b>Функции в этом файле (19)</b></summary>


- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo41) `:41`

- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo82) `:82`

- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo128) `:128`

- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo154) `:154`

- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo178) `:178`

- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo200) `:200`

- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo221) `:221`

- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo237) `:237`

- 🔗 [DeepCopy](#deepcopy-pkgproxyapisconfigzz_generateddeepcopygo253) `:253`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo30) `:30`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo51) `:51`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo100) `:100`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo138) `:138`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo164) `:164`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo188) `:188`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo210) `:210`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo231) `:231`

- 🔗 [DeepCopyInto](#deepcopyinto-pkgproxyapisconfigzz_generateddeepcopygo247) `:247`

- 🔗 [DeepCopyObject](#deepcopyobject-pkgproxyapisconfigzz_generateddeepcopygo92) `:92`


</details>


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:41 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DetectLocalConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:41)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new DetectLocalConfiguration.


```go
func (in *DetectLocalConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:41`



---


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:82 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:82)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyConfiguration.


```go
func (in *KubeProxyConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:82`



---


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:128 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyConntrackConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:128)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyConntrackConfiguration.


```go
func (in *KubeProxyConntrackConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:128`



---


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:154 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyIPTablesConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:154)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyIPTablesConfiguration.


```go
func (in *KubeProxyIPTablesConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:154`



---


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:178 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyIPVSConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:178)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyIPVSConfiguration.


```go
func (in *KubeProxyIPVSConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:178`



---


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:200 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyLinuxConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:200)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyLinuxConfiguration.


```go
func (in *KubeProxyLinuxConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:200`



---


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:221 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyNFTablesConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:221)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyNFTablesConfiguration.


```go
func (in *KubeProxyNFTablesConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:221`



---


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:237 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyWindowsConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:237)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyWindowsConfiguration.


```go
func (in *KubeProxyWindowsConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:237`



---


[function] name: DeepCopy file: pkg/proxy/apis/config/zz_generated.deepcopy.go:253 returns_error: нет description: DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyWinkernelConfiguration.


### DeepCopy (pkg/proxy/apis/config/zz_generated.deepcopy.go:253)


DeepCopy is an autogenerated deepcopy function, copying the receiver, creating a new KubeProxyWinkernelConfiguration.


```go
func (in *KubeProxyWinkernelConfiguration) DeepCopy(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:253`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:30 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:30)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *DetectLocalConfiguration) DeepCopyInto((out *DetectLocalConfiguration)) (out *DetectLocalConfiguration)
```


**Тип запроса:** DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** DetectLocalConfiguration


```json
{
  "BridgeInterface": "string",
  "ClusterCIDRs": [],
  "InterfaceNamePrefix": "string"
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:30`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:51 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:51)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *KubeProxyConfiguration) DeepCopyInto((out *KubeProxyConfiguration)) (out *KubeProxyConfiguration)
```


**Тип запроса:** KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** KubeProxyConfiguration


```json
{
  "Linux": {},
  "Windows": {},
  "FeatureGates": {},
  "ClientConnection": {},
  "Logging": {},
  "HostnameOverride": "string",
  "BindAddress": "string",
  "HealthzBindAddress": "string",
  "MetricsBindAddress": "string",
  "BindAddressHardFail": false,
  "EnableProfiling": false,
  "ShowHiddenMetricsForVersion": "string",
  "Mode": {},
  "IPTables": {},
  "IPVS": {},
  "Winkernel": {},
  "NFTables": {},
  "DetectLocalMode": {},
  "DetectLocal": {},
  "NodePortAddresses": [],
  "SyncPeriod": {},
  "MinSyncPeriod": {},
  "ConfigSyncPeriod": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:51`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:100 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:100)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *KubeProxyConntrackConfiguration) DeepCopyInto((out *KubeProxyConntrackConfiguration)) (out *KubeProxyConntrackConfiguration)
```


**Тип запроса:** KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:100`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:138 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:138)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *KubeProxyIPTablesConfiguration) DeepCopyInto((out *KubeProxyIPTablesConfiguration)) (out *KubeProxyIPTablesConfiguration)
```


**Тип запроса:** KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** KubeProxyIPTablesConfiguration


```json
{
  "MasqueradeBit": 0,
  "LocalhostNodePorts": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:138`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:164 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:164)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *KubeProxyIPVSConfiguration) DeepCopyInto((out *KubeProxyIPVSConfiguration)) (out *KubeProxyIPVSConfiguration)
```


**Тип запроса:** KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** KubeProxyIPVSConfiguration


```json
{
  "Scheduler": "string",
  "ExcludeCIDRs": [],
  "StrictARP": false,
  "TCPTimeout": {},
  "TCPFinTimeout": {},
  "UDPTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:164`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:188 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:188)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *KubeProxyLinuxConfiguration) DeepCopyInto((out *KubeProxyLinuxConfiguration)) (out *KubeProxyLinuxConfiguration)
```


**Тип запроса:** KubeProxyLinuxConfiguration


```json
{
  "Conntrack": {},
  "MasqueradeAll": false,
  "OOMScoreAdj": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** KubeProxyLinuxConfiguration


```json
{
  "Conntrack": {},
  "MasqueradeAll": false,
  "OOMScoreAdj": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:188`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:210 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:210)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *KubeProxyNFTablesConfiguration) DeepCopyInto((out *KubeProxyNFTablesConfiguration)) (out *KubeProxyNFTablesConfiguration)
```


**Тип запроса:** KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** KubeProxyNFTablesConfiguration


```json
{
  "MasqueradeBit": 0
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:210`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:231 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:231)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *KubeProxyWindowsConfiguration) DeepCopyInto((out *KubeProxyWindowsConfiguration)) (out *KubeProxyWindowsConfiguration)
```


**Тип запроса:** KubeProxyWindowsConfiguration


```json
{
  "RunAsService": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** KubeProxyWindowsConfiguration


```json
{
  "RunAsService": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:231`



---


[function] name: DeepCopyInto file: pkg/proxy/apis/config/zz_generated.deepcopy.go:247 returns_error: нет description: DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


### DeepCopyInto (pkg/proxy/apis/config/zz_generated.deepcopy.go:247)


DeepCopyInto is an autogenerated deepcopy function, copying the receiver, writing into out. in must be non-nil.


```go
func (in *KubeProxyWinkernelConfiguration) DeepCopyInto((out *KubeProxyWinkernelConfiguration)) (out *KubeProxyWinkernelConfiguration)
```


**Тип запроса:** KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


**Тип ответа:** out


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


**Тип ответа:** KubeProxyWinkernelConfiguration


```json
{
  "NetworkName": "string",
  "SourceVip": "string",
  "EnableDSR": false,
  "RootHnsEndpointName": "string",
  "ForwardHealthCheckVip": false
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:247`



---


[function] name: DeepCopyObject file: pkg/proxy/apis/config/zz_generated.deepcopy.go:92 returns_error: нет description: DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


### DeepCopyObject (pkg/proxy/apis/config/zz_generated.deepcopy.go:92)


DeepCopyObject is an autogenerated deepcopy function, copying the receiver, creating a new runtime.Object.


```go
func (in *KubeProxyConfiguration) DeepCopyObject(()) ()
```


📍 *Расположение:* `pkg/proxy/apis/config/zz_generated.deepcopy.go:92`




## pkg/proxy/config/config.go


📄 Исходный файл: `pkg/proxy/config/config.go`


<details open>
<summary><b>Функции в этом файле (25)</b></summary>


- 🔗 [NewEndpointSliceConfig](#newendpointsliceconfig-pkgproxyconfigconfiggo80) `:80`

- 🔗 [NewNodeConfig](#newnodeconfig-pkgproxyconfigconfiggo283) `:283`

- 🔗 [NewNodeTopologyConfig](#newnodetopologyconfig-pkgproxyconfigconfiggo467) `:467`

- 🔗 [NewServiceCIDRConfig](#newservicecidrconfig-pkgproxyconfigconfiggo370) `:370`

- 🔗 [NewServiceConfig](#newserviceconfig-pkgproxyconfigconfiggo174) `:174`

- 🔗 [RegisterEventHandler](#registereventhandler-pkgproxyconfigconfiggo100) `:100`

- 🔗 [RegisterEventHandler](#registereventhandler-pkgproxyconfigconfiggo194) `:194`

- 🔗 [RegisterEventHandler](#registereventhandler-pkgproxyconfigconfiggo303) `:303`

- 🔗 [RegisterEventHandler](#registereventhandler-pkgproxyconfigconfiggo397) `:397`

- 🔗 [RegisterEventHandler](#registereventhandler-pkgproxyconfigconfiggo503) `:503`

- 🔗 [Run](#run-pkgproxyconfigconfiggo105) `:105`

- 🔗 [Run](#run-pkgproxyconfigconfiggo199) `:199`

- 🔗 [Run](#run-pkgproxyconfigconfiggo308) `:308`

- 🔗 [Run](#run-pkgproxyconfigconfiggo402) `:402`

- 🔗 [handleAddEndpointSlice](#handleaddendpointslice-pkgproxyconfigconfiggo118) `:118`

- 🔗 [handleAddService](#handleaddservice-pkgproxyconfigconfiggo212) `:212`

- 🔗 [handleChangeNode](#handlechangenode-pkgproxyconfigconfiggo321) `:321`

- 🔗 [handleDeleteEndpointSlice](#handledeleteendpointslice-pkgproxyconfigconfiggo147) `:147`

- 🔗 [handleDeleteNode](#handledeletenode-pkgproxyconfigconfiggo333) `:333`

- 🔗 [handleDeleteService](#handledeleteservice-pkgproxyconfigconfiggo241) `:241`

- 🔗 [handleNodeEvent](#handlenodeevent-pkgproxyconfigconfiggo509) `:509`

- 🔗 [handleServiceCIDREvent](#handleservicecidrevent-pkgproxyconfigconfiggo413) `:413`

- 🔗 [handleUpdateEndpointSlice](#handleupdateendpointslice-pkgproxyconfigconfiggo130) `:130`

- 🔗 [handleUpdateService](#handleupdateservice-pkgproxyconfigconfiggo224) `:224`

- 🔗 [newNodeTopologyConfig](#newnodetopologyconfig-pkgproxyconfigconfiggo473) `:473`


</details>


[function] name: NewEndpointSliceConfig file: pkg/proxy/config/config.go:80 returns_error: нет description: NewEndpointSliceConfig creates a new EndpointSliceConfig.


### NewEndpointSliceConfig (pkg/proxy/config/config.go:80)


NewEndpointSliceConfig creates a new EndpointSliceConfig.


```go
func NewEndpointSliceConfig((ctx context.Context, endpointSliceInformer discoveryv1informers.EndpointSliceInformer, resyncPeriod time.Duration)) (ctx context.Context, endpointSliceInformer discoveryv1informers.EndpointSliceInformer, resyncPeriod time.Duration)
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


**Тип ответа:** endpointSliceInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discoveryv1informers.EndpointSliceInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resyncPeriod


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


📍 *Расположение:* `pkg/proxy/config/config.go:80`



---


[function] name: NewNodeConfig file: pkg/proxy/config/config.go:283 returns_error: нет description: NewNodeConfig creates a new NodeConfig.


### NewNodeConfig (pkg/proxy/config/config.go:283)


NewNodeConfig creates a new NodeConfig.


```go
func NewNodeConfig((ctx context.Context, nodeInformer v1informers.NodeInformer, resyncPeriod time.Duration)) (ctx context.Context, nodeInformer v1informers.NodeInformer, resyncPeriod time.Duration)
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


**Тип ответа:** nodeInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/node.go`


**Тип ответа:** v1informers.NodeInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/storage/v1beta1/csinode.go`


**Тип ответа:** resyncPeriod


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


📍 *Расположение:* `pkg/proxy/config/config.go:283`



---


[function] name: NewNodeTopologyConfig file: pkg/proxy/config/config.go:467 returns_error: нет description: NewNodeTopologyConfig creates a new NodeTopologyConfig.


### NewNodeTopologyConfig (pkg/proxy/config/config.go:467)


NewNodeTopologyConfig creates a new NodeTopologyConfig.


```go
func NewNodeTopologyConfig((ctx context.Context, nodeInformer v1informers.NodeInformer, resyncPeriod time.Duration)) (ctx context.Context, nodeInformer v1informers.NodeInformer, resyncPeriod time.Duration)
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


**Тип ответа:** nodeInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/node.go`


**Тип ответа:** v1informers.NodeInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/storage/v1beta1/csinode.go`


**Тип ответа:** resyncPeriod


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


📍 *Расположение:* `pkg/proxy/config/config.go:467`



---


[function] name: NewServiceCIDRConfig file: pkg/proxy/config/config.go:370 returns_error: нет description: NewServiceCIDRConfig creates a new ServiceCIDRConfig.


### NewServiceCIDRConfig (pkg/proxy/config/config.go:370)


NewServiceCIDRConfig creates a new ServiceCIDRConfig.


```go
func NewServiceCIDRConfig((ctx context.Context, serviceCIDRInformer networkingv1informers.ServiceCIDRInformer, resyncPeriod time.Duration)) (ctx context.Context, serviceCIDRInformer networkingv1informers.ServiceCIDRInformer, resyncPeriod time.Duration)
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


**Тип ответа:** serviceCIDRInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/networking/v1beta1/servicecidr.go`


**Тип ответа:** networkingv1informers.ServiceCIDRInformer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resyncPeriod


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


📍 *Расположение:* `pkg/proxy/config/config.go:370`



---


[function] name: NewServiceConfig file: pkg/proxy/config/config.go:174 returns_error: нет description: NewServiceConfig creates a new ServiceConfig.


### NewServiceConfig (pkg/proxy/config/config.go:174)


NewServiceConfig creates a new ServiceConfig.


```go
func NewServiceConfig((ctx context.Context, serviceInformer v1informers.ServiceInformer, resyncPeriod time.Duration)) (ctx context.Context, serviceInformer v1informers.ServiceInformer, resyncPeriod time.Duration)
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


**Тип ответа:** serviceInformer


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** v1informers.ServiceInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/client/informers/externalversions/apiregistration/v1beta1/apiservice.go`


**Тип ответа:** resyncPeriod


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


📍 *Расположение:* `pkg/proxy/config/config.go:174`



---


[function] name: RegisterEventHandler file: pkg/proxy/config/config.go:100 returns_error: нет description: RegisterEventHandler registers a handler which is called on every endpoint slice change.


### RegisterEventHandler (pkg/proxy/config/config.go:100)


RegisterEventHandler registers a handler which is called on every endpoint slice change.


```go
func (c *EndpointSliceConfig) RegisterEventHandler((handler EndpointSliceHandler)) (handler EndpointSliceHandler)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** EndpointSliceHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/config/config.go:100`



---


[function] name: RegisterEventHandler file: pkg/proxy/config/config.go:194 returns_error: нет description: RegisterEventHandler registers a handler which is called on every service change.


### RegisterEventHandler (pkg/proxy/config/config.go:194)


RegisterEventHandler registers a handler which is called on every service change.


```go
func (c *ServiceConfig) RegisterEventHandler((handler ServiceHandler)) (handler ServiceHandler)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** ServiceHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/config/config.go:194`



---


[function] name: RegisterEventHandler file: pkg/proxy/config/config.go:303 returns_error: нет description: RegisterEventHandler registers a handler which is called on every node change.


### RegisterEventHandler (pkg/proxy/config/config.go:303)


RegisterEventHandler registers a handler which is called on every node change.


```go
func (c *NodeConfig) RegisterEventHandler((handler NodeHandler)) (handler NodeHandler)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** NodeHandler


```json
{
  "CreateHook": {},
  "Existing": [],
  "AsyncCalls": [],
  "CreatedNodes": [],
  "DeletedNodes": [],
  "UpdatedNodes": [],
  "UpdatedNodeStatuses": [],
  "RequestCount": 0,
  "lock": {},
  "DeleteWaitChan": {},
  "PatchWaitChan": {}
}
```


*Определено в:* `pkg/controller/testutil/test_utils.go`


📍 *Расположение:* `pkg/proxy/config/config.go:303`



---


[function] name: RegisterEventHandler file: pkg/proxy/config/config.go:397 returns_error: нет description: RegisterEventHandler registers a handler which is called on every ServiceCIDR change.


### RegisterEventHandler (pkg/proxy/config/config.go:397)


RegisterEventHandler registers a handler which is called on every ServiceCIDR change.


```go
func (c *ServiceCIDRConfig) RegisterEventHandler((handler ServiceCIDRHandler)) (handler ServiceCIDRHandler)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** ServiceCIDRHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/config/config.go:397`



---


[function] name: RegisterEventHandler file: pkg/proxy/config/config.go:503 returns_error: нет description: RegisterEventHandler registers a handler which is called on Node object change.


### RegisterEventHandler (pkg/proxy/config/config.go:503)


RegisterEventHandler registers a handler which is called on Node object change.


```go
func (n *NodeTopologyConfig) RegisterEventHandler((handler NodeTopologyHandler)) (handler NodeTopologyHandler)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** NodeTopologyHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/config/config.go:503`



---


[function] name: Run file: pkg/proxy/config/config.go:105 returns_error: нет description: Run waits for cache synced and invokes handlers after syncing.


### Run (pkg/proxy/config/config.go:105)


Run waits for cache synced and invokes handlers after syncing.


```go
func (c *EndpointSliceConfig) Run((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/proxy/config/config.go:105`



---


[function] name: Run file: pkg/proxy/config/config.go:199 returns_error: нет description: Run waits for cache synced and invokes handlers after syncing.


### Run (pkg/proxy/config/config.go:199)


Run waits for cache synced and invokes handlers after syncing.


```go
func (c *ServiceConfig) Run((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/proxy/config/config.go:199`



---


[function] name: Run file: pkg/proxy/config/config.go:308 returns_error: нет description: Run starts the goroutine responsible for calling registered handlers.


### Run (pkg/proxy/config/config.go:308)


Run starts the goroutine responsible for calling registered handlers.


```go
func (c *NodeConfig) Run((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/proxy/config/config.go:308`



---


[function] name: Run file: pkg/proxy/config/config.go:402 returns_error: нет description: Run waits for cache synced and invokes handlers after syncing.


### Run (pkg/proxy/config/config.go:402)


Run waits for cache synced and invokes handlers after syncing.


```go
func (c *ServiceCIDRConfig) Run((stopCh <-chan struct{})) (stopCh <-chan struct{})
```


**Тип ответа:** stopCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/proxy/config/config.go:402`



---


[function] name: handleAddEndpointSlice file: pkg/proxy/config/config.go:118 returns_error: нет description: —


### handleAddEndpointSlice (pkg/proxy/config/config.go:118)


handleAddEndpointSlice is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (c *EndpointSliceConfig) handleAddEndpointSlice((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:118`



---


[function] name: handleAddService file: pkg/proxy/config/config.go:212 returns_error: нет description: —


### handleAddService (pkg/proxy/config/config.go:212)


handleAddService is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (c *ServiceConfig) handleAddService((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:212`



---


[function] name: handleChangeNode file: pkg/proxy/config/config.go:321 returns_error: нет description: —


### handleChangeNode (pkg/proxy/config/config.go:321)


handleChangeNode is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (c *NodeConfig) handleChangeNode((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:321`



---


[function] name: handleDeleteEndpointSlice file: pkg/proxy/config/config.go:147 returns_error: нет description: —


### handleDeleteEndpointSlice (pkg/proxy/config/config.go:147)


handleDeleteEndpointSlice is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (c *EndpointSliceConfig) handleDeleteEndpointSlice((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:147`



---


[function] name: handleDeleteNode file: pkg/proxy/config/config.go:333 returns_error: нет description: —


### handleDeleteNode (pkg/proxy/config/config.go:333)


handleDeleteNode is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (c *NodeConfig) handleDeleteNode((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:333`



---


[function] name: handleDeleteService file: pkg/proxy/config/config.go:241 returns_error: нет description: —


### handleDeleteService (pkg/proxy/config/config.go:241)


handleDeleteService is a method that performs operations based on the provided parameters and returns (obj interface{}).


```go
func (c *ServiceConfig) handleDeleteService((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:241`



---


[function] name: handleNodeEvent file: pkg/proxy/config/config.go:509 returns_error: нет description: handleNodeEvent is a helper function to handle Add, Update and Delete
events on Node objects and call downstream event h


### handleNodeEvent (pkg/proxy/config/config.go:509)


handleNodeEvent is a helper function to handle Add, Update and Delete
events on Node objects and call downstream event handlers.


```go
func (n *NodeTopologyConfig) handleNodeEvent((obj interface{})) (obj interface{})
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:509`



---


[function] name: handleServiceCIDREvent file: pkg/proxy/config/config.go:413 returns_error: нет description: handleServiceCIDREvent is a helper function to handle Add, Update and Delete
events on ServiceCIDR objects and call down


### handleServiceCIDREvent (pkg/proxy/config/config.go:413)


handleServiceCIDREvent is a helper function to handle Add, Update and Delete
events on ServiceCIDR objects and call downstream event handlers.


```go
func (c *ServiceCIDRConfig) handleServiceCIDREvent((oldObj, newObj interface{})) (oldObj, newObj interface{})
```


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:413`



---


[function] name: handleUpdateEndpointSlice file: pkg/proxy/config/config.go:130 returns_error: нет description: —


### handleUpdateEndpointSlice (pkg/proxy/config/config.go:130)


handleUpdateEndpointSlice is a method that performs operations based on the provided parameters and returns (oldObj, newObj interface{}).


```go
func (c *EndpointSliceConfig) handleUpdateEndpointSlice((oldObj, newObj interface{})) (oldObj, newObj interface{})
```


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:130`



---


[function] name: handleUpdateService file: pkg/proxy/config/config.go:224 returns_error: нет description: —


### handleUpdateService (pkg/proxy/config/config.go:224)


handleUpdateService is a method that performs operations based on the provided parameters and returns (oldObj, newObj interface{}).


```go
func (c *ServiceConfig) handleUpdateService((oldObj, newObj interface{})) (oldObj, newObj interface{})
```


**Тип ответа:** oldObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newObj


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/config/config.go:224`



---


[function] name: newNodeTopologyConfig file: pkg/proxy/config/config.go:473 returns_error: нет description: newNodeTopologyConfig implements NewNodeTopologyConfig by additionally consuming a callback function which is invoked wh


### newNodeTopologyConfig (pkg/proxy/config/config.go:473)


newNodeTopologyConfig implements NewNodeTopologyConfig by additionally consuming a callback function which is invoked when
event handler completes processing and is only used for testing.


```go
func newNodeTopologyConfig((ctx context.Context, nodeInformer v1informers.NodeInformer, resyncPeriod time.Duration, callback func())) (ctx context.Context, nodeInformer v1informers.NodeInformer, resyncPeriod time.Duration, callback func())
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


**Тип ответа:** nodeInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/node.go`


**Тип ответа:** v1informers.NodeInformer


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/storage/v1beta1/csinode.go`


**Тип ответа:** resyncPeriod


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


**Тип ответа:** callback


```json
{
  "commit": {},
  "revert": {}
}
```


*Определено в:* `pkg/registry/core/service/storage/transaction.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/config/config.go:473`




## pkg/proxy/conntrack/cleanup.go


📄 Исходный файл: `pkg/proxy/conntrack/cleanup.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CleanStaleEntries](#cleanstaleentries-pkgproxyconntrackcleanupgo45) `:45`


</details>


[function] name: CleanStaleEntries file: pkg/proxy/conntrack/cleanup.go:45 returns_error: нет description: CleanStaleEntries scans conntrack table and removes any entries
for a service that do not correspond to a serving endpoi


### CleanStaleEntries (pkg/proxy/conntrack/cleanup.go:45)


CleanStaleEntries scans conntrack table and removes any entries
for a service that do not correspond to a serving endpoint.
List existing conntrack entries and calculate the desired conntrack state
based on the current Services and Endpoints.


```go
func CleanStaleEntries((ct Interface, ipFamily v1.IPFamily,
	svcPortMap proxy.ServicePortMap, endpointsMap proxy.EndpointsMap)) (ct Interface, ipFamily v1.IPFamily,
	svcPortMap proxy.ServicePortMap, endpointsMap proxy.EndpointsMap)
```


**Тип ответа:** ct


```json
{
  "cache": {},
  "logger": {}
}
```


*Определено в:* `pkg/controller/volume/selinuxwarning/metrics.go`


**Тип ответа:** Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** svcPortMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointsMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.EndpointsMap


```json
{
  "UpdatedServices": {},
  "ConntrackCleanupRequired": false,
  "LastChangeTriggerTimes": {}
}
```


*Определено в:* `pkg/proxy/endpointschangetracker.go`


📍 *Расположение:* `pkg/proxy/conntrack/cleanup.go:45`




## pkg/proxy/conntrack/conntrack.go


📄 Исходный файл: `pkg/proxy/conntrack/conntrack.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [DeleteEntries](#deleteentries-pkgproxyconntrackconntrackgo69) `:69`

- 🔗 [ListEntries](#listentries-pkgproxyconntrackconntrackgo59) `:59`

- 🔗 [New](#new-pkgproxyconntrackconntrackgo50) `:50`

- 🔗 [newConntracker](#newconntracker-pkgproxyconntrackconntrackgo54) `:54`


</details>


[function] name: DeleteEntries file: pkg/proxy/conntrack/conntrack.go:69 returns_error: да description: DeleteEntries deletes the given conntrack entries on the specified IP family.
It returns the number of deleted entries a


### DeleteEntries (pkg/proxy/conntrack/conntrack.go:69)


DeleteEntries deletes the given conntrack entries on the specified IP family.
It returns the number of deleted entries and an error if any.


```go
func (ct *conntracker) DeleteEntries((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/conntrack/conntrack.go:69`



---


[function] name: ListEntries file: pkg/proxy/conntrack/conntrack.go:59 returns_error: да description: ListEntries list all conntrack entries for connections of the given IP family.


### ListEntries (pkg/proxy/conntrack/conntrack.go:59)


ListEntries list all conntrack entries for connections of the given IP family.


```go
func (ct *conntracker) ListEntries((entries []*netlink.ConntrackFlow, err error)) (entries []*netlink.ConntrackFlow, err error)
```


**Тип запроса:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** entries


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** netlink.ConntrackFlow


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


*Типы возврата:* `entries []*netlink.ConntrackFlow`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/conntrack/conntrack.go:59`



---


[function] name: New file: pkg/proxy/conntrack/conntrack.go:50 returns_error: нет description: —


### New (pkg/proxy/conntrack/conntrack.go:50)


New is a function that performs operations based on the provided parameters and returns ().


```go
func New(()) ()
```


📍 *Расположение:* `pkg/proxy/conntrack/conntrack.go:50`



---


[function] name: newConntracker file: pkg/proxy/conntrack/conntrack.go:54 returns_error: нет description: —


### newConntracker (pkg/proxy/conntrack/conntrack.go:54)


newConntracker is a function that performs operations based on the provided parameters and returns (handler netlinkHandler).


```go
func newConntracker((handler netlinkHandler)) (handler netlinkHandler)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** netlinkHandler


```json
{
  "socket": null
}
```


*Определено в:* `pkg/proxy/util/nfacct/handler.go`


📍 *Расположение:* `pkg/proxy/conntrack/conntrack.go:54`




## pkg/proxy/conntrack/fake.go


📄 Исходный файл: `pkg/proxy/conntrack/fake.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [ConntrackDeleteFilters](#conntrackdeletefilters-pkgproxyconntrackfakego51) `:51`

- 🔗 [ConntrackTableList](#conntracktablelist-pkgproxyconntrackfakego44) `:44`

- 🔗 [NewFake](#newfake-pkgproxyconntrackfakego28) `:28`


</details>


[function] name: ConntrackDeleteFilters file: pkg/proxy/conntrack/fake.go:51 returns_error: да description: —


### ConntrackDeleteFilters (pkg/proxy/conntrack/fake.go:51)


ConntrackDeleteFilters is a method that performs operations based on the provided parameters and may return an error.


```go
func (f *fakeHandler) ConntrackDeleteFilters((uint, error)) (uint, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `uint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/conntrack/fake.go:51`



---


[function] name: ConntrackTableList file: pkg/proxy/conntrack/fake.go:44 returns_error: да description: —


### ConntrackTableList (pkg/proxy/conntrack/fake.go:44)


ConntrackTableList is a method that performs operations based on the provided parameters and may return an error.


```go
func (f *fakeHandler) ConntrackTableList(([]*netlink.ConntrackFlow, error)) ([]*netlink.ConntrackFlow, error)
```


**Тип запроса:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*netlink.ConntrackFlow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/conntrack/fake.go:44`



---


[function] name: NewFake file: pkg/proxy/conntrack/fake.go:28 returns_error: нет description: NewFake creates a new FakeInterface


### NewFake (pkg/proxy/conntrack/fake.go:28)


NewFake creates a new FakeInterface


```go
func NewFake(()) ()
```


📍 *Расположение:* `pkg/proxy/conntrack/fake.go:28`




## pkg/proxy/conntrack/filter.go


📄 Исходный файл: `pkg/proxy/conntrack/filter.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MatchConntrackFlow](#matchconntrackflow-pkgproxyconntrackfiltergo61) `:61`

- 🔗 [flowKey](#flowkey-pkgproxyconntrackfiltergo47) `:47`

- 🔗 [newFlowFilter](#newflowfilter-pkgproxyconntrackfiltergo36) `:36`


</details>


[function] name: MatchConntrackFlow file: pkg/proxy/conntrack/filter.go:61 returns_error: нет description: MatchConntrackFlow applies the filter to the flow and returns true if the flow matches the filter


### MatchConntrackFlow (pkg/proxy/conntrack/filter.go:61)


MatchConntrackFlow applies the filter to the flow and returns true if the flow matches the filter


```go
func (f *flowFilter) MatchConntrackFlow((flow *netlink.ConntrackFlow)) (flow *netlink.ConntrackFlow)
```


**Тип запроса:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flow


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/flowcontrol/v1beta1/flowschema.go`


**Тип ответа:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/conntrack/filter.go:61`



---


[function] name: flowKey file: pkg/proxy/conntrack/filter.go:47 returns_error: нет description: flowKey returns a unique key for the given flow.


### flowKey (pkg/proxy/conntrack/filter.go:47)


flowKey returns a unique key for the given flow.


```go
func flowKey((flow *netlink.ConntrackFlow)) (flow *netlink.ConntrackFlow)
```


**Тип запроса:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flow


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/flowcontrol/v1beta1/flowschema.go`


**Тип ответа:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/conntrack/filter.go:47`



---


[function] name: newFlowFilter file: pkg/proxy/conntrack/filter.go:36 returns_error: нет description: —


### newFlowFilter (pkg/proxy/conntrack/filter.go:36)


newFlowFilter is a function that performs operations based on the provided parameters and returns (flows []*netlink.ConntrackFlow).


```go
func newFlowFilter((flows []*netlink.ConntrackFlow)) (flows []*netlink.ConntrackFlow)
```


**Тип запроса:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** flows


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** netlink.ConntrackFlow


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/conntrack/filter.go:36`




## pkg/proxy/conntrack/sysctls.go


📄 Исходный файл: `pkg/proxy/conntrack/sysctls.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [SetMax](#setmax-pkgproxyconntracksysctlsgo139) `:139`

- 🔗 [SetSysctls](#setsysctls-pkgproxyconntracksysctlsgo37) `:37`

- 🔗 [SetTCPBeLiberal](#settcpbeliberal-pkgproxyconntracksysctlsgo167) `:167`

- 🔗 [SetTCPCloseWaitTimeout](#settcpclosewaittimeout-pkgproxyconntracksysctlsgo163) `:163`

- 🔗 [SetTCPEstablishedTimeout](#settcpestablishedtimeout-pkgproxyconntracksysctlsgo159) `:159`

- 🔗 [SetUDPStreamTimeout](#setudpstreamtimeout-pkgproxyconntracksysctlsgo175) `:175`

- 🔗 [SetUDPTimeout](#setudptimeout-pkgproxyconntracksysctlsgo171) `:171`

- 🔗 [detectNumCPU](#detectnumcpu-pkgproxyconntracksysctlsgo127) `:127`

- 🔗 [getConntrackMax](#getconntrackmax-pkgproxyconntracksysctlsgo109) `:109`

- 🔗 [readIntStringFile](#readintstringfile-pkgproxyconntracksysctlsgo193) `:193`

- 🔗 [setIntSysCtl](#setintsysctl-pkgproxyconntracksysctlsgo179) `:179`

- 🔗 [setSysctls](#setsysctls-pkgproxyconntracksysctlsgo60) `:60`

- 🔗 [writeIntStringFile](#writeintstringfile-pkgproxyconntracksysctlsgo201) `:201`


</details>


[function] name: SetMax file: pkg/proxy/conntrack/sysctls.go:139 returns_error: нет description: —


### SetMax (pkg/proxy/conntrack/sysctls.go:139)


SetMax is a method that updates data based on the provided parameters and returns (ctx context.Context, max int).


```go
func (rct realConntrackConfigurer) SetMax((ctx context.Context, max int)) (ctx context.Context, max int)
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


**Тип ответа:** max


```json
{
  "maxSeats": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/max_seats.go`


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:139`



---


[function] name: SetSysctls file: pkg/proxy/conntrack/sysctls.go:37 returns_error: нет description: —


### SetSysctls (pkg/proxy/conntrack/sysctls.go:37)


SetSysctls is a function that updates data based on the provided parameters and returns (ctx context.Context, config *proxyconfigapi.KubeProxyConntrackConfiguration).


```go
func SetSysctls((ctx context.Context, config *proxyconfigapi.KubeProxyConntrackConfiguration)) (ctx context.Context, config *proxyconfigapi.KubeProxyConntrackConfiguration)
```


**Тип запроса:** proxyconfigapi.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** proxyconfigapi.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:37`



---


[function] name: SetTCPBeLiberal file: pkg/proxy/conntrack/sysctls.go:167 returns_error: нет description: —


### SetTCPBeLiberal (pkg/proxy/conntrack/sysctls.go:167)


SetTCPBeLiberal is a method that updates data based on the provided parameters and returns (ctx context.Context, value int).


```go
func (rct realConntrackConfigurer) SetTCPBeLiberal((ctx context.Context, value int)) (ctx context.Context, value int)
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


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:167`



---


[function] name: SetTCPCloseWaitTimeout file: pkg/proxy/conntrack/sysctls.go:163 returns_error: нет description: —


### SetTCPCloseWaitTimeout (pkg/proxy/conntrack/sysctls.go:163)


SetTCPCloseWaitTimeout is a method that updates data based on the provided parameters and returns (ctx context.Context, seconds int).


```go
func (rct realConntrackConfigurer) SetTCPCloseWaitTimeout((ctx context.Context, seconds int)) (ctx context.Context, seconds int)
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


**Тип ответа:** seconds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:163`



---


[function] name: SetTCPEstablishedTimeout file: pkg/proxy/conntrack/sysctls.go:159 returns_error: нет description: —


### SetTCPEstablishedTimeout (pkg/proxy/conntrack/sysctls.go:159)


SetTCPEstablishedTimeout is a method that updates data based on the provided parameters and returns (ctx context.Context, seconds int).


```go
func (rct realConntrackConfigurer) SetTCPEstablishedTimeout((ctx context.Context, seconds int)) (ctx context.Context, seconds int)
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


**Тип ответа:** seconds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:159`



---


[function] name: SetUDPStreamTimeout file: pkg/proxy/conntrack/sysctls.go:175 returns_error: нет description: —


### SetUDPStreamTimeout (pkg/proxy/conntrack/sysctls.go:175)


SetUDPStreamTimeout is a method that updates data based on the provided parameters and returns (ctx context.Context, seconds int).


```go
func (rct realConntrackConfigurer) SetUDPStreamTimeout((ctx context.Context, seconds int)) (ctx context.Context, seconds int)
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


**Тип ответа:** seconds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:175`



---


[function] name: SetUDPTimeout file: pkg/proxy/conntrack/sysctls.go:171 returns_error: нет description: —


### SetUDPTimeout (pkg/proxy/conntrack/sysctls.go:171)


SetUDPTimeout is a method that updates data based on the provided parameters and returns (ctx context.Context, seconds int).


```go
func (rct realConntrackConfigurer) SetUDPTimeout((ctx context.Context, seconds int)) (ctx context.Context, seconds int)
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


**Тип ответа:** seconds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:171`



---


[function] name: detectNumCPU file: pkg/proxy/conntrack/sysctls.go:127 returns_error: нет description: —


### detectNumCPU (pkg/proxy/conntrack/sysctls.go:127)


detectNumCPU is a function that performs operations based on the provided parameters and returns ().


```go
func detectNumCPU(()) ()
```


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:127`



---


[function] name: getConntrackMax file: pkg/proxy/conntrack/sysctls.go:109 returns_error: да description: —


### getConntrackMax (pkg/proxy/conntrack/sysctls.go:109)


getConntrackMax is a function that performs operations based on the provided parameters and may return an error.


```go
func getConntrackMax((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:109`



---


[function] name: readIntStringFile file: pkg/proxy/conntrack/sysctls.go:193 returns_error: да description: —


### readIntStringFile (pkg/proxy/conntrack/sysctls.go:193)


readIntStringFile is a function that performs operations based on the provided parameters and may return an error.


```go
func readIntStringFile((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:193`



---


[function] name: setIntSysCtl file: pkg/proxy/conntrack/sysctls.go:179 returns_error: нет description: —


### setIntSysCtl (pkg/proxy/conntrack/sysctls.go:179)


setIntSysCtl is a method that performs operations based on the provided parameters and returns (ctx context.Context, name string, value int).


```go
func (rct realConntrackConfigurer) setIntSysCtl((ctx context.Context, name string, value int)) (ctx context.Context, name string, value int)
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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:179`



---


[function] name: setSysctls file: pkg/proxy/conntrack/sysctls.go:60 returns_error: нет description: —


### setSysctls (pkg/proxy/conntrack/sysctls.go:60)


setSysctls is a function that performs operations based on the provided parameters and returns (ctx context.Context, ct conntrackConfigurer, config *proxyconfigapi.KubeProxyConntrackConfiguration).


```go
func setSysctls((ctx context.Context, ct conntrackConfigurer, config *proxyconfigapi.KubeProxyConntrackConfiguration)) (ctx context.Context, ct conntrackConfigurer, config *proxyconfigapi.KubeProxyConntrackConfiguration)
```


**Тип запроса:** proxyconfigapi.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


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


**Тип ответа:** ct


```json
{
  "cache": {},
  "logger": {}
}
```


*Определено в:* `pkg/controller/volume/selinuxwarning/metrics.go`


**Тип ответа:** conntrackConfigurer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** proxyconfigapi.KubeProxyConntrackConfiguration


```json
{
  "MaxPerCore": 0,
  "Min": 0,
  "TCPEstablishedTimeout": null,
  "TCPCloseWaitTimeout": null,
  "TCPBeLiberal": false,
  "UDPTimeout": {},
  "UDPStreamTimeout": {}
}
```


*Определено в:* `pkg/proxy/apis/config/types.go`


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:60`



---


[function] name: writeIntStringFile file: pkg/proxy/conntrack/sysctls.go:201 returns_error: нет description: —


### writeIntStringFile (pkg/proxy/conntrack/sysctls.go:201)


writeIntStringFile is a function that performs operations based on the provided parameters and returns (filename string, value int).


```go
func writeIntStringFile((filename string, value int)) (filename string, value int)
```


**Тип ответа:** filename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/proxy/conntrack/sysctls.go:201`




## pkg/proxy/endpoint.go


📄 Исходный файл: `pkg/proxy/endpoint.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [IP](#ip-pkgproxyendpointgo97) `:97`

- 🔗 [IsLocal](#islocal-pkgproxyendpointgo107) `:107`

- 🔗 [IsReady](#isready-pkgproxyendpointgo112) `:112`

- 🔗 [IsServing](#isserving-pkgproxyendpointgo118) `:118`

- 🔗 [IsTerminating](#isterminating-pkgproxyendpointgo124) `:124`

- 🔗 [NodeHints](#nodehints-pkgproxyendpointgo134) `:134`

- 🔗 [Port](#port-pkgproxyendpointgo102) `:102`

- 🔗 [String](#string-pkgproxyendpointgo92) `:92`

- 🔗 [ZoneHints](#zonehints-pkgproxyendpointgo129) `:129`

- 🔗 [newBaseEndpointInfo](#newbaseendpointinfo-pkgproxyendpointgo138) `:138`


</details>


[function] name: IP file: pkg/proxy/endpoint.go:97 returns_error: нет description: IP returns just the IP part of the endpoint, it's a part of proxy.Endpoint interface.


### IP (pkg/proxy/endpoint.go:97)


IP returns just the IP part of the endpoint, it's a part of proxy.Endpoint interface.


```go
func (info *BaseEndpointInfo) IP(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:97`



---


[function] name: IsLocal file: pkg/proxy/endpoint.go:107 returns_error: нет description: IsLocal is part of proxy.Endpoint interface.


### IsLocal (pkg/proxy/endpoint.go:107)


IsLocal is part of proxy.Endpoint interface.


```go
func (info *BaseEndpointInfo) IsLocal(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:107`



---


[function] name: IsReady file: pkg/proxy/endpoint.go:112 returns_error: нет description: IsReady returns true if an endpoint is ready and not terminating.


### IsReady (pkg/proxy/endpoint.go:112)


IsReady returns true if an endpoint is ready and not terminating.


```go
func (info *BaseEndpointInfo) IsReady(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:112`



---


[function] name: IsServing file: pkg/proxy/endpoint.go:118 returns_error: нет description: IsServing returns true if an endpoint is ready, regardless of if the
endpoint is terminating.


### IsServing (pkg/proxy/endpoint.go:118)


IsServing returns true if an endpoint is ready, regardless of if the
endpoint is terminating.


```go
func (info *BaseEndpointInfo) IsServing(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:118`



---


[function] name: IsTerminating file: pkg/proxy/endpoint.go:124 returns_error: нет description: IsTerminating retruns true if an endpoint is terminating. For pods,
that is any pod with a deletion timestamp.


### IsTerminating (pkg/proxy/endpoint.go:124)


IsTerminating retruns true if an endpoint is terminating. For pods,
that is any pod with a deletion timestamp.


```go
func (info *BaseEndpointInfo) IsTerminating(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:124`



---


[function] name: NodeHints file: pkg/proxy/endpoint.go:134 returns_error: нет description: NodeHints returns the node hints for the endpoint.


### NodeHints (pkg/proxy/endpoint.go:134)


NodeHints returns the node hints for the endpoint.


```go
func (info *BaseEndpointInfo) NodeHints(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:134`



---


[function] name: Port file: pkg/proxy/endpoint.go:102 returns_error: нет description: Port returns just the Port part of the endpoint.


### Port (pkg/proxy/endpoint.go:102)


Port returns just the Port part of the endpoint.


```go
func (info *BaseEndpointInfo) Port(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:102`



---


[function] name: String file: pkg/proxy/endpoint.go:92 returns_error: нет description: String is part of proxy.Endpoint interface.


### String (pkg/proxy/endpoint.go:92)


String is part of proxy.Endpoint interface.


```go
func (info *BaseEndpointInfo) String(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:92`



---


[function] name: ZoneHints file: pkg/proxy/endpoint.go:129 returns_error: нет description: ZoneHints returns the zone hints for the endpoint.


### ZoneHints (pkg/proxy/endpoint.go:129)


ZoneHints returns the zone hints for the endpoint.


```go
func (info *BaseEndpointInfo) ZoneHints(()) ()
```


📍 *Расположение:* `pkg/proxy/endpoint.go:129`



---


[function] name: newBaseEndpointInfo file: pkg/proxy/endpoint.go:138 returns_error: нет description: —


### newBaseEndpointInfo (pkg/proxy/endpoint.go:138)


newBaseEndpointInfo is a function that performs operations based on the provided parameters and returns (ip string, port int, isLocal, ready, serving, terminating bool, zoneHints, nodeHints sets.Set[string]).


```go
func newBaseEndpointInfo((ip string, port int, isLocal, ready, serving, terminating bool, zoneHints, nodeHints sets.Set[string])) (ip string, port int, isLocal, ready, serving, terminating bool, zoneHints, nodeHints sets.Set[string])
```


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


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


**Тип ответа:** isLocal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ready


```json
{
  "state": {},
  "lastErr": {},
  "generation": 0,
  "lock": {},
  "restartLock": {},
  "waitCh": {},
  "clock": {},
  "lastStateChangeTime": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/ready.go`


**Тип ответа:** serving


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** terminating


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** zoneHints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeHints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


📍 *Расположение:* `pkg/proxy/endpoint.go:138`




## pkg/proxy/endpointschangetracker.go


📄 Исходный файл: `pkg/proxy/endpointschangetracker.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [EndpointSliceUpdate](#endpointsliceupdate-pkgproxyendpointschangetrackergo81) `:81`

- 🔗 [LocalReadyEndpoints](#localreadyendpoints-pkgproxyendpointschangetrackergo276) `:276`

- 🔗 [NewEndpointsChangeTracker](#newendpointschangetracker-pkgproxyendpointschangetrackergo62) `:62`

- 🔗 [Update](#update-pkgproxyendpointschangetrackergo193) `:193`

- 🔗 [checkoutChanges](#checkoutchanges-pkgproxyendpointschangetrackergo120) `:120`

- 🔗 [checkoutTriggerTimes](#checkouttriggertimes-pkgproxyendpointschangetrackergo128) `:128`

- 🔗 [getLastChangeTriggerTime](#getlastchangetriggertime-pkgproxyendpointschangetrackergo147) `:147`

- 🔗 [getLocalReadyEndpointIPs](#getlocalreadyendpointips-pkgproxyendpointschangetrackergo252) `:252`

- 🔗 [merge](#merge-pkgproxyendpointschangetrackergo238) `:238`

- 🔗 [unmerge](#unmerge-pkgproxyendpointschangetrackergo245) `:245`


</details>


[function] name: EndpointSliceUpdate file: pkg/proxy/endpointschangetracker.go:81 returns_error: нет description: EndpointSliceUpdate updates the EndpointsChangeTracker by adding/updating or removing
endpointSlice (depending on remove


### EndpointSliceUpdate (pkg/proxy/endpointschangetracker.go:81)


EndpointSliceUpdate updates the EndpointsChangeTracker by adding/updating or removing
endpointSlice (depending on removeSlice). It returns true if this update contained a
change that needs to be synced; note that this is different from the return value of
ServiceChangeTracker.Update().


```go
func (ect *EndpointsChangeTracker) EndpointSliceUpdate((endpointSlice *discovery.EndpointSlice, removeSlice bool)) (endpointSlice *discovery.EndpointSlice, removeSlice bool)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** removeSlice


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:81`



---


[function] name: LocalReadyEndpoints file: pkg/proxy/endpointschangetracker.go:276 returns_error: нет description: LocalReadyEndpoints returns a map of Service names to the number of local ready
endpoints for that service.


### LocalReadyEndpoints (pkg/proxy/endpointschangetracker.go:276)


LocalReadyEndpoints returns a map of Service names to the number of local ready
endpoints for that service.


```go
func (em EndpointsMap) LocalReadyEndpoints(()) ()
```


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:276`



---


[function] name: NewEndpointsChangeTracker file: pkg/proxy/endpointschangetracker.go:62 returns_error: нет description: NewEndpointsChangeTracker initializes an EndpointsChangeTracker


### NewEndpointsChangeTracker (pkg/proxy/endpointschangetracker.go:62)


NewEndpointsChangeTracker initializes an EndpointsChangeTracker


```go
func NewEndpointsChangeTracker((ipFamily v1.IPFamily, nodeName string, makeEndpointInfo makeEndpointFunc, processEndpointsMapChange processEndpointsMapChangeFunc)) (ipFamily v1.IPFamily, nodeName string, makeEndpointInfo makeEndpointFunc, processEndpointsMapChange processEndpointsMapChangeFunc)
```


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** makeEndpointInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** makeEndpointFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** processEndpointsMapChange


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** processEndpointsMapChangeFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:62`



---


[function] name: Update file: pkg/proxy/endpointschangetracker.go:193 returns_error: нет description: Update updates em based on the changes in ect, returns information about the diff since
the last Update, triggers proces


### Update (pkg/proxy/endpointschangetracker.go:193)


Update updates em based on the changes in ect, returns information about the diff since
the last Update, triggers processEndpointsMapChange on every change, and clears the
changes map.


```go
func (em EndpointsMap) Update((ect *EndpointsChangeTracker)) (ect *EndpointsChangeTracker)
```


**Тип запроса:** EndpointsChangeTracker


```json
{
  "lock": {},
  "processEndpointsMapChange": {},
  "addressType": {},
  "endpointSliceCache": null,
  "lastChangeTriggerTimes": {},
  "trackerStartTime": {}
}
```


*Определено в:* `pkg/proxy/endpointschangetracker.go`


**Тип ответа:** ect


```json
{
  "cache": {},
  "logger": {}
}
```


*Определено в:* `pkg/controller/volume/selinuxwarning/metrics.go`


**Тип ответа:** EndpointsChangeTracker


```json
{
  "lock": {},
  "processEndpointsMapChange": {},
  "addressType": {},
  "endpointSliceCache": null,
  "lastChangeTriggerTimes": {},
  "trackerStartTime": {}
}
```


*Определено в:* `pkg/proxy/endpointschangetracker.go`


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:193`



---


[function] name: checkoutChanges file: pkg/proxy/endpointschangetracker.go:120 returns_error: нет description: checkoutChanges returns a map of pending endpointsChanges and marks them as
applied.


### checkoutChanges (pkg/proxy/endpointschangetracker.go:120)


checkoutChanges returns a map of pending endpointsChanges and marks them as
applied.


```go
func (ect *EndpointsChangeTracker) checkoutChanges(()) ()
```


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:120`



---


[function] name: checkoutTriggerTimes file: pkg/proxy/endpointschangetracker.go:128 returns_error: нет description: checkoutTriggerTimes applies the locally cached trigger times to a map of
trigger times that have been passed in and emp


### checkoutTriggerTimes (pkg/proxy/endpointschangetracker.go:128)


checkoutTriggerTimes applies the locally cached trigger times to a map of
trigger times that have been passed in and empties the local cache.


```go
func (ect *EndpointsChangeTracker) checkoutTriggerTimes((lastChangeTriggerTimes *map[types.NamespacedName][]time.Time)) (lastChangeTriggerTimes *map[types.NamespacedName][]time.Time)
```


**Тип запроса:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** lastChangeTriggerTimes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


**Тип ответа:** time.Time


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:128`



---


[function] name: getLastChangeTriggerTime file: pkg/proxy/endpointschangetracker.go:147 returns_error: нет description: getLastChangeTriggerTime returns the time.Time value of the
EndpointsLastChangeTriggerTime annotation stored in the give


### getLastChangeTriggerTime (pkg/proxy/endpointschangetracker.go:147)


getLastChangeTriggerTime returns the time.Time value of the
EndpointsLastChangeTriggerTime annotation stored in the given endpoints
object or the "zero" time if the annotation wasn't set or was set
incorrectly.


```go
func getLastChangeTriggerTime((annotations map[string]string)) (annotations map[string]string)
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


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:147`



---


[function] name: getLocalReadyEndpointIPs file: pkg/proxy/endpointschangetracker.go:252 returns_error: нет description: getLocalEndpointIPs returns endpoints IPs if given endpoint is local - local means the endpoint is running in same host 


### getLocalReadyEndpointIPs (pkg/proxy/endpointschangetracker.go:252)


getLocalEndpointIPs returns endpoints IPs if given endpoint is local - local means the endpoint is running in same host as kube-proxy.


```go
func (em EndpointsMap) getLocalReadyEndpointIPs(()) ()
```


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:252`



---


[function] name: merge file: pkg/proxy/endpointschangetracker.go:238 returns_error: нет description: Merge ensures that the current EndpointsMap contains all <service, endpoints> pairs from the EndpointsMap passed in.


### merge (pkg/proxy/endpointschangetracker.go:238)


Merge ensures that the current EndpointsMap contains all <service, endpoints> pairs from the EndpointsMap passed in.


```go
func (em EndpointsMap) merge((other EndpointsMap)) (other EndpointsMap)
```


**Тип ответа:** other


```json
{
  "OS": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ordering/structs/doc.go`


**Тип ответа:** EndpointsMap


```json
{
  "UpdatedServices": {},
  "ConntrackCleanupRequired": false,
  "LastChangeTriggerTimes": {}
}
```


*Определено в:* `pkg/proxy/endpointschangetracker.go`


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:238`



---


[function] name: unmerge file: pkg/proxy/endpointschangetracker.go:245 returns_error: нет description: Unmerge removes the <service, endpoints> pairs from the current EndpointsMap which are contained in the EndpointsMap pas


### unmerge (pkg/proxy/endpointschangetracker.go:245)


Unmerge removes the <service, endpoints> pairs from the current EndpointsMap which are contained in the EndpointsMap passed in.


```go
func (em EndpointsMap) unmerge((other EndpointsMap)) (other EndpointsMap)
```


**Тип ответа:** other


```json
{
  "OS": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ordering/structs/doc.go`


**Тип ответа:** EndpointsMap


```json
{
  "UpdatedServices": {},
  "ConntrackCleanupRequired": false,
  "LastChangeTriggerTimes": {}
}
```


*Определено в:* `pkg/proxy/endpointschangetracker.go`


📍 *Расположение:* `pkg/proxy/endpointschangetracker.go:245`




## pkg/proxy/endpointslicecache.go


📄 Исходный файл: `pkg/proxy/endpointslicecache.go`


<details open>
<summary><b>Функции в этом файле (16)</b></summary>


- 🔗 [Len](#len-pkgproxyendpointslicecachego336) `:336`

- 🔗 [Less](#less-pkgproxyendpointslicecachego342) `:342`

- 🔗 [NewEndpointSliceCache](#newendpointslicecache-pkgproxyendpointslicecachego70) `:70`

- 🔗 [Swap](#swap-pkgproxyendpointslicecachego339) `:339`

- 🔗 [addEndpoints](#addendpoints-pkgproxyendpointslicecachego197) `:197`

- 🔗 [checkoutChanges](#checkoutchanges-pkgproxyendpointslicecachego122) `:122`

- 🔗 [endpointInfoByServicePort](#endpointinfobyserviceport-pkgproxyendpointslicecachego168) `:168`

- 🔗 [endpointSliceCacheKeys](#endpointslicecachekeys-pkgproxyendpointslicecachego322) `:322`

- 🔗 [endpointsMapFromEndpointInfo](#endpointsmapfromendpointinfo-pkgproxyendpointslicecachego291) `:291`

- 🔗 [esDataChanged](#esdatachanged-pkgproxyendpointslicecachego261) `:261`

- 🔗 [formatEndpointsList](#formatendpointslist-pkgproxyendpointslicecachego313) `:313`

- 🔗 [getEndpointsMap](#getendpointsmap-pkgproxyendpointslicecachego162) `:162`

- 🔗 [isLocal](#islocal-pkgproxyendpointslicecachego255) `:255`

- 🔗 [newEndpointSliceTracker](#newendpointslicetracker-pkgproxyendpointslicecachego82) `:82`

- 🔗 [standardEndpointInfo](#standardendpointinfo-pkgproxyendpointslicecachego90) `:90`

- 🔗 [updatePending](#updatepending-pkgproxyendpointslicecachego95) `:95`


</details>


[function] name: Len file: pkg/proxy/endpointslicecache.go:336 returns_error: нет description: —


### Len (pkg/proxy/endpointslicecache.go:336)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (e byEndpoint) Len(()) ()
```


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:336`



---


[function] name: Less file: pkg/proxy/endpointslicecache.go:342 returns_error: нет description: —


### Less (pkg/proxy/endpointslicecache.go:342)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (e byEndpoint) Less((i, j int)) (i, j int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:342`



---


[function] name: NewEndpointSliceCache file: pkg/proxy/endpointslicecache.go:70 returns_error: нет description: NewEndpointSliceCache initializes an EndpointSliceCache.


### NewEndpointSliceCache (pkg/proxy/endpointslicecache.go:70)


NewEndpointSliceCache initializes an EndpointSliceCache.


```go
func NewEndpointSliceCache((nodeName string, makeEndpointInfo makeEndpointFunc)) (nodeName string, makeEndpointInfo makeEndpointFunc)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** makeEndpointInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** makeEndpointFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:70`



---


[function] name: Swap file: pkg/proxy/endpointslicecache.go:339 returns_error: нет description: —


### Swap (pkg/proxy/endpointslicecache.go:339)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (e byEndpoint) Swap((i, j int)) (i, j int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:339`



---


[function] name: addEndpoints file: pkg/proxy/endpointslicecache.go:197 returns_error: нет description: addEndpoints adds an Endpoint for each unique endpoint.


### addEndpoints (pkg/proxy/endpointslicecache.go:197)


addEndpoints adds an Endpoint for each unique endpoint.


```go
func (cache *EndpointSliceCache) addEndpoints((svcPortName *ServicePortName, portNum int, endpointSet map[string]Endpoint, endpoints []discovery.Endpoint)) (svcPortName *ServicePortName, portNum int, endpointSet map[string]Endpoint, endpoints []discovery.Endpoint)
```


**Тип запроса:** ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** svcPortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** portNum


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** discovery.Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:197`



---


[function] name: checkoutChanges file: pkg/proxy/endpointslicecache.go:122 returns_error: нет description: checkoutChanges returns a map of all endpointsChanges that are
pending and then marks them as applied.


### checkoutChanges (pkg/proxy/endpointslicecache.go:122)


checkoutChanges returns a map of all endpointsChanges that are
pending and then marks them as applied.


```go
func (cache *EndpointSliceCache) checkoutChanges(()) ()
```


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:122`



---


[function] name: endpointInfoByServicePort file: pkg/proxy/endpointslicecache.go:168 returns_error: нет description: endpointInfoByServicePort groups endpoint info by service port name and address.


### endpointInfoByServicePort (pkg/proxy/endpointslicecache.go:168)


endpointInfoByServicePort groups endpoint info by service port name and address.


```go
func (cache *EndpointSliceCache) endpointInfoByServicePort((serviceNN types.NamespacedName, sliceDataByName endpointSliceDataByName)) (serviceNN types.NamespacedName, sliceDataByName endpointSliceDataByName)
```


**Тип ответа:** serviceNN


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


**Тип ответа:** sliceDataByName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointSliceDataByName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:168`



---


[function] name: endpointSliceCacheKeys file: pkg/proxy/endpointslicecache.go:322 returns_error: да description: endpointSliceCacheKeys returns cache keys used for a given EndpointSlice.


### endpointSliceCacheKeys (pkg/proxy/endpointslicecache.go:322)


endpointSliceCacheKeys returns cache keys used for a given EndpointSlice.


```go
func endpointSliceCacheKeys((types.NamespacedName, string, error)) (types.NamespacedName, string, error)
```


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `types.NamespacedName`, `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:322`



---


[function] name: endpointsMapFromEndpointInfo file: pkg/proxy/endpointslicecache.go:291 returns_error: нет description: endpointsMapFromEndpointInfo computes an endpointsMap from endpointInfo that
has been grouped by service port and IP.


### endpointsMapFromEndpointInfo (pkg/proxy/endpointslicecache.go:291)


endpointsMapFromEndpointInfo computes an endpointsMap from endpointInfo that
has been grouped by service port and IP.


```go
func endpointsMapFromEndpointInfo((endpointInfoBySP map[ServicePortName]map[string]Endpoint)) (endpointInfoBySP map[ServicePortName]map[string]Endpoint)
```


**Тип ответа:** endpointInfoBySP


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:291`



---


[function] name: esDataChanged file: pkg/proxy/endpointslicecache.go:261 returns_error: нет description: esDataChanged returns true if the esData parameter should be set as a new
pending value in the cache.


### esDataChanged (pkg/proxy/endpointslicecache.go:261)


esDataChanged returns true if the esData parameter should be set as a new
pending value in the cache.


```go
func (cache *EndpointSliceCache) esDataChanged((serviceKey types.NamespacedName, sliceKey string, esData *endpointSliceData)) (serviceKey types.NamespacedName, sliceKey string, esData *endpointSliceData)
```


**Тип запроса:** endpointSliceData


```json
{
  "endpointSlice": null,
  "remove": false
}
```


*Определено в:* `pkg/proxy/endpointslicecache.go`


**Тип ответа:** serviceKey


```json
{
  "Namespace": "string",
  "Name": "string",
  "Port": 0
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/apiserver/handler_discovery.go`


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


**Тип ответа:** sliceKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** esData


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointSliceData


```json
{
  "endpointSlice": null,
  "remove": false
}
```


*Определено в:* `pkg/proxy/endpointslicecache.go`


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:261`



---


[function] name: formatEndpointsList file: pkg/proxy/endpointslicecache.go:313 returns_error: нет description: formatEndpointsList returns a string list converted from an endpoints list.


### formatEndpointsList (pkg/proxy/endpointslicecache.go:313)


formatEndpointsList returns a string list converted from an endpoints list.


```go
func formatEndpointsList((endpoints []Endpoint)) (endpoints []Endpoint)
```


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:313`



---


[function] name: getEndpointsMap file: pkg/proxy/endpointslicecache.go:162 returns_error: нет description: getEndpointsMap computes an EndpointsMap for a given set of EndpointSlices.


### getEndpointsMap (pkg/proxy/endpointslicecache.go:162)


getEndpointsMap computes an EndpointsMap for a given set of EndpointSlices.


```go
func (cache *EndpointSliceCache) getEndpointsMap((serviceNN types.NamespacedName, sliceDataByName endpointSliceDataByName)) (serviceNN types.NamespacedName, sliceDataByName endpointSliceDataByName)
```


**Тип ответа:** serviceNN


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


**Тип ответа:** sliceDataByName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointSliceDataByName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:162`



---


[function] name: isLocal file: pkg/proxy/endpointslicecache.go:255 returns_error: нет description: —


### isLocal (pkg/proxy/endpointslicecache.go:255)


isLocal is a method that performs operations based on the provided parameters and returns (nodeName string).


```go
func (cache *EndpointSliceCache) isLocal((nodeName string)) (nodeName string)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:255`



---


[function] name: newEndpointSliceTracker file: pkg/proxy/endpointslicecache.go:82 returns_error: нет description: newEndpointSliceTracker initializes an endpointSliceTracker.


### newEndpointSliceTracker (pkg/proxy/endpointslicecache.go:82)


newEndpointSliceTracker initializes an endpointSliceTracker.


```go
func newEndpointSliceTracker(()) ()
```


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:82`



---


[function] name: standardEndpointInfo file: pkg/proxy/endpointslicecache.go:90 returns_error: нет description: standardEndpointInfo is the default makeEndpointFunc.


### standardEndpointInfo (pkg/proxy/endpointslicecache.go:90)


standardEndpointInfo is the default makeEndpointFunc.


```go
func standardEndpointInfo((ep *BaseEndpointInfo, _ *ServicePortName)) (ep *BaseEndpointInfo, _ *ServicePortName)
```


**Тип запроса:** BaseEndpointInfo


```json
{
  "ip": "string",
  "port": 0,
  "endpoint": "string",
  "isLocal": false,
  "ready": false,
  "serving": false,
  "terminating": false,
  "zoneHints": {},
  "nodeHints": {}
}
```


*Определено в:* `pkg/proxy/endpoint.go`


**Тип запроса:** ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** ep


```json
{
  "PodMaxInUnschedulablePodsDuration": {}
}
```


*Определено в:* `cmd/kube-scheduler/app/options/deprecated.go`


**Тип ответа:** BaseEndpointInfo


```json
{
  "ip": "string",
  "port": 0,
  "endpoint": "string",
  "isLocal": false,
  "ready": false,
  "serving": false,
  "terminating": false,
  "zoneHints": {},
  "nodeHints": {}
}
```


*Определено в:* `pkg/proxy/endpoint.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:90`



---


[function] name: updatePending file: pkg/proxy/endpointslicecache.go:95 returns_error: нет description: updatePending updates a pending slice in the cache.


### updatePending (pkg/proxy/endpointslicecache.go:95)


updatePending updates a pending slice in the cache.


```go
func (cache *EndpointSliceCache) updatePending((endpointSlice *discovery.EndpointSlice, remove bool)) (endpointSlice *discovery.EndpointSlice, remove bool)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** remove


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/endpointslicecache.go:95`




## pkg/proxy/healthcheck/common.go


📄 Исходный файл: `pkg/proxy/healthcheck/common.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [Listen](#listen-pkgproxyhealthcheckcommongo51) `:51`

- 🔗 [New](#new-pkgproxyhealthcheckcommongo60) `:60`


</details>


[function] name: Listen file: pkg/proxy/healthcheck/common.go:51 returns_error: да description: —


### Listen (pkg/proxy/healthcheck/common.go:51)


Listen is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (stdNetListener) Listen((net.Listener, error)) (net.Listener, error)
```


**Тип ответа:** net.Listener


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `net.Listener`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/healthcheck/common.go:51`



---


[function] name: New file: pkg/proxy/healthcheck/common.go:60 returns_error: нет description: —


### New (pkg/proxy/healthcheck/common.go:60)


New is a method that performs operations based on the provided parameters and returns (handler http.Handler).


```go
func (stdHTTPServerFactory) New((handler http.Handler)) (handler http.Handler)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** http.Handler


```json
{
  "notify": [],
  "final": {},
  "once": {}
}
```


*Определено в:* `pkg/util/interrupt/interrupt.go`


📍 *Расположение:* `pkg/proxy/healthcheck/common.go:60`




## pkg/proxy/healthcheck/proxy_health.go


📄 Исходный файл: `pkg/proxy/healthcheck/proxy_health.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [Health](#health-pkgproxyhealthcheckproxy_healthgo131) `:131`

- 🔗 [NewProxyHealthServer](#newproxyhealthserver-pkgproxyhealthcheckproxy_healthgo89) `:89`

- 🔗 [NodeEligible](#nodeeligible-pkgproxyhealthcheckproxy_healthgo180) `:180`

- 🔗 [QueuedUpdate](#queuedupdate-pkgproxyhealthcheckproxy_healthgo121) `:121`

- 🔗 [Run](#run-pkgproxyhealthcheckproxy_healthgo200) `:200`

- 🔗 [ServeHTTP](#servehttp-pkgproxyhealthcheckproxy_healthgo223) `:223`

- 🔗 [ServeHTTP](#servehttp-pkgproxyhealthcheckproxy_healthgo255) `:255`

- 🔗 [Updated](#updated-pkgproxyhealthcheckproxy_healthgo109) `:109`

- 🔗 [newProxyHealthServer](#newproxyhealthserver-pkgproxyhealthcheckproxy_healthgo93) `:93`


</details>


[function] name: Health file: pkg/proxy/healthcheck/proxy_health.go:131 returns_error: нет description: Health returns proxy health status.


### Health (pkg/proxy/healthcheck/proxy_health.go:131)


Health returns proxy health status.


```go
func (hs *ProxyHealthServer) Health(()) ()
```


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:131`



---


[function] name: NewProxyHealthServer file: pkg/proxy/healthcheck/proxy_health.go:89 returns_error: нет description: NewProxyHealthServer returns a proxy health http server.


### NewProxyHealthServer (pkg/proxy/healthcheck/proxy_health.go:89)


NewProxyHealthServer returns a proxy health http server.


```go
func NewProxyHealthServer((addr string, healthTimeout time.Duration, nodeManager nodeManager)) (addr string, healthTimeout time.Duration, nodeManager nodeManager)
```


**Тип ответа:** addr


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** healthTimeout


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


**Тип ответа:** nodeManager


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeManager


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:89`



---


[function] name: NodeEligible file: pkg/proxy/healthcheck/proxy_health.go:180 returns_error: нет description: NodeEligible returns if node is eligible or not. Eligible is defined
as being: not tainted by ToBeDeletedTaint and not d


### NodeEligible (pkg/proxy/healthcheck/proxy_health.go:180)


NodeEligible returns if node is eligible or not. Eligible is defined
as being: not tainted by ToBeDeletedTaint and not deleted.


```go
func (hs *ProxyHealthServer) NodeEligible(()) ()
```


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:180`



---


[function] name: QueuedUpdate file: pkg/proxy/healthcheck/proxy_health.go:121 returns_error: нет description: QueuedUpdate should be called when the proxier receives a Service or Endpoints event
from API Server containing informat


### QueuedUpdate (pkg/proxy/healthcheck/proxy_health.go:121)


QueuedUpdate should be called when the proxier receives a Service or Endpoints event
from API Server containing information that requires updating service rules. It
indicates that the proxier for the given IP family has received changes but has not
yet pushed them to its backend. If the proxier does not call Updated within the
healthTimeout time then it will be considered unhealthy.


```go
func (hs *ProxyHealthServer) QueuedUpdate((ipFamily v1.IPFamily)) (ipFamily v1.IPFamily)
```


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:121`



---


[function] name: Run file: pkg/proxy/healthcheck/proxy_health.go:200 returns_error: нет description: Run starts the healthz HTTP server and blocks until it exits.


### Run (pkg/proxy/healthcheck/proxy_health.go:200)


Run starts the healthz HTTP server and blocks until it exits.


```go
func (hs *ProxyHealthServer) Run((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:200`



---


[function] name: ServeHTTP file: pkg/proxy/healthcheck/proxy_health.go:223 returns_error: нет description: —


### ServeHTTP (pkg/proxy/healthcheck/proxy_health.go:223)


ServeHTTP is a method that performs operations based on the provided parameters and returns (resp http.ResponseWriter, _ *http.Request).


```go
func (h healthzHandler) ServeHTTP((resp http.ResponseWriter, _ *http.Request)) (resp http.ResponseWriter, _ *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** resp


```json
{
  "w": {},
  "ctx": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/peerproxy/peerproxy_handler.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:223`



---


[function] name: ServeHTTP file: pkg/proxy/healthcheck/proxy_health.go:255 returns_error: нет description: —


### ServeHTTP (pkg/proxy/healthcheck/proxy_health.go:255)


ServeHTTP is a method that performs operations based on the provided parameters and returns (resp http.ResponseWriter, req *http.Request).


```go
func (h livezHandler) ServeHTTP((resp http.ResponseWriter, req *http.Request)) (resp http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** resp


```json
{
  "w": {},
  "ctx": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/peerproxy/peerproxy_handler.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


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


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:255`



---


[function] name: Updated file: pkg/proxy/healthcheck/proxy_health.go:109 returns_error: нет description: Updated should be called when the proxier of the given IP family has successfully updated
the service rules to reflect t


### Updated (pkg/proxy/healthcheck/proxy_health.go:109)


Updated should be called when the proxier of the given IP family has successfully updated
the service rules to reflect the current state and should be considered healthy now.


```go
func (hs *ProxyHealthServer) Updated((ipFamily v1.IPFamily)) (ipFamily v1.IPFamily)
```


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:109`



---


[function] name: newProxyHealthServer file: pkg/proxy/healthcheck/proxy_health.go:93 returns_error: нет description: —


### newProxyHealthServer (pkg/proxy/healthcheck/proxy_health.go:93)


newProxyHealthServer is a function that performs operations based on the provided parameters and returns (listener listener, httpServerFactory httpServerFactory, c clock.Clock, addr string, healthTimeout time.Duration, nodeManager nodeManager).


```go
func newProxyHealthServer((listener listener, httpServerFactory httpServerFactory, c clock.Clock, addr string, healthTimeout time.Duration, nodeManager nodeManager)) (listener listener, httpServerFactory httpServerFactory, c clock.Clock, addr string, healthTimeout time.Duration, nodeManager nodeManager)
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


**Тип ответа:** httpServerFactory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** httpServerFactory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** clock.Clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** addr


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** healthTimeout


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


**Тип ответа:** nodeManager


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeManager


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/healthcheck/proxy_health.go:93`




## pkg/proxy/healthcheck/service_health.go


📄 Исходный файл: `pkg/proxy/healthcheck/service_health.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [NewFakeServiceHealthServer](#newfakeservicehealthserver-pkgproxyhealthcheckservice_healthgo279) `:279`

- 🔗 [NewServiceHealthServer](#newservicehealthserver-pkgproxyhealthcheckservice_healthgo86) `:86`

- 🔗 [ServeHTTP](#servehttp-pkgproxyhealthcheckservice_healthgo223) `:223`

- 🔗 [SyncEndpoints](#syncendpoints-pkgproxyhealthcheckservice_healthgo256) `:256`

- 🔗 [SyncEndpoints](#syncendpoints-pkgproxyhealthcheckservice_healthgo289) `:289`

- 🔗 [SyncServices](#syncservices-pkgproxyhealthcheckservice_healthgo104) `:104`

- 🔗 [SyncServices](#syncservices-pkgproxyhealthcheckservice_healthgo284) `:284`

- 🔗 [closeAll](#closeall-pkgproxyhealthcheckservice_healthgo200) `:200`

- 🔗 [listenAndServeAll](#listenandserveall-pkgproxyhealthcheckservice_healthgo163) `:163`

- 🔗 [newServiceHealthServer](#newservicehealthserver-pkgproxyhealthcheckservice_healthgo60) `:60`


</details>


[function] name: NewFakeServiceHealthServer file: pkg/proxy/healthcheck/service_health.go:279 returns_error: нет description: NewFakeServiceHealthServer allocates a new fake service healthcheck server manager


### NewFakeServiceHealthServer (pkg/proxy/healthcheck/service_health.go:279)


NewFakeServiceHealthServer allocates a new fake service healthcheck server manager


```go
func NewFakeServiceHealthServer(()) ()
```


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:279`



---


[function] name: NewServiceHealthServer file: pkg/proxy/healthcheck/service_health.go:86 returns_error: нет description: NewServiceHealthServer allocates a new service healthcheck server manager


### NewServiceHealthServer (pkg/proxy/healthcheck/service_health.go:86)


NewServiceHealthServer allocates a new service healthcheck server manager


```go
func NewServiceHealthServer((nodeName string, recorder events.EventRecorder, nodePortAddresses *proxyutil.NodePortAddresses, healthzServer proxyHealthChecker)) (nodeName string, recorder events.EventRecorder, nodePortAddresses *proxyutil.NodePortAddresses, healthzServer proxyHealthChecker)
```


**Тип запроса:** proxyutil.NodePortAddresses


```json
{
  "cidrStrings": [],
  "cidrs": [],
  "containsIPv4Loopback": false,
  "matchAll": false
}
```


*Определено в:* `pkg/proxy/util/nodeport_addresses.go`


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** recorder


```json
{
  "mu": {},
  "warnings": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/token/cache/cached_token_authenticator.go`


**Тип ответа:** events.EventRecorder


```json
{
  "recorder": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** nodePortAddresses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyutil.NodePortAddresses


```json
{
  "cidrStrings": [],
  "cidrs": [],
  "containsIPv4Loopback": false,
  "matchAll": false
}
```


*Определено в:* `pkg/proxy/util/nodeport_addresses.go`


**Тип ответа:** healthzServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyHealthChecker


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:86`



---


[function] name: ServeHTTP file: pkg/proxy/healthcheck/service_health.go:223 returns_error: нет description: —


### ServeHTTP (pkg/proxy/healthcheck/service_health.go:223)


ServeHTTP is a method that performs operations based on the provided parameters and returns (resp http.ResponseWriter, req *http.Request).


```go
func (h hcHandler) ServeHTTP((resp http.ResponseWriter, req *http.Request)) (resp http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** resp


```json
{
  "w": {},
  "ctx": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/peerproxy/peerproxy_handler.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


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


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:223`



---


[function] name: SyncEndpoints file: pkg/proxy/healthcheck/service_health.go:256 returns_error: нет description: —


### SyncEndpoints (pkg/proxy/healthcheck/service_health.go:256)


SyncEndpoints is a method that performs operations based on the provided parameters and returns (newEndpoints map[types.NamespacedName]int).


```go
func (hcs *server) SyncEndpoints((newEndpoints map[types.NamespacedName]int)) (newEndpoints map[types.NamespacedName]int)
```


**Тип ответа:** newEndpoints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:256`



---


[function] name: SyncEndpoints file: pkg/proxy/healthcheck/service_health.go:289 returns_error: нет description: SyncEndpoints is part of ServiceHealthServer


### SyncEndpoints (pkg/proxy/healthcheck/service_health.go:289)


SyncEndpoints is part of ServiceHealthServer


```go
func (fake FakeServiceHealthServer) SyncEndpoints((_ map[types.NamespacedName]int)) (_ map[types.NamespacedName]int)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:289`



---


[function] name: SyncServices file: pkg/proxy/healthcheck/service_health.go:104 returns_error: нет description: —


### SyncServices (pkg/proxy/healthcheck/service_health.go:104)


SyncServices is a method that performs operations based on the provided parameters and returns (newServices map[types.NamespacedName]uint16).


```go
func (hcs *server) SyncServices((newServices map[types.NamespacedName]uint16)) (newServices map[types.NamespacedName]uint16)
```


**Тип ответа:** newServices


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:104`



---


[function] name: SyncServices file: pkg/proxy/healthcheck/service_health.go:284 returns_error: нет description: SyncServices is part of ServiceHealthServer


### SyncServices (pkg/proxy/healthcheck/service_health.go:284)


SyncServices is part of ServiceHealthServer


```go
func (fake FakeServiceHealthServer) SyncServices((_ map[types.NamespacedName]uint16)) (_ map[types.NamespacedName]uint16)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** types.NamespacedName


```json
{
  "Namespace": "string",
  "Name": "string"
}
```


*Определено в:* `test/e2e/framework/namespacedname.go`


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:284`



---


[function] name: closeAll file: pkg/proxy/healthcheck/service_health.go:200 returns_error: нет description: —


### closeAll (pkg/proxy/healthcheck/service_health.go:200)


closeAll is a method that performs operations based on the provided parameters and returns ().


```go
func (hcI *hcInstance) closeAll(()) ()
```


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:200`



---


[function] name: listenAndServeAll file: pkg/proxy/healthcheck/service_health.go:163 returns_error: нет description: listenAll opens health check port on all the addresses provided


### listenAndServeAll (pkg/proxy/healthcheck/service_health.go:163)


listenAll opens health check port on all the addresses provided


```go
func (hcI *hcInstance) listenAndServeAll((hcs *server)) (hcs *server)
```


**Тип запроса:** server


```json
{
  "socketName": "string",
  "socketDir": "string",
  "mutex": {},
  "wg": {},
  "grpc": null,
  "rhandler": {},
  "chandler": {},
  "clients": {},
  "lastError": {}
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/plugin/v1beta1/server.go`


**Тип ответа:** hcs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** server


```json
{
  "socketName": "string",
  "socketDir": "string",
  "mutex": {},
  "wg": {},
  "grpc": null,
  "rhandler": {},
  "chandler": {},
  "clients": {},
  "lastError": {}
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/plugin/v1beta1/server.go`


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:163`



---


[function] name: newServiceHealthServer file: pkg/proxy/healthcheck/service_health.go:60 returns_error: нет description: —


### newServiceHealthServer (pkg/proxy/healthcheck/service_health.go:60)


newServiceHealthServer is a function that performs operations based on the provided parameters and returns (nodeName string, recorder events.EventRecorder, listener listener, factory httpServerFactory, nodePortAddresses *proxyutil.NodePortAddresses, healthzServer proxyHealthChecker).


```go
func newServiceHealthServer((nodeName string, recorder events.EventRecorder, listener listener, factory httpServerFactory, nodePortAddresses *proxyutil.NodePortAddresses, healthzServer proxyHealthChecker)) (nodeName string, recorder events.EventRecorder, listener listener, factory httpServerFactory, nodePortAddresses *proxyutil.NodePortAddresses, healthzServer proxyHealthChecker)
```


**Тип запроса:** proxyutil.NodePortAddresses


```json
{
  "cidrStrings": [],
  "cidrs": [],
  "containsIPv4Loopback": false,
  "matchAll": false
}
```


*Определено в:* `pkg/proxy/util/nodeport_addresses.go`


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** recorder


```json
{
  "mu": {},
  "warnings": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/token/cache/cached_token_authenticator.go`


**Тип ответа:** events.EventRecorder


```json
{
  "recorder": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


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


**Тип ответа:** factory


```json
{
  "clientGetter": {},
  "openAPIParser": null,
  "oapi": null,
  "parser": {},
  "getter": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/util/factory_client_access.go`


**Тип ответа:** httpServerFactory


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodePortAddresses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyutil.NodePortAddresses


```json
{
  "cidrStrings": [],
  "cidrs": [],
  "containsIPv4Loopback": false,
  "matchAll": false
}
```


*Определено в:* `pkg/proxy/util/nodeport_addresses.go`


**Тип ответа:** healthzServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyHealthChecker


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/healthcheck/service_health.go:60`




## pkg/proxy/iptables/cleanup.go


📄 Исходный файл: `pkg/proxy/iptables/cleanup.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [CleanupLeftovers](#cleanupleftovers-pkgproxyiptablescleanupgo33) `:33`

- 🔗 [cleanupLeftoversForFamily](#cleanupleftoversforfamily-pkgproxyiptablescleanupgo41) `:41`


</details>


[function] name: CleanupLeftovers file: pkg/proxy/iptables/cleanup.go:33 returns_error: нет description: CleanupLeftovers removes all iptables rules and chains created by the Proxier
It returns true if an error was encountere


### CleanupLeftovers (pkg/proxy/iptables/cleanup.go:33)


CleanupLeftovers removes all iptables rules and chains created by the Proxier
It returns true if an error was encountered. Errors are logged.


```go
func CleanupLeftovers((encounteredError bool)) (encounteredError bool)
```


**Тип ответа:** encounteredError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/cleanup.go:33`



---


[function] name: cleanupLeftoversForFamily file: pkg/proxy/iptables/cleanup.go:41 returns_error: нет description: —


### cleanupLeftoversForFamily (pkg/proxy/iptables/cleanup.go:41)


cleanupLeftoversForFamily is a function that performs operations based on the provided parameters and may return an error.


```go
func cleanupLeftoversForFamily((encounteredError bool)) (encounteredError bool)
```


**Тип ответа:** encounteredError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/cleanup.go:41`




## pkg/proxy/iptables/proxier.go


📄 Исходный файл: `pkg/proxy/iptables/proxier.go`


<details open>
<summary><b>Функции в этом файле (32)</b></summary>


- 🔗 [NewDualStackProxier](#newdualstackproxier-pkgproxyiptablesproxiergo93) `:93`

- 🔗 [NewProxier](#newproxier-pkgproxyiptablesproxiergo215) `:215`

- 🔗 [OnEndpointSliceAdd](#onendpointsliceadd-pkgproxyiptablesproxiergo494) `:494`

- 🔗 [OnEndpointSliceDelete](#onendpointslicedelete-pkgproxyiptablesproxiergo510) `:510`

- 🔗 [OnEndpointSliceUpdate](#onendpointsliceupdate-pkgproxyiptablesproxiergo502) `:502`

- 🔗 [OnEndpointSlicesSynced](#onendpointslicessynced-pkgproxyiptablesproxiergo518) `:518`

- 🔗 [OnServiceAdd](#onserviceadd-pkgproxyiptablesproxiergo461) `:461`

- 🔗 [OnServiceCIDRsChanged](#onservicecidrschanged-pkgproxyiptablesproxiergo540) `:540`

- 🔗 [OnServiceDelete](#onservicedelete-pkgproxyiptablesproxiergo475) `:475`

- 🔗 [OnServiceSynced](#onservicesynced-pkgproxyiptablesproxiergo482) `:482`

- 🔗 [OnServiceUpdate](#onserviceupdate-pkgproxyiptablesproxiergo467) `:467`

- 🔗 [OnTopologyChange](#ontopologychange-pkgproxyiptablesproxiergo529) `:529`

- 🔗 [Sync](#sync-pkgproxyiptablesproxiergo426) `:426`

- 🔗 [SyncLoop](#syncloop-pkgproxyiptablesproxiergo435) `:435`

- 🔗 [appendServiceCommentLocked](#appendservicecommentlocked-pkgproxyiptablesproxiergo614) `:614`

- 🔗 [computeProbability](#computeprobability-pkgproxyiptablesproxiergo403) `:403`

- 🔗 [forceSyncProxyRules](#forcesyncproxyrules-pkgproxyiptablesproxiergo627) `:627`

- 🔗 [isInitialized](#isinitialized-pkgproxyiptablesproxiergo455) `:455`

- 🔗 [isServiceChainName](#isservicechainname-pkgproxyiptablesproxiergo596) `:596`

- 🔗 [newEndpointInfo](#newendpointinfo-pkgproxyiptablesproxiergo362) `:362`

- 🔗 [newServiceInfo](#newserviceinfo-pkgproxyiptablesproxiergo338) `:338`

- 🔗 [portProtoHash](#portprotohash-pkgproxyiptablesproxiergo546) `:546`

- 🔗 [precomputeProbabilities](#precomputeprobabilities-pkgproxyiptablesproxiergo408) `:408`

- 🔗 [probability](#probability-pkgproxyiptablesproxiergo418) `:418`

- 🔗 [serviceExternalChainName](#serviceexternalchainname-pkgproxyiptablesproxiergo584) `:584`

- 🔗 [serviceFirewallChainName](#servicefirewallchainname-pkgproxyiptablesproxiergo576) `:576`

- 🔗 [servicePortEndpointChainName](#serviceportendpointchainname-pkgproxyiptablesproxiergo590) `:590`

- 🔗 [servicePortPolicyClusterChain](#serviceportpolicyclusterchain-pkgproxyiptablesproxiergo563) `:563`

- 🔗 [servicePortPolicyLocalChainName](#serviceportpolicylocalchainname-pkgproxyiptablesproxiergo570) `:570`

- 🔗 [setInitialized](#setinitialized-pkgproxyiptablesproxiergo447) `:447`

- 🔗 [syncProxyRules](#syncproxyrules-pkgproxyiptablesproxiergo638) `:638`

- 🔗 [writeServiceToEndpointRules](#writeservicetoendpointrules-pkgproxyiptablesproxiergo1444) `:1444`


</details>


[function] name: NewDualStackProxier file: pkg/proxy/iptables/proxier.go:93 returns_error: да description: NewDualStackProxier creates a MetaProxier instance, with IPv4 and IPv6 proxies.


### NewDualStackProxier (pkg/proxy/iptables/proxier.go:93)


NewDualStackProxier creates a MetaProxier instance, with IPv4 and IPv6 proxies.


```go
func NewDualStackProxier((proxy.Provider, error)) (proxy.Provider, error)
```


**Тип ответа:** proxy.Provider


```json
{
  "cadvisor": {},
  "podManager": {}
}
```


*Определено в:* `pkg/kubelet/stats/provider.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `proxy.Provider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:93`



---


[function] name: NewProxier file: pkg/proxy/iptables/proxier.go:215 returns_error: да description: NewProxier returns a new single-stack IPTables proxier.


### NewProxier (pkg/proxy/iptables/proxier.go:215)


NewProxier returns a new single-stack IPTables proxier.


```go
func NewProxier((*Proxier, error)) (*Proxier, error)
```


**Тип запроса:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Proxier`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:215`



---


[function] name: OnEndpointSliceAdd file: pkg/proxy/iptables/proxier.go:494 returns_error: нет description: OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


### OnEndpointSliceAdd (pkg/proxy/iptables/proxier.go:494)


OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


```go
func (proxier *Proxier) OnEndpointSliceAdd((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:494`



---


[function] name: OnEndpointSliceDelete file: pkg/proxy/iptables/proxier.go:510 returns_error: нет description: OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


### OnEndpointSliceDelete (pkg/proxy/iptables/proxier.go:510)


OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


```go
func (proxier *Proxier) OnEndpointSliceDelete((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:510`



---


[function] name: OnEndpointSliceUpdate file: pkg/proxy/iptables/proxier.go:502 returns_error: нет description: OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


### OnEndpointSliceUpdate (pkg/proxy/iptables/proxier.go:502)


OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


```go
func (proxier *Proxier) OnEndpointSliceUpdate((_, endpointSlice *discovery.EndpointSlice)) (_, endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:502`



---


[function] name: OnEndpointSlicesSynced file: pkg/proxy/iptables/proxier.go:518 returns_error: нет description: OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to lo


### OnEndpointSlicesSynced (pkg/proxy/iptables/proxier.go:518)


OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *Proxier) OnEndpointSlicesSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:518`



---


[function] name: OnServiceAdd file: pkg/proxy/iptables/proxier.go:461 returns_error: нет description: OnServiceAdd is called whenever creation of new service object
is observed.


### OnServiceAdd (pkg/proxy/iptables/proxier.go:461)


OnServiceAdd is called whenever creation of new service object
is observed.


```go
func (proxier *Proxier) OnServiceAdd((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:461`



---


[function] name: OnServiceCIDRsChanged file: pkg/proxy/iptables/proxier.go:540 returns_error: нет description: OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of 


### OnServiceCIDRsChanged (pkg/proxy/iptables/proxier.go:540)


OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of service cidrs.


```go
func (proxier *Proxier) OnServiceCIDRsChanged((_ []string)) (_ []string)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:540`



---


[function] name: OnServiceDelete file: pkg/proxy/iptables/proxier.go:475 returns_error: нет description: OnServiceDelete is called whenever deletion of an existing service
object is observed.


### OnServiceDelete (pkg/proxy/iptables/proxier.go:475)


OnServiceDelete is called whenever deletion of an existing service
object is observed.


```go
func (proxier *Proxier) OnServiceDelete((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:475`



---


[function] name: OnServiceSynced file: pkg/proxy/iptables/proxier.go:482 returns_error: нет description: OnServiceSynced is called once all the initial event handlers were
called and the state is fully propagated to local cac


### OnServiceSynced (pkg/proxy/iptables/proxier.go:482)


OnServiceSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *Proxier) OnServiceSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:482`



---


[function] name: OnServiceUpdate file: pkg/proxy/iptables/proxier.go:467 returns_error: нет description: OnServiceUpdate is called whenever modification of an existing
service object is observed.


### OnServiceUpdate (pkg/proxy/iptables/proxier.go:467)


OnServiceUpdate is called whenever modification of an existing
service object is observed.


```go
func (proxier *Proxier) OnServiceUpdate((oldService, service *v1.Service)) (oldService, service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:467`



---


[function] name: OnTopologyChange file: pkg/proxy/iptables/proxier.go:529 returns_error: нет description: OnTopologyChange is called whenever this node's proxy relevant topology-related labels change.


### OnTopologyChange (pkg/proxy/iptables/proxier.go:529)


OnTopologyChange is called whenever this node's proxy relevant topology-related labels change.


```go
func (proxier *Proxier) OnTopologyChange((topologyLabels map[string]string)) (topologyLabels map[string]string)
```


**Тип ответа:** topologyLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:529`



---


[function] name: Sync file: pkg/proxy/iptables/proxier.go:426 returns_error: нет description: Sync is called to synchronize the proxier state to iptables as soon as possible.


### Sync (pkg/proxy/iptables/proxier.go:426)


Sync is called to synchronize the proxier state to iptables as soon as possible.


```go
func (proxier *Proxier) Sync(()) ()
```


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:426`



---


[function] name: SyncLoop file: pkg/proxy/iptables/proxier.go:435 returns_error: нет description: SyncLoop runs periodic work.  This is expected to run as a goroutine or as the main loop of the app.  It does not return


### SyncLoop (pkg/proxy/iptables/proxier.go:435)


SyncLoop runs periodic work.  This is expected to run as a goroutine or as the main loop of the app.  It does not return.


```go
func (proxier *Proxier) SyncLoop(()) ()
```


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:435`



---


[function] name: appendServiceCommentLocked file: pkg/proxy/iptables/proxier.go:614 returns_error: нет description: Assumes proxier.mu is held.


### appendServiceCommentLocked (pkg/proxy/iptables/proxier.go:614)


Assumes proxier.mu is held.


```go
func (proxier *Proxier) appendServiceCommentLocked((args []string, svcName string)) (args []string, svcName string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** svcName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:614`



---


[function] name: computeProbability file: pkg/proxy/iptables/proxier.go:403 returns_error: нет description: —


### computeProbability (pkg/proxy/iptables/proxier.go:403)


computeProbability is a function that performs operations based on the provided parameters and returns (n int).


```go
func computeProbability((n int)) (n int)
```


**Тип ответа:** n


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:403`



---


[function] name: forceSyncProxyRules file: pkg/proxy/iptables/proxier.go:627 returns_error: нет description: Called by the iptables.Monitor, and in response to topology changes; this calls
syncProxyRules() and tells it to resync 


### forceSyncProxyRules (pkg/proxy/iptables/proxier.go:627)


Called by the iptables.Monitor, and in response to topology changes; this calls
syncProxyRules() and tells it to resync all services, regardless of whether the
Service or Endpoints/EndpointSlice objects themselves have changed


```go
func (proxier *Proxier) forceSyncProxyRules(()) ()
```


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:627`



---


[function] name: isInitialized file: pkg/proxy/iptables/proxier.go:455 returns_error: нет description: —


### isInitialized (pkg/proxy/iptables/proxier.go:455)


isInitialized is a method that performs operations based on the provided parameters and returns ().


```go
func (proxier *Proxier) isInitialized(()) ()
```


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:455`



---


[function] name: isServiceChainName file: pkg/proxy/iptables/proxier.go:596 returns_error: нет description: —


### isServiceChainName (pkg/proxy/iptables/proxier.go:596)


isServiceChainName is a function that performs operations based on the provided parameters and returns (chainString string).


```go
func isServiceChainName((chainString string)) (chainString string)
```


**Тип ответа:** chainString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:596`



---


[function] name: newEndpointInfo file: pkg/proxy/iptables/proxier.go:362 returns_error: нет description: returns a new proxy.Endpoint which abstracts a endpointInfo


### newEndpointInfo (pkg/proxy/iptables/proxier.go:362)


returns a new proxy.Endpoint which abstracts a endpointInfo


```go
func newEndpointInfo((baseInfo *proxy.BaseEndpointInfo, svcPortName *proxy.ServicePortName)) (baseInfo *proxy.BaseEndpointInfo, svcPortName *proxy.ServicePortName)
```


**Тип запроса:** proxy.BaseEndpointInfo


```json
{
  "ip": "string",
  "port": 0,
  "endpoint": "string",
  "isLocal": false,
  "ready": false,
  "serving": false,
  "terminating": false,
  "zoneHints": {},
  "nodeHints": {}
}
```


*Определено в:* `pkg/proxy/endpoint.go`


**Тип запроса:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** baseInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.BaseEndpointInfo


```json
{
  "ip": "string",
  "port": 0,
  "endpoint": "string",
  "isLocal": false,
  "ready": false,
  "serving": false,
  "terminating": false,
  "zoneHints": {},
  "nodeHints": {}
}
```


*Определено в:* `pkg/proxy/endpoint.go`


**Тип ответа:** svcPortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:362`



---


[function] name: newServiceInfo file: pkg/proxy/iptables/proxier.go:338 returns_error: нет description: returns a new proxy.ServicePort which abstracts a serviceInfo


### newServiceInfo (pkg/proxy/iptables/proxier.go:338)


returns a new proxy.ServicePort which abstracts a serviceInfo


```go
func newServiceInfo((port *v1.ServicePort, service *v1.Service, bsvcPortInfo *proxy.BaseServicePortInfo)) (port *v1.ServicePort, service *v1.Service, bsvcPortInfo *proxy.BaseServicePortInfo)
```


**Тип запроса:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** proxy.BaseServicePortInfo


```json
{
  "clusterIP": {},
  "port": 0,
  "protocol": {},
  "nodePort": 0,
  "loadBalancerVIPs": [],
  "sessionAffinityType": {},
  "stickyMaxAgeSeconds": 0,
  "externalIPs": [],
  "loadBalancerSourceRanges": [],
  "healthCheckNodePort": 0,
  "externalPolicyLocal": false,
  "internalPolicyLocal": false
}
```


*Определено в:* `pkg/proxy/serviceport.go`


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


**Тип ответа:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** bsvcPortInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.BaseServicePortInfo


```json
{
  "clusterIP": {},
  "port": 0,
  "protocol": {},
  "nodePort": 0,
  "loadBalancerVIPs": [],
  "sessionAffinityType": {},
  "stickyMaxAgeSeconds": 0,
  "externalIPs": [],
  "loadBalancerSourceRanges": [],
  "healthCheckNodePort": 0,
  "externalPolicyLocal": false,
  "internalPolicyLocal": false
}
```


*Определено в:* `pkg/proxy/serviceport.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:338`



---


[function] name: portProtoHash file: pkg/proxy/iptables/proxier.go:546 returns_error: нет description: portProtoHash takes the ServicePortName and protocol for a service
returns the associated 16 character hash. This is com


### portProtoHash (pkg/proxy/iptables/proxier.go:546)


portProtoHash takes the ServicePortName and protocol for a service
returns the associated 16 character hash. This is computed by hashing (sha256)
then encoding to base32 and truncating to 16 chars. We do this because IPTables
Chain Names must be <= 28 chars long, and the longer they are the harder they are to read.


```go
func portProtoHash((servicePortName string, protocol string)) (servicePortName string, protocol string)
```


**Тип ответа:** servicePortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:546`



---


[function] name: precomputeProbabilities file: pkg/proxy/iptables/proxier.go:408 returns_error: нет description: This assumes proxier.mu is held


### precomputeProbabilities (pkg/proxy/iptables/proxier.go:408)


This assumes proxier.mu is held


```go
func (proxier *Proxier) precomputeProbabilities((numberOfPrecomputed int)) (numberOfPrecomputed int)
```


**Тип ответа:** numberOfPrecomputed


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:408`



---


[function] name: probability file: pkg/proxy/iptables/proxier.go:418 returns_error: нет description: This assumes proxier.mu is held


### probability (pkg/proxy/iptables/proxier.go:418)


This assumes proxier.mu is held


```go
func (proxier *Proxier) probability((n int)) (n int)
```


**Тип ответа:** n


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:418`



---


[function] name: serviceExternalChainName file: pkg/proxy/iptables/proxier.go:584 returns_error: нет description: serviceExternalChainName returns the name of the KUBE-EXT-XXXX chain for a service, which
implements "short-circuiting" 


### serviceExternalChainName (pkg/proxy/iptables/proxier.go:584)


serviceExternalChainName returns the name of the KUBE-EXT-XXXX chain for a service, which
implements "short-circuiting" for internally-originated external-destination traffic when using
`Local` external traffic policy.  It forwards traffic from local sources to the KUBE-SVC-XXXX
chain and traffic from external sources to the KUBE-SVL-XXXX chain.


```go
func serviceExternalChainName((servicePortName string, protocol string)) (servicePortName string, protocol string)
```


**Тип ответа:** servicePortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:584`



---


[function] name: serviceFirewallChainName file: pkg/proxy/iptables/proxier.go:576 returns_error: нет description: serviceFirewallChainName returns the name of the KUBE-FW-XXXX chain for a service, which
is used to implement the filter


### serviceFirewallChainName (pkg/proxy/iptables/proxier.go:576)


serviceFirewallChainName returns the name of the KUBE-FW-XXXX chain for a service, which
is used to implement the filtering for the LoadBalancerSourceRanges feature.


```go
func serviceFirewallChainName((servicePortName string, protocol string)) (servicePortName string, protocol string)
```


**Тип ответа:** servicePortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:576`



---


[function] name: servicePortEndpointChainName file: pkg/proxy/iptables/proxier.go:590 returns_error: нет description: servicePortEndpointChainName returns the name of the KUBE-SEP-XXXX chain for a particular
service endpoint.


### servicePortEndpointChainName (pkg/proxy/iptables/proxier.go:590)


servicePortEndpointChainName returns the name of the KUBE-SEP-XXXX chain for a particular
service endpoint.


```go
func servicePortEndpointChainName((servicePortName string, protocol string, endpoint string)) (servicePortName string, protocol string, endpoint string)
```


**Тип ответа:** servicePortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpoint


```json
{
  "URL": "string",
  "AccessToken": "string",
  "JWT": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:590`



---


[function] name: servicePortPolicyClusterChain file: pkg/proxy/iptables/proxier.go:563 returns_error: нет description: servicePortPolicyClusterChain returns the name of the KUBE-SVC-XXXX chain for a service, which is the
main iptables chai


### servicePortPolicyClusterChain (pkg/proxy/iptables/proxier.go:563)


servicePortPolicyClusterChain returns the name of the KUBE-SVC-XXXX chain for a service, which is the
main iptables chain for that service, used for dispatching to endpoints when using `Cluster`
traffic policy.


```go
func servicePortPolicyClusterChain((servicePortName string, protocol string)) (servicePortName string, protocol string)
```


**Тип ответа:** servicePortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:563`



---


[function] name: servicePortPolicyLocalChainName file: pkg/proxy/iptables/proxier.go:570 returns_error: нет description: servicePortPolicyLocalChainName returns the name of the KUBE-SVL-XXXX chain for a service, which
handles dispatching to 


### servicePortPolicyLocalChainName (pkg/proxy/iptables/proxier.go:570)


servicePortPolicyLocalChainName returns the name of the KUBE-SVL-XXXX chain for a service, which
handles dispatching to local endpoints when using `Local` traffic policy. This chain only
exists if the service has `Local` internal or external traffic policy.


```go
func servicePortPolicyLocalChainName((servicePortName string, protocol string)) (servicePortName string, protocol string)
```


**Тип ответа:** servicePortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:570`



---


[function] name: setInitialized file: pkg/proxy/iptables/proxier.go:447 returns_error: нет description: —


### setInitialized (pkg/proxy/iptables/proxier.go:447)


setInitialized is a method that performs operations based on the provided parameters and returns (value bool).


```go
func (proxier *Proxier) setInitialized((value bool)) (value bool)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:447`



---


[function] name: syncProxyRules file: pkg/proxy/iptables/proxier.go:638 returns_error: да description: This is where all of the iptables-save/restore calls happen.
The only other iptables rules are those that are setup in i


### syncProxyRules (pkg/proxy/iptables/proxier.go:638)


This is where all of the iptables-save/restore calls happen.
The only other iptables rules are those that are setup in iptablesInit()
This assumes proxier.mu is NOT held


```go
func (proxier *Proxier) syncProxyRules((retryError error)) (retryError error)
```


**Тип ответа:** retryError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `retryError error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:638`



---


[function] name: writeServiceToEndpointRules file: pkg/proxy/iptables/proxier.go:1444 returns_error: нет description: —


### writeServiceToEndpointRules (pkg/proxy/iptables/proxier.go:1444)


writeServiceToEndpointRules is a method that performs operations based on the provided parameters and returns (natRules proxyutil.LineBuffer, svcPortNameString string, svcInfo proxy.ServicePort, svcChain utiliptables.Chain, endpoints []proxy.Endpoint, args []string).


```go
func (proxier *Proxier) writeServiceToEndpointRules((natRules proxyutil.LineBuffer, svcPortNameString string, svcInfo proxy.ServicePort, svcChain utiliptables.Chain, endpoints []proxy.Endpoint, args []string)) (natRules proxyutil.LineBuffer, svcPortNameString string, svcInfo proxy.ServicePort, svcChain utiliptables.Chain, endpoints []proxy.Endpoint, args []string)
```


**Тип ответа:** natRules


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxyutil.LineBuffer


```json
{
  "b": {},
  "lines": 0
}
```


*Определено в:* `pkg/proxy/util/linebuffer.go`


**Тип ответа:** svcPortNameString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** svcInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svcChain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utiliptables.Chain


```json
{
  "Name": {},
  "Packets": 0,
  "Bytes": 0,
  "Rules": [],
  "Deleted": false
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** proxy.Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/iptables/proxier.go:1444`




## pkg/proxy/ipvs/cleanup.go


📄 Исходный файл: `pkg/proxy/ipvs/cleanup.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [CleanupLeftovers](#cleanupleftovers-pkgproxyipvscleanupgo74) `:74`

- 🔗 [cleanupIptablesLeftovers](#cleanupiptablesleftovers-pkgproxyipvscleanupgo34) `:34`

- 🔗 [cleanupLeftovers](#cleanupleftovers-pkgproxyipvscleanupgo91) `:91`


</details>


[function] name: CleanupLeftovers file: pkg/proxy/ipvs/cleanup.go:74 returns_error: нет description: CleanupLeftovers clean up all ipvs and iptables rules created by ipvs Proxier.


### CleanupLeftovers (pkg/proxy/ipvs/cleanup.go:74)


CleanupLeftovers clean up all ipvs and iptables rules created by ipvs Proxier.


```go
func CleanupLeftovers((encounteredError bool)) (encounteredError bool)
```


**Тип ответа:** encounteredError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/cleanup.go:74`



---


[function] name: cleanupIptablesLeftovers file: pkg/proxy/ipvs/cleanup.go:34 returns_error: нет description: CleanupIptablesLeftovers removes all iptables rules and chains created by the Proxier
It returns true if an error was en


### cleanupIptablesLeftovers (pkg/proxy/ipvs/cleanup.go:34)


CleanupIptablesLeftovers removes all iptables rules and chains created by the Proxier
It returns true if an error was encountered. Errors are logged.


```go
func cleanupIptablesLeftovers((encounteredError bool)) (encounteredError bool)
```


**Тип ответа:** encounteredError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/cleanup.go:34`



---


[function] name: cleanupLeftovers file: pkg/proxy/ipvs/cleanup.go:91 returns_error: нет description: —


### cleanupLeftovers (pkg/proxy/ipvs/cleanup.go:91)


cleanupLeftovers is a function that performs operations based on the provided parameters and may return an error.


```go
func cleanupLeftovers((encounteredError bool)) (encounteredError bool)
```


**Тип ответа:** encounteredError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/cleanup.go:91`




## pkg/proxy/ipvs/graceful_termination.go


📄 Исходный файл: `pkg/proxy/ipvs/graceful_termination.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [GetUniqueRSName](#getuniquersname-pkgproxyipvsgraceful_terminationgo48) `:48`

- 🔗 [GracefulDeleteRS](#gracefuldeleters-pkgproxyipvsgraceful_terminationgo147) `:147`

- 🔗 [InTerminationList](#interminationlist-pkgproxyipvsgraceful_terminationgo141) `:141`

- 🔗 [MoveRSOutofGracefulDeleteList](#moversoutofgracefuldeletelist-pkgproxyipvsgraceful_terminationgo203) `:203`

- 🔗 [NewGracefulTerminationManager](#newgracefulterminationmanager-pkgproxyipvsgraceful_terminationgo130) `:130`

- 🔗 [Run](#run-pkgproxyipvsgraceful_terminationgo217) `:217`

- 🔗 [String](#string-pkgproxyipvsgraceful_terminationgo43) `:43`

- 🔗 [add](#add-pkgproxyipvsgraceful_terminationgo58) `:58`

- 🔗 [deleteRsFunc](#deletersfunc-pkgproxyipvsgraceful_terminationgo170) `:170`

- 🔗 [exist](#exist-pkgproxyipvsgraceful_terminationgo112) `:112`

- 🔗 [flushList](#flushlist-pkgproxyipvsgraceful_terminationgo93) `:93`

- 🔗 [len](#len-pkgproxyipvsgraceful_terminationgo86) `:86`

- 🔗 [remove](#remove-pkgproxyipvsgraceful_terminationgo73) `:73`

- 🔗 [tryDeleteRs](#trydeleters-pkgproxyipvsgraceful_terminationgo196) `:196`


</details>


[function] name: GetUniqueRSName file: pkg/proxy/ipvs/graceful_termination.go:48 returns_error: нет description: GetUniqueRSName return a string type unique rs name with vs information


### GetUniqueRSName (pkg/proxy/ipvs/graceful_termination.go:48)


GetUniqueRSName return a string type unique rs name with vs information


```go
func GetUniqueRSName((vs *utilipvs.VirtualServer, rs *utilipvs.RealServer)) (vs *utilipvs.VirtualServer, rs *utilipvs.RealServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип запроса:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:48`



---


[function] name: GracefulDeleteRS file: pkg/proxy/ipvs/graceful_termination.go:147 returns_error: нет description: GracefulDeleteRS to update rs weight to 0, and add rs to graceful terminate list


### GracefulDeleteRS (pkg/proxy/ipvs/graceful_termination.go:147)


GracefulDeleteRS to update rs weight to 0, and add rs to graceful terminate list


```go
func (m *GracefulTerminationManager) GracefulDeleteRS((vs *utilipvs.VirtualServer, rs *utilipvs.RealServer)) (vs *utilipvs.VirtualServer, rs *utilipvs.RealServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип запроса:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:147`



---


[function] name: InTerminationList file: pkg/proxy/ipvs/graceful_termination.go:141 returns_error: нет description: InTerminationList to check whether specified unique rs name is in graceful termination list


### InTerminationList (pkg/proxy/ipvs/graceful_termination.go:141)


InTerminationList to check whether specified unique rs name is in graceful termination list


```go
func (m *GracefulTerminationManager) InTerminationList((uniqueRS string)) (uniqueRS string)
```


**Тип ответа:** uniqueRS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:141`



---


[function] name: MoveRSOutofGracefulDeleteList file: pkg/proxy/ipvs/graceful_termination.go:203 returns_error: нет description: MoveRSOutofGracefulDeleteList to delete an rs and remove it from the rsList immediately


### MoveRSOutofGracefulDeleteList (pkg/proxy/ipvs/graceful_termination.go:203)


MoveRSOutofGracefulDeleteList to delete an rs and remove it from the rsList immediately


```go
func (m *GracefulTerminationManager) MoveRSOutofGracefulDeleteList((uniqueRS string)) (uniqueRS string)
```


**Тип ответа:** uniqueRS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:203`



---


[function] name: NewGracefulTerminationManager file: pkg/proxy/ipvs/graceful_termination.go:130 returns_error: нет description: NewGracefulTerminationManager create a gracefulTerminationManager to manage ipvs rs graceful termination work


### NewGracefulTerminationManager (pkg/proxy/ipvs/graceful_termination.go:130)


NewGracefulTerminationManager create a gracefulTerminationManager to manage ipvs rs graceful termination work


```go
func NewGracefulTerminationManager((ipvs utilipvs.Interface)) (ipvs utilipvs.Interface)
```


**Тип ответа:** ipvs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilipvs.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:130`



---


[function] name: Run file: pkg/proxy/ipvs/graceful_termination.go:217 returns_error: нет description: Run start a goroutine to try to delete rs in the graceful delete rsList with an interval 1 minute


### Run (pkg/proxy/ipvs/graceful_termination.go:217)


Run start a goroutine to try to delete rs in the graceful delete rsList with an interval 1 minute


```go
func (m *GracefulTerminationManager) Run(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:217`



---


[function] name: String file: pkg/proxy/ipvs/graceful_termination.go:43 returns_error: нет description: String return the unique real server name(with virtual server information)


### String (pkg/proxy/ipvs/graceful_termination.go:43)


String return the unique real server name(with virtual server information)


```go
func (g *listItem) String(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:43`



---


[function] name: add file: pkg/proxy/ipvs/graceful_termination.go:58 returns_error: нет description: add push an new element to the rsList


### add (pkg/proxy/ipvs/graceful_termination.go:58)


add push an new element to the rsList


```go
func (q *graceTerminateRSList) add((rs *listItem)) (rs *listItem)
```


**Тип запроса:** listItem


```json
{
  "VirtualServer": null,
  "RealServer": null
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** listItem


```json
{
  "VirtualServer": null,
  "RealServer": null
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:58`



---


[function] name: deleteRsFunc file: pkg/proxy/ipvs/graceful_termination.go:170 returns_error: да description: —


### deleteRsFunc (pkg/proxy/ipvs/graceful_termination.go:170)


deleteRsFunc is a method that performs operations based on the provided parameters and may return an error.


```go
func (m *GracefulTerminationManager) deleteRsFunc((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:170`



---


[function] name: exist file: pkg/proxy/ipvs/graceful_termination.go:112 returns_error: нет description: exist check whether the specified unique RS is in the rsList


### exist (pkg/proxy/ipvs/graceful_termination.go:112)


exist check whether the specified unique RS is in the rsList


```go
func (q *graceTerminateRSList) exist((*listItem, bool)) (*listItem, bool)
```


**Тип запроса:** listItem


```json
{
  "VirtualServer": null,
  "RealServer": null
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


**Тип ответа:** listItem


```json
{
  "VirtualServer": null,
  "RealServer": null
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:112`



---


[function] name: flushList file: pkg/proxy/ipvs/graceful_termination.go:93 returns_error: да description: —


### flushList (pkg/proxy/ipvs/graceful_termination.go:93)


flushList is a method that performs operations based on the provided parameters and may return an error.


```go
func (q *graceTerminateRSList) flushList((handler func(rsToDelete *listItem) (bool, error))) (handler func(rsToDelete *listItem) (bool, error))
```


**Тип запроса:** listItem


```json
{
  "VirtualServer": null,
  "RealServer": null
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rsToDelete


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** listItem


```json
{
  "VirtualServer": null,
  "RealServer": null
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `handler func(rsToDelete *listItem) (bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:93`



---


[function] name: len file: pkg/proxy/ipvs/graceful_termination.go:86 returns_error: нет description: return the size of the list


### len (pkg/proxy/ipvs/graceful_termination.go:86)


return the size of the list


```go
func (q *graceTerminateRSList) len(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:86`



---


[function] name: remove file: pkg/proxy/ipvs/graceful_termination.go:73 returns_error: нет description: remove remove an element from the rsList


### remove (pkg/proxy/ipvs/graceful_termination.go:73)


remove remove an element from the rsList


```go
func (q *graceTerminateRSList) remove((rs *listItem)) (rs *listItem)
```


**Тип запроса:** listItem


```json
{
  "VirtualServer": null,
  "RealServer": null
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** listItem


```json
{
  "VirtualServer": null,
  "RealServer": null
}
```


*Определено в:* `pkg/proxy/ipvs/graceful_termination.go`


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:73`



---


[function] name: tryDeleteRs file: pkg/proxy/ipvs/graceful_termination.go:196 returns_error: нет description: —


### tryDeleteRs (pkg/proxy/ipvs/graceful_termination.go:196)


tryDeleteRs is a method that performs operations based on the provided parameters and returns ().


```go
func (m *GracefulTerminationManager) tryDeleteRs(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/graceful_termination.go:196`




## pkg/proxy/ipvs/ipset.go


📄 Исходный файл: `pkg/proxy/ipvs/ipset.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [NewIPSet](#newipset-pkgproxyipvsipsetgo103) `:103`

- 🔗 [checkMinVersion](#checkminversion-pkgproxyipvsipsetgo195) `:195`

- 🔗 [ensureIPSet](#ensureipset-pkgproxyipvsipsetgo186) `:186`

- 🔗 [getComment](#getcomment-pkgproxyipvsipsetgo143) `:143`

- 🔗 [isEmpty](#isempty-pkgproxyipvsipsetgo139) `:139`

- 🔗 [resetEntries](#resetentries-pkgproxyipvsipsetgo147) `:147`

- 🔗 [syncIPSetEntries](#syncipsetentries-pkgproxyipvsipsetgo151) `:151`

- 🔗 [validateEntry](#validateentry-pkgproxyipvsipsetgo135) `:135`


</details>


[function] name: NewIPSet file: pkg/proxy/ipvs/ipset.go:103 returns_error: нет description: NewIPSet initialize a new IPSet struct


### NewIPSet (pkg/proxy/ipvs/ipset.go:103)


NewIPSet initialize a new IPSet struct


```go
func NewIPSet((handle utilipset.Interface, name string, setType utilipset.Type, isIPv6 bool, comment string)) (handle utilipset.Interface, name string, setType utilipset.Type, isIPv6 bool, comment string)
```


**Тип ответа:** handle


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Тип ответа:** utilipset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** setType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilipset.Type


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


**Тип ответа:** isIPv6


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** comment


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset.go:103`



---


[function] name: checkMinVersion file: pkg/proxy/ipvs/ipset.go:195 returns_error: нет description: checkMinVersion checks if ipset current version satisfies required min version


### checkMinVersion (pkg/proxy/ipvs/ipset.go:195)


checkMinVersion checks if ipset current version satisfies required min version


```go
func checkMinVersion((vstring string)) (vstring string)
```


**Тип ответа:** vstring


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset.go:195`



---


[function] name: ensureIPSet file: pkg/proxy/ipvs/ipset.go:186 returns_error: нет description: —


### ensureIPSet (pkg/proxy/ipvs/ipset.go:186)


ensureIPSet is a function that performs operations based on the provided parameters and returns (set *IPSet).


```go
func ensureIPSet((set *IPSet)) (set *IPSet)
```


**Тип запроса:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset.go:186`



---


[function] name: getComment file: pkg/proxy/ipvs/ipset.go:143 returns_error: нет description: —


### getComment (pkg/proxy/ipvs/ipset.go:143)


getComment is a method that performs operations based on the provided parameters and returns ().


```go
func (set *IPSet) getComment(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset.go:143`



---


[function] name: isEmpty file: pkg/proxy/ipvs/ipset.go:139 returns_error: нет description: —


### isEmpty (pkg/proxy/ipvs/ipset.go:139)


isEmpty is a method that performs operations based on the provided parameters and returns ().


```go
func (set *IPSet) isEmpty(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset.go:139`



---


[function] name: resetEntries file: pkg/proxy/ipvs/ipset.go:147 returns_error: нет description: —


### resetEntries (pkg/proxy/ipvs/ipset.go:147)


resetEntries is a method that performs operations based on the provided parameters and returns ().


```go
func (set *IPSet) resetEntries(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset.go:147`



---


[function] name: syncIPSetEntries file: pkg/proxy/ipvs/ipset.go:151 returns_error: нет description: —


### syncIPSetEntries (pkg/proxy/ipvs/ipset.go:151)


syncIPSetEntries is a method that performs operations based on the provided parameters and returns ().


```go
func (set *IPSet) syncIPSetEntries(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset.go:151`



---


[function] name: validateEntry file: pkg/proxy/ipvs/ipset.go:135 returns_error: нет description: —


### validateEntry (pkg/proxy/ipvs/ipset.go:135)


validateEntry is a method that performs operations based on the provided parameters and returns (entry *utilipset.Entry).


```go
func (set *IPSet) validateEntry((entry *utilipset.Entry)) (entry *utilipset.Entry)
```


**Тип запроса:** utilipset.Entry


```json
{
  "IP": "string",
  "Port": 0,
  "Protocol": "string",
  "Net": "string",
  "IP2": "string",
  "SetType": {}
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** entry


```json
{
  "val": {},
  "expiry": {},
  "generation": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/cache/expiring.go`


**Тип ответа:** utilipset.Entry


```json
{
  "IP": "string",
  "Port": 0,
  "Protocol": "string",
  "Net": "string",
  "IP2": "string",
  "SetType": {}
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset.go:135`




## pkg/proxy/ipvs/ipset/ipset.go


📄 Исходный файл: `pkg/proxy/ipvs/ipset/ipset.go`


<details open>
<summary><b>Функции в этом файле (25)</b></summary>


- 🔗 [AddEntry](#addentry-pkgproxyipvsipsetipsetgo324) `:324`

- 🔗 [CreateSet](#createset-pkgproxyipvsipsetipsetgo287) `:287`

- 🔗 [DelEntry](#delentry-pkgproxyipvsipsetipsetgo336) `:336`

- 🔗 [DestroyAllSets](#destroyallsets-pkgproxyipvsipsetipsetgo376) `:376`

- 🔗 [DestroySet](#destroyset-pkgproxyipvsipsetipsetgo368) `:368`

- 🔗 [FlushSet](#flushset-pkgproxyipvsipsetipsetgo360) `:360`

- 🔗 [GetVersion](#getversion-pkgproxyipvsipsetipsetgo414) `:414`

- 🔗 [IsNotFoundError](#isnotfounderror-pkgproxyipvsipsetipsetgo475) `:475`

- 🔗 [ListEntries](#listentries-pkgproxyipvsipsetipsetgo393) `:393`

- 🔗 [ListSets](#listsets-pkgproxyipvsipsetipsetgo384) `:384`

- 🔗 [New](#new-pkgproxyipvsipsetipsetgo280) `:280`

- 🔗 [String](#string-pkgproxyipvsipsetipsetgo229) `:229`

- 🔗 [TestEntry](#testentry-pkgproxyipvsipsetipsetgo344) `:344`

- 🔗 [Validate](#validate-pkgproxyipvsipsetipsetgo99) `:99`

- 🔗 [Validate](#validate-pkgproxyipvsipsetipsetgo170) `:170`

- 🔗 [checkIP](#checkip-pkgproxyipvsipsetipsetgo266) `:266`

- 🔗 [checkIPandProtocol](#checkipandprotocol-pkgproxyipvsipsetipsetgo255) `:255`

- 🔗 [createSet](#createset-pkgproxyipvsipsetipsetgo300) `:300`

- 🔗 [getIPSetVersionString](#getipsetversionstring-pkgproxyipvsipsetipsetgo420) `:420`

- 🔗 [parsePortRange](#parseportrange-pkgproxyipvsipsetipsetgo502) `:502`

- 🔗 [setIPSetDefaults](#setipsetdefaults-pkgproxyipvsipsetipsetgo129) `:129`

- 🔗 [validateHashFamily](#validatehashfamily-pkgproxyipvsipsetipsetgo465) `:465`

- 🔗 [validateIPSetType](#validateipsettype-pkgproxyipvsipsetipsetgo455) `:455`

- 🔗 [validatePortRange](#validateportrange-pkgproxyipvsipsetipsetgo437) `:437`

- 🔗 [validateProtocol](#validateprotocol-pkgproxyipvsipsetipsetgo492) `:492`


</details>


[function] name: AddEntry file: pkg/proxy/ipvs/ipset/ipset.go:324 returns_error: нет description: AddEntry adds a new entry to the named set.
If the -exist option is specified, ipset ignores the error otherwise raised 


### AddEntry (pkg/proxy/ipvs/ipset/ipset.go:324)


AddEntry adds a new entry to the named set.
If the -exist option is specified, ipset ignores the error otherwise raised when
the same set (setname and create parameters are identical) already exists.


```go
func (runner *runner) AddEntry((entry string, set *IPSet, ignoreExistErr bool)) (entry string, set *IPSet, ignoreExistErr bool)
```


**Тип запроса:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** entry


```json
{
  "val": {},
  "expiry": {},
  "generation": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/cache/expiring.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** ignoreExistErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:324`



---


[function] name: CreateSet file: pkg/proxy/ipvs/ipset/ipset.go:287 returns_error: нет description: CreateSet creates a new set, it will ignore error when the set already exists if ignoreExistErr=true.


### CreateSet (pkg/proxy/ipvs/ipset/ipset.go:287)


CreateSet creates a new set, it will ignore error when the set already exists if ignoreExistErr=true.


```go
func (runner *runner) CreateSet((set *IPSet, ignoreExistErr bool)) (set *IPSet, ignoreExistErr bool)
```


**Тип запроса:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** ignoreExistErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:287`



---


[function] name: DelEntry file: pkg/proxy/ipvs/ipset/ipset.go:336 returns_error: нет description: DelEntry is used to delete the specified entry from the set.


### DelEntry (pkg/proxy/ipvs/ipset/ipset.go:336)


DelEntry is used to delete the specified entry from the set.


```go
func (runner *runner) DelEntry((entry string, set string)) (entry string, set string)
```


**Тип ответа:** entry


```json
{
  "val": {},
  "expiry": {},
  "generation": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/cache/expiring.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:336`



---


[function] name: DestroyAllSets file: pkg/proxy/ipvs/ipset/ipset.go:376 returns_error: нет description: DestroyAllSets is used to destroy all sets.


### DestroyAllSets (pkg/proxy/ipvs/ipset/ipset.go:376)


DestroyAllSets is used to destroy all sets.


```go
func (runner *runner) DestroyAllSets(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:376`



---


[function] name: DestroySet file: pkg/proxy/ipvs/ipset/ipset.go:368 returns_error: нет description: DestroySet is used to destroy a named set.


### DestroySet (pkg/proxy/ipvs/ipset/ipset.go:368)


DestroySet is used to destroy a named set.


```go
func (runner *runner) DestroySet((set string)) (set string)
```


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:368`



---


[function] name: FlushSet file: pkg/proxy/ipvs/ipset/ipset.go:360 returns_error: нет description: FlushSet deletes all entries from a named set.


### FlushSet (pkg/proxy/ipvs/ipset/ipset.go:360)


FlushSet deletes all entries from a named set.


```go
func (runner *runner) FlushSet((set string)) (set string)
```


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:360`



---


[function] name: GetVersion file: pkg/proxy/ipvs/ipset/ipset.go:414 returns_error: да description: GetVersion returns the version string.


### GetVersion (pkg/proxy/ipvs/ipset/ipset.go:414)


GetVersion returns the version string.


```go
func (runner *runner) GetVersion((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:414`



---


[function] name: IsNotFoundError file: pkg/proxy/ipvs/ipset/ipset.go:475 returns_error: да description: IsNotFoundError returns true if the error indicates "not found".  It parses
the error string looking for known values, w


### IsNotFoundError (pkg/proxy/ipvs/ipset/ipset.go:475)


IsNotFoundError returns true if the error indicates "not found".  It parses
the error string looking for known values, which is imperfect but works in
practice.


```go
func IsNotFoundError((err error)) (err error)
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


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:475`



---


[function] name: ListEntries file: pkg/proxy/ipvs/ipset/ipset.go:393 returns_error: да description: ListEntries lists all the entries from a named set.


### ListEntries (pkg/proxy/ipvs/ipset/ipset.go:393)


ListEntries lists all the entries from a named set.


```go
func (runner *runner) ListEntries(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:393`



---


[function] name: ListSets file: pkg/proxy/ipvs/ipset/ipset.go:384 returns_error: да description: ListSets list all set names from kernel


### ListSets (pkg/proxy/ipvs/ipset/ipset.go:384)


ListSets list all set names from kernel


```go
func (runner *runner) ListSets(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:384`



---


[function] name: New file: pkg/proxy/ipvs/ipset/ipset.go:280 returns_error: нет description: New returns a new Interface which will exec ipset.


### New (pkg/proxy/ipvs/ipset/ipset.go:280)


New returns a new Interface which will exec ipset.


```go
func New(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:280`



---


[function] name: String file: pkg/proxy/ipvs/ipset/ipset.go:229 returns_error: нет description: String returns the string format for ipset entry.


### String (pkg/proxy/ipvs/ipset/ipset.go:229)


String returns the string format for ipset entry.


```go
func (e *Entry) String(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:229`



---


[function] name: TestEntry file: pkg/proxy/ipvs/ipset/ipset.go:344 returns_error: да description: TestEntry is used to check whether the specified entry is in the set or not.


### TestEntry (pkg/proxy/ipvs/ipset/ipset.go:344)


TestEntry is used to check whether the specified entry is in the set or not.


```go
func (runner *runner) TestEntry((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:344`



---


[function] name: Validate file: pkg/proxy/ipvs/ipset/ipset.go:99 returns_error: нет description: Validate checks if a given ipset is valid or not.


### Validate (pkg/proxy/ipvs/ipset/ipset.go:99)


Validate checks if a given ipset is valid or not.


```go
func (set *IPSet) Validate(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:99`



---


[function] name: Validate file: pkg/proxy/ipvs/ipset/ipset.go:170 returns_error: нет description: Validate checks if a given ipset entry is valid or not.  The set parameter is the ipset that entry belongs to.


### Validate (pkg/proxy/ipvs/ipset/ipset.go:170)


Validate checks if a given ipset entry is valid or not.  The set parameter is the ipset that entry belongs to.


```go
func (e *Entry) Validate((set *IPSet)) (set *IPSet)
```


**Тип запроса:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:170`



---


[function] name: checkIP file: pkg/proxy/ipvs/ipset/ipset.go:266 returns_error: нет description: checkIP checks if IP of Entry is valid.


### checkIP (pkg/proxy/ipvs/ipset/ipset.go:266)


checkIP checks if IP of Entry is valid.


```go
func (e *Entry) checkIP((set *IPSet)) (set *IPSet)
```


**Тип запроса:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:266`



---


[function] name: checkIPandProtocol file: pkg/proxy/ipvs/ipset/ipset.go:255 returns_error: нет description: checkIPandProtocol checks if IP and Protocol of Entry is valid.


### checkIPandProtocol (pkg/proxy/ipvs/ipset/ipset.go:255)


checkIPandProtocol checks if IP and Protocol of Entry is valid.


```go
func (e *Entry) checkIPandProtocol((set *IPSet)) (set *IPSet)
```


**Тип запроса:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:255`



---


[function] name: createSet file: pkg/proxy/ipvs/ipset/ipset.go:300 returns_error: нет description: If ignoreExistErr is set to true, then the -exist option of ipset will be specified, ipset ignores the error
otherwise r


### createSet (pkg/proxy/ipvs/ipset/ipset.go:300)


If ignoreExistErr is set to true, then the -exist option of ipset will be specified, ipset ignores the error
otherwise raised when the same set (setname and create parameters are identical) already exists.


```go
func (runner *runner) createSet((set *IPSet, ignoreExistErr bool)) (set *IPSet, ignoreExistErr bool)
```


**Тип запроса:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** ignoreExistErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:300`



---


[function] name: getIPSetVersionString file: pkg/proxy/ipvs/ipset/ipset.go:420 returns_error: да description: getIPSetVersionString runs "ipset --version" to get the version string
in the form of "X.Y", i.e "6.19"


### getIPSetVersionString (pkg/proxy/ipvs/ipset/ipset.go:420)


getIPSetVersionString runs "ipset --version" to get the version string
in the form of "X.Y", i.e "6.19"


```go
func getIPSetVersionString((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:420`



---


[function] name: parsePortRange file: pkg/proxy/ipvs/ipset/ipset.go:502 returns_error: да description: parsePortRange parse the begin and end port from a raw string(format: a-b).  beginPort <= endPort
in the return value.


### parsePortRange (pkg/proxy/ipvs/ipset/ipset.go:502)


parsePortRange parse the begin and end port from a raw string(format: a-b).  beginPort <= endPort
in the return value.


```go
func parsePortRange((beginPort int, endPort int, err error)) (beginPort int, endPort int, err error)
```


**Тип ответа:** beginPort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endPort


```json
{
  "Name": "string",
  "Number": 0
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/networking/v1/servicebackendport.go`


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


*Типы возврата:* `beginPort int`, `endPort int`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:502`



---


[function] name: setIPSetDefaults file: pkg/proxy/ipvs/ipset/ipset.go:129 returns_error: нет description: setIPSetDefaults sets some IPSet fields if not present to their default values.


### setIPSetDefaults (pkg/proxy/ipvs/ipset/ipset.go:129)


setIPSetDefaults sets some IPSet fields if not present to their default values.


```go
func (set *IPSet) setIPSetDefaults(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:129`



---


[function] name: validateHashFamily file: pkg/proxy/ipvs/ipset/ipset.go:465 returns_error: нет description: checks if given hash family is supported in ipset


### validateHashFamily (pkg/proxy/ipvs/ipset/ipset.go:465)


checks if given hash family is supported in ipset


```go
func validateHashFamily((family string)) (family string)
```


**Тип ответа:** family


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:465`



---


[function] name: validateIPSetType file: pkg/proxy/ipvs/ipset/ipset.go:455 returns_error: нет description: checks if the given ipset type is valid.


### validateIPSetType (pkg/proxy/ipvs/ipset/ipset.go:455)


checks if the given ipset type is valid.


```go
func validateIPSetType((set Type)) (set Type)
```


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** Type


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:455`



---


[function] name: validatePortRange file: pkg/proxy/ipvs/ipset/ipset.go:437 returns_error: нет description: checks if port range is valid. The begin port number is not necessarily less than
end port number - ipset util can accep


### validatePortRange (pkg/proxy/ipvs/ipset/ipset.go:437)


checks if port range is valid. The begin port number is not necessarily less than
end port number - ipset util can accept it.  It means both 1-100 and 100-1 are valid.


```go
func validatePortRange((portRange string)) (portRange string)
```


**Тип ответа:** portRange


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:437`



---


[function] name: validateProtocol file: pkg/proxy/ipvs/ipset/ipset.go:492 returns_error: нет description: checks if given protocol is supported in entry


### validateProtocol (pkg/proxy/ipvs/ipset/ipset.go:492)


checks if given protocol is supported in entry


```go
func validateProtocol((protocol string)) (protocol string)
```


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset/ipset.go:492`




## pkg/proxy/ipvs/ipset/testing/fake.go


📄 Исходный файл: `pkg/proxy/ipvs/ipset/testing/fake.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [AddEntry](#addentry-pkgproxyipvsipsettestingfakego98) `:98`

- 🔗 [CreateSet](#createset-pkgproxyipvsipsettestingfakego83) `:83`

- 🔗 [DelEntry](#delentry-pkgproxyipvsipsettestingfakego111) `:111`

- 🔗 [DestroyAllSets](#destroyallsets-pkgproxyipvsipsettestingfakego76) `:76`

- 🔗 [DestroySet](#destroyset-pkgproxyipvsipsettestingfakego69) `:69`

- 🔗 [FlushSet](#flushset-pkgproxyipvsipsettestingfakego53) `:53`

- 🔗 [GetVersion](#getversion-pkgproxyipvsipsettestingfakego48) `:48`

- 🔗 [ListEntries](#listentries-pkgproxyipvsipsettestingfakego129) `:129`

- 🔗 [ListSets](#listsets-pkgproxyipvsipsettestingfakego137) `:137`

- 🔗 [NewFake](#newfake-pkgproxyipvsipsettestingfakego39) `:39`

- 🔗 [TestEntry](#testentry-pkgproxyipvsipsettestingfakego120) `:120`


</details>


[function] name: AddEntry file: pkg/proxy/ipvs/ipset/testing/fake.go:98 returns_error: нет description: AddEntry is part of interface.


### AddEntry (pkg/proxy/ipvs/ipset/testing/fake.go:98)


AddEntry is part of interface.


```go
func (f *FakeIPSet) AddEntry((entry string, set *ipset.IPSet, ignoreExistErr bool)) (entry string, set *ipset.IPSet, ignoreExistErr bool)
```


**Тип запроса:** ipset.IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** entry


```json
{
  "val": {},
  "expiry": {},
  "generation": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/cache/expiring.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** ipset.IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** ignoreExistErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:98`



---


[function] name: CreateSet file: pkg/proxy/ipvs/ipset/testing/fake.go:83 returns_error: нет description: CreateSet is part of interface.


### CreateSet (pkg/proxy/ipvs/ipset/testing/fake.go:83)


CreateSet is part of interface.


```go
func (f *FakeIPSet) CreateSet((set *ipset.IPSet, ignoreExistErr bool)) (set *ipset.IPSet, ignoreExistErr bool)
```


**Тип запроса:** ipset.IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


**Тип ответа:** ipset.IPSet


```json
{
  "Name": "string",
  "SetType": {},
  "HashFamily": "string",
  "HashSize": 0,
  "MaxElem": 0,
  "PortRange": "string",
  "Comment": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/ipset/ipset.go`


**Тип ответа:** ignoreExistErr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:83`



---


[function] name: DelEntry file: pkg/proxy/ipvs/ipset/testing/fake.go:111 returns_error: нет description: DelEntry is part of interface.


### DelEntry (pkg/proxy/ipvs/ipset/testing/fake.go:111)


DelEntry is part of interface.


```go
func (f *FakeIPSet) DelEntry((entry string, set string)) (entry string, set string)
```


**Тип ответа:** entry


```json
{
  "val": {},
  "expiry": {},
  "generation": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/cache/expiring.go`


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:111`



---


[function] name: DestroyAllSets file: pkg/proxy/ipvs/ipset/testing/fake.go:76 returns_error: нет description: DestroyAllSets is part of interface.


### DestroyAllSets (pkg/proxy/ipvs/ipset/testing/fake.go:76)


DestroyAllSets is part of interface.


```go
func (f *FakeIPSet) DestroyAllSets(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:76`



---


[function] name: DestroySet file: pkg/proxy/ipvs/ipset/testing/fake.go:69 returns_error: нет description: DestroySet is part of interface.  It deletes both the entries and the set itself.


### DestroySet (pkg/proxy/ipvs/ipset/testing/fake.go:69)


DestroySet is part of interface.  It deletes both the entries and the set itself.


```go
func (f *FakeIPSet) DestroySet((set string)) (set string)
```


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:69`



---


[function] name: FlushSet file: pkg/proxy/ipvs/ipset/testing/fake.go:53 returns_error: нет description: FlushSet is part of interface.  It deletes all entries from a named set but keeps the set itself.


### FlushSet (pkg/proxy/ipvs/ipset/testing/fake.go:53)


FlushSet is part of interface.  It deletes all entries from a named set but keeps the set itself.


```go
func (f *FakeIPSet) FlushSet((set string)) (set string)
```


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:53`



---


[function] name: GetVersion file: pkg/proxy/ipvs/ipset/testing/fake.go:48 returns_error: да description: GetVersion is part of interface.


### GetVersion (pkg/proxy/ipvs/ipset/testing/fake.go:48)


GetVersion is part of interface.


```go
func (f *FakeIPSet) GetVersion((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:48`



---


[function] name: ListEntries file: pkg/proxy/ipvs/ipset/testing/fake.go:129 returns_error: да description: ListEntries is part of interface.


### ListEntries (pkg/proxy/ipvs/ipset/testing/fake.go:129)


ListEntries is part of interface.


```go
func (f *FakeIPSet) ListEntries(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:129`



---


[function] name: ListSets file: pkg/proxy/ipvs/ipset/testing/fake.go:137 returns_error: да description: ListSets is part of interface.


### ListSets (pkg/proxy/ipvs/ipset/testing/fake.go:137)


ListSets is part of interface.


```go
func (f *FakeIPSet) ListSets(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:137`



---


[function] name: NewFake file: pkg/proxy/ipvs/ipset/testing/fake.go:39 returns_error: нет description: NewFake create a new fake ipset interface - it initialize the FakeIPSet.


### NewFake (pkg/proxy/ipvs/ipset/testing/fake.go:39)


NewFake create a new fake ipset interface - it initialize the FakeIPSet.


```go
func NewFake((version string)) (version string)
```


**Тип ответа:** version


```json
{
  "factory": {},
  "namespace": "string",
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/informers/externalversions/example3.io/v1/interface.go`


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:39`



---


[function] name: TestEntry file: pkg/proxy/ipvs/ipset/testing/fake.go:120 returns_error: да description: TestEntry is part of interface.


### TestEntry (pkg/proxy/ipvs/ipset/testing/fake.go:120)


TestEntry is part of interface.


```go
func (f *FakeIPSet) TestEntry((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/ipset/testing/fake.go:120`




## pkg/proxy/ipvs/netlink_linux.go


📄 Исходный файл: `pkg/proxy/ipvs/netlink_linux.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [DeleteDummyDevice](#deletedummydevice-pkgproxyipvsnetlink_linuxgo96) `:96`

- 🔗 [EnsureAddressBind](#ensureaddressbind-pkgproxyipvsnetlink_linuxgo45) `:45`

- 🔗 [EnsureDummyDevice](#ensuredummydevice-pkgproxyipvsnetlink_linuxgo83) `:83`

- 🔗 [GetAllLocalAddresses](#getalllocaladdresses-pkgproxyipvsnetlink_linuxgo132) `:132`

- 🔗 [GetAllLocalAddressesExcept](#getalllocaladdressesexcept-pkgproxyipvsnetlink_linuxgo173) `:173`

- 🔗 [GetLocalAddresses](#getlocaladdresses-pkgproxyipvsnetlink_linuxgo143) `:143`

- 🔗 [ListBindAddress](#listbindaddress-pkgproxyipvsnetlink_linuxgo113) `:113`

- 🔗 [NewNetLinkHandle](#newnetlinkhandle-pkgproxyipvsnetlink_linuxgo40) `:40`

- 🔗 [UnbindAddress](#unbindaddress-pkgproxyipvsnetlink_linuxgo65) `:65`

- 🔗 [isValidForSet](#isvalidforset-pkgproxyipvsnetlink_linuxgo155) `:155`


</details>


[function] name: DeleteDummyDevice file: pkg/proxy/ipvs/netlink_linux.go:96 returns_error: нет description: DeleteDummyDevice is part of interface.


### DeleteDummyDevice (pkg/proxy/ipvs/netlink_linux.go:96)


DeleteDummyDevice is part of interface.


```go
func (h *netlinkHandle) DeleteDummyDevice((devName string)) (devName string)
```


**Тип ответа:** devName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:96`



---


[function] name: EnsureAddressBind file: pkg/proxy/ipvs/netlink_linux.go:45 returns_error: да description: EnsureAddressBind checks if address is bound to the interface and, if not, binds it. If the address is already bound, re


### EnsureAddressBind (pkg/proxy/ipvs/netlink_linux.go:45)


EnsureAddressBind checks if address is bound to the interface and, if not, binds it. If the address is already bound, return true.


```go
func (h *netlinkHandle) EnsureAddressBind((exist bool, err error)) (exist bool, err error)
```


**Тип ответа:** exist


```json
{
  "matchConditionExpressions": {},
  "validationExpressions": {},
  "validationMessageExpressions": {},
  "auditAnnotationValuesExpressions": {},
  "applyConfigurationExpressions": {},
  "jsonPatchExpressions": {}
}
```


*Определено в:* `pkg/apis/admissionregistration/validation/validation.go`


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


*Типы возврата:* `exist bool`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:45`



---


[function] name: EnsureDummyDevice file: pkg/proxy/ipvs/netlink_linux.go:83 returns_error: да description: EnsureDummyDevice is part of interface


### EnsureDummyDevice (pkg/proxy/ipvs/netlink_linux.go:83)


EnsureDummyDevice is part of interface


```go
func (h *netlinkHandle) EnsureDummyDevice((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:83`



---


[function] name: GetAllLocalAddresses file: pkg/proxy/ipvs/netlink_linux.go:132 returns_error: да description: GetAllLocalAddresses return all local addresses on the node.
Only the addresses of the current family are returned.
IPv6


### GetAllLocalAddresses (pkg/proxy/ipvs/netlink_linux.go:132)


GetAllLocalAddresses return all local addresses on the node.
Only the addresses of the current family are returned.
IPv6 link-local and loopback addresses are excluded.


```go
func (h *netlinkHandle) GetAllLocalAddresses((sets.Set[string], error)) (sets.Set[string], error)
```


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `sets.Set[string]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:132`



---


[function] name: GetAllLocalAddressesExcept file: pkg/proxy/ipvs/netlink_linux.go:173 returns_error: да description: GetAllLocalAddressesExcept return all local addresses on the node,
except from the passed dev.  This is not the same as 


### GetAllLocalAddressesExcept (pkg/proxy/ipvs/netlink_linux.go:173)


GetAllLocalAddressesExcept return all local addresses on the node,
except from the passed dev.  This is not the same as to take the
diff between GetAllLocalAddresses and GetLocalAddresses since an
address can be assigned to many interfaces. This problem raised
https://github.com/kubernetes/kubernetes/issues/114815


```go
func (h *netlinkHandle) GetAllLocalAddressesExcept((sets.Set[string], error)) (sets.Set[string], error)
```


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `sets.Set[string]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:173`



---


[function] name: GetLocalAddresses file: pkg/proxy/ipvs/netlink_linux.go:143 returns_error: да description: GetLocalAddresses return all local addresses for an interface.
Only the addresses of the current family are returned.
IP


### GetLocalAddresses (pkg/proxy/ipvs/netlink_linux.go:143)


GetLocalAddresses return all local addresses for an interface.
Only the addresses of the current family are returned.
IPv6 link-local and loopback addresses are excluded.


```go
func (h *netlinkHandle) GetLocalAddresses((sets.Set[string], error)) (sets.Set[string], error)
```


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `sets.Set[string]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:143`



---


[function] name: ListBindAddress file: pkg/proxy/ipvs/netlink_linux.go:113 returns_error: да description: ListBindAddress will list all IP addresses which are bound in a given interface


### ListBindAddress (pkg/proxy/ipvs/netlink_linux.go:113)


ListBindAddress will list all IP addresses which are bound in a given interface


```go
func (h *netlinkHandle) ListBindAddress(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:113`



---


[function] name: NewNetLinkHandle file: pkg/proxy/ipvs/netlink_linux.go:40 returns_error: нет description: NewNetLinkHandle will create a new NetLinkHandle


### NewNetLinkHandle (pkg/proxy/ipvs/netlink_linux.go:40)


NewNetLinkHandle will create a new NetLinkHandle


```go
func NewNetLinkHandle((isIPv6 bool)) (isIPv6 bool)
```


**Тип ответа:** isIPv6


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:40`



---


[function] name: UnbindAddress file: pkg/proxy/ipvs/netlink_linux.go:65 returns_error: нет description: UnbindAddress makes sure IP address is unbound from the network interface.


### UnbindAddress (pkg/proxy/ipvs/netlink_linux.go:65)


UnbindAddress makes sure IP address is unbound from the network interface.


```go
func (h *netlinkHandle) UnbindAddress((address, devName string)) (address, devName string)
```


**Тип ответа:** address


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** devName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:65`



---


[function] name: isValidForSet file: pkg/proxy/ipvs/netlink_linux.go:155 returns_error: нет description: —


### isValidForSet (pkg/proxy/ipvs/netlink_linux.go:155)


isValidForSet is a method that performs operations based on the provided parameters and returns (ip net.IP).


```go
func (h *netlinkHandle) isValidForSet((ip net.IP)) (ip net.IP)
```


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `pkg/proxy/ipvs/netlink_linux.go:155`




## pkg/proxy/ipvs/proxier.go


📄 Исходный файл: `pkg/proxy/ipvs/proxier.go`


<details open>
<summary><b>Функции в этом файле (28)</b></summary>


- 🔗 [NewDualStackProxier](#newdualstackproxier-pkgproxyipvsproxiergo109) `:109`

- 🔗 [NewProxier](#newproxier-pkgproxyipvsproxiergo255) `:255`

- 🔗 [OnEndpointSliceAdd](#onendpointsliceadd-pkgproxyipvsproxiergo626) `:626`

- 🔗 [OnEndpointSliceDelete](#onendpointslicedelete-pkgproxyipvsproxiergo642) `:642`

- 🔗 [OnEndpointSliceUpdate](#onendpointsliceupdate-pkgproxyipvsproxiergo634) `:634`

- 🔗 [OnEndpointSlicesSynced](#onendpointslicessynced-pkgproxyipvsproxiergo650) `:650`

- 🔗 [OnServiceAdd](#onserviceadd-pkgproxyipvsproxiergo597) `:597`

- 🔗 [OnServiceCIDRsChanged](#onservicecidrschanged-pkgproxyipvsproxiergo671) `:671`

- 🔗 [OnServiceDelete](#onservicedelete-pkgproxyipvsproxiergo609) `:609`

- 🔗 [OnServiceSynced](#onservicesynced-pkgproxyipvsproxiergo614) `:614`

- 🔗 [OnServiceUpdate](#onserviceupdate-pkgproxyipvsproxiergo602) `:602`

- 🔗 [OnTopologyChange](#ontopologychange-pkgproxyipvsproxiergo661) `:661`

- 🔗 [Sync](#sync-pkgproxyipvsproxiergo565) `:565`

- 🔗 [SyncLoop](#syncloop-pkgproxyipvsproxiergo574) `:574`

- 🔗 [acceptIPVSTraffic](#acceptipvstraffic-pkgproxyipvsproxiergo1510) `:1510`

- 🔗 [cleanLegacyService](#cleanlegacyservice-pkgproxyipvsproxiergo1738) `:1738`

- 🔗 [createAndLinkKubeChain](#createandlinkkubechain-pkgproxyipvsproxiergo1531) `:1531`

- 🔗 [filterCIDRs](#filtercidrs-pkgproxyipvsproxiergo409) `:409`

- 🔗 [getFirstColumn](#getfirstcolumn-pkgproxyipvsproxiergo547) `:547`

- 🔗 [getIPFamily](#getipfamily-pkgproxyipvsproxiergo1766) `:1766`

- 🔗 [isIPInExcludeCIDRs](#isipinexcludecidrs-pkgproxyipvsproxiergo1756) `:1756`

- 🔗 [isInitialized](#isinitialized-pkgproxyipvsproxiergo592) `:592`

- 🔗 [newServiceInfo](#newserviceinfo-pkgproxyipvsproxiergo534) `:534`

- 🔗 [setInitialized](#setinitialized-pkgproxyipvsproxiergo584) `:584`

- 🔗 [syncEndpoint](#syncendpoint-pkgproxyipvsproxiergo1593) `:1593`

- 🔗 [syncProxyRules](#syncproxyrules-pkgproxyipvsproxiergo674) `:674`

- 🔗 [syncService](#syncservice-pkgproxyipvsproxiergo1553) `:1553`

- 🔗 [writeIptablesRules](#writeiptablesrules-pkgproxyipvsproxiergo1275) `:1275`


</details>


[function] name: NewDualStackProxier file: pkg/proxy/ipvs/proxier.go:109 returns_error: да description: NewDualStackProxier returns a new Proxier for dual-stack operation


### NewDualStackProxier (pkg/proxy/ipvs/proxier.go:109)


NewDualStackProxier returns a new Proxier for dual-stack operation


```go
func NewDualStackProxier((proxy.Provider, error)) (proxy.Provider, error)
```


**Тип ответа:** proxy.Provider


```json
{
  "cadvisor": {},
  "podManager": {}
}
```


*Определено в:* `pkg/kubelet/stats/provider.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `proxy.Provider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:109`



---


[function] name: NewProxier file: pkg/proxy/ipvs/proxier.go:255 returns_error: да description: NewProxier returns a new single-stack IPVS proxier.


### NewProxier (pkg/proxy/ipvs/proxier.go:255)


NewProxier returns a new single-stack IPVS proxier.


```go
func NewProxier((*Proxier, error)) (*Proxier, error)
```


**Тип запроса:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Proxier`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:255`



---


[function] name: OnEndpointSliceAdd file: pkg/proxy/ipvs/proxier.go:626 returns_error: нет description: OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


### OnEndpointSliceAdd (pkg/proxy/ipvs/proxier.go:626)


OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


```go
func (proxier *Proxier) OnEndpointSliceAdd((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:626`



---


[function] name: OnEndpointSliceDelete file: pkg/proxy/ipvs/proxier.go:642 returns_error: нет description: OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


### OnEndpointSliceDelete (pkg/proxy/ipvs/proxier.go:642)


OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


```go
func (proxier *Proxier) OnEndpointSliceDelete((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:642`



---


[function] name: OnEndpointSliceUpdate file: pkg/proxy/ipvs/proxier.go:634 returns_error: нет description: OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


### OnEndpointSliceUpdate (pkg/proxy/ipvs/proxier.go:634)


OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


```go
func (proxier *Proxier) OnEndpointSliceUpdate((_, endpointSlice *discovery.EndpointSlice)) (_, endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:634`



---


[function] name: OnEndpointSlicesSynced file: pkg/proxy/ipvs/proxier.go:650 returns_error: нет description: OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to lo


### OnEndpointSlicesSynced (pkg/proxy/ipvs/proxier.go:650)


OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *Proxier) OnEndpointSlicesSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:650`



---


[function] name: OnServiceAdd file: pkg/proxy/ipvs/proxier.go:597 returns_error: нет description: OnServiceAdd is called whenever creation of new service object is observed.


### OnServiceAdd (pkg/proxy/ipvs/proxier.go:597)


OnServiceAdd is called whenever creation of new service object is observed.


```go
func (proxier *Proxier) OnServiceAdd((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:597`



---


[function] name: OnServiceCIDRsChanged file: pkg/proxy/ipvs/proxier.go:671 returns_error: нет description: OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of 


### OnServiceCIDRsChanged (pkg/proxy/ipvs/proxier.go:671)


OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of service cidrs.


```go
func (proxier *Proxier) OnServiceCIDRsChanged((_ []string)) (_ []string)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:671`



---


[function] name: OnServiceDelete file: pkg/proxy/ipvs/proxier.go:609 returns_error: нет description: OnServiceDelete is called whenever deletion of an existing service object is observed.


### OnServiceDelete (pkg/proxy/ipvs/proxier.go:609)


OnServiceDelete is called whenever deletion of an existing service object is observed.


```go
func (proxier *Proxier) OnServiceDelete((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:609`



---


[function] name: OnServiceSynced file: pkg/proxy/ipvs/proxier.go:614 returns_error: нет description: OnServiceSynced is called once all the initial event handlers were called and the state is fully propagated to local cac


### OnServiceSynced (pkg/proxy/ipvs/proxier.go:614)


OnServiceSynced is called once all the initial event handlers were called and the state is fully propagated to local cache.


```go
func (proxier *Proxier) OnServiceSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:614`



---


[function] name: OnServiceUpdate file: pkg/proxy/ipvs/proxier.go:602 returns_error: нет description: OnServiceUpdate is called whenever modification of an existing service object is observed.


### OnServiceUpdate (pkg/proxy/ipvs/proxier.go:602)


OnServiceUpdate is called whenever modification of an existing service object is observed.


```go
func (proxier *Proxier) OnServiceUpdate((oldService, service *v1.Service)) (oldService, service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:602`



---


[function] name: OnTopologyChange file: pkg/proxy/ipvs/proxier.go:661 returns_error: нет description: OnTopologyChange is called whenever this node's proxy relevant topology-related labels change.


### OnTopologyChange (pkg/proxy/ipvs/proxier.go:661)


OnTopologyChange is called whenever this node's proxy relevant topology-related labels change.


```go
func (proxier *Proxier) OnTopologyChange((topologyLabels map[string]string)) (topologyLabels map[string]string)
```


**Тип ответа:** topologyLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:661`



---


[function] name: Sync file: pkg/proxy/ipvs/proxier.go:565 returns_error: нет description: Sync is called to synchronize the proxier state to iptables and ipvs as soon as possible.


### Sync (pkg/proxy/ipvs/proxier.go:565)


Sync is called to synchronize the proxier state to iptables and ipvs as soon as possible.


```go
func (proxier *Proxier) Sync(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:565`



---


[function] name: SyncLoop file: pkg/proxy/ipvs/proxier.go:574 returns_error: нет description: SyncLoop runs periodic work.  This is expected to run as a goroutine or as the main loop of the app.  It does not return


### SyncLoop (pkg/proxy/ipvs/proxier.go:574)


SyncLoop runs periodic work.  This is expected to run as a goroutine or as the main loop of the app.  It does not return.


```go
func (proxier *Proxier) SyncLoop(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:574`



---


[function] name: acceptIPVSTraffic file: pkg/proxy/ipvs/proxier.go:1510 returns_error: нет description: —


### acceptIPVSTraffic (pkg/proxy/ipvs/proxier.go:1510)


acceptIPVSTraffic is a method that performs operations based on the provided parameters and returns ().


```go
func (proxier *Proxier) acceptIPVSTraffic(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:1510`



---


[function] name: cleanLegacyService file: pkg/proxy/ipvs/proxier.go:1738 returns_error: нет description: —


### cleanLegacyService (pkg/proxy/ipvs/proxier.go:1738)


cleanLegacyService is a method that performs operations based on the provided parameters and returns (activeServices sets.Set[string], currentServices map[string]*utilipvs.VirtualServer).


```go
func (proxier *Proxier) cleanLegacyService((activeServices sets.Set[string], currentServices map[string]*utilipvs.VirtualServer)) (activeServices sets.Set[string], currentServices map[string]*utilipvs.VirtualServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** activeServices


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Тип ответа:** currentServices


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:1738`



---


[function] name: createAndLinkKubeChain file: pkg/proxy/ipvs/proxier.go:1531 returns_error: нет description: createAndLinkKubeChain create all kube chains that ipvs proxier need and write basic link.


### createAndLinkKubeChain (pkg/proxy/ipvs/proxier.go:1531)


createAndLinkKubeChain create all kube chains that ipvs proxier need and write basic link.


```go
func (proxier *Proxier) createAndLinkKubeChain(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:1531`



---


[function] name: filterCIDRs file: pkg/proxy/ipvs/proxier.go:409 returns_error: нет description: —


### filterCIDRs (pkg/proxy/ipvs/proxier.go:409)


filterCIDRs is a function that performs operations based on the provided parameters and returns (wantIPv6 bool, cidrs []string).


```go
func filterCIDRs((wantIPv6 bool, cidrs []string)) (wantIPv6 bool, cidrs []string)
```


**Тип ответа:** wantIPv6


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cidrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:409`



---


[function] name: getFirstColumn file: pkg/proxy/ipvs/proxier.go:547 returns_error: да description: getFirstColumn reads all the content from r into memory and return a
slice which consists of the first word from each li


### getFirstColumn (pkg/proxy/ipvs/proxier.go:547)


getFirstColumn reads all the content from r into memory and return a
slice which consists of the first word from each line.


```go
func getFirstColumn(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:547`



---


[function] name: getIPFamily file: pkg/proxy/ipvs/proxier.go:1766 returns_error: нет description: —


### getIPFamily (pkg/proxy/ipvs/proxier.go:1766)


getIPFamily is a function that performs operations based on the provided parameters and returns (ip net.IP).


```go
func getIPFamily((ip net.IP)) (ip net.IP)
```


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:1766`



---


[function] name: isIPInExcludeCIDRs file: pkg/proxy/ipvs/proxier.go:1756 returns_error: нет description: —


### isIPInExcludeCIDRs (pkg/proxy/ipvs/proxier.go:1756)


isIPInExcludeCIDRs is a method that performs operations based on the provided parameters and returns (ip net.IP).


```go
func (proxier *Proxier) isIPInExcludeCIDRs((ip net.IP)) (ip net.IP)
```


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:1756`



---


[function] name: isInitialized file: pkg/proxy/ipvs/proxier.go:592 returns_error: нет description: —


### isInitialized (pkg/proxy/ipvs/proxier.go:592)


isInitialized is a method that performs operations based on the provided parameters and returns ().


```go
func (proxier *Proxier) isInitialized(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:592`



---


[function] name: newServiceInfo file: pkg/proxy/ipvs/proxier.go:534 returns_error: нет description: returns a new proxy.ServicePort which abstracts a serviceInfo


### newServiceInfo (pkg/proxy/ipvs/proxier.go:534)


returns a new proxy.ServicePort which abstracts a serviceInfo


```go
func newServiceInfo((port *v1.ServicePort, service *v1.Service, bsvcPortInfo *proxy.BaseServicePortInfo)) (port *v1.ServicePort, service *v1.Service, bsvcPortInfo *proxy.BaseServicePortInfo)
```


**Тип запроса:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** proxy.BaseServicePortInfo


```json
{
  "clusterIP": {},
  "port": 0,
  "protocol": {},
  "nodePort": 0,
  "loadBalancerVIPs": [],
  "sessionAffinityType": {},
  "stickyMaxAgeSeconds": 0,
  "externalIPs": [],
  "loadBalancerSourceRanges": [],
  "healthCheckNodePort": 0,
  "externalPolicyLocal": false,
  "internalPolicyLocal": false
}
```


*Определено в:* `pkg/proxy/serviceport.go`


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


**Тип ответа:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** bsvcPortInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.BaseServicePortInfo


```json
{
  "clusterIP": {},
  "port": 0,
  "protocol": {},
  "nodePort": 0,
  "loadBalancerVIPs": [],
  "sessionAffinityType": {},
  "stickyMaxAgeSeconds": 0,
  "externalIPs": [],
  "loadBalancerSourceRanges": [],
  "healthCheckNodePort": 0,
  "externalPolicyLocal": false,
  "internalPolicyLocal": false
}
```


*Определено в:* `pkg/proxy/serviceport.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:534`



---


[function] name: setInitialized file: pkg/proxy/ipvs/proxier.go:584 returns_error: нет description: —


### setInitialized (pkg/proxy/ipvs/proxier.go:584)


setInitialized is a method that performs operations based on the provided parameters and returns (value bool).


```go
func (proxier *Proxier) setInitialized((value bool)) (value bool)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:584`



---


[function] name: syncEndpoint file: pkg/proxy/ipvs/proxier.go:1593 returns_error: нет description: —


### syncEndpoint (pkg/proxy/ipvs/proxier.go:1593)


syncEndpoint is a method that performs operations based on the provided parameters and returns (svcPortName proxy.ServicePortName, onlyNodeLocalEndpoints bool, vs *utilipvs.VirtualServer).


```go
func (proxier *Proxier) syncEndpoint((svcPortName proxy.ServicePortName, onlyNodeLocalEndpoints bool, vs *utilipvs.VirtualServer)) (svcPortName proxy.ServicePortName, onlyNodeLocalEndpoints bool, vs *utilipvs.VirtualServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** svcPortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** onlyNodeLocalEndpoints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:1593`



---


[function] name: syncProxyRules file: pkg/proxy/ipvs/proxier.go:674 returns_error: да description: This is where all of the ipvs calls happen.


### syncProxyRules (pkg/proxy/ipvs/proxier.go:674)


This is where all of the ipvs calls happen.


```go
func (proxier *Proxier) syncProxyRules((retryError error)) (retryError error)
```


**Тип ответа:** retryError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `retryError error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:674`



---


[function] name: syncService file: pkg/proxy/ipvs/proxier.go:1553 returns_error: нет description: —


### syncService (pkg/proxy/ipvs/proxier.go:1553)


syncService is a method that performs operations based on the provided parameters and returns (svcName string, vs *utilipvs.VirtualServer, bindAddr bool, alreadyBoundAddrs sets.Set[string]).


```go
func (proxier *Proxier) syncService((svcName string, vs *utilipvs.VirtualServer, bindAddr bool, alreadyBoundAddrs sets.Set[string])) (svcName string, vs *utilipvs.VirtualServer, bindAddr bool, alreadyBoundAddrs sets.Set[string])
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** svcName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** bindAddr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** alreadyBoundAddrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:1553`



---


[function] name: writeIptablesRules file: pkg/proxy/ipvs/proxier.go:1275 returns_error: нет description: writeIptablesRules write all iptables rules to proxier.natRules or proxier.FilterRules that ipvs proxier needed
accordin


### writeIptablesRules (pkg/proxy/ipvs/proxier.go:1275)


writeIptablesRules write all iptables rules to proxier.natRules or proxier.FilterRules that ipvs proxier needed
according to proxier.ipsetList information and the ipset match relationship that `ipsetWithIptablesChain` specified.
some ipset(kubeClusterIPSet for example) have particular match rules and iptables jump relation should be sync separately.


```go
func (proxier *Proxier) writeIptablesRules(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/proxier.go:1275`




## pkg/proxy/ipvs/supported.go


📄 Исходный файл: `pkg/proxy/ipvs/supported.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CanUseIPVSProxier](#canuseipvsproxier-pkgproxyipvssupportedgo35) `:35`


</details>


[function] name: CanUseIPVSProxier file: pkg/proxy/ipvs/supported.go:35 returns_error: нет description: CanUseIPVSProxier checks if we can use the ipvs Proxier.
The ipset version and the scheduler are checked. If any virtual


### CanUseIPVSProxier (pkg/proxy/ipvs/supported.go:35)


CanUseIPVSProxier checks if we can use the ipvs Proxier.
The ipset version and the scheduler are checked. If any virtual servers (VS)
already exist with the configured scheduler, we just return. Otherwise
we check if a dummy VS can be configured with the configured scheduler.
Kernel modules will be loaded automatically if necessary.


```go
func CanUseIPVSProxier((ctx context.Context, ipvs utilipvs.Interface, ipsetver IPSetVersioner, scheduler string)) (ctx context.Context, ipvs utilipvs.Interface, ipsetver IPSetVersioner, scheduler string)
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


**Тип ответа:** ipvs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** utilipvs.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** ipsetver


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** IPSetVersioner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** scheduler


```json
{
  "prepareFn": {}
}
```


*Определено в:* `test/integration/scheduler_perf/options.go`


📍 *Расположение:* `pkg/proxy/ipvs/supported.go:35`




## pkg/proxy/ipvs/testing/fake.go


📄 Исходный файл: `pkg/proxy/ipvs/testing/fake.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [DeleteDummyDevice](#deletedummydevice-pkgproxyipvstestingfakego98) `:98`

- 🔗 [EnsureAddressBind](#ensureaddressbind-pkgproxyipvstestingfakego47) `:47`

- 🔗 [EnsureDummyDevice](#ensuredummydevice-pkgproxyipvstestingfakego84) `:84`

- 🔗 [GetAllLocalAddresses](#getalllocaladdresses-pkgproxyipvstestingfakego131) `:131`

- 🔗 [GetAllLocalAddressesExcept](#getalllocaladdressesexcept-pkgproxyipvstestingfakego145) `:145`

- 🔗 [GetLocalAddresses](#getlocaladdresses-pkgproxyipvstestingfakego121) `:121`

- 🔗 [ListBindAddress](#listbindaddress-pkgproxyipvstestingfakego110) `:110`

- 🔗 [NewFakeNetlinkHandle](#newfakenetlinkhandle-pkgproxyipvstestingfakego38) `:38`

- 🔗 [SetLocalAddresses](#setlocaladdresses-pkgproxyipvstestingfakego161) `:161`

- 🔗 [UnbindAddress](#unbindaddress-pkgproxyipvstestingfakego65) `:65`

- 🔗 [isValidForSet](#isvalidforset-pkgproxyipvstestingfakego173) `:173`


</details>


[function] name: DeleteDummyDevice file: pkg/proxy/ipvs/testing/fake.go:98 returns_error: нет description: DeleteDummyDevice is a mock implementation


### DeleteDummyDevice (pkg/proxy/ipvs/testing/fake.go:98)


DeleteDummyDevice is a mock implementation


```go
func (h *FakeNetlinkHandle) DeleteDummyDevice((devName string)) (devName string)
```


**Тип ответа:** devName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:98`



---


[function] name: EnsureAddressBind file: pkg/proxy/ipvs/testing/fake.go:47 returns_error: да description: EnsureAddressBind is a mock implementation


### EnsureAddressBind (pkg/proxy/ipvs/testing/fake.go:47)


EnsureAddressBind is a mock implementation


```go
func (h *FakeNetlinkHandle) EnsureAddressBind((exist bool, err error)) (exist bool, err error)
```


**Тип ответа:** exist


```json
{
  "matchConditionExpressions": {},
  "validationExpressions": {},
  "validationMessageExpressions": {},
  "auditAnnotationValuesExpressions": {},
  "applyConfigurationExpressions": {},
  "jsonPatchExpressions": {}
}
```


*Определено в:* `pkg/apis/admissionregistration/validation/validation.go`


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


*Типы возврата:* `exist bool`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:47`



---


[function] name: EnsureDummyDevice file: pkg/proxy/ipvs/testing/fake.go:84 returns_error: да description: EnsureDummyDevice is a mock implementation


### EnsureDummyDevice (pkg/proxy/ipvs/testing/fake.go:84)


EnsureDummyDevice is a mock implementation


```go
func (h *FakeNetlinkHandle) EnsureDummyDevice((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:84`



---


[function] name: GetAllLocalAddresses file: pkg/proxy/ipvs/testing/fake.go:131 returns_error: да description: —


### GetAllLocalAddresses (pkg/proxy/ipvs/testing/fake.go:131)


GetAllLocalAddresses is a method that retrieves data based on the provided parameters and may return an error.


```go
func (h *FakeNetlinkHandle) GetAllLocalAddresses((sets.Set[string], error)) (sets.Set[string], error)
```


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `sets.Set[string]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:131`



---


[function] name: GetAllLocalAddressesExcept file: pkg/proxy/ipvs/testing/fake.go:145 returns_error: да description: —


### GetAllLocalAddressesExcept (pkg/proxy/ipvs/testing/fake.go:145)


GetAllLocalAddressesExcept is a method that retrieves data based on the provided parameters and may return an error.


```go
func (h *FakeNetlinkHandle) GetAllLocalAddressesExcept((sets.Set[string], error)) (sets.Set[string], error)
```


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `sets.Set[string]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:145`



---


[function] name: GetLocalAddresses file: pkg/proxy/ipvs/testing/fake.go:121 returns_error: да description: GetLocalAddresses is a mock implementation


### GetLocalAddresses (pkg/proxy/ipvs/testing/fake.go:121)


GetLocalAddresses is a mock implementation


```go
func (h *FakeNetlinkHandle) GetLocalAddresses((sets.Set[string], error)) (sets.Set[string], error)
```


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `sets.Set[string]`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:121`



---


[function] name: ListBindAddress file: pkg/proxy/ipvs/testing/fake.go:110 returns_error: да description: ListBindAddress is a mock implementation


### ListBindAddress (pkg/proxy/ipvs/testing/fake.go:110)


ListBindAddress is a mock implementation


```go
func (h *FakeNetlinkHandle) ListBindAddress(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:110`



---


[function] name: NewFakeNetlinkHandle file: pkg/proxy/ipvs/testing/fake.go:38 returns_error: нет description: NewFakeNetlinkHandle will create a new FakeNetlinkHandle


### NewFakeNetlinkHandle (pkg/proxy/ipvs/testing/fake.go:38)


NewFakeNetlinkHandle will create a new FakeNetlinkHandle


```go
func NewFakeNetlinkHandle((isIPv6 bool)) (isIPv6 bool)
```


**Тип ответа:** isIPv6


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:38`



---


[function] name: SetLocalAddresses file: pkg/proxy/ipvs/testing/fake.go:161 returns_error: нет description: SetLocalAddresses set IP addresses to the given interface device.  It's not part of interface.


### SetLocalAddresses (pkg/proxy/ipvs/testing/fake.go:161)


SetLocalAddresses set IP addresses to the given interface device.  It's not part of interface.


```go
func (h *FakeNetlinkHandle) SetLocalAddresses((dev string, ips ...string)) (dev string, ips ...string)
```


**Тип ответа:** dev


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/resource/v1beta1/deviceclass.go`


**Тип ответа:** ips


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:161`



---


[function] name: UnbindAddress file: pkg/proxy/ipvs/testing/fake.go:65 returns_error: нет description: UnbindAddress is a mock implementation


### UnbindAddress (pkg/proxy/ipvs/testing/fake.go:65)


UnbindAddress is a mock implementation


```go
func (h *FakeNetlinkHandle) UnbindAddress((address, devName string)) (address, devName string)
```


**Тип ответа:** address


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** devName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:65`



---


[function] name: isValidForSet file: pkg/proxy/ipvs/testing/fake.go:173 returns_error: нет description: —


### isValidForSet (pkg/proxy/ipvs/testing/fake.go:173)


isValidForSet is a method that performs operations based on the provided parameters and returns (ipString string).


```go
func (h *FakeNetlinkHandle) isValidForSet((ipString string)) (ipString string)
```


**Тип ответа:** ipString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/testing/fake.go:173`




## pkg/proxy/ipvs/util/ipvs.go


📄 Исходный файл: `pkg/proxy/ipvs/util/ipvs.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Equal](#equal-pkgproxyipvsutilipvsgo78) `:78`

- 🔗 [Equal](#equal-pkgproxyipvsutilipvsgo106) `:106`

- 🔗 [IsRsGracefulTerminationNeeded](#isrsgracefulterminationneeded-pkgproxyipvsutilipvsgo112) `:112`

- 🔗 [String](#string-pkgproxyipvsutilipvsgo87) `:87`

- 🔗 [String](#string-pkgproxyipvsutilipvsgo100) `:100`


</details>


[function] name: Equal file: pkg/proxy/ipvs/util/ipvs.go:78 returns_error: нет description: Equal check the equality of virtual server.
We don't use struct == since it doesn't work because of slice.


### Equal (pkg/proxy/ipvs/util/ipvs.go:78)


Equal check the equality of virtual server.
We don't use struct == since it doesn't work because of slice.


```go
func (svc *VirtualServer) Equal((other *VirtualServer)) (other *VirtualServer)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** other


```json
{
  "OS": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ordering/structs/doc.go`


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs.go:78`



---


[function] name: Equal file: pkg/proxy/ipvs/util/ipvs.go:106 returns_error: нет description: Equal check the equality of real server.
We don't use struct == since it doesn't work because of slice.


### Equal (pkg/proxy/ipvs/util/ipvs.go:106)


Equal check the equality of real server.
We don't use struct == since it doesn't work because of slice.


```go
func (rs *RealServer) Equal((other *RealServer)) (other *RealServer)
```


**Тип запроса:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** other


```json
{
  "OS": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ordering/structs/doc.go`


**Тип ответа:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs.go:106`



---


[function] name: IsRsGracefulTerminationNeeded file: pkg/proxy/ipvs/util/ipvs.go:112 returns_error: нет description: IsRsGracefulTerminationNeeded returns true if protocol requires graceful termination for the stale connections


### IsRsGracefulTerminationNeeded (pkg/proxy/ipvs/util/ipvs.go:112)


IsRsGracefulTerminationNeeded returns true if protocol requires graceful termination for the stale connections


```go
func IsRsGracefulTerminationNeeded((proto string)) (proto string)
```


**Тип ответа:** proto


```json
{
  "providerID": "string"
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/controllers/service/controller.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs.go:112`



---


[function] name: String file: pkg/proxy/ipvs/util/ipvs.go:87 returns_error: нет description: —


### String (pkg/proxy/ipvs/util/ipvs.go:87)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (svc *VirtualServer) String(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs.go:87`



---


[function] name: String file: pkg/proxy/ipvs/util/ipvs.go:100 returns_error: нет description: —


### String (pkg/proxy/ipvs/util/ipvs.go:100)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (rs *RealServer) String(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs.go:100`




## pkg/proxy/ipvs/util/ipvs_linux.go


📄 Исходный файл: `pkg/proxy/ipvs/util/ipvs_linux.go`


<details open>
<summary><b>Функции в этом файле (18)</b></summary>


- 🔗 [AddRealServer](#addrealserver-pkgproxyipvsutilipvs_linuxgo136) `:136`

- 🔗 [AddVirtualServer](#addvirtualserver-pkgproxyipvsutilipvs_linuxgo57) `:57`

- 🔗 [ConfigureTimeouts](#configuretimeouts-pkgproxyipvsutilipvs_linuxgo204) `:204`

- 🔗 [DeleteRealServer](#deleterealserver-pkgproxyipvsutilipvs_linuxgo151) `:151`

- 🔗 [DeleteVirtualServer](#deletevirtualserver-pkgproxyipvsutilipvs_linuxgo79) `:79`

- 🔗 [Flush](#flush-pkgproxyipvsutilipvs_linuxgo129) `:129`

- 🔗 [GetRealServers](#getrealservers-pkgproxyipvsutilipvs_linuxgo180) `:180`

- 🔗 [GetVirtualServer](#getvirtualserver-pkgproxyipvsutilipvs_linuxgo90) `:90`

- 🔗 [GetVirtualServers](#getvirtualservers-pkgproxyipvsutilipvs_linuxgo110) `:110`

- 🔗 [New](#new-pkgproxyipvsutilipvs_linuxgo45) `:45`

- 🔗 [UpdateRealServer](#updaterealserver-pkgproxyipvsutilipvs_linuxgo165) `:165`

- 🔗 [UpdateVirtualServer](#updatevirtualserver-pkgproxyipvsutilipvs_linuxgo68) `:68`

- 🔗 [protocolToString](#protocoltostring-pkgproxyipvsutilipvs_linuxgo309) `:309`

- 🔗 [stringToProtocol](#stringtoprotocol-pkgproxyipvsutilipvs_linuxgo296) `:296`

- 🔗 [toIPVSDestination](#toipvsdestination-pkgproxyipvsutilipvs_linuxgo284) `:284`

- 🔗 [toIPVSService](#toipvsservice-pkgproxyipvsutilipvs_linuxgo260) `:260`

- 🔗 [toRealServer](#torealserver-pkgproxyipvsutilipvs_linuxgo246) `:246`

- 🔗 [toVirtualServer](#tovirtualserver-pkgproxyipvsutilipvs_linuxgo215) `:215`


</details>


[function] name: AddRealServer file: pkg/proxy/ipvs/util/ipvs_linux.go:136 returns_error: нет description: AddRealServer is part of ipvs.Interface.


### AddRealServer (pkg/proxy/ipvs/util/ipvs_linux.go:136)


AddRealServer is part of ipvs.Interface.


```go
func (runner *runner) AddRealServer((vs *VirtualServer, rs *RealServer)) (vs *VirtualServer, rs *RealServer)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип запроса:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:136`



---


[function] name: AddVirtualServer file: pkg/proxy/ipvs/util/ipvs_linux.go:57 returns_error: нет description: AddVirtualServer is part of ipvs.Interface.


### AddVirtualServer (pkg/proxy/ipvs/util/ipvs_linux.go:57)


AddVirtualServer is part of ipvs.Interface.


```go
func (runner *runner) AddVirtualServer((vs *VirtualServer)) (vs *VirtualServer)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:57`



---


[function] name: ConfigureTimeouts file: pkg/proxy/ipvs/util/ipvs_linux.go:204 returns_error: нет description: ConfigureTimeouts is the equivalent to running "ipvsadm --set" to configure tcp, tcpfin and udp timeouts


### ConfigureTimeouts (pkg/proxy/ipvs/util/ipvs_linux.go:204)


ConfigureTimeouts is the equivalent to running "ipvsadm --set" to configure tcp, tcpfin and udp timeouts


```go
func (runner *runner) ConfigureTimeouts((tcpTimeout, tcpFinTimeout, udpTimeout time.Duration)) (tcpTimeout, tcpFinTimeout, udpTimeout time.Duration)
```


**Тип ответа:** tcpTimeout


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tcpFinTimeout


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** udpTimeout


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


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:204`



---


[function] name: DeleteRealServer file: pkg/proxy/ipvs/util/ipvs_linux.go:151 returns_error: нет description: DeleteRealServer is part of ipvs.Interface.


### DeleteRealServer (pkg/proxy/ipvs/util/ipvs_linux.go:151)


DeleteRealServer is part of ipvs.Interface.


```go
func (runner *runner) DeleteRealServer((vs *VirtualServer, rs *RealServer)) (vs *VirtualServer, rs *RealServer)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип запроса:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:151`



---


[function] name: DeleteVirtualServer file: pkg/proxy/ipvs/util/ipvs_linux.go:79 returns_error: нет description: DeleteVirtualServer is part of ipvs.Interface.


### DeleteVirtualServer (pkg/proxy/ipvs/util/ipvs_linux.go:79)


DeleteVirtualServer is part of ipvs.Interface.


```go
func (runner *runner) DeleteVirtualServer((vs *VirtualServer)) (vs *VirtualServer)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:79`



---


[function] name: Flush file: pkg/proxy/ipvs/util/ipvs_linux.go:129 returns_error: нет description: Flush is part of ipvs.Interface. Currently we delete IPVS services one by one


### Flush (pkg/proxy/ipvs/util/ipvs_linux.go:129)


Flush is part of ipvs.Interface. Currently we delete IPVS services one by one


```go
func (runner *runner) Flush(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:129`



---


[function] name: GetRealServers file: pkg/proxy/ipvs/util/ipvs_linux.go:180 returns_error: да description: GetRealServers is part of ipvs.Interface.


### GetRealServers (pkg/proxy/ipvs/util/ipvs_linux.go:180)


GetRealServers is part of ipvs.Interface.


```go
func (runner *runner) GetRealServers(([]*RealServer, error)) ([]*RealServer, error)
```


**Тип запроса:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*RealServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:180`



---


[function] name: GetVirtualServer file: pkg/proxy/ipvs/util/ipvs_linux.go:90 returns_error: да description: GetVirtualServer is part of ipvs.Interface.


### GetVirtualServer (pkg/proxy/ipvs/util/ipvs_linux.go:90)


GetVirtualServer is part of ipvs.Interface.


```go
func (runner *runner) GetVirtualServer((*VirtualServer, error)) (*VirtualServer, error)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VirtualServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:90`



---


[function] name: GetVirtualServers file: pkg/proxy/ipvs/util/ipvs_linux.go:110 returns_error: да description: GetVirtualServers is part of ipvs.Interface.


### GetVirtualServers (pkg/proxy/ipvs/util/ipvs_linux.go:110)


GetVirtualServers is part of ipvs.Interface.


```go
func (runner *runner) GetVirtualServers(([]*VirtualServer, error)) ([]*VirtualServer, error)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*VirtualServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:110`



---


[function] name: New file: pkg/proxy/ipvs/util/ipvs_linux.go:45 returns_error: нет description: New returns a new Interface which will call ipvs APIs.


### New (pkg/proxy/ipvs/util/ipvs_linux.go:45)


New returns a new Interface which will call ipvs APIs.


```go
func New(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:45`



---


[function] name: UpdateRealServer file: pkg/proxy/ipvs/util/ipvs_linux.go:165 returns_error: нет description: —


### UpdateRealServer (pkg/proxy/ipvs/util/ipvs_linux.go:165)


UpdateRealServer is a method that updates data based on the provided parameters and returns (vs *VirtualServer, rs *RealServer).


```go
func (runner *runner) UpdateRealServer((vs *VirtualServer, rs *RealServer)) (vs *VirtualServer, rs *RealServer)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип запроса:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:165`



---


[function] name: UpdateVirtualServer file: pkg/proxy/ipvs/util/ipvs_linux.go:68 returns_error: нет description: UpdateVirtualServer is part of ipvs.Interface.


### UpdateVirtualServer (pkg/proxy/ipvs/util/ipvs_linux.go:68)


UpdateVirtualServer is part of ipvs.Interface.


```go
func (runner *runner) UpdateVirtualServer((vs *VirtualServer)) (vs *VirtualServer)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** vs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:68`



---


[function] name: protocolToString file: pkg/proxy/ipvs/util/ipvs_linux.go:309 returns_error: нет description: protocolTypeToString returns the name for the given protocol.


### protocolToString (pkg/proxy/ipvs/util/ipvs_linux.go:309)


protocolTypeToString returns the name for the given protocol.


```go
func protocolToString((proto Protocol)) (proto Protocol)
```


**Тип ответа:** proto


```json
{
  "providerID": "string"
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/controllers/service/controller.go`


**Тип ответа:** Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:309`



---


[function] name: stringToProtocol file: pkg/proxy/ipvs/util/ipvs_linux.go:296 returns_error: нет description: stringToProtocolType returns the protocol type for the given name


### stringToProtocol (pkg/proxy/ipvs/util/ipvs_linux.go:296)


stringToProtocolType returns the protocol type for the given name


```go
func stringToProtocol((protocol string)) (protocol string)
```


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:296`



---


[function] name: toIPVSDestination file: pkg/proxy/ipvs/util/ipvs_linux.go:284 returns_error: да description: toIPVSDestination converts a RealServer to the equivalent IPVS Destination structure.


### toIPVSDestination (pkg/proxy/ipvs/util/ipvs_linux.go:284)


toIPVSDestination converts a RealServer to the equivalent IPVS Destination structure.


```go
func toIPVSDestination((*libipvs.Destination, error)) (*libipvs.Destination, error)
```


**Тип запроса:** libipvs.Destination


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** libipvs.Destination


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*libipvs.Destination`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:284`



---


[function] name: toIPVSService file: pkg/proxy/ipvs/util/ipvs_linux.go:260 returns_error: да description: toIPVSService converts a VirtualServer to the equivalent IPVS Service structure.


### toIPVSService (pkg/proxy/ipvs/util/ipvs_linux.go:260)


toIPVSService converts a VirtualServer to the equivalent IPVS Service structure.


```go
func toIPVSService((*libipvs.Service, error)) (*libipvs.Service, error)
```


**Тип запроса:** libipvs.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** libipvs.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*libipvs.Service`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:260`



---


[function] name: toRealServer file: pkg/proxy/ipvs/util/ipvs_linux.go:246 returns_error: да description: toRealServer converts an IPVS Destination to the equivalent RealServer structure.


### toRealServer (pkg/proxy/ipvs/util/ipvs_linux.go:246)


toRealServer converts an IPVS Destination to the equivalent RealServer structure.


```go
func toRealServer((*RealServer, error)) (*RealServer, error)
```


**Тип запроса:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*RealServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:246`



---


[function] name: toVirtualServer file: pkg/proxy/ipvs/util/ipvs_linux.go:215 returns_error: да description: toVirtualServer converts an IPVS Service to the equivalent VirtualServer structure.


### toVirtualServer (pkg/proxy/ipvs/util/ipvs_linux.go:215)


toVirtualServer converts an IPVS Service to the equivalent VirtualServer structure.


```go
func toVirtualServer((*VirtualServer, error)) (*VirtualServer, error)
```


**Тип запроса:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VirtualServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/ipvs_linux.go:215`




## pkg/proxy/ipvs/util/testing/fake.go


📄 Исходный файл: `pkg/proxy/ipvs/util/testing/fake.go`


<details open>
<summary><b>Функции в этом файле (19)</b></summary>


- 🔗 [AddRealServer](#addrealserver-pkgproxyipvsutiltestingfakego160) `:160`

- 🔗 [AddVirtualServer](#addvirtualserver-pkgproxyipvsutiltestingfakego96) `:96`

- 🔗 [ConfigureTimeouts](#configuretimeouts-pkgproxyipvsutiltestingfakego227) `:227`

- 🔗 [DeleteRealServer](#deleterealserver-pkgproxyipvsutiltestingfakego192) `:192`

- 🔗 [DeleteVirtualServer](#deletevirtualserver-pkgproxyipvsutiltestingfakego118) `:118`

- 🔗 [Flush](#flush-pkgproxyipvsutiltestingfakego152) `:152`

- 🔗 [GetRealServers](#getrealservers-pkgproxyipvsutiltestingfakego180) `:180`

- 🔗 [GetVirtualServer](#getvirtualserver-pkgproxyipvsutiltestingfakego130) `:130`

- 🔗 [GetVirtualServers](#getvirtualservers-pkgproxyipvsutiltestingfakego143) `:143`

- 🔗 [Len](#len-pkgproxyipvsutiltestingfakego62) `:62`

- 🔗 [Less](#less-pkgproxyipvsutiltestingfakego65) `:65`

- 🔗 [NewFake](#newfake-pkgproxyipvsutiltestingfakego73) `:73`

- 🔗 [String](#string-pkgproxyipvsutiltestingfakego45) `:45`

- 🔗 [String](#string-pkgproxyipvsutiltestingfakego55) `:55`

- 🔗 [Swap](#swap-pkgproxyipvsutiltestingfakego68) `:68`

- 🔗 [UpdateRealServer](#updaterealserver-pkgproxyipvsutiltestingfakego218) `:218`

- 🔗 [UpdateVirtualServer](#updatevirtualserver-pkgproxyipvsutiltestingfakego108) `:108`

- 🔗 [toRealServerKey](#torealserverkey-pkgproxyipvsutiltestingfakego88) `:88`

- 🔗 [toServiceKey](#toservicekey-pkgproxyipvsutiltestingfakego80) `:80`


</details>


[function] name: AddRealServer file: pkg/proxy/ipvs/util/testing/fake.go:160 returns_error: нет description: AddRealServer is a fake implementation, it simply creates a RealServer for a VirtualServer in the cache store.


### AddRealServer (pkg/proxy/ipvs/util/testing/fake.go:160)


AddRealServer is a fake implementation, it simply creates a RealServer for a VirtualServer in the cache store.


```go
func (f *FakeIPVS) AddRealServer((serv *utilipvs.VirtualServer, dest *utilipvs.RealServer)) (serv *utilipvs.VirtualServer, dest *utilipvs.RealServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип запроса:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** serv


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:160`



---


[function] name: AddVirtualServer file: pkg/proxy/ipvs/util/testing/fake.go:96 returns_error: нет description: AddVirtualServer is a fake implementation, it simply adds the VirtualServer into the cache store.


### AddVirtualServer (pkg/proxy/ipvs/util/testing/fake.go:96)


AddVirtualServer is a fake implementation, it simply adds the VirtualServer into the cache store.


```go
func (f *FakeIPVS) AddVirtualServer((serv *utilipvs.VirtualServer)) (serv *utilipvs.VirtualServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** serv


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:96`



---


[function] name: ConfigureTimeouts file: pkg/proxy/ipvs/util/testing/fake.go:227 returns_error: нет description: ConfigureTimeouts is not supported for fake IPVS


### ConfigureTimeouts (pkg/proxy/ipvs/util/testing/fake.go:227)


ConfigureTimeouts is not supported for fake IPVS


```go
func (f *FakeIPVS) ConfigureTimeouts((time.Duration, time.Duration, time.Duration)) (time.Duration, time.Duration, time.Duration)
```


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


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:227`



---


[function] name: DeleteRealServer file: pkg/proxy/ipvs/util/testing/fake.go:192 returns_error: нет description: DeleteRealServer is a fake implementation, it deletes the real server in the cache store.


### DeleteRealServer (pkg/proxy/ipvs/util/testing/fake.go:192)


DeleteRealServer is a fake implementation, it deletes the real server in the cache store.


```go
func (f *FakeIPVS) DeleteRealServer((serv *utilipvs.VirtualServer, dest *utilipvs.RealServer)) (serv *utilipvs.VirtualServer, dest *utilipvs.RealServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип запроса:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** serv


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:192`



---


[function] name: DeleteVirtualServer file: pkg/proxy/ipvs/util/testing/fake.go:118 returns_error: нет description: DeleteVirtualServer is a fake implementation, it simply deletes the VirtualServer from the cache store.


### DeleteVirtualServer (pkg/proxy/ipvs/util/testing/fake.go:118)


DeleteVirtualServer is a fake implementation, it simply deletes the VirtualServer from the cache store.


```go
func (f *FakeIPVS) DeleteVirtualServer((serv *utilipvs.VirtualServer)) (serv *utilipvs.VirtualServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** serv


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:118`



---


[function] name: Flush file: pkg/proxy/ipvs/util/testing/fake.go:152 returns_error: нет description: Flush is a fake implementation, it simply clears the cache store.


### Flush (pkg/proxy/ipvs/util/testing/fake.go:152)


Flush is a fake implementation, it simply clears the cache store.


```go
func (f *FakeIPVS) Flush(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:152`



---


[function] name: GetRealServers file: pkg/proxy/ipvs/util/testing/fake.go:180 returns_error: да description: GetRealServers is a fake implementation, it simply returns all RealServers in the cache store.


### GetRealServers (pkg/proxy/ipvs/util/testing/fake.go:180)


GetRealServers is a fake implementation, it simply returns all RealServers in the cache store.


```go
func (f *FakeIPVS) GetRealServers(([]*utilipvs.RealServer, error)) ([]*utilipvs.RealServer, error)
```


**Тип запроса:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*utilipvs.RealServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:180`



---


[function] name: GetVirtualServer file: pkg/proxy/ipvs/util/testing/fake.go:130 returns_error: да description: GetVirtualServer is a fake implementation, it tries to find a specific VirtualServer from the cache store.


### GetVirtualServer (pkg/proxy/ipvs/util/testing/fake.go:130)


GetVirtualServer is a fake implementation, it tries to find a specific VirtualServer from the cache store.


```go
func (f *FakeIPVS) GetVirtualServer((*utilipvs.VirtualServer, error)) (*utilipvs.VirtualServer, error)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*utilipvs.VirtualServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:130`



---


[function] name: GetVirtualServers file: pkg/proxy/ipvs/util/testing/fake.go:143 returns_error: да description: GetVirtualServers is a fake implementation, it simply returns all VirtualServers in the cache store.


### GetVirtualServers (pkg/proxy/ipvs/util/testing/fake.go:143)


GetVirtualServers is a fake implementation, it simply returns all VirtualServers in the cache store.


```go
func (f *FakeIPVS) GetVirtualServers(([]*utilipvs.VirtualServer, error)) ([]*utilipvs.VirtualServer, error)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*utilipvs.VirtualServer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:143`



---


[function] name: Len file: pkg/proxy/ipvs/util/testing/fake.go:62 returns_error: нет description: —


### Len (pkg/proxy/ipvs/util/testing/fake.go:62)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (a byAddress) Len(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:62`



---


[function] name: Less file: pkg/proxy/ipvs/util/testing/fake.go:65 returns_error: нет description: —


### Less (pkg/proxy/ipvs/util/testing/fake.go:65)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (a byAddress) Less((i, j int)) (i, j int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:65`



---


[function] name: NewFake file: pkg/proxy/ipvs/util/testing/fake.go:73 returns_error: нет description: NewFake creates a fake ipvs implementation - a cache store.


### NewFake (pkg/proxy/ipvs/util/testing/fake.go:73)


NewFake creates a fake ipvs implementation - a cache store.


```go
func NewFake(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:73`



---


[function] name: String file: pkg/proxy/ipvs/util/testing/fake.go:45 returns_error: нет description: —


### String (pkg/proxy/ipvs/util/testing/fake.go:45)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (s *ServiceKey) String(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:45`



---


[function] name: String file: pkg/proxy/ipvs/util/testing/fake.go:55 returns_error: нет description: —


### String (pkg/proxy/ipvs/util/testing/fake.go:55)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (r *RealServerKey) String(()) ()
```


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:55`



---


[function] name: Swap file: pkg/proxy/ipvs/util/testing/fake.go:68 returns_error: нет description: —


### Swap (pkg/proxy/ipvs/util/testing/fake.go:68)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (a byAddress) Swap((i, j int)) (i, j int)
```


**Тип ответа:** i


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** j


```json
{
  "cfgPath": "string",
  "token": "string",
  "controlPlane": false,
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "patchesDir": "string",
  "dryRun": false,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/join.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:68`



---


[function] name: UpdateRealServer file: pkg/proxy/ipvs/util/testing/fake.go:218 returns_error: нет description: UpdateRealServer is a fake implementation, it deletes the old real server then add new real server


### UpdateRealServer (pkg/proxy/ipvs/util/testing/fake.go:218)


UpdateRealServer is a fake implementation, it deletes the old real server then add new real server


```go
func (f *FakeIPVS) UpdateRealServer((serv *utilipvs.VirtualServer, dest *utilipvs.RealServer)) (serv *utilipvs.VirtualServer, dest *utilipvs.RealServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип запроса:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** serv


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:218`



---


[function] name: UpdateVirtualServer file: pkg/proxy/ipvs/util/testing/fake.go:108 returns_error: нет description: UpdateVirtualServer is a fake implementation, it updates the VirtualServer in the cache store.


### UpdateVirtualServer (pkg/proxy/ipvs/util/testing/fake.go:108)


UpdateVirtualServer is a fake implementation, it updates the VirtualServer in the cache store.


```go
func (f *FakeIPVS) UpdateVirtualServer((serv *utilipvs.VirtualServer)) (serv *utilipvs.VirtualServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** serv


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:108`



---


[function] name: toRealServerKey file: pkg/proxy/ipvs/util/testing/fake.go:88 returns_error: нет description: —


### toRealServerKey (pkg/proxy/ipvs/util/testing/fake.go:88)


toRealServerKey is a function that performs operations based on the provided parameters and returns (rs *utilipvs.RealServer).


```go
func toRealServerKey((rs *utilipvs.RealServer)) (rs *utilipvs.RealServer)
```


**Тип запроса:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** rs


```json
{
  "OldVersion": {},
  "CurrentVersion": {},
  "Document": []
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/utils.go`


**Тип ответа:** utilipvs.RealServer


```json
{
  "Address": {},
  "Port": 0,
  "Weight": 0,
  "ActiveConn": 0,
  "InactiveConn": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:88`



---


[function] name: toServiceKey file: pkg/proxy/ipvs/util/testing/fake.go:80 returns_error: нет description: —


### toServiceKey (pkg/proxy/ipvs/util/testing/fake.go:80)


toServiceKey is a function that performs operations based on the provided parameters and returns (serv *utilipvs.VirtualServer).


```go
func toServiceKey((serv *utilipvs.VirtualServer)) (serv *utilipvs.VirtualServer)
```


**Тип запроса:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


**Тип ответа:** serv


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/service.go`


**Тип ответа:** utilipvs.VirtualServer


```json
{
  "Address": {},
  "Protocol": "string",
  "Port": 0,
  "Scheduler": "string",
  "Flags": {},
  "Timeout": 0
}
```


*Определено в:* `pkg/proxy/ipvs/util/ipvs.go`


📍 *Расположение:* `pkg/proxy/ipvs/util/testing/fake.go:80`




## pkg/proxy/kubemark/hollow_proxy.go


📄 Исходный файл: `pkg/proxy/kubemark/hollow_proxy.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [NewHollowProxy](#newhollowproxy-pkgproxykubemarkhollow_proxygo56) `:56`

- 🔗 [OnEndpointSliceAdd](#onendpointsliceadd-pkgproxykubemarkhollow_proxygo49) `:49`

- 🔗 [OnEndpointSliceDelete](#onendpointslicedelete-pkgproxykubemarkhollow_proxygo51) `:51`

- 🔗 [OnEndpointSliceUpdate](#onendpointsliceupdate-pkgproxykubemarkhollow_proxygo50) `:50`

- 🔗 [OnEndpointSlicesSynced](#onendpointslicessynced-pkgproxykubemarkhollow_proxygo52) `:52`

- 🔗 [OnServiceAdd](#onserviceadd-pkgproxykubemarkhollow_proxygo45) `:45`

- 🔗 [OnServiceCIDRsChanged](#onservicecidrschanged-pkgproxykubemarkhollow_proxygo53) `:53`

- 🔗 [OnServiceDelete](#onservicedelete-pkgproxykubemarkhollow_proxygo47) `:47`

- 🔗 [OnServiceSynced](#onservicesynced-pkgproxykubemarkhollow_proxygo48) `:48`

- 🔗 [OnServiceUpdate](#onserviceupdate-pkgproxykubemarkhollow_proxygo46) `:46`

- 🔗 [OnTopologyChange](#ontopologychange-pkgproxykubemarkhollow_proxygo54) `:54`

- 🔗 [Run](#run-pkgproxykubemarkhollow_proxygo87) `:87`

- 🔗 [Sync](#sync-pkgproxykubemarkhollow_proxygo41) `:41`

- 🔗 [SyncLoop](#syncloop-pkgproxykubemarkhollow_proxygo42) `:42`


</details>


[function] name: NewHollowProxy file: pkg/proxy/kubemark/hollow_proxy.go:56 returns_error: нет description: —


### NewHollowProxy (pkg/proxy/kubemark/hollow_proxy.go:56)


NewHollowProxy is a function that performs operations based on the provided parameters and returns (
	nodeName string,
	client clientset.Interface,
	eventClient v1core.EventsGetter,
	broadcaster events.EventBroadcaster,
	recorder events.EventRecorder,
).


```go
func NewHollowProxy((
	nodeName string,
	client clientset.Interface,
	eventClient v1core.EventsGetter,
	broadcaster events.EventBroadcaster,
	recorder events.EventRecorder,
)) (
	nodeName string,
	client clientset.Interface,
	eventClient v1core.EventsGetter,
	broadcaster events.EventBroadcaster,
	recorder events.EventRecorder,
)
```


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** eventClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1core.EventsGetter


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** broadcaster


```json
{
  "result": {},
  "stopped": {},
  "stop": {},
  "id": 0,
  "m": null
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/watch/mux.go`


**Тип ответа:** events.EventBroadcaster


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** recorder


```json
{
  "mu": {},
  "warnings": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/token/cache/cached_token_authenticator.go`


**Тип ответа:** events.EventRecorder


```json
{
  "recorder": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:56`



---


[function] name: OnEndpointSliceAdd file: pkg/proxy/kubemark/hollow_proxy.go:49 returns_error: нет description: —


### OnEndpointSliceAdd (pkg/proxy/kubemark/hollow_proxy.go:49)


OnEndpointSliceAdd is a method that performs operations based on the provided parameters and returns (slice *discoveryv1.EndpointSlice).


```go
func (*FakeProxier) OnEndpointSliceAdd((slice *discoveryv1.EndpointSlice)) (slice *discoveryv1.EndpointSlice)
```


**Тип запроса:** discoveryv1.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** slice


```json
{
  "elements": [],
  "idx": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/common/valuesreflect.go`


**Тип ответа:** discoveryv1.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:49`



---


[function] name: OnEndpointSliceDelete file: pkg/proxy/kubemark/hollow_proxy.go:51 returns_error: нет description: —


### OnEndpointSliceDelete (pkg/proxy/kubemark/hollow_proxy.go:51)


OnEndpointSliceDelete is a method that performs operations based on the provided parameters and returns (slice *discoveryv1.EndpointSlice).


```go
func (*FakeProxier) OnEndpointSliceDelete((slice *discoveryv1.EndpointSlice)) (slice *discoveryv1.EndpointSlice)
```


**Тип запроса:** discoveryv1.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** slice


```json
{
  "elements": [],
  "idx": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/common/valuesreflect.go`


**Тип ответа:** discoveryv1.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:51`



---


[function] name: OnEndpointSliceUpdate file: pkg/proxy/kubemark/hollow_proxy.go:50 returns_error: нет description: —


### OnEndpointSliceUpdate (pkg/proxy/kubemark/hollow_proxy.go:50)


OnEndpointSliceUpdate is a method that performs operations based on the provided parameters and returns (oldSlice, slice *discoveryv1.EndpointSlice).


```go
func (*FakeProxier) OnEndpointSliceUpdate((oldSlice, slice *discoveryv1.EndpointSlice)) (oldSlice, slice *discoveryv1.EndpointSlice)
```


**Тип запроса:** discoveryv1.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** oldSlice


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** slice


```json
{
  "elements": [],
  "idx": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/cel/common/valuesreflect.go`


**Тип ответа:** discoveryv1.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:50`



---


[function] name: OnEndpointSlicesSynced file: pkg/proxy/kubemark/hollow_proxy.go:52 returns_error: нет description: —


### OnEndpointSlicesSynced (pkg/proxy/kubemark/hollow_proxy.go:52)


OnEndpointSlicesSynced is a method that performs operations based on the provided parameters and returns ().


```go
func (*FakeProxier) OnEndpointSlicesSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:52`



---


[function] name: OnServiceAdd file: pkg/proxy/kubemark/hollow_proxy.go:45 returns_error: нет description: —


### OnServiceAdd (pkg/proxy/kubemark/hollow_proxy.go:45)


OnServiceAdd is a method that performs operations based on the provided parameters and returns (service *v1.Service).


```go
func (*FakeProxier) OnServiceAdd((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:45`



---


[function] name: OnServiceCIDRsChanged file: pkg/proxy/kubemark/hollow_proxy.go:53 returns_error: нет description: —


### OnServiceCIDRsChanged (pkg/proxy/kubemark/hollow_proxy.go:53)


OnServiceCIDRsChanged is a method that performs operations based on the provided parameters and returns (_ []string).


```go
func (*FakeProxier) OnServiceCIDRsChanged((_ []string)) (_ []string)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:53`



---


[function] name: OnServiceDelete file: pkg/proxy/kubemark/hollow_proxy.go:47 returns_error: нет description: —


### OnServiceDelete (pkg/proxy/kubemark/hollow_proxy.go:47)


OnServiceDelete is a method that performs operations based on the provided parameters and returns (service *v1.Service).


```go
func (*FakeProxier) OnServiceDelete((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:47`



---


[function] name: OnServiceSynced file: pkg/proxy/kubemark/hollow_proxy.go:48 returns_error: нет description: —


### OnServiceSynced (pkg/proxy/kubemark/hollow_proxy.go:48)


OnServiceSynced is a method that performs operations based on the provided parameters and returns ().


```go
func (*FakeProxier) OnServiceSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:48`



---


[function] name: OnServiceUpdate file: pkg/proxy/kubemark/hollow_proxy.go:46 returns_error: нет description: —


### OnServiceUpdate (pkg/proxy/kubemark/hollow_proxy.go:46)


OnServiceUpdate is a method that performs operations based on the provided parameters and returns (oldService, service *v1.Service).


```go
func (*FakeProxier) OnServiceUpdate((oldService, service *v1.Service)) (oldService, service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:46`



---


[function] name: OnTopologyChange file: pkg/proxy/kubemark/hollow_proxy.go:54 returns_error: нет description: —


### OnTopologyChange (pkg/proxy/kubemark/hollow_proxy.go:54)


OnTopologyChange is a method that performs operations based on the provided parameters and returns (_ map[string]string).


```go
func (*FakeProxier) OnTopologyChange((_ map[string]string)) (_ map[string]string)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:54`



---


[function] name: Run file: pkg/proxy/kubemark/hollow_proxy.go:87 returns_error: нет description: —


### Run (pkg/proxy/kubemark/hollow_proxy.go:87)


Run is a method that performs operations based on the provided parameters and returns ().


```go
func (hp *HollowProxy) Run(()) ()
```


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:87`



---


[function] name: Sync file: pkg/proxy/kubemark/hollow_proxy.go:41 returns_error: нет description: —


### Sync (pkg/proxy/kubemark/hollow_proxy.go:41)


Sync is a method that performs operations based on the provided parameters and returns ().


```go
func (*FakeProxier) Sync(()) ()
```


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:41`



---


[function] name: SyncLoop file: pkg/proxy/kubemark/hollow_proxy.go:42 returns_error: нет description: —


### SyncLoop (pkg/proxy/kubemark/hollow_proxy.go:42)


SyncLoop is a method that performs operations based on the provided parameters and returns ().


```go
func (*FakeProxier) SyncLoop(()) ()
```


📍 *Расположение:* `pkg/proxy/kubemark/hollow_proxy.go:42`




## pkg/proxy/metaproxier/meta_proxier.go


📄 Исходный файл: `pkg/proxy/metaproxier/meta_proxier.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [NewMetaProxier](#newmetaproxier-pkgproxymetaproxiermeta_proxiergo36) `:36`

- 🔗 [OnEndpointSliceAdd](#onendpointsliceadd-pkgproxymetaproxiermeta_proxiergo87) `:87`

- 🔗 [OnEndpointSliceDelete](#onendpointslicedelete-pkgproxymetaproxiermeta_proxiergo113) `:113`

- 🔗 [OnEndpointSliceUpdate](#onendpointsliceupdate-pkgproxymetaproxiermeta_proxiergo100) `:100`

- 🔗 [OnEndpointSlicesSynced](#onendpointslicessynced-pkgproxymetaproxiermeta_proxiergo126) `:126`

- 🔗 [OnServiceAdd](#onserviceadd-pkgproxymetaproxiermeta_proxiergo58) `:58`

- 🔗 [OnServiceCIDRsChanged](#onservicecidrschanged-pkgproxymetaproxiermeta_proxiergo139) `:139`

- 🔗 [OnServiceDelete](#onservicedelete-pkgproxymetaproxiermeta_proxiergo72) `:72`

- 🔗 [OnServiceSynced](#onservicesynced-pkgproxymetaproxiermeta_proxiergo80) `:80`

- 🔗 [OnServiceUpdate](#onserviceupdate-pkgproxymetaproxiermeta_proxiergo65) `:65`

- 🔗 [OnTopologyChange](#ontopologychange-pkgproxymetaproxiermeta_proxiergo132) `:132`

- 🔗 [Sync](#sync-pkgproxymetaproxiermeta_proxiergo45) `:45`

- 🔗 [SyncLoop](#syncloop-pkgproxymetaproxiermeta_proxiergo52) `:52`


</details>


[function] name: NewMetaProxier file: pkg/proxy/metaproxier/meta_proxier.go:36 returns_error: нет description: NewMetaProxier returns a dual-stack "meta-proxier". Proxier API
calls will be dispatched to the ProxyProvider instances 


### NewMetaProxier (pkg/proxy/metaproxier/meta_proxier.go:36)


NewMetaProxier returns a dual-stack "meta-proxier". Proxier API
calls will be dispatched to the ProxyProvider instances depending
on address family.


```go
func NewMetaProxier((ipv4Proxier, ipv6Proxier proxy.Provider)) (ipv4Proxier, ipv6Proxier proxy.Provider)
```


**Тип ответа:** ipv4Proxier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ipv6Proxier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.Provider


```json
{
  "cadvisor": {},
  "podManager": {}
}
```


*Определено в:* `pkg/kubelet/stats/provider.go`


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:36`



---


[function] name: OnEndpointSliceAdd file: pkg/proxy/metaproxier/meta_proxier.go:87 returns_error: нет description: OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


### OnEndpointSliceAdd (pkg/proxy/metaproxier/meta_proxier.go:87)


OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


```go
func (proxier *metaProxier) OnEndpointSliceAdd((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:87`



---


[function] name: OnEndpointSliceDelete file: pkg/proxy/metaproxier/meta_proxier.go:113 returns_error: нет description: OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


### OnEndpointSliceDelete (pkg/proxy/metaproxier/meta_proxier.go:113)


OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


```go
func (proxier *metaProxier) OnEndpointSliceDelete((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:113`



---


[function] name: OnEndpointSliceUpdate file: pkg/proxy/metaproxier/meta_proxier.go:100 returns_error: нет description: OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


### OnEndpointSliceUpdate (pkg/proxy/metaproxier/meta_proxier.go:100)


OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


```go
func (proxier *metaProxier) OnEndpointSliceUpdate((oldEndpointSlice, newEndpointSlice *discovery.EndpointSlice)) (oldEndpointSlice, newEndpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** oldEndpointSlice


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newEndpointSlice


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:100`



---


[function] name: OnEndpointSlicesSynced file: pkg/proxy/metaproxier/meta_proxier.go:126 returns_error: нет description: OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to lo


### OnEndpointSlicesSynced (pkg/proxy/metaproxier/meta_proxier.go:126)


OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *metaProxier) OnEndpointSlicesSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:126`



---


[function] name: OnServiceAdd file: pkg/proxy/metaproxier/meta_proxier.go:58 returns_error: нет description: OnServiceAdd is called whenever creation of new service object is observed.


### OnServiceAdd (pkg/proxy/metaproxier/meta_proxier.go:58)


OnServiceAdd is called whenever creation of new service object is observed.


```go
func (proxier *metaProxier) OnServiceAdd((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:58`



---


[function] name: OnServiceCIDRsChanged file: pkg/proxy/metaproxier/meta_proxier.go:139 returns_error: нет description: OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of 


### OnServiceCIDRsChanged (pkg/proxy/metaproxier/meta_proxier.go:139)


OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of service cidrs.


```go
func (proxier *metaProxier) OnServiceCIDRsChanged((cidrs []string)) (cidrs []string)
```


**Тип ответа:** cidrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:139`



---


[function] name: OnServiceDelete file: pkg/proxy/metaproxier/meta_proxier.go:72 returns_error: нет description: OnServiceDelete is called whenever deletion of an existing service
object is observed.


### OnServiceDelete (pkg/proxy/metaproxier/meta_proxier.go:72)


OnServiceDelete is called whenever deletion of an existing service
object is observed.


```go
func (proxier *metaProxier) OnServiceDelete((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:72`



---


[function] name: OnServiceSynced file: pkg/proxy/metaproxier/meta_proxier.go:80 returns_error: нет description: OnServiceSynced is called once all the initial event handlers were
called and the state is fully propagated to local cac


### OnServiceSynced (pkg/proxy/metaproxier/meta_proxier.go:80)


OnServiceSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *metaProxier) OnServiceSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:80`



---


[function] name: OnServiceUpdate file: pkg/proxy/metaproxier/meta_proxier.go:65 returns_error: нет description: OnServiceUpdate is called whenever modification of an existing
service object is observed.


### OnServiceUpdate (pkg/proxy/metaproxier/meta_proxier.go:65)


OnServiceUpdate is called whenever modification of an existing
service object is observed.


```go
func (proxier *metaProxier) OnServiceUpdate((oldService, service *v1.Service)) (oldService, service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:65`



---


[function] name: OnTopologyChange file: pkg/proxy/metaproxier/meta_proxier.go:132 returns_error: нет description: OnTopologyChange is called whenever change in proxy relevant topology labels is observed.


### OnTopologyChange (pkg/proxy/metaproxier/meta_proxier.go:132)


OnTopologyChange is called whenever change in proxy relevant topology labels is observed.


```go
func (proxier *metaProxier) OnTopologyChange((topologyLabels map[string]string)) (topologyLabels map[string]string)
```


**Тип ответа:** topologyLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:132`



---


[function] name: Sync file: pkg/proxy/metaproxier/meta_proxier.go:45 returns_error: нет description: Sync immediately synchronizes the ProxyProvider's current state to
proxy rules.


### Sync (pkg/proxy/metaproxier/meta_proxier.go:45)


Sync immediately synchronizes the ProxyProvider's current state to
proxy rules.


```go
func (proxier *metaProxier) Sync(()) ()
```


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:45`



---


[function] name: SyncLoop file: pkg/proxy/metaproxier/meta_proxier.go:52 returns_error: нет description: SyncLoop runs periodic work.  This is expected to run as a
goroutine or as the main loop of the app.  It does not return


### SyncLoop (pkg/proxy/metaproxier/meta_proxier.go:52)


SyncLoop runs periodic work.  This is expected to run as a
goroutine or as the main loop of the app.  It does not return.


```go
func (proxier *metaProxier) SyncLoop(()) ()
```


📍 *Расположение:* `pkg/proxy/metaproxier/meta_proxier.go:52`




## pkg/proxy/metrics/metrics.go


📄 Исходный файл: `pkg/proxy/metrics/metrics.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [CollectWithStability](#collectwithstability-pkgproxymetricsmetricsgo402) `:402`

- 🔗 [DescribeWithStability](#describewithstability-pkgproxymetricsmetricsgo397) `:397`

- 🔗 [RegisterMetrics](#registermetrics-pkgproxymetricsmetricsgo314) `:314`

- 🔗 [SinceInSeconds](#sinceinseconds-pkgproxymetricsmetricsgo370) `:370`

- 🔗 [newNFAcctMetricCollector](#newnfacctmetriccollector-pkgproxymetricsmetricsgo376) `:376`


</details>


[function] name: CollectWithStability file: pkg/proxy/metrics/metrics.go:402 returns_error: нет description: CollectWithStability implements the metrics.StableCollector interface.


### CollectWithStability (pkg/proxy/metrics/metrics.go:402)


CollectWithStability implements the metrics.StableCollector interface.


```go
func (n *nfacctMetricCollector) CollectWithStability((ch chan<- metrics.Metric)) (ch chan<- metrics.Metric)
```


**Тип ответа:** ch


```json
{
  "Directory": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** metrics.Metric


```json
{
  "Name": "string",
  "Subsystem": "string",
  "Namespace": "string",
  "Help": "string",
  "Type": "string",
  "DeprecatedVersion": "string",
  "StabilityLevel": "string",
  "Labels": [],
  "Buckets": [],
  "Objectives": {},
  "AgeBuckets": 0,
  "BufCap": 0,
  "MaxAge": 0,
  "ConstLabels": {},
  "ComponentEndpoints": []
}
```


*Определено в:* `test/instrumentation/internal/metric/metric.go`


📍 *Расположение:* `pkg/proxy/metrics/metrics.go:402`



---


[function] name: DescribeWithStability file: pkg/proxy/metrics/metrics.go:397 returns_error: нет description: DescribeWithStability implements the metrics.StableCollector interface.


### DescribeWithStability (pkg/proxy/metrics/metrics.go:397)


DescribeWithStability implements the metrics.StableCollector interface.


```go
func (n *nfacctMetricCollector) DescribeWithStability((ch chan<- *metrics.Desc)) (ch chan<- *metrics.Desc)
```


**Тип запроса:** metrics.Desc


```json
{
  "fqName": "string",
  "help": "string",
  "constLabels": {},
  "variableLabels": [],
  "promDesc": null,
  "annotatedHelp": "string",
  "stabilityLevel": {},
  "deprecatedVersion": "string",
  "isDeprecated": false,
  "isHidden": false,
  "isCreated": false,
  "createLock": {},
  "markDeprecationOnce": {},
  "createOnce": {},
  "deprecateOnce": {},
  "hideOnce": {},
  "annotateOnce": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/desc.go`


**Тип ответа:** ch


```json
{
  "Directory": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta3/types.go`


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** metrics.Desc


```json
{
  "fqName": "string",
  "help": "string",
  "constLabels": {},
  "variableLabels": [],
  "promDesc": null,
  "annotatedHelp": "string",
  "stabilityLevel": {},
  "deprecatedVersion": "string",
  "isDeprecated": false,
  "isHidden": false,
  "isCreated": false,
  "createLock": {},
  "markDeprecationOnce": {},
  "createOnce": {},
  "deprecateOnce": {},
  "hideOnce": {},
  "annotateOnce": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/desc.go`


📍 *Расположение:* `pkg/proxy/metrics/metrics.go:397`



---


[function] name: RegisterMetrics file: pkg/proxy/metrics/metrics.go:314 returns_error: нет description: RegisterMetrics registers kube-proxy metrics.


### RegisterMetrics (pkg/proxy/metrics/metrics.go:314)


RegisterMetrics registers kube-proxy metrics.


```go
func RegisterMetrics((mode kubeproxyconfig.ProxyMode)) (mode kubeproxyconfig.ProxyMode)
```


**Тип ответа:** mode


```json
{
  "cache": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/cache.go`


**Тип ответа:** kubeproxyconfig.ProxyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/metrics/metrics.go:314`



---


[function] name: SinceInSeconds file: pkg/proxy/metrics/metrics.go:370 returns_error: нет description: SinceInSeconds gets the time since the specified start in seconds.


### SinceInSeconds (pkg/proxy/metrics/metrics.go:370)


SinceInSeconds gets the time since the specified start in seconds.


```go
func SinceInSeconds((start time.Time)) (start time.Time)
```


**Тип ответа:** start


```json
{
  "Action": null,
  "ExitCodes": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/containerrestartrule.go`


**Тип ответа:** time.Time


```json
{
  "ControlPlaneComponentHealthCheck": null,
  "KubeletHealthCheck": null,
  "KubernetesAPICall": null,
  "EtcdAPICall": null,
  "TLSBootstrap": null,
  "Discovery": null,
  "UpgradeManifests": null
}
```


*Определено в:* `cmd/kubeadm/app/apis/kubeadm/v1beta4/types.go`


📍 *Расположение:* `pkg/proxy/metrics/metrics.go:370`



---


[function] name: newNFAcctMetricCollector file: pkg/proxy/metrics/metrics.go:376 returns_error: нет description: —


### newNFAcctMetricCollector (pkg/proxy/metrics/metrics.go:376)


newNFAcctMetricCollector is a function that performs operations based on the provided parameters and returns (counter string, description *metrics.Desc).


```go
func newNFAcctMetricCollector((counter string, description *metrics.Desc)) (counter string, description *metrics.Desc)
```


**Тип запроса:** metrics.Desc


```json
{
  "fqName": "string",
  "help": "string",
  "constLabels": {},
  "variableLabels": [],
  "promDesc": null,
  "annotatedHelp": "string",
  "stabilityLevel": {},
  "deprecatedVersion": "string",
  "isDeprecated": false,
  "isHidden": false,
  "isCreated": false,
  "createLock": {},
  "markDeprecationOnce": {},
  "createOnce": {},
  "deprecateOnce": {},
  "hideOnce": {},
  "annotateOnce": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/desc.go`


**Тип ответа:** counter


```json
{
  "counter": null,
  "id": "string",
  "reason": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/x509metrics/server_cert_deprecations.go`


**Тип ответа:** description


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metrics.Desc


```json
{
  "fqName": "string",
  "help": "string",
  "constLabels": {},
  "variableLabels": [],
  "promDesc": null,
  "annotatedHelp": "string",
  "stabilityLevel": {},
  "deprecatedVersion": "string",
  "isDeprecated": false,
  "isHidden": false,
  "isCreated": false,
  "createLock": {},
  "markDeprecationOnce": {},
  "createOnce": {},
  "deprecateOnce": {},
  "hideOnce": {},
  "annotateOnce": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/desc.go`


📍 *Расположение:* `pkg/proxy/metrics/metrics.go:376`




## pkg/proxy/nftables/cleanup.go


📄 Исходный файл: `pkg/proxy/nftables/cleanup.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [CleanupLeftovers](#cleanupleftovers-pkgproxynftablescleanupgo30) `:30`


</details>


[function] name: CleanupLeftovers file: pkg/proxy/nftables/cleanup.go:30 returns_error: нет description: CleanupLeftovers removes all nftables rules and chains created by the Proxier
It returns true if an error was encountere


### CleanupLeftovers (pkg/proxy/nftables/cleanup.go:30)


CleanupLeftovers removes all nftables rules and chains created by the Proxier
It returns true if an error was encountered. Errors are logged.


```go
func CleanupLeftovers((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `pkg/proxy/nftables/cleanup.go:30`




## pkg/proxy/nftables/proxier.go


📄 Исходный файл: `pkg/proxy/nftables/proxier.go`


<details open>
<summary><b>Функции в этом файле (36)</b></summary>


- 🔗 [NewDualStackProxier](#newdualstackproxier-pkgproxynftablesproxiergo100) `:100`

- 🔗 [NewProxier](#newproxier-pkgproxynftablesproxiergo206) `:206`

- 🔗 [OnEndpointSliceAdd](#onendpointsliceadd-pkgproxynftablesproxiergo721) `:721`

- 🔗 [OnEndpointSliceDelete](#onendpointslicedelete-pkgproxynftablesproxiergo737) `:737`

- 🔗 [OnEndpointSliceUpdate](#onendpointsliceupdate-pkgproxynftablesproxiergo729) `:729`

- 🔗 [OnEndpointSlicesSynced](#onendpointslicessynced-pkgproxynftablesproxiergo745) `:745`

- 🔗 [OnServiceAdd](#onserviceadd-pkgproxynftablesproxiergo689) `:689`

- 🔗 [OnServiceCIDRsChanged](#onservicecidrschanged-pkgproxynftablesproxiergo767) `:767`

- 🔗 [OnServiceDelete](#onservicedelete-pkgproxynftablesproxiergo703) `:703`

- 🔗 [OnServiceSynced](#onservicesynced-pkgproxynftablesproxiergo709) `:709`

- 🔗 [OnServiceUpdate](#onserviceupdate-pkgproxynftablesproxiergo695) `:695`

- 🔗 [OnTopologyChange](#ontopologychange-pkgproxynftablesproxiergo756) `:756`

- 🔗 [Sync](#sync-pkgproxynftablesproxiergo655) `:655`

- 🔗 [SyncLoop](#syncloop-pkgproxynftablesproxiergo664) `:664`

- 🔗 [cleanupLeftoverKeys](#cleanupleftoverkeys-pkgproxynftablesproxiergo984) `:984`

- 🔗 [ensureChain](#ensurechain-pkgproxynftablesproxiergo392) `:392`

- 🔗 [ensureElem](#ensureelem-pkgproxynftablesproxiergo966) `:966`

- 🔗 [epChainSkipUpdate](#epchainskipupdate-pkgproxynftablesproxiergo1750) `:1750`

- 🔗 [hashAndTruncate](#hashandtruncate-pkgproxynftablesproxiergo809) `:809`

- 🔗 [isAffinitySetName](#isaffinitysetname-pkgproxynftablesproxiergo895) `:895`

- 🔗 [isInitialized](#isinitialized-pkgproxynftablesproxiergo683) `:683`

- 🔗 [isServiceChainName](#isservicechainname-pkgproxynftablesproxiergo887) `:887`

- 🔗 [joinNFTSlice](#joinnftslice-pkgproxynftablesproxiergo909) `:909`

- 🔗 [logFailure](#logfailure-pkgproxynftablesproxiergo1001) `:1001`

- 🔗 [newEndpointInfo](#newendpointinfo-pkgproxynftablesproxiergo317) `:317`

- 🔗 [newNFTElementStorage](#newnftelementstorage-pkgproxynftablesproxiergo920) `:920`

- 🔗 [newServiceInfo](#newserviceinfo-pkgproxynftablesproxiergo291) `:291`

- 🔗 [readOrReset](#readorreset-pkgproxynftablesproxiergo932) `:932`

- 🔗 [resetLeftoverKeys](#resetleftoverkeys-pkgproxynftablesproxiergo957) `:957`

- 🔗 [servicePortChainNameBase](#serviceportchainnamebase-pkgproxynftablesproxiergo822) `:822`

- 🔗 [servicePortEndpointChainNameBase](#serviceportendpointchainnamebase-pkgproxynftablesproxiergo855) `:855`

- 🔗 [setInitialized](#setinitialized-pkgproxynftablesproxiergo675) `:675`

- 🔗 [setupNFTables](#setupnftables-pkgproxynftablesproxiergo408) `:408`

- 🔗 [splitNFTSlice](#splitnftslice-pkgproxynftablesproxiergo914) `:914`

- 🔗 [syncProxyRules](#syncproxyrules-pkgproxynftablesproxiergo1017) `:1017`

- 🔗 [writeServiceToEndpointRules](#writeservicetoendpointrules-pkgproxynftablesproxiergo1773) `:1773`


</details>


[function] name: NewDualStackProxier file: pkg/proxy/nftables/proxier.go:100 returns_error: да description: NewDualStackProxier creates a MetaProxier instance, with IPv4 and IPv6 proxies.


### NewDualStackProxier (pkg/proxy/nftables/proxier.go:100)


NewDualStackProxier creates a MetaProxier instance, with IPv4 and IPv6 proxies.


```go
func NewDualStackProxier((proxy.Provider, error)) (proxy.Provider, error)
```


**Тип ответа:** proxy.Provider


```json
{
  "cadvisor": {},
  "podManager": {}
}
```


*Определено в:* `pkg/kubelet/stats/provider.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `proxy.Provider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:100`



---


[function] name: NewProxier file: pkg/proxy/nftables/proxier.go:206 returns_error: да description: NewProxier returns a new single-stack NFTables proxier.


### NewProxier (pkg/proxy/nftables/proxier.go:206)


NewProxier returns a new single-stack NFTables proxier.


```go
func NewProxier((*Proxier, error)) (*Proxier, error)
```


**Тип запроса:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Proxier`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:206`



---


[function] name: OnEndpointSliceAdd file: pkg/proxy/nftables/proxier.go:721 returns_error: нет description: OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


### OnEndpointSliceAdd (pkg/proxy/nftables/proxier.go:721)


OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


```go
func (proxier *Proxier) OnEndpointSliceAdd((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:721`



---


[function] name: OnEndpointSliceDelete file: pkg/proxy/nftables/proxier.go:737 returns_error: нет description: OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


### OnEndpointSliceDelete (pkg/proxy/nftables/proxier.go:737)


OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


```go
func (proxier *Proxier) OnEndpointSliceDelete((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:737`



---


[function] name: OnEndpointSliceUpdate file: pkg/proxy/nftables/proxier.go:729 returns_error: нет description: OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


### OnEndpointSliceUpdate (pkg/proxy/nftables/proxier.go:729)


OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


```go
func (proxier *Proxier) OnEndpointSliceUpdate((_, endpointSlice *discovery.EndpointSlice)) (_, endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:729`



---


[function] name: OnEndpointSlicesSynced file: pkg/proxy/nftables/proxier.go:745 returns_error: нет description: OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to lo


### OnEndpointSlicesSynced (pkg/proxy/nftables/proxier.go:745)


OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *Proxier) OnEndpointSlicesSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:745`



---


[function] name: OnServiceAdd file: pkg/proxy/nftables/proxier.go:689 returns_error: нет description: OnServiceAdd is called whenever creation of new service object
is observed.


### OnServiceAdd (pkg/proxy/nftables/proxier.go:689)


OnServiceAdd is called whenever creation of new service object
is observed.


```go
func (proxier *Proxier) OnServiceAdd((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:689`



---


[function] name: OnServiceCIDRsChanged file: pkg/proxy/nftables/proxier.go:767 returns_error: нет description: OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of 


### OnServiceCIDRsChanged (pkg/proxy/nftables/proxier.go:767)


OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of service cidrs.


```go
func (proxier *Proxier) OnServiceCIDRsChanged((cidrs []string)) (cidrs []string)
```


**Тип ответа:** cidrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:767`



---


[function] name: OnServiceDelete file: pkg/proxy/nftables/proxier.go:703 returns_error: нет description: OnServiceDelete is called whenever deletion of an existing service
object is observed.


### OnServiceDelete (pkg/proxy/nftables/proxier.go:703)


OnServiceDelete is called whenever deletion of an existing service
object is observed.


```go
func (proxier *Proxier) OnServiceDelete((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:703`



---


[function] name: OnServiceSynced file: pkg/proxy/nftables/proxier.go:709 returns_error: нет description: OnServiceSynced is called once all the initial event handlers were
called and the state is fully propagated to local cac


### OnServiceSynced (pkg/proxy/nftables/proxier.go:709)


OnServiceSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *Proxier) OnServiceSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:709`



---


[function] name: OnServiceUpdate file: pkg/proxy/nftables/proxier.go:695 returns_error: нет description: OnServiceUpdate is called whenever modification of an existing
service object is observed.


### OnServiceUpdate (pkg/proxy/nftables/proxier.go:695)


OnServiceUpdate is called whenever modification of an existing
service object is observed.


```go
func (proxier *Proxier) OnServiceUpdate((oldService, service *v1.Service)) (oldService, service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:695`



---


[function] name: OnTopologyChange file: pkg/proxy/nftables/proxier.go:756 returns_error: нет description: OnTopologyChange is called whenever this node's proxy relevant topology-related labels change.


### OnTopologyChange (pkg/proxy/nftables/proxier.go:756)


OnTopologyChange is called whenever this node's proxy relevant topology-related labels change.


```go
func (proxier *Proxier) OnTopologyChange((topologyLabels map[string]string)) (topologyLabels map[string]string)
```


**Тип ответа:** topologyLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:756`



---


[function] name: Sync file: pkg/proxy/nftables/proxier.go:655 returns_error: нет description: Sync is called to synchronize the proxier state to nftables as soon as possible.


### Sync (pkg/proxy/nftables/proxier.go:655)


Sync is called to synchronize the proxier state to nftables as soon as possible.


```go
func (proxier *Proxier) Sync(()) ()
```


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:655`



---


[function] name: SyncLoop file: pkg/proxy/nftables/proxier.go:664 returns_error: нет description: SyncLoop runs periodic work.  This is expected to run as a goroutine or as the main loop of the app.  It does not return


### SyncLoop (pkg/proxy/nftables/proxier.go:664)


SyncLoop runs periodic work.  This is expected to run as a goroutine or as the main loop of the app.  It does not return.


```go
func (proxier *Proxier) SyncLoop(()) ()
```


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:664`



---


[function] name: cleanupLeftoverKeys file: pkg/proxy/nftables/proxier.go:984 returns_error: нет description: —


### cleanupLeftoverKeys (pkg/proxy/nftables/proxier.go:984)


cleanupLeftoverKeys is a method that performs operations based on the provided parameters and returns (tx *knftables.Transaction).


```go
func (s *nftElementStorage) cleanupLeftoverKeys((tx *knftables.Transaction)) (tx *knftables.Transaction)
```


**Тип запроса:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** tx


```json
{
  "valueCtx": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/kubeletplugin/nonblockinggrpcserver.go`


**Тип ответа:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:984`



---


[function] name: ensureChain file: pkg/proxy/nftables/proxier.go:392 returns_error: нет description: ensureChain adds commands to tx to ensure that chain exists and doesn't contain
anything from before this transaction (u


### ensureChain (pkg/proxy/nftables/proxier.go:392)


ensureChain adds commands to tx to ensure that chain exists and doesn't contain
anything from before this transaction (using createdChains to ensure that we don't
Flush a chain more than once and lose *new* rules as well.)
If skipCreation is true, chain will not be added to the transaction, but will be added to the createdChains
for proper cleanup in the end of the sync iteration.


```go
func ensureChain((chain string, tx *knftables.Transaction, createdChains sets.Set[string], skipCreation bool)) (chain string, tx *knftables.Transaction, createdChains sets.Set[string], skipCreation bool)
```


**Тип запроса:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** chain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** tx


```json
{
  "valueCtx": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/kubeletplugin/nonblockinggrpcserver.go`


**Тип ответа:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** createdChains


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Тип ответа:** skipCreation


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:392`



---


[function] name: ensureElem file: pkg/proxy/nftables/proxier.go:966 returns_error: нет description: ensureElem adds elem to the transaction if elem is not present in the container, and updates internal
leftoverKeys set t


### ensureElem (pkg/proxy/nftables/proxier.go:966)


ensureElem adds elem to the transaction if elem is not present in the container, and updates internal
leftoverKeys set to track unused elements.


```go
func (s *nftElementStorage) ensureElem((tx *knftables.Transaction, elem *knftables.Element)) (tx *knftables.Transaction, elem *knftables.Element)
```


**Тип запроса:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип запроса:** knftables.Element


```json
{
  "Key": "string",
  "Object": {},
  "Labels": {},
  "Fields": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/store/store.go`


**Тип ответа:** tx


```json
{
  "valueCtx": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/kubeletplugin/nonblockinggrpcserver.go`


**Тип ответа:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** elem


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** knftables.Element


```json
{
  "Key": "string",
  "Object": {},
  "Labels": {},
  "Fields": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/cacher/store/store.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:966`



---


[function] name: epChainSkipUpdate file: pkg/proxy/nftables/proxier.go:1750 returns_error: нет description: epChainSkipUpdate returns true if the EP chain doesn't need to be updated.


### epChainSkipUpdate (pkg/proxy/nftables/proxier.go:1750)


epChainSkipUpdate returns true if the EP chain doesn't need to be updated.


```go
func (proxier *Proxier) epChainSkipUpdate((existingChains, existingAffinitySets sets.Set[string], svcInfo *servicePortInfo, epInfo *endpointInfo)) (existingChains, existingAffinitySets sets.Set[string], svcInfo *servicePortInfo, epInfo *endpointInfo)
```


**Тип запроса:** servicePortInfo


```json
{
  "nameString": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/proxier.go`


**Тип запроса:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** existingChains


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** existingAffinitySets


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sets.Set


```json
{
  "sha256Hashes": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/pubkeypin/pubkeypin.go`


**Тип ответа:** svcInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** servicePortInfo


```json
{
  "nameString": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/proxier.go`


**Тип ответа:** epInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:1750`



---


[function] name: hashAndTruncate file: pkg/proxy/nftables/proxier.go:809 returns_error: нет description: hashAndTruncate prefixes name with a hash of itself and then truncates to
chainNameBaseLengthMax. The hash ensures that 


### hashAndTruncate (pkg/proxy/nftables/proxier.go:809)


hashAndTruncate prefixes name with a hash of itself and then truncates to
chainNameBaseLengthMax. The hash ensures that (a) the name is still unique if we have
to truncate the end, and (b) it's visually distinguishable from other chains that would
otherwise have nearly identical names (e.g., different endpoint chains for a given
service that differ in only a single digit).


```go
func hashAndTruncate((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:809`



---


[function] name: isAffinitySetName file: pkg/proxy/nftables/proxier.go:895 returns_error: нет description: —


### isAffinitySetName (pkg/proxy/nftables/proxier.go:895)


isAffinitySetName is a function that performs operations based on the provided parameters and returns (set string).


```go
func isAffinitySetName((set string)) (set string)
```


**Тип ответа:** set


```json
{
  "kubeconfigPath": "string",
  "cfgPath": "string",
  "ignorePreflightErrors": [],
  "externalcfg": null,
  "skipCRIDetect": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/reset.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:895`



---


[function] name: isInitialized file: pkg/proxy/nftables/proxier.go:683 returns_error: нет description: —


### isInitialized (pkg/proxy/nftables/proxier.go:683)


isInitialized is a method that performs operations based on the provided parameters and returns ().


```go
func (proxier *Proxier) isInitialized(()) ()
```


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:683`



---


[function] name: isServiceChainName file: pkg/proxy/nftables/proxier.go:887 returns_error: нет description: —


### isServiceChainName (pkg/proxy/nftables/proxier.go:887)


isServiceChainName is a function that performs operations based on the provided parameters and returns (chainString string).


```go
func isServiceChainName((chainString string)) (chainString string)
```


**Тип ответа:** chainString


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:887`



---


[function] name: joinNFTSlice file: pkg/proxy/nftables/proxier.go:909 returns_error: нет description: joinNFTSlice converts nft element key or value (type []string) to string to store in the nftElementStorage.
The separato


### joinNFTSlice (pkg/proxy/nftables/proxier.go:909)


joinNFTSlice converts nft element key or value (type []string) to string to store in the nftElementStorage.
The separator is the same as the one used by nft commands, so we know that the parsing is going to be unambiguous.


```go
func joinNFTSlice((k []string)) (k []string)
```


**Тип ответа:** k


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


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:909`



---


[function] name: logFailure file: pkg/proxy/nftables/proxier.go:1001 returns_error: нет description: logFailure logs the transaction and the full table with a rate limit.


### logFailure (pkg/proxy/nftables/proxier.go:1001)


logFailure logs the transaction and the full table with a rate limit.


```go
func (proxier *Proxier) logFailure((tx *knftables.Transaction)) (tx *knftables.Transaction)
```


**Тип запроса:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** tx


```json
{
  "valueCtx": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/kubeletplugin/nonblockinggrpcserver.go`


**Тип ответа:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:1001`



---


[function] name: newEndpointInfo file: pkg/proxy/nftables/proxier.go:317 returns_error: нет description: returns a new proxy.Endpoint which abstracts a endpointInfo


### newEndpointInfo (pkg/proxy/nftables/proxier.go:317)


returns a new proxy.Endpoint which abstracts a endpointInfo


```go
func newEndpointInfo((baseInfo *proxy.BaseEndpointInfo, svcPortName *proxy.ServicePortName)) (baseInfo *proxy.BaseEndpointInfo, svcPortName *proxy.ServicePortName)
```


**Тип запроса:** proxy.BaseEndpointInfo


```json
{
  "ip": "string",
  "port": 0,
  "endpoint": "string",
  "isLocal": false,
  "ready": false,
  "serving": false,
  "terminating": false,
  "zoneHints": {},
  "nodeHints": {}
}
```


*Определено в:* `pkg/proxy/endpoint.go`


**Тип запроса:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** baseInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.BaseEndpointInfo


```json
{
  "ip": "string",
  "port": 0,
  "endpoint": "string",
  "isLocal": false,
  "ready": false,
  "serving": false,
  "terminating": false,
  "zoneHints": {},
  "nodeHints": {}
}
```


*Определено в:* `pkg/proxy/endpoint.go`


**Тип ответа:** svcPortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:317`



---


[function] name: newNFTElementStorage file: pkg/proxy/nftables/proxier.go:920 returns_error: нет description: newNFTElementStorage creates an empty nftElementStorage.
nftElementStorage.reset() must be called before the first usage


### newNFTElementStorage (pkg/proxy/nftables/proxier.go:920)


newNFTElementStorage creates an empty nftElementStorage.
nftElementStorage.reset() must be called before the first usage.


```go
func newNFTElementStorage((containerType, containerName string)) (containerType, containerName string)
```


**Тип ответа:** containerType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** containerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:920`



---


[function] name: newServiceInfo file: pkg/proxy/nftables/proxier.go:291 returns_error: нет description: returns a new proxy.ServicePort which abstracts a serviceInfo


### newServiceInfo (pkg/proxy/nftables/proxier.go:291)


returns a new proxy.ServicePort which abstracts a serviceInfo


```go
func newServiceInfo((port *v1.ServicePort, service *v1.Service, bsvcPortInfo *proxy.BaseServicePortInfo)) (port *v1.ServicePort, service *v1.Service, bsvcPortInfo *proxy.BaseServicePortInfo)
```


**Тип запроса:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** proxy.BaseServicePortInfo


```json
{
  "clusterIP": {},
  "port": 0,
  "protocol": {},
  "nodePort": 0,
  "loadBalancerVIPs": [],
  "sessionAffinityType": {},
  "stickyMaxAgeSeconds": 0,
  "externalIPs": [],
  "loadBalancerSourceRanges": [],
  "healthCheckNodePort": 0,
  "externalPolicyLocal": false,
  "internalPolicyLocal": false
}
```


*Определено в:* `pkg/proxy/serviceport.go`


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


**Тип ответа:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** bsvcPortInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.BaseServicePortInfo


```json
{
  "clusterIP": {},
  "port": 0,
  "protocol": {},
  "nodePort": 0,
  "loadBalancerVIPs": [],
  "sessionAffinityType": {},
  "stickyMaxAgeSeconds": 0,
  "externalIPs": [],
  "loadBalancerSourceRanges": [],
  "healthCheckNodePort": 0,
  "externalPolicyLocal": false,
  "internalPolicyLocal": false
}
```


*Определено в:* `pkg/proxy/serviceport.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:291`



---


[function] name: readOrReset file: pkg/proxy/nftables/proxier.go:932 returns_error: нет description: readOrReset updates the existing elements from the nftables map/set.
If reading fails, it clears the internal state and 


### readOrReset (pkg/proxy/nftables/proxier.go:932)


readOrReset updates the existing elements from the nftables map/set.
If reading fails, it clears the internal state and flushes the nftables map/set.


```go
func (s *nftElementStorage) readOrReset((tx *knftables.Transaction, nftables knftables.Interface, logger klog.Logger)) (tx *knftables.Transaction, nftables knftables.Interface, logger klog.Logger)
```


**Тип запроса:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** tx


```json
{
  "valueCtx": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/kubeletplugin/nonblockinggrpcserver.go`


**Тип ответа:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** nftables


```json
{
  "name": "string",
  "chainType": {},
  "hook": {},
  "priority": {}
}
```


*Определено в:* `pkg/proxy/nftables/proxier.go`


**Тип ответа:** knftables.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** klog.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:932`



---


[function] name: resetLeftoverKeys file: pkg/proxy/nftables/proxier.go:957 returns_error: нет description: resetLeftoverKeys is only called internally by nftElementStorage methods.


### resetLeftoverKeys (pkg/proxy/nftables/proxier.go:957)


resetLeftoverKeys is only called internally by nftElementStorage methods.


```go
func (s *nftElementStorage) resetLeftoverKeys(()) ()
```


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:957`



---


[function] name: servicePortChainNameBase file: pkg/proxy/nftables/proxier.go:822 returns_error: нет description: servicePortChainNameBase returns the base name for a chain for the given ServicePort.
This is something like "HASH-names


### servicePortChainNameBase (pkg/proxy/nftables/proxier.go:822)


servicePortChainNameBase returns the base name for a chain for the given ServicePort.
This is something like "HASH-namespace/serviceName/protocol/portName", e.g,
"ULMVA6XW-ns1/svc1/tcp/p80".


```go
func servicePortChainNameBase((servicePortName *proxy.ServicePortName, protocol string)) (servicePortName *proxy.ServicePortName, protocol string)
```


**Тип запроса:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** servicePortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:822`



---


[function] name: servicePortEndpointChainNameBase file: pkg/proxy/nftables/proxier.go:855 returns_error: нет description: servicePortEndpointChainNameBase returns the suffix for chain names for the given
endpoint. This is something like
"HASH


### servicePortEndpointChainNameBase (pkg/proxy/nftables/proxier.go:855)


servicePortEndpointChainNameBase returns the suffix for chain names for the given
endpoint. This is something like
"HASH-namespace/serviceName/protocol/portName__endpointIP/endpointport", e.g.,
"5OJB2KTY-ns1/svc1/tcp/p80__10.180.0.1/80".


```go
func servicePortEndpointChainNameBase((servicePortName *proxy.ServicePortName, protocol, endpoint string)) (servicePortName *proxy.ServicePortName, protocol, endpoint string)
```


**Тип запроса:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** servicePortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpoint


```json
{
  "URL": "string",
  "AccessToken": "string",
  "JWT": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:855`



---


[function] name: setInitialized file: pkg/proxy/nftables/proxier.go:675 returns_error: нет description: —


### setInitialized (pkg/proxy/nftables/proxier.go:675)


setInitialized is a method that performs operations based on the provided parameters and returns (value bool).


```go
func (proxier *Proxier) setInitialized((value bool)) (value bool)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:675`



---


[function] name: setupNFTables file: pkg/proxy/nftables/proxier.go:408 returns_error: нет description: —


### setupNFTables (pkg/proxy/nftables/proxier.go:408)


setupNFTables is a method that performs operations based on the provided parameters and returns (tx *knftables.Transaction).


```go
func (proxier *Proxier) setupNFTables((tx *knftables.Transaction)) (tx *knftables.Transaction)
```


**Тип запроса:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** tx


```json
{
  "valueCtx": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/kubeletplugin/nonblockinggrpcserver.go`


**Тип ответа:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:408`



---


[function] name: splitNFTSlice file: pkg/proxy/nftables/proxier.go:914 returns_error: нет description: splitNFTSlice converts nftElementStorage key or value string representation back to slice.


### splitNFTSlice (pkg/proxy/nftables/proxier.go:914)


splitNFTSlice converts nftElementStorage key or value string representation back to slice.


```go
func splitNFTSlice((k string)) (k string)
```


**Тип ответа:** k


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


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:914`



---


[function] name: syncProxyRules file: pkg/proxy/nftables/proxier.go:1017 returns_error: да description: This is where all of the nftables calls happen.
This assumes proxier.mu is NOT held


### syncProxyRules (pkg/proxy/nftables/proxier.go:1017)


This is where all of the nftables calls happen.
This assumes proxier.mu is NOT held


```go
func (proxier *Proxier) syncProxyRules((retryError error)) (retryError error)
```


**Тип ответа:** retryError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `retryError error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:1017`



---


[function] name: writeServiceToEndpointRules file: pkg/proxy/nftables/proxier.go:1773 returns_error: нет description: —


### writeServiceToEndpointRules (pkg/proxy/nftables/proxier.go:1773)


writeServiceToEndpointRules is a method that performs operations based on the provided parameters and returns (tx *knftables.Transaction, svcInfo *servicePortInfo, svcChain string, endpoints []proxy.Endpoint).


```go
func (proxier *Proxier) writeServiceToEndpointRules((tx *knftables.Transaction, svcInfo *servicePortInfo, svcChain string, endpoints []proxy.Endpoint)) (tx *knftables.Transaction, svcInfo *servicePortInfo, svcChain string, endpoints []proxy.Endpoint)
```


**Тип запроса:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип запроса:** servicePortInfo


```json
{
  "nameString": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/proxier.go`


**Тип ответа:** tx


```json
{
  "valueCtx": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/kubeletplugin/nonblockinggrpcserver.go`


**Тип ответа:** knftables.Transaction


```json
{
  "Object": {},
  "Type": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/store.go`


**Тип ответа:** svcInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** servicePortInfo


```json
{
  "nameString": "string"
}
```


*Определено в:* `pkg/proxy/ipvs/proxier.go`


**Тип ответа:** svcChain


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** proxy.Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/nftables/proxier.go:1773`




## pkg/proxy/nftables/supported.go


📄 Исходный файл: `pkg/proxy/nftables/supported.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [getNFTablesInterface](#getnftablesinterface-pkgproxynftablessupportedgo32) `:32`


</details>


[function] name: getNFTablesInterface file: pkg/proxy/nftables/supported.go:32 returns_error: да description: Create a knftables.Interface and check if we can use the nftables proxy mode on this host.


### getNFTablesInterface (pkg/proxy/nftables/supported.go:32)


Create a knftables.Interface and check if we can use the nftables proxy mode on this host.


```go
func getNFTablesInterface((knftables.Interface, error)) (knftables.Interface, error)
```


**Тип ответа:** knftables.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `knftables.Interface`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/nftables/supported.go:32`




## pkg/proxy/node.go


📄 Исходный файл: `pkg/proxy/node.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [NewNodeManager](#newnodemanager-pkgproxynodego63) `:63`

- 🔗 [Node](#node-pkgproxynodego159) `:159`

- 🔗 [NodeIPs](#nodeips-pkgproxynodego149) `:149`

- 🔗 [NodeInformer](#nodeinformer-pkgproxynodego170) `:170`

- 🔗 [OnNodeChange](#onnodechange-pkgproxynodego175) `:175`

- 🔗 [OnNodeDelete](#onnodedelete-pkgproxynodego206) `:206`

- 🔗 [OnNodeSynced](#onnodesynced-pkgproxynodego214) `:214`

- 🔗 [PodCIDRs](#podcidrs-pkgproxynodego154) `:154`

- 🔗 [getNodeInfo](#getnodeinfo-pkgproxynodego138) `:138`

- 🔗 [newNodeManager](#newnodemanager-pkgproxynodego70) `:70`


</details>


[function] name: NewNodeManager file: pkg/proxy/node.go:63 returns_error: да description: NewNodeManager initializes node informer that selects for the given node, waits for cache sync
and returns NodeManager a


### NewNodeManager (pkg/proxy/node.go:63)


NewNodeManager initializes node informer that selects for the given node, waits for cache sync
and returns NodeManager after waiting some amount of time for the node object to exist
and have NodeIPs (and PodCIDRs if watchPodCIDRs is true). Note: for backward compatibility,
NewNodeManager doesn't return any error if it failed to retrieve NodeIPs and watchPodCIDRs
is false.


```go
func NewNodeManager((*NodeManager, error)) (*NodeManager, error)
```


**Тип запроса:** NodeManager


```json
{
  "nodeInformer": {},
  "nodeLister": {},
  "exitFunc": {},
  "watchPodCIDRs": false,
  "nodeIPs": [],
  "podCIDRs": [],
  "mu": {},
  "node": null
}
```


*Определено в:* `pkg/proxy/node.go`


**Тип ответа:** NodeManager


```json
{
  "nodeInformer": {},
  "nodeLister": {},
  "exitFunc": {},
  "watchPodCIDRs": false,
  "nodeIPs": [],
  "podCIDRs": [],
  "mu": {},
  "node": null
}
```


*Определено в:* `pkg/proxy/node.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NodeManager`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/node.go:63`



---


[function] name: Node file: pkg/proxy/node.go:159 returns_error: нет description: Node returns a copy of the latest node object, or nil if the Node has not yet been seen.


### Node (pkg/proxy/node.go:159)


Node returns a copy of the latest node object, or nil if the Node has not yet been seen.


```go
func (n *NodeManager) Node(()) ()
```


📍 *Расположение:* `pkg/proxy/node.go:159`



---


[function] name: NodeIPs file: pkg/proxy/node.go:149 returns_error: нет description: NodeIPs returns the NodeIPs polled in NewNodeManager(). (This may be empty if
NewNodeManager timed out without getting a


### NodeIPs (pkg/proxy/node.go:149)


NodeIPs returns the NodeIPs polled in NewNodeManager(). (This may be empty if
NewNodeManager timed out without getting any IPs.)


```go
func (n *NodeManager) NodeIPs(()) ()
```


📍 *Расположение:* `pkg/proxy/node.go:149`



---


[function] name: NodeInformer file: pkg/proxy/node.go:170 returns_error: нет description: NodeInformer returns the NodeInformer.


### NodeInformer (pkg/proxy/node.go:170)


NodeInformer returns the NodeInformer.


```go
func (n *NodeManager) NodeInformer(()) ()
```


📍 *Расположение:* `pkg/proxy/node.go:170`



---


[function] name: OnNodeChange file: pkg/proxy/node.go:175 returns_error: нет description: OnNodeChange is a handler for Node creation and update.


### OnNodeChange (pkg/proxy/node.go:175)


OnNodeChange is a handler for Node creation and update.


```go
func (n *NodeManager) OnNodeChange((node *v1.Node)) (node *v1.Node)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** node


```json
{
  "identity": {},
  "dependentsLock": {},
  "dependents": {},
  "deletingDependents": false,
  "deletingDependentsLock": {},
  "beingDeleted": false,
  "beingDeletedLock": {},
  "virtual": false,
  "virtualLock": {},
  "owners": [],
  "ownersLock": {}
}
```


*Определено в:* `pkg/controller/garbagecollector/graph.go`


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/node.go:175`



---


[function] name: OnNodeDelete file: pkg/proxy/node.go:206 returns_error: нет description: OnNodeDelete is a handler for Node deletes.


### OnNodeDelete (pkg/proxy/node.go:206)


OnNodeDelete is a handler for Node deletes.


```go
func (n *NodeManager) OnNodeDelete((node *v1.Node)) (node *v1.Node)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** node


```json
{
  "identity": {},
  "dependentsLock": {},
  "dependents": {},
  "deletingDependents": false,
  "deletingDependentsLock": {},
  "beingDeleted": false,
  "beingDeletedLock": {},
  "virtual": false,
  "virtualLock": {},
  "owners": [],
  "ownersLock": {}
}
```


*Определено в:* `pkg/controller/garbagecollector/graph.go`


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/node.go:206`



---


[function] name: OnNodeSynced file: pkg/proxy/node.go:214 returns_error: нет description: OnNodeSynced is called after the cache is synced and all pre-existing Nodes have been reported


### OnNodeSynced (pkg/proxy/node.go:214)


OnNodeSynced is called after the cache is synced and all pre-existing Nodes have been reported


```go
func (n *NodeManager) OnNodeSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/node.go:214`



---


[function] name: PodCIDRs file: pkg/proxy/node.go:154 returns_error: нет description: PodCIDRs returns the PodCIDRs polled in NewNodeManager().


### PodCIDRs (pkg/proxy/node.go:154)


PodCIDRs returns the PodCIDRs polled in NewNodeManager().


```go
func (n *NodeManager) PodCIDRs(()) ()
```


📍 *Расположение:* `pkg/proxy/node.go:154`



---


[function] name: getNodeInfo file: pkg/proxy/node.go:138 returns_error: нет description: —


### getNodeInfo (pkg/proxy/node.go:138)


getNodeInfo is a function that performs operations based on the provided parameters and returns (*v1.Node, []net.IP, []string).


```go
func getNodeInfo((*v1.Node, []net.IP, []string)) (*v1.Node, []net.IP, []string)
```


**Тип запроса:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** v1.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `pkg/proxy/node.go:138`



---


[function] name: newNodeManager file: pkg/proxy/node.go:70 returns_error: да description: newNodeManager implements NewNodeManager with configurable exit function, poll interval and timeouts.


### newNodeManager (pkg/proxy/node.go:70)


newNodeManager implements NewNodeManager with configurable exit function, poll interval and timeouts.


```go
func newNodeManager((*NodeManager, error)) (*NodeManager, error)
```


**Тип запроса:** NodeManager


```json
{
  "nodeInformer": {},
  "nodeLister": {},
  "exitFunc": {},
  "watchPodCIDRs": false,
  "nodeIPs": [],
  "podCIDRs": [],
  "mu": {},
  "node": null
}
```


*Определено в:* `pkg/proxy/node.go`


**Тип ответа:** NodeManager


```json
{
  "nodeInformer": {},
  "nodeLister": {},
  "exitFunc": {},
  "watchPodCIDRs": false,
  "nodeIPs": [],
  "podCIDRs": [],
  "mu": {},
  "node": null
}
```


*Определено в:* `pkg/proxy/node.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NodeManager`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/node.go:70`




## pkg/proxy/runner/bounded_frequency_runner.go


📄 Исходный файл: `pkg/proxy/runner/bounded_frequency_runner.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Loop](#loop-pkgproxyrunnerbounded_frequency_runnergo89) `:89`

- 🔗 [NewBoundedFrequencyRunner](#newboundedfrequencyrunner-pkgproxyrunnerbounded_frequency_runnergo62) `:62`

- 🔗 [Run](#run-pkgproxyrunnerbounded_frequency_runnergo149) `:149`

- 🔗 [construct](#construct-pkgproxyrunnerbounded_frequency_runnergo67) `:67`


</details>


[function] name: Loop file: pkg/proxy/runner/bounded_frequency_runner.go:89 returns_error: нет description: Loop handles the periodic timer and run requests.  This is expected to be
called as a goroutine.


### Loop (pkg/proxy/runner/bounded_frequency_runner.go:89)


Loop handles the periodic timer and run requests.  This is expected to be
called as a goroutine.


```go
func (bfr *BoundedFrequencyRunner) Loop((stop <-chan struct{})) (stop <-chan struct{})
```


**Тип ответа:** stop


```json
{
  "Opcode": {}
}
```


*Определено в:* `test/integration/scheduler_perf/operations.go`


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** struct


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


📍 *Расположение:* `pkg/proxy/runner/bounded_frequency_runner.go:89`



---


[function] name: NewBoundedFrequencyRunner file: pkg/proxy/runner/bounded_frequency_runner.go:62 returns_error: да description: NewBoundedFrequencyRunner creates and returns a new BoundedFrequencyRunner.
This runner manages the execution frequency 


### NewBoundedFrequencyRunner (pkg/proxy/runner/bounded_frequency_runner.go:62)


NewBoundedFrequencyRunner creates and returns a new BoundedFrequencyRunner.
This runner manages the execution frequency of the provided function `fn`.

The runner guarantees two properties:
1. Minimum Interval (`minInterval`): At least `minInterval` must pass between
the *completion* of one execution and the *start* of the next. Calls to
`Run()` during this cooldown period are coalesced and deferred until the
interval expires. This prevents burst executions.
2. Maximum Interval (`maxInterval`): The function `fn` is guaranteed to run
at least once per `maxInterval`, ensuring periodic execution even without
explicit `Run()` calls (e.g., for refreshing state).

`maxInterval` must be greater than or equal to `minInterval`; otherwise,
this function will panic.

If `fn` returns an error, then it will be run again no later than `retryInterval`
(unless another trigger, like `Run()` or `maxInterval`, causes it to run sooner). Any
successful run will abort the retry attempt.


```go
func NewBoundedFrequencyRunner((name string, fn func() error, minInterval, retryInterval, maxInterval time.Duration)) (name string, fn func() error, minInterval, retryInterval, maxInterval time.Duration)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** minInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** retryInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxInterval


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `name string`, `fn func() error`, `minInterval`, `retryInterval`, `maxInterval time.Duration`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/runner/bounded_frequency_runner.go:62`



---


[function] name: Run file: pkg/proxy/runner/bounded_frequency_runner.go:149 returns_error: нет description: Run the work function as soon as possible.  If this is called while Loop is not
running, the call may be deferred indefi


### Run (pkg/proxy/runner/bounded_frequency_runner.go:149)


Run the work function as soon as possible.  If this is called while Loop is not
running, the call may be deferred indefinitely.
Once there is a queued request to call the work function, further calls to
Run() will have no effect until after it runs.


```go
func (bfr *BoundedFrequencyRunner) Run(()) ()
```


📍 *Расположение:* `pkg/proxy/runner/bounded_frequency_runner.go:149`



---


[function] name: construct file: pkg/proxy/runner/bounded_frequency_runner.go:67 returns_error: да description: Make an instance with dependencies injected.


### construct (pkg/proxy/runner/bounded_frequency_runner.go:67)


Make an instance with dependencies injected.


```go
func construct((name string, fn func() error, minInterval, retryInterval, maxInterval time.Duration, clock clock.Clock)) (name string, fn func() error, minInterval, retryInterval, maxInterval time.Duration, clock clock.Clock)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** minInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** retryInterval


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** maxInterval


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


**Тип ответа:** clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** clock.Clock


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `name string`, `fn func() error`, `minInterval`, `retryInterval`, `maxInterval time.Duration`, `clock clock.Clock`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/runner/bounded_frequency_runner.go:67`




## pkg/proxy/servicechangetracker.go


📄 Исходный файл: `pkg/proxy/servicechangetracker.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [HealthCheckNodePorts](#healthchecknodeports-pkgproxyservicechangetrackergo121) `:121`

- 🔗 [NewServiceChangeTracker](#newservicechangetracker-pkgproxyservicechangetrackergo62) `:62`

- 🔗 [Update](#update-pkgproxyservicechangetrackergo76) `:76`

- 🔗 [Update](#update-pkgproxyservicechangetrackergo168) `:168`

- 🔗 [filter](#filter-pkgproxyservicechangetrackergo211) `:211`

- 🔗 [merge](#merge-pkgproxyservicechangetrackergo198) `:198`

- 🔗 [serviceToServiceMap](#servicetoservicemap-pkgproxyservicechangetrackergo136) `:136`

- 🔗 [unmerge](#unmerge-pkgproxyservicechangetrackergo221) `:221`


</details>


[function] name: HealthCheckNodePorts file: pkg/proxy/servicechangetracker.go:121 returns_error: нет description: HealthCheckNodePorts returns a map of Service names to HealthCheckNodePort values
for all Services in sm with non-zero H


### HealthCheckNodePorts (pkg/proxy/servicechangetracker.go:121)


HealthCheckNodePorts returns a map of Service names to HealthCheckNodePort values
for all Services in sm with non-zero HealthCheckNodePort.


```go
func (sm ServicePortMap) HealthCheckNodePorts(()) ()
```


📍 *Расположение:* `pkg/proxy/servicechangetracker.go:121`



---


[function] name: NewServiceChangeTracker file: pkg/proxy/servicechangetracker.go:62 returns_error: нет description: NewServiceChangeTracker initializes a ServiceChangeTracker


### NewServiceChangeTracker (pkg/proxy/servicechangetracker.go:62)


NewServiceChangeTracker initializes a ServiceChangeTracker


```go
func NewServiceChangeTracker((ipFamily v1.IPFamily, makeServiceInfo makeServicePortFunc, processServiceMapChange processServiceMapChangeFunc)) (ipFamily v1.IPFamily, makeServiceInfo makeServicePortFunc, processServiceMapChange processServiceMapChangeFunc)
```


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** makeServiceInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** makeServicePortFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** processServiceMapChange


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** processServiceMapChangeFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/servicechangetracker.go:62`



---


[function] name: Update file: pkg/proxy/servicechangetracker.go:76 returns_error: нет description: Update updates the ServiceChangeTracker based on the <previous, current> service pair
(where either previous or current,


### Update (pkg/proxy/servicechangetracker.go:76)


Update updates the ServiceChangeTracker based on the <previous, current> service pair
(where either previous or current, but not both, can be nil). It returns true if sct
contains changes that need to be synced (whether or not those changes were caused by
this update); note that this is different from the return value of
EndpointChangeTracker.EndpointSliceUpdate().


```go
func (sct *ServiceChangeTracker) Update((previous, current *v1.Service)) (previous, current *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** previous


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** current


```json
{
  "visitors": [],
  "concurrency": 0
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/visitor.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/servicechangetracker.go:76`



---


[function] name: Update file: pkg/proxy/servicechangetracker.go:168 returns_error: нет description: Update updates ServicePortMap base on the given changes, returns information about the
diff since the last Update, trigg


### Update (pkg/proxy/servicechangetracker.go:168)


Update updates ServicePortMap base on the given changes, returns information about the
diff since the last Update, triggers processServiceMapChange on every change, and
clears the changes map.


```go
func (sm ServicePortMap) Update((sct *ServiceChangeTracker)) (sct *ServiceChangeTracker)
```


**Тип запроса:** ServiceChangeTracker


```json
{
  "lock": {},
  "items": {},
  "makeServiceInfo": {},
  "processServiceMapChange": {},
  "ipFamily": {}
}
```


*Определено в:* `pkg/proxy/servicechangetracker.go`


**Тип ответа:** sct


```json
{
  "Name": "string",
  "Value": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/sysctl.go`


**Тип ответа:** ServiceChangeTracker


```json
{
  "lock": {},
  "items": {},
  "makeServiceInfo": {},
  "processServiceMapChange": {},
  "ipFamily": {}
}
```


*Определено в:* `pkg/proxy/servicechangetracker.go`


📍 *Расположение:* `pkg/proxy/servicechangetracker.go:168`



---


[function] name: filter file: pkg/proxy/servicechangetracker.go:211 returns_error: нет description: filter filters out elements from ServicePortMap base on given ports string sets.


### filter (pkg/proxy/servicechangetracker.go:211)


filter filters out elements from ServicePortMap base on given ports string sets.


```go
func (sm *ServicePortMap) filter((other ServicePortMap)) (other ServicePortMap)
```


**Тип ответа:** other


```json
{
  "OS": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ordering/structs/doc.go`


**Тип ответа:** ServicePortMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/servicechangetracker.go:211`



---


[function] name: merge file: pkg/proxy/servicechangetracker.go:198 returns_error: нет description: merge adds other ServicePortMap's elements to current ServicePortMap.
If collision, other ALWAYS win. Otherwise add the 


### merge (pkg/proxy/servicechangetracker.go:198)


merge adds other ServicePortMap's elements to current ServicePortMap.
If collision, other ALWAYS win. Otherwise add the other to current.
In other words, if some elements in current collisions with other, update the current by other.


```go
func (sm *ServicePortMap) merge((other ServicePortMap)) (other ServicePortMap)
```


**Тип ответа:** other


```json
{
  "OS": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ordering/structs/doc.go`


**Тип ответа:** ServicePortMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/servicechangetracker.go:198`



---


[function] name: serviceToServiceMap file: pkg/proxy/servicechangetracker.go:136 returns_error: нет description: serviceToServiceMap translates a single Service object to a ServicePortMap.

NOTE: service object should NOT be modified


### serviceToServiceMap (pkg/proxy/servicechangetracker.go:136)


serviceToServiceMap translates a single Service object to a ServicePortMap.

NOTE: service object should NOT be modified.


```go
func (sct *ServiceChangeTracker) serviceToServiceMap((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/servicechangetracker.go:136`



---


[function] name: unmerge file: pkg/proxy/servicechangetracker.go:221 returns_error: нет description: unmerge deletes all other ServicePortMap's elements from current ServicePortMap.


### unmerge (pkg/proxy/servicechangetracker.go:221)


unmerge deletes all other ServicePortMap's elements from current ServicePortMap.


```go
func (sm *ServicePortMap) unmerge((other ServicePortMap)) (other ServicePortMap)
```


**Тип ответа:** other


```json
{
  "OS": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ordering/structs/doc.go`


**Тип ответа:** ServicePortMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/servicechangetracker.go:221`




## pkg/proxy/serviceport.go


📄 Исходный файл: `pkg/proxy/serviceport.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [ClusterIP](#clusterip-pkgproxyserviceportgo98) `:98`

- 🔗 [ExternalIPs](#externalips-pkgproxyserviceportgo138) `:138`

- 🔗 [ExternalPolicyLocal](#externalpolicylocal-pkgproxyserviceportgo148) `:148`

- 🔗 [ExternallyAccessible](#externallyaccessible-pkgproxyserviceportgo158) `:158`

- 🔗 [HealthCheckNodePort](#healthchecknodeport-pkgproxyserviceportgo128) `:128`

- 🔗 [InternalPolicyLocal](#internalpolicylocal-pkgproxyserviceportgo153) `:153`

- 🔗 [LoadBalancerSourceRanges](#loadbalancersourceranges-pkgproxyserviceportgo123) `:123`

- 🔗 [LoadBalancerVIPs](#loadbalancervips-pkgproxyserviceportgo143) `:143`

- 🔗 [NodePort](#nodeport-pkgproxyserviceportgo133) `:133`

- 🔗 [Port](#port-pkgproxyserviceportgo103) `:103`

- 🔗 [Protocol](#protocol-pkgproxyserviceportgo118) `:118`

- 🔗 [SessionAffinityType](#sessionaffinitytype-pkgproxyserviceportgo108) `:108`

- 🔗 [StickyMaxAgeSeconds](#stickymaxageseconds-pkgproxyserviceportgo113) `:113`

- 🔗 [String](#string-pkgproxyserviceportgo93) `:93`

- 🔗 [UsesClusterEndpoints](#usesclusterendpoints-pkgproxyserviceportgo163) `:163`

- 🔗 [UsesLocalEndpoints](#useslocalendpoints-pkgproxyserviceportgo171) `:171`

- 🔗 [newBaseServiceInfo](#newbaseserviceinfo-pkgproxyserviceportgo175) `:175`


</details>


[function] name: ClusterIP file: pkg/proxy/serviceport.go:98 returns_error: нет description: ClusterIP is part of ServicePort interface.


### ClusterIP (pkg/proxy/serviceport.go:98)


ClusterIP is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) ClusterIP(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:98`



---


[function] name: ExternalIPs file: pkg/proxy/serviceport.go:138 returns_error: нет description: ExternalIPs is part of ServicePort interface.


### ExternalIPs (pkg/proxy/serviceport.go:138)


ExternalIPs is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) ExternalIPs(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:138`



---


[function] name: ExternalPolicyLocal file: pkg/proxy/serviceport.go:148 returns_error: нет description: ExternalPolicyLocal is part of ServicePort interface.


### ExternalPolicyLocal (pkg/proxy/serviceport.go:148)


ExternalPolicyLocal is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) ExternalPolicyLocal(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:148`



---


[function] name: ExternallyAccessible file: pkg/proxy/serviceport.go:158 returns_error: нет description: ExternallyAccessible is part of ServicePort interface.


### ExternallyAccessible (pkg/proxy/serviceport.go:158)


ExternallyAccessible is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) ExternallyAccessible(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:158`



---


[function] name: HealthCheckNodePort file: pkg/proxy/serviceport.go:128 returns_error: нет description: HealthCheckNodePort is part of ServicePort interface.


### HealthCheckNodePort (pkg/proxy/serviceport.go:128)


HealthCheckNodePort is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) HealthCheckNodePort(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:128`



---


[function] name: InternalPolicyLocal file: pkg/proxy/serviceport.go:153 returns_error: нет description: InternalPolicyLocal is part of ServicePort interface


### InternalPolicyLocal (pkg/proxy/serviceport.go:153)


InternalPolicyLocal is part of ServicePort interface


```go
func (bsvcPortInfo *BaseServicePortInfo) InternalPolicyLocal(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:153`



---


[function] name: LoadBalancerSourceRanges file: pkg/proxy/serviceport.go:123 returns_error: нет description: LoadBalancerSourceRanges is part of ServicePort interface


### LoadBalancerSourceRanges (pkg/proxy/serviceport.go:123)


LoadBalancerSourceRanges is part of ServicePort interface


```go
func (bsvcPortInfo *BaseServicePortInfo) LoadBalancerSourceRanges(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:123`



---


[function] name: LoadBalancerVIPs file: pkg/proxy/serviceport.go:143 returns_error: нет description: LoadBalancerVIPs is part of ServicePort interface.


### LoadBalancerVIPs (pkg/proxy/serviceport.go:143)


LoadBalancerVIPs is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) LoadBalancerVIPs(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:143`



---


[function] name: NodePort file: pkg/proxy/serviceport.go:133 returns_error: нет description: NodePort is part of the ServicePort interface.


### NodePort (pkg/proxy/serviceport.go:133)


NodePort is part of the ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) NodePort(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:133`



---


[function] name: Port file: pkg/proxy/serviceport.go:103 returns_error: нет description: Port is part of ServicePort interface.


### Port (pkg/proxy/serviceport.go:103)


Port is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) Port(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:103`



---


[function] name: Protocol file: pkg/proxy/serviceport.go:118 returns_error: нет description: Protocol is part of ServicePort interface.


### Protocol (pkg/proxy/serviceport.go:118)


Protocol is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) Protocol(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:118`



---


[function] name: SessionAffinityType file: pkg/proxy/serviceport.go:108 returns_error: нет description: SessionAffinityType is part of the ServicePort interface.


### SessionAffinityType (pkg/proxy/serviceport.go:108)


SessionAffinityType is part of the ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) SessionAffinityType(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:108`



---


[function] name: StickyMaxAgeSeconds file: pkg/proxy/serviceport.go:113 returns_error: нет description: StickyMaxAgeSeconds is part of the ServicePort interface


### StickyMaxAgeSeconds (pkg/proxy/serviceport.go:113)


StickyMaxAgeSeconds is part of the ServicePort interface


```go
func (bsvcPortInfo *BaseServicePortInfo) StickyMaxAgeSeconds(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:113`



---


[function] name: String file: pkg/proxy/serviceport.go:93 returns_error: нет description: String is part of ServicePort interface.


### String (pkg/proxy/serviceport.go:93)


String is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) String(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:93`



---


[function] name: UsesClusterEndpoints file: pkg/proxy/serviceport.go:163 returns_error: нет description: UsesClusterEndpoints is part of ServicePort interface.


### UsesClusterEndpoints (pkg/proxy/serviceport.go:163)


UsesClusterEndpoints is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) UsesClusterEndpoints(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:163`



---


[function] name: UsesLocalEndpoints file: pkg/proxy/serviceport.go:171 returns_error: нет description: UsesLocalEndpoints is part of ServicePort interface.


### UsesLocalEndpoints (pkg/proxy/serviceport.go:171)


UsesLocalEndpoints is part of ServicePort interface.


```go
func (bsvcPortInfo *BaseServicePortInfo) UsesLocalEndpoints(()) ()
```


📍 *Расположение:* `pkg/proxy/serviceport.go:171`



---


[function] name: newBaseServiceInfo file: pkg/proxy/serviceport.go:175 returns_error: нет description: —


### newBaseServiceInfo (pkg/proxy/serviceport.go:175)


newBaseServiceInfo is a function that performs operations based on the provided parameters and returns (service *v1.Service, ipFamily v1.IPFamily, port *v1.ServicePort).


```go
func newBaseServiceInfo((service *v1.Service, ipFamily v1.IPFamily, port *v1.ServicePort)) (service *v1.Service, ipFamily v1.IPFamily, port *v1.ServicePort)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


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


**Тип ответа:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/serviceport.go:175`




## pkg/proxy/topology.go


📄 Исходный файл: `pkg/proxy/topology.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [CategorizeEndpoints](#categorizeendpoints-pkgproxytopologygo48) `:48`

- 🔗 [availableForTopology](#availablefortopology-pkgproxytopologygo223) `:223`

- 🔗 [filterEndpoints](#filterendpoints-pkgproxytopologygo237) `:237`

- 🔗 [topologyModeFromHints](#topologymodefromhints-pkgproxytopologygo164) `:164`


</details>


[function] name: CategorizeEndpoints file: pkg/proxy/topology.go:48 returns_error: нет description: CategorizeEndpoints returns:

- The service's usable Cluster-traffic-policy endpoints (taking topology into account, if



### CategorizeEndpoints (pkg/proxy/topology.go:48)


CategorizeEndpoints returns:

- The service's usable Cluster-traffic-policy endpoints (taking topology into account, if
relevant). This will be nil if the service does not ever use Cluster traffic policy.

- The service's usable Local-traffic-policy endpoints. This will be nil if the
service does not ever use Local traffic policy.

- The combined list of all endpoints reachable from this node (which is the union of the
previous two lists, but in the case where it is identical to one or the other, we avoid
allocating a separate list).

- An indication of whether the service has any endpoints reachable from anywhere in the
cluster. (This may be true even if allReachableEndpoints is empty.)

"Usable endpoints" means Ready endpoints by default, but will fall back to
Serving-Terminating endpoints (independently for Cluster and Local) if no Ready
endpoints are available.

Note: NodeTopologyConfig.handleNodeEvent (pkg/proxy/config) filters topology labels
before notifying proxiers. If you modify the logic over here to  watch other endpoint
types or labels, ensure the filtering logic in NodeTopologyConfig is updated accordingly.


```go
func CategorizeEndpoints((clusterEndpoints, localEndpoints, allReachableEndpoints []Endpoint, hasAnyEndpoints bool)) (clusterEndpoints, localEndpoints, allReachableEndpoints []Endpoint, hasAnyEndpoints bool)
```


**Тип ответа:** clusterEndpoints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** localEndpoints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** allReachableEndpoints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** hasAnyEndpoints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/topology.go:48`



---


[function] name: availableForTopology file: pkg/proxy/topology.go:223 returns_error: нет description: availableForTopology checks if this endpoint is available for use on this node when
using the given topologyMode. (Note 


### availableForTopology (pkg/proxy/topology.go:223)


availableForTopology checks if this endpoint is available for use on this node when
using the given topologyMode. (Note that there's no fallback here; the fallback happens
when deciding which mode to use, not when applying that decision.)


```go
func availableForTopology((endpoint Endpoint, topologyMode, nodeName, zone string)) (endpoint Endpoint, topologyMode, nodeName, zone string)
```


**Тип ответа:** endpoint


```json
{
  "URL": "string",
  "AccessToken": "string",
  "JWT": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


**Тип ответа:** Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** topologyMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** zone


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/topology.go:223`



---


[function] name: filterEndpoints file: pkg/proxy/topology.go:237 returns_error: нет description: filterEndpoints filters endpoints according to predicate


### filterEndpoints (pkg/proxy/topology.go:237)


filterEndpoints filters endpoints according to predicate


```go
func filterEndpoints((endpoints []Endpoint, predicate func(Endpoint) bool)) (endpoints []Endpoint, predicate func(Endpoint) bool)
```


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** predicate


```json
{
  "getNodeAnyWayFunc": {},
  "pluginResourceUpdateFunc": {},
  "admissionFailureHandler": {}
}
```


*Определено в:* `pkg/kubelet/lifecycle/predicate.go`


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/topology.go:237`



---


[function] name: topologyModeFromHints file: pkg/proxy/topology.go:164 returns_error: нет description: topologyModeFromHints returns a topology mode ("", "PreferSameZone", or
"PreferSameNode") based on the Endpoint hints:
-


### topologyModeFromHints (pkg/proxy/topology.go:164)


topologyModeFromHints returns a topology mode ("", "PreferSameZone", or
"PreferSameNode") based on the Endpoint hints:
- If the PreferSameTrafficDistribution feature gate is enabled, and every ready
endpoint has a node hint, and at least one endpoint is hinted for this node, then
it returns "PreferSameNode".
- Otherwise, if every ready endpoint has a zone hint, and at least one endpoint is
hinted for this node's zone, then it returns "PreferSameZone".
- Otherwise it returns "" (meaning, no topology / default traffic distribution).


```go
func topologyModeFromHints((svcInfo ServicePort, endpoints []Endpoint, nodeName, zone string)) (svcInfo ServicePort, endpoints []Endpoint, nodeName, zone string)
```


**Тип ответа:** svcInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** zone


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/topology.go:164`




## pkg/proxy/types.go


📄 Исходный файл: `pkg/proxy/types.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [String](#string-pkgproxytypesgo50) `:50`

- 🔗 [fmtPortName](#fmtportname-pkgproxytypesgo54) `:54`


</details>


[function] name: String file: pkg/proxy/types.go:50 returns_error: нет description: —


### String (pkg/proxy/types.go:50)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (spn ServicePortName) String(()) ()
```


📍 *Расположение:* `pkg/proxy/types.go:50`



---


[function] name: fmtPortName file: pkg/proxy/types.go:54 returns_error: нет description: —


### fmtPortName (pkg/proxy/types.go:54)


fmtPortName is a function that performs operations based on the provided parameters and returns (in string).


```go
func fmtPortName((in string)) (in string)
```


**Тип ответа:** in


```json
{
  "columns": [],
  "headerIsPrinted": false
}
```


*Определено в:* `cmd/kubeadm/app/cmd/token.go`


📍 *Расположение:* `pkg/proxy/types.go:54`




## pkg/proxy/util/endpoints.go


📄 Исходный файл: `pkg/proxy/util/endpoints.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [IPPart](#ippart-pkgproxyutilendpointsgo29) `:29`


</details>


[function] name: IPPart file: pkg/proxy/util/endpoints.go:29 returns_error: нет description: IPPart returns just the IP part of an IP or IP:port or endpoint string. If the IP
part is an IPv6 address enclosed in br


### IPPart (pkg/proxy/util/endpoints.go:29)


IPPart returns just the IP part of an IP or IP:port or endpoint string. If the IP
part is an IPv6 address enclosed in brackets (e.g. "[fd00:1::5]:9999"),
then the brackets are stripped as well.


```go
func IPPart((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `pkg/proxy/util/endpoints.go:29`




## pkg/proxy/util/linebuffer.go


📄 Исходный файл: `pkg/proxy/util/linebuffer.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [Bytes](#bytes-pkgproxyutillinebuffergo102) `:102`

- 🔗 [Bytes](#bytes-pkgproxyutillinebuffergo148) `:148`

- 🔗 [Lines](#lines-pkgproxyutillinebuffergo112) `:112`

- 🔗 [Lines](#lines-pkgproxyutillinebuffergo158) `:158`

- 🔗 [MarshalLog](#marshallog-pkgproxyutillinebuffergo117) `:117`

- 🔗 [NewDiscardLineBuffer](#newdiscardlinebuffer-pkgproxyutillinebuffergo128) `:128`

- 🔗 [NewLineBuffer](#newlinebuffer-pkgproxyutillinebuffergo60) `:60`

- 🔗 [Reset](#reset-pkgproxyutillinebuffergo96) `:96`

- 🔗 [Reset](#reset-pkgproxyutillinebuffergo143) `:143`

- 🔗 [String](#string-pkgproxyutillinebuffergo107) `:107`

- 🔗 [String](#string-pkgproxyutillinebuffergo153) `:153`

- 🔗 [Write](#write-pkgproxyutillinebuffergo65) `:65`

- 🔗 [Write](#write-pkgproxyutillinebuffergo133) `:133`

- 🔗 [WriteBytes](#writebytes-pkgproxyutillinebuffergo89) `:89`

- 🔗 [WriteBytes](#writebytes-pkgproxyutillinebuffergo138) `:138`


</details>


[function] name: Bytes file: pkg/proxy/util/linebuffer.go:102 returns_error: нет description: Bytes is part of LineBuffer


### Bytes (pkg/proxy/util/linebuffer.go:102)


Bytes is part of LineBuffer


```go
func (buf *realLineBuffer) Bytes(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:102`



---


[function] name: Bytes file: pkg/proxy/util/linebuffer.go:148 returns_error: нет description: Bytes is part of LineBuffer


### Bytes (pkg/proxy/util/linebuffer.go:148)


Bytes is part of LineBuffer


```go
func (buf *discardLineBuffer) Bytes(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:148`



---


[function] name: Lines file: pkg/proxy/util/linebuffer.go:112 returns_error: нет description: Lines is part of LineBuffer


### Lines (pkg/proxy/util/linebuffer.go:112)


Lines is part of LineBuffer


```go
func (buf *realLineBuffer) Lines(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:112`



---


[function] name: Lines file: pkg/proxy/util/linebuffer.go:158 returns_error: нет description: Lines is part of LineBuffer


### Lines (pkg/proxy/util/linebuffer.go:158)


Lines is part of LineBuffer


```go
func (buf *discardLineBuffer) Lines(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:158`



---


[function] name: MarshalLog file: pkg/proxy/util/linebuffer.go:117 returns_error: нет description: Implements the logs.Marshaler interface


### MarshalLog (pkg/proxy/util/linebuffer.go:117)


Implements the logs.Marshaler interface


```go
func (buf *realLineBuffer) MarshalLog(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:117`



---


[function] name: NewDiscardLineBuffer file: pkg/proxy/util/linebuffer.go:128 returns_error: нет description: NewDiscardLineBuffer returns a dummy LineBuffer that counts the number of writes but
throws away the data. (This is used


### NewDiscardLineBuffer (pkg/proxy/util/linebuffer.go:128)


NewDiscardLineBuffer returns a dummy LineBuffer that counts the number of writes but
throws away the data. (This is used for iptables proxy partial syncs, to keep track of
how many rules we managed to avoid having to sync.)


```go
func NewDiscardLineBuffer(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:128`



---


[function] name: NewLineBuffer file: pkg/proxy/util/linebuffer.go:60 returns_error: нет description: NewLineBuffer returns a new "real" LineBuffer


### NewLineBuffer (pkg/proxy/util/linebuffer.go:60)


NewLineBuffer returns a new "real" LineBuffer


```go
func NewLineBuffer(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:60`



---


[function] name: Reset file: pkg/proxy/util/linebuffer.go:96 returns_error: нет description: Reset is part of LineBuffer


### Reset (pkg/proxy/util/linebuffer.go:96)


Reset is part of LineBuffer


```go
func (buf *realLineBuffer) Reset(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:96`



---


[function] name: Reset file: pkg/proxy/util/linebuffer.go:143 returns_error: нет description: Reset is part of LineBuffer


### Reset (pkg/proxy/util/linebuffer.go:143)


Reset is part of LineBuffer


```go
func (buf *discardLineBuffer) Reset(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:143`



---


[function] name: String file: pkg/proxy/util/linebuffer.go:107 returns_error: нет description: String is part of LineBuffer


### String (pkg/proxy/util/linebuffer.go:107)


String is part of LineBuffer


```go
func (buf *realLineBuffer) String(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:107`



---


[function] name: String file: pkg/proxy/util/linebuffer.go:153 returns_error: нет description: String is part of LineBuffer


### String (pkg/proxy/util/linebuffer.go:153)


String is part of LineBuffer


```go
func (buf *discardLineBuffer) String(()) ()
```


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:153`



---


[function] name: Write file: pkg/proxy/util/linebuffer.go:65 returns_error: нет description: Write is part of LineBuffer


### Write (pkg/proxy/util/linebuffer.go:65)


Write is part of LineBuffer


```go
func (buf *realLineBuffer) Write((args ...interface{})) (args ...interface{})
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:65`



---


[function] name: Write file: pkg/proxy/util/linebuffer.go:133 returns_error: нет description: Write is part of LineBuffer


### Write (pkg/proxy/util/linebuffer.go:133)


Write is part of LineBuffer


```go
func (buf *discardLineBuffer) Write((args ...interface{})) (args ...interface{})
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:133`



---


[function] name: WriteBytes file: pkg/proxy/util/linebuffer.go:89 returns_error: нет description: WriteBytes is part of LineBuffer


### WriteBytes (pkg/proxy/util/linebuffer.go:89)


WriteBytes is part of LineBuffer


```go
func (buf *realLineBuffer) WriteBytes((bytes []byte)) (bytes []byte)
```


**Тип ответа:** bytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:89`



---


[function] name: WriteBytes file: pkg/proxy/util/linebuffer.go:138 returns_error: нет description: WriteBytes is part of LineBuffer


### WriteBytes (pkg/proxy/util/linebuffer.go:138)


WriteBytes is part of LineBuffer


```go
func (buf *discardLineBuffer) WriteBytes((bytes []byte)) (bytes []byte)
```


**Тип ответа:** bytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/linebuffer.go:138`




## pkg/proxy/util/localdetector.go


📄 Исходный файл: `pkg/proxy/util/localdetector.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [IfLocal](#iflocal-pkgproxyutillocaldetectorgo56) `:56`

- 🔗 [IfLocalNFT](#iflocalnft-pkgproxyutillocaldetectorgo64) `:64`

- 🔗 [IfNotLocal](#ifnotlocal-pkgproxyutillocaldetectorgo60) `:60`

- 🔗 [IfNotLocalNFT](#ifnotlocalnft-pkgproxyutillocaldetectorgo68) `:68`

- 🔗 [IsImplemented](#isimplemented-pkgproxyutillocaldetectorgo52) `:52`

- 🔗 [NewDetectLocalByBridgeInterface](#newdetectlocalbybridgeinterface-pkgproxyutillocaldetectorgo97) `:97`

- 🔗 [NewDetectLocalByCIDR](#newdetectlocalbycidr-pkgproxyutillocaldetectorgo80) `:80`

- 🔗 [NewDetectLocalByInterfaceNamePrefix](#newdetectlocalbyinterfacenameprefix-pkgproxyutillocaldetectorgo109) `:109`

- 🔗 [NewNoOpLocalDetector](#newnooplocaldetector-pkgproxyutillocaldetectorgo73) `:73`


</details>


[function] name: IfLocal file: pkg/proxy/util/localdetector.go:56 returns_error: нет description: —


### IfLocal (pkg/proxy/util/localdetector.go:56)


IfLocal is a method that performs operations based on the provided parameters and returns ().


```go
func (d *detectLocal) IfLocal(()) ()
```


📍 *Расположение:* `pkg/proxy/util/localdetector.go:56`



---


[function] name: IfLocalNFT file: pkg/proxy/util/localdetector.go:64 returns_error: нет description: —


### IfLocalNFT (pkg/proxy/util/localdetector.go:64)


IfLocalNFT is a method that performs operations based on the provided parameters and returns ().


```go
func (d *detectLocal) IfLocalNFT(()) ()
```


📍 *Расположение:* `pkg/proxy/util/localdetector.go:64`



---


[function] name: IfNotLocal file: pkg/proxy/util/localdetector.go:60 returns_error: нет description: —


### IfNotLocal (pkg/proxy/util/localdetector.go:60)


IfNotLocal is a method that performs operations based on the provided parameters and returns ().


```go
func (d *detectLocal) IfNotLocal(()) ()
```


📍 *Расположение:* `pkg/proxy/util/localdetector.go:60`



---


[function] name: IfNotLocalNFT file: pkg/proxy/util/localdetector.go:68 returns_error: нет description: —


### IfNotLocalNFT (pkg/proxy/util/localdetector.go:68)


IfNotLocalNFT is a method that performs operations based on the provided parameters and returns ().


```go
func (d *detectLocal) IfNotLocalNFT(()) ()
```


📍 *Расположение:* `pkg/proxy/util/localdetector.go:68`



---


[function] name: IsImplemented file: pkg/proxy/util/localdetector.go:52 returns_error: нет description: —


### IsImplemented (pkg/proxy/util/localdetector.go:52)


IsImplemented is a method that performs operations based on the provided parameters and returns ().


```go
func (d *detectLocal) IsImplemented(()) ()
```


📍 *Расположение:* `pkg/proxy/util/localdetector.go:52`



---


[function] name: NewDetectLocalByBridgeInterface file: pkg/proxy/util/localdetector.go:97 returns_error: нет description: NewDetectLocalByBridgeInterface returns a LocalTrafficDetector that considers traffic
from interfaceName to be from a lo


### NewDetectLocalByBridgeInterface (pkg/proxy/util/localdetector.go:97)


NewDetectLocalByBridgeInterface returns a LocalTrafficDetector that considers traffic
from interfaceName to be from a local pod, and traffic from other interfaces to be
non-local.


```go
func NewDetectLocalByBridgeInterface((interfaceName string)) (interfaceName string)
```


**Тип ответа:** interfaceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/localdetector.go:97`



---


[function] name: NewDetectLocalByCIDR file: pkg/proxy/util/localdetector.go:80 returns_error: нет description: NewDetectLocalByCIDR returns a LocalTrafficDetector that considers traffic from the
provided cidr to be from a local pod


### NewDetectLocalByCIDR (pkg/proxy/util/localdetector.go:80)


NewDetectLocalByCIDR returns a LocalTrafficDetector that considers traffic from the
provided cidr to be from a local pod, and other traffic to be non-local. cidr is
assumed to be valid.


```go
func NewDetectLocalByCIDR((cidr string)) (cidr string)
```


**Тип ответа:** cidr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/localdetector.go:80`



---


[function] name: NewDetectLocalByInterfaceNamePrefix file: pkg/proxy/util/localdetector.go:109 returns_error: нет description: NewDetectLocalByInterfaceNamePrefix returns a LocalTrafficDetector that considers
traffic from interfaces starting with 


### NewDetectLocalByInterfaceNamePrefix (pkg/proxy/util/localdetector.go:109)


NewDetectLocalByInterfaceNamePrefix returns a LocalTrafficDetector that considers
traffic from interfaces starting with interfacePrefix to be from a local pod, and
traffic from other interfaces to be non-local.


```go
func NewDetectLocalByInterfaceNamePrefix((interfacePrefix string)) (interfacePrefix string)
```


**Тип ответа:** interfacePrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/localdetector.go:109`



---


[function] name: NewNoOpLocalDetector file: pkg/proxy/util/localdetector.go:73 returns_error: нет description: NewNoOpLocalDetector returns a no-op implementation of LocalTrafficDetector.


### NewNoOpLocalDetector (pkg/proxy/util/localdetector.go:73)


NewNoOpLocalDetector returns a no-op implementation of LocalTrafficDetector.


```go
func NewNoOpLocalDetector(()) ()
```


📍 *Расположение:* `pkg/proxy/util/localdetector.go:73`




## pkg/proxy/util/network.go


📄 Исходный файл: `pkg/proxy/util/network.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [InterfaceAddrs](#interfaceaddrs-pkgproxyutilnetworkgo35) `:35`


</details>


[function] name: InterfaceAddrs file: pkg/proxy/util/network.go:35 returns_error: да description: InterfaceAddrs wraps net.InterfaceAddrs(), it's a part of NetworkInterfacer interface.


### InterfaceAddrs (pkg/proxy/util/network.go:35)


InterfaceAddrs wraps net.InterfaceAddrs(), it's a part of NetworkInterfacer interface.


```go
func (RealNetwork) InterfaceAddrs(([]net.Addr, error)) ([]net.Addr, error)
```


**Тип ответа:** net.Addr


```json
{
  "Namespace": "string",
  "Port": 0
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]net.Addr`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/network.go:35`




## pkg/proxy/util/nfacct/handler.go


📄 Исходный файл: `pkg/proxy/util/nfacct/handler.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [newNetlinkHandler](#newnetlinkhandler-pkgproxyutilnfaccthandlergo48) `:48`

- 🔗 [newRequest](#newrequest-pkgproxyutilnfaccthandlergo59) `:59`


</details>


[function] name: newNetlinkHandler file: pkg/proxy/util/nfacct/handler.go:48 returns_error: да description: newNetlinkHandler initializes a netlink socket in the current network namespace and returns
an instance of netlinkHandle


### newNetlinkHandler (pkg/proxy/util/nfacct/handler.go:48)


newNetlinkHandler initializes a netlink socket in the current network namespace and returns
an instance of netlinkHandler with the initialized socket.


```go
func newNetlinkHandler((handler, error)) (handler, error)
```


**Тип ответа:** handler


```json
{
  "tosvc": {},
  "fromsvc": {},
  "acceptPreshutdown": false,
  "preshutdownHandler": {}
}
```


*Определено в:* `pkg/windows/service/service.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `handler`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/nfacct/handler.go:48`



---


[function] name: newRequest file: pkg/proxy/util/nfacct/handler.go:59 returns_error: нет description: newRequest creates a netlink request tailored for the NFAcct subsystem encapsulating the
specified cmd and flags. It inc


### newRequest (pkg/proxy/util/nfacct/handler.go:59)


newRequest creates a netlink request tailored for the NFAcct subsystem encapsulating the
specified cmd and flags. It incorporates the netlink header and netfilter generic header
into the resulting request.


```go
func (n *netlinkHandler) newRequest((cmd int, flags uint16)) (cmd int, flags uint16)
```


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


**Тип ответа:** flags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/nfacct/handler.go:59`




## pkg/proxy/util/nfacct/nfacct_linux.go


📄 Исходный файл: `pkg/proxy/util/nfacct/nfacct_linux.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [Add](#add-pkgproxyutilnfacctnfacct_linuxgo109) `:109`

- 🔗 [Ensure](#ensure-pkgproxyutilnfacctnfacct_linuxgo93) `:93`

- 🔗 [Get](#get-pkgproxyutilnfacctnfacct_linuxgo127) `:127`

- 🔗 [List](#list-pkgproxyutilnfacctnfacct_linuxgo150) `:150`

- 🔗 [New](#new-pkgproxyutilnfacctnfacct_linuxgo66) `:66`

- 🔗 [decode](#decode-pkgproxyutilnfacctnfacct_linuxgo243) `:243`

- 🔗 [handleError](#handleerror-pkgproxyutilnfacctnfacct_linuxgo181) `:181`

- 🔗 [newInternal](#newinternal-pkgproxyutilnfacctnfacct_linuxgo87) `:87`


</details>


[function] name: Add file: pkg/proxy/util/nfacct/nfacct_linux.go:109 returns_error: нет description: Add is part of the interface.


### Add (pkg/proxy/util/nfacct/nfacct_linux.go:109)


Add is part of the interface.


```go
func (r *runner) Add((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_linux.go:109`



---


[function] name: Ensure file: pkg/proxy/util/nfacct/nfacct_linux.go:93 returns_error: нет description: Ensure is part of the interface.


### Ensure (pkg/proxy/util/nfacct/nfacct_linux.go:93)


Ensure is part of the interface.


```go
func (r *runner) Ensure((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_linux.go:93`



---


[function] name: Get file: pkg/proxy/util/nfacct/nfacct_linux.go:127 returns_error: да description: Get is part of the interface.


### Get (pkg/proxy/util/nfacct/nfacct_linux.go:127)


Get is part of the interface.


```go
func (r *runner) Get((*Counter, error)) (*Counter, error)
```


**Тип запроса:** Counter


```json
{
  "Name": "string",
  "Packets": 0,
  "Bytes": 0
}
```


*Определено в:* `pkg/proxy/util/nfacct/nfacct.go`


**Тип ответа:** Counter


```json
{
  "Name": "string",
  "Packets": 0,
  "Bytes": 0
}
```


*Определено в:* `pkg/proxy/util/nfacct/nfacct.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Counter`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_linux.go:127`



---


[function] name: List file: pkg/proxy/util/nfacct/nfacct_linux.go:150 returns_error: да description: List is part of the interface.


### List (pkg/proxy/util/nfacct/nfacct_linux.go:150)


List is part of the interface.


```go
func (r *runner) List(([]*Counter, error)) ([]*Counter, error)
```


**Тип запроса:** Counter


```json
{
  "Name": "string",
  "Packets": 0,
  "Bytes": 0
}
```


*Определено в:* `pkg/proxy/util/nfacct/nfacct.go`


**Тип ответа:** Counter


```json
{
  "Name": "string",
  "Packets": 0,
  "Bytes": 0
}
```


*Определено в:* `pkg/proxy/util/nfacct/nfacct.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]*Counter`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_linux.go:150`



---


[function] name: New file: pkg/proxy/util/nfacct/nfacct_linux.go:66 returns_error: да description: New returns a new Interface. If the netfilter_nfacct subsystem is
not available in the kernel it will return error.


### New (pkg/proxy/util/nfacct/nfacct_linux.go:66)


New returns a new Interface. If the netfilter_nfacct subsystem is
not available in the kernel it will return error.


```go
func New((Interface, error)) (Interface, error)
```


**Тип ответа:** Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Interface`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_linux.go:66`



---


[function] name: decode file: pkg/proxy/util/nfacct/nfacct_linux.go:243 returns_error: да description: decode function processes a byte stream, requiring the 'strict' parameter to be true in production and
false only for te


### decode (pkg/proxy/util/nfacct/nfacct_linux.go:243)


decode function processes a byte stream, requiring the 'strict' parameter to be true in production and
false only for testing purposes. If in strict mode and any of the relevant attributes (name, packets, or bytes)
have not been processed, an error is returned indicating a failure to decode the byte stream.

Parse the netlink message as per the documentation outlined in:
https://docs.kernel.org/userspace-api/netlink/intro.html

Message Components:
- netfilter generic message [4 bytes]
struct nfgenmsg (definition: https://github.com/torvalds/linux/blob/v6.7/include/uapi/linux/netfilter/nfnetlink.h#L32-L38)
- attributes [variable-sized, must align to 4 bytes from the start of attribute]
struct nlattr (definition: https://github.com/torvalds/linux/blob/v6.7/include/uapi/linux/netlink.h#L220-L232)

Attribute Components:
- length [2 bytes]
length includes bytes for defining the length itself, bytes for defining the type,
and the actual bytes of data without any padding.
- type [2 bytes]
- data [variable-sized]
- padding [optional]

Example. Counter{Name: "dummy-metric", Packets: 123, Bytes: 54321} in netlink message:

struct nfgenmsg{
__u8  nfgen_family: AF_NETLINK
__u8    version:    nl.NFNETLINK_V0
__be16  res_id:     nl.NFNETLINK_V0
}

struct nlattr{
__u16 nla_len:      13
__u16 nla_type:     NFACCT_NAME
char data:          dummy-metric\0
}

(padding:)
data:               \0\0\0

struct nlattr{
__u16 nla_len:      12
__u16 nla_type:     NFACCT_PKTS
__u64: data:        123
}

struct nlattr{
__u16 nla_len:      12
__u16 nla_type:     NFACCT_BYTES
__u64: data:        54321
}


```go
func decode((*Counter, error)) (*Counter, error)
```


**Тип запроса:** Counter


```json
{
  "Name": "string",
  "Packets": 0,
  "Bytes": 0
}
```


*Определено в:* `pkg/proxy/util/nfacct/nfacct.go`


**Тип ответа:** Counter


```json
{
  "Name": "string",
  "Packets": 0,
  "Bytes": 0
}
```


*Определено в:* `pkg/proxy/util/nfacct/nfacct.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Counter`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_linux.go:243`



---


[function] name: handleError file: pkg/proxy/util/nfacct/nfacct_linux.go:181 returns_error: да description: —


### handleError (pkg/proxy/util/nfacct/nfacct_linux.go:181)


handleError is a function that performs operations based on the provided parameters and may return an error.


```go
func handleError((err error)) (err error)
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


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_linux.go:181`



---


[function] name: newInternal file: pkg/proxy/util/nfacct/nfacct_linux.go:87 returns_error: да description: newInternal returns a new Interface with the given handler.


### newInternal (pkg/proxy/util/nfacct/nfacct_linux.go:87)


newInternal returns a new Interface with the given handler.


```go
func newInternal((Interface, error)) (Interface, error)
```


**Тип ответа:** Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Interface`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_linux.go:87`




## pkg/proxy/util/nfacct/nfacct_others.go


📄 Исходный файл: `pkg/proxy/util/nfacct/nfacct_others.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [New](#new-pkgproxyutilnfacctnfacct_othersgo28) `:28`


</details>


[function] name: New file: pkg/proxy/util/nfacct/nfacct_others.go:28 returns_error: да description: —


### New (pkg/proxy/util/nfacct/nfacct_others.go:28)


New is a function that performs operations based on the provided parameters and may return an error.


```go
func New((Interface, error)) (Interface, error)
```


**Тип ответа:** Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `Interface`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/nfacct/nfacct_others.go:28`




## pkg/proxy/util/nodeport_addresses.go


📄 Исходный файл: `pkg/proxy/util/nodeport_addresses.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [ContainsIPv4Loopback](#containsipv4loopback-pkgproxyutilnodeport_addressesgo132) `:132`

- 🔗 [GetNodeIPs](#getnodeips-pkgproxyutilnodeport_addressesgo96) `:96`

- 🔗 [MatchAll](#matchall-pkgproxyutilnodeport_addressesgo89) `:89`

- 🔗 [NewNodePortAddresses](#newnodeportaddresses-pkgproxyutilnodeport_addressesgo44) `:44`

- 🔗 [String](#string-pkgproxyutilnodeport_addressesgo84) `:84`


</details>


[function] name: ContainsIPv4Loopback file: pkg/proxy/util/nodeport_addresses.go:132 returns_error: нет description: ContainsIPv4Loopback returns true if npa's CIDRs contain an IPv4 loopback address.


### ContainsIPv4Loopback (pkg/proxy/util/nodeport_addresses.go:132)


ContainsIPv4Loopback returns true if npa's CIDRs contain an IPv4 loopback address.


```go
func (npa *NodePortAddresses) ContainsIPv4Loopback(()) ()
```


📍 *Расположение:* `pkg/proxy/util/nodeport_addresses.go:132`



---


[function] name: GetNodeIPs file: pkg/proxy/util/nodeport_addresses.go:96 returns_error: да description: GetNodeIPs return all matched node IP addresses for npa's CIDRs. If no matching
IPs are found, it returns an empty list.


### GetNodeIPs (pkg/proxy/util/nodeport_addresses.go:96)


GetNodeIPs return all matched node IP addresses for npa's CIDRs. If no matching
IPs are found, it returns an empty list.
NetworkInterfacer is injected for test purpose.


```go
func (npa *NodePortAddresses) GetNodeIPs(([]net.IP, error)) ([]net.IP, error)
```


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]net.IP`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/nodeport_addresses.go:96`



---


[function] name: MatchAll file: pkg/proxy/util/nodeport_addresses.go:89 returns_error: нет description: MatchAll returns true if npa matches all node IPs (of npa's given family)


### MatchAll (pkg/proxy/util/nodeport_addresses.go:89)


MatchAll returns true if npa matches all node IPs (of npa's given family)


```go
func (npa *NodePortAddresses) MatchAll(()) ()
```


📍 *Расположение:* `pkg/proxy/util/nodeport_addresses.go:89`



---


[function] name: NewNodePortAddresses file: pkg/proxy/util/nodeport_addresses.go:44 returns_error: нет description: NewNodePortAddresses takes an IP family and the `--nodeport-addresses` value (which is
assumed to contain only valid CID


### NewNodePortAddresses (pkg/proxy/util/nodeport_addresses.go:44)


NewNodePortAddresses takes an IP family and the `--nodeport-addresses` value (which is
assumed to contain only valid CIDRs, potentially of both IP families) and returns a
NodePortAddresses object for the given family. If there are no CIDRs of the given
family then the CIDR "0.0.0.0/0" or "::/0" will be added (even if there are CIDRs of
the other family).


```go
func NewNodePortAddresses((family v1.IPFamily, cidrStrings []string)) (family v1.IPFamily, cidrStrings []string)
```


**Тип ответа:** family


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cidrStrings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/nodeport_addresses.go:44`



---


[function] name: String file: pkg/proxy/util/nodeport_addresses.go:84 returns_error: нет description: —


### String (pkg/proxy/util/nodeport_addresses.go:84)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (npa *NodePortAddresses) String(()) ()
```


📍 *Расположение:* `pkg/proxy/util/nodeport_addresses.go:84`




## pkg/proxy/util/testing/fake.go


📄 Исходный файл: `pkg/proxy/util/testing/fake.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [AddInterfaceAddr](#addinterfaceaddr-pkgproxyutiltestingfakego37) `:37`

- 🔗 [InterfaceAddrs](#interfaceaddrs-pkgproxyutiltestingfakego43) `:43`

- 🔗 [NewFakeNetwork](#newfakenetwork-pkgproxyutiltestingfakego29) `:29`


</details>


[function] name: AddInterfaceAddr file: pkg/proxy/util/testing/fake.go:37 returns_error: нет description: AddInterfaceAddr create an interface and its associated addresses for FakeNetwork implementation.


### AddInterfaceAddr (pkg/proxy/util/testing/fake.go:37)


AddInterfaceAddr create an interface and its associated addresses for FakeNetwork implementation.


```go
func (f *FakeNetwork) AddInterfaceAddr((intf *net.Interface, addrs []net.Addr)) (intf *net.Interface, addrs []net.Addr)
```


**Тип запроса:** net.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** intf


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** addrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.Addr


```json
{
  "Namespace": "string",
  "Port": 0
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


📍 *Расположение:* `pkg/proxy/util/testing/fake.go:37`



---


[function] name: InterfaceAddrs file: pkg/proxy/util/testing/fake.go:43 returns_error: да description: InterfaceAddrs is part of NetworkInterfacer interface.


### InterfaceAddrs (pkg/proxy/util/testing/fake.go:43)


InterfaceAddrs is part of NetworkInterfacer interface.


```go
func (f *FakeNetwork) InterfaceAddrs(([]net.Addr, error)) ([]net.Addr, error)
```


**Тип ответа:** net.Addr


```json
{
  "Namespace": "string",
  "Port": 0
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]net.Addr`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/util/testing/fake.go:43`



---


[function] name: NewFakeNetwork file: pkg/proxy/util/testing/fake.go:29 returns_error: нет description: NewFakeNetwork initializes a FakeNetwork.


### NewFakeNetwork (pkg/proxy/util/testing/fake.go:29)


NewFakeNetwork initializes a FakeNetwork.


```go
func NewFakeNetwork(()) ()
```


📍 *Расположение:* `pkg/proxy/util/testing/fake.go:29`




## pkg/proxy/util/utils.go


📄 Исходный файл: `pkg/proxy/util/utils.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [AddressSet](#addressset-pkgproxyutilutilsgo72) `:72`

- 🔗 [AppendPortIfNeeded](#appendportifneeded-pkgproxyutilutilsgo160) `:160`

- 🔗 [EnsureSysctl](#ensuresysctl-pkgproxyutilutilsgo177) `:177`

- 🔗 [GetClusterIPByFamily](#getclusteripbyfamily-pkgproxyutilutilsgo188) `:188`

- 🔗 [GetIPFamilyFromIP](#getipfamilyfromip-pkgproxyutilutilsgo133) `:133`

- 🔗 [IsVIPMode](#isvipmode-pkgproxyutilutilsgo214) `:214`

- 🔗 [IsZeroCIDR](#iszerocidr-pkgproxyutilutilsgo47) `:47`

- 🔗 [MapCIDRsByIPFamily](#mapcidrsbyipfamily-pkgproxyutilutilsgo113) `:113`

- 🔗 [MapIPsByIPFamily](#mapipsbyipfamily-pkgproxyutilutilsgo92) `:92`

- 🔗 [OtherIPFamily](#otheripfamily-pkgproxyutilutilsgo150) `:150`

- 🔗 [ShouldSkipService](#shouldskipservice-pkgproxyutilutilsgo56) `:56`

- 🔗 [convertToV1IPFamily](#converttov1ipfamily-pkgproxyutilutilsgo138) `:138`


</details>


[function] name: AddressSet file: pkg/proxy/util/utils.go:72 returns_error: нет description: AddressSet validates the addresses in the slice using the "isValid" function.
Addresses that pass the validation are ret


### AddressSet (pkg/proxy/util/utils.go:72)


AddressSet validates the addresses in the slice using the "isValid" function.
Addresses that pass the validation are returned as a string Set.


```go
func AddressSet((isValid func(ip net.IP) bool, addrs []net.Addr)) (isValid func(ip net.IP) bool, addrs []net.Addr)
```


**Тип ответа:** isValid


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** addrs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.Addr


```json
{
  "Namespace": "string",
  "Port": 0
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


📍 *Расположение:* `pkg/proxy/util/utils.go:72`



---


[function] name: AppendPortIfNeeded file: pkg/proxy/util/utils.go:160 returns_error: нет description: AppendPortIfNeeded appends the given port to IP address unless it is already in
"ipv4:port" or "[ipv6]:port" format.


### AppendPortIfNeeded (pkg/proxy/util/utils.go:160)


AppendPortIfNeeded appends the given port to IP address unless it is already in
"ipv4:port" or "[ipv6]:port" format.


```go
func AppendPortIfNeeded((addr string, port int32)) (addr string, port int32)
```


**Тип ответа:** addr


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


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


📍 *Расположение:* `pkg/proxy/util/utils.go:160`



---


[function] name: EnsureSysctl file: pkg/proxy/util/utils.go:177 returns_error: нет description: EnsureSysctl sets a kernel sysctl to a given numeric value.


### EnsureSysctl (pkg/proxy/util/utils.go:177)


EnsureSysctl sets a kernel sysctl to a given numeric value.


```go
func EnsureSysctl((sysctl utilsysctl.Interface, name string, newVal int)) (sysctl utilsysctl.Interface, name string, newVal int)
```


**Тип ответа:** sysctl


```json
{
  "name": "string",
  "kernel": "string"
}
```


*Определено в:* `pkg/kubelet/sysctl/safe_sysctls.go`


**Тип ответа:** utilsysctl.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** newVal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/utils.go:177`



---


[function] name: GetClusterIPByFamily file: pkg/proxy/util/utils.go:188 returns_error: нет description: GetClusterIPByFamily returns a service clusterip by family


### GetClusterIPByFamily (pkg/proxy/util/utils.go:188)


GetClusterIPByFamily returns a service clusterip by family


```go
func GetClusterIPByFamily((ipFamily v1.IPFamily, service *v1.Service)) (ipFamily v1.IPFamily, service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/util/utils.go:188`



---


[function] name: GetIPFamilyFromIP file: pkg/proxy/util/utils.go:133 returns_error: нет description: GetIPFamilyFromIP Returns the IP family of ipStr, or IPFamilyUnknown if ipStr can't be parsed as an IP


### GetIPFamilyFromIP (pkg/proxy/util/utils.go:133)


GetIPFamilyFromIP Returns the IP family of ipStr, or IPFamilyUnknown if ipStr can't be parsed as an IP


```go
func GetIPFamilyFromIP((ip net.IP)) (ip net.IP)
```


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `pkg/proxy/util/utils.go:133`



---


[function] name: IsVIPMode file: pkg/proxy/util/utils.go:214 returns_error: нет description: —


### IsVIPMode (pkg/proxy/util/utils.go:214)


IsVIPMode is a function that performs operations based on the provided parameters and returns (ing v1.LoadBalancerIngress).


```go
func IsVIPMode((ing v1.LoadBalancerIngress)) (ing v1.LoadBalancerIngress)
```


**Тип ответа:** ing


```json
{
  "ID": "string",
  "Secret": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/bootstraptoken/v1/types.go`


**Тип ответа:** v1.LoadBalancerIngress


```json
{
  "IP": "string",
  "Hostname": "string",
  "IPMode": null,
  "Ports": []
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/util/utils.go:214`



---


[function] name: IsZeroCIDR file: pkg/proxy/util/utils.go:47 returns_error: нет description: IsZeroCIDR checks whether the input CIDR string is either
the IPv4 or IPv6 zero CIDR


### IsZeroCIDR (pkg/proxy/util/utils.go:47)


IsZeroCIDR checks whether the input CIDR string is either
the IPv4 or IPv6 zero CIDR


```go
func IsZeroCIDR((cidr *net.IPNet)) (cidr *net.IPNet)
```


**Тип запроса:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cidr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** net.IPNet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/utils.go:47`



---


[function] name: MapCIDRsByIPFamily file: pkg/proxy/util/utils.go:113 returns_error: нет description: MapCIDRsByIPFamily maps a slice of CIDRs to their respective IP families (v4 or v6)


### MapCIDRsByIPFamily (pkg/proxy/util/utils.go:113)


MapCIDRsByIPFamily maps a slice of CIDRs to their respective IP families (v4 or v6)


```go
func MapCIDRsByIPFamily((cidrsStrings []string)) (cidrsStrings []string)
```


**Тип ответа:** cidrsStrings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/utils.go:113`



---


[function] name: MapIPsByIPFamily file: pkg/proxy/util/utils.go:92 returns_error: нет description: MapIPsByIPFamily maps a slice of IPs to their respective IP families (v4 or v6)


### MapIPsByIPFamily (pkg/proxy/util/utils.go:92)


MapIPsByIPFamily maps a slice of IPs to their respective IP families (v4 or v6)


```go
func MapIPsByIPFamily((ipStrings []string)) (ipStrings []string)
```


**Тип ответа:** ipStrings


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/utils.go:92`



---


[function] name: OtherIPFamily file: pkg/proxy/util/utils.go:150 returns_error: нет description: OtherIPFamily returns the other ip family


### OtherIPFamily (pkg/proxy/util/utils.go:150)


OtherIPFamily returns the other ip family


```go
func OtherIPFamily((ipFamily v1.IPFamily)) (ipFamily v1.IPFamily)
```


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/utils.go:150`



---


[function] name: ShouldSkipService file: pkg/proxy/util/utils.go:56 returns_error: нет description: ShouldSkipService checks if a given service should skip proxying


### ShouldSkipService (pkg/proxy/util/utils.go:56)


ShouldSkipService checks if a given service should skip proxying


```go
func ShouldSkipService((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/util/utils.go:56`



---


[function] name: convertToV1IPFamily file: pkg/proxy/util/utils.go:138 returns_error: нет description: Convert netutils.IPFamily to v1.IPFamily


### convertToV1IPFamily (pkg/proxy/util/utils.go:138)


Convert netutils.IPFamily to v1.IPFamily


```go
func convertToV1IPFamily((ipFamily netutils.IPFamily)) (ipFamily netutils.IPFamily)
```


**Тип ответа:** ipFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** netutils.IPFamily


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/util/utils.go:138`




## pkg/proxy/winkernel/hcnutils.go


📄 Исходный файл: `pkg/proxy/winkernel/hcnutils.go`


<details open>
<summary><b>Функции в этом файле (20)</b></summary>


- 🔗 [CreateEndpoint](#createendpoint-pkgproxywinkernelhcnutilsgo84) `:84`

- 🔗 [CreateLoadBalancer](#createloadbalancer-pkgproxywinkernelhcnutilsgo104) `:104`

- 🔗 [CreateRemoteEndpoint](#createremoteendpoint-pkgproxywinkernelhcnutilsgo88) `:88`

- 🔗 [DeleteAllHnsLoadBalancerPolicy](#deleteallhnsloadbalancerpolicy-pkgproxywinkernelhcnutilsgo128) `:128`

- 🔗 [DeleteEndpoint](#deleteendpoint-pkgproxywinkernelhcnutilsgo92) `:92`

- 🔗 [DeleteLoadBalancer](#deleteloadbalancer-pkgproxywinkernelhcnutilsgo112) `:112`

- 🔗 [DsrSupported](#dsrsupported-pkgproxywinkernelhcnutilsgo124) `:124`

- 🔗 [GetEndpointByID](#getendpointbyid-pkgproxywinkernelhcnutilsgo76) `:76`

- 🔗 [GetEndpointByName](#getendpointbyname-pkgproxywinkernelhcnutilsgo80) `:80`

- 🔗 [GetLoadBalancerByID](#getloadbalancerbyid-pkgproxywinkernelhcnutilsgo100) `:100`

- 🔗 [GetNetworkByID](#getnetworkbyid-pkgproxywinkernelhcnutilsgo64) `:64`

- 🔗 [GetNetworkByName](#getnetworkbyname-pkgproxywinkernelhcnutilsgo60) `:60`

- 🔗 [GetSupportedFeatures](#getsupportedfeatures-pkgproxywinkernelhcnutilsgo116) `:116`

- 🔗 [Ipv6DualStackSupported](#ipv6dualstacksupported-pkgproxywinkernelhcnutilsgo120) `:120`

- 🔗 [ListEndpoints](#listendpoints-pkgproxywinkernelhcnutilsgo68) `:68`

- 🔗 [ListEndpointsOfNetwork](#listendpointsofnetwork-pkgproxywinkernelhcnutilsgo72) `:72`

- 🔗 [ListLoadBalancers](#listloadbalancers-pkgproxywinkernelhcnutilsgo96) `:96`

- 🔗 [RemoteSubnetSupported](#remotesubnetsupported-pkgproxywinkernelhcnutilsgo143) `:143`

- 🔗 [UpdateLoadBalancer](#updateloadbalancer-pkgproxywinkernelhcnutilsgo108) `:108`

- 🔗 [newHcnImpl](#newhcnimpl-pkgproxywinkernelhcnutilsgo56) `:56`


</details>


[function] name: CreateEndpoint file: pkg/proxy/winkernel/hcnutils.go:84 returns_error: да description: —


### CreateEndpoint (pkg/proxy/winkernel/hcnutils.go:84)


CreateEndpoint is a method that creates new data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) CreateEndpoint((*hcn.HostComputeEndpoint, error)) (*hcn.HostComputeEndpoint, error)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:84`



---


[function] name: CreateLoadBalancer file: pkg/proxy/winkernel/hcnutils.go:104 returns_error: да description: —


### CreateLoadBalancer (pkg/proxy/winkernel/hcnutils.go:104)


CreateLoadBalancer is a method that creates new data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) CreateLoadBalancer((*hcn.HostComputeLoadBalancer, error)) (*hcn.HostComputeLoadBalancer, error)
```


**Тип запроса:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeLoadBalancer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:104`



---


[function] name: CreateRemoteEndpoint file: pkg/proxy/winkernel/hcnutils.go:88 returns_error: да description: —


### CreateRemoteEndpoint (pkg/proxy/winkernel/hcnutils.go:88)


CreateRemoteEndpoint is a method that creates new data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) CreateRemoteEndpoint((*hcn.HostComputeEndpoint, error)) (*hcn.HostComputeEndpoint, error)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:88`



---


[function] name: DeleteAllHnsLoadBalancerPolicy file: pkg/proxy/winkernel/hcnutils.go:128 returns_error: нет description: —


### DeleteAllHnsLoadBalancerPolicy (pkg/proxy/winkernel/hcnutils.go:128)


DeleteAllHnsLoadBalancerPolicy is a method that deletes data based on the provided parameters and returns ().


```go
func (hcnObj hcnImpl) DeleteAllHnsLoadBalancerPolicy(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:128`



---


[function] name: DeleteEndpoint file: pkg/proxy/winkernel/hcnutils.go:92 returns_error: нет description: —


### DeleteEndpoint (pkg/proxy/winkernel/hcnutils.go:92)


DeleteEndpoint is a method that deletes data based on the provided parameters and returns (endpoint *hcn.HostComputeEndpoint).


```go
func (hcnObj hcnImpl) DeleteEndpoint((endpoint *hcn.HostComputeEndpoint)) (endpoint *hcn.HostComputeEndpoint)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpoint


```json
{
  "URL": "string",
  "AccessToken": "string",
  "JWT": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:92`



---


[function] name: DeleteLoadBalancer file: pkg/proxy/winkernel/hcnutils.go:112 returns_error: нет description: —


### DeleteLoadBalancer (pkg/proxy/winkernel/hcnutils.go:112)


DeleteLoadBalancer is a method that deletes data based on the provided parameters and returns (loadBalancer *hcn.HostComputeLoadBalancer).


```go
func (hcnObj hcnImpl) DeleteLoadBalancer((loadBalancer *hcn.HostComputeLoadBalancer)) (loadBalancer *hcn.HostComputeLoadBalancer)
```


**Тип запроса:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** loadBalancer


```json
{
  "ip": "string",
  "hnsID": "string",
  "healthCheckHnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:112`



---


[function] name: DsrSupported file: pkg/proxy/winkernel/hcnutils.go:124 returns_error: нет description: —


### DsrSupported (pkg/proxy/winkernel/hcnutils.go:124)


DsrSupported is a method that performs operations based on the provided parameters and returns ().


```go
func (hcnObj hcnImpl) DsrSupported(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:124`



---


[function] name: GetEndpointByID file: pkg/proxy/winkernel/hcnutils.go:76 returns_error: да description: —


### GetEndpointByID (pkg/proxy/winkernel/hcnutils.go:76)


GetEndpointByID is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) GetEndpointByID((*hcn.HostComputeEndpoint, error)) (*hcn.HostComputeEndpoint, error)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:76`



---


[function] name: GetEndpointByName file: pkg/proxy/winkernel/hcnutils.go:80 returns_error: да description: —


### GetEndpointByName (pkg/proxy/winkernel/hcnutils.go:80)


GetEndpointByName is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) GetEndpointByName((*hcn.HostComputeEndpoint, error)) (*hcn.HostComputeEndpoint, error)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:80`



---


[function] name: GetLoadBalancerByID file: pkg/proxy/winkernel/hcnutils.go:100 returns_error: да description: —


### GetLoadBalancerByID (pkg/proxy/winkernel/hcnutils.go:100)


GetLoadBalancerByID is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) GetLoadBalancerByID((*hcn.HostComputeLoadBalancer, error)) (*hcn.HostComputeLoadBalancer, error)
```


**Тип запроса:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeLoadBalancer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:100`



---


[function] name: GetNetworkByID file: pkg/proxy/winkernel/hcnutils.go:64 returns_error: да description: —


### GetNetworkByID (pkg/proxy/winkernel/hcnutils.go:64)


GetNetworkByID is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) GetNetworkByID((*hcn.HostComputeNetwork, error)) (*hcn.HostComputeNetwork, error)
```


**Тип запроса:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeNetwork`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:64`



---


[function] name: GetNetworkByName file: pkg/proxy/winkernel/hcnutils.go:60 returns_error: да description: —


### GetNetworkByName (pkg/proxy/winkernel/hcnutils.go:60)


GetNetworkByName is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) GetNetworkByName((*hcn.HostComputeNetwork, error)) (*hcn.HostComputeNetwork, error)
```


**Тип запроса:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeNetwork`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:60`



---


[function] name: GetSupportedFeatures file: pkg/proxy/winkernel/hcnutils.go:116 returns_error: нет description: —


### GetSupportedFeatures (pkg/proxy/winkernel/hcnutils.go:116)


GetSupportedFeatures is a method that retrieves data based on the provided parameters and returns ().


```go
func (hcnObj hcnImpl) GetSupportedFeatures(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:116`



---


[function] name: Ipv6DualStackSupported file: pkg/proxy/winkernel/hcnutils.go:120 returns_error: нет description: —


### Ipv6DualStackSupported (pkg/proxy/winkernel/hcnutils.go:120)


Ipv6DualStackSupported is a method that performs operations based on the provided parameters and returns ().


```go
func (hcnObj hcnImpl) Ipv6DualStackSupported(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:120`



---


[function] name: ListEndpoints file: pkg/proxy/winkernel/hcnutils.go:68 returns_error: да description: —


### ListEndpoints (pkg/proxy/winkernel/hcnutils.go:68)


ListEndpoints is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) ListEndpoints(([]hcn.HostComputeEndpoint, error)) ([]hcn.HostComputeEndpoint, error)
```


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:68`



---


[function] name: ListEndpointsOfNetwork file: pkg/proxy/winkernel/hcnutils.go:72 returns_error: да description: —


### ListEndpointsOfNetwork (pkg/proxy/winkernel/hcnutils.go:72)


ListEndpointsOfNetwork is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) ListEndpointsOfNetwork(([]hcn.HostComputeEndpoint, error)) ([]hcn.HostComputeEndpoint, error)
```


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:72`



---


[function] name: ListLoadBalancers file: pkg/proxy/winkernel/hcnutils.go:96 returns_error: да description: —


### ListLoadBalancers (pkg/proxy/winkernel/hcnutils.go:96)


ListLoadBalancers is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) ListLoadBalancers(([]hcn.HostComputeLoadBalancer, error)) ([]hcn.HostComputeLoadBalancer, error)
```


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]hcn.HostComputeLoadBalancer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:96`



---


[function] name: RemoteSubnetSupported file: pkg/proxy/winkernel/hcnutils.go:143 returns_error: нет description: —


### RemoteSubnetSupported (pkg/proxy/winkernel/hcnutils.go:143)


RemoteSubnetSupported is a method that performs operations based on the provided parameters and returns ().


```go
func (hcnObj hcnImpl) RemoteSubnetSupported(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:143`



---


[function] name: UpdateLoadBalancer file: pkg/proxy/winkernel/hcnutils.go:108 returns_error: да description: —


### UpdateLoadBalancer (pkg/proxy/winkernel/hcnutils.go:108)


UpdateLoadBalancer is a method that updates data based on the provided parameters and may return an error.


```go
func (hcnObj hcnImpl) UpdateLoadBalancer((*hcn.HostComputeLoadBalancer, error)) (*hcn.HostComputeLoadBalancer, error)
```


**Тип запроса:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeLoadBalancer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:108`



---


[function] name: newHcnImpl file: pkg/proxy/winkernel/hcnutils.go:56 returns_error: нет description: —


### newHcnImpl (pkg/proxy/winkernel/hcnutils.go:56)


newHcnImpl is a function that performs operations based on the provided parameters and returns ().


```go
func newHcnImpl(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/hcnutils.go:56`




## pkg/proxy/winkernel/hns.go


📄 Исходный файл: `pkg/proxy/winkernel/hns.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [createEndpoint](#createendpoint-pkgproxywinkernelhnsgo236) `:236`

- 🔗 [deleteEndpoint](#deleteendpoint-pkgproxywinkernelhnsgo295) `:295`

- 🔗 [deleteLoadBalancer](#deleteloadbalancer-pkgproxywinkernelhnsgo522) `:522`

- 🔗 [findLoadBalancerID](#findloadbalancerid-pkgproxywinkernelhnsgo308) `:308`

- 🔗 [getAllEndpointsByNetwork](#getallendpointsbynetwork-pkgproxywinkernelhnsgo117) `:117`

- 🔗 [getAllLoadBalancers](#getallloadbalancers-pkgproxywinkernelhnsgo318) `:318`

- 🔗 [getEndpointByID](#getendpointbyid-pkgproxywinkernelhnsgo178) `:178`

- 🔗 [getEndpointByIpAddress](#getendpointbyipaddress-pkgproxywinkernelhnsgo191) `:191`

- 🔗 [getEndpointByName](#getendpointbyname-pkgproxywinkernelhnsgo223) `:223`

- 🔗 [getLoadBalancer](#getloadbalancer-pkgproxywinkernelhnsgo348) `:348`

- 🔗 [getLoadBalancerPolicyFlags](#getloadbalancerpolicyflags-pkgproxywinkernelhnsgo57) `:57`

- 🔗 [getNetworkByName](#getnetworkbyname-pkgproxywinkernelhnsgo84) `:84`

- 🔗 [hashEndpoints](#hashendpoints-pkgproxywinkernelhnsgo545) `:545`

- 🔗 [updateLoadBalancer](#updateloadbalancer-pkgproxywinkernelhnsgo444) `:444`

- 🔗 [xor](#xor-pkgproxywinkernelhnsgo572) `:572`


</details>


[function] name: createEndpoint file: pkg/proxy/winkernel/hns.go:236 returns_error: да description: —


### createEndpoint (pkg/proxy/winkernel/hns.go:236)


createEndpoint is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) createEndpoint((*endpointInfo, error)) (*endpointInfo, error)
```


**Тип запроса:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*endpointInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:236`



---


[function] name: deleteEndpoint file: pkg/proxy/winkernel/hns.go:295 returns_error: нет description: —


### deleteEndpoint (pkg/proxy/winkernel/hns.go:295)


deleteEndpoint is a method that performs operations based on the provided parameters and returns (hnsID string).


```go
func (hns hns) deleteEndpoint((hnsID string)) (hnsID string)
```


**Тип ответа:** hnsID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:295`



---


[function] name: deleteLoadBalancer file: pkg/proxy/winkernel/hns.go:522 returns_error: нет description: —


### deleteLoadBalancer (pkg/proxy/winkernel/hns.go:522)


deleteLoadBalancer is a method that performs operations based on the provided parameters and returns (hnsID string).


```go
func (hns hns) deleteLoadBalancer((hnsID string)) (hnsID string)
```


**Тип ответа:** hnsID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:522`



---


[function] name: findLoadBalancerID file: pkg/proxy/winkernel/hns.go:308 returns_error: да description: findLoadBalancerID will construct a id from the provided loadbalancer fields


### findLoadBalancerID (pkg/proxy/winkernel/hns.go:308)


findLoadBalancerID will construct a id from the provided loadbalancer fields


```go
func findLoadBalancerID((loadBalancerIdentifier, error)) (loadBalancerIdentifier, error)
```


**Тип ответа:** loadBalancerIdentifier


```json
{
  "protocol": 0,
  "internalPort": 0,
  "externalPort": 0,
  "vip": "string",
  "endpointsHash": {},
  "isIPv6": false
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `loadBalancerIdentifier`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:308`



---


[function] name: getAllEndpointsByNetwork file: pkg/proxy/winkernel/hns.go:117 returns_error: да description: —


### getAllEndpointsByNetwork (pkg/proxy/winkernel/hns.go:117)


getAllEndpointsByNetwork is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) getAllEndpointsByNetwork((map[string]*(endpointInfo), error)) (map[string]*(endpointInfo), error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]*(endpointInfo)`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:117`



---


[function] name: getAllLoadBalancers file: pkg/proxy/winkernel/hns.go:318 returns_error: да description: —


### getAllLoadBalancers (pkg/proxy/winkernel/hns.go:318)


getAllLoadBalancers is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) getAllLoadBalancers((map[loadBalancerIdentifier]*loadBalancerInfo, error)) (map[loadBalancerIdentifier]*loadBalancerInfo, error)
```


**Тип запроса:** loadBalancerInfo


```json
{
  "hnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** loadBalancerIdentifier


```json
{
  "protocol": 0,
  "internalPort": 0,
  "externalPort": 0,
  "vip": "string",
  "endpointsHash": {},
  "isIPv6": false
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** loadBalancerInfo


```json
{
  "hnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[loadBalancerIdentifier]*loadBalancerInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:318`



---


[function] name: getEndpointByID file: pkg/proxy/winkernel/hns.go:178 returns_error: да description: —


### getEndpointByID (pkg/proxy/winkernel/hns.go:178)


getEndpointByID is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) getEndpointByID((*endpointInfo, error)) (*endpointInfo, error)
```


**Тип запроса:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*endpointInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:178`



---


[function] name: getEndpointByIpAddress file: pkg/proxy/winkernel/hns.go:191 returns_error: да description: —


### getEndpointByIpAddress (pkg/proxy/winkernel/hns.go:191)


getEndpointByIpAddress is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) getEndpointByIpAddress((*endpointInfo, error)) (*endpointInfo, error)
```


**Тип запроса:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*endpointInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:191`



---


[function] name: getEndpointByName file: pkg/proxy/winkernel/hns.go:223 returns_error: да description: —


### getEndpointByName (pkg/proxy/winkernel/hns.go:223)


getEndpointByName is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) getEndpointByName((*endpointInfo, error)) (*endpointInfo, error)
```


**Тип запроса:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*endpointInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:223`



---


[function] name: getLoadBalancer file: pkg/proxy/winkernel/hns.go:348 returns_error: да description: —


### getLoadBalancer (pkg/proxy/winkernel/hns.go:348)


getLoadBalancer is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) getLoadBalancer((*loadBalancerInfo, error)) (*loadBalancerInfo, error)
```


**Тип запроса:** loadBalancerInfo


```json
{
  "hnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** loadBalancerInfo


```json
{
  "hnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*loadBalancerInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:348`



---


[function] name: getLoadBalancerPolicyFlags file: pkg/proxy/winkernel/hns.go:57 returns_error: нет description: —


### getLoadBalancerPolicyFlags (pkg/proxy/winkernel/hns.go:57)


getLoadBalancerPolicyFlags is a function that performs operations based on the provided parameters and returns (lbPortMappingFlags hcn.LoadBalancerPortMappingFlags, lbFlags hcn.LoadBalancerFlags).


```go
func getLoadBalancerPolicyFlags((lbPortMappingFlags hcn.LoadBalancerPortMappingFlags, lbFlags hcn.LoadBalancerFlags)) (lbPortMappingFlags hcn.LoadBalancerPortMappingFlags, lbFlags hcn.LoadBalancerFlags)
```


**Тип ответа:** lbPortMappingFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.LoadBalancerPortMappingFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lbFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.LoadBalancerFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:57`



---


[function] name: getNetworkByName file: pkg/proxy/winkernel/hns.go:84 returns_error: да description: —


### getNetworkByName (pkg/proxy/winkernel/hns.go:84)


getNetworkByName is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) getNetworkByName((*hnsNetworkInfo, error)) (*hnsNetworkInfo, error)
```


**Тип запроса:** hnsNetworkInfo


```json
{
  "name": "string",
  "id": "string",
  "networkType": "string",
  "remoteSubnets": []
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** hnsNetworkInfo


```json
{
  "name": "string",
  "id": "string",
  "networkType": "string",
  "remoteSubnets": []
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hnsNetworkInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:84`



---


[function] name: hashEndpoints file: pkg/proxy/winkernel/hns.go:545 returns_error: да description: Calculates a hash from the given endpoint IDs.


### hashEndpoints (pkg/proxy/winkernel/hns.go:545)


Calculates a hash from the given endpoint IDs.


```go
func hashEndpoints((hash [20]byte, err error)) (hash [20]byte, err error)
```


**Тип ответа:** hash


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


*Типы возврата:* `hash [20]byte`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:545`



---


[function] name: updateLoadBalancer file: pkg/proxy/winkernel/hns.go:444 returns_error: да description: —


### updateLoadBalancer (pkg/proxy/winkernel/hns.go:444)


updateLoadBalancer is a method that performs operations based on the provided parameters and may return an error.


```go
func (hns hns) updateLoadBalancer((*loadBalancerInfo, error)) (*loadBalancerInfo, error)
```


**Тип запроса:** loadBalancerInfo


```json
{
  "hnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** loadBalancerInfo


```json
{
  "hnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*loadBalancerInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:444`



---


[function] name: xor file: pkg/proxy/winkernel/hns.go:572 returns_error: нет description: —


### xor (pkg/proxy/winkernel/hns.go:572)


xor is a function that performs operations based on the provided parameters and returns (xorbytes [20]byte).


```go
func xor((xorbytes [20]byte)) (xorbytes [20]byte)
```


**Тип ответа:** xorbytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/hns.go:572`




## pkg/proxy/winkernel/proxier.go


📄 Исходный файл: `pkg/proxy/winkernel/proxier.go`


<details open>
<summary><b>Функции в этом файле (66)</b></summary>


- 🔗 [Cleanup](#cleanup-pkgproxywinkernelproxiergo472) `:472`

- 🔗 [CleanupLeftovers](#cleanupleftovers-pkgproxywinkernelproxiergo834) `:834`

- 🔗 [DecrementRefCount](#decrementrefcount-pkgproxywinkernelproxiergo460) `:460`

- 🔗 [Enum](#enum-pkgproxywinkernelproxiergo621) `:621`

- 🔗 [GetHostMac](#gethostmac-pkgproxywinkernelproxiergo1782) `:1782`

- 🔗 [IP](#ip-pkgproxywinkernelproxiergo294) `:294`

- 🔗 [IsLocal](#islocal-pkgproxywinkernelproxiergo264) `:264`

- 🔗 [IsReady](#isready-pkgproxywinkernelproxiergo269) `:269`

- 🔗 [IsServing](#isserving-pkgproxywinkernelproxiergo274) `:274`

- 🔗 [IsTerminating](#isterminating-pkgproxywinkernelproxiergo279) `:279`

- 🔗 [NewDualStackProxier](#newdualstackproxier-pkgproxywinkernelproxiergo800) `:800`

- 🔗 [NewProxier](#newproxier-pkgproxywinkernelproxiergo642) `:642`

- 🔗 [NodeHints](#nodehints-pkgproxywinkernelproxiergo289) `:289`

- 🔗 [OnEndpointSliceAdd](#onendpointsliceadd-pkgproxywinkernelproxiergo987) `:987`

- 🔗 [OnEndpointSliceDelete](#onendpointslicedelete-pkgproxywinkernelproxiergo1003) `:1003`

- 🔗 [OnEndpointSliceUpdate](#onendpointsliceupdate-pkgproxywinkernelproxiergo995) `:995`

- 🔗 [OnEndpointSlicesSynced](#onendpointslicessynced-pkgproxywinkernelproxiergo1011) `:1011`

- 🔗 [OnServiceAdd](#onserviceadd-pkgproxywinkernelproxiergo955) `:955`

- 🔗 [OnServiceCIDRsChanged](#onservicecidrschanged-pkgproxywinkernelproxiergo1023) `:1023`

- 🔗 [OnServiceDelete](#onservicedelete-pkgproxywinkernelproxiergo969) `:969`

- 🔗 [OnServiceSynced](#onservicesynced-pkgproxywinkernelproxiergo975) `:975`

- 🔗 [OnServiceUpdate](#onserviceupdate-pkgproxywinkernelproxiergo961) `:961`

- 🔗 [OnTopologyChange](#ontopologychange-pkgproxywinkernelproxiergo1030) `:1030`

- 🔗 [Port](#port-pkgproxywinkernelproxiergo299) `:299`

- 🔗 [String](#string-pkgproxywinkernelproxiergo63) `:63`

- 🔗 [String](#string-pkgproxywinkernelproxiergo73) `:73`

- 🔗 [String](#string-pkgproxywinkernelproxiergo84) `:84`

- 🔗 [String](#string-pkgproxywinkernelproxiergo97) `:97`

- 🔗 [String](#string-pkgproxywinkernelproxiergo129) `:129`

- 🔗 [String](#string-pkgproxywinkernelproxiergo259) `:259`

- 🔗 [String](#string-pkgproxywinkernelproxiergo617) `:617`

- 🔗 [Sync](#sync-pkgproxywinkernelproxiergo922) `:922`

- 🔗 [SyncLoop](#syncloop-pkgproxywinkernelproxiergo931) `:931`

- 🔗 [ZoneHints](#zonehints-pkgproxywinkernelproxiergo284) `:284`

- 🔗 [cleanupAllPolicies](#cleanupallpolicies-pkgproxywinkernelproxiergo843) `:843`

- 🔗 [cleanupAllPolicies](#cleanupallpolicies-pkgproxywinkernelproxiergo1032) `:1032`

- 🔗 [cleanupStaleLoadbalancers](#cleanupstaleloadbalancers-pkgproxywinkernelproxiergo193) `:193`

- 🔗 [conjureMac](#conjuremac-pkgproxywinkernelproxiergo307) `:307`

- 🔗 [deleteExistingLoadBalancer](#deleteexistingloadbalancer-pkgproxywinkernelproxiergo1739) `:1739`

- 🔗 [deleteLoadBalancer](#deleteloadbalancer-pkgproxywinkernelproxiergo1767) `:1767`

- 🔗 [deleteLoadBalancerPolicy](#deleteloadbalancerpolicy-pkgproxywinkernelproxiergo871) `:871`

- 🔗 [endpointsMapChange](#endpointsmapchange-pkgproxywinkernelproxiergo333) `:333`

- 🔗 [findRemoteSubnetProviderAddress](#findremotesubnetprovideraddress-pkgproxywinkernelproxiergo546) `:546`

- 🔗 [getNetworkInfo](#getnetworkinfo-pkgproxywinkernelproxiergo227) `:227`

- 🔗 [getNetworkName](#getnetworkname-pkgproxywinkernelproxiergo216) `:216`

- 🔗 [getRefCount](#getrefcount-pkgproxywinkernelproxiergo494) `:494`

- 🔗 [handleUpdateLoadbalancerFailure](#handleupdateloadbalancerfailure-pkgproxywinkernelproxiergo1112) `:1112`

- 🔗 [isAllEndpointsNonServing](#isallendpointsnonserving-pkgproxywinkernelproxiergo1083) `:1083`

- 🔗 [isAllEndpointsTerminating](#isallendpointsterminating-pkgproxywinkernelproxiergo1058) `:1058`

- 🔗 [isInitialized](#isinitialized-pkgproxywinkernelproxiergo949) `:949`

- 🔗 [isNetworkNotFoundError](#isnetworknotfounderror-pkgproxywinkernelproxiergo1043) `:1043`

- 🔗 [isOverlay](#isoverlay-pkgproxywinkernelproxiergo237) `:237`

- 🔗 [logFormattedEndpoints](#logformattedendpoints-pkgproxywinkernelproxiergo180) `:180`

- 🔗 [newEndpointInfo](#newendpointinfo-pkgproxywinkernelproxiergo426) `:426`

- 🔗 [newHostNetworkService](#newhostnetworkservice-pkgproxywinkernelproxiergo164) `:164`

- 🔗 [newProxierInternal](#newproxierinternal-pkgproxywinkernelproxiergo687) `:687`

- 🔗 [newServiceInfo](#newserviceinfo-pkgproxywinkernelproxiergo504) `:504`

- 🔗 [newSourceVIP](#newsourcevip-pkgproxywinkernelproxiergo445) `:445`

- 🔗 [onEndpointsMapChange](#onendpointsmapchange-pkgproxywinkernelproxiergo354) `:354`

- 🔗 [onServiceMapChange](#onservicemapchange-pkgproxywinkernelproxiergo408) `:408`

- 🔗 [requiresUpdateLoadbalancer](#requiresupdateloadbalancer-pkgproxywinkernelproxiergo1106) `:1106`

- 🔗 [serviceMapChange](#servicemapchange-pkgproxywinkernelproxiergo395) `:395`

- 🔗 [setInitialized](#setinitialized-pkgproxywinkernelproxiergo941) `:941`

- 🔗 [syncProxyRules](#syncproxyrules-pkgproxywinkernelproxiergo1127) `:1127`

- 🔗 [updateQueriedEndpoints](#updatequeriedendpoints-pkgproxywinkernelproxiergo1100) `:1100`

- 🔗 [updateTerminatedEndpoints](#updateterminatedendpoints-pkgproxywinkernelproxiergo321) `:321`


</details>


[function] name: Cleanup file: pkg/proxy/winkernel/proxier.go:472 returns_error: нет description: —


### Cleanup (pkg/proxy/winkernel/proxier.go:472)


Cleanup is a method that performs operations based on the provided parameters and returns ().


```go
func (ep *endpointInfo) Cleanup(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:472`



---


[function] name: CleanupLeftovers file: pkg/proxy/winkernel/proxier.go:834 returns_error: нет description: CleanupLeftovers removes all hns rules created by the Proxier
It returns true if an error was encountered. Errors are lo


### CleanupLeftovers (pkg/proxy/winkernel/proxier.go:834)


CleanupLeftovers removes all hns rules created by the Proxier
It returns true if an error was encountered. Errors are logged.


```go
func CleanupLeftovers((encounteredError bool)) (encounteredError bool)
```


**Тип ответа:** encounteredError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:834`



---


[function] name: DecrementRefCount file: pkg/proxy/winkernel/proxier.go:460 returns_error: нет description: —


### DecrementRefCount (pkg/proxy/winkernel/proxier.go:460)


DecrementRefCount is a method that performs operations based on the provided parameters and returns ().


```go
func (ep *endpointInfo) DecrementRefCount(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:460`



---


[function] name: Enum file: pkg/proxy/winkernel/proxier.go:621 returns_error: нет description: —


### Enum (pkg/proxy/winkernel/proxier.go:621)


Enum is a function that performs operations based on the provided parameters and returns (p v1.Protocol).


```go
func Enum((p v1.Protocol)) (p v1.Protocol)
```


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


**Тип ответа:** v1.Protocol


```json
{
  "errorStream": {},
  "remoteStdin": {},
  "remoteStdout": {},
  "remoteStderr": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/remotecommand/v1.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:621`



---


[function] name: GetHostMac file: pkg/proxy/winkernel/proxier.go:1782 returns_error: нет description: —


### GetHostMac (pkg/proxy/winkernel/proxier.go:1782)


GetHostMac is a method that retrieves data based on the provided parameters and returns (nodeIP net.IP).


```go
func (r *localHostMacProvider) GetHostMac((nodeIP net.IP)) (nodeIP net.IP)
```


**Тип ответа:** nodeIP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1782`



---


[function] name: IP file: pkg/proxy/winkernel/proxier.go:294 returns_error: нет description: IP returns just the IP part of the endpoint, it's a part of proxy.Endpoint interface.


### IP (pkg/proxy/winkernel/proxier.go:294)


IP returns just the IP part of the endpoint, it's a part of proxy.Endpoint interface.


```go
func (info *endpointInfo) IP(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:294`



---


[function] name: IsLocal file: pkg/proxy/winkernel/proxier.go:264 returns_error: нет description: IsLocal is part of proxy.Endpoint interface.


### IsLocal (pkg/proxy/winkernel/proxier.go:264)


IsLocal is part of proxy.Endpoint interface.


```go
func (info *endpointInfo) IsLocal(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:264`



---


[function] name: IsReady file: pkg/proxy/winkernel/proxier.go:269 returns_error: нет description: IsReady returns true if an endpoint is ready and not terminating.


### IsReady (pkg/proxy/winkernel/proxier.go:269)


IsReady returns true if an endpoint is ready and not terminating.


```go
func (info *endpointInfo) IsReady(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:269`



---


[function] name: IsServing file: pkg/proxy/winkernel/proxier.go:274 returns_error: нет description: IsServing returns true if an endpoint is ready, regardless of it's terminating state.


### IsServing (pkg/proxy/winkernel/proxier.go:274)


IsServing returns true if an endpoint is ready, regardless of it's terminating state.


```go
func (info *endpointInfo) IsServing(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:274`



---


[function] name: IsTerminating file: pkg/proxy/winkernel/proxier.go:279 returns_error: нет description: IsTerminating returns true if an endpoint is terminating.


### IsTerminating (pkg/proxy/winkernel/proxier.go:279)


IsTerminating returns true if an endpoint is terminating.


```go
func (info *endpointInfo) IsTerminating(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:279`



---


[function] name: NewDualStackProxier file: pkg/proxy/winkernel/proxier.go:800 returns_error: да description: —


### NewDualStackProxier (pkg/proxy/winkernel/proxier.go:800)


NewDualStackProxier is a function that performs operations based on the provided parameters and may return an error.


```go
func NewDualStackProxier((proxy.Provider, error)) (proxy.Provider, error)
```


**Тип ответа:** proxy.Provider


```json
{
  "cadvisor": {},
  "podManager": {}
}
```


*Определено в:* `pkg/kubelet/stats/provider.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `proxy.Provider`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:800`



---


[function] name: NewProxier file: pkg/proxy/winkernel/proxier.go:642 returns_error: да description: NewProxier returns a new single-stack winkernel proxier.


### NewProxier (pkg/proxy/winkernel/proxier.go:642)


NewProxier returns a new single-stack winkernel proxier.


```go
func NewProxier((*Proxier, error)) (*Proxier, error)
```


**Тип запроса:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Proxier`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:642`



---


[function] name: NodeHints file: pkg/proxy/winkernel/proxier.go:289 returns_error: нет description: NodeHints returns the node hints for the endpoint.


### NodeHints (pkg/proxy/winkernel/proxier.go:289)


NodeHints returns the node hints for the endpoint.


```go
func (info *endpointInfo) NodeHints(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:289`



---


[function] name: OnEndpointSliceAdd file: pkg/proxy/winkernel/proxier.go:987 returns_error: нет description: OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


### OnEndpointSliceAdd (pkg/proxy/winkernel/proxier.go:987)


OnEndpointSliceAdd is called whenever creation of a new endpoint slice object
is observed.


```go
func (proxier *Proxier) OnEndpointSliceAdd((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:987`



---


[function] name: OnEndpointSliceDelete file: pkg/proxy/winkernel/proxier.go:1003 returns_error: нет description: OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


### OnEndpointSliceDelete (pkg/proxy/winkernel/proxier.go:1003)


OnEndpointSliceDelete is called whenever deletion of an existing endpoint slice
object is observed.


```go
func (proxier *Proxier) OnEndpointSliceDelete((endpointSlice *discovery.EndpointSlice)) (endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1003`



---


[function] name: OnEndpointSliceUpdate file: pkg/proxy/winkernel/proxier.go:995 returns_error: нет description: OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


### OnEndpointSliceUpdate (pkg/proxy/winkernel/proxier.go:995)


OnEndpointSliceUpdate is called whenever modification of an existing endpoint
slice object is observed.


```go
func (proxier *Proxier) OnEndpointSliceUpdate((_, endpointSlice *discovery.EndpointSlice)) (_, endpointSlice *discovery.EndpointSlice)
```


**Тип запроса:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** endpointSlice


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/discovery/v1beta1/endpointslice.go`


**Тип ответа:** discovery.EndpointSlice


```json
{
  "AddressType": {},
  "Endpoints": [],
  "Ports": []
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:995`



---


[function] name: OnEndpointSlicesSynced file: pkg/proxy/winkernel/proxier.go:1011 returns_error: нет description: OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to lo


### OnEndpointSlicesSynced (pkg/proxy/winkernel/proxier.go:1011)


OnEndpointSlicesSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *Proxier) OnEndpointSlicesSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1011`



---


[function] name: OnServiceAdd file: pkg/proxy/winkernel/proxier.go:955 returns_error: нет description: OnServiceAdd is called whenever creation of new service object
is observed.


### OnServiceAdd (pkg/proxy/winkernel/proxier.go:955)


OnServiceAdd is called whenever creation of new service object
is observed.


```go
func (proxier *Proxier) OnServiceAdd((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:955`



---


[function] name: OnServiceCIDRsChanged file: pkg/proxy/winkernel/proxier.go:1023 returns_error: нет description: OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of 


### OnServiceCIDRsChanged (pkg/proxy/winkernel/proxier.go:1023)


OnServiceCIDRsChanged is called whenever a change is observed
in any of the ServiceCIDRs, and provides complete list of service cidrs.


```go
func (proxier *Proxier) OnServiceCIDRsChanged((_ []string)) (_ []string)
```


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1023`



---


[function] name: OnServiceDelete file: pkg/proxy/winkernel/proxier.go:969 returns_error: нет description: OnServiceDelete is called whenever deletion of an existing service
object is observed.


### OnServiceDelete (pkg/proxy/winkernel/proxier.go:969)


OnServiceDelete is called whenever deletion of an existing service
object is observed.


```go
func (proxier *Proxier) OnServiceDelete((service *v1.Service)) (service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:969`



---


[function] name: OnServiceSynced file: pkg/proxy/winkernel/proxier.go:975 returns_error: нет description: OnServiceSynced is called once all the initial event handlers were
called and the state is fully propagated to local cac


### OnServiceSynced (pkg/proxy/winkernel/proxier.go:975)


OnServiceSynced is called once all the initial event handlers were
called and the state is fully propagated to local cache.


```go
func (proxier *Proxier) OnServiceSynced(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:975`



---


[function] name: OnServiceUpdate file: pkg/proxy/winkernel/proxier.go:961 returns_error: нет description: OnServiceUpdate is called whenever modification of an existing
service object is observed.


### OnServiceUpdate (pkg/proxy/winkernel/proxier.go:961)


OnServiceUpdate is called whenever modification of an existing
service object is observed.


```go
func (proxier *Proxier) OnServiceUpdate((oldService, service *v1.Service)) (oldService, service *v1.Service)
```


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** oldService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:961`



---


[function] name: OnTopologyChange file: pkg/proxy/winkernel/proxier.go:1030 returns_error: нет description: TODO(imroc): implement OnTopologyChanged for winkernel proxier.
OnTopologyChange is called whenever node topology labels


### OnTopologyChange (pkg/proxy/winkernel/proxier.go:1030)


TODO(imroc): implement OnTopologyChanged for winkernel proxier.
OnTopologyChange is called whenever node topology labels are changed.
The informer is tweaked to listen for updates of the node where this
instance of kube-proxy is running, this guarantees the changed labels
are for this node.


```go
func (proxier *Proxier) OnTopologyChange((topologyLabels map[string]string)) (topologyLabels map[string]string)
```


**Тип ответа:** topologyLabels


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1030`



---


[function] name: Port file: pkg/proxy/winkernel/proxier.go:299 returns_error: нет description: Port returns just the Port part of the endpoint.


### Port (pkg/proxy/winkernel/proxier.go:299)


Port returns just the Port part of the endpoint.


```go
func (info *endpointInfo) Port(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:299`



---


[function] name: String file: pkg/proxy/winkernel/proxier.go:63 returns_error: нет description: —


### String (pkg/proxy/winkernel/proxier.go:63)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (info externalIPInfo) String(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:63`



---


[function] name: String file: pkg/proxy/winkernel/proxier.go:73 returns_error: нет description: —


### String (pkg/proxy/winkernel/proxier.go:73)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (info loadBalancerIngressInfo) String(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:73`



---


[function] name: String file: pkg/proxy/winkernel/proxier.go:84 returns_error: нет description: —


### String (pkg/proxy/winkernel/proxier.go:84)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (info loadBalancerInfo) String(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:84`



---


[function] name: String file: pkg/proxy/winkernel/proxier.go:97 returns_error: нет description: —


### String (pkg/proxy/winkernel/proxier.go:97)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (info loadBalancerIdentifier) String(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:97`



---


[function] name: String file: pkg/proxy/winkernel/proxier.go:129 returns_error: нет description: —


### String (pkg/proxy/winkernel/proxier.go:129)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (info serviceInfo) String(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:129`



---


[function] name: String file: pkg/proxy/winkernel/proxier.go:259 returns_error: нет description: String is part of proxy.Endpoint interface.


### String (pkg/proxy/winkernel/proxier.go:259)


String is part of proxy.Endpoint interface.


```go
func (info endpointInfo) String(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:259`



---


[function] name: String file: pkg/proxy/winkernel/proxier.go:617 returns_error: нет description: —


### String (pkg/proxy/winkernel/proxier.go:617)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (lp *localPort) String(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:617`



---


[function] name: Sync file: pkg/proxy/winkernel/proxier.go:922 returns_error: нет description: Sync is called to synchronize the proxier state to hns as soon as possible.


### Sync (pkg/proxy/winkernel/proxier.go:922)


Sync is called to synchronize the proxier state to hns as soon as possible.


```go
func (proxier *Proxier) Sync(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:922`



---


[function] name: SyncLoop file: pkg/proxy/winkernel/proxier.go:931 returns_error: нет description: SyncLoop runs periodic work.  This is expected to run as a goroutine or as the main loop of the app.  It does not return


### SyncLoop (pkg/proxy/winkernel/proxier.go:931)


SyncLoop runs periodic work.  This is expected to run as a goroutine or as the main loop of the app.  It does not return.


```go
func (proxier *Proxier) SyncLoop(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:931`



---


[function] name: ZoneHints file: pkg/proxy/winkernel/proxier.go:284 returns_error: нет description: ZoneHints returns the zone hints for the endpoint.


### ZoneHints (pkg/proxy/winkernel/proxier.go:284)


ZoneHints returns the zone hints for the endpoint.


```go
func (info *endpointInfo) ZoneHints(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:284`



---


[function] name: cleanupAllPolicies file: pkg/proxy/winkernel/proxier.go:843 returns_error: нет description: —


### cleanupAllPolicies (pkg/proxy/winkernel/proxier.go:843)


cleanupAllPolicies is a method that performs operations based on the provided parameters and returns (endpoints []proxy.Endpoint, mapStaleLoadbalancers map[string]bool, isEndpointChange bool).


```go
func (svcInfo *serviceInfo) cleanupAllPolicies((endpoints []proxy.Endpoint, mapStaleLoadbalancers map[string]bool, isEndpointChange bool)) (endpoints []proxy.Endpoint, mapStaleLoadbalancers map[string]bool, isEndpointChange bool)
```


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** proxy.Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** mapStaleLoadbalancers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** isEndpointChange


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:843`



---


[function] name: cleanupAllPolicies file: pkg/proxy/winkernel/proxier.go:1032 returns_error: нет description: —


### cleanupAllPolicies (pkg/proxy/winkernel/proxier.go:1032)


cleanupAllPolicies is a method that performs operations based on the provided parameters and returns ().


```go
func (proxier *Proxier) cleanupAllPolicies(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1032`



---


[function] name: cleanupStaleLoadbalancers file: pkg/proxy/winkernel/proxier.go:193 returns_error: нет description: This will cleanup stale load balancers which are pending delete
in last iteration. This function will act like a self he


### cleanupStaleLoadbalancers (pkg/proxy/winkernel/proxier.go:193)


This will cleanup stale load balancers which are pending delete
in last iteration. This function will act like a self healing of stale
loadbalancer entries.


```go
func (proxier *Proxier) cleanupStaleLoadbalancers(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:193`



---


[function] name: conjureMac file: pkg/proxy/winkernel/proxier.go:307 returns_error: нет description: Uses mac prefix and IPv4 address to return a mac address
This ensures mac addresses are unique for proper load balancing


### conjureMac (pkg/proxy/winkernel/proxier.go:307)


Uses mac prefix and IPv4 address to return a mac address
This ensures mac addresses are unique for proper load balancing
There is a possibility of MAC collisions but this Mac address is used for remote endpoints only
and not sent on the wire.


```go
func conjureMac((macPrefix string, ip net.IP)) (macPrefix string, ip net.IP)
```


**Тип ответа:** macPrefix


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:307`



---


[function] name: deleteExistingLoadBalancer file: pkg/proxy/winkernel/proxier.go:1739 returns_error: нет description: deleteExistingLoadBalancer checks whether loadbalancer delete is needed or not.
If it is needed, the function will delet


### deleteExistingLoadBalancer (pkg/proxy/winkernel/proxier.go:1739)


deleteExistingLoadBalancer checks whether loadbalancer delete is needed or not.
If it is needed, the function will delete the existing loadbalancer and return true, else false.


```go
func (proxier *Proxier) deleteExistingLoadBalancer((hns HostNetworkService, winProxyOptimization bool, lbHnsID *string, vip string, protocol, intPort, extPort uint16, endpoints []endpointInfo, queriedLoadBalancers map[loadBalancerIdentifier]*loadBalancerInfo)) (hns HostNetworkService, winProxyOptimization bool, lbHnsID *string, vip string, protocol, intPort, extPort uint16, endpoints []endpointInfo, queriedLoadBalancers map[loadBalancerIdentifier]*loadBalancerInfo)
```


**Тип запроса:** loadBalancerInfo


```json
{
  "hnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** hns


```json
{
  "hcn": {}
}
```


*Определено в:* `pkg/proxy/winkernel/hns.go`


**Тип ответа:** HostNetworkService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** winProxyOptimization


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lbHnsID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** vip


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** protocol


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** intPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/discovery/v1beta1/endpointport.go`


**Тип ответа:** extPort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpoints


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/endpoints.go`


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** queriedLoadBalancers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** loadBalancerIdentifier


```json
{
  "protocol": 0,
  "internalPort": 0,
  "externalPort": 0,
  "vip": "string",
  "endpointsHash": {},
  "isIPv6": false
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** loadBalancerInfo


```json
{
  "hnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1739`



---


[function] name: deleteLoadBalancer file: pkg/proxy/winkernel/proxier.go:1767 returns_error: нет description: —


### deleteLoadBalancer (pkg/proxy/winkernel/proxier.go:1767)


deleteLoadBalancer is a method that performs operations based on the provided parameters and returns (hns HostNetworkService, lbHnsID *string).


```go
func (proxier *Proxier) deleteLoadBalancer((hns HostNetworkService, lbHnsID *string)) (hns HostNetworkService, lbHnsID *string)
```


**Тип ответа:** hns


```json
{
  "hcn": {}
}
```


*Определено в:* `pkg/proxy/winkernel/hns.go`


**Тип ответа:** HostNetworkService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** lbHnsID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1767`



---


[function] name: deleteLoadBalancerPolicy file: pkg/proxy/winkernel/proxier.go:871 returns_error: нет description: —


### deleteLoadBalancerPolicy (pkg/proxy/winkernel/proxier.go:871)


deleteLoadBalancerPolicy is a method that performs operations based on the provided parameters and returns (mapStaleLoadbalancer map[string]bool).


```go
func (svcInfo *serviceInfo) deleteLoadBalancerPolicy((mapStaleLoadbalancer map[string]bool)) (mapStaleLoadbalancer map[string]bool)
```


**Тип ответа:** mapStaleLoadbalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:871`



---


[function] name: endpointsMapChange file: pkg/proxy/winkernel/proxier.go:333 returns_error: нет description: —


### endpointsMapChange (pkg/proxy/winkernel/proxier.go:333)


endpointsMapChange is a method that performs operations based on the provided parameters and returns (oldEndpointsMap, newEndpointsMap proxy.EndpointsMap).


```go
func (proxier *Proxier) endpointsMapChange((oldEndpointsMap, newEndpointsMap proxy.EndpointsMap)) (oldEndpointsMap, newEndpointsMap proxy.EndpointsMap)
```


**Тип ответа:** oldEndpointsMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newEndpointsMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.EndpointsMap


```json
{
  "UpdatedServices": {},
  "ConntrackCleanupRequired": false,
  "LastChangeTriggerTimes": {}
}
```


*Определено в:* `pkg/proxy/endpointschangetracker.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:333`



---


[function] name: findRemoteSubnetProviderAddress file: pkg/proxy/winkernel/proxier.go:546 returns_error: нет description: —


### findRemoteSubnetProviderAddress (pkg/proxy/winkernel/proxier.go:546)


findRemoteSubnetProviderAddress is a method that performs operations based on the provided parameters and returns (ip string).


```go
func (network hnsNetworkInfo) findRemoteSubnetProviderAddress((ip string)) (ip string)
```


**Тип ответа:** ip


```json
{
  "name": "string",
  "constructor": {},
  "requiredFeatureGates": [],
  "aliases": [],
  "isDisabledByDefault": false,
  "isCloudProviderController": false,
  "requiresSpecialHandling": false
}
```


*Определено в:* `cmd/kube-controller-manager/app/controller_descriptor.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:546`



---


[function] name: getNetworkInfo file: pkg/proxy/winkernel/proxier.go:227 returns_error: да description: —


### getNetworkInfo (pkg/proxy/winkernel/proxier.go:227)


getNetworkInfo is a function that performs operations based on the provided parameters and may return an error.


```go
func getNetworkInfo((*hnsNetworkInfo, error)) (*hnsNetworkInfo, error)
```


**Тип запроса:** hnsNetworkInfo


```json
{
  "name": "string",
  "id": "string",
  "networkType": "string",
  "remoteSubnets": []
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** hnsNetworkInfo


```json
{
  "name": "string",
  "id": "string",
  "networkType": "string",
  "remoteSubnets": []
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hnsNetworkInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:227`



---


[function] name: getNetworkName file: pkg/proxy/winkernel/proxier.go:216 returns_error: да description: —


### getNetworkName (pkg/proxy/winkernel/proxier.go:216)


getNetworkName is a function that performs operations based on the provided parameters and may return an error.


```go
func getNetworkName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:216`



---


[function] name: getRefCount file: pkg/proxy/winkernel/proxier.go:494 returns_error: нет description: —


### getRefCount (pkg/proxy/winkernel/proxier.go:494)


getRefCount is a method that performs operations based on the provided parameters and returns (hnsID string).


```go
func (refCountMap endPointsReferenceCountMap) getRefCount((hnsID string)) (hnsID string)
```


**Тип ответа:** hnsID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:494`



---


[function] name: handleUpdateLoadbalancerFailure file: pkg/proxy/winkernel/proxier.go:1112 returns_error: нет description: handleUpdateLoadbalancerFailure will handle the error returned by updatePolicy. If the error is due to unsupported featu


### handleUpdateLoadbalancerFailure (pkg/proxy/winkernel/proxier.go:1112)


handleUpdateLoadbalancerFailure will handle the error returned by updatePolicy. If the error is due to unsupported feature,
then it will set the supportedFeatures.ModifyLoadbalancer to false. return true means skip the iteration.


```go
func (proxier *Proxier) handleUpdateLoadbalancerFailure((skipIteration bool)) (skipIteration bool)
```


**Тип ответа:** skipIteration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1112`



---


[function] name: isAllEndpointsNonServing file: pkg/proxy/winkernel/proxier.go:1083 returns_error: нет description: isAllEndpointsNonServing function will return true if all the endpoints are non serving.
If atleast one is serving, then


### isAllEndpointsNonServing (pkg/proxy/winkernel/proxier.go:1083)


isAllEndpointsNonServing function will return true if all the endpoints are non serving.
If atleast one is serving, then return false


```go
func (proxier *Proxier) isAllEndpointsNonServing((svcName proxy.ServicePortName, isLocalTrafficDSR bool)) (svcName proxy.ServicePortName, isLocalTrafficDSR bool)
```


**Тип ответа:** svcName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** isLocalTrafficDSR


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1083`



---


[function] name: isAllEndpointsTerminating file: pkg/proxy/winkernel/proxier.go:1058 returns_error: нет description: isAllEndpointsTerminating function will return true if all the endpoints are terminating.
If atleast one is not terminat


### isAllEndpointsTerminating (pkg/proxy/winkernel/proxier.go:1058)


isAllEndpointsTerminating function will return true if all the endpoints are terminating.
If atleast one is not terminating, then return false


```go
func (proxier *Proxier) isAllEndpointsTerminating((svcName proxy.ServicePortName, isLocalTrafficDSR bool)) (svcName proxy.ServicePortName, isLocalTrafficDSR bool)
```


**Тип ответа:** svcName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** isLocalTrafficDSR


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1058`



---


[function] name: isInitialized file: pkg/proxy/winkernel/proxier.go:949 returns_error: нет description: —


### isInitialized (pkg/proxy/winkernel/proxier.go:949)


isInitialized is a method that performs operations based on the provided parameters and returns ().


```go
func (proxier *Proxier) isInitialized(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:949`



---


[function] name: isNetworkNotFoundError file: pkg/proxy/winkernel/proxier.go:1043 returns_error: да description: —


### isNetworkNotFoundError (pkg/proxy/winkernel/proxier.go:1043)


isNetworkNotFoundError is a function that performs operations based on the provided parameters and may return an error.


```go
func isNetworkNotFoundError((err error)) (err error)
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


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1043`



---


[function] name: isOverlay file: pkg/proxy/winkernel/proxier.go:237 returns_error: нет description: —


### isOverlay (pkg/proxy/winkernel/proxier.go:237)


isOverlay is a function that performs operations based on the provided parameters and returns (hnsNetworkInfo *hnsNetworkInfo).


```go
func isOverlay((hnsNetworkInfo *hnsNetworkInfo)) (hnsNetworkInfo *hnsNetworkInfo)
```


**Тип запроса:** hnsNetworkInfo


```json
{
  "name": "string",
  "id": "string",
  "networkType": "string",
  "remoteSubnets": []
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** hnsNetworkInfo


```json
{
  "name": "string",
  "id": "string",
  "networkType": "string",
  "remoteSubnets": []
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** hnsNetworkInfo


```json
{
  "name": "string",
  "id": "string",
  "networkType": "string",
  "remoteSubnets": []
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:237`



---


[function] name: logFormattedEndpoints file: pkg/proxy/winkernel/proxier.go:180 returns_error: нет description: logFormattedEndpoints will log all endpoints and its states which are taking part in endpointmap change.
This mostly for


### logFormattedEndpoints (pkg/proxy/winkernel/proxier.go:180)


logFormattedEndpoints will log all endpoints and its states which are taking part in endpointmap change.
This mostly for debugging purpose and verbosity is set to 5.


```go
func logFormattedEndpoints((logMsg string, logLevel klog.Level, svcPortName proxy.ServicePortName, eps []proxy.Endpoint)) (logMsg string, logLevel klog.Level, svcPortName proxy.ServicePortName, eps []proxy.Endpoint)
```


**Тип ответа:** logMsg


```json
{
  "info": {}
}
```


*Определено в:* `staging/src/k8s.io/component-base/logs/api/v1/text.go`


**Тип ответа:** logLevel


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** klog.Level


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/flowcontrol/v1beta1/prioritylevelconfiguration.go`


**Тип ответа:** svcPortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** eps


```json
{
  "steps": [],
  "currentStepIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/config/navigation_step_parser.go`


**Тип ответа:** proxy.Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:180`



---


[function] name: newEndpointInfo file: pkg/proxy/winkernel/proxier.go:426 returns_error: нет description: returns a new proxy.Endpoint which abstracts a endpointInfo


### newEndpointInfo (pkg/proxy/winkernel/proxier.go:426)


returns a new proxy.Endpoint which abstracts a endpointInfo


```go
func (proxier *Proxier) newEndpointInfo((baseInfo *proxy.BaseEndpointInfo, _ *proxy.ServicePortName)) (baseInfo *proxy.BaseEndpointInfo, _ *proxy.ServicePortName)
```


**Тип запроса:** proxy.BaseEndpointInfo


```json
{
  "ip": "string",
  "port": 0,
  "endpoint": "string",
  "isLocal": false,
  "ready": false,
  "serving": false,
  "terminating": false,
  "zoneHints": {},
  "nodeHints": {}
}
```


*Определено в:* `pkg/proxy/endpoint.go`


**Тип запроса:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** baseInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.BaseEndpointInfo


```json
{
  "ip": "string",
  "port": 0,
  "endpoint": "string",
  "isLocal": false,
  "ready": false,
  "serving": false,
  "terminating": false,
  "zoneHints": {},
  "nodeHints": {}
}
```


*Определено в:* `pkg/proxy/endpoint.go`


**Тип ответа:** _


```json
{
  "mock": null
}
```


*Определено в:* `test/utils/oidc/handlers/mocks.go`


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:426`



---


[function] name: newHostNetworkService file: pkg/proxy/winkernel/proxier.go:164 returns_error: нет description: —


### newHostNetworkService (pkg/proxy/winkernel/proxier.go:164)


newHostNetworkService is a function that performs operations based on the provided parameters and returns (HostNetworkService, hcn.SupportedFeatures).


```go
func newHostNetworkService((HostNetworkService, hcn.SupportedFeatures)) (HostNetworkService, hcn.SupportedFeatures)
```


**Тип ответа:** HostNetworkService


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.SupportedFeatures


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:164`



---


[function] name: newProxierInternal file: pkg/proxy/winkernel/proxier.go:687 returns_error: да description: allow internal testing of proxier


### newProxierInternal (pkg/proxy/winkernel/proxier.go:687)


allow internal testing of proxier


```go
func newProxierInternal((*Proxier, error)) (*Proxier, error)
```


**Тип запроса:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** Proxier


```json
{
  "ipFamily": {},
  "endpointsChanges": null,
  "serviceChanges": null,
  "endPointsRefCount": {},
  "mu": {},
  "svcPortMap": {},
  "endpointsMap": {},
  "endpointSlicesSynced": false,
  "servicesSynced": false,
  "initialized": 0,
  "syncRunner": null,
  "nodeName": "string",
  "nodeIP": {},
  "serviceHealthServer": {},
  "healthzServer": null,
  "hns": {},
  "hcn": {},
  "network": {},
  "sourceVip": "string",
  "hostMac": "string",
  "isDSR": false,
  "supportedFeatures": {},
  "healthzPort": 0,
  "forwardHealthCheckVip": false,
  "rootHnsEndpointName": "string",
  "mapStaleLoadbalancers": {},
  "terminatedEndpoints": {}
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*Proxier`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:687`



---


[function] name: newServiceInfo file: pkg/proxy/winkernel/proxier.go:504 returns_error: нет description: returns a new proxy.ServicePort which abstracts a serviceInfo


### newServiceInfo (pkg/proxy/winkernel/proxier.go:504)


returns a new proxy.ServicePort which abstracts a serviceInfo


```go
func (proxier *Proxier) newServiceInfo((port *v1.ServicePort, service *v1.Service, bsvcPortInfo *proxy.BaseServicePortInfo)) (port *v1.ServicePort, service *v1.Service, bsvcPortInfo *proxy.BaseServicePortInfo)
```


**Тип запроса:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип запроса:** proxy.BaseServicePortInfo


```json
{
  "clusterIP": {},
  "port": 0,
  "protocol": {},
  "nodePort": 0,
  "loadBalancerVIPs": [],
  "sessionAffinityType": {},
  "stickyMaxAgeSeconds": 0,
  "externalIPs": [],
  "loadBalancerSourceRanges": [],
  "healthCheckNodePort": 0,
  "externalPolicyLocal": false,
  "internalPolicyLocal": false
}
```


*Определено в:* `pkg/proxy/serviceport.go`


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


**Тип ответа:** v1.ServicePort


```json
{
  "Name": "string",
  "Protocol": {},
  "AppProtocol": "string",
  "Port": 0,
  "TargetPort": {},
  "NodePort": 0
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** service


```json
{
  "nodeID": "string",
  "vols": [],
  "volsRWL": {},
  "volsNID": {},
  "snapshots": {},
  "snapshotsNID": {},
  "config": {}
}
```


*Определено в:* `test/e2e/storage/drivers/csi-test/mock/service/service.go`


**Тип ответа:** v1.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** bsvcPortInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.BaseServicePortInfo


```json
{
  "clusterIP": {},
  "port": 0,
  "protocol": {},
  "nodePort": 0,
  "loadBalancerVIPs": [],
  "sessionAffinityType": {},
  "stickyMaxAgeSeconds": 0,
  "externalIPs": [],
  "loadBalancerSourceRanges": [],
  "healthCheckNodePort": 0,
  "externalPolicyLocal": false,
  "internalPolicyLocal": false
}
```


*Определено в:* `pkg/proxy/serviceport.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:504`



---


[function] name: newSourceVIP file: pkg/proxy/winkernel/proxier.go:445 returns_error: да description: —


### newSourceVIP (pkg/proxy/winkernel/proxier.go:445)


newSourceVIP is a function that performs operations based on the provided parameters and may return an error.


```go
func newSourceVIP((*endpointInfo, error)) (*endpointInfo, error)
```


**Тип запроса:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*endpointInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:445`



---


[function] name: onEndpointsMapChange file: pkg/proxy/winkernel/proxier.go:354 returns_error: нет description: —


### onEndpointsMapChange (pkg/proxy/winkernel/proxier.go:354)


onEndpointsMapChange is a method that performs operations based on the provided parameters and returns (svcPortName *proxy.ServicePortName, redundantCleanup bool).


```go
func (proxier *Proxier) onEndpointsMapChange((svcPortName *proxy.ServicePortName, redundantCleanup bool)) (svcPortName *proxy.ServicePortName, redundantCleanup bool)
```


**Тип запроса:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** svcPortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** redundantCleanup


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:354`



---


[function] name: onServiceMapChange file: pkg/proxy/winkernel/proxier.go:408 returns_error: нет description: —


### onServiceMapChange (pkg/proxy/winkernel/proxier.go:408)


onServiceMapChange is a method that performs operations based on the provided parameters and returns (svcPortName *proxy.ServicePortName).


```go
func (proxier *Proxier) onServiceMapChange((svcPortName *proxy.ServicePortName)) (svcPortName *proxy.ServicePortName)
```


**Тип запроса:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


**Тип ответа:** svcPortName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** proxy.ServicePortName


```json
{
  "Port": "string",
  "Protocol": {}
}
```


*Определено в:* `pkg/proxy/types.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:408`



---


[function] name: requiresUpdateLoadbalancer file: pkg/proxy/winkernel/proxier.go:1106 returns_error: нет description: —


### requiresUpdateLoadbalancer (pkg/proxy/winkernel/proxier.go:1106)


requiresUpdateLoadbalancer is a method that performs operations based on the provided parameters and returns (lbHnsID string, endpointCount int).


```go
func (proxier *Proxier) requiresUpdateLoadbalancer((lbHnsID string, endpointCount int)) (lbHnsID string, endpointCount int)
```


**Тип ответа:** lbHnsID


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointCount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1106`



---


[function] name: serviceMapChange file: pkg/proxy/winkernel/proxier.go:395 returns_error: нет description: —


### serviceMapChange (pkg/proxy/winkernel/proxier.go:395)


serviceMapChange is a method that performs operations based on the provided parameters and returns (previous, current proxy.ServicePortMap).


```go
func (proxier *Proxier) serviceMapChange((previous, current proxy.ServicePortMap)) (previous, current proxy.ServicePortMap)
```


**Тип ответа:** previous


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** current


```json
{
  "visitors": [],
  "concurrency": 0
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/visitor.go`


**Тип ответа:** proxy.ServicePortMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:395`



---


[function] name: setInitialized file: pkg/proxy/winkernel/proxier.go:941 returns_error: нет description: —


### setInitialized (pkg/proxy/winkernel/proxier.go:941)


setInitialized is a method that performs operations based on the provided parameters and returns (value bool).


```go
func (proxier *Proxier) setInitialized((value bool)) (value bool)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:941`



---


[function] name: syncProxyRules file: pkg/proxy/winkernel/proxier.go:1127 returns_error: да description: This is where all of the hns save/restore calls happen.
assumes proxier.mu is held


### syncProxyRules (pkg/proxy/winkernel/proxier.go:1127)


This is where all of the hns save/restore calls happen.
assumes proxier.mu is held


```go
func (proxier *Proxier) syncProxyRules((retryError error)) (retryError error)
```


**Тип ответа:** retryError


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `retryError error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1127`



---


[function] name: updateQueriedEndpoints file: pkg/proxy/winkernel/proxier.go:1100 returns_error: нет description: updateQueriedEndpoints updates the queriedEndpoints map with newly created endpoint details


### updateQueriedEndpoints (pkg/proxy/winkernel/proxier.go:1100)


updateQueriedEndpoints updates the queriedEndpoints map with newly created endpoint details


```go
func updateQueriedEndpoints((newHnsEndpoint *endpointInfo, queriedEndpoints map[string]*endpointInfo)) (newHnsEndpoint *endpointInfo, queriedEndpoints map[string]*endpointInfo)
```


**Тип запроса:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип запроса:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** newHnsEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


**Тип ответа:** queriedEndpoints


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** endpointInfo


```json
{
  "e": {},
  "opts": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/manager.go`


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:1100`



---


[function] name: updateTerminatedEndpoints file: pkg/proxy/winkernel/proxier.go:321 returns_error: нет description: This will keep the track of all terminated endpoints.
This is done by adding the endpoints from old endpoint map and rem


### updateTerminatedEndpoints (pkg/proxy/winkernel/proxier.go:321)


This will keep the track of all terminated endpoints.
This is done by adding the endpoints from old endpoint map and removing the endpoints from new endpoint map.
This way, we have entries which are only present in old endpoint map and not in new endpoint map.


```go
func (proxier *Proxier) updateTerminatedEndpoints((eps []proxy.Endpoint, isOldEndpointsMap bool)) (eps []proxy.Endpoint, isOldEndpointsMap bool)
```


**Тип ответа:** eps


```json
{
  "steps": [],
  "currentStepIndex": 0
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/config/navigation_step_parser.go`


**Тип ответа:** proxy.Endpoint


```json
{
  "Addresses": [],
  "Conditions": {},
  "Hostname": "string",
  "TargetRef": null,
  "DeprecatedTopology": {},
  "NodeName": "string",
  "Zone": "string",
  "Hints": null
}
```


*Определено в:* `pkg/apis/discovery/types.go`


**Тип ответа:** isOldEndpointsMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/proxier.go:321`




## pkg/proxy/winkernel/supported.go


📄 Исходный файл: `pkg/proxy/winkernel/supported.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [CanUseWinKernelProxier](#canusewinkernelproxier-pkgproxywinkernelsupportedgo40) `:40`

- 🔗 [DualStackCompatible](#dualstackcompatible-pkgproxywinkernelsupportedgo66) `:66`

- 🔗 [IsCompatible](#iscompatible-pkgproxywinkernelsupportedgo51) `:51`


</details>


[function] name: CanUseWinKernelProxier file: pkg/proxy/winkernel/supported.go:40 returns_error: да description: CanUseWinKernelProxier returns true if we should use the Kernel Proxier
instead of the "classic" userspace Proxier.  Thi


### CanUseWinKernelProxier (pkg/proxy/winkernel/supported.go:40)


CanUseWinKernelProxier returns true if we should use the Kernel Proxier
instead of the "classic" userspace Proxier.  This is determined by checking
the windows kernel version and for the existence of kernel features.


```go
func CanUseWinKernelProxier((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/supported.go:40`



---


[function] name: DualStackCompatible file: pkg/proxy/winkernel/supported.go:66 returns_error: нет description: —


### DualStackCompatible (pkg/proxy/winkernel/supported.go:66)


DualStackCompatible is a method that performs operations based on the provided parameters and returns (networkName string).


```go
func (t DualStackCompatTester) DualStackCompatible((networkName string)) (networkName string)
```


**Тип ответа:** networkName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/supported.go:66`



---


[function] name: IsCompatible file: pkg/proxy/winkernel/supported.go:51 returns_error: нет description: IsCompatible returns true if winkernel can support this mode of proxy


### IsCompatible (pkg/proxy/winkernel/supported.go:51)


IsCompatible returns true if winkernel can support this mode of proxy


```go
func (lkct WindowsKernelCompatTester) IsCompatible(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/supported.go:51`




## pkg/proxy/winkernel/testing/hcnutils_mock.go


📄 Исходный файл: `pkg/proxy/winkernel/testing/hcnutils_mock.go`


<details open>
<summary><b>Функции в этом файле (23)</b></summary>


- 🔗 [CreateEndpoint](#createendpoint-pkgproxywinkerneltestinghcnutils_mockgo140) `:140`

- 🔗 [CreateLoadBalancer](#createloadbalancer-pkgproxywinkerneltestinghcnutils_mockgo186) `:186`

- 🔗 [CreateRemoteEndpoint](#createremoteendpoint-pkgproxywinkerneltestinghcnutils_mockgo157) `:157`

- 🔗 [DeleteAllHnsLoadBalancerPolicy](#deleteallhnsloadbalancerpolicy-pkgproxywinkerneltestinghcnutils_mockgo241) `:241`

- 🔗 [DeleteEndpoint](#deleteendpoint-pkgproxywinkerneltestinghcnutils_mockgo161) `:161`

- 🔗 [DeleteLoadBalancer](#deleteloadbalancer-pkgproxywinkerneltestinghcnutils_mockgo215) `:215`

- 🔗 [DsrSupported](#dsrsupported-pkgproxywinkerneltestinghcnutils_mockgo234) `:234`

- 🔗 [GetEndpointByID](#getendpointbyid-pkgproxywinkerneltestinghcnutils_mockgo124) `:124`

- 🔗 [GetEndpointByName](#getendpointbyname-pkgproxywinkerneltestinghcnutils_mockgo132) `:132`

- 🔗 [GetLoadBalancerByID](#getloadbalancerbyid-pkgproxywinkerneltestinghcnutils_mockgo178) `:178`

- 🔗 [GetNetworkByID](#getnetworkbyid-pkgproxywinkerneltestinghcnutils_mockgo102) `:102`

- 🔗 [GetNetworkByName](#getnetworkbyname-pkgproxywinkerneltestinghcnutils_mockgo98) `:98`

- 🔗 [GetSupportedFeatures](#getsupportedfeatures-pkgproxywinkerneltestinghcnutils_mockgo223) `:223`

- 🔗 [Ipv6DualStackSupported](#ipv6dualstacksupported-pkgproxywinkerneltestinghcnutils_mockgo227) `:227`

- 🔗 [ListEndpoints](#listendpoints-pkgproxywinkerneltestinghcnutils_mockgo106) `:106`

- 🔗 [ListEndpointsOfNetwork](#listendpointsofnetwork-pkgproxywinkerneltestinghcnutils_mockgo114) `:114`

- 🔗 [ListLoadBalancers](#listloadbalancers-pkgproxywinkerneltestinghcnutils_mockgo170) `:170`

- 🔗 [NewHcnMock](#newhcnmock-pkgproxywinkerneltestinghcnutils_mockgo53) `:53`

- 🔗 [PopulateQueriedEndpoints](#populatequeriedendpoints-pkgproxywinkerneltestinghcnutils_mockgo71) `:71`

- 🔗 [RemoteSubnetSupported](#remotesubnetsupported-pkgproxywinkerneltestinghcnutils_mockgo247) `:247`

- 🔗 [UpdateLoadBalancer](#updateloadbalancer-pkgproxywinkerneltestinghcnutils_mockgo206) `:206`

- 🔗 [generateEndpointGuid](#generateendpointguid-pkgproxywinkerneltestinghcnutils_mockgo40) `:40`

- 🔗 [generateLoadbalancerGuid](#generateloadbalancerguid-pkgproxywinkerneltestinghcnutils_mockgo47) `:47`


</details>


[function] name: CreateEndpoint file: pkg/proxy/winkernel/testing/hcnutils_mock.go:140 returns_error: да description: —


### CreateEndpoint (pkg/proxy/winkernel/testing/hcnutils_mock.go:140)


CreateEndpoint is a method that creates new data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) CreateEndpoint((*hcn.HostComputeEndpoint, error)) (*hcn.HostComputeEndpoint, error)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:140`



---


[function] name: CreateLoadBalancer file: pkg/proxy/winkernel/testing/hcnutils_mock.go:186 returns_error: да description: —


### CreateLoadBalancer (pkg/proxy/winkernel/testing/hcnutils_mock.go:186)


CreateLoadBalancer is a method that creates new data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) CreateLoadBalancer((*hcn.HostComputeLoadBalancer, error)) (*hcn.HostComputeLoadBalancer, error)
```


**Тип запроса:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeLoadBalancer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:186`



---


[function] name: CreateRemoteEndpoint file: pkg/proxy/winkernel/testing/hcnutils_mock.go:157 returns_error: да description: —


### CreateRemoteEndpoint (pkg/proxy/winkernel/testing/hcnutils_mock.go:157)


CreateRemoteEndpoint is a method that creates new data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) CreateRemoteEndpoint((*hcn.HostComputeEndpoint, error)) (*hcn.HostComputeEndpoint, error)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:157`



---


[function] name: DeleteAllHnsLoadBalancerPolicy file: pkg/proxy/winkernel/testing/hcnutils_mock.go:241 returns_error: нет description: —


### DeleteAllHnsLoadBalancerPolicy (pkg/proxy/winkernel/testing/hcnutils_mock.go:241)


DeleteAllHnsLoadBalancerPolicy is a method that deletes data based on the provided parameters and returns ().


```go
func (hcnObj HcnMock) DeleteAllHnsLoadBalancerPolicy(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:241`



---


[function] name: DeleteEndpoint file: pkg/proxy/winkernel/testing/hcnutils_mock.go:161 returns_error: нет description: —


### DeleteEndpoint (pkg/proxy/winkernel/testing/hcnutils_mock.go:161)


DeleteEndpoint is a method that deletes data based on the provided parameters and returns (endpoint *hcn.HostComputeEndpoint).


```go
func (hcnObj HcnMock) DeleteEndpoint((endpoint *hcn.HostComputeEndpoint)) (endpoint *hcn.HostComputeEndpoint)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpoint


```json
{
  "URL": "string",
  "AccessToken": "string",
  "JWT": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:161`



---


[function] name: DeleteLoadBalancer file: pkg/proxy/winkernel/testing/hcnutils_mock.go:215 returns_error: нет description: —


### DeleteLoadBalancer (pkg/proxy/winkernel/testing/hcnutils_mock.go:215)


DeleteLoadBalancer is a method that deletes data based on the provided parameters and returns (loadBalancer *hcn.HostComputeLoadBalancer).


```go
func (hcnObj HcnMock) DeleteLoadBalancer((loadBalancer *hcn.HostComputeLoadBalancer)) (loadBalancer *hcn.HostComputeLoadBalancer)
```


**Тип запроса:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** loadBalancer


```json
{
  "ip": "string",
  "hnsID": "string",
  "healthCheckHnsID": "string"
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:215`



---


[function] name: DsrSupported file: pkg/proxy/winkernel/testing/hcnutils_mock.go:234 returns_error: нет description: —


### DsrSupported (pkg/proxy/winkernel/testing/hcnutils_mock.go:234)


DsrSupported is a method that performs operations based on the provided parameters and returns ().


```go
func (hcnObj HcnMock) DsrSupported(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:234`



---


[function] name: GetEndpointByID file: pkg/proxy/winkernel/testing/hcnutils_mock.go:124 returns_error: да description: —


### GetEndpointByID (pkg/proxy/winkernel/testing/hcnutils_mock.go:124)


GetEndpointByID is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) GetEndpointByID((*hcn.HostComputeEndpoint, error)) (*hcn.HostComputeEndpoint, error)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:124`



---


[function] name: GetEndpointByName file: pkg/proxy/winkernel/testing/hcnutils_mock.go:132 returns_error: да description: —


### GetEndpointByName (pkg/proxy/winkernel/testing/hcnutils_mock.go:132)


GetEndpointByName is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) GetEndpointByName((*hcn.HostComputeEndpoint, error)) (*hcn.HostComputeEndpoint, error)
```


**Тип запроса:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:132`



---


[function] name: GetLoadBalancerByID file: pkg/proxy/winkernel/testing/hcnutils_mock.go:178 returns_error: да description: —


### GetLoadBalancerByID (pkg/proxy/winkernel/testing/hcnutils_mock.go:178)


GetLoadBalancerByID is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) GetLoadBalancerByID((*hcn.HostComputeLoadBalancer, error)) (*hcn.HostComputeLoadBalancer, error)
```


**Тип запроса:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeLoadBalancer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:178`



---


[function] name: GetNetworkByID file: pkg/proxy/winkernel/testing/hcnutils_mock.go:102 returns_error: да description: —


### GetNetworkByID (pkg/proxy/winkernel/testing/hcnutils_mock.go:102)


GetNetworkByID is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) GetNetworkByID((*hcn.HostComputeNetwork, error)) (*hcn.HostComputeNetwork, error)
```


**Тип запроса:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeNetwork`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:102`



---


[function] name: GetNetworkByName file: pkg/proxy/winkernel/testing/hcnutils_mock.go:98 returns_error: да description: —


### GetNetworkByName (pkg/proxy/winkernel/testing/hcnutils_mock.go:98)


GetNetworkByName is a method that retrieves data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) GetNetworkByName((*hcn.HostComputeNetwork, error)) (*hcn.HostComputeNetwork, error)
```


**Тип запроса:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeNetwork`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:98`



---


[function] name: GetSupportedFeatures file: pkg/proxy/winkernel/testing/hcnutils_mock.go:223 returns_error: нет description: —


### GetSupportedFeatures (pkg/proxy/winkernel/testing/hcnutils_mock.go:223)


GetSupportedFeatures is a method that retrieves data based on the provided parameters and returns ().


```go
func (hcnObj HcnMock) GetSupportedFeatures(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:223`



---


[function] name: Ipv6DualStackSupported file: pkg/proxy/winkernel/testing/hcnutils_mock.go:227 returns_error: нет description: —


### Ipv6DualStackSupported (pkg/proxy/winkernel/testing/hcnutils_mock.go:227)


Ipv6DualStackSupported is a method that performs operations based on the provided parameters and returns ().


```go
func (hcnObj HcnMock) Ipv6DualStackSupported(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:227`



---


[function] name: ListEndpoints file: pkg/proxy/winkernel/testing/hcnutils_mock.go:106 returns_error: да description: —


### ListEndpoints (pkg/proxy/winkernel/testing/hcnutils_mock.go:106)


ListEndpoints is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) ListEndpoints(([]hcn.HostComputeEndpoint, error)) ([]hcn.HostComputeEndpoint, error)
```


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:106`



---


[function] name: ListEndpointsOfNetwork file: pkg/proxy/winkernel/testing/hcnutils_mock.go:114 returns_error: да description: —


### ListEndpointsOfNetwork (pkg/proxy/winkernel/testing/hcnutils_mock.go:114)


ListEndpointsOfNetwork is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) ListEndpointsOfNetwork(([]hcn.HostComputeEndpoint, error)) ([]hcn.HostComputeEndpoint, error)
```


**Тип ответа:** hcn.HostComputeEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]hcn.HostComputeEndpoint`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:114`



---


[function] name: ListLoadBalancers file: pkg/proxy/winkernel/testing/hcnutils_mock.go:170 returns_error: да description: —


### ListLoadBalancers (pkg/proxy/winkernel/testing/hcnutils_mock.go:170)


ListLoadBalancers is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) ListLoadBalancers(([]hcn.HostComputeLoadBalancer, error)) ([]hcn.HostComputeLoadBalancer, error)
```


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]hcn.HostComputeLoadBalancer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:170`



---


[function] name: NewHcnMock file: pkg/proxy/winkernel/testing/hcnutils_mock.go:53 returns_error: нет description: —


### NewHcnMock (pkg/proxy/winkernel/testing/hcnutils_mock.go:53)


NewHcnMock is a function that performs operations based on the provided parameters and returns (hnsNetwork *hcn.HostComputeNetwork).


```go
func NewHcnMock((hnsNetwork *hcn.HostComputeNetwork)) (hnsNetwork *hcn.HostComputeNetwork)
```


**Тип запроса:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hnsNetwork


```json
{
  "name": "string",
  "id": "string",
  "networkType": "string",
  "remoteSubnets": []
}
```


*Определено в:* `pkg/proxy/winkernel/proxier.go`


**Тип ответа:** hcn.HostComputeNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:53`



---


[function] name: PopulateQueriedEndpoints file: pkg/proxy/winkernel/testing/hcnutils_mock.go:71 returns_error: нет description: —


### PopulateQueriedEndpoints (pkg/proxy/winkernel/testing/hcnutils_mock.go:71)


PopulateQueriedEndpoints is a method that performs operations based on the provided parameters and returns (epId, hnsId, ipAddress, mac string, prefixLen uint8).


```go
func (hcnObj HcnMock) PopulateQueriedEndpoints((epId, hnsId, ipAddress, mac string, prefixLen uint8)) (epId, hnsId, ipAddress, mac string, prefixLen uint8)
```


**Тип ответа:** epId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hnsId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ipAddress


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mac


```json
{
  "sysfs": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/deviceattribute/machine.go`


**Тип ответа:** prefixLen


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:71`



---


[function] name: RemoteSubnetSupported file: pkg/proxy/winkernel/testing/hcnutils_mock.go:247 returns_error: нет description: —


### RemoteSubnetSupported (pkg/proxy/winkernel/testing/hcnutils_mock.go:247)


RemoteSubnetSupported is a method that performs operations based on the provided parameters and returns ().


```go
func (hcnObj HcnMock) RemoteSubnetSupported(()) ()
```


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:247`



---


[function] name: UpdateLoadBalancer file: pkg/proxy/winkernel/testing/hcnutils_mock.go:206 returns_error: да description: —


### UpdateLoadBalancer (pkg/proxy/winkernel/testing/hcnutils_mock.go:206)


UpdateLoadBalancer is a method that updates data based on the provided parameters and may return an error.


```go
func (hcnObj HcnMock) UpdateLoadBalancer((*hcn.HostComputeLoadBalancer, error)) (*hcn.HostComputeLoadBalancer, error)
```


**Тип запроса:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hcn.HostComputeLoadBalancer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*hcn.HostComputeLoadBalancer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:206`



---


[function] name: generateEndpointGuid file: pkg/proxy/winkernel/testing/hcnutils_mock.go:40 returns_error: нет description: —


### generateEndpointGuid (pkg/proxy/winkernel/testing/hcnutils_mock.go:40)


generateEndpointGuid is a method that performs operations based on the provided parameters and returns (endpointId string, endpointName string).


```go
func (hcnObj HcnMock) generateEndpointGuid((endpointId string, endpointName string)) (endpointId string, endpointName string)
```


**Тип ответа:** endpointId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** endpointName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:40`



---


[function] name: generateLoadbalancerGuid file: pkg/proxy/winkernel/testing/hcnutils_mock.go:47 returns_error: нет description: —


### generateLoadbalancerGuid (pkg/proxy/winkernel/testing/hcnutils_mock.go:47)


generateLoadbalancerGuid is a method that performs operations based on the provided parameters and returns (loadbalancerId string).


```go
func (hcnObj HcnMock) generateLoadbalancerGuid((loadbalancerId string)) (loadbalancerId string)
```


**Тип ответа:** loadbalancerId


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/proxy/winkernel/testing/hcnutils_mock.go:47`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_probe.md)

- [Следующая директория](pkg_quota.md)


---

