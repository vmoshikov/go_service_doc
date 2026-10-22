---
title: "Функции: pkg/printers"
type: functions
repo: kubernetes
language: ru
chunk_boundary: h3
group: pkg/printers
---


# Функции: pkg/printers


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_kubemark.md)

- [Следующая директория](pkg_probe.md)


---


## Меню по файлам


- 📄 [pkg/printers/interface.go](#pkgprintersinterfacego)

- 📄 [pkg/printers/internalversion/printers.go](#pkgprintersinternalversionprintersgo)

- 📄 [pkg/printers/storage/storage.go](#pkgprintersstoragestoragego)

- 📄 [pkg/printers/tablegenerator.go](#pkgprinterstablegeneratorgo)


---


## pkg/printers/interface.go


📄 Исходный файл: `pkg/printers/interface.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [PrintObj](#printobj-pkgprintersinterfacego35) `:35`


</details>


[function] name: PrintObj file: pkg/printers/interface.go:35 returns_error: нет description: PrintObj implements ResourcePrinter


### PrintObj (pkg/printers/interface.go:35)


PrintObj implements ResourcePrinter


```go
func (fn ResourcePrinterFunc) PrintObj((obj runtime.Object, w io.Writer)) (obj runtime.Object, w io.Writer)
```


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** runtime.Object


```json
{
  "Kind": "string",
  "Namespace": "string",
  "Name": "string",
  "UID": {},
  "APIVersion": "string",
  "ResourceVersion": "string",
  "FieldPath": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


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


📍 *Расположение:* `pkg/printers/interface.go:35`




## pkg/printers/internalversion/printers.go


📄 Исходный файл: `pkg/printers/internalversion/printers.go`


<details open>
<summary><b>Функции в этом файле (158)</b></summary>


- 🔗 [AddHandlers](#addhandlers-pkgprintersinternalversionprintersgo93) `:93`

- 🔗 [Len](#len-pkgprintersinternalversionprintersgo3364) `:3364`

- 🔗 [Less](#less-pkgprintersinternalversionprintersgo3372) `:3372`

- 🔗 [Swap](#swap-pkgprintersinternalversionprintersgo3368) `:3368`

- 🔗 [extractCSRStatus](#extractcsrstatus-pkgprintersinternalversionprintersgo2298) `:2298`

- 🔗 [findNodeRoles](#findnoderoles-pkgprintersinternalversionprintersgo2033) `:2033`

- 🔗 [firstNonEmpty](#firstnonempty-pkgprintersinternalversionprintersgo2791) `:2791`

- 🔗 [formatDiscoveryEndpoints](#formatdiscoveryendpoints-pkgprintersinternalversionprintersgo822) `:822`

- 🔗 [formatDiscoveryPorts](#formatdiscoveryports-pkgprintersinternalversionprintersgo800) `:800`

- 🔗 [formatEndpoints](#formatendpoints-pkgprintersinternalversionprintersgo749) `:749`

- 🔗 [formatEventSource](#formateventsource-pkgprintersinternalversionprintersgo2784) `:2784`

- 🔗 [formatEventSourceComponentInstance](#formateventsourcecomponentinstance-pkgprintersinternalversionprintersgo2800) `:2800`

- 🔗 [formatHPAMetrics](#formathpametrics-pkgprintersinternalversionprintersgo2474) `:2474`

- 🔗 [formatHosts](#formathosts-pkgprintersinternalversionprintersgo1423) `:1423`

- 🔗 [formatPorts](#formatports-pkgprintersinternalversionprintersgo1445) `:1445`

- 🔗 [formatResourceName](#formatresourcename-pkgprintersinternalversionprintersgo2843) `:2843`

- 🔗 [formatStorageVersions](#formatstorageversions-pkgprintersinternalversionprintersgo3030) `:3030`

- 🔗 [getNodeExternalIP](#getnodeexternalip-pkgprintersinternalversionprintersgo2008) `:2008`

- 🔗 [getNodeInternalIP](#getnodeinternalip-pkgprintersinternalversionprintersgo2019) `:2019`

- 🔗 [getServiceExternalIP](#getserviceexternalip-pkgprintersinternalversionprintersgo1343) `:1343`

- 🔗 [hasJobCondition](#hasjobcondition-pkgprintersinternalversionprintersgo1096) `:1096`

- 🔗 [hasPodReadyCondition](#haspodreadycondition-pkgprintersinternalversionprintersgo1087) `:1087`

- 🔗 [ingressLoadBalancerStatusStringer](#ingressloadbalancerstatusstringer-pkgprintersinternalversionprintersgo1470) `:1470`

- 🔗 [isPodInitializedConditionTrue](#ispodinitializedconditiontrue-pkgprintersinternalversionprintersgo3376) `:3376`

- 🔗 [layoutContainerCells](#layoutcontainercells-pkgprintersinternalversionprintersgo2767) `:2767`

- 🔗 [listWithMoreString](#listwithmorestring-pkgprintersinternalversionprintersgo840) `:840`

- 🔗 [loadBalancerStatusStringer](#loadbalancerstatusstringer-pkgprintersinternalversionprintersgo1325) `:1325`

- 🔗 [makePortString](#makeportstring-pkgprintersinternalversionprintersgo1375) `:1375`

- 🔗 [printBool](#printbool-pkgprintersinternalversionprintersgo3353) `:3353`

- 🔗 [printBoolPtr](#printboolptr-pkgprintersinternalversionprintersgo3345) `:3345`

- 🔗 [printCSIDriver](#printcsidriver-pkgprintersinternalversionprintersgo1652) `:1652`

- 🔗 [printCSIDriverList](#printcsidriverlist-pkgprintersinternalversionprintersgo1698) `:1698`

- 🔗 [printCSINode](#printcsinode-pkgprintersinternalversionprintersgo1632) `:1632`

- 🔗 [printCSINodeList](#printcsinodelist-pkgprintersinternalversionprintersgo1640) `:1640`

- 🔗 [printCSIStorageCapacity](#printcsistoragecapacity-pkgprintersinternalversionprintersgo1710) `:1710`

- 🔗 [printCSIStorageCapacityList](#printcsistoragecapacitylist-pkgprintersinternalversionprintersgo1724) `:1724`

- 🔗 [printCertificateSigningRequest](#printcertificatesigningrequest-pkgprintersinternalversionprintersgo2281) `:2281`

- 🔗 [printCertificateSigningRequestList](#printcertificatesigningrequestlist-pkgprintersinternalversionprintersgo2328) `:2328`

- 🔗 [printClusterRoleBinding](#printclusterrolebinding-pkgprintersinternalversionprintersgo2254) `:2254`

- 🔗 [printClusterRoleBindingList](#printclusterrolebindinglist-pkgprintersinternalversionprintersgo2269) `:2269`

- 🔗 [printClusterTrustBundle](#printclustertrustbundle-pkgprintersinternalversionprintersgo2340) `:2340`

- 🔗 [printClusterTrustBundleList](#printclustertrustbundlelist-pkgprintersinternalversionprintersgo2352) `:2352`

- 🔗 [printComponentStatus](#printcomponentstatus-pkgprintersinternalversionprintersgo2402) `:2402`

- 🔗 [printComponentStatusList](#printcomponentstatuslist-pkgprintersinternalversionprintersgo2425) `:2425`

- 🔗 [printConfigMap](#printconfigmap-pkgprintersinternalversionprintersgo2606) `:2606`

- 🔗 [printConfigMapList](#printconfigmaplist-pkgprintersinternalversionprintersgo2614) `:2614`

- 🔗 [printControllerRevision](#printcontrollerrevision-pkgprintersinternalversionprintersgo2807) `:2807`

- 🔗 [printControllerRevisionList](#printcontrollerrevisionlist-pkgprintersinternalversionprintersgo2829) `:2829`

- 🔗 [printCronJob](#printcronjob-pkgprintersinternalversionprintersgo1288) `:1288`

- 🔗 [printCronJobList](#printcronjoblist-pkgprintersinternalversionprintersgo1311) `:1311`

- 🔗 [printDaemonSet](#printdaemonset-pkgprintersinternalversionprintersgo1561) `:1561`

- 🔗 [printDaemonSetList](#printdaemonsetlist-pkgprintersinternalversionprintersgo1580) `:1580`

- 🔗 [printDeployment](#printdeployment-pkgprintersinternalversionprintersgo2437) `:2437`

- 🔗 [printDeploymentList](#printdeploymentlist-pkgprintersinternalversionprintersgo2462) `:2462`

- 🔗 [printDeviceClass](#printdeviceclass-pkgprintersinternalversionprintersgo3157) `:3157`

- 🔗 [printDeviceClassList](#printdeviceclasslist-pkgprintersinternalversionprintersgo3166) `:3166`

- 🔗 [printDeviceTaint](#printdevicetaint-pkgprintersinternalversionprintersgo3263) `:3263`

- 🔗 [printDeviceTaintRuleList](#printdevicetaintrulelist-pkgprintersinternalversionprintersgo3277) `:3277`

- 🔗 [printEndpointSlice](#printendpointslice-pkgprintersinternalversionprintersgo1612) `:1612`

- 🔗 [printEndpointSliceList](#printendpointslicelist-pkgprintersinternalversionprintersgo1620) `:1620`

- 🔗 [printEndpoints](#printendpoints-pkgprintersinternalversionprintersgo1592) `:1592`

- 🔗 [printEndpointsList](#printendpointslist-pkgprintersinternalversionprintersgo1600) `:1600`

- 🔗 [printEvent](#printevent-pkgprintersinternalversionprintersgo2158) `:2158`

- 🔗 [printEventList](#printeventlist-pkgprintersinternalversionprintersgo2215) `:2215`

- 🔗 [printFlowSchema](#printflowschema-pkgprintersinternalversionprintersgo2978) `:2978`

- 🔗 [printFlowSchemaList](#printflowschemalist-pkgprintersinternalversionprintersgo3001) `:3001`

- 🔗 [printHorizontalPodAutoscaler](#printhorizontalpodautoscaler-pkgprintersinternalversionprintersgo2575) `:2575`

- 🔗 [printHorizontalPodAutoscalerList](#printhorizontalpodautoscalerlist-pkgprintersinternalversionprintersgo2594) `:2594`

- 🔗 [printIPAddress](#printipaddress-pkgprintersinternalversionprintersgo3114) `:3114`

- 🔗 [printIPAddressList](#printipaddresslist-pkgprintersinternalversionprintersgo3137) `:3137`

- 🔗 [printIngress](#printingress-pkgprintersinternalversionprintersgo1452) `:1452`

- 🔗 [printIngressClass](#printingressclass-pkgprintersinternalversionprintersgo1500) `:1500`

- 🔗 [printIngressClassList](#printingressclasslist-pkgprintersinternalversionprintersgo1522) `:1522`

- 🔗 [printIngressList](#printingresslist-pkgprintersinternalversionprintersgo1488) `:1488`

- 🔗 [printJob](#printjob-pkgprintersinternalversionprintersgo1224) `:1224`

- 🔗 [printJobList](#printjoblist-pkgprintersinternalversionprintersgo1276) `:1276`

- 🔗 [printLease](#printlease-pkgprintersinternalversionprintersgo2711) `:2711`

- 🔗 [printLeaseCandidate](#printleasecandidate-pkgprintersinternalversionprintersgo2736) `:2736`

- 🔗 [printLeaseCandidateList](#printleasecandidatelist-pkgprintersinternalversionprintersgo2745) `:2745`

- 🔗 [printLeaseList](#printleaselist-pkgprintersinternalversionprintersgo2724) `:2724`

- 🔗 [printMutatingAdmissionPolicy](#printmutatingadmissionpolicy-pkgprintersinternalversionprintersgo1834) `:1834`

- 🔗 [printMutatingAdmissionPolicyBinding](#printmutatingadmissionpolicybinding-pkgprintersinternalversionprintersgo1858) `:1858`

- 🔗 [printMutatingAdmissionPolicyBindingList](#printmutatingadmissionpolicybindinglist-pkgprintersinternalversionprintersgo1880) `:1880`

- 🔗 [printMutatingAdmissionPolicyList](#printmutatingadmissionpolicylist-pkgprintersinternalversionprintersgo1846) `:1846`

- 🔗 [printMutatingWebhook](#printmutatingwebhook-pkgprintersinternalversionprintersgo1736) `:1736`

- 🔗 [printMutatingWebhookList](#printmutatingwebhooklist-pkgprintersinternalversionprintersgo1744) `:1744`

- 🔗 [printNamespace](#printnamespace-pkgprintersinternalversionprintersgo1892) `:1892`

- 🔗 [printNamespaceList](#printnamespacelist-pkgprintersinternalversionprintersgo1900) `:1900`

- 🔗 [printNetworkPolicy](#printnetworkpolicy-pkgprintersinternalversionprintersgo2626) `:2626`

- 🔗 [printNetworkPolicyList](#printnetworkpolicylist-pkgprintersinternalversionprintersgo2634) `:2634`

- 🔗 [printNode](#printnode-pkgprintersinternalversionprintersgo1952) `:1952`

- 🔗 [printNodeList](#printnodelist-pkgprintersinternalversionprintersgo2049) `:2049`

- 🔗 [printPersistentVolume](#printpersistentvolume-pkgprintersinternalversionprintersgo2061) `:2061`

- 🔗 [printPersistentVolumeClaim](#printpersistentvolumeclaim-pkgprintersinternalversionprintersgo2111) `:2111`

- 🔗 [printPersistentVolumeClaimList](#printpersistentvolumeclaimlist-pkgprintersinternalversionprintersgo2146) `:2146`

- 🔗 [printPersistentVolumeList](#printpersistentvolumelist-pkgprintersinternalversionprintersgo2099) `:2099`

- 🔗 [printPod](#printpod-pkgprintersinternalversionprintersgo898) `:898`

- 🔗 [printPodCertificateRequest](#printpodcertificaterequest-pkgprintersinternalversionprintersgo2364) `:2364`

- 🔗 [printPodCertificateRequestList](#printpodcertificaterequestlist-pkgprintersinternalversionprintersgo2390) `:2390`

- 🔗 [printPodDisruptionBudget](#printpoddisruptionbudget-pkgprintersinternalversionprintersgo1126) `:1126`

- 🔗 [printPodDisruptionBudgetList](#printpoddisruptionbudgetlist-pkgprintersinternalversionprintersgo1149) `:1149`

- 🔗 [printPodList](#printpodlist-pkgprintersinternalversionprintersgo886) `:886`

- 🔗 [printPodTemplate](#printpodtemplate-pkgprintersinternalversionprintersgo1105) `:1105`

- 🔗 [printPodTemplateList](#printpodtemplatelist-pkgprintersinternalversionprintersgo1114) `:1114`

- 🔗 [printPriorityClass](#printpriorityclass-pkgprintersinternalversionprintersgo2895) `:2895`

- 🔗 [printPriorityClassList](#printpriorityclasslist-pkgprintersinternalversionprintersgo2914) `:2914`

- 🔗 [printPriorityLevelConfiguration](#printprioritylevelconfiguration-pkgprintersinternalversionprintersgo3058) `:3058`

- 🔗 [printPriorityLevelConfigurationList](#printprioritylevelconfigurationlist-pkgprintersinternalversionprintersgo3080) `:3080`

- 🔗 [printReplicaSet](#printreplicaset-pkgprintersinternalversionprintersgo1195) `:1195`

- 🔗 [printReplicaSetList](#printreplicasetlist-pkgprintersinternalversionprintersgo1212) `:1212`

- 🔗 [printReplicationController](#printreplicationcontroller-pkgprintersinternalversionprintersgo1162) `:1162`

- 🔗 [printReplicationControllerList](#printreplicationcontrollerlist-pkgprintersinternalversionprintersgo1183) `:1183`

- 🔗 [printResourceClaim](#printresourceclaim-pkgprintersinternalversionprintersgo3178) `:3178`

- 🔗 [printResourceClaimList](#printresourceclaimlist-pkgprintersinternalversionprintersgo3205) `:3205`

- 🔗 [printResourceClaimTemplate](#printresourceclaimtemplate-pkgprintersinternalversionprintersgo3217) `:3217`

- 🔗 [printResourceClaimTemplateList](#printresourceclaimtemplatelist-pkgprintersinternalversionprintersgo3226) `:3226`

- 🔗 [printResourceQuota](#printresourcequota-pkgprintersinternalversionprintersgo2851) `:2851`

- 🔗 [printResourceQuotaList](#printresourcequotalist-pkgprintersinternalversionprintersgo2883) `:2883`

- 🔗 [printResourceSlice](#printresourceslice-pkgprintersinternalversionprintersgo3238) `:3238`

- 🔗 [printResourceSliceList](#printresourceslicelist-pkgprintersinternalversionprintersgo3251) `:3251`

- 🔗 [printRoleBinding](#printrolebinding-pkgprintersinternalversionprintersgo2227) `:2227`

- 🔗 [printRoleBindingList](#printrolebindinglist-pkgprintersinternalversionprintersgo2242) `:2242`

- 🔗 [printRuntimeClass](#printruntimeclass-pkgprintersinternalversionprintersgo2926) `:2926`

- 🔗 [printRuntimeClassList](#printruntimeclasslist-pkgprintersinternalversionprintersgo2938) `:2938`

- 🔗 [printScale](#printscale-pkgprintersinternalversionprintersgo3149) `:3149`

- 🔗 [printSecret](#printsecret-pkgprintersinternalversionprintersgo1912) `:1912`

- 🔗 [printSecretList](#printsecretlist-pkgprintersinternalversionprintersgo1920) `:1920`

- 🔗 [printService](#printservice-pkgprintersinternalversionprintersgo1387) `:1387`

- 🔗 [printServiceAccount](#printserviceaccount-pkgprintersinternalversionprintersgo1932) `:1932`

- 🔗 [printServiceAccountList](#printserviceaccountlist-pkgprintersinternalversionprintersgo1940) `:1940`

- 🔗 [printServiceCIDR](#printservicecidr-pkgprintersinternalversionprintersgo3092) `:3092`

- 🔗 [printServiceCIDRList](#printservicecidrlist-pkgprintersinternalversionprintersgo3102) `:3102`

- 🔗 [printServiceList](#printservicelist-pkgprintersinternalversionprintersgo1411) `:1411`

- 🔗 [printStatefulSet](#printstatefulset-pkgprintersinternalversionprintersgo1534) `:1534`

- 🔗 [printStatefulSetList](#printstatefulsetlist-pkgprintersinternalversionprintersgo1549) `:1549`

- 🔗 [printStatus](#printstatus-pkgprintersinternalversionprintersgo2757) `:2757`

- 🔗 [printStorageClass](#printstorageclass-pkgprintersinternalversionprintersgo2646) `:2646`

- 🔗 [printStorageClassList](#printstorageclasslist-pkgprintersinternalversionprintersgo2677) `:2677`

- 🔗 [printStorageVersion](#printstorageversion-pkgprintersinternalversionprintersgo3018) `:3018`

- 🔗 [printStorageVersionList](#printstorageversionlist-pkgprintersinternalversionprintersgo3046) `:3046`

- 🔗 [printStorageVersionMigration](#printstorageversionmigration-pkgprintersinternalversionprintersgo3289) `:3289`

- 🔗 [printStorageVersionMigrationList](#printstorageversionmigrationlist-pkgprintersinternalversionprintersgo3311) `:3311`

- 🔗 [printValidatingAdmissionPolicy](#printvalidatingadmissionpolicy-pkgprintersinternalversionprintersgo1776) `:1776`

- 🔗 [printValidatingAdmissionPolicyBinding](#printvalidatingadmissionpolicybinding-pkgprintersinternalversionprintersgo1800) `:1800`

- 🔗 [printValidatingAdmissionPolicyBindingList](#printvalidatingadmissionpolicybindinglist-pkgprintersinternalversionprintersgo1822) `:1822`

- 🔗 [printValidatingAdmissionPolicyList](#printvalidatingadmissionpolicylist-pkgprintersinternalversionprintersgo1788) `:1788`

- 🔗 [printValidatingWebhook](#printvalidatingwebhook-pkgprintersinternalversionprintersgo1756) `:1756`

- 🔗 [printValidatingWebhookList](#printvalidatingwebhooklist-pkgprintersinternalversionprintersgo1764) `:1764`

- 🔗 [printVolumeAttachment](#printvolumeattachment-pkgprintersinternalversionprintersgo2951) `:2951`

- 🔗 [printVolumeAttachmentList](#printvolumeattachmentlist-pkgprintersinternalversionprintersgo2966) `:2966`

- 🔗 [printVolumeAttributesClass](#printvolumeattributesclass-pkgprintersinternalversionprintersgo2689) `:2689`

- 🔗 [printVolumeAttributesClassList](#printvolumeattributesclasslist-pkgprintersinternalversionprintersgo2699) `:2699`

- 🔗 [printWorkload](#printworkload-pkgprintersinternalversionprintersgo3324) `:3324`

- 🔗 [printWorkloadList](#printworkloadlist-pkgprintersinternalversionprintersgo3334) `:3334`

- 🔗 [resourceClaimState](#resourceclaimstate-pkgprintersinternalversionprintersgo3187) `:3187`

- 🔗 [translateMicroTimestampSince](#translatemicrotimestampsince-pkgprintersinternalversionprintersgo853) `:853`

- 🔗 [translateTimestampSince](#translatetimestampsince-pkgprintersinternalversionprintersgo863) `:863`

- 🔗 [translateTimestampUntil](#translatetimestampuntil-pkgprintersinternalversionprintersgo873) `:873`


</details>


[function] name: AddHandlers file: pkg/printers/internalversion/printers.go:93 returns_error: нет description: AddHandlers adds print handlers for default Kubernetes types dealing with internal versions.


### AddHandlers (pkg/printers/internalversion/printers.go:93)


AddHandlers adds print handlers for default Kubernetes types dealing with internal versions.


```go
func AddHandlers((h printers.PrintHandler)) (h printers.PrintHandler)
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


**Тип ответа:** printers.PrintHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:93`



---


[function] name: Len file: pkg/printers/internalversion/printers.go:3364 returns_error: нет description: —


### Len (pkg/printers/internalversion/printers.go:3364)


Len is a method that performs operations based on the provided parameters and returns ().


```go
func (list SortableResourceNames) Len(()) ()
```


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3364`



---


[function] name: Less file: pkg/printers/internalversion/printers.go:3372 returns_error: нет description: —


### Less (pkg/printers/internalversion/printers.go:3372)


Less is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (list SortableResourceNames) Less((i, j int)) (i, j int)
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


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3372`



---


[function] name: Swap file: pkg/printers/internalversion/printers.go:3368 returns_error: нет description: —


### Swap (pkg/printers/internalversion/printers.go:3368)


Swap is a method that performs operations based on the provided parameters and returns (i, j int).


```go
func (list SortableResourceNames) Swap((i, j int)) (i, j int)
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


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3368`



---


[function] name: extractCSRStatus file: pkg/printers/internalversion/printers.go:2298 returns_error: нет description: —


### extractCSRStatus (pkg/printers/internalversion/printers.go:2298)


extractCSRStatus is a function that performs operations based on the provided parameters and returns (csr *certificates.CertificateSigningRequest).


```go
func extractCSRStatus((csr *certificates.CertificateSigningRequest)) (csr *certificates.CertificateSigningRequest)
```


**Тип запроса:** certificates.CertificateSigningRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/certificates/types.go`


**Тип ответа:** csr


```json
{
  "recognize": {},
  "permission": {},
  "successMessage": "string"
}
```


*Определено в:* `pkg/controller/certificates/approver/sarapprove.go`


**Тип ответа:** certificates.CertificateSigningRequest


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/certificates/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2298`



---


[function] name: findNodeRoles file: pkg/printers/internalversion/printers.go:2033 returns_error: нет description: findNodeRoles returns the roles of a given node.
The roles are determined by looking for:
* a node-role.kubernetes.io/<r


### findNodeRoles (pkg/printers/internalversion/printers.go:2033)


findNodeRoles returns the roles of a given node.
The roles are determined by looking for:
* a node-role.kubernetes.io/<role>="" label
* a kubernetes.io/role="<role>" label


```go
func findNodeRoles((node *api.Node)) (node *api.Node)
```


**Тип запроса:** api.Node


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


**Тип ответа:** api.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2033`



---


[function] name: firstNonEmpty file: pkg/printers/internalversion/printers.go:2791 returns_error: нет description: —


### firstNonEmpty (pkg/printers/internalversion/printers.go:2791)


firstNonEmpty is a function that performs operations based on the provided parameters and returns (ss ...string).


```go
func firstNonEmpty((ss ...string)) (ss ...string)
```


**Тип ответа:** ss


```json
{
  "incomingImports": {},
  "transitiveIncomingImports": {}
}
```


*Определено в:* `cmd/import-boss/main.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2791`



---


[function] name: formatDiscoveryEndpoints file: pkg/printers/internalversion/printers.go:822 returns_error: нет description: —


### formatDiscoveryEndpoints (pkg/printers/internalversion/printers.go:822)


formatDiscoveryEndpoints is a function that performs operations based on the provided parameters and returns (endpoints []discovery.Endpoint).


```go
func formatDiscoveryEndpoints((endpoints []discovery.Endpoint)) (endpoints []discovery.Endpoint)
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


📍 *Расположение:* `pkg/printers/internalversion/printers.go:822`



---


[function] name: formatDiscoveryPorts file: pkg/printers/internalversion/printers.go:800 returns_error: нет description: —


### formatDiscoveryPorts (pkg/printers/internalversion/printers.go:800)


formatDiscoveryPorts is a function that performs operations based on the provided parameters and returns (ports []discovery.EndpointPort).


```go
func formatDiscoveryPorts((ports []discovery.EndpointPort)) (ports []discovery.EndpointPort)
```


**Тип ответа:** ports


```json
{
  "Verbs": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/discovery/helper.go`


**Тип ответа:** discovery.EndpointPort


```json
{
  "Name": "string",
  "Protocol": null,
  "Port": 0,
  "AppProtocol": "string"
}
```


*Определено в:* `pkg/apis/discovery/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:800`



---


[function] name: formatEndpoints file: pkg/printers/internalversion/printers.go:749 returns_error: нет description: Pass ports=nil for all ports.


### formatEndpoints (pkg/printers/internalversion/printers.go:749)


Pass ports=nil for all ports.


```go
func formatEndpoints((endpoints *api.Endpoints, ports sets.String)) (endpoints *api.Endpoints, ports sets.String)
```


**Тип запроса:** api.Endpoints


```json
{
  "Subsets": []
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


**Тип ответа:** api.Endpoints


```json
{
  "Subsets": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** ports


```json
{
  "Verbs": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/discovery/helper.go`


**Тип ответа:** sets.String


```json
{
  "ID": "string",
  "Secret": "string"
}
```


*Определено в:* `cmd/kubeadm/app/apis/bootstraptoken/v1/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:749`



---


[function] name: formatEventSource file: pkg/printers/internalversion/printers.go:2784 returns_error: нет description: formatEventSource formats EventSource as a comma separated string excluding Host when empty.
It uses reportingController


### formatEventSource (pkg/printers/internalversion/printers.go:2784)


formatEventSource formats EventSource as a comma separated string excluding Host when empty.
It uses reportingController when Source.Component is empty and reportingInstance when Source.Host is empty


```go
func formatEventSource((es api.EventSource, reportingController, reportingInstance string)) (es api.EventSource, reportingController, reportingInstance string)
```


**Тип ответа:** es


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


**Тип ответа:** api.EventSource


```json
{
  "Component": "string",
  "Host": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** reportingController


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reportingInstance


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2784`



---


[function] name: formatEventSourceComponentInstance file: pkg/printers/internalversion/printers.go:2800 returns_error: нет description: —


### formatEventSourceComponentInstance (pkg/printers/internalversion/printers.go:2800)


formatEventSourceComponentInstance is a function that performs operations based on the provided parameters and returns (component, instance string).


```go
func formatEventSourceComponentInstance((component, instance string)) (component, instance string)
```


**Тип ответа:** component


```json
{
  "name": "string",
  "args": [],
  "defaultAddr": "string",
  "defaultPort": "string",
  "endpoint": "string"
}
```


*Определено в:* `cmd/kubeadm/app/util/apiclient/wait.go`


**Тип ответа:** instance


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2800`



---


[function] name: formatHPAMetrics file: pkg/printers/internalversion/printers.go:2474 returns_error: нет description: —


### formatHPAMetrics (pkg/printers/internalversion/printers.go:2474)


formatHPAMetrics is a function that performs operations based on the provided parameters and returns (specs []autoscaling.MetricSpec, statuses []autoscaling.MetricStatus).


```go
func formatHPAMetrics((specs []autoscaling.MetricSpec, statuses []autoscaling.MetricStatus)) (specs []autoscaling.MetricSpec, statuses []autoscaling.MetricStatus)
```


**Тип ответа:** specs


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** autoscaling.MetricSpec


```json
{
  "Type": {},
  "Object": null,
  "Pods": null,
  "Resource": null,
  "ContainerResource": null,
  "External": null
}
```


*Определено в:* `pkg/apis/autoscaling/types.go`


**Тип ответа:** statuses


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** autoscaling.MetricStatus


```json
{
  "Type": {},
  "Object": null,
  "Pods": null,
  "Resource": null,
  "ContainerResource": null,
  "External": null
}
```


*Определено в:* `pkg/apis/autoscaling/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2474`



---


[function] name: formatHosts file: pkg/printers/internalversion/printers.go:1423 returns_error: нет description: —


### formatHosts (pkg/printers/internalversion/printers.go:1423)


formatHosts is a function that performs operations based on the provided parameters and returns (rules []networking.IngressRule).


```go
func formatHosts((rules []networking.IngressRule)) (rules []networking.IngressRule)
```


**Тип ответа:** rules


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** networking.IngressRule


```json
{
  "Host": "string"
}
```


*Определено в:* `pkg/apis/networking/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1423`



---


[function] name: formatPorts file: pkg/printers/internalversion/printers.go:1445 returns_error: нет description: —


### formatPorts (pkg/printers/internalversion/printers.go:1445)


formatPorts is a function that performs operations based on the provided parameters and returns (tls []networking.IngressTLS).


```go
func formatPorts((tls []networking.IngressTLS)) (tls []networking.IngressTLS)
```


**Тип ответа:** tls


```json
{
  "mu": {},
  "transports": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/transport/cache.go`


**Тип ответа:** networking.IngressTLS


```json
{
  "Hosts": [],
  "SecretName": "string"
}
```


*Определено в:* `pkg/apis/networking/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1445`



---


[function] name: formatResourceName file: pkg/printers/internalversion/printers.go:2843 returns_error: нет description: formatResourceName receives a resource kind, name, and boolean specifying
whether or not to update the current name to "


### formatResourceName (pkg/printers/internalversion/printers.go:2843)


formatResourceName receives a resource kind, name, and boolean specifying
whether or not to update the current name to "kind/name"


```go
func formatResourceName((kind schema.GroupKind, name string, withKind bool)) (kind schema.GroupKind, name string, withKind bool)
```


**Тип ответа:** kind


```json
{
  "restMapping": null
}
```


*Определено в:* `staging/src/k8s.io/kubectl/pkg/cmd/apply/applyset.go`


**Тип ответа:** schema.GroupKind


```json
{
  "Group": "string",
  "Kind": "string"
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/runtime/schema/group_version.go`


**Тип ответа:** name


```json
{
  "nodeName": "string"
}
```


*Определено в:* `cmd/kubeadm/app/preflight/checks.go`


**Тип ответа:** withKind


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2843`



---


[function] name: formatStorageVersions file: pkg/printers/internalversion/printers.go:3030 returns_error: нет description: —


### formatStorageVersions (pkg/printers/internalversion/printers.go:3030)


formatStorageVersions is a function that performs operations based on the provided parameters and returns (storageVersions []apiserverinternal.ServerStorageVersion).


```go
func formatStorageVersions((storageVersions []apiserverinternal.ServerStorageVersion)) (storageVersions []apiserverinternal.ServerStorageVersion)
```


**Тип ответа:** storageVersions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** apiserverinternal.ServerStorageVersion


```json
{
  "APIServerID": "string",
  "EncodingVersion": "string",
  "DecodableVersions": [],
  "ServedVersions": []
}
```


*Определено в:* `pkg/apis/apiserverinternal/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3030`



---


[function] name: getNodeExternalIP file: pkg/printers/internalversion/printers.go:2008 returns_error: нет description: Returns first external ip of the node or "<none>" if none is found.


### getNodeExternalIP (pkg/printers/internalversion/printers.go:2008)


Returns first external ip of the node or "<none>" if none is found.


```go
func getNodeExternalIP((node *api.Node)) (node *api.Node)
```


**Тип запроса:** api.Node


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


**Тип ответа:** api.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2008`



---


[function] name: getNodeInternalIP file: pkg/printers/internalversion/printers.go:2019 returns_error: нет description: Returns the internal IP of the node or "<none>" if none is found.


### getNodeInternalIP (pkg/printers/internalversion/printers.go:2019)


Returns the internal IP of the node or "<none>" if none is found.


```go
func getNodeInternalIP((node *api.Node)) (node *api.Node)
```


**Тип запроса:** api.Node


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


**Тип ответа:** api.Node


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2019`



---


[function] name: getServiceExternalIP file: pkg/printers/internalversion/printers.go:1343 returns_error: нет description: —


### getServiceExternalIP (pkg/printers/internalversion/printers.go:1343)


getServiceExternalIP is a function that performs operations based on the provided parameters and returns (svc *api.Service, wide bool).


```go
func getServiceExternalIP((svc *api.Service, wide bool)) (svc *api.Service, wide bool)
```


**Тип запроса:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** svc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** api.Service


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** wide


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1343`



---


[function] name: hasJobCondition file: pkg/printers/internalversion/printers.go:1096 returns_error: нет description: —


### hasJobCondition (pkg/printers/internalversion/printers.go:1096)


hasJobCondition is a function that performs operations based on the provided parameters and returns (conditions []batch.JobCondition, conditionType batch.JobConditionType).


```go
func hasJobCondition((conditions []batch.JobCondition, conditionType batch.JobConditionType)) (conditions []batch.JobCondition, conditionType batch.JobConditionType)
```


**Тип ответа:** conditions


```json
{
  "UID": null,
  "ResourceVersion": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/preconditions.go`


**Тип ответа:** batch.JobCondition


```json
{
  "Type": {},
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/batch/types.go`


**Тип ответа:** conditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** batch.JobConditionType


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1096`



---


[function] name: hasPodReadyCondition file: pkg/printers/internalversion/printers.go:1087 returns_error: нет description: —


### hasPodReadyCondition (pkg/printers/internalversion/printers.go:1087)


hasPodReadyCondition is a function that performs operations based on the provided parameters and returns (conditions []api.PodCondition).


```go
func hasPodReadyCondition((conditions []api.PodCondition)) (conditions []api.PodCondition)
```


**Тип ответа:** conditions


```json
{
  "UID": null,
  "ResourceVersion": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/applyconfigurations/meta/v1/preconditions.go`


**Тип ответа:** api.PodCondition


```json
{
  "Type": {},
  "ObservedGeneration": 0,
  "Status": {},
  "LastProbeTime": {},
  "LastTransitionTime": {},
  "Reason": "string",
  "Message": "string"
}
```


*Определено в:* `pkg/apis/core/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1087`



---


[function] name: ingressLoadBalancerStatusStringer file: pkg/printers/internalversion/printers.go:1470 returns_error: нет description: ingressLoadBalancerStatusStringer behaves mostly like a string interface and converts the given status to a string.
`wid


### ingressLoadBalancerStatusStringer (pkg/printers/internalversion/printers.go:1470)


ingressLoadBalancerStatusStringer behaves mostly like a string interface and converts the given status to a string.
`wide` indicates whether the returned value is meant for --o=wide output. If not, it's clipped to 16 bytes.


```go
func ingressLoadBalancerStatusStringer((s networking.IngressLoadBalancerStatus, wide bool)) (s networking.IngressLoadBalancerStatus, wide bool)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** networking.IngressLoadBalancerStatus


```json
{
  "Ingress": []
}
```


*Определено в:* `pkg/apis/networking/types.go`


**Тип ответа:** wide


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1470`



---


[function] name: isPodInitializedConditionTrue file: pkg/printers/internalversion/printers.go:3376 returns_error: нет description: —


### isPodInitializedConditionTrue (pkg/printers/internalversion/printers.go:3376)


isPodInitializedConditionTrue is a function that performs operations based on the provided parameters and returns (status *api.PodStatus).


```go
func isPodInitializedConditionTrue((status *api.PodStatus)) (status *api.PodStatus)
```


**Тип запроса:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


**Тип ответа:** status


```json
{
  "supportedMediaTypes": []
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`


**Тип ответа:** api.PodStatus


```json
{
  "ID": {},
  "Name": "string",
  "Namespace": "string",
  "IPs": [],
  "ContainerStatuses": [],
  "ActiveContainerStatuses": [],
  "SandboxStatuses": [],
  "TimeStamp": {}
}
```


*Определено в:* `pkg/kubelet/container/runtime.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3376`



---


[function] name: layoutContainerCells file: pkg/printers/internalversion/printers.go:2767 returns_error: нет description: Lay out all the containers on one line if use wide output.


### layoutContainerCells (pkg/printers/internalversion/printers.go:2767)


Lay out all the containers on one line if use wide output.


```go
func layoutContainerCells((names string, images string)) (names string, images string)
```


**Тип ответа:** names


```json
{
  "client": null,
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/client/external_metrics/client.go`


**Тип ответа:** images


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2767`



---


[function] name: listWithMoreString file: pkg/printers/internalversion/printers.go:840 returns_error: нет description: —


### listWithMoreString (pkg/printers/internalversion/printers.go:840)


listWithMoreString is a function that performs operations based on the provided parameters and returns (list []string, more bool, count, max int).


```go
func listWithMoreString((list []string, more bool, count, max int)) (list []string, more bool, count, max int)
```


**Тип ответа:** list


```json
{
  "parent": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/tools/cache/listwatch.go`


**Тип ответа:** more


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** count


```json
{
  "factory": {},
  "tweakListOptions": {},
  "namespace": "string"
}
```


*Определено в:* `staging/src/k8s.io/client-go/informers/core/v1/serviceaccount.go`


**Тип ответа:** max


```json
{
  "maxSeats": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/max_seats.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:840`



---


[function] name: loadBalancerStatusStringer file: pkg/printers/internalversion/printers.go:1325 returns_error: нет description: loadBalancerStatusStringer behaves mostly like a string interface and converts the given status to a string.
`wide` indi


### loadBalancerStatusStringer (pkg/printers/internalversion/printers.go:1325)


loadBalancerStatusStringer behaves mostly like a string interface and converts the given status to a string.
`wide` indicates whether the returned value is meant for --o=wide output. If not, it's clipped to 16 bytes.


```go
func loadBalancerStatusStringer((s api.LoadBalancerStatus, wide bool)) (s api.LoadBalancerStatus, wide bool)
```


**Тип ответа:** s


```json
{
  "fromVersion": "string",
  "toVersion": "string"
}
```


*Определено в:* `cmd/genfeaturegates/genfeaturegates.go`


**Тип ответа:** api.LoadBalancerStatus


```json
{
  "Ingress": []
}
```


*Определено в:* `pkg/apis/core/types.go`


**Тип ответа:** wide


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1325`



---


[function] name: makePortString file: pkg/printers/internalversion/printers.go:1375 returns_error: нет description: —


### makePortString (pkg/printers/internalversion/printers.go:1375)


makePortString is a function that performs operations based on the provided parameters and returns (ports []api.ServicePort).


```go
func makePortString((ports []api.ServicePort)) (ports []api.ServicePort)
```


**Тип ответа:** ports


```json
{
  "Verbs": []
}
```


*Определено в:* `staging/src/k8s.io/client-go/discovery/helper.go`


**Тип ответа:** api.ServicePort


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


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1375`



---


[function] name: printBool file: pkg/printers/internalversion/printers.go:3353 returns_error: нет description: —


### printBool (pkg/printers/internalversion/printers.go:3353)


printBool is a function that performs operations based on the provided parameters and returns (value bool).


```go
func printBool((value bool)) (value bool)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3353`



---


[function] name: printBoolPtr file: pkg/printers/internalversion/printers.go:3345 returns_error: нет description: —


### printBoolPtr (pkg/printers/internalversion/printers.go:3345)


printBoolPtr is a function that performs operations based on the provided parameters and returns (value *bool).


```go
func printBoolPtr((value *bool)) (value *bool)
```


**Тип ответа:** value


```json
{
  "parentValue": {}
}
```


*Определено в:* `test/e2e/framework/ginkgologger.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3345`



---


[function] name: printCSIDriver file: pkg/printers/internalversion/printers.go:1652 returns_error: да description: —


### printCSIDriver (pkg/printers/internalversion/printers.go:1652)


printCSIDriver is a function that performs operations based on the provided parameters and may return an error.


```go
func printCSIDriver(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1652`



---


[function] name: printCSIDriverList file: pkg/printers/internalversion/printers.go:1698 returns_error: да description: —


### printCSIDriverList (pkg/printers/internalversion/printers.go:1698)


printCSIDriverList is a function that performs operations based on the provided parameters and may return an error.


```go
func printCSIDriverList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1698`



---


[function] name: printCSINode file: pkg/printers/internalversion/printers.go:1632 returns_error: да description: —


### printCSINode (pkg/printers/internalversion/printers.go:1632)


printCSINode is a function that performs operations based on the provided parameters and may return an error.


```go
func printCSINode(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1632`



---


[function] name: printCSINodeList file: pkg/printers/internalversion/printers.go:1640 returns_error: да description: —


### printCSINodeList (pkg/printers/internalversion/printers.go:1640)


printCSINodeList is a function that performs operations based on the provided parameters and may return an error.


```go
func printCSINodeList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1640`



---


[function] name: printCSIStorageCapacity file: pkg/printers/internalversion/printers.go:1710 returns_error: да description: —


### printCSIStorageCapacity (pkg/printers/internalversion/printers.go:1710)


printCSIStorageCapacity is a function that performs operations based on the provided parameters and may return an error.


```go
func printCSIStorageCapacity(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1710`



---


[function] name: printCSIStorageCapacityList file: pkg/printers/internalversion/printers.go:1724 returns_error: да description: —


### printCSIStorageCapacityList (pkg/printers/internalversion/printers.go:1724)


printCSIStorageCapacityList is a function that performs operations based on the provided parameters and may return an error.


```go
func printCSIStorageCapacityList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1724`



---


[function] name: printCertificateSigningRequest file: pkg/printers/internalversion/printers.go:2281 returns_error: да description: —


### printCertificateSigningRequest (pkg/printers/internalversion/printers.go:2281)


printCertificateSigningRequest is a function that performs operations based on the provided parameters and may return an error.


```go
func printCertificateSigningRequest(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2281`



---


[function] name: printCertificateSigningRequestList file: pkg/printers/internalversion/printers.go:2328 returns_error: да description: —


### printCertificateSigningRequestList (pkg/printers/internalversion/printers.go:2328)


printCertificateSigningRequestList is a function that performs operations based on the provided parameters and may return an error.


```go
func printCertificateSigningRequestList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2328`



---


[function] name: printClusterRoleBinding file: pkg/printers/internalversion/printers.go:2254 returns_error: да description: —


### printClusterRoleBinding (pkg/printers/internalversion/printers.go:2254)


printClusterRoleBinding is a function that performs operations based on the provided parameters and may return an error.


```go
func printClusterRoleBinding(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2254`



---


[function] name: printClusterRoleBindingList file: pkg/printers/internalversion/printers.go:2269 returns_error: да description: Prints the ClusterRoleBinding in a human-friendly format.


### printClusterRoleBindingList (pkg/printers/internalversion/printers.go:2269)


Prints the ClusterRoleBinding in a human-friendly format.


```go
func printClusterRoleBindingList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2269`



---


[function] name: printClusterTrustBundle file: pkg/printers/internalversion/printers.go:2340 returns_error: да description: —


### printClusterTrustBundle (pkg/printers/internalversion/printers.go:2340)


printClusterTrustBundle is a function that performs operations based on the provided parameters and may return an error.


```go
func printClusterTrustBundle(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2340`



---


[function] name: printClusterTrustBundleList file: pkg/printers/internalversion/printers.go:2352 returns_error: да description: —


### printClusterTrustBundleList (pkg/printers/internalversion/printers.go:2352)


printClusterTrustBundleList is a function that performs operations based on the provided parameters and may return an error.


```go
func printClusterTrustBundleList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2352`



---


[function] name: printComponentStatus file: pkg/printers/internalversion/printers.go:2402 returns_error: да description: —


### printComponentStatus (pkg/printers/internalversion/printers.go:2402)


printComponentStatus is a function that performs operations based on the provided parameters and may return an error.


```go
func printComponentStatus(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2402`



---


[function] name: printComponentStatusList file: pkg/printers/internalversion/printers.go:2425 returns_error: да description: —


### printComponentStatusList (pkg/printers/internalversion/printers.go:2425)


printComponentStatusList is a function that performs operations based on the provided parameters and may return an error.


```go
func printComponentStatusList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2425`



---


[function] name: printConfigMap file: pkg/printers/internalversion/printers.go:2606 returns_error: да description: —


### printConfigMap (pkg/printers/internalversion/printers.go:2606)


printConfigMap is a function that performs operations based on the provided parameters and may return an error.


```go
func printConfigMap(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2606`



---


[function] name: printConfigMapList file: pkg/printers/internalversion/printers.go:2614 returns_error: да description: —


### printConfigMapList (pkg/printers/internalversion/printers.go:2614)


printConfigMapList is a function that performs operations based on the provided parameters and may return an error.


```go
func printConfigMapList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2614`



---


[function] name: printControllerRevision file: pkg/printers/internalversion/printers.go:2807 returns_error: да description: —


### printControllerRevision (pkg/printers/internalversion/printers.go:2807)


printControllerRevision is a function that performs operations based on the provided parameters and may return an error.


```go
func printControllerRevision(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2807`



---


[function] name: printControllerRevisionList file: pkg/printers/internalversion/printers.go:2829 returns_error: да description: —


### printControllerRevisionList (pkg/printers/internalversion/printers.go:2829)


printControllerRevisionList is a function that performs operations based on the provided parameters and may return an error.


```go
func printControllerRevisionList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2829`



---


[function] name: printCronJob file: pkg/printers/internalversion/printers.go:1288 returns_error: да description: —


### printCronJob (pkg/printers/internalversion/printers.go:1288)


printCronJob is a function that performs operations based on the provided parameters and may return an error.


```go
func printCronJob(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1288`



---


[function] name: printCronJobList file: pkg/printers/internalversion/printers.go:1311 returns_error: да description: —


### printCronJobList (pkg/printers/internalversion/printers.go:1311)


printCronJobList is a function that performs operations based on the provided parameters and may return an error.


```go
func printCronJobList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1311`



---


[function] name: printDaemonSet file: pkg/printers/internalversion/printers.go:1561 returns_error: да description: —


### printDaemonSet (pkg/printers/internalversion/printers.go:1561)


printDaemonSet is a function that performs operations based on the provided parameters and may return an error.


```go
func printDaemonSet(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1561`



---


[function] name: printDaemonSetList file: pkg/printers/internalversion/printers.go:1580 returns_error: да description: —


### printDaemonSetList (pkg/printers/internalversion/printers.go:1580)


printDaemonSetList is a function that performs operations based on the provided parameters and may return an error.


```go
func printDaemonSetList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1580`



---


[function] name: printDeployment file: pkg/printers/internalversion/printers.go:2437 returns_error: да description: —


### printDeployment (pkg/printers/internalversion/printers.go:2437)


printDeployment is a function that performs operations based on the provided parameters and may return an error.


```go
func printDeployment(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2437`



---


[function] name: printDeploymentList file: pkg/printers/internalversion/printers.go:2462 returns_error: да description: —


### printDeploymentList (pkg/printers/internalversion/printers.go:2462)


printDeploymentList is a function that performs operations based on the provided parameters and may return an error.


```go
func printDeploymentList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2462`



---


[function] name: printDeviceClass file: pkg/printers/internalversion/printers.go:3157 returns_error: да description: —


### printDeviceClass (pkg/printers/internalversion/printers.go:3157)


printDeviceClass is a function that performs operations based on the provided parameters and may return an error.


```go
func printDeviceClass(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3157`



---


[function] name: printDeviceClassList file: pkg/printers/internalversion/printers.go:3166 returns_error: да description: —


### printDeviceClassList (pkg/printers/internalversion/printers.go:3166)


printDeviceClassList is a function that performs operations based on the provided parameters and may return an error.


```go
func printDeviceClassList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3166`



---


[function] name: printDeviceTaint file: pkg/printers/internalversion/printers.go:3263 returns_error: да description: —


### printDeviceTaint (pkg/printers/internalversion/printers.go:3263)


printDeviceTaint is a function that performs operations based on the provided parameters and may return an error.


```go
func printDeviceTaint(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3263`



---


[function] name: printDeviceTaintRuleList file: pkg/printers/internalversion/printers.go:3277 returns_error: да description: —


### printDeviceTaintRuleList (pkg/printers/internalversion/printers.go:3277)


printDeviceTaintRuleList is a function that performs operations based on the provided parameters and may return an error.


```go
func printDeviceTaintRuleList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3277`



---


[function] name: printEndpointSlice file: pkg/printers/internalversion/printers.go:1612 returns_error: да description: —


### printEndpointSlice (pkg/printers/internalversion/printers.go:1612)


printEndpointSlice is a function that performs operations based on the provided parameters and may return an error.


```go
func printEndpointSlice(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1612`



---


[function] name: printEndpointSliceList file: pkg/printers/internalversion/printers.go:1620 returns_error: да description: —


### printEndpointSliceList (pkg/printers/internalversion/printers.go:1620)


printEndpointSliceList is a function that performs operations based on the provided parameters and may return an error.


```go
func printEndpointSliceList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1620`



---


[function] name: printEndpoints file: pkg/printers/internalversion/printers.go:1592 returns_error: да description: —


### printEndpoints (pkg/printers/internalversion/printers.go:1592)


printEndpoints is a function that performs operations based on the provided parameters and may return an error.


```go
func printEndpoints(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1592`



---


[function] name: printEndpointsList file: pkg/printers/internalversion/printers.go:1600 returns_error: да description: —


### printEndpointsList (pkg/printers/internalversion/printers.go:1600)


printEndpointsList is a function that performs operations based on the provided parameters and may return an error.


```go
func printEndpointsList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1600`



---


[function] name: printEvent file: pkg/printers/internalversion/printers.go:2158 returns_error: да description: —


### printEvent (pkg/printers/internalversion/printers.go:2158)


printEvent is a function that performs operations based on the provided parameters and may return an error.


```go
func printEvent(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2158`



---


[function] name: printEventList file: pkg/printers/internalversion/printers.go:2215 returns_error: да description: Sorts and prints the EventList in a human-friendly format.


### printEventList (pkg/printers/internalversion/printers.go:2215)


Sorts and prints the EventList in a human-friendly format.


```go
func printEventList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2215`



---


[function] name: printFlowSchema file: pkg/printers/internalversion/printers.go:2978 returns_error: да description: —


### printFlowSchema (pkg/printers/internalversion/printers.go:2978)


printFlowSchema is a function that performs operations based on the provided parameters and may return an error.


```go
func printFlowSchema(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2978`



---


[function] name: printFlowSchemaList file: pkg/printers/internalversion/printers.go:3001 returns_error: да description: —


### printFlowSchemaList (pkg/printers/internalversion/printers.go:3001)


printFlowSchemaList is a function that performs operations based on the provided parameters and may return an error.


```go
func printFlowSchemaList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3001`



---


[function] name: printHorizontalPodAutoscaler file: pkg/printers/internalversion/printers.go:2575 returns_error: да description: —


### printHorizontalPodAutoscaler (pkg/printers/internalversion/printers.go:2575)


printHorizontalPodAutoscaler is a function that performs operations based on the provided parameters and may return an error.


```go
func printHorizontalPodAutoscaler(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2575`



---


[function] name: printHorizontalPodAutoscalerList file: pkg/printers/internalversion/printers.go:2594 returns_error: да description: —


### printHorizontalPodAutoscalerList (pkg/printers/internalversion/printers.go:2594)


printHorizontalPodAutoscalerList is a function that performs operations based on the provided parameters and may return an error.


```go
func printHorizontalPodAutoscalerList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2594`



---


[function] name: printIPAddress file: pkg/printers/internalversion/printers.go:3114 returns_error: да description: —


### printIPAddress (pkg/printers/internalversion/printers.go:3114)


printIPAddress is a function that performs operations based on the provided parameters and may return an error.


```go
func printIPAddress(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3114`



---


[function] name: printIPAddressList file: pkg/printers/internalversion/printers.go:3137 returns_error: да description: —


### printIPAddressList (pkg/printers/internalversion/printers.go:3137)


printIPAddressList is a function that performs operations based on the provided parameters and may return an error.


```go
func printIPAddressList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3137`



---


[function] name: printIngress file: pkg/printers/internalversion/printers.go:1452 returns_error: да description: —


### printIngress (pkg/printers/internalversion/printers.go:1452)


printIngress is a function that performs operations based on the provided parameters and may return an error.


```go
func printIngress(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1452`



---


[function] name: printIngressClass file: pkg/printers/internalversion/printers.go:1500 returns_error: да description: —


### printIngressClass (pkg/printers/internalversion/printers.go:1500)


printIngressClass is a function that performs operations based on the provided parameters and may return an error.


```go
func printIngressClass(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1500`



---


[function] name: printIngressClassList file: pkg/printers/internalversion/printers.go:1522 returns_error: да description: —


### printIngressClassList (pkg/printers/internalversion/printers.go:1522)


printIngressClassList is a function that performs operations based on the provided parameters and may return an error.


```go
func printIngressClassList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1522`



---


[function] name: printIngressList file: pkg/printers/internalversion/printers.go:1488 returns_error: да description: —


### printIngressList (pkg/printers/internalversion/printers.go:1488)


printIngressList is a function that performs operations based on the provided parameters and may return an error.


```go
func printIngressList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1488`



---


[function] name: printJob file: pkg/printers/internalversion/printers.go:1224 returns_error: да description: —


### printJob (pkg/printers/internalversion/printers.go:1224)


printJob is a function that performs operations based on the provided parameters and may return an error.


```go
func printJob(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1224`



---


[function] name: printJobList file: pkg/printers/internalversion/printers.go:1276 returns_error: да description: —


### printJobList (pkg/printers/internalversion/printers.go:1276)


printJobList is a function that performs operations based on the provided parameters and may return an error.


```go
func printJobList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1276`



---


[function] name: printLease file: pkg/printers/internalversion/printers.go:2711 returns_error: да description: —


### printLease (pkg/printers/internalversion/printers.go:2711)


printLease is a function that performs operations based on the provided parameters and may return an error.


```go
func printLease(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2711`



---


[function] name: printLeaseCandidate file: pkg/printers/internalversion/printers.go:2736 returns_error: да description: —


### printLeaseCandidate (pkg/printers/internalversion/printers.go:2736)


printLeaseCandidate is a function that performs operations based on the provided parameters and may return an error.


```go
func printLeaseCandidate(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2736`



---


[function] name: printLeaseCandidateList file: pkg/printers/internalversion/printers.go:2745 returns_error: да description: —


### printLeaseCandidateList (pkg/printers/internalversion/printers.go:2745)


printLeaseCandidateList is a function that performs operations based on the provided parameters and may return an error.


```go
func printLeaseCandidateList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2745`



---


[function] name: printLeaseList file: pkg/printers/internalversion/printers.go:2724 returns_error: да description: —


### printLeaseList (pkg/printers/internalversion/printers.go:2724)


printLeaseList is a function that performs operations based on the provided parameters and may return an error.


```go
func printLeaseList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2724`



---


[function] name: printMutatingAdmissionPolicy file: pkg/printers/internalversion/printers.go:1834 returns_error: да description: —


### printMutatingAdmissionPolicy (pkg/printers/internalversion/printers.go:1834)


printMutatingAdmissionPolicy is a function that performs operations based on the provided parameters and may return an error.


```go
func printMutatingAdmissionPolicy(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1834`



---


[function] name: printMutatingAdmissionPolicyBinding file: pkg/printers/internalversion/printers.go:1858 returns_error: да description: —


### printMutatingAdmissionPolicyBinding (pkg/printers/internalversion/printers.go:1858)


printMutatingAdmissionPolicyBinding is a function that performs operations based on the provided parameters and may return an error.


```go
func printMutatingAdmissionPolicyBinding(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1858`



---


[function] name: printMutatingAdmissionPolicyBindingList file: pkg/printers/internalversion/printers.go:1880 returns_error: да description: —


### printMutatingAdmissionPolicyBindingList (pkg/printers/internalversion/printers.go:1880)


printMutatingAdmissionPolicyBindingList is a function that performs operations based on the provided parameters and may return an error.


```go
func printMutatingAdmissionPolicyBindingList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1880`



---


[function] name: printMutatingAdmissionPolicyList file: pkg/printers/internalversion/printers.go:1846 returns_error: да description: —


### printMutatingAdmissionPolicyList (pkg/printers/internalversion/printers.go:1846)


printMutatingAdmissionPolicyList is a function that performs operations based on the provided parameters and may return an error.


```go
func printMutatingAdmissionPolicyList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1846`



---


[function] name: printMutatingWebhook file: pkg/printers/internalversion/printers.go:1736 returns_error: да description: —


### printMutatingWebhook (pkg/printers/internalversion/printers.go:1736)


printMutatingWebhook is a function that performs operations based on the provided parameters and may return an error.


```go
func printMutatingWebhook(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1736`



---


[function] name: printMutatingWebhookList file: pkg/printers/internalversion/printers.go:1744 returns_error: да description: —


### printMutatingWebhookList (pkg/printers/internalversion/printers.go:1744)


printMutatingWebhookList is a function that performs operations based on the provided parameters and may return an error.


```go
func printMutatingWebhookList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1744`



---


[function] name: printNamespace file: pkg/printers/internalversion/printers.go:1892 returns_error: да description: —


### printNamespace (pkg/printers/internalversion/printers.go:1892)


printNamespace is a function that performs operations based on the provided parameters and may return an error.


```go
func printNamespace(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1892`



---


[function] name: printNamespaceList file: pkg/printers/internalversion/printers.go:1900 returns_error: да description: —


### printNamespaceList (pkg/printers/internalversion/printers.go:1900)


printNamespaceList is a function that performs operations based on the provided parameters and may return an error.


```go
func printNamespaceList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1900`



---


[function] name: printNetworkPolicy file: pkg/printers/internalversion/printers.go:2626 returns_error: да description: —


### printNetworkPolicy (pkg/printers/internalversion/printers.go:2626)


printNetworkPolicy is a function that performs operations based on the provided parameters and may return an error.


```go
func printNetworkPolicy(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2626`



---


[function] name: printNetworkPolicyList file: pkg/printers/internalversion/printers.go:2634 returns_error: да description: —


### printNetworkPolicyList (pkg/printers/internalversion/printers.go:2634)


printNetworkPolicyList is a function that performs operations based on the provided parameters and may return an error.


```go
func printNetworkPolicyList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2634`



---


[function] name: printNode file: pkg/printers/internalversion/printers.go:1952 returns_error: да description: —


### printNode (pkg/printers/internalversion/printers.go:1952)


printNode is a function that performs operations based on the provided parameters and may return an error.


```go
func printNode(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1952`



---


[function] name: printNodeList file: pkg/printers/internalversion/printers.go:2049 returns_error: да description: —


### printNodeList (pkg/printers/internalversion/printers.go:2049)


printNodeList is a function that performs operations based on the provided parameters and may return an error.


```go
func printNodeList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2049`



---


[function] name: printPersistentVolume file: pkg/printers/internalversion/printers.go:2061 returns_error: да description: —


### printPersistentVolume (pkg/printers/internalversion/printers.go:2061)


printPersistentVolume is a function that performs operations based on the provided parameters and may return an error.


```go
func printPersistentVolume(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2061`



---


[function] name: printPersistentVolumeClaim file: pkg/printers/internalversion/printers.go:2111 returns_error: да description: —


### printPersistentVolumeClaim (pkg/printers/internalversion/printers.go:2111)


printPersistentVolumeClaim is a function that performs operations based on the provided parameters and may return an error.


```go
func printPersistentVolumeClaim(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2111`



---


[function] name: printPersistentVolumeClaimList file: pkg/printers/internalversion/printers.go:2146 returns_error: да description: —


### printPersistentVolumeClaimList (pkg/printers/internalversion/printers.go:2146)


printPersistentVolumeClaimList is a function that performs operations based on the provided parameters and may return an error.


```go
func printPersistentVolumeClaimList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2146`



---


[function] name: printPersistentVolumeList file: pkg/printers/internalversion/printers.go:2099 returns_error: да description: —


### printPersistentVolumeList (pkg/printers/internalversion/printers.go:2099)


printPersistentVolumeList is a function that performs operations based on the provided parameters and may return an error.


```go
func printPersistentVolumeList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2099`



---


[function] name: printPod file: pkg/printers/internalversion/printers.go:898 returns_error: да description: —


### printPod (pkg/printers/internalversion/printers.go:898)


printPod is a function that performs operations based on the provided parameters and may return an error.


```go
func printPod(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:898`



---


[function] name: printPodCertificateRequest file: pkg/printers/internalversion/printers.go:2364 returns_error: да description: —


### printPodCertificateRequest (pkg/printers/internalversion/printers.go:2364)


printPodCertificateRequest is a function that performs operations based on the provided parameters and may return an error.


```go
func printPodCertificateRequest(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2364`



---


[function] name: printPodCertificateRequestList file: pkg/printers/internalversion/printers.go:2390 returns_error: да description: —


### printPodCertificateRequestList (pkg/printers/internalversion/printers.go:2390)


printPodCertificateRequestList is a function that performs operations based on the provided parameters and may return an error.


```go
func printPodCertificateRequestList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2390`



---


[function] name: printPodDisruptionBudget file: pkg/printers/internalversion/printers.go:1126 returns_error: да description: —


### printPodDisruptionBudget (pkg/printers/internalversion/printers.go:1126)


printPodDisruptionBudget is a function that performs operations based on the provided parameters and may return an error.


```go
func printPodDisruptionBudget(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1126`



---


[function] name: printPodDisruptionBudgetList file: pkg/printers/internalversion/printers.go:1149 returns_error: да description: —


### printPodDisruptionBudgetList (pkg/printers/internalversion/printers.go:1149)


printPodDisruptionBudgetList is a function that performs operations based on the provided parameters and may return an error.


```go
func printPodDisruptionBudgetList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1149`



---


[function] name: printPodList file: pkg/printers/internalversion/printers.go:886 returns_error: да description: —


### printPodList (pkg/printers/internalversion/printers.go:886)


printPodList is a function that performs operations based on the provided parameters and may return an error.


```go
func printPodList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:886`



---


[function] name: printPodTemplate file: pkg/printers/internalversion/printers.go:1105 returns_error: да description: —


### printPodTemplate (pkg/printers/internalversion/printers.go:1105)


printPodTemplate is a function that performs operations based on the provided parameters and may return an error.


```go
func printPodTemplate(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1105`



---


[function] name: printPodTemplateList file: pkg/printers/internalversion/printers.go:1114 returns_error: да description: —


### printPodTemplateList (pkg/printers/internalversion/printers.go:1114)


printPodTemplateList is a function that performs operations based on the provided parameters and may return an error.


```go
func printPodTemplateList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1114`



---


[function] name: printPriorityClass file: pkg/printers/internalversion/printers.go:2895 returns_error: да description: —


### printPriorityClass (pkg/printers/internalversion/printers.go:2895)


printPriorityClass is a function that performs operations based on the provided parameters and may return an error.


```go
func printPriorityClass(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2895`



---


[function] name: printPriorityClassList file: pkg/printers/internalversion/printers.go:2914 returns_error: да description: —


### printPriorityClassList (pkg/printers/internalversion/printers.go:2914)


printPriorityClassList is a function that performs operations based on the provided parameters and may return an error.


```go
func printPriorityClassList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2914`



---


[function] name: printPriorityLevelConfiguration file: pkg/printers/internalversion/printers.go:3058 returns_error: да description: —


### printPriorityLevelConfiguration (pkg/printers/internalversion/printers.go:3058)


printPriorityLevelConfiguration is a function that performs operations based on the provided parameters and may return an error.


```go
func printPriorityLevelConfiguration(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3058`



---


[function] name: printPriorityLevelConfigurationList file: pkg/printers/internalversion/printers.go:3080 returns_error: да description: —


### printPriorityLevelConfigurationList (pkg/printers/internalversion/printers.go:3080)


printPriorityLevelConfigurationList is a function that performs operations based on the provided parameters and may return an error.


```go
func printPriorityLevelConfigurationList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3080`



---


[function] name: printReplicaSet file: pkg/printers/internalversion/printers.go:1195 returns_error: да description: —


### printReplicaSet (pkg/printers/internalversion/printers.go:1195)


printReplicaSet is a function that performs operations based on the provided parameters and may return an error.


```go
func printReplicaSet(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1195`



---


[function] name: printReplicaSetList file: pkg/printers/internalversion/printers.go:1212 returns_error: да description: —


### printReplicaSetList (pkg/printers/internalversion/printers.go:1212)


printReplicaSetList is a function that performs operations based on the provided parameters and may return an error.


```go
func printReplicaSetList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1212`



---


[function] name: printReplicationController file: pkg/printers/internalversion/printers.go:1162 returns_error: да description: TODO(AdoHe): try to put wide output in a single method


### printReplicationController (pkg/printers/internalversion/printers.go:1162)


TODO(AdoHe): try to put wide output in a single method


```go
func printReplicationController(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1162`



---


[function] name: printReplicationControllerList file: pkg/printers/internalversion/printers.go:1183 returns_error: да description: —


### printReplicationControllerList (pkg/printers/internalversion/printers.go:1183)


printReplicationControllerList is a function that performs operations based on the provided parameters and may return an error.


```go
func printReplicationControllerList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1183`



---


[function] name: printResourceClaim file: pkg/printers/internalversion/printers.go:3178 returns_error: да description: —


### printResourceClaim (pkg/printers/internalversion/printers.go:3178)


printResourceClaim is a function that performs operations based on the provided parameters and may return an error.


```go
func printResourceClaim(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3178`



---


[function] name: printResourceClaimList file: pkg/printers/internalversion/printers.go:3205 returns_error: да description: —


### printResourceClaimList (pkg/printers/internalversion/printers.go:3205)


printResourceClaimList is a function that performs operations based on the provided parameters and may return an error.


```go
func printResourceClaimList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3205`



---


[function] name: printResourceClaimTemplate file: pkg/printers/internalversion/printers.go:3217 returns_error: да description: —


### printResourceClaimTemplate (pkg/printers/internalversion/printers.go:3217)


printResourceClaimTemplate is a function that performs operations based on the provided parameters and may return an error.


```go
func printResourceClaimTemplate(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3217`



---


[function] name: printResourceClaimTemplateList file: pkg/printers/internalversion/printers.go:3226 returns_error: да description: —


### printResourceClaimTemplateList (pkg/printers/internalversion/printers.go:3226)


printResourceClaimTemplateList is a function that performs operations based on the provided parameters and may return an error.


```go
func printResourceClaimTemplateList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3226`



---


[function] name: printResourceQuota file: pkg/printers/internalversion/printers.go:2851 returns_error: да description: —


### printResourceQuota (pkg/printers/internalversion/printers.go:2851)


printResourceQuota is a function that performs operations based on the provided parameters and may return an error.


```go
func printResourceQuota(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2851`



---


[function] name: printResourceQuotaList file: pkg/printers/internalversion/printers.go:2883 returns_error: да description: —


### printResourceQuotaList (pkg/printers/internalversion/printers.go:2883)


printResourceQuotaList is a function that performs operations based on the provided parameters and may return an error.


```go
func printResourceQuotaList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2883`



---


[function] name: printResourceSlice file: pkg/printers/internalversion/printers.go:3238 returns_error: да description: —


### printResourceSlice (pkg/printers/internalversion/printers.go:3238)


printResourceSlice is a function that performs operations based on the provided parameters and may return an error.


```go
func printResourceSlice(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3238`



---


[function] name: printResourceSliceList file: pkg/printers/internalversion/printers.go:3251 returns_error: да description: —


### printResourceSliceList (pkg/printers/internalversion/printers.go:3251)


printResourceSliceList is a function that performs operations based on the provided parameters and may return an error.


```go
func printResourceSliceList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3251`



---


[function] name: printRoleBinding file: pkg/printers/internalversion/printers.go:2227 returns_error: да description: —


### printRoleBinding (pkg/printers/internalversion/printers.go:2227)


printRoleBinding is a function that performs operations based on the provided parameters and may return an error.


```go
func printRoleBinding(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2227`



---


[function] name: printRoleBindingList file: pkg/printers/internalversion/printers.go:2242 returns_error: да description: Prints the RoleBinding in a human-friendly format.


### printRoleBindingList (pkg/printers/internalversion/printers.go:2242)


Prints the RoleBinding in a human-friendly format.


```go
func printRoleBindingList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2242`



---


[function] name: printRuntimeClass file: pkg/printers/internalversion/printers.go:2926 returns_error: да description: —


### printRuntimeClass (pkg/printers/internalversion/printers.go:2926)


printRuntimeClass is a function that performs operations based on the provided parameters and may return an error.


```go
func printRuntimeClass(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2926`



---


[function] name: printRuntimeClassList file: pkg/printers/internalversion/printers.go:2938 returns_error: да description: —


### printRuntimeClassList (pkg/printers/internalversion/printers.go:2938)


printRuntimeClassList is a function that performs operations based on the provided parameters and may return an error.


```go
func printRuntimeClassList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2938`



---


[function] name: printScale file: pkg/printers/internalversion/printers.go:3149 returns_error: да description: —


### printScale (pkg/printers/internalversion/printers.go:3149)


printScale is a function that performs operations based on the provided parameters and may return an error.


```go
func printScale(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3149`



---


[function] name: printSecret file: pkg/printers/internalversion/printers.go:1912 returns_error: да description: —


### printSecret (pkg/printers/internalversion/printers.go:1912)


printSecret is a function that performs operations based on the provided parameters and may return an error.


```go
func printSecret(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1912`



---


[function] name: printSecretList file: pkg/printers/internalversion/printers.go:1920 returns_error: да description: —


### printSecretList (pkg/printers/internalversion/printers.go:1920)


printSecretList is a function that performs operations based on the provided parameters and may return an error.


```go
func printSecretList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1920`



---


[function] name: printService file: pkg/printers/internalversion/printers.go:1387 returns_error: да description: —


### printService (pkg/printers/internalversion/printers.go:1387)


printService is a function that performs operations based on the provided parameters and may return an error.


```go
func printService(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1387`



---


[function] name: printServiceAccount file: pkg/printers/internalversion/printers.go:1932 returns_error: да description: —


### printServiceAccount (pkg/printers/internalversion/printers.go:1932)


printServiceAccount is a function that performs operations based on the provided parameters and may return an error.


```go
func printServiceAccount(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1932`



---


[function] name: printServiceAccountList file: pkg/printers/internalversion/printers.go:1940 returns_error: да description: —


### printServiceAccountList (pkg/printers/internalversion/printers.go:1940)


printServiceAccountList is a function that performs operations based on the provided parameters and may return an error.


```go
func printServiceAccountList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1940`



---


[function] name: printServiceCIDR file: pkg/printers/internalversion/printers.go:3092 returns_error: да description: —


### printServiceCIDR (pkg/printers/internalversion/printers.go:3092)


printServiceCIDR is a function that performs operations based on the provided parameters and may return an error.


```go
func printServiceCIDR(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3092`



---


[function] name: printServiceCIDRList file: pkg/printers/internalversion/printers.go:3102 returns_error: да description: —


### printServiceCIDRList (pkg/printers/internalversion/printers.go:3102)


printServiceCIDRList is a function that performs operations based on the provided parameters and may return an error.


```go
func printServiceCIDRList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3102`



---


[function] name: printServiceList file: pkg/printers/internalversion/printers.go:1411 returns_error: да description: —


### printServiceList (pkg/printers/internalversion/printers.go:1411)


printServiceList is a function that performs operations based on the provided parameters and may return an error.


```go
func printServiceList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1411`



---


[function] name: printStatefulSet file: pkg/printers/internalversion/printers.go:1534 returns_error: да description: —


### printStatefulSet (pkg/printers/internalversion/printers.go:1534)


printStatefulSet is a function that performs operations based on the provided parameters and may return an error.


```go
func printStatefulSet(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1534`



---


[function] name: printStatefulSetList file: pkg/printers/internalversion/printers.go:1549 returns_error: да description: —


### printStatefulSetList (pkg/printers/internalversion/printers.go:1549)


printStatefulSetList is a function that performs operations based on the provided parameters and may return an error.


```go
func printStatefulSetList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1549`



---


[function] name: printStatus file: pkg/printers/internalversion/printers.go:2757 returns_error: да description: —


### printStatus (pkg/printers/internalversion/printers.go:2757)


printStatus is a function that performs operations based on the provided parameters and may return an error.


```go
func printStatus(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2757`



---


[function] name: printStorageClass file: pkg/printers/internalversion/printers.go:2646 returns_error: да description: —


### printStorageClass (pkg/printers/internalversion/printers.go:2646)


printStorageClass is a function that performs operations based on the provided parameters and may return an error.


```go
func printStorageClass(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2646`



---


[function] name: printStorageClassList file: pkg/printers/internalversion/printers.go:2677 returns_error: да description: —


### printStorageClassList (pkg/printers/internalversion/printers.go:2677)


printStorageClassList is a function that performs operations based on the provided parameters and may return an error.


```go
func printStorageClassList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2677`



---


[function] name: printStorageVersion file: pkg/printers/internalversion/printers.go:3018 returns_error: да description: —


### printStorageVersion (pkg/printers/internalversion/printers.go:3018)


printStorageVersion is a function that performs operations based on the provided parameters and may return an error.


```go
func printStorageVersion(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3018`



---


[function] name: printStorageVersionList file: pkg/printers/internalversion/printers.go:3046 returns_error: да description: —


### printStorageVersionList (pkg/printers/internalversion/printers.go:3046)


printStorageVersionList is a function that performs operations based on the provided parameters and may return an error.


```go
func printStorageVersionList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3046`



---


[function] name: printStorageVersionMigration file: pkg/printers/internalversion/printers.go:3289 returns_error: да description: —


### printStorageVersionMigration (pkg/printers/internalversion/printers.go:3289)


printStorageVersionMigration is a function that performs operations based on the provided parameters and may return an error.


```go
func printStorageVersionMigration(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3289`



---


[function] name: printStorageVersionMigrationList file: pkg/printers/internalversion/printers.go:3311 returns_error: да description: —


### printStorageVersionMigrationList (pkg/printers/internalversion/printers.go:3311)


printStorageVersionMigrationList is a function that performs operations based on the provided parameters and may return an error.


```go
func printStorageVersionMigrationList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3311`



---


[function] name: printValidatingAdmissionPolicy file: pkg/printers/internalversion/printers.go:1776 returns_error: да description: —


### printValidatingAdmissionPolicy (pkg/printers/internalversion/printers.go:1776)


printValidatingAdmissionPolicy is a function that performs operations based on the provided parameters and may return an error.


```go
func printValidatingAdmissionPolicy(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1776`



---


[function] name: printValidatingAdmissionPolicyBinding file: pkg/printers/internalversion/printers.go:1800 returns_error: да description: —


### printValidatingAdmissionPolicyBinding (pkg/printers/internalversion/printers.go:1800)


printValidatingAdmissionPolicyBinding is a function that performs operations based on the provided parameters and may return an error.


```go
func printValidatingAdmissionPolicyBinding(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1800`



---


[function] name: printValidatingAdmissionPolicyBindingList file: pkg/printers/internalversion/printers.go:1822 returns_error: да description: —


### printValidatingAdmissionPolicyBindingList (pkg/printers/internalversion/printers.go:1822)


printValidatingAdmissionPolicyBindingList is a function that performs operations based on the provided parameters and may return an error.


```go
func printValidatingAdmissionPolicyBindingList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1822`



---


[function] name: printValidatingAdmissionPolicyList file: pkg/printers/internalversion/printers.go:1788 returns_error: да description: —


### printValidatingAdmissionPolicyList (pkg/printers/internalversion/printers.go:1788)


printValidatingAdmissionPolicyList is a function that performs operations based on the provided parameters and may return an error.


```go
func printValidatingAdmissionPolicyList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1788`



---


[function] name: printValidatingWebhook file: pkg/printers/internalversion/printers.go:1756 returns_error: да description: —


### printValidatingWebhook (pkg/printers/internalversion/printers.go:1756)


printValidatingWebhook is a function that performs operations based on the provided parameters and may return an error.


```go
func printValidatingWebhook(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1756`



---


[function] name: printValidatingWebhookList file: pkg/printers/internalversion/printers.go:1764 returns_error: да description: —


### printValidatingWebhookList (pkg/printers/internalversion/printers.go:1764)


printValidatingWebhookList is a function that performs operations based on the provided parameters and may return an error.


```go
func printValidatingWebhookList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:1764`



---


[function] name: printVolumeAttachment file: pkg/printers/internalversion/printers.go:2951 returns_error: да description: —


### printVolumeAttachment (pkg/printers/internalversion/printers.go:2951)


printVolumeAttachment is a function that performs operations based on the provided parameters and may return an error.


```go
func printVolumeAttachment(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2951`



---


[function] name: printVolumeAttachmentList file: pkg/printers/internalversion/printers.go:2966 returns_error: да description: —


### printVolumeAttachmentList (pkg/printers/internalversion/printers.go:2966)


printVolumeAttachmentList is a function that performs operations based on the provided parameters and may return an error.


```go
func printVolumeAttachmentList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2966`



---


[function] name: printVolumeAttributesClass file: pkg/printers/internalversion/printers.go:2689 returns_error: да description: —


### printVolumeAttributesClass (pkg/printers/internalversion/printers.go:2689)


printVolumeAttributesClass is a function that performs operations based on the provided parameters and may return an error.


```go
func printVolumeAttributesClass(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2689`



---


[function] name: printVolumeAttributesClassList file: pkg/printers/internalversion/printers.go:2699 returns_error: да description: —


### printVolumeAttributesClassList (pkg/printers/internalversion/printers.go:2699)


printVolumeAttributesClassList is a function that performs operations based on the provided parameters and may return an error.


```go
func printVolumeAttributesClassList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:2699`



---


[function] name: printWorkload file: pkg/printers/internalversion/printers.go:3324 returns_error: да description: —


### printWorkload (pkg/printers/internalversion/printers.go:3324)


printWorkload is a function that performs operations based on the provided parameters and may return an error.


```go
func printWorkload(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3324`



---


[function] name: printWorkloadList file: pkg/printers/internalversion/printers.go:3334 returns_error: да description: —


### printWorkloadList (pkg/printers/internalversion/printers.go:3334)


printWorkloadList is a function that performs operations based on the provided parameters and may return an error.


```go
func printWorkloadList(([]metav1.TableRow, error)) ([]metav1.TableRow, error)
```


**Тип ответа:** metav1.TableRow


```json
{
  "Cells": [],
  "Conditions": [],
  "Object": {}
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]metav1.TableRow`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3334`



---


[function] name: resourceClaimState file: pkg/printers/internalversion/printers.go:3187 returns_error: нет description: —


### resourceClaimState (pkg/printers/internalversion/printers.go:3187)


resourceClaimState is a function that performs operations based on the provided parameters and returns (obj *resource.ResourceClaim).


```go
func resourceClaimState((obj *resource.ResourceClaim)) (obj *resource.ResourceClaim)
```


**Тип запроса:** resource.ResourceClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


**Тип ответа:** obj


```json
{
  "tracker": {}
}
```


*Определено в:* `staging/src/k8s.io/client-go/testing/fixture.go`


**Тип ответа:** resource.ResourceClaim


```json
{
  "Spec": {},
  "Status": {}
}
```


*Определено в:* `pkg/apis/resource/types.go`


📍 *Расположение:* `pkg/printers/internalversion/printers.go:3187`



---


[function] name: translateMicroTimestampSince file: pkg/printers/internalversion/printers.go:853 returns_error: нет description: translateMicroTimestampSince returns the elapsed time since timestamp in
human-readable approximation.


### translateMicroTimestampSince (pkg/printers/internalversion/printers.go:853)


translateMicroTimestampSince returns the elapsed time since timestamp in
human-readable approximation.


```go
func translateMicroTimestampSince((timestamp metav1.MicroTime)) (timestamp metav1.MicroTime)
```


**Тип ответа:** timestamp


```json
{
  "lastUpdatedAt": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/request/object_count_tracker.go`


**Тип ответа:** metav1.MicroTime


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/internalversion/printers.go:853`



---


[function] name: translateTimestampSince file: pkg/printers/internalversion/printers.go:863 returns_error: нет description: translateTimestampSince returns the elapsed time since timestamp in
human-readable approximation.


### translateTimestampSince (pkg/printers/internalversion/printers.go:863)


translateTimestampSince returns the elapsed time since timestamp in
human-readable approximation.


```go
func translateTimestampSince((timestamp metav1.Time)) (timestamp metav1.Time)
```


**Тип ответа:** timestamp


```json
{
  "lastUpdatedAt": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/request/object_count_tracker.go`


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


📍 *Расположение:* `pkg/printers/internalversion/printers.go:863`



---


[function] name: translateTimestampUntil file: pkg/printers/internalversion/printers.go:873 returns_error: нет description: translateTimestampUntil returns the elapsed time until timestamp in
human-readable approximation.


### translateTimestampUntil (pkg/printers/internalversion/printers.go:873)


translateTimestampUntil returns the elapsed time until timestamp in
human-readable approximation.


```go
func translateTimestampUntil((timestamp metav1.Time)) (timestamp metav1.Time)
```


**Тип ответа:** timestamp


```json
{
  "lastUpdatedAt": {}
}
```


*Определено в:* `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/request/object_count_tracker.go`


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


📍 *Расположение:* `pkg/printers/internalversion/printers.go:873`




## pkg/printers/storage/storage.go


📄 Исходный файл: `pkg/printers/storage/storage.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ConvertToTable](#converttotable-pkgprintersstoragestoragego34) `:34`


</details>


[function] name: ConvertToTable file: pkg/printers/storage/storage.go:34 returns_error: да description: ConvertToTable method - converts objects to metav1.Table objects using TableGenerator


### ConvertToTable (pkg/printers/storage/storage.go:34)


ConvertToTable method - converts objects to metav1.Table objects using TableGenerator


```go
func (c TableConvertor) ConvertToTable((*metav1.Table, error)) (*metav1.Table, error)
```


**Тип запроса:** metav1.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** metav1.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*metav1.Table`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/storage/storage.go:34`




## pkg/printers/tablegenerator.go


📄 Исходный файл: `pkg/printers/tablegenerator.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [GenerateTable](#generatetable-pkgprinterstablegeneratorgo78) `:78`

- 🔗 [NewTableGenerator](#newtablegenerator-pkgprinterstablegeneratorgo61) `:61`

- 🔗 [TableHandler](#tablehandler-pkgprinterstablegeneratorgo125) `:125`

- 🔗 [ValidateRowPrintHandlerFunc](#validaterowprinthandlerfunc-pkgprinterstablegeneratorgo155) `:155`

- 🔗 [With](#with-pkgprinterstablegeneratorgo68) `:68`


</details>


[function] name: GenerateTable file: pkg/printers/tablegenerator.go:78 returns_error: да description: GenerateTable returns a table for the provided object, using the printer registered for that type. It returns
a table th


### GenerateTable (pkg/printers/tablegenerator.go:78)


GenerateTable returns a table for the provided object, using the printer registered for that type. It returns
a table that includes all of the information requested by options, but will not remove rows or columns. The
caller is responsible for applying rules related to filtering rows or columns.


```go
func (h *HumanReadableGenerator) GenerateTable((*metav1.Table, error)) (*metav1.Table, error)
```


**Тип запроса:** metav1.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Тип ответа:** metav1.Table


```json
{
  "Name": {},
  "Chains": []
}
```


*Определено в:* `pkg/util/iptables/testing/parse.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*metav1.Table`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `pkg/printers/tablegenerator.go:78`



---


[function] name: NewTableGenerator file: pkg/printers/tablegenerator.go:61 returns_error: нет description: NewTableGenerator creates a HumanReadableGenerator suitable for calling GenerateTable().


### NewTableGenerator (pkg/printers/tablegenerator.go:61)


NewTableGenerator creates a HumanReadableGenerator suitable for calling GenerateTable().


```go
func NewTableGenerator(()) ()
```


📍 *Расположение:* `pkg/printers/tablegenerator.go:61`



---


[function] name: TableHandler file: pkg/printers/tablegenerator.go:125 returns_error: нет description: TableHandler adds a print handler with a given set of columns to HumanReadableGenerator instance.
See ValidateRowPrintHa


### TableHandler (pkg/printers/tablegenerator.go:125)


TableHandler adds a print handler with a given set of columns to HumanReadableGenerator instance.
See ValidateRowPrintHandlerFunc for required method signature.


```go
func (h *HumanReadableGenerator) TableHandler((columnDefinitions []metav1.TableColumnDefinition, printFunc interface{})) (columnDefinitions []metav1.TableColumnDefinition, printFunc interface{})
```


**Тип ответа:** columnDefinitions


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** metav1.TableColumnDefinition


```json
{
  "Name": "string",
  "Type": "string",
  "Format": "string",
  "Description": "string",
  "Priority": 0
}
```


*Определено в:* `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go`


**Тип ответа:** printFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** interface


```json
{
  "X": 0.0
}
```


*Определено в:* `staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/interface_fuzzer.go`


📍 *Расположение:* `pkg/printers/tablegenerator.go:125`



---


[function] name: ValidateRowPrintHandlerFunc file: pkg/printers/tablegenerator.go:155 returns_error: нет description: ValidateRowPrintHandlerFunc validates print handler signature.
printFunc is the function that will be called to print an


### ValidateRowPrintHandlerFunc (pkg/printers/tablegenerator.go:155)


ValidateRowPrintHandlerFunc validates print handler signature.
printFunc is the function that will be called to print an object.
It must be of the following type:

func printFunc(object ObjectType, options GenerateOptions) ([]metav1.TableRow, error)

where ObjectType is the type of the object that will be printed, and the first
return value is an array of rows, with each row containing a number of cells that
match the number of columns defined for that printer function.


```go
func ValidateRowPrintHandlerFunc((printFunc reflect.Value)) (printFunc reflect.Value)
```


**Тип ответа:** printFunc


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** reflect.Value


```json
{
  "items": []
}
```


*Определено в:* `staging/src/k8s.io/metrics/pkg/apis/custom_metrics/v1beta1/types.go`


📍 *Расположение:* `pkg/printers/tablegenerator.go:155`



---


[function] name: With file: pkg/printers/tablegenerator.go:68 returns_error: нет description: With method - accepts a list of builder functions that modify HumanReadableGenerator


### With (pkg/printers/tablegenerator.go:68)


With method - accepts a list of builder functions that modify HumanReadableGenerator


```go
func (h *HumanReadableGenerator) With((fns ...func(PrintHandler))) (fns ...func(PrintHandler))
```


**Тип ответа:** fns


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** func


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** PrintHandler


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `pkg/printers/tablegenerator.go:68`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](pkg_kubemark.md)

- [Следующая директория](pkg_probe.md)


---

