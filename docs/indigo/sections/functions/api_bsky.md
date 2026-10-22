---
title: "Функции: api/bsky"
type: functions
repo: indigo
language: ru
chunk_boundary: h3
group: api/bsky
---


# Функции: api/bsky


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_atproto.md)

- [Следующая директория](api_chat.md)


---


## Меню по файлам


- 📄 [api/bsky/actordefs.go](#apibskyactordefsgo)

- 📄 [api/bsky/actorgetPreferences.go](#apibskyactorgetpreferencesgo)

- 📄 [api/bsky/actorgetProfile.go](#apibskyactorgetprofilego)

- 📄 [api/bsky/actorgetProfiles.go](#apibskyactorgetprofilesgo)

- 📄 [api/bsky/actorgetSuggestions.go](#apibskyactorgetsuggestionsgo)

- 📄 [api/bsky/actorprofile.go](#apibskyactorprofilego)

- 📄 [api/bsky/actorputPreferences.go](#apibskyactorputpreferencesgo)

- 📄 [api/bsky/actorsearchActors.go](#apibskyactorsearchactorsgo)

- 📄 [api/bsky/actorsearchActorsTypeahead.go](#apibskyactorsearchactorstypeaheadgo)

- 📄 [api/bsky/actorstatus.go](#apibskyactorstatusgo)

- 📄 [api/bsky/ageassurancebegin.go](#apibskyageassurancebegingo)

- 📄 [api/bsky/ageassurancedefs.go](#apibskyageassurancedefsgo)

- 📄 [api/bsky/ageassurancegetConfig.go](#apibskyageassurancegetconfiggo)

- 📄 [api/bsky/ageassurancegetState.go](#apibskyageassurancegetstatego)

- 📄 [api/bsky/bookmarkcreateBookmark.go](#apibskybookmarkcreatebookmarkgo)

- 📄 [api/bsky/bookmarkdefs.go](#apibskybookmarkdefsgo)

- 📄 [api/bsky/bookmarkdeleteBookmark.go](#apibskybookmarkdeletebookmarkgo)

- 📄 [api/bsky/bookmarkgetBookmarks.go](#apibskybookmarkgetbookmarksgo)

- 📄 [api/bsky/cbor_gen.go](#apibskycbor_gengo)

- 📄 [api/bsky/contactdismissMatch.go](#apibskycontactdismissmatchgo)

- 📄 [api/bsky/contactgetMatches.go](#apibskycontactgetmatchesgo)

- 📄 [api/bsky/contactgetSyncStatus.go](#apibskycontactgetsyncstatusgo)

- 📄 [api/bsky/contactimportContacts.go](#apibskycontactimportcontactsgo)

- 📄 [api/bsky/contactremoveData.go](#apibskycontactremovedatago)

- 📄 [api/bsky/contactsendNotification.go](#apibskycontactsendnotificationgo)

- 📄 [api/bsky/contactstartPhoneVerification.go](#apibskycontactstartphoneverificationgo)

- 📄 [api/bsky/contactverifyPhone.go](#apibskycontactverifyphonego)

- 📄 [api/bsky/draftcreateDraft.go](#apibskydraftcreatedraftgo)

- 📄 [api/bsky/draftdefs.go](#apibskydraftdefsgo)

- 📄 [api/bsky/draftdeleteDraft.go](#apibskydraftdeletedraftgo)

- 📄 [api/bsky/draftgetDrafts.go](#apibskydraftgetdraftsgo)

- 📄 [api/bsky/draftupdateDraft.go](#apibskydraftupdatedraftgo)

- 📄 [api/bsky/embedexternal.go](#apibskyembedexternalgo)

- 📄 [api/bsky/embedimages.go](#apibskyembedimagesgo)

- 📄 [api/bsky/embedrecord.go](#apibskyembedrecordgo)

- 📄 [api/bsky/embedrecordWithMedia.go](#apibskyembedrecordwithmediago)

- 📄 [api/bsky/embedvideo.go](#apibskyembedvideogo)

- 📄 [api/bsky/feeddefs.go](#apibskyfeeddefsgo)

- 📄 [api/bsky/feeddescribeFeedGenerator.go](#apibskyfeeddescribefeedgeneratorgo)

- 📄 [api/bsky/feedgenerator.go](#apibskyfeedgeneratorgo)

- 📄 [api/bsky/feedgetActorFeeds.go](#apibskyfeedgetactorfeedsgo)

- 📄 [api/bsky/feedgetActorLikes.go](#apibskyfeedgetactorlikesgo)

- 📄 [api/bsky/feedgetAuthorFeed.go](#apibskyfeedgetauthorfeedgo)

- 📄 [api/bsky/feedgetFeed.go](#apibskyfeedgetfeedgo)

- 📄 [api/bsky/feedgetFeedGenerator.go](#apibskyfeedgetfeedgeneratorgo)

- 📄 [api/bsky/feedgetFeedGenerators.go](#apibskyfeedgetfeedgeneratorsgo)

- 📄 [api/bsky/feedgetFeedSkeleton.go](#apibskyfeedgetfeedskeletongo)

- 📄 [api/bsky/feedgetLikes.go](#apibskyfeedgetlikesgo)

- 📄 [api/bsky/feedgetListFeed.go](#apibskyfeedgetlistfeedgo)

- 📄 [api/bsky/feedgetPostThread.go](#apibskyfeedgetpostthreadgo)

- 📄 [api/bsky/feedgetPosts.go](#apibskyfeedgetpostsgo)

- 📄 [api/bsky/feedgetQuotes.go](#apibskyfeedgetquotesgo)

- 📄 [api/bsky/feedgetRepostedBy.go](#apibskyfeedgetrepostedbygo)

- 📄 [api/bsky/feedgetSuggestedFeeds.go](#apibskyfeedgetsuggestedfeedsgo)

- 📄 [api/bsky/feedgetTimeline.go](#apibskyfeedgettimelinego)

- 📄 [api/bsky/feedlike.go](#apibskyfeedlikego)

- 📄 [api/bsky/feedpost.go](#apibskyfeedpostgo)

- 📄 [api/bsky/feedpostgate.go](#apibskyfeedpostgatego)

- 📄 [api/bsky/feedrepost.go](#apibskyfeedrepostgo)

- 📄 [api/bsky/feedsearchPosts.go](#apibskyfeedsearchpostsgo)

- 📄 [api/bsky/feedsendInteractions.go](#apibskyfeedsendinteractionsgo)

- 📄 [api/bsky/feedthreadgate.go](#apibskyfeedthreadgatego)

- 📄 [api/bsky/graphblock.go](#apibskygraphblockgo)

- 📄 [api/bsky/graphfollow.go](#apibskygraphfollowgo)

- 📄 [api/bsky/graphgetActorStarterPacks.go](#apibskygraphgetactorstarterpacksgo)

- 📄 [api/bsky/graphgetBlocks.go](#apibskygraphgetblocksgo)

- 📄 [api/bsky/graphgetFollowers.go](#apibskygraphgetfollowersgo)

- 📄 [api/bsky/graphgetFollows.go](#apibskygraphgetfollowsgo)

- 📄 [api/bsky/graphgetKnownFollowers.go](#apibskygraphgetknownfollowersgo)

- 📄 [api/bsky/graphgetList.go](#apibskygraphgetlistgo)

- 📄 [api/bsky/graphgetListBlocks.go](#apibskygraphgetlistblocksgo)

- 📄 [api/bsky/graphgetListMutes.go](#apibskygraphgetlistmutesgo)

- 📄 [api/bsky/graphgetLists.go](#apibskygraphgetlistsgo)

- 📄 [api/bsky/graphgetListsWithMembership.go](#apibskygraphgetlistswithmembershipgo)

- 📄 [api/bsky/graphgetMutes.go](#apibskygraphgetmutesgo)

- 📄 [api/bsky/graphgetRelationships.go](#apibskygraphgetrelationshipsgo)

- 📄 [api/bsky/graphgetStarterPack.go](#apibskygraphgetstarterpackgo)

- 📄 [api/bsky/graphgetStarterPacks.go](#apibskygraphgetstarterpacksgo)

- 📄 [api/bsky/graphgetStarterPacksWithMembership.go](#apibskygraphgetstarterpackswithmembershipgo)

- 📄 [api/bsky/graphgetSuggestedFollowsByActor.go](#apibskygraphgetsuggestedfollowsbyactorgo)

- 📄 [api/bsky/graphlist.go](#apibskygraphlistgo)

- 📄 [api/bsky/graphlistblock.go](#apibskygraphlistblockgo)

- 📄 [api/bsky/graphlistitem.go](#apibskygraphlistitemgo)

- 📄 [api/bsky/graphmuteActor.go](#apibskygraphmuteactorgo)

- 📄 [api/bsky/graphmuteActorList.go](#apibskygraphmuteactorlistgo)

- 📄 [api/bsky/graphmuteThread.go](#apibskygraphmutethreadgo)

- 📄 [api/bsky/graphsearchStarterPacks.go](#apibskygraphsearchstarterpacksgo)

- 📄 [api/bsky/graphstarterpack.go](#apibskygraphstarterpackgo)

- 📄 [api/bsky/graphunmuteActor.go](#apibskygraphunmuteactorgo)

- 📄 [api/bsky/graphunmuteActorList.go](#apibskygraphunmuteactorlistgo)

- 📄 [api/bsky/graphunmuteThread.go](#apibskygraphunmutethreadgo)

- 📄 [api/bsky/graphverification.go](#apibskygraphverificationgo)

- 📄 [api/bsky/labelergetServices.go](#apibskylabelergetservicesgo)

- 📄 [api/bsky/labelerservice.go](#apibskylabelerservicego)

- 📄 [api/bsky/notificationdeclaration.go](#apibskynotificationdeclarationgo)

- 📄 [api/bsky/notificationgetPreferences.go](#apibskynotificationgetpreferencesgo)

- 📄 [api/bsky/notificationgetUnreadCount.go](#apibskynotificationgetunreadcountgo)

- 📄 [api/bsky/notificationlistActivitySubscriptions.go](#apibskynotificationlistactivitysubscriptionsgo)

- 📄 [api/bsky/notificationlistNotifications.go](#apibskynotificationlistnotificationsgo)

- 📄 [api/bsky/notificationputActivitySubscription.go](#apibskynotificationputactivitysubscriptiongo)

- 📄 [api/bsky/notificationputPreferences.go](#apibskynotificationputpreferencesgo)

- 📄 [api/bsky/notificationputPreferencesV2.go](#apibskynotificationputpreferencesv2go)

- 📄 [api/bsky/notificationregisterPush.go](#apibskynotificationregisterpushgo)

- 📄 [api/bsky/notificationunregisterPush.go](#apibskynotificationunregisterpushgo)

- 📄 [api/bsky/notificationupdateSeen.go](#apibskynotificationupdateseengo)

- 📄 [api/bsky/richtextfacet.go](#apibskyrichtextfacetgo)

- 📄 [api/bsky/unspeccedgetAgeAssuranceState.go](#apibskyunspeccedgetageassurancestatego)

- 📄 [api/bsky/unspeccedgetConfig.go](#apibskyunspeccedgetconfiggo)

- 📄 [api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go](#apibskyunspeccedgetonboardingsuggestedstarterpacksgo)

- 📄 [api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go](#apibskyunspeccedgetonboardingsuggestedstarterpacksskeletongo)

- 📄 [api/bsky/unspeccedgetPopularFeedGenerators.go](#apibskyunspeccedgetpopularfeedgeneratorsgo)

- 📄 [api/bsky/unspeccedgetPostThreadOtherV2.go](#apibskyunspeccedgetpostthreadotherv2go)

- 📄 [api/bsky/unspeccedgetPostThreadV2.go](#apibskyunspeccedgetpostthreadv2go)

- 📄 [api/bsky/unspeccedgetSuggestedFeeds.go](#apibskyunspeccedgetsuggestedfeedsgo)

- 📄 [api/bsky/unspeccedgetSuggestedFeedsSkeleton.go](#apibskyunspeccedgetsuggestedfeedsskeletongo)

- 📄 [api/bsky/unspeccedgetSuggestedStarterPacks.go](#apibskyunspeccedgetsuggestedstarterpacksgo)

- 📄 [api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go](#apibskyunspeccedgetsuggestedstarterpacksskeletongo)

- 📄 [api/bsky/unspeccedgetSuggestedUsers.go](#apibskyunspeccedgetsuggestedusersgo)

- 📄 [api/bsky/unspeccedgetSuggestedUsersSkeleton.go](#apibskyunspeccedgetsuggestedusersskeletongo)

- 📄 [api/bsky/unspeccedgetSuggestionsSkeleton.go](#apibskyunspeccedgetsuggestionsskeletongo)

- 📄 [api/bsky/unspeccedgetTaggedSuggestions.go](#apibskyunspeccedgettaggedsuggestionsgo)

- 📄 [api/bsky/unspeccedgetTrendingTopics.go](#apibskyunspeccedgettrendingtopicsgo)

- 📄 [api/bsky/unspeccedgetTrends.go](#apibskyunspeccedgettrendsgo)

- 📄 [api/bsky/unspeccedgetTrendsSkeleton.go](#apibskyunspeccedgettrendsskeletongo)

- 📄 [api/bsky/unspeccedinitAgeAssurance.go](#apibskyunspeccedinitageassurancego)

- 📄 [api/bsky/unspeccedsearchActorsSkeleton.go](#apibskyunspeccedsearchactorsskeletongo)

- 📄 [api/bsky/unspeccedsearchPostsSkeleton.go](#apibskyunspeccedsearchpostsskeletongo)

- 📄 [api/bsky/unspeccedsearchStarterPacksSkeleton.go](#apibskyunspeccedsearchstarterpacksskeletongo)

- 📄 [api/bsky/videogetJobStatus.go](#apibskyvideogetjobstatusgo)

- 📄 [api/bsky/videogetUploadLimits.go](#apibskyvideogetuploadlimitsgo)

- 📄 [api/bsky/videouploadVideo.go](#apibskyvideouploadvideogo)


---


## api/bsky/actordefs.go


📄 Исходный файл: `api/bsky/actordefs.go`


<details open>
<summary><b>Функции в этом файле (8)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apibskyactordefsgo155) `:155`

- 🔗 [MarshalJSON](#marshaljson-apibskyactordefsgo185) `:185`

- 🔗 [MarshalJSON](#marshaljson-apibskyactordefsgo246) `:246`

- 🔗 [MarshalJSON](#marshaljson-apibskyactordefsgo482) `:482`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyactordefsgo163) `:163`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyactordefsgo205) `:205`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyactordefsgo306) `:306`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyactordefsgo490) `:490`


</details>


[function] name: MarshalJSON file: api/bsky/actordefs.go:155 returns_error: да description: —


### MarshalJSON (api/bsky/actordefs.go:155)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorDefs_PostInteractionSettingsPref_PostgateEmbeddingRules_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actordefs.go:155`



---


[function] name: MarshalJSON file: api/bsky/actordefs.go:185 returns_error: да description: —


### MarshalJSON (api/bsky/actordefs.go:185)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorDefs_PostInteractionSettingsPref_ThreadgateAllowRules_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actordefs.go:185`



---


[function] name: MarshalJSON file: api/bsky/actordefs.go:246 returns_error: да description: —


### MarshalJSON (api/bsky/actordefs.go:246)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorDefs_Preferences_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actordefs.go:246`



---


[function] name: MarshalJSON file: api/bsky/actordefs.go:482 returns_error: да description: —


### MarshalJSON (api/bsky/actordefs.go:482)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorDefs_StatusView_Embed) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actordefs.go:482`



---


[function] name: UnmarshalJSON file: api/bsky/actordefs.go:163 returns_error: нет description: —


### UnmarshalJSON (api/bsky/actordefs.go:163)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ActorDefs_PostInteractionSettingsPref_PostgateEmbeddingRules_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/actordefs.go:163`



---


[function] name: UnmarshalJSON file: api/bsky/actordefs.go:205 returns_error: нет description: —


### UnmarshalJSON (api/bsky/actordefs.go:205)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ActorDefs_PostInteractionSettingsPref_ThreadgateAllowRules_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/actordefs.go:205`



---


[function] name: UnmarshalJSON file: api/bsky/actordefs.go:306 returns_error: нет description: —


### UnmarshalJSON (api/bsky/actordefs.go:306)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ActorDefs_Preferences_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/actordefs.go:306`



---


[function] name: UnmarshalJSON file: api/bsky/actordefs.go:490 returns_error: нет description: —


### UnmarshalJSON (api/bsky/actordefs.go:490)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ActorDefs_StatusView_Embed) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/actordefs.go:490`




## api/bsky/actorgetPreferences.go


📄 Исходный файл: `api/bsky/actorgetPreferences.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorGetPreferences](#actorgetpreferences-apibskyactorgetpreferencesgo19) `:19`


</details>


[function] name: ActorGetPreferences file: api/bsky/actorgetPreferences.go:19 returns_error: да description: ActorGetPreferences calls the XRPC method "app.bsky.actor.getPreferences".


### ActorGetPreferences (api/bsky/actorgetPreferences.go:19)


ActorGetPreferences calls the XRPC method "app.bsky.actor.getPreferences".


```go
func ActorGetPreferences((*ActorGetPreferences_Output, error)) (*ActorGetPreferences_Output, error)
```


**Тип запроса:** ActorGetPreferences_Output


```json
{
  "preferences": []
}
```


*Определено в:* `api/bsky/actorgetPreferences.go`


**Тип ответа:** ActorGetPreferences_Output


```json
{
  "preferences": []
}
```


*Определено в:* `api/bsky/actorgetPreferences.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ActorGetPreferences_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actorgetPreferences.go:19`




## api/bsky/actorgetProfile.go


📄 Исходный файл: `api/bsky/actorgetProfile.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorGetProfile](#actorgetprofile-apibskyactorgetprofilego16) `:16`


</details>


[function] name: ActorGetProfile file: api/bsky/actorgetProfile.go:16 returns_error: да description: ActorGetProfile calls the XRPC method "app.bsky.actor.getProfile".

actor: Handle or DID of account to fetch profile of.


### ActorGetProfile (api/bsky/actorgetProfile.go:16)


ActorGetProfile calls the XRPC method "app.bsky.actor.getProfile".

actor: Handle or DID of account to fetch profile of.


```go
func ActorGetProfile((*ActorDefs_ProfileViewDetailed, error)) (*ActorDefs_ProfileViewDetailed, error)
```


**Тип запроса:** ActorDefs_ProfileViewDetailed


```json
{
  "associated": null,
  "avatar": "string",
  "banner": "string",
  "createdAt": "string",
  "debug": null,
  "description": "string",
  "did": "string",
  "displayName": "string",
  "followersCount": 0,
  "followsCount": 0,
  "handle": "string",
  "indexedAt": "string",
  "joinedViaStarterPack": null,
  "labels": [],
  "pinnedPost": null,
  "postsCount": 0,
  "pronouns": "string",
  "status": null,
  "verification": null,
  "viewer": null,
  "website": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Тип ответа:** ActorDefs_ProfileViewDetailed


```json
{
  "associated": null,
  "avatar": "string",
  "banner": "string",
  "createdAt": "string",
  "debug": null,
  "description": "string",
  "did": "string",
  "displayName": "string",
  "followersCount": 0,
  "followsCount": 0,
  "handle": "string",
  "indexedAt": "string",
  "joinedViaStarterPack": null,
  "labels": [],
  "pinnedPost": null,
  "postsCount": 0,
  "pronouns": "string",
  "status": null,
  "verification": null,
  "viewer": null,
  "website": "string"
}
```


*Определено в:* `api/bsky/actordefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ActorDefs_ProfileViewDetailed`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actorgetProfile.go:16`




## api/bsky/actorgetProfiles.go


📄 Исходный файл: `api/bsky/actorgetProfiles.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorGetProfiles](#actorgetprofiles-apibskyactorgetprofilesgo19) `:19`


</details>


[function] name: ActorGetProfiles file: api/bsky/actorgetProfiles.go:19 returns_error: да description: ActorGetProfiles calls the XRPC method "app.bsky.actor.getProfiles".


### ActorGetProfiles (api/bsky/actorgetProfiles.go:19)


ActorGetProfiles calls the XRPC method "app.bsky.actor.getProfiles".


```go
func ActorGetProfiles((*ActorGetProfiles_Output, error)) (*ActorGetProfiles_Output, error)
```


**Тип запроса:** ActorGetProfiles_Output


```json
{
  "profiles": []
}
```


*Определено в:* `api/bsky/actorgetProfiles.go`


**Тип ответа:** ActorGetProfiles_Output


```json
{
  "profiles": []
}
```


*Определено в:* `api/bsky/actorgetProfiles.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ActorGetProfiles_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actorgetProfiles.go:19`




## api/bsky/actorgetSuggestions.go


📄 Исходный файл: `api/bsky/actorgetSuggestions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorGetSuggestions](#actorgetsuggestions-apibskyactorgetsuggestionsgo24) `:24`


</details>


[function] name: ActorGetSuggestions file: api/bsky/actorgetSuggestions.go:24 returns_error: да description: ActorGetSuggestions calls the XRPC method "app.bsky.actor.getSuggestions".


### ActorGetSuggestions (api/bsky/actorgetSuggestions.go:24)


ActorGetSuggestions calls the XRPC method "app.bsky.actor.getSuggestions".


```go
func ActorGetSuggestions((*ActorGetSuggestions_Output, error)) (*ActorGetSuggestions_Output, error)
```


**Тип запроса:** ActorGetSuggestions_Output


```json
{
  "actors": [],
  "cursor": "string",
  "recId": 0,
  "recIdStr": "string"
}
```


*Определено в:* `api/bsky/actorgetSuggestions.go`


**Тип ответа:** ActorGetSuggestions_Output


```json
{
  "actors": [],
  "cursor": "string",
  "recId": 0,
  "recIdStr": "string"
}
```


*Определено в:* `api/bsky/actorgetSuggestions.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ActorGetSuggestions_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actorgetSuggestions.go:24`




## api/bsky/actorprofile.go


📄 Исходный файл: `api/bsky/actorprofile.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskyactorprofilego69) `:69`

- 🔗 [MarshalJSON](#marshaljson-apibskyactorprofilego46) `:46`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyactorprofilego81) `:81`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyactorprofilego54) `:54`

- 🔗 [init](#init-apibskyactorprofilego18) `:18`


</details>


[function] name: MarshalCBOR file: api/bsky/actorprofile.go:69 returns_error: нет description: —


### MarshalCBOR (api/bsky/actorprofile.go:69)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *ActorProfile_Labels) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/actorprofile.go:69`



---


[function] name: MarshalJSON file: api/bsky/actorprofile.go:46 returns_error: да description: —


### MarshalJSON (api/bsky/actorprofile.go:46)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorProfile_Labels) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actorprofile.go:46`



---


[function] name: UnmarshalCBOR file: api/bsky/actorprofile.go:81 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/actorprofile.go:81)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *ActorProfile_Labels) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/actorprofile.go:81`



---


[function] name: UnmarshalJSON file: api/bsky/actorprofile.go:54 returns_error: нет description: —


### UnmarshalJSON (api/bsky/actorprofile.go:54)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ActorProfile_Labels) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/actorprofile.go:54`



---


[function] name: init file: api/bsky/actorprofile.go:18 returns_error: нет description: —


### init (api/bsky/actorprofile.go:18)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/actorprofile.go:18`




## api/bsky/actorputPreferences.go


📄 Исходный файл: `api/bsky/actorputPreferences.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorPutPreferences](#actorputpreferences-apibskyactorputpreferencesgo19) `:19`


</details>


[function] name: ActorPutPreferences file: api/bsky/actorputPreferences.go:19 returns_error: нет description: ActorPutPreferences calls the XRPC method "app.bsky.actor.putPreferences".


### ActorPutPreferences (api/bsky/actorputPreferences.go:19)


ActorPutPreferences calls the XRPC method "app.bsky.actor.putPreferences".


```go
func ActorPutPreferences((ctx context.Context, c lexutil.LexClient, input *ActorPutPreferences_Input)) (ctx context.Context, c lexutil.LexClient, input *ActorPutPreferences_Input)
```


**Тип запроса:** ActorPutPreferences_Input


```json
{
  "preferences": []
}
```


*Определено в:* `api/bsky/actorputPreferences.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ActorPutPreferences_Input


```json
{
  "preferences": []
}
```


*Определено в:* `api/bsky/actorputPreferences.go`


📍 *Расположение:* `api/bsky/actorputPreferences.go:19`




## api/bsky/actorsearchActors.go


📄 Исходный файл: `api/bsky/actorsearchActors.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorSearchActors](#actorsearchactors-apibskyactorsearchactorsgo23) `:23`


</details>


[function] name: ActorSearchActors file: api/bsky/actorsearchActors.go:23 returns_error: да description: ActorSearchActors calls the XRPC method "app.bsky.actor.searchActors".

q: Search query string. Syntax, phrase, boolean,


### ActorSearchActors (api/bsky/actorsearchActors.go:23)


ActorSearchActors calls the XRPC method "app.bsky.actor.searchActors".

q: Search query string. Syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.
term: DEPRECATED: use 'q' instead.


```go
func ActorSearchActors((*ActorSearchActors_Output, error)) (*ActorSearchActors_Output, error)
```


**Тип запроса:** ActorSearchActors_Output


```json
{
  "actors": [],
  "cursor": "string"
}
```


*Определено в:* `api/bsky/actorsearchActors.go`


**Тип ответа:** ActorSearchActors_Output


```json
{
  "actors": [],
  "cursor": "string"
}
```


*Определено в:* `api/bsky/actorsearchActors.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ActorSearchActors_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actorsearchActors.go:23`




## api/bsky/actorsearchActorsTypeahead.go


📄 Исходный файл: `api/bsky/actorsearchActorsTypeahead.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ActorSearchActorsTypeahead](#actorsearchactorstypeahead-apibskyactorsearchactorstypeaheadgo22) `:22`


</details>


[function] name: ActorSearchActorsTypeahead file: api/bsky/actorsearchActorsTypeahead.go:22 returns_error: да description: ActorSearchActorsTypeahead calls the XRPC method "app.bsky.actor.searchActorsTypeahead".

q: Search query prefix; not a 


### ActorSearchActorsTypeahead (api/bsky/actorsearchActorsTypeahead.go:22)


ActorSearchActorsTypeahead calls the XRPC method "app.bsky.actor.searchActorsTypeahead".

q: Search query prefix; not a full query string.
term: DEPRECATED: use 'q' instead.


```go
func ActorSearchActorsTypeahead((*ActorSearchActorsTypeahead_Output, error)) (*ActorSearchActorsTypeahead_Output, error)
```


**Тип запроса:** ActorSearchActorsTypeahead_Output


```json
{
  "actors": []
}
```


*Определено в:* `api/bsky/actorsearchActorsTypeahead.go`


**Тип ответа:** ActorSearchActorsTypeahead_Output


```json
{
  "actors": []
}
```


*Определено в:* `api/bsky/actorsearchActorsTypeahead.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ActorSearchActorsTypeahead_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actorsearchActorsTypeahead.go:22`




## api/bsky/actorstatus.go


📄 Исходный файл: `api/bsky/actorstatus.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskyactorstatusgo60) `:60`

- 🔗 [MarshalJSON](#marshaljson-apibskyactorstatusgo37) `:37`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyactorstatusgo72) `:72`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyactorstatusgo45) `:45`

- 🔗 [init](#init-apibskyactorstatusgo17) `:17`


</details>


[function] name: MarshalCBOR file: api/bsky/actorstatus.go:60 returns_error: нет description: —


### MarshalCBOR (api/bsky/actorstatus.go:60)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *ActorStatus_Embed) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/actorstatus.go:60`



---


[function] name: MarshalJSON file: api/bsky/actorstatus.go:37 returns_error: да description: —


### MarshalJSON (api/bsky/actorstatus.go:37)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorStatus_Embed) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/actorstatus.go:37`



---


[function] name: UnmarshalCBOR file: api/bsky/actorstatus.go:72 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/actorstatus.go:72)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *ActorStatus_Embed) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/actorstatus.go:72`



---


[function] name: UnmarshalJSON file: api/bsky/actorstatus.go:45 returns_error: нет description: —


### UnmarshalJSON (api/bsky/actorstatus.go:45)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *ActorStatus_Embed) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/actorstatus.go:45`



---


[function] name: init file: api/bsky/actorstatus.go:17 returns_error: нет description: —


### init (api/bsky/actorstatus.go:17)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/actorstatus.go:17`




## api/bsky/ageassurancebegin.go


📄 Исходный файл: `api/bsky/ageassurancebegin.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AgeassuranceBegin](#ageassurancebegin-apibskyageassurancebegingo26) `:26`


</details>


[function] name: AgeassuranceBegin file: api/bsky/ageassurancebegin.go:26 returns_error: да description: AgeassuranceBegin calls the XRPC method "app.bsky.ageassurance.begin".


### AgeassuranceBegin (api/bsky/ageassurancebegin.go:26)


AgeassuranceBegin calls the XRPC method "app.bsky.ageassurance.begin".


```go
func AgeassuranceBegin((*AgeassuranceDefs_State, error)) (*AgeassuranceDefs_State, error)
```


**Тип запроса:** AgeassuranceDefs_State


```json
{
  "access": "string",
  "lastInitiatedAt": "string",
  "status": "string"
}
```


*Определено в:* `api/bsky/ageassurancedefs.go`


**Тип ответа:** AgeassuranceDefs_State


```json
{
  "access": "string",
  "lastInitiatedAt": "string",
  "status": "string"
}
```


*Определено в:* `api/bsky/ageassurancedefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AgeassuranceDefs_State`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/ageassurancebegin.go:26`




## api/bsky/ageassurancedefs.go


📄 Исходный файл: `api/bsky/ageassurancedefs.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apibskyageassurancedefsgo110) `:110`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyageassurancedefsgo142) `:142`


</details>


[function] name: MarshalJSON file: api/bsky/ageassurancedefs.go:110 returns_error: да description: —


### MarshalJSON (api/bsky/ageassurancedefs.go:110)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *AgeassuranceDefs_ConfigRegion_Rules_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/ageassurancedefs.go:110`



---


[function] name: UnmarshalJSON file: api/bsky/ageassurancedefs.go:142 returns_error: нет description: —


### UnmarshalJSON (api/bsky/ageassurancedefs.go:142)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *AgeassuranceDefs_ConfigRegion_Rules_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/ageassurancedefs.go:142`




## api/bsky/ageassurancegetConfig.go


📄 Исходный файл: `api/bsky/ageassurancegetConfig.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AgeassuranceGetConfig](#ageassurancegetconfig-apibskyageassurancegetconfiggo14) `:14`


</details>


[function] name: AgeassuranceGetConfig file: api/bsky/ageassurancegetConfig.go:14 returns_error: да description: AgeassuranceGetConfig calls the XRPC method "app.bsky.ageassurance.getConfig".


### AgeassuranceGetConfig (api/bsky/ageassurancegetConfig.go:14)


AgeassuranceGetConfig calls the XRPC method "app.bsky.ageassurance.getConfig".


```go
func AgeassuranceGetConfig((*AgeassuranceDefs_Config, error)) (*AgeassuranceDefs_Config, error)
```


**Тип запроса:** AgeassuranceDefs_Config


```json
{
  "regions": []
}
```


*Определено в:* `api/bsky/ageassurancedefs.go`


**Тип ответа:** AgeassuranceDefs_Config


```json
{
  "regions": []
}
```


*Определено в:* `api/bsky/ageassurancedefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AgeassuranceDefs_Config`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/ageassurancegetConfig.go:14`




## api/bsky/ageassurancegetState.go


📄 Исходный файл: `api/bsky/ageassurancegetState.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [AgeassuranceGetState](#ageassurancegetstate-apibskyageassurancegetstatego20) `:20`


</details>


[function] name: AgeassuranceGetState file: api/bsky/ageassurancegetState.go:20 returns_error: да description: AgeassuranceGetState calls the XRPC method "app.bsky.ageassurance.getState".


### AgeassuranceGetState (api/bsky/ageassurancegetState.go:20)


AgeassuranceGetState calls the XRPC method "app.bsky.ageassurance.getState".


```go
func AgeassuranceGetState((*AgeassuranceGetState_Output, error)) (*AgeassuranceGetState_Output, error)
```


**Тип запроса:** AgeassuranceGetState_Output


```json
{
  "metadata": null,
  "state": null
}
```


*Определено в:* `api/bsky/ageassurancegetState.go`


**Тип ответа:** AgeassuranceGetState_Output


```json
{
  "metadata": null,
  "state": null
}
```


*Определено в:* `api/bsky/ageassurancegetState.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*AgeassuranceGetState_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/ageassurancegetState.go:20`




## api/bsky/bookmarkcreateBookmark.go


📄 Исходный файл: `api/bsky/bookmarkcreateBookmark.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [BookmarkCreateBookmark](#bookmarkcreatebookmark-apibskybookmarkcreatebookmarkgo20) `:20`


</details>


[function] name: BookmarkCreateBookmark file: api/bsky/bookmarkcreateBookmark.go:20 returns_error: нет description: BookmarkCreateBookmark calls the XRPC method "app.bsky.bookmark.createBookmark".


### BookmarkCreateBookmark (api/bsky/bookmarkcreateBookmark.go:20)


BookmarkCreateBookmark calls the XRPC method "app.bsky.bookmark.createBookmark".


```go
func BookmarkCreateBookmark((ctx context.Context, c lexutil.LexClient, input *BookmarkCreateBookmark_Input)) (ctx context.Context, c lexutil.LexClient, input *BookmarkCreateBookmark_Input)
```


**Тип запроса:** BookmarkCreateBookmark_Input


```json
{
  "cid": "string",
  "uri": "string"
}
```


*Определено в:* `api/bsky/bookmarkcreateBookmark.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BookmarkCreateBookmark_Input


```json
{
  "cid": "string",
  "uri": "string"
}
```


*Определено в:* `api/bsky/bookmarkcreateBookmark.go`


📍 *Расположение:* `api/bsky/bookmarkcreateBookmark.go:20`




## api/bsky/bookmarkdefs.go


📄 Исходный файл: `api/bsky/bookmarkdefs.go`


<details open>
<summary><b>Функции в этом файле (2)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apibskybookmarkdefsgo37) `:37`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskybookmarkdefsgo53) `:53`


</details>


[function] name: MarshalJSON file: api/bsky/bookmarkdefs.go:37 returns_error: да description: —


### MarshalJSON (api/bsky/bookmarkdefs.go:37)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *BookmarkDefs_BookmarkView_Item) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/bookmarkdefs.go:37`



---


[function] name: UnmarshalJSON file: api/bsky/bookmarkdefs.go:53 returns_error: нет description: —


### UnmarshalJSON (api/bsky/bookmarkdefs.go:53)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *BookmarkDefs_BookmarkView_Item) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/bookmarkdefs.go:53`




## api/bsky/bookmarkdeleteBookmark.go


📄 Исходный файл: `api/bsky/bookmarkdeleteBookmark.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [BookmarkDeleteBookmark](#bookmarkdeletebookmark-apibskybookmarkdeletebookmarkgo19) `:19`


</details>


[function] name: BookmarkDeleteBookmark file: api/bsky/bookmarkdeleteBookmark.go:19 returns_error: нет description: BookmarkDeleteBookmark calls the XRPC method "app.bsky.bookmark.deleteBookmark".


### BookmarkDeleteBookmark (api/bsky/bookmarkdeleteBookmark.go:19)


BookmarkDeleteBookmark calls the XRPC method "app.bsky.bookmark.deleteBookmark".


```go
func BookmarkDeleteBookmark((ctx context.Context, c lexutil.LexClient, input *BookmarkDeleteBookmark_Input)) (ctx context.Context, c lexutil.LexClient, input *BookmarkDeleteBookmark_Input)
```


**Тип запроса:** BookmarkDeleteBookmark_Input


```json
{
  "uri": "string"
}
```


*Определено в:* `api/bsky/bookmarkdeleteBookmark.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** BookmarkDeleteBookmark_Input


```json
{
  "uri": "string"
}
```


*Определено в:* `api/bsky/bookmarkdeleteBookmark.go`


📍 *Расположение:* `api/bsky/bookmarkdeleteBookmark.go:19`




## api/bsky/bookmarkgetBookmarks.go


📄 Исходный файл: `api/bsky/bookmarkgetBookmarks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [BookmarkGetBookmarks](#bookmarkgetbookmarks-apibskybookmarkgetbookmarksgo20) `:20`


</details>


[function] name: BookmarkGetBookmarks file: api/bsky/bookmarkgetBookmarks.go:20 returns_error: да description: BookmarkGetBookmarks calls the XRPC method "app.bsky.bookmark.getBookmarks".


### BookmarkGetBookmarks (api/bsky/bookmarkgetBookmarks.go:20)


BookmarkGetBookmarks calls the XRPC method "app.bsky.bookmark.getBookmarks".


```go
func BookmarkGetBookmarks((*BookmarkGetBookmarks_Output, error)) (*BookmarkGetBookmarks_Output, error)
```


**Тип запроса:** BookmarkGetBookmarks_Output


```json
{
  "bookmarks": [],
  "cursor": "string"
}
```


*Определено в:* `api/bsky/bookmarkgetBookmarks.go`


**Тип ответа:** BookmarkGetBookmarks_Output


```json
{
  "bookmarks": [],
  "cursor": "string"
}
```


*Определено в:* `api/bsky/bookmarkgetBookmarks.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*BookmarkGetBookmarks_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/bookmarkgetBookmarks.go:20`




## api/bsky/cbor_gen.go


📄 Исходный файл: `api/bsky/cbor_gen.go`


<details open>
<summary><b>Функции в этом файле (84)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo23) `:23`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo641) `:641`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo851) `:851`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo1021) `:1021`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo1159) `:1159`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo1322) `:1322`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo1493) `:1493`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo1625) `:1625`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo1837) `:1837`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo2017) `:2017`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo2225) `:2225`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo2822) `:2822`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo2954) `:2954`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo3164) `:3164`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo3341) `:3341`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo3504) `:3504`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo3634) `:3634`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo3764) `:3764`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo3894) `:3894`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo4062) `:4062`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo4226) `:4226`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo4390) `:4390`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo4830) `:4830`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo5028) `:5028`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo5571) `:5571`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo5735) `:5735`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo5898) `:5898`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo6225) `:6225`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo6355) `:6355`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo6451) `:6451`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo6547) `:6547`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo6643) `:6643`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo6743) `:6743`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo7163) `:7163`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo7645) `:7645`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo7883) `:7883`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo8198) `:8198`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo8334) `:8334`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo8661) `:8661`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo8757) `:8757`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo8989) `:8989`

- 🔗 [MarshalCBOR](#marshalcbor-apibskycbor_gengo9269) `:9269`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo318) `:318`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo737) `:737`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo927) `:927`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo1067) `:1067`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo1218) `:1218`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo1381) `:1381`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo1542) `:1542`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo1732) `:1732`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo1914) `:1914`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo2120) `:2120`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo2554) `:2554`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo2871) `:2871`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo3050) `:3050`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo3220) `:3220`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo3400) `:3400`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo3560) `:3560`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo3690) `:3690`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo3820) `:3820`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo3959) `:3959`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo4134) `:4134`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo4305) `:4305`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo4614) `:4614`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo4932) `:4932`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo5311) `:5311`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo5650) `:5650`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo5794) `:5794`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo6051) `:6051`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo6281) `:6281`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo6388) `:6388`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo6484) `:6484`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo6580) `:6580`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo6680) `:6680`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo6948) `:6948`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo7391) `:7391`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo7732) `:7732`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo8025) `:8025`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo8251) `:8251`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo8487) `:8487`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo8694) `:8694`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo8882) `:8882`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo9128) `:9128`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskycbor_gengo9325) `:9325`


</details>


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:23 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:23)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPost) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:23`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:641 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:641)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedRepost) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:641`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:851 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:851)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPost_Entity) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:851`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:1021 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:1021)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPost_ReplyRef) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:1021`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:1159 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:1159)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPost_TextSlice) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:1159`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:1322 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:1322)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedImages) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:1322`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:1493 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:1493)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedExternal) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:1493`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:1625 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:1625)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedExternal_External) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:1625`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:1837 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:1837)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedImages_Image) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:1837`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:2017 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:2017)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphFollow) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:2017`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:2225 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:2225)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *ActorProfile) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:2225`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:2822 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:2822)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedRecord) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:2822`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:2954 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:2954)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedLike) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:2954`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:3164 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:3164)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *RichtextFacet) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:3164`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:3341 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:3341)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *RichtextFacet_ByteSlice) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:3341`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:3504 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:3504)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *RichtextFacet_Link) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:3504`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:3634 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:3634)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *RichtextFacet_Mention) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:3634`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:3764 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:3764)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *RichtextFacet_Tag) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:3764`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:3894 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:3894)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedRecordWithMedia) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:3894`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:4062 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:4062)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedDefs_NotFoundPost) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:4062`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:4226 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:4226)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphBlock) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:4226`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:4390 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:4390)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphList) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:4390`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:4830 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:4830)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphListitem) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:4830`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:5028 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:5028)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedGenerator) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:5028`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:5571 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:5571)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphListblock) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:5571`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:5735 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:5735)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedDefs_AspectRatio) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:5735`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:5898 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:5898)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedThreadgate) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:5898`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:6225 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:6225)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedThreadgate_ListRule) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:6225`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:6355 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:6355)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedThreadgate_MentionRule) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:6355`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:6451 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:6451)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedThreadgate_FollowerRule) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:6451`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:6547 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:6547)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedThreadgate_FollowingRule) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:6547`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:6643 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:6643)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphStarterpack_FeedItem) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:6643`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:6743 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:6743)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphStarterpack) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:6743`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:7163 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:7163)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelerService) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:7163`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:7645 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:7645)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelerDefs_LabelerPolicies) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:7645`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:7883 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:7883)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedVideo) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:7883`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:8198 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:8198)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedVideo_Caption) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:8198`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:8334 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:8334)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPostgate) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:8334`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:8661 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:8661)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPostgate_DisableRule) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:8661`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:8757 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:8757)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphVerification) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:8757`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:8989 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:8989)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *ActorStatus) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:8989`



---


[function] name: MarshalCBOR file: api/bsky/cbor_gen.go:9269 returns_error: нет description: —


### MarshalCBOR (api/bsky/cbor_gen.go:9269)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *NotificationDeclaration) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/cbor_gen.go:9269`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:318 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:318)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPost) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:318`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:737 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:737)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedRepost) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:737`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:927 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:927)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPost_Entity) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:927`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:1067 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:1067)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPost_ReplyRef) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:1067`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:1218 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:1218)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPost_TextSlice) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:1218`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:1381 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:1381)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedImages) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:1381`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:1542 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:1542)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedExternal) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:1542`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:1732 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:1732)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedExternal_External) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:1732`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:1914 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:1914)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedImages_Image) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:1914`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:2120 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:2120)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphFollow) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:2120`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:2554 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:2554)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorProfile) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:2554`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:2871 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:2871)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedRecord) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:2871`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:3050 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:3050)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedLike) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:3050`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:3220 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:3220)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RichtextFacet) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:3220`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:3400 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:3400)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RichtextFacet_ByteSlice) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:3400`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:3560 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:3560)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RichtextFacet_Link) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:3560`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:3690 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:3690)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RichtextFacet_Mention) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:3690`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:3820 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:3820)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RichtextFacet_Tag) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:3820`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:3959 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:3959)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedRecordWithMedia) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:3959`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:4134 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:4134)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedDefs_NotFoundPost) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:4134`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:4305 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:4305)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphBlock) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:4305`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:4614 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:4614)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphList) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:4614`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:4932 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:4932)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphListitem) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:4932`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:5311 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:5311)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedGenerator) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:5311`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:5650 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:5650)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphListblock) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:5650`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:5794 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:5794)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedDefs_AspectRatio) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:5794`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:6051 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:6051)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedThreadgate) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:6051`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:6281 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:6281)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedThreadgate_ListRule) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:6281`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:6388 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:6388)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedThreadgate_MentionRule) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:6388`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:6484 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:6484)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedThreadgate_FollowerRule) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:6484`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:6580 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:6580)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedThreadgate_FollowingRule) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:6580`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:6680 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:6680)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphStarterpack_FeedItem) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:6680`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:6948 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:6948)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphStarterpack) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:6948`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:7391 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:7391)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelerService) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:7391`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:7732 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:7732)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelerDefs_LabelerPolicies) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:7732`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:8025 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:8025)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedVideo) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:8025`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:8251 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:8251)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedVideo_Caption) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:8251`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:8487 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:8487)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPostgate) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:8487`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:8694 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:8694)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPostgate_DisableRule) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:8694`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:8882 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:8882)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphVerification) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:8882`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:9128 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:9128)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *ActorStatus) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:9128`



---


[function] name: UnmarshalCBOR file: api/bsky/cbor_gen.go:9325 returns_error: да description: —


### UnmarshalCBOR (api/bsky/cbor_gen.go:9325)


UnmarshalCBOR is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *NotificationDeclaration) UnmarshalCBOR((err error)) (err error)
```


**Тип ответа:** err


```json
{
  "$type": "string",
  "access": "string",
  "comment": "string",
  "status": "string"
}
```


*Определено в:* `api/ozone/moderationdefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `err error`


*Пример возврата ошибки:* при ошибке возвращается ненулевой `error` (см. код функции).


📍 *Расположение:* `api/bsky/cbor_gen.go:9325`




## api/bsky/contactdismissMatch.go


📄 Исходный файл: `api/bsky/contactdismissMatch.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ContactDismissMatch](#contactdismissmatch-apibskycontactdismissmatchgo24) `:24`


</details>


[function] name: ContactDismissMatch file: api/bsky/contactdismissMatch.go:24 returns_error: да description: ContactDismissMatch calls the XRPC method "app.bsky.contact.dismissMatch".


### ContactDismissMatch (api/bsky/contactdismissMatch.go:24)


ContactDismissMatch calls the XRPC method "app.bsky.contact.dismissMatch".


```go
func ContactDismissMatch((*ContactDismissMatch_Output, error)) (*ContactDismissMatch_Output, error)
```


**Тип запроса:** ContactDismissMatch_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContactDismissMatch_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ContactDismissMatch_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/contactdismissMatch.go:24`




## api/bsky/contactgetMatches.go


📄 Исходный файл: `api/bsky/contactgetMatches.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ContactGetMatches](#contactgetmatches-apibskycontactgetmatchesgo20) `:20`


</details>


[function] name: ContactGetMatches file: api/bsky/contactgetMatches.go:20 returns_error: да description: ContactGetMatches calls the XRPC method "app.bsky.contact.getMatches".


### ContactGetMatches (api/bsky/contactgetMatches.go:20)


ContactGetMatches calls the XRPC method "app.bsky.contact.getMatches".


```go
func ContactGetMatches((*ContactGetMatches_Output, error)) (*ContactGetMatches_Output, error)
```


**Тип запроса:** ContactGetMatches_Output


```json
{
  "cursor": "string",
  "matches": []
}
```


*Определено в:* `api/bsky/contactgetMatches.go`


**Тип ответа:** ContactGetMatches_Output


```json
{
  "cursor": "string",
  "matches": []
}
```


*Определено в:* `api/bsky/contactgetMatches.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ContactGetMatches_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/contactgetMatches.go:20`




## api/bsky/contactgetSyncStatus.go


📄 Исходный файл: `api/bsky/contactgetSyncStatus.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ContactGetSyncStatus](#contactgetsyncstatus-apibskycontactgetsyncstatusgo20) `:20`


</details>


[function] name: ContactGetSyncStatus file: api/bsky/contactgetSyncStatus.go:20 returns_error: да description: ContactGetSyncStatus calls the XRPC method "app.bsky.contact.getSyncStatus".


### ContactGetSyncStatus (api/bsky/contactgetSyncStatus.go:20)


ContactGetSyncStatus calls the XRPC method "app.bsky.contact.getSyncStatus".


```go
func ContactGetSyncStatus((*ContactGetSyncStatus_Output, error)) (*ContactGetSyncStatus_Output, error)
```


**Тип запроса:** ContactGetSyncStatus_Output


```json
{
  "syncStatus": null
}
```


*Определено в:* `api/bsky/contactgetSyncStatus.go`


**Тип ответа:** ContactGetSyncStatus_Output


```json
{
  "syncStatus": null
}
```


*Определено в:* `api/bsky/contactgetSyncStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ContactGetSyncStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/contactgetSyncStatus.go:20`




## api/bsky/contactimportContacts.go


📄 Исходный файл: `api/bsky/contactimportContacts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ContactImportContacts](#contactimportcontacts-apibskycontactimportcontactsgo28) `:28`


</details>


[function] name: ContactImportContacts file: api/bsky/contactimportContacts.go:28 returns_error: да description: ContactImportContacts calls the XRPC method "app.bsky.contact.importContacts".


### ContactImportContacts (api/bsky/contactimportContacts.go:28)


ContactImportContacts calls the XRPC method "app.bsky.contact.importContacts".


```go
func ContactImportContacts((*ContactImportContacts_Output, error)) (*ContactImportContacts_Output, error)
```


**Тип запроса:** ContactImportContacts_Output


```json
{
  "matchesAndContactIndexes": []
}
```


*Определено в:* `api/bsky/contactimportContacts.go`


**Тип ответа:** ContactImportContacts_Output


```json
{
  "matchesAndContactIndexes": []
}
```


*Определено в:* `api/bsky/contactimportContacts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ContactImportContacts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/contactimportContacts.go:28`




## api/bsky/contactremoveData.go


📄 Исходный файл: `api/bsky/contactremoveData.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ContactRemoveData](#contactremovedata-apibskycontactremovedatago22) `:22`


</details>


[function] name: ContactRemoveData file: api/bsky/contactremoveData.go:22 returns_error: да description: ContactRemoveData calls the XRPC method "app.bsky.contact.removeData".


### ContactRemoveData (api/bsky/contactremoveData.go:22)


ContactRemoveData calls the XRPC method "app.bsky.contact.removeData".


```go
func ContactRemoveData((*ContactRemoveData_Output, error)) (*ContactRemoveData_Output, error)
```


**Тип запроса:** ContactRemoveData_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContactRemoveData_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ContactRemoveData_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/contactremoveData.go:22`




## api/bsky/contactsendNotification.go


📄 Исходный файл: `api/bsky/contactsendNotification.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ContactSendNotification](#contactsendnotification-apibskycontactsendnotificationgo26) `:26`


</details>


[function] name: ContactSendNotification file: api/bsky/contactsendNotification.go:26 returns_error: да description: ContactSendNotification calls the XRPC method "app.bsky.contact.sendNotification".


### ContactSendNotification (api/bsky/contactsendNotification.go:26)


ContactSendNotification calls the XRPC method "app.bsky.contact.sendNotification".


```go
func ContactSendNotification((*ContactSendNotification_Output, error)) (*ContactSendNotification_Output, error)
```


**Тип запроса:** ContactSendNotification_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContactSendNotification_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ContactSendNotification_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/contactsendNotification.go:26`




## api/bsky/contactstartPhoneVerification.go


📄 Исходный файл: `api/bsky/contactstartPhoneVerification.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ContactStartPhoneVerification](#contactstartphoneverification-apibskycontactstartphoneverificationgo24) `:24`


</details>


[function] name: ContactStartPhoneVerification file: api/bsky/contactstartPhoneVerification.go:24 returns_error: да description: ContactStartPhoneVerification calls the XRPC method "app.bsky.contact.startPhoneVerification".


### ContactStartPhoneVerification (api/bsky/contactstartPhoneVerification.go:24)


ContactStartPhoneVerification calls the XRPC method "app.bsky.contact.startPhoneVerification".


```go
func ContactStartPhoneVerification((*ContactStartPhoneVerification_Output, error)) (*ContactStartPhoneVerification_Output, error)
```


**Тип запроса:** ContactStartPhoneVerification_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** ContactStartPhoneVerification_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ContactStartPhoneVerification_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/contactstartPhoneVerification.go:24`




## api/bsky/contactverifyPhone.go


📄 Исходный файл: `api/bsky/contactverifyPhone.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [ContactVerifyPhone](#contactverifyphone-apibskycontactverifyphonego28) `:28`


</details>


[function] name: ContactVerifyPhone file: api/bsky/contactverifyPhone.go:28 returns_error: да description: ContactVerifyPhone calls the XRPC method "app.bsky.contact.verifyPhone".


### ContactVerifyPhone (api/bsky/contactverifyPhone.go:28)


ContactVerifyPhone calls the XRPC method "app.bsky.contact.verifyPhone".


```go
func ContactVerifyPhone((*ContactVerifyPhone_Output, error)) (*ContactVerifyPhone_Output, error)
```


**Тип запроса:** ContactVerifyPhone_Output


```json
{
  "token": "string"
}
```


*Определено в:* `api/bsky/contactverifyPhone.go`


**Тип ответа:** ContactVerifyPhone_Output


```json
{
  "token": "string"
}
```


*Определено в:* `api/bsky/contactverifyPhone.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*ContactVerifyPhone_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/contactverifyPhone.go:28`




## api/bsky/draftcreateDraft.go


📄 Исходный файл: `api/bsky/draftcreateDraft.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DraftCreateDraft](#draftcreatedraft-apibskydraftcreatedraftgo25) `:25`


</details>


[function] name: DraftCreateDraft file: api/bsky/draftcreateDraft.go:25 returns_error: да description: DraftCreateDraft calls the XRPC method "app.bsky.draft.createDraft".


### DraftCreateDraft (api/bsky/draftcreateDraft.go:25)


DraftCreateDraft calls the XRPC method "app.bsky.draft.createDraft".


```go
func DraftCreateDraft((*DraftCreateDraft_Output, error)) (*DraftCreateDraft_Output, error)
```


**Тип запроса:** DraftCreateDraft_Output


```json
{
  "id": "string"
}
```


*Определено в:* `api/bsky/draftcreateDraft.go`


**Тип ответа:** DraftCreateDraft_Output


```json
{
  "id": "string"
}
```


*Определено в:* `api/bsky/draftcreateDraft.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DraftCreateDraft_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/draftcreateDraft.go:25`




## api/bsky/draftdefs.go


📄 Исходный файл: `api/bsky/draftdefs.go`


<details open>
<summary><b>Функции в этом файле (6)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apibskydraftdefsgo83) `:83`

- 🔗 [MarshalJSON](#marshaljson-apibskydraftdefsgo132) `:132`

- 🔗 [MarshalJSON](#marshaljson-apibskydraftdefsgo162) `:162`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskydraftdefsgo91) `:91`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskydraftdefsgo140) `:140`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskydraftdefsgo182) `:182`


</details>


[function] name: MarshalJSON file: api/bsky/draftdefs.go:83 returns_error: да description: —


### MarshalJSON (api/bsky/draftdefs.go:83)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *DraftDefs_DraftPost_Labels) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/draftdefs.go:83`



---


[function] name: MarshalJSON file: api/bsky/draftdefs.go:132 returns_error: да description: —


### MarshalJSON (api/bsky/draftdefs.go:132)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *DraftDefs_Draft_PostgateEmbeddingRules_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/draftdefs.go:132`



---


[function] name: MarshalJSON file: api/bsky/draftdefs.go:162 returns_error: да description: —


### MarshalJSON (api/bsky/draftdefs.go:162)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *DraftDefs_Draft_ThreadgateAllow_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/draftdefs.go:162`



---


[function] name: UnmarshalJSON file: api/bsky/draftdefs.go:91 returns_error: нет description: —


### UnmarshalJSON (api/bsky/draftdefs.go:91)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *DraftDefs_DraftPost_Labels) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/draftdefs.go:91`



---


[function] name: UnmarshalJSON file: api/bsky/draftdefs.go:140 returns_error: нет description: —


### UnmarshalJSON (api/bsky/draftdefs.go:140)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *DraftDefs_Draft_PostgateEmbeddingRules_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/draftdefs.go:140`



---


[function] name: UnmarshalJSON file: api/bsky/draftdefs.go:182 returns_error: нет description: —


### UnmarshalJSON (api/bsky/draftdefs.go:182)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *DraftDefs_Draft_ThreadgateAllow_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/draftdefs.go:182`




## api/bsky/draftdeleteDraft.go


📄 Исходный файл: `api/bsky/draftdeleteDraft.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DraftDeleteDraft](#draftdeletedraft-apibskydraftdeletedraftgo19) `:19`


</details>


[function] name: DraftDeleteDraft file: api/bsky/draftdeleteDraft.go:19 returns_error: нет description: DraftDeleteDraft calls the XRPC method "app.bsky.draft.deleteDraft".


### DraftDeleteDraft (api/bsky/draftdeleteDraft.go:19)


DraftDeleteDraft calls the XRPC method "app.bsky.draft.deleteDraft".


```go
func DraftDeleteDraft((ctx context.Context, c lexutil.LexClient, input *DraftDeleteDraft_Input)) (ctx context.Context, c lexutil.LexClient, input *DraftDeleteDraft_Input)
```


**Тип запроса:** DraftDeleteDraft_Input


```json
{
  "id": "string"
}
```


*Определено в:* `api/bsky/draftdeleteDraft.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DraftDeleteDraft_Input


```json
{
  "id": "string"
}
```


*Определено в:* `api/bsky/draftdeleteDraft.go`


📍 *Расположение:* `api/bsky/draftdeleteDraft.go:19`




## api/bsky/draftgetDrafts.go


📄 Исходный файл: `api/bsky/draftgetDrafts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DraftGetDrafts](#draftgetdrafts-apibskydraftgetdraftsgo20) `:20`


</details>


[function] name: DraftGetDrafts file: api/bsky/draftgetDrafts.go:20 returns_error: да description: DraftGetDrafts calls the XRPC method "app.bsky.draft.getDrafts".


### DraftGetDrafts (api/bsky/draftgetDrafts.go:20)


DraftGetDrafts calls the XRPC method "app.bsky.draft.getDrafts".


```go
func DraftGetDrafts((*DraftGetDrafts_Output, error)) (*DraftGetDrafts_Output, error)
```


**Тип запроса:** DraftGetDrafts_Output


```json
{
  "cursor": "string",
  "drafts": []
}
```


*Определено в:* `api/bsky/draftgetDrafts.go`


**Тип ответа:** DraftGetDrafts_Output


```json
{
  "cursor": "string",
  "drafts": []
}
```


*Определено в:* `api/bsky/draftgetDrafts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*DraftGetDrafts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/draftgetDrafts.go:20`




## api/bsky/draftupdateDraft.go


📄 Исходный файл: `api/bsky/draftupdateDraft.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [DraftUpdateDraft](#draftupdatedraft-apibskydraftupdatedraftgo19) `:19`


</details>


[function] name: DraftUpdateDraft file: api/bsky/draftupdateDraft.go:19 returns_error: нет description: DraftUpdateDraft calls the XRPC method "app.bsky.draft.updateDraft".


### DraftUpdateDraft (api/bsky/draftupdateDraft.go:19)


DraftUpdateDraft calls the XRPC method "app.bsky.draft.updateDraft".


```go
func DraftUpdateDraft((ctx context.Context, c lexutil.LexClient, input *DraftUpdateDraft_Input)) (ctx context.Context, c lexutil.LexClient, input *DraftUpdateDraft_Input)
```


**Тип запроса:** DraftUpdateDraft_Input


```json
{
  "draft": null
}
```


*Определено в:* `api/bsky/draftupdateDraft.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** DraftUpdateDraft_Input


```json
{
  "draft": null
}
```


*Определено в:* `api/bsky/draftupdateDraft.go`


📍 *Расположение:* `api/bsky/draftupdateDraft.go:19`




## api/bsky/embedexternal.go


📄 Исходный файл: `api/bsky/embedexternal.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskyembedexternalgo11) `:11`


</details>


[function] name: init file: api/bsky/embedexternal.go:11 returns_error: нет description: —


### init (api/bsky/embedexternal.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/embedexternal.go:11`




## api/bsky/embedimages.go


📄 Исходный файл: `api/bsky/embedimages.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskyembedimagesgo11) `:11`


</details>


[function] name: init file: api/bsky/embedimages.go:11 returns_error: нет description: —


### init (api/bsky/embedimages.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/embedimages.go:11`




## api/bsky/embedrecord.go


📄 Исходный файл: `api/bsky/embedrecord.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apibskyembedrecordgo78) `:78`

- 🔗 [MarshalJSON](#marshaljson-apibskyembedrecordgo140) `:140`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyembedrecordgo102) `:102`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyembedrecordgo176) `:176`

- 🔗 [init](#init-apibskyembedrecordgo15) `:15`


</details>


[function] name: MarshalJSON file: api/bsky/embedrecord.go:78 returns_error: да description: —


### MarshalJSON (api/bsky/embedrecord.go:78)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedRecord_ViewRecord_Embeds_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/embedrecord.go:78`



---


[function] name: MarshalJSON file: api/bsky/embedrecord.go:140 returns_error: да description: —


### MarshalJSON (api/bsky/embedrecord.go:140)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedRecord_View_Record) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/embedrecord.go:140`



---


[function] name: UnmarshalJSON file: api/bsky/embedrecord.go:102 returns_error: нет description: —


### UnmarshalJSON (api/bsky/embedrecord.go:102)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *EmbedRecord_ViewRecord_Embeds_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/embedrecord.go:102`



---


[function] name: UnmarshalJSON file: api/bsky/embedrecord.go:176 returns_error: нет description: —


### UnmarshalJSON (api/bsky/embedrecord.go:176)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *EmbedRecord_View_Record) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/embedrecord.go:176`



---


[function] name: init file: api/bsky/embedrecord.go:15 returns_error: нет description: —


### init (api/bsky/embedrecord.go:15)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/embedrecord.go:15`




## api/bsky/embedrecordWithMedia.go


📄 Исходный файл: `api/bsky/embedrecordWithMedia.go`


<details open>
<summary><b>Функции в этом файле (7)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskyembedrecordwithmediago71) `:71`

- 🔗 [MarshalJSON](#marshaljson-apibskyembedrecordwithmediago34) `:34`

- 🔗 [MarshalJSON](#marshaljson-apibskyembedrecordwithmediago123) `:123`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyembedrecordwithmediago89) `:89`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyembedrecordwithmediago50) `:50`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyembedrecordwithmediago139) `:139`

- 🔗 [init](#init-apibskyembedrecordwithmediago17) `:17`


</details>


[function] name: MarshalCBOR file: api/bsky/embedrecordWithMedia.go:71 returns_error: нет description: —


### MarshalCBOR (api/bsky/embedrecordWithMedia.go:71)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *EmbedRecordWithMedia_Media) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/embedrecordWithMedia.go:71`



---


[function] name: MarshalJSON file: api/bsky/embedrecordWithMedia.go:34 returns_error: да description: —


### MarshalJSON (api/bsky/embedrecordWithMedia.go:34)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedRecordWithMedia_Media) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/embedrecordWithMedia.go:34`



---


[function] name: MarshalJSON file: api/bsky/embedrecordWithMedia.go:123 returns_error: да description: —


### MarshalJSON (api/bsky/embedrecordWithMedia.go:123)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *EmbedRecordWithMedia_View_Media) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/embedrecordWithMedia.go:123`



---


[function] name: UnmarshalCBOR file: api/bsky/embedrecordWithMedia.go:89 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/embedrecordWithMedia.go:89)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *EmbedRecordWithMedia_Media) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/embedrecordWithMedia.go:89`



---


[function] name: UnmarshalJSON file: api/bsky/embedrecordWithMedia.go:50 returns_error: нет description: —


### UnmarshalJSON (api/bsky/embedrecordWithMedia.go:50)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *EmbedRecordWithMedia_Media) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/embedrecordWithMedia.go:50`



---


[function] name: UnmarshalJSON file: api/bsky/embedrecordWithMedia.go:139 returns_error: нет description: —


### UnmarshalJSON (api/bsky/embedrecordWithMedia.go:139)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *EmbedRecordWithMedia_View_Media) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/embedrecordWithMedia.go:139`



---


[function] name: init file: api/bsky/embedrecordWithMedia.go:17 returns_error: нет description: —


### init (api/bsky/embedrecordWithMedia.go:17)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/embedrecordWithMedia.go:17`




## api/bsky/embedvideo.go


📄 Исходный файл: `api/bsky/embedvideo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskyembedvideogo11) `:11`


</details>


[function] name: init file: api/bsky/embedvideo.go:11 returns_error: нет description: —


### init (api/bsky/embedvideo.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/embedvideo.go:11`




## api/bsky/feeddefs.go


📄 Исходный файл: `api/bsky/feeddefs.go`


<details open>
<summary><b>Функции в этом файле (14)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apibskyfeeddefsgo45) `:45`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeeddefsgo145) `:145`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeeddefsgo224) `:224`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeeddefsgo267) `:267`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeeddefsgo317) `:317`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeeddefsgo380) `:380`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeeddefsgo423) `:423`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeeddefsgo57) `:57`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeeddefsgo169) `:169`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeeddefsgo240) `:240`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeeddefsgo283) `:283`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeeddefsgo329) `:329`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeeddefsgo396) `:396`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeeddefsgo439) `:439`


</details>


[function] name: MarshalJSON file: api/bsky/feeddefs.go:45 returns_error: да description: —


### MarshalJSON (api/bsky/feeddefs.go:45)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedDefs_FeedViewPost_Reason) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feeddefs.go:45`



---


[function] name: MarshalJSON file: api/bsky/feeddefs.go:145 returns_error: да description: —


### MarshalJSON (api/bsky/feeddefs.go:145)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedDefs_PostView_Embed) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feeddefs.go:145`



---


[function] name: MarshalJSON file: api/bsky/feeddefs.go:224 returns_error: да description: —


### MarshalJSON (api/bsky/feeddefs.go:224)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedDefs_ReplyRef_Parent) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feeddefs.go:224`



---


[function] name: MarshalJSON file: api/bsky/feeddefs.go:267 returns_error: да description: —


### MarshalJSON (api/bsky/feeddefs.go:267)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedDefs_ReplyRef_Root) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feeddefs.go:267`



---


[function] name: MarshalJSON file: api/bsky/feeddefs.go:317 returns_error: да description: —


### MarshalJSON (api/bsky/feeddefs.go:317)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedDefs_SkeletonFeedPost_Reason) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feeddefs.go:317`



---


[function] name: MarshalJSON file: api/bsky/feeddefs.go:380 returns_error: да description: —


### MarshalJSON (api/bsky/feeddefs.go:380)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedDefs_ThreadViewPost_Parent) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feeddefs.go:380`



---


[function] name: MarshalJSON file: api/bsky/feeddefs.go:423 returns_error: да description: —


### MarshalJSON (api/bsky/feeddefs.go:423)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedDefs_ThreadViewPost_Replies_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feeddefs.go:423`



---


[function] name: UnmarshalJSON file: api/bsky/feeddefs.go:57 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feeddefs.go:57)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedDefs_FeedViewPost_Reason) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feeddefs.go:57`



---


[function] name: UnmarshalJSON file: api/bsky/feeddefs.go:169 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feeddefs.go:169)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedDefs_PostView_Embed) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feeddefs.go:169`



---


[function] name: UnmarshalJSON file: api/bsky/feeddefs.go:240 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feeddefs.go:240)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedDefs_ReplyRef_Parent) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feeddefs.go:240`



---


[function] name: UnmarshalJSON file: api/bsky/feeddefs.go:283 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feeddefs.go:283)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedDefs_ReplyRef_Root) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feeddefs.go:283`



---


[function] name: UnmarshalJSON file: api/bsky/feeddefs.go:329 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feeddefs.go:329)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedDefs_SkeletonFeedPost_Reason) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feeddefs.go:329`



---


[function] name: UnmarshalJSON file: api/bsky/feeddefs.go:396 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feeddefs.go:396)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedDefs_ThreadViewPost_Parent) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feeddefs.go:396`



---


[function] name: UnmarshalJSON file: api/bsky/feeddefs.go:439 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feeddefs.go:439)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedDefs_ThreadViewPost_Replies_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feeddefs.go:439`




## api/bsky/feeddescribeFeedGenerator.go


📄 Исходный файл: `api/bsky/feeddescribeFeedGenerator.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedDescribeFeedGenerator](#feeddescribefeedgenerator-apibskyfeeddescribefeedgeneratorgo32) `:32`


</details>


[function] name: FeedDescribeFeedGenerator file: api/bsky/feeddescribeFeedGenerator.go:32 returns_error: да description: FeedDescribeFeedGenerator calls the XRPC method "app.bsky.feed.describeFeedGenerator".


### FeedDescribeFeedGenerator (api/bsky/feeddescribeFeedGenerator.go:32)


FeedDescribeFeedGenerator calls the XRPC method "app.bsky.feed.describeFeedGenerator".


```go
func FeedDescribeFeedGenerator((*FeedDescribeFeedGenerator_Output, error)) (*FeedDescribeFeedGenerator_Output, error)
```


**Тип запроса:** FeedDescribeFeedGenerator_Output


```json
{
  "did": "string",
  "feeds": [],
  "links": null
}
```


*Определено в:* `api/bsky/feeddescribeFeedGenerator.go`


**Тип ответа:** FeedDescribeFeedGenerator_Output


```json
{
  "did": "string",
  "feeds": [],
  "links": null
}
```


*Определено в:* `api/bsky/feeddescribeFeedGenerator.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedDescribeFeedGenerator_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feeddescribeFeedGenerator.go:32`




## api/bsky/feedgenerator.go


📄 Исходный файл: `api/bsky/feedgenerator.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskyfeedgeneratorgo65) `:65`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeedgeneratorgo42) `:42`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyfeedgeneratorgo77) `:77`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeedgeneratorgo50) `:50`

- 🔗 [init](#init-apibskyfeedgeneratorgo18) `:18`


</details>


[function] name: MarshalCBOR file: api/bsky/feedgenerator.go:65 returns_error: нет description: —


### MarshalCBOR (api/bsky/feedgenerator.go:65)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedGenerator_Labels) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/feedgenerator.go:65`



---


[function] name: MarshalJSON file: api/bsky/feedgenerator.go:42 returns_error: да description: —


### MarshalJSON (api/bsky/feedgenerator.go:42)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedGenerator_Labels) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgenerator.go:42`



---


[function] name: UnmarshalCBOR file: api/bsky/feedgenerator.go:77 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/feedgenerator.go:77)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *FeedGenerator_Labels) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/feedgenerator.go:77`



---


[function] name: UnmarshalJSON file: api/bsky/feedgenerator.go:50 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feedgenerator.go:50)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedGenerator_Labels) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feedgenerator.go:50`



---


[function] name: init file: api/bsky/feedgenerator.go:18 returns_error: нет description: —


### init (api/bsky/feedgenerator.go:18)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/feedgenerator.go:18`




## api/bsky/feedgetActorFeeds.go


📄 Исходный файл: `api/bsky/feedgetActorFeeds.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetActorFeeds](#feedgetactorfeeds-apibskyfeedgetactorfeedsgo20) `:20`


</details>


[function] name: FeedGetActorFeeds file: api/bsky/feedgetActorFeeds.go:20 returns_error: да description: FeedGetActorFeeds calls the XRPC method "app.bsky.feed.getActorFeeds".


### FeedGetActorFeeds (api/bsky/feedgetActorFeeds.go:20)


FeedGetActorFeeds calls the XRPC method "app.bsky.feed.getActorFeeds".


```go
func FeedGetActorFeeds((*FeedGetActorFeeds_Output, error)) (*FeedGetActorFeeds_Output, error)
```


**Тип запроса:** FeedGetActorFeeds_Output


```json
{
  "cursor": "string",
  "feeds": []
}
```


*Определено в:* `api/bsky/feedgetActorFeeds.go`


**Тип ответа:** FeedGetActorFeeds_Output


```json
{
  "cursor": "string",
  "feeds": []
}
```


*Определено в:* `api/bsky/feedgetActorFeeds.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetActorFeeds_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetActorFeeds.go:20`




## api/bsky/feedgetActorLikes.go


📄 Исходный файл: `api/bsky/feedgetActorLikes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetActorLikes](#feedgetactorlikes-apibskyfeedgetactorlikesgo20) `:20`


</details>


[function] name: FeedGetActorLikes file: api/bsky/feedgetActorLikes.go:20 returns_error: да description: FeedGetActorLikes calls the XRPC method "app.bsky.feed.getActorLikes".


### FeedGetActorLikes (api/bsky/feedgetActorLikes.go:20)


FeedGetActorLikes calls the XRPC method "app.bsky.feed.getActorLikes".


```go
func FeedGetActorLikes((*FeedGetActorLikes_Output, error)) (*FeedGetActorLikes_Output, error)
```


**Тип запроса:** FeedGetActorLikes_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetActorLikes.go`


**Тип ответа:** FeedGetActorLikes_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetActorLikes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetActorLikes_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetActorLikes.go:20`




## api/bsky/feedgetAuthorFeed.go


📄 Исходный файл: `api/bsky/feedgetAuthorFeed.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetAuthorFeed](#feedgetauthorfeed-apibskyfeedgetauthorfeedgo22) `:22`


</details>


[function] name: FeedGetAuthorFeed file: api/bsky/feedgetAuthorFeed.go:22 returns_error: да description: FeedGetAuthorFeed calls the XRPC method "app.bsky.feed.getAuthorFeed".

filter: Combinations of post/repost types to inc


### FeedGetAuthorFeed (api/bsky/feedgetAuthorFeed.go:22)


FeedGetAuthorFeed calls the XRPC method "app.bsky.feed.getAuthorFeed".

filter: Combinations of post/repost types to include in response.


```go
func FeedGetAuthorFeed((*FeedGetAuthorFeed_Output, error)) (*FeedGetAuthorFeed_Output, error)
```


**Тип запроса:** FeedGetAuthorFeed_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetAuthorFeed.go`


**Тип ответа:** FeedGetAuthorFeed_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetAuthorFeed.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetAuthorFeed_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetAuthorFeed.go:22`




## api/bsky/feedgetFeed.go


📄 Исходный файл: `api/bsky/feedgetFeed.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetFeed](#feedgetfeed-apibskyfeedgetfeedgo20) `:20`


</details>


[function] name: FeedGetFeed file: api/bsky/feedgetFeed.go:20 returns_error: да description: FeedGetFeed calls the XRPC method "app.bsky.feed.getFeed".


### FeedGetFeed (api/bsky/feedgetFeed.go:20)


FeedGetFeed calls the XRPC method "app.bsky.feed.getFeed".


```go
func FeedGetFeed((*FeedGetFeed_Output, error)) (*FeedGetFeed_Output, error)
```


**Тип запроса:** FeedGetFeed_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetFeed.go`


**Тип ответа:** FeedGetFeed_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetFeed.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetFeed_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetFeed.go:20`




## api/bsky/feedgetFeedGenerator.go


📄 Исходный файл: `api/bsky/feedgetFeedGenerator.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetFeedGenerator](#feedgetfeedgenerator-apibskyfeedgetfeedgeneratorgo25) `:25`


</details>


[function] name: FeedGetFeedGenerator file: api/bsky/feedgetFeedGenerator.go:25 returns_error: да description: FeedGetFeedGenerator calls the XRPC method "app.bsky.feed.getFeedGenerator".

feed: AT-URI of the feed generator record.


### FeedGetFeedGenerator (api/bsky/feedgetFeedGenerator.go:25)


FeedGetFeedGenerator calls the XRPC method "app.bsky.feed.getFeedGenerator".

feed: AT-URI of the feed generator record.


```go
func FeedGetFeedGenerator((*FeedGetFeedGenerator_Output, error)) (*FeedGetFeedGenerator_Output, error)
```


**Тип запроса:** FeedGetFeedGenerator_Output


```json
{
  "isOnline": false,
  "isValid": false,
  "view": null
}
```


*Определено в:* `api/bsky/feedgetFeedGenerator.go`


**Тип ответа:** FeedGetFeedGenerator_Output


```json
{
  "isOnline": false,
  "isValid": false,
  "view": null
}
```


*Определено в:* `api/bsky/feedgetFeedGenerator.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetFeedGenerator_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetFeedGenerator.go:25`




## api/bsky/feedgetFeedGenerators.go


📄 Исходный файл: `api/bsky/feedgetFeedGenerators.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetFeedGenerators](#feedgetfeedgenerators-apibskyfeedgetfeedgeneratorsgo19) `:19`


</details>


[function] name: FeedGetFeedGenerators file: api/bsky/feedgetFeedGenerators.go:19 returns_error: да description: FeedGetFeedGenerators calls the XRPC method "app.bsky.feed.getFeedGenerators".


### FeedGetFeedGenerators (api/bsky/feedgetFeedGenerators.go:19)


FeedGetFeedGenerators calls the XRPC method "app.bsky.feed.getFeedGenerators".


```go
func FeedGetFeedGenerators((*FeedGetFeedGenerators_Output, error)) (*FeedGetFeedGenerators_Output, error)
```


**Тип запроса:** FeedGetFeedGenerators_Output


```json
{
  "feeds": []
}
```


*Определено в:* `api/bsky/feedgetFeedGenerators.go`


**Тип ответа:** FeedGetFeedGenerators_Output


```json
{
  "feeds": []
}
```


*Определено в:* `api/bsky/feedgetFeedGenerators.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetFeedGenerators_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetFeedGenerators.go:19`




## api/bsky/feedgetFeedSkeleton.go


📄 Исходный файл: `api/bsky/feedgetFeedSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetFeedSkeleton](#feedgetfeedskeleton-apibskyfeedgetfeedskeletongo24) `:24`


</details>


[function] name: FeedGetFeedSkeleton file: api/bsky/feedgetFeedSkeleton.go:24 returns_error: да description: FeedGetFeedSkeleton calls the XRPC method "app.bsky.feed.getFeedSkeleton".

feed: Reference to feed generator record des


### FeedGetFeedSkeleton (api/bsky/feedgetFeedSkeleton.go:24)


FeedGetFeedSkeleton calls the XRPC method "app.bsky.feed.getFeedSkeleton".

feed: Reference to feed generator record describing the specific feed being requested.


```go
func FeedGetFeedSkeleton((*FeedGetFeedSkeleton_Output, error)) (*FeedGetFeedSkeleton_Output, error)
```


**Тип запроса:** FeedGetFeedSkeleton_Output


```json
{
  "cursor": "string",
  "feed": [],
  "reqId": "string"
}
```


*Определено в:* `api/bsky/feedgetFeedSkeleton.go`


**Тип ответа:** FeedGetFeedSkeleton_Output


```json
{
  "cursor": "string",
  "feed": [],
  "reqId": "string"
}
```


*Определено в:* `api/bsky/feedgetFeedSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetFeedSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetFeedSkeleton.go:24`




## api/bsky/feedgetLikes.go


📄 Исходный файл: `api/bsky/feedgetLikes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetLikes](#feedgetlikes-apibskyfeedgetlikesgo32) `:32`


</details>


[function] name: FeedGetLikes file: api/bsky/feedgetLikes.go:32 returns_error: да description: FeedGetLikes calls the XRPC method "app.bsky.feed.getLikes".

cid: CID of the subject record (aka, specific version of r


### FeedGetLikes (api/bsky/feedgetLikes.go:32)


FeedGetLikes calls the XRPC method "app.bsky.feed.getLikes".

cid: CID of the subject record (aka, specific version of record), to filter likes.
uri: AT-URI of the subject (eg, a post record).


```go
func FeedGetLikes((*FeedGetLikes_Output, error)) (*FeedGetLikes_Output, error)
```


**Тип запроса:** FeedGetLikes_Output


```json
{
  "cid": "string",
  "cursor": "string",
  "likes": [],
  "uri": "string"
}
```


*Определено в:* `api/bsky/feedgetLikes.go`


**Тип ответа:** FeedGetLikes_Output


```json
{
  "cid": "string",
  "cursor": "string",
  "likes": [],
  "uri": "string"
}
```


*Определено в:* `api/bsky/feedgetLikes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetLikes_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetLikes.go:32`




## api/bsky/feedgetListFeed.go


📄 Исходный файл: `api/bsky/feedgetListFeed.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetListFeed](#feedgetlistfeed-apibskyfeedgetlistfeedgo22) `:22`


</details>


[function] name: FeedGetListFeed file: api/bsky/feedgetListFeed.go:22 returns_error: да description: FeedGetListFeed calls the XRPC method "app.bsky.feed.getListFeed".

list: Reference (AT-URI) to the list record.


### FeedGetListFeed (api/bsky/feedgetListFeed.go:22)


FeedGetListFeed calls the XRPC method "app.bsky.feed.getListFeed".

list: Reference (AT-URI) to the list record.


```go
func FeedGetListFeed((*FeedGetListFeed_Output, error)) (*FeedGetListFeed_Output, error)
```


**Тип запроса:** FeedGetListFeed_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetListFeed.go`


**Тип ответа:** FeedGetListFeed_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetListFeed.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetListFeed_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetListFeed.go:22`




## api/bsky/feedgetPostThread.go


📄 Исходный файл: `api/bsky/feedgetPostThread.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [FeedGetPostThread](#feedgetpostthread-apibskyfeedgetpostthreadgo69) `:69`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeedgetpostthreadgo27) `:27`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeedgetpostthreadgo43) `:43`


</details>


[function] name: FeedGetPostThread file: api/bsky/feedgetPostThread.go:69 returns_error: да description: FeedGetPostThread calls the XRPC method "app.bsky.feed.getPostThread".

depth: How many levels of reply depth should be 


### FeedGetPostThread (api/bsky/feedgetPostThread.go:69)


FeedGetPostThread calls the XRPC method "app.bsky.feed.getPostThread".

depth: How many levels of reply depth should be included in response.
parentHeight: How many levels of parent (and grandparent, etc) post to include.
uri: Reference (AT-URI) to post record.


```go
func FeedGetPostThread((*FeedGetPostThread_Output, error)) (*FeedGetPostThread_Output, error)
```


**Тип запроса:** FeedGetPostThread_Output


```json
{
  "thread": null,
  "threadgate": null
}
```


*Определено в:* `api/bsky/feedgetPostThread.go`


**Тип ответа:** FeedGetPostThread_Output


```json
{
  "thread": null,
  "threadgate": null
}
```


*Определено в:* `api/bsky/feedgetPostThread.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetPostThread_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetPostThread.go:69`



---


[function] name: MarshalJSON file: api/bsky/feedgetPostThread.go:27 returns_error: да description: —


### MarshalJSON (api/bsky/feedgetPostThread.go:27)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedGetPostThread_Output_Thread) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetPostThread.go:27`



---


[function] name: UnmarshalJSON file: api/bsky/feedgetPostThread.go:43 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feedgetPostThread.go:43)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedGetPostThread_Output_Thread) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feedgetPostThread.go:43`




## api/bsky/feedgetPosts.go


📄 Исходный файл: `api/bsky/feedgetPosts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetPosts](#feedgetposts-apibskyfeedgetpostsgo21) `:21`


</details>


[function] name: FeedGetPosts file: api/bsky/feedgetPosts.go:21 returns_error: да description: FeedGetPosts calls the XRPC method "app.bsky.feed.getPosts".

uris: List of post AT-URIs to return hydrated views for.


### FeedGetPosts (api/bsky/feedgetPosts.go:21)


FeedGetPosts calls the XRPC method "app.bsky.feed.getPosts".

uris: List of post AT-URIs to return hydrated views for.


```go
func FeedGetPosts((*FeedGetPosts_Output, error)) (*FeedGetPosts_Output, error)
```


**Тип запроса:** FeedGetPosts_Output


```json
{
  "posts": []
}
```


*Определено в:* `api/bsky/feedgetPosts.go`


**Тип ответа:** FeedGetPosts_Output


```json
{
  "posts": []
}
```


*Определено в:* `api/bsky/feedgetPosts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetPosts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetPosts.go:21`




## api/bsky/feedgetQuotes.go


📄 Исходный файл: `api/bsky/feedgetQuotes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetQuotes](#feedgetquotes-apibskyfeedgetquotesgo25) `:25`


</details>


[function] name: FeedGetQuotes file: api/bsky/feedgetQuotes.go:25 returns_error: да description: FeedGetQuotes calls the XRPC method "app.bsky.feed.getQuotes".

cid: If supplied, filters to quotes of specific version 


### FeedGetQuotes (api/bsky/feedgetQuotes.go:25)


FeedGetQuotes calls the XRPC method "app.bsky.feed.getQuotes".

cid: If supplied, filters to quotes of specific version (by CID) of the post record.
uri: Reference (AT-URI) of post record


```go
func FeedGetQuotes((*FeedGetQuotes_Output, error)) (*FeedGetQuotes_Output, error)
```


**Тип запроса:** FeedGetQuotes_Output


```json
{
  "cid": "string",
  "cursor": "string",
  "posts": [],
  "uri": "string"
}
```


*Определено в:* `api/bsky/feedgetQuotes.go`


**Тип ответа:** FeedGetQuotes_Output


```json
{
  "cid": "string",
  "cursor": "string",
  "posts": [],
  "uri": "string"
}
```


*Определено в:* `api/bsky/feedgetQuotes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetQuotes_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetQuotes.go:25`




## api/bsky/feedgetRepostedBy.go


📄 Исходный файл: `api/bsky/feedgetRepostedBy.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetRepostedBy](#feedgetrepostedby-apibskyfeedgetrepostedbygo25) `:25`


</details>


[function] name: FeedGetRepostedBy file: api/bsky/feedgetRepostedBy.go:25 returns_error: да description: FeedGetRepostedBy calls the XRPC method "app.bsky.feed.getRepostedBy".

cid: If supplied, filters to reposts of specific


### FeedGetRepostedBy (api/bsky/feedgetRepostedBy.go:25)


FeedGetRepostedBy calls the XRPC method "app.bsky.feed.getRepostedBy".

cid: If supplied, filters to reposts of specific version (by CID) of the post record.
uri: Reference (AT-URI) of post record


```go
func FeedGetRepostedBy((*FeedGetRepostedBy_Output, error)) (*FeedGetRepostedBy_Output, error)
```


**Тип запроса:** FeedGetRepostedBy_Output


```json
{
  "cid": "string",
  "cursor": "string",
  "repostedBy": [],
  "uri": "string"
}
```


*Определено в:* `api/bsky/feedgetRepostedBy.go`


**Тип ответа:** FeedGetRepostedBy_Output


```json
{
  "cid": "string",
  "cursor": "string",
  "repostedBy": [],
  "uri": "string"
}
```


*Определено в:* `api/bsky/feedgetRepostedBy.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetRepostedBy_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetRepostedBy.go:25`




## api/bsky/feedgetSuggestedFeeds.go


📄 Исходный файл: `api/bsky/feedgetSuggestedFeeds.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetSuggestedFeeds](#feedgetsuggestedfeeds-apibskyfeedgetsuggestedfeedsgo20) `:20`


</details>


[function] name: FeedGetSuggestedFeeds file: api/bsky/feedgetSuggestedFeeds.go:20 returns_error: да description: FeedGetSuggestedFeeds calls the XRPC method "app.bsky.feed.getSuggestedFeeds".


### FeedGetSuggestedFeeds (api/bsky/feedgetSuggestedFeeds.go:20)


FeedGetSuggestedFeeds calls the XRPC method "app.bsky.feed.getSuggestedFeeds".


```go
func FeedGetSuggestedFeeds((*FeedGetSuggestedFeeds_Output, error)) (*FeedGetSuggestedFeeds_Output, error)
```


**Тип запроса:** FeedGetSuggestedFeeds_Output


```json
{
  "cursor": "string",
  "feeds": []
}
```


*Определено в:* `api/bsky/feedgetSuggestedFeeds.go`


**Тип ответа:** FeedGetSuggestedFeeds_Output


```json
{
  "cursor": "string",
  "feeds": []
}
```


*Определено в:* `api/bsky/feedgetSuggestedFeeds.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetSuggestedFeeds_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetSuggestedFeeds.go:20`




## api/bsky/feedgetTimeline.go


📄 Исходный файл: `api/bsky/feedgetTimeline.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedGetTimeline](#feedgettimeline-apibskyfeedgettimelinego22) `:22`


</details>


[function] name: FeedGetTimeline file: api/bsky/feedgetTimeline.go:22 returns_error: да description: FeedGetTimeline calls the XRPC method "app.bsky.feed.getTimeline".

algorithm: Variant 'algorithm' for timeline. Impleme


### FeedGetTimeline (api/bsky/feedgetTimeline.go:22)


FeedGetTimeline calls the XRPC method "app.bsky.feed.getTimeline".

algorithm: Variant 'algorithm' for timeline. Implementation-specific. NOTE: most feed flexibility has been moved to feed generator mechanism.


```go
func FeedGetTimeline((*FeedGetTimeline_Output, error)) (*FeedGetTimeline_Output, error)
```


**Тип запроса:** FeedGetTimeline_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetTimeline.go`


**Тип ответа:** FeedGetTimeline_Output


```json
{
  "cursor": "string",
  "feed": []
}
```


*Определено в:* `api/bsky/feedgetTimeline.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedGetTimeline_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedgetTimeline.go:22`




## api/bsky/feedlike.go


📄 Исходный файл: `api/bsky/feedlike.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskyfeedlikego12) `:12`


</details>


[function] name: init file: api/bsky/feedlike.go:12 returns_error: нет description: —


### init (api/bsky/feedlike.go:12)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/feedlike.go:12`




## api/bsky/feedpost.go


📄 Исходный файл: `api/bsky/feedpost.go`


<details open>
<summary><b>Функции в этом файле (9)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskyfeedpostgo101) `:101`

- 🔗 [MarshalCBOR](#marshalcbor-apibskyfeedpostgo190) `:190`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeedpostgo50) `:50`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeedpostgo167) `:167`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyfeedpostgo125) `:125`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyfeedpostgo202) `:202`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeedpostgo74) `:74`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeedpostgo175) `:175`

- 🔗 [init](#init-apibskyfeedpostgo18) `:18`


</details>


[function] name: MarshalCBOR file: api/bsky/feedpost.go:101 returns_error: нет description: —


### MarshalCBOR (api/bsky/feedpost.go:101)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPost_Embed) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/feedpost.go:101`



---


[function] name: MarshalCBOR file: api/bsky/feedpost.go:190 returns_error: нет description: —


### MarshalCBOR (api/bsky/feedpost.go:190)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPost_Labels) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/feedpost.go:190`



---


[function] name: MarshalJSON file: api/bsky/feedpost.go:50 returns_error: да description: —


### MarshalJSON (api/bsky/feedpost.go:50)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPost_Embed) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedpost.go:50`



---


[function] name: MarshalJSON file: api/bsky/feedpost.go:167 returns_error: да description: —


### MarshalJSON (api/bsky/feedpost.go:167)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPost_Labels) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedpost.go:167`



---


[function] name: UnmarshalCBOR file: api/bsky/feedpost.go:125 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/feedpost.go:125)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *FeedPost_Embed) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/feedpost.go:125`



---


[function] name: UnmarshalCBOR file: api/bsky/feedpost.go:202 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/feedpost.go:202)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *FeedPost_Labels) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/feedpost.go:202`



---


[function] name: UnmarshalJSON file: api/bsky/feedpost.go:74 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feedpost.go:74)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedPost_Embed) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feedpost.go:74`



---


[function] name: UnmarshalJSON file: api/bsky/feedpost.go:175 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feedpost.go:175)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedPost_Labels) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feedpost.go:175`



---


[function] name: init file: api/bsky/feedpost.go:18 returns_error: нет description: —


### init (api/bsky/feedpost.go:18)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/feedpost.go:18`




## api/bsky/feedpostgate.go


📄 Исходный файл: `api/bsky/feedpostgate.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskyfeedpostgatego66) `:66`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeedpostgatego43) `:43`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyfeedpostgatego78) `:78`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeedpostgatego51) `:51`

- 🔗 [init](#init-apibskyfeedpostgatego17) `:17`


</details>


[function] name: MarshalCBOR file: api/bsky/feedpostgate.go:66 returns_error: нет description: —


### MarshalCBOR (api/bsky/feedpostgate.go:66)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedPostgate_EmbeddingRules_Elem) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/feedpostgate.go:66`



---


[function] name: MarshalJSON file: api/bsky/feedpostgate.go:43 returns_error: да description: —


### MarshalJSON (api/bsky/feedpostgate.go:43)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedPostgate_EmbeddingRules_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedpostgate.go:43`



---


[function] name: UnmarshalCBOR file: api/bsky/feedpostgate.go:78 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/feedpostgate.go:78)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *FeedPostgate_EmbeddingRules_Elem) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/feedpostgate.go:78`



---


[function] name: UnmarshalJSON file: api/bsky/feedpostgate.go:51 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feedpostgate.go:51)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedPostgate_EmbeddingRules_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feedpostgate.go:51`



---


[function] name: init file: api/bsky/feedpostgate.go:17 returns_error: нет description: —


### init (api/bsky/feedpostgate.go:17)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/feedpostgate.go:17`




## api/bsky/feedrepost.go


📄 Исходный файл: `api/bsky/feedrepost.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskyfeedrepostgo12) `:12`


</details>


[function] name: init file: api/bsky/feedrepost.go:12 returns_error: нет description: —


### init (api/bsky/feedrepost.go:12)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/feedrepost.go:12`




## api/bsky/feedsearchPosts.go


📄 Исходный файл: `api/bsky/feedsearchPosts.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedSearchPosts](#feedsearchposts-apibskyfeedsearchpostsgo34) `:34`


</details>


[function] name: FeedSearchPosts file: api/bsky/feedsearchPosts.go:34 returns_error: да description: FeedSearchPosts calls the XRPC method "app.bsky.feed.searchPosts".

author: Filter to posts by the given account. Handle


### FeedSearchPosts (api/bsky/feedsearchPosts.go:34)


FeedSearchPosts calls the XRPC method "app.bsky.feed.searchPosts".

author: Filter to posts by the given account. Handles are resolved to DID before query-time.
cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
domain: Filter to posts with URLs (facet links or embeds) linking to the given domain (hostname). Server may apply hostname normalization.
lang: Filter to posts in the given language. Expected to be based on post language field, though server may override language detection.
mentions: Filter to posts which mention the given account. Handles are resolved to DID before query-time. Only matches rich-text facet mentions.
q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.
since: Filter results for posts after the indicated datetime (inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYYY-MM-DD).
sort: Specifies the ranking order of results.
tag: Filter to posts with the given tag (hashtag), based on rich-text facet or tag field. Do not include the hash (#) prefix. Multiple tags can be specified, with 'AND' matching.
until: Filter results for posts before the indicated datetime (not inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYY-MM-DD).
url: Filter to posts with links (facet links or embeds) pointing to this URL. Server may apply URL normalization or fuzzy matching.


```go
func FeedSearchPosts((*FeedSearchPosts_Output, error)) (*FeedSearchPosts_Output, error)
```


**Тип запроса:** FeedSearchPosts_Output


```json
{
  "cursor": "string",
  "hitsTotal": 0,
  "posts": []
}
```


*Определено в:* `api/bsky/feedsearchPosts.go`


**Тип ответа:** FeedSearchPosts_Output


```json
{
  "cursor": "string",
  "hitsTotal": 0,
  "posts": []
}
```


*Определено в:* `api/bsky/feedsearchPosts.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedSearchPosts_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedsearchPosts.go:34`




## api/bsky/feedsendInteractions.go


📄 Исходный файл: `api/bsky/feedsendInteractions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [FeedSendInteractions](#feedsendinteractions-apibskyfeedsendinteractionsgo23) `:23`


</details>


[function] name: FeedSendInteractions file: api/bsky/feedsendInteractions.go:23 returns_error: да description: FeedSendInteractions calls the XRPC method "app.bsky.feed.sendInteractions".


### FeedSendInteractions (api/bsky/feedsendInteractions.go:23)


FeedSendInteractions calls the XRPC method "app.bsky.feed.sendInteractions".


```go
func FeedSendInteractions((*FeedSendInteractions_Output, error)) (*FeedSendInteractions_Output, error)
```


**Тип запроса:** FeedSendInteractions_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** FeedSendInteractions_Output


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*FeedSendInteractions_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedsendInteractions.go:23`




## api/bsky/feedthreadgate.go


📄 Исходный файл: `api/bsky/feedthreadgate.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskyfeedthreadgatego83) `:83`

- 🔗 [MarshalJSON](#marshaljson-apibskyfeedthreadgatego39) `:39`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyfeedthreadgatego104) `:104`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyfeedthreadgatego59) `:59`

- 🔗 [init](#init-apibskyfeedthreadgatego17) `:17`


</details>


[function] name: MarshalCBOR file: api/bsky/feedthreadgate.go:83 returns_error: нет description: —


### MarshalCBOR (api/bsky/feedthreadgate.go:83)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *FeedThreadgate_Allow_Elem) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/feedthreadgate.go:83`



---


[function] name: MarshalJSON file: api/bsky/feedthreadgate.go:39 returns_error: да description: —


### MarshalJSON (api/bsky/feedthreadgate.go:39)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *FeedThreadgate_Allow_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/feedthreadgate.go:39`



---


[function] name: UnmarshalCBOR file: api/bsky/feedthreadgate.go:104 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/feedthreadgate.go:104)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *FeedThreadgate_Allow_Elem) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/feedthreadgate.go:104`



---


[function] name: UnmarshalJSON file: api/bsky/feedthreadgate.go:59 returns_error: нет description: —


### UnmarshalJSON (api/bsky/feedthreadgate.go:59)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *FeedThreadgate_Allow_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/feedthreadgate.go:59`



---


[function] name: init file: api/bsky/feedthreadgate.go:17 returns_error: нет description: —


### init (api/bsky/feedthreadgate.go:17)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/feedthreadgate.go:17`




## api/bsky/graphblock.go


📄 Исходный файл: `api/bsky/graphblock.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskygraphblockgo11) `:11`


</details>


[function] name: init file: api/bsky/graphblock.go:11 returns_error: нет description: —


### init (api/bsky/graphblock.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/graphblock.go:11`




## api/bsky/graphfollow.go


📄 Исходный файл: `api/bsky/graphfollow.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskygraphfollowgo12) `:12`


</details>


[function] name: init file: api/bsky/graphfollow.go:12 returns_error: нет description: —


### init (api/bsky/graphfollow.go:12)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/graphfollow.go:12`




## api/bsky/graphgetActorStarterPacks.go


📄 Исходный файл: `api/bsky/graphgetActorStarterPacks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetActorStarterPacks](#graphgetactorstarterpacks-apibskygraphgetactorstarterpacksgo20) `:20`


</details>


[function] name: GraphGetActorStarterPacks file: api/bsky/graphgetActorStarterPacks.go:20 returns_error: да description: GraphGetActorStarterPacks calls the XRPC method "app.bsky.graph.getActorStarterPacks".


### GraphGetActorStarterPacks (api/bsky/graphgetActorStarterPacks.go:20)


GraphGetActorStarterPacks calls the XRPC method "app.bsky.graph.getActorStarterPacks".


```go
func GraphGetActorStarterPacks((*GraphGetActorStarterPacks_Output, error)) (*GraphGetActorStarterPacks_Output, error)
```


**Тип запроса:** GraphGetActorStarterPacks_Output


```json
{
  "cursor": "string",
  "starterPacks": []
}
```


*Определено в:* `api/bsky/graphgetActorStarterPacks.go`


**Тип ответа:** GraphGetActorStarterPacks_Output


```json
{
  "cursor": "string",
  "starterPacks": []
}
```


*Определено в:* `api/bsky/graphgetActorStarterPacks.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetActorStarterPacks_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetActorStarterPacks.go:20`




## api/bsky/graphgetBlocks.go


📄 Исходный файл: `api/bsky/graphgetBlocks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetBlocks](#graphgetblocks-apibskygraphgetblocksgo20) `:20`


</details>


[function] name: GraphGetBlocks file: api/bsky/graphgetBlocks.go:20 returns_error: да description: GraphGetBlocks calls the XRPC method "app.bsky.graph.getBlocks".


### GraphGetBlocks (api/bsky/graphgetBlocks.go:20)


GraphGetBlocks calls the XRPC method "app.bsky.graph.getBlocks".


```go
func GraphGetBlocks((*GraphGetBlocks_Output, error)) (*GraphGetBlocks_Output, error)
```


**Тип запроса:** GraphGetBlocks_Output


```json
{
  "blocks": [],
  "cursor": "string"
}
```


*Определено в:* `api/bsky/graphgetBlocks.go`


**Тип ответа:** GraphGetBlocks_Output


```json
{
  "blocks": [],
  "cursor": "string"
}
```


*Определено в:* `api/bsky/graphgetBlocks.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetBlocks_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetBlocks.go:20`




## api/bsky/graphgetFollowers.go


📄 Исходный файл: `api/bsky/graphgetFollowers.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetFollowers](#graphgetfollowers-apibskygraphgetfollowersgo21) `:21`


</details>


[function] name: GraphGetFollowers file: api/bsky/graphgetFollowers.go:21 returns_error: да description: GraphGetFollowers calls the XRPC method "app.bsky.graph.getFollowers".


### GraphGetFollowers (api/bsky/graphgetFollowers.go:21)


GraphGetFollowers calls the XRPC method "app.bsky.graph.getFollowers".


```go
func GraphGetFollowers((*GraphGetFollowers_Output, error)) (*GraphGetFollowers_Output, error)
```


**Тип запроса:** GraphGetFollowers_Output


```json
{
  "cursor": "string",
  "followers": [],
  "subject": null
}
```


*Определено в:* `api/bsky/graphgetFollowers.go`


**Тип ответа:** GraphGetFollowers_Output


```json
{
  "cursor": "string",
  "followers": [],
  "subject": null
}
```


*Определено в:* `api/bsky/graphgetFollowers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetFollowers_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetFollowers.go:21`




## api/bsky/graphgetFollows.go


📄 Исходный файл: `api/bsky/graphgetFollows.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetFollows](#graphgetfollows-apibskygraphgetfollowsgo21) `:21`


</details>


[function] name: GraphGetFollows file: api/bsky/graphgetFollows.go:21 returns_error: да description: GraphGetFollows calls the XRPC method "app.bsky.graph.getFollows".


### GraphGetFollows (api/bsky/graphgetFollows.go:21)


GraphGetFollows calls the XRPC method "app.bsky.graph.getFollows".


```go
func GraphGetFollows((*GraphGetFollows_Output, error)) (*GraphGetFollows_Output, error)
```


**Тип запроса:** GraphGetFollows_Output


```json
{
  "cursor": "string",
  "follows": [],
  "subject": null
}
```


*Определено в:* `api/bsky/graphgetFollows.go`


**Тип ответа:** GraphGetFollows_Output


```json
{
  "cursor": "string",
  "follows": [],
  "subject": null
}
```


*Определено в:* `api/bsky/graphgetFollows.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetFollows_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetFollows.go:21`




## api/bsky/graphgetKnownFollowers.go


📄 Исходный файл: `api/bsky/graphgetKnownFollowers.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetKnownFollowers](#graphgetknownfollowers-apibskygraphgetknownfollowersgo21) `:21`


</details>


[function] name: GraphGetKnownFollowers file: api/bsky/graphgetKnownFollowers.go:21 returns_error: да description: GraphGetKnownFollowers calls the XRPC method "app.bsky.graph.getKnownFollowers".


### GraphGetKnownFollowers (api/bsky/graphgetKnownFollowers.go:21)


GraphGetKnownFollowers calls the XRPC method "app.bsky.graph.getKnownFollowers".


```go
func GraphGetKnownFollowers((*GraphGetKnownFollowers_Output, error)) (*GraphGetKnownFollowers_Output, error)
```


**Тип запроса:** GraphGetKnownFollowers_Output


```json
{
  "cursor": "string",
  "followers": [],
  "subject": null
}
```


*Определено в:* `api/bsky/graphgetKnownFollowers.go`


**Тип ответа:** GraphGetKnownFollowers_Output


```json
{
  "cursor": "string",
  "followers": [],
  "subject": null
}
```


*Определено в:* `api/bsky/graphgetKnownFollowers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetKnownFollowers_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetKnownFollowers.go:21`




## api/bsky/graphgetList.go


📄 Исходный файл: `api/bsky/graphgetList.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetList](#graphgetlist-apibskygraphgetlistgo23) `:23`


</details>


[function] name: GraphGetList file: api/bsky/graphgetList.go:23 returns_error: да description: GraphGetList calls the XRPC method "app.bsky.graph.getList".

list: Reference (AT-URI) of the list record to hydrate.


### GraphGetList (api/bsky/graphgetList.go:23)


GraphGetList calls the XRPC method "app.bsky.graph.getList".

list: Reference (AT-URI) of the list record to hydrate.


```go
func GraphGetList((*GraphGetList_Output, error)) (*GraphGetList_Output, error)
```


**Тип запроса:** GraphGetList_Output


```json
{
  "cursor": "string",
  "items": [],
  "list": null
}
```


*Определено в:* `api/bsky/graphgetList.go`


**Тип ответа:** GraphGetList_Output


```json
{
  "cursor": "string",
  "items": [],
  "list": null
}
```


*Определено в:* `api/bsky/graphgetList.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetList_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetList.go:23`




## api/bsky/graphgetListBlocks.go


📄 Исходный файл: `api/bsky/graphgetListBlocks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetListBlocks](#graphgetlistblocks-apibskygraphgetlistblocksgo20) `:20`


</details>


[function] name: GraphGetListBlocks file: api/bsky/graphgetListBlocks.go:20 returns_error: да description: GraphGetListBlocks calls the XRPC method "app.bsky.graph.getListBlocks".


### GraphGetListBlocks (api/bsky/graphgetListBlocks.go:20)


GraphGetListBlocks calls the XRPC method "app.bsky.graph.getListBlocks".


```go
func GraphGetListBlocks((*GraphGetListBlocks_Output, error)) (*GraphGetListBlocks_Output, error)
```


**Тип запроса:** GraphGetListBlocks_Output


```json
{
  "cursor": "string",
  "lists": []
}
```


*Определено в:* `api/bsky/graphgetListBlocks.go`


**Тип ответа:** GraphGetListBlocks_Output


```json
{
  "cursor": "string",
  "lists": []
}
```


*Определено в:* `api/bsky/graphgetListBlocks.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetListBlocks_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetListBlocks.go:20`




## api/bsky/graphgetListMutes.go


📄 Исходный файл: `api/bsky/graphgetListMutes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetListMutes](#graphgetlistmutes-apibskygraphgetlistmutesgo20) `:20`


</details>


[function] name: GraphGetListMutes file: api/bsky/graphgetListMutes.go:20 returns_error: да description: GraphGetListMutes calls the XRPC method "app.bsky.graph.getListMutes".


### GraphGetListMutes (api/bsky/graphgetListMutes.go:20)


GraphGetListMutes calls the XRPC method "app.bsky.graph.getListMutes".


```go
func GraphGetListMutes((*GraphGetListMutes_Output, error)) (*GraphGetListMutes_Output, error)
```


**Тип запроса:** GraphGetListMutes_Output


```json
{
  "cursor": "string",
  "lists": []
}
```


*Определено в:* `api/bsky/graphgetListMutes.go`


**Тип ответа:** GraphGetListMutes_Output


```json
{
  "cursor": "string",
  "lists": []
}
```


*Определено в:* `api/bsky/graphgetListMutes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetListMutes_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetListMutes.go:20`




## api/bsky/graphgetLists.go


📄 Исходный файл: `api/bsky/graphgetLists.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetLists](#graphgetlists-apibskygraphgetlistsgo23) `:23`


</details>


[function] name: GraphGetLists file: api/bsky/graphgetLists.go:23 returns_error: да description: GraphGetLists calls the XRPC method "app.bsky.graph.getLists".

actor: The account (actor) to enumerate lists from.
purp


### GraphGetLists (api/bsky/graphgetLists.go:23)


GraphGetLists calls the XRPC method "app.bsky.graph.getLists".

actor: The account (actor) to enumerate lists from.
purposes: Optional filter by list purpose. If not specified, all supported types are returned.


```go
func GraphGetLists((*GraphGetLists_Output, error)) (*GraphGetLists_Output, error)
```


**Тип запроса:** GraphGetLists_Output


```json
{
  "cursor": "string",
  "lists": []
}
```


*Определено в:* `api/bsky/graphgetLists.go`


**Тип ответа:** GraphGetLists_Output


```json
{
  "cursor": "string",
  "lists": []
}
```


*Определено в:* `api/bsky/graphgetLists.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetLists_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetLists.go:23`




## api/bsky/graphgetListsWithMembership.go


📄 Исходный файл: `api/bsky/graphgetListsWithMembership.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetListsWithMembership](#graphgetlistswithmembership-apibskygraphgetlistswithmembershipgo31) `:31`


</details>


[function] name: GraphGetListsWithMembership file: api/bsky/graphgetListsWithMembership.go:31 returns_error: да description: GraphGetListsWithMembership calls the XRPC method "app.bsky.graph.getListsWithMembership".

actor: The account (actor) t


### GraphGetListsWithMembership (api/bsky/graphgetListsWithMembership.go:31)


GraphGetListsWithMembership calls the XRPC method "app.bsky.graph.getListsWithMembership".

actor: The account (actor) to check for membership.
purposes: Optional filter by list purpose. If not specified, all supported types are returned.


```go
func GraphGetListsWithMembership((*GraphGetListsWithMembership_Output, error)) (*GraphGetListsWithMembership_Output, error)
```


**Тип запроса:** GraphGetListsWithMembership_Output


```json
{
  "cursor": "string",
  "listsWithMembership": []
}
```


*Определено в:* `api/bsky/graphgetListsWithMembership.go`


**Тип ответа:** GraphGetListsWithMembership_Output


```json
{
  "cursor": "string",
  "listsWithMembership": []
}
```


*Определено в:* `api/bsky/graphgetListsWithMembership.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetListsWithMembership_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetListsWithMembership.go:31`




## api/bsky/graphgetMutes.go


📄 Исходный файл: `api/bsky/graphgetMutes.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetMutes](#graphgetmutes-apibskygraphgetmutesgo20) `:20`


</details>


[function] name: GraphGetMutes file: api/bsky/graphgetMutes.go:20 returns_error: да description: GraphGetMutes calls the XRPC method "app.bsky.graph.getMutes".


### GraphGetMutes (api/bsky/graphgetMutes.go:20)


GraphGetMutes calls the XRPC method "app.bsky.graph.getMutes".


```go
func GraphGetMutes((*GraphGetMutes_Output, error)) (*GraphGetMutes_Output, error)
```


**Тип запроса:** GraphGetMutes_Output


```json
{
  "cursor": "string",
  "mutes": []
}
```


*Определено в:* `api/bsky/graphgetMutes.go`


**Тип ответа:** GraphGetMutes_Output


```json
{
  "cursor": "string",
  "mutes": []
}
```


*Определено в:* `api/bsky/graphgetMutes.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetMutes_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetMutes.go:20`




## api/bsky/graphgetRelationships.go


📄 Исходный файл: `api/bsky/graphgetRelationships.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [GraphGetRelationships](#graphgetrelationships-apibskygraphgetrelationshipsgo60) `:60`

- 🔗 [MarshalJSON](#marshaljson-apibskygraphgetrelationshipsgo26) `:26`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskygraphgetrelationshipsgo38) `:38`


</details>


[function] name: GraphGetRelationships file: api/bsky/graphgetRelationships.go:60 returns_error: да description: GraphGetRelationships calls the XRPC method "app.bsky.graph.getRelationships".

actor: Primary account requesting relati


### GraphGetRelationships (api/bsky/graphgetRelationships.go:60)


GraphGetRelationships calls the XRPC method "app.bsky.graph.getRelationships".

actor: Primary account requesting relationships for.
others: List of 'other' accounts to be related back to the primary.


```go
func GraphGetRelationships((*GraphGetRelationships_Output, error)) (*GraphGetRelationships_Output, error)
```


**Тип запроса:** GraphGetRelationships_Output


```json
{
  "actor": "string",
  "relationships": []
}
```


*Определено в:* `api/bsky/graphgetRelationships.go`


**Тип ответа:** GraphGetRelationships_Output


```json
{
  "actor": "string",
  "relationships": []
}
```


*Определено в:* `api/bsky/graphgetRelationships.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetRelationships_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetRelationships.go:60`



---


[function] name: MarshalJSON file: api/bsky/graphgetRelationships.go:26 returns_error: да description: —


### MarshalJSON (api/bsky/graphgetRelationships.go:26)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphGetRelationships_Output_Relationships_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetRelationships.go:26`



---


[function] name: UnmarshalJSON file: api/bsky/graphgetRelationships.go:38 returns_error: нет description: —


### UnmarshalJSON (api/bsky/graphgetRelationships.go:38)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *GraphGetRelationships_Output_Relationships_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/graphgetRelationships.go:38`




## api/bsky/graphgetStarterPack.go


📄 Исходный файл: `api/bsky/graphgetStarterPack.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetStarterPack](#graphgetstarterpack-apibskygraphgetstarterpackgo21) `:21`


</details>


[function] name: GraphGetStarterPack file: api/bsky/graphgetStarterPack.go:21 returns_error: да description: GraphGetStarterPack calls the XRPC method "app.bsky.graph.getStarterPack".

starterPack: Reference (AT-URI) of the start


### GraphGetStarterPack (api/bsky/graphgetStarterPack.go:21)


GraphGetStarterPack calls the XRPC method "app.bsky.graph.getStarterPack".

starterPack: Reference (AT-URI) of the starter pack record.


```go
func GraphGetStarterPack((*GraphGetStarterPack_Output, error)) (*GraphGetStarterPack_Output, error)
```


**Тип запроса:** GraphGetStarterPack_Output


```json
{
  "starterPack": null
}
```


*Определено в:* `api/bsky/graphgetStarterPack.go`


**Тип ответа:** GraphGetStarterPack_Output


```json
{
  "starterPack": null
}
```


*Определено в:* `api/bsky/graphgetStarterPack.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetStarterPack_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetStarterPack.go:21`




## api/bsky/graphgetStarterPacks.go


📄 Исходный файл: `api/bsky/graphgetStarterPacks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetStarterPacks](#graphgetstarterpacks-apibskygraphgetstarterpacksgo19) `:19`


</details>


[function] name: GraphGetStarterPacks file: api/bsky/graphgetStarterPacks.go:19 returns_error: да description: GraphGetStarterPacks calls the XRPC method "app.bsky.graph.getStarterPacks".


### GraphGetStarterPacks (api/bsky/graphgetStarterPacks.go:19)


GraphGetStarterPacks calls the XRPC method "app.bsky.graph.getStarterPacks".


```go
func GraphGetStarterPacks((*GraphGetStarterPacks_Output, error)) (*GraphGetStarterPacks_Output, error)
```


**Тип запроса:** GraphGetStarterPacks_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/graphgetStarterPacks.go`


**Тип ответа:** GraphGetStarterPacks_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/graphgetStarterPacks.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetStarterPacks_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetStarterPacks.go:19`




## api/bsky/graphgetStarterPacksWithMembership.go


📄 Исходный файл: `api/bsky/graphgetStarterPacksWithMembership.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetStarterPacksWithMembership](#graphgetstarterpackswithmembership-apibskygraphgetstarterpackswithmembershipgo30) `:30`


</details>


[function] name: GraphGetStarterPacksWithMembership file: api/bsky/graphgetStarterPacksWithMembership.go:30 returns_error: да description: GraphGetStarterPacksWithMembership calls the XRPC method "app.bsky.graph.getStarterPacksWithMembership".

actor: The acc


### GraphGetStarterPacksWithMembership (api/bsky/graphgetStarterPacksWithMembership.go:30)


GraphGetStarterPacksWithMembership calls the XRPC method "app.bsky.graph.getStarterPacksWithMembership".

actor: The account (actor) to check for membership.


```go
func GraphGetStarterPacksWithMembership((*GraphGetStarterPacksWithMembership_Output, error)) (*GraphGetStarterPacksWithMembership_Output, error)
```


**Тип запроса:** GraphGetStarterPacksWithMembership_Output


```json
{
  "cursor": "string",
  "starterPacksWithMembership": []
}
```


*Определено в:* `api/bsky/graphgetStarterPacksWithMembership.go`


**Тип ответа:** GraphGetStarterPacksWithMembership_Output


```json
{
  "cursor": "string",
  "starterPacksWithMembership": []
}
```


*Определено в:* `api/bsky/graphgetStarterPacksWithMembership.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetStarterPacksWithMembership_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetStarterPacksWithMembership.go:30`




## api/bsky/graphgetSuggestedFollowsByActor.go


📄 Исходный файл: `api/bsky/graphgetSuggestedFollowsByActor.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphGetSuggestedFollowsByActor](#graphgetsuggestedfollowsbyactor-apibskygraphgetsuggestedfollowsbyactorgo25) `:25`


</details>


[function] name: GraphGetSuggestedFollowsByActor file: api/bsky/graphgetSuggestedFollowsByActor.go:25 returns_error: да description: GraphGetSuggestedFollowsByActor calls the XRPC method "app.bsky.graph.getSuggestedFollowsByActor".


### GraphGetSuggestedFollowsByActor (api/bsky/graphgetSuggestedFollowsByActor.go:25)


GraphGetSuggestedFollowsByActor calls the XRPC method "app.bsky.graph.getSuggestedFollowsByActor".


```go
func GraphGetSuggestedFollowsByActor((*GraphGetSuggestedFollowsByActor_Output, error)) (*GraphGetSuggestedFollowsByActor_Output, error)
```


**Тип запроса:** GraphGetSuggestedFollowsByActor_Output


```json
{
  "isFallback": false,
  "recId": 0,
  "recIdStr": "string",
  "suggestions": []
}
```


*Определено в:* `api/bsky/graphgetSuggestedFollowsByActor.go`


**Тип ответа:** GraphGetSuggestedFollowsByActor_Output


```json
{
  "isFallback": false,
  "recId": 0,
  "recIdStr": "string",
  "suggestions": []
}
```


*Определено в:* `api/bsky/graphgetSuggestedFollowsByActor.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphGetSuggestedFollowsByActor_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphgetSuggestedFollowsByActor.go:25`




## api/bsky/graphlist.go


📄 Исходный файл: `api/bsky/graphlist.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskygraphlistgo62) `:62`

- 🔗 [MarshalJSON](#marshaljson-apibskygraphlistgo39) `:39`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskygraphlistgo74) `:74`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskygraphlistgo47) `:47`

- 🔗 [init](#init-apibskygraphlistgo18) `:18`


</details>


[function] name: MarshalCBOR file: api/bsky/graphlist.go:62 returns_error: нет description: —


### MarshalCBOR (api/bsky/graphlist.go:62)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *GraphList_Labels) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/graphlist.go:62`



---


[function] name: MarshalJSON file: api/bsky/graphlist.go:39 returns_error: да description: —


### MarshalJSON (api/bsky/graphlist.go:39)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *GraphList_Labels) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphlist.go:39`



---


[function] name: UnmarshalCBOR file: api/bsky/graphlist.go:74 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/graphlist.go:74)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *GraphList_Labels) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/graphlist.go:74`



---


[function] name: UnmarshalJSON file: api/bsky/graphlist.go:47 returns_error: нет description: —


### UnmarshalJSON (api/bsky/graphlist.go:47)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *GraphList_Labels) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/graphlist.go:47`



---


[function] name: init file: api/bsky/graphlist.go:18 returns_error: нет description: —


### init (api/bsky/graphlist.go:18)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/graphlist.go:18`




## api/bsky/graphlistblock.go


📄 Исходный файл: `api/bsky/graphlistblock.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskygraphlistblockgo11) `:11`


</details>


[function] name: init file: api/bsky/graphlistblock.go:11 returns_error: нет description: —


### init (api/bsky/graphlistblock.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/graphlistblock.go:11`




## api/bsky/graphlistitem.go


📄 Исходный файл: `api/bsky/graphlistitem.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskygraphlistitemgo11) `:11`


</details>


[function] name: init file: api/bsky/graphlistitem.go:11 returns_error: нет description: —


### init (api/bsky/graphlistitem.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/graphlistitem.go:11`




## api/bsky/graphmuteActor.go


📄 Исходный файл: `api/bsky/graphmuteActor.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphMuteActor](#graphmuteactor-apibskygraphmuteactorgo19) `:19`


</details>


[function] name: GraphMuteActor file: api/bsky/graphmuteActor.go:19 returns_error: нет description: GraphMuteActor calls the XRPC method "app.bsky.graph.muteActor".


### GraphMuteActor (api/bsky/graphmuteActor.go:19)


GraphMuteActor calls the XRPC method "app.bsky.graph.muteActor".


```go
func GraphMuteActor((ctx context.Context, c lexutil.LexClient, input *GraphMuteActor_Input)) (ctx context.Context, c lexutil.LexClient, input *GraphMuteActor_Input)
```


**Тип запроса:** GraphMuteActor_Input


```json
{
  "actor": "string"
}
```


*Определено в:* `api/bsky/graphmuteActor.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GraphMuteActor_Input


```json
{
  "actor": "string"
}
```


*Определено в:* `api/bsky/graphmuteActor.go`


📍 *Расположение:* `api/bsky/graphmuteActor.go:19`




## api/bsky/graphmuteActorList.go


📄 Исходный файл: `api/bsky/graphmuteActorList.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphMuteActorList](#graphmuteactorlist-apibskygraphmuteactorlistgo19) `:19`


</details>


[function] name: GraphMuteActorList file: api/bsky/graphmuteActorList.go:19 returns_error: нет description: GraphMuteActorList calls the XRPC method "app.bsky.graph.muteActorList".


### GraphMuteActorList (api/bsky/graphmuteActorList.go:19)


GraphMuteActorList calls the XRPC method "app.bsky.graph.muteActorList".


```go
func GraphMuteActorList((ctx context.Context, c lexutil.LexClient, input *GraphMuteActorList_Input)) (ctx context.Context, c lexutil.LexClient, input *GraphMuteActorList_Input)
```


**Тип запроса:** GraphMuteActorList_Input


```json
{
  "list": "string"
}
```


*Определено в:* `api/bsky/graphmuteActorList.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GraphMuteActorList_Input


```json
{
  "list": "string"
}
```


*Определено в:* `api/bsky/graphmuteActorList.go`


📍 *Расположение:* `api/bsky/graphmuteActorList.go:19`




## api/bsky/graphmuteThread.go


📄 Исходный файл: `api/bsky/graphmuteThread.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphMuteThread](#graphmutethread-apibskygraphmutethreadgo19) `:19`


</details>


[function] name: GraphMuteThread file: api/bsky/graphmuteThread.go:19 returns_error: нет description: GraphMuteThread calls the XRPC method "app.bsky.graph.muteThread".


### GraphMuteThread (api/bsky/graphmuteThread.go:19)


GraphMuteThread calls the XRPC method "app.bsky.graph.muteThread".


```go
func GraphMuteThread((ctx context.Context, c lexutil.LexClient, input *GraphMuteThread_Input)) (ctx context.Context, c lexutil.LexClient, input *GraphMuteThread_Input)
```


**Тип запроса:** GraphMuteThread_Input


```json
{
  "root": "string"
}
```


*Определено в:* `api/bsky/graphmuteThread.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GraphMuteThread_Input


```json
{
  "root": "string"
}
```


*Определено в:* `api/bsky/graphmuteThread.go`


📍 *Расположение:* `api/bsky/graphmuteThread.go:19`




## api/bsky/graphsearchStarterPacks.go


📄 Исходный файл: `api/bsky/graphsearchStarterPacks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphSearchStarterPacks](#graphsearchstarterpacks-apibskygraphsearchstarterpacksgo22) `:22`


</details>


[function] name: GraphSearchStarterPacks file: api/bsky/graphsearchStarterPacks.go:22 returns_error: да description: GraphSearchStarterPacks calls the XRPC method "app.bsky.graph.searchStarterPacks".

q: Search query string. Syntax, phra


### GraphSearchStarterPacks (api/bsky/graphsearchStarterPacks.go:22)


GraphSearchStarterPacks calls the XRPC method "app.bsky.graph.searchStarterPacks".

q: Search query string. Syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.


```go
func GraphSearchStarterPacks((*GraphSearchStarterPacks_Output, error)) (*GraphSearchStarterPacks_Output, error)
```


**Тип запроса:** GraphSearchStarterPacks_Output


```json
{
  "cursor": "string",
  "starterPacks": []
}
```


*Определено в:* `api/bsky/graphsearchStarterPacks.go`


**Тип ответа:** GraphSearchStarterPacks_Output


```json
{
  "cursor": "string",
  "starterPacks": []
}
```


*Определено в:* `api/bsky/graphsearchStarterPacks.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*GraphSearchStarterPacks_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/graphsearchStarterPacks.go:22`




## api/bsky/graphstarterpack.go


📄 Исходный файл: `api/bsky/graphstarterpack.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskygraphstarterpackgo11) `:11`


</details>


[function] name: init file: api/bsky/graphstarterpack.go:11 returns_error: нет description: —


### init (api/bsky/graphstarterpack.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/graphstarterpack.go:11`




## api/bsky/graphunmuteActor.go


📄 Исходный файл: `api/bsky/graphunmuteActor.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphUnmuteActor](#graphunmuteactor-apibskygraphunmuteactorgo19) `:19`


</details>


[function] name: GraphUnmuteActor file: api/bsky/graphunmuteActor.go:19 returns_error: нет description: GraphUnmuteActor calls the XRPC method "app.bsky.graph.unmuteActor".


### GraphUnmuteActor (api/bsky/graphunmuteActor.go:19)


GraphUnmuteActor calls the XRPC method "app.bsky.graph.unmuteActor".


```go
func GraphUnmuteActor((ctx context.Context, c lexutil.LexClient, input *GraphUnmuteActor_Input)) (ctx context.Context, c lexutil.LexClient, input *GraphUnmuteActor_Input)
```


**Тип запроса:** GraphUnmuteActor_Input


```json
{
  "actor": "string"
}
```


*Определено в:* `api/bsky/graphunmuteActor.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GraphUnmuteActor_Input


```json
{
  "actor": "string"
}
```


*Определено в:* `api/bsky/graphunmuteActor.go`


📍 *Расположение:* `api/bsky/graphunmuteActor.go:19`




## api/bsky/graphunmuteActorList.go


📄 Исходный файл: `api/bsky/graphunmuteActorList.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphUnmuteActorList](#graphunmuteactorlist-apibskygraphunmuteactorlistgo19) `:19`


</details>


[function] name: GraphUnmuteActorList file: api/bsky/graphunmuteActorList.go:19 returns_error: нет description: GraphUnmuteActorList calls the XRPC method "app.bsky.graph.unmuteActorList".


### GraphUnmuteActorList (api/bsky/graphunmuteActorList.go:19)


GraphUnmuteActorList calls the XRPC method "app.bsky.graph.unmuteActorList".


```go
func GraphUnmuteActorList((ctx context.Context, c lexutil.LexClient, input *GraphUnmuteActorList_Input)) (ctx context.Context, c lexutil.LexClient, input *GraphUnmuteActorList_Input)
```


**Тип запроса:** GraphUnmuteActorList_Input


```json
{
  "list": "string"
}
```


*Определено в:* `api/bsky/graphunmuteActorList.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GraphUnmuteActorList_Input


```json
{
  "list": "string"
}
```


*Определено в:* `api/bsky/graphunmuteActorList.go`


📍 *Расположение:* `api/bsky/graphunmuteActorList.go:19`




## api/bsky/graphunmuteThread.go


📄 Исходный файл: `api/bsky/graphunmuteThread.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [GraphUnmuteThread](#graphunmutethread-apibskygraphunmutethreadgo19) `:19`


</details>


[function] name: GraphUnmuteThread file: api/bsky/graphunmuteThread.go:19 returns_error: нет description: GraphUnmuteThread calls the XRPC method "app.bsky.graph.unmuteThread".


### GraphUnmuteThread (api/bsky/graphunmuteThread.go:19)


GraphUnmuteThread calls the XRPC method "app.bsky.graph.unmuteThread".


```go
func GraphUnmuteThread((ctx context.Context, c lexutil.LexClient, input *GraphUnmuteThread_Input)) (ctx context.Context, c lexutil.LexClient, input *GraphUnmuteThread_Input)
```


**Тип запроса:** GraphUnmuteThread_Input


```json
{
  "root": "string"
}
```


*Определено в:* `api/bsky/graphunmuteThread.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** GraphUnmuteThread_Input


```json
{
  "root": "string"
}
```


*Определено в:* `api/bsky/graphunmuteThread.go`


📍 *Расположение:* `api/bsky/graphunmuteThread.go:19`




## api/bsky/graphverification.go


📄 Исходный файл: `api/bsky/graphverification.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskygraphverificationgo11) `:11`


</details>


[function] name: init file: api/bsky/graphverification.go:11 returns_error: нет description: —


### init (api/bsky/graphverification.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/graphverification.go:11`




## api/bsky/labelergetServices.go


📄 Исходный файл: `api/bsky/labelergetServices.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [LabelerGetServices](#labelergetservices-apibskylabelergetservicesgo56) `:56`

- 🔗 [MarshalJSON](#marshaljson-apibskylabelergetservicesgo25) `:25`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskylabelergetservicesgo37) `:37`


</details>


[function] name: LabelerGetServices file: api/bsky/labelergetServices.go:56 returns_error: да description: LabelerGetServices calls the XRPC method "app.bsky.labeler.getServices".


### LabelerGetServices (api/bsky/labelergetServices.go:56)


LabelerGetServices calls the XRPC method "app.bsky.labeler.getServices".


```go
func LabelerGetServices((*LabelerGetServices_Output, error)) (*LabelerGetServices_Output, error)
```


**Тип запроса:** LabelerGetServices_Output


```json
{
  "views": []
}
```


*Определено в:* `api/bsky/labelergetServices.go`


**Тип ответа:** LabelerGetServices_Output


```json
{
  "views": []
}
```


*Определено в:* `api/bsky/labelergetServices.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*LabelerGetServices_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/labelergetServices.go:56`



---


[function] name: MarshalJSON file: api/bsky/labelergetServices.go:25 returns_error: да description: —


### MarshalJSON (api/bsky/labelergetServices.go:25)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelerGetServices_Output_Views_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/labelergetServices.go:25`



---


[function] name: UnmarshalJSON file: api/bsky/labelergetServices.go:37 returns_error: нет description: —


### UnmarshalJSON (api/bsky/labelergetServices.go:37)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *LabelerGetServices_Output_Views_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/labelergetServices.go:37`




## api/bsky/labelerservice.go


📄 Исходный файл: `api/bsky/labelerservice.go`


<details open>
<summary><b>Функции в этом файле (5)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskylabelerservicego62) `:62`

- 🔗 [MarshalJSON](#marshaljson-apibskylabelerservicego39) `:39`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskylabelerservicego74) `:74`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskylabelerservicego47) `:47`

- 🔗 [init](#init-apibskylabelerservicego18) `:18`


</details>


[function] name: MarshalCBOR file: api/bsky/labelerservice.go:62 returns_error: нет description: —


### MarshalCBOR (api/bsky/labelerservice.go:62)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *LabelerService_Labels) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/labelerservice.go:62`



---


[function] name: MarshalJSON file: api/bsky/labelerservice.go:39 returns_error: да description: —


### MarshalJSON (api/bsky/labelerservice.go:39)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *LabelerService_Labels) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/labelerservice.go:39`



---


[function] name: UnmarshalCBOR file: api/bsky/labelerservice.go:74 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/labelerservice.go:74)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *LabelerService_Labels) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/labelerservice.go:74`



---


[function] name: UnmarshalJSON file: api/bsky/labelerservice.go:47 returns_error: нет description: —


### UnmarshalJSON (api/bsky/labelerservice.go:47)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *LabelerService_Labels) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/labelerservice.go:47`



---


[function] name: init file: api/bsky/labelerservice.go:18 returns_error: нет description: —


### init (api/bsky/labelerservice.go:18)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/labelerservice.go:18`




## api/bsky/notificationdeclaration.go


📄 Исходный файл: `api/bsky/notificationdeclaration.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [init](#init-apibskynotificationdeclarationgo11) `:11`


</details>


[function] name: init file: api/bsky/notificationdeclaration.go:11 returns_error: нет description: —


### init (api/bsky/notificationdeclaration.go:11)


init is a function that performs operations based on the provided parameters and returns ().


```go
func init(()) ()
```


📍 *Расположение:* `api/bsky/notificationdeclaration.go:11`




## api/bsky/notificationgetPreferences.go


📄 Исходный файл: `api/bsky/notificationgetPreferences.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationGetPreferences](#notificationgetpreferences-apibskynotificationgetpreferencesgo19) `:19`


</details>


[function] name: NotificationGetPreferences file: api/bsky/notificationgetPreferences.go:19 returns_error: да description: NotificationGetPreferences calls the XRPC method "app.bsky.notification.getPreferences".


### NotificationGetPreferences (api/bsky/notificationgetPreferences.go:19)


NotificationGetPreferences calls the XRPC method "app.bsky.notification.getPreferences".


```go
func NotificationGetPreferences((*NotificationGetPreferences_Output, error)) (*NotificationGetPreferences_Output, error)
```


**Тип запроса:** NotificationGetPreferences_Output


```json
{
  "preferences": null
}
```


*Определено в:* `api/bsky/notificationgetPreferences.go`


**Тип ответа:** NotificationGetPreferences_Output


```json
{
  "preferences": null
}
```


*Определено в:* `api/bsky/notificationgetPreferences.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NotificationGetPreferences_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/notificationgetPreferences.go:19`




## api/bsky/notificationgetUnreadCount.go


📄 Исходный файл: `api/bsky/notificationgetUnreadCount.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationGetUnreadCount](#notificationgetunreadcount-apibskynotificationgetunreadcountgo19) `:19`


</details>


[function] name: NotificationGetUnreadCount file: api/bsky/notificationgetUnreadCount.go:19 returns_error: да description: NotificationGetUnreadCount calls the XRPC method "app.bsky.notification.getUnreadCount".


### NotificationGetUnreadCount (api/bsky/notificationgetUnreadCount.go:19)


NotificationGetUnreadCount calls the XRPC method "app.bsky.notification.getUnreadCount".


```go
func NotificationGetUnreadCount((*NotificationGetUnreadCount_Output, error)) (*NotificationGetUnreadCount_Output, error)
```


**Тип запроса:** NotificationGetUnreadCount_Output


```json
{
  "count": 0
}
```


*Определено в:* `api/bsky/notificationgetUnreadCount.go`


**Тип ответа:** NotificationGetUnreadCount_Output


```json
{
  "count": 0
}
```


*Определено в:* `api/bsky/notificationgetUnreadCount.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NotificationGetUnreadCount_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/notificationgetUnreadCount.go:19`




## api/bsky/notificationlistActivitySubscriptions.go


📄 Исходный файл: `api/bsky/notificationlistActivitySubscriptions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationListActivitySubscriptions](#notificationlistactivitysubscriptions-apibskynotificationlistactivitysubscriptionsgo20) `:20`


</details>


[function] name: NotificationListActivitySubscriptions file: api/bsky/notificationlistActivitySubscriptions.go:20 returns_error: да description: NotificationListActivitySubscriptions calls the XRPC method "app.bsky.notification.listActivitySubscriptions".


### NotificationListActivitySubscriptions (api/bsky/notificationlistActivitySubscriptions.go:20)


NotificationListActivitySubscriptions calls the XRPC method "app.bsky.notification.listActivitySubscriptions".


```go
func NotificationListActivitySubscriptions((*NotificationListActivitySubscriptions_Output, error)) (*NotificationListActivitySubscriptions_Output, error)
```


**Тип запроса:** NotificationListActivitySubscriptions_Output


```json
{
  "cursor": "string",
  "subscriptions": []
}
```


*Определено в:* `api/bsky/notificationlistActivitySubscriptions.go`


**Тип ответа:** NotificationListActivitySubscriptions_Output


```json
{
  "cursor": "string",
  "subscriptions": []
}
```


*Определено в:* `api/bsky/notificationlistActivitySubscriptions.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NotificationListActivitySubscriptions_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/notificationlistActivitySubscriptions.go:20`




## api/bsky/notificationlistNotifications.go


📄 Исходный файл: `api/bsky/notificationlistNotifications.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationListNotifications](#notificationlistnotifications-apibskynotificationlistnotificationsgo39) `:39`


</details>


[function] name: NotificationListNotifications file: api/bsky/notificationlistNotifications.go:39 returns_error: да description: NotificationListNotifications calls the XRPC method "app.bsky.notification.listNotifications".

reasons: Notification re


### NotificationListNotifications (api/bsky/notificationlistNotifications.go:39)


NotificationListNotifications calls the XRPC method "app.bsky.notification.listNotifications".

reasons: Notification reasons to include in response.


```go
func NotificationListNotifications((*NotificationListNotifications_Output, error)) (*NotificationListNotifications_Output, error)
```


**Тип запроса:** NotificationListNotifications_Output


```json
{
  "cursor": "string",
  "notifications": [],
  "priority": false,
  "seenAt": "string"
}
```


*Определено в:* `api/bsky/notificationlistNotifications.go`


**Тип ответа:** NotificationListNotifications_Output


```json
{
  "cursor": "string",
  "notifications": [],
  "priority": false,
  "seenAt": "string"
}
```


*Определено в:* `api/bsky/notificationlistNotifications.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NotificationListNotifications_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/notificationlistNotifications.go:39`




## api/bsky/notificationputActivitySubscription.go


📄 Исходный файл: `api/bsky/notificationputActivitySubscription.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationPutActivitySubscription](#notificationputactivitysubscription-apibskynotificationputactivitysubscriptiongo26) `:26`


</details>


[function] name: NotificationPutActivitySubscription file: api/bsky/notificationputActivitySubscription.go:26 returns_error: да description: NotificationPutActivitySubscription calls the XRPC method "app.bsky.notification.putActivitySubscription".


### NotificationPutActivitySubscription (api/bsky/notificationputActivitySubscription.go:26)


NotificationPutActivitySubscription calls the XRPC method "app.bsky.notification.putActivitySubscription".


```go
func NotificationPutActivitySubscription((*NotificationPutActivitySubscription_Output, error)) (*NotificationPutActivitySubscription_Output, error)
```


**Тип запроса:** NotificationPutActivitySubscription_Output


```json
{
  "activitySubscription": null,
  "subject": "string"
}
```


*Определено в:* `api/bsky/notificationputActivitySubscription.go`


**Тип ответа:** NotificationPutActivitySubscription_Output


```json
{
  "activitySubscription": null,
  "subject": "string"
}
```


*Определено в:* `api/bsky/notificationputActivitySubscription.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NotificationPutActivitySubscription_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/notificationputActivitySubscription.go:26`




## api/bsky/notificationputPreferences.go


📄 Исходный файл: `api/bsky/notificationputPreferences.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationPutPreferences](#notificationputpreferences-apibskynotificationputpreferencesgo19) `:19`


</details>


[function] name: NotificationPutPreferences file: api/bsky/notificationputPreferences.go:19 returns_error: нет description: NotificationPutPreferences calls the XRPC method "app.bsky.notification.putPreferences".


### NotificationPutPreferences (api/bsky/notificationputPreferences.go:19)


NotificationPutPreferences calls the XRPC method "app.bsky.notification.putPreferences".


```go
func NotificationPutPreferences((ctx context.Context, c lexutil.LexClient, input *NotificationPutPreferences_Input)) (ctx context.Context, c lexutil.LexClient, input *NotificationPutPreferences_Input)
```


**Тип запроса:** NotificationPutPreferences_Input


```json
{
  "priority": false
}
```


*Определено в:* `api/bsky/notificationputPreferences.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** NotificationPutPreferences_Input


```json
{
  "priority": false
}
```


*Определено в:* `api/bsky/notificationputPreferences.go`


📍 *Расположение:* `api/bsky/notificationputPreferences.go:19`




## api/bsky/notificationputPreferencesV2.go


📄 Исходный файл: `api/bsky/notificationputPreferencesV2.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationPutPreferencesV2](#notificationputpreferencesv2-apibskynotificationputpreferencesv2go36) `:36`


</details>


[function] name: NotificationPutPreferencesV2 file: api/bsky/notificationputPreferencesV2.go:36 returns_error: да description: NotificationPutPreferencesV2 calls the XRPC method "app.bsky.notification.putPreferencesV2".


### NotificationPutPreferencesV2 (api/bsky/notificationputPreferencesV2.go:36)


NotificationPutPreferencesV2 calls the XRPC method "app.bsky.notification.putPreferencesV2".


```go
func NotificationPutPreferencesV2((*NotificationPutPreferencesV2_Output, error)) (*NotificationPutPreferencesV2_Output, error)
```


**Тип запроса:** NotificationPutPreferencesV2_Output


```json
{
  "preferences": null
}
```


*Определено в:* `api/bsky/notificationputPreferencesV2.go`


**Тип ответа:** NotificationPutPreferencesV2_Output


```json
{
  "preferences": null
}
```


*Определено в:* `api/bsky/notificationputPreferencesV2.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*NotificationPutPreferencesV2_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/notificationputPreferencesV2.go:36`




## api/bsky/notificationregisterPush.go


📄 Исходный файл: `api/bsky/notificationregisterPush.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationRegisterPush](#notificationregisterpush-apibskynotificationregisterpushgo24) `:24`


</details>


[function] name: NotificationRegisterPush file: api/bsky/notificationregisterPush.go:24 returns_error: нет description: NotificationRegisterPush calls the XRPC method "app.bsky.notification.registerPush".


### NotificationRegisterPush (api/bsky/notificationregisterPush.go:24)


NotificationRegisterPush calls the XRPC method "app.bsky.notification.registerPush".


```go
func NotificationRegisterPush((ctx context.Context, c lexutil.LexClient, input *NotificationRegisterPush_Input)) (ctx context.Context, c lexutil.LexClient, input *NotificationRegisterPush_Input)
```


**Тип запроса:** NotificationRegisterPush_Input


```json
{
  "ageRestricted": false,
  "appId": "string",
  "platform": "string",
  "serviceDid": "string",
  "token": "string"
}
```


*Определено в:* `api/bsky/notificationregisterPush.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** NotificationRegisterPush_Input


```json
{
  "ageRestricted": false,
  "appId": "string",
  "platform": "string",
  "serviceDid": "string",
  "token": "string"
}
```


*Определено в:* `api/bsky/notificationregisterPush.go`


📍 *Расположение:* `api/bsky/notificationregisterPush.go:24`




## api/bsky/notificationunregisterPush.go


📄 Исходный файл: `api/bsky/notificationunregisterPush.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationUnregisterPush](#notificationunregisterpush-apibskynotificationunregisterpushgo22) `:22`


</details>


[function] name: NotificationUnregisterPush file: api/bsky/notificationunregisterPush.go:22 returns_error: нет description: NotificationUnregisterPush calls the XRPC method "app.bsky.notification.unregisterPush".


### NotificationUnregisterPush (api/bsky/notificationunregisterPush.go:22)


NotificationUnregisterPush calls the XRPC method "app.bsky.notification.unregisterPush".


```go
func NotificationUnregisterPush((ctx context.Context, c lexutil.LexClient, input *NotificationUnregisterPush_Input)) (ctx context.Context, c lexutil.LexClient, input *NotificationUnregisterPush_Input)
```


**Тип запроса:** NotificationUnregisterPush_Input


```json
{
  "appId": "string",
  "platform": "string",
  "serviceDid": "string",
  "token": "string"
}
```


*Определено в:* `api/bsky/notificationunregisterPush.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** NotificationUnregisterPush_Input


```json
{
  "appId": "string",
  "platform": "string",
  "serviceDid": "string",
  "token": "string"
}
```


*Определено в:* `api/bsky/notificationunregisterPush.go`


📍 *Расположение:* `api/bsky/notificationunregisterPush.go:22`




## api/bsky/notificationupdateSeen.go


📄 Исходный файл: `api/bsky/notificationupdateSeen.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [NotificationUpdateSeen](#notificationupdateseen-apibskynotificationupdateseengo19) `:19`


</details>


[function] name: NotificationUpdateSeen file: api/bsky/notificationupdateSeen.go:19 returns_error: нет description: NotificationUpdateSeen calls the XRPC method "app.bsky.notification.updateSeen".


### NotificationUpdateSeen (api/bsky/notificationupdateSeen.go:19)


NotificationUpdateSeen calls the XRPC method "app.bsky.notification.updateSeen".


```go
func NotificationUpdateSeen((ctx context.Context, c lexutil.LexClient, input *NotificationUpdateSeen_Input)) (ctx context.Context, c lexutil.LexClient, input *NotificationUpdateSeen_Input)
```


**Тип запроса:** NotificationUpdateSeen_Input


```json
{
  "seenAt": "string"
}
```


*Определено в:* `api/bsky/notificationupdateSeen.go`


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


**Тип ответа:** lexutil.LexClient


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** input


*Определение не найдено в проекте (тип может быть во внешнем proto).*


**Тип ответа:** NotificationUpdateSeen_Input


```json
{
  "seenAt": "string"
}
```


*Определено в:* `api/bsky/notificationupdateSeen.go`


📍 *Расположение:* `api/bsky/notificationupdateSeen.go:19`




## api/bsky/richtextfacet.go


📄 Исходный файл: `api/bsky/richtextfacet.go`


<details open>
<summary><b>Функции в этом файле (4)</b></summary>


- 🔗 [MarshalCBOR](#marshalcbor-apibskyrichtextfacetgo76) `:76`

- 🔗 [MarshalJSON](#marshaljson-apibskyrichtextfacetgo39) `:39`

- 🔗 [UnmarshalCBOR](#unmarshalcbor-apibskyrichtextfacetgo94) `:94`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyrichtextfacetgo55) `:55`


</details>


[function] name: MarshalCBOR file: api/bsky/richtextfacet.go:76 returns_error: нет description: —


### MarshalCBOR (api/bsky/richtextfacet.go:76)


MarshalCBOR is a method that performs operations based on the provided parameters and returns (w io.Writer).


```go
func (t *RichtextFacet_Features_Elem) MarshalCBOR((w io.Writer)) (w io.Writer)
```


**Тип ответа:** w


```json
{
  "db": null,
  "logger": null,
  "fullNetworkMode": false,
  "relayUrl": "string",
  "signalCollection": "string"
}
```


*Определено в:* `cmd/tap/crawler.go`


**Тип ответа:** io.Writer


*Определение не найдено в проекте (тип может быть во внешнем proto).*


📍 *Расположение:* `api/bsky/richtextfacet.go:76`



---


[function] name: MarshalJSON file: api/bsky/richtextfacet.go:39 returns_error: да description: —


### MarshalJSON (api/bsky/richtextfacet.go:39)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *RichtextFacet_Features_Elem) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/richtextfacet.go:39`



---


[function] name: UnmarshalCBOR file: api/bsky/richtextfacet.go:94 returns_error: нет description: —


### UnmarshalCBOR (api/bsky/richtextfacet.go:94)


UnmarshalCBOR is a method that performs operations based on the provided parameters and returns (r io.Reader).


```go
func (t *RichtextFacet_Features_Elem) UnmarshalCBOR((r io.Reader)) (r io.Reader)
```


**Тип ответа:** r


```json
{
  "r": {},
  "addr": "string",
  "bytesCounter": {}
}
```


*Определено в:* `events/consumer.go`


**Тип ответа:** io.Reader


```json
{
  "r": null
}
```


*Определено в:* `repo/carutil/reader.go`


📍 *Расположение:* `api/bsky/richtextfacet.go:94`



---


[function] name: UnmarshalJSON file: api/bsky/richtextfacet.go:55 returns_error: нет description: —


### UnmarshalJSON (api/bsky/richtextfacet.go:55)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *RichtextFacet_Features_Elem) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/richtextfacet.go:55`




## api/bsky/unspeccedgetAgeAssuranceState.go


📄 Исходный файл: `api/bsky/unspeccedgetAgeAssuranceState.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetAgeAssuranceState](#unspeccedgetageassurancestate-apibskyunspeccedgetageassurancestatego14) `:14`


</details>


[function] name: UnspeccedGetAgeAssuranceState file: api/bsky/unspeccedgetAgeAssuranceState.go:14 returns_error: да description: UnspeccedGetAgeAssuranceState calls the XRPC method "app.bsky.unspecced.getAgeAssuranceState".


### UnspeccedGetAgeAssuranceState (api/bsky/unspeccedgetAgeAssuranceState.go:14)


UnspeccedGetAgeAssuranceState calls the XRPC method "app.bsky.unspecced.getAgeAssuranceState".


```go
func UnspeccedGetAgeAssuranceState((*UnspeccedDefs_AgeAssuranceState, error)) (*UnspeccedDefs_AgeAssuranceState, error)
```


**Тип запроса:** UnspeccedDefs_AgeAssuranceState


```json
{
  "lastInitiatedAt": "string",
  "status": "string"
}
```


*Определено в:* `api/bsky/unspecceddefs.go`


**Тип ответа:** UnspeccedDefs_AgeAssuranceState


```json
{
  "lastInitiatedAt": "string",
  "status": "string"
}
```


*Определено в:* `api/bsky/unspecceddefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedDefs_AgeAssuranceState`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetAgeAssuranceState.go:14`




## api/bsky/unspeccedgetConfig.go


📄 Исходный файл: `api/bsky/unspeccedgetConfig.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetConfig](#unspeccedgetconfig-apibskyunspeccedgetconfiggo26) `:26`


</details>


[function] name: UnspeccedGetConfig file: api/bsky/unspeccedgetConfig.go:26 returns_error: да description: UnspeccedGetConfig calls the XRPC method "app.bsky.unspecced.getConfig".


### UnspeccedGetConfig (api/bsky/unspeccedgetConfig.go:26)


UnspeccedGetConfig calls the XRPC method "app.bsky.unspecced.getConfig".


```go
func UnspeccedGetConfig((*UnspeccedGetConfig_Output, error)) (*UnspeccedGetConfig_Output, error)
```


**Тип запроса:** UnspeccedGetConfig_Output


```json
{
  "checkEmailConfirmed": false,
  "liveNow": []
}
```


*Определено в:* `api/bsky/unspeccedgetConfig.go`


**Тип ответа:** UnspeccedGetConfig_Output


```json
{
  "checkEmailConfirmed": false,
  "liveNow": []
}
```


*Определено в:* `api/bsky/unspeccedgetConfig.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetConfig_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetConfig.go:26`




## api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go


📄 Исходный файл: `api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetOnboardingSuggestedStarterPacks](#unspeccedgetonboardingsuggestedstarterpacks-apibskyunspeccedgetonboardingsuggestedstarterpacksgo19) `:19`


</details>


[function] name: UnspeccedGetOnboardingSuggestedStarterPacks file: api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go:19 returns_error: да description: UnspeccedGetOnboardingSuggestedStarterPacks calls the XRPC method "app.bsky.unspecced.getOnboardingSuggestedStarterPacks


### UnspeccedGetOnboardingSuggestedStarterPacks (api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go:19)


UnspeccedGetOnboardingSuggestedStarterPacks calls the XRPC method "app.bsky.unspecced.getOnboardingSuggestedStarterPacks".


```go
func UnspeccedGetOnboardingSuggestedStarterPacks((*UnspeccedGetOnboardingSuggestedStarterPacks_Output, error)) (*UnspeccedGetOnboardingSuggestedStarterPacks_Output, error)
```


**Тип запроса:** UnspeccedGetOnboardingSuggestedStarterPacks_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go`


**Тип ответа:** UnspeccedGetOnboardingSuggestedStarterPacks_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetOnboardingSuggestedStarterPacks_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go:19`




## api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetOnboardingSuggestedStarterPacksSkeleton](#unspeccedgetonboardingsuggestedstarterpacksskeleton-apibskyunspeccedgetonboardingsuggestedstarterpacksskeletongo21) `:21`


</details>


[function] name: UnspeccedGetOnboardingSuggestedStarterPacksSkeleton file: api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go:21 returns_error: да description: UnspeccedGetOnboardingSuggestedStarterPacksSkeleton calls the XRPC method "app.bsky.unspecced.getOnboardingSuggestedStar


### UnspeccedGetOnboardingSuggestedStarterPacksSkeleton (api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go:21)


UnspeccedGetOnboardingSuggestedStarterPacksSkeleton calls the XRPC method "app.bsky.unspecced.getOnboardingSuggestedStarterPacksSkeleton".

viewer: DID of the account making the request (not included for public/unauthenticated queries).


```go
func UnspeccedGetOnboardingSuggestedStarterPacksSkeleton((*UnspeccedGetOnboardingSuggestedStarterPacksSkeleton_Output, error)) (*UnspeccedGetOnboardingSuggestedStarterPacksSkeleton_Output, error)
```


**Тип запроса:** UnspeccedGetOnboardingSuggestedStarterPacksSkeleton_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go`


**Тип ответа:** UnspeccedGetOnboardingSuggestedStarterPacksSkeleton_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetOnboardingSuggestedStarterPacksSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go:21`




## api/bsky/unspeccedgetPopularFeedGenerators.go


📄 Исходный файл: `api/bsky/unspeccedgetPopularFeedGenerators.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetPopularFeedGenerators](#unspeccedgetpopularfeedgenerators-apibskyunspeccedgetpopularfeedgeneratorsgo20) `:20`


</details>


[function] name: UnspeccedGetPopularFeedGenerators file: api/bsky/unspeccedgetPopularFeedGenerators.go:20 returns_error: да description: UnspeccedGetPopularFeedGenerators calls the XRPC method "app.bsky.unspecced.getPopularFeedGenerators".


### UnspeccedGetPopularFeedGenerators (api/bsky/unspeccedgetPopularFeedGenerators.go:20)


UnspeccedGetPopularFeedGenerators calls the XRPC method "app.bsky.unspecced.getPopularFeedGenerators".


```go
func UnspeccedGetPopularFeedGenerators((*UnspeccedGetPopularFeedGenerators_Output, error)) (*UnspeccedGetPopularFeedGenerators_Output, error)
```


**Тип запроса:** UnspeccedGetPopularFeedGenerators_Output


```json
{
  "cursor": "string",
  "feeds": []
}
```


*Определено в:* `api/bsky/unspeccedgetPopularFeedGenerators.go`


**Тип ответа:** UnspeccedGetPopularFeedGenerators_Output


```json
{
  "cursor": "string",
  "feeds": []
}
```


*Определено в:* `api/bsky/unspeccedgetPopularFeedGenerators.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetPopularFeedGenerators_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetPopularFeedGenerators.go:20`




## api/bsky/unspeccedgetPostThreadOtherV2.go


📄 Исходный файл: `api/bsky/unspeccedgetPostThreadOtherV2.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apibskyunspeccedgetpostthreadotherv2go33) `:33`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyunspeccedgetpostthreadotherv2go41) `:41`

- 🔗 [UnspeccedGetPostThreadOtherV2](#unspeccedgetpostthreadotherv2-apibskyunspeccedgetpostthreadotherv2go59) `:59`


</details>


[function] name: MarshalJSON file: api/bsky/unspeccedgetPostThreadOtherV2.go:33 returns_error: да description: —


### MarshalJSON (api/bsky/unspeccedgetPostThreadOtherV2.go:33)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *UnspeccedGetPostThreadOtherV2_ThreadItem_Value) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetPostThreadOtherV2.go:33`



---


[function] name: UnmarshalJSON file: api/bsky/unspeccedgetPostThreadOtherV2.go:41 returns_error: нет description: —


### UnmarshalJSON (api/bsky/unspeccedgetPostThreadOtherV2.go:41)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *UnspeccedGetPostThreadOtherV2_ThreadItem_Value) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/unspeccedgetPostThreadOtherV2.go:41`



---


[function] name: UnspeccedGetPostThreadOtherV2 file: api/bsky/unspeccedgetPostThreadOtherV2.go:59 returns_error: да description: UnspeccedGetPostThreadOtherV2 calls the XRPC method "app.bsky.unspecced.getPostThreadOtherV2".

anchor: Reference (AT-UR


### UnspeccedGetPostThreadOtherV2 (api/bsky/unspeccedgetPostThreadOtherV2.go:59)


UnspeccedGetPostThreadOtherV2 calls the XRPC method "app.bsky.unspecced.getPostThreadOtherV2".

anchor: Reference (AT-URI) to post record. This is the anchor post.


```go
func UnspeccedGetPostThreadOtherV2((*UnspeccedGetPostThreadOtherV2_Output, error)) (*UnspeccedGetPostThreadOtherV2_Output, error)
```


**Тип запроса:** UnspeccedGetPostThreadOtherV2_Output


```json
{
  "thread": []
}
```


*Определено в:* `api/bsky/unspeccedgetPostThreadOtherV2.go`


**Тип ответа:** UnspeccedGetPostThreadOtherV2_Output


```json
{
  "thread": []
}
```


*Определено в:* `api/bsky/unspeccedgetPostThreadOtherV2.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetPostThreadOtherV2_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetPostThreadOtherV2.go:59`




## api/bsky/unspeccedgetPostThreadV2.go


📄 Исходный файл: `api/bsky/unspeccedgetPostThreadV2.go`


<details open>
<summary><b>Функции в этом файле (3)</b></summary>


- 🔗 [MarshalJSON](#marshaljson-apibskyunspeccedgetpostthreadv2go39) `:39`

- 🔗 [UnmarshalJSON](#unmarshaljson-apibskyunspeccedgetpostthreadv2go59) `:59`

- 🔗 [UnspeccedGetPostThreadV2](#unspeccedgetpostthreadv2-apibskyunspeccedgetpostthreadv2go90) `:90`


</details>


[function] name: MarshalJSON file: api/bsky/unspeccedgetPostThreadV2.go:39 returns_error: да description: —


### MarshalJSON (api/bsky/unspeccedgetPostThreadV2.go:39)


MarshalJSON is a method that performs operations based on the provided parameters and may return an error.


```go
func (t *UnspeccedGetPostThreadV2_ThreadItem_Value) MarshalJSON(([]byte, error)) ([]byte, error)
```


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `[]byte`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetPostThreadV2.go:39`



---


[function] name: UnmarshalJSON file: api/bsky/unspeccedgetPostThreadV2.go:59 returns_error: нет description: —


### UnmarshalJSON (api/bsky/unspeccedgetPostThreadV2.go:59)


UnmarshalJSON is a method that performs operations based on the provided parameters and returns (b []byte).


```go
func (t *UnspeccedGetPostThreadV2_ThreadItem_Value) UnmarshalJSON((b []byte)) (b []byte)
```


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


📍 *Расположение:* `api/bsky/unspeccedgetPostThreadV2.go:59`



---


[function] name: UnspeccedGetPostThreadV2 file: api/bsky/unspeccedgetPostThreadV2.go:90 returns_error: да description: UnspeccedGetPostThreadV2 calls the XRPC method "app.bsky.unspecced.getPostThreadV2".

above: Whether to include parents 


### UnspeccedGetPostThreadV2 (api/bsky/unspeccedgetPostThreadV2.go:90)


UnspeccedGetPostThreadV2 calls the XRPC method "app.bsky.unspecced.getPostThreadV2".

above: Whether to include parents above the anchor.
anchor: Reference (AT-URI) to post record. This is the anchor post, and the thread will be built around it. It can be any post in the tree, not necessarily a root post.
below: How many levels of replies to include below the anchor.
branchingFactor: Maximum of replies to include at each level of the thread, except for the direct replies to the anchor, which are (NOTE: currently, during unspecced phase) all returned (NOTE: later they might be paginated).
sort: Sorting for the thread replies.


```go
func UnspeccedGetPostThreadV2((*UnspeccedGetPostThreadV2_Output, error)) (*UnspeccedGetPostThreadV2_Output, error)
```


**Тип запроса:** UnspeccedGetPostThreadV2_Output


```json
{
  "hasOtherReplies": false,
  "thread": [],
  "threadgate": null
}
```


*Определено в:* `api/bsky/unspeccedgetPostThreadV2.go`


**Тип ответа:** UnspeccedGetPostThreadV2_Output


```json
{
  "hasOtherReplies": false,
  "thread": [],
  "threadgate": null
}
```


*Определено в:* `api/bsky/unspeccedgetPostThreadV2.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetPostThreadV2_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetPostThreadV2.go:90`




## api/bsky/unspeccedgetSuggestedFeeds.go


📄 Исходный файл: `api/bsky/unspeccedgetSuggestedFeeds.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetSuggestedFeeds](#unspeccedgetsuggestedfeeds-apibskyunspeccedgetsuggestedfeedsgo19) `:19`


</details>


[function] name: UnspeccedGetSuggestedFeeds file: api/bsky/unspeccedgetSuggestedFeeds.go:19 returns_error: да description: UnspeccedGetSuggestedFeeds calls the XRPC method "app.bsky.unspecced.getSuggestedFeeds".


### UnspeccedGetSuggestedFeeds (api/bsky/unspeccedgetSuggestedFeeds.go:19)


UnspeccedGetSuggestedFeeds calls the XRPC method "app.bsky.unspecced.getSuggestedFeeds".


```go
func UnspeccedGetSuggestedFeeds((*UnspeccedGetSuggestedFeeds_Output, error)) (*UnspeccedGetSuggestedFeeds_Output, error)
```


**Тип запроса:** UnspeccedGetSuggestedFeeds_Output


```json
{
  "feeds": []
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedFeeds.go`


**Тип ответа:** UnspeccedGetSuggestedFeeds_Output


```json
{
  "feeds": []
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedFeeds.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetSuggestedFeeds_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetSuggestedFeeds.go:19`




## api/bsky/unspeccedgetSuggestedFeedsSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedgetSuggestedFeedsSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetSuggestedFeedsSkeleton](#unspeccedgetsuggestedfeedsskeleton-apibskyunspeccedgetsuggestedfeedsskeletongo21) `:21`


</details>


[function] name: UnspeccedGetSuggestedFeedsSkeleton file: api/bsky/unspeccedgetSuggestedFeedsSkeleton.go:21 returns_error: да description: UnspeccedGetSuggestedFeedsSkeleton calls the XRPC method "app.bsky.unspecced.getSuggestedFeedsSkeleton".

viewer: DID of


### UnspeccedGetSuggestedFeedsSkeleton (api/bsky/unspeccedgetSuggestedFeedsSkeleton.go:21)


UnspeccedGetSuggestedFeedsSkeleton calls the XRPC method "app.bsky.unspecced.getSuggestedFeedsSkeleton".

viewer: DID of the account making the request (not included for public/unauthenticated queries).


```go
func UnspeccedGetSuggestedFeedsSkeleton((*UnspeccedGetSuggestedFeedsSkeleton_Output, error)) (*UnspeccedGetSuggestedFeedsSkeleton_Output, error)
```


**Тип запроса:** UnspeccedGetSuggestedFeedsSkeleton_Output


```json
{
  "feeds": []
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedFeedsSkeleton.go`


**Тип ответа:** UnspeccedGetSuggestedFeedsSkeleton_Output


```json
{
  "feeds": []
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedFeedsSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetSuggestedFeedsSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetSuggestedFeedsSkeleton.go:21`




## api/bsky/unspeccedgetSuggestedStarterPacks.go


📄 Исходный файл: `api/bsky/unspeccedgetSuggestedStarterPacks.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetSuggestedStarterPacks](#unspeccedgetsuggestedstarterpacks-apibskyunspeccedgetsuggestedstarterpacksgo19) `:19`


</details>


[function] name: UnspeccedGetSuggestedStarterPacks file: api/bsky/unspeccedgetSuggestedStarterPacks.go:19 returns_error: да description: UnspeccedGetSuggestedStarterPacks calls the XRPC method "app.bsky.unspecced.getSuggestedStarterPacks".


### UnspeccedGetSuggestedStarterPacks (api/bsky/unspeccedgetSuggestedStarterPacks.go:19)


UnspeccedGetSuggestedStarterPacks calls the XRPC method "app.bsky.unspecced.getSuggestedStarterPacks".


```go
func UnspeccedGetSuggestedStarterPacks((*UnspeccedGetSuggestedStarterPacks_Output, error)) (*UnspeccedGetSuggestedStarterPacks_Output, error)
```


**Тип запроса:** UnspeccedGetSuggestedStarterPacks_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedStarterPacks.go`


**Тип ответа:** UnspeccedGetSuggestedStarterPacks_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedStarterPacks.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetSuggestedStarterPacks_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetSuggestedStarterPacks.go:19`




## api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetSuggestedStarterPacksSkeleton](#unspeccedgetsuggestedstarterpacksskeleton-apibskyunspeccedgetsuggestedstarterpacksskeletongo21) `:21`


</details>


[function] name: UnspeccedGetSuggestedStarterPacksSkeleton file: api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go:21 returns_error: да description: UnspeccedGetSuggestedStarterPacksSkeleton calls the XRPC method "app.bsky.unspecced.getSuggestedStarterPacksSkeleton".




### UnspeccedGetSuggestedStarterPacksSkeleton (api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go:21)


UnspeccedGetSuggestedStarterPacksSkeleton calls the XRPC method "app.bsky.unspecced.getSuggestedStarterPacksSkeleton".

viewer: DID of the account making the request (not included for public/unauthenticated queries).


```go
func UnspeccedGetSuggestedStarterPacksSkeleton((*UnspeccedGetSuggestedStarterPacksSkeleton_Output, error)) (*UnspeccedGetSuggestedStarterPacksSkeleton_Output, error)
```


**Тип запроса:** UnspeccedGetSuggestedStarterPacksSkeleton_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go`


**Тип ответа:** UnspeccedGetSuggestedStarterPacksSkeleton_Output


```json
{
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetSuggestedStarterPacksSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go:21`




## api/bsky/unspeccedgetSuggestedUsers.go


📄 Исходный файл: `api/bsky/unspeccedgetSuggestedUsers.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetSuggestedUsers](#unspeccedgetsuggestedusers-apibskyunspeccedgetsuggestedusersgo25) `:25`


</details>


[function] name: UnspeccedGetSuggestedUsers file: api/bsky/unspeccedgetSuggestedUsers.go:25 returns_error: да description: UnspeccedGetSuggestedUsers calls the XRPC method "app.bsky.unspecced.getSuggestedUsers".

category: Category of users to


### UnspeccedGetSuggestedUsers (api/bsky/unspeccedgetSuggestedUsers.go:25)


UnspeccedGetSuggestedUsers calls the XRPC method "app.bsky.unspecced.getSuggestedUsers".

category: Category of users to get suggestions for.


```go
func UnspeccedGetSuggestedUsers((*UnspeccedGetSuggestedUsers_Output, error)) (*UnspeccedGetSuggestedUsers_Output, error)
```


**Тип запроса:** UnspeccedGetSuggestedUsers_Output


```json
{
  "actors": [],
  "recId": "string",
  "recIdStr": "string"
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedUsers.go`


**Тип ответа:** UnspeccedGetSuggestedUsers_Output


```json
{
  "actors": [],
  "recId": "string",
  "recIdStr": "string"
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedUsers.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetSuggestedUsers_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetSuggestedUsers.go:25`




## api/bsky/unspeccedgetSuggestedUsersSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedgetSuggestedUsersSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetSuggestedUsersSkeleton](#unspeccedgetsuggestedusersskeleton-apibskyunspeccedgetsuggestedusersskeletongo26) `:26`


</details>


[function] name: UnspeccedGetSuggestedUsersSkeleton file: api/bsky/unspeccedgetSuggestedUsersSkeleton.go:26 returns_error: да description: UnspeccedGetSuggestedUsersSkeleton calls the XRPC method "app.bsky.unspecced.getSuggestedUsersSkeleton".

category: Cate


### UnspeccedGetSuggestedUsersSkeleton (api/bsky/unspeccedgetSuggestedUsersSkeleton.go:26)


UnspeccedGetSuggestedUsersSkeleton calls the XRPC method "app.bsky.unspecced.getSuggestedUsersSkeleton".

category: Category of users to get suggestions for.
viewer: DID of the account making the request (not included for public/unauthenticated queries).


```go
func UnspeccedGetSuggestedUsersSkeleton((*UnspeccedGetSuggestedUsersSkeleton_Output, error)) (*UnspeccedGetSuggestedUsersSkeleton_Output, error)
```


**Тип запроса:** UnspeccedGetSuggestedUsersSkeleton_Output


```json
{
  "dids": [],
  "recId": "string",
  "recIdStr": "string"
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedUsersSkeleton.go`


**Тип ответа:** UnspeccedGetSuggestedUsersSkeleton_Output


```json
{
  "dids": [],
  "recId": "string",
  "recIdStr": "string"
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestedUsersSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetSuggestedUsersSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetSuggestedUsersSkeleton.go:26`




## api/bsky/unspeccedgetSuggestionsSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedgetSuggestionsSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetSuggestionsSkeleton](#unspeccedgetsuggestionsskeleton-apibskyunspeccedgetsuggestionsskeletongo29) `:29`


</details>


[function] name: UnspeccedGetSuggestionsSkeleton file: api/bsky/unspeccedgetSuggestionsSkeleton.go:29 returns_error: да description: UnspeccedGetSuggestionsSkeleton calls the XRPC method "app.bsky.unspecced.getSuggestionsSkeleton".

relativeToDid: DID o


### UnspeccedGetSuggestionsSkeleton (api/bsky/unspeccedgetSuggestionsSkeleton.go:29)


UnspeccedGetSuggestionsSkeleton calls the XRPC method "app.bsky.unspecced.getSuggestionsSkeleton".

relativeToDid: DID of the account to get suggestions relative to. If not provided, suggestions will be based on the viewer.
viewer: DID of the account making the request (not included for public/unauthenticated queries). Used to boost followed accounts in ranking.


```go
func UnspeccedGetSuggestionsSkeleton((*UnspeccedGetSuggestionsSkeleton_Output, error)) (*UnspeccedGetSuggestionsSkeleton_Output, error)
```


**Тип запроса:** UnspeccedGetSuggestionsSkeleton_Output


```json
{
  "actors": [],
  "cursor": "string",
  "recId": 0,
  "recIdStr": "string",
  "relativeToDid": "string"
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestionsSkeleton.go`


**Тип ответа:** UnspeccedGetSuggestionsSkeleton_Output


```json
{
  "actors": [],
  "cursor": "string",
  "recId": 0,
  "recIdStr": "string",
  "relativeToDid": "string"
}
```


*Определено в:* `api/bsky/unspeccedgetSuggestionsSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetSuggestionsSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetSuggestionsSkeleton.go:29`




## api/bsky/unspeccedgetTaggedSuggestions.go


📄 Исходный файл: `api/bsky/unspeccedgetTaggedSuggestions.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetTaggedSuggestions](#unspeccedgettaggedsuggestions-apibskyunspeccedgettaggedsuggestionsgo26) `:26`


</details>


[function] name: UnspeccedGetTaggedSuggestions file: api/bsky/unspeccedgetTaggedSuggestions.go:26 returns_error: да description: UnspeccedGetTaggedSuggestions calls the XRPC method "app.bsky.unspecced.getTaggedSuggestions".


### UnspeccedGetTaggedSuggestions (api/bsky/unspeccedgetTaggedSuggestions.go:26)


UnspeccedGetTaggedSuggestions calls the XRPC method "app.bsky.unspecced.getTaggedSuggestions".


```go
func UnspeccedGetTaggedSuggestions((*UnspeccedGetTaggedSuggestions_Output, error)) (*UnspeccedGetTaggedSuggestions_Output, error)
```


**Тип запроса:** UnspeccedGetTaggedSuggestions_Output


```json
{
  "suggestions": []
}
```


*Определено в:* `api/bsky/unspeccedgetTaggedSuggestions.go`


**Тип ответа:** UnspeccedGetTaggedSuggestions_Output


```json
{
  "suggestions": []
}
```


*Определено в:* `api/bsky/unspeccedgetTaggedSuggestions.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetTaggedSuggestions_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetTaggedSuggestions.go:26`




## api/bsky/unspeccedgetTrendingTopics.go


📄 Исходный файл: `api/bsky/unspeccedgetTrendingTopics.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetTrendingTopics](#unspeccedgettrendingtopics-apibskyunspeccedgettrendingtopicsgo22) `:22`


</details>


[function] name: UnspeccedGetTrendingTopics file: api/bsky/unspeccedgetTrendingTopics.go:22 returns_error: да description: UnspeccedGetTrendingTopics calls the XRPC method "app.bsky.unspecced.getTrendingTopics".

viewer: DID of the account mak


### UnspeccedGetTrendingTopics (api/bsky/unspeccedgetTrendingTopics.go:22)


UnspeccedGetTrendingTopics calls the XRPC method "app.bsky.unspecced.getTrendingTopics".

viewer: DID of the account making the request (not included for public/unauthenticated queries). Used to boost followed accounts in ranking.


```go
func UnspeccedGetTrendingTopics((*UnspeccedGetTrendingTopics_Output, error)) (*UnspeccedGetTrendingTopics_Output, error)
```


**Тип запроса:** UnspeccedGetTrendingTopics_Output


```json
{
  "suggested": [],
  "topics": []
}
```


*Определено в:* `api/bsky/unspeccedgetTrendingTopics.go`


**Тип ответа:** UnspeccedGetTrendingTopics_Output


```json
{
  "suggested": [],
  "topics": []
}
```


*Определено в:* `api/bsky/unspeccedgetTrendingTopics.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetTrendingTopics_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetTrendingTopics.go:22`




## api/bsky/unspeccedgetTrends.go


📄 Исходный файл: `api/bsky/unspeccedgetTrends.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetTrends](#unspeccedgettrends-apibskyunspeccedgettrendsgo19) `:19`


</details>


[function] name: UnspeccedGetTrends file: api/bsky/unspeccedgetTrends.go:19 returns_error: да description: UnspeccedGetTrends calls the XRPC method "app.bsky.unspecced.getTrends".


### UnspeccedGetTrends (api/bsky/unspeccedgetTrends.go:19)


UnspeccedGetTrends calls the XRPC method "app.bsky.unspecced.getTrends".


```go
func UnspeccedGetTrends((*UnspeccedGetTrends_Output, error)) (*UnspeccedGetTrends_Output, error)
```


**Тип запроса:** UnspeccedGetTrends_Output


```json
{
  "trends": []
}
```


*Определено в:* `api/bsky/unspeccedgetTrends.go`


**Тип ответа:** UnspeccedGetTrends_Output


```json
{
  "trends": []
}
```


*Определено в:* `api/bsky/unspeccedgetTrends.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetTrends_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetTrends.go:19`




## api/bsky/unspeccedgetTrendsSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedgetTrendsSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedGetTrendsSkeleton](#unspeccedgettrendsskeleton-apibskyunspeccedgettrendsskeletongo21) `:21`


</details>


[function] name: UnspeccedGetTrendsSkeleton file: api/bsky/unspeccedgetTrendsSkeleton.go:21 returns_error: да description: UnspeccedGetTrendsSkeleton calls the XRPC method "app.bsky.unspecced.getTrendsSkeleton".

viewer: DID of the account mak


### UnspeccedGetTrendsSkeleton (api/bsky/unspeccedgetTrendsSkeleton.go:21)


UnspeccedGetTrendsSkeleton calls the XRPC method "app.bsky.unspecced.getTrendsSkeleton".

viewer: DID of the account making the request (not included for public/unauthenticated queries).


```go
func UnspeccedGetTrendsSkeleton((*UnspeccedGetTrendsSkeleton_Output, error)) (*UnspeccedGetTrendsSkeleton_Output, error)
```


**Тип запроса:** UnspeccedGetTrendsSkeleton_Output


```json
{
  "trends": []
}
```


*Определено в:* `api/bsky/unspeccedgetTrendsSkeleton.go`


**Тип ответа:** UnspeccedGetTrendsSkeleton_Output


```json
{
  "trends": []
}
```


*Определено в:* `api/bsky/unspeccedgetTrendsSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedGetTrendsSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedgetTrendsSkeleton.go:21`




## api/bsky/unspeccedinitAgeAssurance.go


📄 Исходный файл: `api/bsky/unspeccedinitAgeAssurance.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedInitAgeAssurance](#unspeccedinitageassurance-apibskyunspeccedinitageassurancego24) `:24`


</details>


[function] name: UnspeccedInitAgeAssurance file: api/bsky/unspeccedinitAgeAssurance.go:24 returns_error: да description: UnspeccedInitAgeAssurance calls the XRPC method "app.bsky.unspecced.initAgeAssurance".


### UnspeccedInitAgeAssurance (api/bsky/unspeccedinitAgeAssurance.go:24)


UnspeccedInitAgeAssurance calls the XRPC method "app.bsky.unspecced.initAgeAssurance".


```go
func UnspeccedInitAgeAssurance((*UnspeccedDefs_AgeAssuranceState, error)) (*UnspeccedDefs_AgeAssuranceState, error)
```


**Тип запроса:** UnspeccedDefs_AgeAssuranceState


```json
{
  "lastInitiatedAt": "string",
  "status": "string"
}
```


*Определено в:* `api/bsky/unspecceddefs.go`


**Тип ответа:** UnspeccedDefs_AgeAssuranceState


```json
{
  "lastInitiatedAt": "string",
  "status": "string"
}
```


*Определено в:* `api/bsky/unspecceddefs.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedDefs_AgeAssuranceState`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedinitAgeAssurance.go:24`




## api/bsky/unspeccedsearchActorsSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedsearchActorsSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedSearchActorsSkeleton](#unspeccedsearchactorsskeleton-apibskyunspeccedsearchactorsskeletongo27) `:27`


</details>


[function] name: UnspeccedSearchActorsSkeleton file: api/bsky/unspeccedsearchActorsSkeleton.go:27 returns_error: да description: UnspeccedSearchActorsSkeleton calls the XRPC method "app.bsky.unspecced.searchActorsSkeleton".

cursor: Optional paginat


### UnspeccedSearchActorsSkeleton (api/bsky/unspeccedsearchActorsSkeleton.go:27)


UnspeccedSearchActorsSkeleton calls the XRPC method "app.bsky.unspecced.searchActorsSkeleton".

cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended. For typeahead search, only simple term match is supported, not full syntax.
typeahead: If true, acts as fast/simple 'typeahead' query.
viewer: DID of the account making the request (not included for public/unauthenticated queries). Used to boost followed accounts in ranking.


```go
func UnspeccedSearchActorsSkeleton((*UnspeccedSearchActorsSkeleton_Output, error)) (*UnspeccedSearchActorsSkeleton_Output, error)
```


**Тип запроса:** UnspeccedSearchActorsSkeleton_Output


```json
{
  "actors": [],
  "cursor": "string",
  "hitsTotal": 0
}
```


*Определено в:* `api/bsky/unspeccedsearchActorsSkeleton.go`


**Тип ответа:** UnspeccedSearchActorsSkeleton_Output


```json
{
  "actors": [],
  "cursor": "string",
  "hitsTotal": 0
}
```


*Определено в:* `api/bsky/unspeccedsearchActorsSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedSearchActorsSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedsearchActorsSkeleton.go:27`




## api/bsky/unspeccedsearchPostsSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedsearchPostsSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedSearchPostsSkeleton](#unspeccedsearchpostsskeleton-apibskyunspeccedsearchpostsskeletongo35) `:35`


</details>


[function] name: UnspeccedSearchPostsSkeleton file: api/bsky/unspeccedsearchPostsSkeleton.go:35 returns_error: да description: UnspeccedSearchPostsSkeleton calls the XRPC method "app.bsky.unspecced.searchPostsSkeleton".

author: Filter to posts by


### UnspeccedSearchPostsSkeleton (api/bsky/unspeccedsearchPostsSkeleton.go:35)


UnspeccedSearchPostsSkeleton calls the XRPC method "app.bsky.unspecced.searchPostsSkeleton".

author: Filter to posts by the given account. Handles are resolved to DID before query-time.
cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
domain: Filter to posts with URLs (facet links or embeds) linking to the given domain (hostname). Server may apply hostname normalization.
lang: Filter to posts in the given language. Expected to be based on post language field, though server may override language detection.
mentions: Filter to posts which mention the given account. Handles are resolved to DID before query-time. Only matches rich-text facet mentions.
q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.
since: Filter results for posts after the indicated datetime (inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYYY-MM-DD).
sort: Specifies the ranking order of results.
tag: Filter to posts with the given tag (hashtag), based on rich-text facet or tag field. Do not include the hash (#) prefix. Multiple tags can be specified, with 'AND' matching.
until: Filter results for posts before the indicated datetime (not inclusive). Expected to use 'sortAt' timestamp, which may not match 'createdAt'. Can be a datetime, or just an ISO date (YYY-MM-DD).
url: Filter to posts with links (facet links or embeds) pointing to this URL. Server may apply URL normalization or fuzzy matching.
viewer: DID of the account making the request (not included for public/unauthenticated queries). Used for 'from:me' queries.


```go
func UnspeccedSearchPostsSkeleton((*UnspeccedSearchPostsSkeleton_Output, error)) (*UnspeccedSearchPostsSkeleton_Output, error)
```


**Тип запроса:** UnspeccedSearchPostsSkeleton_Output


```json
{
  "cursor": "string",
  "hitsTotal": 0,
  "posts": []
}
```


*Определено в:* `api/bsky/unspeccedsearchPostsSkeleton.go`


**Тип ответа:** UnspeccedSearchPostsSkeleton_Output


```json
{
  "cursor": "string",
  "hitsTotal": 0,
  "posts": []
}
```


*Определено в:* `api/bsky/unspeccedsearchPostsSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedSearchPostsSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedsearchPostsSkeleton.go:35`




## api/bsky/unspeccedsearchStarterPacksSkeleton.go


📄 Исходный файл: `api/bsky/unspeccedsearchStarterPacksSkeleton.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [UnspeccedSearchStarterPacksSkeleton](#unspeccedsearchstarterpacksskeleton-apibskyunspeccedsearchstarterpacksskeletongo26) `:26`


</details>


[function] name: UnspeccedSearchStarterPacksSkeleton file: api/bsky/unspeccedsearchStarterPacksSkeleton.go:26 returns_error: да description: UnspeccedSearchStarterPacksSkeleton calls the XRPC method "app.bsky.unspecced.searchStarterPacksSkeleton".

cursor: Opti


### UnspeccedSearchStarterPacksSkeleton (api/bsky/unspeccedsearchStarterPacksSkeleton.go:26)


UnspeccedSearchStarterPacksSkeleton calls the XRPC method "app.bsky.unspecced.searchStarterPacksSkeleton".

cursor: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
q: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.
viewer: DID of the account making the request (not included for public/unauthenticated queries).


```go
func UnspeccedSearchStarterPacksSkeleton((*UnspeccedSearchStarterPacksSkeleton_Output, error)) (*UnspeccedSearchStarterPacksSkeleton_Output, error)
```


**Тип запроса:** UnspeccedSearchStarterPacksSkeleton_Output


```json
{
  "cursor": "string",
  "hitsTotal": 0,
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedsearchStarterPacksSkeleton.go`


**Тип ответа:** UnspeccedSearchStarterPacksSkeleton_Output


```json
{
  "cursor": "string",
  "hitsTotal": 0,
  "starterPacks": []
}
```


*Определено в:* `api/bsky/unspeccedsearchStarterPacksSkeleton.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*UnspeccedSearchStarterPacksSkeleton_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/unspeccedsearchStarterPacksSkeleton.go:26`




## api/bsky/videogetJobStatus.go


📄 Исходный файл: `api/bsky/videogetJobStatus.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [VideoGetJobStatus](#videogetjobstatus-apibskyvideogetjobstatusgo19) `:19`


</details>


[function] name: VideoGetJobStatus file: api/bsky/videogetJobStatus.go:19 returns_error: да description: VideoGetJobStatus calls the XRPC method "app.bsky.video.getJobStatus".


### VideoGetJobStatus (api/bsky/videogetJobStatus.go:19)


VideoGetJobStatus calls the XRPC method "app.bsky.video.getJobStatus".


```go
func VideoGetJobStatus((*VideoGetJobStatus_Output, error)) (*VideoGetJobStatus_Output, error)
```


**Тип запроса:** VideoGetJobStatus_Output


```json
{
  "jobStatus": null
}
```


*Определено в:* `api/bsky/videogetJobStatus.go`


**Тип ответа:** VideoGetJobStatus_Output


```json
{
  "jobStatus": null
}
```


*Определено в:* `api/bsky/videogetJobStatus.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VideoGetJobStatus_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/videogetJobStatus.go:19`




## api/bsky/videogetUploadLimits.go


📄 Исходный файл: `api/bsky/videogetUploadLimits.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [VideoGetUploadLimits](#videogetuploadlimits-apibskyvideogetuploadlimitsgo23) `:23`


</details>


[function] name: VideoGetUploadLimits file: api/bsky/videogetUploadLimits.go:23 returns_error: да description: VideoGetUploadLimits calls the XRPC method "app.bsky.video.getUploadLimits".


### VideoGetUploadLimits (api/bsky/videogetUploadLimits.go:23)


VideoGetUploadLimits calls the XRPC method "app.bsky.video.getUploadLimits".


```go
func VideoGetUploadLimits((*VideoGetUploadLimits_Output, error)) (*VideoGetUploadLimits_Output, error)
```


**Тип запроса:** VideoGetUploadLimits_Output


```json
{
  "canUpload": false,
  "error": "string",
  "message": "string",
  "remainingDailyBytes": 0,
  "remainingDailyVideos": 0
}
```


*Определено в:* `api/bsky/videogetUploadLimits.go`


**Тип ответа:** VideoGetUploadLimits_Output


```json
{
  "canUpload": false,
  "error": "string",
  "message": "string",
  "remainingDailyBytes": 0,
  "remainingDailyVideos": 0
}
```


*Определено в:* `api/bsky/videogetUploadLimits.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VideoGetUploadLimits_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/videogetUploadLimits.go:23`




## api/bsky/videouploadVideo.go


📄 Исходный файл: `api/bsky/videouploadVideo.go`


<details open>
<summary><b>Функции в этом файле (1)</b></summary>


- 🔗 [VideoUploadVideo](#videouploadvideo-apibskyvideouploadvideogo20) `:20`


</details>


[function] name: VideoUploadVideo file: api/bsky/videouploadVideo.go:20 returns_error: да description: VideoUploadVideo calls the XRPC method "app.bsky.video.uploadVideo".


### VideoUploadVideo (api/bsky/videouploadVideo.go:20)


VideoUploadVideo calls the XRPC method "app.bsky.video.uploadVideo".


```go
func VideoUploadVideo((*VideoUploadVideo_Output, error)) (*VideoUploadVideo_Output, error)
```


**Тип запроса:** VideoUploadVideo_Output


```json
{
  "jobStatus": null
}
```


*Определено в:* `api/bsky/videouploadVideo.go`


**Тип ответа:** VideoUploadVideo_Output


```json
{
  "jobStatus": null
}
```


*Определено в:* `api/bsky/videouploadVideo.go`


**Возвращаемые ошибки:** функция возвращает `error`; при ошибке вызывающий код получает ненулевой `error` (см. сигнатуру выше).


*Типы возврата:* `*VideoUploadVideo_Output`, `error`


*Пример возврата ошибки:* `return nil, err` (или `return nil, fmt.Errorf("...")`)


📍 *Расположение:* `api/bsky/videouploadVideo.go:20`





---


## Навигация


- [К оглавлению документации](../../README.md)

- [К индексу функций](../functions.md)

- [К разделам](../)

- [Предыдущая директория](api_atproto.md)

- [Следующая директория](api_chat.md)


---

