---
title: "Функции: test/e2e_node"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: test/e2e_node
---


# Функции: test/e2e_node


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_e2e_kubeadm.md)

- [Следующая директория](test_fixtures.md)


---


## Меню по файлам


- 📄 [test/e2e_node/benchmark_util.go](#teste2e_nodebenchmark_utilgo)

- 📄 [test/e2e_node/builder/build.go](#teste2e_nodebuilderbuildgo)

- 📄 [test/e2e_node/checkpoint_container.go](#teste2e_nodecheckpoint_containergo)

- 📄 [test/e2e_node/container_lifecycle_pod_construction.go](#teste2e_nodecontainer_lifecycle_pod_constructiongo)

- 📄 [test/e2e_node/criproxy/endpoint.go](#teste2e_nodecriproxyendpointgo)

- 📄 [test/e2e_node/criproxy/proxy_image_service.go](#teste2e_nodecriproxyproxy_image_servicego)

- 📄 [test/e2e_node/criproxy/proxy_runtime_service.go](#teste2e_nodecriproxyproxy_runtime_servicego)

- 📄 [test/e2e_node/environment/conformance.go](#teste2e_nodeenvironmentconformancego)

- 📄 [test/e2e_node/image_list.go](#teste2e_nodeimage_listgo)

- 📄 [test/e2e_node/kubeletconfig/kubeletconfig.go](#teste2e_nodekubeletconfigkubeletconfiggo)

- 📄 [test/e2e_node/node_problem_detector_linux.go](#teste2e_nodenode_problem_detector_linuxgo)

- 📄 [test/e2e_node/numa_alignment.go](#teste2e_nodenuma_alignmentgo)

- 📄 [test/e2e_node/perf/workloads/npb_ep.go](#teste2e_nodeperfworkloadsnpb_epgo)

- 📄 [test/e2e_node/perf/workloads/npb_is.go](#teste2e_nodeperfworkloadsnpb_isgo)

- 📄 [test/e2e_node/perf/workloads/pytorch_wide_deep.go](#teste2e_nodeperfworkloadspytorch_wide_deepgo)

- 📄 [test/e2e_node/perf/workloads/utils.go](#teste2e_nodeperfworkloadsutilsgo)

- 📄 [test/e2e_node/plugins/gcp-credential-provider/main.go](#teste2e_nodepluginsgcp-credential-providermaingo)

- 📄 [test/e2e_node/plugins/gcp-credential-provider/provider.go](#teste2e_nodepluginsgcp-credential-providerprovidergo)

- 📄 [test/e2e_node/pod_host_ips.go](#teste2e_nodepod_host_ipsgo)

- 📄 [test/e2e_node/remote/cadvisor_e2e.go](#teste2e_noderemotecadvisor_e2ego)

- 📄 [test/e2e_node/remote/gce/gce_runner.go](#teste2e_noderemotegcegce_runnergo)

- 📄 [test/e2e_node/remote/gce/gcloud.go](#teste2e_noderemotegcegcloudgo)

- 📄 [test/e2e_node/remote/node_conformance.go](#teste2e_noderemotenode_conformancego)

- 📄 [test/e2e_node/remote/node_e2e.go](#teste2e_noderemotenode_e2ego)

- 📄 [test/e2e_node/remote/remote.go](#teste2e_noderemoteremotego)

- 📄 [test/e2e_node/remote/run_remote_suite.go](#teste2e_noderemoterun_remote_suitego)

- 📄 [test/e2e_node/remote/ssh.go](#teste2e_noderemotesshgo)

- 📄 [test/e2e_node/remote/ssh_runner.go](#teste2e_noderemotessh_runnergo)

- 📄 [test/e2e_node/remote/types.go](#teste2e_noderemotetypesgo)

- 📄 [test/e2e_node/remote/utils.go](#teste2e_noderemoteutilsgo)

- 📄 [test/e2e_node/resource_collector.go](#teste2e_noderesource_collectorgo)

- 📄 [test/e2e_node/runner/local/run_local.go](#teste2e_noderunnerlocalrun_localgo)

- 📄 [test/e2e_node/runner/remote/run_remote.go](#teste2e_noderunnerremoterun_remotego)

- 📄 [test/e2e_node/services/apiserver.go](#teste2e_nodeservicesapiservergo)

- 📄 [test/e2e_node/services/internal_services.go](#teste2e_nodeservicesinternal_servicesgo)

- 📄 [test/e2e_node/services/kubelet.go](#teste2e_nodeserviceskubeletgo)

- 📄 [test/e2e_node/services/logs.go](#teste2e_nodeserviceslogsgo)

- 📄 [test/e2e_node/services/namespace_controller.go](#teste2e_nodeservicesnamespace_controllergo)

- 📄 [test/e2e_node/services/server.go](#teste2e_nodeservicesservergo)

- 📄 [test/e2e_node/services/services.go](#teste2e_nodeservicesservicesgo)

- 📄 [test/e2e_node/services/util.go](#teste2e_nodeservicesutilgo)

- 📄 [test/e2e_node/testdeviceplugin/device-plugin.go](#teste2e_nodetestdeviceplugindevice-plugingo)

- 📄 [test/e2e_node/testing-manifests/embed.go](#teste2e_nodetesting-manifestsembedgo)

- 📄 [test/e2e_node/util.go](#teste2e_nodeutilgo)

- 📄 [test/e2e_node/util_criproxy_linux.go](#teste2e_nodeutil_criproxy_linuxgo)

- 📄 [test/e2e_node/util_kubeletconfig.go](#teste2e_nodeutil_kubeletconfiggo)

- 📄 [test/e2e_node/util_machineinfo_linux.go](#teste2e_nodeutil_machineinfo_linuxgo)

- 📄 [test/e2e_node/util_machineinfo_unsupported.go](#teste2e_nodeutil_machineinfo_unsupportedgo)

- 📄 [test/e2e_node/util_sriov.go](#teste2e_nodeutil_sriovgo)

- 📄 [test/e2e_node/util_sriov_linux.go](#teste2e_nodeutil_sriov_linuxgo)

- 📄 [test/e2e_node/util_sriov_unsupported.go](#teste2e_nodeutil_sriov_unsupportedgo)

- 📄 [test/e2e_node/util_xfs_linux.go](#teste2e_nodeutil_xfs_linuxgo)

- 📄 [test/e2e_node/util_xfs_unsupported.go](#teste2e_nodeutil_xfs_unsupportedgo)


---


## test/e2e_node/benchmark_util.go


📄 Исходный файл: `test/e2e_node/benchmark_util.go`


<details open>
<summary><b>Функции в этом файле (11)</b></summary>


- 🔗 [Len](#len-teste2e_nodebenchmark_utilgo96) `:96`

- 🔗 [Less](#less-teste2e_nodebenchmark_utilgo98) `:98`

- 🔗 [Swap](#swap-teste2e_nodebenchmark_utilgo97) `:97`

- 🔗 [dumpDataToFile](#dumpdatatofile-teste2e_nodebenchmark_utilgo48) `:48`

- 🔗 [getCumulatedPodTimeSeries](#getcumulatedpodtimeseries-teste2e_nodebenchmark_utilgo101) `:101`

- 🔗 [getLatencyPerfData](#getlatencyperfdata-teste2e_nodebenchmark_utilgo112) `:112`

- 🔗 [getTestNodeInfo](#gettestnodeinfo-teste2e_nodebenchmark_utilgo158) `:158`

- 🔗 [getThroughputPerfData](#getthroughputperfdata-teste2e_nodebenchmark_utilgo135) `:135`

- 🔗 [logDensityTimeSeries](#logdensitytimeseries-teste2e_nodebenchmark_utilgo74) `:74`

- 🔗 [logPerfData](#logperfdata-teste2e_nodebenchmark_utilgo62) `:62`

- 🔗 [printPerfData](#printperfdata-teste2e_nodebenchmark_utilgo198) `:198`


</details>


[function] name: Len file: test/e2e_node/benchmark_util.go:96 returns_error: нет description: —


### Len (test/e2e_node/benchmark_util.go:96)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (a int64arr) Len(()) ()
```


📍 *Расположение:* `test/e2e_node/benchmark_util.go:96`



---


[function] name: Less file: test/e2e_node/benchmark_util.go:98 returns_error: нет description: —


### Less (test/e2e_node/benchmark_util.go:98)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (a int64arr) Less((i, j int)) (i, j int)
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


📍 *Расположение:* `test/e2e_node/benchmark_util.go:98`



---


[function] name: Swap file: test/e2e_node/benchmark_util.go:97 returns_error: нет description: —


### Swap (test/e2e_node/benchmark_util.go:97)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (a int64arr) Swap((i, j int)) (i, j int)
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


📍 *Расположение:* `test/e2e_node/benchmark_util.go:97`



---


[function] name: dumpDataToFile file: test/e2e_node/benchmark_util.go:48 returns_error: нет description: dumpDataToFile inserts the current timestamp into the labels and writes the
data for the test into the file with the spe


### dumpDataToFile (test/e2e_node/benchmark_util.go:48)


dumpDataToFile inserts the current timestamp into the labels and writes the
data for the test into the file with the specified prefix.


```go
func dumpDataToFile((data interface{}, labels map[string]string, prefix string)) (data interface{}, labels map[string]string, prefix string)
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


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


**Тип ответа:** labels


```json
{
  "key": "string",
  "namespace": "string"
}
```


*Определено в:* `pkg/controller/util/selectors/bimultimap.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** prefix


```json
{
  "prefix": "string",
  "handler": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go`


📍 *Расположение:* `test/e2e_node/benchmark_util.go:48`



---


[function] name: getCumulatedPodTimeSeries file: test/e2e_node/benchmark_util.go:101 returns_error: нет description: getCumulatedPodTimeSeries gets the cumulative pod number time series.


### getCumulatedPodTimeSeries (test/e2e_node/benchmark_util.go:101)


getCumulatedPodTimeSeries gets the cumulative pod number time series.


```go
func getCumulatedPodTimeSeries((timePerPod map[string]metav1.Time)) (timePerPod map[string]metav1.Time)
```


**Тип ответа:** timePerPod


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** metav1.Time


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


📍 *Расположение:* `test/e2e_node/benchmark_util.go:101`



---


[function] name: getLatencyPerfData file: test/e2e_node/benchmark_util.go:112 returns_error: нет description: getLatencyPerfData returns perf data of pod startup latency.


### getLatencyPerfData (test/e2e_node/benchmark_util.go:112)


getLatencyPerfData returns perf data of pod startup latency.


```go
func getLatencyPerfData((latency e2emetrics.LatencyMetric, testInfo map[string]string)) (latency e2emetrics.LatencyMetric, testInfo map[string]string)
```


**Тип ответа:** latency


```json
{
  "m": null
}
```


*Определено в:* `staging/src/k8s.io/component-base/metrics/prometheus/restclient/metrics.go`


**Тип ответа:** e2emetrics.LatencyMetric


```json
{
  "Perc50": {},
  "Perc90": {},
  "Perc99": {},
  "Perc100": {}
}
```


*Определено в:* `test/e2e/framework/metrics/pod.go`


**Тип ответа:** testInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/e2e_node/benchmark_util.go:112`



---


[function] name: getTestNodeInfo file: test/e2e_node/benchmark_util.go:158 returns_error: нет description: getTestNodeInfo returns a label map containing the test name and
description, the name of the node on which the test wil


### getTestNodeInfo (test/e2e_node/benchmark_util.go:158)


getTestNodeInfo returns a label map containing the test name and
description, the name of the node on which the test will be run, the image
name of the node, and the node capacities.


```go
func getTestNodeInfo((f *framework.Framework, testName, testDesc string)) (f *framework.Framework, testName, testDesc string)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** testName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** testDesc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/benchmark_util.go:158`



---


[function] name: getThroughputPerfData file: test/e2e_node/benchmark_util.go:135 returns_error: нет description: getThroughputPerfData returns perf data of pod creation startup throughput.


### getThroughputPerfData (test/e2e_node/benchmark_util.go:135)


getThroughputPerfData returns perf data of pod creation startup throughput.


```go
func getThroughputPerfData((batchLag time.Duration, e2eLags []e2emetrics.PodLatencyData, podsNr int, testInfo map[string]string)) (batchLag time.Duration, e2eLags []e2emetrics.PodLatencyData, podsNr int, testInfo map[string]string)
```


**Тип ответа:** batchLag


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


**Тип ответа:** e2eLags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** e2emetrics.PodLatencyData


```json
{
  "Name": "string",
  "Node": "string",
  "Latency": {}
}
```


*Определено в:* `test/e2e/framework/metrics/latencies.go`


**Тип ответа:** podsNr


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** testInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/e2e_node/benchmark_util.go:135`



---


[function] name: logDensityTimeSeries file: test/e2e_node/benchmark_util.go:74 returns_error: нет description: logDensityTimeSeries writes the time series data of operation and resource
usage to a standalone json file if the framew


### logDensityTimeSeries (test/e2e_node/benchmark_util.go:74)


logDensityTimeSeries writes the time series data of operation and resource
usage to a standalone json file if the framework.TestContext.ReportDir is
non-empty, or to the general build log otherwise. If an error occurs,
no perf data will be logged.


```go
func logDensityTimeSeries((rc *ResourceCollector, create, watch map[string]metav1.Time, testInfo map[string]string)) (rc *ResourceCollector, create, watch map[string]metav1.Time, testInfo map[string]string)
```


**Тип запроса:** ResourceCollector


```json
{
  "client": null,
  "request": null,
  "pollingInterval": {},
  "buffers": {},
  "lock": {},
  "stopCh": {}
}
```


*Определено в:* `test/e2e_node/resource_collector.go`


**Тип ответа:** rc


```json
{
  "Printer": {}
}
```


*Определено в:* `cmd/kubeadm/app/util/output/output.go`


**Тип ответа:** ResourceCollector


```json
{
  "client": null,
  "request": null,
  "pollingInterval": {},
  "buffers": {},
  "lock": {},
  "stopCh": {}
}
```


*Определено в:* `test/e2e_node/resource_collector.go`


**Тип ответа:** create


```json
{
  "Opcode": {},
  "Count": 0,
  "CountParam": "string",
  "Namespace": "string",
  "TemplatePath": "string"
}
```


*Определено в:* `test/integration/scheduler_perf/dra.go`


**Тип ответа:** watch


```json
{
  "parent": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/listwatch.go`


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** metav1.Time


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


**Тип ответа:** testInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/e2e_node/benchmark_util.go:74`



---


[function] name: logPerfData file: test/e2e_node/benchmark_util.go:62 returns_error: нет description: logPerfData writes the perf data to a standalone json file if the
framework.TestContext.ReportDir is non-empty, or to th


### logPerfData (test/e2e_node/benchmark_util.go:62)


logPerfData writes the perf data to a standalone json file if the
framework.TestContext.ReportDir is non-empty, or to the general build log
otherwise. The perfType identifies which type of the perf data it is, such
as "cpu" and "memory". If an error occurs, no perf data will be logged.


```go
func logPerfData((p *perftype.PerfData, perfType string)) (p *perftype.PerfData, perfType string)
```


**Тип запроса:** perftype.PerfData


```json
{
  "Version": "string",
  "DataItems": [],
  "Labels": {}
}
```


*Определено в:* `test/e2e/perftype/perftype.go`


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


**Тип ответа:** perftype.PerfData


```json
{
  "Version": "string",
  "DataItems": [],
  "Labels": {}
}
```


*Определено в:* `test/e2e/perftype/perftype.go`


**Тип ответа:** perfType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/benchmark_util.go:62`



---


[function] name: printPerfData file: test/e2e_node/benchmark_util.go:198 returns_error: нет description: printPerfData prints the perfdata in json format with PerfResultTag prefix.
If an error occurs, nothing will be printed.


### printPerfData (test/e2e_node/benchmark_util.go:198)


printPerfData prints the perfdata in json format with PerfResultTag prefix.
If an error occurs, nothing will be printed.


```go
func printPerfData((p *perftype.PerfData)) (p *perftype.PerfData)
```


**Тип запроса:** perftype.PerfData


```json
{
  "Version": "string",
  "DataItems": [],
  "Labels": {}
}
```


*Определено в:* `test/e2e/perftype/perftype.go`


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


**Тип ответа:** perftype.PerfData


```json
{
  "Version": "string",
  "DataItems": [],
  "Labels": {}
}
```


*Определено в:* `test/e2e/perftype/perftype.go`


📍 *Расположение:* `test/e2e_node/benchmark_util.go:198`




## test/e2e_node/builder/build.go


📄 Исходный файл: `test/e2e_node/builder/build.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [BuildGo](#buildgo-teste2e_nodebuilderbuildgo47) `:47`

- 🔗 [BuildTargets](#buildtargets-teste2e_nodebuilderbuildgo58) `:58`

- 🔗 [GetKubeletServerBin](#getkubeletserverbin-teste2e_nodebuilderbuildgo141) `:141`

- 🔗 [GetTargetBuildArch](#gettargetbuildarch-teste2e_nodebuilderbuildgo98) `:98`

- 🔗 [IsDockerizedBuild](#isdockerizedbuild-teste2e_nodebuilderbuildgo93) `:93`

- 🔗 [IsTargetArchArm64](#istargetarcharm64-teste2e_nodebuilderbuildgo103) `:103`

- 🔗 [getK8sBin](#getk8sbin-teste2e_nodebuilderbuildgo107) `:107`


</details>


[function] name: BuildGo file: test/e2e_node/builder/build.go:47 returns_error: нет description: BuildGo builds k8s binaries.


### BuildGo (test/e2e_node/builder/build.go:47)


BuildGo builds k8s binaries.


```go
func BuildGo(()) ()
```


📍 *Расположение:* `test/e2e_node/builder/build.go:47`



---


[function] name: BuildTargets file: test/e2e_node/builder/build.go:58 returns_error: нет description: BuildGo builds k8s binaries.


### BuildTargets (test/e2e_node/builder/build.go:58)


BuildGo builds k8s binaries.


```go
func BuildTargets((cgo bool)) (cgo bool)
```


**Тип ответа:** cgo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/builder/build.go:58`



---


[function] name: GetKubeletServerBin file: test/e2e_node/builder/build.go:141 returns_error: нет description: GetKubeletServerBin returns the path of kubelet binary.


### GetKubeletServerBin (test/e2e_node/builder/build.go:141)


GetKubeletServerBin returns the path of kubelet binary.


```go
func GetKubeletServerBin(()) ()
```


📍 *Расположение:* `test/e2e_node/builder/build.go:141`



---


[function] name: GetTargetBuildArch file: test/e2e_node/builder/build.go:98 returns_error: нет description: GetTargetBuildArch returns the target build architecture for dockerized build


### GetTargetBuildArch (test/e2e_node/builder/build.go:98)


GetTargetBuildArch returns the target build architecture for dockerized build


```go
func GetTargetBuildArch(()) ()
```


📍 *Расположение:* `test/e2e_node/builder/build.go:98`



---


[function] name: IsDockerizedBuild file: test/e2e_node/builder/build.go:93 returns_error: нет description: IsDockerizedBuild returns if test needs to use dockerized build


### IsDockerizedBuild (test/e2e_node/builder/build.go:93)


IsDockerizedBuild returns if test needs to use dockerized build


```go
func IsDockerizedBuild(()) ()
```


📍 *Расположение:* `test/e2e_node/builder/build.go:93`



---


[function] name: IsTargetArchArm64 file: test/e2e_node/builder/build.go:103 returns_error: нет description: IsTargetArchArm64 returns if the target is for linux/arm64 platform


### IsTargetArchArm64 (test/e2e_node/builder/build.go:103)


IsTargetArchArm64 returns if the target is for linux/arm64 platform


```go
func IsTargetArchArm64(()) ()
```


📍 *Расположение:* `test/e2e_node/builder/build.go:103`



---


[function] name: getK8sBin file: test/e2e_node/builder/build.go:107 returns_error: да description: —


### getK8sBin (test/e2e_node/builder/build.go:107)


getK8sBin is a function that performs operations based on the provided parameters and may return an error.


```go
func getK8sBin((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/builder/build.go:107`




## test/e2e_node/checkpoint_container.go


📄 Исходный файл: `test/e2e_node/checkpoint_container.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [getCheckpointContainerErrorMetric](#getcheckpointcontainererrormetric-teste2e_nodecheckpoint_containergo107) `:107`

- 🔗 [getCheckpointContainerMetric](#getcheckpointcontainermetric-teste2e_nodecheckpoint_containergo81) `:81`

- 🔗 [proxyPostRequest](#proxypostrequest-teste2e_nodecheckpoint_containergo57) `:57`


</details>


[function] name: getCheckpointContainerErrorMetric file: test/e2e_node/checkpoint_container.go:107 returns_error: да description: —


### getCheckpointContainerErrorMetric (test/e2e_node/checkpoint_container.go:107)


getCheckpointContainerErrorMetric is a function that performs operations based on the provided parameters and may return an error.


```go
func getCheckpointContainerErrorMetric((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/checkpoint_container.go:107`



---


[function] name: getCheckpointContainerMetric file: test/e2e_node/checkpoint_container.go:81 returns_error: да description: —


### getCheckpointContainerMetric (test/e2e_node/checkpoint_container.go:81)


getCheckpointContainerMetric is a function that performs operations based on the provided parameters and may return an error.


```go
func getCheckpointContainerMetric((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/checkpoint_container.go:81`



---


[function] name: proxyPostRequest file: test/e2e_node/checkpoint_container.go:57 returns_error: да description: proxyPostRequest performs a post on a node proxy endpoint given the nodename and rest client.


### proxyPostRequest (test/e2e_node/checkpoint_container.go:57)


proxyPostRequest performs a post on a node proxy endpoint given the nodename and rest client.


```go
func proxyPostRequest((restclient.Result, error)) (restclient.Result, error)
```


**Тип ответа:** restclient.Result


```json
{
  "Host": "string",
  "Cmd": "string",
  "Stdout": "string",
  "Stderr": "string",
  "Code": 0
}
```


*Определено в:* `test/e2e/storage/utils/host_exec.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `restclient.Result`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/checkpoint_container.go:57`




## test/e2e_node/container_lifecycle_pod_construction.go


📄 Исходный файл: `test/e2e_node/container_lifecycle_pod_construction.go`


<details open>
<summary><b>Функции в этом файле (20)</b></summary>


- 🔗 [DoesntStart](#doesntstart-teste2e_nodecontainer_lifecycle_pod_constructiongo216) `:216`

- 🔗 [ExecCommand](#execcommand-teste2e_nodecontainer_lifecycle_pod_constructiongo62) `:62`

- 🔗 [Exits](#exits-teste2e_nodecontainer_lifecycle_pod_constructiongo224) `:224`

- 🔗 [ExitsBefore](#exitsbefore-teste2e_nodecontainer_lifecycle_pod_constructiongo191) `:191`

- 🔗 [FindIndex](#findindex-teste2e_nodecontainer_lifecycle_pod_constructiongo272) `:272`

- 🔗 [HasNotRestarted](#hasnotrestarted-teste2e_nodecontainer_lifecycle_pod_constructiongo248) `:248`

- 🔗 [HasRestarted](#hasrestarted-teste2e_nodecontainer_lifecycle_pod_constructiongo232) `:232`

- 🔗 [IsBefore](#isbefore-teste2e_nodecontainer_lifecycle_pod_constructiongo265) `:265`

- 🔗 [RunTogether](#runtogether-teste2e_nodecontainer_lifecycle_pod_constructiongo131) `:131`

- 🔗 [RunTogetherLhsFirst](#runtogetherlhsfirst-teste2e_nodecontainer_lifecycle_pod_constructiongo141) `:141`

- 🔗 [Starts](#starts-teste2e_nodecontainer_lifecycle_pod_constructiongo208) `:208`

- 🔗 [StartsBefore](#startsbefore-teste2e_nodecontainer_lifecycle_pod_constructiongo174) `:174`

- 🔗 [String](#string-teste2e_nodecontainer_lifecycle_pod_constructiongo122) `:122`

- 🔗 [TimeOfLastLoop](#timeoflastloop-teste2e_nodecontainer_lifecycle_pod_constructiongo311) `:311`

- 🔗 [TimeOfStart](#timeofstart-teste2e_nodecontainer_lifecycle_pod_constructiongo302) `:302`

- 🔗 [findIndex](#findindex-teste2e_nodecontainer_lifecycle_pod_constructiongo280) `:280`

- 🔗 [findLastIndex](#findlastindex-teste2e_nodecontainer_lifecycle_pod_constructiongo291) `:291`

- 🔗 [parseOutput](#parseoutput-teste2e_nodecontainer_lifecycle_pod_constructiongo323) `:323`

- 🔗 [preparePod](#preparepod-teste2e_nodecontainer_lifecycle_pod_constructiongo372) `:372`

- 🔗 [sleepCommand](#sleepcommand-teste2e_nodecontainer_lifecycle_pod_constructiongo110) `:110`


</details>


[function] name: DoesntStart file: test/e2e_node/container_lifecycle_pod_construction.go:216 returns_error: нет description: DoesntStart returns an error if the container was found to have started


### DoesntStart (test/e2e_node/container_lifecycle_pod_construction.go:216)


DoesntStart returns an error if the container was found to have started


```go
func (o containerOutputList) DoesntStart((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:216`



---


[function] name: ExecCommand file: test/e2e_node/container_lifecycle_pod_construction.go:62 returns_error: нет description: ExecCommand returns the command to execute in the container that implements
execCommand and logs activities to a contain


### ExecCommand (test/e2e_node/container_lifecycle_pod_construction.go:62)


ExecCommand returns the command to execute in the container that implements
execCommand and logs activities to a container specific log that persists
across container restarts. The final log is written to container log so it
can be retrieved by the test harness during the container execution.
Log to /proc/1/fd/1 so that the lifecycle hook handler logs are captured as
well.


```go
func ExecCommand((name string, c execCommand)) (name string, c execCommand)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


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


**Тип ответа:** execCommand


```json
{
  "ExitCode": 0,
  "StartDelay": 0,
  "Delay": 0,
  "LoopForever": false,
  "TerminationSeconds": 0,
  "ContainerName": "string",
  "LoopPeriod": 0.0
}
```


*Определено в:* `test/e2e_node/container_lifecycle_pod_construction.go`


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:62`



---


[function] name: Exits file: test/e2e_node/container_lifecycle_pod_construction.go:224 returns_error: нет description: Exits returns an error if the container was not found to have exited


### Exits (test/e2e_node/container_lifecycle_pod_construction.go:224)


Exits returns an error if the container was not found to have exited


```go
func (o containerOutputList) Exits((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:224`



---


[function] name: ExitsBefore file: test/e2e_node/container_lifecycle_pod_construction.go:191 returns_error: нет description: ExitsBefore returns an error if lhs did not end before rhs


### ExitsBefore (test/e2e_node/container_lifecycle_pod_construction.go:191)


ExitsBefore returns an error if lhs did not end before rhs


```go
func (o containerOutputList) ExitsBefore((lhs, rhs string)) (lhs, rhs string)
```


**Тип ответа:** lhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:191`



---


[function] name: FindIndex file: test/e2e_node/container_lifecycle_pod_construction.go:272 returns_error: да description: —


### FindIndex (test/e2e_node/container_lifecycle_pod_construction.go:272)


FindIndex is a method that lists or finds data based on the provided parameters and may return an error.


```go
func (o containerOutputList) FindIndex((containerOutputIndex, error)) (containerOutputIndex, error)
```


**Тип ответа:** containerOutputIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `containerOutputIndex`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:272`



---


[function] name: HasNotRestarted file: test/e2e_node/container_lifecycle_pod_construction.go:248 returns_error: нет description: HasNotRestarted returns an error if the container was found to have restarted


### HasNotRestarted (test/e2e_node/container_lifecycle_pod_construction.go:248)


HasNotRestarted returns an error if the container was found to have restarted


```go
func (o containerOutputList) HasNotRestarted((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:248`



---


[function] name: HasRestarted file: test/e2e_node/container_lifecycle_pod_construction.go:232 returns_error: нет description: HasRestarted returns an error if the container was not found to have restarted


### HasRestarted (test/e2e_node/container_lifecycle_pod_construction.go:232)


HasRestarted returns an error if the container was not found to have restarted


```go
func (o containerOutputList) HasRestarted((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:232`



---


[function] name: IsBefore file: test/e2e_node/container_lifecycle_pod_construction.go:265 returns_error: нет description: —


### IsBefore (test/e2e_node/container_lifecycle_pod_construction.go:265)


IsBefore is a method that performs operations based on the provided parameters and returns (other containerOutputIndex).


```go
func (i containerOutputIndex) IsBefore((other containerOutputIndex)) (other containerOutputIndex)
```


**Тип ответа:** other


```json
{
  "OS": "string"
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ordering/structs/doc.go`


**Тип ответа:** containerOutputIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:265`



---


[function] name: RunTogether file: test/e2e_node/container_lifecycle_pod_construction.go:131 returns_error: нет description: RunTogether returns an error if containers don't run together


### RunTogether (test/e2e_node/container_lifecycle_pod_construction.go:131)


RunTogether returns an error if containers don't run together


```go
func (o containerOutputList) RunTogether((lhs, rhs string)) (lhs, rhs string)
```


**Тип ответа:** lhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:131`



---


[function] name: RunTogetherLhsFirst file: test/e2e_node/container_lifecycle_pod_construction.go:141 returns_error: нет description: RunTogetherLhsFirst returns an error if containers don't run together or if rhs starts before lhs


### RunTogetherLhsFirst (test/e2e_node/container_lifecycle_pod_construction.go:141)


RunTogetherLhsFirst returns an error if containers don't run together or if rhs starts before lhs


```go
func (o containerOutputList) RunTogetherLhsFirst((lhs, rhs string)) (lhs, rhs string)
```


**Тип ответа:** lhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:141`



---


[function] name: Starts file: test/e2e_node/container_lifecycle_pod_construction.go:208 returns_error: нет description: Starts returns an error if the container was not found to have started


### Starts (test/e2e_node/container_lifecycle_pod_construction.go:208)


Starts returns an error if the container was not found to have started


```go
func (o containerOutputList) Starts((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:208`



---


[function] name: StartsBefore file: test/e2e_node/container_lifecycle_pod_construction.go:174 returns_error: нет description: StartsBefore returns an error if lhs did not start before rhs


### StartsBefore (test/e2e_node/container_lifecycle_pod_construction.go:174)


StartsBefore returns an error if lhs did not start before rhs


```go
func (o containerOutputList) StartsBefore((lhs, rhs string)) (lhs, rhs string)
```


**Тип ответа:** lhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** rhs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:174`



---


[function] name: String file: test/e2e_node/container_lifecycle_pod_construction.go:122 returns_error: нет description: —


### String (test/e2e_node/container_lifecycle_pod_construction.go:122)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (o containerOutputList) String(()) ()
```


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:122`



---


[function] name: TimeOfLastLoop file: test/e2e_node/container_lifecycle_pod_construction.go:311 returns_error: да description: TimeOfLastLoop returns the UNIX time in milliseconds when the specified container last looped.


### TimeOfLastLoop (test/e2e_node/container_lifecycle_pod_construction.go:311)


TimeOfLastLoop returns the UNIX time in milliseconds when the specified container last looped.


```go
func (o containerOutputList) TimeOfLastLoop((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:311`



---


[function] name: TimeOfStart file: test/e2e_node/container_lifecycle_pod_construction.go:302 returns_error: да description: TimeOfStart returns the UNIX time in milliseconds when the specified container started.


### TimeOfStart (test/e2e_node/container_lifecycle_pod_construction.go:302)


TimeOfStart returns the UNIX time in milliseconds when the specified container started.


```go
func (o containerOutputList) TimeOfStart((int64, error)) (int64, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int64`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:302`



---


[function] name: findIndex file: test/e2e_node/container_lifecycle_pod_construction.go:280 returns_error: нет description: —


### findIndex (test/e2e_node/container_lifecycle_pod_construction.go:280)


findIndex is a method that performs operations based on the provided parameters and returns (name string, command string, startIdx int).


```go
func (o containerOutputList) findIndex((name string, command string, startIdx int)) (name string, command string, startIdx int)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** command


```json
{
  "PrintFlags": null,
  "Name": "string",
  "StructuredGenerator": {},
  "DryRunStrategy": {},
  "CreateAnnotation": false,
  "FieldManager": "string",
  "ValidationDirective": "string",
  "Namespace": "string",
  "EnforceNamespace": false,
  "Mapper": {},
  "DynamicClient": {},
  "PrintObj": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/create/create.go`


**Тип ответа:** startIdx


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:280`



---


[function] name: findLastIndex file: test/e2e_node/container_lifecycle_pod_construction.go:291 returns_error: нет description: —


### findLastIndex (test/e2e_node/container_lifecycle_pod_construction.go:291)


findLastIndex is a method that performs operations based on the provided parameters and returns (name string, command string).


```go
func (o containerOutputList) findLastIndex((name string, command string)) (name string, command string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** command


```json
{
  "PrintFlags": null,
  "Name": "string",
  "StructuredGenerator": {},
  "DryRunStrategy": {},
  "CreateAnnotation": false,
  "FieldManager": "string",
  "ValidationDirective": "string",
  "Namespace": "string",
  "EnforceNamespace": false,
  "Mapper": {},
  "DynamicClient": {},
  "PrintObj": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/create/create.go`


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:291`



---


[function] name: parseOutput file: test/e2e_node/container_lifecycle_pod_construction.go:323 returns_error: нет description: parseOutput combines the container log from all of the init and regular
containers and parses/sorts the outputs to produ


### parseOutput (test/e2e_node/container_lifecycle_pod_construction.go:323)


parseOutput combines the container log from all of the init and regular
containers and parses/sorts the outputs to produce an execution log


```go
func parseOutput((ctx context.Context, f *framework.Framework, pod *v1.Pod)) (ctx context.Context, f *framework.Framework, pod *v1.Pod)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип запроса:** v1.Pod


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** v1.Pod


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


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:323`



---


[function] name: preparePod file: test/e2e_node/container_lifecycle_pod_construction.go:372 returns_error: нет description: preparePod adds an empty dir volume and mounts it to each container at /persistent


### preparePod (test/e2e_node/container_lifecycle_pod_construction.go:372)


preparePod adds an empty dir volume and mounts it to each container at /persistent


```go
func preparePod((pod *v1.Pod)) (pod *v1.Pod)
```


**Тип запроса:** v1.Pod


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


**Тип ответа:** pod


```json
{
  "podName": {},
  "podObj": null
}
```


*Определено в:* `pkg/controller/volume/attachdetach/cache/desired_state_of_world.go`


**Тип ответа:** v1.Pod


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


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:372`



---


[function] name: sleepCommand file: test/e2e_node/container_lifecycle_pod_construction.go:110 returns_error: нет description: sleepCommand returns a command that sleeps for the given number of seconds
in background and waits for it to finish so t


### sleepCommand (test/e2e_node/container_lifecycle_pod_construction.go:110)


sleepCommand returns a command that sleeps for the given number of seconds
in background and waits for it to finish so that the parent process can
handle signals.


```go
func sleepCommand((seconds int)) (seconds int)
```


**Тип ответа:** seconds


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/container_lifecycle_pod_construction.go:110`




## test/e2e_node/criproxy/endpoint.go


📄 Исходный файл: `test/e2e_node/criproxy/endpoint.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GenerateEndpoint](#generateendpoint-teste2e_nodecriproxyendpointgo30) `:30`


</details>


[function] name: GenerateEndpoint file: test/e2e_node/criproxy/endpoint.go:30 returns_error: да description: GenerateEndpoint generates a new unix socket server of grpc server.


### GenerateEndpoint (test/e2e_node/criproxy/endpoint.go:30)


GenerateEndpoint generates a new unix socket server of grpc server.


```go
func GenerateEndpoint((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/endpoint.go:30`




## test/e2e_node/criproxy/proxy_image_service.go


📄 Исходный файл: `test/e2e_node/criproxy/proxy_image_service.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [ImageFsInfo](#imagefsinfo-teste2e_nodecriproxyproxy_image_servicego94) `:94`

- 🔗 [ImageStatus](#imagestatus-teste2e_nodecriproxyproxy_image_servicego51) `:51`

- 🔗 [ListImages](#listimages-teste2e_nodecriproxyproxy_image_servicego34) `:34`

- 🔗 [PullImage](#pullimage-teste2e_nodecriproxyproxy_image_servicego64) `:64`

- 🔗 [RemoveImage](#removeimage-teste2e_nodecriproxyproxy_image_servicego81) `:81`


</details>


[function] name: ImageFsInfo file: test/e2e_node/criproxy/proxy_image_service.go:94 returns_error: да description: ImageFsInfo returns information of the filesystem that is used to store images.


### ImageFsInfo (test/e2e_node/criproxy/proxy_image_service.go:94)


ImageFsInfo returns information of the filesystem that is used to store images.


```go
func (p *RemoteRuntime) ImageFsInfo((*kubeapi.ImageFsInfoResponse, error)) (*kubeapi.ImageFsInfoResponse, error)
```


**Тип запроса:** kubeapi.ImageFsInfoResponse


```json
{
  "state": {},
  "imageFilesystems": [],
  "containerFilesystems": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** kubeapi.ImageFsInfoResponse


```json
{
  "state": {},
  "imageFilesystems": [],
  "containerFilesystems": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeapi.ImageFsInfoResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_image_service.go:94`



---


[function] name: ImageStatus file: test/e2e_node/criproxy/proxy_image_service.go:51 returns_error: да description: ImageStatus returns the status of the image. If the image is not
present, returns a response with ImageStatusResponse.Im


### ImageStatus (test/e2e_node/criproxy/proxy_image_service.go:51)


ImageStatus returns the status of the image. If the image is not
present, returns a response with ImageStatusResponse.Image set to
nil.


```go
func (p *RemoteRuntime) ImageStatus((*kubeapi.ImageStatusResponse, error)) (*kubeapi.ImageStatusResponse, error)
```


**Тип запроса:** kubeapi.ImageStatusResponse


```json
{
  "state": {},
  "Image": null,
  "info": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** kubeapi.ImageStatusResponse


```json
{
  "state": {},
  "Image": null,
  "info": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeapi.ImageStatusResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_image_service.go:51`



---


[function] name: ListImages file: test/e2e_node/criproxy/proxy_image_service.go:34 returns_error: да description: ListImages lists existing images.


### ListImages (test/e2e_node/criproxy/proxy_image_service.go:34)


ListImages lists existing images.


```go
func (p *RemoteRuntime) ListImages((*kubeapi.ListImagesResponse, error)) (*kubeapi.ListImagesResponse, error)
```


**Тип запроса:** kubeapi.ListImagesResponse


```json
{
  "state": {},
  "Images": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** kubeapi.ListImagesResponse


```json
{
  "state": {},
  "Images": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeapi.ListImagesResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_image_service.go:34`



---


[function] name: PullImage file: test/e2e_node/criproxy/proxy_image_service.go:64 returns_error: да description: PullImage pulls an image with authentication config.


### PullImage (test/e2e_node/criproxy/proxy_image_service.go:64)


PullImage pulls an image with authentication config.


```go
func (p *RemoteRuntime) PullImage((*kubeapi.PullImageResponse, error)) (*kubeapi.PullImageResponse, error)
```


**Тип запроса:** kubeapi.PullImageResponse


```json
{
  "state": {},
  "imageRef": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** kubeapi.PullImageResponse


```json
{
  "state": {},
  "imageRef": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeapi.PullImageResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_image_service.go:64`



---


[function] name: RemoveImage file: test/e2e_node/criproxy/proxy_image_service.go:81 returns_error: да description: RemoveImage removes the image.
This call is idempotent, and must not return an error if the image has
already been remov


### RemoveImage (test/e2e_node/criproxy/proxy_image_service.go:81)


RemoveImage removes the image.
This call is idempotent, and must not return an error if the image has
already been removed.


```go
func (p *RemoteRuntime) RemoveImage((*kubeapi.RemoveImageResponse, error)) (*kubeapi.RemoveImageResponse, error)
```


**Тип запроса:** kubeapi.RemoveImageResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** kubeapi.RemoveImageResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeapi.RemoveImageResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_image_service.go:81`




## test/e2e_node/criproxy/proxy_runtime_service.go


📄 Исходный файл: `test/e2e_node/criproxy/proxy_runtime_service.go`


<details open>
<summary><b>Функции в этом файле (36)</b></summary>


- 🔗 [AddInjector](#addinjector-teste2e_nodecriproxyproxy_runtime_servicego70) `:70`

- 🔗 [Attach](#attach-teste2e_nodecriproxyproxy_runtime_servicego329) `:329`

- 🔗 [CheckpointContainer](#checkpointcontainer-teste2e_nodecriproxyproxy_runtime_servicego462) `:462`

- 🔗 [ContainerStats](#containerstats-teste2e_nodecriproxyproxy_runtime_servicego348) `:348`

- 🔗 [ContainerStatus](#containerstatus-teste2e_nodecriproxyproxy_runtime_servicego284) `:284`

- 🔗 [CreateContainer](#createcontainer-teste2e_nodecriproxyproxy_runtime_servicego213) `:213`

- 🔗 [Exec](#exec-teste2e_nodecriproxyproxy_runtime_servicego320) `:320`

- 🔗 [ExecSync](#execsync-teste2e_nodecriproxyproxy_runtime_servicego297) `:297`

- 🔗 [GetContainerEvents](#getcontainerevents-teste2e_nodecriproxyproxy_runtime_servicego474) `:474`

- 🔗 [ListContainerStats](#listcontainerstats-teste2e_nodecriproxyproxy_runtime_servicego361) `:361`

- 🔗 [ListContainers](#listcontainers-teste2e_nodecriproxyproxy_runtime_servicego270) `:270`

- 🔗 [ListMetricDescriptors](#listmetricdescriptors-teste2e_nodecriproxyproxy_runtime_servicego499) `:499`

- 🔗 [ListPodSandbox](#listpodsandbox-teste2e_nodecriproxyproxy_runtime_servicego200) `:200`

- 🔗 [ListPodSandboxMetrics](#listpodsandboxmetrics-teste2e_nodecriproxyproxy_runtime_servicego512) `:512`

- 🔗 [ListPodSandboxStats](#listpodsandboxstats-teste2e_nodecriproxyproxy_runtime_servicego388) `:388`

- 🔗 [NewRemoteRuntimeProxy](#newremoteruntimeproxy-teste2e_nodecriproxyproxy_runtime_servicego99) `:99`

- 🔗 [PodSandboxStats](#podsandboxstats-teste2e_nodecriproxyproxy_runtime_servicego375) `:375`

- 🔗 [PodSandboxStatus](#podsandboxstatus-teste2e_nodecriproxyproxy_runtime_servicego187) `:187`

- 🔗 [PortForward](#portforward-teste2e_nodecriproxyproxy_runtime_servicego338) `:338`

- 🔗 [RemoveContainer](#removecontainer-teste2e_nodecriproxyproxy_runtime_servicego257) `:257`

- 🔗 [RemovePodSandbox](#removepodsandbox-teste2e_nodecriproxyproxy_runtime_servicego173) `:173`

- 🔗 [ReopenContainerLog](#reopencontainerlog-teste2e_nodecriproxyproxy_runtime_servicego449) `:449`

- 🔗 [ResetInjectors](#resetinjectors-teste2e_nodecriproxyproxy_runtime_servicego75) `:75`

- 🔗 [RunPodSandbox](#runpodsandbox-teste2e_nodecriproxyproxy_runtime_servicego141) `:141`

- 🔗 [RuntimeConfig](#runtimeconfig-teste2e_nodecriproxyproxy_runtime_servicego525) `:525`

- 🔗 [Start](#start-teste2e_nodecriproxyproxy_runtime_servicego112) `:112`

- 🔗 [StartContainer](#startcontainer-teste2e_nodecriproxyproxy_runtime_servicego226) `:226`

- 🔗 [Status](#status-teste2e_nodecriproxyproxy_runtime_servicego423) `:423`

- 🔗 [Stop](#stop-teste2e_nodecriproxyproxy_runtime_servicego127) `:127`

- 🔗 [StopContainer](#stopcontainer-teste2e_nodecriproxyproxy_runtime_servicego241) `:241`

- 🔗 [StopPodSandbox](#stoppodsandbox-teste2e_nodecriproxyproxy_runtime_servicego157) `:157`

- 🔗 [UpdateContainerResources](#updatecontainerresources-teste2e_nodecriproxyproxy_runtime_servicego436) `:436`

- 🔗 [UpdatePodSandboxResources](#updatepodsandboxresources-teste2e_nodecriproxyproxy_runtime_servicego414) `:414`

- 🔗 [UpdateRuntimeConfig](#updateruntimeconfig-teste2e_nodecriproxyproxy_runtime_servicego401) `:401`

- 🔗 [Version](#version-teste2e_nodecriproxyproxy_runtime_servicego132) `:132`

- 🔗 [runInjectors](#runinjectors-teste2e_nodecriproxyproxy_runtime_servicego79) `:79`


</details>


[function] name: AddInjector file: test/e2e_node/criproxy/proxy_runtime_service.go:70 returns_error: да description: AddInjector inject the error or delay to the next call to the RuntimeService.


### AddInjector (test/e2e_node/criproxy/proxy_runtime_service.go:70)


AddInjector inject the error or delay to the next call to the RuntimeService.


```go
func (p *RemoteRuntime) AddInjector((injector func(string) error)) (injector func(string) error)
```


**Тип ответа:** injector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `injector func(string) error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:70`



---


[function] name: Attach file: test/e2e_node/criproxy/proxy_runtime_service.go:329 returns_error: да description: Attach prepares a streaming endpoint to attach to a running container.


### Attach (test/e2e_node/criproxy/proxy_runtime_service.go:329)


Attach prepares a streaming endpoint to attach to a running container.


```go
func (p *RemoteRuntime) Attach((*runtimeapi.AttachResponse, error)) (*runtimeapi.AttachResponse, error)
```


**Тип запроса:** runtimeapi.AttachResponse


```json
{
  "state": {},
  "Url": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.AttachResponse


```json
{
  "state": {},
  "Url": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.AttachResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:329`



---


[function] name: CheckpointContainer file: test/e2e_node/criproxy/proxy_runtime_service.go:462 returns_error: да description: CheckpointContainer checkpoints the given container.


### CheckpointContainer (test/e2e_node/criproxy/proxy_runtime_service.go:462)


CheckpointContainer checkpoints the given container.


```go
func (p *RemoteRuntime) CheckpointContainer((*runtimeapi.CheckpointContainerResponse, error)) (*runtimeapi.CheckpointContainerResponse, error)
```


**Тип запроса:** runtimeapi.CheckpointContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.CheckpointContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.CheckpointContainerResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:462`



---


[function] name: ContainerStats file: test/e2e_node/criproxy/proxy_runtime_service.go:348 returns_error: да description: ContainerStats returns stats of the container. If the container does not
exist, the call returns an error.


### ContainerStats (test/e2e_node/criproxy/proxy_runtime_service.go:348)


ContainerStats returns stats of the container. If the container does not
exist, the call returns an error.


```go
func (p *RemoteRuntime) ContainerStats((*runtimeapi.ContainerStatsResponse, error)) (*runtimeapi.ContainerStatsResponse, error)
```


**Тип запроса:** runtimeapi.ContainerStatsResponse


```json
{
  "state": {},
  "Stats": null,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ContainerStatsResponse


```json
{
  "state": {},
  "Stats": null,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ContainerStatsResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:348`



---


[function] name: ContainerStatus file: test/e2e_node/criproxy/proxy_runtime_service.go:284 returns_error: да description: ContainerStatus returns status of the container. If the container is not
present, returns an error.


### ContainerStatus (test/e2e_node/criproxy/proxy_runtime_service.go:284)


ContainerStatus returns status of the container. If the container is not
present, returns an error.


```go
func (p *RemoteRuntime) ContainerStatus((*runtimeapi.ContainerStatusResponse, error)) (*runtimeapi.ContainerStatusResponse, error)
```


**Тип запроса:** runtimeapi.ContainerStatusResponse


```json
{
  "state": {},
  "Status": null,
  "info": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ContainerStatusResponse


```json
{
  "state": {},
  "Status": null,
  "info": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ContainerStatusResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:284`



---


[function] name: CreateContainer file: test/e2e_node/criproxy/proxy_runtime_service.go:213 returns_error: да description: CreateContainer creates a new container in specified PodSandbox


### CreateContainer (test/e2e_node/criproxy/proxy_runtime_service.go:213)


CreateContainer creates a new container in specified PodSandbox


```go
func (p *RemoteRuntime) CreateContainer((*runtimeapi.CreateContainerResponse, error)) (*runtimeapi.CreateContainerResponse, error)
```


**Тип запроса:** runtimeapi.CreateContainerResponse


```json
{
  "state": {},
  "containerId": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.CreateContainerResponse


```json
{
  "state": {},
  "containerId": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.CreateContainerResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:213`



---


[function] name: Exec file: test/e2e_node/criproxy/proxy_runtime_service.go:320 returns_error: да description: Exec prepares a streaming endpoint to execute a command in the container.


### Exec (test/e2e_node/criproxy/proxy_runtime_service.go:320)


Exec prepares a streaming endpoint to execute a command in the container.


```go
func (p *RemoteRuntime) Exec((*runtimeapi.ExecResponse, error)) (*runtimeapi.ExecResponse, error)
```


**Тип запроса:** runtimeapi.ExecResponse


```json
{
  "state": {},
  "Url": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ExecResponse


```json
{
  "state": {},
  "Url": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ExecResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:320`



---


[function] name: ExecSync file: test/e2e_node/criproxy/proxy_runtime_service.go:297 returns_error: да description: ExecSync runs a command in a container synchronously.


### ExecSync (test/e2e_node/criproxy/proxy_runtime_service.go:297)


ExecSync runs a command in a container synchronously.


```go
func (p *RemoteRuntime) ExecSync((*runtimeapi.ExecSyncResponse, error)) (*runtimeapi.ExecSyncResponse, error)
```


**Тип запроса:** runtimeapi.ExecSyncResponse


```json
{
  "state": {},
  "Stdout": [],
  "Stderr": [],
  "exitCode": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ExecSyncResponse


```json
{
  "state": {},
  "Stdout": [],
  "Stderr": [],
  "exitCode": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ExecSyncResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:297`



---


[function] name: GetContainerEvents file: test/e2e_node/criproxy/proxy_runtime_service.go:474 returns_error: нет description: —


### GetContainerEvents (test/e2e_node/criproxy/proxy_runtime_service.go:474)


GetContainerEvents is a method that retrieves data based on the provided parameters and returns (req *runtimeapi.GetEventsRequest, ces runtimeapi.RuntimeService_GetContainerEventsServer).


```go
func (p *RemoteRuntime) GetContainerEvents((req *runtimeapi.GetEventsRequest, ces runtimeapi.RuntimeService_GetContainerEventsServer)) (req *runtimeapi.GetEventsRequest, ces runtimeapi.RuntimeService_GetContainerEventsServer)
```


**Тип запроса:** runtimeapi.GetEventsRequest


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


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


**Тип ответа:** runtimeapi.GetEventsRequest


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** ces


```json
{
  "Reuse": {},
  "UseStatusResources": false,
  "InPlacePodLevelResourcesVerticalScalingEnabled": false,
  "ExcludeOverhead": false,
  "ContainerFn": {},
  "NonMissingContainerRequests": {},
  "SkipPodLevelResources": false,
  "SkipContainerLevelResources": false
}
```


*Определено в:* `staging/src/k8s.io/component-helpers/resource/helpers.go`


**Тип ответа:** runtimeapi.RuntimeService_GetContainerEventsServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:474`



---


[function] name: ListContainerStats file: test/e2e_node/criproxy/proxy_runtime_service.go:361 returns_error: да description: ListContainerStats returns stats of all running containers.


### ListContainerStats (test/e2e_node/criproxy/proxy_runtime_service.go:361)


ListContainerStats returns stats of all running containers.


```go
func (p *RemoteRuntime) ListContainerStats((*runtimeapi.ListContainerStatsResponse, error)) (*runtimeapi.ListContainerStatsResponse, error)
```


**Тип запроса:** runtimeapi.ListContainerStatsResponse


```json
{
  "state": {},
  "Stats": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ListContainerStatsResponse


```json
{
  "state": {},
  "Stats": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ListContainerStatsResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:361`



---


[function] name: ListContainers file: test/e2e_node/criproxy/proxy_runtime_service.go:270 returns_error: да description: ListContainers lists all containers by filters.


### ListContainers (test/e2e_node/criproxy/proxy_runtime_service.go:270)


ListContainers lists all containers by filters.


```go
func (p *RemoteRuntime) ListContainers((*runtimeapi.ListContainersResponse, error)) (*runtimeapi.ListContainersResponse, error)
```


**Тип запроса:** runtimeapi.ListContainersResponse


```json
{
  "state": {},
  "Containers": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ListContainersResponse


```json
{
  "state": {},
  "Containers": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ListContainersResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:270`



---


[function] name: ListMetricDescriptors file: test/e2e_node/criproxy/proxy_runtime_service.go:499 returns_error: да description: ListMetricDescriptors gets the descriptors for the metrics that will be returned in ListPodSandboxMetrics.


### ListMetricDescriptors (test/e2e_node/criproxy/proxy_runtime_service.go:499)


ListMetricDescriptors gets the descriptors for the metrics that will be returned in ListPodSandboxMetrics.


```go
func (p *RemoteRuntime) ListMetricDescriptors((*runtimeapi.ListMetricDescriptorsResponse, error)) (*runtimeapi.ListMetricDescriptorsResponse, error)
```


**Тип запроса:** runtimeapi.ListMetricDescriptorsResponse


```json
{
  "state": {},
  "Descriptors": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ListMetricDescriptorsResponse


```json
{
  "state": {},
  "Descriptors": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ListMetricDescriptorsResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:499`



---


[function] name: ListPodSandbox file: test/e2e_node/criproxy/proxy_runtime_service.go:200 returns_error: да description: ListPodSandbox returns a list of PodSandboxes.


### ListPodSandbox (test/e2e_node/criproxy/proxy_runtime_service.go:200)


ListPodSandbox returns a list of PodSandboxes.


```go
func (p *RemoteRuntime) ListPodSandbox((*runtimeapi.ListPodSandboxResponse, error)) (*runtimeapi.ListPodSandboxResponse, error)
```


**Тип запроса:** runtimeapi.ListPodSandboxResponse


```json
{
  "state": {},
  "Items": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ListPodSandboxResponse


```json
{
  "state": {},
  "Items": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ListPodSandboxResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:200`



---


[function] name: ListPodSandboxMetrics file: test/e2e_node/criproxy/proxy_runtime_service.go:512 returns_error: да description: ListPodSandboxMetrics retrieves the metrics for all pod sandboxes.


### ListPodSandboxMetrics (test/e2e_node/criproxy/proxy_runtime_service.go:512)


ListPodSandboxMetrics retrieves the metrics for all pod sandboxes.


```go
func (p *RemoteRuntime) ListPodSandboxMetrics((*runtimeapi.ListPodSandboxMetricsResponse, error)) (*runtimeapi.ListPodSandboxMetricsResponse, error)
```


**Тип запроса:** runtimeapi.ListPodSandboxMetricsResponse


```json
{
  "state": {},
  "podMetrics": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ListPodSandboxMetricsResponse


```json
{
  "state": {},
  "podMetrics": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ListPodSandboxMetricsResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:512`



---


[function] name: ListPodSandboxStats file: test/e2e_node/criproxy/proxy_runtime_service.go:388 returns_error: да description: ListPodSandboxStats returns stats of all running pods.


### ListPodSandboxStats (test/e2e_node/criproxy/proxy_runtime_service.go:388)


ListPodSandboxStats returns stats of all running pods.


```go
func (p *RemoteRuntime) ListPodSandboxStats((*runtimeapi.ListPodSandboxStatsResponse, error)) (*runtimeapi.ListPodSandboxStatsResponse, error)
```


**Тип запроса:** runtimeapi.ListPodSandboxStatsResponse


```json
{
  "state": {},
  "Stats": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ListPodSandboxStatsResponse


```json
{
  "state": {},
  "Stats": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ListPodSandboxStatsResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:388`



---


[function] name: NewRemoteRuntimeProxy file: test/e2e_node/criproxy/proxy_runtime_service.go:99 returns_error: нет description: NewRemoteRuntimeProxy creates a new RemoteRuntime.


### NewRemoteRuntimeProxy (test/e2e_node/criproxy/proxy_runtime_service.go:99)


NewRemoteRuntimeProxy creates a new RemoteRuntime.


```go
func NewRemoteRuntimeProxy((runtimeService internalapi.RuntimeService, imageService internalapi.ImageManagerService)) (runtimeService internalapi.RuntimeService, imageService internalapi.ImageManagerService)
```


**Тип ответа:** runtimeService


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


**Тип ответа:** internalapi.RuntimeService


```json
{
  "Called": [],
  "Errors": {},
  "FakeStatus": null,
  "Containers": {},
  "Sandboxes": {},
  "FakeContainerStats": {},
  "FakePodSandboxStats": {},
  "FakePodSandboxMetrics": {},
  "FakeMetricDescriptors": {},
  "FakeContainerMetrics": {},
  "FakeLinuxConfiguration": null,
  "ErrorOnSandboxCreate": false
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/testing/fake_runtime_service.go`


**Тип ответа:** imageService


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


**Тип ответа:** internalapi.ImageManagerService


```json
{
  "service": {}
}
```


*Определено в:* `pkg/kubelet/kuberuntime/instrumented_services.go`


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:99`



---


[function] name: PodSandboxStats file: test/e2e_node/criproxy/proxy_runtime_service.go:375 returns_error: да description: PodSandboxStats returns stats of the pod. If the pod does not
exist, the call returns an error.


### PodSandboxStats (test/e2e_node/criproxy/proxy_runtime_service.go:375)


PodSandboxStats returns stats of the pod. If the pod does not
exist, the call returns an error.


```go
func (p *RemoteRuntime) PodSandboxStats((*runtimeapi.PodSandboxStatsResponse, error)) (*runtimeapi.PodSandboxStatsResponse, error)
```


**Тип запроса:** runtimeapi.PodSandboxStatsResponse


```json
{
  "state": {},
  "Stats": null,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.PodSandboxStatsResponse


```json
{
  "state": {},
  "Stats": null,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.PodSandboxStatsResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:375`



---


[function] name: PodSandboxStatus file: test/e2e_node/criproxy/proxy_runtime_service.go:187 returns_error: да description: PodSandboxStatus returns the status of the PodSandbox. If the PodSandbox is not
present, returns an error.


### PodSandboxStatus (test/e2e_node/criproxy/proxy_runtime_service.go:187)


PodSandboxStatus returns the status of the PodSandbox. If the PodSandbox is not
present, returns an error.


```go
func (p *RemoteRuntime) PodSandboxStatus((*runtimeapi.PodSandboxStatusResponse, error)) (*runtimeapi.PodSandboxStatusResponse, error)
```


**Тип запроса:** runtimeapi.PodSandboxStatusResponse


```json
{
  "state": {},
  "Status": null,
  "info": {},
  "containersStatuses": [],
  "Timestamp": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.PodSandboxStatusResponse


```json
{
  "state": {},
  "Status": null,
  "info": {},
  "containersStatuses": [],
  "Timestamp": 0,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.PodSandboxStatusResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:187`



---


[function] name: PortForward file: test/e2e_node/criproxy/proxy_runtime_service.go:338 returns_error: да description: PortForward prepares a streaming endpoint to forward ports from a PodSandbox.


### PortForward (test/e2e_node/criproxy/proxy_runtime_service.go:338)


PortForward prepares a streaming endpoint to forward ports from a PodSandbox.


```go
func (p *RemoteRuntime) PortForward((*runtimeapi.PortForwardResponse, error)) (*runtimeapi.PortForwardResponse, error)
```


**Тип запроса:** runtimeapi.PortForwardResponse


```json
{
  "state": {},
  "Url": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.PortForwardResponse


```json
{
  "state": {},
  "Url": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.PortForwardResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:338`



---


[function] name: RemoveContainer file: test/e2e_node/criproxy/proxy_runtime_service.go:257 returns_error: да description: RemoveContainer removes the container. If the container is running, the
container must be forcibly removed.
This call is


### RemoveContainer (test/e2e_node/criproxy/proxy_runtime_service.go:257)


RemoveContainer removes the container. If the container is running, the
container must be forcibly removed.
This call is idempotent, and must not return an error if the container has
already been removed.


```go
func (p *RemoteRuntime) RemoveContainer((*runtimeapi.RemoveContainerResponse, error)) (*runtimeapi.RemoveContainerResponse, error)
```


**Тип запроса:** runtimeapi.RemoveContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.RemoveContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.RemoveContainerResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:257`



---


[function] name: RemovePodSandbox file: test/e2e_node/criproxy/proxy_runtime_service.go:173 returns_error: да description: RemovePodSandbox removes the sandbox. If there are any running containers
in the sandbox, they must be forcibly terminat


### RemovePodSandbox (test/e2e_node/criproxy/proxy_runtime_service.go:173)


RemovePodSandbox removes the sandbox. If there are any running containers
in the sandbox, they must be forcibly terminated and removed.
This call is idempotent, and must not return an error if the sandbox has
already been removed.


```go
func (p *RemoteRuntime) RemovePodSandbox((*runtimeapi.RemovePodSandboxResponse, error)) (*runtimeapi.RemovePodSandboxResponse, error)
```


**Тип запроса:** runtimeapi.RemovePodSandboxResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.RemovePodSandboxResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.RemovePodSandboxResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:173`



---


[function] name: ReopenContainerLog file: test/e2e_node/criproxy/proxy_runtime_service.go:449 returns_error: да description: ReopenContainerLog reopens the container log file.


### ReopenContainerLog (test/e2e_node/criproxy/proxy_runtime_service.go:449)


ReopenContainerLog reopens the container log file.


```go
func (p *RemoteRuntime) ReopenContainerLog((*runtimeapi.ReopenContainerLogResponse, error)) (*runtimeapi.ReopenContainerLogResponse, error)
```


**Тип запроса:** runtimeapi.ReopenContainerLogResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.ReopenContainerLogResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.ReopenContainerLogResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:449`



---


[function] name: ResetInjectors file: test/e2e_node/criproxy/proxy_runtime_service.go:75 returns_error: нет description: ResetInjectors resets all registered injectors.


### ResetInjectors (test/e2e_node/criproxy/proxy_runtime_service.go:75)


ResetInjectors resets all registered injectors.


```go
func (p *RemoteRuntime) ResetInjectors(()) ()
```


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:75`



---


[function] name: RunPodSandbox file: test/e2e_node/criproxy/proxy_runtime_service.go:141 returns_error: да description: RunPodSandbox creates and starts a pod-level sandbox. Runtimes must ensure
the sandbox is in the ready state on success.


### RunPodSandbox (test/e2e_node/criproxy/proxy_runtime_service.go:141)


RunPodSandbox creates and starts a pod-level sandbox. Runtimes must ensure
the sandbox is in the ready state on success.


```go
func (p *RemoteRuntime) RunPodSandbox((*runtimeapi.RunPodSandboxResponse, error)) (*runtimeapi.RunPodSandboxResponse, error)
```


**Тип запроса:** runtimeapi.RunPodSandboxResponse


```json
{
  "state": {},
  "podSandboxId": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.RunPodSandboxResponse


```json
{
  "state": {},
  "podSandboxId": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.RunPodSandboxResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:141`



---


[function] name: RuntimeConfig file: test/e2e_node/criproxy/proxy_runtime_service.go:525 returns_error: да description: RuntimeConfig returns the configuration information of the runtime.


### RuntimeConfig (test/e2e_node/criproxy/proxy_runtime_service.go:525)


RuntimeConfig returns the configuration information of the runtime.


```go
func (p *RemoteRuntime) RuntimeConfig((*runtimeapi.RuntimeConfigResponse, error)) (*runtimeapi.RuntimeConfigResponse, error)
```


**Тип запроса:** runtimeapi.RuntimeConfigResponse


```json
{
  "state": {},
  "Linux": null,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.RuntimeConfigResponse


```json
{
  "state": {},
  "Linux": null,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.RuntimeConfigResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:525`



---


[function] name: Start file: test/e2e_node/criproxy/proxy_runtime_service.go:112 returns_error: нет description: Start starts the remote runtime proxy.


### Start (test/e2e_node/criproxy/proxy_runtime_service.go:112)


Start starts the remote runtime proxy.


```go
func (p *RemoteRuntime) Start((endpoint string)) (endpoint string)
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


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:112`



---


[function] name: StartContainer file: test/e2e_node/criproxy/proxy_runtime_service.go:226 returns_error: да description: StartContainer starts the container.


### StartContainer (test/e2e_node/criproxy/proxy_runtime_service.go:226)


StartContainer starts the container.


```go
func (p *RemoteRuntime) StartContainer((*runtimeapi.StartContainerResponse, error)) (*runtimeapi.StartContainerResponse, error)
```


**Тип запроса:** runtimeapi.StartContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.StartContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.StartContainerResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:226`



---


[function] name: Status file: test/e2e_node/criproxy/proxy_runtime_service.go:423 returns_error: да description: Status returns the status of the runtime.


### Status (test/e2e_node/criproxy/proxy_runtime_service.go:423)


Status returns the status of the runtime.


```go
func (p *RemoteRuntime) Status((*runtimeapi.StatusResponse, error)) (*runtimeapi.StatusResponse, error)
```


**Тип запроса:** runtimeapi.StatusResponse


```json
{
  "state": {},
  "Status": null,
  "info": {},
  "runtimeHandlers": [],
  "Features": null,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.StatusResponse


```json
{
  "state": {},
  "Status": null,
  "info": {},
  "runtimeHandlers": [],
  "Features": null,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.StatusResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:423`



---


[function] name: Stop file: test/e2e_node/criproxy/proxy_runtime_service.go:127 returns_error: нет description: Stop stops the fake remote runtime proxy.


### Stop (test/e2e_node/criproxy/proxy_runtime_service.go:127)


Stop stops the fake remote runtime proxy.


```go
func (p *RemoteRuntime) Stop(()) ()
```


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:127`



---


[function] name: StopContainer file: test/e2e_node/criproxy/proxy_runtime_service.go:241 returns_error: да description: StopContainer stops a running container with a grace period (i.e., timeout).
This call is idempotent, and must not retur


### StopContainer (test/e2e_node/criproxy/proxy_runtime_service.go:241)


StopContainer stops a running container with a grace period (i.e., timeout).
This call is idempotent, and must not return an error if the container has
already been stopped.


```go
func (p *RemoteRuntime) StopContainer((*runtimeapi.StopContainerResponse, error)) (*runtimeapi.StopContainerResponse, error)
```


**Тип запроса:** runtimeapi.StopContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.StopContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.StopContainerResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:241`



---


[function] name: StopPodSandbox file: test/e2e_node/criproxy/proxy_runtime_service.go:157 returns_error: да description: StopPodSandbox stops any running process that is part of the sandbox and
reclaims network resources (e.g., IP addresses)


### StopPodSandbox (test/e2e_node/criproxy/proxy_runtime_service.go:157)


StopPodSandbox stops any running process that is part of the sandbox and
reclaims network resources (e.g., IP addresses) allocated to the sandbox.
If there are any running containers in the sandbox, they must be forcibly
terminated.


```go
func (p *RemoteRuntime) StopPodSandbox((*runtimeapi.StopPodSandboxResponse, error)) (*runtimeapi.StopPodSandboxResponse, error)
```


**Тип запроса:** runtimeapi.StopPodSandboxResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.StopPodSandboxResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.StopPodSandboxResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:157`



---


[function] name: UpdateContainerResources file: test/e2e_node/criproxy/proxy_runtime_service.go:436 returns_error: да description: UpdateContainerResources updates ContainerConfig of the container.


### UpdateContainerResources (test/e2e_node/criproxy/proxy_runtime_service.go:436)


UpdateContainerResources updates ContainerConfig of the container.


```go
func (p *RemoteRuntime) UpdateContainerResources((*runtimeapi.UpdateContainerResourcesResponse, error)) (*runtimeapi.UpdateContainerResourcesResponse, error)
```


**Тип запроса:** runtimeapi.UpdateContainerResourcesResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.UpdateContainerResourcesResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.UpdateContainerResourcesResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:436`



---


[function] name: UpdatePodSandboxResources file: test/e2e_node/criproxy/proxy_runtime_service.go:414 returns_error: да description: UpdatePodSandboxResources synchronously updates the PodSandboxConfig.


### UpdatePodSandboxResources (test/e2e_node/criproxy/proxy_runtime_service.go:414)


UpdatePodSandboxResources synchronously updates the PodSandboxConfig.


```go
func (p *RemoteRuntime) UpdatePodSandboxResources((*runtimeapi.UpdatePodSandboxResourcesResponse, error)) (*runtimeapi.UpdatePodSandboxResourcesResponse, error)
```


**Тип запроса:** runtimeapi.UpdatePodSandboxResourcesResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.UpdatePodSandboxResourcesResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.UpdatePodSandboxResourcesResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:414`



---


[function] name: UpdateRuntimeConfig file: test/e2e_node/criproxy/proxy_runtime_service.go:401 returns_error: да description: UpdateRuntimeConfig updates the runtime configuration based on the given request.


### UpdateRuntimeConfig (test/e2e_node/criproxy/proxy_runtime_service.go:401)


UpdateRuntimeConfig updates the runtime configuration based on the given request.


```go
func (p *RemoteRuntime) UpdateRuntimeConfig((*runtimeapi.UpdateRuntimeConfigResponse, error)) (*runtimeapi.UpdateRuntimeConfigResponse, error)
```


**Тип запроса:** runtimeapi.UpdateRuntimeConfigResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.UpdateRuntimeConfigResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.UpdateRuntimeConfigResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:401`



---


[function] name: Version file: test/e2e_node/criproxy/proxy_runtime_service.go:132 returns_error: да description: Version returns the runtime name, runtime version, and runtime API version.


### Version (test/e2e_node/criproxy/proxy_runtime_service.go:132)


Version returns the runtime name, runtime version, and runtime API version.


```go
func (p *RemoteRuntime) Version((*runtimeapi.VersionResponse, error)) (*runtimeapi.VersionResponse, error)
```


**Тип запроса:** runtimeapi.VersionResponse


```json
{
  "state": {},
  "Version": "string",
  "runtimeName": "string",
  "runtimeVersion": "string",
  "runtimeApiVersion": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Тип ответа:** runtimeapi.VersionResponse


```json
{
  "state": {},
  "Version": "string",
  "runtimeName": "string",
  "runtimeVersion": "string",
  "runtimeApiVersion": "string",
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*runtimeapi.VersionResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:132`



---


[function] name: runInjectors file: test/e2e_node/criproxy/proxy_runtime_service.go:79 returns_error: нет description: —


### runInjectors (test/e2e_node/criproxy/proxy_runtime_service.go:79)


runInjectors is a method that performs operations based on the provided parameters and returns (apiName string).


```go
func (p *RemoteRuntime) runInjectors((apiName string)) (apiName string)
```


**Тип ответа:** apiName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/criproxy/proxy_runtime_service.go:79`




## test/e2e_node/environment/conformance.go


📄 Исходный файл: `test/e2e_node/environment/conformance.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [appendNotNil](#appendnotnil-teste2e_nodeenvironmentconformancego221) `:221`

- 🔗 [check](#check-teste2e_nodeenvironmentconformancego60) `:60`

- 🔗 [daemons](#daemons-teste2e_nodeenvironmentconformancego194) `:194`

- 🔗 [dns](#dns-teste2e_nodeenvironmentconformancego89) `:89`

- 🔗 [firewall](#firewall-teste2e_nodeenvironmentconformancego162) `:162`

- 🔗 [init](#init-teste2e_nodeenvironmentconformancego41) `:41`

- 🔗 [kernel](#kernel-teste2e_nodeenvironmentconformancego147) `:147`

- 🔗 [main](#main-teste2e_nodeenvironmentconformancego48) `:48`

- 🔗 [printError](#printerror-teste2e_nodeenvironmentconformancego208) `:208`

- 🔗 [printSuccess](#printsuccess-teste2e_nodeenvironmentconformancego215) `:215`


</details>


[function] name: appendNotNil file: test/e2e_node/environment/conformance.go:221 returns_error: да description: appendNotNil appends err to errs iff err is not nil


### appendNotNil (test/e2e_node/environment/conformance.go:221)


appendNotNil appends err to errs iff err is not nil


```go
func appendNotNil((errs []error, err error)) (errs []error, err error)
```


**Тип ответа:** errs


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


*Типы возврата:* `errs []error`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/environment/conformance.go:221`



---


[function] name: check file: test/e2e_node/environment/conformance.go:60 returns_error: нет description: check returns errors found while checking the provided components.  Will prevent errors to stdout.


### check (test/e2e_node/environment/conformance.go:60)


check returns errors found while checking the provided components.  Will prevent errors to stdout.


```go
func check((options ...string)) (options ...string)
```


**Тип ответа:** options


```json
{
  "SinceTime": "2023-01-01T00:00:00Z",
  "UntilTime": "2023-01-01T00:00:00Z",
  "TailLines": 0,
  "Boot": 0,
  "Pattern": "string"
}
```


*Определено в:* `pkg/kubelet/kubelet_server_journal.go`


📍 *Расположение:* `test/e2e_node/environment/conformance.go:60`



---


[function] name: daemons file: test/e2e_node/environment/conformance.go:194 returns_error: нет description: daemons checks that the required node programs are running: kubelet and kube-proxy


### daemons (test/e2e_node/environment/conformance.go:194)


daemons checks that the required node programs are running: kubelet and kube-proxy


```go
func daemons(()) ()
```


📍 *Расположение:* `test/e2e_node/environment/conformance.go:194`



---


[function] name: dns file: test/e2e_node/environment/conformance.go:89 returns_error: нет description: dns checks that cluster dns has been properly configured and can resolve the kubernetes.default service


### dns (test/e2e_node/environment/conformance.go:89)


dns checks that cluster dns has been properly configured and can resolve the kubernetes.default service


```go
func dns(()) ()
```


📍 *Расположение:* `test/e2e_node/environment/conformance.go:89`



---


[function] name: firewall file: test/e2e_node/environment/conformance.go:162 returns_error: нет description: firewall checks that iptables does not have common firewall rules setup that would disrupt traffic


### firewall (test/e2e_node/environment/conformance.go:162)


firewall checks that iptables does not have common firewall rules setup that would disrupt traffic


```go
func firewall(()) ()
```


📍 *Расположение:* `test/e2e_node/environment/conformance.go:162`



---


[function] name: init file: test/e2e_node/environment/conformance.go:41 returns_error: нет description: —


### init (test/e2e_node/environment/conformance.go:41)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/environment/conformance.go:41`



---


[function] name: kernel file: test/e2e_node/environment/conformance.go:147 returns_error: нет description: kernel checks that the kernel has been configured correctly to support the required cgroup features


### kernel (test/e2e_node/environment/conformance.go:147)


kernel checks that the kernel has been configured correctly to support the required cgroup features


```go
func kernel(()) ()
```


📍 *Расположение:* `test/e2e_node/environment/conformance.go:147`



---


[function] name: main file: test/e2e_node/environment/conformance.go:48 returns_error: нет description: TODO: Should we write an e2e test for this?


### main (test/e2e_node/environment/conformance.go:48)


TODO: Should we write an e2e test for this?


```go
func main(()) ()
```


📍 *Расположение:* `test/e2e_node/environment/conformance.go:48`



---


[function] name: printError file: test/e2e_node/environment/conformance.go:208 returns_error: нет description: printError provides its arguments to print a format string to the console (newline terminated) and returns an
error with


### printError (test/e2e_node/environment/conformance.go:208)


printError provides its arguments to print a format string to the console (newline terminated) and returns an
error with the same string


```go
func printError((s string, args ...interface{})) (s string, args ...interface{})
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/e2e_node/environment/conformance.go:208`



---


[function] name: printSuccess file: test/e2e_node/environment/conformance.go:215 returns_error: нет description: printSuccess provides its arguments to print a format string to the console (newline terminated) and returns nil


### printSuccess (test/e2e_node/environment/conformance.go:215)


printSuccess provides its arguments to print a format string to the console (newline terminated) and returns nil


```go
func printSuccess((s string, args ...interface{})) (s string, args ...interface{})
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `test/e2e_node/environment/conformance.go:215`




## test/e2e_node/image_list.go


📄 Исходный файл: `test/e2e_node/image_list.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [Name](#name-teste2e_nodeimage_listgo117) `:117`

- 🔗 [PrePullAllImages](#prepullallimages-teste2e_nodeimage_listgo145) `:145`

- 🔗 [Pull](#pull-teste2e_nodeimage_listgo121) `:121`

- 🔗 [Remove](#remove-teste2e_nodeimage_listgo130) `:130`

- 🔗 [RemoveImage](#removeimage-teste2e_nodeimage_listgo213) `:213`

- 🔗 [getContainerImageFromE2ETestDaemonset](#getcontainerimagefrome2etestdaemonset-teste2e_nodeimage_listgo221) `:221`

- 🔗 [getNodeProblemDetectorImage](#getnodeproblemdetectorimage-teste2e_nodeimage_listgo94) `:94`

- 🔗 [getPuller](#getpuller-teste2e_nodeimage_listgo134) `:134`

- 🔗 [getSRIOVDevicePluginImage](#getsriovdevicepluginimage-teste2e_nodeimage_listgo239) `:239`

- 🔗 [updateImageAllowList](#updateimageallowlist-teste2e_nodeimage_listgo72) `:72`


</details>


[function] name: Name file: test/e2e_node/image_list.go:117 returns_error: нет description: —


### Name (test/e2e_node/image_list.go:117)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (rp *remotePuller) Name(()) ()
```


📍 *Расположение:* `test/e2e_node/image_list.go:117`



---


[function] name: PrePullAllImages file: test/e2e_node/image_list.go:145 returns_error: нет description: PrePullAllImages pre-fetches all images tests depend on so that we don't fail in an actual test.


### PrePullAllImages (test/e2e_node/image_list.go:145)


PrePullAllImages pre-fetches all images tests depend on so that we don't fail in an actual test.


```go
func PrePullAllImages((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/e2e_node/image_list.go:145`



---


[function] name: Pull file: test/e2e_node/image_list.go:121 returns_error: да description: —


### Pull (test/e2e_node/image_list.go:121)


Pull is a method that performs operations based on the provided parameters and may return an error.


```go
func (rp *remotePuller) Pull(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/image_list.go:121`



---


[function] name: Remove file: test/e2e_node/image_list.go:130 returns_error: нет description: —


### Remove (test/e2e_node/image_list.go:130)


Remove is a method that deletes data based on the provided parameters and returns (ctx context.Context, image string).


```go
func (rp *remotePuller) Remove((ctx context.Context, image string)) (ctx context.Context, image string)
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


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `test/e2e_node/image_list.go:130`



---


[function] name: RemoveImage file: test/e2e_node/image_list.go:213 returns_error: нет description: —


### RemoveImage (test/e2e_node/image_list.go:213)


RemoveImage is a function that deletes data based on the provided parameters and returns (ctx context.Context, image string).


```go
func RemoveImage((ctx context.Context, image string)) (ctx context.Context, image string)
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


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


📍 *Расположение:* `test/e2e_node/image_list.go:213`



---


[function] name: getContainerImageFromE2ETestDaemonset file: test/e2e_node/image_list.go:221 returns_error: да description: —


### getContainerImageFromE2ETestDaemonset (test/e2e_node/image_list.go:221)


getContainerImageFromE2ETestDaemonset is a function that performs operations based on the provided parameters and may return an error.


```go
func getContainerImageFromE2ETestDaemonset((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/image_list.go:221`



---


[function] name: getNodeProblemDetectorImage file: test/e2e_node/image_list.go:94 returns_error: нет description: —


### getNodeProblemDetectorImage (test/e2e_node/image_list.go:94)


getNodeProblemDetectorImage is a function that performs operations based on the provided parameters and returns ().


```go
func getNodeProblemDetectorImage(()) ()
```


📍 *Расположение:* `test/e2e_node/image_list.go:94`



---


[function] name: getPuller file: test/e2e_node/image_list.go:134 returns_error: да description: —


### getPuller (test/e2e_node/image_list.go:134)


getPuller is a function that performs operations based on the provided parameters and may return an error.


```go
func getPuller((puller, error)) (puller, error)
```


**Тип ответа:** puller


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `puller`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/image_list.go:134`



---


[function] name: getSRIOVDevicePluginImage file: test/e2e_node/image_list.go:239 returns_error: да description: getSRIOVDevicePluginImage returns the image of SRIOV device plugin.


### getSRIOVDevicePluginImage (test/e2e_node/image_list.go:239)


getSRIOVDevicePluginImage returns the image of SRIOV device plugin.


```go
func getSRIOVDevicePluginImage((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/image_list.go:239`



---


[function] name: updateImageAllowList file: test/e2e_node/image_list.go:72 returns_error: нет description: updateImageAllowList updates the e2epod.ImagePrePullList with
1. the hard coded lists
2. the ones passed in from framewo


### updateImageAllowList (test/e2e_node/image_list.go:72)


updateImageAllowList updates the e2epod.ImagePrePullList with
1. the hard coded lists
2. the ones passed in from framework.TestContext.ExtraEnvs
So this function needs to be called after the extra envs are applied.


```go
func updateImageAllowList((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/e2e_node/image_list.go:72`




## test/e2e_node/kubeletconfig/kubeletconfig.go


📄 Исходный файл: `test/e2e_node/kubeletconfig/kubeletconfig.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [GetCurrentKubeletConfig](#getcurrentkubeletconfig-teste2e_nodekubeletconfigkubeletconfiggo110) `:110`

- 🔗 [GetCurrentKubeletConfigFromFile](#getcurrentkubeletconfigfromfile-teste2e_nodekubeletconfigkubeletconfiggo58) `:58`

- 🔗 [WriteKubeletConfigFile](#writekubeletconfigfile-teste2e_nodekubeletconfigkubeletconfiggo91) `:91`

- 🔗 [decodeConfigz](#decodeconfigz-teste2e_nodekubeletconfigkubeletconfiggo192) `:192`

- 🔗 [getKubeletConfigFilePath](#getkubeletconfigfilepath-teste2e_nodekubeletconfigkubeletconfiggo45) `:45`

- 🔗 [pollConfigz](#pollconfigz-teste2e_nodekubeletconfigkubeletconfiggo123) `:123`


</details>


[function] name: GetCurrentKubeletConfig file: test/e2e_node/kubeletconfig/kubeletconfig.go:110 returns_error: да description: GetCurrentKubeletConfig fetches the current Kubelet Config for the given node


### GetCurrentKubeletConfig (test/e2e_node/kubeletconfig/kubeletconfig.go:110)


GetCurrentKubeletConfig fetches the current Kubelet Config for the given node


```go
func GetCurrentKubeletConfig((*kubeletconfig.KubeletConfiguration, error)) (*kubeletconfig.KubeletConfiguration, error)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfig.KubeletConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/kubeletconfig/kubeletconfig.go:110`



---


[function] name: GetCurrentKubeletConfigFromFile file: test/e2e_node/kubeletconfig/kubeletconfig.go:58 returns_error: да description: GetCurrentKubeletConfigFromFile returns the current kubelet configuration under the filesystem.
This method should only 


### GetCurrentKubeletConfigFromFile (test/e2e_node/kubeletconfig/kubeletconfig.go:58)


GetCurrentKubeletConfigFromFile returns the current kubelet configuration under the filesystem.
This method should only run together with e2e node tests, meaning the test executor and the cluster nodes is the
same machine


```go
func GetCurrentKubeletConfigFromFile((*kubeletconfig.KubeletConfiguration, error)) (*kubeletconfig.KubeletConfiguration, error)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfig.KubeletConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/kubeletconfig/kubeletconfig.go:58`



---


[function] name: WriteKubeletConfigFile file: test/e2e_node/kubeletconfig/kubeletconfig.go:91 returns_error: нет description: WriteKubeletConfigFile updates the kubelet configuration under the filesystem
This method should only run together with 


### WriteKubeletConfigFile (test/e2e_node/kubeletconfig/kubeletconfig.go:91)


WriteKubeletConfigFile updates the kubelet configuration under the filesystem
This method should only run together with e2e node tests, meaning the test executor and the cluster nodes is the
same machine


```go
func WriteKubeletConfigFile((kubeletConfig *kubeletconfig.KubeletConfiguration)) (kubeletConfig *kubeletconfig.KubeletConfiguration)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletConfig


```json
{
  "config": {}
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/kubelet.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


📍 *Расположение:* `test/e2e_node/kubeletconfig/kubeletconfig.go:91`



---


[function] name: decodeConfigz file: test/e2e_node/kubeletconfig/kubeletconfig.go:192 returns_error: да description: Decodes the http response from /configz and returns a kubeletconfig.KubeletConfiguration (internal type).


### decodeConfigz (test/e2e_node/kubeletconfig/kubeletconfig.go:192)


Decodes the http response from /configz and returns a kubeletconfig.KubeletConfiguration (internal type).


```go
func decodeConfigz((*kubeletconfig.KubeletConfiguration, error)) (*kubeletconfig.KubeletConfiguration, error)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfig.KubeletConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/kubeletconfig/kubeletconfig.go:192`



---


[function] name: getKubeletConfigFilePath file: test/e2e_node/kubeletconfig/kubeletconfig.go:45 returns_error: да description: —


### getKubeletConfigFilePath (test/e2e_node/kubeletconfig/kubeletconfig.go:45)


getKubeletConfigFilePath is a function that performs operations based on the provided parameters and may return an error.


```go
func getKubeletConfigFilePath((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/kubeletconfig/kubeletconfig.go:45`



---


[function] name: pollConfigz file: test/e2e_node/kubeletconfig/kubeletconfig.go:123 returns_error: нет description: returns a status 200 response from the /configz endpoint or nil if fails


### pollConfigz (test/e2e_node/kubeletconfig/kubeletconfig.go:123)


returns a status 200 response from the /configz endpoint or nil if fails


```go
func pollConfigz((ctx context.Context, timeout time.Duration, pollInterval time.Duration, nodeName, namespace string, useProxy bool, standaloneMode bool)) (ctx context.Context, timeout time.Duration, pollInterval time.Duration, nodeName, namespace string, useProxy bool, standaloneMode bool)
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


**Тип ответа:** pollInterval


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


**Тип ответа:** nodeName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** useProxy


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** standaloneMode


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/kubeletconfig/kubeletconfig.go:123`




## test/e2e_node/node_problem_detector_linux.go


📄 Исходный файл: `test/e2e_node/node_problem_detector_linux.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [injectLog](#injectlog-teste2e_nodenode_problem_detector_linuxgo449) `:449`

- 🔗 [verifyEvents](#verifyevents-teste2e_nodenode_problem_detector_linuxgo465) `:465`

- 🔗 [verifyNodeCondition](#verifynodecondition-teste2e_nodenode_problem_detector_linuxgo500) `:500`

- 🔗 [verifyTotalEvents](#verifytotalevents-teste2e_nodenode_problem_detector_linuxgo484) `:484`


</details>


[function] name: injectLog file: test/e2e_node/node_problem_detector_linux.go:449 returns_error: нет description: injectLog injects kernel log into specified file.


### injectLog (test/e2e_node/node_problem_detector_linux.go:449)


injectLog injects kernel log into specified file.


```go
func injectLog((file string, timestamp time.Time, log string, num int)) (file string, timestamp time.Time, log string, num int)
```


**Тип ответа:** file


```json
{
  "path": "string",
  "period": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/token_source.go`


**Тип ответа:** timestamp


```json
{
  "lastUpdatedAt": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/request/object_count_tracker.go`


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


**Тип ответа:** log


```json
{
  "startOnce": {},
  "lastVerified": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/healthz/healthz.go`


**Тип ответа:** num


```json
{
  "validator": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/enum.go`


📍 *Расположение:* `test/e2e_node/node_problem_detector_linux.go:449`



---


[function] name: verifyEvents file: test/e2e_node/node_problem_detector_linux.go:465 returns_error: нет description: verifyEvents verifies there are num specific events generated with given reason and message.


### verifyEvents (test/e2e_node/node_problem_detector_linux.go:465)


verifyEvents verifies there are num specific events generated with given reason and message.


```go
func verifyEvents((ctx context.Context, e coreclientset.EventInterface, options metav1.ListOptions, num int, reason, message string)) (ctx context.Context, e coreclientset.EventInterface, options metav1.ListOptions, num int, reason, message string)
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


**Тип ответа:** coreclientset.EventInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options


```json
{
  "SinceTime": "2023-01-01T00:00:00Z",
  "UntilTime": "2023-01-01T00:00:00Z",
  "TailLines": 0,
  "Boot": 0,
  "Pattern": "string"
}
```


*Определено в:* `pkg/kubelet/kubelet_server_journal.go`


**Тип ответа:** metav1.ListOptions


```json
{
  "LabelSelector": {},
  "FieldSelector": {},
  "Watch": false,
  "AllowWatchBookmarks": false,
  "ResourceVersion": "string",
  "ResourceVersionMatch": {},
  "TimeoutSeconds": 0,
  "Limit": 0,
  "Continue": "string",
  "SendInitialEvents": false
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/internalversion/types.go`


**Тип ответа:** num


```json
{
  "validator": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/enum.go`


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/node_problem_detector_linux.go:465`



---


[function] name: verifyNodeCondition file: test/e2e_node/node_problem_detector_linux.go:500 returns_error: нет description: verifyNodeCondition verifies specific node condition is generated, if reason and message are empty, they will not be che


### verifyNodeCondition (test/e2e_node/node_problem_detector_linux.go:500)


verifyNodeCondition verifies specific node condition is generated, if reason and message are empty, they will not be checked


```go
func verifyNodeCondition((ctx context.Context, n coreclientset.NodeInterface, condition v1.NodeConditionType, status v1.ConditionStatus, reason, message string)) (ctx context.Context, n coreclientset.NodeInterface, condition v1.NodeConditionType, status v1.ConditionStatus, reason, message string)
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


**Тип ответа:** coreclientset.NodeInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** condition


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition.go`


**Тип ответа:** v1.NodeConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** v1.ConditionStatus


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** message


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/node_problem_detector_linux.go:500`



---


[function] name: verifyTotalEvents file: test/e2e_node/node_problem_detector_linux.go:484 returns_error: нет description: verifyTotalEvents verifies there are num events in total.


### verifyTotalEvents (test/e2e_node/node_problem_detector_linux.go:484)


verifyTotalEvents verifies there are num events in total.


```go
func verifyTotalEvents((ctx context.Context, e coreclientset.EventInterface, options metav1.ListOptions, num int)) (ctx context.Context, e coreclientset.EventInterface, options metav1.ListOptions, num int)
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


**Тип ответа:** coreclientset.EventInterface


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** options


```json
{
  "SinceTime": "2023-01-01T00:00:00Z",
  "UntilTime": "2023-01-01T00:00:00Z",
  "TailLines": 0,
  "Boot": 0,
  "Pattern": "string"
}
```


*Определено в:* `pkg/kubelet/kubelet_server_journal.go`


**Тип ответа:** metav1.ListOptions


```json
{
  "LabelSelector": {},
  "FieldSelector": {},
  "Watch": false,
  "AllowWatchBookmarks": false,
  "ResourceVersion": "string",
  "ResourceVersionMatch": {},
  "TimeoutSeconds": 0,
  "Limit": 0,
  "Continue": "string",
  "SendInitialEvents": false
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/internalversion/types.go`


**Тип ответа:** num


```json
{
  "validator": {}
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/enum.go`


📍 *Расположение:* `test/e2e_node/node_problem_detector_linux.go:484`




## test/e2e_node/numa_alignment.go


📄 Исходный файл: `test/e2e_node/numa_alignment.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [CheckAlignment](#checkalignment-teste2e_nodenuma_alignmentgo39) `:39`

- 🔗 [String](#string-teste2e_nodenuma_alignmentgo56) `:56`

- 🔗 [checkNUMAAlignment](#checknumaalignment-teste2e_nodenuma_alignmentgo192) `:192`

- 🔗 [containerWantsDevices](#containerwantsdevices-teste2e_nodenuma_alignmentgo187) `:187`

- 🔗 [getCPUToNUMANodeMapFromEnv](#getcputonumanodemapfromenv-teste2e_nodenuma_alignmentgo92) `:92`

- 🔗 [getCPUsPerNUMANode](#getcpuspernumanode-teste2e_nodenuma_alignmentgo80) `:80`

- 🔗 [getPCIDeviceInfo](#getpcideviceinfo-teste2e_nodenuma_alignmentgo230) `:230`

- 🔗 [getPCIDeviceToNumaNodeMapFromEnv](#getpcidevicetonumanodemapfromenv-teste2e_nodenuma_alignmentgo141) `:141`

- 🔗 [makeEnvMap](#makeenvmap-teste2e_nodenuma_alignmentgo164) `:164`

- 🔗 [numaNodeFromSysFsEntry](#numanodefromsysfsentry-teste2e_nodenuma_alignmentgo270) `:270`


</details>


[function] name: CheckAlignment file: test/e2e_node/numa_alignment.go:39 returns_error: нет description: —


### CheckAlignment (test/e2e_node/numa_alignment.go:39)


CheckAlignment is a method that performs operations based on the provided parameters and returns ().


```go
func (R *numaPodResources) CheckAlignment(()) ()
```


📍 *Расположение:* `test/e2e_node/numa_alignment.go:39`



---


[function] name: String file: test/e2e_node/numa_alignment.go:56 returns_error: нет description: —


### String (test/e2e_node/numa_alignment.go:56)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (R *numaPodResources) String(()) ()
```


📍 *Расположение:* `test/e2e_node/numa_alignment.go:56`



---


[function] name: checkNUMAAlignment file: test/e2e_node/numa_alignment.go:192 returns_error: да description: —


### checkNUMAAlignment (test/e2e_node/numa_alignment.go:192)


checkNUMAAlignment is a function that performs operations based on the provided parameters and may return an error.


```go
func checkNUMAAlignment((*numaPodResources, error)) (*numaPodResources, error)
```


**Тип запроса:** numaPodResources


```json
{
  "CPUToNUMANode": {},
  "PCIDevsToNUMANode": {}
}
```


*Определено в:* `test/e2e_node/numa_alignment.go`


**Тип ответа:** numaPodResources


```json
{
  "CPUToNUMANode": {},
  "PCIDevsToNUMANode": {}
}
```


*Определено в:* `test/e2e_node/numa_alignment.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*numaPodResources`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/numa_alignment.go:192`



---


[function] name: containerWantsDevices file: test/e2e_node/numa_alignment.go:187 returns_error: нет description: —


### containerWantsDevices (test/e2e_node/numa_alignment.go:187)


containerWantsDevices is a function that performs operations based on the provided parameters and returns (cnt *v1.Container, envInfo *testEnvInfo).


```go
func containerWantsDevices((cnt *v1.Container, envInfo *testEnvInfo)) (cnt *v1.Container, envInfo *testEnvInfo)
```


**Тип запроса:** v1.Container


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


**Тип запроса:** testEnvInfo


```json
{
  "numaNodes": 0,
  "sriovResourceName": "string",
  "policy": "string",
  "scope": "string"
}
```


*Определено в:* `test/e2e_node/numa_alignment.go`


**Тип ответа:** cnt


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** v1.Container


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


**Тип ответа:** envInfo


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** testEnvInfo


```json
{
  "numaNodes": 0,
  "sriovResourceName": "string",
  "policy": "string",
  "scope": "string"
}
```


*Определено в:* `test/e2e_node/numa_alignment.go`


📍 *Расположение:* `test/e2e_node/numa_alignment.go:187`



---


[function] name: getCPUToNUMANodeMapFromEnv file: test/e2e_node/numa_alignment.go:92 returns_error: да description: —


### getCPUToNUMANodeMapFromEnv (test/e2e_node/numa_alignment.go:92)


getCPUToNUMANodeMapFromEnv is a function that performs operations based on the provided parameters and may return an error.


```go
func getCPUToNUMANodeMapFromEnv((map[int]int, error)) (map[int]int, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[int]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/numa_alignment.go:92`



---


[function] name: getCPUsPerNUMANode file: test/e2e_node/numa_alignment.go:80 returns_error: да description: —


### getCPUsPerNUMANode (test/e2e_node/numa_alignment.go:80)


getCPUsPerNUMANode is a function that performs operations based on the provided parameters and may return an error.


```go
func getCPUsPerNUMANode(([]int, error)) ([]int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/numa_alignment.go:80`



---


[function] name: getPCIDeviceInfo file: test/e2e_node/numa_alignment.go:230 returns_error: да description: —


### getPCIDeviceInfo (test/e2e_node/numa_alignment.go:230)


getPCIDeviceInfo is a function that performs operations based on the provided parameters and may return an error.


```go
func getPCIDeviceInfo(([]pciDeviceInfo, error)) ([]pciDeviceInfo, error)
```


**Тип ответа:** pciDeviceInfo


```json
{
  "Address": "string",
  "NUMANode": 0,
  "IsPhysFn": false,
  "IsVFn": false
}
```


*Определено в:* `test/e2e_node/numa_alignment.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]pciDeviceInfo`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/numa_alignment.go:230`



---


[function] name: getPCIDeviceToNumaNodeMapFromEnv file: test/e2e_node/numa_alignment.go:141 returns_error: да description: —


### getPCIDeviceToNumaNodeMapFromEnv (test/e2e_node/numa_alignment.go:141)


getPCIDeviceToNumaNodeMapFromEnv is a function that performs operations based on the provided parameters and may return an error.


```go
func getPCIDeviceToNumaNodeMapFromEnv((map[string]int, error)) (map[string]int, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/numa_alignment.go:141`



---


[function] name: makeEnvMap file: test/e2e_node/numa_alignment.go:164 returns_error: да description: —


### makeEnvMap (test/e2e_node/numa_alignment.go:164)


makeEnvMap is a function that performs operations based on the provided parameters and may return an error.


```go
func makeEnvMap((map[string]string, error)) (map[string]string, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/numa_alignment.go:164`



---


[function] name: numaNodeFromSysFsEntry file: test/e2e_node/numa_alignment.go:270 returns_error: нет description: —


### numaNodeFromSysFsEntry (test/e2e_node/numa_alignment.go:270)


numaNodeFromSysFsEntry is a function that performs operations based on the provided parameters and returns (content string).


```go
func numaNodeFromSysFsEntry((content string)) (content string)
```


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/numa_alignment.go:270`




## test/e2e_node/perf/workloads/npb_ep.go


📄 Исходный файл: `test/e2e_node/perf/workloads/npb_ep.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [ExtractPerformanceFromLogs](#extractperformancefromlogs-teste2e_nodeperfworkloadsnpb_epgo111) `:111`

- 🔗 [KubeletConfig](#kubeletconfig-teste2e_nodeperfworkloadsnpb_epgo73) `:73`

- 🔗 [Name](#name-teste2e_nodeperfworkloadsnpb_epgo39) `:39`

- 🔗 [PodSpec](#podspec-teste2e_nodeperfworkloadsnpb_epgo43) `:43`

- 🔗 [PostTestExec](#posttestexec-teste2e_nodeperfworkloadsnpb_epgo103) `:103`

- 🔗 [PreTestExec](#pretestexec-teste2e_nodeperfworkloadsnpb_epgo95) `:95`

- 🔗 [Timeout](#timeout-teste2e_nodeperfworkloadsnpb_epgo69) `:69`


</details>


[function] name: ExtractPerformanceFromLogs file: test/e2e_node/perf/workloads/npb_ep.go:111 returns_error: да description: —


### ExtractPerformanceFromLogs (test/e2e_node/perf/workloads/npb_ep.go:111)


ExtractPerformanceFromLogs is a method that performs operations based on the provided parameters and may return an error.


```go
func (w npbEPWorkload) ExtractPerformanceFromLogs((perf time.Duration, err error)) (perf time.Duration, err error)
```


**Тип ответа:** perf


```json
{
  "mutex": null,
  "perObjectInterval": {},
  "operationMetrics": null
}
```


*Определено в:* `test/e2e/storage/testsuites/volumeperf.go`


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


*Типы возврата:* `perf time.Duration`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_ep.go:111`



---


[function] name: KubeletConfig file: test/e2e_node/perf/workloads/npb_ep.go:73 returns_error: да description: —


### KubeletConfig (test/e2e_node/perf/workloads/npb_ep.go:73)


KubeletConfig is a method that performs operations based on the provided parameters and may return an error.


```go
func (w npbEPWorkload) KubeletConfig((newCfg *kubeletconfig.KubeletConfiguration, err error)) (newCfg *kubeletconfig.KubeletConfiguration, err error)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** newCfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


*Типы возврата:* `newCfg *kubeletconfig.KubeletConfiguration`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_ep.go:73`



---


[function] name: Name file: test/e2e_node/perf/workloads/npb_ep.go:39 returns_error: нет description: —


### Name (test/e2e_node/perf/workloads/npb_ep.go:39)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbEPWorkload) Name(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_ep.go:39`



---


[function] name: PodSpec file: test/e2e_node/perf/workloads/npb_ep.go:43 returns_error: нет description: —


### PodSpec (test/e2e_node/perf/workloads/npb_ep.go:43)


PodSpec is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbEPWorkload) PodSpec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_ep.go:43`



---


[function] name: PostTestExec file: test/e2e_node/perf/workloads/npb_ep.go:103 returns_error: нет description: —


### PostTestExec (test/e2e_node/perf/workloads/npb_ep.go:103)


PostTestExec is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbEPWorkload) PostTestExec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_ep.go:103`



---


[function] name: PreTestExec file: test/e2e_node/perf/workloads/npb_ep.go:95 returns_error: нет description: —


### PreTestExec (test/e2e_node/perf/workloads/npb_ep.go:95)


PreTestExec is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbEPWorkload) PreTestExec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_ep.go:95`



---


[function] name: Timeout file: test/e2e_node/perf/workloads/npb_ep.go:69 returns_error: нет description: —


### Timeout (test/e2e_node/perf/workloads/npb_ep.go:69)


Timeout is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbEPWorkload) Timeout(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_ep.go:69`




## test/e2e_node/perf/workloads/npb_is.go


📄 Исходный файл: `test/e2e_node/perf/workloads/npb_is.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [ExtractPerformanceFromLogs](#extractperformancefromlogs-teste2e_nodeperfworkloadsnpb_isgo83) `:83`

- 🔗 [KubeletConfig](#kubeletconfig-teste2e_nodeperfworkloadsnpb_isgo71) `:71`

- 🔗 [Name](#name-teste2e_nodeperfworkloadsnpb_isgo37) `:37`

- 🔗 [PodSpec](#podspec-teste2e_nodeperfworkloadsnpb_isgo41) `:41`

- 🔗 [PostTestExec](#posttestexec-teste2e_nodeperfworkloadsnpb_isgo79) `:79`

- 🔗 [PreTestExec](#pretestexec-teste2e_nodeperfworkloadsnpb_isgo75) `:75`

- 🔗 [Timeout](#timeout-teste2e_nodeperfworkloadsnpb_isgo67) `:67`


</details>


[function] name: ExtractPerformanceFromLogs file: test/e2e_node/perf/workloads/npb_is.go:83 returns_error: да description: —


### ExtractPerformanceFromLogs (test/e2e_node/perf/workloads/npb_is.go:83)


ExtractPerformanceFromLogs is a method that performs operations based on the provided parameters and may return an error.


```go
func (w npbISWorkload) ExtractPerformanceFromLogs((perf time.Duration, err error)) (perf time.Duration, err error)
```


**Тип ответа:** perf


```json
{
  "mutex": null,
  "perObjectInterval": {},
  "operationMetrics": null
}
```


*Определено в:* `test/e2e/storage/testsuites/volumeperf.go`


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


*Типы возврата:* `perf time.Duration`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_is.go:83`



---


[function] name: KubeletConfig file: test/e2e_node/perf/workloads/npb_is.go:71 returns_error: да description: —


### KubeletConfig (test/e2e_node/perf/workloads/npb_is.go:71)


KubeletConfig is a method that performs operations based on the provided parameters and may return an error.


```go
func (w npbISWorkload) KubeletConfig((newCfg *kubeletconfig.KubeletConfiguration, err error)) (newCfg *kubeletconfig.KubeletConfiguration, err error)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** newCfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


*Типы возврата:* `newCfg *kubeletconfig.KubeletConfiguration`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_is.go:71`



---


[function] name: Name file: test/e2e_node/perf/workloads/npb_is.go:37 returns_error: нет description: —


### Name (test/e2e_node/perf/workloads/npb_is.go:37)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbISWorkload) Name(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_is.go:37`



---


[function] name: PodSpec file: test/e2e_node/perf/workloads/npb_is.go:41 returns_error: нет description: —


### PodSpec (test/e2e_node/perf/workloads/npb_is.go:41)


PodSpec is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbISWorkload) PodSpec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_is.go:41`



---


[function] name: PostTestExec file: test/e2e_node/perf/workloads/npb_is.go:79 returns_error: нет description: —


### PostTestExec (test/e2e_node/perf/workloads/npb_is.go:79)


PostTestExec is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbISWorkload) PostTestExec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_is.go:79`



---


[function] name: PreTestExec file: test/e2e_node/perf/workloads/npb_is.go:75 returns_error: нет description: —


### PreTestExec (test/e2e_node/perf/workloads/npb_is.go:75)


PreTestExec is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbISWorkload) PreTestExec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_is.go:75`



---


[function] name: Timeout file: test/e2e_node/perf/workloads/npb_is.go:67 returns_error: нет description: —


### Timeout (test/e2e_node/perf/workloads/npb_is.go:67)


Timeout is a method that performs operations based on the provided parameters and returns ().


```go
func (w npbISWorkload) Timeout(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/npb_is.go:67`




## test/e2e_node/perf/workloads/pytorch_wide_deep.go


📄 Исходный файл: `test/e2e_node/perf/workloads/pytorch_wide_deep.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [ExtractPerformanceFromLogs](#extractperformancefromlogs-teste2e_nodeperfworkloadspytorch_wide_deepgo110) `:110`

- 🔗 [KubeletConfig](#kubeletconfig-teste2e_nodeperfworkloadspytorch_wide_deepgo72) `:72`

- 🔗 [Name](#name-teste2e_nodeperfworkloadspytorch_wide_deepgo39) `:39`

- 🔗 [PodSpec](#podspec-teste2e_nodeperfworkloadspytorch_wide_deepgo43) `:43`

- 🔗 [PostTestExec](#posttestexec-teste2e_nodeperfworkloadspytorch_wide_deepgo102) `:102`

- 🔗 [PreTestExec](#pretestexec-teste2e_nodeperfworkloadspytorch_wide_deepgo94) `:94`

- 🔗 [Timeout](#timeout-teste2e_nodeperfworkloadspytorch_wide_deepgo68) `:68`


</details>


[function] name: ExtractPerformanceFromLogs file: test/e2e_node/perf/workloads/pytorch_wide_deep.go:110 returns_error: да description: —


### ExtractPerformanceFromLogs (test/e2e_node/perf/workloads/pytorch_wide_deep.go:110)


ExtractPerformanceFromLogs is a method that performs operations based on the provided parameters and may return an error.


```go
func (w pytorchWideDeepWorkload) ExtractPerformanceFromLogs((perf time.Duration, err error)) (perf time.Duration, err error)
```


**Тип ответа:** perf


```json
{
  "mutex": null,
  "perObjectInterval": {},
  "operationMetrics": null
}
```


*Определено в:* `test/e2e/storage/testsuites/volumeperf.go`


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


*Типы возврата:* `perf time.Duration`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/perf/workloads/pytorch_wide_deep.go:110`



---


[function] name: KubeletConfig file: test/e2e_node/perf/workloads/pytorch_wide_deep.go:72 returns_error: да description: —


### KubeletConfig (test/e2e_node/perf/workloads/pytorch_wide_deep.go:72)


KubeletConfig is a method that performs operations based on the provided parameters and may return an error.


```go
func (w pytorchWideDeepWorkload) KubeletConfig((newCfg *kubeletconfig.KubeletConfiguration, err error)) (newCfg *kubeletconfig.KubeletConfiguration, err error)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** newCfg


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


*Типы возврата:* `newCfg *kubeletconfig.KubeletConfiguration`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/perf/workloads/pytorch_wide_deep.go:72`



---


[function] name: Name file: test/e2e_node/perf/workloads/pytorch_wide_deep.go:39 returns_error: нет description: —


### Name (test/e2e_node/perf/workloads/pytorch_wide_deep.go:39)


Name is a method that performs operations based on the provided parameters and returns ().


```go
func (w pytorchWideDeepWorkload) Name(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/pytorch_wide_deep.go:39`



---


[function] name: PodSpec file: test/e2e_node/perf/workloads/pytorch_wide_deep.go:43 returns_error: нет description: —


### PodSpec (test/e2e_node/perf/workloads/pytorch_wide_deep.go:43)


PodSpec is a method that performs operations based on the provided parameters and returns ().


```go
func (w pytorchWideDeepWorkload) PodSpec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/pytorch_wide_deep.go:43`



---


[function] name: PostTestExec file: test/e2e_node/perf/workloads/pytorch_wide_deep.go:102 returns_error: нет description: —


### PostTestExec (test/e2e_node/perf/workloads/pytorch_wide_deep.go:102)


PostTestExec is a method that performs operations based on the provided parameters and returns ().


```go
func (w pytorchWideDeepWorkload) PostTestExec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/pytorch_wide_deep.go:102`



---


[function] name: PreTestExec file: test/e2e_node/perf/workloads/pytorch_wide_deep.go:94 returns_error: нет description: —


### PreTestExec (test/e2e_node/perf/workloads/pytorch_wide_deep.go:94)


PreTestExec is a method that performs operations based on the provided parameters and returns ().


```go
func (w pytorchWideDeepWorkload) PreTestExec(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/pytorch_wide_deep.go:94`



---


[function] name: Timeout file: test/e2e_node/perf/workloads/pytorch_wide_deep.go:68 returns_error: нет description: —


### Timeout (test/e2e_node/perf/workloads/pytorch_wide_deep.go:68)


Timeout is a method that performs operations based on the provided parameters and returns ().


```go
func (w pytorchWideDeepWorkload) Timeout(()) ()
```


📍 *Расположение:* `test/e2e_node/perf/workloads/pytorch_wide_deep.go:68`




## test/e2e_node/perf/workloads/utils.go


📄 Исходный файл: `test/e2e_node/perf/workloads/utils.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [getMatchingLineFromLog](#getmatchinglinefromlog-teste2e_nodeperfworkloadsutilsgo31) `:31`

- 🔗 [runCmd](#runcmd-teste2e_nodeperfworkloadsutilsgo26) `:26`


</details>


[function] name: getMatchingLineFromLog file: test/e2e_node/perf/workloads/utils.go:31 returns_error: да description: —


### getMatchingLineFromLog (test/e2e_node/perf/workloads/utils.go:31)


getMatchingLineFromLog is a function that performs operations based on the provided parameters and may return an error.


```go
func getMatchingLineFromLog((line string, err error)) (line string, err error)
```


**Тип ответа:** line


```json
{
  "wrap": 0,
  "words": []
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/explain/formatter.go`


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


*Типы возврата:* `line string`, `err error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/perf/workloads/utils.go:31`



---


[function] name: runCmd file: test/e2e_node/perf/workloads/utils.go:26 returns_error: нет description: —


### runCmd (test/e2e_node/perf/workloads/utils.go:26)


runCmd is a function that performs operations based on the provided parameters and returns (cmd string, args []string).


```go
func runCmd((cmd string, args []string)) (cmd string, args []string)
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


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/perf/workloads/utils.go:26`




## test/e2e_node/plugins/gcp-credential-provider/main.go


📄 Исходный файл: `test/e2e_node/plugins/gcp-credential-provider/main.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [getClaims](#getclaims-teste2e_nodepluginsgcp-credential-providermaingo133) `:133`

- 🔗 [getCredentials](#getcredentials-teste2e_nodepluginsgcp-credential-providermaingo50) `:50`

- 🔗 [main](#main-teste2e_nodepluginsgcp-credential-providermaingo44) `:44`


</details>


[function] name: getClaims file: test/e2e_node/plugins/gcp-credential-provider/main.go:133 returns_error: да description: getClaims is used to extract claims from the service account token when the plugin is running in service account mode
Th


### getClaims (test/e2e_node/plugins/gcp-credential-provider/main.go:133)


getClaims is used to extract claims from the service account token when the plugin is running in service account mode
This is solely for testing assertions and is not an actual security layer.
We get claims and validate the audience of the token (audience in the token matches the audience configured
in tokenAttributes.serviceAccountTokenAudience in CredentialProviderConfig).


```go
func getClaims((claims, error)) (claims, error)
```


**Тип ответа:** claims


```json
{
  "Kubernetes": {}
}
```


*Определено в:* `test/images/agnhost/openidmetadata/openidmetadata.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `claims`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/plugins/gcp-credential-provider/main.go:133`



---


[function] name: getCredentials file: test/e2e_node/plugins/gcp-credential-provider/main.go:50 returns_error: нет description: —


### getCredentials (test/e2e_node/plugins/gcp-credential-provider/main.go:50)


getCredentials is a function that performs operations based on the provided parameters and returns (tokenEndpoint string, r io.Reader, w io.Writer).


```go
func getCredentials((tokenEndpoint string, r io.Reader, w io.Writer)) (tokenEndpoint string, r io.Reader, w io.Writer)
```


**Тип ответа:** tokenEndpoint


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** io.Reader


```json
{
  "logger": {},
  "err": {},
  "r": {},
  "ping": false,
  "timeout": {},
  "protocols": {},
  "selectedProtocol": "string",
  "handleCrash": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/stream.go`


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


**Тип ответа:** io.Writer


```json
{
  "baseName": "string",
  "certificateDir": "string"
}
```


*Определено в:* `cmd/kubeadm/app/phases/certs/renewal/readwriter.go`


📍 *Расположение:* `test/e2e_node/plugins/gcp-credential-provider/main.go:50`



---


[function] name: main file: test/e2e_node/plugins/gcp-credential-provider/main.go:44 returns_error: нет description: —


### main (test/e2e_node/plugins/gcp-credential-provider/main.go:44)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/e2e_node/plugins/gcp-credential-provider/main.go:44`




## test/e2e_node/plugins/gcp-credential-provider/provider.go


📄 Исходный файл: `test/e2e_node/plugins/gcp-credential-provider/provider.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [Error](#error-teste2e_nodepluginsgcp-credential-providerprovidergo45) `:45`

- 🔗 [Provide](#provide-teste2e_nodepluginsgcp-credential-providerprovidergo61) `:61`

- 🔗 [readURL](#readurl-teste2e_nodepluginsgcp-credential-providerprovidergo86) `:86`


</details>


[function] name: Error file: test/e2e_node/plugins/gcp-credential-provider/provider.go:45 returns_error: нет description: Error implements error


### Error (test/e2e_node/plugins/gcp-credential-provider/provider.go:45)


Error implements error


```go
func (h *HTTPError) Error(()) ()
```


📍 *Расположение:* `test/e2e_node/plugins/gcp-credential-provider/provider.go:45`



---


[function] name: Provide file: test/e2e_node/plugins/gcp-credential-provider/provider.go:61 returns_error: да description: —


### Provide (test/e2e_node/plugins/gcp-credential-provider/provider.go:61)


Provide is a method that performs operations based on the provided parameters and may return an error.


```go
func (p *provider) Provide((map[string]credentialproviderv1.AuthConfig, error)) (map[string]credentialproviderv1.AuthConfig, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** credentialproviderv1.AuthConfig


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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[string]credentialproviderv1.AuthConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/plugins/gcp-credential-provider/provider.go:61`



---


[function] name: readURL file: test/e2e_node/plugins/gcp-credential-provider/provider.go:86 returns_error: да description: —


### readURL (test/e2e_node/plugins/gcp-credential-provider/provider.go:86)


readURL is a function that performs operations based on the provided parameters and may return an error.


```go
func readURL((body []byte, err error)) (body []byte, err error)
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


📍 *Расположение:* `test/e2e_node/plugins/gcp-credential-provider/provider.go:86`




## test/e2e_node/pod_host_ips.go


📄 Исходный файл: `test/e2e_node/pod_host_ips.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [genHostIPsForNode](#genhostipsfornode-teste2e_nodepod_host_ipsgo128) `:128`

- 🔗 [genPodHostIPs](#genpodhostips-teste2e_nodepod_host_ipsgo109) `:109`


</details>


[function] name: genHostIPsForNode file: test/e2e_node/pod_host_ips.go:128 returns_error: да description: —


### genHostIPsForNode (test/e2e_node/pod_host_ips.go:128)


genHostIPsForNode is a function that performs operations based on the provided parameters and may return an error.


```go
func genHostIPsForNode(([]v1.HostIP, error)) ([]v1.HostIP, error)
```


**Тип ответа:** v1.HostIP


```json
{
  "IP": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]v1.HostIP`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/pod_host_ips.go:128`



---


[function] name: genPodHostIPs file: test/e2e_node/pod_host_ips.go:109 returns_error: нет description: —


### genPodHostIPs (test/e2e_node/pod_host_ips.go:109)


genPodHostIPs is a function that performs operations based on the provided parameters and returns (podName string, hostNetwork bool).


```go
func genPodHostIPs((podName string, hostNetwork bool)) (podName string, hostNetwork bool)
```


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** hostNetwork


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/pod_host_ips.go:109`




## test/e2e_node/remote/cadvisor_e2e.go


📄 Исходный файл: `test/e2e_node/remote/cadvisor_e2e.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [RunTest](#runtest-teste2e_noderemotecadvisor_e2ego66) `:66`

- 🔗 [SetupTestPackage](#setuptestpackage-teste2e_noderemotecadvisor_e2ego38) `:38`

- 🔗 [init](#init-teste2e_noderemotecadvisor_e2ego33) `:33`

- 🔗 [runCommand](#runcommand-teste2e_noderemotecadvisor_e2ego54) `:54`


</details>


[function] name: RunTest file: test/e2e_node/remote/cadvisor_e2e.go:66 returns_error: да description: RunTest implements TestSuite.RunTest


### RunTest (test/e2e_node/remote/cadvisor_e2e.go:66)


RunTest implements TestSuite.RunTest


```go
func (n *CAdvisorE2ERemote) RunTest((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/cadvisor_e2e.go:66`



---


[function] name: SetupTestPackage file: test/e2e_node/remote/cadvisor_e2e.go:38 returns_error: нет description: SetupTestPackage implements TestSuite.SetupTestPackage


### SetupTestPackage (test/e2e_node/remote/cadvisor_e2e.go:38)


SetupTestPackage implements TestSuite.SetupTestPackage


```go
func (n *CAdvisorE2ERemote) SetupTestPackage((tardir, systemSpecName string)) (tardir, systemSpecName string)
```


**Тип ответа:** tardir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** systemSpecName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/cadvisor_e2e.go:38`



---


[function] name: init file: test/e2e_node/remote/cadvisor_e2e.go:33 returns_error: нет description: init performs initialization for cadvisor remote testing


### init (test/e2e_node/remote/cadvisor_e2e.go:33)


init performs initialization for cadvisor remote testing


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/cadvisor_e2e.go:33`



---


[function] name: runCommand file: test/e2e_node/remote/cadvisor_e2e.go:54 returns_error: нет description: —


### runCommand (test/e2e_node/remote/cadvisor_e2e.go:54)


runCommand is a function that performs operations based on the provided parameters and returns (command string, args ...string).


```go
func runCommand((command string, args ...string)) (command string, args ...string)
```


**Тип ответа:** command


```json
{
  "PrintFlags": null,
  "Name": "string",
  "StructuredGenerator": {},
  "DryRunStrategy": {},
  "CreateAnnotation": false,
  "FieldManager": "string",
  "ValidationDirective": "string",
  "Namespace": "string",
  "EnforceNamespace": false,
  "Mapper": {},
  "DynamicClient": {},
  "PrintObj": {}
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/create/create.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/cadvisor_e2e.go:54`




## test/e2e_node/remote/gce/gce_runner.go


📄 Исходный файл: `test/e2e_node/remote/gce/gce_runner.go`


<details open>
<summary><b>Функции в этом файле (25)</b></summary>


- 🔗 [DeleteGCEInstance](#deletegceinstance-teste2e_noderemotegcegce_runnergo350) `:350`

- 🔗 [Len](#len-teste2e_noderemotegcegce_runnergo328) `:328`

- 🔗 [Less](#less-teste2e_noderemotegcegce_runnergo329) `:329`

- 🔗 [NewGCERunner](#newgcerunner-teste2e_noderemotegcegce_runnergo94) `:94`

- 🔗 [Set](#set-teste2e_noderemotegcegce_runnergo56) `:56`

- 🔗 [StartTests](#starttests-teste2e_noderemotegcegce_runnergo117) `:117`

- 🔗 [String](#string-teste2e_noderemotegcegce_runnergo51) `:51`

- 🔗 [Swap](#swap-teste2e_noderemotegcegce_runnergo330) `:330`

- 🔗 [Validate](#validate-teste2e_noderemotegcegce_runnergo101) `:101`

- 🔗 [createGCEInstance](#creategceinstance-teste2e_noderemotegcegce_runnergo487) `:487`

- 🔗 [getExternalIP](#getexternalip-teste2e_noderemotegcegce_runnergo682) `:682`

- 🔗 [getGCEImage](#getgceimage-teste2e_noderemotegcegce_runnergo190) `:190`

- 🔗 [getImageMetadata](#getimagemetadata-teste2e_noderemotegcegce_runnergo332) `:332`

- 🔗 [ignitionInjectGCEPublicKey](#ignitioninjectgcepublickey-teste2e_noderemotegcegce_runnergo395) `:395`

- 🔗 [imageToInstanceName](#imagetoinstancename-teste2e_noderemotegcegce_runnergo653) `:653`

- 🔗 [init](#init-teste2e_noderemotegcegce_runnergo42) `:42`

- 🔗 [init](#init-teste2e_noderemotegcegce_runnergo81) `:81`

- 🔗 [isCloudInitUsed](#iscloudinitused-teste2e_noderemotegcegce_runnergo641) `:641`

- 🔗 [machineType](#machinetype-teste2e_noderemotegcegce_runnergo734) `:734`

- 🔗 [parseInstanceMetadata](#parseinstancemetadata-teste2e_noderemotegcegce_runnergo358) `:358`

- 🔗 [prepareGceImages](#preparegceimages-teste2e_noderemotegcegce_runnergo231) `:231`

- 🔗 [rebootInstance](#rebootinstance-teste2e_noderemotegcegce_runnergo746) `:746`

- 🔗 [registerGceHostIP](#registergcehostip-teste2e_noderemotegcegce_runnergo667) `:667`

- 🔗 [testGCEImage](#testgceimage-teste2e_noderemotegcegce_runnergo427) `:427`

- 🔗 [updateKernelArguments](#updatekernelarguments-teste2e_noderemotegcegce_runnergo695) `:695`


</details>


[function] name: DeleteGCEInstance file: test/e2e_node/remote/gce/gce_runner.go:350 returns_error: нет description: —


### DeleteGCEInstance (test/e2e_node/remote/gce/gce_runner.go:350)


DeleteGCEInstance is a method that deletes data based on the provided parameters and returns (host string).


```go
func (g *GCERunner) DeleteGCEInstance((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:350`



---


[function] name: Len file: test/e2e_node/remote/gce/gce_runner.go:328 returns_error: нет description: —


### Len (test/e2e_node/remote/gce/gce_runner.go:328)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (a byCreationTime) Len(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:328`



---


[function] name: Less file: test/e2e_node/remote/gce/gce_runner.go:329 returns_error: нет description: —


### Less (test/e2e_node/remote/gce/gce_runner.go:329)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (a byCreationTime) Less((i, j int)) (i, j int)
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


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:329`



---


[function] name: NewGCERunner file: test/e2e_node/remote/gce/gce_runner.go:94 returns_error: нет description: —


### NewGCERunner (test/e2e_node/remote/gce/gce_runner.go:94)


NewGCERunner is a function that performs operations based on the provided parameters and returns (cfg remote.Config).


```go
func NewGCERunner((cfg remote.Config)) (cfg remote.Config)
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


**Тип ответа:** remote.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:94`



---


[function] name: Set file: test/e2e_node/remote/gce/gce_runner.go:56 returns_error: нет description: Set function of flag.Value


### Set (test/e2e_node/remote/gce/gce_runner.go:56)


Set function of flag.Value


```go
func (e *envs) Set((value string)) (value string)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:56`



---


[function] name: StartTests file: test/e2e_node/remote/gce/gce_runner.go:117 returns_error: нет description: —


### StartTests (test/e2e_node/remote/gce/gce_runner.go:117)


StartTests is a method that performs operations based on the provided parameters and returns (numTests int).


```go
func (g *GCERunner) StartTests((numTests int)) (numTests int)
```


**Тип ответа:** numTests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:117`



---


[function] name: String file: test/e2e_node/remote/gce/gce_runner.go:51 returns_error: нет description: String function of flag.Value


### String (test/e2e_node/remote/gce/gce_runner.go:51)


String function of flag.Value


```go
func (e *envs) String(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:51`



---


[function] name: Swap file: test/e2e_node/remote/gce/gce_runner.go:330 returns_error: нет description: —


### Swap (test/e2e_node/remote/gce/gce_runner.go:330)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (a byCreationTime) Swap((i, j int)) (i, j int)
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


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:330`



---


[function] name: Validate file: test/e2e_node/remote/gce/gce_runner.go:101 returns_error: нет description: —


### Validate (test/e2e_node/remote/gce/gce_runner.go:101)


Validate is a method that performs operations based on the provided parameters and returns ().


```go
func (g *GCERunner) Validate(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:101`



---


[function] name: createGCEInstance file: test/e2e_node/remote/gce/gce_runner.go:487 returns_error: да description: Provision a gce instance using image


### createGCEInstance (test/e2e_node/remote/gce/gce_runner.go:487)


Provision a gce instance using image


```go
func (g *GCERunner) createGCEInstance((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:487`



---


[function] name: getExternalIP file: test/e2e_node/remote/gce/gce_runner.go:682 returns_error: нет description: —


### getExternalIP (test/e2e_node/remote/gce/gce_runner.go:682)


getExternalIP is a method that performs operations based on the provided parameters and returns (instance *gceInstance).


```go
func (g *GCERunner) getExternalIP((instance *gceInstance)) (instance *gceInstance)
```


**Тип запроса:** gceInstance


```json
{
  "CreationTimestamp": "string",
  "Description": "string",
  "Fingerprint": "string",
  "ID": "string",
  "KeyRevocationActionType": "string",
  "Kind": "string",
  "LabelFingerprint": "string",
  "LastStartTimestamp": "string",
  "MachineType": "string",
  "Metadata": {},
  "Name": "string",
  "NetworkInterfaces": [],
  "Status": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


**Тип ответа:** instance


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gceInstance


```json
{
  "CreationTimestamp": "string",
  "Description": "string",
  "Fingerprint": "string",
  "ID": "string",
  "KeyRevocationActionType": "string",
  "Kind": "string",
  "LabelFingerprint": "string",
  "LastStartTimestamp": "string",
  "MachineType": "string",
  "Metadata": {},
  "Name": "string",
  "NetworkInterfaces": [],
  "Status": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:682`



---


[function] name: getGCEImage file: test/e2e_node/remote/gce/gce_runner.go:190 returns_error: да description: Returns an image name based on regex and given GCE project.


### getGCEImage (test/e2e_node/remote/gce/gce_runner.go:190)


Returns an image name based on regex and given GCE project.


```go
func (g *GCERunner) getGCEImage((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:190`



---


[function] name: getImageMetadata file: test/e2e_node/remote/gce/gce_runner.go:332 returns_error: нет description: —


### getImageMetadata (test/e2e_node/remote/gce/gce_runner.go:332)


getImageMetadata is a method that performs operations based on the provided parameters and returns (input string).


```go
func (g *GCERunner) getImageMetadata((input string)) (input string)
```


**Тип ответа:** input


```json
{
  "builder": null
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/client-gen/args/gvpackages.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:332`



---


[function] name: ignitionInjectGCEPublicKey file: test/e2e_node/remote/gce/gce_runner.go:395 returns_error: нет description: ignitionInjectGCEPublicKey tries to inject the GCE SSH public key into the
provided ignition file path.

This will only 


### ignitionInjectGCEPublicKey (test/e2e_node/remote/gce/gce_runner.go:395)


ignitionInjectGCEPublicKey tries to inject the GCE SSH public key into the
provided ignition file path.

This will only being done if the job has the
IGNITION_INJECT_GCE_SSH_PUBLIC_KEY_FILE environment variable set, while it
tried to replace the GCE_SSH_PUBLIC_KEY_FILE_CONTENT placeholder.


```go
func ignitionInjectGCEPublicKey((content string)) (content string)
```


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:395`



---


[function] name: imageToInstanceName file: test/e2e_node/remote/gce/gce_runner.go:653 returns_error: нет description: —


### imageToInstanceName (test/e2e_node/remote/gce/gce_runner.go:653)


imageToInstanceName is a method that performs operations based on the provided parameters and returns (imageConfig *internalGCEImage).


```go
func (g *GCERunner) imageToInstanceName((imageConfig *internalGCEImage)) (imageConfig *internalGCEImage)
```


**Тип запроса:** internalGCEImage


```json
{
  "image": "string",
  "imageDesc": "string",
  "kernelArguments": [],
  "project": "string",
  "resources": {},
  "metadata": null,
  "machine": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gce_runner.go`


**Тип ответа:** imageConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** internalGCEImage


```json
{
  "image": "string",
  "imageDesc": "string",
  "kernelArguments": [],
  "project": "string",
  "resources": {},
  "metadata": null,
  "machine": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gce_runner.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:653`



---


[function] name: init file: test/e2e_node/remote/gce/gce_runner.go:42 returns_error: нет description: —


### init (test/e2e_node/remote/gce/gce_runner.go:42)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:42`



---


[function] name: init file: test/e2e_node/remote/gce/gce_runner.go:81 returns_error: нет description: —


### init (test/e2e_node/remote/gce/gce_runner.go:81)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:81`



---


[function] name: isCloudInitUsed file: test/e2e_node/remote/gce/gce_runner.go:641 returns_error: нет description: —


### isCloudInitUsed (test/e2e_node/remote/gce/gce_runner.go:641)


isCloudInitUsed is a method that performs operations based on the provided parameters and returns (metadata *gceMetadata).


```go
func (g *GCERunner) isCloudInitUsed((metadata *gceMetadata)) (metadata *gceMetadata)
```


**Тип запроса:** gceMetadata


```json
{
  "Fingerprint": "string",
  "Kind": "string",
  "Items": []
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


**Тип ответа:** metadata


```json
{
  "lister": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/metadata/metadatalister/shim.go`


**Тип ответа:** gceMetadata


```json
{
  "Fingerprint": "string",
  "Kind": "string",
  "Items": []
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:641`



---


[function] name: machineType file: test/e2e_node/remote/gce/gce_runner.go:734 returns_error: нет description: —


### machineType (test/e2e_node/remote/gce/gce_runner.go:734)


machineType is a method that performs operations based on the provided parameters and returns (machine string).


```go
func (g *GCERunner) machineType((machine string)) (machine string)
```


**Тип ответа:** machine


```json
{
  "sysfs": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/deviceattribute/machine.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:734`



---


[function] name: parseInstanceMetadata file: test/e2e_node/remote/gce/gce_runner.go:358 returns_error: нет description: —


### parseInstanceMetadata (test/e2e_node/remote/gce/gce_runner.go:358)


parseInstanceMetadata is a method that performs operations based on the provided parameters and returns (str string).


```go
func (g *GCERunner) parseInstanceMetadata((str string)) (str string)
```


**Тип ответа:** str


```json
{
  "BaseDir": "string",
  "IgnoredSubTrees": [],
  "AllowedImports": [],
  "ExcludeTests": false
}
```


*Определено в:* `cmd/importverifier/importverifier.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:358`



---


[function] name: prepareGceImages file: test/e2e_node/remote/gce/gce_runner.go:231 returns_error: да description: —


### prepareGceImages (test/e2e_node/remote/gce/gce_runner.go:231)


prepareGceImages is a method that performs operations based on the provided parameters and may return an error.


```go
func (g *GCERunner) prepareGceImages((*internalGCEImageConfig, error)) (*internalGCEImageConfig, error)
```


**Тип запроса:** internalGCEImageConfig


```json
{
  "images": {}
}
```


*Определено в:* `test/e2e_node/remote/gce/gce_runner.go`


**Тип ответа:** internalGCEImageConfig


```json
{
  "images": {}
}
```


*Определено в:* `test/e2e_node/remote/gce/gce_runner.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*internalGCEImageConfig`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:231`



---


[function] name: rebootInstance file: test/e2e_node/remote/gce/gce_runner.go:746 returns_error: нет description: —


### rebootInstance (test/e2e_node/remote/gce/gce_runner.go:746)


rebootInstance is a method that performs operations based on the provided parameters and returns (instance *gceInstance).


```go
func (g *GCERunner) rebootInstance((instance *gceInstance)) (instance *gceInstance)
```


**Тип запроса:** gceInstance


```json
{
  "CreationTimestamp": "string",
  "Description": "string",
  "Fingerprint": "string",
  "ID": "string",
  "KeyRevocationActionType": "string",
  "Kind": "string",
  "LabelFingerprint": "string",
  "LastStartTimestamp": "string",
  "MachineType": "string",
  "Metadata": {},
  "Name": "string",
  "NetworkInterfaces": [],
  "Status": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


**Тип ответа:** instance


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gceInstance


```json
{
  "CreationTimestamp": "string",
  "Description": "string",
  "Fingerprint": "string",
  "ID": "string",
  "KeyRevocationActionType": "string",
  "Kind": "string",
  "LabelFingerprint": "string",
  "LastStartTimestamp": "string",
  "MachineType": "string",
  "Metadata": {},
  "Name": "string",
  "NetworkInterfaces": [],
  "Status": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:746`



---


[function] name: registerGceHostIP file: test/e2e_node/remote/gce/gce_runner.go:667 returns_error: нет description: —


### registerGceHostIP (test/e2e_node/remote/gce/gce_runner.go:667)


registerGceHostIP is a method that performs operations based on the provided parameters and returns (host string).


```go
func (g *GCERunner) registerGceHostIP((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:667`



---


[function] name: testGCEImage file: test/e2e_node/remote/gce/gce_runner.go:427 returns_error: нет description: Provision a gce instance using image and run the tests in archive against the instance.
Delete the instance afterward.


### testGCEImage (test/e2e_node/remote/gce/gce_runner.go:427)


Provision a gce instance using image and run the tests in archive against the instance.
Delete the instance afterward.


```go
func (g *GCERunner) testGCEImage((suite remote.TestSuite, archivePath string, imageConfig *internalGCEImage, junitFileName string)) (suite remote.TestSuite, archivePath string, imageConfig *internalGCEImage, junitFileName string)
```


**Тип запроса:** internalGCEImage


```json
{
  "image": "string",
  "imageDesc": "string",
  "kernelArguments": [],
  "project": "string",
  "resources": {},
  "metadata": null,
  "machine": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gce_runner.go`


**Тип ответа:** suite


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** remote.TestSuite


```json
{
  "XMLName": {},
  "Name": "string",
  "Tests": 0,
  "Disabled": 0,
  "Errors": 0,
  "Failures": 0,
  "Skipped": 0,
  "Time": 0.0,
  "Timestamp": {},
  "ID": 0,
  "Package": "string",
  "Hostname": "string",
  "Properties": [],
  "TestCases": [],
  "SystemOut": "string",
  "SystemErr": "string"
}
```


*Определено в:* `test/utils/junit/junit.go`


**Тип ответа:** archivePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** imageConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** internalGCEImage


```json
{
  "image": "string",
  "imageDesc": "string",
  "kernelArguments": [],
  "project": "string",
  "resources": {},
  "metadata": null,
  "machine": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gce_runner.go`


**Тип ответа:** junitFileName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:427`



---


[function] name: updateKernelArguments file: test/e2e_node/remote/gce/gce_runner.go:695 returns_error: нет description: —


### updateKernelArguments (test/e2e_node/remote/gce/gce_runner.go:695)


updateKernelArguments is a method that performs operations based on the provided parameters and returns (instance *gceInstance, image string, kernelArgs []string).


```go
func (g *GCERunner) updateKernelArguments((instance *gceInstance, image string, kernelArgs []string)) (instance *gceInstance, image string, kernelArgs []string)
```


**Тип запроса:** gceInstance


```json
{
  "CreationTimestamp": "string",
  "Description": "string",
  "Fingerprint": "string",
  "ID": "string",
  "KeyRevocationActionType": "string",
  "Kind": "string",
  "LabelFingerprint": "string",
  "LastStartTimestamp": "string",
  "MachineType": "string",
  "Metadata": {},
  "Name": "string",
  "NetworkInterfaces": [],
  "Status": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


**Тип ответа:** instance


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** gceInstance


```json
{
  "CreationTimestamp": "string",
  "Description": "string",
  "Fingerprint": "string",
  "ID": "string",
  "KeyRevocationActionType": "string",
  "Kind": "string",
  "LabelFingerprint": "string",
  "LastStartTimestamp": "string",
  "MachineType": "string",
  "Metadata": {},
  "Name": "string",
  "NetworkInterfaces": [],
  "Status": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


**Тип ответа:** image


```json
{
  "cc": {}
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api_grpc.pb.go`


**Тип ответа:** kernelArgs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/gce/gce_runner.go:695`




## test/e2e_node/remote/gce/gcloud.go


📄 Исходный файл: `test/e2e_node/remote/gce/gcloud.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [getGCEInstance](#getgceinstance-teste2e_noderemotegcegcloudgo119) `:119`

- 🔗 [getSerialOutput](#getserialoutput-teste2e_noderemotegcegcloudgo133) `:133`

- 🔗 [runGCPCommand](#rungcpcommand-teste2e_noderemotegcegcloudgo98) `:98`

- 🔗 [runGCPCommandNoProject](#rungcpcommandnoproject-teste2e_noderemotegcegcloudgo105) `:105`

- 🔗 [runGCPCommandWithZone](#rungcpcommandwithzone-teste2e_noderemotegcegcloudgo84) `:84`

- 🔗 [runGCPCommandWithZones](#rungcpcommandwithzones-teste2e_noderemotegcegcloudgo91) `:91`


</details>


[function] name: getGCEInstance file: test/e2e_node/remote/gce/gcloud.go:119 returns_error: да description: —


### getGCEInstance (test/e2e_node/remote/gce/gcloud.go:119)


getGCEInstance is a function that performs operations based on the provided parameters and may return an error.


```go
func getGCEInstance((*gceInstance, error)) (*gceInstance, error)
```


**Тип запроса:** gceInstance


```json
{
  "CreationTimestamp": "string",
  "Description": "string",
  "Fingerprint": "string",
  "ID": "string",
  "KeyRevocationActionType": "string",
  "Kind": "string",
  "LabelFingerprint": "string",
  "LastStartTimestamp": "string",
  "MachineType": "string",
  "Metadata": {},
  "Name": "string",
  "NetworkInterfaces": [],
  "Status": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


**Тип ответа:** gceInstance


```json
{
  "CreationTimestamp": "string",
  "Description": "string",
  "Fingerprint": "string",
  "ID": "string",
  "KeyRevocationActionType": "string",
  "Kind": "string",
  "LabelFingerprint": "string",
  "LastStartTimestamp": "string",
  "MachineType": "string",
  "Metadata": {},
  "Name": "string",
  "NetworkInterfaces": [],
  "Status": "string"
}
```


*Определено в:* `test/e2e_node/remote/gce/gcloud.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*gceInstance`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gcloud.go:119`



---


[function] name: getSerialOutput file: test/e2e_node/remote/gce/gcloud.go:133 returns_error: да description: —


### getSerialOutput (test/e2e_node/remote/gce/gcloud.go:133)


getSerialOutput is a method that performs operations based on the provided parameters and may return an error.


```go
func (g *GCERunner) getSerialOutput((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gcloud.go:133`



---


[function] name: runGCPCommand file: test/e2e_node/remote/gce/gcloud.go:98 returns_error: да description: —


### runGCPCommand (test/e2e_node/remote/gce/gcloud.go:98)


runGCPCommand is a function that performs operations based on the provided parameters and may return an error.


```go
func runGCPCommand(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gcloud.go:98`



---


[function] name: runGCPCommandNoProject file: test/e2e_node/remote/gce/gcloud.go:105 returns_error: да description: —


### runGCPCommandNoProject (test/e2e_node/remote/gce/gcloud.go:105)


runGCPCommandNoProject is a function that performs operations based on the provided parameters and may return an error.


```go
func runGCPCommandNoProject(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gcloud.go:105`



---


[function] name: runGCPCommandWithZone file: test/e2e_node/remote/gce/gcloud.go:84 returns_error: да description: —


### runGCPCommandWithZone (test/e2e_node/remote/gce/gcloud.go:84)


runGCPCommandWithZone is a function that performs operations based on the provided parameters and may return an error.


```go
func runGCPCommandWithZone(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gcloud.go:84`



---


[function] name: runGCPCommandWithZones file: test/e2e_node/remote/gce/gcloud.go:91 returns_error: да description: —


### runGCPCommandWithZones (test/e2e_node/remote/gce/gcloud.go:91)


runGCPCommandWithZones is a function that performs operations based on the provided parameters and may return an error.


```go
func runGCPCommandWithZones(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/gce/gcloud.go:91`




## test/e2e_node/remote/node_conformance.go


📄 Исходный файл: `test/e2e_node/remote/node_conformance.go`


<details open>
<summary><b>Функции в этом файле (13)</b></summary>


- 🔗 [RunTest](#runtest-teste2e_noderemotenode_conformancego266) `:266`

- 🔗 [SetupTestPackage](#setuptestpackage-teste2e_noderemotenode_conformancego105) `:105`

- 🔗 [buildConformanceTest](#buildconformancetest-teste2e_noderemotenode_conformancego79) `:79`

- 🔗 [commandToString](#commandtostring-teste2e_noderemotenode_conformancego54) `:54`

- 🔗 [generateSecureToken](#generatesecuretoken-teste2e_noderemotenode_conformancego313) `:313`

- 🔗 [getConformanceDirectory](#getconformancedirectory-teste2e_noderemotenode_conformancego45) `:45`

- 🔗 [getConformanceTestImageName](#getconformancetestimagename-teste2e_noderemotenode_conformancego71) `:71`

- 🔗 [getPodPath](#getpodpath-teste2e_noderemotenode_conformancego160) `:160`

- 🔗 [init](#init-teste2e_noderemotenode_conformancego40) `:40`

- 🔗 [isSystemd](#issystemd-teste2e_noderemotenode_conformancego165) `:165`

- 🔗 [launchKubelet](#launchkubelet-teste2e_noderemotenode_conformancego179) `:179`

- 🔗 [loadConformanceImage](#loadconformanceimage-teste2e_noderemotenode_conformancego139) `:139`

- 🔗 [stopKubelet](#stopkubelet-teste2e_noderemotenode_conformancego227) `:227`


</details>


[function] name: RunTest file: test/e2e_node/remote/node_conformance.go:266 returns_error: да description: RunTest runs test on the node.


### RunTest (test/e2e_node/remote/node_conformance.go:266)


RunTest runs test on the node.


```go
func (c *ConformanceRemote) RunTest((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:266`



---


[function] name: SetupTestPackage file: test/e2e_node/remote/node_conformance.go:105 returns_error: нет description: SetupTestPackage sets up the test package with binaries k8s required for node conformance test


### SetupTestPackage (test/e2e_node/remote/node_conformance.go:105)


SetupTestPackage sets up the test package with binaries k8s required for node conformance test


```go
func (c *ConformanceRemote) SetupTestPackage((tardir, systemSpecName string)) (tardir, systemSpecName string)
```


**Тип ответа:** tardir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** systemSpecName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:105`



---


[function] name: buildConformanceTest file: test/e2e_node/remote/node_conformance.go:79 returns_error: нет description: buildConformanceTest builds node conformance test image tarball into binDir.


### buildConformanceTest (test/e2e_node/remote/node_conformance.go:79)


buildConformanceTest builds node conformance test image tarball into binDir.


```go
func buildConformanceTest((binDir, systemSpecName string)) (binDir, systemSpecName string)
```


**Тип ответа:** binDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** systemSpecName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:79`



---


[function] name: commandToString file: test/e2e_node/remote/node_conformance.go:54 returns_error: нет description: commandToString is a helper function which formats command to string.


### commandToString (test/e2e_node/remote/node_conformance.go:54)


commandToString is a helper function which formats command to string.


```go
func commandToString((c *exec.Cmd)) (c *exec.Cmd)
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


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:54`



---


[function] name: generateSecureToken file: test/e2e_node/remote/node_conformance.go:313 returns_error: да description: generateSecureToken returns a string of length tokenLen, consisting
of random bytes encoded as base64 for use as a Beare


### generateSecureToken (test/e2e_node/remote/node_conformance.go:313)


generateSecureToken returns a string of length tokenLen, consisting
of random bytes encoded as base64 for use as a Bearer Token during
communication with an APIServer


```go
func generateSecureToken((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:313`



---


[function] name: getConformanceDirectory file: test/e2e_node/remote/node_conformance.go:45 returns_error: да description: getConformanceDirectory gets node conformance test build directory.


### getConformanceDirectory (test/e2e_node/remote/node_conformance.go:45)


getConformanceDirectory gets node conformance test build directory.


```go
func getConformanceDirectory((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:45`



---


[function] name: getConformanceTestImageName file: test/e2e_node/remote/node_conformance.go:71 returns_error: нет description: getConformanceTestImageName returns name of the conformance test image given the system spec name.


### getConformanceTestImageName (test/e2e_node/remote/node_conformance.go:71)


getConformanceTestImageName returns name of the conformance test image given the system spec name.


```go
func getConformanceTestImageName((systemSpecName string)) (systemSpecName string)
```


**Тип ответа:** systemSpecName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:71`



---


[function] name: getPodPath file: test/e2e_node/remote/node_conformance.go:160 returns_error: нет description: getPodPath returns pod manifest full path.


### getPodPath (test/e2e_node/remote/node_conformance.go:160)


getPodPath returns pod manifest full path.


```go
func getPodPath((workspace string)) (workspace string)
```


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:160`



---


[function] name: init file: test/e2e_node/remote/node_conformance.go:40 returns_error: нет description: —


### init (test/e2e_node/remote/node_conformance.go:40)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:40`



---


[function] name: isSystemd file: test/e2e_node/remote/node_conformance.go:165 returns_error: да description: isSystemd returns whether the node is a systemd node.


### isSystemd (test/e2e_node/remote/node_conformance.go:165)


isSystemd returns whether the node is a systemd node.


```go
func isSystemd((bool, error)) (bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:165`



---


[function] name: launchKubelet file: test/e2e_node/remote/node_conformance.go:179 returns_error: нет description: launchKubelet launches kubelet by running e2e_node.test binary in run-kubelet-mode.
This is a temporary solution, we sho


### launchKubelet (test/e2e_node/remote/node_conformance.go:179)


launchKubelet launches kubelet by running e2e_node.test binary in run-kubelet-mode.
This is a temporary solution, we should change node e2e to use the same node bootstrap
with cluster e2e and launch kubelet outside of the test for both regular node e2e and
node conformance test.
TODO(random-liu): Switch to use standard node bootstrap script.


```go
func launchKubelet((host, workspace, results, testArgs, bearerToken string)) (host, workspace, results, testArgs, bearerToken string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** results


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** testArgs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** bearerToken


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:179`



---


[function] name: loadConformanceImage file: test/e2e_node/remote/node_conformance.go:139 returns_error: нет description: loadConformanceImage loads node conformance image from tar file.


### loadConformanceImage (test/e2e_node/remote/node_conformance.go:139)


loadConformanceImage loads node conformance image from tar file.


```go
func loadConformanceImage((host, workspace string)) (host, workspace string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:139`



---


[function] name: stopKubelet file: test/e2e_node/remote/node_conformance.go:227 returns_error: нет description: stopKubelet stops kubelet launcher and kubelet gracefully.


### stopKubelet (test/e2e_node/remote/node_conformance.go:227)


stopKubelet stops kubelet launcher and kubelet gracefully.


```go
func stopKubelet((host, workspace string)) (host, workspace string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_conformance.go:227`




## test/e2e_node/remote/node_e2e.go


📄 Исходный файл: `test/e2e_node/remote/node_e2e.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [RunTest](#runtest-teste2e_noderemotenode_e2ego177) `:177`

- 🔗 [SetupTestPackage](#setuptestpackage-teste2e_noderemotenode_e2ego44) `:44`

- 🔗 [getOSDistribution](#getosdistribution-teste2e_noderemotenode_e2ego161) `:161`

- 🔗 [init](#init-teste2e_noderemotenode_e2ego39) `:39`

- 🔗 [osSpecificActions](#osspecificactions-teste2e_noderemotenode_e2ego122) `:122`

- 🔗 [prependCredentialProviderFlag](#prependcredentialproviderflag-teste2e_noderemotenode_e2ego113) `:113`

- 🔗 [prependMemcgNotificationFlag](#prependmemcgnotificationflag-teste2e_noderemotenode_e2ego107) `:107`

- 🔗 [setKubeletSELinuxLabels](#setkubeletselinuxlabels-teste2e_noderemotenode_e2ego146) `:146`


</details>


[function] name: RunTest file: test/e2e_node/remote/node_e2e.go:177 returns_error: да description: RunTest runs test on the node.


### RunTest (test/e2e_node/remote/node_e2e.go:177)


RunTest runs test on the node.


```go
func (n *NodeE2ERemote) RunTest((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/node_e2e.go:177`



---


[function] name: SetupTestPackage file: test/e2e_node/remote/node_e2e.go:44 returns_error: нет description: SetupTestPackage sets up the test package with binaries k8s required for node e2e tests


### SetupTestPackage (test/e2e_node/remote/node_e2e.go:44)


SetupTestPackage sets up the test package with binaries k8s required for node e2e tests


```go
func (n *NodeE2ERemote) SetupTestPackage((tardir, systemSpecName string)) (tardir, systemSpecName string)
```


**Тип ответа:** tardir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** systemSpecName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_e2e.go:44`



---


[function] name: getOSDistribution file: test/e2e_node/remote/node_e2e.go:161 returns_error: да description: —


### getOSDistribution (test/e2e_node/remote/node_e2e.go:161)


getOSDistribution is a function that performs operations based on the provided parameters and may return an error.


```go
func getOSDistribution((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/node_e2e.go:161`



---


[function] name: init file: test/e2e_node/remote/node_e2e.go:39 returns_error: нет description: init initializes the node e2e test suite.


### init (test/e2e_node/remote/node_e2e.go:39)


init initializes the node e2e test suite.


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/node_e2e.go:39`



---


[function] name: osSpecificActions file: test/e2e_node/remote/node_e2e.go:122 returns_error: да description: osSpecificActions takes OS specific actions required for the node tests


### osSpecificActions (test/e2e_node/remote/node_e2e.go:122)


osSpecificActions takes OS specific actions required for the node tests


```go
func osSpecificActions((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/node_e2e.go:122`



---


[function] name: prependCredentialProviderFlag file: test/e2e_node/remote/node_e2e.go:113 returns_error: нет description: prependCredentialProviderFlag prepends the flags for enabling
a credential provider plugin.


### prependCredentialProviderFlag (test/e2e_node/remote/node_e2e.go:113)


prependCredentialProviderFlag prepends the flags for enabling
a credential provider plugin.


```go
func prependCredentialProviderFlag((args, workspace string)) (args, workspace string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_e2e.go:113`



---


[function] name: prependMemcgNotificationFlag file: test/e2e_node/remote/node_e2e.go:107 returns_error: нет description: prependMemcgNotificationFlag prepends the flag for enabling memcg
notification to args and returns the result.


### prependMemcgNotificationFlag (test/e2e_node/remote/node_e2e.go:107)


prependMemcgNotificationFlag prepends the flag for enabling memcg
notification to args and returns the result.


```go
func prependMemcgNotificationFlag((args string)) (args string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_e2e.go:107`



---


[function] name: setKubeletSELinuxLabels file: test/e2e_node/remote/node_e2e.go:146 returns_error: нет description: setKubeletSELinuxLabels set the appropriate SELinux labels for the
kubelet on Fedora CoreOS distribution


### setKubeletSELinuxLabels (test/e2e_node/remote/node_e2e.go:146)


setKubeletSELinuxLabels set the appropriate SELinux labels for the
kubelet on Fedora CoreOS distribution


```go
func setKubeletSELinuxLabels((host, workspace string)) (host, workspace string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/node_e2e.go:146`




## test/e2e_node/remote/remote.go


📄 Исходный файл: `test/e2e_node/remote/remote.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [CreateTestArchive](#createtestarchive-teste2e_noderemoteremotego71) `:71`

- 🔗 [GetTimestampFromWorkspaceDir](#gettimestampfromworkspacedir-teste2e_noderemoteremotego207) `:207`

- 🔗 [RunRemote](#runremote-teste2e_noderemoteremotego112) `:112`

- 🔗 [WriteLog](#writelog-teste2e_noderemoteremotego283) `:283`

- 🔗 [collectSystemLog](#collectsystemlog-teste2e_noderemoteremotego255) `:255`

- 🔗 [copyKubeletConfigIfExists](#copykubeletconfigifexists-teste2e_noderemoteremotego39) `:39`

- 🔗 [getTestArtifacts](#gettestartifacts-teste2e_noderemoteremotego217) `:217`

- 🔗 [getTimestamp](#gettimestamp-teste2e_noderemoteremotego195) `:195`

- 🔗 [newWorkspaceDir](#newworkspacedir-teste2e_noderemoteremotego199) `:199`


</details>


[function] name: CreateTestArchive file: test/e2e_node/remote/remote.go:71 returns_error: да description: CreateTestArchive creates the archive package for the node e2e test.


### CreateTestArchive (test/e2e_node/remote/remote.go:71)


CreateTestArchive creates the archive package for the node e2e test.


```go
func CreateTestArchive((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/remote.go:71`



---


[function] name: GetTimestampFromWorkspaceDir file: test/e2e_node/remote/remote.go:207 returns_error: нет description: GetTimestampFromWorkspaceDir parses the workspace directory name and gets the timestamp part of it.
This can later be us


### GetTimestampFromWorkspaceDir (test/e2e_node/remote/remote.go:207)


GetTimestampFromWorkspaceDir parses the workspace directory name and gets the timestamp part of it.
This can later be used to name other artifacts (such as the
kubelet-${instance}.service systemd transient service used to launch
Kubelet) so that they can be matched to each other.


```go
func GetTimestampFromWorkspaceDir((dir string)) (dir string)
```


**Тип ответа:** dir


```json
{
  "name": "string",
  "goRestfulContainer": null,
  "nonGoRestfulMux": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/handler.go`


📍 *Расположение:* `test/e2e_node/remote/remote.go:207`



---


[function] name: RunRemote file: test/e2e_node/remote/remote.go:112 returns_error: да description: —


### RunRemote (test/e2e_node/remote/remote.go:112)


RunRemote is a function that performs operations based on the provided parameters and may return an error.


```go
func RunRemote((string, bool, error)) (string, bool, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `bool`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/remote.go:112`



---


[function] name: WriteLog file: test/e2e_node/remote/remote.go:283 returns_error: нет description: WriteLog is a temporary function to make it possible to write log
in the runner. This is used to collect serial console 


### WriteLog (test/e2e_node/remote/remote.go:283)


WriteLog is a temporary function to make it possible to write log
in the runner. This is used to collect serial console log.
TODO(random-liu): Use the log-dump script in cluster e2e.


```go
func WriteLog((host, filename, content string)) (host, filename, content string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** filename


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** content


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/remote.go:283`



---


[function] name: collectSystemLog file: test/e2e_node/remote/remote.go:255 returns_error: нет description: collectSystemLog is a temporary hack to collect system log when encountered on
unexpected error.


### collectSystemLog (test/e2e_node/remote/remote.go:255)


collectSystemLog is a temporary hack to collect system log when encountered on
unexpected error.


```go
func collectSystemLog((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


📍 *Расположение:* `test/e2e_node/remote/remote.go:255`



---


[function] name: copyKubeletConfigIfExists file: test/e2e_node/remote/remote.go:39 returns_error: нет description: —


### copyKubeletConfigIfExists (test/e2e_node/remote/remote.go:39)


copyKubeletConfigIfExists is a function that performs operations based on the provided parameters and returns (kubeletConfigFile, dstDir string).


```go
func copyKubeletConfigIfExists((kubeletConfigFile, dstDir string)) (kubeletConfigFile, dstDir string)
```


**Тип ответа:** kubeletConfigFile


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** dstDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/remote.go:39`



---


[function] name: getTestArtifacts file: test/e2e_node/remote/remote.go:217 returns_error: нет description: —


### getTestArtifacts (test/e2e_node/remote/remote.go:217)


getTestArtifacts is a function that performs operations based on the provided parameters and returns (host, testDir string).


```go
func getTestArtifacts((host, testDir string)) (host, testDir string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** testDir


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/remote.go:217`



---


[function] name: getTimestamp file: test/e2e_node/remote/remote.go:195 returns_error: нет description: —


### getTimestamp (test/e2e_node/remote/remote.go:195)


getTimestamp is a function that performs operations based on the provided parameters and returns ().


```go
func getTimestamp(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/remote.go:195`



---


[function] name: newWorkspaceDir file: test/e2e_node/remote/remote.go:199 returns_error: нет description: —


### newWorkspaceDir (test/e2e_node/remote/remote.go:199)


newWorkspaceDir is a function that performs operations based on the provided parameters and returns ().


```go
func newWorkspaceDir(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/remote.go:199`




## test/e2e_node/remote/run_remote_suite.go


📄 Исходный файл: `test/e2e_node/remote/run_remote_suite.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [RunRemoteTestSuite](#runremotetestsuite-teste2e_noderemoterun_remote_suitego63) `:63`

- 🔗 [callGubernator](#callgubernator-teste2e_noderemoterun_remote_suitego189) `:189`

- 🔗 [deleteArchive](#deletearchive-teste2e_noderemoterun_remote_suitego213) `:213`

- 🔗 [getArchive](#getarchive-teste2e_noderemoterun_remote_suitego204) `:204`

- 🔗 [getFlag](#getflag-teste2e_noderemoterun_remote_suitego55) `:55`

- 🔗 [parseHostsList](#parsehostslist-teste2e_noderemoterun_remote_suitego223) `:223`

- 🔗 [splitCommaList](#splitcommalist-teste2e_noderemoterun_remote_suitego182) `:182`


</details>


[function] name: RunRemoteTestSuite file: test/e2e_node/remote/run_remote_suite.go:63 returns_error: нет description: —


### RunRemoteTestSuite (test/e2e_node/remote/run_remote_suite.go:63)


RunRemoteTestSuite is a function that performs operations based on the provided parameters and returns (testSuite TestSuite).


```go
func RunRemoteTestSuite((testSuite TestSuite)) (testSuite TestSuite)
```


**Тип ответа:** testSuite


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestSuite


```json
{
  "XMLName": {},
  "Name": "string",
  "Tests": 0,
  "Disabled": 0,
  "Errors": 0,
  "Failures": 0,
  "Skipped": 0,
  "Time": 0.0,
  "Timestamp": {},
  "ID": 0,
  "Package": "string",
  "Hostname": "string",
  "Properties": [],
  "TestCases": [],
  "SystemOut": "string",
  "SystemErr": "string"
}
```


*Определено в:* `test/utils/junit/junit.go`


📍 *Расположение:* `test/e2e_node/remote/run_remote_suite.go:63`



---


[function] name: callGubernator file: test/e2e_node/remote/run_remote_suite.go:189 returns_error: нет description: —


### callGubernator (test/e2e_node/remote/run_remote_suite.go:189)


callGubernator is a function that performs operations based on the provided parameters and returns (gubernator bool).


```go
func callGubernator((gubernator bool)) (gubernator bool)
```


**Тип ответа:** gubernator


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/run_remote_suite.go:189`



---


[function] name: deleteArchive file: test/e2e_node/remote/run_remote_suite.go:213 returns_error: нет description: —


### deleteArchive (test/e2e_node/remote/run_remote_suite.go:213)


deleteArchive is a method that performs operations based on the provided parameters and returns ().


```go
func (a *Archive) deleteArchive(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/run_remote_suite.go:213`



---


[function] name: getArchive file: test/e2e_node/remote/run_remote_suite.go:204 returns_error: да description: —


### getArchive (test/e2e_node/remote/run_remote_suite.go:204)


getArchive is a method that performs operations based on the provided parameters and may return an error.


```go
func (a *Archive) getArchive((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/run_remote_suite.go:204`



---


[function] name: getFlag file: test/e2e_node/remote/run_remote_suite.go:55 returns_error: нет description: —


### getFlag (test/e2e_node/remote/run_remote_suite.go:55)


getFlag is a function that performs operations based on the provided parameters and returns (name string).


```go
func getFlag((name string)) (name string)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


📍 *Расположение:* `test/e2e_node/remote/run_remote_suite.go:55`



---


[function] name: parseHostsList file: test/e2e_node/remote/run_remote_suite.go:223 returns_error: нет description: parseHostsList splits a host list of the form a=1.2.3.4,b=5.6.7.8 into the list of hosts [a,b] while registering the
giv


### parseHostsList (test/e2e_node/remote/run_remote_suite.go:223)


parseHostsList splits a host list of the form a=1.2.3.4,b=5.6.7.8 into the list of hosts [a,b] while registering the
given addresses


```go
func parseHostsList((hostList string)) (hostList string)
```


**Тип ответа:** hostList


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/run_remote_suite.go:223`



---


[function] name: splitCommaList file: test/e2e_node/remote/run_remote_suite.go:182 returns_error: нет description: —


### splitCommaList (test/e2e_node/remote/run_remote_suite.go:182)


splitCommaList is a function that performs operations based on the provided parameters and returns (s string).


```go
func splitCommaList((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `test/e2e_node/remote/run_remote_suite.go:182`




## test/e2e_node/remote/ssh.go


📄 Исходный файл: `test/e2e_node/remote/ssh.go`


<details open>
<summary><b>Функции в этом файле (10)</b></summary>


- 🔗 [AddHostnameIP](#addhostnameip-teste2e_noderemotesshgo67) `:67`

- 🔗 [AddSSHKey](#addsshkey-teste2e_noderemotesshgo79) `:79`

- 🔗 [GetHostnameOrIP](#gethostnameorip-teste2e_noderemotesshgo98) `:98`

- 🔗 [GetSSHUser](#getsshuser-teste2e_noderemotesshgo87) `:87`

- 🔗 [SSH](#ssh-teste2e_noderemotesshgo120) `:120`

- 🔗 [SSHNoSudo](#sshnosudo-teste2e_noderemotesshgo126) `:126`

- 🔗 [getPrivateSSHKey](#getprivatesshkey-teste2e_noderemotesshgo156) `:156`

- 🔗 [getSSHCommand](#getsshcommand-teste2e_noderemotesshgo114) `:114`

- 🔗 [init](#init-teste2e_noderemotesshgo40) `:40`

- 🔗 [runSSHCommand](#runsshcommand-teste2e_noderemotesshgo131) `:131`


</details>


[function] name: AddHostnameIP file: test/e2e_node/remote/ssh.go:67 returns_error: нет description: AddHostnameIP adds <hostname,ip> pair into hostnameIPOverrides map.


### AddHostnameIP (test/e2e_node/remote/ssh.go:67)


AddHostnameIP adds <hostname,ip> pair into hostnameIPOverrides map.


```go
func AddHostnameIP((hostname, ip string)) (hostname, ip string)
```


**Тип ответа:** hostname


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


📍 *Расположение:* `test/e2e_node/remote/ssh.go:67`



---


[function] name: AddSSHKey file: test/e2e_node/remote/ssh.go:79 returns_error: нет description: AddSSHKey adds a <hosrtname,path to SSH private key> pair into the sshKeyOverrides map


### AddSSHKey (test/e2e_node/remote/ssh.go:79)


AddSSHKey adds a <hosrtname,path to SSH private key> pair into the sshKeyOverrides map


```go
func AddSSHKey((hostname, keyFilePath string)) (hostname, keyFilePath string)
```


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** keyFilePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/ssh.go:79`



---


[function] name: GetHostnameOrIP file: test/e2e_node/remote/ssh.go:98 returns_error: нет description: GetHostnameOrIP converts hostname into ip and apply user if necessary.


### GetHostnameOrIP (test/e2e_node/remote/ssh.go:98)


GetHostnameOrIP converts hostname into ip and apply user if necessary.


```go
func GetHostnameOrIP((hostname string)) (hostname string)
```


**Тип ответа:** hostname


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/ssh.go:98`



---


[function] name: GetSSHUser file: test/e2e_node/remote/ssh.go:87 returns_error: нет description: GetSSHUser returns the ssh-user CLI flag, the KUBE_SSH_USER environment variable, or the default ssh user
for the ssh en


### GetSSHUser (test/e2e_node/remote/ssh.go:87)


GetSSHUser returns the ssh-user CLI flag, the KUBE_SSH_USER environment variable, or the default ssh user
for the ssh environment in that order


```go
func GetSSHUser(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/ssh.go:87`



---


[function] name: SSH file: test/e2e_node/remote/ssh.go:120 returns_error: да description: SSH executes ssh command with runSSHCommand as root. The `sudo` makes sure that all commands
are executed by root, so th


### SSH (test/e2e_node/remote/ssh.go:120)


SSH executes ssh command with runSSHCommand as root. The `sudo` makes sure that all commands
are executed by root, so that there won't be permission mismatch between different commands.


```go
func SSH((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/ssh.go:120`



---


[function] name: SSHNoSudo file: test/e2e_node/remote/ssh.go:126 returns_error: да description: SSHNoSudo executes ssh command with runSSHCommand as normal user. Sometimes we need this,
for example creating a directo


### SSHNoSudo (test/e2e_node/remote/ssh.go:126)


SSHNoSudo executes ssh command with runSSHCommand as normal user. Sometimes we need this,
for example creating a directory that we'll copy files there with scp.


```go
func SSHNoSudo((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/ssh.go:126`



---


[function] name: getPrivateSSHKey file: test/e2e_node/remote/ssh.go:156 returns_error: да description: getPrivateSSHKey returns the path to ssh private key


### getPrivateSSHKey (test/e2e_node/remote/ssh.go:156)


getPrivateSSHKey returns the path to ssh private key


```go
func getPrivateSSHKey((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/ssh.go:156`



---


[function] name: getSSHCommand file: test/e2e_node/remote/ssh.go:114 returns_error: нет description: getSSHCommand handles proper quoting so that multiple commands are executed in the same shell over ssh


### getSSHCommand (test/e2e_node/remote/ssh.go:114)


getSSHCommand handles proper quoting so that multiple commands are executed in the same shell over ssh


```go
func getSSHCommand((sep string, args ...string)) (sep string, args ...string)
```


**Тип ответа:** sep


```json
{
  "Delegate": {},
  "Ready": false
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/get/get.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/ssh.go:114`



---


[function] name: init file: test/e2e_node/remote/ssh.go:40 returns_error: нет description: —


### init (test/e2e_node/remote/ssh.go:40)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/ssh.go:40`



---


[function] name: runSSHCommand file: test/e2e_node/remote/ssh.go:131 returns_error: да description: runSSHCommand executes the ssh or scp command, adding the flag provided --ssh-options


### runSSHCommand (test/e2e_node/remote/ssh.go:131)


runSSHCommand executes the ssh or scp command, adding the flag provided --ssh-options


```go
func runSSHCommand((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/ssh.go:131`




## test/e2e_node/remote/ssh_runner.go


📄 Исходный файл: `test/e2e_node/remote/ssh_runner.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [NewSSHRunner](#newsshrunner-teste2e_noderemotessh_runnergo58) `:58`

- 🔗 [StartTests](#starttests-teste2e_noderemotessh_runnergo29) `:29`

- 🔗 [Validate](#validate-teste2e_noderemotessh_runnergo64) `:64`


</details>


[function] name: NewSSHRunner file: test/e2e_node/remote/ssh_runner.go:58 returns_error: нет description: —


### NewSSHRunner (test/e2e_node/remote/ssh_runner.go:58)


NewSSHRunner is a function that performs operations based on the provided parameters and returns (cfg Config).


```go
func NewSSHRunner((cfg Config)) (cfg Config)
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


**Тип ответа:** Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/e2e_node/remote/ssh_runner.go:58`



---


[function] name: StartTests file: test/e2e_node/remote/ssh_runner.go:29 returns_error: нет description: —


### StartTests (test/e2e_node/remote/ssh_runner.go:29)


StartTests is a method that performs operations based on the provided parameters and returns (numTests int).


```go
func (s *SSHRunner) StartTests((numTests int)) (numTests int)
```


**Тип ответа:** numTests


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/ssh_runner.go:29`



---


[function] name: Validate file: test/e2e_node/remote/ssh_runner.go:64 returns_error: нет description: —


### Validate (test/e2e_node/remote/ssh_runner.go:64)


Validate is a method that performs operations based on the provided parameters and returns ().


```go
func (s *SSHRunner) Validate(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/ssh_runner.go:64`




## test/e2e_node/remote/types.go


📄 Исходный файл: `test/e2e_node/remote/types.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GetRunner](#getrunner-teste2e_noderemotetypesgo86) `:86`

- 🔗 [GetTestSuite](#gettestsuite-teste2e_noderemotetypesgo70) `:70`

- 🔗 [GetTestSuiteKeys](#gettestsuitekeys-teste2e_noderemotetypesgo62) `:62`

- 🔗 [RegisterRunner](#registerrunner-teste2e_noderemotetypesgo82) `:82`

- 🔗 [RegisterTestSuite](#registertestsuite-teste2e_noderemotetypesgo58) `:58`


</details>


[function] name: GetRunner file: test/e2e_node/remote/types.go:86 returns_error: да description: —


### GetRunner (test/e2e_node/remote/types.go:86)


GetRunner is a function that retrieves data based on the provided parameters and may return an error.


```go
func GetRunner((NewRunner, error)) (NewRunner, error)
```


**Тип ответа:** NewRunner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `NewRunner`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/types.go:86`



---


[function] name: GetTestSuite file: test/e2e_node/remote/types.go:70 returns_error: да description: —


### GetTestSuite (test/e2e_node/remote/types.go:70)


GetTestSuite is a function that retrieves data based on the provided parameters and may return an error.


```go
func GetTestSuite((TestSuite, error)) (TestSuite, error)
```


**Тип ответа:** TestSuite


```json
{
  "XMLName": {},
  "Name": "string",
  "Tests": 0,
  "Disabled": 0,
  "Errors": 0,
  "Failures": 0,
  "Skipped": 0,
  "Time": 0.0,
  "Timestamp": {},
  "ID": 0,
  "Package": "string",
  "Hostname": "string",
  "Properties": [],
  "TestCases": [],
  "SystemOut": "string",
  "SystemErr": "string"
}
```


*Определено в:* `test/utils/junit/junit.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `TestSuite`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/remote/types.go:70`



---


[function] name: GetTestSuiteKeys file: test/e2e_node/remote/types.go:62 returns_error: нет description: —


### GetTestSuiteKeys (test/e2e_node/remote/types.go:62)


GetTestSuiteKeys is a function that retrieves data based on the provided parameters and returns ().


```go
func GetTestSuiteKeys(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/types.go:62`



---


[function] name: RegisterRunner file: test/e2e_node/remote/types.go:82 returns_error: нет description: —


### RegisterRunner (test/e2e_node/remote/types.go:82)


RegisterRunner is a function that performs operations based on the provided parameters and returns (name string, runner NewRunner).


```go
func RegisterRunner((name string, runner NewRunner)) (name string, runner NewRunner)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** runner


```json
{
  "mu": {},
  "exec": {},
  "protocol": {},
  "hasCheck": false,
  "hasRandomFully": false,
  "waitFlag": [],
  "restoreWaitFlag": [],
  "lockfilePath14x": "string",
  "lockfilePath16x": "string"
}
```


*Определено в:* `pkg/util/iptables/iptables.go`


**Тип ответа:** NewRunner


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/types.go:82`



---


[function] name: RegisterTestSuite file: test/e2e_node/remote/types.go:58 returns_error: нет description: —


### RegisterTestSuite (test/e2e_node/remote/types.go:58)


RegisterTestSuite is a function that performs operations based on the provided parameters and returns (name string, suite TestSuite).


```go
func RegisterTestSuite((name string, suite TestSuite)) (name string, suite TestSuite)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** suite


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** TestSuite


```json
{
  "XMLName": {},
  "Name": "string",
  "Tests": 0,
  "Disabled": 0,
  "Errors": 0,
  "Failures": 0,
  "Skipped": 0,
  "Time": 0.0,
  "Timestamp": {},
  "ID": 0,
  "Package": "string",
  "Hostname": "string",
  "Properties": [],
  "TestCases": [],
  "SystemOut": "string",
  "SystemErr": "string"
}
```


*Определено в:* `test/utils/junit/junit.go`


📍 *Расположение:* `test/e2e_node/remote/types.go:58`




## test/e2e_node/remote/utils.go


📄 Исходный файл: `test/e2e_node/remote/utils.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [cleanupNodeProcesses](#cleanupnodeprocesses-teste2e_noderemoteutilsgo199) `:199`

- 🔗 [configureCredentialProvider](#configurecredentialprovider-teste2e_noderemoteutilsgo155) `:155`

- 🔗 [configureFirewall](#configurefirewall-teste2e_noderemoteutilsgo178) `:178`

- 🔗 [getCNIURL](#getcniurl-teste2e_noderemoteutilsgo96) `:96`

- 🔗 [getECRCredentialProviderURL](#getecrcredentialproviderurl-teste2e_noderemoteutilsgo135) `:135`

- 🔗 [quote](#quote-teste2e_noderemoteutilsgo214) `:214`

- 🔗 [setupCNI](#setupcni-teste2e_noderemoteutilsgo108) `:108`

- 🔗 [setupECRCredentialProvider](#setupecrcredentialprovider-teste2e_noderemoteutilsgo143) `:143`


</details>


[function] name: cleanupNodeProcesses file: test/e2e_node/remote/utils.go:199 returns_error: нет description: cleanupNodeProcesses kills all running node processes may conflict with the test.


### cleanupNodeProcesses (test/e2e_node/remote/utils.go:199)


cleanupNodeProcesses kills all running node processes may conflict with the test.


```go
func cleanupNodeProcesses((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


📍 *Расположение:* `test/e2e_node/remote/utils.go:199`



---


[function] name: configureCredentialProvider file: test/e2e_node/remote/utils.go:155 returns_error: нет description: —


### configureCredentialProvider (test/e2e_node/remote/utils.go:155)


configureCredentialProvider is a function that performs operations based on the provided parameters and returns (host, workspace string).


```go
func configureCredentialProvider((host, workspace string)) (host, workspace string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/utils.go:155`



---


[function] name: configureFirewall file: test/e2e_node/remote/utils.go:178 returns_error: нет description: configureFirewall configures iptable firewall rules.


### configureFirewall (test/e2e_node/remote/utils.go:178)


configureFirewall configures iptable firewall rules.


```go
func configureFirewall((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


📍 *Расположение:* `test/e2e_node/remote/utils.go:178`



---


[function] name: getCNIURL file: test/e2e_node/remote/utils.go:96 returns_error: нет description: —


### getCNIURL (test/e2e_node/remote/utils.go:96)


getCNIURL is a function that performs operations based on the provided parameters and returns ().


```go
func getCNIURL(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/utils.go:96`



---


[function] name: getECRCredentialProviderURL file: test/e2e_node/remote/utils.go:135 returns_error: нет description: —


### getECRCredentialProviderURL (test/e2e_node/remote/utils.go:135)


getECRCredentialProviderURL is a function that performs operations based on the provided parameters and returns ().


```go
func getECRCredentialProviderURL(()) ()
```


📍 *Расположение:* `test/e2e_node/remote/utils.go:135`



---


[function] name: quote file: test/e2e_node/remote/utils.go:214 returns_error: нет description: Quotes a shell literal so it can be nested within another shell scope.


### quote (test/e2e_node/remote/utils.go:214)


Quotes a shell literal so it can be nested within another shell scope.


```go
func quote((s string)) (s string)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


📍 *Расположение:* `test/e2e_node/remote/utils.go:214`



---


[function] name: setupCNI file: test/e2e_node/remote/utils.go:108 returns_error: нет description: Install the cni plugin and add basic bridge configuration to the
configuration directory.


### setupCNI (test/e2e_node/remote/utils.go:108)


Install the cni plugin and add basic bridge configuration to the
configuration directory.


```go
func setupCNI((host, workspace string)) (host, workspace string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/utils.go:108`



---


[function] name: setupECRCredentialProvider file: test/e2e_node/remote/utils.go:143 returns_error: нет description: —


### setupECRCredentialProvider (test/e2e_node/remote/utils.go:143)


setupECRCredentialProvider is a function that performs operations based on the provided parameters and returns (host, workspace string).


```go
func setupECRCredentialProvider((host, workspace string)) (host, workspace string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


**Тип ответа:** workspace


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/remote/utils.go:143`




## test/e2e_node/resource_collector.go


📄 Исходный файл: `test/e2e_node/resource_collector.go`


<details open>
<summary><b>Функции в этом файле (21)</b></summary>


- 🔗 [GetBasicCPUStats](#getbasiccpustats-teste2e_noderesource_collectorgo212) `:212`

- 🔗 [GetCPUSummary](#getcpusummary-teste2e_noderesource_collectorgo132) `:132`

- 🔗 [GetLatest](#getlatest-teste2e_noderesource_collectorgo187) `:187`

- 🔗 [GetResourceTimeSeries](#getresourcetimeseries-teste2e_noderesource_collectorgo437) `:437`

- 🔗 [Len](#len-teste2e_noderesource_collectorgo203) `:203`

- 🔗 [Less](#less-teste2e_noderesource_collectorgo205) `:205`

- 🔗 [LogLatest](#loglatest-teste2e_noderesource_collectorgo142) `:142`

- 🔗 [NewResourceCollector](#newresourcecollector-teste2e_noderesource_collectorgo76) `:76`

- 🔗 [Reset](#reset-teste2e_noderesource_collectorgo123) `:123`

- 🔗 [Start](#start-teste2e_noderesource_collectorgo86) `:86`

- 🔗 [Stop](#stop-teste2e_noderesource_collectorgo118) `:118`

- 🔗 [Swap](#swap-teste2e_noderesource_collectorgo204) `:204`

- 🔗 [collectStats](#collectstats-teste2e_noderesource_collectorgo151) `:151`

- 🔗 [computeContainerResourceUsage](#computecontainerresourceusage-teste2e_noderesource_collectorgo174) `:174`

- 🔗 [deletePodsSync](#deletepodssync-teste2e_noderesource_collectorgo365) `:365`

- 🔗 [formatCPUSummary](#formatcpusummary-teste2e_noderesource_collectorgo252) `:252`

- 🔗 [formatResourceUsageStats](#formatresourceusagestats-teste2e_noderesource_collectorgo234) `:234`

- 🔗 [getCadvisorPod](#getcadvisorpod-teste2e_noderesource_collectorgo291) `:291`

- 🔗 [getContainer](#getcontainer-teste2e_noderesource_collectorgo474) `:474`

- 🔗 [getContainerNameForProcess](#getcontainernameforprocess-teste2e_noderesource_collectorgo456) `:456`

- 🔗 [newTestPods](#newtestpods-teste2e_noderesource_collectorgo382) `:382`


</details>


[function] name: GetBasicCPUStats file: test/e2e_node/resource_collector.go:212 returns_error: нет description: GetBasicCPUStats returns the percentiles the cpu usage in cores for
containerName. This method examines all data current


### GetBasicCPUStats (test/e2e_node/resource_collector.go:212)


GetBasicCPUStats returns the percentiles the cpu usage in cores for
containerName. This method examines all data currently in the buffer.


```go
func (r *ResourceCollector) GetBasicCPUStats((containerName string)) (containerName string)
```


**Тип ответа:** containerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/resource_collector.go:212`



---


[function] name: GetCPUSummary file: test/e2e_node/resource_collector.go:132 returns_error: нет description: GetCPUSummary gets CPU usage in percentile.


### GetCPUSummary (test/e2e_node/resource_collector.go:132)


GetCPUSummary gets CPU usage in percentile.


```go
func (r *ResourceCollector) GetCPUSummary(()) ()
```


📍 *Расположение:* `test/e2e_node/resource_collector.go:132`



---


[function] name: GetLatest file: test/e2e_node/resource_collector.go:187 returns_error: да description: GetLatest gets the latest resource usage from stats buffer.


### GetLatest (test/e2e_node/resource_collector.go:187)


GetLatest gets the latest resource usage from stats buffer.


```go
func (r *ResourceCollector) GetLatest((e2ekubelet.ResourceUsagePerContainer, error)) (e2ekubelet.ResourceUsagePerContainer, error)
```


**Тип ответа:** e2ekubelet.ResourceUsagePerContainer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `e2ekubelet.ResourceUsagePerContainer`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/resource_collector.go:187`



---


[function] name: GetResourceTimeSeries file: test/e2e_node/resource_collector.go:437 returns_error: нет description: GetResourceTimeSeries gets the time series of resource usage of each container.


### GetResourceTimeSeries (test/e2e_node/resource_collector.go:437)


GetResourceTimeSeries gets the time series of resource usage of each container.


```go
func (r *ResourceCollector) GetResourceTimeSeries(()) ()
```


📍 *Расположение:* `test/e2e_node/resource_collector.go:437`



---


[function] name: Len file: test/e2e_node/resource_collector.go:203 returns_error: нет description: —


### Len (test/e2e_node/resource_collector.go:203)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (r resourceUsageByCPU) Len(()) ()
```


📍 *Расположение:* `test/e2e_node/resource_collector.go:203`



---


[function] name: Less file: test/e2e_node/resource_collector.go:205 returns_error: нет description: —


### Less (test/e2e_node/resource_collector.go:205)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (r resourceUsageByCPU) Less((i, j int)) (i, j int)
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


📍 *Расположение:* `test/e2e_node/resource_collector.go:205`



---


[function] name: LogLatest file: test/e2e_node/resource_collector.go:142 returns_error: нет description: LogLatest logs the latest resource usage.


### LogLatest (test/e2e_node/resource_collector.go:142)


LogLatest logs the latest resource usage.


```go
func (r *ResourceCollector) LogLatest(()) ()
```


📍 *Расположение:* `test/e2e_node/resource_collector.go:142`



---


[function] name: NewResourceCollector file: test/e2e_node/resource_collector.go:76 returns_error: нет description: NewResourceCollector creates a resource collector object which collects
resource usage periodically from Cadvisor


### NewResourceCollector (test/e2e_node/resource_collector.go:76)


NewResourceCollector creates a resource collector object which collects
resource usage periodically from Cadvisor


```go
func NewResourceCollector((interval time.Duration)) (interval time.Duration)
```


**Тип ответа:** interval


```json
{
  "First": 0,
  "Last": 0
}
```


*Определено в:* `pkg/controller/job/indexed_job_utils.go`


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


📍 *Расположение:* `test/e2e_node/resource_collector.go:76`



---


[function] name: Reset file: test/e2e_node/resource_collector.go:123 returns_error: нет description: Reset clears the stats buffer of resource collector.


### Reset (test/e2e_node/resource_collector.go:123)


Reset clears the stats buffer of resource collector.


```go
func (r *ResourceCollector) Reset(()) ()
```


📍 *Расположение:* `test/e2e_node/resource_collector.go:123`



---


[function] name: Start file: test/e2e_node/resource_collector.go:86 returns_error: нет description: Start starts resource collector and connects to the standalone Cadvisor pod
then repeatedly runs collectStats.


### Start (test/e2e_node/resource_collector.go:86)


Start starts resource collector and connects to the standalone Cadvisor pod
then repeatedly runs collectStats.


```go
func (r *ResourceCollector) Start(()) ()
```


📍 *Расположение:* `test/e2e_node/resource_collector.go:86`



---


[function] name: Stop file: test/e2e_node/resource_collector.go:118 returns_error: нет description: Stop stops resource collector collecting stats. It does not clear the buffer


### Stop (test/e2e_node/resource_collector.go:118)


Stop stops resource collector collecting stats. It does not clear the buffer


```go
func (r *ResourceCollector) Stop(()) ()
```


📍 *Расположение:* `test/e2e_node/resource_collector.go:118`



---


[function] name: Swap file: test/e2e_node/resource_collector.go:204 returns_error: нет description: —


### Swap (test/e2e_node/resource_collector.go:204)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (r resourceUsageByCPU) Swap((i, j int)) (i, j int)
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


📍 *Расположение:* `test/e2e_node/resource_collector.go:204`



---


[function] name: collectStats file: test/e2e_node/resource_collector.go:151 returns_error: нет description: collectStats collects resource usage from Cadvisor.


### collectStats (test/e2e_node/resource_collector.go:151)


collectStats collects resource usage from Cadvisor.


```go
func (r *ResourceCollector) collectStats((oldStatsMap map[string]*cadvisorapiv2.ContainerStats)) (oldStatsMap map[string]*cadvisorapiv2.ContainerStats)
```


**Тип запроса:** cadvisorapiv2.ContainerStats


```json
{
  "Name": "string",
  "StartTime": {},
  "CPU": null,
  "Memory": null,
  "IO": null,
  "Accelerators": [],
  "Rootfs": null,
  "Logs": null,
  "userDefinedMetrics": [],
  "Swap": null
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/stats/v1alpha1/types.go`


**Тип ответа:** oldStatsMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** cadvisorapiv2.ContainerStats


```json
{
  "Name": "string",
  "StartTime": {},
  "CPU": null,
  "Memory": null,
  "IO": null,
  "Accelerators": [],
  "Rootfs": null,
  "Logs": null,
  "userDefinedMetrics": [],
  "Swap": null
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/stats/v1alpha1/types.go`


📍 *Расположение:* `test/e2e_node/resource_collector.go:151`



---


[function] name: computeContainerResourceUsage file: test/e2e_node/resource_collector.go:174 returns_error: нет description: computeContainerResourceUsage computes resource usage based on new data sample.


### computeContainerResourceUsage (test/e2e_node/resource_collector.go:174)


computeContainerResourceUsage computes resource usage based on new data sample.


```go
func computeContainerResourceUsage((name string, oldStats, newStats *cadvisorapiv2.ContainerStats)) (name string, oldStats, newStats *cadvisorapiv2.ContainerStats)
```


**Тип запроса:** cadvisorapiv2.ContainerStats


```json
{
  "Name": "string",
  "StartTime": {},
  "CPU": null,
  "Memory": null,
  "IO": null,
  "Accelerators": [],
  "Rootfs": null,
  "Logs": null,
  "userDefinedMetrics": [],
  "Swap": null
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/stats/v1alpha1/types.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** oldStats


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** newStats


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cadvisorapiv2.ContainerStats


```json
{
  "Name": "string",
  "StartTime": {},
  "CPU": null,
  "Memory": null,
  "IO": null,
  "Accelerators": [],
  "Rootfs": null,
  "Logs": null,
  "userDefinedMetrics": [],
  "Swap": null
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/stats/v1alpha1/types.go`


📍 *Расположение:* `test/e2e_node/resource_collector.go:174`



---


[function] name: deletePodsSync file: test/e2e_node/resource_collector.go:365 returns_error: нет description: deletePodsSync deletes a list of pods and block until pods disappear.


### deletePodsSync (test/e2e_node/resource_collector.go:365)


deletePodsSync deletes a list of pods and block until pods disappear.


```go
func deletePodsSync((ctx context.Context, f *framework.Framework, pods []*v1.Pod)) (ctx context.Context, f *framework.Framework, pods []*v1.Pod)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип запроса:** v1.Pod


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** pods


```json
{
  "pods": {},
  "mu": {}
}
```


*Определено в:* `pkg/scheduler/framework/runtime/pods_in_prebind_map.go`


**Тип ответа:** v1.Pod


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


📍 *Расположение:* `test/e2e_node/resource_collector.go:365`



---


[function] name: formatCPUSummary file: test/e2e_node/resource_collector.go:252 returns_error: нет description: —


### formatCPUSummary (test/e2e_node/resource_collector.go:252)


formatCPUSummary is a function that performs operations based on the provided parameters and returns (summary e2ekubelet.ContainersCPUSummary).


```go
func formatCPUSummary((summary e2ekubelet.ContainersCPUSummary)) (summary e2ekubelet.ContainersCPUSummary)
```


**Тип ответа:** summary


```json
{
  "kubeletCreationTime": {},
  "systemBootTime": {},
  "provider": {}
}
```


*Определено в:* `pkg/kubelet/server/stats/summary.go`


**Тип ответа:** e2ekubelet.ContainersCPUSummary


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/resource_collector.go:252`



---


[function] name: formatResourceUsageStats file: test/e2e_node/resource_collector.go:234 returns_error: нет description: —


### formatResourceUsageStats (test/e2e_node/resource_collector.go:234)


formatResourceUsageStats is a function that performs operations based on the provided parameters and returns (containerStats e2ekubelet.ResourceUsagePerContainer).


```go
func formatResourceUsageStats((containerStats e2ekubelet.ResourceUsagePerContainer)) (containerStats e2ekubelet.ResourceUsagePerContainer)
```


**Тип ответа:** containerStats


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** e2ekubelet.ResourceUsagePerContainer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/resource_collector.go:234`



---


[function] name: getCadvisorPod file: test/e2e_node/resource_collector.go:291 returns_error: нет description: createCadvisorPod creates a standalone cadvisor pod for fine-grain resource monitoring.


### getCadvisorPod (test/e2e_node/resource_collector.go:291)


createCadvisorPod creates a standalone cadvisor pod for fine-grain resource monitoring.


```go
func getCadvisorPod(()) ()
```


📍 *Расположение:* `test/e2e_node/resource_collector.go:291`



---


[function] name: getContainer file: test/e2e_node/resource_collector.go:474 returns_error: да description: getContainer returns the cgroup associated with the specified pid.
It enforces a unified hierarchy for memory and cpu cg


### getContainer (test/e2e_node/resource_collector.go:474)


getContainer returns the cgroup associated with the specified pid.
It enforces a unified hierarchy for memory and cpu cgroups.
On systemd environments, it uses the name=systemd cgroup for the specified pid.


```go
func getContainer((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/resource_collector.go:474`



---


[function] name: getContainerNameForProcess file: test/e2e_node/resource_collector.go:456 returns_error: да description: —


### getContainerNameForProcess (test/e2e_node/resource_collector.go:456)


getContainerNameForProcess is a function that performs operations based on the provided parameters and may return an error.


```go
func getContainerNameForProcess((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/resource_collector.go:456`



---


[function] name: newTestPods file: test/e2e_node/resource_collector.go:382 returns_error: нет description: newTestPods creates a list of pods (specification) for test.


### newTestPods (test/e2e_node/resource_collector.go:382)


newTestPods creates a list of pods (specification) for test.


```go
func newTestPods((numPods int, volume bool, imageName, podType string)) (numPods int, volume bool, imageName, podType string)
```


**Тип ответа:** numPods


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** volume


```json
{
  "factory": {},
  "tweakListOptions": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/storage/v1alpha1/volumeattributesclass.go`


**Тип ответа:** imageName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/resource_collector.go:382`




## test/e2e_node/runner/local/run_local.go


📄 Исходный файл: `test/e2e_node/runner/local/run_local.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [addGinkgoArgPrefix](#addginkgoargprefix-teste2e_noderunnerlocalrun_localgo106) `:106`

- 🔗 [main](#main-teste2e_noderunnerlocalrun_localgo44) `:44`

- 🔗 [runCommand](#runcommand-teste2e_noderunnerlocalrun_localgo120) `:120`


</details>


[function] name: addGinkgoArgPrefix file: test/e2e_node/runner/local/run_local.go:106 returns_error: нет description: —


### addGinkgoArgPrefix (test/e2e_node/runner/local/run_local.go:106)


addGinkgoArgPrefix is a function that performs operations based on the provided parameters and returns (ginkgoFlags string).


```go
func addGinkgoArgPrefix((ginkgoFlags string)) (ginkgoFlags string)
```


**Тип ответа:** ginkgoFlags


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/runner/local/run_local.go:106`



---


[function] name: main file: test/e2e_node/runner/local/run_local.go:44 returns_error: нет description: —


### main (test/e2e_node/runner/local/run_local.go:44)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/e2e_node/runner/local/run_local.go:44`



---


[function] name: runCommand file: test/e2e_node/runner/local/run_local.go:120 returns_error: нет description: —


### runCommand (test/e2e_node/runner/local/run_local.go:120)


runCommand is a function that performs operations based on the provided parameters and returns (interactive bool, name string, args ...string).


```go
func runCommand((interactive bool, name string, args ...string)) (interactive bool, name string, args ...string)
```


**Тип ответа:** interactive


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/runner/local/run_local.go:120`




## test/e2e_node/runner/remote/run_remote.go


📄 Исходный файл: `test/e2e_node/runner/remote/run_remote.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [main](#main-teste2e_noderunnerremoterun_remotego40) `:40`


</details>


[function] name: main file: test/e2e_node/runner/remote/run_remote.go:40 returns_error: нет description: —


### main (test/e2e_node/runner/remote/run_remote.go:40)


main is a function that performs operations based on the provided parameters and returns ().


```go
func main(()) ()
```


📍 *Расположение:* `test/e2e_node/runner/remote/run_remote.go:40`




## test/e2e_node/services/apiserver.go


📄 Исходный файл: `test/e2e_node/services/apiserver.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [Name](#name-teste2e_nodeservicesapiservergo141) `:141`

- 🔗 [NewAPIServer](#newapiserver-teste2e_nodeservicesapiservergo54) `:54`

- 🔗 [Start](#start-teste2e_nodeservicesapiservergo63) `:63`

- 🔗 [Stop](#stop-teste2e_nodeservicesapiservergo130) `:130`

- 🔗 [generateTokenFile](#generatetokenfile-teste2e_nodeservicesapiservergo153) `:153`

- 🔗 [getAPIServerClientURL](#getapiserverclienturl-teste2e_nodeservicesapiservergo145) `:145`

- 🔗 [getAPIServerHealthCheckURL](#getapiserverhealthcheckurl-teste2e_nodeservicesapiservergo149) `:149`


</details>


[function] name: Name file: test/e2e_node/services/apiserver.go:141 returns_error: нет description: Name returns the name of APIServer.


### Name (test/e2e_node/services/apiserver.go:141)


Name returns the name of APIServer.


```go
func (a *APIServer) Name(()) ()
```


📍 *Расположение:* `test/e2e_node/services/apiserver.go:141`



---


[function] name: NewAPIServer file: test/e2e_node/services/apiserver.go:54 returns_error: нет description: NewAPIServer creates an apiserver.


### NewAPIServer (test/e2e_node/services/apiserver.go:54)


NewAPIServer creates an apiserver.


```go
func NewAPIServer((storageConfig storagebackend.Config)) (storageConfig storagebackend.Config)
```


**Тип ответа:** storageConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** storagebackend.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/e2e_node/services/apiserver.go:54`



---


[function] name: Start file: test/e2e_node/services/apiserver.go:63 returns_error: нет description: Start starts the apiserver, returns when apiserver is ready.
The background goroutine runs until the context is canceled


### Start (test/e2e_node/services/apiserver.go:63)


Start starts the apiserver, returns when apiserver is ready.
The background goroutine runs until the context is canceled
or Stop is called, whether happens first.


```go
func (a *APIServer) Start((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/e2e_node/services/apiserver.go:63`



---


[function] name: Stop file: test/e2e_node/services/apiserver.go:130 returns_error: нет description: Stop stops the apiserver. Does not block.


### Stop (test/e2e_node/services/apiserver.go:130)


Stop stops the apiserver. Does not block.


```go
func (a *APIServer) Stop(()) ()
```


📍 *Расположение:* `test/e2e_node/services/apiserver.go:130`



---


[function] name: generateTokenFile file: test/e2e_node/services/apiserver.go:153 returns_error: нет description: —


### generateTokenFile (test/e2e_node/services/apiserver.go:153)


generateTokenFile is a function that performs operations based on the provided parameters and returns (tokenFilePath string).


```go
func generateTokenFile((tokenFilePath string)) (tokenFilePath string)
```


**Тип ответа:** tokenFilePath


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/services/apiserver.go:153`



---


[function] name: getAPIServerClientURL file: test/e2e_node/services/apiserver.go:145 returns_error: нет description: —


### getAPIServerClientURL (test/e2e_node/services/apiserver.go:145)


getAPIServerClientURL is a function that performs operations based on the provided parameters and returns ().


```go
func getAPIServerClientURL(()) ()
```


📍 *Расположение:* `test/e2e_node/services/apiserver.go:145`



---


[function] name: getAPIServerHealthCheckURL file: test/e2e_node/services/apiserver.go:149 returns_error: нет description: —


### getAPIServerHealthCheckURL (test/e2e_node/services/apiserver.go:149)


getAPIServerHealthCheckURL is a function that performs operations based on the provided parameters and returns ().


```go
func getAPIServerHealthCheckURL(()) ()
```


📍 *Расположение:* `test/e2e_node/services/apiserver.go:149`




## test/e2e_node/services/internal_services.go


📄 Исходный файл: `test/e2e_node/services/internal_services.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [SetFeatureGatesForInProcessComponents](#setfeaturegatesforinprocesscomponents-teste2e_nodeservicesinternal_servicesgo144) `:144`

- 🔗 [getServicesHealthCheckURLs](#getserviceshealthcheckurls-teste2e_nodeservicesinternal_servicesgo138) `:138`

- 🔗 [newE2EServices](#newe2eservices-teste2e_nodeservicesinternal_servicesgo43) `:43`

- 🔗 [run](#run-teste2e_nodeservicesinternal_servicesgo49) `:49`

- 🔗 [start](#start-teste2e_nodeservicesinternal_servicesgo60) `:60`

- 🔗 [startAPIServer](#startapiserver-teste2e_nodeservicesinternal_servicesgo124) `:124`

- 🔗 [startEtcd](#startetcd-teste2e_nodeservicesinternal_servicesgo115) `:115`

- 🔗 [startNamespaceController](#startnamespacecontroller-teste2e_nodeservicesinternal_servicesgo131) `:131`

- 🔗 [stop](#stop-teste2e_nodeservicesinternal_servicesgo80) `:80`


</details>


[function] name: SetFeatureGatesForInProcessComponents file: test/e2e_node/services/internal_services.go:144 returns_error: нет description: —


### SetFeatureGatesForInProcessComponents (test/e2e_node/services/internal_services.go:144)


SetFeatureGatesForInProcessComponents is a function that updates data based on the provided parameters and returns (featureGates map[string]bool).


```go
func SetFeatureGatesForInProcessComponents((featureGates map[string]bool)) (featureGates map[string]bool)
```


**Тип ответа:** featureGates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/e2e_node/services/internal_services.go:144`



---


[function] name: getServicesHealthCheckURLs file: test/e2e_node/services/internal_services.go:138 returns_error: нет description: getServicesHealthCheckURLs returns the health check urls for the internal services.


### getServicesHealthCheckURLs (test/e2e_node/services/internal_services.go:138)


getServicesHealthCheckURLs returns the health check urls for the internal services.


```go
func getServicesHealthCheckURLs(()) ()
```


📍 *Расположение:* `test/e2e_node/services/internal_services.go:138`



---


[function] name: newE2EServices file: test/e2e_node/services/internal_services.go:43 returns_error: нет description: —


### newE2EServices (test/e2e_node/services/internal_services.go:43)


newE2EServices is a function that performs operations based on the provided parameters and returns ().


```go
func newE2EServices(()) ()
```


📍 *Расположение:* `test/e2e_node/services/internal_services.go:43`



---


[function] name: run file: test/e2e_node/services/internal_services.go:49 returns_error: нет description: run starts all e2e services and wait for the termination signal. Once receives the
termination signal, it will stop the 


### run (test/e2e_node/services/internal_services.go:49)


run starts all e2e services and wait for the termination signal. Once receives the
termination signal, it will stop the e2e services gracefully.


```go
func (es *e2eServices) run((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/e2e_node/services/internal_services.go:49`



---


[function] name: start file: test/e2e_node/services/internal_services.go:60 returns_error: нет description: start starts the tests embedded services or returns an error.


### start (test/e2e_node/services/internal_services.go:60)


start starts the tests embedded services or returns an error.


```go
func (es *e2eServices) start((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/e2e_node/services/internal_services.go:60`



---


[function] name: startAPIServer file: test/e2e_node/services/internal_services.go:124 returns_error: нет description: startAPIServer starts the embedded API server or returns an error.


### startAPIServer (test/e2e_node/services/internal_services.go:124)


startAPIServer starts the embedded API server or returns an error.


```go
func (es *e2eServices) startAPIServer((ctx context.Context, etcdStorage *storagebackend.Config)) (ctx context.Context, etcdStorage *storagebackend.Config)
```


**Тип запроса:** storagebackend.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


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


**Тип ответа:** etcdStorage


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** storagebackend.Config


```json
{
  "Proxy": {},
  "Services": {}
}
```


*Определено в:* `pkg/registry/core/rest/storage_core.go`


📍 *Расположение:* `test/e2e_node/services/internal_services.go:124`



---


[function] name: startEtcd file: test/e2e_node/services/internal_services.go:115 returns_error: нет description: startEtcd starts the embedded etcd instance or returns an error.


### startEtcd (test/e2e_node/services/internal_services.go:115)


startEtcd starts the embedded etcd instance or returns an error.


```go
func (es *e2eServices) startEtcd((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/e2e_node/services/internal_services.go:115`



---


[function] name: startNamespaceController file: test/e2e_node/services/internal_services.go:131 returns_error: нет description: startNamespaceController starts the embedded namespace controller or returns an error.


### startNamespaceController (test/e2e_node/services/internal_services.go:131)


startNamespaceController starts the embedded namespace controller or returns an error.


```go
func (es *e2eServices) startNamespaceController((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/e2e_node/services/internal_services.go:131`



---


[function] name: stop file: test/e2e_node/services/internal_services.go:80 returns_error: нет description: stop stops the embedded e2e services.


### stop (test/e2e_node/services/internal_services.go:80)


stop stops the embedded e2e services.


```go
func (es *e2eServices) stop((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/e2e_node/services/internal_services.go:80`




## test/e2e_node/services/kubelet.go


📄 Исходный файл: `test/e2e_node/services/kubelet.go`


<details open>
<summary><b>Функции в этом файле (15)</b></summary>


- 🔗 [KubeletConfigDirCWDDir](#kubeletconfigdircwddir-teste2e_nodeserviceskubeletgo421) `:421`

- 🔗 [RunKubelet](#runkubelet-teste2e_nodeserviceskubeletgo78) `:78`

- 🔗 [Set](#set-teste2e_nodeserviceskubeletgo58) `:58`

- 🔗 [String](#string-teste2e_nodeserviceskubeletgo53) `:53`

- 🔗 [WriteKubeletConfigFile](#writekubeletconfigfile-teste2e_nodeserviceskubeletgo338) `:338`

- 🔗 [adjustArgsForSystemd](#adjustargsforsystemd-teste2e_nodeserviceskubeletgo449) `:449`

- 🔗 [baseKubeConfiguration](#basekubeconfiguration-teste2e_nodeserviceskubeletgo100) `:100`

- 🔗 [createKubeconfig](#createkubeconfig-teste2e_nodeserviceskubeletgo369) `:369`

- 🔗 [createKubeconfigCWD](#createkubeconfigcwd-teste2e_nodeserviceskubeletgo435) `:435`

- 🔗 [createPodDirectory](#createpoddirectory-teste2e_nodeserviceskubeletgo356) `:356`

- 🔗 [createRootDirectory](#createrootdirectory-teste2e_nodeserviceskubeletgo394) `:394`

- 🔗 [init](#init-teste2e_nodeserviceskubeletgo69) `:69`

- 🔗 [kubeconfigCWDPath](#kubeconfigcwdpath-teste2e_nodeserviceskubeletgo404) `:404`

- 🔗 [kubeletConfigCWDPath](#kubeletconfigcwdpath-teste2e_nodeserviceskubeletgo412) `:412`

- 🔗 [startKubelet](#startkubelet-teste2e_nodeserviceskubeletgo156) `:156`


</details>


[function] name: KubeletConfigDirCWDDir file: test/e2e_node/services/kubelet.go:421 returns_error: да description: —


### KubeletConfigDirCWDDir (test/e2e_node/services/kubelet.go:421)


KubeletConfigDirCWDDir is a function that performs operations based on the provided parameters and may return an error.


```go
func KubeletConfigDirCWDDir((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/kubelet.go:421`



---


[function] name: RunKubelet file: test/e2e_node/services/kubelet.go:78 returns_error: нет description: RunKubelet starts kubelet and waits for termination signal. Once receives the
termination signal, it will stop the kubel


### RunKubelet (test/e2e_node/services/kubelet.go:78)


RunKubelet starts kubelet and waits for termination signal. Once receives the
termination signal, it will stop the kubelet gracefully.


```go
func RunKubelet((ctx context.Context, featureGates map[string]bool)) (ctx context.Context, featureGates map[string]bool)
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


**Тип ответа:** featureGates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/e2e_node/services/kubelet.go:78`



---


[function] name: Set file: test/e2e_node/services/kubelet.go:58 returns_error: нет description: Set function of flag.Value


### Set (test/e2e_node/services/kubelet.go:58)


Set function of flag.Value


```go
func (a *args) Set((value string)) (value string)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `test/e2e_node/services/kubelet.go:58`



---


[function] name: String file: test/e2e_node/services/kubelet.go:53 returns_error: нет description: String function of flag.Value


### String (test/e2e_node/services/kubelet.go:53)


String function of flag.Value


```go
func (a *args) String(()) ()
```


📍 *Расположение:* `test/e2e_node/services/kubelet.go:53`



---


[function] name: WriteKubeletConfigFile file: test/e2e_node/services/kubelet.go:338 returns_error: нет description: WriteKubeletConfigFile writes the kubelet config file based on the args and returns the filename


### WriteKubeletConfigFile (test/e2e_node/services/kubelet.go:338)


WriteKubeletConfigFile writes the kubelet config file based on the args and returns the filename


```go
func WriteKubeletConfigFile((internal *kubeletconfig.KubeletConfiguration, path string)) (internal *kubeletconfig.KubeletConfiguration, path string)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** internal


```json
{
  "devices": []
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/structured/internal/experimental/allocator_experimental.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


📍 *Расположение:* `test/e2e_node/services/kubelet.go:338`



---


[function] name: adjustArgsForSystemd file: test/e2e_node/services/kubelet.go:449 returns_error: нет description: adjustArgsForSystemd escape special characters in kubelet arguments for systemd. Systemd
may try to do auto expansion wi


### adjustArgsForSystemd (test/e2e_node/services/kubelet.go:449)


adjustArgsForSystemd escape special characters in kubelet arguments for systemd. Systemd
may try to do auto expansion without escaping.


```go
func adjustArgsForSystemd((args []string)) (args []string)
```


**Тип ответа:** args


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/services/kubelet.go:449`



---


[function] name: baseKubeConfiguration file: test/e2e_node/services/kubelet.go:100 returns_error: да description: —


### baseKubeConfiguration (test/e2e_node/services/kubelet.go:100)


baseKubeConfiguration is a function that performs operations based on the provided parameters and may return an error.


```go
func baseKubeConfiguration((*kubeletconfig.KubeletConfiguration, error)) (*kubeletconfig.KubeletConfiguration, error)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfig.KubeletConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/kubelet.go:100`



---


[function] name: createKubeconfig file: test/e2e_node/services/kubelet.go:369 returns_error: нет description: createKubeconfig creates a kubeconfig file at the fully qualified `path`. The parent dirs must exist.


### createKubeconfig (test/e2e_node/services/kubelet.go:369)


createKubeconfig creates a kubeconfig file at the fully qualified `path`. The parent dirs must exist.


```go
func createKubeconfig((path string)) (path string)
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


📍 *Расположение:* `test/e2e_node/services/kubelet.go:369`



---


[function] name: createKubeconfigCWD file: test/e2e_node/services/kubelet.go:435 returns_error: да description: like createKubeconfig, but creates kubeconfig at current-working-directory/kubeconfig
returns a fully-qualified path to 


### createKubeconfigCWD (test/e2e_node/services/kubelet.go:435)


like createKubeconfig, but creates kubeconfig at current-working-directory/kubeconfig
returns a fully-qualified path to the kubeconfig file


```go
func createKubeconfigCWD((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/kubelet.go:435`



---


[function] name: createPodDirectory file: test/e2e_node/services/kubelet.go:356 returns_error: да description: createPodDirectory creates pod directory.


### createPodDirectory (test/e2e_node/services/kubelet.go:356)


createPodDirectory creates pod directory.


```go
func createPodDirectory((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/kubelet.go:356`



---


[function] name: createRootDirectory file: test/e2e_node/services/kubelet.go:394 returns_error: нет description: —


### createRootDirectory (test/e2e_node/services/kubelet.go:394)


createRootDirectory is a function that performs operations based on the provided parameters and returns (path string).


```go
func createRootDirectory((path string)) (path string)
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


📍 *Расположение:* `test/e2e_node/services/kubelet.go:394`



---


[function] name: init file: test/e2e_node/services/kubelet.go:69 returns_error: нет description: —


### init (test/e2e_node/services/kubelet.go:69)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/services/kubelet.go:69`



---


[function] name: kubeconfigCWDPath file: test/e2e_node/services/kubelet.go:404 returns_error: да description: —


### kubeconfigCWDPath (test/e2e_node/services/kubelet.go:404)


kubeconfigCWDPath is a function that performs operations based on the provided parameters and may return an error.


```go
func kubeconfigCWDPath((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/kubelet.go:404`



---


[function] name: kubeletConfigCWDPath file: test/e2e_node/services/kubelet.go:412 returns_error: да description: —


### kubeletConfigCWDPath (test/e2e_node/services/kubelet.go:412)


kubeletConfigCWDPath is a function that performs operations based on the provided parameters and may return an error.


```go
func kubeletConfigCWDPath((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/kubelet.go:412`



---


[function] name: startKubelet file: test/e2e_node/services/kubelet.go:156 returns_error: да description: startKubelet starts the Kubelet in a separate process or returns an error
if the Kubelet fails to start.


### startKubelet (test/e2e_node/services/kubelet.go:156)


startKubelet starts the Kubelet in a separate process or returns an error
if the Kubelet fails to start.


```go
func (e *E2EServices) startKubelet((*server, error)) (*server, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*server`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/kubelet.go:156`




## test/e2e_node/services/logs.go


📄 Исходный файл: `test/e2e_node/services/logs.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Set](#set-teste2e_nodeserviceslogsgo46) `:46`

- 🔗 [String](#string-teste2e_nodeserviceslogsgo41) `:41`

- 🔗 [getLogFiles](#getlogfiles-teste2e_nodeserviceslogsgo88) `:88`

- 🔗 [init](#init-teste2e_nodeserviceslogsgo60) `:60`


</details>


[function] name: Set file: test/e2e_node/services/logs.go:46 returns_error: нет description: Set function of flag.Value


### Set (test/e2e_node/services/logs.go:46)


Set function of flag.Value


```go
func (l *logFiles) Set((value string)) (value string)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `test/e2e_node/services/logs.go:46`



---


[function] name: String file: test/e2e_node/services/logs.go:41 returns_error: нет description: String function of flag.Value


### String (test/e2e_node/services/logs.go:41)


String function of flag.Value


```go
func (l *logFiles) String(()) ()
```


📍 *Расположение:* `test/e2e_node/services/logs.go:41`



---


[function] name: getLogFiles file: test/e2e_node/services/logs.go:88 returns_error: нет description: getLogFiles get all logs to collect after the test.


### getLogFiles (test/e2e_node/services/logs.go:88)


getLogFiles get all logs to collect after the test.


```go
func getLogFiles(()) ()
```


📍 *Расположение:* `test/e2e_node/services/logs.go:88`



---


[function] name: init file: test/e2e_node/services/logs.go:60 returns_error: нет description: —


### init (test/e2e_node/services/logs.go:60)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `test/e2e_node/services/logs.go:60`




## test/e2e_node/services/namespace_controller.go


📄 Исходный файл: `test/e2e_node/services/namespace_controller.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [Name](#name-teste2e_nodeservicesnamespace_controllergo97) `:97`

- 🔗 [NewNamespaceController](#newnamespacecontroller-teste2e_nodeservicesnamespace_controllergo48) `:48`

- 🔗 [Start](#start-teste2e_nodeservicesnamespace_controllergo53) `:53`

- 🔗 [Stop](#stop-teste2e_nodeservicesnamespace_controllergo91) `:91`


</details>


[function] name: Name file: test/e2e_node/services/namespace_controller.go:97 returns_error: нет description: Name returns the name of namespace controller.


### Name (test/e2e_node/services/namespace_controller.go:97)


Name returns the name of namespace controller.


```go
func (n *NamespaceController) Name(()) ()
```


📍 *Расположение:* `test/e2e_node/services/namespace_controller.go:97`



---


[function] name: NewNamespaceController file: test/e2e_node/services/namespace_controller.go:48 returns_error: нет description: NewNamespaceController creates a new namespace controller.


### NewNamespaceController (test/e2e_node/services/namespace_controller.go:48)


NewNamespaceController creates a new namespace controller.


```go
func NewNamespaceController((host string)) (host string)
```


**Тип ответа:** host


```json
{
  "driverInfo": {},
  "manifests": [],
  "volumeAttributes": []
}
```


*Определено в:* `test/e2e/storage/drivers/csi.go`


📍 *Расположение:* `test/e2e_node/services/namespace_controller.go:48`



---


[function] name: Start file: test/e2e_node/services/namespace_controller.go:53 returns_error: нет description: Start starts the namespace controller.


### Start (test/e2e_node/services/namespace_controller.go:53)


Start starts the namespace controller.


```go
func (n *NamespaceController) Start((ctx context.Context)) (ctx context.Context)
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


📍 *Расположение:* `test/e2e_node/services/namespace_controller.go:53`



---


[function] name: Stop file: test/e2e_node/services/namespace_controller.go:91 returns_error: нет description: Stop stops the namespace controller.


### Stop (test/e2e_node/services/namespace_controller.go:91)


Stop stops the namespace controller.


```go
func (n *NamespaceController) Stop(()) ()
```


📍 *Расположение:* `test/e2e_node/services/namespace_controller.go:91`




## test/e2e_node/services/server.go


📄 Исходный файл: `test/e2e_node/services/server.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [String](#string-teste2e_nodeservicesservergo95) `:95`

- 🔗 [commandToString](#commandtostring-teste2e_nodeservicesservergo88) `:88`

- 🔗 [kill](#kill-teste2e_nodeservicesservergo259) `:259`

- 🔗 [newServer](#newserver-teste2e_nodeservicesservergo73) `:73`

- 🔗 [start](#start-teste2e_nodeservicesservergo104) `:104`

- 🔗 [stopUnit](#stopunit-teste2e_nodeservicesservergo320) `:320`


</details>


[function] name: String file: test/e2e_node/services/server.go:95 returns_error: нет description: —


### String (test/e2e_node/services/server.go:95)


String is a method that performs operations based on the provided parameters and returns ().


```go
func (s *server) String(()) ()
```


📍 *Расположение:* `test/e2e_node/services/server.go:95`



---


[function] name: commandToString file: test/e2e_node/services/server.go:88 returns_error: нет description: commandToString format command to string.


### commandToString (test/e2e_node/services/server.go:88)


commandToString format command to string.


```go
func commandToString((c *exec.Cmd)) (c *exec.Cmd)
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


📍 *Расположение:* `test/e2e_node/services/server.go:88`



---


[function] name: kill file: test/e2e_node/services/server.go:259 returns_error: нет description: kill runs the server's kill command.


### kill (test/e2e_node/services/server.go:259)


kill runs the server's kill command.


```go
func (s *server) kill(()) ()
```


📍 *Расположение:* `test/e2e_node/services/server.go:259`



---


[function] name: newServer file: test/e2e_node/services/server.go:73 returns_error: нет description: newServer returns a new server with the given name, commands, health check
URLs, etc.


### newServer (test/e2e_node/services/server.go:73)


newServer returns a new server with the given name, commands, health check
URLs, etc.


```go
func newServer((name string, start, kill, restart *exec.Cmd, urls []string, outputFileName string, monitorParent, restartOnExit bool, systemdUnitName string)) (name string, start, kill, restart *exec.Cmd, urls []string, outputFileName string, monitorParent, restartOnExit bool, systemdUnitName string)
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


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** start


```json
{
  "Action": null,
  "ExitCodes": null
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/core/v1/containerrestartrule.go`


**Тип ответа:** kill


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** restart


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** urls


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** outputFileName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** monitorParent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** restartOnExit


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** systemdUnitName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/services/server.go:73`



---


[function] name: start file: test/e2e_node/services/server.go:104 returns_error: нет description: start starts the server by running its commands, monitors it with a health
check, and ensures that it is restarted if ap


### start (test/e2e_node/services/server.go:104)


start starts the server by running its commands, monitors it with a health
check, and ensures that it is restarted if applicable.

Note: restartOnExit == true requires len(s.healthCheckUrls) > 0 to work properly.


```go
func (s *server) start(()) ()
```


📍 *Расположение:* `test/e2e_node/services/server.go:104`



---


[function] name: stopUnit file: test/e2e_node/services/server.go:320 returns_error: нет description: —


### stopUnit (test/e2e_node/services/server.go:320)


stopUnit is a method that performs operations based on the provided parameters and returns ().


```go
func (s *server) stopUnit(()) ()
```


📍 *Расположение:* `test/e2e_node/services/server.go:320`




## test/e2e_node/services/services.go


📄 Исходный файл: `test/e2e_node/services/services.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [NewE2EServices](#newe2eservices-teste2e_nodeservicesservicesgo45) `:45`

- 🔗 [RunE2EServices](#rune2eservices-teste2e_nodeservicesservicesgo116) `:116`

- 🔗 [Start](#start-teste2e_nodeservicesservicesgo64) `:64`

- 🔗 [Stop](#stop-teste2e_nodeservicesservicesgo85) `:85`

- 🔗 [collectLogFiles](#collectlogfiles-teste2e_nodeservicesservicesgo149) `:149`

- 🔗 [copyLogFile](#copylogfile-teste2e_nodeservicesservicesgo195) `:195`

- 🔗 [isJournaldAvailable](#isjournaldavailable-teste2e_nodeservicesservicesgo190) `:190`

- 🔗 [startInternalServices](#startinternalservices-teste2e_nodeservicesservicesgo131) `:131`


</details>


[function] name: NewE2EServices file: test/e2e_node/services/services.go:45 returns_error: нет description: NewE2EServices returns a new E2EServices instance.


### NewE2EServices (test/e2e_node/services/services.go:45)


NewE2EServices returns a new E2EServices instance.


```go
func NewE2EServices((monitorParent bool)) (monitorParent bool)
```


**Тип ответа:** monitorParent


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/services/services.go:45`



---


[function] name: RunE2EServices file: test/e2e_node/services/services.go:116 returns_error: нет description: RunE2EServices actually start the e2e services. This function is used to
start e2e services in current process. This is 


### RunE2EServices (test/e2e_node/services/services.go:116)


RunE2EServices actually start the e2e services. This function is used to
start e2e services in current process. This is only used in run-services-mode.


```go
func RunE2EServices((t *testing.T)) (t *testing.T)
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


📍 *Расположение:* `test/e2e_node/services/services.go:116`



---


[function] name: Start file: test/e2e_node/services/services.go:64 returns_error: нет description: Start starts the e2e services in another process by calling back into the
test binary.  Returns when all e2e services ar


### Start (test/e2e_node/services/services.go:64)


Start starts the e2e services in another process by calling back into the
test binary.  Returns when all e2e services are ready or an error.

We want to statically link e2e services into the test binary, but we don't
want their glog output to pollute the test result. So we run the binary in
run-services-mode to start e2e services in another process.
The function starts 2 processes:
* internal e2e services: services which statically linked in the test binary - apiserver, etcd and
namespace controller.
* kubelet: kubelet binary is outside. (We plan to move main kubelet start logic out when we have
standard kubelet launcher)


```go
func (e *E2EServices) Start((ctx context.Context, featureGates map[string]bool)) (ctx context.Context, featureGates map[string]bool)
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


**Тип ответа:** featureGates


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


📍 *Расположение:* `test/e2e_node/services/services.go:64`



---


[function] name: Stop file: test/e2e_node/services/services.go:85 returns_error: нет description: Stop stops the e2e services.


### Stop (test/e2e_node/services/services.go:85)


Stop stops the e2e services.


```go
func (e *E2EServices) Stop(()) ()
```


📍 *Расположение:* `test/e2e_node/services/services.go:85`



---


[function] name: collectLogFiles file: test/e2e_node/services/services.go:149 returns_error: нет description: collectLogFiles collects logs of interest either via journalctl or by creating sym
links. Since we scp files from the re


### collectLogFiles (test/e2e_node/services/services.go:149)


collectLogFiles collects logs of interest either via journalctl or by creating sym
links. Since we scp files from the remote directory, symlinks will be
treated as normal files and file contents will be copied over.


```go
func (e *E2EServices) collectLogFiles(()) ()
```


📍 *Расположение:* `test/e2e_node/services/services.go:149`



---


[function] name: copyLogFile file: test/e2e_node/services/services.go:195 returns_error: нет description: —


### copyLogFile (test/e2e_node/services/services.go:195)


copyLogFile is a function that performs operations based on the provided parameters and returns (src, target string).


```go
func copyLogFile((src, target string)) (src, target string)
```


**Тип ответа:** src


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** target


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/services/services.go:195`



---


[function] name: isJournaldAvailable file: test/e2e_node/services/services.go:190 returns_error: нет description: isJournaldAvailable returns whether the system executing the tests uses
journald.


### isJournaldAvailable (test/e2e_node/services/services.go:190)


isJournaldAvailable returns whether the system executing the tests uses
journald.


```go
func isJournaldAvailable(()) ()
```


📍 *Расположение:* `test/e2e_node/services/services.go:190`



---


[function] name: startInternalServices file: test/e2e_node/services/services.go:131 returns_error: да description: startInternalServices starts the internal services in a separate process.


### startInternalServices (test/e2e_node/services/services.go:131)


startInternalServices starts the internal services in a separate process.


```go
func (e *E2EServices) startInternalServices((*server, error)) (*server, error)
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


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*server`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/services.go:131`




## test/e2e_node/services/util.go


📄 Исходный файл: `test/e2e_node/services/util.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [healthCheck](#healthcheck-teste2e_nodeservicesutilgo96) `:96`

- 🔗 [readinessCheck](#readinesscheck-teste2e_nodeservicesutilgo47) `:47`

- 🔗 [waitForTerminationSignal](#waitforterminationsignal-teste2e_nodeservicesutilgo38) `:38`


</details>


[function] name: healthCheck file: test/e2e_node/services/util.go:96 returns_error: нет description: Perform a health check. Anything other than a 200-response is treated as a failure.
Only returns non-recoverable errors.


### healthCheck (test/e2e_node/services/util.go:96)


Perform a health check. Anything other than a 200-response is treated as a failure.
Only returns non-recoverable errors.


```go
func healthCheck((client *http.Client, url string)) (client *http.Client, url string)
```


**Тип запроса:** http.Client


```json
{
  "clientSet": {},
  "useAPI": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/client/client.go`


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


**Тип ответа:** http.Client


```json
{
  "clientSet": {},
  "useAPI": {}
}
```


*Определено в:* `staging/src/k8s.io/dynamic-resource-allocation/client/client.go`


**Тип ответа:** url


```json
{
  "baseURL": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


📍 *Расположение:* `test/e2e_node/services/util.go:96`



---


[function] name: readinessCheck file: test/e2e_node/services/util.go:47 returns_error: да description: readinessCheck checks whether services are ready via the supplied health
check URLs. Once there is an error in errCh, th


### readinessCheck (test/e2e_node/services/util.go:47)


readinessCheck checks whether services are ready via the supplied health
check URLs. Once there is an error in errCh, the function will stop waiting
and return the error.


```go
func readinessCheck((name string, urls []string, errCh <-chan error)) (name string, urls []string, errCh <-chan error)
```


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** urls


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** errCh


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** chan


```json
{
  "stopCh": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/util/wait/wait.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `name string`, `urls []string`, `errCh <-chan error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/services/util.go:47`



---


[function] name: waitForTerminationSignal file: test/e2e_node/services/util.go:38 returns_error: нет description: waitForTerminationSignal waits for termination signal.


### waitForTerminationSignal (test/e2e_node/services/util.go:38)


waitForTerminationSignal waits for termination signal.


```go
func waitForTerminationSignal(()) ()
```


📍 *Расположение:* `test/e2e_node/services/util.go:38`




## test/e2e_node/testdeviceplugin/device-plugin.go


📄 Исходный файл: `test/e2e_node/testdeviceplugin/device-plugin.go`


<details open>
<summary><b>Функции в этом файле (12)</b></summary>


- 🔗 [Allocate](#allocate-teste2e_nodetestdeviceplugindevice-plugingo119) `:119`

- 🔗 [Calls](#calls-teste2e_nodetestdeviceplugindevice-plugingo223) `:223`

- 🔗 [GetDevicePluginOptions](#getdevicepluginoptions-teste2e_nodetestdeviceplugindevice-plugingo59) `:59`

- 🔗 [GetPreferredAllocation](#getpreferredallocation-teste2e_nodetestdeviceplugindevice-plugingo147) `:147`

- 🔗 [ListAndWatch](#listandwatch-teste2e_nodetestdeviceplugindevice-plugingo83) `:83`

- 🔗 [NewDevicePlugin](#newdeviceplugin-teste2e_nodetestdeviceplugindevice-plugingo51) `:51`

- 🔗 [PreStartContainer](#prestartcontainer-teste2e_nodetestdeviceplugindevice-plugingo143) `:143`

- 🔗 [RegisterDevicePlugin](#registerdeviceplugin-teste2e_nodetestdeviceplugindevice-plugingo151) `:151`

- 🔗 [Stop](#stop-teste2e_nodetestdeviceplugindevice-plugingo204) `:204`

- 🔗 [UpdateDevices](#updatedevices-teste2e_nodetestdeviceplugindevice-plugingo233) `:233`

- 🔗 [WasCalled](#wascalled-teste2e_nodetestdeviceplugindevice-plugingo211) `:211`

- 🔗 [sendDevices](#senddevices-teste2e_nodetestdeviceplugindevice-plugingo71) `:71`


</details>


[function] name: Allocate file: test/e2e_node/testdeviceplugin/device-plugin.go:119 returns_error: да description: —


### Allocate (test/e2e_node/testdeviceplugin/device-plugin.go:119)


Allocate is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DevicePlugin) Allocate((*kubeletdevicepluginv1beta1.AllocateResponse, error)) (*kubeletdevicepluginv1beta1.AllocateResponse, error)
```


**Тип запроса:** kubeletdevicepluginv1beta1.AllocateResponse


```json
{
  "state": {},
  "containerResponses": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Тип ответа:** kubeletdevicepluginv1beta1.AllocateResponse


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


*Типы возврата:* `*kubeletdevicepluginv1beta1.AllocateResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:119`



---


[function] name: Calls file: test/e2e_node/testdeviceplugin/device-plugin.go:223 returns_error: нет description: —


### Calls (test/e2e_node/testdeviceplugin/device-plugin.go:223)


Calls is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DevicePlugin) Calls(()) ()
```


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:223`



---


[function] name: GetDevicePluginOptions file: test/e2e_node/testdeviceplugin/device-plugin.go:59 returns_error: да description: —


### GetDevicePluginOptions (test/e2e_node/testdeviceplugin/device-plugin.go:59)


GetDevicePluginOptions is a method that retrieves data based on the provided parameters and may return an error.


```go
func (dp *DevicePlugin) GetDevicePluginOptions((*kubeletdevicepluginv1beta1.DevicePluginOptions, error)) (*kubeletdevicepluginv1beta1.DevicePluginOptions, error)
```


**Тип запроса:** kubeletdevicepluginv1beta1.DevicePluginOptions


```json
{
  "state": {},
  "preStartRequired": false,
  "getPreferredAllocationAvailable": false,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Тип ответа:** kubeletdevicepluginv1beta1.DevicePluginOptions


```json
{
  "state": {},
  "preStartRequired": false,
  "getPreferredAllocationAvailable": false,
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletdevicepluginv1beta1.DevicePluginOptions`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:59`



---


[function] name: GetPreferredAllocation file: test/e2e_node/testdeviceplugin/device-plugin.go:147 returns_error: да description: —


### GetPreferredAllocation (test/e2e_node/testdeviceplugin/device-plugin.go:147)


GetPreferredAllocation is a method that retrieves data based on the provided parameters and may return an error.


```go
func (dp *DevicePlugin) GetPreferredAllocation((*kubeletdevicepluginv1beta1.PreferredAllocationResponse, error)) (*kubeletdevicepluginv1beta1.PreferredAllocationResponse, error)
```


**Тип запроса:** kubeletdevicepluginv1beta1.PreferredAllocationResponse


```json
{
  "state": {},
  "containerResponses": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Тип ответа:** kubeletdevicepluginv1beta1.PreferredAllocationResponse


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


*Типы возврата:* `*kubeletdevicepluginv1beta1.PreferredAllocationResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:147`



---


[function] name: ListAndWatch file: test/e2e_node/testdeviceplugin/device-plugin.go:83 returns_error: нет description: —


### ListAndWatch (test/e2e_node/testdeviceplugin/device-plugin.go:83)


ListAndWatch is a method that lists or finds data based on the provided parameters and returns (empty *kubeletdevicepluginv1beta1.Empty, stream kubeletdevicepluginv1beta1.DevicePlugin_ListAndWatchServer).


```go
func (dp *DevicePlugin) ListAndWatch((empty *kubeletdevicepluginv1beta1.Empty, stream kubeletdevicepluginv1beta1.DevicePlugin_ListAndWatchServer)) (empty *kubeletdevicepluginv1beta1.Empty, stream kubeletdevicepluginv1beta1.DevicePlugin_ListAndWatchServer)
```


**Тип запроса:** kubeletdevicepluginv1beta1.Empty


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Тип ответа:** empty


```json
{
  "gv": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/discovery/cached/memory/memcache.go`


**Тип ответа:** kubeletdevicepluginv1beta1.Empty


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Тип ответа:** stream


```json
{
  "streamConn": {}
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


**Тип ответа:** kubeletdevicepluginv1beta1.DevicePlugin_ListAndWatchServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:83`



---


[function] name: NewDevicePlugin file: test/e2e_node/testdeviceplugin/device-plugin.go:51 returns_error: да description: —


### NewDevicePlugin (test/e2e_node/testdeviceplugin/device-plugin.go:51)


NewDevicePlugin is a function that performs operations based on the provided parameters and may return an error.


```go
func NewDevicePlugin((errorInjector func(string) error)) (errorInjector func(string) error)
```


**Тип ответа:** errorInjector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `errorInjector func(string) error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:51`



---


[function] name: PreStartContainer file: test/e2e_node/testdeviceplugin/device-plugin.go:143 returns_error: да description: —


### PreStartContainer (test/e2e_node/testdeviceplugin/device-plugin.go:143)


PreStartContainer is a method that performs operations based on the provided parameters and may return an error.


```go
func (dp *DevicePlugin) PreStartContainer((*kubeletdevicepluginv1beta1.PreStartContainerResponse, error)) (*kubeletdevicepluginv1beta1.PreStartContainerResponse, error)
```


**Тип запроса:** kubeletdevicepluginv1beta1.PreStartContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Тип ответа:** kubeletdevicepluginv1beta1.PreStartContainerResponse


```json
{
  "state": {},
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletdevicepluginv1beta1.PreStartContainerResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:143`



---


[function] name: RegisterDevicePlugin file: test/e2e_node/testdeviceplugin/device-plugin.go:151 returns_error: нет description: —


### RegisterDevicePlugin (test/e2e_node/testdeviceplugin/device-plugin.go:151)


RegisterDevicePlugin is a method that performs operations based on the provided parameters and returns (ctx context.Context, uniqueName, resourceName string, devices []*kubeletdevicepluginv1beta1.Device).


```go
func (dp *DevicePlugin) RegisterDevicePlugin((ctx context.Context, uniqueName, resourceName string, devices []*kubeletdevicepluginv1beta1.Device)) (ctx context.Context, uniqueName, resourceName string, devices []*kubeletdevicepluginv1beta1.Device)
```


**Тип запроса:** kubeletdevicepluginv1beta1.Device


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


**Тип ответа:** uniqueName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** resourceName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** devices


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeletdevicepluginv1beta1.Device


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


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:151`



---


[function] name: Stop file: test/e2e_node/testdeviceplugin/device-plugin.go:204 returns_error: нет description: —


### Stop (test/e2e_node/testdeviceplugin/device-plugin.go:204)


Stop is a method that performs operations based on the provided parameters and returns ().


```go
func (dp *DevicePlugin) Stop(()) ()
```


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:204`



---


[function] name: UpdateDevices file: test/e2e_node/testdeviceplugin/device-plugin.go:233 returns_error: нет description: —


### UpdateDevices (test/e2e_node/testdeviceplugin/device-plugin.go:233)


UpdateDevices is a method that updates data based on the provided parameters and returns (devices []*kubeletdevicepluginv1beta1.Device).


```go
func (dp *DevicePlugin) UpdateDevices((devices []*kubeletdevicepluginv1beta1.Device)) (devices []*kubeletdevicepluginv1beta1.Device)
```


**Тип запроса:** kubeletdevicepluginv1beta1.Device


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


**Тип ответа:** devices


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeletdevicepluginv1beta1.Device


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


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:233`



---


[function] name: WasCalled file: test/e2e_node/testdeviceplugin/device-plugin.go:211 returns_error: нет description: —


### WasCalled (test/e2e_node/testdeviceplugin/device-plugin.go:211)


WasCalled is a method that performs operations based on the provided parameters and returns (method string).


```go
func (dp *DevicePlugin) WasCalled((method string)) (method string)
```


**Тип ответа:** method


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:211`



---


[function] name: sendDevices file: test/e2e_node/testdeviceplugin/device-plugin.go:71 returns_error: нет description: —


### sendDevices (test/e2e_node/testdeviceplugin/device-plugin.go:71)


sendDevices is a method that performs operations based on the provided parameters and returns (stream kubeletdevicepluginv1beta1.DevicePlugin_ListAndWatchServer).


```go
func (dp *DevicePlugin) sendDevices((stream kubeletdevicepluginv1beta1.DevicePlugin_ListAndWatchServer)) (stream kubeletdevicepluginv1beta1.DevicePlugin_ListAndWatchServer)
```


**Тип ответа:** stream


```json
{
  "streamConn": {}
}
```


*Определено в:* `test/e2e/storage/drivers/proxy/portproxy.go`


**Тип ответа:** kubeletdevicepluginv1beta1.DevicePlugin_ListAndWatchServer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/testdeviceplugin/device-plugin.go:71`




## test/e2e_node/testing-manifests/embed.go


📄 Исходный файл: `test/e2e_node/testing-manifests/embed.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GetE2ENodeTestingManifestsFS](#gete2enodetestingmanifestsfs-teste2e_nodetesting-manifestsembedgo28) `:28`


</details>


[function] name: GetE2ENodeTestingManifestsFS file: test/e2e_node/testing-manifests/embed.go:28 returns_error: нет description: —


### GetE2ENodeTestingManifestsFS (test/e2e_node/testing-manifests/embed.go:28)


GetE2ENodeTestingManifestsFS is a function that retrieves data based on the provided parameters and returns ().


```go
func GetE2ENodeTestingManifestsFS(()) ()
```


📍 *Расположение:* `test/e2e_node/testing-manifests/embed.go:28`




## test/e2e_node/util.go


📄 Исходный файл: `test/e2e_node/util.go`


<details open>
<summary><b>Функции в этом файле (37)</b></summary>


- 🔗 [WaitForPodContainerRestartCount](#waitforpodcontainerrestartcount-teste2e_nodeutilgo560) `:560`

- 🔗 [WaitForPodInitContainerRestartCount](#waitforpodinitcontainerrestartcount-teste2e_nodeutilgo547) `:547`

- 🔗 [WaitForPodInitContainerToFail](#waitforpodinitcontainertofail-teste2e_nodeutilgo575) `:575`

- 🔗 [addAfterEachForCleaningUpPods](#addaftereachforcleaninguppods-teste2e_nodeutilgo168) `:168`

- 🔗 [deletePodSyncAndWait](#deletepodsyncandwait-teste2e_nodeutilgo646) `:646`

- 🔗 [deletePodSyncByName](#deletepodsyncbyname-teste2e_nodeutilgo599) `:599`

- 🔗 [deletePods](#deletepods-teste2e_nodeutilgo608) `:608`

- 🔗 [deletePodsAsync](#deletepodsasync-teste2e_nodeutilgo632) `:632`

- 🔗 [deleteStateFile](#deletestatefile-teste2e_nodeutilgo202) `:202`

- 🔗 [findContainerRuntimeServiceName](#findcontainerruntimeservicename-teste2e_nodeutilgo326) `:326`

- 🔗 [findKubeletServiceName](#findkubeletservicename-teste2e_nodeutilgo309) `:309`

- 🔗 [getCRIClient](#getcriclient-teste2e_nodeutilgo283) `:283`

- 🔗 [getLocalNode](#getlocalnode-teste2e_nodeutilgo231) `:231`

- 🔗 [getLocalNodeCPUDetails](#getlocalnodecpudetails-teste2e_nodeutilgo252) `:252`

- 🔗 [getLocalTestNode](#getlocaltestnode-teste2e_nodeutilgo242) `:242`

- 🔗 [getNodeSummary](#getnodesummary-teste2e_nodeutilgo98) `:98`

- 🔗 [getPidFromPidFile](#getpidfrompidfile-teste2e_nodeutilgo524) `:524`

- 🔗 [getPidsForProcess](#getpidsforprocess-teste2e_nodeutilgo512) `:512`

- 🔗 [getV1NodeDevices](#getv1nodedevices-teste2e_nodeutilgo149) `:149`

- 🔗 [getV1alpha1NodeDevices](#getv1alpha1nodedevices-teste2e_nodeutilgo130) `:130`

- 🔗 [kubeletHealthCheck](#kubelethealthcheck-teste2e_nodeutilgo434) `:434`

- 🔗 [listNamespaceEvents](#listnamespaceevents-teste2e_nodeutilgo208) `:208`

- 🔗 [logKubeletLatencyMetrics](#logkubeletlatencymetrics-teste2e_nodeutilgo269) `:269`

- 🔗 [logNodeEvents](#lognodeevents-teste2e_nodeutilgo225) `:225`

- 🔗 [logPodEvents](#logpodevents-teste2e_nodeutilgo219) `:219`

- 🔗 [mustStopKubelet](#muststopkubelet-teste2e_nodeutilgo411) `:411`

- 🔗 [nodeNameOrIP](#nodenameorip-teste2e_nodeutilgo595) `:595`

- 🔗 [performContainerRuntimeUnitOp](#performcontainerruntimeunitop-teste2e_nodeutilgo353) `:353`

- 🔗 [reduceAllocatableMemoryUsageIfCgroupv1](#reduceallocatablememoryusageifcgroupv1-teste2e_nodeutilgo466) `:466`

- 🔗 [restartKubelet](#restartkubelet-teste2e_nodeutilgo400) `:400`

- 🔗 [startContainerRuntime](#startcontainerruntime-teste2e_nodeutilgo388) `:388`

- 🔗 [stopContainerRuntime](#stopcontainerruntime-teste2e_nodeutilgo384) `:384`

- 🔗 [toCgroupFsName](#tocgroupfsname-teste2e_nodeutilgo455) `:455`

- 🔗 [waitForAllContainerRemoval](#waitforallcontainerremoval-teste2e_nodeutilgo491) `:491`

- 🔗 [waitForContainerRemoval](#waitforcontainerremoval-teste2e_nodeutilgo614) `:614`

- 🔗 [waitForKubeletToStart](#waitforkubelettostart-teste2e_nodeutilgo183) `:183`

- 🔗 [withFeatureGate](#withfeaturegate-teste2e_nodeutilgo478) `:478`


</details>


[function] name: WaitForPodContainerRestartCount file: test/e2e_node/util.go:560 returns_error: нет description: WaitForPodContainerRestartCount waits for the given Pod container to achieve at least a given restartCount
TODO: eventua


### WaitForPodContainerRestartCount (test/e2e_node/util.go:560)


WaitForPodContainerRestartCount waits for the given Pod container to achieve at least a given restartCount
TODO: eventually look at moving to test/e2e/framework/pod


```go
func WaitForPodContainerRestartCount((ctx context.Context, c clientset.Interface, namespace, podName string, containerIndex int, desiredRestartCount int32, timeout time.Duration)) (ctx context.Context, c clientset.Interface, namespace, podName string, containerIndex int, desiredRestartCount int32, timeout time.Duration)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** containerIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desiredRestartCount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/e2e_node/util.go:560`



---


[function] name: WaitForPodInitContainerRestartCount file: test/e2e_node/util.go:547 returns_error: нет description: WaitForPodInitContainerRestartCount waits for the given Pod init container
to achieve at least a given restartCount
TODO


### WaitForPodInitContainerRestartCount (test/e2e_node/util.go:547)


WaitForPodInitContainerRestartCount waits for the given Pod init container
to achieve at least a given restartCount
TODO: eventually look at moving to test/e2e/framework/pod


```go
func WaitForPodInitContainerRestartCount((ctx context.Context, c clientset.Interface, namespace, podName string, initContainerIndex int, desiredRestartCount int32, timeout time.Duration)) (ctx context.Context, c clientset.Interface, namespace, podName string, initContainerIndex int, desiredRestartCount int32, timeout time.Duration)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** initContainerIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** desiredRestartCount


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/e2e_node/util.go:547`



---


[function] name: WaitForPodInitContainerToFail file: test/e2e_node/util.go:575 returns_error: нет description: WaitForPodInitContainerToFail waits for the given Pod init container to fail with the given reason, specifically due to



### WaitForPodInitContainerToFail (test/e2e_node/util.go:575)


WaitForPodInitContainerToFail waits for the given Pod init container to fail with the given reason, specifically due to
invalid container configuration. In this case, the container will remain in a waiting state with a specific
reason set, which should match the given reason.
TODO: eventually look at moving to test/e2e/framework/pod


```go
func WaitForPodInitContainerToFail((ctx context.Context, c clientset.Interface, namespace, podName string, containerIndex int, reason string, timeout time.Duration)) (ctx context.Context, c clientset.Interface, namespace, podName string, containerIndex int, reason string, timeout time.Duration)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** namespace


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** containerIndex


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reason


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


📍 *Расположение:* `test/e2e_node/util.go:575`



---


[function] name: addAfterEachForCleaningUpPods file: test/e2e_node/util.go:168 returns_error: нет description: —


### addAfterEachForCleaningUpPods (test/e2e_node/util.go:168)


addAfterEachForCleaningUpPods is a function that performs operations based on the provided parameters and returns (f *framework.Framework).


```go
func addAfterEachForCleaningUpPods((f *framework.Framework)) (f *framework.Framework)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


📍 *Расположение:* `test/e2e_node/util.go:168`



---


[function] name: deletePodSyncAndWait file: test/e2e_node/util.go:646 returns_error: нет description: —


### deletePodSyncAndWait (test/e2e_node/util.go:646)


deletePodSyncAndWait is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework, podNS, podName string).


```go
func deletePodSyncAndWait((ctx context.Context, f *framework.Framework, podNS, podName string)) (ctx context.Context, f *framework.Framework, podNS, podName string)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** podNS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:646`



---


[function] name: deletePodSyncByName file: test/e2e_node/util.go:599 returns_error: нет description: —


### deletePodSyncByName (test/e2e_node/util.go:599)


deletePodSyncByName is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework, podName string).


```go
func deletePodSyncByName((ctx context.Context, f *framework.Framework, podName string)) (ctx context.Context, f *framework.Framework, podName string)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:599`



---


[function] name: deletePods file: test/e2e_node/util.go:608 returns_error: нет description: —


### deletePods (test/e2e_node/util.go:608)


deletePods is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework, podNames []string).


```go
func deletePods((ctx context.Context, f *framework.Framework, podNames []string)) (ctx context.Context, f *framework.Framework, podNames []string)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** podNames


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:608`



---


[function] name: deletePodsAsync file: test/e2e_node/util.go:632 returns_error: нет description: —


### deletePodsAsync (test/e2e_node/util.go:632)


deletePodsAsync is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework, podMap map[string]*v1.Pod).


```go
func deletePodsAsync((ctx context.Context, f *framework.Framework, podMap map[string]*v1.Pod)) (ctx context.Context, f *framework.Framework, podMap map[string]*v1.Pod)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип запроса:** v1.Pod


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** podMap


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** v1.Pod


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


📍 *Расположение:* `test/e2e_node/util.go:632`



---


[function] name: deleteStateFile file: test/e2e_node/util.go:202 returns_error: нет description: —


### deleteStateFile (test/e2e_node/util.go:202)


deleteStateFile is a function that performs operations based on the provided parameters and returns (stateFileName string).


```go
func deleteStateFile((stateFileName string)) (stateFileName string)
```


**Тип ответа:** stateFileName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:202`



---


[function] name: findContainerRuntimeServiceName file: test/e2e_node/util.go:326 returns_error: да description: —


### findContainerRuntimeServiceName (test/e2e_node/util.go:326)


findContainerRuntimeServiceName is a function that performs operations based on the provided parameters and may return an error.


```go
func findContainerRuntimeServiceName((string, error)) (string, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `string`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util.go:326`



---


[function] name: findKubeletServiceName file: test/e2e_node/util.go:309 returns_error: нет description: findKubeletServiceName searches the unit name among the services known to systemd.
if the `running` parameter is true, r


### findKubeletServiceName (test/e2e_node/util.go:309)


findKubeletServiceName searches the unit name among the services known to systemd.
if the `running` parameter is true, restricts the search among currently running services;
otherwise, also stopped, failed, exited (non-running in general) services are also considered.
TODO: Find a uniform way to deal with systemctl/initctl/service operations. #34494


```go
func findKubeletServiceName((running bool)) (running bool)
```


**Тип ответа:** running


```json
{
  "interval": {},
  "client": null,
  "compactor": {},
  "cancel": {},
  "refs": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/storagebackend/factory/etcd3.go`


📍 *Расположение:* `test/e2e_node/util.go:309`



---


[function] name: getCRIClient file: test/e2e_node/util.go:283 returns_error: да description: getCRIClient connects CRI and returns CRI runtime service clients and image service client.


### getCRIClient (test/e2e_node/util.go:283)


getCRIClient connects CRI and returns CRI runtime service clients and image service client.


```go
func getCRIClient((internalapi.RuntimeService, internalapi.ImageManagerService, error)) (internalapi.RuntimeService, internalapi.ImageManagerService, error)
```


**Тип ответа:** internalapi.RuntimeService


```json
{
  "Called": [],
  "Errors": {},
  "FakeStatus": null,
  "Containers": {},
  "Sandboxes": {},
  "FakeContainerStats": {},
  "FakePodSandboxStats": {},
  "FakePodSandboxMetrics": {},
  "FakeMetricDescriptors": {},
  "FakeContainerMetrics": {},
  "FakeLinuxConfiguration": null,
  "ErrorOnSandboxCreate": false
}
```


*Определено в:* `staging/src/k8s.io/cri-api/pkg/apis/testing/fake_runtime_service.go`


**Тип ответа:** internalapi.ImageManagerService


```json
{
  "service": {}
}
```


*Определено в:* `pkg/kubelet/kuberuntime/instrumented_services.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `internalapi.RuntimeService`, `internalapi.ImageManagerService`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util.go:283`



---


[function] name: getLocalNode file: test/e2e_node/util.go:231 returns_error: нет description: —


### getLocalNode (test/e2e_node/util.go:231)


getLocalNode is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework).


```go
func getLocalNode((ctx context.Context, f *framework.Framework)) (ctx context.Context, f *framework.Framework)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


📍 *Расположение:* `test/e2e_node/util.go:231`



---


[function] name: getLocalNodeCPUDetails file: test/e2e_node/util.go:252 returns_error: нет description: —


### getLocalNodeCPUDetails (test/e2e_node/util.go:252)


getLocalNodeCPUDetails is a function that performs operations based on the provided parameters and returns (cpuCapVal int64, cpuAllocVal int64, cpuResVal int64).


```go
func getLocalNodeCPUDetails((cpuCapVal int64, cpuAllocVal int64, cpuResVal int64)) (cpuCapVal int64, cpuAllocVal int64, cpuResVal int64)
```


**Тип ответа:** cpuCapVal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cpuAllocVal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cpuResVal


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:252`



---


[function] name: getLocalTestNode file: test/e2e_node/util.go:242 returns_error: нет description: getLocalTestNode fetches the node object describing the local worker node set up by the e2e_node infra, alongside with i


### getLocalTestNode (test/e2e_node/util.go:242)


getLocalTestNode fetches the node object describing the local worker node set up by the e2e_node infra, alongside with its ready state.
getLocalTestNode is a variant of `getLocalNode` which reports but does not set any requirement about the node readiness state, letting
the caller decide. The check is intentionally done like `getLocalNode` does.
Note `getLocalNode` aborts (as in ginkgo.Expect) the test implicitly if the worker node is not ready.


```go
func getLocalTestNode((*v1.Node, bool)) (*v1.Node, bool)
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


📍 *Расположение:* `test/e2e_node/util.go:242`



---


[function] name: getNodeSummary file: test/e2e_node/util.go:98 returns_error: да description: —


### getNodeSummary (test/e2e_node/util.go:98)


getNodeSummary is a function that performs operations based on the provided parameters and may return an error.


```go
func getNodeSummary((*stats.Summary, error)) (*stats.Summary, error)
```


**Тип запроса:** stats.Summary


```json
{
  "Node": {},
  "Pods": []
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/stats/v1alpha1/types.go`


**Тип ответа:** stats.Summary


```json
{
  "Node": {},
  "Pods": []
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/stats/v1alpha1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*stats.Summary`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util.go:98`



---


[function] name: getPidFromPidFile file: test/e2e_node/util.go:524 returns_error: да description: —


### getPidFromPidFile (test/e2e_node/util.go:524)


getPidFromPidFile is a function that performs operations based on the provided parameters and may return an error.


```go
func getPidFromPidFile((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util.go:524`



---


[function] name: getPidsForProcess file: test/e2e_node/util.go:512 returns_error: да description: —


### getPidsForProcess (test/e2e_node/util.go:512)


getPidsForProcess is a function that performs operations based on the provided parameters and may return an error.


```go
func getPidsForProcess(([]int, error)) ([]int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util.go:512`



---


[function] name: getV1NodeDevices file: test/e2e_node/util.go:149 returns_error: да description: —


### getV1NodeDevices (test/e2e_node/util.go:149)


getV1NodeDevices is a function that performs operations based on the provided parameters and may return an error.


```go
func getV1NodeDevices((*kubeletpodresourcesv1.ListPodResourcesResponse, error)) (*kubeletpodresourcesv1.ListPodResourcesResponse, error)
```


**Тип запроса:** kubeletpodresourcesv1.ListPodResourcesResponse


```json
{
  "state": {},
  "podResources": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/podresources/v1alpha1/api.pb.go`


**Тип ответа:** kubeletpodresourcesv1.ListPodResourcesResponse


```json
{
  "state": {},
  "podResources": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/podresources/v1alpha1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletpodresourcesv1.ListPodResourcesResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util.go:149`



---


[function] name: getV1alpha1NodeDevices file: test/e2e_node/util.go:130 returns_error: да description: —


### getV1alpha1NodeDevices (test/e2e_node/util.go:130)


getV1alpha1NodeDevices is a function that performs operations based on the provided parameters and may return an error.


```go
func getV1alpha1NodeDevices((*kubeletpodresourcesv1alpha1.ListPodResourcesResponse, error)) (*kubeletpodresourcesv1alpha1.ListPodResourcesResponse, error)
```


**Тип запроса:** kubeletpodresourcesv1alpha1.ListPodResourcesResponse


```json
{
  "state": {},
  "podResources": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/podresources/v1alpha1/api.pb.go`


**Тип ответа:** kubeletpodresourcesv1alpha1.ListPodResourcesResponse


```json
{
  "state": {},
  "podResources": [],
  "unknownFields": {},
  "sizeCache": {}
}
```


*Определено в:* `staging/src/k8s.io/kubelet/pkg/apis/podresources/v1alpha1/api.pb.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletpodresourcesv1alpha1.ListPodResourcesResponse`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util.go:130`



---


[function] name: kubeletHealthCheck file: test/e2e_node/util.go:434 returns_error: нет description: —


### kubeletHealthCheck (test/e2e_node/util.go:434)


kubeletHealthCheck is a function that performs operations based on the provided parameters and returns (url string).


```go
func kubeletHealthCheck((url string)) (url string)
```


**Тип ответа:** url


```json
{
  "baseURL": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/testcase.go`


📍 *Расположение:* `test/e2e_node/util.go:434`



---


[function] name: listNamespaceEvents file: test/e2e_node/util.go:208 returns_error: нет description: listNamespaceEvents lists the events in the given namespace.


### listNamespaceEvents (test/e2e_node/util.go:208)


listNamespaceEvents lists the events in the given namespace.


```go
func listNamespaceEvents((ctx context.Context, c clientset.Interface, ns string)) (ctx context.Context, c clientset.Interface, ns string)
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


**Тип ответа:** clientset.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


**Тип ответа:** ns


```json
{
  "Generic": null,
  "KubeCloudShared": null,
  "ServiceController": null,
  "AttachDetachController": null,
  "CSRSigningController": null,
  "DaemonSetController": null,
  "DeploymentController": null,
  "DeviceTaintEvictionController": null,
  "ResourceClaimController": null,
  "StatefulSetController": null,
  "DeprecatedFlags": null,
  "EndpointController": null,
  "EndpointSliceController": null,
  "EndpointSliceMirroringController": null,
  "EphemeralVolumeController": null,
  "GarbageCollectorController": null,
  "HPAController": null,
  "JobController": null,
  "CronJobController": null,
  "LegacySATokenCleaner": null,
  "NamespaceController": null,
  "NodeIPAMController": null,
  "NodeLifecycleController": null,
  "PersistentVolumeBinderController": null,
  "PodGCController": null,
  "ReplicaSetController": null,
  "ReplicationController": null,
  "ResourceQuotaController": null,
  "SAController": null,
  "TTLAfterFinishedController": null,
  "ValidatingAdmissionPolicyStatusController": null,
  "SecureServing": null,
  "Authentication": null,
  "Authorization": null,
  "Metrics": null,
  "Logs": null,
  "Master": "string",
  "ShowHiddenMetricsForVersion": "string",
  "ControllerShutdownTimeout": {},
  "ComponentGlobalsRegistry": {},
  "ParsedFlags": null
}
```


*Определено в:* `cmd/kube-controller-manager/app/options/options.go`


📍 *Расположение:* `test/e2e_node/util.go:208`



---


[function] name: logKubeletLatencyMetrics file: test/e2e_node/util.go:269 returns_error: нет description: logKubeletLatencyMetrics logs KubeletLatencyMetrics computed from the Prometheus
metrics exposed on the current node and


### logKubeletLatencyMetrics (test/e2e_node/util.go:269)


logKubeletLatencyMetrics logs KubeletLatencyMetrics computed from the Prometheus
metrics exposed on the current node and identified by the metricNames.
The Kubelet subsystem prefix is automatically prepended to these metric names.


```go
func logKubeletLatencyMetrics((ctx context.Context, metricNames ...string)) (ctx context.Context, metricNames ...string)
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


**Тип ответа:** metricNames


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:269`



---


[function] name: logNodeEvents file: test/e2e_node/util.go:225 returns_error: нет description: —


### logNodeEvents (test/e2e_node/util.go:225)


logNodeEvents is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework).


```go
func logNodeEvents((ctx context.Context, f *framework.Framework)) (ctx context.Context, f *framework.Framework)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


📍 *Расположение:* `test/e2e_node/util.go:225`



---


[function] name: logPodEvents file: test/e2e_node/util.go:219 returns_error: нет description: —


### logPodEvents (test/e2e_node/util.go:219)


logPodEvents is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework).


```go
func logPodEvents((ctx context.Context, f *framework.Framework)) (ctx context.Context, f *framework.Framework)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


📍 *Расположение:* `test/e2e_node/util.go:219`



---


[function] name: mustStopKubelet file: test/e2e_node/util.go:411 returns_error: нет description: mustStopKubelet will kill the running kubelet, and returns a func that will restart the process again


### mustStopKubelet (test/e2e_node/util.go:411)


mustStopKubelet will kill the running kubelet, and returns a func that will restart the process again


```go
func mustStopKubelet((ctx context.Context, f *framework.Framework)) (ctx context.Context, f *framework.Framework)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


📍 *Расположение:* `test/e2e_node/util.go:411`



---


[function] name: nodeNameOrIP file: test/e2e_node/util.go:595 returns_error: нет description: —


### nodeNameOrIP (test/e2e_node/util.go:595)


nodeNameOrIP is a function that performs operations based on the provided parameters and returns ().


```go
func nodeNameOrIP(()) ()
```


📍 *Расположение:* `test/e2e_node/util.go:595`



---


[function] name: performContainerRuntimeUnitOp file: test/e2e_node/util.go:353 returns_error: нет description: —


### performContainerRuntimeUnitOp (test/e2e_node/util.go:353)


performContainerRuntimeUnitOp is a function that performs operations based on the provided parameters and returns (op containerRuntimeUnitOp).


```go
func performContainerRuntimeUnitOp((op containerRuntimeUnitOp)) (op containerRuntimeUnitOp)
```


**Тип ответа:** op


```json
{
  "realOp": {}
}
```


*Определено в:* `test/integration/scheduler_perf/scheduler_perf.go`


**Тип ответа:** containerRuntimeUnitOp


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:353`



---


[function] name: reduceAllocatableMemoryUsageIfCgroupv1 file: test/e2e_node/util.go:466 returns_error: нет description: reduceAllocatableMemoryUsageIfCgroupv1 uses memory.force_empty (https://lwn.net/Articles/432224/)
to make the kernel rec


### reduceAllocatableMemoryUsageIfCgroupv1 (test/e2e_node/util.go:466)


reduceAllocatableMemoryUsageIfCgroupv1 uses memory.force_empty (https://lwn.net/Articles/432224/)
to make the kernel reclaim memory in the allocatable cgroup
the time to reduce pressure may be unbounded, but usually finishes within a second.
memory.force_empty is no supported in cgroupv2.


```go
func reduceAllocatableMemoryUsageIfCgroupv1(()) ()
```


📍 *Расположение:* `test/e2e_node/util.go:466`



---


[function] name: restartKubelet file: test/e2e_node/util.go:400 returns_error: нет description: restartKubelet restarts the current kubelet service.
the "current" kubelet service is the instance managed by the curren


### restartKubelet (test/e2e_node/util.go:400)


restartKubelet restarts the current kubelet service.
the "current" kubelet service is the instance managed by the current e2e_node test run.
If `running` is true, restarts only if the current kubelet is actually running. In some cases,
the kubelet may have exited or can be stopped, typically because it was intentionally stopped
earlier during a test, or, sometimes, because it just crashed.
Warning: the "current" kubelet is poorly defined. The "current" kubelet is assumed to be the most
recent kubelet service unit, IOW there is not a unique ID we use to bind explicitly a kubelet
instance to a test run.


```go
func restartKubelet((ctx context.Context, running bool)) (ctx context.Context, running bool)
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


**Тип ответа:** running


```json
{
  "interval": {},
  "client": null,
  "compactor": {},
  "cancel": {},
  "refs": 0
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/storage/storagebackend/factory/etcd3.go`


📍 *Расположение:* `test/e2e_node/util.go:400`



---


[function] name: startContainerRuntime file: test/e2e_node/util.go:388 returns_error: нет description: —


### startContainerRuntime (test/e2e_node/util.go:388)


startContainerRuntime is a function that performs operations based on the provided parameters and returns ().


```go
func startContainerRuntime(()) ()
```


📍 *Расположение:* `test/e2e_node/util.go:388`



---


[function] name: stopContainerRuntime file: test/e2e_node/util.go:384 returns_error: нет description: —


### stopContainerRuntime (test/e2e_node/util.go:384)


stopContainerRuntime is a function that performs operations based on the provided parameters and returns ().


```go
func stopContainerRuntime(()) ()
```


📍 *Расположение:* `test/e2e_node/util.go:384`



---


[function] name: toCgroupFsName file: test/e2e_node/util.go:455 returns_error: нет description: —


### toCgroupFsName (test/e2e_node/util.go:455)


toCgroupFsName is a function that performs operations based on the provided parameters and returns (cgroupName cm.CgroupName).


```go
func toCgroupFsName((cgroupName cm.CgroupName)) (cgroupName cm.CgroupName)
```


**Тип ответа:** cgroupName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** cm.CgroupName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:455`



---


[function] name: waitForAllContainerRemoval file: test/e2e_node/util.go:491 returns_error: нет description: waitForAllContainerRemoval waits until all the containers on a given pod are really gone.
This is needed by the e2e test


### waitForAllContainerRemoval (test/e2e_node/util.go:491)


waitForAllContainerRemoval waits until all the containers on a given pod are really gone.
This is needed by the e2e tests which involve exclusive resource allocation (cpu, topology manager; podresources; etc.)
In these cases, we need to make sure the tests clean up after themselves to make sure each test runs in
a pristine environment. The only way known so far to do that is to introduce this wait.
Worth noting, however, that this makes the test runtime much bigger.


```go
func waitForAllContainerRemoval((ctx context.Context, podName, podNS string)) (ctx context.Context, podName, podNS string)
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


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podNS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:491`



---


[function] name: waitForContainerRemoval file: test/e2e_node/util.go:614 returns_error: нет description: —


### waitForContainerRemoval (test/e2e_node/util.go:614)


waitForContainerRemoval is a function that performs operations based on the provided parameters and returns (ctx context.Context, containerName, podName, podNS string).


```go
func waitForContainerRemoval((ctx context.Context, containerName, podName, podNS string)) (ctx context.Context, containerName, podName, podNS string)
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


**Тип ответа:** containerName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** podNS


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util.go:614`



---


[function] name: waitForKubeletToStart file: test/e2e_node/util.go:183 returns_error: нет description: —


### waitForKubeletToStart (test/e2e_node/util.go:183)


waitForKubeletToStart is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework).


```go
func waitForKubeletToStart((ctx context.Context, f *framework.Framework)) (ctx context.Context, f *framework.Framework)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


📍 *Расположение:* `test/e2e_node/util.go:183`



---


[function] name: withFeatureGate file: test/e2e_node/util.go:478 returns_error: нет description: Equivalent of featuregatetesting.SetFeatureGateDuringTest
which can't be used here because we're not in a Testing contex


### withFeatureGate (test/e2e_node/util.go:478)


Equivalent of featuregatetesting.SetFeatureGateDuringTest
which can't be used here because we're not in a Testing context.
This must be in a non-"_test" file to pass
make verify WHAT=test-featuregates


```go
func withFeatureGate((feature featuregate.Feature, desired bool)) (feature featuregate.Feature, desired bool)
```


**Тип ответа:** feature


```json
{
  "Name": "string",
  "FullName": "string",
  "VersionedSpecs": []
}
```


*Определено в:* `test/compatibility_lifecycle/cmd/feature_gates.go`


**Тип ответа:** featuregate.Feature


```json
{
  "Name": "string",
  "Comments": []
}
```


*Определено в:* `hack/tools/golangci-lint/sorted/pkg/sorted.go`


**Тип ответа:** desired


```json
{
  "portsByKey": {},
  "endpointsByKey": {},
  "numDesiredEndpoints": 0
}
```


*Определено в:* `pkg/controller/endpointslicemirroring/reconciler_helpers.go`


📍 *Расположение:* `test/e2e_node/util.go:478`




## test/e2e_node/util_criproxy_linux.go


📄 Исходный файл: `test/e2e_node/util_criproxy_linux.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [addCRIProxyInjector](#addcriproxyinjector-teste2e_nodeutil_criproxy_linuxgo28) `:28`

- 🔗 [resetCRIProxyInjector](#resetcriproxyinjector-teste2e_nodeutil_criproxy_linuxgo37) `:37`


</details>


[function] name: addCRIProxyInjector file: test/e2e_node/util_criproxy_linux.go:28 returns_error: да description: addCRIProxyInjector registers an injector function for the CRIProxy.


### addCRIProxyInjector (test/e2e_node/util_criproxy_linux.go:28)


addCRIProxyInjector registers an injector function for the CRIProxy.


```go
func addCRIProxyInjector((proxy *criproxy.RemoteRuntime, injector func(apiName string) error)) (proxy *criproxy.RemoteRuntime, injector func(apiName string) error)
```


**Тип запроса:** criproxy.RemoteRuntime


```json
{
  "server": null,
  "injectors": [],
  "runtimeService": {},
  "imageService": {}
}
```


*Определено в:* `test/e2e_node/criproxy/proxy_runtime_service.go`


**Тип ответа:** proxy


```json
{
  "localDelegate": {},
  "proxyCurrentCertKeyContent": {},
  "proxyTransportDial": null,
  "serviceResolver": {},
  "handlingInfo": {},
  "rejectForwardingRedirects": false,
  "tracerProvider": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/apiserver/handler_proxy.go`


**Тип ответа:** criproxy.RemoteRuntime


```json
{
  "server": null,
  "injectors": [],
  "runtimeService": {},
  "imageService": {}
}
```


*Определено в:* `test/e2e_node/criproxy/proxy_runtime_service.go`


**Тип ответа:** injector


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiName


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `proxy *criproxy.RemoteRuntime`, `injector func(apiName string) error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util_criproxy_linux.go:28`



---


[function] name: resetCRIProxyInjector file: test/e2e_node/util_criproxy_linux.go:37 returns_error: нет description: resetCRIProxyInjector resets all injector functions for the CRIProxy.


### resetCRIProxyInjector (test/e2e_node/util_criproxy_linux.go:37)


resetCRIProxyInjector resets all injector functions for the CRIProxy.


```go
func resetCRIProxyInjector((proxy *criproxy.RemoteRuntime)) (proxy *criproxy.RemoteRuntime)
```


**Тип запроса:** criproxy.RemoteRuntime


```json
{
  "server": null,
  "injectors": [],
  "runtimeService": {},
  "imageService": {}
}
```


*Определено в:* `test/e2e_node/criproxy/proxy_runtime_service.go`


**Тип ответа:** proxy


```json
{
  "localDelegate": {},
  "proxyCurrentCertKeyContent": {},
  "proxyTransportDial": null,
  "serviceResolver": {},
  "handlingInfo": {},
  "rejectForwardingRedirects": false,
  "tracerProvider": {}
}
```


*Определено в:* `staging/src/k8s.io/kube-aggregator/pkg/apiserver/handler_proxy.go`


**Тип ответа:** criproxy.RemoteRuntime


```json
{
  "server": null,
  "injectors": [],
  "runtimeService": {},
  "imageService": {}
}
```


*Определено в:* `test/e2e_node/criproxy/proxy_runtime_service.go`


📍 *Расположение:* `test/e2e_node/util_criproxy_linux.go:37`




## test/e2e_node/util_kubeletconfig.go


📄 Исходный файл: `test/e2e_node/util_kubeletconfig.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [getCurrentKubeletConfig](#getcurrentkubeletconfig-teste2e_nodeutil_kubeletconfiggo36) `:36`

- 🔗 [getNodeReadyStatus](#getnodereadystatus-teste2e_nodeutil_kubeletconfiggo103) `:103`

- 🔗 [isNodeReady](#isnodeready-teste2e_nodeutil_kubeletconfiggo113) `:113`

- 🔗 [tempSetCurrentKubeletConfig](#tempsetcurrentkubeletconfig-teste2e_nodeutil_kubeletconfiggo43) `:43`

- 🔗 [updateKubeletConfig](#updatekubeletconfig-teste2e_nodeutil_kubeletconfiggo97) `:97`

- 🔗 [updateKubeletConfigWithOptions](#updatekubeletconfigwithoptions-teste2e_nodeutil_kubeletconfiggo74) `:74`


</details>


[function] name: getCurrentKubeletConfig file: test/e2e_node/util_kubeletconfig.go:36 returns_error: да description: Returns the current KubeletConfiguration


### getCurrentKubeletConfig (test/e2e_node/util_kubeletconfig.go:36)


Returns the current KubeletConfiguration


```go
func getCurrentKubeletConfig((*kubeletconfig.KubeletConfiguration, error)) (*kubeletconfig.KubeletConfiguration, error)
```


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*kubeletconfig.KubeletConfiguration`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util_kubeletconfig.go:36`



---


[function] name: getNodeReadyStatus file: test/e2e_node/util_kubeletconfig.go:103 returns_error: нет description: —


### getNodeReadyStatus (test/e2e_node/util_kubeletconfig.go:103)


getNodeReadyStatus is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework).


```go
func getNodeReadyStatus((ctx context.Context, f *framework.Framework)) (ctx context.Context, f *framework.Framework)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


📍 *Расположение:* `test/e2e_node/util_kubeletconfig.go:103`



---


[function] name: isNodeReady file: test/e2e_node/util_kubeletconfig.go:113 returns_error: нет description: isNodeReady returns true if a node is ready; false otherwise.


### isNodeReady (test/e2e_node/util_kubeletconfig.go:113)


isNodeReady returns true if a node is ready; false otherwise.


```go
func isNodeReady((node *v1.Node)) (node *v1.Node)
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


📍 *Расположение:* `test/e2e_node/util_kubeletconfig.go:113`



---


[function] name: tempSetCurrentKubeletConfig file: test/e2e_node/util_kubeletconfig.go:43 returns_error: нет description: Must be called within a Context. Allows the function to modify the KubeletConfiguration during the BeforeEach of the con


### tempSetCurrentKubeletConfig (test/e2e_node/util_kubeletconfig.go:43)


Must be called within a Context. Allows the function to modify the KubeletConfiguration during the BeforeEach of the context.
The change is reverted in the AfterEach of the context.


```go
func tempSetCurrentKubeletConfig((f *framework.Framework, updateFunction func(ctx context.Context, initialConfig *kubeletconfig.KubeletConfiguration))) (f *framework.Framework, updateFunction func(ctx context.Context, initialConfig *kubeletconfig.KubeletConfiguration))
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** updateFunction


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


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


**Тип ответа:** initialConfig


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


📍 *Расположение:* `test/e2e_node/util_kubeletconfig.go:43`



---


[function] name: updateKubeletConfig file: test/e2e_node/util_kubeletconfig.go:97 returns_error: нет description: —


### updateKubeletConfig (test/e2e_node/util_kubeletconfig.go:97)


updateKubeletConfig is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework, kubeletConfig *kubeletconfig.KubeletConfiguration, deleteStateFiles bool).


```go
func updateKubeletConfig((ctx context.Context, f *framework.Framework, kubeletConfig *kubeletconfig.KubeletConfiguration, deleteStateFiles bool)) (ctx context.Context, f *framework.Framework, kubeletConfig *kubeletconfig.KubeletConfiguration, deleteStateFiles bool)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** kubeletConfig


```json
{
  "config": {}
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/kubelet.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** deleteStateFiles


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util_kubeletconfig.go:97`



---


[function] name: updateKubeletConfigWithOptions file: test/e2e_node/util_kubeletconfig.go:74 returns_error: нет description: —


### updateKubeletConfigWithOptions (test/e2e_node/util_kubeletconfig.go:74)


updateKubeletConfigWithOptions is a function that performs operations based on the provided parameters and returns (ctx context.Context, f *framework.Framework, kubeletConfig *kubeletconfig.KubeletConfiguration, opts updateKubeletOptions).


```go
func updateKubeletConfigWithOptions((ctx context.Context, f *framework.Framework, kubeletConfig *kubeletconfig.KubeletConfiguration, opts updateKubeletOptions)) (ctx context.Context, f *framework.Framework, kubeletConfig *kubeletconfig.KubeletConfiguration, opts updateKubeletOptions)
```


**Тип запроса:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип запроса:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


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


**Тип ответа:** framework.Framework


```json
{
  "BaseName": "string",
  "UniqueName": "string",
  "clientConfig": null,
  "restMapper": null,
  "ClientSet": {},
  "KubemarkExternalClusterClientSet": {},
  "DynamicClient": {},
  "ScalesGetter": {},
  "SkipNamespaceCreation": false,
  "SkipSecretCreation": false,
  "Namespace": null,
  "namespacesToDelete": [],
  "NamespaceDeletionTimeout": {},
  "NamespacePodSecurityEnforceLevel": {},
  "NamespacePodSecurityWarnLevel": {},
  "NamespacePodSecurityAuditLevel": {},
  "NamespacePodSecurityLevel": {},
  "flakeReport": null,
  "Options": {},
  "TestSummaries": [],
  "Timeouts": null,
  "DumpAllNamespaceInfo": {}
}
```


*Определено в:* `test/e2e/framework/framework.go`


**Тип ответа:** kubeletConfig


```json
{
  "config": {}
}
```


*Определено в:* `cmd/kubeadm/app/componentconfigs/kubelet.go`


**Тип ответа:** kubeletconfig.KubeletConfiguration


```json
{
  "EnableServer": false,
  "StaticPodPath": "string",
  "PodLogsDir": "string",
  "SyncFrequency": {},
  "FileCheckFrequency": {},
  "HTTPCheckFrequency": {},
  "StaticPodURL": "string",
  "StaticPodURLHeader": {},
  "Address": "string",
  "Port": 0,
  "ReadOnlyPort": 0,
  "VolumePluginDir": "string",
  "ProviderID": "string",
  "TLSCertFile": "string",
  "TLSPrivateKeyFile": "string",
  "TLSCipherSuites": [],
  "TLSMinVersion": "string",
  "RotateCertificates": false,
  "ServerTLSBootstrap": false,
  "Authentication": {},
  "Authorization": {},
  "RegistryPullQPS": 0,
  "RegistryBurst": 0,
  "ImagePullCredentialsVerificationPolicy": "string",
  "PreloadedImagesVerificationAllowlist": [],
  "EventRecordQPS": 0,
  "EventBurst": 0,
  "EnableDebuggingHandlers": false,
  "EnableContentionProfiling": false,
  "HealthzPort": 0,
  "HealthzBindAddress": "string",
  "OOMScoreAdj": 0,
  "ClusterDomain": "string",
  "ClusterDNS": [],
  "StreamingConnectionIdleTimeout": {},
  "NodeStatusUpdateFrequency": {},
  "NodeStatusReportFrequency": {},
  "NodeLeaseDurationSeconds": 0,
  "ImageMinimumGCAge": {},
  "ImageMaximumGCAge": {},
  "ImageGCHighThresholdPercent": 0,
  "ImageGCLowThresholdPercent": 0,
  "VolumeStatsAggPeriod": {},
  "KubeletCgroups": "string",
  "SystemCgroups": "string",
  "CgroupRoot": "string",
  "CgroupsPerQOS": false,
  "CgroupDriver": "string",
  "SingleProcessOOMKill": false,
  "CPUManagerPolicy": "string",
  "CPUManagerPolicyOptions": {},
  "CPUManagerReconcilePeriod": {},
  "MemoryManagerPolicy": "string",
  "TopologyManagerPolicy": "string",
  "TopologyManagerScope": "string",
  "TopologyManagerPolicyOptions": {},
  "QOSReserved": {},
  "RuntimeRequestTimeout": {},
  "HairpinMode": "string",
  "MaxPods": 0,
  "PodCIDR": "string",
  "PodPidsLimit": 0,
  "ResolverConfig": "string",
  "RunOnce": false,
  "CPUCFSQuota": false,
  "CPUCFSQuotaPeriod": {},
  "MaxOpenFiles": 0,
  "NodeStatusMaxImages": 0,
  "ContentType": "string",
  "KubeAPIQPS": 0,
  "KubeAPIBurst": 0,
  "SerializeImagePulls": false,
  "MaxParallelImagePulls": 0,
  "EvictionHard": {},
  "EvictionSoft": {},
  "EvictionSoftGracePeriod": {},
  "EvictionPressureTransitionPeriod": {},
  "EvictionMaxPodGracePeriod": 0,
  "EvictionMinimumReclaim": {},
  "MergeDefaultEvictionSettings": false,
  "PodsPerCore": 0,
  "EnableControllerAttachDetach": false,
  "ProtectKernelDefaults": false,
  "MakeIPTablesUtilChains": false,
  "IPTablesMasqueradeBit": 0,
  "IPTablesDropBit": 0,
  "FeatureGates": {},
  "FailSwapOn": false,
  "MemorySwap": {},
  "ContainerLogMaxSize": "string",
  "ContainerLogMaxFiles": 0,
  "ContainerLogMaxWorkers": 0,
  "ContainerLogMonitorInterval": {},
  "ConfigMapAndSecretChangeDetectionStrategy": {},
  "AllowedUnsafeSysctls": [],
  "KernelMemcgNotification": false,
  "SystemReserved": {},
  "KubeReserved": {},
  "SystemReservedCgroup": "string",
  "KubeReservedCgroup": "string",
  "EnforceNodeAllocatable": [],
  "ReservedSystemCPUs": "string",
  "ShowHiddenMetricsForVersion": "string",
  "Logging": {},
  "EnableSystemLogHandler": false,
  "EnableSystemLogQuery": false,
  "ShutdownGracePeriod": {},
  "ShutdownGracePeriodCriticalPods": {},
  "ShutdownGracePeriodByPodPriority": [],
  "ReservedMemory": [],
  "EnableProfilingHandler": false,
  "EnableDebugFlagsHandler": false,
  "SeccompDefault": false,
  "MemoryThrottlingFactor": 0.0,
  "RegisterWithTaints": [],
  "RegisterNode": false,
  "Tracing": null,
  "LocalStorageCapacityIsolation": false,
  "ContainerRuntimeEndpoint": "string",
  "ImageServiceEndpoint": "string",
  "FailCgroupV1": false,
  "CrashLoopBackOff": {},
  "UserNamespaces": null
}
```


*Определено в:* `pkg/kubelet/apis/config/types.go`


**Тип ответа:** opts


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** updateKubeletOptions


```json
{
  "deleteStateFiles": false,
  "ensureConsistentReadyNode": false
}
```


*Определено в:* `test/e2e_node/util_kubeletconfig.go`


📍 *Расположение:* `test/e2e_node/util_kubeletconfig.go:74`




## test/e2e_node/util_machineinfo_linux.go


📄 Исходный файл: `test/e2e_node/util_machineinfo_linux.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [IsCgroup2UnifiedMode](#iscgroup2unifiedmode-teste2e_nodeutil_machineinfo_linuxgo38) `:38`

- 🔗 [getCPUSiblingList](#getcpusiblinglist-teste2e_nodeutil_machineinfo_linuxgo75) `:75`

- 🔗 [getCoreSiblingList](#getcoresiblinglist-teste2e_nodeutil_machineinfo_linuxgo81) `:81`

- 🔗 [getNumaNodeCPUs](#getnumanodecpus-teste2e_nodeutil_machineinfo_linuxgo88) `:88`

- 🔗 [getUncoreCPUGroupSize](#getuncorecpugroupsize-teste2e_nodeutil_machineinfo_linuxgo62) `:62`

- 🔗 [isHTEnabled](#ishtenabled-teste2e_nodeutil_machineinfo_linuxgo42) `:42`

- 🔗 [isMultiNUMA](#ismultinuma-teste2e_nodeutil_machineinfo_linuxgo52) `:52`


</details>


[function] name: IsCgroup2UnifiedMode file: test/e2e_node/util_machineinfo_linux.go:38 returns_error: нет description: IsCgroup2UnifiedMode returns whether we are running in cgroup v2 unified mode.


### IsCgroup2UnifiedMode (test/e2e_node/util_machineinfo_linux.go:38)


IsCgroup2UnifiedMode returns whether we are running in cgroup v2 unified mode.


```go
func IsCgroup2UnifiedMode(()) ()
```


📍 *Расположение:* `test/e2e_node/util_machineinfo_linux.go:38`



---


[function] name: getCPUSiblingList file: test/e2e_node/util_machineinfo_linux.go:75 returns_error: нет description: —


### getCPUSiblingList (test/e2e_node/util_machineinfo_linux.go:75)


getCPUSiblingList is a function that performs operations based on the provided parameters and returns (cpuRes int64).


```go
func getCPUSiblingList((cpuRes int64)) (cpuRes int64)
```


**Тип ответа:** cpuRes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util_machineinfo_linux.go:75`



---


[function] name: getCoreSiblingList file: test/e2e_node/util_machineinfo_linux.go:81 returns_error: нет description: —


### getCoreSiblingList (test/e2e_node/util_machineinfo_linux.go:81)


getCoreSiblingList is a function that performs operations based on the provided parameters and returns (cpuRes int64).


```go
func getCoreSiblingList((cpuRes int64)) (cpuRes int64)
```


**Тип ответа:** cpuRes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util_machineinfo_linux.go:81`



---


[function] name: getNumaNodeCPUs file: test/e2e_node/util_machineinfo_linux.go:88 returns_error: да description: getNumaNodeCPUs retrieves CPUs for each NUMA node.


### getNumaNodeCPUs (test/e2e_node/util_machineinfo_linux.go:88)


getNumaNodeCPUs retrieves CPUs for each NUMA node.


```go
func getNumaNodeCPUs((map[int]cpuset.CPUSet, error)) (map[int]cpuset.CPUSet, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** cpuset.CPUSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[int]cpuset.CPUSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util_machineinfo_linux.go:88`



---


[function] name: getUncoreCPUGroupSize file: test/e2e_node/util_machineinfo_linux.go:62 returns_error: нет description: —


### getUncoreCPUGroupSize (test/e2e_node/util_machineinfo_linux.go:62)


getUncoreCPUGroupSize is a function that performs operations based on the provided parameters and returns ().


```go
func getUncoreCPUGroupSize(()) ()
```


📍 *Расположение:* `test/e2e_node/util_machineinfo_linux.go:62`



---


[function] name: isHTEnabled file: test/e2e_node/util_machineinfo_linux.go:42 returns_error: нет description: —


### isHTEnabled (test/e2e_node/util_machineinfo_linux.go:42)


isHTEnabled is a function that performs operations based on the provided parameters and returns ().


```go
func isHTEnabled(()) ()
```


📍 *Расположение:* `test/e2e_node/util_machineinfo_linux.go:42`



---


[function] name: isMultiNUMA file: test/e2e_node/util_machineinfo_linux.go:52 returns_error: нет description: —


### isMultiNUMA (test/e2e_node/util_machineinfo_linux.go:52)


isMultiNUMA is a function that performs operations based on the provided parameters and returns ().


```go
func isMultiNUMA(()) ()
```


📍 *Расположение:* `test/e2e_node/util_machineinfo_linux.go:52`




## test/e2e_node/util_machineinfo_unsupported.go


📄 Исходный файл: `test/e2e_node/util_machineinfo_unsupported.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [IsCgroup2UnifiedMode](#iscgroup2unifiedmode-teste2e_nodeutil_machineinfo_unsupportedgo28) `:28`

- 🔗 [getCPUSiblingList](#getcpusiblinglist-teste2e_nodeutil_machineinfo_unsupportedgo44) `:44`

- 🔗 [getCoreSiblingList](#getcoresiblinglist-teste2e_nodeutil_machineinfo_unsupportedgo48) `:48`

- 🔗 [getNumaNodeCPUs](#getnumanodecpus-teste2e_nodeutil_machineinfo_unsupportedgo53) `:53`

- 🔗 [getUncoreCPUGroupSize](#getuncorecpugroupsize-teste2e_nodeutil_machineinfo_unsupportedgo40) `:40`

- 🔗 [isHTEnabled](#ishtenabled-teste2e_nodeutil_machineinfo_unsupportedgo32) `:32`

- 🔗 [isMultiNUMA](#ismultinuma-teste2e_nodeutil_machineinfo_unsupportedgo36) `:36`


</details>


[function] name: IsCgroup2UnifiedMode file: test/e2e_node/util_machineinfo_unsupported.go:28 returns_error: нет description: IsCgroup2UnifiedMode returns whether we are running in cgroup v2 unified mode.


### IsCgroup2UnifiedMode (test/e2e_node/util_machineinfo_unsupported.go:28)


IsCgroup2UnifiedMode returns whether we are running in cgroup v2 unified mode.


```go
func IsCgroup2UnifiedMode(()) ()
```


📍 *Расположение:* `test/e2e_node/util_machineinfo_unsupported.go:28`



---


[function] name: getCPUSiblingList file: test/e2e_node/util_machineinfo_unsupported.go:44 returns_error: нет description: —


### getCPUSiblingList (test/e2e_node/util_machineinfo_unsupported.go:44)


getCPUSiblingList is a function that performs operations based on the provided parameters and returns (cpuRes int64).


```go
func getCPUSiblingList((cpuRes int64)) (cpuRes int64)
```


**Тип ответа:** cpuRes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util_machineinfo_unsupported.go:44`



---


[function] name: getCoreSiblingList file: test/e2e_node/util_machineinfo_unsupported.go:48 returns_error: нет description: —


### getCoreSiblingList (test/e2e_node/util_machineinfo_unsupported.go:48)


getCoreSiblingList is a function that performs operations based on the provided parameters and returns (cpuRes int64).


```go
func getCoreSiblingList((cpuRes int64)) (cpuRes int64)
```


**Тип ответа:** cpuRes


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `test/e2e_node/util_machineinfo_unsupported.go:48`



---


[function] name: getNumaNodeCPUs file: test/e2e_node/util_machineinfo_unsupported.go:53 returns_error: да description: getNumaNodeCPUs retrieves CPUs for each NUMA node.


### getNumaNodeCPUs (test/e2e_node/util_machineinfo_unsupported.go:53)


getNumaNodeCPUs retrieves CPUs for each NUMA node.


```go
func getNumaNodeCPUs((map[int]cpuset.CPUSet, error)) (map[int]cpuset.CPUSet, error)
```


**Тип ответа:** map


```json
{
  "compilationResults": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/authentication/cel/mapper.go`


**Тип ответа:** cpuset.CPUSet


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `map[int]cpuset.CPUSet`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util_machineinfo_unsupported.go:53`



---


[function] name: getUncoreCPUGroupSize file: test/e2e_node/util_machineinfo_unsupported.go:40 returns_error: нет description: —


### getUncoreCPUGroupSize (test/e2e_node/util_machineinfo_unsupported.go:40)


getUncoreCPUGroupSize is a function that performs operations based on the provided parameters and returns ().


```go
func getUncoreCPUGroupSize(()) ()
```


📍 *Расположение:* `test/e2e_node/util_machineinfo_unsupported.go:40`



---


[function] name: isHTEnabled file: test/e2e_node/util_machineinfo_unsupported.go:32 returns_error: нет description: —


### isHTEnabled (test/e2e_node/util_machineinfo_unsupported.go:32)


isHTEnabled is a function that performs operations based on the provided parameters and returns ().


```go
func isHTEnabled(()) ()
```


📍 *Расположение:* `test/e2e_node/util_machineinfo_unsupported.go:32`



---


[function] name: isMultiNUMA file: test/e2e_node/util_machineinfo_unsupported.go:36 returns_error: нет description: —


### isMultiNUMA (test/e2e_node/util_machineinfo_unsupported.go:36)


isMultiNUMA is a function that performs operations based on the provided parameters and returns ().


```go
func isMultiNUMA(()) ()
```


📍 *Расположение:* `test/e2e_node/util_machineinfo_unsupported.go:36`




## test/e2e_node/util_sriov.go


📄 Исходный файл: `test/e2e_node/util_sriov.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [requireSRIOVDevices](#requiresriovdevices-teste2e_nodeutil_sriovgo35) `:35`


</details>


[function] name: requireSRIOVDevices file: test/e2e_node/util_sriov.go:35 returns_error: нет description: —


### requireSRIOVDevices (test/e2e_node/util_sriov.go:35)


requireSRIOVDevices is a function that performs operations based on the provided parameters and returns ().


```go
func requireSRIOVDevices(()) ()
```


📍 *Расположение:* `test/e2e_node/util_sriov.go:35`




## test/e2e_node/util_sriov_linux.go


📄 Исходный файл: `test/e2e_node/util_sriov_linux.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [countSRIOVDevices](#countsriovdevices-teste2e_nodeutil_sriov_linuxgo29) `:29`


</details>


[function] name: countSRIOVDevices file: test/e2e_node/util_sriov_linux.go:29 returns_error: да description: countSRIOVDevices provides a rough estimate of SRIOV Virtual Functions available on the system.
This is a rough check we


### countSRIOVDevices (test/e2e_node/util_sriov_linux.go:29)


countSRIOVDevices provides a rough estimate of SRIOV Virtual Functions available on the system.
This is a rough check we use to rule out unsuitable systems, not to detect suitable systems.


```go
func countSRIOVDevices((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util_sriov_linux.go:29`




## test/e2e_node/util_sriov_unsupported.go


📄 Исходный файл: `test/e2e_node/util_sriov_unsupported.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [countSRIOVDevices](#countsriovdevices-teste2e_nodeutil_sriov_unsupportedgo21) `:21`


</details>


[function] name: countSRIOVDevices file: test/e2e_node/util_sriov_unsupported.go:21 returns_error: да description: —


### countSRIOVDevices (test/e2e_node/util_sriov_unsupported.go:21)


countSRIOVDevices is a function that performs operations based on the provided parameters and may return an error.


```go
func countSRIOVDevices((int, error)) (int, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `int`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `test/e2e_node/util_sriov_unsupported.go:21`




## test/e2e_node/util_xfs_linux.go


📄 Исходный файл: `test/e2e_node/util_xfs_linux.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [detectMountpoint](#detectmountpoint-teste2e_nodeutil_xfs_linuxgo28) `:28`

- 🔗 [isXfs](#isxfs-teste2e_nodeutil_xfs_linuxgo63) `:63`


</details>


[function] name: detectMountpoint file: test/e2e_node/util_xfs_linux.go:28 returns_error: нет description: —


### detectMountpoint (test/e2e_node/util_xfs_linux.go:28)


detectMountpoint is a function that performs operations based on the provided parameters and returns (m mount.Interface, path string).


```go
func detectMountpoint((m mount.Interface, path string)) (m mount.Interface, path string)
```


**Тип ответа:** m


```json
{
  "Name": "string",
  "Shorthand": "string",
  "DefaultValue": "string",
  "Usage": "string"
}
```


*Определено в:* `cmd/genyaml/gen_kubectl_yaml.go`


**Тип ответа:** mount.Interface


```json
{
  "clients": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/custom_metrics/multi_client.go`


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


📍 *Расположение:* `test/e2e_node/util_xfs_linux.go:28`



---


[function] name: isXfs file: test/e2e_node/util_xfs_linux.go:63 returns_error: нет description: XFS over-allocates and then eventually removes that excess allocation.
That can lead to a file growing beyond its eventu


### isXfs (test/e2e_node/util_xfs_linux.go:63)


XFS over-allocates and then eventually removes that excess allocation.
That can lead to a file growing beyond its eventual size, causing
an unnecessary eviction:

% ls -ls
total 32704
32704 -rw-r--r-- 1 rkrawitz rkrawitz 20971520 Jan 15 13:16 foo.bin

This issue can be hit regardless of the means used to count storage.
It is not present in ext4fs.


```go
func isXfs((dir string)) (dir string)
```


**Тип ответа:** dir


```json
{
  "name": "string",
  "goRestfulContainer": null,
  "nonGoRestfulMux": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/handler.go`


📍 *Расположение:* `test/e2e_node/util_xfs_linux.go:63`




## test/e2e_node/util_xfs_unsupported.go


📄 Исходный файл: `test/e2e_node/util_xfs_unsupported.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [isXfs](#isxfs-teste2e_nodeutil_xfs_unsupportedgo21) `:21`


</details>


[function] name: isXfs file: test/e2e_node/util_xfs_unsupported.go:21 returns_error: нет description: —


### isXfs (test/e2e_node/util_xfs_unsupported.go:21)


isXfs is a function that performs operations based on the provided parameters and returns (dir string).


```go
func isXfs((dir string)) (dir string)
```


**Тип ответа:** dir


```json
{
  "name": "string",
  "goRestfulContainer": null,
  "nonGoRestfulMux": null
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/handler.go`


📍 *Расположение:* `test/e2e_node/util_xfs_unsupported.go:21`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](test_e2e_kubeadm.md)

- [Следующая директория](test_fixtures.md)


---

