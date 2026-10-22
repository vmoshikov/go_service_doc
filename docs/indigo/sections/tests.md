---
title: Тестирование
type: tests
repo: indigo
language: ru
chunk_boundary: h4
---


# Тестирование


## Навигация


- [К оглавлению документации](../README.md)

- [Диаграммы](../diagrams/)

- [Импорты](imports.md)

- [Структуры и типы](structures.md)

- [Функции](functions.md)

- [Спецификация API](api.md)

- [Тестирование](tests.md)

- [Используемые библиотеки](libraries.md)


---


## Меню по файлам


- 📄 [atproto/atclient/admin_auth_test.go](#atprotoatclientadmin_auth_testgo)

- 📄 [atproto/atclient/apiclient_test.go](#atprotoatclientapiclient_testgo)

- 📄 [atproto/atclient/examples_test.go](#atprotoatclientexamples_testgo)

- 📄 [atproto/atclient/params_test.go](#atprotoatclientparams_testgo)

- 📄 [atproto/atclient/password_auth_test.go](#atprotoatclientpassword_auth_testgo)

- 📄 [atproto/atcrypto/examples_test.go](#atprotoatcryptoexamples_testgo)

- 📄 [atproto/atcrypto/interop_fixtures_test.go](#atprotoatcryptointerop_fixtures_testgo)

- 📄 [atproto/atcrypto/jwk_test.go](#atprotoatcryptojwk_testgo)

- 📄 [atproto/atcrypto/keys_test.go](#atprotoatcryptokeys_testgo)

- 📄 [atproto/atcrypto/w3c_didkey_test.go](#atprotoatcryptow3c_didkey_testgo)

- 📄 [atproto/atdata/basic_test.go](#atprotoatdatabasic_testgo)

- 📄 [atproto/atdata/extract_test.go](#atprotoatdataextract_testgo)

- 📄 [atproto/atdata/interop_test.go](#atprotoatdatainterop_testgo)

- 📄 [atproto/auth/http_test.go](#atprotoauthhttp_testgo)

- 📄 [atproto/auth/jwt_test.go](#atprotoauthjwt_testgo)

- 📄 [atproto/auth/oauth/resolver_test.go](#atprotoauthoauthresolver_testgo)

- 📄 [atproto/auth/oauthscope_test.go](#atprotoauthoauthscope_testgo)

- 📄 [atproto/auth/permission_test.go](#atprotoauthpermission_testgo)

- 📄 [atproto/identity/apidir/examples_test.go](#atprotoidentityapidirexamples_testgo)

- 📄 [atproto/identity/apidir/live_test.go](#atprotoidentityapidirlive_testgo)

- 📄 [atproto/identity/diddoc_test.go](#atprotoidentitydiddoc_testgo)

- 📄 [atproto/identity/identity_test.go](#atprotoidentityidentity_testgo)

- 📄 [atproto/identity/live_test.go](#atprotoidentitylive_testgo)

- 📄 [atproto/identity/mock_directory_test.go](#atprotoidentitymock_directory_testgo)

- 📄 [atproto/identity/redisdir/live_test.go](#atprotoidentityredisdirlive_testgo)

- 📄 [atproto/labeling/label_test.go](#atprotolabelinglabel_testgo)

- 📄 [atproto/lexicon/catalog_test.go](#atprotolexiconcatalog_testgo)

- 📄 [atproto/lexicon/examples_test.go](#atprotolexiconexamples_testgo)

- 📄 [atproto/lexicon/interop_language_test.go](#atprotolexiconinterop_language_testgo)

- 📄 [atproto/lexicon/interop_record_test.go](#atprotolexiconinterop_record_testgo)

- 📄 [atproto/lexicon/language_test.go](#atprotolexiconlanguage_testgo)

- 📄 [atproto/lexicon/mimetype_test.go](#atprotolexiconmimetype_testgo)

- 📄 [atproto/lexicon/validation_test.go](#atprotolexiconvalidation_testgo)

- 📄 [atproto/repo/inductive_interop_test.go](#atprotorepoinductive_interop_testgo)

- 📄 [atproto/repo/mst/mst_interop_test.go](#atprotorepomstmst_interop_testgo)

- 📄 [atproto/repo/mst/mst_test.go](#atprotorepomstmst_testgo)

- 📄 [atproto/repo/mst/util_interop_test.go](#atprotorepomstutil_interop_testgo)

- 📄 [atproto/repo/operation_test.go](#atprotorepooperation_testgo)

- 📄 [atproto/repo/sync_test.go](#atprotoreposync_testgo)

- 📄 [atproto/syntax/atidentifier_test.go](#atprotosyntaxatidentifier_testgo)

- 📄 [atproto/syntax/aturi_test.go](#atprotosyntaxaturi_testgo)

- 📄 [atproto/syntax/cid_test.go](#atprotosyntaxcid_testgo)

- 📄 [atproto/syntax/datetime_test.go](#atprotosyntaxdatetime_testgo)

- 📄 [atproto/syntax/did_test.go](#atprotosyntaxdid_testgo)

- 📄 [atproto/syntax/handle_test.go](#atprotosyntaxhandle_testgo)

- 📄 [atproto/syntax/json_test.go](#atprotosyntaxjson_testgo)

- 📄 [atproto/syntax/language_test.go](#atprotosyntaxlanguage_testgo)

- 📄 [atproto/syntax/nsid_test.go](#atprotosyntaxnsid_testgo)

- 📄 [atproto/syntax/path_test.go](#atprotosyntaxpath_testgo)

- 📄 [atproto/syntax/recordkey_test.go](#atprotosyntaxrecordkey_testgo)

- 📄 [atproto/syntax/tid_test.go](#atprotosyntaxtid_testgo)

- 📄 [atproto/syntax/uri_test.go](#atprotosyntaxuri_testgo)

- 📄 [automod/capture/capture_test.go](#automodcapturecapture_testgo)

- 📄 [automod/countstore/countstore_test.go](#automodcountstorecountstore_testgo)

- 📄 [automod/engine/action_dedupe_test.go](#automodengineaction_dedupe_testgo)

- 📄 [automod/engine/cid_from_cdn_test.go](#automodenginecid_from_cdn_testgo)

- 📄 [automod/engine/circuit_breaker_test.go](#automodenginecircuit_breaker_testgo)

- 📄 [automod/engine/engine_test.go](#automodengineengine_testgo)

- 📄 [automod/flagstore/flagstore_redis_test.go](#automodflagstoreflagstore_redis_testgo)

- 📄 [automod/flagstore/flagstore_test.go](#automodflagstoreflagstore_testgo)

- 📄 [automod/helpers/account_test.go](#automodhelpersaccount_testgo)

- 📄 [automod/helpers/bsky_test.go](#automodhelpersbsky_testgo)

- 📄 [automod/helpers/text_test.go](#automodhelperstext_testgo)

- 📄 [automod/keyword/keyword_test.go](#automodkeywordkeyword_testgo)

- 📄 [automod/keyword/slur_regex_test.go](#automodkeywordslur_regex_testgo)

- 📄 [automod/keyword/tokenize_test.go](#automodkeywordtokenize_testgo)

- 📄 [automod/rules/hashtags_test.go](#automodruleshashtags_testgo)

- 📄 [automod/rules/keyword_test.go](#automodruleskeyword_testgo)

- 📄 [automod/rules/misleading_test.go](#automodrulesmisleading_testgo)

- 📄 [automod/rules/replies_test.go](#automodrulesreplies_testgo)

- 📄 [automod/visual/hiveai_test.go](#automodvisualhiveai_testgo)

- 📄 [backfill/backfill_test.go](#backfillbackfill_testgo)

- 📄 [carstore/repo_test.go](#carstorerepo_testgo)

- 📄 [cmd/collectiondir/pebble_test.go](#cmdcollectiondirpebble_testgo)

- 📄 [cmd/relay/relay/account_test.go](#cmdrelayrelayaccount_testgo)

- 📄 [cmd/relay/relay/host_checker_test.go](#cmdrelayrelayhost_checker_testgo)

- 📄 [cmd/relay/relay/host_test.go](#cmdrelayrelayhost_testgo)

- 📄 [cmd/relay/relay/models/methods_test.go](#cmdrelayrelaymodelsmethods_testgo)

- 📄 [cmd/relay/stream/persist/diskpersist/diskpersist_test.go](#cmdrelaystreampersistdiskpersistdiskpersist_testgo)

- 📄 [cmd/relay/testing/framework_test.go](#cmdrelaytestingframework_testgo)

- 📄 [cmd/relay/testing/sync_test.go](#cmdrelaytestingsync_testgo)

- 📄 [cmd/tap/firehose_test.go](#cmdtapfirehose_testgo)

- 📄 [cmd/tap/outbox_test.go](#cmdtapoutbox_testgo)

- 📄 [cmd/tap/resyncer_test.go](#cmdtapresyncer_testgo)

- 📄 [cmd/tap/server_test.go](#cmdtapserver_testgo)

- 📄 [cmd/tap/util_test.go](#cmdtaputil_testgo)

- 📄 [events/dbpersist/dbpersist_test.go](#eventsdbpersistdbpersist_testgo)

- 📄 [events/diskpersist/diskpersist_test.go](#eventsdiskpersistdiskpersist_testgo)

- 📄 [events/pebblepersist/pebblepersist_test.go](#eventspebblepersistpebblepersist_testgo)

- 📄 [fakedata/localinterop_test.go](#fakedatalocalinterop_testgo)

- 📄 [lex/gen_test.go](#lexgen_testgo)

- 📄 [lex/lexgen/util_test.go](#lexlexgenutil_testgo)

- 📄 [lex/lexlint/lint_test.go](#lexlexlintlint_testgo)

- 📄 [lex/lexlint/syntax_test.go](#lexlexlintsyntax_testgo)

- 📄 [lex/util/decoder_test.go](#lexutildecoder_testgo)

- 📄 [lex/util/lex_interop_old_test.go](#lexutillex_interop_old_testgo)

- 📄 [lex/util/lex_interop_test.go](#lexutillex_interop_testgo)

- 📄 [lex/util/lex_types_test.go](#lexutillex_types_testgo)

- 📄 [mst/mst_interop_test.go](#mstmst_interop_testgo)

- 📄 [mst/mst_test.go](#mstmst_testgo)

- 📄 [repo/repo_test.go](#reporepo_testgo)

- 📄 [repomgr/bench_test.go](#repomgrbench_testgo)

- 📄 [repomgr/ingest_test.go](#repomgringest_testgo)

- 📄 [search/japanese_test.go](#searchjapanese_testgo)

- 📄 [search/parse_query_test.go](#searchparse_query_testgo)

- 📄 [search/query_test.go](#searchquery_testgo)

- 📄 [search/transform_test.go](#searchtransform_testgo)

- 📄 [search/url_test.go](#searchurl_testgo)

- 📄 [testing/car_did_repro_test.go](#testingcar_did_repro_testgo)

- 📄 [testing/feedpost_test.go](#testingfeedpost_testgo)

- 📄 [testing/repo_slice_test.go](#testingrepo_slice_testgo)

- 📄 [testing/sig_test.go](#testingsig_testgo)

- 📄 [util/cliutil/key_test.go](#utilcliutilkey_testgo)

- 📄 [util/ssrf/ssrf_test.go](#utilssrfssrf_testgo)

- 📄 [xrpc/xrpc_test.go](#xrpcxrpc_testgo)


---


## Тесты


### atproto/atclient/admin_auth_test.go


📄 Исходный файл: `atproto/atclient/admin_auth_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestAdminAuth](#testadminauth) `:26`


</details>



---


[test] name: TestAdminAuth file: atproto/atclient/admin_auth_test.go:26


#### TestAdminAuth


📍 *Расположение: `atproto/atclient/admin_auth_test.go:26`*


### atproto/atclient/apiclient_test.go


📄 Исходный файл: `atproto/atclient/apiclient_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestEncodeLabelerHeader](#testencodelabelerheader) `:11`


</details>



---


[test] name: TestEncodeLabelerHeader file: atproto/atclient/apiclient_test.go:11


#### TestEncodeLabelerHeader


📍 *Расположение: `atproto/atclient/apiclient_test.go:11`*


### atproto/atclient/params_test.go


📄 Исходный файл: `atproto/atclient/params_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestParseParams](#testparseparams) `:13`


</details>



---


[test] name: TestParseParams file: atproto/atclient/params_test.go:13


#### TestParseParams


📍 *Расположение: `atproto/atclient/params_test.go:13`*


### atproto/atclient/password_auth_test.go


📄 Исходный файл: `atproto/atclient/password_auth_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestPasswordAuth](#testpasswordauth) `:112`


</details>



---


[test] name: TestPasswordAuth file: atproto/atclient/password_auth_test.go:112


#### TestPasswordAuth


📍 *Расположение: `atproto/atclient/password_auth_test.go:112`*


### atproto/atcrypto/interop_fixtures_test.go


📄 Исходный файл: `atproto/atcrypto/interop_fixtures_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestInteropSignatureFixtures](#testinteropsignaturefixtures) `:24`


</details>



---


[test] name: TestInteropSignatureFixtures file: atproto/atcrypto/interop_fixtures_test.go:24


#### TestInteropSignatureFixtures


📍 *Расположение: `atproto/atcrypto/interop_fixtures_test.go:24`*


### atproto/atcrypto/jwk_test.go


📄 Исходный файл: `atproto/atcrypto/jwk_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestK256GenJWK](#testk256genjwk) `:75`

- 🔗 [TestP256GenJWK](#testp256genjwk) `:50`

- 🔗 [TestParseJWK](#testparsejwk) `:9`


</details>



---


[test] name: TestK256GenJWK file: atproto/atcrypto/jwk_test.go:75


#### TestK256GenJWK


📍 *Расположение: `atproto/atcrypto/jwk_test.go:75`*



---


[test] name: TestP256GenJWK file: atproto/atcrypto/jwk_test.go:50


#### TestP256GenJWK


📍 *Расположение: `atproto/atcrypto/jwk_test.go:50`*



---


[test] name: TestParseJWK file: atproto/atcrypto/jwk_test.go:9


#### TestParseJWK


📍 *Расположение: `atproto/atcrypto/jwk_test.go:9`*


### atproto/atcrypto/keys_test.go


📄 Исходный файл: `atproto/atcrypto/keys_test.go`


<details open>
<summary><b>Тесты в этом файле (5)</b></summary>


- 🔗 [TestKeyBasics](#testkeybasics) `:10`

- 🔗 [TestKeyCompressionK256](#testkeycompressionk256) `:140`

- 🔗 [TestKeyCompressionP256](#testkeycompressionp256) `:122`

- 🔗 [TestLowSMany](#testlowsmany) `:91`

- 🔗 [TestParsePrivateMultibase](#testparseprivatemultibase) `:158`


</details>



---


[test] name: TestKeyBasics file: atproto/atcrypto/keys_test.go:10


#### TestKeyBasics


📍 *Расположение: `atproto/atcrypto/keys_test.go:10`*



---


[test] name: TestKeyCompressionK256 file: atproto/atcrypto/keys_test.go:140


#### TestKeyCompressionK256


📍 *Расположение: `atproto/atcrypto/keys_test.go:140`*



---


[test] name: TestKeyCompressionP256 file: atproto/atcrypto/keys_test.go:122


#### TestKeyCompressionP256


📍 *Расположение: `atproto/atcrypto/keys_test.go:122`*



---


[test] name: TestLowSMany file: atproto/atcrypto/keys_test.go:91 description: this does a large number of sign/verify cycles, to try and hit any bad high-S si


#### TestLowSMany


this does a large number of sign/verify cycles, to try and hit any bad high-S signatures


📍 *Расположение: `atproto/atcrypto/keys_test.go:91`*



---


[test] name: TestParsePrivateMultibase file: atproto/atcrypto/keys_test.go:158


#### TestParsePrivateMultibase


📍 *Расположение: `atproto/atcrypto/keys_test.go:158`*


### atproto/atcrypto/w3c_didkey_test.go


📄 Исходный файл: `atproto/atcrypto/w3c_didkey_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestDIDKeyFixtures](#testdidkeyfixtures) `:20`


</details>



---


[test] name: TestDIDKeyFixtures file: atproto/atcrypto/w3c_didkey_test.go:20


#### TestDIDKeyFixtures


📍 *Расположение: `atproto/atcrypto/w3c_didkey_test.go:20`*


### atproto/atdata/basic_test.go


📄 Исходный файл: `atproto/atdata/basic_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestExtractBlobs](#testextractblobs) `:62`

- 🔗 [TestSimpleValidation](#testsimplevalidation) `:13`

- 🔗 [TestSyntaxSerialize](#testsyntaxserialize) `:37`


</details>



---


[test] name: TestExtractBlobs file: atproto/atdata/basic_test.go:62


#### TestExtractBlobs


📍 *Расположение: `atproto/atdata/basic_test.go:62`*



---


[test] name: TestSimpleValidation file: atproto/atdata/basic_test.go:13


#### TestSimpleValidation


📍 *Расположение: `atproto/atdata/basic_test.go:13`*



---


[test] name: TestSyntaxSerialize file: atproto/atdata/basic_test.go:37


#### TestSyntaxSerialize


📍 *Расположение: `atproto/atdata/basic_test.go:37`*


### atproto/atdata/extract_test.go


📄 Исходный файл: `atproto/atdata/extract_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestExtract](#testextract) `:11`


</details>



---


[test] name: TestExtract file: atproto/atdata/extract_test.go:11


#### TestExtract


📍 *Расположение: `atproto/atdata/extract_test.go:11`*


### atproto/atdata/interop_test.go


📄 Исходный файл: `atproto/atdata/interop_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestInteropDataModelFixtures](#testinteropdatamodelfixtures) `:20`

- 🔗 [TestInteropDataModelInvalid](#testinteropdatamodelinvalid) `:111`

- 🔗 [TestInteropDataModelValid](#testinteropdatamodelvalid) `:86`


</details>



---


[test] name: TestInteropDataModelFixtures file: atproto/atdata/interop_test.go:20


#### TestInteropDataModelFixtures


📍 *Расположение: `atproto/atdata/interop_test.go:20`*



---


[test] name: TestInteropDataModelInvalid file: atproto/atdata/interop_test.go:111


#### TestInteropDataModelInvalid


📍 *Расположение: `atproto/atdata/interop_test.go:111`*



---


[test] name: TestInteropDataModelValid file: atproto/atdata/interop_test.go:86


#### TestInteropDataModelValid


📍 *Расположение: `atproto/atdata/interop_test.go:86`*


### atproto/auth/http_test.go


📄 Исходный файл: `atproto/auth/http_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestAdminAuthMiddleware](#testadminauthmiddleware) `:29`

- 🔗 [TestServiceAuthMiddleware](#testserviceauthmiddleware) `:73`


</details>



---


[test] name: TestAdminAuthMiddleware file: atproto/auth/http_test.go:29


#### TestAdminAuthMiddleware


📍 *Расположение: `atproto/auth/http_test.go:29`*



---


[test] name: TestServiceAuthMiddleware file: atproto/auth/http_test.go:73


#### TestServiceAuthMiddleware


📍 *Расположение: `atproto/auth/http_test.go:73`*


### atproto/auth/jwt_test.go


📄 Исходный файл: `atproto/auth/jwt_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestK256SigningValidation](#testk256signingvalidation) `:150`

- 🔗 [TestP256SigningValidation](#testp256signingvalidation) `:142`

- 🔗 [TestSignatureMethods](#testsignaturemethods) `:39`


</details>



---


[test] name: TestK256SigningValidation file: atproto/auth/jwt_test.go:150


#### TestK256SigningValidation


📍 *Расположение: `atproto/auth/jwt_test.go:150`*



---


[test] name: TestP256SigningValidation file: atproto/auth/jwt_test.go:142


#### TestP256SigningValidation


📍 *Расположение: `atproto/auth/jwt_test.go:142`*



---


[test] name: TestSignatureMethods file: atproto/auth/jwt_test.go:39


#### TestSignatureMethods


📍 *Расположение: `atproto/auth/jwt_test.go:39`*


### atproto/auth/oauth/resolver_test.go


📄 Исходный файл: `atproto/auth/oauth/resolver_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestResolver](#testresolver) `:122`

- 🔗 [TestValidateMetadata](#testvalidatemetadata) `:14`


</details>



---


[test] name: TestResolver file: atproto/auth/oauth/resolver_test.go:122


#### TestResolver


📍 *Расположение: `atproto/auth/oauth/resolver_test.go:122`*



---


[test] name: TestValidateMetadata file: atproto/auth/oauth/resolver_test.go:14 description: TODO: localhost (dev mode) resolution


#### TestValidateMetadata


TODO: localhost (dev mode) resolution


📍 *Расположение: `atproto/auth/oauth/resolver_test.go:14`*


### atproto/auth/oauthscope_test.go


📄 Исходный файл: `atproto/auth/oauthscope_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestParseOAuthScope](#testparseoauthscope) `:9`


</details>



---


[test] name: TestParseOAuthScope file: atproto/auth/oauthscope_test.go:9


#### TestParseOAuthScope


📍 *Расположение: `atproto/auth/oauthscope_test.go:9`*


### atproto/auth/permission_test.go


📄 Исходный файл: `atproto/auth/permission_test.go`


<details open>
<summary><b>Тесты в этом файле (6)</b></summary>


- 🔗 [TestGenericGenericScopesValid](#testgenericgenericscopesvalid) `:45`

- 🔗 [TestGenericScopesInvalid](#testgenericscopesinvalid) `:71`

- 🔗 [TestInteropPermissionInvalid](#testinteroppermissioninvalid) `:125`

- 🔗 [TestInteropPermissionValid](#testinteroppermissionvalid) `:94`

- 🔗 [TestRoundTrip](#testroundtrip) `:13`

- 🔗 [TestValidBlobAccept](#testvalidblobaccept) `:148`


</details>



---


[test] name: TestGenericGenericScopesValid file: atproto/auth/permission_test.go:45


#### TestGenericGenericScopesValid


📍 *Расположение: `atproto/auth/permission_test.go:45`*



---


[test] name: TestGenericScopesInvalid file: atproto/auth/permission_test.go:71


#### TestGenericScopesInvalid


📍 *Расположение: `atproto/auth/permission_test.go:71`*



---


[test] name: TestInteropPermissionInvalid file: atproto/auth/permission_test.go:125


#### TestInteropPermissionInvalid


📍 *Расположение: `atproto/auth/permission_test.go:125`*



---


[test] name: TestInteropPermissionValid file: atproto/auth/permission_test.go:94


#### TestInteropPermissionValid


📍 *Расположение: `atproto/auth/permission_test.go:94`*



---


[test] name: TestRoundTrip file: atproto/auth/permission_test.go:13


#### TestRoundTrip


📍 *Расположение: `atproto/auth/permission_test.go:13`*



---


[test] name: TestValidBlobAccept file: atproto/auth/permission_test.go:148


#### TestValidBlobAccept


📍 *Расположение: `atproto/auth/permission_test.go:148`*


### atproto/identity/apidir/live_test.go


📄 Исходный файл: `atproto/identity/apidir/live_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestBasicLookups](#testbasiclookups) `:12`


</details>



---


[test] name: TestBasicLookups file: atproto/identity/apidir/live_test.go:12


#### TestBasicLookups


📍 *Расположение: `atproto/identity/apidir/live_test.go:12`*


### atproto/identity/diddoc_test.go


📄 Исходный файл: `atproto/identity/diddoc_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestDIDDocFeedGenParse](#testdiddocfeedgenparse) `:53`

- 🔗 [TestDIDDocParse](#testdiddocparse) `:12`


</details>



---


[test] name: TestDIDDocFeedGenParse file: atproto/identity/diddoc_test.go:53


#### TestDIDDocFeedGenParse


📍 *Расположение: `atproto/identity/diddoc_test.go:53`*



---


[test] name: TestDIDDocParse file: atproto/identity/diddoc_test.go:12


#### TestDIDDocParse


📍 *Расположение: `atproto/identity/diddoc_test.go:12`*


### atproto/identity/identity_test.go


📄 Исходный файл: `atproto/identity/identity_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestHandleExtraction](#testhandleextraction) `:13`


</details>



---


[test] name: TestHandleExtraction file: atproto/identity/identity_test.go:13 description: Tests parsing and normalizing handles from DID documents


#### TestHandleExtraction


Tests parsing and normalizing handles from DID documents


📍 *Расположение: `atproto/identity/identity_test.go:13`*


### atproto/identity/live_test.go


📄 Исходный файл: `atproto/identity/live_test.go`


<details open>
<summary><b>Тесты в этом файле (5)</b></summary>


- 🔗 [TestBaseDirectory](#testbasedirectory) `:58`

- 🔗 [TestCacheCoalesce](#testcachecoalesce) `:73`

- 🔗 [TestCacheDirectory](#testcachedirectory) `:64`

- 🔗 [TestFallbackDNS](#testfallbackdns) `:120`

- 🔗 [TestResolveNSID](#testresolvensid) `:142`


</details>



---


[test] name: TestBaseDirectory file: atproto/identity/live_test.go:58


#### TestBaseDirectory


📍 *Расположение: `atproto/identity/live_test.go:58`*



---


[test] name: TestCacheCoalesce file: atproto/identity/live_test.go:73


#### TestCacheCoalesce


📍 *Расположение: `atproto/identity/live_test.go:73`*



---


[test] name: TestCacheDirectory file: atproto/identity/live_test.go:64


#### TestCacheDirectory


📍 *Расположение: `atproto/identity/live_test.go:64`*



---


[test] name: TestFallbackDNS file: atproto/identity/live_test.go:120


#### TestFallbackDNS


📍 *Расположение: `atproto/identity/live_test.go:120`*



---


[test] name: TestResolveNSID file: atproto/identity/live_test.go:142


#### TestResolveNSID


📍 *Расположение: `atproto/identity/live_test.go:142`*


### atproto/identity/mock_directory_test.go


📄 Исходный файл: `atproto/identity/mock_directory_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestMockDirectory](#testmockdirectory) `:12`


</details>



---


[test] name: TestMockDirectory file: atproto/identity/mock_directory_test.go:12


#### TestMockDirectory


📍 *Расположение: `atproto/identity/mock_directory_test.go:12`*


### atproto/identity/redisdir/live_test.go


📄 Исходный файл: `atproto/identity/redisdir/live_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestRedisCoalesce](#testrediscoalesce) `:88`

- 🔗 [TestRedisDirectory](#testredisdirectory) `:64`


</details>



---


[test] name: TestRedisCoalesce file: atproto/identity/redisdir/live_test.go:88


#### TestRedisCoalesce


📍 *Расположение: `atproto/identity/redisdir/live_test.go:88`*



---


[test] name: TestRedisDirectory file: atproto/identity/redisdir/live_test.go:64


#### TestRedisDirectory


📍 *Расположение: `atproto/identity/redisdir/live_test.go:64`*


### atproto/labeling/label_test.go


📄 Исходный файл: `atproto/labeling/label_test.go`


<details open>
<summary><b>Тесты в этом файле (5)</b></summary>


- 🔗 [TestFromLexicon](#testfromlexicon) `:124`

- 🔗 [TestParseLabel](#testparselabel) `:51`

- 🔗 [TestSignLabel](#testsignlabel) `:69`

- 🔗 [TestToLexicon](#testtolexicon) `:94`

- 🔗 [TestVerifyLabel](#testverifylabel) `:13`


</details>



---


[test] name: TestFromLexicon file: atproto/labeling/label_test.go:124


#### TestFromLexicon


📍 *Расположение: `atproto/labeling/label_test.go:124`*



---


[test] name: TestParseLabel file: atproto/labeling/label_test.go:51


#### TestParseLabel


📍 *Расположение: `atproto/labeling/label_test.go:51`*



---


[test] name: TestSignLabel file: atproto/labeling/label_test.go:69


#### TestSignLabel


📍 *Расположение: `atproto/labeling/label_test.go:69`*



---


[test] name: TestToLexicon file: atproto/labeling/label_test.go:94


#### TestToLexicon


📍 *Расположение: `atproto/labeling/label_test.go:94`*



---


[test] name: TestVerifyLabel file: atproto/labeling/label_test.go:13


#### TestVerifyLabel


📍 *Расположение: `atproto/labeling/label_test.go:13`*


### atproto/lexicon/catalog_test.go


📄 Исходный файл: `atproto/lexicon/catalog_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestDirCatalog](#testdircatalog) `:28`

- 🔗 [TestEmbedCatalog](#testembedcatalog) `:13`


</details>



---


[test] name: TestDirCatalog file: atproto/lexicon/catalog_test.go:28


#### TestDirCatalog


📍 *Расположение: `atproto/lexicon/catalog_test.go:28`*



---


[test] name: TestEmbedCatalog file: atproto/lexicon/catalog_test.go:13


#### TestEmbedCatalog


📍 *Расположение: `atproto/lexicon/catalog_test.go:13`*


### atproto/lexicon/interop_language_test.go


📄 Исходный файл: `atproto/lexicon/interop_language_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestInteropLexiconInvalid](#testinteroplexiconinvalid) `:67`

- 🔗 [TestInteropLexiconValid](#testinteroplexiconvalid) `:18`


</details>



---


[test] name: TestInteropLexiconInvalid file: atproto/lexicon/interop_language_test.go:67


#### TestInteropLexiconInvalid


📍 *Расположение: `atproto/lexicon/interop_language_test.go:67`*



---


[test] name: TestInteropLexiconValid file: atproto/lexicon/interop_language_test.go:18


#### TestInteropLexiconValid


📍 *Расположение: `atproto/lexicon/interop_language_test.go:18`*


### atproto/lexicon/interop_record_test.go


📄 Исходный файл: `atproto/lexicon/interop_record_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestInteropRecordInvalid](#testinteroprecordinvalid) `:56`

- 🔗 [TestInteropRecordValid](#testinteroprecordvalid) `:21`


</details>



---


[test] name: TestInteropRecordInvalid file: atproto/lexicon/interop_record_test.go:56


#### TestInteropRecordInvalid


📍 *Расположение: `atproto/lexicon/interop_record_test.go:56`*



---


[test] name: TestInteropRecordValid file: atproto/lexicon/interop_record_test.go:21


#### TestInteropRecordValid


📍 *Расположение: `atproto/lexicon/interop_record_test.go:21`*


### atproto/lexicon/language_test.go


📄 Исходный файл: `atproto/lexicon/language_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestBasicLabelLexicon](#testbasiclabellexicon) `:12`


</details>



---


[test] name: TestBasicLabelLexicon file: atproto/lexicon/language_test.go:12


#### TestBasicLabelLexicon


📍 *Расположение: `atproto/lexicon/language_test.go:12`*


### atproto/lexicon/mimetype_test.go


📄 Исходный файл: `atproto/lexicon/mimetype_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestAcceptableMimeType](#testacceptablemimetype) `:9`


</details>



---


[test] name: TestAcceptableMimeType file: atproto/lexicon/mimetype_test.go:9


#### TestAcceptableMimeType


📍 *Расположение: `atproto/lexicon/mimetype_test.go:9`*


### atproto/lexicon/validation_test.go


📄 Исходный файл: `atproto/lexicon/validation_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestBasicCatalog](#testbasiccatalog) `:9`


</details>



---


[test] name: TestBasicCatalog file: atproto/lexicon/validation_test.go:9


#### TestBasicCatalog


📍 *Расположение: `atproto/lexicon/validation_test.go:9`*


### atproto/repo/inductive_interop_test.go


📄 Исходный файл: `atproto/repo/inductive_interop_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestCommitProofFixtures](#testcommitprooffixtures) `:149`


</details>



---


[test] name: TestCommitProofFixtures file: atproto/repo/inductive_interop_test.go:149


#### TestCommitProofFixtures


📍 *Расположение: `atproto/repo/inductive_interop_test.go:149`*


### atproto/repo/mst/mst_interop_test.go


📄 Исходный файл: `atproto/repo/mst/mst_interop_test.go`


<details open>
<summary><b>Тесты в этом файле (6)</b></summary>


- 🔗 [TestInteropEdgeCasesHigher](#testinteropedgecaseshigher) `:225`

- 🔗 [TestInteropEdgeCasesInsertion](#testinteropedgecasesinsertion) `:163`

- 🔗 [TestInteropEdgeCasesTrimTop](#testinteropedgecasestrimtop) `:124`

- 🔗 [TestInteropKnownMaps](#testinteropknownmaps) `:74`

- 🔗 [TestInteropKnownMapsTricky](#testinteropknownmapstricky) `:106`

- 🔗 [TestManualNode](#testmanualnode) `:44`


</details>



---


[test] name: TestInteropEdgeCasesHigher file: atproto/repo/mst/mst_interop_test.go:225 description: "handles new layers that are two higher than existing"


#### TestInteropEdgeCasesHigher


"handles new layers that are two higher than existing"


📍 *Расположение: `atproto/repo/mst/mst_interop_test.go:225`*



---


[test] name: TestInteropEdgeCasesInsertion file: atproto/repo/mst/mst_interop_test.go:163


#### TestInteropEdgeCasesInsertion


📍 *Расположение: `atproto/repo/mst/mst_interop_test.go:163`*



---


[test] name: TestInteropEdgeCasesTrimTop file: atproto/repo/mst/mst_interop_test.go:124 description: "trims top of tree on delete"


#### TestInteropEdgeCasesTrimTop


"trims top of tree on delete"


📍 *Расположение: `atproto/repo/mst/mst_interop_test.go:124`*



---


[test] name: TestInteropKnownMaps file: atproto/repo/mst/mst_interop_test.go:74


#### TestInteropKnownMaps


📍 *Расположение: `atproto/repo/mst/mst_interop_test.go:74`*



---


[test] name: TestInteropKnownMapsTricky file: atproto/repo/mst/mst_interop_test.go:106


#### TestInteropKnownMapsTricky


📍 *Расположение: `atproto/repo/mst/mst_interop_test.go:106`*



---


[test] name: TestManualNode file: atproto/repo/mst/mst_interop_test.go:44 description: TODO: TestAllowedKeys


#### TestManualNode


TODO: TestAllowedKeys


📍 *Расположение: `atproto/repo/mst/mst_interop_test.go:44`*


### atproto/repo/mst/mst_test.go


📄 Исходный файл: `atproto/repo/mst/mst_test.go`


<details open>
<summary><b>Тесты в этом файле (6)</b></summary>


- 🔗 [TestBasicMST](#testbasicmst) `:14`

- 🔗 [TestBasicMap](#testbasicmap) `:98`

- 🔗 [TestBrokenCaseOne](#testbrokencaseone) `:246`

- 🔗 [TestKeyLimits](#testkeylimits) `:74`

- 🔗 [TestRandomTree](#testrandomtree) `:147`

- 🔗 [TestRandomUntilError](#testrandomuntilerror) `:215`


</details>



---


[test] name: TestBasicMST file: atproto/repo/mst/mst_test.go:14


#### TestBasicMST


📍 *Расположение: `atproto/repo/mst/mst_test.go:14`*



---


[test] name: TestBasicMap file: atproto/repo/mst/mst_test.go:98


#### TestBasicMap


📍 *Расположение: `atproto/repo/mst/mst_test.go:98`*



---


[test] name: TestBrokenCaseOne file: atproto/repo/mst/mst_test.go:246


#### TestBrokenCaseOne


📍 *Расположение: `atproto/repo/mst/mst_test.go:246`*



---


[test] name: TestKeyLimits file: atproto/repo/mst/mst_test.go:74


#### TestKeyLimits


📍 *Расположение: `atproto/repo/mst/mst_test.go:74`*



---


[test] name: TestRandomTree file: atproto/repo/mst/mst_test.go:147


#### TestRandomTree


📍 *Расположение: `atproto/repo/mst/mst_test.go:147`*



---


[test] name: TestRandomUntilError file: atproto/repo/mst/mst_test.go:215


#### TestRandomUntilError


📍 *Расположение: `atproto/repo/mst/mst_test.go:215`*


### atproto/repo/mst/util_interop_test.go


📄 Исходный файл: `atproto/repo/mst/util_interop_test.go`


<details open>
<summary><b>Тесты в этом файле (4)</b></summary>


- 🔗 [TestExampleKeyHeights](#testexamplekeyheights) `:83`

- 🔗 [TestHeightForKey](#testheightforkey) `:67`

- 🔗 [TestPrefixLen](#testprefixlen) `:12`

- 🔗 [TestPrefixLenWide](#testprefixlenwide) `:40`


</details>



---


[test] name: TestExampleKeyHeights file: atproto/repo/mst/util_interop_test.go:83


#### TestExampleKeyHeights


📍 *Расположение: `atproto/repo/mst/util_interop_test.go:83`*



---


[test] name: TestHeightForKey file: atproto/repo/mst/util_interop_test.go:67


#### TestHeightForKey


📍 *Расположение: `atproto/repo/mst/util_interop_test.go:67`*



---


[test] name: TestPrefixLen file: atproto/repo/mst/util_interop_test.go:12


#### TestPrefixLen


📍 *Расположение: `atproto/repo/mst/util_interop_test.go:12`*



---


[test] name: TestPrefixLenWide file: atproto/repo/mst/util_interop_test.go:40


#### TestPrefixLenWide


📍 *Расположение: `atproto/repo/mst/util_interop_test.go:40`*


### atproto/repo/operation_test.go


📄 Исходный файл: `atproto/repo/operation_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestBasicOperation](#testbasicoperation) `:51`

- 🔗 [TestNormalizeOps](#testnormalizeops) `:252`

- 🔗 [TestRandomOperations](#testrandomoperations) `:105`


</details>



---


[test] name: TestBasicOperation file: atproto/repo/operation_test.go:51


#### TestBasicOperation


📍 *Расположение: `atproto/repo/operation_test.go:51`*



---


[test] name: TestNormalizeOps file: atproto/repo/operation_test.go:252


#### TestNormalizeOps


📍 *Расположение: `atproto/repo/operation_test.go:252`*



---


[test] name: TestRandomOperations file: atproto/repo/operation_test.go:105


#### TestRandomOperations


📍 *Расположение: `atproto/repo/operation_test.go:105`*


### atproto/repo/sync_test.go


📄 Исходный файл: `atproto/repo/sync_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestFirehoseMergePartialNodes](#testfirehosemergepartialnodes) `:21`

- 🔗 [TestFirehoseTrimTopPartial](#testfirehosetrimtoppartial) `:16`


</details>



---


[test] name: TestFirehoseMergePartialNodes file: atproto/repo/sync_test.go:21


#### TestFirehoseMergePartialNodes


📍 *Расположение: `atproto/repo/sync_test.go:21`*



---


[test] name: TestFirehoseTrimTopPartial file: atproto/repo/sync_test.go:16


#### TestFirehoseTrimTopPartial


📍 *Расположение: `atproto/repo/sync_test.go:16`*


### atproto/syntax/atidentifier_test.go


📄 Исходный файл: `atproto/syntax/atidentifier_test.go`


<details open>
<summary><b>Тесты в этом файле (4)</b></summary>


- 🔗 [TestDowncase](#testdowncase) `:52`

- 🔗 [TestEmpty](#testempty) `:74`

- 🔗 [TestInteropAtIdentifiersInvalid](#testinteropatidentifiersinvalid) `:32`

- 🔗 [TestInteropAtIdentifiersValid](#testinteropatidentifiersvalid) `:12`


</details>



---


[test] name: TestDowncase file: atproto/syntax/atidentifier_test.go:52


#### TestDowncase


📍 *Расположение: `atproto/syntax/atidentifier_test.go:52`*



---


[test] name: TestEmpty file: atproto/syntax/atidentifier_test.go:74


#### TestEmpty


📍 *Расположение: `atproto/syntax/atidentifier_test.go:74`*



---


[test] name: TestInteropAtIdentifiersInvalid file: atproto/syntax/atidentifier_test.go:32


#### TestInteropAtIdentifiersInvalid


📍 *Расположение: `atproto/syntax/atidentifier_test.go:32`*



---


[test] name: TestInteropAtIdentifiersValid file: atproto/syntax/atidentifier_test.go:12


#### TestInteropAtIdentifiersValid


📍 *Расположение: `atproto/syntax/atidentifier_test.go:12`*


### atproto/syntax/aturi_test.go


📄 Исходный файл: `atproto/syntax/aturi_test.go`


<details open>
<summary><b>Тесты в этом файле (6)</b></summary>


- 🔗 [TestATURINoPanic](#testaturinopanic) `:112`

- 🔗 [TestATURINormalize](#testaturinormalize) `:97`

- 🔗 [TestATURIParts](#testaturiparts) `:61`

- 🔗 [TestATURIPath](#testaturipath) `:81`

- 🔗 [TestInteropATURIsInvalid](#testinteropaturisinvalid) `:41`

- 🔗 [TestInteropATURIsValid](#testinteropaturisvalid) `:12`


</details>



---


[test] name: TestATURINoPanic file: atproto/syntax/aturi_test.go:112


#### TestATURINoPanic


📍 *Расположение: `atproto/syntax/aturi_test.go:112`*



---


[test] name: TestATURINormalize file: atproto/syntax/aturi_test.go:97


#### TestATURINormalize


📍 *Расположение: `atproto/syntax/aturi_test.go:97`*



---


[test] name: TestATURIParts file: atproto/syntax/aturi_test.go:61


#### TestATURIParts


📍 *Расположение: `atproto/syntax/aturi_test.go:61`*



---


[test] name: TestATURIPath file: atproto/syntax/aturi_test.go:81


#### TestATURIPath


📍 *Расположение: `atproto/syntax/aturi_test.go:81`*



---


[test] name: TestInteropATURIsInvalid file: atproto/syntax/aturi_test.go:41


#### TestInteropATURIsInvalid


📍 *Расположение: `atproto/syntax/aturi_test.go:41`*



---


[test] name: TestInteropATURIsValid file: atproto/syntax/aturi_test.go:12


#### TestInteropATURIsValid


📍 *Расположение: `atproto/syntax/aturi_test.go:12`*


### atproto/syntax/cid_test.go


📄 Исходный файл: `atproto/syntax/cid_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestInteropCIDsInvalid](#testinteropcidsinvalid) `:32`

- 🔗 [TestInteropCIDsValid](#testinteropcidsvalid) `:12`


</details>



---


[test] name: TestInteropCIDsInvalid file: atproto/syntax/cid_test.go:32


#### TestInteropCIDsInvalid


📍 *Расположение: `atproto/syntax/cid_test.go:32`*



---


[test] name: TestInteropCIDsValid file: atproto/syntax/cid_test.go:12


#### TestInteropCIDsValid


📍 *Расположение: `atproto/syntax/cid_test.go:12`*


### atproto/syntax/datetime_test.go


📄 Исходный файл: `atproto/syntax/datetime_test.go`


<details open>
<summary><b>Тесты в этом файле (5)</b></summary>


- 🔗 [TestDatetimeNow](#testdatetimenow) `:109`

- 🔗 [TestInteropDatetimeInvalid](#testinteropdatetimeinvalid) `:32`

- 🔗 [TestInteropDatetimeTimeInvalid](#testinteropdatetimetimeinvalid) `:52`

- 🔗 [TestInteropDatetimeValid](#testinteropdatetimevalid) `:12`

- 🔗 [TestParseDatetimeLenient](#testparsedatetimelenient) `:77`


</details>



---


[test] name: TestDatetimeNow file: atproto/syntax/datetime_test.go:109


#### TestDatetimeNow


📍 *Расположение: `atproto/syntax/datetime_test.go:109`*



---


[test] name: TestInteropDatetimeInvalid file: atproto/syntax/datetime_test.go:32


#### TestInteropDatetimeInvalid


📍 *Расположение: `atproto/syntax/datetime_test.go:32`*



---


[test] name: TestInteropDatetimeTimeInvalid file: atproto/syntax/datetime_test.go:52


#### TestInteropDatetimeTimeInvalid


📍 *Расположение: `atproto/syntax/datetime_test.go:52`*



---


[test] name: TestInteropDatetimeValid file: atproto/syntax/datetime_test.go:12


#### TestInteropDatetimeValid


📍 *Расположение: `atproto/syntax/datetime_test.go:12`*



---


[test] name: TestParseDatetimeLenient file: atproto/syntax/datetime_test.go:77


#### TestParseDatetimeLenient


📍 *Расположение: `atproto/syntax/datetime_test.go:77`*


### atproto/syntax/did_test.go


📄 Исходный файл: `atproto/syntax/did_test.go`


<details open>
<summary><b>Тесты в этом файле (4)</b></summary>


- 🔗 [TestDIDNoPanic](#testdidnopanic) `:61`

- 🔗 [TestDIDParts](#testdidparts) `:52`

- 🔗 [TestInteropDIDsInvalid](#testinteropdidsinvalid) `:32`

- 🔗 [TestInteropDIDsValid](#testinteropdidsvalid) `:12`


</details>



---


[test] name: TestDIDNoPanic file: atproto/syntax/did_test.go:61


#### TestDIDNoPanic


📍 *Расположение: `atproto/syntax/did_test.go:61`*



---


[test] name: TestDIDParts file: atproto/syntax/did_test.go:52


#### TestDIDParts


📍 *Расположение: `atproto/syntax/did_test.go:52`*



---


[test] name: TestInteropDIDsInvalid file: atproto/syntax/did_test.go:32


#### TestInteropDIDsInvalid


📍 *Расположение: `atproto/syntax/did_test.go:32`*



---


[test] name: TestInteropDIDsValid file: atproto/syntax/did_test.go:12


#### TestInteropDIDsValid


📍 *Расположение: `atproto/syntax/did_test.go:12`*


### atproto/syntax/handle_test.go


📄 Исходный файл: `atproto/syntax/handle_test.go`


<details open>
<summary><b>Тесты в этом файле (5)</b></summary>


- 🔗 [TestHandleInterfaces](#testhandleinterfaces) `:76`

- 🔗 [TestHandleNoPanic](#testhandlenopanic) `:66`

- 🔗 [TestHandleNormalize](#testhandlenormalize) `:53`

- 🔗 [TestInteropHandlesInvalid](#testinterophandlesinvalid) `:33`

- 🔗 [TestInteropHandlesValid](#testinterophandlesvalid) `:13`


</details>



---


[test] name: TestHandleInterfaces file: atproto/syntax/handle_test.go:76


#### TestHandleInterfaces


📍 *Расположение: `atproto/syntax/handle_test.go:76`*



---


[test] name: TestHandleNoPanic file: atproto/syntax/handle_test.go:66


#### TestHandleNoPanic


📍 *Расположение: `atproto/syntax/handle_test.go:66`*



---


[test] name: TestHandleNormalize file: atproto/syntax/handle_test.go:53


#### TestHandleNormalize


📍 *Расположение: `atproto/syntax/handle_test.go:53`*



---


[test] name: TestInteropHandlesInvalid file: atproto/syntax/handle_test.go:33


#### TestInteropHandlesInvalid


📍 *Расположение: `atproto/syntax/handle_test.go:33`*



---


[test] name: TestInteropHandlesValid file: atproto/syntax/handle_test.go:13


#### TestInteropHandlesValid


📍 *Расположение: `atproto/syntax/handle_test.go:13`*


### atproto/syntax/json_test.go


📄 Исходный файл: `atproto/syntax/json_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestJSONEncoding](#testjsonencoding) `:10`

- 🔗 [TestJSONHandle](#testjsonhandle) `:74`


</details>



---


[test] name: TestJSONEncoding file: atproto/syntax/json_test.go:10


#### TestJSONEncoding


📍 *Расположение: `atproto/syntax/json_test.go:10`*



---


[test] name: TestJSONHandle file: atproto/syntax/json_test.go:74


#### TestJSONHandle


📍 *Расположение: `atproto/syntax/json_test.go:74`*


### atproto/syntax/language_test.go


📄 Исходный файл: `atproto/syntax/language_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestInteropLanguagesInvalid](#testinteroplanguagesinvalid) `:32`

- 🔗 [TestInteropLanguagesValid](#testinteroplanguagesvalid) `:12`


</details>



---


[test] name: TestInteropLanguagesInvalid file: atproto/syntax/language_test.go:32


#### TestInteropLanguagesInvalid


📍 *Расположение: `atproto/syntax/language_test.go:32`*



---


[test] name: TestInteropLanguagesValid file: atproto/syntax/language_test.go:12


#### TestInteropLanguagesValid


📍 *Расположение: `atproto/syntax/language_test.go:12`*


### atproto/syntax/nsid_test.go


📄 Исходный файл: `atproto/syntax/nsid_test.go`


<details open>
<summary><b>Тесты в этом файле (5)</b></summary>


- 🔗 [TestInteropNSIDsInvalid](#testinteropnsidsinvalid) `:32`

- 🔗 [TestInteropNSIDsValid](#testinteropnsidsvalid) `:12`

- 🔗 [TestNSIDNoPanic](#testnsidnopanic) `:69`

- 🔗 [TestNSIDNormalize](#testnsidnormalize) `:60`

- 🔗 [TestNSIDParts](#testnsidparts) `:52`


</details>



---


[test] name: TestInteropNSIDsInvalid file: atproto/syntax/nsid_test.go:32


#### TestInteropNSIDsInvalid


📍 *Расположение: `atproto/syntax/nsid_test.go:32`*



---


[test] name: TestInteropNSIDsValid file: atproto/syntax/nsid_test.go:12


#### TestInteropNSIDsValid


📍 *Расположение: `atproto/syntax/nsid_test.go:12`*



---


[test] name: TestNSIDNoPanic file: atproto/syntax/nsid_test.go:69


#### TestNSIDNoPanic


📍 *Расположение: `atproto/syntax/nsid_test.go:69`*



---


[test] name: TestNSIDNormalize file: atproto/syntax/nsid_test.go:60


#### TestNSIDNormalize


📍 *Расположение: `atproto/syntax/nsid_test.go:60`*



---


[test] name: TestNSIDParts file: atproto/syntax/nsid_test.go:52


#### TestNSIDParts


📍 *Расположение: `atproto/syntax/nsid_test.go:52`*


### atproto/syntax/path_test.go


📄 Исходный файл: `atproto/syntax/path_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestRepoPath](#testrepopath) `:9`


</details>



---


[test] name: TestRepoPath file: atproto/syntax/path_test.go:9


#### TestRepoPath


📍 *Расположение: `atproto/syntax/path_test.go:9`*


### atproto/syntax/recordkey_test.go


📄 Исходный файл: `atproto/syntax/recordkey_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestInteropRecordKeysInvalid](#testinteroprecordkeysinvalid) `:32`

- 🔗 [TestInteropRecordKeysValid](#testinteroprecordkeysvalid) `:12`

- 🔗 [TestRecordKeyNoPanic](#testrecordkeynopanic) `:52`


</details>



---


[test] name: TestInteropRecordKeysInvalid file: atproto/syntax/recordkey_test.go:32


#### TestInteropRecordKeysInvalid


📍 *Расположение: `atproto/syntax/recordkey_test.go:32`*



---


[test] name: TestInteropRecordKeysValid file: atproto/syntax/recordkey_test.go:12


#### TestInteropRecordKeysValid


📍 *Расположение: `atproto/syntax/recordkey_test.go:12`*



---


[test] name: TestRecordKeyNoPanic file: atproto/syntax/recordkey_test.go:52


#### TestRecordKeyNoPanic


📍 *Расположение: `atproto/syntax/recordkey_test.go:52`*


### atproto/syntax/tid_test.go


📄 Исходный файл: `atproto/syntax/tid_test.go`


<details open>
<summary><b>Тесты в этом файле (7)</b></summary>


- 🔗 [TestInteropTIDsInvalid](#testinteroptidsinvalid) `:33`

- 🔗 [TestInteropTIDsValid](#testinteroptidsvalid) `:13`

- 🔗 [TestTIDClock](#testtidclock) `:121`

- 🔗 [TestTIDConstruction](#testtidconstruction) `:100`

- 🔗 [TestTIDExamples](#testtidexamples) `:73`

- 🔗 [TestTIDNoPanic](#testtidnopanic) `:90`

- 🔗 [TestTIDParts](#testtidparts) `:53`


</details>



---


[test] name: TestInteropTIDsInvalid file: atproto/syntax/tid_test.go:33


#### TestInteropTIDsInvalid


📍 *Расположение: `atproto/syntax/tid_test.go:33`*



---


[test] name: TestInteropTIDsValid file: atproto/syntax/tid_test.go:13


#### TestInteropTIDsValid


📍 *Расположение: `atproto/syntax/tid_test.go:13`*



---


[test] name: TestTIDClock file: atproto/syntax/tid_test.go:121


#### TestTIDClock


📍 *Расположение: `atproto/syntax/tid_test.go:121`*



---


[test] name: TestTIDConstruction file: atproto/syntax/tid_test.go:100


#### TestTIDConstruction


📍 *Расположение: `atproto/syntax/tid_test.go:100`*



---


[test] name: TestTIDExamples file: atproto/syntax/tid_test.go:73


#### TestTIDExamples


📍 *Расположение: `atproto/syntax/tid_test.go:73`*



---


[test] name: TestTIDNoPanic file: atproto/syntax/tid_test.go:90


#### TestTIDNoPanic


📍 *Расположение: `atproto/syntax/tid_test.go:90`*



---


[test] name: TestTIDParts file: atproto/syntax/tid_test.go:53


#### TestTIDParts


📍 *Расположение: `atproto/syntax/tid_test.go:53`*


### atproto/syntax/uri_test.go


📄 Исходный файл: `atproto/syntax/uri_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestInteropURIsInvalid](#testinteropurisinvalid) `:32`

- 🔗 [TestInteropURIsValid](#testinteropurisvalid) `:12`


</details>



---


[test] name: TestInteropURIsInvalid file: atproto/syntax/uri_test.go:32


#### TestInteropURIsInvalid


📍 *Расположение: `atproto/syntax/uri_test.go:32`*



---


[test] name: TestInteropURIsValid file: atproto/syntax/uri_test.go:12


#### TestInteropURIsValid


📍 *Расположение: `atproto/syntax/uri_test.go:12`*


### automod/capture/capture_test.go


📄 Исходный файл: `automod/capture/capture_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestNoOpCaptureReplyRule](#testnoopcapturereplyrule) `:12`


</details>



---


[test] name: TestNoOpCaptureReplyRule file: automod/capture/capture_test.go:12


#### TestNoOpCaptureReplyRule


📍 *Расположение: `automod/capture/capture_test.go:12`*


### automod/countstore/countstore_test.go


📄 Исходный файл: `automod/countstore/countstore_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestMemCountStoreBasics](#testmemcountstorebasics) `:12`

- 🔗 [TestMemCountStoreConcurrent](#testmemcountstoreconcurrent) `:50`


</details>



---


[test] name: TestMemCountStoreBasics file: automod/countstore/countstore_test.go:12


#### TestMemCountStoreBasics


📍 *Расположение: `automod/countstore/countstore_test.go:12`*



---


[test] name: TestMemCountStoreConcurrent file: automod/countstore/countstore_test.go:50


#### TestMemCountStoreConcurrent


📍 *Расположение: `automod/countstore/countstore_test.go:50`*


### automod/engine/action_dedupe_test.go


📄 Исходный файл: `automod/engine/action_dedupe_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestAccountReportDedupe](#testaccountreportdedupe) `:21`


</details>



---


[test] name: TestAccountReportDedupe file: automod/engine/action_dedupe_test.go:21


#### TestAccountReportDedupe


📍 *Расположение: `automod/engine/action_dedupe_test.go:21`*


### automod/engine/cid_from_cdn_test.go


📄 Исходный файл: `automod/engine/cid_from_cdn_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestCidFromCdnUrl](#testcidfromcdnurl) `:8`


</details>



---


[test] name: TestCidFromCdnUrl file: automod/engine/cid_from_cdn_test.go:8


#### TestCidFromCdnUrl


📍 *Расположение: `automod/engine/cid_from_cdn_test.go:8`*


### automod/engine/circuit_breaker_test.go


📄 Исходный файл: `automod/engine/circuit_breaker_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestReportCircuitBreaker](#testreportcircuitbreaker) `:73`

- 🔗 [TestTakedownCircuitBreaker](#testtakedowncircuitbreaker) `:27`


</details>



---


[test] name: TestReportCircuitBreaker file: automod/engine/circuit_breaker_test.go:73


#### TestReportCircuitBreaker


📍 *Расположение: `automod/engine/circuit_breaker_test.go:73`*



---


[test] name: TestTakedownCircuitBreaker file: automod/engine/circuit_breaker_test.go:27


#### TestTakedownCircuitBreaker


📍 *Расположение: `automod/engine/circuit_breaker_test.go:27`*


### automod/engine/engine_test.go


📄 Исходный файл: `automod/engine/engine_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestEngineBasics](#testenginebasics) `:15`


</details>



---


[test] name: TestEngineBasics file: automod/engine/engine_test.go:15


#### TestEngineBasics


📍 *Расположение: `automod/engine/engine_test.go:15`*


### automod/flagstore/flagstore_redis_test.go


📄 Исходный файл: `automod/flagstore/flagstore_redis_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestRedisFlagStoreBasics](#testredisflagstorebasics) `:10`


</details>



---


[test] name: TestRedisFlagStoreBasics file: automod/flagstore/flagstore_redis_test.go:10


#### TestRedisFlagStoreBasics


📍 *Расположение: `automod/flagstore/flagstore_redis_test.go:10`*


### automod/flagstore/flagstore_test.go


📄 Исходный файл: `automod/flagstore/flagstore_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestFlagStoreBasics](#testflagstorebasics) `:10`


</details>



---


[test] name: TestFlagStoreBasics file: automod/flagstore/flagstore_test.go:10


#### TestFlagStoreBasics


📍 *Расположение: `automod/flagstore/flagstore_test.go:10`*


### automod/helpers/account_test.go


📄 Исходный файл: `automod/helpers/account_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestAccountIsYoungerThan](#testaccountisyoungerthan) `:13`


</details>



---


[test] name: TestAccountIsYoungerThan file: automod/helpers/account_test.go:13


#### TestAccountIsYoungerThan


📍 *Расположение: `automod/helpers/account_test.go:13`*


### automod/helpers/bsky_test.go


📄 Исходный файл: `automod/helpers/bsky_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestParentOrRootIsDid](#testparentorrootisdid) `:11`

- 🔗 [TestPostMentionsDid](#testpostmentionsdid) `:90`


</details>



---


[test] name: TestParentOrRootIsDid file: automod/helpers/bsky_test.go:11


#### TestParentOrRootIsDid


📍 *Расположение: `automod/helpers/bsky_test.go:11`*



---


[test] name: TestPostMentionsDid file: automod/helpers/bsky_test.go:90


#### TestPostMentionsDid


📍 *Расположение: `automod/helpers/bsky_test.go:90`*


### automod/helpers/text_test.go


📄 Исходный файл: `automod/helpers/text_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestExtractURL](#testextracturl) `:37`

- 🔗 [TestHashOfString](#testhashofstring) `:59`

- 🔗 [TestTokenizeText](#testtokenizetext) `:11`


</details>



---


[test] name: TestExtractURL file: automod/helpers/text_test.go:37


#### TestExtractURL


📍 *Расположение: `automod/helpers/text_test.go:37`*



---


[test] name: TestHashOfString file: automod/helpers/text_test.go:59


#### TestHashOfString


📍 *Расположение: `automod/helpers/text_test.go:59`*



---


[test] name: TestTokenizeText file: automod/helpers/text_test.go:11


#### TestTokenizeText


📍 *Расположение: `automod/helpers/text_test.go:11`*


### automod/keyword/keyword_test.go


📄 Исходный файл: `automod/keyword/keyword_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestTokenInSet](#testtokeninset) `:9`


</details>



---


[test] name: TestTokenInSet file: automod/keyword/keyword_test.go:9


#### TestTokenInSet


📍 *Расположение: `automod/keyword/keyword_test.go:9`*


### automod/keyword/slur_regex_test.go


📄 Исходный файл: `automod/keyword/slur_regex_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestSlugContainsExplicitSlur](#testslugcontainsexplicitslur) `:9`

- 🔗 [TestStringContainsExplicitSlur](#teststringcontainsexplicitslur) `:47`


</details>



---


[test] name: TestSlugContainsExplicitSlur file: automod/keyword/slur_regex_test.go:9


#### TestSlugContainsExplicitSlur


📍 *Расположение: `automod/keyword/slur_regex_test.go:9`*



---


[test] name: TestStringContainsExplicitSlur file: automod/keyword/slur_regex_test.go:47


#### TestStringContainsExplicitSlur


📍 *Расположение: `automod/keyword/slur_regex_test.go:47`*


### automod/keyword/tokenize_test.go


📄 Исходный файл: `automod/keyword/tokenize_test.go`


<details open>
<summary><b>Тесты в этом файле (4)</b></summary>


- 🔗 [TestTokenizeIdentifier](#testtokenizeidentifier) `:74`

- 🔗 [TestTokenizeText](#testtokenizetext) `:10`

- 🔗 [TestTokenizeTextWithCensorChars](#testtokenizetextwithcensorchars) `:31`

- 🔗 [TestTokenizeTextWithCustomRegex](#testtokenizetextwithcustomregex) `:53`


</details>



---


[test] name: TestTokenizeIdentifier file: automod/keyword/tokenize_test.go:74


#### TestTokenizeIdentifier


📍 *Расположение: `automod/keyword/tokenize_test.go:74`*



---


[test] name: TestTokenizeText file: automod/keyword/tokenize_test.go:10


#### TestTokenizeText


📍 *Расположение: `automod/keyword/tokenize_test.go:10`*



---


[test] name: TestTokenizeTextWithCensorChars file: automod/keyword/tokenize_test.go:31


#### TestTokenizeTextWithCensorChars


📍 *Расположение: `automod/keyword/tokenize_test.go:31`*



---


[test] name: TestTokenizeTextWithCustomRegex file: automod/keyword/tokenize_test.go:53


#### TestTokenizeTextWithCustomRegex


📍 *Расположение: `automod/keyword/tokenize_test.go:53`*


### automod/rules/hashtags_test.go


📄 Исходный файл: `automod/rules/hashtags_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestBadHashtagPostRule](#testbadhashtagpostrule) `:17`


</details>



---


[test] name: TestBadHashtagPostRule file: automod/rules/hashtags_test.go:17


#### TestBadHashtagPostRule


📍 *Расположение: `automod/rules/hashtags_test.go:17`*


### automod/rules/keyword_test.go


📄 Исходный файл: `automod/rules/keyword_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestBadWordHandleRule](#testbadwordhandlerule) `:17`

- 🔗 [TestBadWordPostRule](#testbadwordpostrule) `:57`


</details>



---


[test] name: TestBadWordHandleRule file: automod/rules/keyword_test.go:17


#### TestBadWordHandleRule


📍 *Расположение: `automod/rules/keyword_test.go:17`*



---


[test] name: TestBadWordPostRule file: automod/rules/keyword_test.go:57


#### TestBadWordPostRule


📍 *Расположение: `automod/rules/keyword_test.go:57`*


### automod/rules/misleading_test.go


📄 Исходный файл: `automod/rules/misleading_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestIsMisleadingURL](#testismisleadingurl) `:117`

- 🔗 [TestMisleadingMentionPostRule](#testmisleadingmentionpostrule) `:66`

- 🔗 [TestMisleadingURLPostRule](#testmisleadingurlpostrule) `:19`


</details>



---


[test] name: TestIsMisleadingURL file: automod/rules/misleading_test.go:117


#### TestIsMisleadingURL


📍 *Расположение: `automod/rules/misleading_test.go:117`*



---


[test] name: TestMisleadingMentionPostRule file: automod/rules/misleading_test.go:66


#### TestMisleadingMentionPostRule


📍 *Расположение: `automod/rules/misleading_test.go:66`*



---


[test] name: TestMisleadingURLPostRule file: automod/rules/misleading_test.go:19


#### TestMisleadingURLPostRule


📍 *Расположение: `automod/rules/misleading_test.go:19`*


### automod/rules/replies_test.go


📄 Исходный файл: `automod/rules/replies_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestIdenticalReplyPostRule](#testidenticalreplypostrule) `:14`


</details>



---


[test] name: TestIdenticalReplyPostRule file: automod/rules/replies_test.go:14


#### TestIdenticalReplyPostRule


📍 *Расположение: `automod/rules/replies_test.go:14`*


### automod/visual/hiveai_test.go


📄 Исходный файл: `automod/visual/hiveai_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestHiveParse](#testhiveparse) `:11`


</details>



---


[test] name: TestHiveParse file: automod/visual/hiveai_test.go:11


#### TestHiveParse


📍 *Расположение: `automod/visual/hiveai_test.go:11`*


### backfill/backfill_test.go


📄 Исходный файл: `backfill/backfill_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestBackfill](#testbackfill) `:20`


</details>



---


[test] name: TestBackfill file: backfill/backfill_test.go:20


#### TestBackfill


📍 *Расположение: `backfill/backfill_test.go:20`*


### carstore/repo_test.go


📄 Исходный файл: `carstore/repo_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestBasicOperation](#testbasicoperation) `:99`

- 🔗 [TestDuplicateBlockAcrossShards](#testduplicateblockacrossshards) `:495`

- 🔗 [TestRepeatedCompactions](#testrepeatedcompactions) `:185`


</details>



---


[test] name: TestBasicOperation file: carstore/repo_test.go:99


#### TestBasicOperation


📍 *Расположение: `carstore/repo_test.go:99`*



---


[test] name: TestDuplicateBlockAcrossShards file: carstore/repo_test.go:495


#### TestDuplicateBlockAcrossShards


📍 *Расположение: `carstore/repo_test.go:495`*



---


[test] name: TestRepeatedCompactions file: carstore/repo_test.go:185


#### TestRepeatedCompactions


📍 *Расположение: `carstore/repo_test.go:185`*


### cmd/collectiondir/pebble_test.go


📄 Исходный файл: `cmd/collectiondir/pebble_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestPebbleCollectionDirectory](#testpebblecollectiondirectory) `:58`


</details>



---


[test] name: TestPebbleCollectionDirectory file: cmd/collectiondir/pebble_test.go:58


#### TestPebbleCollectionDirectory


📍 *Расположение: `cmd/collectiondir/pebble_test.go:58`*


### cmd/relay/relay/account_test.go


📄 Исходный файл: `cmd/relay/relay/account_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestNormalizeDID](#testnormalizedid) `:16`


</details>



---


[test] name: TestNormalizeDID file: cmd/relay/relay/account_test.go:16


#### TestNormalizeDID


📍 *Расположение: `cmd/relay/relay/account_test.go:16`*


### cmd/relay/relay/host_checker_test.go


📄 Исходный файл: `cmd/relay/relay/host_checker_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestLiveHostChecker](#testlivehostchecker) `:36`

- 🔗 [TestMockHostChecker](#testmockhostchecker) `:14`


</details>



---


[test] name: TestLiveHostChecker file: cmd/relay/relay/host_checker_test.go:36 description: NOTE: this test does live network resolutions


#### TestLiveHostChecker


NOTE: this test does live network resolutions


📍 *Расположение: `cmd/relay/relay/host_checker_test.go:36`*



---


[test] name: TestMockHostChecker file: cmd/relay/relay/host_checker_test.go:14


#### TestMockHostChecker


📍 *Расположение: `cmd/relay/relay/host_checker_test.go:14`*


### cmd/relay/relay/host_test.go


📄 Исходный файл: `cmd/relay/relay/host_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestIsTrustedDomain](#testistrusteddomain) `:54`

- 🔗 [TestParseHostname](#testparsehostname) `:16`


</details>



---


[test] name: TestIsTrustedDomain file: cmd/relay/relay/host_test.go:54


#### TestIsTrustedDomain


📍 *Расположение: `cmd/relay/relay/host_test.go:54`*



---


[test] name: TestParseHostname file: cmd/relay/relay/host_test.go:16


#### TestParseHostname


📍 *Расположение: `cmd/relay/relay/host_test.go:16`*


### cmd/relay/relay/models/methods_test.go


📄 Исходный файл: `cmd/relay/relay/models/methods_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestHostURLs](#testhosturls) `:9`


</details>



---


[test] name: TestHostURLs file: cmd/relay/relay/models/methods_test.go:9


#### TestHostURLs


📍 *Расположение: `cmd/relay/relay/models/methods_test.go:9`*


### cmd/relay/stream/persist/diskpersist/diskpersist_test.go


📄 Исходный файл: `cmd/relay/stream/persist/diskpersist/diskpersist_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestInitialSequenceNumber](#testinitialsequencenumber) `:28`


</details>



---


[test] name: TestInitialSequenceNumber file: cmd/relay/stream/persist/diskpersist/diskpersist_test.go:28


#### TestInitialSequenceNumber


📍 *Расположение: `cmd/relay/stream/persist/diskpersist/diskpersist_test.go:28`*


### cmd/relay/testing/framework_test.go


📄 Исходный файл: `cmd/relay/testing/framework_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestBasicScenario](#testbasicscenario) `:82`

- 🔗 [TestFramework](#testframework) `:18`

- 🔗 [TestScenarioLoad](#testscenarioload) `:55`


</details>



---


[test] name: TestBasicScenario file: cmd/relay/testing/framework_test.go:82


#### TestBasicScenario


📍 *Расположение: `cmd/relay/testing/framework_test.go:82`*



---


[test] name: TestFramework file: cmd/relay/testing/framework_test.go:18 description: meta test for the testing framework itself. simply connects the consumer to the 


#### TestFramework


meta test for the testing framework itself. simply connects the consumer to the producer


📍 *Расположение: `cmd/relay/testing/framework_test.go:18`*



---


[test] name: TestScenarioLoad file: cmd/relay/testing/framework_test.go:55 description: simply loads a scenario from JSON and checks data looks right


#### TestScenarioLoad


simply loads a scenario from JSON and checks data looks right


📍 *Расположение: `cmd/relay/testing/framework_test.go:55`*


### cmd/relay/testing/sync_test.go


📄 Исходный файл: `cmd/relay/testing/sync_test.go`


<details open>
<summary><b>Тесты в этом файле (7)</b></summary>


- 🔗 [TestAccountLifecycle](#testaccountlifecycle) `:65`

- 🔗 [TestDeactivationScenario](#testdeactivationscenario) `:38`

- 🔗 [TestLegacyScenario](#testlegacyscenario) `:82`

- 🔗 [TestPostScenarios](#testpostscenarios) `:10`

- 🔗 [TestRevOrderingScenario](#testrevorderingscenario) `:47`

- 🔗 [TestSeqOrderingScenario](#testseqorderingscenario) `:56`

- 🔗 [TestWrongKey](#testwrongkey) `:19`


</details>



---


[test] name: TestAccountLifecycle file: cmd/relay/testing/sync_test.go:65


#### TestAccountLifecycle


📍 *Расположение: `cmd/relay/testing/sync_test.go:65`*



---


[test] name: TestDeactivationScenario file: cmd/relay/testing/sync_test.go:38


#### TestDeactivationScenario


📍 *Расположение: `cmd/relay/testing/sync_test.go:38`*



---


[test] name: TestLegacyScenario file: cmd/relay/testing/sync_test.go:82


#### TestLegacyScenario


📍 *Расположение: `cmd/relay/testing/sync_test.go:82`*



---


[test] name: TestPostScenarios file: cmd/relay/testing/sync_test.go:10


#### TestPostScenarios


📍 *Расположение: `cmd/relay/testing/sync_test.go:10`*



---


[test] name: TestRevOrderingScenario file: cmd/relay/testing/sync_test.go:47


#### TestRevOrderingScenario


📍 *Расположение: `cmd/relay/testing/sync_test.go:47`*



---


[test] name: TestSeqOrderingScenario file: cmd/relay/testing/sync_test.go:56


#### TestSeqOrderingScenario


📍 *Расположение: `cmd/relay/testing/sync_test.go:56`*



---


[test] name: TestWrongKey file: cmd/relay/testing/sync_test.go:19


#### TestWrongKey


📍 *Расположение: `cmd/relay/testing/sync_test.go:19`*


### cmd/tap/firehose_test.go


📄 Исходный файл: `cmd/tap/firehose_test.go`


<details open>
<summary><b>Тесты в этом файле (18)</b></summary>


- 🔗 [TestCursorSaveAndLoad](#testcursorsaveandload) `:516`

- 🔗 [TestGetCursor_NoPriorSave](#testgetcursor_nopriorsave) `:503`

- 🔗 [TestProcessAccount_Deactivation](#testprocessaccount_deactivation) `:129`

- 🔗 [TestProcessAccount_Deletion](#testprocessaccount_deletion) `:195`

- 🔗 [TestProcessAccount_FullNetworkAutoTrack](#testprocessaccount_fullnetworkautotrack) `:297`

- 🔗 [TestProcessAccount_FullNetworkInactiveSkipped](#testprocessaccount_fullnetworkinactiveskipped) `:476`

- 🔗 [TestProcessAccount_NoOpSameStatus](#testprocessaccount_noopsamestatus) `:247`

- 🔗 [TestProcessAccount_Reactivation](#testprocessaccount_reactivation) `:162`

- 🔗 [TestProcessAccount_UnknownStatus](#testprocessaccount_unknownstatus) `:442`

- 🔗 [TestProcessAccount_UntrackedRepo](#testprocessaccount_untrackedrepo) `:272`

- 🔗 [TestProcessCommit_SkipsReplayedRev](#testprocesscommit_skipsreplayedrev) `:100`

- 🔗 [TestProcessCommit_SkipsWrongState](#testprocesscommit_skipswrongstate) `:74`

- 🔗 [TestProcessCommit_UntrackedRepo](#testprocesscommit_untrackedrepo) `:26`

- 🔗 [TestProcessCommit_UntrackedRepo_FullNetworkAutoTrack](#testprocesscommit_untrackedrepo_fullnetworkautotrack) `:49`

- 🔗 [TestProcessIdentity_FullNetworkAutoTrack](#testprocessidentity_fullnetworkautotrack) `:417`

- 🔗 [TestProcessIdentity_HandleChange](#testprocessidentity_handlechange) `:323`

- 🔗 [TestProcessIdentity_NoChange](#testprocessidentity_nochange) `:362`

- 🔗 [TestProcessIdentity_UntrackedRepo](#testprocessidentity_untrackedrepo) `:393`


</details>



---


[test] name: TestCursorSaveAndLoad file: cmd/tap/firehose_test.go:516


#### TestCursorSaveAndLoad


📍 *Расположение: `cmd/tap/firehose_test.go:516`*



---


[test] name: TestGetCursor_NoPriorSave file: cmd/tap/firehose_test.go:503 description: --- Cursor management tests ---


#### TestGetCursor_NoPriorSave


--- Cursor management tests ---


📍 *Расположение: `cmd/tap/firehose_test.go:503`*



---


[test] name: TestProcessAccount_Deactivation file: cmd/tap/firehose_test.go:129 description: --- ProcessAccount tests ---


#### TestProcessAccount_Deactivation


--- ProcessAccount tests ---


📍 *Расположение: `cmd/tap/firehose_test.go:129`*



---


[test] name: TestProcessAccount_Deletion file: cmd/tap/firehose_test.go:195


#### TestProcessAccount_Deletion


📍 *Расположение: `cmd/tap/firehose_test.go:195`*



---


[test] name: TestProcessAccount_FullNetworkAutoTrack file: cmd/tap/firehose_test.go:297


#### TestProcessAccount_FullNetworkAutoTrack


📍 *Расположение: `cmd/tap/firehose_test.go:297`*



---


[test] name: TestProcessAccount_FullNetworkInactiveSkipped file: cmd/tap/firehose_test.go:476


#### TestProcessAccount_FullNetworkInactiveSkipped


📍 *Расположение: `cmd/tap/firehose_test.go:476`*



---


[test] name: TestProcessAccount_NoOpSameStatus file: cmd/tap/firehose_test.go:247


#### TestProcessAccount_NoOpSameStatus


📍 *Расположение: `cmd/tap/firehose_test.go:247`*



---


[test] name: TestProcessAccount_Reactivation file: cmd/tap/firehose_test.go:162


#### TestProcessAccount_Reactivation


📍 *Расположение: `cmd/tap/firehose_test.go:162`*



---


[test] name: TestProcessAccount_UnknownStatus file: cmd/tap/firehose_test.go:442


#### TestProcessAccount_UnknownStatus


📍 *Расположение: `cmd/tap/firehose_test.go:442`*



---


[test] name: TestProcessAccount_UntrackedRepo file: cmd/tap/firehose_test.go:272


#### TestProcessAccount_UntrackedRepo


📍 *Расположение: `cmd/tap/firehose_test.go:272`*



---


[test] name: TestProcessCommit_SkipsReplayedRev file: cmd/tap/firehose_test.go:100


#### TestProcessCommit_SkipsReplayedRev


📍 *Расположение: `cmd/tap/firehose_test.go:100`*



---


[test] name: TestProcessCommit_SkipsWrongState file: cmd/tap/firehose_test.go:74


#### TestProcessCommit_SkipsWrongState


📍 *Расположение: `cmd/tap/firehose_test.go:74`*



---


[test] name: TestProcessCommit_UntrackedRepo file: cmd/tap/firehose_test.go:26 description: --- ProcessCommit skip path tests ---


#### TestProcessCommit_UntrackedRepo


--- ProcessCommit skip path tests ---


📍 *Расположение: `cmd/tap/firehose_test.go:26`*



---


[test] name: TestProcessCommit_UntrackedRepo_FullNetworkAutoTrack file: cmd/tap/firehose_test.go:49


#### TestProcessCommit_UntrackedRepo_FullNetworkAutoTrack


📍 *Расположение: `cmd/tap/firehose_test.go:49`*



---


[test] name: TestProcessIdentity_FullNetworkAutoTrack file: cmd/tap/firehose_test.go:417


#### TestProcessIdentity_FullNetworkAutoTrack


📍 *Расположение: `cmd/tap/firehose_test.go:417`*



---


[test] name: TestProcessIdentity_HandleChange file: cmd/tap/firehose_test.go:323 description: --- ProcessIdentity tests ---


#### TestProcessIdentity_HandleChange


--- ProcessIdentity tests ---


📍 *Расположение: `cmd/tap/firehose_test.go:323`*



---


[test] name: TestProcessIdentity_NoChange file: cmd/tap/firehose_test.go:362


#### TestProcessIdentity_NoChange


📍 *Расположение: `cmd/tap/firehose_test.go:362`*



---


[test] name: TestProcessIdentity_UntrackedRepo file: cmd/tap/firehose_test.go:393


#### TestProcessIdentity_UntrackedRepo


📍 *Расположение: `cmd/tap/firehose_test.go:393`*


### cmd/tap/outbox_test.go


📄 Исходный файл: `cmd/tap/outbox_test.go`


<details open>
<summary><b>Тесты в этом файле (10)</b></summary>


- 🔗 [TestFireAndForget_BasicDelivery](#testfireandforget_basicdelivery) `:12`

- 🔗 [TestFireAndForget_MultiDID](#testfireandforget_multidid) `:36`

- 🔗 [TestIdentityEvent_Delivery](#testidentityevent_delivery) `:285`

- 🔗 [TestWebhook_BasicDelivery](#testwebhook_basicdelivery) `:269`

- 🔗 [TestWebsocketAck_BasicDelivery](#testwebsocketack_basicdelivery) `:68`

- 🔗 [TestWebsocketAck_ConsecutiveLiveEvents](#testwebsocketack_consecutiveliveevents) `:168`

- 🔗 [TestWebsocketAck_FastPathLiveBlocksHistorical](#testwebsocketack_fastpathliveblockshistorical) `:212`

- 🔗 [TestWebsocketAck_NoStallOnPreconnectEvents](#testwebsocketack_nostallonpreconnectevents) `:249`

- 🔗 [TestWebsocketAck_OrderingHistorical](#testwebsocketack_orderinghistorical) `:91`

- 🔗 [TestWebsocketAck_OrderingLiveBarrier](#testwebsocketack_orderinglivebarrier) `:113`


</details>



---


[test] name: TestFireAndForget_BasicDelivery file: cmd/tap/outbox_test.go:12


#### TestFireAndForget_BasicDelivery


📍 *Расположение: `cmd/tap/outbox_test.go:12`*



---


[test] name: TestFireAndForget_MultiDID file: cmd/tap/outbox_test.go:36


#### TestFireAndForget_MultiDID


📍 *Расположение: `cmd/tap/outbox_test.go:36`*



---


[test] name: TestIdentityEvent_Delivery file: cmd/tap/outbox_test.go:285


#### TestIdentityEvent_Delivery


📍 *Расположение: `cmd/tap/outbox_test.go:285`*



---


[test] name: TestWebhook_BasicDelivery file: cmd/tap/outbox_test.go:269


#### TestWebhook_BasicDelivery


📍 *Расположение: `cmd/tap/outbox_test.go:269`*



---


[test] name: TestWebsocketAck_BasicDelivery file: cmd/tap/outbox_test.go:68


#### TestWebsocketAck_BasicDelivery


📍 *Расположение: `cmd/tap/outbox_test.go:68`*



---


[test] name: TestWebsocketAck_ConsecutiveLiveEvents file: cmd/tap/outbox_test.go:168


#### TestWebsocketAck_ConsecutiveLiveEvents


📍 *Расположение: `cmd/tap/outbox_test.go:168`*



---


[test] name: TestWebsocketAck_FastPathLiveBlocksHistorical file: cmd/tap/outbox_test.go:212 description: TestWebsocketAck_FastPathLiveBlocksHistorical verifies that when a live event
is


#### TestWebsocketAck_FastPathLiveBlocksHistorical


TestWebsocketAck_FastPathLiveBlocksHistorical verifies that when a live event
is sent via the DIDWorker's fast path (first event for a DID), subsequent
historical events are blocked until the live event is acked.
Regression test for: bugfix(cmd/tap): prevent DID worker live-barrier stall


📍 *Расположение: `cmd/tap/outbox_test.go:212`*



---


[test] name: TestWebsocketAck_NoStallOnPreconnectEvents file: cmd/tap/outbox_test.go:249


#### TestWebsocketAck_NoStallOnPreconnectEvents


📍 *Расположение: `cmd/tap/outbox_test.go:249`*



---


[test] name: TestWebsocketAck_OrderingHistorical file: cmd/tap/outbox_test.go:91


#### TestWebsocketAck_OrderingHistorical


📍 *Расположение: `cmd/tap/outbox_test.go:91`*



---


[test] name: TestWebsocketAck_OrderingLiveBarrier file: cmd/tap/outbox_test.go:113


#### TestWebsocketAck_OrderingLiveBarrier


📍 *Расположение: `cmd/tap/outbox_test.go:113`*


### cmd/tap/resyncer_test.go


📄 Исходный файл: `cmd/tap/resyncer_test.go`


<details open>
<summary><b>Тесты в этом файле (10)</b></summary>


- 🔗 [TestClaimResyncJob_NoneAvailable](#testclaimresyncjob_noneavailable) `:93`

- 🔗 [TestClaimResyncJob_Priority](#testclaimresyncjob_priority) `:23`

- 🔗 [TestClaimResyncJob_RetryAfterRespected](#testclaimresyncjob_retryafterrespected) `:59`

- 🔗 [TestDrainResyncBuffer_Basic](#testdrainresyncbuffer_basic) `:224`

- 🔗 [TestDrainResyncBuffer_ChainedCommits](#testdrainresyncbuffer_chainedcommits) `:330`

- 🔗 [TestDrainResyncBuffer_SkipsMismatchedPrevData](#testdrainresyncbuffer_skipsmismatchedprevdata) `:282`

- 🔗 [TestHandleResyncError_ExponentialBackoff](#testhandleresyncerror_exponentialbackoff) `:163`

- 🔗 [TestHandleResyncError_WithError](#testhandleresyncerror_witherror) `:109`

- 🔗 [TestHandleResyncError_WithNilError](#testhandleresyncerror_withnilerror) `:140`

- 🔗 [TestResetPartiallyResynced](#testresetpartiallyresynced) `:194`


</details>



---


[test] name: TestClaimResyncJob_NoneAvailable file: cmd/tap/resyncer_test.go:93


#### TestClaimResyncJob_NoneAvailable


📍 *Расположение: `cmd/tap/resyncer_test.go:93`*



---


[test] name: TestClaimResyncJob_Priority file: cmd/tap/resyncer_test.go:23 description: --- claimResyncJob tests ---


#### TestClaimResyncJob_Priority


--- claimResyncJob tests ---


📍 *Расположение: `cmd/tap/resyncer_test.go:23`*



---


[test] name: TestClaimResyncJob_RetryAfterRespected file: cmd/tap/resyncer_test.go:59


#### TestClaimResyncJob_RetryAfterRespected


📍 *Расположение: `cmd/tap/resyncer_test.go:59`*



---


[test] name: TestDrainResyncBuffer_Basic file: cmd/tap/resyncer_test.go:224 description: --- drainResyncBuffer tests ---


#### TestDrainResyncBuffer_Basic


--- drainResyncBuffer tests ---


📍 *Расположение: `cmd/tap/resyncer_test.go:224`*



---


[test] name: TestDrainResyncBuffer_ChainedCommits file: cmd/tap/resyncer_test.go:330


#### TestDrainResyncBuffer_ChainedCommits


📍 *Расположение: `cmd/tap/resyncer_test.go:330`*



---


[test] name: TestDrainResyncBuffer_SkipsMismatchedPrevData file: cmd/tap/resyncer_test.go:282


#### TestDrainResyncBuffer_SkipsMismatchedPrevData


📍 *Расположение: `cmd/tap/resyncer_test.go:282`*



---


[test] name: TestHandleResyncError_ExponentialBackoff file: cmd/tap/resyncer_test.go:163


#### TestHandleResyncError_ExponentialBackoff


📍 *Расположение: `cmd/tap/resyncer_test.go:163`*



---


[test] name: TestHandleResyncError_WithError file: cmd/tap/resyncer_test.go:109 description: --- handleResyncError tests ---


#### TestHandleResyncError_WithError


--- handleResyncError tests ---


📍 *Расположение: `cmd/tap/resyncer_test.go:109`*



---


[test] name: TestHandleResyncError_WithNilError file: cmd/tap/resyncer_test.go:140


#### TestHandleResyncError_WithNilError


📍 *Расположение: `cmd/tap/resyncer_test.go:140`*



---


[test] name: TestResetPartiallyResynced file: cmd/tap/resyncer_test.go:194 description: --- resetPartiallyResynced tests ---


#### TestResetPartiallyResynced


--- resetPartiallyResynced tests ---


📍 *Расположение: `cmd/tap/resyncer_test.go:194`*


### cmd/tap/server_test.go


📄 Исходный файл: `cmd/tap/server_test.go`


<details open>
<summary><b>Тесты в этом файле (6)</b></summary>


- 🔗 [TestAddAndRemoveRepos](#testaddandremoverepos) `:31`

- 🔗 [TestHealthcheck](#testhealthcheck) `:15`

- 🔗 [TestStatsOutboxBuffer](#teststatsoutboxbuffer) `:99`

- 🔗 [TestStatsRecordCount](#teststatsrecordcount) `:80`

- 🔗 [TestStatsRepoCount](#teststatsrepocount) `:62`

- 🔗 [TestStatsResyncBuffer](#teststatsresyncbuffer) `:116`


</details>



---


[test] name: TestAddAndRemoveRepos file: cmd/tap/server_test.go:31


#### TestAddAndRemoveRepos


📍 *Расположение: `cmd/tap/server_test.go:31`*



---


[test] name: TestHealthcheck file: cmd/tap/server_test.go:15


#### TestHealthcheck


📍 *Расположение: `cmd/tap/server_test.go:15`*



---


[test] name: TestStatsOutboxBuffer file: cmd/tap/server_test.go:99


#### TestStatsOutboxBuffer


📍 *Расположение: `cmd/tap/server_test.go:99`*



---


[test] name: TestStatsRecordCount file: cmd/tap/server_test.go:80


#### TestStatsRecordCount


📍 *Расположение: `cmd/tap/server_test.go:80`*



---


[test] name: TestStatsRepoCount file: cmd/tap/server_test.go:62


#### TestStatsRepoCount


📍 *Расположение: `cmd/tap/server_test.go:62`*



---


[test] name: TestStatsResyncBuffer file: cmd/tap/server_test.go:116


#### TestStatsResyncBuffer


📍 *Расположение: `cmd/tap/server_test.go:116`*


### cmd/tap/util_test.go


📄 Исходный файл: `cmd/tap/util_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestRunPeriodicallyReturnsOnContextCancel](#testrunperiodicallyreturnsoncontextcancel) `:43`

- 🔗 [TestRunPeriodicallyStopsOnTaskError](#testrunperiodicallystopsontaskerror) `:12`


</details>



---


[test] name: TestRunPeriodicallyReturnsOnContextCancel file: cmd/tap/util_test.go:43


#### TestRunPeriodicallyReturnsOnContextCancel


📍 *Расположение: `cmd/tap/util_test.go:43`*



---


[test] name: TestRunPeriodicallyStopsOnTaskError file: cmd/tap/util_test.go:12


#### TestRunPeriodicallyStopsOnTaskError


📍 *Расположение: `cmd/tap/util_test.go:12`*


### events/diskpersist/diskpersist_test.go


📄 Исходный файл: `events/diskpersist/diskpersist_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestDiskPersist](#testdiskpersist) `:163`

- 🔗 [TestDiskPersister](#testdiskpersister) `:290`

- 🔗 [TestDiskPersisterTakedowns](#testdiskpersistertakedowns) `:397`


</details>



---


[test] name: TestDiskPersist file: events/diskpersist/diskpersist_test.go:163


#### TestDiskPersist


📍 *Расположение: `events/diskpersist/diskpersist_test.go:163`*



---


[test] name: TestDiskPersister file: events/diskpersist/diskpersist_test.go:290


#### TestDiskPersister


📍 *Расположение: `events/diskpersist/diskpersist_test.go:290`*



---


[test] name: TestDiskPersisterTakedowns file: events/diskpersist/diskpersist_test.go:397


#### TestDiskPersisterTakedowns


📍 *Расположение: `events/diskpersist/diskpersist_test.go:397`*


### events/pebblepersist/pebblepersist_test.go


📄 Исходный файл: `events/pebblepersist/pebblepersist_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestPebblePersist](#testpebblepersist) `:25`


</details>



---


[test] name: TestPebblePersist file: events/pebblepersist/pebblepersist_test.go:25


#### TestPebblePersist


📍 *Расположение: `events/pebblepersist/pebblepersist_test.go:25`*


### fakedata/localinterop_test.go


📄 Исходный файл: `fakedata/localinterop_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestFakedataLocalInterop](#testfakedatalocalinterop) `:55`


</details>



---


[test] name: TestFakedataLocalInterop file: fakedata/localinterop_test.go:55 description: runs basic fakedata generation against a local PDS process. eg, the
typescript i


#### TestFakedataLocalInterop


runs basic fakedata generation against a local PDS process. eg, the
typescript implementation, running locally or in docker


📍 *Расположение: `fakedata/localinterop_test.go:55`*


### lex/gen_test.go


📄 Исходный файл: `lex/gen_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestParsePackages](#testparsepackages) `:5`


</details>



---


[test] name: TestParsePackages file: lex/gen_test.go:5


#### TestParsePackages


📍 *Расположение: `lex/gen_test.go:5`*


### lex/lexgen/util_test.go


📄 Исходный файл: `lex/lexgen/util_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestNSIDNames](#testnsidnames) `:11`


</details>



---


[test] name: TestNSIDNames file: lex/lexgen/util_test.go:11


#### TestNSIDNames


📍 *Расположение: `lex/lexgen/util_test.go:11`*


### lex/lexlint/lint_test.go


📄 Исходный файл: `lex/lexlint/lint_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestLexLintFixtures](#testlexlintfixtures) `:21`


</details>



---


[test] name: TestLexLintFixtures file: lex/lexlint/lint_test.go:21


#### TestLexLintFixtures


📍 *Расположение: `lex/lexlint/lint_test.go:21`*


### lex/lexlint/syntax_test.go


📄 Исходный файл: `lex/lexlint/syntax_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestCheckSchemaName](#testcheckschemaname) `:9`


</details>



---


[test] name: TestCheckSchemaName file: lex/lexlint/syntax_test.go:9


#### TestCheckSchemaName


📍 *Расположение: `lex/lexlint/syntax_test.go:9`*


### lex/util/decoder_test.go


📄 Исходный файл: `lex/util/decoder_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestLTDMarshal](#testltdmarshal) `:7`

- 🔗 [TestNewFromType](#testnewfromtype) `:24`


</details>



---


[test] name: TestLTDMarshal file: lex/util/decoder_test.go:7


#### TestLTDMarshal


📍 *Расположение: `lex/util/decoder_test.go:7`*



---


[test] name: TestNewFromType file: lex/util/decoder_test.go:24


#### TestNewFromType


📍 *Расположение: `lex/util/decoder_test.go:24`*


### lex/util/lex_interop_old_test.go


📄 Исходный файл: `lex/util/lex_interop_old_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestInteropBasicOldSchema](#testinteropbasicoldschema) `:37`

- 🔗 [TestInteropIpldOldSchema](#testinteropipldoldschema) `:109`


</details>



---


[test] name: TestInteropBasicOldSchema file: lex/util/lex_interop_old_test.go:37


#### TestInteropBasicOldSchema


📍 *Расположение: `lex/util/lex_interop_old_test.go:37`*



---


[test] name: TestInteropIpldOldSchema file: lex/util/lex_interop_old_test.go:109


#### TestInteropIpldOldSchema


📍 *Расположение: `lex/util/lex_interop_old_test.go:109`*


### lex/util/lex_interop_test.go


📄 Исходный файл: `lex/util/lex_interop_test.go`


<details open>
<summary><b>Тесты в этом файле (4)</b></summary>


- 🔗 [TestCborGen](#testcborgen) `:51`

- 🔗 [TestInteropBasicSchema](#testinteropbasicschema) `:57`

- 🔗 [TestInteropIpldNestedSchema](#testinteropipldnestedschema) `:226`

- 🔗 [TestInteropIpldSchema](#testinteropipldschema) `:140`


</details>



---


[test] name: TestCborGen file: lex/util/lex_interop_test.go:51


#### TestCborGen


📍 *Расположение: `lex/util/lex_interop_test.go:51`*



---


[test] name: TestInteropBasicSchema file: lex/util/lex_interop_test.go:57


#### TestInteropBasicSchema


📍 *Расположение: `lex/util/lex_interop_test.go:57`*



---


[test] name: TestInteropIpldNestedSchema file: lex/util/lex_interop_test.go:226


#### TestInteropIpldNestedSchema


📍 *Расположение: `lex/util/lex_interop_test.go:226`*



---


[test] name: TestInteropIpldSchema file: lex/util/lex_interop_test.go:140


#### TestInteropIpldSchema


📍 *Расположение: `lex/util/lex_interop_test.go:140`*


### lex/util/lex_types_test.go


📄 Исходный файл: `lex/util/lex_types_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestBlobParse](#testblobparse) `:16`


</details>



---


[test] name: TestBlobParse file: lex/util/lex_types_test.go:16


#### TestBlobParse


📍 *Расположение: `lex/util/lex_types_test.go:16`*


### mst/mst_interop_test.go


📄 Исходный файл: `mst/mst_interop_test.go`


<details open>
<summary><b>Тесты в этом файле (10)</b></summary>


- 🔗 [TestAllowedKeys](#testallowedkeys) `:85`

- 🔗 [TestInteropEdgeCasesHigher](#testinteropedgecaseshigher) `:340`

- 🔗 [TestInteropEdgeCasesInsertion](#testinteropedgecasesinsertion) `:280`

- 🔗 [TestInteropEdgeCasesTrimTop](#testinteropedgecasestrimtop) `:243`

- 🔗 [TestInteropKnownMaps](#testinteropknownmaps) `:195`

- 🔗 [TestInteropKnownMapsTricky](#testinteropknownmapstricky) `:226`

- 🔗 [TestLeadingZeros](#testleadingzeros) `:17`

- 🔗 [TestManualNode](#testmanualnode) `:160`

- 🔗 [TestPrefixLen](#testprefixlen) `:30`

- 🔗 [TestPrefixLenWide](#testprefixlenwide) `:46`


</details>



---


[test] name: TestAllowedKeys file: mst/mst_interop_test.go:85


#### TestAllowedKeys


📍 *Расположение: `mst/mst_interop_test.go:85`*



---


[test] name: TestInteropEdgeCasesHigher file: mst/mst_interop_test.go:340 description: "handles new layers that are two higher than existing"


#### TestInteropEdgeCasesHigher


"handles new layers that are two higher than existing"


📍 *Расположение: `mst/mst_interop_test.go:340`*



---


[test] name: TestInteropEdgeCasesInsertion file: mst/mst_interop_test.go:280


#### TestInteropEdgeCasesInsertion


📍 *Расположение: `mst/mst_interop_test.go:280`*



---


[test] name: TestInteropEdgeCasesTrimTop file: mst/mst_interop_test.go:243 description: "trims top of tree on delete"


#### TestInteropEdgeCasesTrimTop


"trims top of tree on delete"


📍 *Расположение: `mst/mst_interop_test.go:243`*



---


[test] name: TestInteropKnownMaps file: mst/mst_interop_test.go:195


#### TestInteropKnownMaps


📍 *Расположение: `mst/mst_interop_test.go:195`*



---


[test] name: TestInteropKnownMapsTricky file: mst/mst_interop_test.go:226


#### TestInteropKnownMapsTricky


📍 *Расположение: `mst/mst_interop_test.go:226`*



---


[test] name: TestLeadingZeros file: mst/mst_interop_test.go:17


#### TestLeadingZeros


📍 *Расположение: `mst/mst_interop_test.go:17`*



---


[test] name: TestManualNode file: mst/mst_interop_test.go:160


#### TestManualNode


📍 *Расположение: `mst/mst_interop_test.go:160`*



---


[test] name: TestPrefixLen file: mst/mst_interop_test.go:30


#### TestPrefixLen


📍 *Расположение: `mst/mst_interop_test.go:30`*



---


[test] name: TestPrefixLenWide file: mst/mst_interop_test.go:46


#### TestPrefixLenWide


📍 *Расположение: `mst/mst_interop_test.go:46`*


### mst/mst_test.go


📄 Исходный файл: `mst/mst_test.go`


<details open>
<summary><b>Тесты в этом файле (9)</b></summary>


- 🔗 [TestBasicMst](#testbasicmst) `:35`

- 🔗 [TestCountPrefixLen](#testcountprefixlen) `:619`

- 🔗 [TestDiffInsertionsBasic](#testdiffinsertionsbasic) `:182`

- 🔗 [TestDiffInsertionsLarge](#testdiffinsertionslarge) `:207`

- 🔗 [TestDiffMutationsBasic](#testdiffmutationsbasic) `:277`

- 🔗 [TestDiffNoOverlap](#testdiffnooverlap) `:222`

- 🔗 [TestDiffSmallOverlap](#testdiffsmalloverlap) `:237`

- 🔗 [TestDiffSmallOverlapSmall](#testdiffsmalloverlapsmall) `:257`

- 🔗 [TestLeadingZerosOnHashAllocs](#testleadingzerosonhashallocs) `:510`


</details>



---


[test] name: TestBasicMst file: mst/mst_test.go:35


#### TestBasicMst


📍 *Расположение: `mst/mst_test.go:35`*



---


[test] name: TestCountPrefixLen file: mst/mst_test.go:619


#### TestCountPrefixLen


📍 *Расположение: `mst/mst_test.go:619`*



---


[test] name: TestDiffInsertionsBasic file: mst/mst_test.go:182


#### TestDiffInsertionsBasic


📍 *Расположение: `mst/mst_test.go:182`*



---


[test] name: TestDiffInsertionsLarge file: mst/mst_test.go:207


#### TestDiffInsertionsLarge


📍 *Расположение: `mst/mst_test.go:207`*



---


[test] name: TestDiffMutationsBasic file: mst/mst_test.go:277


#### TestDiffMutationsBasic


📍 *Расположение: `mst/mst_test.go:277`*



---


[test] name: TestDiffNoOverlap file: mst/mst_test.go:222


#### TestDiffNoOverlap


📍 *Расположение: `mst/mst_test.go:222`*



---


[test] name: TestDiffSmallOverlap file: mst/mst_test.go:237


#### TestDiffSmallOverlap


📍 *Расположение: `mst/mst_test.go:237`*



---


[test] name: TestDiffSmallOverlapSmall file: mst/mst_test.go:257


#### TestDiffSmallOverlapSmall


📍 *Расположение: `mst/mst_test.go:257`*



---


[test] name: TestLeadingZerosOnHashAllocs file: mst/mst_test.go:510


#### TestLeadingZerosOnHashAllocs


📍 *Расположение: `mst/mst_test.go:510`*


### repo/repo_test.go


📄 Исходный файл: `repo/repo_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestRepo](#testrepo) `:12`


</details>



---


[test] name: TestRepo file: repo/repo_test.go:12


#### TestRepo


📍 *Расположение: `repo/repo_test.go:12`*


### repomgr/ingest_test.go


📄 Исходный файл: `repomgr/ingest_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestDuplicateRecord](#testduplicaterecord) `:191`

- 🔗 [TestIngestWithGap](#testingestwithgap) `:99`

- 🔗 [TestLoadNewRepo](#testloadnewrepo) `:35`


</details>



---


[test] name: TestDuplicateRecord file: repomgr/ingest_test.go:191


#### TestDuplicateRecord


📍 *Расположение: `repomgr/ingest_test.go:191`*



---


[test] name: TestIngestWithGap file: repomgr/ingest_test.go:99


#### TestIngestWithGap


📍 *Расположение: `repomgr/ingest_test.go:99`*



---


[test] name: TestLoadNewRepo file: repomgr/ingest_test.go:35


#### TestLoadNewRepo


📍 *Расположение: `repomgr/ingest_test.go:35`*


### search/japanese_test.go


📄 Исходный файл: `search/japanese_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestJapaneseDetection](#testjapanesedetection) `:9`


</details>



---


[test] name: TestJapaneseDetection file: search/japanese_test.go:9


#### TestJapaneseDetection


📍 *Расположение: `search/japanese_test.go:9`*


### search/parse_query_test.go


📄 Исходный файл: `search/parse_query_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestParseQuery](#testparsequery) `:13`


</details>



---


[test] name: TestParseQuery file: search/parse_query_test.go:13


#### TestParseQuery


📍 *Расположение: `search/parse_query_test.go:13`*


### search/query_test.go


📄 Исходный файл: `search/query_test.go`


<details open>
<summary><b>Тесты в этом файле (2)</b></summary>


- 🔗 [TestJapaneseRegressions](#testjapaneseregressions) `:90`

- 🔗 [TestParsedQuery](#testparsedquery) `:204`


</details>



---


[test] name: TestJapaneseRegressions file: search/query_test.go:90


#### TestJapaneseRegressions


📍 *Расположение: `search/query_test.go:90`*



---


[test] name: TestParsedQuery file: search/query_test.go:204


#### TestParsedQuery


📍 *Расположение: `search/query_test.go:204`*


### search/transform_test.go


📄 Исходный файл: `search/transform_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestParseEmojis](#testparseemojis) `:16`

- 🔗 [TestTransformPostFixtures](#testtransformpostfixtures) `:81`

- 🔗 [TestTransformProfileFixtures](#testtransformprofilefixtures) `:35`


</details>



---


[test] name: TestParseEmojis file: search/transform_test.go:16


#### TestParseEmojis


📍 *Расположение: `search/transform_test.go:16`*



---


[test] name: TestTransformPostFixtures file: search/transform_test.go:81


#### TestTransformPostFixtures


📍 *Расположение: `search/transform_test.go:81`*



---


[test] name: TestTransformProfileFixtures file: search/transform_test.go:35


#### TestTransformProfileFixtures


📍 *Расположение: `search/transform_test.go:35`*


### search/url_test.go


📄 Исходный файл: `search/url_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestNormalizeLossyURL](#testnormalizelossyurl) `:9`


</details>



---


[test] name: TestNormalizeLossyURL file: search/url_test.go:9


#### TestNormalizeLossyURL


📍 *Расположение: `search/url_test.go:9`*


### testing/car_did_repro_test.go


📄 Исходный файл: `testing/car_did_repro_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestReproduceRepo](#testreproducerepo) `:191`


</details>



---


[test] name: TestReproduceRepo file: testing/car_did_repro_test.go:191


#### TestReproduceRepo


📍 *Расположение: `testing/car_did_repro_test.go:191`*


### testing/feedpost_test.go


📄 Исходный файл: `testing/feedpost_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestFeedPostParse](#testfeedpostparse) `:21`

- 🔗 [TestFeedPostRichtextLink](#testfeedpostrichtextlink) `:151`

- 🔗 [TestPostToJson](#testposttojson) `:129`


</details>



---


[test] name: TestFeedPostParse file: testing/feedpost_test.go:21


#### TestFeedPostParse


📍 *Расположение: `testing/feedpost_test.go:21`*



---


[test] name: TestFeedPostRichtextLink file: testing/feedpost_test.go:151 description: checks a corner-case with $type: "app.bsky.richtext.facet#link"


#### TestFeedPostRichtextLink


checks a corner-case with $type: "app.bsky.richtext.facet#link"


📍 *Расположение: `testing/feedpost_test.go:151`*



---


[test] name: TestPostToJson file: testing/feedpost_test.go:129


#### TestPostToJson


📍 *Расположение: `testing/feedpost_test.go:129`*


### testing/repo_slice_test.go


📄 Исходный файл: `testing/repo_slice_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestRepoSliceParse](#testreposliceparse) `:18`


</details>



---


[test] name: TestRepoSliceParse file: testing/repo_slice_test.go:18 description: ipfs dag import testing/repo_slice.car
ipfs dag get bafyreiapesxwibnujg44xphqq23


#### TestRepoSliceParse


ipfs dag import testing/repo_slice.car
ipfs dag get bafyreiapesxwibnujg44xphqq23ekkozgcmnenj2onnx4gkgy4uipziyc4 | jq .
ipfs dag get bafyreiapesxwibnujg44xphqq23ekkozgcmnenj2onnx4gkgy4uipziyc4 --output-codec=dag-cbor > testing/repo_record.cbor


📍 *Расположение: `testing/repo_slice_test.go:18`*


### testing/sig_test.go


📄 Исходный файл: `testing/sig_test.go`


<details open>
<summary><b>Тесты в этом файле (3)</b></summary>


- 🔗 [TestInteropSignatures](#testinteropsignatures) `:125`

- 🔗 [TestVerification](#testverification) `:21`

- 🔗 [TestVerificationK256](#testverificationk256) `:72`


</details>



---


[test] name: TestInteropSignatures file: testing/sig_test.go:125


#### TestInteropSignatures


📍 *Расположение: `testing/sig_test.go:125`*



---


[test] name: TestVerification file: testing/sig_test.go:21


#### TestVerification


📍 *Расположение: `testing/sig_test.go:21`*



---


[test] name: TestVerificationK256 file: testing/sig_test.go:72


#### TestVerificationK256


📍 *Расположение: `testing/sig_test.go:72`*


### util/cliutil/key_test.go


📄 Исходный файл: `util/cliutil/key_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestKeyGenerationAndLoading](#testkeygenerationandloading) `:9`


</details>



---


[test] name: TestKeyGenerationAndLoading file: util/cliutil/key_test.go:9


#### TestKeyGenerationAndLoading


📍 *Расположение: `util/cliutil/key_test.go:9`*


### util/ssrf/ssrf_test.go


📄 Исходный файл: `util/ssrf/ssrf_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestPublicOnlyTransport](#testpubliconlytransport) `:10`


</details>



---


[test] name: TestPublicOnlyTransport file: util/ssrf/ssrf_test.go:10


#### TestPublicOnlyTransport


📍 *Расположение: `util/ssrf/ssrf_test.go:10`*


### xrpc/xrpc_test.go


📄 Исходный файл: `xrpc/xrpc_test.go`


<details open>
<summary><b>Тесты в этом файле (1)</b></summary>


- 🔗 [TestMakeParams](#testmakeparams) `:8`


</details>



---


[test] name: TestMakeParams file: xrpc/xrpc_test.go:8 description: TestMakeParams tests the makeParams function.


#### TestMakeParams


TestMakeParams tests the makeParams function.


📍 *Расположение: `xrpc/xrpc_test.go:8`*


## Бенчмарки


### carstore/repo_test.go


📄 Исходный файл: `carstore/repo_test.go`


<details open>
<summary><b>Бенчмарки в этом файле (3)</b></summary>


- 🔗 [BenchmarkRepoWritesCarstore](#benchmarkrepowritescarstore) `:346`

- 🔗 [BenchmarkRepoWritesFlatfs](#benchmarkrepowritesflatfs) `:416`

- 🔗 [BenchmarkRepoWritesSqliteCarstore](#benchmarkrepowritessqlitecarstore) `:352`


</details>



---


[benchmark] name: BenchmarkRepoWritesCarstore file: carstore/repo_test.go:346


#### BenchmarkRepoWritesCarstore


📍 *Расположение: `carstore/repo_test.go:346`*



---


[benchmark] name: BenchmarkRepoWritesFlatfs file: carstore/repo_test.go:416


#### BenchmarkRepoWritesFlatfs


📍 *Расположение: `carstore/repo_test.go:416`*



---


[benchmark] name: BenchmarkRepoWritesSqliteCarstore file: carstore/repo_test.go:352


#### BenchmarkRepoWritesSqliteCarstore


📍 *Расположение: `carstore/repo_test.go:352`*


### events/dbpersist/dbpersist_test.go


📄 Исходный файл: `events/dbpersist/dbpersist_test.go`


<details open>
<summary><b>Бенчмарки в этом файле (2)</b></summary>


- 🔗 [BenchmarkDBPersist](#benchmarkdbpersist) `:24`

- 🔗 [BenchmarkPlayback](#benchmarkplayback) `:144`


</details>



---


[benchmark] name: BenchmarkDBPersist file: events/dbpersist/dbpersist_test.go:24


#### BenchmarkDBPersist


📍 *Расположение: `events/dbpersist/dbpersist_test.go:24`*



---


[benchmark] name: BenchmarkPlayback file: events/dbpersist/dbpersist_test.go:144


#### BenchmarkPlayback


📍 *Расположение: `events/dbpersist/dbpersist_test.go:144`*


### events/diskpersist/diskpersist_test.go


📄 Исходный файл: `events/diskpersist/diskpersist_test.go`


<details open>
<summary><b>Бенчмарки в этом файле (1)</b></summary>


- 🔗 [BenchmarkDiskPersist](#benchmarkdiskpersist) `:174`


</details>



---


[benchmark] name: BenchmarkDiskPersist file: events/diskpersist/diskpersist_test.go:174


#### BenchmarkDiskPersist


📍 *Расположение: `events/diskpersist/diskpersist_test.go:174`*


### mst/mst_test.go


📄 Исходный файл: `mst/mst_test.go`


<details open>
<summary><b>Бенчмарки в этом файле (4)</b></summary>


- 🔗 [BenchmarkCountPrefixLen](#benchmarkcountprefixlen) `:627`

- 🔗 [BenchmarkDiffTrees](#benchmarkdifftrees) `:551`

- 🔗 [BenchmarkIsValidMstKey](#benchmarkisvalidmstkey) `:501`

- 🔗 [BenchmarkLeadingZerosOnHash](#benchmarkleadingzerosonhash) `:544`


</details>



---


[benchmark] name: BenchmarkCountPrefixLen file: mst/mst_test.go:627


#### BenchmarkCountPrefixLen


📍 *Расположение: `mst/mst_test.go:627`*



---


[benchmark] name: BenchmarkDiffTrees file: mst/mst_test.go:551


#### BenchmarkDiffTrees


📍 *Расположение: `mst/mst_test.go:551`*



---


[benchmark] name: BenchmarkIsValidMstKey file: mst/mst_test.go:501


#### BenchmarkIsValidMstKey


📍 *Расположение: `mst/mst_test.go:501`*



---


[benchmark] name: BenchmarkLeadingZerosOnHash file: mst/mst_test.go:544


#### BenchmarkLeadingZerosOnHash


📍 *Расположение: `mst/mst_test.go:544`*


### repomgr/bench_test.go


📄 Исходный файл: `repomgr/bench_test.go`


<details open>
<summary><b>Бенчмарки в этом файле (1)</b></summary>


- 🔗 [BenchmarkRepoMgrCreates](#benchmarkrepomgrcreates) `:44`


</details>



---


[benchmark] name: BenchmarkRepoMgrCreates file: repomgr/bench_test.go:44


#### BenchmarkRepoMgrCreates


📍 *Расположение: `repomgr/bench_test.go:44`*


## Примеры


### atproto/atclient/examples_test.go


📄 Исходный файл: `atproto/atclient/examples_test.go`


<details open>
<summary><b>Примеры в этом файле (1)</b></summary>


- 🔗 [ExampleGet](#exampleget) `:11`


</details>



---


[example] name: ExampleGet file: atproto/atclient/examples_test.go:11


#### ExampleGet


📍 *Расположение: `atproto/atclient/examples_test.go:11`*


### atproto/atcrypto/examples_test.go


📄 Исходный файл: `atproto/atcrypto/examples_test.go`


<details open>
<summary><b>Примеры в этом файле (2)</b></summary>


- 🔗 [ExamplePrivateKey](#exampleprivatekey) `:25`

- 🔗 [ExamplePublicKey](#examplepublickey) `:8`


</details>



---


[example] name: ExamplePrivateKey file: atproto/atcrypto/examples_test.go:25


#### ExamplePrivateKey


📍 *Расположение: `atproto/atcrypto/examples_test.go:25`*



---


[example] name: ExamplePublicKey file: atproto/atcrypto/examples_test.go:8


#### ExamplePublicKey


📍 *Расположение: `atproto/atcrypto/examples_test.go:8`*


### atproto/identity/apidir/examples_test.go


📄 Исходный файл: `atproto/identity/apidir/examples_test.go`


<details open>
<summary><b>Примеры в этом файле (1)</b></summary>


- 🔗 [ExampleAPIDirectory](#exampleapidirectory) `:10`


</details>



---


[example] name: ExampleAPIDirectory file: atproto/identity/apidir/examples_test.go:10


#### ExampleAPIDirectory


📍 *Расположение: `atproto/identity/apidir/examples_test.go:10`*


### atproto/lexicon/examples_test.go


📄 Исходный файл: `atproto/lexicon/examples_test.go`


<details open>
<summary><b>Примеры в этом файле (1)</b></summary>


- 🔗 [ExampleValidateRecord](#examplevalidaterecord) `:9`


</details>



---


[example] name: ExampleValidateRecord file: atproto/lexicon/examples_test.go:9


#### ExampleValidateRecord


📍 *Расположение: `atproto/lexicon/examples_test.go:9`*



---


## Навигация


- [К оглавлению документации](../README.md)

- [Диаграммы](../diagrams/)

- [Импорты](imports.md)

- [Структуры и типы](structures.md)

- [Функции](functions.md)

- [Спецификация API](api.md)

- [Тестирование](tests.md)

- [Используемые библиотеки](libraries.md)


---

