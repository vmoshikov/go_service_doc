---
title: "Функции: test/images"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/images
---


# Функции: test/images


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_fuzz.md)

- [Следующая директория](test_instrumentation.md)


---


## Меню по файлам


- 📄 [test/images/agnhost/agnhost.go](#testimagesagnhostagnhostgo)

- 📄 [test/images/agnhost/audit-proxy/main.go](#testimagesagnhostaudit-proxymaingo)

- 📄 [test/images/agnhost/connect/connect.go](#testimagesagnhostconnectconnectgo)

- 📄 [test/images/agnhost/crd-conversion-webhook/config.go](#testimagesagnhostcrd-conversion-webhookconfiggo)

- 📄 [test/images/agnhost/crd-conversion-webhook/converter/example_converter.go](#testimagesagnhostcrd-conversion-webhookconverterexample_convertergo)

- 📄 [test/images/agnhost/crd-conversion-webhook/converter/framework.go](#testimagesagnhostcrd-conversion-webhookconverterframeworkgo)

- 📄 [test/images/agnhost/crd-conversion-webhook/main.go](#testimagesagnhostcrd-conversion-webhookmaingo)

- 📄 [test/images/agnhost/dns/common.go](#testimagesagnhostdnscommongo)

- 📄 [test/images/agnhost/dns/dns.go](#testimagesagnhostdnsdnsgo)

- 📄 [test/images/agnhost/dns/dns_windows.go](#testimagesagnhostdnsdns_windowsgo)

- 📄 [test/images/agnhost/entrypoint-tester/ep.go](#testimagesagnhostentrypoint-testerepgo)

- 📄 [test/images/agnhost/external-metrics/provider.go](#testimagesagnhostexternal-metricsprovidergo)

- 📄 [test/images/agnhost/external-metrics/server.go](#testimagesagnhostexternal-metricsservergo)

- 📄 [test/images/agnhost/fakegitserver/gitserver.go](#testimagesagnhostfakegitservergitservergo)

- 📄 [test/images/agnhost/fakeregistryserver/registryserver.go](#testimagesagnhostfakeregistryserverregistryservergo)

- 📄 [test/images/agnhost/grpc-health-checking/grpc-health-checking.go](#testimagesagnhostgrpc-health-checkinggrpc-health-checkinggo)

- 📄 [test/images/agnhost/guestbook/guestbook.go](#testimagesagnhostguestbookguestbookgo)

- 📄 [test/images/agnhost/inclusterclient/main.go](#testimagesagnhostinclusterclientmaingo)

- 📄 [test/images/agnhost/liveness/server.go](#testimagesagnhostlivenessservergo)

- 📄 [test/images/agnhost/logs-generator/logs_generator.go](#testimagesagnhostlogs-generatorlogs_generatorgo)

- 📄 [test/images/agnhost/mounttest/mt.go](#testimagesagnhostmounttestmtgo)

- 📄 [test/images/agnhost/mounttest/mt_utils.go](#testimagesagnhostmounttestmt_utilsgo)

- 📄 [test/images/agnhost/mounttest/mt_utils_linux.go](#testimagesagnhostmounttestmt_utils_linuxgo)

- 📄 [test/images/agnhost/mounttest/mt_utils_other.go](#testimagesagnhostmounttestmt_utils_othergo)

- 📄 [test/images/agnhost/mounttest/mt_utils_windows.go](#testimagesagnhostmounttestmt_utils_windowsgo)

- 📄 [test/images/agnhost/mtlsclient/client.go](#testimagesagnhostmtlsclientclientgo)

- 📄 [test/images/agnhost/mtlsserver/server.go](#testimagesagnhostmtlsserverservergo)

- 📄 [test/images/agnhost/net/main.go](#testimagesagnhostnetmaingo)

- 📄 [test/images/agnhost/net/nat/closewait.go](#testimagesagnhostnetnatclosewaitgo)

- 📄 [test/images/agnhost/netexec/netexec.go](#testimagesagnhostnetexecnetexecgo)

- 📄 [test/images/agnhost/nettest/nettest.go](#testimagesagnhostnettestnettestgo)

- 📄 [test/images/agnhost/no-snat-test-proxy/main.go](#testimagesagnhostno-snat-test-proxymaingo)

- 📄 [test/images/agnhost/no-snat-test/main.go](#testimagesagnhostno-snat-testmaingo)

- 📄 [test/images/agnhost/nonewprivs/main.go](#testimagesagnhostnonewprivsmaingo)

- 📄 [test/images/agnhost/openidmetadata/openidmetadata.go](#testimagesagnhostopenidmetadataopenidmetadatago)

- 📄 [test/images/agnhost/pause/pause.go](#testimagesagnhostpausepausego)

- 📄 [test/images/agnhost/podcertificatesigner/podcertificatesigner.go](#testimagesagnhostpodcertificatesignerpodcertificatesignergo)

- 📄 [test/images/agnhost/port-forward-tester/portforwardtester.go](#testimagesagnhostport-forward-testerportforwardtestergo)

- 📄 [test/images/agnhost/porter/porter.go](#testimagesagnhostporterportergo)

- 📄 [test/images/agnhost/resource-consumer-controller/controller.go](#testimagesagnhostresource-consumer-controllercontrollergo)

- 📄 [test/images/agnhost/serve-hostname/serve_hostname.go](#testimagesagnhostserve-hostnameserve_hostnamego)

- 📄 [test/images/agnhost/tcp-reset/tcp_reset.go](#testimagesagnhosttcp-resettcp_resetgo)

- 📄 [test/images/agnhost/test-webserver/test-webserver.go](#testimagesagnhosttest-webservertest-webservergo)

- 📄 [test/images/agnhost/webhook/addlabel.go](#testimagesagnhostwebhookaddlabelgo)

- 📄 [test/images/agnhost/webhook/alwaysallow.go](#testimagesagnhostwebhookalwaysallowgo)

- 📄 [test/images/agnhost/webhook/alwaysdeny.go](#testimagesagnhostwebhookalwaysdenygo)

- 📄 [test/images/agnhost/webhook/config.go](#testimagesagnhostwebhookconfiggo)

- 📄 [test/images/agnhost/webhook/configmap.go](#testimagesagnhostwebhookconfigmapgo)

- 📄 [test/images/agnhost/webhook/convert.go](#testimagesagnhostwebhookconvertgo)

- 📄 [test/images/agnhost/webhook/crd.go](#testimagesagnhostwebhookcrdgo)

- 📄 [test/images/agnhost/webhook/customresource.go](#testimagesagnhostwebhookcustomresourcego)

- 📄 [test/images/agnhost/webhook/main.go](#testimagesagnhostwebhookmaingo)

- 📄 [test/images/agnhost/webhook/pods.go](#testimagesagnhostwebhookpodsgo)

- 📄 [test/images/agnhost/webhook/scheme.go](#testimagesagnhostwebhookschemego)

- 📄 [test/images/apparmor-loader/loader.go](#testimagesapparmor-loaderloadergo)

- 📄 [test/images/busybox/hostname.go](#testimagesbusyboxhostnamego)

- 📄 [test/images/nonewprivs/nnp.go](#testimagesnonewprivsnnpgo)

- 📄 [test/images/pets/peer-finder/peer-finder.go](#testimagespetspeer-finderpeer-findergo)

- 📄 [test/images/regression-issue-74839/main.go](#testimagesregression-issue-74839maingo)

- 📄 [test/images/regression-issue-74839/tcp.go](#testimagesregression-issue-74839tcpgo)

- 📄 [test/images/resource-consumer/consume-cpu/common.go](#testimagesresource-consumerconsume-cpucommongo)

- 📄 [test/images/resource-consumer/consume-cpu/consume_cpu.go](#testimagesresource-consumerconsume-cpuconsume_cpugo)

- 📄 [test/images/resource-consumer/consume-cpu/consume_cpu_windows.go](#testimagesresource-consumerconsume-cpuconsume_cpu_windowsgo)

- 📄 [test/images/resource-consumer/resource_consumer.go](#testimagesresource-consumerresource_consumergo)

- 📄 [test/images/resource-consumer/resource_consumer_handler.go](#testimagesresource-consumerresource_consumer_handlergo)

- 📄 [test/images/resource-consumer/utils.go](#testimagesresource-consumerutilsgo)

- 📄 [test/images/resource-consumer/utils_common.go](#testimagesresource-consumerutils_commongo)

- 📄 [test/images/resource-consumer/utils_windows.go](#testimagesresource-consumerutils_windowsgo)

- 📄 [test/images/sample-device-plugin/sampledeviceplugin.go](#testimagessample-device-pluginsampledeviceplugingo)


---


## test/images/agnhost/agnhost.go


📄 Исходный файл: `test/images/agnhost/agnhost.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testimagesagnhostagnhostgo62) `:62`


</details>


[function] name: main file: test/images/agnhost/agnhost.go:62 returns_error: нет description: —


### main (test/images/agnhost/agnhost.go:62)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/agnhost/agnhost.go:62`




## test/images/agnhost/audit-proxy/main.go


📄 Исходный файл: `test/images/agnhost/audit-proxy/main.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [handler](#handler-testimagesagnhostaudit-proxymaingo59) `:59`

- 🔗 [main](#main-testimagesagnhostaudit-proxymaingo48) `:48`


</details>


[function] name: handler file: test/images/agnhost/audit-proxy/main.go:59 returns_error: нет description: —


### handler (test/images/agnhost/audit-proxy/main.go:59)


handler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, req *http.Request).


```go
func handler((w http.ResponseWriter, req *http.Request)) (w http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


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


📍 *Расположение:* `test/images/agnhost/audit-proxy/main.go:59`



---


[function] name: main file: test/images/agnhost/audit-proxy/main.go:48 returns_error: нет description: —


### main (test/images/agnhost/audit-proxy/main.go:48)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/audit-proxy/main.go:48`




## test/images/agnhost/connect/connect.go


📄 Исходный файл: `test/images/agnhost/connect/connect.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [connectSCTP](#connectsctp-testimagesagnhostconnectconnectgo108) `:108`

- 🔗 [connectTCP](#connecttcp-testimagesagnhostconnectconnectgo75) `:75`

- 🔗 [connectUDP](#connectudp-testimagesagnhostconnectconnectgo155) `:155`

- 🔗 [init](#init-testimagesagnhostconnectconnectgo53) `:53`

- 🔗 [main](#main-testimagesagnhostconnectconnectgo60) `:60`

- 🔗 [parseUDPErrorAndExit](#parseudperrorandexit-testimagesagnhostconnectconnectgo194) `:194`


</details>


[function] name: connectSCTP file: test/images/agnhost/connect/connect.go:108 returns_error: нет description: —


### connectSCTP (test/images/agnhost/connect/connect.go:108)


connectSCTP is a function that performs operations based on the provided parameters and returns (dest string, timeout time.Duration, data string).


```go
func connectSCTP((dest string, timeout time.Duration, data string)) (dest string, timeout time.Duration, data string)
```


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


📍 *Расположение:* `test/images/agnhost/connect/connect.go:108`



---


[function] name: connectTCP file: test/images/agnhost/connect/connect.go:75 returns_error: нет description: —


### connectTCP (test/images/agnhost/connect/connect.go:75)


connectTCP is a function that performs operations based on the provided parameters and returns (dest string, timeout time.Duration).


```go
func connectTCP((dest string, timeout time.Duration)) (dest string, timeout time.Duration)
```


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


📍 *Расположение:* `test/images/agnhost/connect/connect.go:75`



---


[function] name: connectUDP file: test/images/agnhost/connect/connect.go:155 returns_error: нет description: —


### connectUDP (test/images/agnhost/connect/connect.go:155)


connectUDP is a function that performs operations based on the provided parameters and returns (dest string, timeout time.Duration, data string).


```go
func connectUDP((dest string, timeout time.Duration, data string)) (dest string, timeout time.Duration, data string)
```


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** timeout


```json
{
  "handler": {},
  "timeout": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go`


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


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


📍 *Расположение:* `test/images/agnhost/connect/connect.go:155`



---


[function] name: init file: test/images/agnhost/connect/connect.go:53 returns_error: нет description: —


### init (test/images/agnhost/connect/connect.go:53)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/connect/connect.go:53`



---


[function] name: main file: test/images/agnhost/connect/connect.go:60 returns_error: нет description: —


### main (test/images/agnhost/connect/connect.go:60)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/connect/connect.go:60`



---


[function] name: parseUDPErrorAndExit file: test/images/agnhost/connect/connect.go:194 returns_error: да description: —


### parseUDPErrorAndExit (test/images/agnhost/connect/connect.go:194)


parseUDPErrorAndExit is a function that performs operations based on the provided parameters and may return an error.


```go
func parseUDPErrorAndExit((err error)) (err error)
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


📍 *Расположение:* `test/images/agnhost/connect/connect.go:194`




## test/images/agnhost/crd-conversion-webhook/config.go


📄 Исходный файл: `test/images/agnhost/crd-conversion-webhook/config.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [configTLS](#configtls-testimagesagnhostcrd-conversion-webhookconfiggo40) `:40`

- 🔗 [getClient](#getclient-testimagesagnhostcrd-conversion-webhookconfiggo28) `:28`


</details>


[function] name: configTLS file: test/images/agnhost/crd-conversion-webhook/config.go:40 returns_error: нет description: —


### configTLS (test/images/agnhost/crd-conversion-webhook/config.go:40)


configTLS is a function that performs operations based on the provided parameters and returns (config Config, clientset *kubernetes.Clientset).


```go
func configTLS((config Config, clientset *kubernetes.Clientset)) (config Config, clientset *kubernetes.Clientset)
```


**Тип запроса:** kubernetes.Clientset


```json
{
  "discovery": null,
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/clientset/versioned/fake/clientset_generated.go`


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


**Тип ответа:** clientset


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubernetes.Clientset


```json
{
  "discovery": null,
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/examples/apiserver/clientset/versioned/fake/clientset_generated.go`


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/config.go:40`



---


[function] name: getClient file: test/images/agnhost/crd-conversion-webhook/config.go:28 returns_error: нет description: Get a clientset with in-cluster config.


### getClient (test/images/agnhost/crd-conversion-webhook/config.go:28)


Get a clientset with in-cluster config.


```go
func getClient(()) ()
```


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/config.go:28`




## test/images/agnhost/crd-conversion-webhook/converter/example_converter.go


📄 Исходный файл: `test/images/agnhost/crd-conversion-webhook/converter/example_converter.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [convertExampleCRD](#convertexamplecrd-testimagesagnhostcrd-conversion-webhookconverterexample_convertergo29) `:29`


</details>


[function] name: convertExampleCRD file: test/images/agnhost/crd-conversion-webhook/converter/example_converter.go:29 returns_error: нет description: —


### convertExampleCRD (test/images/agnhost/crd-conversion-webhook/converter/example_converter.go:29)


convertExampleCRD is a function that performs operations based on the provided parameters and returns (*unstructured.Unstructured, metav1.Status).


```go
func convertExampleCRD((*unstructured.Unstructured, metav1.Status)) (*unstructured.Unstructured, metav1.Status)
```


**Тип запроса:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Тип ответа:** unstructured.Unstructured


```json
{
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/testing/types.go`


**Тип ответа:** metav1.Status


```json
{
  "SoftRequirements": {}
}
```


*Определено в:* `pkg/kubelet/cm/container_manager.go`


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/example_converter.go:29`




## test/images/agnhost/crd-conversion-webhook/converter/framework.go


📄 Исходный файл: `test/images/agnhost/crd-conversion-webhook/converter/framework.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [ServeExampleConvert](#serveexampleconvert-testimagesagnhostcrd-conversion-webhookconverterframeworkgo200) `:200`

- 🔗 [addToScheme](#addtoscheme-testimagesagnhostcrd-conversion-webhookconverterframeworkgo214) `:214`

- 🔗 [doConversionV1](#doconversionv1-testimagesagnhostcrd-conversion-webhookconverterframeworkgo89) `:89`

- 🔗 [doConversionV1beta1](#doconversionv1beta1-testimagesagnhostcrd-conversion-webhookconverterframeworkgo58) `:58`

- 🔗 [getInputSerializer](#getinputserializer-testimagesagnhostcrd-conversion-webhookconverterframeworkgo224) `:224`

- 🔗 [getOutputSerializer](#getoutputserializer-testimagesagnhostcrd-conversion-webhookconverterframeworkgo232) `:232`

- 🔗 [init](#init-testimagesagnhostcrd-conversion-webhookconverterframeworkgo210) `:210`

- 🔗 [serve](#serve-testimagesagnhostcrd-conversion-webhookconverterframeworkgo118) `:118`

- 🔗 [statusErrorWithMessage](#statuserrorwithmessage-testimagesagnhostcrd-conversion-webhookconverterframeworkgo43) `:43`

- 🔗 [statusSucceed](#statussucceed-testimagesagnhostcrd-conversion-webhookconverterframeworkgo50) `:50`


</details>


[function] name: ServeExampleConvert file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:200 returns_error: нет description: ServeExampleConvert servers endpoint for the example converter defined as convertExampleCRD function.


### ServeExampleConvert (test/images/agnhost/crd-conversion-webhook/converter/framework.go:200)


ServeExampleConvert servers endpoint for the example converter defined as convertExampleCRD function.


```go
func ServeExampleConvert((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:200`



---


[function] name: addToScheme file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:214 returns_error: нет description: —


### addToScheme (test/images/agnhost/crd-conversion-webhook/converter/framework.go:214)


addToScheme is a function that performs operations based on the provided parameters and returns (scheme *runtime.Scheme).


```go
func addToScheme((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
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


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:214`



---


[function] name: doConversionV1 file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:89 returns_error: нет description: doConversionV1 converts the requested objects in the v1 ConversionRequest using the given conversion function and
return


### doConversionV1 (test/images/agnhost/crd-conversion-webhook/converter/framework.go:89)


doConversionV1 converts the requested objects in the v1 ConversionRequest using the given conversion function and
returns a conversion response. Failures are reported with the Reason in the conversion response.


```go
func doConversionV1((convertRequest *v1.ConversionRequest, convert convertFunc)) (convertRequest *v1.ConversionRequest, convert convertFunc)
```


**Тип запроса:** v1.ConversionRequest


```json
{
  "uid": {},
  "desiredAPIVersion": "string",
  "objects": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** convertRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.ConversionRequest


```json
{
  "uid": {},
  "desiredAPIVersion": "string",
  "objects": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** convert


```json
{
  "headers": [],
  "additionalColumns": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresource/tableconvertor/tableconvertor.go`


**Тип ответа:** convertFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:89`



---


[function] name: doConversionV1beta1 file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:58 returns_error: нет description: doConversionV1beta1 converts the requested objects in the v1beta1 ConversionRequest using the given conversion function 


### doConversionV1beta1 (test/images/agnhost/crd-conversion-webhook/converter/framework.go:58)


doConversionV1beta1 converts the requested objects in the v1beta1 ConversionRequest using the given conversion function and
returns a conversion response. Failures are reported with the Reason in the conversion response.


```go
func doConversionV1beta1((convertRequest *v1beta1.ConversionRequest, convert convertFunc)) (convertRequest *v1beta1.ConversionRequest, convert convertFunc)
```


**Тип запроса:** v1beta1.ConversionRequest


```json
{
  "uid": {},
  "desiredAPIVersion": "string",
  "objects": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** convertRequest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1beta1.ConversionRequest


```json
{
  "uid": {},
  "desiredAPIVersion": "string",
  "objects": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/types.go`


**Тип ответа:** convert


```json
{
  "headers": [],
  "additionalColumns": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresource/tableconvertor/tableconvertor.go`


**Тип ответа:** convertFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:58`



---


[function] name: getInputSerializer file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:224 returns_error: нет description: —


### getInputSerializer (test/images/agnhost/crd-conversion-webhook/converter/framework.go:224)


getInputSerializer is a function that performs operations based on the provided parameters and returns (contentType string).


```go
func getInputSerializer((contentType string)) (contentType string)
```


**Тип ответа:** contentType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:224`



---


[function] name: getOutputSerializer file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:232 returns_error: нет description: —


### getOutputSerializer (test/images/agnhost/crd-conversion-webhook/converter/framework.go:232)


getOutputSerializer is a function that performs operations based on the provided parameters and returns (accept string).


```go
func getOutputSerializer((accept string)) (accept string)
```


**Тип ответа:** accept


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:232`



---


[function] name: init file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:210 returns_error: нет description: —


### init (test/images/agnhost/crd-conversion-webhook/converter/framework.go:210)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:210`



---


[function] name: serve file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:118 returns_error: нет description: —


### serve (test/images/agnhost/crd-conversion-webhook/converter/framework.go:118)


serve is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request, convert convertFunc).


```go
func serve((w http.ResponseWriter, r *http.Request, convert convertFunc)) (w http.ResponseWriter, r *http.Request, convert convertFunc)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** convert


```json
{
  "headers": [],
  "additionalColumns": []
}
```


*Определено в:* `staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresource/tableconvertor/tableconvertor.go`


**Тип ответа:** convertFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:118`



---


[function] name: statusErrorWithMessage file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:43 returns_error: нет description: —


### statusErrorWithMessage (test/images/agnhost/crd-conversion-webhook/converter/framework.go:43)


statusErrorWithMessage is a function that performs operations based on the provided parameters and returns (msg string, params ...interface{}).


```go
func statusErrorWithMessage((msg string, params ...interface{})) (msg string, params ...interface{})
```


**Тип ответа:** msg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** params


```json
{
  "params": {},
  "isUsed": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:43`



---


[function] name: statusSucceed file: test/images/agnhost/crd-conversion-webhook/converter/framework.go:50 returns_error: нет description: —


### statusSucceed (test/images/agnhost/crd-conversion-webhook/converter/framework.go:50)


statusSucceed is a function that performs operations based on the provided parameters and returns ().


```go
func statusSucceed(()) ()
```


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/converter/framework.go:50`




## test/images/agnhost/crd-conversion-webhook/main.go


📄 Исходный файл: `test/images/agnhost/crd-conversion-webhook/main.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-testimagesagnhostcrd-conversion-webhookmaingo47) `:47`

- 🔗 [main](#main-testimagesagnhostcrd-conversion-webhookmaingo63) `:63`


</details>


[function] name: init file: test/images/agnhost/crd-conversion-webhook/main.go:47 returns_error: нет description: —


### init (test/images/agnhost/crd-conversion-webhook/main.go:47)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/main.go:47`



---


[function] name: main file: test/images/agnhost/crd-conversion-webhook/main.go:63 returns_error: нет description: —


### main (test/images/agnhost/crd-conversion-webhook/main.go:63)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/crd-conversion-webhook/main.go:63`




## test/images/agnhost/dns/common.go


📄 Исходный файл: `test/images/agnhost/dns/common.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [printDNSServerList](#printdnsserverlist-testimagesagnhostdnscommongo59) `:59`

- 🔗 [printDNSSuffixList](#printdnssuffixlist-testimagesagnhostdnscommongo54) `:54`

- 🔗 [printHostsFile](#printhostsfile-testimagesagnhostdnscommongo64) `:64`

- 🔗 [readFile](#readfile-testimagesagnhostdnscommongo68) `:68`


</details>


[function] name: printDNSServerList file: test/images/agnhost/dns/common.go:59 returns_error: нет description: —


### printDNSServerList (test/images/agnhost/dns/common.go:59)


printDNSServerList is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func printDNSServerList((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/dns/common.go:59`



---


[function] name: printDNSSuffixList file: test/images/agnhost/dns/common.go:54 returns_error: нет description: —


### printDNSSuffixList (test/images/agnhost/dns/common.go:54)


printDNSSuffixList is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func printDNSSuffixList((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/dns/common.go:54`



---


[function] name: printHostsFile file: test/images/agnhost/dns/common.go:64 returns_error: нет description: —


### printHostsFile (test/images/agnhost/dns/common.go:64)


printHostsFile is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func printHostsFile((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/dns/common.go:64`



---


[function] name: readFile file: test/images/agnhost/dns/common.go:68 returns_error: нет description: —


### readFile (test/images/agnhost/dns/common.go:68)


readFile is a function that performs operations based on the provided parameters and returns (fileName string).


```go
func readFile((fileName string)) (fileName string)
```


**Тип ответа:** fileName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/dns/common.go:68`




## test/images/agnhost/dns/dns.go


📄 Исходный файл: `test/images/agnhost/dns/dns.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [GetDNSSuffixList](#getdnssuffixlist-testimagesagnhostdnsdnsgo33) `:33`

- 🔗 [getDNSServerList](#getdnsserverlist-testimagesagnhostdnsdnsgo46) `:46`


</details>


[function] name: GetDNSSuffixList file: test/images/agnhost/dns/dns.go:33 returns_error: нет description: GetDNSSuffixList reads DNS config file and returns the list of configured DNS suffixes


### GetDNSSuffixList (test/images/agnhost/dns/dns.go:33)


GetDNSSuffixList reads DNS config file and returns the list of configured DNS suffixes


```go
func GetDNSSuffixList(()) ()
```


📍 *Расположение:* `test/images/agnhost/dns/dns.go:33`



---


[function] name: getDNSServerList file: test/images/agnhost/dns/dns.go:46 returns_error: нет description: —


### getDNSServerList (test/images/agnhost/dns/dns.go:46)


getDNSServerList is a function that performs operations based on the provided parameters and returns ().


```go
func getDNSServerList(()) ()
```


📍 *Расположение:* `test/images/agnhost/dns/dns.go:46`




## test/images/agnhost/dns/dns_windows.go


📄 Исходный файл: `test/images/agnhost/dns/dns_windows.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GetDNSSuffixList](#getdnssuffixlist-testimagesagnhostdnsdns_windowsgo84) `:84`

- 🔗 [elemInList](#eleminlist-testimagesagnhostdnsdns_windowsgo60) `:60`

- 🔗 [getDNSServerList](#getdnsserverlist-testimagesagnhostdnsdns_windowsgo138) `:138`

- 🔗 [getNetworkParams](#getnetworkparams-testimagesagnhostdnsdns_windowsgo118) `:118`

- 🔗 [getRegistryValue](#getregistryvalue-testimagesagnhostdnsdns_windowsgo69) `:69`


</details>


[function] name: GetDNSSuffixList file: test/images/agnhost/dns/dns_windows.go:84 returns_error: нет description: GetDNSSuffixList reads DNS config file and returns the list of configured DNS suffixes


### GetDNSSuffixList (test/images/agnhost/dns/dns_windows.go:84)


GetDNSSuffixList reads DNS config file and returns the list of configured DNS suffixes


```go
func GetDNSSuffixList(()) ()
```


📍 *Расположение:* `test/images/agnhost/dns/dns_windows.go:84`



---


[function] name: elemInList file: test/images/agnhost/dns/dns_windows.go:60 returns_error: нет description: —


### elemInList (test/images/agnhost/dns/dns_windows.go:60)


elemInList is a function that performs operations based on the provided parameters and returns (elem string, list []string).


```go
func elemInList((elem string, list []string)) (elem string, list []string)
```


**Тип ответа:** elem


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** list


```json
{
  "parent": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/listwatch.go`


📍 *Расположение:* `test/images/agnhost/dns/dns_windows.go:60`



---


[function] name: getDNSServerList file: test/images/agnhost/dns/dns_windows.go:138 returns_error: нет description: —


### getDNSServerList (test/images/agnhost/dns/dns_windows.go:138)


getDNSServerList is a function that performs operations based on the provided parameters and returns ().


```go
func getDNSServerList(()) ()
```


📍 *Расположение:* `test/images/agnhost/dns/dns_windows.go:138`



---


[function] name: getNetworkParams file: test/images/agnhost/dns/dns_windows.go:118 returns_error: нет description: —


### getNetworkParams (test/images/agnhost/dns/dns_windows.go:118)


getNetworkParams is a function that performs operations based on the provided parameters and returns ().


```go
func getNetworkParams(()) ()
```


📍 *Расположение:* `test/images/agnhost/dns/dns_windows.go:118`



---


[function] name: getRegistryValue file: test/images/agnhost/dns/dns_windows.go:69 returns_error: нет description: —


### getRegistryValue (test/images/agnhost/dns/dns_windows.go:69)


getRegistryValue is a function that performs operations based on the provided parameters and returns (reg, key string).


```go
func getRegistryValue((reg, key string)) (reg, key string)
```


**Тип ответа:** reg


```json
{
  "cache": null,
  "keyFunc": {},
  "messageFunc": {},
  "maxEvents": 0,
  "maxIntervalInSeconds": 0,
  "clock": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/events_cache.go`


**Тип ответа:** key


```json
{
  "container": "string",
  "resource": "string",
  "request": "string"
}
```


*Определено в:* `pkg/apis/core/validation/validation.go`


📍 *Расположение:* `test/images/agnhost/dns/dns_windows.go:69`




## test/images/agnhost/entrypoint-tester/ep.go


📄 Исходный файл: `test/images/agnhost/entrypoint-tester/ep.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testimagesagnhostentrypoint-testerepgo35) `:35`


</details>


[function] name: main file: test/images/agnhost/entrypoint-tester/ep.go:35 returns_error: нет description: This program prints all the executable's arguments and exits.


### main (test/images/agnhost/entrypoint-tester/ep.go:35)


This program prints all the executable's arguments and exits.


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/entrypoint-tester/ep.go:35`




## test/images/agnhost/external-metrics/provider.go


📄 Исходный файл: `test/images/agnhost/external-metrics/provider.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [NewConfigurableProvider](#newconfigurableprovider-testimagesagnhostexternal-metricsprovidergo40) `:40`

- 🔗 [buildMetricKey](#buildmetrickey-testimagesagnhostexternal-metricsprovidergo50) `:50`

- 🔗 [createMetric](#createmetric-testimagesagnhostexternal-metricsprovidergo107) `:107`

- 🔗 [getMetrics](#getmetrics-testimagesagnhostexternal-metricsprovidergo121) `:121`

- 🔗 [parseLabels](#parselabels-testimagesagnhostexternal-metricsprovidergo64) `:64`

- 🔗 [setMetricFailure](#setmetricfailure-testimagesagnhostexternal-metricsprovidergo81) `:81`

- 🔗 [setMetricValue](#setmetricvalue-testimagesagnhostexternal-metricsprovidergo96) `:96`


</details>


[function] name: NewConfigurableProvider file: test/images/agnhost/external-metrics/provider.go:40 returns_error: нет description: —


### NewConfigurableProvider (test/images/agnhost/external-metrics/provider.go:40)


NewConfigurableProvider is a function that performs operations based on the provided parameters and returns ().


```go
func NewConfigurableProvider(()) ()
```


📍 *Расположение:* `test/images/agnhost/external-metrics/provider.go:40`



---


[function] name: buildMetricKey file: test/images/agnhost/external-metrics/provider.go:50 returns_error: нет description: buildMetricKey creates a unique key combining metric name and labels
This allows multiple instances of the same metric w


### buildMetricKey (test/images/agnhost/external-metrics/provider.go:50)


buildMetricKey creates a unique key combining metric name and labels
This allows multiple instances of the same metric with different labels


```go
func buildMetricKey((metricName string, metricLabels map[string]string)) (metricName string, metricLabels map[string]string)
```


**Тип ответа:** metricName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metricLabels


```json
{
  "transformationType": "string",
  "providerName": "string",
  "keyIDHash": "string",
  "apiServerIDHash": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/envelope/metrics/metrics.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/images/agnhost/external-metrics/provider.go:50`



---


[function] name: createMetric file: test/images/agnhost/external-metrics/provider.go:107 returns_error: нет description: —


### createMetric (test/images/agnhost/external-metrics/provider.go:107)


createMetric is a method that performs operations based on the provided parameters and returns (metricName string, metricLabels map[string]string, metricValue int, shouldFail bool).


```go
func (p *metricProvider) createMetric((metricName string, metricLabels map[string]string, metricValue int, shouldFail bool)) (metricName string, metricLabels map[string]string, metricValue int, shouldFail bool)
```


**Тип ответа:** metricName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metricLabels


```json
{
  "transformationType": "string",
  "providerName": "string",
  "keyIDHash": "string",
  "apiServerIDHash": "string"
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/envelope/metrics/metrics.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** metricValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** shouldFail


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/external-metrics/provider.go:107`



---


[function] name: getMetrics file: test/images/agnhost/external-metrics/provider.go:121 returns_error: нет description: getMetrics returns all metrics matching the given name and label selector


### getMetrics (test/images/agnhost/external-metrics/provider.go:121)


getMetrics returns all metrics matching the given name and label selector


```go
func (p *metricProvider) getMetrics((metricName string, labelSelector map[string]string)) (metricName string, labelSelector map[string]string)
```


**Тип ответа:** metricName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** labelSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/images/agnhost/external-metrics/provider.go:121`



---


[function] name: parseLabels file: test/images/agnhost/external-metrics/provider.go:64 returns_error: нет description: parseLabels parses label selector from query string format
Example: "env=prod,region=us-west"


### parseLabels (test/images/agnhost/external-metrics/provider.go:64)


parseLabels parses label selector from query string format
Example: "env=prod,region=us-west"


```go
func parseLabels((labelSelector string)) (labelSelector string)
```


**Тип ответа:** labelSelector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/external-metrics/provider.go:64`



---


[function] name: setMetricFailure file: test/images/agnhost/external-metrics/provider.go:81 returns_error: нет description: setMetricFailure controls whether a specific metric should fail


### setMetricFailure (test/images/agnhost/external-metrics/provider.go:81)


setMetricFailure controls whether a specific metric should fail


```go
func (p *metricProvider) setMetricFailure((metricKey string, failStr string)) (metricKey string, failStr string)
```


**Тип ответа:** metricKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** failStr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/external-metrics/provider.go:81`



---


[function] name: setMetricValue file: test/images/agnhost/external-metrics/provider.go:96 returns_error: нет description: setMetricFailure controls whether a specific metric should fail


### setMetricValue (test/images/agnhost/external-metrics/provider.go:96)


setMetricFailure controls whether a specific metric should fail


```go
func (p *metricProvider) setMetricValue((metricKey string, metricValue int)) (metricKey string, metricValue int)
```


**Тип ответа:** metricKey


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metricValue


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/external-metrics/provider.go:96`




## test/images/agnhost/external-metrics/server.go


📄 Исходный файл: `test/images/agnhost/external-metrics/server.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [createMetric](#createmetric-testimagesagnhostexternal-metricsservergo296) `:296`

- 🔗 [failMetric](#failmetric-testimagesagnhostexternal-metricsservergo212) `:212`

- 🔗 [handleMetrics](#handlemetrics-testimagesagnhostexternal-metricsservergo120) `:120`

- 🔗 [healthz](#healthz-testimagesagnhostexternal-metricsservergo113) `:113`

- 🔗 [init](#init-testimagesagnhostexternal-metricsservergo52) `:52`

- 🔗 [main](#main-testimagesagnhostexternal-metricsservergo58) `:58`

- 🔗 [setMetric](#setmetric-testimagesagnhostexternal-metricsservergo252) `:252`


</details>


[function] name: createMetric file: test/images/agnhost/external-metrics/server.go:296 returns_error: нет description: —


### createMetric (test/images/agnhost/external-metrics/server.go:296)


createMetric is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func createMetric((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/external-metrics/server.go:296`



---


[function] name: failMetric file: test/images/agnhost/external-metrics/server.go:212 returns_error: нет description: failMetric handles requests to mark a metric as failing or not failing.
Supports label selectors via the "labels" query 


### failMetric (test/images/agnhost/external-metrics/server.go:212)


failMetric handles requests to mark a metric as failing or not failing.
Supports label selectors via the "labels" query parameter (format: key1=value1,key2=value2).


```go
func failMetric((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/external-metrics/server.go:212`



---


[function] name: handleMetrics file: test/images/agnhost/external-metrics/server.go:120 returns_error: нет description: —


### handleMetrics (test/images/agnhost/external-metrics/server.go:120)


handleMetrics is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func handleMetrics((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/external-metrics/server.go:120`



---


[function] name: healthz file: test/images/agnhost/external-metrics/server.go:113 returns_error: нет description: —


### healthz (test/images/agnhost/external-metrics/server.go:113)


healthz is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func healthz((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/external-metrics/server.go:113`



---


[function] name: init file: test/images/agnhost/external-metrics/server.go:52 returns_error: нет description: —


### init (test/images/agnhost/external-metrics/server.go:52)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/external-metrics/server.go:52`



---


[function] name: main file: test/images/agnhost/external-metrics/server.go:58 returns_error: нет description: —


### main (test/images/agnhost/external-metrics/server.go:58)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/external-metrics/server.go:58`



---


[function] name: setMetric file: test/images/agnhost/external-metrics/server.go:252 returns_error: нет description: —


### setMetric (test/images/agnhost/external-metrics/server.go:252)


setMetric is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func setMetric((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/external-metrics/server.go:252`




## test/images/agnhost/fakegitserver/gitserver.go


📄 Исходный файл: `test/images/agnhost/fakegitserver/gitserver.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [hello](#hello-testimagesagnhostfakegitservergitservergo36) `:36`

- 🔗 [main](#main-testimagesagnhostfakegitservergitservergo43) `:43`


</details>


[function] name: hello file: test/images/agnhost/fakegitserver/gitserver.go:36 returns_error: нет description: —


### hello (test/images/agnhost/fakegitserver/gitserver.go:36)


hello is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func hello((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/fakegitserver/gitserver.go:36`



---


[function] name: main file: test/images/agnhost/fakegitserver/gitserver.go:43 returns_error: нет description: When doing `git clone localhost:8000`, you will clone an empty git repo named "8000" on local.
You can also use `git clo


### main (test/images/agnhost/fakegitserver/gitserver.go:43)


When doing `git clone localhost:8000`, you will clone an empty git repo named "8000" on local.
You can also use `git clone localhost:8000 my-repo-name` to rename that repo.


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/fakegitserver/gitserver.go:43`




## test/images/agnhost/fakeregistryserver/registryserver.go


📄 Исходный файл: `test/images/agnhost/fakeregistryserver/registryserver.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [NewRegistryServerMux](#newregistryservermux-testimagesagnhostfakeregistryserverregistryservergo67) `:67`

- 🔗 [auth](#auth-testimagesagnhostfakeregistryserverregistryservergo79) `:79`

- 🔗 [digestToPath](#digesttopath-testimagesagnhostfakeregistryserverregistryservergo96) `:96`

- 🔗 [handleBlobs](#handleblobs-testimagesagnhostfakeregistryserverregistryservergo107) `:107`

- 🔗 [handleManifests](#handlemanifests-testimagesagnhostfakeregistryserverregistryservergo117) `:117`

- 🔗 [handleV2](#handlev2-testimagesagnhostfakeregistryserverregistryservergo158) `:158`

- 🔗 [init](#init-testimagesagnhostfakeregistryserverregistryservergo42) `:42`

- 🔗 [main](#main-testimagesagnhostfakeregistryserverregistryservergo55) `:55`


</details>


[function] name: NewRegistryServerMux file: test/images/agnhost/fakeregistryserver/registryserver.go:67 returns_error: нет description: —


### NewRegistryServerMux (test/images/agnhost/fakeregistryserver/registryserver.go:67)


NewRegistryServerMux is a function that performs operations based on the provided parameters and returns (isPrivate bool).


```go
func NewRegistryServerMux((isPrivate bool)) (isPrivate bool)
```


**Тип ответа:** isPrivate


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/fakeregistryserver/registryserver.go:67`



---


[function] name: auth file: test/images/agnhost/fakeregistryserver/registryserver.go:79 returns_error: нет description: —


### auth (test/images/agnhost/fakeregistryserver/registryserver.go:79)


auth is a function that performs operations based on the provided parameters and returns (h http.Handler).


```go
func auth((h http.Handler)) (h http.Handler)
```


**Тип ответа:** h


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.Handler


```json
{
  "notify": [],
  "final": {},
  "once": {}
}
```


*Определено в:* `pkg/util/interrupt/interrupt.go`


📍 *Расположение:* `test/images/agnhost/fakeregistryserver/registryserver.go:79`



---


[function] name: digestToPath file: test/images/agnhost/fakeregistryserver/registryserver.go:96 returns_error: нет description: digestToPath converts a digest to a nested directory path following the Docker
registry storage layout. For example, "sh


### digestToPath (test/images/agnhost/fakeregistryserver/registryserver.go:96)


digestToPath converts a digest to a nested directory path following the Docker
registry storage layout. For example, "sha256:abc123..." becomes
"<baseDir>/sha256/ab/abc123.../data". This avoids filesystem issues with colons
in filenames on Windows and matches the standard Docker registry layout.


```go
func digestToPath((baseDir, digest string)) (baseDir, digest string)
```


**Тип ответа:** baseDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** digest


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/fakeregistryserver/registryserver.go:96`



---


[function] name: handleBlobs file: test/images/agnhost/fakeregistryserver/registryserver.go:107 returns_error: нет description: handleBlobs serves blob requests


### handleBlobs (test/images/agnhost/fakeregistryserver/registryserver.go:107)


handleBlobs serves blob requests


```go
func handleBlobs((w http.ResponseWriter, r *http.Request, imageName, identifier string)) (w http.ResponseWriter, r *http.Request, imageName, identifier string)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** imageName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** identifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/fakeregistryserver/registryserver.go:107`



---


[function] name: handleManifests file: test/images/agnhost/fakeregistryserver/registryserver.go:117 returns_error: нет description: handleManifests serves manifest requests. It dynamically sets the Content-Type
based on the manifest's mediaType field. 


### handleManifests (test/images/agnhost/fakeregistryserver/registryserver.go:117)


handleManifests serves manifest requests. It dynamically sets the Content-Type
based on the manifest's mediaType field. If the identifier is a tag, it
reads the digest from the tag file and issues a redirect.


```go
func handleManifests((w http.ResponseWriter, r *http.Request, imageName, identifier string)) (w http.ResponseWriter, r *http.Request, imageName, identifier string)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** imageName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** identifier


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/fakeregistryserver/registryserver.go:117`



---


[function] name: handleV2 file: test/images/agnhost/fakeregistryserver/registryserver.go:158 returns_error: нет description: —


### handleV2 (test/images/agnhost/fakeregistryserver/registryserver.go:158)


handleV2 is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func handleV2((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/fakeregistryserver/registryserver.go:158`



---


[function] name: init file: test/images/agnhost/fakeregistryserver/registryserver.go:42 returns_error: нет description: —


### init (test/images/agnhost/fakeregistryserver/registryserver.go:42)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/fakeregistryserver/registryserver.go:42`



---


[function] name: main file: test/images/agnhost/fakeregistryserver/registryserver.go:55 returns_error: нет description: —


### main (test/images/agnhost/fakeregistryserver/registryserver.go:55)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/fakeregistryserver/registryserver.go:55`




## test/images/agnhost/grpc-health-checking/grpc-health-checking.go


📄 Исходный файл: `test/images/agnhost/grpc-health-checking/grpc-health-checking.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [Check](#check-testimagesagnhostgrpc-health-checkinggrpc-health-checkinggo77) `:77`

- 🔗 [List](#list-testimagesagnhostgrpc-health-checkinggrpc-health-checkinggo73) `:73`

- 🔗 [NewHealthChecker](#newhealthchecker-testimagesagnhostgrpc-health-checkinggrpc-health-checkinggo100) `:100`

- 🔗 [Watch](#watch-testimagesagnhostgrpc-health-checkinggrpc-health-checkinggo96) `:96`

- 🔗 [init](#init-testimagesagnhostgrpc-health-checkinggrpc-health-checkinggo57) `:57`

- 🔗 [main](#main-testimagesagnhostgrpc-health-checkinggrpc-health-checkinggo106) `:106`


</details>


[function] name: Check file: test/images/agnhost/grpc-health-checking/grpc-health-checking.go:77 returns_error: да description: —


### Check (test/images/agnhost/grpc-health-checking/grpc-health-checking.go:77)


Check is a method that performs operations based on the provided parameters and may return an error.


```go
func (s *HealthChecker) Check((*grpc_health_v1.HealthCheckResponse, error)) (*grpc_health_v1.HealthCheckResponse, error)
```


**Тип запроса:** grpc_health_v1.HealthCheckResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** grpc_health_v1.HealthCheckResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*grpc_health_v1.HealthCheckResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/grpc-health-checking/grpc-health-checking.go:77`



---


[function] name: List file: test/images/agnhost/grpc-health-checking/grpc-health-checking.go:73 returns_error: да description: —


### List (test/images/agnhost/grpc-health-checking/grpc-health-checking.go:73)


List is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (s *HealthChecker) List((*grpc_health_v1.HealthListResponse, error)) (*grpc_health_v1.HealthListResponse, error)
```


**Тип запроса:** grpc_health_v1.HealthListResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** grpc_health_v1.HealthListResponse


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*grpc_health_v1.HealthListResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/grpc-health-checking/grpc-health-checking.go:73`



---


[function] name: NewHealthChecker file: test/images/agnhost/grpc-health-checking/grpc-health-checking.go:100 returns_error: нет description: —


### NewHealthChecker (test/images/agnhost/grpc-health-checking/grpc-health-checking.go:100)


NewHealthChecker is a function that performs operations based on the provided parameters and returns (started time.Time).


```go
func NewHealthChecker((started time.Time)) (started time.Time)
```


**Тип ответа:** started


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/images/agnhost/grpc-health-checking/grpc-health-checking.go:100`



---


[function] name: Watch file: test/images/agnhost/grpc-health-checking/grpc-health-checking.go:96 returns_error: нет description: —


### Watch (test/images/agnhost/grpc-health-checking/grpc-health-checking.go:96)


Watch is a method that performs operations based on the provided parameters and returns (req *grpc_health_v1.HealthCheckRequest, server grpc_health_v1.Health_WatchServer).


```go
func (s *HealthChecker) Watch((req *grpc_health_v1.HealthCheckRequest, server grpc_health_v1.Health_WatchServer)) (req *grpc_health_v1.HealthCheckRequest, server grpc_health_v1.Health_WatchServer)
```


**Тип запроса:** grpc_health_v1.HealthCheckRequest


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


**Тип ответа:** grpc_health_v1.HealthCheckRequest


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


**Тип ответа:** grpc_health_v1.Health_WatchServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/grpc-health-checking/grpc-health-checking.go:96`



---


[function] name: init file: test/images/agnhost/grpc-health-checking/grpc-health-checking.go:57 returns_error: нет description: —


### init (test/images/agnhost/grpc-health-checking/grpc-health-checking.go:57)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/grpc-health-checking/grpc-health-checking.go:57`



---


[function] name: main file: test/images/agnhost/grpc-health-checking/grpc-health-checking.go:106 returns_error: нет description: —


### main (test/images/agnhost/grpc-health-checking/grpc-health-checking.go:106)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/grpc-health-checking/grpc-health-checking.go:106`




## test/images/agnhost/guestbook/guestbook.go


📄 Исходный файл: `test/images/agnhost/guestbook/guestbook.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [createHTTPClient](#createhttpclient-testimagesagnhostguestbookguestbookgo289) `:289`

- 🔗 [dialHTTP](#dialhttp-testimagesagnhostguestbookguestbookgo274) `:274`

- 🔗 [getHandler](#gethandler-testimagesagnhostguestbookguestbookgo159) `:159`

- 🔗 [getIP](#getip-testimagesagnhostguestbookguestbookgo297) `:297`

- 🔗 [guestbookHandler](#guestbookhandler-testimagesagnhostguestbookguestbookgo231) `:231`

- 🔗 [init](#init-testimagesagnhostguestbookguestbookgo62) `:62`

- 🔗 [main](#main-testimagesagnhostguestbookguestbookgo69) `:69`

- 🔗 [registerHandler](#registerhandler-testimagesagnhostguestbookguestbookgo134) `:134`

- 🔗 [registerNode](#registernode-testimagesagnhostguestbookguestbookgo74) `:74`

- 🔗 [setHandler](#sethandler-testimagesagnhostguestbookguestbookgo191) `:191`

- 🔗 [startHTTPServer](#starthttpserver-testimagesagnhostguestbookguestbookgo124) `:124`


</details>


[function] name: createHTTPClient file: test/images/agnhost/guestbook/guestbook.go:289 returns_error: нет description: —


### createHTTPClient (test/images/agnhost/guestbook/guestbook.go:289)


createHTTPClient is a function that performs operations based on the provided parameters and returns (transport *http.Transport).


```go
func createHTTPClient((transport *http.Transport)) (transport *http.Transport)
```


**Тип запроса:** http.Transport


```json
{
  "Scheme": "string",
  "Host": "string",
  "PathPrepend": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/proxy/transport.go`


**Тип ответа:** transport


```json
{
  "m": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/prometheus/restclient/metrics.go`


**Тип ответа:** http.Transport


```json
{
  "Scheme": "string",
  "Host": "string",
  "PathPrepend": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/proxy/transport.go`


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:289`



---


[function] name: dialHTTP file: test/images/agnhost/guestbook/guestbook.go:274 returns_error: да description: —


### dialHTTP (test/images/agnhost/guestbook/guestbook.go:274)


dialHTTP is a function that performs operations based on the provided parameters and may return an error.


```go
func dialHTTP((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:274`



---


[function] name: getHandler file: test/images/agnhost/guestbook/guestbook.go:159 returns_error: нет description: getHandler will return '{"data": value}', where value is the stored value for
the given key if non-empty, or entire stor


### getHandler (test/images/agnhost/guestbook/guestbook.go:159)


getHandler will return '{"data": value}', where value is the stored value for
the given key if non-empty, or entire store.


```go
func getHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:159`



---


[function] name: getIP file: test/images/agnhost/guestbook/guestbook.go:297 returns_error: да description: —


### getIP (test/images/agnhost/guestbook/guestbook.go:297)


getIP is a function that performs operations based on the provided parameters and may return an error.


```go
func getIP((net.IP, error)) (net.IP, error)
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


*Типы возврата:* `net.IP`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:297`



---


[function] name: guestbookHandler file: test/images/agnhost/guestbook/guestbook.go:231 returns_error: нет description: guestbookHandler will proxy the request to agnhost-primary if the given cmd is
'set' or agnhost-replica if the given cmd


### guestbookHandler (test/images/agnhost/guestbook/guestbook.go:231)


guestbookHandler will proxy the request to agnhost-primary if the given cmd is
'set' or agnhost-replica if the given cmd is 'get'.


```go
func guestbookHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:231`



---


[function] name: init file: test/images/agnhost/guestbook/guestbook.go:62 returns_error: нет description: —


### init (test/images/agnhost/guestbook/guestbook.go:62)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:62`



---


[function] name: main file: test/images/agnhost/guestbook/guestbook.go:69 returns_error: нет description: —


### main (test/images/agnhost/guestbook/guestbook.go:69)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:69`



---


[function] name: registerHandler file: test/images/agnhost/guestbook/guestbook.go:134 returns_error: нет description: registerHandler will register the caller in this server's list of replicas.
/set requests will be propagated to replicas


### registerHandler (test/images/agnhost/guestbook/guestbook.go:134)


registerHandler will register the caller in this server's list of replicas.
/set requests will be propagated to replicas, if any.


```go
func registerHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:134`



---


[function] name: registerNode file: test/images/agnhost/guestbook/guestbook.go:74 returns_error: нет description: —


### registerNode (test/images/agnhost/guestbook/guestbook.go:74)


registerNode is a function that performs operations based on the provided parameters and returns (registerTo, port string).


```go
func registerNode((registerTo, port string)) (registerTo, port string)
```


**Тип ответа:** registerTo


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


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:74`



---


[function] name: setHandler file: test/images/agnhost/guestbook/guestbook.go:191 returns_error: нет description: setHandler will set the given key-value pair in its own store and propagate
it to its replicas, if any. Will return '{"m


### setHandler (test/images/agnhost/guestbook/guestbook.go:191)


setHandler will set the given key-value pair in its own store and propagate
it to its replicas, if any. Will return '{"message": "Updated"}' to the caller on success.


```go
func setHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:191`



---


[function] name: startHTTPServer file: test/images/agnhost/guestbook/guestbook.go:124 returns_error: нет description: —


### startHTTPServer (test/images/agnhost/guestbook/guestbook.go:124)


startHTTPServer is a function that performs operations based on the provided parameters and returns (port string).


```go
func startHTTPServer((port string)) (port string)
```


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


📍 *Расположение:* `test/images/agnhost/guestbook/guestbook.go:124`




## test/images/agnhost/inclusterclient/main.go


📄 Исходный файл: `test/images/agnhost/inclusterclient/main.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [RoundTrip](#roundtrip-testimagesagnhostinclusterclientmaingo92) `:92`

- 🔗 [WrappedRoundTripper](#wrappedroundtripper-testimagesagnhostinclusterclientmaingo103) `:103`

- 🔗 [init](#init-testimagesagnhostinclusterclientmaingo50) `:50`

- 🔗 [main](#main-testimagesagnhostinclusterclientmaingo55) `:55`


</details>


[function] name: RoundTrip file: test/images/agnhost/inclusterclient/main.go:92 returns_error: да description: —


### RoundTrip (test/images/agnhost/inclusterclient/main.go:92)


RoundTrip is a method that performs operations based on the provided parameters and may return an error.


```go
func (rt *debugRt) RoundTrip((*http.Response, error)) (*http.Response, error)
```


**Тип запроса:** http.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Тип ответа:** http.Response


```json
{
  "Audiences": {},
  "User": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/authenticator/interfaces.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*http.Response`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/inclusterclient/main.go:92`



---


[function] name: WrappedRoundTripper file: test/images/agnhost/inclusterclient/main.go:103 returns_error: нет description: —


### WrappedRoundTripper (test/images/agnhost/inclusterclient/main.go:103)


WrappedRoundTripper is a method that performs operations based on the provided parameters and returns ().


```go
func (rt *debugRt) WrappedRoundTripper(()) ()
```


📍 *Расположение:* `test/images/agnhost/inclusterclient/main.go:103`



---


[function] name: init file: test/images/agnhost/inclusterclient/main.go:50 returns_error: нет description: —


### init (test/images/agnhost/inclusterclient/main.go:50)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/inclusterclient/main.go:50`



---


[function] name: main file: test/images/agnhost/inclusterclient/main.go:55 returns_error: нет description: —


### main (test/images/agnhost/inclusterclient/main.go:55)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/inclusterclient/main.go:55`




## test/images/agnhost/liveness/server.go


📄 Исходный файл: `test/images/agnhost/liveness/server.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testimagesagnhostlivenessservergo41) `:41`


</details>


[function] name: main file: test/images/agnhost/liveness/server.go:41 returns_error: нет description: —


### main (test/images/agnhost/liveness/server.go:41)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/liveness/server.go:41`




## test/images/agnhost/logs-generator/logs_generator.go


📄 Исходный файл: `test/images/agnhost/logs-generator/logs_generator.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [generateLogLine](#generatelogline-testimagesagnhostlogs-generatorlogs_generatorgo82) `:82`

- 🔗 [generateLogs](#generatelogs-testimagesagnhostlogs-generatorlogs_generatorgo62) `:62`

- 🔗 [init](#init-testimagesagnhostlogs-generatorlogs_generatorgo56) `:56`


</details>


[function] name: generateLogLine file: test/images/agnhost/logs-generator/logs_generator.go:82 returns_error: нет description: Generates apiserver-like line with average length of 100 symbols


### generateLogLine (test/images/agnhost/logs-generator/logs_generator.go:82)


Generates apiserver-like line with average length of 100 symbols


```go
func generateLogLine((id int)) (id int)
```


**Тип ответа:** id


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/coordination/v1beta1/leasecandidate.go`


📍 *Расположение:* `test/images/agnhost/logs-generator/logs_generator.go:82`



---


[function] name: generateLogs file: test/images/agnhost/logs-generator/logs_generator.go:62 returns_error: нет description: Outputs linesTotal lines of logs to stdout uniformly for duration


### generateLogs (test/images/agnhost/logs-generator/logs_generator.go:62)


Outputs linesTotal lines of logs to stdout uniformly for duration


```go
func generateLogs((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/logs-generator/logs_generator.go:62`



---


[function] name: init file: test/images/agnhost/logs-generator/logs_generator.go:56 returns_error: нет description: —


### init (test/images/agnhost/logs-generator/logs_generator.go:56)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/logs-generator/logs_generator.go:56`




## test/images/agnhost/mounttest/mt.go


📄 Исходный файл: `test/images/agnhost/mounttest/mt.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [init](#init-testimagesagnhostmounttestmtgo51) `:51`

- 🔗 [main](#main-testimagesagnhostmounttestmtgo68) `:68`

- 🔗 [readFileContent](#readfilecontent-testimagesagnhostmounttestmtgo143) `:143`

- 🔗 [readFileContentInLoop](#readfilecontentinloop-testimagesagnhostmounttestmtgo175) `:175`

- 🔗 [readWriteNewFile](#readwritenewfile-testimagesagnhostmounttestmtgo161) `:161`

- 🔗 [testFileContent](#testfilecontent-testimagesagnhostmounttestmtgo182) `:182`


</details>


[function] name: init file: test/images/agnhost/mounttest/mt.go:51 returns_error: нет description: —


### init (test/images/agnhost/mounttest/mt.go:51)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/mounttest/mt.go:51`



---


[function] name: main file: test/images/agnhost/mounttest/mt.go:68 returns_error: нет description: This program performs some tests on the filesystem as dictated by the
flags passed by the user.


### main (test/images/agnhost/mounttest/mt.go:68)


This program performs some tests on the filesystem as dictated by the
flags passed by the user.


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mounttest/mt.go:68`



---


[function] name: readFileContent file: test/images/agnhost/mounttest/mt.go:143 returns_error: нет description: —


### readFileContent (test/images/agnhost/mounttest/mt.go:143)


readFileContent is a function that performs operations based on the provided parameters and returns (path string).


```go
func readFileContent((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt.go:143`



---


[function] name: readFileContentInLoop file: test/images/agnhost/mounttest/mt.go:175 returns_error: нет description: —


### readFileContentInLoop (test/images/agnhost/mounttest/mt.go:175)


readFileContentInLoop is a function that performs operations based on the provided parameters and returns (path string, retryDuration int, breakOnExpectedContent bool).


```go
func readFileContentInLoop((path string, retryDuration int, breakOnExpectedContent bool)) (path string, retryDuration int, breakOnExpectedContent bool)
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


**Тип ответа:** retryDuration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** breakOnExpectedContent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mounttest/mt.go:175`



---


[function] name: readWriteNewFile file: test/images/agnhost/mounttest/mt.go:161 returns_error: нет description: —


### readWriteNewFile (test/images/agnhost/mounttest/mt.go:161)


readWriteNewFile is a function that performs operations based on the provided parameters and returns (path string, perm os.FileMode).


```go
func readWriteNewFile((path string, perm os.FileMode)) (path string, perm os.FileMode)
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


**Тип ответа:** perm


```json
{
  "nested": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/dynamic/scheme.go`


**Тип ответа:** os.FileMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mounttest/mt.go:161`



---


[function] name: testFileContent file: test/images/agnhost/mounttest/mt.go:182 returns_error: нет description: —


### testFileContent (test/images/agnhost/mounttest/mt.go:182)


testFileContent is a function that performs operations based on the provided parameters and returns (filePath string, retryDuration int, breakOnExpectedContent bool).


```go
func testFileContent((filePath string, retryDuration int, breakOnExpectedContent bool)) (filePath string, retryDuration int, breakOnExpectedContent bool)
```


**Тип ответа:** filePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** retryDuration


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** breakOnExpectedContent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mounttest/mt.go:182`




## test/images/agnhost/mounttest/mt_utils.go


📄 Исходный файл: `test/images/agnhost/mounttest/mt_utils.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [fileMode](#filemode-testimagesagnhostmounttestmt_utilsgo47) `:47`

- 🔗 [fileOwner](#fileowner-testimagesagnhostmounttestmt_utilsgo77) `:77`

- 🔗 [filePerm](#fileperm-testimagesagnhostmounttestmt_utilsgo62) `:62`

- 🔗 [fsType](#fstype-testimagesagnhostmounttestmt_utilsgo31) `:31`

- 🔗 [umask](#umask-testimagesagnhostmounttestmt_utilsgo27) `:27`


</details>


[function] name: fileMode file: test/images/agnhost/mounttest/mt_utils.go:47 returns_error: нет description: —


### fileMode (test/images/agnhost/mounttest/mt_utils.go:47)


fileMode is a function that performs operations based on the provided parameters and returns (path string).


```go
func fileMode((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils.go:47`



---


[function] name: fileOwner file: test/images/agnhost/mounttest/mt_utils.go:77 returns_error: нет description: —


### fileOwner (test/images/agnhost/mounttest/mt_utils.go:77)


fileOwner is a function that performs operations based on the provided parameters and returns (path string).


```go
func fileOwner((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils.go:77`



---


[function] name: filePerm file: test/images/agnhost/mounttest/mt_utils.go:62 returns_error: нет description: —


### filePerm (test/images/agnhost/mounttest/mt_utils.go:62)


filePerm is a function that performs operations based on the provided parameters and returns (path string).


```go
func filePerm((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils.go:62`



---


[function] name: fsType file: test/images/agnhost/mounttest/mt_utils.go:31 returns_error: нет description: —


### fsType (test/images/agnhost/mounttest/mt_utils.go:31)


fsType is a function that performs operations based on the provided parameters and returns (path string).


```go
func fsType((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils.go:31`



---


[function] name: umask file: test/images/agnhost/mounttest/mt_utils.go:27 returns_error: нет description: —


### umask (test/images/agnhost/mounttest/mt_utils.go:27)


umask is a function that performs operations based on the provided parameters and returns (mask int).


```go
func umask((mask int)) (mask int)
```


**Тип ответа:** mask


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils.go:27`




## test/images/agnhost/mounttest/mt_utils_linux.go


📄 Исходный файл: `test/images/agnhost/mounttest/mt_utils_linux.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [formatFsType](#formatfstype-testimagesagnhostmounttestmt_utils_linuxgo29) `:29`


</details>


[function] name: formatFsType file: test/images/agnhost/mounttest/mt_utils_linux.go:29 returns_error: нет description: formatFsType returns a string representation of the filesystem type.
It translates known filesystem magic numbers to hum


### formatFsType (test/images/agnhost/mounttest/mt_utils_linux.go:29)


formatFsType returns a string representation of the filesystem type.
It translates known filesystem magic numbers to human-readable names.


```go
func formatFsType((fsType int64)) (fsType int64)
```


**Тип ответа:** fsType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils_linux.go:29`




## test/images/agnhost/mounttest/mt_utils_other.go


📄 Исходный файл: `test/images/agnhost/mounttest/mt_utils_other.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [formatFsType](#formatfstype-testimagesagnhostmounttestmt_utils_othergo24) `:24`


</details>


[function] name: formatFsType file: test/images/agnhost/mounttest/mt_utils_other.go:24 returns_error: нет description: formatFsType returns a string representation of the filesystem type.


### formatFsType (test/images/agnhost/mounttest/mt_utils_other.go:24)


formatFsType returns a string representation of the filesystem type.


```go
func formatFsType((fsType int64)) (fsType int64)
```


**Тип ответа:** fsType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils_other.go:24`




## test/images/agnhost/mounttest/mt_utils_windows.go


📄 Исходный файл: `test/images/agnhost/mounttest/mt_utils_windows.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [fileMode](#filemode-testimagesagnhostmounttestmt_utils_windowsgo42) `:42`

- 🔗 [fileOwner](#fileowner-testimagesagnhostmounttestmt_utils_windowsgo36) `:36`

- 🔗 [filePerm](#fileperm-testimagesagnhostmounttestmt_utils_windowsgo56) `:56`

- 🔗 [fsType](#fstype-testimagesagnhostmounttestmt_utils_windowsgo111) `:111`

- 🔗 [getFilePerm](#getfileperm-testimagesagnhostmounttestmt_utils_windowsgo70) `:70`

- 🔗 [umask](#umask-testimagesagnhostmounttestmt_utils_windowsgo31) `:31`


</details>


[function] name: fileMode file: test/images/agnhost/mounttest/mt_utils_windows.go:42 returns_error: нет description: —


### fileMode (test/images/agnhost/mounttest/mt_utils_windows.go:42)


fileMode is a function that performs operations based on the provided parameters and returns (path string).


```go
func fileMode((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils_windows.go:42`



---


[function] name: fileOwner file: test/images/agnhost/mounttest/mt_utils_windows.go:36 returns_error: нет description: —


### fileOwner (test/images/agnhost/mounttest/mt_utils_windows.go:36)


fileOwner is a function that performs operations based on the provided parameters and returns (path string).


```go
func fileOwner((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils_windows.go:36`



---


[function] name: filePerm file: test/images/agnhost/mounttest/mt_utils_windows.go:56 returns_error: нет description: —


### filePerm (test/images/agnhost/mounttest/mt_utils_windows.go:56)


filePerm is a function that performs operations based on the provided parameters and returns (path string).


```go
func filePerm((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils_windows.go:56`



---


[function] name: fsType file: test/images/agnhost/mounttest/mt_utils_windows.go:111 returns_error: нет description: —


### fsType (test/images/agnhost/mounttest/mt_utils_windows.go:111)


fsType is a function that performs operations based on the provided parameters and returns (path string).


```go
func fsType((path string)) (path string)
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


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils_windows.go:111`



---


[function] name: getFilePerm file: test/images/agnhost/mounttest/mt_utils_windows.go:70 returns_error: да description: —


### getFilePerm (test/images/agnhost/mounttest/mt_utils_windows.go:70)


getFilePerm is a function that performs operations based on the provided parameters and may return an error.


```go
func getFilePerm((os.FileMode, error)) (os.FileMode, error)
```


**Тип ответа:** os.FileMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `os.FileMode`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils_windows.go:70`



---


[function] name: umask file: test/images/agnhost/mounttest/mt_utils_windows.go:31 returns_error: нет description: —


### umask (test/images/agnhost/mounttest/mt_utils_windows.go:31)


umask is a function that performs operations based on the provided parameters and returns (mask int).


```go
func umask((mask int)) (mask int)
```


**Тип ответа:** mask


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mounttest/mt_utils_windows.go:31`




## test/images/agnhost/mtlsclient/client.go


📄 Исходный файл: `test/images/agnhost/mtlsclient/client.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [init](#init-testimagesagnhostmtlsclientclientgo51) `:51`

- 🔗 [main](#main-testimagesagnhostmtlsclientclientgo57) `:57`

- 🔗 [pollOnce](#pollonce-testimagesagnhostmtlsclientclientgo77) `:77`


</details>


[function] name: init file: test/images/agnhost/mtlsclient/client.go:51 returns_error: нет description: —


### init (test/images/agnhost/mtlsclient/client.go:51)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/mtlsclient/client.go:51`



---


[function] name: main file: test/images/agnhost/mtlsclient/client.go:57 returns_error: нет description: —


### main (test/images/agnhost/mtlsclient/client.go:57)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mtlsclient/client.go:57`



---


[function] name: pollOnce file: test/images/agnhost/mtlsclient/client.go:77 returns_error: нет description: —


### pollOnce (test/images/agnhost/mtlsclient/client.go:77)


pollOnce is a function that performs operations based on the provided parameters and returns ().


```go
func pollOnce(()) ()
```


📍 *Расположение:* `test/images/agnhost/mtlsclient/client.go:77`




## test/images/agnhost/mtlsserver/server.go


📄 Исходный файл: `test/images/agnhost/mtlsserver/server.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [handleGetSPIFFEEcho](#handlegetspiffeecho-testimagesagnhostmtlsserverservergo113) `:113`

- 🔗 [init](#init-testimagesagnhostmtlsserverservergo47) `:47`

- 🔗 [main](#main-testimagesagnhostmtlsserverservergo53) `:53`

- 🔗 [serve](#serve-testimagesagnhostmtlsserverservergo67) `:67`


</details>


[function] name: handleGetSPIFFEEcho file: test/images/agnhost/mtlsserver/server.go:113 returns_error: нет description: —


### handleGetSPIFFEEcho (test/images/agnhost/mtlsserver/server.go:113)


handleGetSPIFFEEcho is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func handleGetSPIFFEEcho((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/mtlsserver/server.go:113`



---


[function] name: init file: test/images/agnhost/mtlsserver/server.go:47 returns_error: нет description: —


### init (test/images/agnhost/mtlsserver/server.go:47)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/mtlsserver/server.go:47`



---


[function] name: main file: test/images/agnhost/mtlsserver/server.go:53 returns_error: нет description: —


### main (test/images/agnhost/mtlsserver/server.go:53)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/mtlsserver/server.go:53`



---


[function] name: serve file: test/images/agnhost/mtlsserver/server.go:67 returns_error: нет description: —


### serve (test/images/agnhost/mtlsserver/server.go:67)


serve is a function that performs operations based on the provided parameters and returns ().


```go
func serve(()) ()
```


📍 *Расположение:* `test/images/agnhost/mtlsserver/server.go:67`




## test/images/agnhost/net/main.go


📄 Исходный файл: `test/images/agnhost/net/main.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [executeRunner](#executerunner-testimagesagnhostnetmaingo132) `:132`

- 🔗 [handleRunRequest](#handlerunrequest-testimagesagnhostnetmaingo152) `:152`

- 🔗 [init](#init-testimagesagnhostnetmaingo75) `:75`

- 🔗 [main](#main-testimagesagnhostnetmaingo89) `:89`

- 🔗 [makeRunnerMap](#makerunnermap-testimagesagnhostnetmaingo124) `:124`


</details>


[function] name: executeRunner file: test/images/agnhost/net/main.go:132 returns_error: да description: —


### executeRunner (test/images/agnhost/net/main.go:132)


executeRunner is a function that performs operations based on the provided parameters and may return an error.


```go
func executeRunner((logOutput, error)) (logOutput, error)
```


**Тип ответа:** logOutput


```json
{
  "b": {}
}
```


*Определено в:* `test/images/agnhost/net/main.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `logOutput`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/net/main.go:132`



---


[function] name: handleRunRequest file: test/images/agnhost/net/main.go:152 returns_error: нет description: handleRunRequest handles a request JSON to the network tester.


### handleRunRequest (test/images/agnhost/net/main.go:152)


handleRunRequest handles a request JSON to the network tester.


```go
func handleRunRequest((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/net/main.go:152`



---


[function] name: init file: test/images/agnhost/net/main.go:75 returns_error: нет description: —


### init (test/images/agnhost/net/main.go:75)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/net/main.go:75`



---


[function] name: main file: test/images/agnhost/net/main.go:89 returns_error: нет description: —


### main (test/images/agnhost/net/main.go:89)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/net/main.go:89`



---


[function] name: makeRunnerMap file: test/images/agnhost/net/main.go:124 returns_error: нет description: —


### makeRunnerMap (test/images/agnhost/net/main.go:124)


makeRunnerMap is a function that performs operations based on the provided parameters and returns ().


```go
func makeRunnerMap(()) ()
```


📍 *Расположение:* `test/images/agnhost/net/main.go:124`




## test/images/agnhost/net/nat/closewait.go


📄 Исходный файл: `test/images/agnhost/net/nat/closewait.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [NewCloseWaitClient](#newclosewaitclient-testimagesagnhostnetnatclosewaitgo134) `:134`

- 🔗 [NewCloseWaitServer](#newclosewaitserver-testimagesagnhostnetnatclosewaitgo58) `:58`

- 🔗 [NewOptions](#newoptions-testimagesagnhostnetnatclosewaitgo63) `:63`

- 🔗 [NewOptions](#newoptions-testimagesagnhostnetnatclosewaitgo139) `:139`

- 🔗 [Run](#run-testimagesagnhostnetnatclosewaitgo68) `:68`

- 🔗 [Run](#run-testimagesagnhostnetnatclosewaitgo144) `:144`


</details>


[function] name: NewCloseWaitClient file: test/images/agnhost/net/nat/closewait.go:134 returns_error: нет description: NewCloseWaitClient creates a new runner


### NewCloseWaitClient (test/images/agnhost/net/nat/closewait.go:134)


NewCloseWaitClient creates a new runner


```go
func NewCloseWaitClient(()) ()
```


📍 *Расположение:* `test/images/agnhost/net/nat/closewait.go:134`



---


[function] name: NewCloseWaitServer file: test/images/agnhost/net/nat/closewait.go:58 returns_error: нет description: NewCloseWaitServer returns a new Runner.


### NewCloseWaitServer (test/images/agnhost/net/nat/closewait.go:58)


NewCloseWaitServer returns a new Runner.


```go
func NewCloseWaitServer(()) ()
```


📍 *Расположение:* `test/images/agnhost/net/nat/closewait.go:58`



---


[function] name: NewOptions file: test/images/agnhost/net/nat/closewait.go:63 returns_error: нет description: NewOptions allocates new options structure.


### NewOptions (test/images/agnhost/net/nat/closewait.go:63)


NewOptions allocates new options structure.


```go
func (server *closeWaitServer) NewOptions(()) ()
```


📍 *Расположение:* `test/images/agnhost/net/nat/closewait.go:63`



---


[function] name: NewOptions file: test/images/agnhost/net/nat/closewait.go:139 returns_error: нет description: NewOptions allocates new options structure.


### NewOptions (test/images/agnhost/net/nat/closewait.go:139)


NewOptions allocates new options structure.


```go
func (client *closeWaitClient) NewOptions(()) ()
```


📍 *Расположение:* `test/images/agnhost/net/nat/closewait.go:139`



---


[function] name: Run file: test/images/agnhost/net/nat/closewait.go:68 returns_error: нет description: Run the server-side of the test.


### Run (test/images/agnhost/net/nat/closewait.go:68)


Run the server-side of the test.


```go
func (server *closeWaitServer) Run((logger *log.Logger, rawOptions interface{})) (logger *log.Logger, rawOptions interface{})
```


**Тип запроса:** log.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** log.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** rawOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/images/agnhost/net/nat/closewait.go:68`



---


[function] name: Run file: test/images/agnhost/net/nat/closewait.go:144 returns_error: нет description: Run the client.m


### Run (test/images/agnhost/net/nat/closewait.go:144)


Run the client.m


```go
func (client *closeWaitClient) Run((logger *log.Logger, rawOptions interface{})) (logger *log.Logger, rawOptions interface{})
```


**Тип запроса:** log.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** log.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** rawOptions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/images/agnhost/net/nat/closewait.go:144`




## test/images/agnhost/netexec/netexec.go


📄 Исходный файл: `test/images/agnhost/netexec/netexec.go`


<details open>
<summary><b>Функции в этом файле (28)</b></summary>


- 🔗 [addRoutes](#addroutes-testimagesagnhostnetexecnetexecgo211) `:211`

- 🔗 [assertNoError](#assertnoerror-testimagesagnhostnetexecnetexecgo732) `:732`

- 🔗 [clientIPHandler](#clientiphandler-testimagesagnhostnetexecnetexecgo270) `:270`

- 🔗 [createHTTPClient](#createhttpclient-testimagesagnhostnetexecnetexecgo465) `:465`

- 🔗 [dialHTTP](#dialhttp-testimagesagnhostnetexecnetexecgo450) `:450`

- 🔗 [dialHandler](#dialhandler-testimagesagnhostnetexecnetexecgo376) `:376`

- 🔗 [dialSCTP](#dialsctp-testimagesagnhostnetexecnetexecgo494) `:494`

- 🔗 [dialUDP](#dialudp-testimagesagnhostnetexecnetexecgo473) `:473`

- 🔗 [echoHandler](#echohandler-testimagesagnhostnetexecnetexecgo255) `:255`

- 🔗 [exitHandler](#exithandler-testimagesagnhostnetexecnetexecgo301) `:301`

- 🔗 [getHostName](#gethostname-testimagesagnhostnetexecnetexecgo726) `:726`

- 🔗 [headerHandler](#headerhandler-testimagesagnhostnetexecnetexecgo280) `:280`

- 🔗 [healthzHandler](#healthzhandler-testimagesagnhostnetexecnetexecgo336) `:336`

- 🔗 [hostNameHandler](#hostnamehandler-testimagesagnhostnetexecnetexecgo603) `:603`

- 🔗 [hostnameHandler](#hostnamehandler-testimagesagnhostnetexecnetexecgo329) `:329`

- 🔗 [init](#init-testimagesagnhostnetexecnetexecgo136) `:136`

- 🔗 [main](#main-testimagesagnhostnetexecnetexecgo149) `:149`

- 🔗 [parseAddresses](#parseaddresses-testimagesagnhostnetexecnetexecgo738) `:738`

- 🔗 [readyzHandler](#readyzhandler-testimagesagnhostnetexecnetexecgo347) `:347`

- 🔗 [redirectHandler](#redirecthandler-testimagesagnhostnetexecnetexecgo608) `:608`

- 🔗 [rootHandler](#roothandler-testimagesagnhostnetexecnetexecgo250) `:250`

- 🔗 [serverPortHandler](#serverporthandler-testimagesagnhostnetexecnetexecgo275) `:275`

- 🔗 [shellHandler](#shellhandler-testimagesagnhostnetexecnetexecgo515) `:515`

- 🔗 [shutdownHandler](#shutdownhandler-testimagesagnhostnetexecnetexecgo371) `:371`

- 🔗 [startSCTPServer](#startsctpserver-testimagesagnhostnetexecnetexecgo672) `:672`

- 🔗 [startServer](#startserver-testimagesagnhostnetexecnetexecgo230) `:230`

- 🔗 [startUDPServer](#startudpserver-testimagesagnhostnetexecnetexecgo625) `:625`

- 🔗 [uploadHandler](#uploadhandler-testimagesagnhostnetexecnetexecgo538) `:538`


</details>


[function] name: addRoutes file: test/images/agnhost/netexec/netexec.go:211 returns_error: нет description: —


### addRoutes (test/images/agnhost/netexec/netexec.go:211)


addRoutes is a function that performs operations based on the provided parameters and returns (mux *http.ServeMux, sigTermReceived chan struct{}, exitCh chan shutdownRequest).


```go
func addRoutes((mux *http.ServeMux, sigTermReceived chan struct{}, exitCh chan shutdownRequest)) (mux *http.ServeMux, sigTermReceived chan struct{}, exitCh chan shutdownRequest)
```


**Тип запроса:** http.ServeMux


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** mux


```json
{
  "merger": {},
  "sourceLock": {},
  "sources": {}
}
```


*Определено в:* `pkg/kubelet/config/mux.go`


**Тип ответа:** http.ServeMux


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sigTermReceived


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


**Тип ответа:** exitCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** shutdownRequest


```json
{
  "code": 0,
  "timeout": {}
}
```


*Определено в:* `test/images/agnhost/netexec/netexec.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:211`



---


[function] name: assertNoError file: test/images/agnhost/netexec/netexec.go:732 returns_error: да description: —


### assertNoError (test/images/agnhost/netexec/netexec.go:732)


assertNoError is a function that performs operations based on the provided parameters and may return an error.


```go
func assertNoError((err error, detail string)) (err error, detail string)
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


**Тип ответа:** detail


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`, `detail string`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:732`



---


[function] name: clientIPHandler file: test/images/agnhost/netexec/netexec.go:270 returns_error: нет description: —


### clientIPHandler (test/images/agnhost/netexec/netexec.go:270)


clientIPHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func clientIPHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:270`



---


[function] name: createHTTPClient file: test/images/agnhost/netexec/netexec.go:465 returns_error: нет description: —


### createHTTPClient (test/images/agnhost/netexec/netexec.go:465)


createHTTPClient is a function that performs operations based on the provided parameters and returns (transport *http.Transport).


```go
func createHTTPClient((transport *http.Transport)) (transport *http.Transport)
```


**Тип запроса:** http.Transport


```json
{
  "Scheme": "string",
  "Host": "string",
  "PathPrepend": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/proxy/transport.go`


**Тип ответа:** transport


```json
{
  "m": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/prometheus/restclient/metrics.go`


**Тип ответа:** http.Transport


```json
{
  "Scheme": "string",
  "Host": "string",
  "PathPrepend": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/proxy/transport.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:465`



---


[function] name: dialHTTP file: test/images/agnhost/netexec/netexec.go:450 returns_error: да description: —


### dialHTTP (test/images/agnhost/netexec/netexec.go:450)


dialHTTP is a function that performs operations based on the provided parameters and may return an error.


```go
func dialHTTP((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:450`



---


[function] name: dialHandler file: test/images/agnhost/netexec/netexec.go:376 returns_error: нет description: —


### dialHandler (test/images/agnhost/netexec/netexec.go:376)


dialHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func dialHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:376`



---


[function] name: dialSCTP file: test/images/agnhost/netexec/netexec.go:494 returns_error: да description: —


### dialSCTP (test/images/agnhost/netexec/netexec.go:494)


dialSCTP is a function that performs operations based on the provided parameters and may return an error.


```go
func dialSCTP((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:494`



---


[function] name: dialUDP file: test/images/agnhost/netexec/netexec.go:473 returns_error: да description: —


### dialUDP (test/images/agnhost/netexec/netexec.go:473)


dialUDP is a function that performs operations based on the provided parameters and may return an error.


```go
func dialUDP((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:473`



---


[function] name: echoHandler file: test/images/agnhost/netexec/netexec.go:255 returns_error: нет description: —


### echoHandler (test/images/agnhost/netexec/netexec.go:255)


echoHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func echoHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:255`



---


[function] name: exitHandler file: test/images/agnhost/netexec/netexec.go:301 returns_error: нет description: —


### exitHandler (test/images/agnhost/netexec/netexec.go:301)


exitHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request, exitCh chan<- shutdownRequest).


```go
func exitHandler((w http.ResponseWriter, r *http.Request, exitCh chan<- shutdownRequest)) (w http.ResponseWriter, r *http.Request, exitCh chan<- shutdownRequest)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** exitCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** shutdownRequest


```json
{
  "code": 0,
  "timeout": {}
}
```


*Определено в:* `test/images/agnhost/netexec/netexec.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:301`



---


[function] name: getHostName file: test/images/agnhost/netexec/netexec.go:726 returns_error: нет description: —


### getHostName (test/images/agnhost/netexec/netexec.go:726)


getHostName is a function that performs operations based on the provided parameters and returns ().


```go
func getHostName(()) ()
```


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:726`



---


[function] name: headerHandler file: test/images/agnhost/netexec/netexec.go:280 returns_error: нет description: —


### headerHandler (test/images/agnhost/netexec/netexec.go:280)


headerHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func headerHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:280`



---


[function] name: healthzHandler file: test/images/agnhost/netexec/netexec.go:336 returns_error: нет description: healthHandler response with a 200 if the UDP server is ready. It also serves
as a health check of the HTTP server by vir


### healthzHandler (test/images/agnhost/netexec/netexec.go:336)


healthHandler response with a 200 if the UDP server is ready. It also serves
as a health check of the HTTP server by virtue of being a HTTP handler.


```go
func healthzHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:336`



---


[function] name: hostNameHandler file: test/images/agnhost/netexec/netexec.go:603 returns_error: нет description: —


### hostNameHandler (test/images/agnhost/netexec/netexec.go:603)


hostNameHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func hostNameHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:603`



---


[function] name: hostnameHandler file: test/images/agnhost/netexec/netexec.go:329 returns_error: нет description: —


### hostnameHandler (test/images/agnhost/netexec/netexec.go:329)


hostnameHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func hostnameHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:329`



---


[function] name: init file: test/images/agnhost/netexec/netexec.go:136 returns_error: нет description: —


### init (test/images/agnhost/netexec/netexec.go:136)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:136`



---


[function] name: main file: test/images/agnhost/netexec/netexec.go:149 returns_error: нет description: —


### main (test/images/agnhost/netexec/netexec.go:149)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:149`



---


[function] name: parseAddresses file: test/images/agnhost/netexec/netexec.go:738 returns_error: да description: —


### parseAddresses (test/images/agnhost/netexec/netexec.go:738)


parseAddresses is a function that performs operations based on the provided parameters and may return an error.


```go
func parseAddresses(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:738`



---


[function] name: readyzHandler file: test/images/agnhost/netexec/netexec.go:347 returns_error: нет description: readyzHandler response with a 200 if the UDP server is ready. It serves as a readyz that will return a 503
once a sig-te


### readyzHandler (test/images/agnhost/netexec/netexec.go:347)


readyzHandler response with a 200 if the UDP server is ready. It serves as a readyz that will return a 503
once a sig-term has been received.   This allows for graceful removal from endpoints during a pod delete flow.


```go
func readyzHandler((sigTermReceived chan struct{})) (sigTermReceived chan struct{})
```


**Тип ответа:** sigTermReceived


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


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:347`



---


[function] name: redirectHandler file: test/images/agnhost/netexec/netexec.go:608 returns_error: нет description: —


### redirectHandler (test/images/agnhost/netexec/netexec.go:608)


redirectHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func redirectHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:608`



---


[function] name: rootHandler file: test/images/agnhost/netexec/netexec.go:250 returns_error: нет description: —


### rootHandler (test/images/agnhost/netexec/netexec.go:250)


rootHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func rootHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:250`



---


[function] name: serverPortHandler file: test/images/agnhost/netexec/netexec.go:275 returns_error: нет description: —


### serverPortHandler (test/images/agnhost/netexec/netexec.go:275)


serverPortHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serverPortHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:275`



---


[function] name: shellHandler file: test/images/agnhost/netexec/netexec.go:515 returns_error: нет description: —


### shellHandler (test/images/agnhost/netexec/netexec.go:515)


shellHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func shellHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:515`



---


[function] name: shutdownHandler file: test/images/agnhost/netexec/netexec.go:371 returns_error: нет description: —


### shutdownHandler (test/images/agnhost/netexec/netexec.go:371)


shutdownHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func shutdownHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:371`



---


[function] name: startSCTPServer file: test/images/agnhost/netexec/netexec.go:672 returns_error: нет description: sctp server supports the hostName, echo and clientIP commands.


### startSCTPServer (test/images/agnhost/netexec/netexec.go:672)


sctp server supports the hostName, echo and clientIP commands.


```go
func startSCTPServer((sctpPort int)) (sctpPort int)
```


**Тип ответа:** sctpPort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:672`



---


[function] name: startServer file: test/images/agnhost/netexec/netexec.go:230 returns_error: да description: —


### startServer (test/images/agnhost/netexec/netexec.go:230)


startServer is a function that performs operations based on the provided parameters and may return an error.


```go
func startServer((server *http.Server, exitCh chan shutdownRequest, fn func() error)) (server *http.Server, exitCh chan shutdownRequest, fn func() error)
```


**Тип запроса:** http.Server


```json
{
  "flagz": {},
  "auth": {},
  "host": {},
  "restfulCont": {},
  "metricsBuckets": {},
  "metricsMethodBuckets": {},
  "resourceAnalyzer": {},
  "extendedCheckers": []
}
```


*Определено в:* `pkg/kubelet/server/server.go`


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


**Тип ответа:** http.Server


```json
{
  "flagz": {},
  "auth": {},
  "host": {},
  "restfulCont": {},
  "metricsBuckets": {},
  "metricsMethodBuckets": {},
  "resourceAnalyzer": {},
  "extendedCheckers": []
}
```


*Определено в:* `pkg/kubelet/server/server.go`


**Тип ответа:** exitCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Тип ответа:** shutdownRequest


```json
{
  "code": 0,
  "timeout": {}
}
```


*Определено в:* `test/images/agnhost/netexec/netexec.go`


**Тип ответа:** fn


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `server *http.Server`, `exitCh chan shutdownRequest`, `fn func() error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:230`



---


[function] name: startUDPServer file: test/images/agnhost/netexec/netexec.go:625 returns_error: нет description: udp server supports the hostName, echo and clientIP commands.


### startUDPServer (test/images/agnhost/netexec/netexec.go:625)


udp server supports the hostName, echo and clientIP commands.


```go
func startUDPServer((address string, udpPort int)) (address string, udpPort int)
```


**Тип ответа:** address


```json
{
  "ip": "string",
  "uid": {}
}
```


*Определено в:* `pkg/api/v1/endpoints/util.go`


**Тип ответа:** udpPort


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:625`



---


[function] name: uploadHandler file: test/images/agnhost/netexec/netexec.go:538 returns_error: нет description: —


### uploadHandler (test/images/agnhost/netexec/netexec.go:538)


uploadHandler is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func uploadHandler((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/netexec/netexec.go:538`




## test/images/agnhost/nettest/nettest.go


📄 Исходный файл: `test/images/agnhost/nettest/nettest.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Logf](#logf-testimagesagnhostnettestnettestgo184) `:184`

- 🔗 [appendErr](#appenderr-testimagesagnhostnettestnettestgo175) `:175`

- 🔗 [appendSuccessfulSend](#appendsuccessfulsend-testimagesagnhostnettestnettestgo194) `:194`

- 🔗 [contactOthers](#contactothers-testimagesagnhostnettestnettestgo250) `:250`

- 🔗 [contactSingle](#contactsingle-testimagesagnhostnettestnettestgo337) `:337`

- 🔗 [doneContactingPeers](#donecontactingpeers-testimagesagnhostnettestnettestgo110) `:110`

- 🔗 [getWebserverEndpoints](#getwebserverendpoints-testimagesagnhostnettestnettestgo318) `:318`

- 🔗 [init](#init-testimagesagnhostnettestnettestgo86) `:86`

- 🔗 [main](#main-testimagesagnhostnettestnettestgo208) `:208`

- 🔗 [serveRead](#serveread-testimagesagnhostnettestnettestgo134) `:134`

- 🔗 [serveStatus](#servestatus-testimagesagnhostnettestnettestgo117) `:117`

- 🔗 [serveWrite](#servewrite-testimagesagnhostnettestnettestgo156) `:156`


</details>


[function] name: Logf file: test/images/agnhost/nettest/nettest.go:184 returns_error: нет description: Logf writes to the log message list. s must not be locked.
s's Log member will drop an old message if it would otherwise


### Logf (test/images/agnhost/nettest/nettest.go:184)


Logf writes to the log message list. s must not be locked.
s's Log member will drop an old message if it would otherwise
become longer than 500 messages.


```go
func (s *State) Logf((format string, args ...interface{})) (format string, args ...interface{})
```


**Тип ответа:** format


```json
{
  "availableOnNodes": null,
  "allocation": null
}
```


*Определено в:* `pkg/scheduler/framework/plugins/dynamicresources/dynamicresources.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:184`



---


[function] name: appendErr file: test/images/agnhost/nettest/nettest.go:175 returns_error: да description: appendErr adds err to the list, if err is not nil. s must be locked.


### appendErr (test/images/agnhost/nettest/nettest.go:175)


appendErr adds err to the list, if err is not nil. s must be locked.


```go
func (s *State) appendErr((err error)) (err error)
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


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:175`



---


[function] name: appendSuccessfulSend file: test/images/agnhost/nettest/nettest.go:194 returns_error: нет description: s must not be locked


### appendSuccessfulSend (test/images/agnhost/nettest/nettest.go:194)


s must not be locked


```go
func (s *State) appendSuccessfulSend((toHostname string)) (toHostname string)
```


**Тип ответа:** toHostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:194`



---


[function] name: contactOthers file: test/images/agnhost/nettest/nettest.go:250 returns_error: нет description: Find all sibling pods in the service and post to their /write handler.


### contactOthers (test/images/agnhost/nettest/nettest.go:250)


Find all sibling pods in the service and post to their /write handler.


```go
func contactOthers((state *State)) (state *State)
```


**Тип запроса:** State


```json
{
  "Received": {}
}
```


*Определено в:* `test/e2e/node/pre_stop.go`


**Тип ответа:** state


```json
{
  "StartTime": {},
  "EndTime": {}
}
```


*Определено в:* `pkg/kubelet/nodeshutdown/storage.go`


**Тип ответа:** State


```json
{
  "Received": {}
}
```


*Определено в:* `test/e2e/node/pre_stop.go`


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:250`



---


[function] name: contactSingle file: test/images/agnhost/nettest/nettest.go:337 returns_error: нет description: contactSingle dials the address 'e' and tries to POST to its /write address.


### contactSingle (test/images/agnhost/nettest/nettest.go:337)


contactSingle dials the address 'e' and tries to POST to its /write address.


```go
func contactSingle((e string, state *State)) (e string, state *State)
```


**Тип запроса:** State


```json
{
  "Received": {}
}
```


*Определено в:* `test/e2e/node/pre_stop.go`


**Тип ответа:** e


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


**Тип ответа:** state


```json
{
  "StartTime": {},
  "EndTime": {}
}
```


*Определено в:* `pkg/kubelet/nodeshutdown/storage.go`


**Тип ответа:** State


```json
{
  "Received": {}
}
```


*Определено в:* `test/e2e/node/pre_stop.go`


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:337`



---


[function] name: doneContactingPeers file: test/images/agnhost/nettest/nettest.go:110 returns_error: нет description: —


### doneContactingPeers (test/images/agnhost/nettest/nettest.go:110)


doneContactingPeers is a method that performs operations based on the provided parameters and returns ().


```go
func (s *State) doneContactingPeers(()) ()
```


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:110`



---


[function] name: getWebserverEndpoints file: test/images/agnhost/nettest/nettest.go:318 returns_error: нет description: getWebserverEndpoints returns the webserver endpoints as a set of String, each in the format like "http://{ip}:{port}"


### getWebserverEndpoints (test/images/agnhost/nettest/nettest.go:318)


getWebserverEndpoints returns the webserver endpoints as a set of String, each in the format like "http://{ip}:{port}"


```go
func getWebserverEndpoints((client clientset.Interface)) (client clientset.Interface)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:318`



---


[function] name: init file: test/images/agnhost/nettest/nettest.go:86 returns_error: нет description: —


### init (test/images/agnhost/nettest/nettest.go:86)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:86`



---


[function] name: main file: test/images/agnhost/nettest/nettest.go:208 returns_error: нет description: —


### main (test/images/agnhost/nettest/nettest.go:208)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:208`



---


[function] name: serveRead file: test/images/agnhost/nettest/nettest.go:134 returns_error: нет description: serveRead writes our json encoded state


### serveRead (test/images/agnhost/nettest/nettest.go:134)


serveRead writes our json encoded state


```go
func (s *State) serveRead((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:134`



---


[function] name: serveStatus file: test/images/agnhost/nettest/nettest.go:117 returns_error: нет description: serveStatus returns "pass", "running", or "fail".


### serveStatus (test/images/agnhost/nettest/nettest.go:117)


serveStatus returns "pass", "running", or "fail".


```go
func (s *State) serveStatus((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:117`



---


[function] name: serveWrite file: test/images/agnhost/nettest/nettest.go:156 returns_error: нет description: serveWrite records the contact in our state.


### serveWrite (test/images/agnhost/nettest/nettest.go:156)


serveWrite records the contact in our state.


```go
func (s *State) serveWrite((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/nettest/nettest.go:156`




## test/images/agnhost/no-snat-test-proxy/main.go


📄 Исходный файл: `test/images/agnhost/no-snat-test-proxy/main.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [Run](#run-testimagesagnhostno-snat-test-proxymaingo64) `:64`

- 🔗 [checknosnat](#checknosnat-testimagesagnhostno-snat-test-proxymaingo76) `:76`

- 🔗 [checknosnatURL](#checknosnaturl-testimagesagnhostno-snat-test-proxymaingo72) `:72`

- 🔗 [init](#init-testimagesagnhostno-snat-test-proxymaingo40) `:40`

- 🔗 [main](#main-testimagesagnhostno-snat-test-proxymaingo50) `:50`


</details>


[function] name: Run file: test/images/agnhost/no-snat-test-proxy/main.go:64 returns_error: нет description: —


### Run (test/images/agnhost/no-snat-test-proxy/main.go:64)


Run is a method that performs operations based on the provided parameters and returns ().


```go
func (m *masqTestProxy) Run(()) ()
```


📍 *Расположение:* `test/images/agnhost/no-snat-test-proxy/main.go:64`



---


[function] name: checknosnat file: test/images/agnhost/no-snat-test-proxy/main.go:76 returns_error: нет description: —


### checknosnat (test/images/agnhost/no-snat-test-proxy/main.go:76)


checknosnat is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, req *http.Request).


```go
func checknosnat((w http.ResponseWriter, req *http.Request)) (w http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


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


📍 *Расположение:* `test/images/agnhost/no-snat-test-proxy/main.go:76`



---


[function] name: checknosnatURL file: test/images/agnhost/no-snat-test-proxy/main.go:72 returns_error: нет description: —


### checknosnatURL (test/images/agnhost/no-snat-test-proxy/main.go:72)


checknosnatURL is a function that performs operations based on the provided parameters and returns (pip, ips string).


```go
func checknosnatURL((pip, ips string)) (pip, ips string)
```


**Тип ответа:** pip


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ips


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/no-snat-test-proxy/main.go:72`



---


[function] name: init file: test/images/agnhost/no-snat-test-proxy/main.go:40 returns_error: нет description: —


### init (test/images/agnhost/no-snat-test-proxy/main.go:40)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/no-snat-test-proxy/main.go:40`



---


[function] name: main file: test/images/agnhost/no-snat-test-proxy/main.go:50 returns_error: нет description: —


### main (test/images/agnhost/no-snat-test-proxy/main.go:50)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/no-snat-test-proxy/main.go:50`




## test/images/agnhost/no-snat-test/main.go


📄 Исходный файл: `test/images/agnhost/no-snat-test/main.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Run](#run-testimagesagnhostno-snat-testmaingo73) `:73`

- 🔗 [check](#check-testimagesagnhostno-snat-testmaingo137) `:137`

- 🔗 [init](#init-testimagesagnhostno-snat-testmaingo46) `:46`

- 🔗 [joinErrors](#joinerrors-testimagesagnhostno-snat-testmaingo103) `:103`

- 🔗 [main](#main-testimagesagnhostno-snat-testmaingo59) `:59`

- 🔗 [mkChecknosnat](#mkchecknosnat-testimagesagnhostno-snat-testmaingo112) `:112`

- 🔗 [whoami](#whoami-testimagesagnhostno-snat-testmaingo132) `:132`


</details>


[function] name: Run file: test/images/agnhost/no-snat-test/main.go:73 returns_error: нет description: —


### Run (test/images/agnhost/no-snat-test/main.go:73)


Run is a method that performs operations based on the provided parameters and returns ().


```go
func (m *masqTester) Run(()) ()
```


📍 *Расположение:* `test/images/agnhost/no-snat-test/main.go:73`



---


[function] name: check file: test/images/agnhost/no-snat-test/main.go:137 returns_error: нет description: Queries ip/whoami and compares response to pip, uses nip to differentiate SNAT from other potential failure modes


### check (test/images/agnhost/no-snat-test/main.go:137)


Queries ip/whoami and compares response to pip, uses nip to differentiate SNAT from other potential failure modes


```go
func check((ip string, pip string, nip string)) (ip string, pip string, nip string)
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


**Тип ответа:** pip


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nip


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/no-snat-test/main.go:137`



---


[function] name: init file: test/images/agnhost/no-snat-test/main.go:46 returns_error: нет description: —


### init (test/images/agnhost/no-snat-test/main.go:46)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/no-snat-test/main.go:46`



---


[function] name: joinErrors file: test/images/agnhost/no-snat-test/main.go:103 returns_error: да description: —


### joinErrors (test/images/agnhost/no-snat-test/main.go:103)


joinErrors is a function that performs operations based on the provided parameters and may return an error.


```go
func joinErrors((errs []error, sep string)) (errs []error, sep string)
```


**Тип ответа:** errs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** sep


```json
{
  "Delegate": {},
  "Ready": false
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/get/get.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `errs []error`, `sep string`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/no-snat-test/main.go:103`



---


[function] name: main file: test/images/agnhost/no-snat-test/main.go:59 returns_error: нет description: —


### main (test/images/agnhost/no-snat-test/main.go:59)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/no-snat-test/main.go:59`



---


[function] name: mkChecknosnat file: test/images/agnhost/no-snat-test/main.go:112 returns_error: нет description: Builds checknosnat handler, using pod and node ip of current location


### mkChecknosnat (test/images/agnhost/no-snat-test/main.go:112)


Builds checknosnat handler, using pod and node ip of current location


```go
func mkChecknosnat((pip string, nip string)) (pip string, nip string)
```


**Тип ответа:** pip


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** nip


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/no-snat-test/main.go:112`



---


[function] name: whoami file: test/images/agnhost/no-snat-test/main.go:132 returns_error: нет description: Writes the req.RemoteAddr into the response, req.RemoteAddr is the address of the incoming connection


### whoami (test/images/agnhost/no-snat-test/main.go:132)


Writes the req.RemoteAddr into the response, req.RemoteAddr is the address of the incoming connection


```go
func whoami((w http.ResponseWriter, req *http.Request)) (w http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


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


📍 *Расположение:* `test/images/agnhost/no-snat-test/main.go:132`




## test/images/agnhost/nonewprivs/main.go


📄 Исходный файл: `test/images/agnhost/nonewprivs/main.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testimagesagnhostnonewprivsmaingo35) `:35`


</details>


[function] name: main file: test/images/agnhost/nonewprivs/main.go:35 returns_error: нет description: —


### main (test/images/agnhost/nonewprivs/main.go:35)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/nonewprivs/main.go:35`




## test/images/agnhost/openidmetadata/openidmetadata.go


📄 Исходный файл: `test/images/agnhost/openidmetadata/openidmetadata.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [String](#string-testimagesagnhostopenidmetadataopenidmetadatago160) `:160`

- 🔗 [ensureWindowsDNSAvailability](#ensurewindowsdnsavailability-testimagesagnhostopenidmetadataopenidmetadatago205) `:205`

- 🔗 [gettoken](#gettoken-testimagesagnhostopenidmetadataopenidmetadatago164) `:164`

- 🔗 [init](#init-testimagesagnhostopenidmetadataopenidmetadatago55) `:55`

- 🔗 [main](#main-testimagesagnhostopenidmetadataopenidmetadatago61) `:61`

- 🔗 [validate](#validate-testimagesagnhostopenidmetadataopenidmetadatago102) `:102`

- 🔗 [withExternalOAuth2Client](#withexternaloauth2client-testimagesagnhostopenidmetadataopenidmetadatago169) `:169`

- 🔗 [withInClusterOauth2Client](#withinclusteroauth2client-testimagesagnhostopenidmetadataopenidmetadatago180) `:180`


</details>


[function] name: String file: test/images/agnhost/openidmetadata/openidmetadata.go:160 returns_error: нет description: —


### String (test/images/agnhost/openidmetadata/openidmetadata.go:160)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (k *claims) String(()) ()
```


📍 *Расположение:* `test/images/agnhost/openidmetadata/openidmetadata.go:160`



---


[function] name: ensureWindowsDNSAvailability file: test/images/agnhost/openidmetadata/openidmetadata.go:205 returns_error: нет description: DNS can be available sometime after the container starts due to the way
networking is set up for Windows nodes with dock


### ensureWindowsDNSAvailability (test/images/agnhost/openidmetadata/openidmetadata.go:205)


DNS can be available sometime after the container starts due to the way
networking is set up for Windows nodes with dockershim as the container runtime.
In this case, we should make sure we are able to resolve the issuer before
invoking oidc.NewProvider.
See https://github.com/kubernetes/kubernetes/issues/99470 for more details.


```go
func ensureWindowsDNSAvailability((issuer string)) (issuer string)
```


**Тип ответа:** issuer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/openidmetadata/openidmetadata.go:205`



---


[function] name: gettoken file: test/images/agnhost/openidmetadata/openidmetadata.go:164 returns_error: да description: —


### gettoken (test/images/agnhost/openidmetadata/openidmetadata.go:164)


gettoken is a function that performs operations based on the provided parameters and may return an error.


```go
func gettoken((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/openidmetadata/openidmetadata.go:164`



---


[function] name: init file: test/images/agnhost/openidmetadata/openidmetadata.go:55 returns_error: нет description: —


### init (test/images/agnhost/openidmetadata/openidmetadata.go:55)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/openidmetadata/openidmetadata.go:55`



---


[function] name: main file: test/images/agnhost/openidmetadata/openidmetadata.go:61 returns_error: нет description: —


### main (test/images/agnhost/openidmetadata/openidmetadata.go:61)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/openidmetadata/openidmetadata.go:61`



---


[function] name: validate file: test/images/agnhost/openidmetadata/openidmetadata.go:102 returns_error: нет description: —


### validate (test/images/agnhost/openidmetadata/openidmetadata.go:102)


validate is a function that performs operations based on the provided parameters and returns (ctx context.Context, raw string).


```go
func validate((ctx context.Context, raw string)) (ctx context.Context, raw string)
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


**Тип ответа:** raw


```json
{
  "version": null,
  "verStr": "string",
  "isAlpha": false,
  "isBeta": false,
  "isGA": false,
  "isDeprecated": false,
  "defaultOn": false,
  "locked": false
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `test/images/agnhost/openidmetadata/openidmetadata.go:102`



---


[function] name: withExternalOAuth2Client file: test/images/agnhost/openidmetadata/openidmetadata.go:169 returns_error: да description: —


### withExternalOAuth2Client (test/images/agnhost/openidmetadata/openidmetadata.go:169)


withExternalOAuth2Client is a function that performs operations based on the provided parameters and may return an error.


```go
func withExternalOAuth2Client((context.Context, error)) (context.Context, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `context.Context`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/openidmetadata/openidmetadata.go:169`



---


[function] name: withInClusterOauth2Client file: test/images/agnhost/openidmetadata/openidmetadata.go:180 returns_error: да description: —


### withInClusterOauth2Client (test/images/agnhost/openidmetadata/openidmetadata.go:180)


withInClusterOauth2Client is a function that performs operations based on the provided parameters and may return an error.


```go
func withInClusterOauth2Client((context.Context, error)) (context.Context, error)
```


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `context.Context`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/agnhost/openidmetadata/openidmetadata.go:180`




## test/images/agnhost/pause/pause.go


📄 Исходный файл: `test/images/agnhost/pause/pause.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [pause](#pause-testimagesagnhostpausepausego37) `:37`


</details>


[function] name: pause file: test/images/agnhost/pause/pause.go:37 returns_error: нет description: —


### pause (test/images/agnhost/pause/pause.go:37)


pause is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func pause((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/pause/pause.go:37`




## test/images/agnhost/podcertificatesigner/podcertificatesigner.go


📄 Исходный файл: `test/images/agnhost/podcertificatesigner/podcertificatesigner.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-testimagesagnhostpodcertificatesignerpodcertificatesignergo47) `:47`

- 🔗 [run](#run-testimagesagnhostpodcertificatesignerpodcertificatesignergo52) `:52`


</details>


[function] name: init file: test/images/agnhost/podcertificatesigner/podcertificatesigner.go:47 returns_error: нет description: —


### init (test/images/agnhost/podcertificatesigner/podcertificatesigner.go:47)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/podcertificatesigner/podcertificatesigner.go:47`



---


[function] name: run file: test/images/agnhost/podcertificatesigner/podcertificatesigner.go:52 returns_error: нет description: —


### run (test/images/agnhost/podcertificatesigner/podcertificatesigner.go:52)


run is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func run((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/podcertificatesigner/podcertificatesigner.go:52`




## test/images/agnhost/port-forward-tester/portforwardtester.go


📄 Исходный файл: `test/images/agnhost/port-forward-tester/portforwardtester.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [getEnvInt](#getenvint-testimagesagnhostport-forward-testerportforwardtestergo43) `:43`

- 🔗 [main](#main-testimagesagnhostport-forward-testerportforwardtestergo83) `:83`


</details>


[function] name: getEnvInt file: test/images/agnhost/port-forward-tester/portforwardtester.go:43 returns_error: нет description: —


### getEnvInt (test/images/agnhost/port-forward-tester/portforwardtester.go:43)


getEnvInt is a function that performs operations based on the provided parameters and returns (name string).


```go
func getEnvInt((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/images/agnhost/port-forward-tester/portforwardtester.go:43`



---


[function] name: main file: test/images/agnhost/port-forward-tester/portforwardtester.go:83 returns_error: нет description: —


### main (test/images/agnhost/port-forward-tester/portforwardtester.go:83)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/port-forward-tester/portforwardtester.go:83`




## test/images/agnhost/porter/porter.go


📄 Исходный файл: `test/images/agnhost/porter/porter.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [init](#init-testimagesagnhostporterportergo73) `:73`

- 🔗 [main](#main-testimagesagnhostporterportergo77) `:77`

- 🔗 [serveSCTPPort](#servesctpport-testimagesagnhostporterportergo194) `:194`

- 🔗 [serveTCPPort](#servetcpport-testimagesagnhostporterportergo108) `:108`

- 🔗 [serveTLSPort](#servetlsport-testimagesagnhostporterportergo164) `:164`

- 🔗 [serveUDPPort](#serveudpport-testimagesagnhostporterportergo131) `:131`


</details>


[function] name: init file: test/images/agnhost/porter/porter.go:73 returns_error: нет description: —


### init (test/images/agnhost/porter/porter.go:73)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/porter/porter.go:73`



---


[function] name: main file: test/images/agnhost/porter/porter.go:77 returns_error: нет description: —


### main (test/images/agnhost/porter/porter.go:77)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/porter/porter.go:77`



---


[function] name: serveSCTPPort file: test/images/agnhost/porter/porter.go:194 returns_error: нет description: —


### serveSCTPPort (test/images/agnhost/porter/porter.go:194)


serveSCTPPort is a function that performs operations based on the provided parameters and returns (port, value string).


```go
func serveSCTPPort((port, value string)) (port, value string)
```


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


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `test/images/agnhost/porter/porter.go:194`



---


[function] name: serveTCPPort file: test/images/agnhost/porter/porter.go:108 returns_error: нет description: —


### serveTCPPort (test/images/agnhost/porter/porter.go:108)


serveTCPPort is a function that performs operations based on the provided parameters and returns (port, value string).


```go
func serveTCPPort((port, value string)) (port, value string)
```


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


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `test/images/agnhost/porter/porter.go:108`



---


[function] name: serveTLSPort file: test/images/agnhost/porter/porter.go:164 returns_error: нет description: —


### serveTLSPort (test/images/agnhost/porter/porter.go:164)


serveTLSPort is a function that performs operations based on the provided parameters and returns (port, value string).


```go
func serveTLSPort((port, value string)) (port, value string)
```


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


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `test/images/agnhost/porter/porter.go:164`



---


[function] name: serveUDPPort file: test/images/agnhost/porter/porter.go:131 returns_error: нет description: —


### serveUDPPort (test/images/agnhost/porter/porter.go:131)


serveUDPPort is a function that performs operations based on the provided parameters and returns (port, value string).


```go
func serveUDPPort((port, value string)) (port, value string)
```


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


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `test/images/agnhost/porter/porter.go:131`




## test/images/agnhost/resource-consumer-controller/controller.go


📄 Исходный файл: `test/images/agnhost/resource-consumer-controller/controller.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [ServeHTTP](#servehttp-testimagesagnhostresource-consumer-controllercontrollergo95) `:95`

- 🔗 [createConsumerURL](#createconsumerurl-testimagesagnhostresource-consumer-controllercontrollergo241) `:241`

- 🔗 [getDNSDomain](#getdnsdomain-testimagesagnhostresource-consumer-controllercontrollergo54) `:54`

- 🔗 [handleBumpMetric](#handlebumpmetric-testimagesagnhostresource-consumer-controllercontrollergo189) `:189`

- 🔗 [handleConsumeCPU](#handleconsumecpu-testimagesagnhostresource-consumer-controllercontrollergo123) `:123`

- 🔗 [handleConsumeMem](#handleconsumemem-testimagesagnhostresource-consumer-controllercontrollergo156) `:156`

- 🔗 [init](#init-testimagesagnhostresource-consumer-controllercontrollergo73) `:73`

- 🔗 [main](#main-testimagesagnhostresource-consumer-controllercontrollergo80) `:80`

- 🔗 [newController](#newcontroller-testimagesagnhostresource-consumer-controllercontrollergo90) `:90`

- 🔗 [sendConsumeCPURequests](#sendconsumecpurequests-testimagesagnhostresource-consumer-controllercontrollergo223) `:223`

- 🔗 [sendConsumeCustomMetric](#sendconsumecustommetric-testimagesagnhostresource-consumer-controllercontrollergo235) `:235`

- 🔗 [sendConsumeMemRequests](#sendconsumememrequests-testimagesagnhostresource-consumer-controllercontrollergo229) `:229`

- 🔗 [sendOneConsumeCPURequest](#sendoneconsumecpurequest-testimagesagnhostresource-consumer-controllercontrollergo247) `:247`

- 🔗 [sendOneConsumeCustomMetric](#sendoneconsumecustommetric-testimagesagnhostresource-consumer-controllercontrollergo275) `:275`

- 🔗 [sendOneConsumeMemRequest](#sendoneconsumememrequest-testimagesagnhostresource-consumer-controllercontrollergo261) `:261`


</details>


[function] name: ServeHTTP file: test/images/agnhost/resource-consumer-controller/controller.go:95 returns_error: нет description: —


### ServeHTTP (test/images/agnhost/resource-consumer-controller/controller.go:95)


ServeHTTP is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, req *http.Request).


```go
func (c *controller) ServeHTTP((w http.ResponseWriter, req *http.Request)) (w http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


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


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:95`



---


[function] name: createConsumerURL file: test/images/agnhost/resource-consumer-controller/controller.go:241 returns_error: нет description: —


### createConsumerURL (test/images/agnhost/resource-consumer-controller/controller.go:241)


createConsumerURL is a function that performs operations based on the provided parameters and returns (suffix string).


```go
func createConsumerURL((suffix string)) (suffix string)
```


**Тип ответа:** suffix


```json
{
  "decSuffixes": {},
  "binSuffixes": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/resource/suffix.go`


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:241`



---


[function] name: getDNSDomain file: test/images/agnhost/resource-consumer-controller/controller.go:54 returns_error: нет description: getDNSDomain walks through DNS configuration and looks for "svc.foo" record
where "foo" is currently configured DNS suff


### getDNSDomain (test/images/agnhost/resource-consumer-controller/controller.go:54)


getDNSDomain walks through DNS configuration and looks for "svc.foo" record
where "foo" is currently configured DNS suffix. Then picks that 'foo' part up
and returns to a caller.


```go
func getDNSDomain(()) ()
```


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:54`



---


[function] name: handleBumpMetric file: test/images/agnhost/resource-consumer-controller/controller.go:189 returns_error: нет description: —


### handleBumpMetric (test/images/agnhost/resource-consumer-controller/controller.go:189)


handleBumpMetric is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, query url.Values).


```go
func (c *controller) handleBumpMetric((w http.ResponseWriter, query url.Values)) (w http.ResponseWriter, query url.Values)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** query


```json
{
  "finder": {},
  "root": {},
  "queryParam": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/query_param_verifier_v3.go`


**Тип ответа:** url.Values


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:189`



---


[function] name: handleConsumeCPU file: test/images/agnhost/resource-consumer-controller/controller.go:123 returns_error: нет description: —


### handleConsumeCPU (test/images/agnhost/resource-consumer-controller/controller.go:123)


handleConsumeCPU is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, query url.Values).


```go
func (c *controller) handleConsumeCPU((w http.ResponseWriter, query url.Values)) (w http.ResponseWriter, query url.Values)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** query


```json
{
  "finder": {},
  "root": {},
  "queryParam": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/query_param_verifier_v3.go`


**Тип ответа:** url.Values


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:123`



---


[function] name: handleConsumeMem file: test/images/agnhost/resource-consumer-controller/controller.go:156 returns_error: нет description: —


### handleConsumeMem (test/images/agnhost/resource-consumer-controller/controller.go:156)


handleConsumeMem is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, query url.Values).


```go
func (c *controller) handleConsumeMem((w http.ResponseWriter, query url.Values)) (w http.ResponseWriter, query url.Values)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** query


```json
{
  "finder": {},
  "root": {},
  "queryParam": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/query_param_verifier_v3.go`


**Тип ответа:** url.Values


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:156`



---


[function] name: init file: test/images/agnhost/resource-consumer-controller/controller.go:73 returns_error: нет description: —


### init (test/images/agnhost/resource-consumer-controller/controller.go:73)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:73`



---


[function] name: main file: test/images/agnhost/resource-consumer-controller/controller.go:80 returns_error: нет description: —


### main (test/images/agnhost/resource-consumer-controller/controller.go:80)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:80`



---


[function] name: newController file: test/images/agnhost/resource-consumer-controller/controller.go:90 returns_error: нет description: —


### newController (test/images/agnhost/resource-consumer-controller/controller.go:90)


newController is a function that performs operations based on the provided parameters and returns ().


```go
func newController(()) ()
```


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:90`



---


[function] name: sendConsumeCPURequests file: test/images/agnhost/resource-consumer-controller/controller.go:223 returns_error: нет description: —


### sendConsumeCPURequests (test/images/agnhost/resource-consumer-controller/controller.go:223)


sendConsumeCPURequests is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, requests, millicores, durationSec int).


```go
func (c *controller) sendConsumeCPURequests((w http.ResponseWriter, requests, millicores, durationSec int)) (w http.ResponseWriter, requests, millicores, durationSec int)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** requests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** millicores


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:223`



---


[function] name: sendConsumeCustomMetric file: test/images/agnhost/resource-consumer-controller/controller.go:235 returns_error: нет description: —


### sendConsumeCustomMetric (test/images/agnhost/resource-consumer-controller/controller.go:235)


sendConsumeCustomMetric is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, metric string, requests, delta, durationSec int).


```go
func (c *controller) sendConsumeCustomMetric((w http.ResponseWriter, metric string, requests, delta, durationSec int)) (w http.ResponseWriter, metric string, requests, delta, durationSec int)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** metric


```json
{
  "base": {},
  "jwksURL": "string",
  "jwtIssuer": "string",
  "apiServerID": "string",
  "shouldRecordFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


**Тип ответа:** requests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** delta


```json
{
  "PushFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/undelta_store.go`


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:235`



---


[function] name: sendConsumeMemRequests file: test/images/agnhost/resource-consumer-controller/controller.go:229 returns_error: нет description: —


### sendConsumeMemRequests (test/images/agnhost/resource-consumer-controller/controller.go:229)


sendConsumeMemRequests is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, requests, megabytes, durationSec int).


```go
func (c *controller) sendConsumeMemRequests((w http.ResponseWriter, requests, megabytes, durationSec int)) (w http.ResponseWriter, requests, megabytes, durationSec int)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** requests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** megabytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:229`



---


[function] name: sendOneConsumeCPURequest file: test/images/agnhost/resource-consumer-controller/controller.go:247 returns_error: нет description: sendOneConsumeCPURequest sends POST request for cpu consumption


### sendOneConsumeCPURequest (test/images/agnhost/resource-consumer-controller/controller.go:247)


sendOneConsumeCPURequest sends POST request for cpu consumption


```go
func (c *controller) sendOneConsumeCPURequest((w http.ResponseWriter, millicores int, durationSec int)) (w http.ResponseWriter, millicores int, durationSec int)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** millicores


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:247`



---


[function] name: sendOneConsumeCustomMetric file: test/images/agnhost/resource-consumer-controller/controller.go:275 returns_error: нет description: sendOneConsumeCustomMetric sends POST request for custom metric consumption


### sendOneConsumeCustomMetric (test/images/agnhost/resource-consumer-controller/controller.go:275)


sendOneConsumeCustomMetric sends POST request for custom metric consumption


```go
func (c *controller) sendOneConsumeCustomMetric((w http.ResponseWriter, customMetricName string, delta int, durationSec int)) (w http.ResponseWriter, customMetricName string, delta int, durationSec int)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** customMetricName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** delta


```json
{
  "PushFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/undelta_store.go`


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:275`



---


[function] name: sendOneConsumeMemRequest file: test/images/agnhost/resource-consumer-controller/controller.go:261 returns_error: нет description: sendOneConsumeMemRequest sends POST request for memory consumption


### sendOneConsumeMemRequest (test/images/agnhost/resource-consumer-controller/controller.go:261)


sendOneConsumeMemRequest sends POST request for memory consumption


```go
func (c *controller) sendOneConsumeMemRequest((w http.ResponseWriter, megabytes int, durationSec int)) (w http.ResponseWriter, megabytes int, durationSec int)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** megabytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/resource-consumer-controller/controller.go:261`




## test/images/agnhost/serve-hostname/serve_hostname.go


📄 Исходный файл: `test/images/agnhost/serve-hostname/serve_hostname.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-testimagesagnhostserve-hostnameserve_hostnamego51) `:51`

- 🔗 [main](#main-testimagesagnhostserve-hostnameserve_hostnamego59) `:59`


</details>


[function] name: init file: test/images/agnhost/serve-hostname/serve_hostname.go:51 returns_error: нет description: —


### init (test/images/agnhost/serve-hostname/serve_hostname.go:51)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/serve-hostname/serve_hostname.go:51`



---


[function] name: main file: test/images/agnhost/serve-hostname/serve_hostname.go:59 returns_error: нет description: —


### main (test/images/agnhost/serve-hostname/serve_hostname.go:59)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/serve-hostname/serve_hostname.go:59`




## test/images/agnhost/tcp-reset/tcp_reset.go


📄 Исходный файл: `test/images/agnhost/tcp-reset/tcp_reset.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-testimagesagnhosttcp-resettcp_resetgo46) `:46`

- 🔗 [main](#main-testimagesagnhosttcp-resettcp_resetgo50) `:50`


</details>


[function] name: init file: test/images/agnhost/tcp-reset/tcp_reset.go:46 returns_error: нет description: —


### init (test/images/agnhost/tcp-reset/tcp_reset.go:46)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/tcp-reset/tcp_reset.go:46`



---


[function] name: main file: test/images/agnhost/tcp-reset/tcp_reset.go:50 returns_error: нет description: —


### main (test/images/agnhost/tcp-reset/tcp_reset.go:50)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/tcp-reset/tcp_reset.go:50`




## test/images/agnhost/test-webserver/test-webserver.go


📄 Исходный файл: `test/images/agnhost/test-webserver/test-webserver.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [init](#init-testimagesagnhosttest-webservertest-webservergo41) `:41`

- 🔗 [main](#main-testimagesagnhosttest-webservertest-webservergo45) `:45`


</details>


[function] name: init file: test/images/agnhost/test-webserver/test-webserver.go:41 returns_error: нет description: —


### init (test/images/agnhost/test-webserver/test-webserver.go:41)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/test-webserver/test-webserver.go:41`



---


[function] name: main file: test/images/agnhost/test-webserver/test-webserver.go:45 returns_error: нет description: —


### main (test/images/agnhost/test-webserver/test-webserver.go:45)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/test-webserver/test-webserver.go:45`




## test/images/agnhost/webhook/addlabel.go


📄 Исходный файл: `test/images/agnhost/webhook/addlabel.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [addLabel](#addlabel-testimagesagnhostwebhookaddlabelgo40) `:40`


</details>


[function] name: addLabel file: test/images/agnhost/webhook/addlabel.go:40 returns_error: нет description: Add a label {"added-label": "yes"} to the object


### addLabel (test/images/agnhost/webhook/addlabel.go:40)


Add a label {"added-label": "yes"} to the object


```go
func addLabel((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/addlabel.go:40`




## test/images/agnhost/webhook/alwaysallow.go


📄 Исходный файл: `test/images/agnhost/webhook/alwaysallow.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [alwaysAllowDelayFiveSeconds](#alwaysallowdelayfiveseconds-testimagesagnhostwebhookalwaysallowgo28) `:28`


</details>


[function] name: alwaysAllowDelayFiveSeconds file: test/images/agnhost/webhook/alwaysallow.go:28 returns_error: нет description: alwaysAllowDelayFiveSeconds sleeps for five seconds and allows all requests made to this function.


### alwaysAllowDelayFiveSeconds (test/images/agnhost/webhook/alwaysallow.go:28)


alwaysAllowDelayFiveSeconds sleeps for five seconds and allows all requests made to this function.


```go
func alwaysAllowDelayFiveSeconds((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/alwaysallow.go:28`




## test/images/agnhost/webhook/alwaysdeny.go


📄 Исходный файл: `test/images/agnhost/webhook/alwaysdeny.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [alwaysDeny](#alwaysdeny-testimagesagnhostwebhookalwaysdenygo26) `:26`


</details>


[function] name: alwaysDeny file: test/images/agnhost/webhook/alwaysdeny.go:26 returns_error: нет description: alwaysDeny all requests made to this function.


### alwaysDeny (test/images/agnhost/webhook/alwaysdeny.go:26)


alwaysDeny all requests made to this function.


```go
func alwaysDeny((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/alwaysdeny.go:26`




## test/images/agnhost/webhook/config.go


📄 Исходный файл: `test/images/agnhost/webhook/config.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [configTLS](#configtls-testimagesagnhostwebhookconfiggo31) `:31`


</details>


[function] name: configTLS file: test/images/agnhost/webhook/config.go:31 returns_error: нет description: —


### configTLS (test/images/agnhost/webhook/config.go:31)


configTLS is a function that performs operations based on the provided parameters and returns (config Config).


```go
func configTLS((config Config)) (config Config)
```


**Тип ответа:** config


```json
{
  "sleepDuration": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/record/event.go`


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/images/agnhost/webhook/config.go:31`




## test/images/agnhost/webhook/configmap.go


📄 Исходный файл: `test/images/agnhost/webhook/configmap.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [admitConfigMaps](#admitconfigmaps-testimagesagnhostwebhookconfigmapgo36) `:36`

- 🔗 [mutateConfigmaps](#mutateconfigmaps-testimagesagnhostwebhookconfigmapgo76) `:76`


</details>


[function] name: admitConfigMaps file: test/images/agnhost/webhook/configmap.go:36 returns_error: нет description: deny configmaps with specific key-value pair.


### admitConfigMaps (test/images/agnhost/webhook/configmap.go:36)


deny configmaps with specific key-value pair.


```go
func admitConfigMaps((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/configmap.go:36`



---


[function] name: mutateConfigmaps file: test/images/agnhost/webhook/configmap.go:76 returns_error: нет description: —


### mutateConfigmaps (test/images/agnhost/webhook/configmap.go:76)


mutateConfigmaps is a function that performs operations based on the provided parameters and returns (ar v1.AdmissionReview).


```go
func mutateConfigmaps((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/configmap.go:76`




## test/images/agnhost/webhook/convert.go


📄 Исходный файл: `test/images/agnhost/webhook/convert.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [convertAdmissionRequestToV1](#convertadmissionrequesttov1-testimagesagnhostwebhookconvertgo25) `:25`

- 🔗 [convertAdmissionRequestToV1beta1](#convertadmissionrequesttov1beta1-testimagesagnhostwebhookconvertgo45) `:45`

- 🔗 [convertAdmissionResponseToV1](#convertadmissionresponsetov1-testimagesagnhostwebhookconvertgo65) `:65`

- 🔗 [convertAdmissionResponseToV1beta1](#convertadmissionresponsetov1beta1-testimagesagnhostwebhookconvertgo82) `:82`

- 🔗 [toV1AdmissionResponse](#tov1admissionresponse-testimagesagnhostwebhookconvertgo99) `:99`


</details>


[function] name: convertAdmissionRequestToV1 file: test/images/agnhost/webhook/convert.go:25 returns_error: нет description: —


### convertAdmissionRequestToV1 (test/images/agnhost/webhook/convert.go:25)


convertAdmissionRequestToV1 is a function that performs operations based on the provided parameters and returns (r *v1beta1.AdmissionRequest).


```go
func convertAdmissionRequestToV1((r *v1beta1.AdmissionRequest)) (r *v1beta1.AdmissionRequest)
```


**Тип запроса:** v1beta1.AdmissionRequest


```json
{
  "UID": {},
  "Kind": {},
  "Resource": {},
  "SubResource": "string",
  "RequestKind": null,
  "RequestResource": null,
  "RequestSubResource": "string",
  "Name": "string",
  "Namespace": "string",
  "Operation": {},
  "UserInfo": {},
  "Object": {},
  "OldObject": {},
  "DryRun": false,
  "Options": {}
}
```


*Определено в:* `pkg/apis/admission/types.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** v1beta1.AdmissionRequest


```json
{
  "UID": {},
  "Kind": {},
  "Resource": {},
  "SubResource": "string",
  "RequestKind": null,
  "RequestResource": null,
  "RequestSubResource": "string",
  "Name": "string",
  "Namespace": "string",
  "Operation": {},
  "UserInfo": {},
  "Object": {},
  "OldObject": {},
  "DryRun": false,
  "Options": {}
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/convert.go:25`



---


[function] name: convertAdmissionRequestToV1beta1 file: test/images/agnhost/webhook/convert.go:45 returns_error: нет description: —


### convertAdmissionRequestToV1beta1 (test/images/agnhost/webhook/convert.go:45)


convertAdmissionRequestToV1beta1 is a function that performs operations based on the provided parameters and returns (r *v1.AdmissionRequest).


```go
func convertAdmissionRequestToV1beta1((r *v1.AdmissionRequest)) (r *v1.AdmissionRequest)
```


**Тип запроса:** v1.AdmissionRequest


```json
{
  "UID": {},
  "Kind": {},
  "Resource": {},
  "SubResource": "string",
  "RequestKind": null,
  "RequestResource": null,
  "RequestSubResource": "string",
  "Name": "string",
  "Namespace": "string",
  "Operation": {},
  "UserInfo": {},
  "Object": {},
  "OldObject": {},
  "DryRun": false,
  "Options": {}
}
```


*Определено в:* `pkg/apis/admission/types.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** v1.AdmissionRequest


```json
{
  "UID": {},
  "Kind": {},
  "Resource": {},
  "SubResource": "string",
  "RequestKind": null,
  "RequestResource": null,
  "RequestSubResource": "string",
  "Name": "string",
  "Namespace": "string",
  "Operation": {},
  "UserInfo": {},
  "Object": {},
  "OldObject": {},
  "DryRun": false,
  "Options": {}
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/convert.go:45`



---


[function] name: convertAdmissionResponseToV1 file: test/images/agnhost/webhook/convert.go:65 returns_error: нет description: —


### convertAdmissionResponseToV1 (test/images/agnhost/webhook/convert.go:65)


convertAdmissionResponseToV1 is a function that performs operations based on the provided parameters and returns (r *v1beta1.AdmissionResponse).


```go
func convertAdmissionResponseToV1((r *v1beta1.AdmissionResponse)) (r *v1beta1.AdmissionResponse)
```


**Тип запроса:** v1beta1.AdmissionResponse


```json
{
  "UID": {},
  "Allowed": false,
  "Result": null,
  "Patch": [],
  "PatchType": null,
  "AuditAnnotations": {},
  "Warnings": []
}
```


*Определено в:* `pkg/apis/admission/types.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** v1beta1.AdmissionResponse


```json
{
  "UID": {},
  "Allowed": false,
  "Result": null,
  "Patch": [],
  "PatchType": null,
  "AuditAnnotations": {},
  "Warnings": []
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/convert.go:65`



---


[function] name: convertAdmissionResponseToV1beta1 file: test/images/agnhost/webhook/convert.go:82 returns_error: нет description: —


### convertAdmissionResponseToV1beta1 (test/images/agnhost/webhook/convert.go:82)


convertAdmissionResponseToV1beta1 is a function that performs operations based on the provided parameters and returns (r *v1.AdmissionResponse).


```go
func convertAdmissionResponseToV1beta1((r *v1.AdmissionResponse)) (r *v1.AdmissionResponse)
```


**Тип запроса:** v1.AdmissionResponse


```json
{
  "UID": {},
  "Allowed": false,
  "Result": null,
  "Patch": [],
  "PatchType": null,
  "AuditAnnotations": {},
  "Warnings": []
}
```


*Определено в:* `pkg/apis/admission/types.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** v1.AdmissionResponse


```json
{
  "UID": {},
  "Allowed": false,
  "Result": null,
  "Patch": [],
  "PatchType": null,
  "AuditAnnotations": {},
  "Warnings": []
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/convert.go:82`



---


[function] name: toV1AdmissionResponse file: test/images/agnhost/webhook/convert.go:99 returns_error: да description: —


### toV1AdmissionResponse (test/images/agnhost/webhook/convert.go:99)


toV1AdmissionResponse is a function that performs operations based on the provided parameters and may return an error.


```go
func toV1AdmissionResponse((err error)) (err error)
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


📍 *Расположение:* `test/images/agnhost/webhook/convert.go:99`




## test/images/agnhost/webhook/crd.go


📄 Исходный файл: `test/images/agnhost/webhook/crd.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [admitCRD](#admitcrd-testimagesagnhostwebhookcrdgo30) `:30`


</details>


[function] name: admitCRD file: test/images/agnhost/webhook/crd.go:30 returns_error: нет description: This function expects all CRDs submitted to it to be apiextensions.k8s.io/v1beta1 or apiextensions.k8s.io/v1.


### admitCRD (test/images/agnhost/webhook/crd.go:30)


This function expects all CRDs submitted to it to be apiextensions.k8s.io/v1beta1 or apiextensions.k8s.io/v1.


```go
func admitCRD((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/crd.go:30`




## test/images/agnhost/webhook/customresource.go


📄 Исходный файл: `test/images/agnhost/webhook/customresource.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [admitCustomResource](#admitcustomresource-testimagesagnhostwebhookcustomresourcego66) `:66`

- 🔗 [mutateCustomResource](#mutatecustomresource-testimagesagnhostwebhookcustomresourcego36) `:36`


</details>


[function] name: admitCustomResource file: test/images/agnhost/webhook/customresource.go:66 returns_error: нет description: —


### admitCustomResource (test/images/agnhost/webhook/customresource.go:66)


admitCustomResource is a function that performs operations based on the provided parameters and returns (ar v1.AdmissionReview).


```go
func admitCustomResource((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/customresource.go:66`



---


[function] name: mutateCustomResource file: test/images/agnhost/webhook/customresource.go:36 returns_error: нет description: —


### mutateCustomResource (test/images/agnhost/webhook/customresource.go:36)


mutateCustomResource is a function that performs operations based on the provided parameters and returns (ar v1.AdmissionReview).


```go
func mutateCustomResource((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/customresource.go:36`




## test/images/agnhost/webhook/main.go


📄 Исходный файл: `test/images/agnhost/webhook/main.go`


<details open>
<summary><b>Функции в этом файле (17)</b></summary>


- 🔗 [delegateV1beta1AdmitToV1](#delegatev1beta1admittov1-testimagesagnhostwebhookmaingo83) `:83`

- 🔗 [init](#init-testimagesagnhostwebhookmaingo53) `:53`

- 🔗 [main](#main-testimagesagnhostwebhookmaingo211) `:211`

- 🔗 [newDelegateToV1AdmitHandler](#newdelegatetov1admithandler-testimagesagnhostwebhookmaingo76) `:76`

- 🔗 [serve](#serve-testimagesagnhostwebhookmaingo93) `:93`

- 🔗 [serveAddLabel](#serveaddlabel-testimagesagnhostwebhookmaingo171) `:171`

- 🔗 [serveAlwaysAllowDelayFiveSeconds](#servealwaysallowdelayfiveseconds-testimagesagnhostwebhookmaingo163) `:163`

- 🔗 [serveAlwaysDeny](#servealwaysdeny-testimagesagnhostwebhookmaingo167) `:167`

- 🔗 [serveAttachingPods](#serveattachingpods-testimagesagnhostwebhookmaingo179) `:179`

- 🔗 [serveCRD](#servecrd-testimagesagnhostwebhookmaingo207) `:207`

- 🔗 [serveConfigmaps](#serveconfigmaps-testimagesagnhostwebhookmaingo191) `:191`

- 🔗 [serveCustomResource](#servecustomresource-testimagesagnhostwebhookmaingo199) `:199`

- 🔗 [serveMutateConfigmaps](#servemutateconfigmaps-testimagesagnhostwebhookmaingo195) `:195`

- 🔗 [serveMutateCustomResource](#servemutatecustomresource-testimagesagnhostwebhookmaingo203) `:203`

- 🔗 [serveMutatePods](#servemutatepods-testimagesagnhostwebhookmaingo183) `:183`

- 🔗 [serveMutatePodsSidecar](#servemutatepodssidecar-testimagesagnhostwebhookmaingo187) `:187`

- 🔗 [servePods](#servepods-testimagesagnhostwebhookmaingo175) `:175`


</details>


[function] name: delegateV1beta1AdmitToV1 file: test/images/agnhost/webhook/main.go:83 returns_error: нет description: —


### delegateV1beta1AdmitToV1 (test/images/agnhost/webhook/main.go:83)


delegateV1beta1AdmitToV1 is a function that performs operations based on the provided parameters and returns (f admitv1Func).


```go
func delegateV1beta1AdmitToV1((f admitv1Func)) (f admitv1Func)
```


**Тип ответа:** f


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** admitv1Func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/webhook/main.go:83`



---


[function] name: init file: test/images/agnhost/webhook/main.go:53 returns_error: нет description: —


### init (test/images/agnhost/webhook/main.go:53)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/webhook/main.go:53`



---


[function] name: main file: test/images/agnhost/webhook/main.go:211 returns_error: нет description: —


### main (test/images/agnhost/webhook/main.go:211)


main is a function that performs operations based on the provided parameters and returns (cmd *cobra.Command, args []string).


```go
func main((cmd *cobra.Command, args []string)) (cmd *cobra.Command, args []string)
```


**Тип запроса:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


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


**Тип ответа:** cobra.Command


```json
{
  "webhookConfigs": {},
  "controllerInitFuncConstructors": {},
  "controllerAliases": {},
  "additionalFlags": {},
  "options": null,
  "cloudInitializer": {},
  "stopCh": {},
  "cmdName": "string",
  "long": "string",
  "defaults": null
}
```


*Определено в:* `staging/src/k8s.io/cloud-provider/app/builder.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/webhook/main.go:211`



---


[function] name: newDelegateToV1AdmitHandler file: test/images/agnhost/webhook/main.go:76 returns_error: нет description: —


### newDelegateToV1AdmitHandler (test/images/agnhost/webhook/main.go:76)


newDelegateToV1AdmitHandler is a function that performs operations based on the provided parameters and returns (f admitv1Func).


```go
func newDelegateToV1AdmitHandler((f admitv1Func)) (f admitv1Func)
```


**Тип ответа:** f


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** admitv1Func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/webhook/main.go:76`



---


[function] name: serve file: test/images/agnhost/webhook/main.go:93 returns_error: нет description: serve handles the http portion of a request prior to handing to an admit
function


### serve (test/images/agnhost/webhook/main.go:93)


serve handles the http portion of a request prior to handing to an admit
function


```go
func serve((w http.ResponseWriter, r *http.Request, admit admitHandler)) (w http.ResponseWriter, r *http.Request, admit admitHandler)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** admit


```json
{
  "v1beta1": {},
  "v1": {}
}
```


*Определено в:* `test/images/agnhost/webhook/main.go`


**Тип ответа:** admitHandler


```json
{
  "v1beta1": {},
  "v1": {}
}
```


*Определено в:* `test/images/agnhost/webhook/main.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:93`



---


[function] name: serveAddLabel file: test/images/agnhost/webhook/main.go:171 returns_error: нет description: —


### serveAddLabel (test/images/agnhost/webhook/main.go:171)


serveAddLabel is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveAddLabel((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:171`



---


[function] name: serveAlwaysAllowDelayFiveSeconds file: test/images/agnhost/webhook/main.go:163 returns_error: нет description: —


### serveAlwaysAllowDelayFiveSeconds (test/images/agnhost/webhook/main.go:163)


serveAlwaysAllowDelayFiveSeconds is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveAlwaysAllowDelayFiveSeconds((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:163`



---


[function] name: serveAlwaysDeny file: test/images/agnhost/webhook/main.go:167 returns_error: нет description: —


### serveAlwaysDeny (test/images/agnhost/webhook/main.go:167)


serveAlwaysDeny is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveAlwaysDeny((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:167`



---


[function] name: serveAttachingPods file: test/images/agnhost/webhook/main.go:179 returns_error: нет description: —


### serveAttachingPods (test/images/agnhost/webhook/main.go:179)


serveAttachingPods is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveAttachingPods((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:179`



---


[function] name: serveCRD file: test/images/agnhost/webhook/main.go:207 returns_error: нет description: —


### serveCRD (test/images/agnhost/webhook/main.go:207)


serveCRD is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveCRD((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:207`



---


[function] name: serveConfigmaps file: test/images/agnhost/webhook/main.go:191 returns_error: нет description: —


### serveConfigmaps (test/images/agnhost/webhook/main.go:191)


serveConfigmaps is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveConfigmaps((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:191`



---


[function] name: serveCustomResource file: test/images/agnhost/webhook/main.go:199 returns_error: нет description: —


### serveCustomResource (test/images/agnhost/webhook/main.go:199)


serveCustomResource is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveCustomResource((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:199`



---


[function] name: serveMutateConfigmaps file: test/images/agnhost/webhook/main.go:195 returns_error: нет description: —


### serveMutateConfigmaps (test/images/agnhost/webhook/main.go:195)


serveMutateConfigmaps is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveMutateConfigmaps((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:195`



---


[function] name: serveMutateCustomResource file: test/images/agnhost/webhook/main.go:203 returns_error: нет description: —


### serveMutateCustomResource (test/images/agnhost/webhook/main.go:203)


serveMutateCustomResource is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveMutateCustomResource((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:203`



---


[function] name: serveMutatePods file: test/images/agnhost/webhook/main.go:183 returns_error: нет description: —


### serveMutatePods (test/images/agnhost/webhook/main.go:183)


serveMutatePods is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveMutatePods((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:183`



---


[function] name: serveMutatePodsSidecar file: test/images/agnhost/webhook/main.go:187 returns_error: нет description: —


### serveMutatePodsSidecar (test/images/agnhost/webhook/main.go:187)


serveMutatePodsSidecar is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func serveMutatePodsSidecar((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:187`



---


[function] name: servePods file: test/images/agnhost/webhook/main.go:175 returns_error: нет description: —


### servePods (test/images/agnhost/webhook/main.go:175)


servePods is a function that performs operations based on the provided parameters and returns (w http.ResponseWriter, r *http.Request).


```go
func servePods((w http.ResponseWriter, r *http.Request)) (w http.ResponseWriter, r *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** r


```json
{
  "fset": null,
  "ctx": {},
  "failed": false,
  "donePaths": {}
}
```


*Определено в:* `cmd/preferredimports/preferredimports.go`


**Тип ответа:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


📍 *Расположение:* `test/images/agnhost/webhook/main.go:175`




## test/images/agnhost/webhook/pods.go


📄 Исходный файл: `test/images/agnhost/webhook/pods.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [admitPods](#admitpods-testimagesagnhostwebhookpodsgo39) `:39`

- 🔗 [applyPodPatch](#applypodpatch-testimagesagnhostwebhookpodsgo118) `:118`

- 🔗 [denySpecificAttachment](#denyspecificattachment-testimagesagnhostwebhookpodsgo145) `:145`

- 🔗 [hasContainer](#hascontainer-testimagesagnhostwebhookpodsgo109) `:109`

- 🔗 [mutatePods](#mutatepods-testimagesagnhostwebhookpodsgo82) `:82`

- 🔗 [mutatePodsSidecar](#mutatepodssidecar-testimagesagnhostwebhookpodsgo92) `:92`


</details>


[function] name: admitPods file: test/images/agnhost/webhook/pods.go:39 returns_error: нет description: only allow pods to pull images from specific registry.


### admitPods (test/images/agnhost/webhook/pods.go:39)


only allow pods to pull images from specific registry.


```go
func admitPods((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/pods.go:39`



---


[function] name: applyPodPatch file: test/images/agnhost/webhook/pods.go:118 returns_error: нет description: —


### applyPodPatch (test/images/agnhost/webhook/pods.go:118)


applyPodPatch is a function that performs operations based on the provided parameters and returns (ar v1.AdmissionReview, shouldPatchPod func(*corev1.Pod) bool, patch string).


```go
func applyPodPatch((ar v1.AdmissionReview, shouldPatchPod func(*corev1.Pod) bool, patch string)) (ar v1.AdmissionReview, shouldPatchPod func(*corev1.Pod) bool, patch string)
```


**Тип запроса:** corev1.Pod


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "CreatedAt": 0,
  "Containers": [],
  "Sandboxes": []
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


**Тип ответа:** shouldPatchPod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.Pod


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "CreatedAt": 0,
  "Containers": [],
  "Sandboxes": []
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** patch


```json
{
  "namer": {},
  "creater": {},
  "defaulter": {},
  "typer": {},
  "unsafeConvertor": {},
  "resource": {},
  "kind": {},
  "subresource": "string",
  "dryRun": false,
  "validationDirective": "string",
  "objectInterfaces": {},
  "hubGroupVersion": {},
  "createValidation": {},
  "updateValidation": {},
  "admissionCheck": {},
  "codec": {},
  "options": null,
  "restPatcher": {},
  "name": "string",
  "patchType": {},
  "patchBytes": [],
  "userAgent": "string",
  "namespace": "string",
  "updatedObjectInfo": {},
  "mechanism": {},
  "forceAllowCreate": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/handlers/patch.go`


📍 *Расположение:* `test/images/agnhost/webhook/pods.go:118`



---


[function] name: denySpecificAttachment file: test/images/agnhost/webhook/pods.go:145 returns_error: нет description: denySpecificAttachment denies `kubectl attach to-be-attached-pod -i -c=container1"
or equivalent client requests.


### denySpecificAttachment (test/images/agnhost/webhook/pods.go:145)


denySpecificAttachment denies `kubectl attach to-be-attached-pod -i -c=container1"
or equivalent client requests.


```go
func denySpecificAttachment((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/pods.go:145`



---


[function] name: hasContainer file: test/images/agnhost/webhook/pods.go:109 returns_error: нет description: —


### hasContainer (test/images/agnhost/webhook/pods.go:109)


hasContainer is a function that performs operations based on the provided parameters and returns (containers []corev1.Container, containerName string).


```go
func hasContainer((containers []corev1.Container, containerName string)) (containers []corev1.Container, containerName string)
```


**Тип ответа:** containers


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** corev1.Container


```json
{
  "ID": {},
  "Name": "string",
  "Image": "string",
  "ImageID": "string",
  "ImageRef": "string",
  "ImageRuntimeHandler": "string",
  "Hash": 0,
  "State": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** containerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/agnhost/webhook/pods.go:109`



---


[function] name: mutatePods file: test/images/agnhost/webhook/pods.go:82 returns_error: нет description: —


### mutatePods (test/images/agnhost/webhook/pods.go:82)


mutatePods is a function that performs operations based on the provided parameters and returns (ar v1.AdmissionReview).


```go
func mutatePods((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/pods.go:82`



---


[function] name: mutatePodsSidecar file: test/images/agnhost/webhook/pods.go:92 returns_error: нет description: —


### mutatePodsSidecar (test/images/agnhost/webhook/pods.go:92)


mutatePodsSidecar is a function that performs operations based on the provided parameters and returns (ar v1.AdmissionReview).


```go
func mutatePodsSidecar((ar v1.AdmissionReview)) (ar v1.AdmissionReview)
```


**Тип ответа:** ar


```json
{
  "controllerContext": {},
  "controllerName": "string",
  "discoveryClient": {}
}
```


*Определено в:* `cmd/kube-controller-manager/app/core.go`


**Тип ответа:** v1.AdmissionReview


```json
{
  "Request": null,
  "Response": null
}
```


*Определено в:* `pkg/apis/admission/types.go`


📍 *Расположение:* `test/images/agnhost/webhook/pods.go:92`




## test/images/agnhost/webhook/scheme.go


📄 Исходный файл: `test/images/agnhost/webhook/scheme.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [addToScheme](#addtoscheme-testimagesagnhostwebhookschemego37) `:37`

- 🔗 [init](#init-testimagesagnhostwebhookschemego33) `:33`


</details>


[function] name: addToScheme file: test/images/agnhost/webhook/scheme.go:37 returns_error: нет description: —


### addToScheme (test/images/agnhost/webhook/scheme.go:37)


addToScheme is a function that performs operations based on the provided parameters and returns (scheme *runtime.Scheme).


```go
func addToScheme((scheme *runtime.Scheme)) (scheme *runtime.Scheme)
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


📍 *Расположение:* `test/images/agnhost/webhook/scheme.go:37`



---


[function] name: init file: test/images/agnhost/webhook/scheme.go:33 returns_error: нет description: —


### init (test/images/agnhost/webhook/scheme.go:33)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/images/agnhost/webhook/scheme.go:33`




## test/images/apparmor-loader/loader.go


📄 Исходный файл: `test/images/apparmor-loader/loader.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [getLoadedProfiles](#getloadedprofiles-testimagesapparmor-loaderloadergo234) `:234`

- 🔗 [getProfileNames](#getprofilenames-testimagesapparmor-loaderloadergo167) `:167`

- 🔗 [loadNewProfiles](#loadnewprofiles-testimagesapparmor-loaderloadergo111) `:111`

- 🔗 [loadProfiles](#loadprofiles-testimagesapparmor-loaderloadergo192) `:192`

- 🔗 [main](#main-testimagesapparmor-loaderloadergo45) `:45`

- 🔗 [parseProfileName](#parseprofilename-testimagesapparmor-loaderloadergo262) `:262`

- 🔗 [pollForever](#pollforever-testimagesapparmor-loaderloadergo96) `:96`

- 🔗 [resolveSymlink](#resolvesymlink-testimagesapparmor-loaderloadergo209) `:209`

- 🔗 [runOnce](#runonce-testimagesapparmor-loaderloadergo79) `:79`

- 🔗 [unloadedProfiles](#unloadedprofiles-testimagesapparmor-loaderloadergo183) `:183`


</details>


[function] name: getLoadedProfiles file: test/images/apparmor-loader/loader.go:234 returns_error: да description: TODO: This is copied from k8s.io/kubernetes/pkg/security/apparmor.getLoadedProfiles.

Refactor that method to expose it 


### getLoadedProfiles (test/images/apparmor-loader/loader.go:234)


TODO: This is copied from k8s.io/kubernetes/pkg/security/apparmor.getLoadedProfiles.

Refactor that method to expose it in a reusable way, and delete this version.


```go
func getLoadedProfiles((map[string]bool, error)) (map[string]bool, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/apparmor-loader/loader.go:234`



---


[function] name: getProfileNames file: test/images/apparmor-loader/loader.go:167 returns_error: да description: —


### getProfileNames (test/images/apparmor-loader/loader.go:167)


getProfileNames is a function that performs operations based on the provided parameters and may return an error.


```go
func getProfileNames(([]string, error)) ([]string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/apparmor-loader/loader.go:167`



---


[function] name: loadNewProfiles file: test/images/apparmor-loader/loader.go:111 returns_error: нет description: —


### loadNewProfiles (test/images/apparmor-loader/loader.go:111)


loadNewProfiles is a function that performs operations based on the provided parameters and returns (success bool, newProfiles []string).


```go
func loadNewProfiles((success bool, newProfiles []string)) (success bool, newProfiles []string)
```


**Тип ответа:** success


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newProfiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/apparmor-loader/loader.go:111`



---


[function] name: loadProfiles file: test/images/apparmor-loader/loader.go:192 returns_error: нет description: —


### loadProfiles (test/images/apparmor-loader/loader.go:192)


loadProfiles is a function that performs operations based on the provided parameters and returns (path string).


```go
func loadProfiles((path string)) (path string)
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


📍 *Расположение:* `test/images/apparmor-loader/loader.go:192`



---


[function] name: main file: test/images/apparmor-loader/loader.go:45 returns_error: нет description: —


### main (test/images/apparmor-loader/loader.go:45)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/apparmor-loader/loader.go:45`



---


[function] name: parseProfileName file: test/images/apparmor-loader/loader.go:262 returns_error: нет description: The profiles file is formatted with one profile per line, matching a form:

namespace://profile-name (mode)
profile-name


### parseProfileName (test/images/apparmor-loader/loader.go:262)


The profiles file is formatted with one profile per line, matching a form:

namespace://profile-name (mode)
profile-name (mode)

Where mode is {enforce, complain, kill}. The "namespace://" is only included for namespaced
profiles. For the purposes of Kubernetes, we consider the namespace part of the profile name.


```go
func parseProfileName((profileLine string)) (profileLine string)
```


**Тип ответа:** profileLine


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/apparmor-loader/loader.go:262`



---


[function] name: pollForever file: test/images/apparmor-loader/loader.go:96 returns_error: нет description: Poll the directories indefinitely.


### pollForever (test/images/apparmor-loader/loader.go:96)


Poll the directories indefinitely.


```go
func pollForever(()) ()
```


📍 *Расположение:* `test/images/apparmor-loader/loader.go:96`



---


[function] name: resolveSymlink file: test/images/apparmor-loader/loader.go:209 returns_error: да description: If the given fileinfo is a symlink, return the FileInfo of the target. Otherwise, return the
given fileinfo.


### resolveSymlink (test/images/apparmor-loader/loader.go:209)


If the given fileinfo is a symlink, return the FileInfo of the target. Otherwise, return the
given fileinfo.


```go
func resolveSymlink((os.FileInfo, error)) (os.FileInfo, error)
```


**Тип ответа:** os.FileInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `os.FileInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/apparmor-loader/loader.go:209`



---


[function] name: runOnce file: test/images/apparmor-loader/loader.go:79 returns_error: нет description: No polling: run once and exit.


### runOnce (test/images/apparmor-loader/loader.go:79)


No polling: run once and exit.


```go
func runOnce(()) ()
```


📍 *Расположение:* `test/images/apparmor-loader/loader.go:79`



---


[function] name: unloadedProfiles file: test/images/apparmor-loader/loader.go:183 returns_error: нет description: —


### unloadedProfiles (test/images/apparmor-loader/loader.go:183)


unloadedProfiles is a function that performs operations based on the provided parameters and returns (loadedProfiles map[string]bool, profiles []string).


```go
func unloadedProfiles((loadedProfiles map[string]bool, profiles []string)) (loadedProfiles map[string]bool, profiles []string)
```


**Тип ответа:** loadedProfiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** profiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/apparmor-loader/loader.go:183`




## test/images/busybox/hostname.go


📄 Исходный файл: `test/images/busybox/hostname.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [getOutboundIP](#getoutboundip-testimagesbusyboxhostnamego27) `:27`

- 🔗 [main](#main-testimagesbusyboxhostnamego37) `:37`


</details>


[function] name: getOutboundIP file: test/images/busybox/hostname.go:27 returns_error: нет description: —


### getOutboundIP (test/images/busybox/hostname.go:27)


getOutboundIP is a function that performs operations based on the provided parameters and returns ().


```go
func getOutboundIP(()) ()
```


📍 *Расположение:* `test/images/busybox/hostname.go:27`



---


[function] name: main file: test/images/busybox/hostname.go:37 returns_error: нет description: —


### main (test/images/busybox/hostname.go:37)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/busybox/hostname.go:37`




## test/images/nonewprivs/nnp.go


📄 Исходный файл: `test/images/nonewprivs/nnp.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testimagesnonewprivsnnpgo24) `:24`


</details>


[function] name: main file: test/images/nonewprivs/nnp.go:24 returns_error: нет description: —


### main (test/images/nonewprivs/nnp.go:24)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/nonewprivs/nnp.go:24`




## test/images/pets/peer-finder/peer-finder.go


📄 Исходный файл: `test/images/pets/peer-finder/peer-finder.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [lookup](#lookup-testimagespetspeer-finderpeer-findergo48) `:48`

- 🔗 [main](#main-testimagespetspeer-finderpeer-findergo88) `:88`

- 🔗 [shellOut](#shellout-testimagespetspeer-finderpeer-findergo62) `:62`


</details>


[function] name: lookup file: test/images/pets/peer-finder/peer-finder.go:48 returns_error: да description: —


### lookup (test/images/pets/peer-finder/peer-finder.go:48)


lookup is a function that performs operations based on the provided parameters and may return an error.


```go
func lookup((sets.String, error)) (sets.String, error)
```


**Тип ответа:** sets.String


```json
{
  "ID": "string",
  "Secret": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/bootstraptoken/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `sets.String`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/pets/peer-finder/peer-finder.go:48`



---


[function] name: main file: test/images/pets/peer-finder/peer-finder.go:88 returns_error: нет description: —


### main (test/images/pets/peer-finder/peer-finder.go:88)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/pets/peer-finder/peer-finder.go:88`



---


[function] name: shellOut file: test/images/pets/peer-finder/peer-finder.go:62 returns_error: нет description: —


### shellOut (test/images/pets/peer-finder/peer-finder.go:62)


shellOut is a function that performs operations based on the provided parameters and returns (sendStdin, script string).


```go
func shellOut((sendStdin, script string)) (sendStdin, script string)
```


**Тип ответа:** sendStdin


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** script


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


📍 *Расположение:* `test/images/pets/peer-finder/peer-finder.go:62`




## test/images/regression-issue-74839/main.go


📄 Исходный файл: `test/images/regression-issue-74839/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [getIPs](#getips-testimagesregression-issue-74839maingo142) `:142`

- 🔗 [main](#main-testimagesregression-issue-74839maingo33) `:33`

- 🔗 [probe](#probe-testimagesregression-issue-74839maingo67) `:67`


</details>


[function] name: getIPs file: test/images/regression-issue-74839/main.go:142 returns_error: нет description: getIPs gets the IPs from the downward API
we don't have to validate the IPs because
they are validated previously by kub


### getIPs (test/images/regression-issue-74839/main.go:142)


getIPs gets the IPs from the downward API
we don't have to validate the IPs because
they are validated previously by kubernetes/CNI


```go
func getIPs(()) ()
```


📍 *Расположение:* `test/images/regression-issue-74839/main.go:142`



---


[function] name: main file: test/images/regression-issue-74839/main.go:33 returns_error: нет description: —


### main (test/images/regression-issue-74839/main.go:33)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/regression-issue-74839/main.go:33`



---


[function] name: probe file: test/images/regression-issue-74839/main.go:67 returns_error: нет description: —


### probe (test/images/regression-issue-74839/main.go:67)


probe is a function that performs operations based on the provided parameters and returns (ip string).


```go
func probe((ip string)) (ip string)
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


📍 *Расположение:* `test/images/regression-issue-74839/main.go:67`




## test/images/regression-issue-74839/tcp.go


📄 Исходный файл: `test/images/regression-issue-74839/tcp.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [DataOffset](#dataoffset-testimagesregression-issue-74839tcpgo84) `:84`

- 🔗 [FlagString](#flagstring-testimagesregression-issue-74839tcpgo88) `:88`

- 🔗 [add](#add-testimagesregression-issue-74839tcpgo196) `:196`

- 🔗 [checksumTCP](#checksumtcp-testimagesregression-issue-74839tcpgo143) `:143`

- 🔗 [decode](#decode-testimagesregression-issue-74839tcpgo75) `:75`

- 🔗 [encode](#encode-testimagesregression-issue-74839tcpgo122) `:122`

- 🔗 [finalize](#finalize-testimagesregression-issue-74839tcpgo182) `:182`


</details>


[function] name: DataOffset file: test/images/regression-issue-74839/tcp.go:84 returns_error: нет description: —


### DataOffset (test/images/regression-issue-74839/tcp.go:84)


DataOffset is a method that performs operations based on the provided parameters and returns ().


```go
func (t *tcpPacket) DataOffset(()) ()
```


📍 *Расположение:* `test/images/regression-issue-74839/tcp.go:84`



---


[function] name: FlagString file: test/images/regression-issue-74839/tcp.go:88 returns_error: нет description: —


### FlagString (test/images/regression-issue-74839/tcp.go:88)


FlagString is a method that performs operations based on the provided parameters and returns ().


```go
func (t *tcpPacket) FlagString(()) ()
```


📍 *Расположение:* `test/images/regression-issue-74839/tcp.go:88`



---


[function] name: add file: test/images/regression-issue-74839/tcp.go:196 returns_error: нет description: —


### add (test/images/regression-issue-74839/tcp.go:196)


add is a method that performs operations based on the provided parameters and returns (data []byte).


```go
func (c *tcpChecksummer) add((data []byte)) (data []byte)
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


📍 *Расположение:* `test/images/regression-issue-74839/tcp.go:196`



---


[function] name: checksumTCP file: test/images/regression-issue-74839/tcp.go:143 returns_error: нет description: —


### checksumTCP (test/images/regression-issue-74839/tcp.go:143)


checksumTCP is a function that performs operations based on the provided parameters and returns (src, dest net.IP, tcpHeader, data []byte).


```go
func checksumTCP((src, dest net.IP, tcpHeader, data []byte)) (src, dest net.IP, tcpHeader, data []byte)
```


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** tcpHeader


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


📍 *Расположение:* `test/images/regression-issue-74839/tcp.go:143`



---


[function] name: decode file: test/images/regression-issue-74839/tcp.go:75 returns_error: да description: —


### decode (test/images/regression-issue-74839/tcp.go:75)


decode is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *tcpPacket) decode(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/regression-issue-74839/tcp.go:75`



---


[function] name: encode file: test/images/regression-issue-74839/tcp.go:122 returns_error: нет description: —


### encode (test/images/regression-issue-74839/tcp.go:122)


encode is a method that performs operations based on the provided parameters and returns (src, dest net.IP, data []byte).


```go
func (t *tcpPacket) encode((src, dest net.IP, data []byte)) (src, dest net.IP, data []byte)
```


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dest


```json
{
  "F": {},
  "T": {},
  "Destination": {}
}
```


*Определено в:* `plugin/pkg/auth/authorizer/node/graph.go`


**Тип ответа:** net.IP


```json
{
  "nodeIPAMControllerConfiguration": {},
  "nodeIPAMControllerOptions": {}
}
```


*Определено в:* `cmd/cloud-controller-manager/nodeipamcontroller.go`


**Тип ответа:** data


```json
{
  "status": null,
  "err": {},
  "modified": {}
}
```


*Определено в:* `pkg/kubelet/container/cache.go`


📍 *Расположение:* `test/images/regression-issue-74839/tcp.go:122`



---


[function] name: finalize file: test/images/regression-issue-74839/tcp.go:182 returns_error: нет description: —


### finalize (test/images/regression-issue-74839/tcp.go:182)


finalize is a method that performs operations based on the provided parameters and returns ().


```go
func (c *tcpChecksummer) finalize(()) ()
```


📍 *Расположение:* `test/images/regression-issue-74839/tcp.go:182`




## test/images/resource-consumer/consume-cpu/common.go


📄 Исходный файл: `test/images/resource-consumer/consume-cpu/common.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [doSomething](#dosomething-testimagesresource-consumerconsume-cpucommongo27) `:27`


</details>


[function] name: doSomething file: test/images/resource-consumer/consume-cpu/common.go:27 returns_error: нет description: —


### doSomething (test/images/resource-consumer/consume-cpu/common.go:27)


doSomething is a function that performs operations based on the provided parameters and returns ().


```go
func doSomething(()) ()
```


📍 *Расположение:* `test/images/resource-consumer/consume-cpu/common.go:27`




## test/images/resource-consumer/consume-cpu/consume_cpu.go


📄 Исходный файл: `test/images/resource-consumer/consume-cpu/consume_cpu.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testimagesresource-consumerconsume-cpuconsume_cpugo28) `:28`


</details>


[function] name: main file: test/images/resource-consumer/consume-cpu/consume_cpu.go:28 returns_error: нет description: —


### main (test/images/resource-consumer/consume-cpu/consume_cpu.go:28)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/resource-consumer/consume-cpu/consume_cpu.go:28`




## test/images/resource-consumer/consume-cpu/consume_cpu_windows.go


📄 Исходный файл: `test/images/resource-consumer/consume-cpu/consume_cpu_windows.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [main](#main-testimagesresource-consumerconsume-cpuconsume_cpu_windowsgo58) `:58`

- 🔗 [statsNow](#statsnow-testimagesresource-consumerconsume-cpuconsume_cpu_windowsgo37) `:37`

- 🔗 [usageNow](#usagenow-testimagesresource-consumerconsume-cpuconsume_cpu_windowsgo49) `:49`


</details>


[function] name: main file: test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:58 returns_error: нет description: —


### main (test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:58)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:58`



---


[function] name: statsNow file: test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:37 returns_error: нет description: Retrieves the amount of CPU time this process has used since it started.


### statsNow (test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:37)


Retrieves the amount of CPU time this process has used since it started.


```go
func statsNow((s procCPUStats)) (s procCPUStats)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** procCPUStats


```json
{
  "User": 0,
  "System": 0,
  "Time": {},
  "Total": 0
}
```


*Определено в:* `test/images/resource-consumer/consume-cpu/consume_cpu_windows.go`


📍 *Расположение:* `test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:37`



---


[function] name: usageNow file: test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:49 returns_error: нет description: Given stats from two time points, calculates the millicores used by this
process between the two samples.


### usageNow (test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:49)


Given stats from two time points, calculates the millicores used by this
process between the two samples.


```go
func usageNow((first procCPUStats, second procCPUStats)) (first procCPUStats, second procCPUStats)
```


**Тип ответа:** first


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** procCPUStats


```json
{
  "User": 0,
  "System": 0,
  "Time": {},
  "Total": 0
}
```


*Определено в:* `test/images/resource-consumer/consume-cpu/consume_cpu_windows.go`


**Тип ответа:** second


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** procCPUStats


```json
{
  "User": 0,
  "System": 0,
  "Time": {},
  "Total": 0
}
```


*Определено в:* `test/images/resource-consumer/consume-cpu/consume_cpu_windows.go`


📍 *Расположение:* `test/images/resource-consumer/consume-cpu/consume_cpu_windows.go:49`




## test/images/resource-consumer/resource_consumer.go


📄 Исходный файл: `test/images/resource-consumer/resource_consumer.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-testimagesresource-consumerresource_consumergo28) `:28`


</details>


[function] name: main file: test/images/resource-consumer/resource_consumer.go:28 returns_error: нет description: —


### main (test/images/resource-consumer/resource_consumer.go:28)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/resource-consumer/resource_consumer.go:28`




## test/images/resource-consumer/resource_consumer_handler.go


📄 Исходный файл: `test/images/resource-consumer/resource_consumer_handler.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [NewResourceConsumerHandler](#newresourceconsumerhandler-testimagesresource-consumerresource_consumer_handlergo37) `:37`

- 🔗 [ServeHTTP](#servehttp-testimagesresource-consumerresource_consumer_handlergo41) `:41`

- 🔗 [bumpMetric](#bumpmetric-testimagesresource-consumerresource_consumer_handlergo141) `:141`

- 🔗 [handleBumpMetric](#handlebumpmetric-testimagesresource-consumerresource_consumer_handlergo157) `:157`

- 🔗 [handleConsumeCPU](#handleconsumecpu-testimagesresource-consumerresource_consumer_handlergo79) `:79`

- 🔗 [handleConsumeMem](#handleconsumemem-testimagesresource-consumerresource_consumer_handlergo102) `:102`

- 🔗 [handleGetCurrentStatus](#handlegetcurrentstatus-testimagesresource-consumerresource_consumer_handlergo125) `:125`

- 🔗 [handleMetrics](#handlemetrics-testimagesresource-consumerresource_consumer_handlergo131) `:131`


</details>


[function] name: NewResourceConsumerHandler file: test/images/resource-consumer/resource_consumer_handler.go:37 returns_error: нет description: NewResourceConsumerHandler creates and initializes a ResourceConsumerHandler to defaults.


### NewResourceConsumerHandler (test/images/resource-consumer/resource_consumer_handler.go:37)


NewResourceConsumerHandler creates and initializes a ResourceConsumerHandler to defaults.


```go
func NewResourceConsumerHandler(()) ()
```


📍 *Расположение:* `test/images/resource-consumer/resource_consumer_handler.go:37`



---


[function] name: ServeHTTP file: test/images/resource-consumer/resource_consumer_handler.go:41 returns_error: нет description: —


### ServeHTTP (test/images/resource-consumer/resource_consumer_handler.go:41)


ServeHTTP is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, req *http.Request).


```go
func (handler *ResourceConsumerHandler) ServeHTTP((w http.ResponseWriter, req *http.Request)) (w http.ResponseWriter, req *http.Request)
```


**Тип запроса:** http.Request


```json
{
  "Subresources": []
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/api/operation/operation.go`


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


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


📍 *Расположение:* `test/images/resource-consumer/resource_consumer_handler.go:41`



---


[function] name: bumpMetric file: test/images/resource-consumer/resource_consumer_handler.go:141 returns_error: нет description: —


### bumpMetric (test/images/resource-consumer/resource_consumer_handler.go:141)


bumpMetric is a method that performs operations based on the provided parameters and returns (metric string, delta float64, duration time.Duration).


```go
func (handler *ResourceConsumerHandler) bumpMetric((metric string, delta float64, duration time.Duration)) (metric string, delta float64, duration time.Duration)
```


**Тип ответа:** metric


```json
{
  "base": {},
  "jwksURL": "string",
  "jwtIssuer": "string",
  "apiServerID": "string",
  "shouldRecordFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go`


**Тип ответа:** delta


```json
{
  "PushFunc": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/undelta_store.go`


**Тип ответа:** duration


```json
{
  "clock": {},
  "latency": {},
  "mu": {},
  "aggregateFunction": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/request/webhook_duration.go`


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


📍 *Расположение:* `test/images/resource-consumer/resource_consumer_handler.go:141`



---


[function] name: handleBumpMetric file: test/images/resource-consumer/resource_consumer_handler.go:157 returns_error: нет description: —


### handleBumpMetric (test/images/resource-consumer/resource_consumer_handler.go:157)


handleBumpMetric is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, query url.Values).


```go
func (handler *ResourceConsumerHandler) handleBumpMetric((w http.ResponseWriter, query url.Values)) (w http.ResponseWriter, query url.Values)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** query


```json
{
  "finder": {},
  "root": {},
  "queryParam": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/query_param_verifier_v3.go`


**Тип ответа:** url.Values


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/images/resource-consumer/resource_consumer_handler.go:157`



---


[function] name: handleConsumeCPU file: test/images/resource-consumer/resource_consumer_handler.go:79 returns_error: нет description: —


### handleConsumeCPU (test/images/resource-consumer/resource_consumer_handler.go:79)


handleConsumeCPU is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, query url.Values).


```go
func (handler *ResourceConsumerHandler) handleConsumeCPU((w http.ResponseWriter, query url.Values)) (w http.ResponseWriter, query url.Values)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** query


```json
{
  "finder": {},
  "root": {},
  "queryParam": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/query_param_verifier_v3.go`


**Тип ответа:** url.Values


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/images/resource-consumer/resource_consumer_handler.go:79`



---


[function] name: handleConsumeMem file: test/images/resource-consumer/resource_consumer_handler.go:102 returns_error: нет description: —


### handleConsumeMem (test/images/resource-consumer/resource_consumer_handler.go:102)


handleConsumeMem is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter, query url.Values).


```go
func (handler *ResourceConsumerHandler) handleConsumeMem((w http.ResponseWriter, query url.Values)) (w http.ResponseWriter, query url.Values)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


**Тип ответа:** query


```json
{
  "finder": {},
  "root": {},
  "queryParam": {}
}
```


*Определено в:* `staging/src/k8s.io/cli-runtime/pkg/resource/query_param_verifier_v3.go`


**Тип ответа:** url.Values


```json
{
  "Label": "string",
  "Values": []
}
```


*Определено в:* `test/integration/scheduler_perf/util.go`


📍 *Расположение:* `test/images/resource-consumer/resource_consumer_handler.go:102`



---


[function] name: handleGetCurrentStatus file: test/images/resource-consumer/resource_consumer_handler.go:125 returns_error: нет description: —


### handleGetCurrentStatus (test/images/resource-consumer/resource_consumer_handler.go:125)


handleGetCurrentStatus is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter).


```go
func (handler *ResourceConsumerHandler) handleGetCurrentStatus((w http.ResponseWriter)) (w http.ResponseWriter)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


📍 *Расположение:* `test/images/resource-consumer/resource_consumer_handler.go:125`



---


[function] name: handleMetrics file: test/images/resource-consumer/resource_consumer_handler.go:131 returns_error: нет description: —


### handleMetrics (test/images/resource-consumer/resource_consumer_handler.go:131)


handleMetrics is a method that performs operations based on the provided parameters and returns (w http.ResponseWriter).


```go
func (handler *ResourceConsumerHandler) handleMetrics((w http.ResponseWriter)) (w http.ResponseWriter)
```


**Тип ответа:** w


```json
{
  "KubeconfigPath": "string",
  "BootstrapKubeconfigPath": "string",
  "CertDirectory": "string",
  "KubeletPort": 0,
  "KubeletReadOnlyPort": 0,
  "Morph": "string",
  "NodeName": "string",
  "ServerPort": 0,
  "ContentType": "string",
  "QPS": 0.0,
  "Burst": 0,
  "NodeLabels": {},
  "RegisterWithTaints": [],
  "MaxPods": 0,
  "ExtendedResources": {},
  "UseHostImageService": false,
  "UseRealProxier": false,
  "ProxierSyncPeriod": {},
  "ProxierMinSyncPeriod": {}
}
```


*Определено в:* `cmd/kubemark/app/hollow_node.go`


**Тип ответа:** http.ResponseWriter


```json
{
  "ctx": {},
  "once": {},
  "processResponseStartedStage": false
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit.go`


📍 *Расположение:* `test/images/resource-consumer/resource_consumer_handler.go:131`




## test/images/resource-consumer/utils.go


📄 Исходный файл: `test/images/resource-consumer/utils.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConsumeMem](#consumemem-testimagesresource-consumerutilsgo33) `:33`


</details>


[function] name: ConsumeMem file: test/images/resource-consumer/utils.go:33 returns_error: нет description: ConsumeMem consumes a given number of megabytes for the specified duration.


### ConsumeMem (test/images/resource-consumer/utils.go:33)


ConsumeMem consumes a given number of megabytes for the specified duration.


```go
func ConsumeMem((megabytes int, durationSec int)) (megabytes int, durationSec int)
```


**Тип ответа:** megabytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/resource-consumer/utils.go:33`




## test/images/resource-consumer/utils_common.go


📄 Исходный файл: `test/images/resource-consumer/utils_common.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [ConsumeCPU](#consumecpu-testimagesresource-consumerutils_commongo26) `:26`

- 🔗 [GetCurrentStatus](#getcurrentstatus-testimagesresource-consumerutils_commongo39) `:39`


</details>


[function] name: ConsumeCPU file: test/images/resource-consumer/utils_common.go:26 returns_error: нет description: ConsumeCPU consumes a given number of millicores for the specified duration.


### ConsumeCPU (test/images/resource-consumer/utils_common.go:26)


ConsumeCPU consumes a given number of millicores for the specified duration.


```go
func ConsumeCPU((millicores int, durationSec int)) (millicores int, durationSec int)
```


**Тип ответа:** millicores


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/resource-consumer/utils_common.go:26`



---


[function] name: GetCurrentStatus file: test/images/resource-consumer/utils_common.go:39 returns_error: нет description: GetCurrentStatus prints out a no-op.


### GetCurrentStatus (test/images/resource-consumer/utils_common.go:39)


GetCurrentStatus prints out a no-op.


```go
func GetCurrentStatus(()) ()
```


📍 *Расположение:* `test/images/resource-consumer/utils_common.go:39`




## test/images/resource-consumer/utils_windows.go


📄 Исходный файл: `test/images/resource-consumer/utils_windows.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConsumeMem](#consumemem-testimagesresource-consumerutils_windowsgo34) `:34`


</details>


[function] name: ConsumeMem file: test/images/resource-consumer/utils_windows.go:34 returns_error: нет description: ConsumeMem consumes a given number of megabytes for the specified duration.


### ConsumeMem (test/images/resource-consumer/utils_windows.go:34)


ConsumeMem consumes a given number of megabytes for the specified duration.


```go
func ConsumeMem((megabytes int, durationSec int)) (megabytes int, durationSec int)
```


**Тип ответа:** megabytes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** durationSec


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/images/resource-consumer/utils_windows.go:34`




## test/images/sample-device-plugin/sampledeviceplugin.go


📄 Исходный файл: `test/images/sample-device-plugin/sampledeviceplugin.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [createCDIFile](#createcdifile-testimagessample-device-pluginsampledeviceplugingo236) `:236`

- 🔗 [handleRegistrationProcess](#handleregistrationprocess-testimagessample-device-pluginsampledeviceplugingo206) `:206`

- 🔗 [main](#main-testimagessample-device-pluginsampledeviceplugingo95) `:95`

- 🔗 [stubAllocFunc](#stuballocfunc-testimagessample-device-pluginsampledeviceplugingo42) `:42`

- 🔗 [stubRegisterControlFunc](#stubregistercontrolfunc-testimagessample-device-pluginsampledeviceplugingo91) `:91`


</details>


[function] name: createCDIFile file: test/images/sample-device-plugin/sampledeviceplugin.go:236 returns_error: нет description: —


### createCDIFile (test/images/sample-device-plugin/sampledeviceplugin.go:236)


createCDIFile is a function that performs operations based on the provided parameters and returns (logger klog.Logger, devs []*pluginapi.Device).


```go
func createCDIFile((logger klog.Logger, devs []*pluginapi.Device)) (logger klog.Logger, devs []*pluginapi.Device)
```


**Тип запроса:** pluginapi.Device


```json
{
  "PoolName": "string",
  "DeviceName": "string",
  "ShareID": null,
  "RequestNames": [],
  "CDIDeviceIDs": []
}
```


*Определено в:* `pkg/kubelet/cm/dra/state/state.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** klog.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** devs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** pluginapi.Device


```json
{
  "PoolName": "string",
  "DeviceName": "string",
  "ShareID": null,
  "RequestNames": [],
  "CDIDeviceIDs": []
}
```


*Определено в:* `pkg/kubelet/cm/dra/state/state.go`


📍 *Расположение:* `test/images/sample-device-plugin/sampledeviceplugin.go:236`



---


[function] name: handleRegistrationProcess file: test/images/sample-device-plugin/sampledeviceplugin.go:206 returns_error: нет description: —


### handleRegistrationProcess (test/images/sample-device-plugin/sampledeviceplugin.go:206)


handleRegistrationProcess is a function that performs operations based on the provided parameters and returns (logger klog.Logger, registerControlFile string, dpStub *plugin.Stub, watcher *fsnotify.Watcher, updateCh chan<- bool).


```go
func handleRegistrationProcess((logger klog.Logger, registerControlFile string, dpStub *plugin.Stub, watcher *fsnotify.Watcher, updateCh chan<- bool)) (logger klog.Logger, registerControlFile string, dpStub *plugin.Stub, watcher *fsnotify.Watcher, updateCh chan<- bool)
```


**Тип запроса:** plugin.Stub


```json
{
  "devs": [],
  "socket": "string",
  "resourceName": "string",
  "preStartContainerFlag": false,
  "getPreferredAllocationFlag": false,
  "stop": {},
  "wg": {},
  "update": {},
  "server": null,
  "allocFunc": {},
  "getPreferredAllocFunc": {},
  "registerControlFunc": {},
  "registrationStatus": {},
  "endpoint": "string",
  "kubeletRestartWatcher": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/plugin/v1beta1/stub.go`


**Тип запроса:** fsnotify.Watcher


```json
{
  "path": "string",
  "fs": {},
  "fsWatcher": null,
  "desiredStateOfWorld": {}
}
```


*Определено в:* `pkg/kubelet/pluginmanager/pluginwatcher/plugin_watcher.go`


**Тип ответа:** logger


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** klog.Logger


```json
{
  "logger": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/events/event_recorder.go`


**Тип ответа:** registerControlFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dpStub


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** plugin.Stub


```json
{
  "devs": [],
  "socket": "string",
  "resourceName": "string",
  "preStartContainerFlag": false,
  "getPreferredAllocationFlag": false,
  "stop": {},
  "wg": {},
  "update": {},
  "server": null,
  "allocFunc": {},
  "getPreferredAllocFunc": {},
  "registerControlFunc": {},
  "registrationStatus": {},
  "endpoint": "string",
  "kubeletRestartWatcher": null
}
```


*Определено в:* `pkg/kubelet/cm/devicemanager/plugin/v1beta1/stub.go`


**Тип ответа:** watcher


```json
{
  "client": null,
  "codec": {},
  "newFunc": {},
  "objectType": "string",
  "groupResource": {},
  "versioner": {},
  "transformer": {},
  "getCurrentStorageRV": {},
  "getResourceSizeEstimator": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/etcd3/watcher.go`


**Тип ответа:** fsnotify.Watcher


```json
{
  "path": "string",
  "fs": {},
  "fsWatcher": null,
  "desiredStateOfWorld": {}
}
```


*Определено в:* `pkg/kubelet/pluginmanager/pluginwatcher/plugin_watcher.go`


**Тип ответа:** updateCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


📍 *Расположение:* `test/images/sample-device-plugin/sampledeviceplugin.go:206`



---


[function] name: main file: test/images/sample-device-plugin/sampledeviceplugin.go:95 returns_error: нет description: —


### main (test/images/sample-device-plugin/sampledeviceplugin.go:95)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/images/sample-device-plugin/sampledeviceplugin.go:95`



---


[function] name: stubAllocFunc file: test/images/sample-device-plugin/sampledeviceplugin.go:42 returns_error: да description: stubAllocFunc creates and returns allocation response for the input allocate request


### stubAllocFunc (test/images/sample-device-plugin/sampledeviceplugin.go:42)


stubAllocFunc creates and returns allocation response for the input allocate request


```go
func stubAllocFunc((*pluginapi.AllocateResponse, error)) (*pluginapi.AllocateResponse, error)
```


**Тип запроса:** pluginapi.AllocateResponse


```json
{
  "state": {},
  "containerResponses": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Тип ответа:** pluginapi.AllocateResponse


```json
{
  "state": {},
  "containerResponses": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*pluginapi.AllocateResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/images/sample-device-plugin/sampledeviceplugin.go:42`



---


[function] name: stubRegisterControlFunc file: test/images/sample-device-plugin/sampledeviceplugin.go:91 returns_error: нет description: stubAllocFunc creates and returns allocation response for the input allocate request


### stubRegisterControlFunc (test/images/sample-device-plugin/sampledeviceplugin.go:91)


stubAllocFunc creates and returns allocation response for the input allocate request


```go
func stubRegisterControlFunc(()) ()
```


📍 *Расположение:* `test/images/sample-device-plugin/sampledeviceplugin.go:91`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_fuzz.md)

- [Следующая директория](test_instrumentation.md)


---

