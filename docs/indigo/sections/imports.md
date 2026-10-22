---
title: Импорты
type: imports
repo: indigo
language: ru
chunk_boundary: h3
---


# Импорты


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


**Модуль:** `github.com/bluesky-social/indigo`


Файл сгенерирован из Go‑исходников и показывает использование импортов.


## Стандартная библиотека



---


[import] path: archive/tar type: stdlib


### archive/tar


- **Тип:** stdlib

- **Алиасы:** `tar`



### Вызовы


`NewWriter`


### Кандидаты на типы


`Header`


### Селекторы (любое использование `pkg.X`)


`Header`, `NewWriter`, `gz`


### Используется в файлах


- 📄 `cmd/netsync/main.go`




---


[import] path: bufio type: stdlib


### bufio


- **Тип:** stdlib

- **Алиасы:** `bufio`



### Вызовы


`NewReader`, `NewScanner`


### Кандидаты на типы


`Reader`


### Селекторы (любое использование `pkg.X`)


`NewReader`, `NewScanner`, `Reader`, `ScanLines`


### Используется в файлах


- 📄 `automod/keyword/cmd/kw-cli/main.go`

- 📄 `carstore/bs.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/gosky/account.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `repo/carutil/reader.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `search/bulk.go`




---


[import] path: bytes type: stdlib


### bytes


- **Тип:** stdlib

- **Алиасы:** `bytes`



### Вызовы


`Clone`, `Compare`, `Equal`, `NewBuffer`, `NewReader`


### Кандидаты на типы


`Buffer`


### Селекторы (любое использование `pkg.X`)


`Buffer`, `Clone`, `Compare`, `Equal`, `NewBuffer`, `NewReader`


### Используется в файлах


- 📄 `api/atproto/syncgetBlob.go`

- 📄 `api/atproto/syncgetBlocks.go`

- 📄 `api/atproto/syncgetCheckout.go`

- 📄 `api/atproto/syncgetRecord.go`

- 📄 `api/atproto/syncgetRepo.go`

- 📄 `api/bsky/actorprofile.go`

- 📄 `api/bsky/actorstatus.go`

- 📄 `api/bsky/embedrecordWithMedia.go`

- 📄 `api/bsky/feedgenerator.go`

- 📄 `api/bsky/feedpost.go`

- 📄 `api/bsky/feedpostgate.go`

- 📄 `api/bsky/feedthreadgate.go`

- 📄 `api/bsky/graphlist.go`

- 📄 `api/bsky/labelerservice.go`

- 📄 `api/bsky/richtextfacet.go`

- 📄 `api/chat/actorexportAccountData.go`

- 📄 `atproto/atclient/apiclient.go`

- 📄 `atproto/atclient/lexclient.go`

- 📄 `atproto/atdata/blob.go`

- 📄 `atproto/atdata/extract.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/labeling/label.go`

- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/commit.go`

- 📄 `atproto/repo/mst/encoding.go`

- 📄 `atproto/repo/mst/node.go`

- 📄 `atproto/repo/mst/verify.go`

- 📄 `atproto/repo/sync.go`

- 📄 `automod/capture/fetch.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/engine/ruleset.go`

- 📄 `automod/engine/slack.go`

- 📄 `automod/rules/keyword.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `automod/visual/prescreen.go`

- 📄 `backfill/backfill.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/slack.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/gosky/bgs.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/relay/forward.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/relay/stream/events.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/webhook_client.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `fakedata/generators.go`

- 📄 `lex/gen.go`

- 📄 `lex/util/decoder.go`

- 📄 `lex/util/lex_types.go`

- 📄 `lex/util/util.go`

- 📄 `repo/repo.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/firehose.go`

- 📄 `search/indexing.go`

- 📄 `search/query.go`

- 📄 `util/labels/labels.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: compress/gzip type: stdlib


### compress/gzip


- **Тип:** stdlib

- **Алиасы:** `gzip`



### Вызовы


`NewReader`, `NewWriter`


### Селекторы (любое использование `pkg.X`)


`NewReader`, `NewWriter`


### Используется в файлах


- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/netsync/main.go`




---


[import] path: context type: stdlib


### context


- **Тип:** stdlib

- **Алиасы:** `context`



### Вызовы


`Background`, `TODO`, `WithCancel`, `WithTimeout`, `WithValue`


### Селекторы (любое использование `pkg.X`)


`Background`, `CancelFunc`, `Context`, `TODO`, `WithCancel`, `WithTimeout`, `WithValue`


### Используется в файлах


- 📄 `api/agnostic/actorgetPreferences.go`

- 📄 `api/agnostic/actorputPreferences.go`

- 📄 `api/agnostic/identitygetRecommendedDidCredentials.go`

- 📄 `api/agnostic/identitysignPlcOperation.go`

- 📄 `api/agnostic/identitysubmitPlcOperation.go`

- 📄 `api/agnostic/repoapplyWrites.go`

- 📄 `api/agnostic/repocreateRecord.go`

- 📄 `api/agnostic/repogetRecord.go`

- 📄 `api/agnostic/repolistRecords.go`

- 📄 `api/agnostic/repoputRecord.go`

- 📄 `api/atproto/admindeleteAccount.go`

- 📄 `api/atproto/admindisableAccountInvites.go`

- 📄 `api/atproto/admindisableInviteCodes.go`

- 📄 `api/atproto/adminenableAccountInvites.go`

- 📄 `api/atproto/admingetAccountInfo.go`

- 📄 `api/atproto/admingetAccountInfos.go`

- 📄 `api/atproto/admingetInviteCodes.go`

- 📄 `api/atproto/admingetSubjectStatus.go`

- 📄 `api/atproto/adminsearchAccounts.go`

- 📄 `api/atproto/adminsendEmail.go`

- 📄 `api/atproto/adminupdateAccountEmail.go`

- 📄 `api/atproto/adminupdateAccountHandle.go`

- 📄 `api/atproto/adminupdateAccountPassword.go`

- 📄 `api/atproto/adminupdateAccountSigningKey.go`

- 📄 `api/atproto/adminupdateSubjectStatus.go`

- 📄 `api/atproto/identitygetRecommendedDidCredentials.go`

- 📄 `api/atproto/identityrefreshIdentity.go`

- 📄 `api/atproto/identityrequestPlcOperationSignature.go`

- 📄 `api/atproto/identityresolveDid.go`

- 📄 `api/atproto/identityresolveHandle.go`

- 📄 `api/atproto/identityresolveIdentity.go`

- 📄 `api/atproto/identitysignPlcOperation.go`

- 📄 `api/atproto/identitysubmitPlcOperation.go`

- 📄 `api/atproto/identityupdateHandle.go`

- 📄 `api/atproto/labelqueryLabels.go`

- 📄 `api/atproto/moderationcreateReport.go`

- 📄 `api/atproto/repoapplyWrites.go`

- 📄 `api/atproto/repocreateRecord.go`

- 📄 `api/atproto/repodeleteRecord.go`

- 📄 `api/atproto/repodescribeRepo.go`

- 📄 `api/atproto/repogetRecord.go`

- 📄 `api/atproto/repoimportRepo.go`

- 📄 `api/atproto/repolistMissingBlobs.go`

- 📄 `api/atproto/repolistRecords.go`

- 📄 `api/atproto/repoputRecord.go`

- 📄 `api/atproto/repouploadBlob.go`

- 📄 `api/atproto/serveractivateAccount.go`

- 📄 `api/atproto/servercheckAccountStatus.go`

- 📄 `api/atproto/serverconfirmEmail.go`

- 📄 `api/atproto/servercreateAccount.go`

- 📄 `api/atproto/servercreateAppPassword.go`

- 📄 `api/atproto/servercreateInviteCode.go`

- 📄 `api/atproto/servercreateInviteCodes.go`

- 📄 `api/atproto/servercreateSession.go`

- 📄 `api/atproto/serverdeactivateAccount.go`

- 📄 `api/atproto/serverdeleteAccount.go`

- 📄 `api/atproto/serverdeleteSession.go`

- 📄 `api/atproto/serverdescribeServer.go`

- 📄 `api/atproto/servergetAccountInviteCodes.go`

- 📄 `api/atproto/servergetServiceAuth.go`

- 📄 `api/atproto/servergetSession.go`

- 📄 `api/atproto/serverlistAppPasswords.go`

- 📄 `api/atproto/serverrefreshSession.go`

- 📄 `api/atproto/serverrequestAccountDelete.go`

- 📄 `api/atproto/serverrequestEmailConfirmation.go`

- 📄 `api/atproto/serverrequestEmailUpdate.go`

- 📄 `api/atproto/serverrequestPasswordReset.go`

- 📄 `api/atproto/serverreserveSigningKey.go`

- 📄 `api/atproto/serverresetPassword.go`

- 📄 `api/atproto/serverrevokeAppPassword.go`

- 📄 `api/atproto/serverupdateEmail.go`

- 📄 `api/atproto/syncgetBlob.go`

- 📄 `api/atproto/syncgetBlocks.go`

- 📄 `api/atproto/syncgetCheckout.go`

- 📄 `api/atproto/syncgetHead.go`

- 📄 `api/atproto/syncgetHostStatus.go`

- 📄 `api/atproto/syncgetLatestCommit.go`

- 📄 `api/atproto/syncgetRecord.go`

- 📄 `api/atproto/syncgetRepo.go`

- 📄 `api/atproto/syncgetRepoStatus.go`

- 📄 `api/atproto/synclistBlobs.go`

- 📄 `api/atproto/synclistHosts.go`

- 📄 `api/atproto/synclistRepos.go`

- 📄 `api/atproto/synclistReposByCollection.go`

- 📄 `api/atproto/syncnotifyOfUpdate.go`

- 📄 `api/atproto/syncrequestCrawl.go`

- 📄 `api/atproto/tempaddReservedHandle.go`

- 📄 `api/atproto/tempcheckHandleAvailability.go`

- 📄 `api/atproto/tempcheckSignupQueue.go`

- 📄 `api/atproto/tempdereferenceScope.go`

- 📄 `api/atproto/tempfetchLabels.go`

- 📄 `api/atproto/temprequestPhoneVerification.go`

- 📄 `api/atproto/temprevokeAccountCredentials.go`

- 📄 `api/bsky/actorgetPreferences.go`

- 📄 `api/bsky/actorgetProfile.go`

- 📄 `api/bsky/actorgetProfiles.go`

- 📄 `api/bsky/actorgetSuggestions.go`

- 📄 `api/bsky/actorputPreferences.go`

- 📄 `api/bsky/actorsearchActors.go`

- 📄 `api/bsky/actorsearchActorsTypeahead.go`

- 📄 `api/bsky/ageassurancebegin.go`

- 📄 `api/bsky/ageassurancegetConfig.go`

- 📄 `api/bsky/ageassurancegetState.go`

- 📄 `api/bsky/bookmarkcreateBookmark.go`

- 📄 `api/bsky/bookmarkdeleteBookmark.go`

- 📄 `api/bsky/bookmarkgetBookmarks.go`

- 📄 `api/bsky/contactdismissMatch.go`

- 📄 `api/bsky/contactgetMatches.go`

- 📄 `api/bsky/contactgetSyncStatus.go`

- 📄 `api/bsky/contactimportContacts.go`

- 📄 `api/bsky/contactremoveData.go`

- 📄 `api/bsky/contactsendNotification.go`

- 📄 `api/bsky/contactstartPhoneVerification.go`

- 📄 `api/bsky/contactverifyPhone.go`

- 📄 `api/bsky/draftcreateDraft.go`

- 📄 `api/bsky/draftdeleteDraft.go`

- 📄 `api/bsky/draftgetDrafts.go`

- 📄 `api/bsky/draftupdateDraft.go`

- 📄 `api/bsky/feeddescribeFeedGenerator.go`

- 📄 `api/bsky/feedgetActorFeeds.go`

- 📄 `api/bsky/feedgetActorLikes.go`

- 📄 `api/bsky/feedgetAuthorFeed.go`

- 📄 `api/bsky/feedgetFeed.go`

- 📄 `api/bsky/feedgetFeedGenerator.go`

- 📄 `api/bsky/feedgetFeedGenerators.go`

- 📄 `api/bsky/feedgetFeedSkeleton.go`

- 📄 `api/bsky/feedgetLikes.go`

- 📄 `api/bsky/feedgetListFeed.go`

- 📄 `api/bsky/feedgetPostThread.go`

- 📄 `api/bsky/feedgetPosts.go`

- 📄 `api/bsky/feedgetQuotes.go`

- 📄 `api/bsky/feedgetRepostedBy.go`

- 📄 `api/bsky/feedgetSuggestedFeeds.go`

- 📄 `api/bsky/feedgetTimeline.go`

- 📄 `api/bsky/feedsearchPosts.go`

- 📄 `api/bsky/feedsendInteractions.go`

- 📄 `api/bsky/graphgetActorStarterPacks.go`

- 📄 `api/bsky/graphgetBlocks.go`

- 📄 `api/bsky/graphgetFollowers.go`

- 📄 `api/bsky/graphgetFollows.go`

- 📄 `api/bsky/graphgetKnownFollowers.go`

- 📄 `api/bsky/graphgetList.go`

- 📄 `api/bsky/graphgetListBlocks.go`

- 📄 `api/bsky/graphgetListMutes.go`

- 📄 `api/bsky/graphgetLists.go`

- 📄 `api/bsky/graphgetListsWithMembership.go`

- 📄 `api/bsky/graphgetMutes.go`

- 📄 `api/bsky/graphgetRelationships.go`

- 📄 `api/bsky/graphgetStarterPack.go`

- 📄 `api/bsky/graphgetStarterPacks.go`

- 📄 `api/bsky/graphgetStarterPacksWithMembership.go`

- 📄 `api/bsky/graphgetSuggestedFollowsByActor.go`

- 📄 `api/bsky/graphmuteActor.go`

- 📄 `api/bsky/graphmuteActorList.go`

- 📄 `api/bsky/graphmuteThread.go`

- 📄 `api/bsky/graphsearchStarterPacks.go`

- 📄 `api/bsky/graphunmuteActor.go`

- 📄 `api/bsky/graphunmuteActorList.go`

- 📄 `api/bsky/graphunmuteThread.go`

- 📄 `api/bsky/labelergetServices.go`

- 📄 `api/bsky/notificationgetPreferences.go`

- 📄 `api/bsky/notificationgetUnreadCount.go`

- 📄 `api/bsky/notificationlistActivitySubscriptions.go`

- 📄 `api/bsky/notificationlistNotifications.go`

- 📄 `api/bsky/notificationputActivitySubscription.go`

- 📄 `api/bsky/notificationputPreferences.go`

- 📄 `api/bsky/notificationputPreferencesV2.go`

- 📄 `api/bsky/notificationregisterPush.go`

- 📄 `api/bsky/notificationunregisterPush.go`

- 📄 `api/bsky/notificationupdateSeen.go`

- 📄 `api/bsky/unspeccedgetAgeAssuranceState.go`

- 📄 `api/bsky/unspeccedgetConfig.go`

- 📄 `api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go`

- 📄 `api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go`

- 📄 `api/bsky/unspeccedgetPopularFeedGenerators.go`

- 📄 `api/bsky/unspeccedgetPostThreadOtherV2.go`

- 📄 `api/bsky/unspeccedgetPostThreadV2.go`

- 📄 `api/bsky/unspeccedgetSuggestedFeeds.go`

- 📄 `api/bsky/unspeccedgetSuggestedFeedsSkeleton.go`

- 📄 `api/bsky/unspeccedgetSuggestedStarterPacks.go`

- 📄 `api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go`

- 📄 `api/bsky/unspeccedgetSuggestedUsers.go`

- 📄 `api/bsky/unspeccedgetSuggestedUsersSkeleton.go`

- 📄 `api/bsky/unspeccedgetSuggestionsSkeleton.go`

- 📄 `api/bsky/unspeccedgetTaggedSuggestions.go`

- 📄 `api/bsky/unspeccedgetTrendingTopics.go`

- 📄 `api/bsky/unspeccedgetTrends.go`

- 📄 `api/bsky/unspeccedgetTrendsSkeleton.go`

- 📄 `api/bsky/unspeccedinitAgeAssurance.go`

- 📄 `api/bsky/unspeccedsearchActorsSkeleton.go`

- 📄 `api/bsky/unspeccedsearchPostsSkeleton.go`

- 📄 `api/bsky/unspeccedsearchStarterPacksSkeleton.go`

- 📄 `api/bsky/videogetJobStatus.go`

- 📄 `api/bsky/videogetUploadLimits.go`

- 📄 `api/bsky/videouploadVideo.go`

- 📄 `api/chat/actordeleteAccount.go`

- 📄 `api/chat/actorexportAccountData.go`

- 📄 `api/chat/convoacceptConvo.go`

- 📄 `api/chat/convoaddReaction.go`

- 📄 `api/chat/convodeleteMessageForSelf.go`

- 📄 `api/chat/convogetConvo.go`

- 📄 `api/chat/convogetConvoAvailability.go`

- 📄 `api/chat/convogetConvoForMembers.go`

- 📄 `api/chat/convogetLog.go`

- 📄 `api/chat/convogetMessages.go`

- 📄 `api/chat/convoleaveConvo.go`

- 📄 `api/chat/convolistConvos.go`

- 📄 `api/chat/convomuteConvo.go`

- 📄 `api/chat/convoremoveReaction.go`

- 📄 `api/chat/convosendMessage.go`

- 📄 `api/chat/convosendMessageBatch.go`

- 📄 `api/chat/convounmuteConvo.go`

- 📄 `api/chat/convoupdateAllRead.go`

- 📄 `api/chat/convoupdateRead.go`

- 📄 `api/chat/moderationgetActorMetadata.go`

- 📄 `api/chat/moderationgetMessageContext.go`

- 📄 `api/chat/moderationupdateActorAccess.go`

- 📄 `api/ozone/communicationcreateTemplate.go`

- 📄 `api/ozone/communicationdeleteTemplate.go`

- 📄 `api/ozone/communicationlistTemplates.go`

- 📄 `api/ozone/communicationupdateTemplate.go`

- 📄 `api/ozone/hostinggetAccountHistory.go`

- 📄 `api/ozone/moderationcancelScheduledActions.go`

- 📄 `api/ozone/moderationemitEvent.go`

- 📄 `api/ozone/moderationgetAccountTimeline.go`

- 📄 `api/ozone/moderationgetEvent.go`

- 📄 `api/ozone/moderationgetRecord.go`

- 📄 `api/ozone/moderationgetRecords.go`

- 📄 `api/ozone/moderationgetRepo.go`

- 📄 `api/ozone/moderationgetReporterStats.go`

- 📄 `api/ozone/moderationgetRepos.go`

- 📄 `api/ozone/moderationgetSubjects.go`

- 📄 `api/ozone/moderationlistScheduledActions.go`

- 📄 `api/ozone/moderationqueryEvents.go`

- 📄 `api/ozone/moderationqueryStatuses.go`

- 📄 `api/ozone/moderationscheduleAction.go`

- 📄 `api/ozone/moderationsearchRepos.go`

- 📄 `api/ozone/safelinkaddRule.go`

- 📄 `api/ozone/safelinkqueryEvents.go`

- 📄 `api/ozone/safelinkqueryRules.go`

- 📄 `api/ozone/safelinkremoveRule.go`

- 📄 `api/ozone/safelinkupdateRule.go`

- 📄 `api/ozone/servergetConfig.go`

- 📄 `api/ozone/setaddValues.go`

- 📄 `api/ozone/setdeleteSet.go`

- 📄 `api/ozone/setdeleteValues.go`

- 📄 `api/ozone/setgetValues.go`

- 📄 `api/ozone/setquerySets.go`

- 📄 `api/ozone/settinglistOptions.go`

- 📄 `api/ozone/settingremoveOptions.go`

- 📄 `api/ozone/settingupsertOption.go`

- 📄 `api/ozone/setupsertSet.go`

- 📄 `api/ozone/signaturefindCorrelation.go`

- 📄 `api/ozone/signaturefindRelatedAccounts.go`

- 📄 `api/ozone/signaturesearchAccounts.go`

- 📄 `api/ozone/teamaddMember.go`

- 📄 `api/ozone/teamdeleteMember.go`

- 📄 `api/ozone/teamlistMembers.go`

- 📄 `api/ozone/teamupdateMember.go`

- 📄 `api/ozone/verificationgrantVerifications.go`

- 📄 `api/ozone/verificationlistVerifications.go`

- 📄 `api/ozone/verificationrevokeVerifications.go`

- 📄 `atproto/atclient/apiclient.go`

- 📄 `atproto/atclient/apirequest.go`

- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/atclient/lexclient.go`

- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/atcrypto/cmd/atp-crypto/main.go`

- 📄 `atproto/auth/http.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/memstore.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/resolver.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/auth/oauth/store.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/base_directory.go`

- 📄 `atproto/identity/cache_directory.go`

- 📄 `atproto/identity/cmd/atp-id/main.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/directory.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/identity/mock_directory.go`

- 📄 `atproto/identity/nsid.go`

- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `atproto/identity/resolver.go`

- 📄 `atproto/lexicon/cmd/lextool/main.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/lexicon/resolve.go`

- 📄 `atproto/lexicon/resolving_catalog.go`

- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/repo/mst/encoding.go`

- 📄 `atproto/repo/mst/tree.go`

- 📄 `atproto/repo/repo.go`

- 📄 `atproto/repo/sync.go`

- 📄 `atproto/repo/tiny_blockstore.go`

- 📄 `atproto/syntax/cmd/atp-syntax/main.go`

- 📄 `automod/cachestore/cachestore.go`

- 📄 `automod/cachestore/cachestore_mem.go`

- 📄 `automod/cachestore/cachestore_redis.go`

- 📄 `automod/capture/capture.go`

- 📄 `automod/capture/fetch.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `automod/countstore/countstore.go`

- 📄 `automod/countstore/countstore_mem.go`

- 📄 `automod/countstore/countstore_redis.go`

- 📄 `automod/engine/context.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/engine_ozone.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/fetch_relationship.go`

- 📄 `automod/engine/notifier.go`

- 📄 `automod/engine/persist.go`

- 📄 `automod/engine/persisthelpers.go`

- 📄 `automod/engine/slack.go`

- 📄 `automod/flagstore/flagstore.go`

- 📄 `automod/flagstore/flagstore_mem.go`

- 📄 `automod/flagstore/flagstore_redis.go`

- 📄 `automod/keyword/cmd/kw-cli/main.go`

- 📄 `automod/setstore/setstore.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `automod/visual/prescreen.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/gormstore.go`

- 📄 `backfill/memstore.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/last_shard_cache.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/main.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/beemo/slack.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/firehose.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/account.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/did.go`

- 📄 `cmd/gosky/handle.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/relay/crawl.go`

- 📄 `cmd/relay/relay/domain_ban.go`

- 📄 `cmd/relay/relay/host.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/stream/eventmgr/event_manager.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/stream/persist/persist.go`

- 📄 `cmd/relay/stream/scheduler.go`

- 📄 `cmd/relay/stream/schedulers/parallel/parallel.go`

- 📄 `cmd/relay/stream/schedulers/sequential/sequential.go`

- 📄 `cmd/relay/testing/consumer.go`

- 📄 `cmd/relay/testing/producer.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/main.go`

- 📄 `cmd/tap/outbox.go`

- 📄 `cmd/tap/repo_manager.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/server.go`

- 📄 `cmd/tap/tap.go`

- 📄 `cmd/tap/util.go`

- 📄 `events/consumer.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `events/persist.go`

- 📄 `events/schedulers/autoscaling/autoscaling.go`

- 📄 `events/schedulers/parallel/parallel.go`

- 📄 `events/schedulers/sequential/sequential.go`

- 📄 `events/yolopersist/yolopersist.go`

- 📄 `fakedata/accounts.go`

- 📄 `fakedata/generators.go`

- 📄 `lex/util/client.go`

- 📄 `mst/diff.go`

- 📄 `mst/mst.go`

- 📄 `mst/mst_util.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/keymgr/keymgr.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/bulk.go`

- 📄 `search/firehose.go`

- 📄 `search/handlers.go`

- 📄 `search/indexing.go`

- 📄 `search/parse_query.go`

- 📄 `search/query.go`

- 📄 `search/server.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/handlers.go`

- 📄 `splitter/ringbuf.go`

- 📄 `splitter/splitter.go`

- 📄 `testing/utils.go`

- 📄 `util/fakekey.go`

- 📄 `util/http.go`

- 📄 `util/readrecordbs.go`

- 📄 `util/tracing/tracing.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: crypto type: stdlib


### crypto


- **Тип:** stdlib

- **Алиасы:** `crypto`



### Селекторы (любое использование `pkg.X`)


`Hash`, `SHA256`


### Используется в файлах


- 📄 `atproto/atcrypto/k256.go`

- 📄 `atproto/auth/jwt_signing.go`

- 📄 `atproto/auth/oauth/jwt_signing.go`




---


[import] path: crypto/ecdh type: stdlib


### crypto/ecdh


- **Тип:** stdlib

- **Алиасы:** `ecdh`



### Вызовы


`P256`


### Кандидаты на типы


`PrivateKey`


### Селекторы (любое использование `pkg.X`)


`P256`, `PrivateKey`


### Используется в файлах


- 📄 `atproto/atcrypto/p256.go`




---


[import] path: crypto/ecdsa type: stdlib


### crypto/ecdsa


- **Тип:** stdlib

- **Алиасы:** `ecdsa`



### Вызовы


`GenerateKey`, `Sign`, `Verify`


### Кандидаты на типы


`PrivateKey`, `PublicKey`


### Селекторы (любое использование `pkg.X`)


`GenerateKey`, `PrivateKey`, `PublicKey`, `Sign`, `Verify`


### Используется в файлах


- 📄 `atproto/atcrypto/jwk.go`

- 📄 `atproto/atcrypto/p256.go`

- 📄 `util/cliutil/key.go`




---


[import] path: crypto/elliptic type: stdlib


### crypto/elliptic


- **Тип:** stdlib

- **Алиасы:** `elliptic`



### Вызовы


`Marshal`, `MarshalCompressed`, `P256`, `Unmarshal`, `UnmarshalCompressed`


### Селекторы (любое использование `pkg.X`)


`Marshal`, `MarshalCompressed`, `P256`, `Unmarshal`, `UnmarshalCompressed`


### Используется в файлах


- 📄 `atproto/atcrypto/jwk.go`

- 📄 `atproto/atcrypto/p256.go`

- 📄 `atproto/atcrypto/p256_lowS.go`

- 📄 `util/cliutil/key.go`




---


[import] path: crypto/rand type: stdlib


### crypto/rand


- **Тип:** stdlib

- **Алиасы:** `rand`



### Вызовы


`Read`


### Селекторы (любое использование `pkg.X`)


`Read`, `Reader`


### Используется в файлах


- 📄 `atproto/atcrypto/k256.go`

- 📄 `atproto/atcrypto/p256.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/util.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/stress/main.go`

- 📄 `testing/utils.go`

- 📄 `util/cliutil/key.go`




---


[import] path: crypto/sha256 type: stdlib


### crypto/sha256


- **Тип:** stdlib

- **Алиасы:** `sha256`



### Вызовы


`Sum256`


### Селекторы (любое использование `pkg.X`)


`Sum256`


### Используется в файлах


- 📄 `atproto/atcrypto/k256.go`

- 📄 `atproto/atcrypto/p256.go`

- 📄 `atproto/auth/oauth/util.go`

- 📄 `atproto/repo/mst/util.go`




---


[import] path: crypto/subtle type: stdlib


### crypto/subtle


- **Тип:** stdlib

- **Алиасы:** `subtle`



### Вызовы


`ConstantTimeCompare`


### Селекторы (любое использование `pkg.X`)


`ConstantTimeCompare`


### Используется в файлах


- 📄 `atproto/auth/http.go`

- 📄 `cmd/relay/service.go`




---


[import] path: crypto/tls type: stdlib


### crypto/tls


- **Тип:** stdlib

- **Алиасы:** `tls`



### Кандидаты на типы


`Config`


### Селекторы (любое использование `pkg.X`)


`Config`


### Используется в файлах


- 📄 `cmd/palomar/main.go`




---


[import] path: crypto/x509 type: stdlib


### crypto/x509


- **Тип:** stdlib

- **Алиасы:** `x509`



### Вызовы


`MarshalPKCS8PrivateKey`, `ParsePKCS8PrivateKey`


### Селекторы (любое использование `pkg.X`)


`MarshalPKCS8PrivateKey`, `ParsePKCS8PrivateKey`


### Используется в файлах


- 📄 `atproto/atcrypto/p256.go`




---


[import] path: database/sql type: stdlib


### database/sql


- **Тип:** stdlib

- **Алиасы:** `sql`



### Вызовы


`Open`


### Кандидаты на типы


`DB`, `TxOptions`


### Селекторы (любое использование `pkg.X`)


`DB`, `NullString`, `Open`, `TxOptions`


### Используется в файлах


- 📄 `carstore/sqlite_store.go`

- 📄 `models/models.go`




---


[import] path: database/sql/driver type: stdlib


### database/sql/driver


- **Тип:** stdlib

- **Алиасы:** `driver`



### Селекторы (любое использование `pkg.X`)


`Value`


### Используется в файлах


- 📄 `models/dbcid.go`




---


[import] path: embed type: stdlib


### embed


- **Тип:** stdlib

- **Алиасы:** `_`, `embed`



### Селекторы (любое использование `pkg.X`)


`FS`


### Используется в файлах


- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/lexicon/catalog.go`

- 📄 `search/indexing.go`




---


[import] path: encoding type: stdlib


### encoding


- **Тип:** stdlib

- **Алиасы:** `encoding`



### Селекторы (любое использование `pkg.X`)


`TextMarshaler`


### Используется в файлах


- 📄 `atproto/atclient/params.go`

- 📄 `atproto/atdata/parse.go`




---


[import] path: encoding/base32 type: stdlib


### encoding/base32


- **Тип:** stdlib

- **Алиасы:** `base32`



### Вызовы


`NewEncoding`


### Кандидаты на типы


`Encoding`


### Селекторы (любое использование `pkg.X`)


`Encoding`, `NewEncoding`, `NoPadding`, `StdEncoding`


### Используется в файлах


- 📄 `atproto/syntax/tid.go`

- 📄 `testing/utils.go`




---


[import] path: encoding/base64 type: stdlib


### encoding/base64


- **Тип:** stdlib

- **Алиасы:** `base64`



### Селекторы (любое использование `pkg.X`)


`RawStdEncoding`, `RawURLEncoding`, `StdEncoding`, `URLEncoding`


### Используется в файлах


- 📄 `atproto/atcrypto/jwk.go`

- 📄 `atproto/atdata/bytes.go`

- 📄 `atproto/atdata/parse.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/util.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/service.go`

- 📄 `lex/util/lex_types.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: encoding/binary type: stdlib


### encoding/binary


- **Тип:** stdlib

- **Алиасы:** `binary`



### Вызовы


`PutUvarint`, `ReadUvarint`


### Селекторы (любое использование `pkg.X`)


`BigEndian`, `LittleEndian`, `MaxVarintLen64`, `PutUvarint`, `ReadUvarint`


### Используется в файлах


- 📄 `atproto/atcrypto/keys.go`

- 📄 `carstore/util.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `repo/carutil/reader.go`




---


[import] path: encoding/csv type: stdlib


### encoding/csv


- **Тип:** stdlib

- **Алиасы:** `csv`



### Вызовы


`NewReader`, `NewWriter`


### Селекторы (любое использование `pkg.X`)


`NewReader`, `NewWriter`, `gz`


### Используется в файлах


- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/serve.go`




---


[import] path: encoding/hex type: stdlib


### encoding/hex


- **Тип:** stdlib

- **Алиасы:** `hex`



### Вызовы


`DecodeString`, `EncodeToString`


### Селекторы (любое использование `pkg.X`)


`DecodeString`, `EncodeToString`


### Используется в файлах


- 📄 `cmd/stress/main.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `search/bulk.go`




---


[import] path: encoding/json type: stdlib


### encoding/json


- **Тип:** stdlib

- **Алиасы:** `json`



### Вызовы


`Marshal`, `MarshalIndent`, `NewDecoder`, `NewEncoder`, `RawMessage`, `Unmarshal`


### Кандидаты на типы


`RawMessage`


### Селекторы (любое использование `pkg.X`)


`Marshal`, `MarshalIndent`, `NewDecoder`, `NewEncoder`, `RawMessage`, `Unmarshal`


### Используется в файлах


- 📄 `api/agnostic/identitygetRecommendedDidCredentials.go`

- 📄 `api/agnostic/identitysignPlcOperation.go`

- 📄 `api/agnostic/identitysubmitPlcOperation.go`

- 📄 `api/agnostic/repoapplyWrites.go`

- 📄 `api/agnostic/repogetRecord.go`

- 📄 `api/agnostic/repolistRecords.go`

- 📄 `api/atproto/admingetSubjectStatus.go`

- 📄 `api/atproto/adminupdateSubjectStatus.go`

- 📄 `api/atproto/moderationcreateReport.go`

- 📄 `api/atproto/repoapplyWrites.go`

- 📄 `api/atproto/tempcheckHandleAvailability.go`

- 📄 `api/bsky/actordefs.go`

- 📄 `api/bsky/actorprofile.go`

- 📄 `api/bsky/actorstatus.go`

- 📄 `api/bsky/ageassurancedefs.go`

- 📄 `api/bsky/bookmarkdefs.go`

- 📄 `api/bsky/draftdefs.go`

- 📄 `api/bsky/embedrecord.go`

- 📄 `api/bsky/embedrecordWithMedia.go`

- 📄 `api/bsky/feeddefs.go`

- 📄 `api/bsky/feedgenerator.go`

- 📄 `api/bsky/feedgetPostThread.go`

- 📄 `api/bsky/feedpost.go`

- 📄 `api/bsky/feedpostgate.go`

- 📄 `api/bsky/feedthreadgate.go`

- 📄 `api/bsky/graphgetRelationships.go`

- 📄 `api/bsky/graphlist.go`

- 📄 `api/bsky/labelergetServices.go`

- 📄 `api/bsky/labelerservice.go`

- 📄 `api/bsky/richtextfacet.go`

- 📄 `api/bsky/unspeccedgetPostThreadOtherV2.go`

- 📄 `api/bsky/unspeccedgetPostThreadV2.go`

- 📄 `api/chat/convodefs.go`

- 📄 `api/chat/convogetLog.go`

- 📄 `api/chat/convogetMessages.go`

- 📄 `api/chat/moderationgetMessageContext.go`

- 📄 `api/ozone/hostinggetAccountHistory.go`

- 📄 `api/ozone/moderationdefs.go`

- 📄 `api/ozone/moderationemitEvent.go`

- 📄 `api/ozone/moderationgetRecords.go`

- 📄 `api/ozone/moderationgetRepos.go`

- 📄 `api/ozone/moderationscheduleAction.go`

- 📄 `api/ozone/verificationdefs.go`

- 📄 `atproto/atclient/apiclient.go`

- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/atclient/lexclient.go`

- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/atcrypto/jwk.go`

- 📄 `atproto/atdata/blob.go`

- 📄 `atproto/atdata/bytes.go`

- 📄 `atproto/atdata/cidlink.go`

- 📄 `atproto/atdata/data.go`

- 📄 `atproto/atdata/extract.go`

- 📄 `atproto/auth/http.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/resolver.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/cmd/atp-id/main.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/mock_directory.go`

- 📄 `atproto/identity/resolver.go`

- 📄 `atproto/lexicon/catalog.go`

- 📄 `atproto/lexicon/cmd/lextool/main.go`

- 📄 `atproto/lexicon/extract_type.go`

- 📄 `atproto/lexicon/language.go`

- 📄 `atproto/lexicon/resolve.go`

- 📄 `atproto/lexicon/resolving_catalog.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/fetch_relationship.go`

- 📄 `automod/engine/slack.go`

- 📄 `automod/setstore/setstore.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `automod/visual/prescreen.go`

- 📄 `cmd/beemo/slack.go`

- 📄 `cmd/bluepages/handlers.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/account.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/bgs.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/did.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/relay/testing/scenario.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/types.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `fakedata/accounts.go`

- 📄 `lex/gen.go`

- 📄 `lex/schema.go`

- 📄 `lex/util/decoder.go`

- 📄 `lex/util/lex_types.go`

- 📄 `lex/util/util.go`

- 📄 `models/dbcid.go`

- 📄 `search/bulk.go`

- 📄 `search/handlers.go`

- 📄 `search/indexing.go`

- 📄 `search/query.go`

- 📄 `util/cliutil/key.go`

- 📄 `util/cliutil/util.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: errors type: stdlib


### errors


- **Тип:** stdlib

- **Алиасы:** `errors`



### Вызовы


`As`, `Is`, `Join`, `New`


### Селекторы (любое использование `pkg.X`)


`As`, `Is`, `Join`, `New`


### Используется в файлах


- 📄 `atproto/atcrypto/keys.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/auth/oauth/types.go`

- 📄 `atproto/auth/permission.go`

- 📄 `atproto/identity/base_directory.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/directory.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/identity/nsid.go`

- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/mst/node_insert.go`

- 📄 `atproto/repo/mst/node_remove.go`

- 📄 `atproto/repo/mst/tree.go`

- 📄 `atproto/repo/repo.go`

- 📄 `atproto/syntax/atidentifier.go`

- 📄 `atproto/syntax/aturi.go`

- 📄 `atproto/syntax/cid.go`

- 📄 `atproto/syntax/datetime.go`

- 📄 `atproto/syntax/did.go`

- 📄 `atproto/syntax/handle.go`

- 📄 `atproto/syntax/language.go`

- 📄 `atproto/syntax/nsid.go`

- 📄 `atproto/syntax/path.go`

- 📄 `atproto/syntax/recordkey.go`

- 📄 `atproto/syntax/tid.go`

- 📄 `atproto/syntax/uri.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/gormstore.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/scylla_stub.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/bluepages/handlers.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/lexgen/main.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/domain_ban.go`

- 📄 `cmd/relay/relay/errors.go`

- 📄 `cmd/relay/relay/host.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/relay/stream/eventmgr/event_manager.go`

- 📄 `cmd/relay/stream/events.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/tap/util.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `lex/lexlint/syntax.go`

- 📄 `repo/carutil/reader.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/metrics.go`

- 📄 `splitter/splitter.go`

- 📄 `util/svcutil/metrics_middleware.go`




---


[import] path: fmt type: stdlib


### fmt


- **Тип:** stdlib

- **Алиасы:** `fmt`



### Вызовы


`Errorf`, `Fprint`, `Fprintf`, `Fprintln`, `Print`, `Printf`, `Println`, `Sprint`, `Sprintf`


### Кандидаты на типы


`Println`


### Селекторы (любое использование `pkg.X`)


`Errorf`, `Fprint`, `Fprintf`, `Fprintln`, `Print`, `Printf`, `Println`, `Sprint`, `Sprintf`


### Используется в файлах


- 📄 `api/agnostic/repoapplyWrites.go`

- 📄 `api/atproto/admingetSubjectStatus.go`

- 📄 `api/atproto/adminupdateSubjectStatus.go`

- 📄 `api/atproto/cbor_gen.go`

- 📄 `api/atproto/moderationcreateReport.go`

- 📄 `api/atproto/repoapplyWrites.go`

- 📄 `api/atproto/tempcheckHandleAvailability.go`

- 📄 `api/bsky/actordefs.go`

- 📄 `api/bsky/actorprofile.go`

- 📄 `api/bsky/actorstatus.go`

- 📄 `api/bsky/ageassurancedefs.go`

- 📄 `api/bsky/bookmarkdefs.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/bsky/draftdefs.go`

- 📄 `api/bsky/embedrecord.go`

- 📄 `api/bsky/embedrecordWithMedia.go`

- 📄 `api/bsky/feeddefs.go`

- 📄 `api/bsky/feedgenerator.go`

- 📄 `api/bsky/feedgetPostThread.go`

- 📄 `api/bsky/feedpost.go`

- 📄 `api/bsky/feedpostgate.go`

- 📄 `api/bsky/feedthreadgate.go`

- 📄 `api/bsky/graphgetRelationships.go`

- 📄 `api/bsky/graphlist.go`

- 📄 `api/bsky/labelergetServices.go`

- 📄 `api/bsky/labelerservice.go`

- 📄 `api/bsky/richtextfacet.go`

- 📄 `api/bsky/unspeccedgetPostThreadOtherV2.go`

- 📄 `api/bsky/unspeccedgetPostThreadV2.go`

- 📄 `api/chat/cbor_gen.go`

- 📄 `api/chat/convodefs.go`

- 📄 `api/chat/convogetLog.go`

- 📄 `api/chat/convogetMessages.go`

- 📄 `api/chat/moderationgetMessageContext.go`

- 📄 `api/ozone/hostinggetAccountHistory.go`

- 📄 `api/ozone/moderationdefs.go`

- 📄 `api/ozone/moderationemitEvent.go`

- 📄 `api/ozone/moderationgetRecords.go`

- 📄 `api/ozone/moderationgetRepos.go`

- 📄 `api/ozone/moderationscheduleAction.go`

- 📄 `api/ozone/verificationdefs.go`

- 📄 `atproto/atclient/apiclient.go`

- 📄 `atproto/atclient/apierror.go`

- 📄 `atproto/atclient/apirequest.go`

- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/atclient/lexclient.go`

- 📄 `atproto/atclient/params.go`

- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/atcrypto/cmd/atp-crypto/main.go`

- 📄 `atproto/atcrypto/jwk.go`

- 📄 `atproto/atcrypto/k256.go`

- 📄 `atproto/atcrypto/keys.go`

- 📄 `atproto/atcrypto/p256.go`

- 📄 `atproto/atdata/blob.go`

- 📄 `atproto/atdata/bytes.go`

- 📄 `atproto/atdata/cbor_gen.go`

- 📄 `atproto/atdata/cidlink.go`

- 📄 `atproto/atdata/data.go`

- 📄 `atproto/atdata/extract.go`

- 📄 `atproto/atdata/parse.go`

- 📄 `atproto/auth/http.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/jwt_signing.go`

- 📄 `atproto/auth/oauth/memstore.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/resolver.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/auth/oauth/types.go`

- 📄 `atproto/auth/oauthscope.go`

- 📄 `atproto/auth/permission.go`

- 📄 `atproto/auth/permission_util.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/base_directory.go`

- 📄 `atproto/identity/cache_directory.go`

- 📄 `atproto/identity/cmd/atp-id/main.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/identity/identity.go`

- 📄 `atproto/identity/mock_directory.go`

- 📄 `atproto/identity/nsid.go`

- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `atproto/labeling/cbor_gen.go`

- 📄 `atproto/labeling/label.go`

- 📄 `atproto/lexicon/catalog.go`

- 📄 `atproto/lexicon/cmd/lextool/main.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/lexicon/language.go`

- 📄 `atproto/lexicon/resolve.go`

- 📄 `atproto/lexicon/resolving_catalog.go`

- 📄 `atproto/lexicon/schemafile.go`

- 📄 `atproto/lexicon/validation.go`

- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/cbor_gen.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/repo/commit.go`

- 📄 `atproto/repo/mst/cbor_gen.go`

- 📄 `atproto/repo/mst/debug.go`

- 📄 `atproto/repo/mst/encoding.go`

- 📄 `atproto/repo/mst/node.go`

- 📄 `atproto/repo/mst/node_insert.go`

- 📄 `atproto/repo/mst/node_remove.go`

- 📄 `atproto/repo/mst/tree.go`

- 📄 `atproto/repo/mst/verify.go`

- 📄 `atproto/repo/operation.go`

- 📄 `atproto/repo/sync.go`

- 📄 `atproto/syntax/aturi.go`

- 📄 `atproto/syntax/cmd/atp-syntax/main.go`

- 📄 `atproto/syntax/datetime.go`

- 📄 `atproto/syntax/handle.go`

- 📄 `atproto/syntax/path.go`

- 📄 `automod/capture/fetch.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `automod/countstore/countstore.go`

- 📄 `automod/engine/blobs.go`

- 📄 `automod/engine/context.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/engine_ozone.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/fetch_relationship.go`

- 📄 `automod/engine/persist.go`

- 📄 `automod/engine/persisthelpers.go`

- 📄 `automod/engine/ruleset.go`

- 📄 `automod/engine/slack.go`

- 📄 `automod/helpers/bsky.go`

- 📄 `automod/helpers/text.go`

- 📄 `automod/keyword/cmd/kw-cli/main.go`

- 📄 `automod/rules/harassment.go`

- 📄 `automod/rules/hashtags.go`

- 📄 `automod/rules/interaction.go`

- 📄 `automod/rules/keyword.go`

- 📄 `automod/rules/mentions.go`

- 📄 `automod/rules/quick.go`

- 📄 `automod/rules/replies.go`

- 📄 `automod/rules/reposts.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `automod/visual/prescreen.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/gormstore.go`

- 📄 `backfill/memstore.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/beemo/slack.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/bluepages/handlers.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/firehose.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/account.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/bgs.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/did.go`

- 📄 `cmd/gosky/handle.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/lexgen/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/relay/crawl.go`

- 📄 `cmd/relay/relay/domain_ban.go`

- 📄 `cmd/relay/relay/host.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/models/methods.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/relay/stream/cbor_gen.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/stream/eventmgr/errors.go`

- 📄 `cmd/relay/stream/events.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `cmd/relay/testing/consumer.go`

- 📄 `cmd/relay/testing/producer.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/relay/testing/scenario.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/main.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/tap.go`

- 📄 `cmd/tap/util.go`

- 📄 `cmd/tap/webhook_client.go`

- 📄 `events/cbor_gen.go`

- 📄 `events/consumer.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `events/persist.go`

- 📄 `events/yolopersist/yolopersist.go`

- 📄 `fakedata/accounts.go`

- 📄 `fakedata/generators.go`

- 📄 `lex/gen.go`

- 📄 `lex/lexgen/codegen.go`

- 📄 `lex/lexgen/flatten.go`

- 📄 `lex/lexgen/util.go`

- 📄 `lex/lexlint/breaking.go`

- 📄 `lex/lexlint/lint.go`

- 📄 `lex/schema.go`

- 📄 `lex/type_schema.go`

- 📄 `lex/util/cbor_gen.go`

- 📄 `lex/util/decoder.go`

- 📄 `lex/util/util.go`

- 📄 `models/dbcid.go`

- 📄 `mst/cbor_gen.go`

- 📄 `mst/diff.go`

- 📄 `mst/mst.go`

- 📄 `mst/mst_util.go`

- 📄 `repo/carutil/reader.go`

- 📄 `repo/cbor_gen.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/keymgr/keymgr.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/bulk.go`

- 📄 `search/firehose.go`

- 📄 `search/handlers.go`

- 📄 `search/indexing.go`

- 📄 `search/query.go`

- 📄 `search/server.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/handlers.go`

- 📄 `splitter/splitter.go`

- 📄 `testing/utils.go`

- 📄 `util/cliutil/key.go`

- 📄 `util/cliutil/util.go`

- 📄 `util/labels/cbor_gen.go`

- 📄 `util/readrecordbs.go`

- 📄 `util/ssrf/ssrf.go`

- 📄 `util/tracing/tracing.go`

- 📄 `util/uri.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: html/template type: stdlib


### html/template


- **Тип:** stdlib

- **Алиасы:** `template`



### Вызовы


`Must`, `New`


### Селекторы (любое использование `pkg.X`)


`Must`, `New`


### Используется в файлах


- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`




---


[import] path: io type: stdlib


### io


- **Тип:** stdlib

- **Алиасы:** `io`



### Вызовы


`Copy`, `CopyN`, `LimitReader`, `NopCloser`, `ReadAll`, `ReadFull`, `TeeReader`


### Кандидаты на типы


`EOF`


### Селекторы (любое использование `pkg.X`)


`Copy`, `CopyN`, `Discard`, `EOF`, `ErrUnexpectedEOF`, `LimitReader`, `NopCloser`, `ReadAll`, `ReadCloser`, `ReadFull`, `Reader`, `SeekCurrent`, `SeekStart`, `Seeker`, `TeeReader`, `Writer`


### Используется в файлах


- 📄 `api/atproto/cbor_gen.go`

- 📄 `api/atproto/repoimportRepo.go`

- 📄 `api/atproto/repouploadBlob.go`

- 📄 `api/bsky/actorprofile.go`

- 📄 `api/bsky/actorstatus.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/bsky/embedrecordWithMedia.go`

- 📄 `api/bsky/feedgenerator.go`

- 📄 `api/bsky/feedpost.go`

- 📄 `api/bsky/feedpostgate.go`

- 📄 `api/bsky/feedthreadgate.go`

- 📄 `api/bsky/graphlist.go`

- 📄 `api/bsky/labelerservice.go`

- 📄 `api/bsky/richtextfacet.go`

- 📄 `api/bsky/videouploadVideo.go`

- 📄 `api/chat/cbor_gen.go`

- 📄 `atproto/atclient/apiclient.go`

- 📄 `atproto/atclient/apirequest.go`

- 📄 `atproto/atclient/lexclient.go`

- 📄 `atproto/atdata/blob.go`

- 📄 `atproto/atdata/bytes.go`

- 📄 `atproto/atdata/cbor_gen.go`

- 📄 `atproto/atdata/cidlink.go`

- 📄 `atproto/atdata/extract.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/labeling/cbor_gen.go`

- 📄 `atproto/lexicon/catalog.go`

- 📄 `atproto/lexicon/cmd/lextool/main.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/cbor_gen.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/repo/mst/cbor_gen.go`

- 📄 `atproto/repo/mst/encoding.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/engine/blobs.go`

- 📄 `automod/setstore/setstore.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/util.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `carstore/util.go`

- 📄 `cmd/beemo/main.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/relay/forward.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/stream/cbor_gen.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/stream/events.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `events/cbor_gen.go`

- 📄 `events/consumer.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `lex/gen.go`

- 📄 `lex/lexgen/codegen.go`

- 📄 `lex/type_schema.go`

- 📄 `lex/util/cbor_gen.go`

- 📄 `lex/util/lex_types.go`

- 📄 `lex/util/util.go`

- 📄 `mst/cbor_gen.go`

- 📄 `repo/carutil/reader.go`

- 📄 `repo/cbor_gen.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/indexing.go`

- 📄 `search/server.go`

- 📄 `splitter/handlers.go`

- 📄 `splitter/splitter.go`

- 📄 `util/labels/cbor_gen.go`

- 📄 `util/svcutil/logger.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: io/fs type: stdlib


### io/fs


- **Тип:** stdlib

- **Алиасы:** `fs`



### Вызовы


`WalkDir`


### Селекторы (любое использование `pkg.X`)


`DirEntry`, `FileInfo`, `WalkDir`


### Используется в файлах


- 📄 `atproto/lexicon/catalog.go`

- 📄 `cmd/lexgen/main.go`




---


[import] path: io/ioutil type: stdlib


### io/ioutil


- **Тип:** stdlib

- **Алиасы:** `ioutil`



### Вызовы


`ReadAll`


### Селекторы (любое использование `pkg.X`)


`ReadAll`


### Используется в файлах


- 📄 `search/query.go`




---


[import] path: log type: stdlib


### log


- **Тип:** stdlib

- **Алиасы:** `log`



### Вызовы


`Error`, `Fatal`, `Fatalf`, `Info`, `With`


### Селекторы (любое использование `pkg.X`)


`Error`, `Fatal`, `Fatalf`, `Info`, `With`


### Используется в файлах


- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/sonar/main.go`




---


[import] path: log/slog type: stdlib


### log/slog


- **Тип:** stdlib

- **Алиасы:** `slog`



### Вызовы


`Debug`, `Default`, `Error`, `Info`, `New`, `NewJSONHandler`, `NewTextHandler`, `SetDefault`, `Warn`, `With`


### Кандидаты на типы


`HandlerOptions`, `Logger`


### Селекторы (любое использование `pkg.X`)


`Debug`, `Default`, `Error`, `HandlerOptions`, `Info`, `Level`, `LevelDebug`, `LevelError`, `LevelInfo`, `LevelWarn`, `Logger`, `New`, `NewJSONHandler`, `NewTextHandler`, `SetDefault`, `Warn`, `With`


### Используется в файлах


- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/atcrypto/cmd/atp-crypto/main.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/identity/cmd/atp-id/main.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `atproto/lexicon/catalog.go`

- 📄 `atproto/lexicon/cmd/lextool/main.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/lexicon/resolve.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/repo/sync.go`

- 📄 `atproto/syntax/cmd/atp-syntax/main.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `automod/countstore/countstore.go`

- 📄 `automod/engine/context.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/testing.go`

- 📄 `automod/keyword/cmd/kw-cli/main.go`

- 📄 `automod/keyword/tokenize.go`

- 📄 `automod/rules/misleading.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `backfill/backfill.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/main.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/firehose.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/stream/eventmgr/event_manager.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/stream/schedulers/parallel/parallel.go`

- 📄 `cmd/relay/testing/consumer.go`

- 📄 `cmd/relay/testing/producer.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/main.go`

- 📄 `cmd/tap/outbox.go`

- 📄 `cmd/tap/repo_manager.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/server.go`

- 📄 `cmd/tap/tap.go`

- 📄 `cmd/tap/webhook_client.go`

- 📄 `events/consumer.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `events/schedulers/autoscaling/autoscaling.go`

- 📄 `events/schedulers/parallel/parallel.go`

- 📄 `fakedata/generators.go`

- 📄 `lex/lexgen/codegen.go`

- 📄 `lex/lexlint/breaking.go`

- 📄 `lex/lexlint/lint.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/keymgr/keymgr.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/indexing.go`

- 📄 `search/parse_query.go`

- 📄 `search/query.go`

- 📄 `search/server.go`

- 📄 `search/transform.go`

- 📄 `splitter/splitter.go`

- 📄 `util/http.go`

- 📄 `util/svcutil/logger.go`




---


[import] path: math type: stdlib


### math


- **Тип:** stdlib

- **Алиасы:** `math`



### Вызовы


`Pow`


### Кандидаты на типы


`Pow`


### Селекторы (любое использование `pkg.X`)


`E`, `Pow`


### Используется в файлах


- 📄 `api/atproto/cbor_gen.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/chat/cbor_gen.go`

- 📄 `atproto/atdata/cbor_gen.go`

- 📄 `atproto/labeling/cbor_gen.go`

- 📄 `atproto/repo/cbor_gen.go`

- 📄 `atproto/repo/mst/cbor_gen.go`

- 📄 `carstore/scylla.go`

- 📄 `cmd/relay/stream/cbor_gen.go`

- 📄 `events/cbor_gen.go`

- 📄 `lex/util/cbor_gen.go`

- 📄 `mst/cbor_gen.go`

- 📄 `repo/cbor_gen.go`

- 📄 `util/labels/cbor_gen.go`




---


[import] path: math/big type: stdlib


### math/big


- **Тип:** stdlib

- **Алиасы:** `big`



### Вызовы


`NewInt`


### Кандидаты на типы


`Int`


### Селекторы (любое использование `pkg.X`)


`Int`, `NewInt`


### Используется в файлах


- 📄 `atproto/atcrypto/jwk.go`

- 📄 `atproto/atcrypto/p256.go`

- 📄 `atproto/atcrypto/p256_lowS.go`




---


[import] path: math/rand type: stdlib


### math/rand


- **Тип:** stdlib

- **Алиасы:** `mathrand`, `rand`



### Вызовы


`Float64`, `Intn`, `Perm`


### Селекторы (любое использование `pkg.X`)


`Float64`, `Intn`, `Perm`


### Используется в файлах


- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/tap/util.go`

- 📄 `fakedata/generators.go`

- 📄 `splitter/splitter.go`

- 📄 `testing/utils.go`




---


[import] path: math/rand/v2 type: stdlib


### math/rand/v2


- **Тип:** stdlib

- **Алиасы:** `v2`



### Используется в файлах


- 📄 `carstore/scylla.go`




---


[import] path: mime/multipart type: stdlib


### mime/multipart


- **Тип:** stdlib

- **Алиасы:** `multipart`



### Вызовы


`NewWriter`


### Селекторы (любое использование `pkg.X`)


`NewWriter`


### Используется в файлах


- 📄 `automod/visual/hiveai_client.go`

- 📄 `automod/visual/prescreen.go`




---


[import] path: net type: stdlib


### net


- **Тип:** stdlib

- **Алиасы:** `net`



### Вызовы


`CIDRMask`, `IPv4`, `Listen`, `ParseIP`, `SplitHostPort`


### Кандидаты на типы


`DNSError`, `Dialer`, `IP`, `IPNet`, `Resolver`, `TCPAddr`


### Селекторы (любое использование `pkg.X`)


`CIDRMask`, `Conn`, `DNSError`, `Dialer`, `Error`, `IP`, `IPNet`, `IPv4`, `Listen`, `ListenConfig`, `Listener`, `ParseIP`, `Resolver`, `SplitHostPort`, `TCPAddr`


### Используется в файлах


- 📄 `atproto/identity/base_directory.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/directory.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/identity/nsid.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/testing/producer.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `events/consumer.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/splitter.go`

- 📄 `util/ssrf/ssrf.go`




---


[import] path: net/http type: stdlib


### net/http


- **Тип:** stdlib

- **Алиасы:** `http`



### Вызовы


`Error`, `Get`, `Handle`, `HandleFunc`, `ListenAndServe`, `NewRequest`, `NewRequestWithContext`, `NewServeMux`, `Redirect`, `RobustHTTPClient`, `Serve`


### Кандидаты на типы


`Client`, `ErrServerClosed`, `Handler`, `HandlerFunc`, `Header`, `Request`, `Response`, `ServeMux`, `Server`, `StatusBadRequest`, `StatusCreated`, `StatusNotFound`, `StatusOK`, `StatusTooManyRequests`, `Transport`


### Селекторы (любое использование `pkg.X`)


`Client`, `DefaultClient`, `DefaultServeMux`, `DefaultTransport`, `ErrServerClosed`, `ErrUseLastResponse`, `Error`, `Get`, `Handle`, `HandleFunc`, `Handler`, `HandlerFunc`, `Header`, `ListenAndServe`, `MethodGet`, `MethodPost`, `NewRequest`, `NewRequestWithContext`, `NewServeMux`, `ProxyFromEnvironment`, `Redirect`, `Request`, `Response`, `ResponseWriter`, `RobustHTTPClient`, `Serve`, `ServeMux`, `Server`, `StatusBadRequest`, `StatusCreated`, `StatusForbidden`, `StatusFound`, `StatusInternalServerError`, `StatusNotFound`, `StatusOK`, `StatusTooManyRequests`, `StatusUnauthorized`, `Transport`


### Используется в файлах


- 📄 `atproto/atclient/admin_auth.go`

- 📄 `atproto/atclient/apiclient.go`

- 📄 `atproto/atclient/apirequest.go`

- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/auth/http.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/resolver.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/base_directory.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/directory.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/engine/blobs.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/slack.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `automod/visual/prescreen.go`

- 📄 `backfill/backfill.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/slack.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/firehose.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/bgs.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/relay/forward.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `cmd/relay/testing/producer.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/main.go`

- 📄 `cmd/tap/outbox.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/server.go`

- 📄 `cmd/tap/util.go`

- 📄 `cmd/tap/webhook_client.go`

- 📄 `lex/util/client.go`

- 📄 `search/firehose.go`

- 📄 `search/metrics.go`

- 📄 `search/server.go`

- 📄 `splitter/handlers.go`

- 📄 `splitter/splitter.go`

- 📄 `util/cliutil/util.go`

- 📄 `util/http.go`

- 📄 `util/ssrf/ssrf.go`

- 📄 `util/svcutil/metrics_middleware.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: net/http/pprof type: stdlib


### net/http/pprof


- **Тип:** stdlib

- **Алиасы:** `_`



### Используется в файлах


- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/tap/main.go`

- 📄 `search/server.go`




---


[import] path: net/url type: stdlib


### net/url


- **Тип:** stdlib

- **Алиасы:** `url`



### Вызовы


`Parse`, `ParseQuery`, `QueryEscape`


### Кандидаты на типы


`URL`, `Values`


### Селекторы (любое использование `pkg.X`)


`Parse`, `ParseQuery`, `QueryEscape`, `URL`, `Values`


### Используется в файлах


- 📄 `atproto/atclient/apirequest.go`

- 📄 `atproto/atclient/params.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/resolver.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/auth/oauth/types.go`

- 📄 `atproto/auth/permission.go`

- 📄 `atproto/auth/permission_util.go`

- 📄 `atproto/identity/identity.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/engine/util.go`

- 📄 `automod/rules/identity.go`

- 📄 `automod/rules/misleading.go`

- 📄 `automod/rules/promo.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/firehose.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/bgs.go`

- 📄 `cmd/relay/relay/host.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `search/firehose.go`

- 📄 `search/transform.go`

- 📄 `search/url.go`

- 📄 `splitter/handlers.go`

- 📄 `splitter/splitter.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: os type: stdlib


### os


- **Тип:** stdlib

- **Алиасы:** `os`



### Вызовы


`Create`, `CreateTemp`, `Exit`, `Getenv`, `IsNotExist`, `Mkdir`, `MkdirAll`, `MkdirTemp`, `Open`, `OpenFile`, `ReadFile`, `Remove`, `RemoveAll`, `Stat`, `WriteFile`


### Кандидаты на типы


`File`


### Селекторы (любое использование `pkg.X`)


`Args`, `Create`, `CreateTemp`, `Exit`, `File`, `Getenv`, `IsNotExist`, `Mkdir`, `MkdirAll`, `MkdirTemp`, `ModePerm`, `O_CREATE`, `O_RDONLY`, `O_RDWR`, `O_WRONLY`, `Open`, `OpenFile`, `ReadFile`, `Remove`, `RemoveAll`, `Signal`, `Stat`, `Stderr`, `Stdin`, `Stdout`, `WriteFile`


### Используется в файлах


- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/atcrypto/cmd/atp-crypto/main.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/identity/cmd/atp-id/main.go`

- 📄 `atproto/lexicon/catalog.go`

- 📄 `atproto/lexicon/cmd/lextool/main.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/syntax/cmd/atp-syntax/main.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/keyword/cmd/kw-cli/main.go`

- 📄 `automod/setstore/setstore.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/beemo/main.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/account.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/lexgen/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/main.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `fakedata/accounts.go`

- 📄 `lex/gen.go`

- 📄 `lex/schema.go`

- 📄 `search/bulk.go`

- 📄 `search/indexing.go`

- 📄 `search/server.go`

- 📄 `splitter/splitter.go`

- 📄 `testing/utils.go`

- 📄 `util/cliutil/key.go`

- 📄 `util/cliutil/util.go`




---


[import] path: os/signal type: stdlib


### os/signal


- **Тип:** stdlib

- **Алиасы:** `signal`



### Вызовы


`Notify`, `NotifyContext`


### Селекторы (любое использование `pkg.X`)


`Notify`, `NotifyContext`


### Используется в файлах


- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/tap/main.go`




---


[import] path: path/filepath type: stdlib


### path/filepath


- **Тип:** stdlib

- **Алиасы:** `filepath`



### Вызовы


`Abs`, `Dir`, `Join`, `Walk`, `WalkDir`


### Селекторы (любое использование `pkg.X`)


`Abs`, `Dir`, `Join`, `Walk`, `WalkDir`


### Используется в файлах


- 📄 `atproto/lexicon/catalog.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/lexgen/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `lex/gen.go`

- 📄 `util/cliutil/key.go`

- 📄 `util/cliutil/util.go`




---


[import] path: reflect type: stdlib


### reflect


- **Тип:** stdlib

- **Алиасы:** `reflect`



### Вызовы


`DeepEqual`, `New`, `TypeOf`, `ValueOf`


### Кандидаты на типы


`Pointer`, `Slice`, `Type`


### Селекторы (любое использование `pkg.X`)


`DeepEqual`, `New`, `Pointer`, `Slice`, `Type`, `TypeOf`, `ValueOf`


### Используется в файлах


- 📄 `atproto/atclient/params.go`

- 📄 `atproto/atdata/parse.go`

- 📄 `atproto/lexicon/language.go`

- 📄 `atproto/lexicon/validation.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `gen/main.go`

- 📄 `lex/lexlint/breaking.go`

- 📄 `lex/util/decoder.go`

- 📄 `mst/mst.go`




---


[import] path: regexp type: stdlib


### regexp


- **Тип:** stdlib

- **Алиасы:** `regexp`



### Вызовы


`Compile`, `MustCompile`, `QuoteMeta`


### Кандидаты на типы


`Regexp`


### Селекторы (любое использование `pkg.X`)


`Compile`, `MustCompile`, `QuoteMeta`, `Regexp`


### Используется в файлах


- 📄 `atproto/syntax/aturi.go`

- 📄 `atproto/syntax/cid.go`

- 📄 `atproto/syntax/datetime.go`

- 📄 `atproto/syntax/did.go`

- 📄 `atproto/syntax/handle.go`

- 📄 `atproto/syntax/language.go`

- 📄 `atproto/syntax/nsid.go`

- 📄 `atproto/syntax/recordkey.go`

- 📄 `atproto/syntax/tid.go`

- 📄 `atproto/syntax/uri.go`

- 📄 `automod/helpers/text.go`

- 📄 `automod/keyword/slugify.go`

- 📄 `automod/keyword/slur_regex.go`

- 📄 `automod/keyword/tokenize.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `lex/lexlint/syntax.go`

- 📄 `search/japanese.go`




---


[import] path: runtime type: stdlib


### runtime


- **Тип:** stdlib

- **Алиасы:** `runtime`



### Вызовы


`NumCPU`, `SetBlockProfileRate`, `SetMutexProfileFraction`


### Селекторы (любое использование `pkg.X`)


`NumCPU`, `SetBlockProfileRate`, `SetMutexProfileFraction`


### Используется в файлах


- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/hepa/main.go`




---


[import] path: slices type: stdlib


### slices


- **Тип:** stdlib

- **Алиасы:** `slices`



### Вызовы


`Clone`, `Contains`, `Delete`, `Equal`, `Insert`, `Reverse`, `SortFunc`


### Селекторы (любое использование `pkg.X`)


`Clone`, `Contains`, `Delete`, `Equal`, `Insert`, `Reverse`, `SortFunc`


### Используется в файлах


- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/types.go`

- 📄 `atproto/repo/mst/node_insert.go`

- 📄 `atproto/repo/mst/node_remove.go`

- 📄 `lex/lexgen/flatten.go`

- 📄 `lex/lexgen/util.go`

- 📄 `lex/lexlint/lint.go`

- 📄 `lex/type_schema.go`

- 📄 `search/handlers.go`




---


[import] path: sort type: stdlib


### sort


- **Тип:** stdlib

- **Алиасы:** `sort`



### Вызовы


`Ints`, `Slice`, `Sort`, `Strings`


### Селекторы (любое использование `pkg.X`)


`Ints`, `Slice`, `Sort`, `Strings`


### Используется в файлах


- 📄 `api/atproto/cbor_gen.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/chat/cbor_gen.go`

- 📄 `atproto/atdata/cbor_gen.go`

- 📄 `atproto/labeling/cbor_gen.go`

- 📄 `atproto/repo/cbor_gen.go`

- 📄 `atproto/repo/mst/cbor_gen.go`

- 📄 `atproto/repo/mst/debug.go`

- 📄 `atproto/repo/operation.go`

- 📄 `carstore/bs.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/relay/stream/cbor_gen.go`

- 📄 `events/cbor_gen.go`

- 📄 `lex/gen.go`

- 📄 `lex/lexgen/codegen.go`

- 📄 `lex/lexgen/flatten.go`

- 📄 `lex/lexlint/breaking.go`

- 📄 `lex/util/cbor_gen.go`

- 📄 `mst/cbor_gen.go`

- 📄 `repo/cbor_gen.go`

- 📄 `util/labels/cbor_gen.go`




---


[import] path: strconv type: stdlib


### strconv


- **Тип:** stdlib

- **Алиасы:** `strconv`



### Вызовы


`Atoi`, `FormatInt`, `FormatUint`, `Itoa`, `ParseBool`, `ParseFloat`, `ParseInt`


### Селекторы (любое использование `pkg.X`)


`Atoi`, `FormatInt`, `FormatUint`, `Itoa`, `ParseBool`, `ParseFloat`, `ParseInt`


### Используется в файлах


- 📄 `carstore/meta_gorm.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/bgs.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `search/bulk.go`

- 📄 `search/handlers.go`

- 📄 `search/metrics.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/splitter.go`

- 📄 `util/svcutil/metrics_middleware.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: strings type: stdlib


### strings


- **Тип:** stdlib

- **Алиасы:** `strings`



### Вызовы


`Contains`, `ContainsAny`, `Count`, `Cut`, `CutSuffix`, `Fields`, `FieldsFunc`, `HasPrefix`, `HasSuffix`, `IndexByte`, `Join`, `NewReader`, `Repeat`, `Replace`, `ReplaceAll`, `Split`, `SplitN`, `Title`, `ToLower`, `TrimPrefix`, `TrimSpace`, `TrimSuffix`


### Селекторы (любое использование `pkg.X`)


`Builder`, `Contains`, `ContainsAny`, `Count`, `Cut`, `CutSuffix`, `Fields`, `FieldsFunc`, `HasPrefix`, `HasSuffix`, `IndexByte`, `Join`, `NewReader`, `Repeat`, `Replace`, `ReplaceAll`, `Split`, `SplitN`, `Title`, `ToLower`, `TrimPrefix`, `TrimSpace`, `TrimSuffix`


### Используется в файлах


- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/atcrypto/keys.go`

- 📄 `atproto/auth/http.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/auth/oauth/types.go`

- 📄 `atproto/auth/oauthscope.go`

- 📄 `atproto/auth/permission_util.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/identity/identity.go`

- 📄 `atproto/lexicon/catalog.go`

- 📄 `atproto/lexicon/language.go`

- 📄 `atproto/lexicon/mimetype.go`

- 📄 `atproto/lexicon/resolving_catalog.go`

- 📄 `atproto/lexicon/schemafile.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/syntax/atidentifier.go`

- 📄 `atproto/syntax/aturi.go`

- 📄 `atproto/syntax/cid.go`

- 📄 `atproto/syntax/datetime.go`

- 📄 `atproto/syntax/did.go`

- 📄 `atproto/syntax/handle.go`

- 📄 `atproto/syntax/nsid.go`

- 📄 `atproto/syntax/path.go`

- 📄 `atproto/syntax/tid.go`

- 📄 `automod/engine/blobs.go`

- 📄 `automod/engine/slack.go`

- 📄 `automod/engine/util.go`

- 📄 `automod/keyword/slugify.go`

- 📄 `automod/keyword/tokenize.go`

- 📄 `automod/rules/gtube.go`

- 📄 `automod/rules/identity.go`

- 📄 `automod/rules/keyword.go`

- 📄 `automod/rules/misleading.go`

- 📄 `automod/rules/misleading_unicode_reverse.go`

- 📄 `automod/rules/nostr.go`

- 📄 `automod/rules/private.go`

- 📄 `automod/rules/promo.go`

- 📄 `automod/rules/quick.go`

- 📄 `automod/rules/reposts.go`

- 📄 `automod/visual/abyss_rule.go`

- 📄 `automod/visual/hiveai_rule.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/gormstore.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `cmd/beemo/main.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/lexgen/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/relay/forward.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/domain_ban.go`

- 📄 `cmd/relay/relay/host.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/tap/main.go`

- 📄 `cmd/tap/tap.go`

- 📄 `cmd/tap/util.go`

- 📄 `lex/gen.go`

- 📄 `lex/lexgen/codegen.go`

- 📄 `lex/lexgen/flatten.go`

- 📄 `lex/lexgen/util.go`

- 📄 `lex/lexlint/lint.go`

- 📄 `lex/schema.go`

- 📄 `lex/type_schema.go`

- 📄 `lex/util/decoder.go`

- 📄 `mst/mst_util.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/bulk.go`

- 📄 `search/firehose.go`

- 📄 `search/handlers.go`

- 📄 `search/indexing.go`

- 📄 `search/metrics.go`

- 📄 `search/parse_query.go`

- 📄 `search/query.go`

- 📄 `search/server.go`

- 📄 `search/transform.go`

- 📄 `splitter/splitter.go`

- 📄 `testing/utils.go`

- 📄 `util/cliutil/util.go`

- 📄 `util/svcutil/logger.go`

- 📄 `util/uri.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: sync type: stdlib


### sync


- **Тип:** stdlib

- **Алиасы:** `sync`



### Вызовы


`OnceFunc`


### Кандидаты на типы


`Mutex`, `Pool`, `WaitGroup`


### Селекторы (любое использование `pkg.X`)


`Cond`, `Map`, `Mutex`, `OnceFunc`, `Pool`, `RWMutex`, `WaitGroup`, `getHostStatus`, `getLatestCommit`, `getRepo`, `getRepoStatus`, `listHosts`, `listRepos`, `listReposByCollection`, `requestCrawl`, `subscribeRepos`


### Используется в файлах


- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/auth/oauth/memstore.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/identity/cache_directory.go`

- 📄 `atproto/identity/mock_directory.go`

- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `atproto/syntax/tid.go`

- 📄 `automod/engine/effects.go`

- 📄 `automod/engine/ruleset.go`

- 📄 `automod/visual/prescreen.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/gormstore.go`

- 📄 `backfill/memstore.go`

- 📄 `carstore/last_shard_cache.go`

- 📄 `carstore/nonarchive.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/stream/eventmgr/event_manager.go`

- 📄 `cmd/relay/stream/eventmgr/subscriber.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/stream/schedulers/parallel/parallel.go`

- 📄 `cmd/relay/testing/consumer.go`

- 📄 `cmd/relay/testing/producer.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/outbox.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/persist.go`

- 📄 `events/schedulers/autoscaling/autoscaling.go`

- 📄 `events/schedulers/autoscaling/throughput.go`

- 📄 `events/schedulers/parallel/parallel.go`

- 📄 `events/yolopersist/yolopersist.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/bulk.go`

- 📄 `search/handlers.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/ringbuf.go`

- 📄 `splitter/splitter.go`




---


[import] path: sync/atomic type: stdlib


### sync/atomic


- **Тип:** stdlib

- **Алиасы:** `atomic`



### Вызовы


`AddInt64`, `LoadInt64`, `StoreInt64`


### Селекторы (любое использование `pkg.X`)


`AddInt64`, `Bool`, `Int64`, `LoadInt64`, `StoreInt64`, `Uint32`, `Uint64`, `Value`


### Используется в файлах


- 📄 `automod/consumer/firehose.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `carstore/bs.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/stream/schedulers/parallel/parallel.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/firehose.go`




---


[import] path: syscall type: stdlib


### syscall


- **Тип:** stdlib

- **Алиасы:** `syscall`



### Селекторы (любое использование `pkg.X`)


`RawConn`, `SIGINT`, `SIGTERM`


### Используется в файлах


- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/tap/main.go`

- 📄 `util/ssrf/ssrf.go`




---


[import] path: time type: stdlib


### time


- **Тип:** stdlib

- **Алиасы:** `time`



### Вызовы


`After`, `Date`, `Duration`, `NewTicker`, `NewTimer`, `Now`, `Parse`, `Since`, `Sleep`, `Unix`, `UnixMicro`


### Кандидаты на типы


`Duration`, `Hour`, `Millisecond`, `Minute`, `Second`, `Time`


### Селекторы (любое использование `pkg.X`)


`After`, `Date`, `DateOnly`, `Duration`, `Format`, `Hour`, `Millisecond`, `Minute`, `NewTicker`, `NewTimer`, `Now`, `Parse`, `RFC3339`, `RFC3339Nano`, `Second`, `Since`, `Sleep`, `Time`, `UTC`, `Unix`, `UnixMicro`


### Используется в файлах


- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/resolver.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/cache_directory.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/directory.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `atproto/syntax/datetime.go`

- 📄 `atproto/syntax/tid.go`

- 📄 `automod/cachestore/cachestore_mem.go`

- 📄 `automod/cachestore/cachestore_redis.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `automod/countstore/countstore.go`

- 📄 `automod/countstore/countstore_redis.go`

- 📄 `automod/engine/account_meta.go`

- 📄 `automod/engine/blobs.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/engine_ozone.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/persisthelpers.go`

- 📄 `automod/engine/testing.go`

- 📄 `automod/helpers/account.go`

- 📄 `automod/rules/harassment.go`

- 📄 `automod/rules/identity.go`

- 📄 `automod/rules/mentions.go`

- 📄 `automod/rules/nostr.go`

- 📄 `automod/rules/promo.go`

- 📄 `automod/rules/quick.go`

- 📄 `automod/rules/replies.go`

- 📄 `automod/rules/reposts.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `automod/visual/hiveai_rule.go`

- 📄 `automod/visual/prescreen.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/gormstore.go`

- 📄 `backfill/memstore.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/scylla.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/firehose.go`

- 📄 `cmd/collectiondir/pebble.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/relay/crawl.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/models/models.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/relay/util.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/stream/eventmgr/event_manager.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/testing/consumer.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/main.go`

- 📄 `cmd/tap/outbox.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/tap.go`

- 📄 `cmd/tap/util.go`

- 📄 `cmd/tap/webhook_client.go`

- 📄 `events/consumer.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `events/schedulers/autoscaling/autoscaling.go`

- 📄 `events/schedulers/autoscaling/throughput.go`

- 📄 `fakedata/generators.go`

- 📄 `models/models.go`

- 📄 `models/moderation.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/firehose.go`

- 📄 `search/indexing.go`

- 📄 `search/metrics.go`

- 📄 `search/parse_query.go`

- 📄 `search/transform.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/splitter.go`

- 📄 `testing/pdsmodels/types.go`

- 📄 `testing/utils.go`

- 📄 `util/cliutil/util.go`

- 📄 `util/http.go`

- 📄 `util/ssrf/ssrf.go`

- 📄 `util/svcutil/metrics_middleware.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: unicode type: stdlib


### unicode


- **Тип:** stdlib

- **Алиасы:** `unicode`



### Вызовы


`IsLetter`, `IsNumber`


### Кандидаты на типы


`MaxASCII`


### Селекторы (любое использование `pkg.X`)


`IsLetter`, `IsNumber`, `MaxASCII`, `Mn`


### Используется в файлах


- 📄 `atproto/auth/permission_util.go`

- 📄 `automod/keyword/tokenize.go`

- 📄 `automod/rules/misleading.go`




---


[import] path: unicode/utf8 type: stdlib


### unicode/utf8


- **Тип:** stdlib

- **Алиасы:** `utf8`



### Вызовы


`RuneCountInString`


### Селекторы (любое использование `pkg.X`)


`RuneCountInString`


### Используется в файлах


- 📄 `automod/rules/replies.go`




---


[import] path: unsafe type: stdlib


### unsafe


- **Тип:** stdlib

- **Алиасы:** `unsafe`



### Вызовы


`Slice`, `StringData`


### Селекторы (любое использование `pkg.X`)


`Slice`, `StringData`


### Используется в файлах


- 📄 `mst/mst_util.go`



## Внешние зависимости



---


[import] path: github.com/PuerkitoBio/purell type: external


### github.com/PuerkitoBio/purell


- **Тип:** external

- **Алиасы:** `purell`



### Вызовы


`NormalizeURLString`


### Селекторы (любое использование `pkg.X`)


`FlagRemoveDirectoryIndex`, `FlagRemoveDuplicateSlashes`, `FlagRemoveFragment`, `FlagRemoveWWW`, `FlagSortQuery`, `FlagsUsuallySafeGreedy`, `NormalizeURLString`


### Используется в файлах


- 📄 `search/url.go`




---


[import] path: github.com/RussellLuo/slidingwindow type: external


### github.com/RussellLuo/slidingwindow


- **Тип:** external

- **Алиасы:** `slidingwindow`



### Вызовы


`NewLimiter`, `NewLocalWindow`


### Кандидаты на типы


`Limiter`


### Селекторы (любое использование `pkg.X`)


`Limiter`, `NewLimiter`, `NewLocalWindow`, `StopFunc`, `Window`


### Используется в файлах


- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/relay/util.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `events/consumer.go`




---


[import] path: github.com/araddon/dateparse type: external


### github.com/araddon/dateparse


- **Тип:** external

- **Алиасы:** `dateparse`



### Вызовы


`ParseAny`


### Селекторы (любое использование `pkg.X`)


`ParseAny`


### Используется в файлах


- 📄 `cmd/sonar/sonar.go`




---


[import] path: github.com/brianvoe/gofakeit/v6 type: external


### github.com/brianvoe/gofakeit/v6


- **Тип:** external

- **Алиасы:** `v6`



### Используется в файлах


- 📄 `fakedata/generators.go`




---


[import] path: github.com/cockroachdb/pebble type: external


### github.com/cockroachdb/pebble


- **Тип:** external

- **Алиасы:** `pebble`



### Вызовы


`Open`


### Кандидаты на типы


`DB`, `IterOptions`, `Iterator`, `Options`


### Селекторы (любое использование `pkg.X`)


`DB`, `ErrNotFound`, `IterOptions`, `Iterator`, `NoSync`, `Open`, `Options`, `Sync`


### Используется в файлах


- 📄 `cmd/collectiondir/pebble.go`

- 📄 `events/pebblepersist/pebblepersist.go`




---


[import] path: github.com/earthboundkid/versioninfo/v2 type: external


### github.com/earthboundkid/versioninfo/v2


- **Тип:** external

- **Алиасы:** `v2`



### Используется в файлах


- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/directory.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/engine/blobs.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/main.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/main.go`

- 📄 `cmd/tap/util.go`

- 📄 `fakedata/accounts.go`

- 📄 `search/firehose.go`

- 📄 `search/server.go`

- 📄 `xrpc/xrpc.go`




---


[import] path: github.com/go-redis/cache/v9 type: external


### github.com/go-redis/cache/v9


- **Тип:** external

- **Алиасы:** `v9`



### Используется в файлах


- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `automod/cachestore/cachestore_redis.go`

- 📄 `cmd/bluepages/resolver.go`




---


[import] path: github.com/gocql/gocql type: external


### github.com/gocql/gocql


- **Тип:** external

- **Алиасы:** `gocql`



### Вызовы


`NewCluster`, `RoundRobinHostPolicy`, `TokenAwareHostPolicy`


### Кандидаты на типы


`RetryType`, `Session`


### Селекторы (любое использование `pkg.X`)


`ErrConnectionClosed`, `ErrNoStreams`, `ErrNotFound`, `ErrSessionClosed`, `ErrTimeoutNoResponse`, `ErrTooManyTimeouts`, `ErrUnavailable`, `NewCluster`, `One`, `Quorum`, `Rethrow`, `Retry`, `RetryNextHost`, `RetryType`, `RetryableQuery`, `RoundRobinHostPolicy`, `Session`, `TokenAwareHostPolicy`


### Используется в файлах


- 📄 `carstore/scylla.go`




---


[import] path: github.com/golang-jwt/jwt/v5 type: external


### github.com/golang-jwt/jwt/v5


- **Тип:** external

- **Алиасы:** `v5`



### Используется в файлах


- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/jwt_signing.go`

- 📄 `atproto/auth/oauth/jwt_signing.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/session.go`




---


[import] path: github.com/google/go-querystring/query type: external


### github.com/google/go-querystring/query


- **Тип:** external

- **Алиасы:** `query`



### Вызовы


`Values`


### Селекторы (любое использование `pkg.X`)


`Values`


### Используется в файлах


- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/session.go`




---


[import] path: github.com/gorilla/sessions type: external


### github.com/gorilla/sessions


- **Тип:** external

- **Алиасы:** `sessions`



### Вызовы


`NewCookieStore`


### Кандидаты на типы


`CookieStore`


### Селекторы (любое использование `pkg.X`)


`CookieStore`, `NewCookieStore`


### Используется в файлах


- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`




---


[import] path: github.com/gorilla/websocket type: external


### github.com/gorilla/websocket


- **Тип:** external

- **Алиасы:** `websocket`



### Вызовы


`Upgrade`


### Кандидаты на типы


`Conn`, `Dialer`, `ErrCloseSent`, `Upgrader`


### Селекторы (любое использование `pkg.X`)


`BinaryMessage`, `Conn`, `DefaultDialer`, `Dialer`, `ErrCloseSent`, `PingMessage`, `PongMessage`, `TextMessage`, `Upgrade`, `Upgrader`


### Используется в файлах


- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/collectiondir/firehose.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/testing/consumer.go`

- 📄 `cmd/relay/testing/producer.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/server.go`

- 📄 `events/consumer.go`

- 📄 `search/firehose.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/splitter.go`




---


[import] path: github.com/hashicorp/go-cleanhttp type: external


### github.com/hashicorp/go-cleanhttp


- **Тип:** external

- **Алиасы:** `go-cleanhttp`



### Используется в файлах


- 📄 `util/http.go`




---


[import] path: github.com/hashicorp/go-retryablehttp type: external


### github.com/hashicorp/go-retryablehttp


- **Тип:** external

- **Алиасы:** `go-retryablehttp`



### Используется в файлах


- 📄 `util/http.go`




---


[import] path: github.com/hashicorp/golang-lru/arc/v2 type: external


### github.com/hashicorp/golang-lru/arc/v2


- **Тип:** external

- **Алиасы:** `arc`



### Кандидаты на типы


`ARCCache`


### Селекторы (любое использование `pkg.X`)


`ARCCache`, `NewARC`


### Используется в файлах


- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`




---


[import] path: github.com/hashicorp/golang-lru/v2 type: external


### github.com/hashicorp/golang-lru/v2


- **Тип:** external

- **Алиасы:** `lru`, `v2`



### Кандидаты на типы


`Cache`


### Селекторы (любое использование `pkg.X`)


`Cache`, `New`


### Используется в файлах


- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/relay/relay/relay.go`




---


[import] path: github.com/hashicorp/golang-lru/v2/expirable type: external


### github.com/hashicorp/golang-lru/v2/expirable


- **Тип:** external

- **Алиасы:** `expirable`



### Кандидаты на типы


`LRU`


### Селекторы (любое использование `pkg.X`)


`LRU`, `NewLRU`


### Используется в файлах


- 📄 `atproto/identity/cache_directory.go`

- 📄 `automod/cachestore/cachestore_mem.go`




---


[import] path: github.com/ipfs/go-block-format type: external


### github.com/ipfs/go-block-format


- **Тип:** external

- **Алиасы:** `bf`, `block`, `blockformat`, `blocks`



### Вызовы


`NewBlockWithCid`


### Кандидаты на типы


`Block`


### Селекторы (любое использование `pkg.X`)


`Block`, `NewBlockWithCid`


### Используется в файлах


- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/mst/encoding.go`

- 📄 `atproto/repo/mst/tree.go`

- 📄 `atproto/repo/repo.go`

- 📄 `atproto/repo/tiny_blockstore.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/repomgr.go`

- 📄 `util/readrecordbs.go`




---


[import] path: github.com/ipfs/go-cid type: external


### github.com/ipfs/go-cid


- **Тип:** external

- **Алиасы:** `cid`, `go-cid`



### Вызовы


`Cid`, `Decode`


### Кандидаты на типы


`Undef`


### Селекторы (любое использование `pkg.X`)


`Cid`, `Decode`, `Undef`


### Используется в файлах


- 📄 `api/atproto/cbor_gen.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/chat/cbor_gen.go`

- 📄 `atproto/atdata/blob.go`

- 📄 `atproto/atdata/cbor_gen.go`

- 📄 `atproto/atdata/cidlink.go`

- 📄 `atproto/atdata/data.go`

- 📄 `atproto/atdata/parse.go`

- 📄 `atproto/labeling/cbor_gen.go`

- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/cbor_gen.go`

- 📄 `atproto/repo/commit.go`

- 📄 `atproto/repo/mst/cbor_gen.go`

- 📄 `atproto/repo/mst/debug.go`

- 📄 `atproto/repo/mst/encoding.go`

- 📄 `atproto/repo/mst/node.go`

- 📄 `atproto/repo/mst/node_insert.go`

- 📄 `atproto/repo/mst/node_remove.go`

- 📄 `atproto/repo/mst/tree.go`

- 📄 `atproto/repo/operation.go`

- 📄 `atproto/repo/repo.go`

- 📄 `atproto/repo/sync.go`

- 📄 `atproto/repo/tiny_blockstore.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/gormstore.go`

- 📄 `backfill/memstore.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/relay/stream/cbor_gen.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `events/cbor_gen.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `lex/util/cbor_gen.go`

- 📄 `lex/util/lex_types.go`

- 📄 `models/dbcid.go`

- 📄 `mst/cbor_gen.go`

- 📄 `mst/diff.go`

- 📄 `mst/mst.go`

- 📄 `mst/mst_util.go`

- 📄 `repo/carutil/reader.go`

- 📄 `repo/cbor_gen.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/bulk.go`

- 📄 `search/firehose.go`

- 📄 `search/indexing.go`

- 📄 `testing/utils.go`

- 📄 `util/labels/cbor_gen.go`

- 📄 `util/readrecordbs.go`




---


[import] path: github.com/ipfs/go-datastore type: external


### github.com/ipfs/go-datastore


- **Тип:** external

- **Алиасы:** `go-datastore`



### Используется в файлах


- 📄 `cmd/gosky/main.go`

- 📄 `cmd/stress/main.go`

- 📄 `repomgr/repomgr.go`




---


[import] path: github.com/ipfs/go-ipfs-blockstore type: external


### github.com/ipfs/go-ipfs-blockstore


- **Тип:** external

- **Алиасы:** `blockstore`



### Вызовы


`NewBlockstore`


### Селекторы (любое использование `pkg.X`)


`Blockstore`, `NewBlockstore`


### Используется в файлах


- 📄 `atproto/repo/mst/encoding.go`

- 📄 `atproto/repo/mst/tree.go`

- 📄 `carstore/bs.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/stress/main.go`

- 📄 `repomgr/repomgr.go`

- 📄 `util/readrecordbs.go`




---


[import] path: github.com/ipfs/go-ipld-cbor type: external


### github.com/ipfs/go-ipld-cbor


- **Тип:** external

- **Алиасы:** `cbor`



### Вызовы


`DecodeInto`, `DumpObject`, `NewCborStore`


### Кандидаты на типы


`BasicIpldStore`, `IpldBlockstore`


### Селекторы (любое использование `pkg.X`)


`BasicIpldStore`, `DecodeInto`, `DumpObject`, `IpldBlockstore`, `IpldStore`, `NewCborStore`


### Используется в файлах


- 📄 `atproto/atdata/data.go`

- 📄 `carstore/bs.go`

- 📄 `cmd/stress/main.go`

- 📄 `mst/diff.go`

- 📄 `mst/mst.go`

- 📄 `mst/mst_util.go`

- 📄 `repo/repo.go`

- 📄 `util/cbor.go`




---


[import] path: github.com/ipfs/go-ipld-format type: external


### github.com/ipfs/go-ipld-format


- **Тип:** external

- **Алиасы:** `ipld`



### Вызовы


`IsNotFound`


### Кандидаты на типы


`ErrNotFound`


### Селекторы (любое использование `pkg.X`)


`ErrNotFound`, `IsNotFound`


### Используется в файлах


- 📄 `atproto/repo/mst/encoding.go`

- 📄 `atproto/repo/tiny_blockstore.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/nonarchive.go`

- 📄 `repomgr/repomgr.go`




---


[import] path: github.com/ipfs/go-libipfs/blocks type: external


### github.com/ipfs/go-libipfs/blocks


- **Тип:** external

- **Алиасы:** `blocks`



### Вызовы


`NewBlock`, `NewBlockWithCid`


### Кандидаты на типы


`Block`


### Селекторы (любое использование `pkg.X`)


`Block`, `NewBlock`, `NewBlockWithCid`


### Используется в файлах


- 📄 `carstore/bs.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/gosky/debug.go`




---


[import] path: github.com/ipld/go-car type: external


### github.com/ipld/go-car


- **Тип:** external

- **Алиасы:** `car`, `go-car`



### Вызовы


`NewCarReader`, `ReadHeader`, `WriteHeader`


### Кандидаты на типы


`CarHeader`


### Селекторы (любое использование `pkg.X`)


`CarHeader`, `NewCarReader`, `ReadHeader`, `WriteHeader`


### Используется в файлах


- 📄 `atproto/repo/car.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/stress/main.go`

- 📄 `repo/carutil/reader.go`

- 📄 `repomgr/repomgr.go`




---


[import] path: github.com/ipld/go-car/util type: external


### github.com/ipld/go-car/util


- **Тип:** external

- **Алиасы:** `carutil`



### Вызовы


`ReadNode`


### Селекторы (любое использование `pkg.X`)


`ReadNode`


### Используется в файлах


- 📄 `carstore/bs.go`




---


[import] path: github.com/ipld/go-car/v2 type: external


### github.com/ipld/go-car/v2


- **Тип:** external

- **Алиасы:** `v2`



### Используется в файлах


- 📄 `cmd/gosky/debug.go`




---


[import] path: github.com/joho/godotenv/autoload type: external


### github.com/joho/godotenv/autoload


- **Тип:** external

- **Алиасы:** `_`



### Используется в файлах


- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `cmd/beemo/main.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/main.go`




---


[import] path: github.com/labstack/echo/v4 type: external


### github.com/labstack/echo/v4


- **Тип:** external

- **Алиасы:** `v4`



### Используется в файлах


- 📄 `cmd/bluepages/handlers.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/relay/forward.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `cmd/tap/server.go`

- 📄 `search/handlers.go`

- 📄 `search/indexing.go`

- 📄 `search/metrics.go`

- 📄 `search/server.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/handlers.go`

- 📄 `splitter/splitter.go`

- 📄 `util/svcutil/metrics_middleware.go`




---


[import] path: github.com/labstack/echo/v4/middleware type: external


### github.com/labstack/echo/v4/middleware


- **Тип:** external

- **Алиасы:** `middleware`



### Вызовы


`BodyLimit`, `CORS`, `CORSWithConfig`, `LoggerWithConfig`, `Recover`, `SecureWithConfig`


### Кандидаты на типы


`CORSConfig`, `LoggerConfig`, `SecureConfig`


### Селекторы (любое использование `pkg.X`)


`BodyLimit`, `CORS`, `CORSConfig`, `CORSWithConfig`, `DefaultLoggerConfig`, `LoggerConfig`, `LoggerWithConfig`, `Recover`, `SecureConfig`, `SecureWithConfig`


### Используется в файлах


- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/tap/server.go`

- 📄 `search/server.go`

- 📄 `splitter/splitter.go`




---


[import] path: github.com/lestrrat-go/jwx/v2/jwa type: external


### github.com/lestrrat-go/jwx/v2/jwa


- **Тип:** external

- **Алиасы:** `jwa`



### Селекторы (любое использование `pkg.X`)


`EllipticCurveAlgorithm`


### Используется в файлах


- 📄 `util/cliutil/key.go`




---


[import] path: github.com/lestrrat-go/jwx/v2/jwk type: external


### github.com/lestrrat-go/jwx/v2/jwk


- **Тип:** external

- **Алиасы:** `jwk`



### Вызовы


`FromRaw`, `ParseKey`


### Селекторы (любое использование `pkg.X`)


`ECDSAPrivateKey`, `FromRaw`, `KeyIDKey`, `ParseKey`


### Используется в файлах


- 📄 `util/cliutil/key.go`




---


[import] path: github.com/mattn/go-sqlite3 type: external


### github.com/mattn/go-sqlite3


- **Тип:** external

- **Алиасы:** `_`



### Используется в файлах


- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`




---


[import] path: github.com/minio/sha256-simd type: external


### github.com/minio/sha256-simd


- **Тип:** external

- **Алиасы:** `sha256`



### Вызовы


`Sum256`


### Селекторы (любое использование `pkg.X`)


`Sum256`


### Используется в файлах


- 📄 `mst/mst_util.go`




---


[import] path: github.com/mr-tron/base58 type: external


### github.com/mr-tron/base58


- **Тип:** external

- **Алиасы:** `base58`



### Вызовы


`Decode`, `Encode`


### Селекторы (любое использование `pkg.X`)


`Decode`, `Encode`


### Используется в файлах


- 📄 `atproto/atcrypto/k256.go`

- 📄 `atproto/atcrypto/keys.go`

- 📄 `atproto/atcrypto/p256.go`

- 📄 `atproto/identity/identity.go`




---


[import] path: github.com/multiformats/go-multihash type: external


### github.com/multiformats/go-multihash


- **Тип:** external

- **Алиасы:** `go-multihash`, `mh`



### Селекторы (любое использование `pkg.X`)


`SHA2_256`


### Используется в файлах


- 📄 `atproto/repo/mst/encoding.go`

- 📄 `testing/utils.go`

- 📄 `util/cbor.go`




---


[import] path: github.com/opensearch-project/opensearch-go/v2 type: external


### github.com/opensearch-project/opensearch-go/v2


- **Тип:** external

- **Алиасы:** `es`



### Вызовы


`NewClient`


### Кандидаты на типы


`Client`, `Config`


### Селекторы (любое использование `pkg.X`)


`Client`, `Config`, `NewClient`


### Используется в файлах


- 📄 `cmd/palomar/main.go`

- 📄 `search/indexing.go`

- 📄 `search/query.go`

- 📄 `search/server.go`




---


[import] path: github.com/opensearch-project/opensearch-go/v2/opensearchapi type: external


### github.com/opensearch-project/opensearch-go/v2/opensearchapi


- **Тип:** external

- **Алиасы:** `esapi`



### Кандидаты на типы


`DeleteRequest`, `UpdateRequest`


### Селекторы (любое использование `pkg.X`)


`DeleteRequest`, `UpdateRequest`


### Используется в файлах


- 📄 `search/indexing.go`




---


[import] path: github.com/orandin/slog-gorm type: external


### github.com/orandin/slog-gorm


- **Тип:** external

- **Алиасы:** `slogGorm`



### Вызовы


`New`


### Селекторы (любое использование `pkg.X`)


`New`


### Используется в файлах


- 📄 `util/cliutil/util.go`




---


[import] path: github.com/polydawn/refmt/cbor type: external


### github.com/polydawn/refmt/cbor


- **Тип:** external

- **Алиасы:** `cbor`



### Вызовы


`NewDecoder`


### Кандидаты на типы


`DecodeOptions`


### Селекторы (любое использование `pkg.X`)


`DecodeOptions`, `NewDecoder`


### Используется в файлах


- 📄 `cmd/gosky/main.go`




---


[import] path: github.com/polydawn/refmt/json type: external


### github.com/polydawn/refmt/json


- **Тип:** external

- **Алиасы:** `rejson`



### Вызовы


`NewEncoder`


### Кандидаты на типы


`EncodeOptions`


### Селекторы (любое использование `pkg.X`)


`EncodeOptions`, `NewEncoder`


### Используется в файлах


- 📄 `cmd/gosky/main.go`




---


[import] path: github.com/polydawn/refmt/shared type: external


### github.com/polydawn/refmt/shared


- **Тип:** external

- **Алиасы:** `shared`



### Кандидаты на типы


`TokenPump`


### Селекторы (любое использование `pkg.X`)


`TokenPump`


### Используется в файлах


- 📄 `cmd/gosky/main.go`




---


[import] path: github.com/prometheus/client_golang/prometheus type: external


### github.com/prometheus/client_golang/prometheus


- **Тип:** external

- **Алиасы:** `promclient`, `prometheus`



### Вызовы


`ExponentialBuckets`, `ExponentialBucketsRange`


### Кандидаты на типы


`CounterOpts`, `GaugeOpts`, `HistogramOpts`


### Селекторы (любое использование `pkg.X`)


`Counter`, `CounterOpts`, `ExponentialBuckets`, `ExponentialBucketsRange`, `Gauge`, `GaugeOpts`, `Histogram`, `HistogramOpts`


### Используется в файлах


- 📄 `atproto/identity/apidir/metrics.go`

- 📄 `atproto/identity/metrics.go`

- 📄 `atproto/identity/metrics_legacy.go`

- 📄 `atproto/identity/redisdir/metrics.go`

- 📄 `atproto/identity/redisdir/metrics_legacy.go`

- 📄 `automod/engine/metrics.go`

- 📄 `automod/visual/metrics.go`

- 📄 `backfill/metrics.go`

- 📄 `backfill/util.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/metrics.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/bluepages/metrics.go`

- 📄 `cmd/collectiondir/metrics.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/relay/metrics.go`

- 📄 `cmd/relay/relay/metrics_slurper.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/stream/eventmgr/metrics.go`

- 📄 `cmd/relay/stream/eventmgr/subscriber.go`

- 📄 `cmd/relay/stream/metrics.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/stream/schedulers/metrics.go`

- 📄 `cmd/relay/stream/schedulers/parallel/parallel.go`

- 📄 `cmd/relay/stream/schedulers/sequential/sequential.go`

- 📄 `cmd/sonar/metrics.go`

- 📄 `cmd/tap/metrics.go`

- 📄 `events/consumer.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/metrics.go`

- 📄 `events/schedulers/autoscaling/autoscaling.go`

- 📄 `events/schedulers/metrics.go`

- 📄 `events/schedulers/parallel/parallel.go`

- 📄 `events/schedulers/sequential/sequential.go`

- 📄 `repomgr/metrics.go`

- 📄 `search/metrics.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/metrics.go`

- 📄 `util/svcutil/metrics_middleware.go`




---


[import] path: github.com/prometheus/client_golang/prometheus/promauto type: external


### github.com/prometheus/client_golang/prometheus/promauto


- **Тип:** external

- **Алиасы:** `promauto`



### Вызовы


`NewCounter`, `NewCounterVec`, `NewGauge`, `NewGaugeVec`, `NewHistogram`, `NewHistogramVec`


### Селекторы (любое использование `pkg.X`)


`NewCounter`, `NewCounterVec`, `NewGauge`, `NewGaugeVec`, `NewHistogram`, `NewHistogramVec`


### Используется в файлах


- 📄 `atproto/identity/apidir/metrics.go`

- 📄 `atproto/identity/metrics.go`

- 📄 `atproto/identity/metrics_legacy.go`

- 📄 `atproto/identity/redisdir/metrics.go`

- 📄 `atproto/identity/redisdir/metrics_legacy.go`

- 📄 `automod/engine/metrics.go`

- 📄 `automod/visual/metrics.go`

- 📄 `backfill/metrics.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/metrics.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/bluepages/metrics.go`

- 📄 `cmd/collectiondir/metrics.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/relay/relay/metrics.go`

- 📄 `cmd/relay/relay/metrics_slurper.go`

- 📄 `cmd/relay/stream/eventmgr/metrics.go`

- 📄 `cmd/relay/stream/metrics.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/stream/schedulers/metrics.go`

- 📄 `cmd/sonar/metrics.go`

- 📄 `cmd/tap/metrics.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/metrics.go`

- 📄 `events/schedulers/metrics.go`

- 📄 `repomgr/metrics.go`

- 📄 `search/metrics.go`

- 📄 `splitter/metrics.go`

- 📄 `util/svcutil/metrics_middleware.go`




---


[import] path: github.com/prometheus/client_golang/prometheus/promhttp type: external


### github.com/prometheus/client_golang/prometheus/promhttp


- **Тип:** external

- **Алиасы:** `promhttp`



### Вызовы


`Handler`


### Селекторы (любое использование `pkg.X`)


`Handler`


### Используется в файлах


- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/tap/main.go`

- 📄 `search/server.go`

- 📄 `splitter/splitter.go`




---


[import] path: github.com/prometheus/client_model/go type: external


### github.com/prometheus/client_model/go


- **Тип:** external

- **Алиасы:** `dto`



### Кандидаты на типы


`Metric`


### Селекторы (любое использование `pkg.X`)


`Metric`


### Используется в файлах


- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `splitter/firehose.go`




---


[import] path: github.com/puzpuzpuz/xsync/v3 type: external


### github.com/puzpuzpuz/xsync/v3


- **Тип:** external

- **Алиасы:** `v3`



### Используется в файлах


- 📄 `automod/countstore/countstore_mem.go`




---


[import] path: github.com/puzpuzpuz/xsync/v4 type: external


### github.com/puzpuzpuz/xsync/v4


- **Тип:** external

- **Алиасы:** `v4`



### Используется в файлах


- 📄 `cmd/tap/outbox.go`




---


[import] path: github.com/redis/go-redis/v9 type: external


### github.com/redis/go-redis/v9


- **Тип:** external

- **Алиасы:** `v9`



### Используется в файлах


- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `automod/cachestore/cachestore_redis.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `automod/countstore/countstore_redis.go`

- 📄 `automod/flagstore/flagstore_redis.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/hepa/server.go`




---


[import] path: github.com/rivo/uniseg type: external


### github.com/rivo/uniseg


- **Тип:** external

- **Алиасы:** `uniseg`



### Вызовы


`GraphemeClusterCount`, `NewGraphemes`


### Селекторы (любое использование `pkg.X`)


`GraphemeClusterCount`, `NewGraphemes`


### Используется в файлах


- 📄 `atproto/lexicon/language.go`

- 📄 `search/transform.go`




---


[import] path: github.com/samber/slog-echo type: external


### github.com/samber/slog-echo


- **Тип:** external

- **Алиасы:** `slogecho`



### Вызовы


`New`


### Селекторы (любое использование `pkg.X`)


`New`


### Используется в файлах


- 📄 `cmd/bluepages/server.go`

- 📄 `search/server.go`




---


[import] path: github.com/spaolacci/murmur3 type: external


### github.com/spaolacci/murmur3


- **Тип:** external

- **Алиасы:** `murmur3`



### Вызовы


`Sum64`


### Селекторы (любое использование `pkg.X`)


`Sum64`


### Используется в файлах


- 📄 `automod/helpers/text.go`




---


[import] path: github.com/urfave/cli/v2 type: external


### github.com/urfave/cli/v2


- **Тип:** external

- **Алиасы:** `cli`, `v2`



### Кандидаты на типы


`Command`, `Context`, `Flag`, `StringFlag`


### Селекторы (любое использование `pkg.X`)


`Command`, `Context`, `Flag`, `StringFlag`


### Используется в файлах


- 📄 `cmd/gosky/account.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/bgs.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/did.go`

- 📄 `cmd/gosky/handle.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/lexgen/main.go`

- 📄 `util/cliutil/util.go`




---


[import] path: github.com/urfave/cli/v3 type: external


### github.com/urfave/cli/v3


- **Тип:** external

- **Алиасы:** `v3`



### Используется в файлах


- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/atcrypto/cmd/atp-crypto/main.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/identity/cmd/atp-id/main.go`

- 📄 `atproto/lexicon/cmd/lextool/main.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/syntax/cmd/atp-syntax/main.go`

- 📄 `automod/keyword/cmd/kw-cli/main.go`

- 📄 `cmd/beemo/main.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/collectiondir/collectiondir.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/main.go`

- 📄 `util/svcutil/logger.go`




---


[import] path: github.com/whyrusleeping/cbor-gen type: external


### github.com/whyrusleeping/cbor-gen


- **Тип:** external

- **Алиасы:** `cbg`, `typegen`



### Вызовы


`CborEncodeMajorType`, `NewCborReader`, `NewCborWriter`, `ReadByteArray`, `ReadCid`, `ReadFullStringIntoBuf`, `ReadStringWithMax`, `ScanForLinks`, `WriteBool`, `WriteByteArray`, `WriteCid`


### Кандидаты на типы


`CborWriter`, `Gen`, `MajArray`, `MajByteString`, `MajMap`, `MajOther`, `MaxLength`


### Селекторы (любое использование `pkg.X`)


`CBORMarshaler`, `CBORUnmarshaler`, `CborEncodeMajorType`, `CborNull`, `CborReader`, `CborWriter`, `Gen`, `MajArray`, `MajByteString`, `MajMap`, `MajNegativeInt`, `MajOther`, `MajTextString`, `MajUnsignedInt`, `MaxLength`, `NewCborReader`, `NewCborWriter`, `ReadByteArray`, `ReadCid`, `ReadFullStringIntoBuf`, `ReadStringWithMax`, `ScanForLinks`, `WriteBool`, `WriteByteArray`, `WriteCid`


### Используется в файлах


- 📄 `api/atproto/cbor_gen.go`

- 📄 `api/bsky/actorprofile.go`

- 📄 `api/bsky/actorstatus.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/bsky/embedrecordWithMedia.go`

- 📄 `api/bsky/feedgenerator.go`

- 📄 `api/bsky/feedpost.go`

- 📄 `api/bsky/feedpostgate.go`

- 📄 `api/bsky/feedthreadgate.go`

- 📄 `api/bsky/graphlist.go`

- 📄 `api/bsky/labelerservice.go`

- 📄 `api/bsky/richtextfacet.go`

- 📄 `api/chat/cbor_gen.go`

- 📄 `atproto/atdata/blob.go`

- 📄 `atproto/atdata/bytes.go`

- 📄 `atproto/atdata/cbor_gen.go`

- 📄 `atproto/atdata/cidlink.go`

- 📄 `atproto/labeling/cbor_gen.go`

- 📄 `atproto/repo/cbor_gen.go`

- 📄 `atproto/repo/mst/cbor_gen.go`

- 📄 `carstore/bs.go`

- 📄 `cmd/relay/stream/cbor_gen.go`

- 📄 `cmd/relay/stream/events.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `events/cbor_gen.go`

- 📄 `events/consumer.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `gen/main.go`

- 📄 `lex/util/cbor_gen.go`

- 📄 `lex/util/decoder.go`

- 📄 `lex/util/lex_types.go`

- 📄 `mst/cbor_gen.go`

- 📄 `repo/cbor_gen.go`

- 📄 `repo/repo.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/firehose.go`

- 📄 `util/labels/cbor_gen.go`




---


[import] path: github.com/whyrusleeping/go-did type: external


### github.com/whyrusleeping/go-did


- **Тип:** external

- **Алиасы:** `did`



### Кандидаты на типы


`Document`, `PrivKey`, `PubKey`


### Селекторы (любое использование `pkg.X`)


`Document`, `PrivKey`, `PubKey`


### Используется в файлах


- 📄 `repomgr/keymgr/keymgr.go`




---


[import] path: gitlab.com/yawning/secp256k1-voi type: external


### gitlab.com/yawning/secp256k1-voi


- **Тип:** external

- **Алиасы:** `secp256k1`



### Вызовы


`NewIdentityPoint`, `NewPointFromCoords`


### Селекторы (любое использование `pkg.X`)


`NewIdentityPoint`, `NewPointFromCoords`


### Используется в файлах


- 📄 `atproto/atcrypto/jwk.go`

- 📄 `atproto/atcrypto/k256.go`




---


[import] path: gitlab.com/yawning/secp256k1-voi/secec type: external


### gitlab.com/yawning/secp256k1-voi/secec


- **Тип:** external

- **Алиасы:** `secp256k1secec`



### Вызовы


`GenerateKey`, `NewPrivateKey`, `NewPublicKey`, `NewPublicKeyFromPoint`


### Кандидаты на типы


`ECDSAOptions`, `PrivateKey`, `PublicKey`


### Селекторы (любое использование `pkg.X`)


`ECDSAOptions`, `EncodingCompact`, `GenerateKey`, `NewPrivateKey`, `NewPublicKey`, `NewPublicKeyFromPoint`, `PrivateKey`, `PublicKey`


### Используется в файлах


- 📄 `atproto/atcrypto/jwk.go`

- 📄 `atproto/atcrypto/k256.go`




---


[import] path: go.opentelemetry.io/contrib/instrumentation/github.com/labstack/echo/otelecho type: external


### go.opentelemetry.io/contrib/instrumentation/github.com/labstack/echo/otelecho


- **Тип:** external

- **Алиасы:** `otelecho`



### Вызовы


`Middleware`


### Селекторы (любое использование `pkg.X`)


`Middleware`


### Используется в файлах


- 📄 `search/server.go`




---


[import] path: go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp type: external


### go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp


- **Тип:** external

- **Алиасы:** `otelhttp`



### Вызовы


`NewTransport`


### Селекторы (любое использование `pkg.X`)


`NewTransport`


### Используется в файлах


- 📄 `backfill/backfill.go`

- 📄 `util/http.go`




---


[import] path: go.opentelemetry.io/otel type: external


### go.opentelemetry.io/otel


- **Тип:** external

- **Алиасы:** `otel`



### Вызовы


`SetTracerProvider`, `Tracer`


### Селекторы (любое использование `pkg.X`)


`SetTracerProvider`, `Tracer`


### Используется в файлах


- 📄 `backfill/backfill.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/last_shard_cache.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/stream/eventmgr/event_manager.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `events/events.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/keymgr/keymgr.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/handlers.go`

- 📄 `util/tracing/tracing.go`




---


[import] path: go.opentelemetry.io/otel/attribute type: external


### go.opentelemetry.io/otel/attribute


- **Тип:** external

- **Алиасы:** `attribute`



### Вызовы


`Bool`, `Int`, `Int64`, `String`


### Селекторы (любое использование `pkg.X`)


`Bool`, `Int`, `Int64`, `String`


### Используется в файлах


- 📄 `carstore/bs.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/handlers.go`

- 📄 `search/indexing.go`

- 📄 `search/query.go`




---


[import] path: go.opentelemetry.io/otel/codes type: external


### go.opentelemetry.io/otel/codes


- **Тип:** external

- **Алиасы:** `codes`



### Селекторы (любое использование `pkg.X`)


`Error`


### Используется в файлах


- 📄 `search/handlers.go`




---


[import] path: go.opentelemetry.io/otel/exporters/jaeger type: external


### go.opentelemetry.io/otel/exporters/jaeger


- **Тип:** external

- **Алиасы:** `jaeger`



### Вызовы


`New`, `WithCollectorEndpoint`, `WithEndpoint`


### Селекторы (любое использование `pkg.X`)


`New`, `WithCollectorEndpoint`, `WithEndpoint`


### Используется в файлах


- 📄 `cmd/relay/otel.go`




---


[import] path: go.opentelemetry.io/otel/exporters/otlp/otlptrace type: external


### go.opentelemetry.io/otel/exporters/otlp/otlptrace


- **Тип:** external

- **Алиасы:** `otlptrace`



### Вызовы


`New`


### Селекторы (любое использование `pkg.X`)


`New`


### Используется в файлах


- 📄 `util/tracing/tracing.go`




---


[import] path: go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp type: external


### go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp


- **Тип:** external

- **Алиасы:** `otlptracehttp`



### Вызовы


`New`, `NewClient`


### Селекторы (любое использование `pkg.X`)


`New`, `NewClient`


### Используется в файлах


- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `util/tracing/tracing.go`




---


[import] path: go.opentelemetry.io/otel/sdk/resource type: external


### go.opentelemetry.io/otel/sdk/resource


- **Тип:** external

- **Алиасы:** `resource`



### Вызовы


`Default`, `Merge`, `NewWithAttributes`


### Селекторы (любое использование `pkg.X`)


`Default`, `Merge`, `NewWithAttributes`


### Используется в файлах


- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `util/tracing/tracing.go`




---


[import] path: go.opentelemetry.io/otel/sdk/trace type: external


### go.opentelemetry.io/otel/sdk/trace


- **Тип:** external

- **Алиасы:** `sdktrace`, `tracesdk`



### Вызовы


`NewTracerProvider`, `TraceIDRatioBased`, `WithBatcher`, `WithResource`, `WithSampler`


### Кандидаты на типы


`TracerProvider`


### Селекторы (любое использование `pkg.X`)


`NewTracerProvider`, `SpanExporter`, `TraceIDRatioBased`, `TracerProvider`, `WithBatcher`, `WithResource`, `WithSampler`


### Используется в файлах


- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/otel.go`

- 📄 `util/tracing/tracing.go`




---


[import] path: go.opentelemetry.io/otel/semconv/v1.17.0 type: external


### go.opentelemetry.io/otel/semconv/v1.17.0


- **Тип:** external

- **Алиасы:** `semconv`



### Вызовы


`ServiceName`


### Селекторы (любое использование `pkg.X`)


`SchemaURL`, `ServiceName`


### Используется в файлах


- 📄 `util/tracing/tracing.go`




---


[import] path: go.opentelemetry.io/otel/semconv/v1.4.0 type: external


### go.opentelemetry.io/otel/semconv/v1.4.0


- **Тип:** external

- **Алиасы:** `semconv`



### Селекторы (любое использование `pkg.X`)


`SchemaURL`, `ServiceNameKey`


### Используется в файлах


- 📄 `cmd/hepa/otel.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/otel.go`




---


[import] path: go.uber.org/automaxprocs type: external


### go.uber.org/automaxprocs


- **Тип:** external

- **Алиасы:** `_`



### Используется в файлах


- 📄 `cmd/beemo/main.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/sonar/main.go`




---


[import] path: golang.org/x/net/publicsuffix type: external


### golang.org/x/net/publicsuffix


- **Тип:** external

- **Алиасы:** `publicsuffix`



### Вызовы


`EffectiveTLDPlusOne`


### Селекторы (любое использование `pkg.X`)


`EffectiveTLDPlusOne`


### Используется в файлах


- 📄 `lex/lexgen/util.go`




---


[import] path: golang.org/x/sync/errgroup type: external


### golang.org/x/sync/errgroup


- **Тип:** external

- **Алиасы:** `errgroup`



### Селекторы (любое использование `pkg.X`)


`Group`


### Используется в файлах


- 📄 `cmd/fakermaker/main.go`




---


[import] path: golang.org/x/sync/semaphore type: external


### golang.org/x/sync/semaphore


- **Тип:** external

- **Алиасы:** `semaphore`



### Вызовы


`NewWeighted`


### Селекторы (любое использование `pkg.X`)


`NewWeighted`


### Используется в файлах


- 📄 `backfill/backfill.go`




---


[import] path: golang.org/x/text/runes type: external


### golang.org/x/text/runes


- **Тип:** external

- **Алиасы:** `runes`



### Вызовы


`In`, `Remove`


### Селекторы (любое использование `pkg.X`)


`In`, `Remove`


### Используется в файлах


- 📄 `automod/keyword/tokenize.go`




---


[import] path: golang.org/x/text/transform type: external


### golang.org/x/text/transform


- **Тип:** external

- **Алиасы:** `transform`



### Вызовы


`Chain`, `String`


### Селекторы (любое использование `pkg.X`)


`Chain`, `String`


### Используется в файлах


- 📄 `automod/keyword/tokenize.go`




---


[import] path: golang.org/x/text/unicode/norm type: external


### golang.org/x/text/unicode/norm


- **Тип:** external

- **Алиасы:** `norm`



### Селекторы (любое использование `pkg.X`)


`NFC`, `NFD`


### Используется в файлах


- 📄 `automod/keyword/tokenize.go`




---


[import] path: golang.org/x/time/rate type: external


### golang.org/x/time/rate


- **Тип:** external

- **Алиасы:** `rate`



### Вызовы


`Limit`, `NewLimiter`


### Кандидаты на типы


`Limiter`


### Селекторы (любое использование `pkg.X`)


`Limit`, `Limiter`, `NewLimiter`


### Используется в файлах


- 📄 `atproto/identity/base_directory.go`

- 📄 `backfill/backfill.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/palomar/main.go`

- 📄 `search/indexing.go`




---


[import] path: golang.org/x/tools/imports type: external


### golang.org/x/tools/imports


- **Тип:** external

- **Алиасы:** `imports`



### Вызовы


`Process`


### Селекторы (любое использование `pkg.X`)


`Process`


### Используется в файлах


- 📄 `lex/gen.go`




---


[import] path: golang.org/x/xerrors type: external


### golang.org/x/xerrors


- **Тип:** external

- **Алиасы:** `xerrors`



### Вызовы


`Errorf`


### Селекторы (любое использование `pkg.X`)


`Errorf`


### Используется в файлах


- 📄 `api/atproto/cbor_gen.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/chat/cbor_gen.go`

- 📄 `atproto/atdata/cbor_gen.go`

- 📄 `atproto/labeling/cbor_gen.go`

- 📄 `atproto/repo/cbor_gen.go`

- 📄 `atproto/repo/mst/cbor_gen.go`

- 📄 `cmd/relay/stream/cbor_gen.go`

- 📄 `events/cbor_gen.go`

- 📄 `lex/util/cbor_gen.go`

- 📄 `lex/util/lex_types.go`

- 📄 `mst/cbor_gen.go`

- 📄 `repo/cbor_gen.go`

- 📄 `util/labels/cbor_gen.go`




---


[import] path: gorm.io/driver/postgres type: external


### gorm.io/driver/postgres


- **Тип:** external

- **Алиасы:** `postgres`



### Вызовы


`Open`


### Кандидаты на типы


`Dialector`


### Селекторы (любое использование `pkg.X`)


`Dialector`, `Open`


### Используется в файлах


- 📄 `carstore/meta_gorm.go`

- 📄 `cmd/tap/tap.go`

- 📄 `util/cliutil/util.go`




---


[import] path: gorm.io/driver/sqlite type: external


### gorm.io/driver/sqlite


- **Тип:** external

- **Алиасы:** `sqlite`



### Вызовы


`Open`


### Селекторы (любое использование `pkg.X`)


`Open`


### Используется в файлах


- 📄 `cmd/tap/tap.go`

- 📄 `util/cliutil/util.go`




---


[import] path: gorm.io/gorm type: external


### gorm.io/gorm


- **Тип:** external

- **Алиасы:** `gorm`



### Вызовы


`Expr`, `Open`


### Кандидаты на типы


`Config`, `DB`, `ErrDuplicatedKey`, `ErrRecordNotFound`


### Селекторы (любое использование `pkg.X`)


`Config`, `DB`, `DeletedAt`, `Dialector`, `ErrDuplicatedKey`, `ErrRecordNotFound`, `Expr`, `Model`, `Open`, `io`


### Используется в файлах


- 📄 `backfill/gormstore.go`

- 📄 `carstore/bs.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/nonarchive.go`

- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/domain_ban.go`

- 📄 `cmd/relay/relay/host.go`

- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/db_helpers.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/repo_manager.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/server.go`

- 📄 `cmd/tap/tap.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `models/models.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/indexing.go`

- 📄 `testing/pdsmodels/types.go`

- 📄 `util/cliutil/util.go`




---


[import] path: gorm.io/gorm/clause type: external


### gorm.io/gorm/clause


- **Тип:** external

- **Алиасы:** `clause`



### Вызовы


`AssignmentColumns`


### Кандидаты на типы


`Column`, `OnConflict`


### Селекторы (любое использование `pkg.X`)


`AssignmentColumns`, `Column`, `OnConflict`


### Используется в файлах


- 📄 `carstore/nonarchive.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/server.go`




---


[import] path: gorm.io/gorm/logger type: external


### gorm.io/gorm/logger


- **Тип:** external

- **Алиасы:** `logger`



### Вызовы


`Error`, `Info`


### Селекторы (любое использование `pkg.X`)


`Default`, `Error`, `Info`, `Silent`


### Используется в файлах


- 📄 `cmd/tap/tap.go`




---


[import] path: gorm.io/plugin/opentelemetry/tracing type: external


### gorm.io/plugin/opentelemetry/tracing


- **Тип:** external

- **Алиасы:** `tracing`



### Вызовы


`NewPlugin`


### Селекторы (любое использование `pkg.X`)


`NewPlugin`


### Используется в файлах


- 📄 `cmd/relay/main.go`



## Локальные пакеты



---


[import] path: github.com/bluesky-social/indigo/api/agnostic type: local


### github.com/bluesky-social/indigo/api/agnostic


- **Тип:** local

- **Алиасы:** `agnostic`, `comatproto`

- **Локальная директория пакета:** `api/agnostic`



### Вызовы


`RepoGetRecord`, `RepoListRecords`


### Селекторы (любое использование `pkg.X`)


`RepoGetRecord`, `RepoListRecords`


### Используется в файлах


- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/lexicon/resolve.go`




---


[import] path: github.com/bluesky-social/indigo/api/atproto type: local


### github.com/bluesky-social/indigo/api/atproto


- **Тип:** local

- **Алиасы:** `atproto`, `comatproto`

- **Локальная директория пакета:** `api/atproto`



### Вызовы


`AdminDisableAccountInvites`, `AdminDisableInviteCodes`, `AdminEnableAccountInvites`, `AdminGetAccountInfo`, `AdminGetInviteCodes`, `IdentityUpdateHandle`, `RepoCreateRecord`, `RepoDeleteRecord`, `RepoDescribeRepo`, `RepoGetRecord`, `RepoListRecords`, `RepoPutRecord`, `RepoUploadBlob`, `ServerCreateAccount`, `ServerCreateInviteCodes`, `ServerCreateSession`, `ServerDeleteAccount`, `ServerDescribeServer`, `ServerRefreshSession`, `ServerRequestAccountDelete`, `ServerRequestPasswordReset`, `ServerResetPassword`, `SyncGetHead`, `SyncGetRepo`, `SyncGetRepoStatus`, `SyncListHosts`, `SyncListRepos`, `SyncListReposByCollection`, `SyncRequestCrawl`, `TempFetchLabels`


### Кандидаты на типы


`AdminDefs_AccountView`, `AdminDefs_RepoRef`, `AdminDefs_ThreatSignature`, `AdminDisableAccountInvites_Input`, `AdminDisableInviteCodes_Input`, `AdminEnableAccountInvites_Input`, `IdentityDefs_IdentityInfo`, `IdentityResolveDid_Output`, `IdentityResolveHandle_Output`, `IdentityUpdateHandle_Input`, `LabelDefs_Label`, `LabelDefs_LabelValueDefinition`, `LabelDefs_LabelValueDefinitionStrings`, `LabelDefs_SelfLabel`, `LabelDefs_SelfLabels`, `LabelSubscribeLabels_Info`, `LabelSubscribeLabels_Labels`, `LexiconSchema`, `RepoApplyWrites_Input_Writes_Elem`, `RepoCreateRecord_Input`, `RepoDeleteRecord_Input`, `RepoListRecords_Record`, `RepoPutRecord_Input`, `RepoStrongRef`, `ServerCreateAccount_Input`, `ServerCreateInviteCodes_Input`, `ServerCreateSession_Input`, `ServerDefs_InviteCode`, `ServerDeleteAccount_Input`, `ServerRequestPasswordReset_Input`, `ServerResetPassword_Input`, `SyncGetHostStatus_Output`, `SyncGetLatestCommit_Output`, `SyncGetRepoStatus_Output`, `SyncListHosts_Host`, `SyncListHosts_Output`, `SyncListReposByCollection_Repo`, `SyncListRepos_Output`, `SyncListRepos_Repo`, `SyncRequestCrawl_Input`, `SyncSubscribeRepos_Account`, `SyncSubscribeRepos_Commit`, `SyncSubscribeRepos_Identity`, `SyncSubscribeRepos_Info`, `SyncSubscribeRepos_RepoOp`, `SyncSubscribeRepos_Sync`


### Селекторы (любое использование `pkg.X`)


`AdminDefs_AccountView`, `AdminDefs_RepoRef`, `AdminDefs_ThreatSignature`, `AdminDisableAccountInvites`, `AdminDisableAccountInvites_Input`, `AdminDisableInviteCodes`, `AdminDisableInviteCodes_Input`, `AdminEnableAccountInvites`, `AdminEnableAccountInvites_Input`, `AdminGetAccountInfo`, `AdminGetInviteCodes`, `IdentityDefs_IdentityInfo`, `IdentityRefreshIdentity_Input`, `IdentityResolveDid_Output`, `IdentityResolveHandle_Output`, `IdentityUpdateHandle`, `IdentityUpdateHandle_Input`, `LabelDefs_Label`, `LabelDefs_LabelValueDefinition`, `LabelDefs_LabelValueDefinitionStrings`, `LabelDefs_SelfLabel`, `LabelDefs_SelfLabels`, `LabelSubscribeLabels_Info`, `LabelSubscribeLabels_Labels`, `LexiconSchema`, `RepoApplyWrites_Input_Writes_Elem`, `RepoCreateRecord`, `RepoCreateRecord_Input`, `RepoDeleteRecord`, `RepoDeleteRecord_Input`, `RepoDescribeRepo`, `RepoGetRecord`, `RepoListRecords`, `RepoListRecords_Record`, `RepoPutRecord`, `RepoPutRecord_Input`, `RepoStrongRef`, `RepoUploadBlob`, `ServerCreateAccount`, `ServerCreateAccount_Input`, `ServerCreateInviteCodes`, `ServerCreateInviteCodes_Input`, `ServerCreateSession`, `ServerCreateSession_Input`, `ServerDefs_InviteCode`, `ServerDeleteAccount`, `ServerDeleteAccount_Input`, `ServerDescribeServer`, `ServerRefreshSession`, `ServerRequestAccountDelete`, `ServerRequestPasswordReset`, `ServerRequestPasswordReset_Input`, `ServerResetPassword`, `ServerResetPassword_Input`, `SyncGetHead`, `SyncGetHostStatus_Output`, `SyncGetLatestCommit_Output`, `SyncGetRepo`, `SyncGetRepoStatus`, `SyncGetRepoStatus_Output`, `SyncListHosts`, `SyncListHosts_Host`, `SyncListHosts_Output`, `SyncListRepos`, `SyncListReposByCollection`, `SyncListReposByCollection_Output`, `SyncListReposByCollection_Repo`, `SyncListRepos_Output`, `SyncListRepos_Repo`, `SyncRequestCrawl`, `SyncRequestCrawl_Input`, `SyncSubscribeRepos_Account`, `SyncSubscribeRepos_Commit`, `SyncSubscribeRepos_Identity`, `SyncSubscribeRepos_Info`, `SyncSubscribeRepos_RepoOp`, `SyncSubscribeRepos_Sync`, `TempFetchLabels`, `sync`


### Используется в файлах


- 📄 `api/bsky/actordefs.go`

- 📄 `api/bsky/actorprofile.go`

- 📄 `api/bsky/bookmarkdefs.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/bsky/draftdefs.go`

- 📄 `api/bsky/embedrecord.go`

- 📄 `api/bsky/feeddefs.go`

- 📄 `api/bsky/feedgenerator.go`

- 📄 `api/bsky/feedlike.go`

- 📄 `api/bsky/feedpost.go`

- 📄 `api/bsky/feedrepost.go`

- 📄 `api/bsky/graphdefs.go`

- 📄 `api/bsky/graphfollow.go`

- 📄 `api/bsky/graphlist.go`

- 📄 `api/bsky/labelerdefs.go`

- 📄 `api/bsky/labelerservice.go`

- 📄 `api/bsky/notificationlistNotifications.go`

- 📄 `api/chat/actordefs.go`

- 📄 `api/ozone/moderationdefs.go`

- 📄 `api/ozone/moderationemitEvent.go`

- 📄 `api/ozone/signaturefindRelatedAccounts.go`

- 📄 `api/ozone/signaturesearchAccounts.go`

- 📄 `atproto/labeling/label.go`

- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `atproto/repo/sync.go`

- 📄 `automod/capture/capture.go`

- 📄 `automod/capture/fetch.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/persist.go`

- 📄 `automod/engine/persisthelpers.go`

- 📄 `backfill/backfill.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/bluepages/handlers.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/account.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/handle.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/relay/stream/consumer.go`

- 📄 `cmd/relay/stream/events.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `cmd/relay/testing/consumer.go`

- 📄 `cmd/relay/testing/scenario.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/util.go`

- 📄 `events/consumer.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `fakedata/accounts.go`

- 📄 `fakedata/generators.go`

- 📄 `gen/main.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/firehose.go`

- 📄 `splitter/handlers.go`

- 📄 `testing/utils.go`

- 📄 `util/labels/labels.go`



### Определения локальных типов (best effort)


#### AdminDefs_AccountView (struct)


*Определено в: `api/atproto/admindefs.go:12`*


| Поле | Тип | JSON |

|------|-----|------|

| `DeactivatedAt` | `*string` | `deactivatedAt` |

| `Did` | `string` | `did` |

| `Email` | `*string` | `email` |

| `EmailConfirmedAt` | `*string` | `emailConfirmedAt` |

| `Handle` | `string` | `handle` |

| `IndexedAt` | `string` | `indexedAt` |

| `InviteNote` | `*string` | `inviteNote` |

| `InvitedBy` | `*ServerDefs_InviteCode` | `invitedBy` |

| `Invites` | `[]*ServerDefs_InviteCode` | `invites` |

| `InvitesDisabled` | `*bool` | `invitesDisabled` |

| `RelatedRecords` | `[]*lexutil.LexiconTypeDecoder` | `relatedRecords` |

| `ThreatSignatures` | `[]*AdminDefs_ThreatSignature` | `threatSignatures` |



#### AdminDefs_RepoRef (struct)


*Определено в: `api/atproto/admindefs.go:36`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Did` | `string` | `did` |



#### AdminDefs_ThreatSignature (struct)


*Определено в: `api/atproto/admindefs.go:48`*


| Поле | Тип | JSON |

|------|-----|------|

| `Property` | `string` | `property` |

| `Value` | `string` | `value` |



#### AdminDisableAccountInvites_Input (struct)


*Определено в: `api/atproto/admindisableAccountInvites.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Account` | `string` | `account` |

| `Note` | `*string` | `note` |



#### AdminDisableInviteCodes_Input (struct)


*Определено в: `api/atproto/admindisableInviteCodes.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Accounts` | `[]string` | `accounts` |

| `Codes` | `[]string` | `codes` |



#### AdminEnableAccountInvites_Input (struct)


*Определено в: `api/atproto/adminenableAccountInvites.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Account` | `string` | `account` |

| `Note` | `*string` | `note` |



#### IdentityDefs_IdentityInfo (struct)


*Определено в: `api/atproto/identitydefs.go:8`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `did` |

| `DidDoc` | `unknown` | `didDoc` |

| `Handle` | `string` | `handle` |



#### IdentityResolveDid_Output (struct)


*Определено в: `api/atproto/identityresolveDid.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `DidDoc` | `unknown` | `didDoc` |



#### IdentityResolveHandle_Output (struct)


*Определено в: `api/atproto/identityresolveHandle.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `did` |



#### IdentityUpdateHandle_Input (struct)


*Определено в: `api/atproto/identityupdateHandle.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Handle` | `string` | `handle` |



#### LabelDefs_Label (struct)


*Определено в: `api/atproto/labeldefs.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cid` | `*string` | `cid` |

| `Cts` | `string` | `cts` |

| `Exp` | `*string` | `exp` |

| `Neg` | `*bool` | `neg` |

| `Sig` | `unknown` | `sig` |

| `Src` | `string` | `src` |

| `Uri` | `string` | `uri` |

| `Val` | `string` | `val` |

| `Ver` | `*int64` | `ver` |



#### LabelDefs_LabelValueDefinition (struct)


*Определено в: `api/atproto/labeldefs.go:38`*


| Поле | Тип | JSON |

|------|-----|------|

| `AdultOnly` | `*bool` | `adultOnly` |

| `Blurs` | `string` | `blurs` |

| `DefaultSetting` | `*string` | `defaultSetting` |

| `Identifier` | `string` | `identifier` |

| `Locales` | `[]*LabelDefs_LabelValueDefinitionStrings` | `locales` |

| `Severity` | `string` | `severity` |



#### LabelDefs_LabelValueDefinitionStrings (struct)


*Определено в: `api/atproto/labeldefs.go:55`*


| Поле | Тип | JSON |

|------|-----|------|

| `Description` | `string` | `description` |

| `Lang` | `string` | `lang` |

| `Name` | `string` | `name` |



#### LabelDefs_SelfLabel (struct)


*Определено в: `api/atproto/labeldefs.go:67`*


| Поле | Тип | JSON |

|------|-----|------|

| `Val` | `string` | `val` |



#### LabelDefs_SelfLabels (struct)


*Определено в: `api/atproto/labeldefs.go:75`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Values` | `[]*LabelDefs_SelfLabel` | `values` |



#### LabelSubscribeLabels_Info (struct)


*Определено в: `api/atproto/labelsubscribeLabels.go:8`*


| Поле | Тип | JSON |

|------|-----|------|

| `Message` | `*string` | `message` |

| `Name` | `string` | `name` |



#### LabelSubscribeLabels_Labels (struct)


*Определено в: `api/atproto/labelsubscribeLabels.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Labels` | `[]*LabelDefs_Label` | `labels` |

| `Seq` | `int64` | `seq` |



#### LexiconSchema (struct)


*Определено в: `api/atproto/lexiconschema.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Lexicon` | `int64` | `lexicon` |



#### RepoApplyWrites_Input_Writes_Elem (struct)


*Определено в: `api/atproto/repoapplyWrites.go:59`*


| Поле | Тип | JSON |

|------|-----|------|

| `RepoApplyWrites_Create` | `*RepoApplyWrites_Create` | `RepoApplyWritesCreate` |

| `RepoApplyWrites_Update` | `*RepoApplyWrites_Update` | `RepoApplyWritesUpdate` |

| `RepoApplyWrites_Delete` | `*RepoApplyWrites_Delete` | `RepoApplyWritesDelete` |



#### RepoCreateRecord_Input (struct)


*Определено в: `api/atproto/repocreateRecord.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Collection` | `string` | `collection` |

| `Record` | `*lexutil.LexiconTypeDecoder` | `record` |

| `Repo` | `string` | `repo` |

| `Rkey` | `*string` | `rkey` |

| `SwapCommit` | `*string` | `swapCommit` |

| `Validate` | `*bool` | `validate` |



#### RepoDeleteRecord_Input (struct)


*Определено в: `api/atproto/repodeleteRecord.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Collection` | `string` | `collection` |

| `Repo` | `string` | `repo` |

| `Rkey` | `string` | `rkey` |

| `SwapCommit` | `*string` | `swapCommit` |

| `SwapRecord` | `*string` | `swapRecord` |



#### RepoListRecords_Record (struct)


*Определено в: `api/atproto/repolistRecords.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cid` | `string` | `cid` |

| `Uri` | `string` | `uri` |

| `Value` | `*lexutil.LexiconTypeDecoder` | `value` |



#### RepoPutRecord_Input (struct)


*Определено в: `api/atproto/repoputRecord.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Collection` | `string` | `collection` |

| `Record` | `*lexutil.LexiconTypeDecoder` | `record` |

| `Repo` | `string` | `repo` |

| `Rkey` | `string` | `rkey` |

| `SwapCommit` | `*string` | `swapCommit` |

| `SwapRecord` | `*string` | `swapRecord` |

| `Validate` | `*bool` | `validate` |



#### RepoStrongRef (struct)


*Определено в: `api/atproto/repostrongRef.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Cid` | `string` | `cid` |

| `Uri` | `string` | `uri` |



#### ServerCreateAccount_Input (struct)


*Определено в: `api/atproto/servercreateAccount.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `*string` | `did` |

| `Email` | `*string` | `email` |

| `Handle` | `string` | `handle` |

| `InviteCode` | `*string` | `inviteCode` |

| `Password` | `*string` | `password` |

| `PlcOp` | `*interface{}` | `plcOp` |

| `RecoveryKey` | `*string` | `recoveryKey` |

| `VerificationCode` | `*string` | `verificationCode` |

| `VerificationPhone` | `*string` | `verificationPhone` |



#### ServerCreateInviteCodes_Input (struct)


*Определено в: `api/atproto/servercreateInviteCodes.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `CodeCount` | `int64` | `codeCount` |

| `ForAccounts` | `[]string` | `forAccounts` |

| `UseCount` | `int64` | `useCount` |



#### ServerCreateSession_Input (struct)


*Определено в: `api/atproto/servercreateSession.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `AllowTakendown` | `*bool` | `allowTakendown` |

| `AuthFactorToken` | `*string` | `authFactorToken` |

| `Identifier` | `string` | `identifier` |

| `Password` | `string` | `password` |



#### ServerDefs_InviteCode (struct)


*Определено в: `api/atproto/serverdefs.go:8`*


| Поле | Тип | JSON |

|------|-----|------|

| `Available` | `int64` | `available` |

| `Code` | `string` | `code` |

| `CreatedAt` | `string` | `createdAt` |

| `CreatedBy` | `string` | `createdBy` |

| `Disabled` | `bool` | `disabled` |

| `ForAccount` | `string` | `forAccount` |

| `Uses` | `[]*ServerDefs_InviteCodeUse` | `uses` |



#### ServerDeleteAccount_Input (struct)


*Определено в: `api/atproto/serverdeleteAccount.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `did` |

| `Password` | `string` | `password` |

| `Token` | `string` | `token` |



#### ServerRequestPasswordReset_Input (struct)


*Определено в: `api/atproto/serverrequestPasswordReset.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Email` | `string` | `email` |



#### ServerResetPassword_Input (struct)


*Определено в: `api/atproto/serverresetPassword.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Password` | `string` | `password` |

| `Token` | `string` | `token` |



#### SyncGetHostStatus_Output (struct)


*Определено в: `api/atproto/syncgetHostStatus.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `AccountCount` | `*int64` | `accountCount` |

| `Hostname` | `string` | `hostname` |

| `Seq` | `*int64` | `seq` |

| `Status` | `*string` | `status` |



#### SyncGetLatestCommit_Output (struct)


*Определено в: `api/atproto/syncgetLatestCommit.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cid` | `string` | `cid` |

| `Rev` | `string` | `rev` |



#### SyncGetRepoStatus_Output (struct)


*Определено в: `api/atproto/syncgetRepoStatus.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Active` | `bool` | `active` |

| `Did` | `string` | `did` |

| `Rev` | `*string` | `rev` |

| `Status` | `*string` | `status` |



#### SyncListHosts_Host (struct)


*Определено в: `api/atproto/synclistHosts.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `AccountCount` | `*int64` | `accountCount` |

| `Hostname` | `string` | `hostname` |

| `Seq` | `*int64` | `seq` |

| `Status` | `*string` | `status` |



#### SyncListHosts_Output (struct)


*Определено в: `api/atproto/synclistHosts.go:24`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cursor` | `*string` | `cursor` |

| `Hosts` | `[]*SyncListHosts_Host` | `hosts` |



#### SyncListReposByCollection_Repo (struct)


*Определено в: `api/atproto/synclistReposByCollection.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `did` |



#### SyncListRepos_Output (struct)


*Определено в: `api/atproto/synclistRepos.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cursor` | `*string` | `cursor` |

| `Repos` | `[]*SyncListRepos_Repo` | `repos` |



#### SyncListRepos_Repo (struct)


*Определено в: `api/atproto/synclistRepos.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `Active` | `*bool` | `active` |

| `Did` | `string` | `did` |

| `Head` | `string` | `head` |

| `Rev` | `string` | `rev` |

| `Status` | `*string` | `status` |



#### SyncRequestCrawl_Input (struct)


*Определено в: `api/atproto/syncrequestCrawl.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Hostname` | `string` | `hostname` |



#### SyncSubscribeRepos_Account (struct)


*Определено в: `api/atproto/syncsubscribeRepos.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Active` | `bool` | `active` |

| `Did` | `string` | `did` |

| `Seq` | `int64` | `seq` |

| `Status` | `*string` | `status` |

| `Time` | `string` | `time` |



#### SyncSubscribeRepos_Commit (struct)


*Определено в: `api/atproto/syncsubscribeRepos.go:27`*


| Поле | Тип | JSON |

|------|-----|------|

| `Blobs` | `[]lexutil.LexLink` | `blobs` |

| `Blocks` | `unknown` | `blocks` |

| `Commit` | `unknown` | `commit` |

| `Ops` | `[]*SyncSubscribeRepos_RepoOp` | `ops` |

| `PrevData` | `*lexutil.LexLink` | `prevData` |

| `Rebase` | `bool` | `rebase` |

| `Repo` | `string` | `repo` |

| `Rev` | `string` | `rev` |

| `Seq` | `int64` | `seq` |

| `Since` | `*string` | `since` |

| `Time` | `string` | `time` |

| `TooBig` | `bool` | `tooBig` |



#### SyncSubscribeRepos_Identity (struct)


*Определено в: `api/atproto/syncsubscribeRepos.go:55`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `did` |

| `Handle` | `*string` | `handle` |

| `Seq` | `int64` | `seq` |

| `Time` | `string` | `time` |



#### SyncSubscribeRepos_Info (struct)


*Определено в: `api/atproto/syncsubscribeRepos.go:64`*


| Поле | Тип | JSON |

|------|-----|------|

| `Message` | `*string` | `message` |

| `Name` | `string` | `name` |



#### SyncSubscribeRepos_RepoOp (struct)


*Определено в: `api/atproto/syncsubscribeRepos.go:72`*


| Поле | Тип | JSON |

|------|-----|------|

| `Action` | `string` | `action` |

| `Cid` | `*lexutil.LexLink` | `cid` |

| `Path` | `string` | `path` |

| `Prev` | `*lexutil.LexLink` | `prev` |



#### SyncSubscribeRepos_Sync (struct)


*Определено в: `api/atproto/syncsubscribeRepos.go:84`*


| Поле | Тип | JSON |

|------|-----|------|

| `Blocks` | `unknown` | `blocks` |

| `Did` | `string` | `did` |

| `Rev` | `string` | `rev` |

| `Seq` | `int64` | `seq` |

| `Time` | `string` | `time` |




---


[import] path: github.com/bluesky-social/indigo/api/bsky type: local


### github.com/bluesky-social/indigo/api/bsky


- **Тип:** local

- **Алиасы:** `appbsky`, `bsky`

- **Локальная директория пакета:** `api/bsky`



### Вызовы


`ActorGetProfile`, `ActorGetSuggestions`, `FeedDescribeFeedGenerator`, `FeedGetAuthorFeed`, `FeedGetFeedSkeleton`, `FeedGetPostThread`, `FeedGetPosts`, `FeedGetTimeline`, `GraphGetFollows`, `GraphGetRelationships`, `GraphMuteActor`, `NotificationGetUnreadCount`, `NotificationListNotifications`


### Кандидаты на типы


`ActorDefs_ProfileAssociated`, `ActorDefs_ProfileView`, `ActorDefs_ProfileViewBasic`, `ActorDefs_ProfileViewDetailed`, `ActorDefs_VerificationState`, `ActorDefs_ViewerState`, `ActorProfile`, `ActorStatus`, `EmbedDefs_AspectRatio`, `EmbedExternal`, `EmbedExternal_External`, `EmbedExternal_View`, `EmbedExternal_ViewExternal`, `EmbedImages`, `EmbedImages_Image`, `EmbedImages_View`, `EmbedImages_ViewImage`, `EmbedRecord`, `EmbedRecordWithMedia`, `EmbedRecordWithMedia_View`, `EmbedRecord_View`, `EmbedRecord_ViewNotFound`, `EmbedRecord_ViewRecord`, `EmbedVideo`, `EmbedVideo_Caption`, `FeedDefs_FeedViewPost`, `FeedDefs_NotFoundPost`, `FeedDefs_PostView`, `FeedDefs_ThreadViewPost`, `FeedGenerator`, `FeedLike`, `FeedPost`, `FeedPost_Embed`, `FeedPost_Entity`, `FeedPost_ReplyRef`, `FeedPost_TextSlice`, `FeedPostgate`, `FeedPostgate_DisableRule`, `FeedRepost`, `FeedThreadgate`, `FeedThreadgate_FollowerRule`, `FeedThreadgate_FollowingRule`, `FeedThreadgate_ListRule`, `FeedThreadgate_MentionRule`, `GraphBlock`, `GraphFollow`, `GraphList`, `GraphListblock`, `GraphListitem`, `GraphMuteActor_Input`, `GraphStarterpack`, `GraphStarterpack_FeedItem`, `GraphVerification`, `LabelerDefs_LabelerPolicies`, `LabelerService`, `NotificationDeclaration`, `RichtextFacet`, `RichtextFacet_ByteSlice`, `RichtextFacet_Link`, `RichtextFacet_Mention`, `RichtextFacet_Tag`, `UnspeccedDefs_SkeletonSearchActor`, `UnspeccedDefs_SkeletonSearchPost`, `UnspeccedSearchActorsSkeleton_Output`, `UnspeccedSearchPostsSkeleton_Output`


### Селекторы (любое использование `pkg.X`)


`ActorDefs_ProfileAssociated`, `ActorDefs_ProfileView`, `ActorDefs_ProfileViewBasic`, `ActorDefs_ProfileViewDetailed`, `ActorDefs_VerificationState`, `ActorDefs_ViewerState`, `ActorGetProfile`, `ActorGetSuggestions`, `ActorProfile`, `ActorStatus`, `EmbedDefs_AspectRatio`, `EmbedExternal`, `EmbedExternal_External`, `EmbedExternal_View`, `EmbedExternal_ViewExternal`, `EmbedImages`, `EmbedImages_Image`, `EmbedImages_View`, `EmbedImages_ViewImage`, `EmbedRecord`, `EmbedRecordWithMedia`, `EmbedRecordWithMedia_View`, `EmbedRecord_View`, `EmbedRecord_ViewNotFound`, `EmbedRecord_ViewRecord`, `EmbedVideo`, `EmbedVideo_Caption`, `FeedDefs_FeedViewPost`, `FeedDefs_NotFoundPost`, `FeedDefs_PostView`, `FeedDefs_ThreadViewPost`, `FeedDescribeFeedGenerator`, `FeedGenerator`, `FeedGetAuthorFeed`, `FeedGetFeedSkeleton`, `FeedGetPostThread`, `FeedGetPosts`, `FeedGetTimeline`, `FeedLike`, `FeedPost`, `FeedPost_Embed`, `FeedPost_Entity`, `FeedPost_ReplyRef`, `FeedPost_TextSlice`, `FeedPostgate`, `FeedPostgate_DisableRule`, `FeedRepost`, `FeedThreadgate`, `FeedThreadgate_FollowerRule`, `FeedThreadgate_FollowingRule`, `FeedThreadgate_ListRule`, `FeedThreadgate_MentionRule`, `GraphBlock`, `GraphFollow`, `GraphGetFollows`, `GraphGetRelationships`, `GraphList`, `GraphListblock`, `GraphListitem`, `GraphMuteActor`, `GraphMuteActor_Input`, `GraphStarterpack`, `GraphStarterpack_FeedItem`, `GraphVerification`, `LabelerDefs_LabelerPolicies`, `LabelerService`, `NotificationDeclaration`, `NotificationGetUnreadCount`, `NotificationListNotifications`, `RichtextFacet`, `RichtextFacet_ByteSlice`, `RichtextFacet_Link`, `RichtextFacet_Mention`, `RichtextFacet_Tag`, `UnspeccedDefs_SkeletonSearchActor`, `UnspeccedDefs_SkeletonSearchPost`, `UnspeccedSearchActorsSkeleton_Output`, `UnspeccedSearchPostsSkeleton_Output`, `actor`, `app`, `auth`, `feed`, `graph`, `network`, `social`


### Используется в файлах


- 📄 `api/chat/actordefs.go`

- 📄 `api/chat/convodefs.go`

- 📄 `api/ozone/teamdefs.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/fetch_relationship.go`

- 📄 `automod/engine/ruleset.go`

- 📄 `automod/engine/ruletypes.go`

- 📄 `automod/engine/testing.go`

- 📄 `automod/helpers/bsky.go`

- 📄 `automod/rules/gtube.go`

- 📄 `automod/rules/harassment.go`

- 📄 `automod/rules/hashtags.go`

- 📄 `automod/rules/keyword.go`

- 📄 `automod/rules/mentions.go`

- 📄 `automod/rules/misleading.go`

- 📄 `automod/rules/misleading_unicode_reverse.go`

- 📄 `automod/rules/nostr.go`

- 📄 `automod/rules/private.go`

- 📄 `automod/rules/profile.go`

- 📄 `automod/rules/promo.go`

- 📄 `automod/rules/quick.go`

- 📄 `automod/rules/replies.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `fakedata/generators.go`

- 📄 `gen/main.go`

- 📄 `models/models.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/bulk.go`

- 📄 `search/firehose.go`

- 📄 `search/handlers.go`

- 📄 `search/indexing.go`

- 📄 `search/transform.go`

- 📄 `testing/utils.go`



### Определения локальных типов (best effort)


#### ActorDefs_ProfileAssociated (struct)


*Определено в: `api/bsky/actordefs.go:361`*


| Поле | Тип | JSON |

|------|-----|------|

| `ActivitySubscription` | `*ActorDefs_ProfileAssociatedActivitySubscription` | `activitySubscription` |

| `Chat` | `*ActorDefs_ProfileAssociatedChat` | `chat` |

| `Feedgens` | `*int64` | `feedgens` |

| `Labeler` | `*bool` | `labeler` |

| `Lists` | `*int64` | `lists` |

| `StarterPacks` | `*int64` | `starterPacks` |



#### ActorDefs_ProfileView (struct)


*Определено в: `api/bsky/actordefs.go:381`*


| Поле | Тип | JSON |

|------|-----|------|

| `Associated` | `*ActorDefs_ProfileAssociated` | `associated` |

| `Avatar` | `*string` | `avatar` |

| `CreatedAt` | `*string` | `createdAt` |

| `Debug` | `*interface{}` | `debug` |

| `Description` | `*string` | `description` |

| `Did` | `string` | `did` |

| `DisplayName` | `*string` | `displayName` |

| `Handle` | `string` | `handle` |

| `IndexedAt` | `*string` | `indexedAt` |

| `Labels` | `[]*comatproto.LabelDefs_Label` | `labels` |

| `Pronouns` | `*string` | `pronouns` |

| `Status` | `*ActorDefs_StatusView` | `status` |

| `Verification` | `*ActorDefs_VerificationState` | `verification` |

| `Viewer` | `*ActorDefs_ViewerState` | `viewer` |



#### ActorDefs_ProfileViewBasic (struct)


*Определено в: `api/bsky/actordefs.go:400`*


| Поле | Тип | JSON |

|------|-----|------|

| `Associated` | `*ActorDefs_ProfileAssociated` | `associated` |

| `Avatar` | `*string` | `avatar` |

| `CreatedAt` | `*string` | `createdAt` |

| `Debug` | `*interface{}` | `debug` |

| `Did` | `string` | `did` |

| `DisplayName` | `*string` | `displayName` |

| `Handle` | `string` | `handle` |

| `Labels` | `[]*comatproto.LabelDefs_Label` | `labels` |

| `Pronouns` | `*string` | `pronouns` |

| `Status` | `*ActorDefs_StatusView` | `status` |

| `Verification` | `*ActorDefs_VerificationState` | `verification` |

| `Viewer` | `*ActorDefs_ViewerState` | `viewer` |



#### ActorDefs_ProfileViewDetailed (struct)


*Определено в: `api/bsky/actordefs.go:417`*


| Поле | Тип | JSON |

|------|-----|------|

| `Associated` | `*ActorDefs_ProfileAssociated` | `associated` |

| `Avatar` | `*string` | `avatar` |

| `Banner` | `*string` | `banner` |

| `CreatedAt` | `*string` | `createdAt` |

| `Debug` | `*interface{}` | `debug` |

| `Description` | `*string` | `description` |

| `Did` | `string` | `did` |

| `DisplayName` | `*string` | `displayName` |

| `FollowersCount` | `*int64` | `followersCount` |

| `FollowsCount` | `*int64` | `followsCount` |

| `Handle` | `string` | `handle` |

| `IndexedAt` | `*string` | `indexedAt` |

| `JoinedViaStarterPack` | `*GraphDefs_StarterPackViewBasic` | `joinedViaStarterPack` |

| `Labels` | `[]*comatproto.LabelDefs_Label` | `labels` |

| `PinnedPost` | `*comatproto.RepoStrongRef` | `pinnedPost` |

| `PostsCount` | `*int64` | `postsCount` |

| `Pronouns` | `*string` | `pronouns` |

| `Status` | `*ActorDefs_StatusView` | `status` |

| `Verification` | `*ActorDefs_VerificationState` | `verification` |

| `Viewer` | `*ActorDefs_ViewerState` | `viewer` |

| `Website` | `*string` | `website` |



#### ActorDefs_VerificationState (struct)


*Определено в: `api/bsky/actordefs.go:524`*


| Поле | Тип | JSON |

|------|-----|------|

| `TrustedVerifierStatus` | `string` | `trustedVerifierStatus` |

| `Verifications` | `[]*ActorDefs_VerificationView` | `verifications` |

| `VerifiedStatus` | `string` | `verifiedStatus` |



#### ActorDefs_ViewerState (struct)


*Определено в: `api/bsky/actordefs.go:550`*


| Поле | Тип | JSON |

|------|-----|------|

| `ActivitySubscription` | `*NotificationDefs_ActivitySubscription` | `activitySubscription` |

| `BlockedBy` | `*bool` | `blockedBy` |

| `Blocking` | `*string` | `blocking` |

| `BlockingByList` | `*GraphDefs_ListViewBasic` | `blockingByList` |

| `FollowedBy` | `*string` | `followedBy` |

| `Following` | `*string` | `following` |

| `KnownFollowers` | `*ActorDefs_KnownFollowers` | `knownFollowers` |

| `Muted` | `*bool` | `muted` |

| `MutedByList` | `*GraphDefs_ListViewBasic` | `mutedByList` |



#### ActorProfile (struct)


*Определено в: `api/bsky/actorprofile.go:22`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Avatar` | `*lexutil.LexBlob` | `avatar` |

| `Banner` | `*lexutil.LexBlob` | `banner` |

| `CreatedAt` | `*string` | `createdAt` |

| `Description` | `*string` | `description` |

| `DisplayName` | `*string` | `displayName` |

| `JoinedViaStarterPack` | `*comatproto.RepoStrongRef` | `joinedViaStarterPack` |

| `Labels` | `*ActorProfile_Labels` | `labels` |

| `PinnedPost` | `*comatproto.RepoStrongRef` | `pinnedPost` |

| `Pronouns` | `*string` | `pronouns` |

| `Website` | `*string` | `website` |



#### ActorStatus (struct)


*Определено в: `api/bsky/actorstatus.go:21`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `DurationMinutes` | `*int64` | `durationMinutes` |

| `Embed` | `*ActorStatus_Embed` | `embed` |

| `Status` | `string` | `status` |



#### EmbedDefs_AspectRatio (struct)


*Определено в: `api/bsky/embeddefs.go:10`*


| Поле | Тип | JSON |

|------|-----|------|

| `Height` | `int64` | `height` |

| `Width` | `int64` | `width` |



#### EmbedExternal (struct)


*Определено в: `api/bsky/embedexternal.go:18`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `External` | `*EmbedExternal_External` | `external` |



#### EmbedExternal_External (struct)


*Определено в: `api/bsky/embedexternal.go:24`*


| Поле | Тип | JSON |

|------|-----|------|

| `Description` | `string` | `description` |

| `Thumb` | `*lexutil.LexBlob` | `thumb` |

| `Title` | `string` | `title` |

| `Uri` | `string` | `uri` |



#### EmbedExternal_View (struct)


*Определено в: `api/bsky/embedexternal.go:32`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `External` | `*EmbedExternal_ViewExternal` | `external` |



#### EmbedExternal_ViewExternal (struct)


*Определено в: `api/bsky/embedexternal.go:38`*


| Поле | Тип | JSON |

|------|-----|------|

| `Description` | `string` | `description` |

| `Thumb` | `*string` | `thumb` |

| `Title` | `string` | `title` |

| `Uri` | `string` | `uri` |



#### EmbedImages (struct)


*Определено в: `api/bsky/embedimages.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Images` | `[]*EmbedImages_Image` | `images` |



#### EmbedImages_Image (struct)


*Определено в: `api/bsky/embedimages.go:22`*


| Поле | Тип | JSON |

|------|-----|------|

| `Alt` | `string` | `alt` |

| `AspectRatio` | `*EmbedDefs_AspectRatio` | `aspectRatio` |

| `Image` | `*lexutil.LexBlob` | `image` |



#### EmbedImages_View (struct)


*Определено в: `api/bsky/embedimages.go:30`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Images` | `[]*EmbedImages_ViewImage` | `images` |



#### EmbedImages_ViewImage (struct)


*Определено в: `api/bsky/embedimages.go:36`*


| Поле | Тип | JSON |

|------|-----|------|

| `Alt` | `string` | `alt` |

| `AspectRatio` | `*EmbedDefs_AspectRatio` | `aspectRatio` |

| `Fullsize` | `string` | `fullsize` |

| `Thumb` | `string` | `thumb` |



#### EmbedRecord (struct)


*Определено в: `api/bsky/embedrecord.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Record` | `*comatproto.RepoStrongRef` | `record` |



#### EmbedRecordWithMedia (struct)


*Определено в: `api/bsky/embedrecordWithMedia.go:22`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Media` | `*EmbedRecordWithMedia_Media` | `media` |

| `Record` | `*EmbedRecord` | `record` |



#### EmbedRecordWithMedia_View (struct)


*Определено в: `api/bsky/embedrecordWithMedia.go:111`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Media` | `*EmbedRecordWithMedia_View_Media` | `media` |

| `Record` | `*EmbedRecord_View` | `record` |



#### EmbedRecord_View (struct)


*Определено в: `api/bsky/embedrecord.go:26`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Record` | `*EmbedRecord_View_Record` | `record` |



#### EmbedRecord_ViewNotFound (struct)


*Определено в: `api/bsky/embedrecord.go:47`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `NotFound` | `bool` | `notFound` |

| `Uri` | `string` | `uri` |



#### EmbedRecord_ViewRecord (struct)


*Определено в: `api/bsky/embedrecord.go:54`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Author` | `*ActorDefs_ProfileViewBasic` | `author` |

| `Cid` | `string` | `cid` |

| `Embeds` | `[]*EmbedRecord_ViewRecord_Embeds_Elem` | `embeds` |

| `IndexedAt` | `string` | `indexedAt` |

| `Labels` | `[]*comatproto.LabelDefs_Label` | `labels` |

| `LikeCount` | `*int64` | `likeCount` |

| `QuoteCount` | `*int64` | `quoteCount` |

| `ReplyCount` | `*int64` | `replyCount` |

| `RepostCount` | `*int64` | `repostCount` |

| `Uri` | `string` | `uri` |

| `Value` | `*lexutil.LexiconTypeDecoder` | `value` |



#### EmbedVideo (struct)


*Определено в: `api/bsky/embedvideo.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Alt` | `*string` | `alt` |

| `AspectRatio` | `*EmbedDefs_AspectRatio` | `aspectRatio` |

| `Captions` | `[]*EmbedVideo_Caption` | `captions` |

| `Video` | `*lexutil.LexBlob` | `video` |



#### EmbedVideo_Caption (struct)


*Определено в: `api/bsky/embedvideo.go:27`*


| Поле | Тип | JSON |

|------|-----|------|

| `File` | `*lexutil.LexBlob` | `file` |

| `Lang` | `string` | `lang` |



#### FeedDefs_FeedViewPost (struct)


*Определено в: `api/bsky/feeddefs.go:30`*


| Поле | Тип | JSON |

|------|-----|------|

| `FeedContext` | `*string` | `feedContext` |

| `Post` | `*FeedDefs_PostView` | `post` |

| `Reason` | `*FeedDefs_FeedViewPost_Reason` | `reason` |

| `Reply` | `*FeedDefs_ReplyRef` | `reply` |

| `ReqId` | `*string` | `reqId` |



#### FeedDefs_NotFoundPost (struct)


*Определено в: `api/bsky/feeddefs.go:110`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `NotFound` | `bool` | `notFound` |

| `Uri` | `string` | `uri` |



#### FeedDefs_PostView (struct)


*Определено в: `api/bsky/feeddefs.go:117`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Author` | `*ActorDefs_ProfileViewBasic` | `author` |

| `BookmarkCount` | `*int64` | `bookmarkCount` |

| `Cid` | `string` | `cid` |

| `Debug` | `*interface{}` | `debug` |

| `Embed` | `*FeedDefs_PostView_Embed` | `embed` |

| `IndexedAt` | `string` | `indexedAt` |

| `Labels` | `[]*comatproto.LabelDefs_Label` | `labels` |

| `LikeCount` | `*int64` | `likeCount` |

| `QuoteCount` | `*int64` | `quoteCount` |

| `Record` | `*lexutil.LexiconTypeDecoder` | `record` |

| `ReplyCount` | `*int64` | `replyCount` |

| `RepostCount` | `*int64` | `repostCount` |

| `Threadgate` | `*FeedDefs_ThreadgateView` | `threadgate` |

| `Uri` | `string` | `uri` |

| `Viewer` | `*FeedDefs_ViewerState` | `viewer` |



#### FeedDefs_ThreadViewPost (struct)


*Определено в: `api/bsky/feeddefs.go:366`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Parent` | `*FeedDefs_ThreadViewPost_Parent` | `parent` |

| `Post` | `*FeedDefs_PostView` | `post` |

| `Replies` | `[]*FeedDefs_ThreadViewPost_Replies_Elem` | `replies` |

| `ThreadContext` | `*FeedDefs_ThreadContext` | `threadContext` |



#### FeedGenerator (struct)


*Определено в: `api/bsky/feedgenerator.go:22`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `AcceptsInteractions` | `*bool` | `acceptsInteractions` |

| `Avatar` | `*lexutil.LexBlob` | `avatar` |

| `ContentMode` | `*string` | `contentMode` |

| `CreatedAt` | `string` | `createdAt` |

| `Description` | `*string` | `description` |

| `DescriptionFacets` | `[]*RichtextFacet` | `descriptionFacets` |

| `Did` | `string` | `did` |

| `DisplayName` | `string` | `displayName` |

| `Labels` | `*FeedGenerator_Labels` | `labels` |



#### FeedLike (struct)


*Определено в: `api/bsky/feedlike.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `Subject` | `*comatproto.RepoStrongRef` | `subject` |

| `Via` | `*comatproto.RepoStrongRef` | `via` |



#### FeedPost (struct)


*Определено в: `api/bsky/feedpost.go:22`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `Embed` | `*FeedPost_Embed` | `embed` |

| `Entities` | `[]*FeedPost_Entity` | `entities` |

| `Facets` | `[]*RichtextFacet` | `facets` |

| `Labels` | `*FeedPost_Labels` | `labels` |

| `Langs` | `[]string` | `langs` |

| `Reply` | `*FeedPost_ReplyRef` | `reply` |

| `Tags` | `[]string` | `tags` |

| `Text` | `string` | `text` |



#### FeedPost_Embed (struct)


*Определено в: `api/bsky/feedpost.go:42`*


| Поле | Тип | JSON |

|------|-----|------|

| `EmbedImages` | `*EmbedImages` | `EmbedImages` |

| `EmbedVideo` | `*EmbedVideo` | `EmbedVideo` |

| `EmbedExternal` | `*EmbedExternal` | `EmbedExternal` |

| `EmbedRecord` | `*EmbedRecord` | `EmbedRecord` |

| `EmbedRecordWithMedia` | `*EmbedRecordWithMedia` | `EmbedRecordWithMedia` |



#### FeedPost_Entity (struct)


*Определено в: `api/bsky/feedpost.go:155`*


| Поле | Тип | JSON |

|------|-----|------|

| `Index` | `*FeedPost_TextSlice` | `index` |

| `Type` | `string` | `type` |

| `Value` | `string` | `value` |



#### FeedPost_ReplyRef (struct)


*Определено в: `api/bsky/feedpost.go:218`*


| Поле | Тип | JSON |

|------|-----|------|

| `Parent` | `*comatproto.RepoStrongRef` | `parent` |

| `Root` | `*comatproto.RepoStrongRef` | `root` |



#### FeedPost_TextSlice (struct)


*Определено в: `api/bsky/feedpost.go:226`*


| Поле | Тип | JSON |

|------|-----|------|

| `End` | `int64` | `end` |

| `Start` | `int64` | `start` |



#### FeedPostgate (struct)


*Определено в: `api/bsky/feedpostgate.go:21`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `DetachedEmbeddingUris` | `[]string` | `detachedEmbeddingUris` |

| `EmbeddingRules` | `[]*FeedPostgate_EmbeddingRules_Elem` | `embeddingRules` |

| `Post` | `string` | `post` |



#### FeedPostgate_DisableRule (struct)


*Определено в: `api/bsky/feedpostgate.go:35`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |



#### FeedRepost (struct)


*Определено в: `api/bsky/feedrepost.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `Subject` | `*comatproto.RepoStrongRef` | `subject` |

| `Via` | `*comatproto.RepoStrongRef` | `via` |



#### FeedThreadgate (struct)


*Определено в: `api/bsky/feedthreadgate.go:21`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Allow` | `[]*FeedThreadgate_Allow_Elem` | `allow` |

| `CreatedAt` | `string` | `createdAt` |

| `HiddenReplies` | `[]string` | `hiddenReplies` |

| `Post` | `string` | `post` |



#### FeedThreadgate_FollowerRule (struct)


*Определено в: `api/bsky/feedthreadgate.go:131`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |



#### FeedThreadgate_FollowingRule (struct)


*Определено в: `api/bsky/feedthreadgate.go:138`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |



#### FeedThreadgate_ListRule (struct)


*Определено в: `api/bsky/feedthreadgate.go:145`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `List` | `string` | `list` |



#### FeedThreadgate_MentionRule (struct)


*Определено в: `api/bsky/feedthreadgate.go:153`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |



#### GraphBlock (struct)


*Определено в: `api/bsky/graphblock.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `Subject` | `string` | `subject` |



#### GraphFollow (struct)


*Определено в: `api/bsky/graphfollow.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `Subject` | `string` | `subject` |

| `Via` | `*comatproto.RepoStrongRef` | `via` |



#### GraphList (struct)


*Определено в: `api/bsky/graphlist.go:22`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Avatar` | `*lexutil.LexBlob` | `avatar` |

| `CreatedAt` | `string` | `createdAt` |

| `Description` | `*string` | `description` |

| `DescriptionFacets` | `[]*RichtextFacet` | `descriptionFacets` |

| `Labels` | `*GraphList_Labels` | `labels` |

| `Name` | `string` | `name` |

| `Purpose` | `*string` | `purpose` |



#### GraphListblock (struct)


*Определено в: `api/bsky/graphlistblock.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `Subject` | `string` | `subject` |



#### GraphListitem (struct)


*Определено в: `api/bsky/graphlistitem.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `List` | `string` | `list` |

| `Subject` | `string` | `subject` |



#### GraphMuteActor_Input (struct)


*Определено в: `api/bsky/graphmuteActor.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Actor` | `string` | `actor` |



#### GraphStarterpack (struct)


*Определено в: `api/bsky/graphstarterpack.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `Description` | `*string` | `description` |

| `DescriptionFacets` | `[]*RichtextFacet` | `descriptionFacets` |

| `Feeds` | `[]*GraphStarterpack_FeedItem` | `feeds` |

| `List` | `string` | `list` |

| `Name` | `string` | `name` |



#### GraphStarterpack_FeedItem (struct)


*Определено в: `api/bsky/graphstarterpack.go:28`*


| Поле | Тип | JSON |

|------|-----|------|

| `Uri` | `string` | `uri` |



#### GraphVerification (struct)


*Определено в: `api/bsky/graphverification.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `DisplayName` | `string` | `displayName` |

| `Handle` | `string` | `handle` |

| `Subject` | `string` | `subject` |



#### LabelerDefs_LabelerPolicies (struct)


*Определено в: `api/bsky/labelerdefs.go:12`*


| Поле | Тип | JSON |

|------|-----|------|

| `LabelValueDefinitions` | `[]*comatproto.LabelDefs_LabelValueDefinition` | `labelValueDefinitions` |

| `LabelValues` | `[]*string` | `labelValues` |



#### LabelerService (struct)


*Определено в: `api/bsky/labelerservice.go:22`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `CreatedAt` | `string` | `createdAt` |

| `Labels` | `*LabelerService_Labels` | `labels` |

| `Policies` | `*LabelerDefs_LabelerPolicies` | `policies` |

| `ReasonTypes` | `[]*string` | `reasonTypes` |

| `SubjectCollections` | `[]string` | `subjectCollections` |

| `SubjectTypes` | `[]*string` | `subjectTypes` |



#### NotificationDeclaration (struct)


*Определено в: `api/bsky/notificationdeclaration.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `AllowSubscriptions` | `string` | `allowSubscriptions` |



#### RichtextFacet (struct)


*Определено в: `api/bsky/richtextfacet.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `Features` | `[]*RichtextFacet_Features_Elem` | `features` |

| `Index` | `*RichtextFacet_ByteSlice` | `index` |



#### RichtextFacet_ByteSlice (struct)


*Определено в: `api/bsky/richtextfacet.go:28`*


| Поле | Тип | JSON |

|------|-----|------|

| `ByteEnd` | `int64` | `byteEnd` |

| `ByteStart` | `int64` | `byteStart` |



#### RichtextFacet_Link (struct)


*Определено в: `api/bsky/richtextfacet.go:118`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Uri` | `string` | `uri` |



#### RichtextFacet_Mention (struct)


*Определено в: `api/bsky/richtextfacet.go:126`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Did` | `string` | `did` |



#### RichtextFacet_Tag (struct)


*Определено в: `api/bsky/richtextfacet.go:134`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Tag` | `string` | `tag` |



#### UnspeccedDefs_SkeletonSearchActor (struct)


*Определено в: `api/bsky/unspecceddefs.go:40`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `did` |



#### UnspeccedDefs_SkeletonSearchPost (struct)


*Определено в: `api/bsky/unspecceddefs.go:45`*


| Поле | Тип | JSON |

|------|-----|------|

| `Uri` | `string` | `uri` |



#### UnspeccedSearchActorsSkeleton_Output (struct)


*Определено в: `api/bsky/unspeccedsearchActorsSkeleton.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Actors` | `[]*UnspeccedDefs_SkeletonSearchActor` | `actors` |

| `Cursor` | `*string` | `cursor` |

| `HitsTotal` | `*int64` | `hitsTotal` |



#### UnspeccedSearchPostsSkeleton_Output (struct)


*Определено в: `api/bsky/unspeccedsearchPostsSkeleton.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cursor` | `*string` | `cursor` |

| `HitsTotal` | `*int64` | `hitsTotal` |

| `Posts` | `[]*UnspeccedDefs_SkeletonSearchPost` | `posts` |




---


[import] path: github.com/bluesky-social/indigo/api/chat type: local


### github.com/bluesky-social/indigo/api/chat


- **Тип:** local

- **Алиасы:** `chat`, `chatbsky`

- **Локальная директория пакета:** `api/chat`



### Кандидаты на типы


`ActorDeclaration`, `ConvoDefs_MessageRef`


### Селекторы (любое использование `pkg.X`)


`ActorDeclaration`, `ConvoDefs_MessageRef`


### Используется в файлах


- 📄 `api/ozone/moderationdefs.go`

- 📄 `gen/main.go`



### Определения локальных типов (best effort)


#### ActorDeclaration (struct)


*Определено в: `api/chat/actordeclaration.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `AllowIncoming` | `string` | `allowIncoming` |



#### ConvoDefs_MessageRef (struct)


*Определено в: `api/chat/convodefs.go:393`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `ConvoId` | `string` | `convoId` |

| `Did` | `string` | `did` |

| `MessageId` | `string` | `messageId` |




---


[import] path: github.com/bluesky-social/indigo/api/ozone type: local


### github.com/bluesky-social/indigo/api/ozone


- **Тип:** local

- **Алиасы:** `toolsozone`

- **Локальная директория пакета:** `api/ozone`



### Вызовы


`ModerationEmitEvent`, `ModerationGetRecord`, `ModerationGetRepo`, `ModerationQueryEvents`


### Кандидаты на типы


`ModerationDefs_ModEventAcknowledge`, `ModerationDefs_ModEventEscalate`, `ModerationDefs_ModEventLabel`, `ModerationDefs_ModEventReport`, `ModerationDefs_ModEventTag`, `ModerationDefs_ModEventTakedown`, `ModerationDefs_ModEventView`, `ModerationDefs_RepoViewDetail`, `ModerationEmitEvent_Input`, `ModerationEmitEvent_Input_Event`, `ModerationEmitEvent_Input_Subject`


### Селекторы (любое использование `pkg.X`)


`ModerationDefs_ModEventAcknowledge`, `ModerationDefs_ModEventEscalate`, `ModerationDefs_ModEventLabel`, `ModerationDefs_ModEventReport`, `ModerationDefs_ModEventTag`, `ModerationDefs_ModEventTakedown`, `ModerationDefs_ModEventView`, `ModerationDefs_ModEventView_Event`, `ModerationDefs_RepoViewDetail`, `ModerationEmitEvent`, `ModerationEmitEvent_Input`, `ModerationEmitEvent_Input_Event`, `ModerationEmitEvent_Input_Subject`, `ModerationGetRecord`, `ModerationGetRepo`, `ModerationQueryEvents`


### Используется в файлах


- 📄 `automod/consumer/ozone.go`

- 📄 `automod/engine/context.go`

- 📄 `automod/engine/engine_ozone.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/persist.go`

- 📄 `automod/engine/persisthelpers.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/gosky/admin.go`



### Определения локальных типов (best effort)


#### ModerationDefs_ModEventAcknowledge (struct)


*Определено в: `api/ozone/moderationdefs.go:180`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `AcknowledgeAccountSubjects` | `*bool` | `acknowledgeAccountSubjects` |

| `Comment` | `*string` | `comment` |



#### ModerationDefs_ModEventEscalate (struct)


*Определено в: `api/ozone/moderationdefs.go:229`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Comment` | `*string` | `comment` |



#### ModerationDefs_ModEventLabel (struct)


*Определено в: `api/ozone/moderationdefs.go:237`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Comment` | `*string` | `comment` |

| `CreateLabelVals` | `[]string` | `createLabelVals` |

| `DurationInHours` | `*int64` | `durationInHours` |

| `NegateLabelVals` | `[]string` | `negateLabelVals` |



#### ModerationDefs_ModEventReport (struct)


*Определено в: `api/ozone/moderationdefs.go:278`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Comment` | `*string` | `comment` |

| `IsReporterMuted` | `*bool` | `isReporterMuted` |

| `ReportType` | `*string` | `reportType` |



#### ModerationDefs_ModEventTag (struct)


*Определено в: `api/ozone/moderationdefs.go:313`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Add` | `[]string` | `add` |

| `Comment` | `*string` | `comment` |

| `Remove` | `[]string` | `remove` |



#### ModerationDefs_ModEventTakedown (struct)


*Определено в: `api/ozone/moderationdefs.go:326`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `AcknowledgeAccountSubjects` | `*bool` | `acknowledgeAccountSubjects` |

| `Comment` | `*string` | `comment` |

| `DurationInHours` | `*int64` | `durationInHours` |

| `Policies` | `[]string` | `policies` |

| `SeverityLevel` | `*string` | `severityLevel` |

| `StrikeCount` | `*int64` | `strikeCount` |

| `StrikeExpiresAt` | `*string` | `strikeExpiresAt` |

| `TargetServices` | `[]string` | `targetServices` |



#### ModerationDefs_ModEventView (struct)


*Определено в: `api/ozone/moderationdefs.go:364`*


| Поле | Тип | JSON |

|------|-----|------|

| `CreatedAt` | `string` | `createdAt` |

| `CreatedBy` | `string` | `createdBy` |

| `CreatorHandle` | `*string` | `creatorHandle` |

| `Event` | `*ModerationDefs_ModEventView_Event` | `event` |

| `Id` | `int64` | `id` |

| `ModTool` | `*ModerationDefs_ModTool` | `modTool` |

| `Subject` | `*ModerationDefs_ModEventView_Subject` | `subject` |

| `SubjectBlobCids` | `[]string` | `subjectBlobCids` |

| `SubjectHandle` | `*string` | `subjectHandle` |



#### ModerationDefs_RepoViewDetail (struct)


*Определено в: `api/ozone/moderationdefs.go:1013`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `DeactivatedAt` | `*string` | `deactivatedAt` |

| `Did` | `string` | `did` |

| `Email` | `*string` | `email` |

| `EmailConfirmedAt` | `*string` | `emailConfirmedAt` |

| `Handle` | `string` | `handle` |

| `IndexedAt` | `string` | `indexedAt` |

| `InviteNote` | `*string` | `inviteNote` |

| `InvitedBy` | `*comatproto.ServerDefs_InviteCode` | `invitedBy` |

| `Invites` | `[]*comatproto.ServerDefs_InviteCode` | `invites` |

| `InvitesDisabled` | `*bool` | `invitesDisabled` |

| `Labels` | `[]*comatproto.LabelDefs_Label` | `labels` |

| `Moderation` | `*ModerationDefs_ModerationDetail` | `moderation` |

| `RelatedRecords` | `[]*lexutil.LexiconTypeDecoder` | `relatedRecords` |

| `ThreatSignatures` | `[]*comatproto.AdminDefs_ThreatSignature` | `threatSignatures` |



#### ModerationEmitEvent_Input (struct)


*Определено в: `api/ozone/moderationemitEvent.go:17`*


| Поле | Тип | JSON |

|------|-----|------|

| `CreatedBy` | `string` | `createdBy` |

| `Event` | `*ModerationEmitEvent_Input_Event` | `event` |

| `ExternalId` | `*string` | `externalId` |

| `ModTool` | `*ModerationDefs_ModTool` | `modTool` |

| `Subject` | `*ModerationEmitEvent_Input_Subject` | `subject` |

| `SubjectBlobCids` | `[]string` | `subjectBlobCids` |



#### ModerationEmitEvent_Input_Event (struct)


*Определено в: `api/ozone/moderationemitEvent.go:27`*


| Поле | Тип | JSON |

|------|-----|------|

| `ModerationDefs_ModEventTakedown` | `*ModerationDefs_ModEventTakedown` | `ModerationDefsModeventtakedown` |

| `ModerationDefs_ModEventAcknowledge` | `*ModerationDefs_ModEventAcknowledge` | `ModerationDefsModeventacknowledge` |

| `ModerationDefs_ModEventEscalate` | `*ModerationDefs_ModEventEscalate` | `ModerationDefsModeventescalate` |

| `ModerationDefs_ModEventComment` | `*ModerationDefs_ModEventComment` | `ModerationDefsModeventcomment` |

| `ModerationDefs_ModEventLabel` | `*ModerationDefs_ModEventLabel` | `ModerationDefsModeventlabel` |

| `ModerationDefs_ModEventReport` | `*ModerationDefs_ModEventReport` | `ModerationDefsModeventreport` |

| `ModerationDefs_ModEventMute` | `*ModerationDefs_ModEventMute` | `ModerationDefsModeventmute` |

| `ModerationDefs_ModEventUnmute` | `*ModerationDefs_ModEventUnmute` | `ModerationDefsModeventunmute` |

| `ModerationDefs_ModEventMuteReporter` | `*ModerationDefs_ModEventMuteReporter` | `ModerationDefsModeventmutereporter` |

| `ModerationDefs_ModEventUnmuteReporter` | `*ModerationDefs_ModEventUnmuteReporter` | `ModerationDefsModeventunmutereporter` |

| `ModerationDefs_ModEventReverseTakedown` | `*ModerationDefs_ModEventReverseTakedown` | `ModerationDefsModeventreversetakedown` |

| `ModerationDefs_ModEventResolveAppeal` | `*ModerationDefs_ModEventResolveAppeal` | `ModerationDefsModeventresolveappeal` |

| `ModerationDefs_ModEventEmail` | `*ModerationDefs_ModEventEmail` | `ModerationDefsModeventemail` |

| `ModerationDefs_ModEventDivert` | `*ModerationDefs_ModEventDivert` | `ModerationDefsModeventdivert` |

| `ModerationDefs_ModEventTag` | `*ModerationDefs_ModEventTag` | `ModerationDefsModeventtag` |

| `ModerationDefs_AccountEvent` | `*ModerationDefs_AccountEvent` | `ModerationDefsAccountevent` |

| `ModerationDefs_IdentityEvent` | `*ModerationDefs_IdentityEvent` | `ModerationDefsIdentityevent` |

| `ModerationDefs_RecordEvent` | `*ModerationDefs_RecordEvent` | `ModerationDefsRecordevent` |

| `ModerationDefs_ModEventPriorityScore` | `*ModerationDefs_ModEventPriorityScore` | `ModerationDefsModeventpriorityscore` |

| `ModerationDefs_AgeAssuranceEvent` | `*ModerationDefs_AgeAssuranceEvent` | `ModerationDefsAgeassuranceevent` |

| `ModerationDefs_AgeAssuranceOverrideEvent` | `*ModerationDefs_AgeAssuranceOverrideEvent` | `ModerationDefsAgeassuranceoverrideevent` |

| `ModerationDefs_RevokeAccountCredentialsEvent` | `*ModerationDefs_RevokeAccountCredentialsEvent` | `ModerationDefsRevokeaccountcredentialsevent` |

| `ModerationDefs_ScheduleTakedownEvent` | `*ModerationDefs_ScheduleTakedownEvent` | `ModerationDefsScheduletakedownevent` |

| `ModerationDefs_CancelScheduledTakedownEvent` | `*ModerationDefs_CancelScheduledTakedownEvent` | `ModerationDefsCancelscheduledtakedownevent` |



#### ModerationEmitEvent_Input_Subject (struct)


*Определено в: `api/ozone/moderationemitEvent.go:238`*


| Поле | Тип | JSON |

|------|-----|------|

| `AdminDefs_RepoRef` | `*comatproto.AdminDefs_RepoRef` | `AdminDefsReporef` |

| `RepoStrongRef` | `*comatproto.RepoStrongRef` | `RepoStrongRef` |




---


[import] path: github.com/bluesky-social/indigo/atproto/atclient type: local


### github.com/bluesky-social/indigo/atproto/atclient


- **Тип:** local

- **Алиасы:** `atclient`

- **Локальная директория пакета:** `atproto/atclient`



### Вызовы


`LoginWithPassword`, `NewAPIClient`, `NewAdminClient`


### Кандидаты на типы


`APIClient`, `APIError`, `ErrorBody`


### Селекторы (любое использование `pkg.X`)


`APIClient`, `APIError`, `AuthMethod`, `ErrorBody`, `LoginWithPassword`, `NewAPIClient`, `NewAdminClient`


### Используется в файлах


- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/lexicon/resolve.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/util.go`



### Определения локальных типов (best effort)


#### APIClient (struct)


*Определено в: `atproto/atclient/apiclient.go:21`*


| Поле | Тип | JSON |

|------|-----|------|

| `Client` | `*http.Client` | `Client` |

| `Host` | `string` | `Host` |

| `Auth` | `AuthMethod` | `Auth` |

| `Headers` | `unknown` | `Headers` |

| `AccountDID` | `*syntax.DID` | `AccountDID` |



#### APIError (struct)


*Определено в: `atproto/atclient/apierror.go:7`*


| Поле | Тип | JSON |

|------|-----|------|

| `StatusCode` | `int` | `StatusCode` |

| `Name` | `string` | `Name` |

| `Message` | `string` | `Message` |



#### ErrorBody (struct)


*Определено в: `atproto/atclient/apierror.go:25`*


| Поле | Тип | JSON |

|------|-----|------|

| `Name` | `string` | `Name` |

| `Message` | `string` | `Message` |




---


[import] path: github.com/bluesky-social/indigo/atproto/atcrypto type: local


### github.com/bluesky-social/indigo/atproto/atcrypto


- **Тип:** local

- **Алиасы:** `atcrypto`

- **Локальная директория пакета:** `atproto/atcrypto`



### Вызовы


`GeneratePrivateKeyK256`, `GeneratePrivateKeyP256`, `ParsePrivateBytesP256`, `ParsePrivateMultibase`, `ParsePublicMultibase`, `ParsePublicUncompressedBytesK256`, `ParsePublicUncompressedBytesP256`


### Кандидаты на типы


`JWK`, `PrivateKeyK256`, `PrivateKeyP256`


### Селекторы (любое использование `pkg.X`)


`GeneratePrivateKeyK256`, `GeneratePrivateKeyP256`, `JWK`, `ParsePrivateBytesP256`, `ParsePrivateMultibase`, `ParsePublicMultibase`, `ParsePublicUncompressedBytesK256`, `ParsePublicUncompressedBytesP256`, `PrivateKey`, `PrivateKeyK256`, `PrivateKeyP256`, `PublicKey`


### Используется в файлах


- 📄 `atproto/atcrypto/cmd/atp-crypto/main.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/jwt_signing.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/jwt_signing.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/auth/oauth/types.go`

- 📄 `atproto/identity/identity.go`

- 📄 `atproto/labeling/label.go`

- 📄 `atproto/repo/commit.go`

- 📄 `util/cliutil/key.go`



### Определения локальных типов (best effort)


#### JWK (struct)


*Определено в: `atproto/atcrypto/jwk.go:18`*


| Поле | Тип | JSON |

|------|-----|------|

| `KeyType` | `string` | `KeyType` |

| `Curve` | `string` | `Curve` |

| `X` | `string` | `X` |

| `Y` | `string` | `Y` |

| `Use` | `string` | `Use` |

| `KeyID` | `*string` | `KeyID` |



#### PrivateKeyK256 (struct)


*Определено в: `atproto/atcrypto/k256.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `privK256` | `*secp256k1secec.PrivateKey` | `privK256` |



#### PrivateKeyP256 (struct)


*Определено в: `atproto/atcrypto/p256.go:18`*


| Поле | Тип | JSON |

|------|-----|------|

| `privP256ecdh` | `*ecdh.PrivateKey` | `privP256ecdh` |

| `privP256` | `unknown` | `privP256` |




---


[import] path: github.com/bluesky-social/indigo/atproto/atdata type: local


### github.com/bluesky-social/indigo/atproto/atdata


- **Тип:** local

- **Алиасы:** `atdata`

- **Локальная директория пакета:** `atproto/atdata`



### Вызовы


`Bytes`, `CIDLink`, `ExtractBlobs`, `UnmarshalCBOR`, `UnmarshalJSON`


### Кандидаты на типы


`BlobSchema`, `CIDLink`, `GenericRecord`, `LegacyBlobSchema`


### Селекторы (любое использование `pkg.X`)


`Blob`, `BlobSchema`, `Bytes`, `CIDLink`, `ExtractBlobs`, `GenericRecord`, `LegacyBlobSchema`, `UnmarshalCBOR`, `UnmarshalJSON`


### Используется в файлах


- 📄 `atproto/labeling/label.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/lexicon/language.go`

- 📄 `atproto/lexicon/resolve.go`

- 📄 `atproto/repo/commit.go`

- 📄 `automod/engine/blobs.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `gen/main.go`



### Определения локальных типов (best effort)


#### BlobSchema (struct)


*Определено в: `atproto/atdata/blob.go:29`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Ref` | `CIDLink` | `ref` |

| `MimeType` | `string` | `mimeType` |

| `Size` | `int64` | `size` |



#### CIDLink (type)


*Определено в: `atproto/atdata/cidlink.go:15`*


```go

cid.Cid

```


#### GenericRecord (struct)


*Определено в: `atproto/atdata/extract.go:11`*


| Поле | Тип | JSON |

|------|-----|------|

| `Type` | `string` | `$type` |



#### LegacyBlobSchema (struct)


*Определено в: `atproto/atdata/blob.go:24`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cid` | `string` | `cid` |

| `MimeType` | `string` | `mimeType` |




---


[import] path: github.com/bluesky-social/indigo/atproto/auth type: local


### github.com/bluesky-social/indigo/atproto/auth


- **Тип:** local

- **Алиасы:** `auth`

- **Локальная директория пакета:** `atproto/auth`



### Вызовы


`AdminAuthMiddleware`


### Селекторы (любое использование `pkg.X`)


`AdminAuthMiddleware`


### Используется в файлах


- 📄 `cmd/tap/server.go`




---


[import] path: github.com/bluesky-social/indigo/atproto/auth/oauth type: local


### github.com/bluesky-social/indigo/atproto/auth/oauth


- **Тип:** local

- **Алиасы:** `oauth`

- **Локальная директория пакета:** `atproto/auth/oauth`



### Вызовы


`NewClientApp`, `NewLocalhostConfig`, `NewMemStore`, `NewPublicConfig`


### Кандидаты на типы


`ClientApp`


### Селекторы (любое использование `pkg.X`)


`ClientApp`, `ClientConfig`, `NewClientApp`, `NewLocalhostConfig`, `NewMemStore`, `NewPublicConfig`


### Используется в файлах


- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`



### Определения локальных типов (best effort)


#### ClientApp (struct)


*Определено в: `atproto/auth/oauth/oauth.go:25`*


| Поле | Тип | JSON |

|------|-----|------|

| `Client` | `*http.Client` | `Client` |

| `Resolver` | `*Resolver` | `Resolver` |

| `Dir` | `unknown` | `Dir` |

| `Config` | `*ClientConfig` | `Config` |

| `Store` | `ClientAuthStore` | `Store` |




---


[import] path: github.com/bluesky-social/indigo/atproto/identity type: local


### github.com/bluesky-social/indigo/atproto/identity


- **Тип:** local

- **Алиасы:** `identity`

- **Локальная директория пакета:** `atproto/identity`



### Вызовы


`DefaultDirectory`, `NewCacheDirectory`, `NewMockDirectory`, `ParseIdentity`


### Кандидаты на типы


`BaseDirectory`, `CacheDirectory`, `DIDDocument`, `Directory`, `ErrDIDNotFound`, `ErrHandleNotFound`, `Identity`


### Селекторы (любое использование `pkg.X`)


`BaseDirectory`, `CacheDirectory`, `DIDDocument`, `DefaultDirectory`, `Directory`, `ErrDIDNotFound`, `ErrDIDResolutionFailed`, `ErrHandleMismatch`, `ErrHandleNotFound`, `ErrHandleResolutionFailed`, `ErrInvalidHandle`, `Identity`, `NewCacheDirectory`, `NewMockDirectory`, `ParseIdentity`, `Resolver`, `refreshIdentity`, `resolveDid`, `resolveHandle`, `resolveIdentity`


### Используется в файлах


- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/cmd/atp-id/main.go`

- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/lexicon/resolve.go`

- 📄 `atproto/lexicon/resolving_catalog.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/repo/sync.go`

- 📄 `automod/capture/fetch.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/engine/account_meta.go`

- 📄 `automod/engine/context.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/testing.go`

- 📄 `backfill/backfill.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/bluepages/handlers.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/bluepages/server.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/did.go`

- 📄 `cmd/gosky/handle.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/relay/testing/scenario.go`

- 📄 `cmd/tap/repo_manager.go`

- 📄 `cmd/tap/server.go`

- 📄 `cmd/tap/tap.go`

- 📄 `search/bulk.go`

- 📄 `search/indexing.go`

- 📄 `search/parse_query.go`

- 📄 `search/query.go`

- 📄 `search/server.go`

- 📄 `search/transform.go`



### Определения локальных типов (best effort)


#### BaseDirectory (struct)


*Определено в: `atproto/identity/base_directory.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `PLCURL` | `string` | `PLCURL` |

| `PLCLimiter` | `*rate.Limiter` | `PLCLimiter` |

| `DIDWebLimitFunc` | `unknown` | `DIDWebLimitFunc` |

| `HTTPClient` | `unknown` | `HTTPClient` |

| `Resolver` | `unknown` | `Resolver` |

| `TryAuthoritativeDNS` | `bool` | `TryAuthoritativeDNS` |

| `SkipDNSDomainSuffixes` | `[]string` | `SkipDNSDomainSuffixes` |

| `FallbackDNSServers` | `[]string` | `FallbackDNSServers` |

| `SkipHandleVerification` | `bool` | `SkipHandleVerification` |

| `UserAgent` | `string` | `UserAgent` |



#### CacheDirectory (struct)


*Определено в: `atproto/identity/cache_directory.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `Inner` | `Directory` | `Inner` |

| `ErrTTL` | `unknown` | `ErrTTL` |

| `InvalidHandleTTL` | `unknown` | `InvalidHandleTTL` |

| `handleCache` | `*expirable.LRU[syntax.Handle, handleEntry]` | `handleCache` |

| `identityCache` | `*expirable.LRU[syntax.DID, identityEntry]` | `identityCache` |

| `didLookupChans` | `unknown` | `didLookupChans` |

| `handleLookupChans` | `unknown` | `handleLookupChans` |



#### DIDDocument (struct)


*Определено в: `atproto/identity/diddoc.go:7`*


| Поле | Тип | JSON |

|------|-----|------|

| `DID` | `unknown` | `DID` |

| `AlsoKnownAs` | `[]string` | `AlsoKnownAs` |

| `VerificationMethod` | `[]DocVerificationMethod` | `VerificationMethod` |

| `Service` | `[]DocService` | `Service` |



#### Directory (interface)


*Определено в: `atproto/identity/directory.go:26`*


```go

interface {
	LookupHandle(ctx context.Context, handle syntax.Handle) (*Identity, error)
	LookupDID(ctx context.Context, did syntax.DID) (*Identity, error)
	Lookup(ctx context.Context, atid syntax.AtIdentifier) (*Identity, error)

	// Flushes any cache of the indicated identifier. If directory is not using caching, can ignore this.
	Purge(ctx context.Context, atid syntax.AtIdentifier) error
}

```


#### Identity (struct)


*Определено в: `atproto/identity/identity.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `DID` | `unknown` | `DID` |

| `Handle` | `unknown` | `Handle` |

| `AlsoKnownAs` | `[]string` | `AlsoKnownAs` |

| `Services` | `map[string]ServiceEndpoint` | `Services` |

| `Keys` | `map[string]VerificationMethod` | `Keys` |




---


[import] path: github.com/bluesky-social/indigo/atproto/identity/apidir type: local


### github.com/bluesky-social/indigo/atproto/identity/apidir


- **Тип:** local

- **Алиасы:** `apidir`

- **Локальная директория пакета:** `atproto/identity/apidir`



### Вызовы


`NewAPIDirectory`


### Селекторы (любое использование `pkg.X`)


`NewAPIDirectory`


### Используется в файлах


- 📄 `cmd/bluepages/main.go`




---


[import] path: github.com/bluesky-social/indigo/atproto/identity/redisdir type: local


### github.com/bluesky-social/indigo/atproto/identity/redisdir


- **Тип:** local

- **Алиасы:** `redisdir`

- **Локальная директория пакета:** `atproto/identity/redisdir`



### Вызовы


`NewRedisDirectory`


### Селекторы (любое использование `pkg.X`)


`NewRedisDirectory`


### Используется в файлах


- 📄 `cmd/hepa/main.go`




---


[import] path: github.com/bluesky-social/indigo/atproto/labeling type: local


### github.com/bluesky-social/indigo/atproto/labeling


- **Тип:** local

- **Алиасы:** `labeling`

- **Локальная директория пакета:** `atproto/labeling`



### Кандидаты на типы


`Label`


### Селекторы (любое использование `pkg.X`)


`Label`


### Используется в файлах


- 📄 `gen/main.go`



### Определения локальных типов (best effort)


#### Label (struct)


*Определено в: `atproto/labeling/label.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `CID` | `*string` | `cid` |

| `CreatedAt` | `string` | `cts` |

| `ExpiresAt` | `*string` | `exp` |

| `Negated` | `*bool` | `neg` |

| `SourceDID` | `string` | `src` |

| `URI` | `string` | `uri` |

| `Val` | `string` | `val` |

| `Version` | `int64` | `ver` |

| `Sig` | `unknown` | `sig` |




---


[import] path: github.com/bluesky-social/indigo/atproto/lexicon type: local


### github.com/bluesky-social/indigo/atproto/lexicon


- **Тип:** local

- **Алиасы:** `lexicon`

- **Локальная директория пакета:** `atproto/lexicon`



### Вызовы


`NewBaseCatalog`, `NewResolvingCatalog`, `SchemaSubscription`, `ValidateRecord`


### Кандидаты на типы


`SchemaBody`, `SchemaDef`, `SchemaFile`, `SchemaObject`, `SchemaParams`, `SchemaUnion`


### Селекторы (любое использование `pkg.X`)


`Catalog`, `LenientMode`, `NewBaseCatalog`, `NewResolvingCatalog`, `SchemaArray`, `SchemaBlob`, `SchemaBody`, `SchemaBoolean`, `SchemaBytes`, `SchemaCIDLink`, `SchemaDef`, `SchemaFile`, `SchemaInteger`, `SchemaObject`, `SchemaParams`, `SchemaPermission`, `SchemaPermissionSet`, `SchemaProcedure`, `SchemaQuery`, `SchemaRecord`, `SchemaRef`, `SchemaString`, `SchemaSubscription`, `SchemaToken`, `SchemaUnion`, `SchemaUnknown`, `ValidateRecord`


### Используется в файлах


- 📄 `atproto/lexicon/cmd/lextool/main.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `lex/lexgen/codegen.go`

- 📄 `lex/lexgen/flatten.go`

- 📄 `lex/lexgen/util.go`

- 📄 `lex/lexlint/breaking.go`

- 📄 `lex/lexlint/lint.go`



### Определения локальных типов (best effort)


#### SchemaBody (struct)


*Определено в: `atproto/lexicon/language.go:547`*


| Поле | Тип | JSON |

|------|-----|------|

| `Description` | `*string` | `Description` |

| `Encoding` | `string` | `Encoding` |

| `Schema` | `*SchemaDef` | `Schema` |



#### SchemaDef (struct)


*Определено в: `atproto/lexicon/language.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `Inner` | `any` | `Inner` |



#### SchemaFile (struct)


*Определено в: `atproto/lexicon/schemafile.go:13`*


| Поле | Тип | JSON |

|------|-----|------|

| `Type` | `string` | `Type` |

| `Lexicon` | `int` | `Lexicon` |

| `ID` | `string` | `ID` |

| `Description` | `*string` | `Description` |

| `Defs` | `map[string]SchemaDef` | `Defs` |



#### SchemaObject (struct)


*Определено в: `atproto/lexicon/language.go:889`*


| Поле | Тип | JSON |

|------|-----|------|

| `Type` | `string` | `Type` |

| `Description` | `*string` | `Description` |

| `Properties` | `map[string]SchemaDef` | `Properties` |

| `Required` | `[]string` | `Required` |

| `Nullable` | `[]string` | `Nullable` |



#### SchemaParams (struct)


*Определено в: `atproto/lexicon/language.go:982`*


| Поле | Тип | JSON |

|------|-----|------|

| `Type` | `string` | `Type` |

| `Description` | `*string` | `Description` |

| `Properties` | `map[string]SchemaDef` | `Properties` |

| `Required` | `[]string` | `Required` |



#### SchemaUnion (struct)


*Определено в: `atproto/lexicon/language.go:1067`*


| Поле | Тип | JSON |

|------|-----|------|

| `Type` | `string` | `Type` |

| `Description` | `*string` | `Description` |

| `Refs` | `[]string` | `Refs` |

| `Closed` | `*bool` | `Closed` |

| `fullRefs` | `[]string` | `fullRefs` |




---


[import] path: github.com/bluesky-social/indigo/atproto/repo type: local


### github.com/bluesky-social/indigo/atproto/repo


- **Тип:** local

- **Алиасы:** `atrepo`, `repo`, `repolib`

- **Локальная директория пакета:** `atproto/repo`



### Вызовы


`LoadCommitFromCAR`, `LoadRepoFromCAR`, `NewTinyBlockstore`, `VerifyCommitMessage`, `VerifyCommitSignature`, `VerifySyncMessage`


### Кандидаты на типы


`Commit`


### Селекторы (любое использование `pkg.X`)


`Commit`, `LoadCommitFromCAR`, `LoadRepoFromCAR`, `MST`, `NewTinyBlockstore`, `VerifyCommitMessage`, `VerifyCommitSignature`, `VerifySyncMessage`


### Используется в файлах


- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `gen/main.go`

- 📄 `repo/repo.go`



### Определения локальных типов (best effort)


#### Commit (struct)


*Определено в: `atproto/repo/commit.go:15`*


| Поле | Тип | JSON |

|------|-----|------|

| `DID` | `string` | `did` |

| `Version` | `int64` | `version` |

| `Prev` | `*cid.Cid` | `prev` |

| `Data` | `unknown` | `data` |

| `Sig` | `[]byte` | `sig` |

| `Rev` | `string` | `rev` |




---


[import] path: github.com/bluesky-social/indigo/atproto/repo/mst type: local


### github.com/bluesky-social/indigo/atproto/repo/mst


- **Тип:** local

- **Алиасы:** `atmst`, `mst`

- **Локальная директория пакета:** `atproto/repo/mst`



### Вызовы


`LoadTreeFromStore`, `NewEmptyTree`


### Кандидаты на типы


`EntryData`, `NodeData`, `Tree`


### Селекторы (любое использование `pkg.X`)


`EntryData`, `LoadTreeFromStore`, `NewEmptyTree`, `NodeData`, `Tree`


### Используется в файлах


- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/operation.go`

- 📄 `atproto/repo/repo.go`

- 📄 `gen/main.go`



### Определения локальных типов (best effort)


#### EntryData (struct)


*Определено в: `atproto/repo/mst/encoding.go:23`*


| Поле | Тип | JSON |

|------|-----|------|

| `PrefixLen` | `int64` | `PrefixLen` |

| `KeySuffix` | `[]byte` | `KeySuffix` |

| `Value` | `unknown` | `Value` |

| `Right` | `*cid.Cid` | `Right` |



#### NodeData (struct)


*Определено в: `atproto/repo/mst/encoding.go:17`*


| Поле | Тип | JSON |

|------|-----|------|

| `Left` | `*cid.Cid` | `Left` |

| `Entries` | `[]EntryData` | `Entries` |



#### Tree (struct)


*Определено в: `atproto/repo/mst/tree.go:18`*


| Поле | Тип | JSON |

|------|-----|------|

| `Root` | `*Node` | `Root` |




---


[import] path: github.com/bluesky-social/indigo/atproto/syntax type: local


### github.com/bluesky-social/indigo/atproto/syntax


- **Тип:** local

- **Алиасы:** `syntax`

- **Локальная директория пакета:** `atproto/syntax`



### Вызовы


`ATURI`, `CID`, `ClockFromTID`, `DID`, `Datetime`, `DatetimeNow`, `Handle`, `NSID`, `NewTIDClock`, `ParseATURI`, `ParseAtIdentifier`, `ParseCID`, `ParseDID`, `ParseDatetime`, `ParseDatetimeLenient`, `ParseDatetimeTime`, `ParseHandle`, `ParseLanguage`, `ParseNSID`, `ParseRecordKey`, `ParseRepoPath`, `ParseTID`, `ParseURI`, `TID`


### Кандидаты на типы


`ATURI`, `AtIdentifier`, `CID`, `DID`, `Datetime`, `Language`, `NSID`, `TIDClock`, `URI`


### Селекторы (любое использование `pkg.X`)


`ATURI`, `AtIdentifier`, `AtprotoDatetimeLayout`, `CID`, `ClockFromTID`, `DID`, `Datetime`, `DatetimeNow`, `Handle`, `HandleInvalid`, `Language`, `NSID`, `NewTIDClock`, `ParseATURI`, `ParseAtIdentifier`, `ParseCID`, `ParseDID`, `ParseDatetime`, `ParseDatetimeLenient`, `ParseDatetimeTime`, `ParseHandle`, `ParseLanguage`, `ParseNSID`, `ParseRecordKey`, `ParseRepoPath`, `ParseTID`, `ParseURI`, `RecordKey`, `TID`, `TIDClock`, `URI`


### Используется в файлах


- 📄 `atproto/atclient/admin_auth.go`

- 📄 `atproto/atclient/apiclient.go`

- 📄 `atproto/atclient/apirequest.go`

- 📄 `atproto/atclient/cmd/atp-client-demo/main.go`

- 📄 `atproto/atclient/lexclient.go`

- 📄 `atproto/atclient/password_auth.go`

- 📄 `atproto/atdata/data.go`

- 📄 `atproto/auth/http.go`

- 📄 `atproto/auth/jwt.go`

- 📄 `atproto/auth/oauth/cmd/oauth-web-demo/main.go`

- 📄 `atproto/auth/oauth/memstore.go`

- 📄 `atproto/auth/oauth/oauth.go`

- 📄 `atproto/auth/oauth/session.go`

- 📄 `atproto/auth/oauth/store.go`

- 📄 `atproto/auth/oauth/types.go`

- 📄 `atproto/auth/permission.go`

- 📄 `atproto/auth/permission_util.go`

- 📄 `atproto/identity/apidir/apidir.go`

- 📄 `atproto/identity/base_directory.go`

- 📄 `atproto/identity/cache_directory.go`

- 📄 `atproto/identity/cmd/atp-id/main.go`

- 📄 `atproto/identity/did.go`

- 📄 `atproto/identity/diddoc.go`

- 📄 `atproto/identity/directory.go`

- 📄 `atproto/identity/handle.go`

- 📄 `atproto/identity/identity.go`

- 📄 `atproto/identity/mock_directory.go`

- 📄 `atproto/identity/nsid.go`

- 📄 `atproto/identity/redisdir/redis_directory.go`

- 📄 `atproto/identity/resolver.go`

- 📄 `atproto/labeling/label.go`

- 📄 `atproto/lexicon/cmd/lextool/net.go`

- 📄 `atproto/lexicon/language.go`

- 📄 `atproto/lexicon/resolve.go`

- 📄 `atproto/lexicon/resolving_catalog.go`

- 📄 `atproto/lexicon/schemafile.go`

- 📄 `atproto/repo/car.go`

- 📄 `atproto/repo/cmd/repo-tool/main.go`

- 📄 `atproto/repo/commit.go`

- 📄 `atproto/repo/repo.go`

- 📄 `atproto/repo/sync.go`

- 📄 `atproto/syntax/cmd/atp-syntax/main.go`

- 📄 `automod/capture/capture.go`

- 📄 `automod/capture/fetch.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `automod/engine/context.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/engine_ozone.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/fetch_relationship.go`

- 📄 `automod/engine/persisthelpers.go`

- 📄 `automod/engine/testing.go`

- 📄 `automod/helpers/bsky.go`

- 📄 `automod/rules/harassment.go`

- 📄 `automod/rules/mentions.go`

- 📄 `automod/rules/misleading.go`

- 📄 `automod/rules/replies.go`

- 📄 `backfill/backfill.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/beemo/notify_mentions.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/bluepages/handlers.go`

- 📄 `cmd/bluepages/main.go`

- 📄 `cmd/bluepages/resolver.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/did.go`

- 📄 `cmd/gosky/handle.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/hepa/main.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/host.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/verify.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/repo_manager.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/server.go`

- 📄 `cmd/tap/util.go`

- 📄 `lex/lexgen/codegen.go`

- 📄 `lex/lexgen/flatten.go`

- 📄 `lex/lexgen/util.go`

- 📄 `lex/lexlint/breaking.go`

- 📄 `lex/lexlint/lint.go`

- 📄 `repo/repo.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/bulk.go`

- 📄 `search/firehose.go`

- 📄 `search/handlers.go`

- 📄 `search/indexing.go`

- 📄 `search/parse_query.go`

- 📄 `search/query.go`

- 📄 `search/transform.go`



### Определения локальных типов (best effort)


#### TIDClock (struct)


*Определено в: `atproto/syntax/tid.go:120`*


| Поле | Тип | JSON |

|------|-----|------|

| `ClockID` | `uint` | `ClockID` |

| `mtx` | `unknown` | `mtx` |

| `lastUnixMicro` | `int64` | `lastUnixMicro` |




---


[import] path: github.com/bluesky-social/indigo/automod type: local


### github.com/bluesky-social/indigo/automod


- **Тип:** local

- **Алиасы:** `automod`

- **Локальная директория пакета:** `automod`



### Кандидаты на типы


`AccountContext`, `BlobRuleFunc`, `Engine`, `IdentityRuleFunc`, `OzoneEventContext`, `OzoneEventRuleFunc`, `PostRuleFunc`, `ProfileRuleFunc`, `RecordContext`, `RecordOp`, `RecordRuleFunc`, `RuleSet`, `SlackNotifier`


### Селекторы (любое использование `pkg.X`)


`AccountContext`, `AccountMeta`, `BlobRuleFunc`, `CreateOp`, `DeleteOp`, `Engine`, `IdentityRuleFunc`, `Notifier`, `OzoneEventContext`, `OzoneEventRuleFunc`, `PostRuleFunc`, `ProfileRuleFunc`, `RecordContext`, `RecordOp`, `RecordRuleFunc`, `ReportReasonOther`, `ReportReasonRude`, `ReportReasonSexual`, `ReportReasonSpam`, `ReportReasonViolation`, `RuleSet`, `SlackNotifier`, `UpdateOp`


### Используется в файлах


- 📄 `automod/capture/capture.go`

- 📄 `automod/capture/fetch.go`

- 📄 `automod/capture/testing.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `automod/helpers/account.go`

- 📄 `automod/helpers/bsky.go`

- 📄 `automod/rules/all.go`

- 📄 `automod/rules/blobs.go`

- 📄 `automod/rules/gtube.go`

- 📄 `automod/rules/harassment.go`

- 📄 `automod/rules/hashtags.go`

- 📄 `automod/rules/identity.go`

- 📄 `automod/rules/interaction.go`

- 📄 `automod/rules/keyword.go`

- 📄 `automod/rules/mentions.go`

- 📄 `automod/rules/misleading.go`

- 📄 `automod/rules/misleading_unicode_reverse.go`

- 📄 `automod/rules/nostr.go`

- 📄 `automod/rules/private.go`

- 📄 `automod/rules/profile.go`

- 📄 `automod/rules/promo.go`

- 📄 `automod/rules/quick.go`

- 📄 `automod/rules/replies.go`

- 📄 `automod/rules/reposts.go`

- 📄 `automod/visual/abyss_rule.go`

- 📄 `automod/visual/hiveai_rule.go`

- 📄 `cmd/hepa/server.go`




---


[import] path: github.com/bluesky-social/indigo/automod/cachestore type: local


### github.com/bluesky-social/indigo/automod/cachestore


- **Тип:** local

- **Алиасы:** `cachestore`

- **Локальная директория пакета:** `automod/cachestore`



### Вызовы


`NewMemCacheStore`, `NewRedisCacheStore`


### Селекторы (любое использование `pkg.X`)


`CacheStore`, `NewMemCacheStore`, `NewRedisCacheStore`


### Используется в файлах


- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/testing.go`

- 📄 `cmd/hepa/server.go`




---


[import] path: github.com/bluesky-social/indigo/automod/capture type: local


### github.com/bluesky-social/indigo/automod/capture


- **Тип:** local

- **Алиасы:** `capture`

- **Локальная директория пакета:** `automod/capture`



### Вызовы


`CaptureRecent`, `FetchAndProcessRecent`, `FetchAndProcessRecord`


### Селекторы (любое использование `pkg.X`)


`CaptureRecent`, `FetchAndProcessRecent`, `FetchAndProcessRecord`


### Используется в файлах


- 📄 `cmd/hepa/main.go`




---


[import] path: github.com/bluesky-social/indigo/automod/consumer type: local


### github.com/bluesky-social/indigo/automod/consumer


- **Тип:** local

- **Алиасы:** `consumer`

- **Локальная директория пакета:** `automod/consumer`



### Кандидаты на типы


`FirehoseConsumer`, `OzoneConsumer`


### Селекторы (любое использование `pkg.X`)


`FirehoseConsumer`, `OzoneConsumer`


### Используется в файлах


- 📄 `cmd/hepa/main.go`



### Определения локальных типов (best effort)


#### FirehoseConsumer (struct)


*Определено в: `automod/consumer/firehose.go:31`*


| Поле | Тип | JSON |

|------|-----|------|

| `Parallelism` | `int` | `Parallelism` |

| `Logger` | `*slog.Logger` | `Logger` |

| `RedisClient` | `*redis.Client` | `RedisClient` |

| `Engine` | `*automod.Engine` | `Engine` |

| `Host` | `string` | `Host` |

| `lastSeq` | `int64` | `lastSeq` |



#### OzoneConsumer (struct)


*Определено в: `automod/consumer/ozone.go:21`*


| Поле | Тип | JSON |

|------|-----|------|

| `Logger` | `*slog.Logger` | `Logger` |

| `RedisClient` | `*redis.Client` | `RedisClient` |

| `OzoneClient` | `*xrpc.Client` | `OzoneClient` |

| `Engine` | `*automod.Engine` | `Engine` |

| `lastCursor` | `unknown` | `lastCursor` |




---


[import] path: github.com/bluesky-social/indigo/automod/countstore type: local


### github.com/bluesky-social/indigo/automod/countstore


- **Тип:** local

- **Алиасы:** `countstore`

- **Локальная директория пакета:** `automod/countstore`



### Вызовы


`NewMemCountStore`, `NewRedisCountStore`


### Селекторы (любое использование `pkg.X`)


`CountStore`, `NewMemCountStore`, `NewRedisCountStore`, `PeriodDay`, `PeriodHour`, `PeriodTotal`


### Используется в файлах


- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/persisthelpers.go`

- 📄 `automod/engine/testing.go`

- 📄 `automod/pkg.go`

- 📄 `automod/rules/harassment.go`

- 📄 `automod/rules/identity.go`

- 📄 `automod/rules/interaction.go`

- 📄 `automod/rules/mentions.go`

- 📄 `automod/rules/promo.go`

- 📄 `automod/rules/replies.go`

- 📄 `automod/rules/reposts.go`

- 📄 `cmd/hepa/server.go`




---


[import] path: github.com/bluesky-social/indigo/automod/engine type: local


### github.com/bluesky-social/indigo/automod/engine


- **Тип:** local

- **Алиасы:** `engine`

- **Локальная директория пакета:** `automod/engine`



### Кандидаты на типы


`EngineConfig`


### Селекторы (любое использование `pkg.X`)


`AccountContext`, `AccountMeta`, `AccountPrivate`, `BlobRuleFunc`, `CreateOp`, `DeleteOp`, `Engine`, `EngineConfig`, `IdentityRuleFunc`, `Notifier`, `OzoneEventContext`, `OzoneEventRuleFunc`, `PostRuleFunc`, `ProfileRuleFunc`, `ProfileSummary`, `RecordContext`, `RecordOp`, `RecordRuleFunc`, `ReportReasonMisleading`, `ReportReasonOther`, `ReportReasonRude`, `ReportReasonSexual`, `ReportReasonSpam`, `ReportReasonViolation`, `RuleSet`, `SlackNotifier`, `UpdateOp`


### Используется в файлах


- 📄 `automod/pkg.go`

- 📄 `cmd/hepa/server.go`



### Определения локальных типов (best effort)


#### EngineConfig (struct)


*Определено в: `automod/engine/engine.go:46`*


| Поле | Тип | JSON |

|------|-----|------|

| `SkipAccountMeta` | `bool` | `SkipAccountMeta` |

| `ReportDupePeriod` | `unknown` | `ReportDupePeriod` |

| `QuotaModReportDay` | `int` | `QuotaModReportDay` |

| `QuotaModTakedownDay` | `int` | `QuotaModTakedownDay` |

| `QuotaModActionDay` | `int` | `QuotaModActionDay` |

| `RecordEventTimeout` | `unknown` | `RecordEventTimeout` |

| `IdentityEventTimeout` | `unknown` | `IdentityEventTimeout` |

| `OzoneEventTimeout` | `unknown` | `OzoneEventTimeout` |




---


[import] path: github.com/bluesky-social/indigo/automod/flagstore type: local


### github.com/bluesky-social/indigo/automod/flagstore


- **Тип:** local

- **Алиасы:** `flagstore`

- **Локальная директория пакета:** `automod/flagstore`



### Вызовы


`NewMemFlagStore`, `NewRedisFlagStore`


### Селекторы (любое использование `pkg.X`)


`FlagStore`, `NewMemFlagStore`, `NewRedisFlagStore`


### Используется в файлах


- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/testing.go`

- 📄 `cmd/hepa/server.go`




---


[import] path: github.com/bluesky-social/indigo/automod/helpers type: local


### github.com/bluesky-social/indigo/automod/helpers


- **Тип:** local

- **Алиасы:** `helpers`

- **Локальная директория пакета:** `automod/helpers`



### Вызовы


`AccountIsOlderThan`, `AccountIsYoungerThan`, `DedupeStrings`, `ExtractFacets`, `ExtractHashtagsPost`, `ExtractTextTokensPost`, `ExtractTextTokensProfile`, `ExtractTextURLs`, `HashOfString`, `IsSelfThread`, `NormalizeHashtag`, `ParentOrRootIsFollower`


### Селекторы (любое использование `pkg.X`)


`AccountIsOlderThan`, `AccountIsYoungerThan`, `DedupeStrings`, `ExtractFacets`, `ExtractHashtagsPost`, `ExtractTextTokensPost`, `ExtractTextTokensProfile`, `ExtractTextURLs`, `HashOfString`, `IsSelfThread`, `NormalizeHashtag`, `ParentOrRootIsFollower`, `PostFacet`


### Используется в файлах


- 📄 `automod/rules/harassment.go`

- 📄 `automod/rules/hashtags.go`

- 📄 `automod/rules/identity.go`

- 📄 `automod/rules/keyword.go`

- 📄 `automod/rules/mentions.go`

- 📄 `automod/rules/misleading.go`

- 📄 `automod/rules/nostr.go`

- 📄 `automod/rules/promo.go`

- 📄 `automod/rules/quick.go`

- 📄 `automod/rules/replies.go`

- 📄 `automod/rules/reposts.go`

- 📄 `automod/visual/hiveai_rule.go`




---


[import] path: github.com/bluesky-social/indigo/automod/keyword type: local


### github.com/bluesky-social/indigo/automod/keyword


- **Тип:** local

- **Алиасы:** `keyword`

- **Локальная директория пакета:** `automod/keyword`



### Вызовы


`SlugContainsExplicitSlur`, `SlugIsExplicitSlur`, `Slugify`, `TokenInSet`, `TokenizeIdentifier`, `TokenizeText`


### Селекторы (любое использование `pkg.X`)


`SlugContainsExplicitSlur`, `SlugIsExplicitSlur`, `Slugify`, `TokenInSet`, `TokenizeIdentifier`, `TokenizeText`


### Используется в файлах


- 📄 `automod/engine/persist.go`

- 📄 `automod/helpers/bsky.go`

- 📄 `automod/keyword/cmd/kw-cli/main.go`

- 📄 `automod/rules/hashtags.go`

- 📄 `automod/rules/keyword.go`

- 📄 `automod/rules/profile.go`




---


[import] path: github.com/bluesky-social/indigo/automod/rules type: local


### github.com/bluesky-social/indigo/automod/rules


- **Тип:** local

- **Алиасы:** `rules`

- **Локальная директория пакета:** `automod/rules`



### Вызовы


`DefaultRules`


### Селекторы (любое использование `pkg.X`)


`DefaultRules`


### Используется в файлах


- 📄 `cmd/hepa/server.go`




---


[import] path: github.com/bluesky-social/indigo/automod/setstore type: local


### github.com/bluesky-social/indigo/automod/setstore


- **Тип:** local

- **Алиасы:** `setstore`

- **Локальная директория пакета:** `automod/setstore`



### Вызовы


`NewMemSetStore`


### Селекторы (любое использование `pkg.X`)


`NewMemSetStore`, `SetStore`


### Используется в файлах


- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/testing.go`

- 📄 `automod/keyword/cmd/kw-cli/main.go`

- 📄 `cmd/hepa/server.go`




---


[import] path: github.com/bluesky-social/indigo/automod/visual type: local


### github.com/bluesky-social/indigo/automod/visual


- **Тип:** local

- **Алиасы:** `visual`

- **Локальная директория пакета:** `automod/visual`



### Вызовы


`NewAbyssClient`, `NewHiveAIClient`, `NewPreScreenClient`


### Селекторы (любое использование `pkg.X`)


`NewAbyssClient`, `NewHiveAIClient`, `NewPreScreenClient`


### Используется в файлах


- 📄 `cmd/hepa/server.go`




---


[import] path: github.com/bluesky-social/indigo/backfill type: local


### github.com/bluesky-social/indigo/backfill


- **Тип:** local

- **Алиасы:** `backfill`

- **Локальная директория пакета:** `backfill`



### Вызовы


`DefaultBackfillOptions`, `NewBackfiller`, `NewGormstore`


### Кандидаты на типы


`Backfiller`, `GormDBJob`, `Gormstore`


### Селекторы (любое использование `pkg.X`)


`Backfiller`, `DefaultBackfillOptions`, `GormDBJob`, `Gormstore`, `NewBackfiller`, `NewGormstore`, `StateEnqueued`


### Используется в файлах


- 📄 `search/firehose.go`

- 📄 `search/indexing.go`



### Определения локальных типов (best effort)


#### Backfiller (struct)


*Определено в: `backfill/backfill.go:65`*


| Поле | Тип | JSON |

|------|-----|------|

| `Name` | `string` | `Name` |

| `HandleCreateRecord` | `unknown` | `HandleCreateRecord` |

| `HandleUpdateRecord` | `unknown` | `HandleUpdateRecord` |

| `HandleDeleteRecord` | `unknown` | `HandleDeleteRecord` |

| `Store` | `Store` | `Store` |

| `ParallelBackfills` | `int` | `ParallelBackfills` |

| `ParallelRecordCreates` | `int` | `ParallelRecordCreates` |

| `NSIDFilter` | `string` | `NSIDFilter` |

| `RelayHost` | `string` | `RelayHost` |

| `syncLimiter` | `*rate.Limiter` | `syncLimiter` |

| `magicHeaderKey` | `string` | `magicHeaderKey` |

| `magicHeaderVal` | `string` | `magicHeaderVal` |

| `tryRelayRepoFetch` | `bool` | `tryRelayRepoFetch` |

| `stop` | `unknown` | `stop` |

| `Directory` | `unknown` | `Directory` |



#### GormDBJob (struct)


*Определено в: `backfill/gormstore.go:34`*


| Поле | Тип | JSON |

|------|-----|------|

| `Repo` | `string` | `Repo` |

| `State` | `string` | `State` |

| `Rev` | `string` | `Rev` |

| `RetryCount` | `int` | `RetryCount` |

| `RetryAfter` | `*time.Time` | `RetryAfter` |



#### Gormstore (struct)


*Определено в: `backfill/gormstore.go:44`*


| Поле | Тип | JSON |

|------|-----|------|

| `lk` | `unknown` | `lk` |

| `jobs` | `map[string]*Gormjob` | `jobs` |

| `qlk` | `unknown` | `qlk` |

| `taskQueue` | `[]string` | `taskQueue` |

| `db` | `*gorm.DB` | `db` |




---


[import] path: github.com/bluesky-social/indigo/carstore type: local


### github.com/bluesky-social/indigo/carstore


- **Тип:** local

- **Алиасы:** `carstore`

- **Локальная директория пакета:** `carstore`



### Вызовы


`LdWrite`


### Кандидаты на типы


`CarStore`, `MaxSliceLength`, `NonArchivalCarstore`


### Селекторы (любое использование `pkg.X`)


`CarStore`, `LdWrite`, `MaxSliceLength`, `NonArchivalCarstore`


### Используется в файлах


- 📄 `cmd/stress/main.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `repomgr/repomgr.go`



### Определения локальных типов (best effort)


#### CarStore (interface)


*Определено в: `carstore/bs.go:47`*


```go

interface {
	// TODO: not really part of general interface
	CompactUserShards(ctx context.Context, user models.Uid, skipBigShards bool) (*CompactionStats, error)
	// TODO: not really part of general interface
	GetCompactionTargets(ctx context.Context, shardCount int) ([]CompactionTarget, error)

	GetUserRepoHead(ctx context.Context, user models.Uid) (cid.Cid, error)
	GetUserRepoRev(ctx context.Context, user models.Uid) (string, error)
	ImportSlice(ctx context.Context, uid models.Uid, since *string, carslice []byte) (cid.Cid, *DeltaSession, error)
	NewDeltaSession(ctx context.Context, user models.Uid, since *string) (*DeltaSession, error)
	ReadOnlySession(user models.Uid) (*DeltaSession, error)
	ReadUserCar(ctx context.Context, user models.Uid, sinceRev string, incremental bool, w io.Writer) error
	Stat(ctx context.Context, usr models.Uid) ([]UserStat, error)
	WipeUserData(ctx context.Context, user models.Uid) error
}

```


#### NonArchivalCarstore (struct)


*Определено в: `carstore/nonarchive.go:21`*


| Поле | Тип | JSON |

|------|-----|------|

| `db` | `*gorm.DB` | `db` |

| `lk` | `unknown` | `lk` |

| `lastCommitCache` | `map[models.Uid]*commitRefInfo` | `lastCommitCache` |

| `log` | `*slog.Logger` | `log` |




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/relay type: local


### github.com/bluesky-social/indigo/cmd/relay/relay


- **Тип:** local

- **Алиасы:** `relay`

- **Локальная директория пакета:** `cmd/relay/relay`



### Вызовы


`CreateDomainBan`, `DefaultRelayConfig`, `DomainIsBanned`, `GetAccount`, `GetAccountRepo`, `GetHost`, `HandleSubscribeRepos`, `Healthcheck`, `IsTrustedHostname`, `ListAccountTakedowns`, `ListAccountsDetailed`, `ListConsumers`, `ListDomainBans`, `ListHosts`, `NewHostClient`, `NewRelay`, `ParseHostname`, `RemoveDomainBan`, `SubscribeToHost`, `UpdateAccountLocalStatus`, `UpdateHostAccountLimit`, `UpdateHostStatus`


### Кандидаты на типы


`Relay`


### Селекторы (любое использование `pkg.X`)


`Config`, `CreateDomainBan`, `DefaultRelayConfig`, `Dir`, `DomainIsBanned`, `ErrAccountNotFound`, `ErrAccountRepoNotFound`, `ErrHostInactive`, `ErrHostNotFound`, `Events`, `EventsReceivedCounter`, `GetAccount`, `GetAccountRepo`, `GetHost`, `HandleSubscribeRepos`, `Healthcheck`, `HostChecker`, `HostPerDayLimiter`, `IsTrustedHostname`, `ListAccountTakedowns`, `ListAccountsDetailed`, `ListConsumers`, `ListDomainBans`, `ListHosts`, `NewHostClient`, `NewRelay`, `ParseHostname`, `Relay`, `RemoveDomainBan`, `Slurper`, `SubscribeToHost`, `UpdateAccountLocalStatus`, `UpdateHostAccountLimit`, `UpdateHostStatus`, `sqlite`


### Используется в файлах


- 📄 `cmd/relay/forward.go`

- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/service.go`

- 📄 `cmd/relay/stubs.go`

- 📄 `cmd/relay/testing/runner.go`



### Определения локальных типов (best effort)


#### Relay (struct)


*Определено в: `cmd/relay/relay/relay.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `db` | `*gorm.DB` | `db` |

| `Dir` | `unknown` | `Dir` |

| `Logger` | `*slog.Logger` | `Logger` |

| `Slurper` | `*Slurper` | `Slurper` |

| `Events` | `*eventmgr.EventManager` | `Events` |

| `HostChecker` | `HostChecker` | `HostChecker` |

| `Config` | `RelayConfig` | `Config` |

| `consumersLk` | `unknown` | `consumersLk` |

| `nextConsumerID` | `uint64` | `nextConsumerID` |

| `consumers` | `map[uint64]*SocketConsumer` | `consumers` |

| `accountCache` | `*lru.Cache[string, *models.Account]` | `accountCache` |

| `HostPerDayLimiter` | `*slidingwindow.Limiter` | `HostPerDayLimiter` |




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/relay/models type: local


### github.com/bluesky-social/indigo/cmd/relay/relay/models


- **Тип:** local

- **Алиасы:** `models`

- **Локальная директория пакета:** `cmd/relay/relay/models`



### Вызовы


`AccountStatus`, `HostStatus`


### Кандидаты на типы


`Account`, `AccountDetailed`, `AccountRepo`, `AccountStatus`, `AccountStatusActive`, `DomainBan`, `Host`, `HostStatusActive`, `HostStatusBanned`


### Селекторы (любое использование `pkg.X`)


`Account`, `AccountDetailed`, `AccountRepo`, `AccountStatus`, `AccountStatusActive`, `AccountStatusDeactivated`, `AccountStatusDeleted`, `AccountStatusDesynchronized`, `AccountStatusHostThrottled`, `AccountStatusInactive`, `AccountStatusSuspended`, `AccountStatusTakendown`, `DomainBan`, `Host`, `HostStatus`, `HostStatusActive`, `HostStatusBanned`, `HostStatusIdle`, `HostStatusOffline`, `PDS`


### Используется в файлах


- 📄 `cmd/relay/handlers.go`

- 📄 `cmd/relay/handlers_admin.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/crawl.go`

- 📄 `cmd/relay/relay/domain_ban.go`

- 📄 `cmd/relay/relay/host.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/relay/verify.go`



### Определения локальных типов (best effort)


#### Account (struct)


*Определено в: `cmd/relay/relay/models/models.go:75`*


| Поле | Тип | JSON |

|------|-----|------|

| `UID` | `uint64` | `UID` |

| `DID` | `string` | `DID` |

| `HostID` | `uint64` | `HostID` |

| `Status` | `AccountStatus` | `Status` |

| `UpstreamStatus` | `AccountStatus` | `UpstreamStatus` |



#### AccountDetailed (struct)


*Определено в: `cmd/relay/relay/models/joins.go:3`*


| Поле | Тип | JSON |

|------|-----|------|

| `UID` | `uint64` | `UID` |

| `DID` | `string` | `DID` |

| `HostID` | `uint64` | `HostID` |

| `Status` | `AccountStatus` | `Status` |

| `UpstreamStatus` | `AccountStatus` | `UpstreamStatus` |

| `Rev` | `string` | `Rev` |

| `CommitCID` | `string` | `CommitCID` |

| `CommitDataCID` | `string` | `CommitDataCID` |



#### AccountRepo (struct)


*Определено в: `cmd/relay/relay/models/models.go:90`*


| Поле | Тип | JSON |

|------|-----|------|

| `UID` | `uint64` | `UID` |

| `Rev` | `string` | `Rev` |

| `CommitCID` | `string` | `CommitCID` |

| `CommitDataCID` | `string` | `CommitDataCID` |



#### DomainBan (struct)


*Определено в: `cmd/relay/relay/models/models.go:7`*


| Поле | Тип | JSON |

|------|-----|------|

| `ID` | `uint64` | `ID` |

| `CreatedAt` | `unknown` | `CreatedAt` |

| `Domain` | `string` | `Domain` |



#### Host (struct)


*Определено в: `cmd/relay/relay/models/models.go:25`*


| Поле | Тип | JSON |

|------|-----|------|

| `ID` | `uint64` | `ID` |

| `CreatedAt` | `unknown` | `CreatedAt` |

| `UpdatedAt` | `unknown` | `UpdatedAt` |

| `Hostname` | `string` | `Hostname` |

| `NoSSL` | `bool` | `NoSSL` |

| `AccountLimit` | `int64` | `AccountLimit` |

| `Trusted` | `bool` | `Trusted` |

| `Status` | `HostStatus` | `Status` |

| `LastSeq` | `int64` | `LastSeq` |

| `AccountCount` | `int64` | `AccountCount` |




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/stream type: local


### github.com/bluesky-social/indigo/cmd/relay/stream


- **Тип:** local

- **Алиасы:** `stream`

- **Локальная директория пакета:** `cmd/relay/stream`



### Вызовы


`HandleRepoStream`, `NewInstrumentedRepoStreamCallbacks`


### Кандидаты на типы


`ErrorFrame`, `RepoStreamCallbacks`, `XRPCStreamEvent`


### Селекторы (любое использование `pkg.X`)


`ErrorFrame`, `EventHeader`, `HandleRepoStream`, `NewInstrumentedRepoStreamCallbacks`, `RepoStreamCallbacks`, `XRPCStreamEvent`


### Используется в файлах


- 📄 `cmd/relay/relay/account.go`

- 📄 `cmd/relay/relay/broadcast.go`

- 📄 `cmd/relay/relay/ingest.go`

- 📄 `cmd/relay/relay/slurper.go`

- 📄 `cmd/relay/stream/eventmgr/event_manager.go`

- 📄 `cmd/relay/stream/eventmgr/subscriber.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`

- 📄 `cmd/relay/stream/persist/persist.go`

- 📄 `cmd/relay/stream/schedulers/parallel/parallel.go`

- 📄 `cmd/relay/stream/schedulers/sequential/sequential.go`

- 📄 `cmd/relay/testing/consumer.go`

- 📄 `cmd/relay/testing/producer.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/relay/testing/scenario.go`



### Определения локальных типов (best effort)


#### ErrorFrame (struct)


*Определено в: `cmd/relay/stream/events.go:150`*


| Поле | Тип | JSON |

|------|-----|------|

| `Error` | `string` | `Error` |

| `Message` | `string` | `Message` |



#### RepoStreamCallbacks (struct)


*Определено в: `cmd/relay/stream/consumer.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `RepoCommit` | `unknown` | `RepoCommit` |

| `RepoSync` | `unknown` | `RepoSync` |

| `RepoIdentity` | `unknown` | `RepoIdentity` |

| `RepoAccount` | `unknown` | `RepoAccount` |

| `RepoInfo` | `unknown` | `RepoInfo` |

| `LabelLabels` | `unknown` | `LabelLabels` |

| `LabelInfo` | `unknown` | `LabelInfo` |

| `Error` | `unknown` | `Error` |



#### XRPCStreamEvent (struct)


*Определено в: `cmd/relay/stream/events.go:25`*


| Поле | Тип | JSON |

|------|-----|------|

| `Error` | `*ErrorFrame` | `Error` |

| `RepoCommit` | `*comatproto.SyncSubscribeRepos_Commit` | `RepoCommit` |

| `RepoSync` | `*comatproto.SyncSubscribeRepos_Sync` | `RepoSync` |

| `RepoIdentity` | `*comatproto.SyncSubscribeRepos_Identity` | `RepoIdentity` |

| `RepoInfo` | `*comatproto.SyncSubscribeRepos_Info` | `RepoInfo` |

| `RepoAccount` | `*comatproto.SyncSubscribeRepos_Account` | `RepoAccount` |

| `LabelLabels` | `*comatproto.LabelSubscribeLabels_Labels` | `LabelLabels` |

| `LabelInfo` | `*comatproto.LabelSubscribeLabels_Info` | `LabelInfo` |

| `PrivUid` | `uint64` | `PrivUid` |

| `PrivPdsId` | `uint` | `PrivPdsId` |

| `PrivRelevantPds` | `[]uint` | `PrivRelevantPds` |

| `Preserialized` | `[]byte` | `Preserialized` |




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/stream/eventmgr type: local


### github.com/bluesky-social/indigo/cmd/relay/stream/eventmgr


- **Тип:** local

- **Алиасы:** `eventmgr`

- **Локальная директория пакета:** `cmd/relay/stream/eventmgr`



### Вызовы


`NewEventManager`


### Кандидаты на типы


`EventManager`


### Селекторы (любое использование `pkg.X`)


`EventManager`, `NewEventManager`


### Используется в файлах


- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/relay/relay.go`

- 📄 `cmd/relay/testing/runner.go`



### Определения локальных типов (best effort)


#### EventManager (struct)


*Определено в: `cmd/relay/stream/eventmgr/event_manager.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `subs` | `[]*Subscriber` | `subs` |

| `subsLk` | `unknown` | `subsLk` |

| `bufferSize` | `int` | `bufferSize` |

| `crossoverBufferSize` | `int` | `crossoverBufferSize` |

| `persister` | `unknown` | `persister` |

| `log` | `*slog.Logger` | `log` |




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/stream/persist type: local


### github.com/bluesky-social/indigo/cmd/relay/stream/persist


- **Тип:** local

- **Алиасы:** `persist`

- **Локальная директория пакета:** `cmd/relay/stream/persist`



### Селекторы (любое использование `pkg.X`)


`EventPersistence`


### Используется в файлах


- 📄 `cmd/relay/stream/eventmgr/event_manager.go`

- 📄 `cmd/relay/stream/persist/diskpersist/diskpersist.go`




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/stream/persist/diskpersist type: local


### github.com/bluesky-social/indigo/cmd/relay/stream/persist/diskpersist


- **Тип:** local

- **Алиасы:** `diskpersist`

- **Локальная директория пакета:** `cmd/relay/stream/persist/diskpersist`



### Вызовы


`DefaultDiskPersistOptions`, `NewDiskPersistence`


### Селекторы (любое использование `pkg.X`)


`DefaultDiskPersistOptions`, `NewDiskPersistence`


### Используется в файлах


- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/testing/runner.go`




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/stream/schedulers type: local


### github.com/bluesky-social/indigo/cmd/relay/stream/schedulers


- **Тип:** local

- **Алиасы:** `schedulers`

- **Локальная директория пакета:** `cmd/relay/stream/schedulers`



### Селекторы (любое использование `pkg.X`)


`WorkItemsActive`, `WorkItemsAdded`, `WorkItemsProcessed`, `WorkersActive`


### Используется в файлах


- 📄 `cmd/relay/stream/schedulers/parallel/parallel.go`

- 📄 `cmd/relay/stream/schedulers/sequential/sequential.go`




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/stream/schedulers/parallel type: local


### github.com/bluesky-social/indigo/cmd/relay/stream/schedulers/parallel


- **Тип:** local

- **Алиасы:** `parallel`

- **Локальная директория пакета:** `cmd/relay/stream/schedulers/parallel`



### Вызовы


`NewScheduler`


### Кандидаты на типы


`Scheduler`


### Селекторы (любое использование `pkg.X`)


`NewScheduler`, `Scheduler`


### Используется в файлах


- 📄 `cmd/relay/relay/slurper.go`



### Определения локальных типов (best effort)


#### Scheduler (struct)


*Определено в: `cmd/relay/stream/schedulers/parallel/parallel.go:16`*


| Поле | Тип | JSON |

|------|-----|------|

| `maxConcurrency` | `int` | `maxConcurrency` |

| `maxQueue` | `int` | `maxQueue` |

| `do` | `unknown` | `do` |

| `feeder` | `unknown` | `feeder` |

| `out` | `unknown` | `out` |

| `lk` | `unknown` | `lk` |

| `active` | `map[string][]*consumerTask` | `active` |

| `ident` | `string` | `ident` |

| `inflightSeq` | `map[int64]bool` | `inflightSeq` |

| `lastSeq` | `unknown` | `lastSeq` |

| `itemsAdded` | `unknown` | `itemsAdded` |

| `itemsProcessed` | `unknown` | `itemsProcessed` |

| `itemsActive` | `unknown` | `itemsActive` |

| `workersActive` | `unknown` | `workersActive` |

| `log` | `*slog.Logger` | `log` |




---


[import] path: github.com/bluesky-social/indigo/cmd/relay/stream/schedulers/sequential type: local


### github.com/bluesky-social/indigo/cmd/relay/stream/schedulers/sequential


- **Тип:** local

- **Алиасы:** `sequential`

- **Локальная директория пакета:** `cmd/relay/stream/schedulers/sequential`



### Вызовы


`NewScheduler`


### Селекторы (любое использование `pkg.X`)


`NewScheduler`


### Используется в файлах


- 📄 `cmd/relay/testing/consumer.go`




---


[import] path: github.com/bluesky-social/indigo/cmd/tap/models type: local


### github.com/bluesky-social/indigo/cmd/tap/models


- **Тип:** local

- **Алиасы:** `models`

- **Локальная директория пакета:** `cmd/tap/models`



### Вызовы


`AccountStatus`


### Кандидаты на типы


`AccountStatusDeleted`, `CollectionCursor`, `FirehoseCursor`, `ListReposCursor`, `OutboxBuffer`, `Repo`, `RepoRecord`, `RepoState`, `RepoStateActive`, `RepoStateResyncing`, `ResyncBuffer`


### Селекторы (любое использование `pkg.X`)


`AccountStatus`, `AccountStatusActive`, `AccountStatusDeactivated`, `AccountStatusDeleted`, `AccountStatusSuspended`, `AccountStatusTakendown`, `CollectionCursor`, `FirehoseCursor`, `ListReposCursor`, `OutboxBuffer`, `Repo`, `RepoRecord`, `RepoState`, `RepoStateActive`, `RepoStateDesynchronized`, `RepoStateError`, `RepoStatePending`, `RepoStateResyncing`, `ResyncBuffer`


### Используется в файлах


- 📄 `cmd/tap/crawler.go`

- 📄 `cmd/tap/db_helpers.go`

- 📄 `cmd/tap/event_manager.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `cmd/tap/repo_manager.go`

- 📄 `cmd/tap/resyncer.go`

- 📄 `cmd/tap/server.go`

- 📄 `cmd/tap/tap.go`

- 📄 `cmd/tap/types.go`



### Определения локальных типов (best effort)


#### CollectionCursor (struct)


*Определено в: `cmd/tap/models/models.go:68`*


| Поле | Тип | JSON |

|------|-----|------|

| `Url` | `string` | `Url` |

| `Collection` | `string` | `Collection` |

| `Cursor` | `string` | `Cursor` |



#### FirehoseCursor (struct)


*Определено в: `cmd/tap/models/models.go:58`*


| Поле | Тип | JSON |

|------|-----|------|

| `Url` | `string` | `Url` |

| `Cursor` | `int64` | `Cursor` |



#### ListReposCursor (struct)


*Определено в: `cmd/tap/models/models.go:63`*


| Поле | Тип | JSON |

|------|-----|------|

| `Url` | `string` | `Url` |

| `Cursor` | `string` | `Cursor` |



#### OutboxBuffer (struct)


*Определено в: `cmd/tap/models/models.go:38`*


| Поле | Тип | JSON |

|------|-----|------|

| `ID` | `uint` | `ID` |

| `Did` | `string` | `Did` |

| `Live` | `bool` | `Live` |

| `Data` | `string` | `Data` |



#### Repo (struct)


*Определено в: `cmd/tap/models/models.go:26`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `Did` |

| `State` | `RepoState` | `State` |

| `Status` | `AccountStatus` | `Status` |

| `Handle` | `string` | `Handle` |

| `Rev` | `string` | `Rev` |

| `PrevData` | `string` | `PrevData` |

| `ErrorMsg` | `string` | `ErrorMsg` |

| `RetryCount` | `int` | `RetryCount` |

| `RetryAfter` | `int64` | `RetryAfter` |



#### RepoRecord (struct)


*Определено в: `cmd/tap/models/models.go:51`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `Did` |

| `Collection` | `string` | `Collection` |

| `Rkey` | `string` | `Rkey` |

| `Cid` | `string` | `Cid` |



#### ResyncBuffer (struct)


*Определено в: `cmd/tap/models/models.go:45`*


| Поле | Тип | JSON |

|------|-----|------|

| `ID` | `uint` | `ID` |

| `Did` | `string` | `Did` |

| `Data` | `string` | `Data` |




---


[import] path: github.com/bluesky-social/indigo/events type: local


### github.com/bluesky-social/indigo/events


- **Тип:** local

- **Алиасы:** `events`

- **Локальная директория пакета:** `events`



### Вызовы


`AddCommit`, `AddEvent`, `AddIdentityEvent`, `HandleRepoStream`, `NewEventManager`, `SequenceForEvent`, `Subscribe`, `WaitForReady`, `addToResyncBuffer`


### Кандидаты на типы


`ErrorFrame`, `EventHeader`, `EventManager`, `RepoStreamCallbacks`, `XRPCStreamEvent`


### Селекторы (любое использование `pkg.X`)


`AddCommit`, `AddEvent`, `AddIdentityEvent`, `ErrorFrame`, `EventHeader`, `EventManager`, `EventPersistence`, `HandleRepoStream`, `NewEventManager`, `RepoStreamCallbacks`, `Scheduler`, `SequenceForEvent`, `Subscribe`, `WaitForReady`, `XRPCStreamEvent`, `addToResyncBuffer`


### Используется в файлах


- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/collectiondir/firehose.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/sonar/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/tap/firehose.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `events/schedulers/autoscaling/autoscaling.go`

- 📄 `events/schedulers/parallel/parallel.go`

- 📄 `events/schedulers/sequential/sequential.go`

- 📄 `events/yolopersist/yolopersist.go`

- 📄 `gen/main.go`

- 📄 `search/firehose.go`

- 📄 `splitter/firehose.go`

- 📄 `splitter/ringbuf.go`

- 📄 `splitter/splitter.go`



### Определения локальных типов (best effort)


#### ErrorFrame (struct)


*Определено в: `events/events.go:320`*


| Поле | Тип | JSON |

|------|-----|------|

| `Error` | `string` | `Error` |

| `Message` | `string` | `Message` |



#### EventHeader (struct)


*Определено в: `events/events.go:159`*


| Поле | Тип | JSON |

|------|-----|------|

| `Op` | `int64` | `Op` |

| `MsgType` | `string` | `MsgType` |



#### EventManager (struct)


*Определено в: `events/events.go:29`*


| Поле | Тип | JSON |

|------|-----|------|

| `subs` | `[]*Subscriber` | `subs` |

| `subsLk` | `unknown` | `subsLk` |

| `bufferSize` | `int` | `bufferSize` |

| `crossoverBufferSize` | `int` | `crossoverBufferSize` |

| `persister` | `EventPersistence` | `persister` |

| `log` | `*slog.Logger` | `log` |



#### RepoStreamCallbacks (struct)


*Определено в: `events/consumer.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `RepoCommit` | `unknown` | `RepoCommit` |

| `RepoSync` | `unknown` | `RepoSync` |

| `RepoIdentity` | `unknown` | `RepoIdentity` |

| `RepoAccount` | `unknown` | `RepoAccount` |

| `RepoInfo` | `unknown` | `RepoInfo` |

| `LabelLabels` | `unknown` | `LabelLabels` |

| `LabelInfo` | `unknown` | `LabelInfo` |

| `Error` | `unknown` | `Error` |



#### XRPCStreamEvent (struct)


*Определено в: `events/events.go:195`*


| Поле | Тип | JSON |

|------|-----|------|

| `Error` | `*ErrorFrame` | `Error` |

| `RepoCommit` | `*comatproto.SyncSubscribeRepos_Commit` | `RepoCommit` |

| `RepoSync` | `*comatproto.SyncSubscribeRepos_Sync` | `RepoSync` |

| `RepoIdentity` | `*comatproto.SyncSubscribeRepos_Identity` | `RepoIdentity` |

| `RepoInfo` | `*comatproto.SyncSubscribeRepos_Info` | `RepoInfo` |

| `RepoAccount` | `*comatproto.SyncSubscribeRepos_Account` | `RepoAccount` |

| `LabelLabels` | `*comatproto.LabelSubscribeLabels_Labels` | `LabelLabels` |

| `LabelInfo` | `*comatproto.LabelSubscribeLabels_Info` | `LabelInfo` |

| `PrivUid` | `unknown` | `PrivUid` |

| `PrivPdsId` | `uint` | `PrivPdsId` |

| `PrivRelevantPds` | `[]uint` | `PrivRelevantPds` |

| `Preserialized` | `[]byte` | `Preserialized` |




---


[import] path: github.com/bluesky-social/indigo/events/pebblepersist type: local


### github.com/bluesky-social/indigo/events/pebblepersist


- **Тип:** local

- **Алиасы:** `pebblepersist`

- **Локальная директория пакета:** `events/pebblepersist`



### Вызовы


`NewPebblePersistance`


### Кандидаты на типы


`PebblePersist`, `PebblePersistOptions`


### Селекторы (любое использование `pkg.X`)


`ErrNoLast`, `NewPebblePersistance`, `PebblePersist`, `PebblePersistOptions`


### Используется в файлах


- 📄 `cmd/rainbow/main.go`

- 📄 `splitter/splitter.go`



### Определения локальных типов (best effort)


#### PebblePersist (struct)


*Определено в: `events/pebblepersist/pebblepersist.go:20`*


| Поле | Тип | JSON |

|------|-----|------|

| `broadcast` | `unknown` | `broadcast` |

| `db` | `*pebble.DB` | `db` |

| `prevSeq` | `int64` | `prevSeq` |

| `prevSeqExtra` | `uint32` | `prevSeqExtra` |

| `cancel` | `unknown` | `cancel` |

| `options` | `PebblePersistOptions` | `options` |



#### PebblePersistOptions (struct)


*Определено в: `events/pebblepersist/pebblepersist.go:32`*


| Поле | Тип | JSON |

|------|-----|------|

| `DbPath` | `string` | `DbPath` |

| `PersistDuration` | `unknown` | `PersistDuration` |

| `GCPeriod` | `unknown` | `GCPeriod` |

| `MaxBytes` | `uint64` | `MaxBytes` |




---


[import] path: github.com/bluesky-social/indigo/events/schedulers type: local


### github.com/bluesky-social/indigo/events/schedulers


- **Тип:** local

- **Алиасы:** `schedulers`

- **Локальная директория пакета:** `events/schedulers`



### Селекторы (любое использование `pkg.X`)


`WorkItemsActive`, `WorkItemsAdded`, `WorkItemsProcessed`, `WorkersActive`


### Используется в файлах


- 📄 `events/schedulers/autoscaling/autoscaling.go`

- 📄 `events/schedulers/parallel/parallel.go`

- 📄 `events/schedulers/sequential/sequential.go`




---


[import] path: github.com/bluesky-social/indigo/events/schedulers/autoscaling type: local


### github.com/bluesky-social/indigo/events/schedulers/autoscaling


- **Тип:** local

- **Алиасы:** `autoscaling`

- **Локальная директория пакета:** `events/schedulers/autoscaling`



### Вызовы


`DefaultAutoscaleSettings`, `NewScheduler`


### Селекторы (любое использование `pkg.X`)


`DefaultAutoscaleSettings`, `NewScheduler`


### Используется в файлах


- 📄 `automod/consumer/firehose.go`

- 📄 `search/firehose.go`




---


[import] path: github.com/bluesky-social/indigo/events/schedulers/parallel type: local


### github.com/bluesky-social/indigo/events/schedulers/parallel


- **Тип:** local

- **Алиасы:** `parallel`

- **Локальная директория пакета:** `events/schedulers/parallel`



### Вызовы


`NewScheduler`


### Селекторы (любое использование `pkg.X`)


`NewScheduler`


### Используется в файлах


- 📄 `atproto/repo/cmd/repo-tool/firehose.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/bluepages/firehose.go`

- 📄 `cmd/tap/firehose.go`




---


[import] path: github.com/bluesky-social/indigo/events/schedulers/sequential type: local


### github.com/bluesky-social/indigo/events/schedulers/sequential


- **Тип:** local

- **Алиасы:** `sequential`

- **Локальная директория пакета:** `events/schedulers/sequential`



### Вызовы


`NewScheduler`


### Селекторы (любое использование `pkg.X`)


`NewScheduler`


### Используется в файлах


- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/streamdiff.go`

- 📄 `cmd/sonar/main.go`

- 📄 `splitter/splitter.go`




---


[import] path: github.com/bluesky-social/indigo/fakedata type: local


### github.com/bluesky-social/indigo/fakedata


- **Тип:** local

- **Алиасы:** `fakedata`

- **Локальная директория пакета:** `fakedata`



### Вызовы


`AccountXrpcClient`, `BrowseAccount`, `GenAccount`, `GenFollowsAndMutes`, `GenLikesRepostsReplies`, `GenPosts`, `GenProfile`, `MeasureIterations`, `ReadAccountCatalog`


### Кандидаты на типы


`AccountContext`


### Селекторы (любое использование `pkg.X`)


`AccountContext`, `AccountXrpcClient`, `BrowseAccount`, `GenAccount`, `GenFollowsAndMutes`, `GenLikesRepostsReplies`, `GenPosts`, `GenProfile`, `MeasureIterations`, `ReadAccountCatalog`


### Используется в файлах


- 📄 `cmd/fakermaker/main.go`



### Определения локальных типов (best effort)


#### AccountContext (struct)


*Определено в: `fakedata/accounts.go:28`*


| Поле | Тип | JSON |

|------|-----|------|

| `Index` | `int` | `Index` |

| `AccountType` | `string` | `AccountType` |

| `Email` | `string` | `Email` |

| `Password` | `string` | `Password` |

| `Auth` | `unknown` | `Auth` |




---


[import] path: github.com/bluesky-social/indigo/lex type: local


### github.com/bluesky-social/indigo/lex


- **Тип:** local

- **Алиасы:** `lex`

- **Локальная директория пакета:** `lex`



### Вызовы


`BuildExtDefMap`, `CreateHandlerStub`, `ParsePackages`, `ReadSchema`, `Run`


### Кандидаты на типы


`Package`, `Schema`


### Селекторы (любое использование `pkg.X`)


`BuildExtDefMap`, `CreateHandlerStub`, `Package`, `ParsePackages`, `ReadSchema`, `Run`, `Schema`


### Используется в файлах


- 📄 `cmd/lexgen/main.go`



### Определения локальных типов (best effort)


#### Package (struct)


*Определено в: `lex/gen.go:453`*


| Поле | Тип | JSON |

|------|-----|------|

| `GoPackage` | `string` | `GoPackage` |

| `Prefix` | `string` | `Prefix` |

| `Outdir` | `string` | `Outdir` |

| `Import` | `string` | `Import` |



#### Schema (struct)


*Определено в: `lex/schema.go:13`*


| Поле | Тип | JSON |

|------|-----|------|

| `path` | `string` | `path` |

| `prefix` | `string` | `prefix` |

| `Lexicon` | `int` | `Lexicon` |

| `ID` | `string` | `ID` |

| `Defs` | `map[string]*TypeSchema` | `Defs` |




---


[import] path: github.com/bluesky-social/indigo/lex/util type: local


### github.com/bluesky-social/indigo/lex/util


- **Тип:** local

- **Алиасы:** `lexutil`, `util`

- **Локальная директория пакета:** `lex/util`



### Вызовы


`CborDecodeValue`, `CborTypeExtractReader`, `LexLink`, `RegisterType`, `TypeExtract`


### Кандидаты на типы


`BlobSchema`, `CborChecker`, `LegacyBlob`, `LexBlob`, `LexLink`, `LexiconTypeDecoder`


### Селекторы (любое использование `pkg.X`)


`BlobSchema`, `CBOR`, `CborChecker`, `CborDecodeValue`, `CborTypeExtractReader`, `ErrUnrecognizedType`, `LegacyBlob`, `LexBlob`, `LexBytes`, `LexClient`, `LexLink`, `LexiconTypeDecoder`, `Procedure`, `Query`, `RegisterType`, `TypeExtract`


### Используется в файлах


- 📄 `api/agnostic/actorgetPreferences.go`

- 📄 `api/agnostic/actorputPreferences.go`

- 📄 `api/agnostic/identitygetRecommendedDidCredentials.go`

- 📄 `api/agnostic/identitysignPlcOperation.go`

- 📄 `api/agnostic/identitysubmitPlcOperation.go`

- 📄 `api/agnostic/repoapplyWrites.go`

- 📄 `api/agnostic/repocreateRecord.go`

- 📄 `api/agnostic/repogetRecord.go`

- 📄 `api/agnostic/repolistRecords.go`

- 📄 `api/agnostic/repoputRecord.go`

- 📄 `api/atproto/admindefs.go`

- 📄 `api/atproto/admindeleteAccount.go`

- 📄 `api/atproto/admindisableAccountInvites.go`

- 📄 `api/atproto/admindisableInviteCodes.go`

- 📄 `api/atproto/adminenableAccountInvites.go`

- 📄 `api/atproto/admingetAccountInfo.go`

- 📄 `api/atproto/admingetAccountInfos.go`

- 📄 `api/atproto/admingetInviteCodes.go`

- 📄 `api/atproto/admingetSubjectStatus.go`

- 📄 `api/atproto/adminsearchAccounts.go`

- 📄 `api/atproto/adminsendEmail.go`

- 📄 `api/atproto/adminupdateAccountEmail.go`

- 📄 `api/atproto/adminupdateAccountHandle.go`

- 📄 `api/atproto/adminupdateAccountPassword.go`

- 📄 `api/atproto/adminupdateAccountSigningKey.go`

- 📄 `api/atproto/adminupdateSubjectStatus.go`

- 📄 `api/atproto/cbor_gen.go`

- 📄 `api/atproto/identitygetRecommendedDidCredentials.go`

- 📄 `api/atproto/identityrefreshIdentity.go`

- 📄 `api/atproto/identityrequestPlcOperationSignature.go`

- 📄 `api/atproto/identityresolveDid.go`

- 📄 `api/atproto/identityresolveHandle.go`

- 📄 `api/atproto/identityresolveIdentity.go`

- 📄 `api/atproto/identitysignPlcOperation.go`

- 📄 `api/atproto/identitysubmitPlcOperation.go`

- 📄 `api/atproto/identityupdateHandle.go`

- 📄 `api/atproto/labeldefs.go`

- 📄 `api/atproto/labelqueryLabels.go`

- 📄 `api/atproto/lexiconschema.go`

- 📄 `api/atproto/moderationcreateReport.go`

- 📄 `api/atproto/repoapplyWrites.go`

- 📄 `api/atproto/repocreateRecord.go`

- 📄 `api/atproto/repodeleteRecord.go`

- 📄 `api/atproto/repodescribeRepo.go`

- 📄 `api/atproto/repogetRecord.go`

- 📄 `api/atproto/repoimportRepo.go`

- 📄 `api/atproto/repolistMissingBlobs.go`

- 📄 `api/atproto/repolistRecords.go`

- 📄 `api/atproto/repoputRecord.go`

- 📄 `api/atproto/repostrongRef.go`

- 📄 `api/atproto/repouploadBlob.go`

- 📄 `api/atproto/serveractivateAccount.go`

- 📄 `api/atproto/servercheckAccountStatus.go`

- 📄 `api/atproto/serverconfirmEmail.go`

- 📄 `api/atproto/servercreateAccount.go`

- 📄 `api/atproto/servercreateAppPassword.go`

- 📄 `api/atproto/servercreateInviteCode.go`

- 📄 `api/atproto/servercreateInviteCodes.go`

- 📄 `api/atproto/servercreateSession.go`

- 📄 `api/atproto/serverdeactivateAccount.go`

- 📄 `api/atproto/serverdeleteAccount.go`

- 📄 `api/atproto/serverdeleteSession.go`

- 📄 `api/atproto/serverdescribeServer.go`

- 📄 `api/atproto/servergetAccountInviteCodes.go`

- 📄 `api/atproto/servergetServiceAuth.go`

- 📄 `api/atproto/servergetSession.go`

- 📄 `api/atproto/serverlistAppPasswords.go`

- 📄 `api/atproto/serverrefreshSession.go`

- 📄 `api/atproto/serverrequestAccountDelete.go`

- 📄 `api/atproto/serverrequestEmailConfirmation.go`

- 📄 `api/atproto/serverrequestEmailUpdate.go`

- 📄 `api/atproto/serverrequestPasswordReset.go`

- 📄 `api/atproto/serverreserveSigningKey.go`

- 📄 `api/atproto/serverresetPassword.go`

- 📄 `api/atproto/serverrevokeAppPassword.go`

- 📄 `api/atproto/serverupdateEmail.go`

- 📄 `api/atproto/syncgetBlob.go`

- 📄 `api/atproto/syncgetBlocks.go`

- 📄 `api/atproto/syncgetCheckout.go`

- 📄 `api/atproto/syncgetHead.go`

- 📄 `api/atproto/syncgetHostStatus.go`

- 📄 `api/atproto/syncgetLatestCommit.go`

- 📄 `api/atproto/syncgetRecord.go`

- 📄 `api/atproto/syncgetRepo.go`

- 📄 `api/atproto/syncgetRepoStatus.go`

- 📄 `api/atproto/synclistBlobs.go`

- 📄 `api/atproto/synclistHosts.go`

- 📄 `api/atproto/synclistRepos.go`

- 📄 `api/atproto/synclistReposByCollection.go`

- 📄 `api/atproto/syncnotifyOfUpdate.go`

- 📄 `api/atproto/syncrequestCrawl.go`

- 📄 `api/atproto/syncsubscribeRepos.go`

- 📄 `api/atproto/tempaddReservedHandle.go`

- 📄 `api/atproto/tempcheckHandleAvailability.go`

- 📄 `api/atproto/tempcheckSignupQueue.go`

- 📄 `api/atproto/tempdereferenceScope.go`

- 📄 `api/atproto/tempfetchLabels.go`

- 📄 `api/atproto/temprequestPhoneVerification.go`

- 📄 `api/atproto/temprevokeAccountCredentials.go`

- 📄 `api/bsky/actordefs.go`

- 📄 `api/bsky/actorgetPreferences.go`

- 📄 `api/bsky/actorgetProfile.go`

- 📄 `api/bsky/actorgetProfiles.go`

- 📄 `api/bsky/actorgetSuggestions.go`

- 📄 `api/bsky/actorprofile.go`

- 📄 `api/bsky/actorputPreferences.go`

- 📄 `api/bsky/actorsearchActors.go`

- 📄 `api/bsky/actorsearchActorsTypeahead.go`

- 📄 `api/bsky/actorstatus.go`

- 📄 `api/bsky/ageassurancebegin.go`

- 📄 `api/bsky/ageassurancedefs.go`

- 📄 `api/bsky/ageassurancegetConfig.go`

- 📄 `api/bsky/ageassurancegetState.go`

- 📄 `api/bsky/bookmarkcreateBookmark.go`

- 📄 `api/bsky/bookmarkdefs.go`

- 📄 `api/bsky/bookmarkdeleteBookmark.go`

- 📄 `api/bsky/bookmarkgetBookmarks.go`

- 📄 `api/bsky/cbor_gen.go`

- 📄 `api/bsky/contactdismissMatch.go`

- 📄 `api/bsky/contactgetMatches.go`

- 📄 `api/bsky/contactgetSyncStatus.go`

- 📄 `api/bsky/contactimportContacts.go`

- 📄 `api/bsky/contactremoveData.go`

- 📄 `api/bsky/contactsendNotification.go`

- 📄 `api/bsky/contactstartPhoneVerification.go`

- 📄 `api/bsky/contactverifyPhone.go`

- 📄 `api/bsky/draftcreateDraft.go`

- 📄 `api/bsky/draftdefs.go`

- 📄 `api/bsky/draftdeleteDraft.go`

- 📄 `api/bsky/draftgetDrafts.go`

- 📄 `api/bsky/draftupdateDraft.go`

- 📄 `api/bsky/embedexternal.go`

- 📄 `api/bsky/embedimages.go`

- 📄 `api/bsky/embedrecord.go`

- 📄 `api/bsky/embedrecordWithMedia.go`

- 📄 `api/bsky/embedvideo.go`

- 📄 `api/bsky/feeddefs.go`

- 📄 `api/bsky/feeddescribeFeedGenerator.go`

- 📄 `api/bsky/feedgenerator.go`

- 📄 `api/bsky/feedgetActorFeeds.go`

- 📄 `api/bsky/feedgetActorLikes.go`

- 📄 `api/bsky/feedgetAuthorFeed.go`

- 📄 `api/bsky/feedgetFeed.go`

- 📄 `api/bsky/feedgetFeedGenerator.go`

- 📄 `api/bsky/feedgetFeedGenerators.go`

- 📄 `api/bsky/feedgetFeedSkeleton.go`

- 📄 `api/bsky/feedgetLikes.go`

- 📄 `api/bsky/feedgetListFeed.go`

- 📄 `api/bsky/feedgetPostThread.go`

- 📄 `api/bsky/feedgetPosts.go`

- 📄 `api/bsky/feedgetQuotes.go`

- 📄 `api/bsky/feedgetRepostedBy.go`

- 📄 `api/bsky/feedgetSuggestedFeeds.go`

- 📄 `api/bsky/feedgetTimeline.go`

- 📄 `api/bsky/feedlike.go`

- 📄 `api/bsky/feedpost.go`

- 📄 `api/bsky/feedpostgate.go`

- 📄 `api/bsky/feedrepost.go`

- 📄 `api/bsky/feedsearchPosts.go`

- 📄 `api/bsky/feedsendInteractions.go`

- 📄 `api/bsky/feedthreadgate.go`

- 📄 `api/bsky/graphblock.go`

- 📄 `api/bsky/graphdefs.go`

- 📄 `api/bsky/graphfollow.go`

- 📄 `api/bsky/graphgetActorStarterPacks.go`

- 📄 `api/bsky/graphgetBlocks.go`

- 📄 `api/bsky/graphgetFollowers.go`

- 📄 `api/bsky/graphgetFollows.go`

- 📄 `api/bsky/graphgetKnownFollowers.go`

- 📄 `api/bsky/graphgetList.go`

- 📄 `api/bsky/graphgetListBlocks.go`

- 📄 `api/bsky/graphgetListMutes.go`

- 📄 `api/bsky/graphgetLists.go`

- 📄 `api/bsky/graphgetListsWithMembership.go`

- 📄 `api/bsky/graphgetMutes.go`

- 📄 `api/bsky/graphgetRelationships.go`

- 📄 `api/bsky/graphgetStarterPack.go`

- 📄 `api/bsky/graphgetStarterPacks.go`

- 📄 `api/bsky/graphgetStarterPacksWithMembership.go`

- 📄 `api/bsky/graphgetSuggestedFollowsByActor.go`

- 📄 `api/bsky/graphlist.go`

- 📄 `api/bsky/graphlistblock.go`

- 📄 `api/bsky/graphlistitem.go`

- 📄 `api/bsky/graphmuteActor.go`

- 📄 `api/bsky/graphmuteActorList.go`

- 📄 `api/bsky/graphmuteThread.go`

- 📄 `api/bsky/graphsearchStarterPacks.go`

- 📄 `api/bsky/graphstarterpack.go`

- 📄 `api/bsky/graphunmuteActor.go`

- 📄 `api/bsky/graphunmuteActorList.go`

- 📄 `api/bsky/graphunmuteThread.go`

- 📄 `api/bsky/graphverification.go`

- 📄 `api/bsky/labelergetServices.go`

- 📄 `api/bsky/labelerservice.go`

- 📄 `api/bsky/notificationdeclaration.go`

- 📄 `api/bsky/notificationgetPreferences.go`

- 📄 `api/bsky/notificationgetUnreadCount.go`

- 📄 `api/bsky/notificationlistActivitySubscriptions.go`

- 📄 `api/bsky/notificationlistNotifications.go`

- 📄 `api/bsky/notificationputActivitySubscription.go`

- 📄 `api/bsky/notificationputPreferences.go`

- 📄 `api/bsky/notificationputPreferencesV2.go`

- 📄 `api/bsky/notificationregisterPush.go`

- 📄 `api/bsky/notificationunregisterPush.go`

- 📄 `api/bsky/notificationupdateSeen.go`

- 📄 `api/bsky/richtextfacet.go`

- 📄 `api/bsky/unspeccedgetAgeAssuranceState.go`

- 📄 `api/bsky/unspeccedgetConfig.go`

- 📄 `api/bsky/unspeccedgetOnboardingSuggestedStarterPacks.go`

- 📄 `api/bsky/unspeccedgetOnboardingSuggestedStarterPacksSkeleton.go`

- 📄 `api/bsky/unspeccedgetPopularFeedGenerators.go`

- 📄 `api/bsky/unspeccedgetPostThreadOtherV2.go`

- 📄 `api/bsky/unspeccedgetPostThreadV2.go`

- 📄 `api/bsky/unspeccedgetSuggestedFeeds.go`

- 📄 `api/bsky/unspeccedgetSuggestedFeedsSkeleton.go`

- 📄 `api/bsky/unspeccedgetSuggestedStarterPacks.go`

- 📄 `api/bsky/unspeccedgetSuggestedStarterPacksSkeleton.go`

- 📄 `api/bsky/unspeccedgetSuggestedUsers.go`

- 📄 `api/bsky/unspeccedgetSuggestedUsersSkeleton.go`

- 📄 `api/bsky/unspeccedgetSuggestionsSkeleton.go`

- 📄 `api/bsky/unspeccedgetTaggedSuggestions.go`

- 📄 `api/bsky/unspeccedgetTrendingTopics.go`

- 📄 `api/bsky/unspeccedgetTrends.go`

- 📄 `api/bsky/unspeccedgetTrendsSkeleton.go`

- 📄 `api/bsky/unspeccedinitAgeAssurance.go`

- 📄 `api/bsky/unspeccedsearchActorsSkeleton.go`

- 📄 `api/bsky/unspeccedsearchPostsSkeleton.go`

- 📄 `api/bsky/unspeccedsearchStarterPacksSkeleton.go`

- 📄 `api/bsky/videodefs.go`

- 📄 `api/bsky/videogetJobStatus.go`

- 📄 `api/bsky/videogetUploadLimits.go`

- 📄 `api/bsky/videouploadVideo.go`

- 📄 `api/chat/actordeclaration.go`

- 📄 `api/chat/actordeleteAccount.go`

- 📄 `api/chat/actorexportAccountData.go`

- 📄 `api/chat/convoacceptConvo.go`

- 📄 `api/chat/convoaddReaction.go`

- 📄 `api/chat/convodefs.go`

- 📄 `api/chat/convodeleteMessageForSelf.go`

- 📄 `api/chat/convogetConvo.go`

- 📄 `api/chat/convogetConvoAvailability.go`

- 📄 `api/chat/convogetConvoForMembers.go`

- 📄 `api/chat/convogetLog.go`

- 📄 `api/chat/convogetMessages.go`

- 📄 `api/chat/convoleaveConvo.go`

- 📄 `api/chat/convolistConvos.go`

- 📄 `api/chat/convomuteConvo.go`

- 📄 `api/chat/convoremoveReaction.go`

- 📄 `api/chat/convosendMessage.go`

- 📄 `api/chat/convosendMessageBatch.go`

- 📄 `api/chat/convounmuteConvo.go`

- 📄 `api/chat/convoupdateAllRead.go`

- 📄 `api/chat/convoupdateRead.go`

- 📄 `api/chat/moderationgetActorMetadata.go`

- 📄 `api/chat/moderationgetMessageContext.go`

- 📄 `api/chat/moderationupdateActorAccess.go`

- 📄 `api/ozone/communicationcreateTemplate.go`

- 📄 `api/ozone/communicationdeleteTemplate.go`

- 📄 `api/ozone/communicationlistTemplates.go`

- 📄 `api/ozone/communicationupdateTemplate.go`

- 📄 `api/ozone/hostinggetAccountHistory.go`

- 📄 `api/ozone/moderationcancelScheduledActions.go`

- 📄 `api/ozone/moderationdefs.go`

- 📄 `api/ozone/moderationemitEvent.go`

- 📄 `api/ozone/moderationgetAccountTimeline.go`

- 📄 `api/ozone/moderationgetEvent.go`

- 📄 `api/ozone/moderationgetRecord.go`

- 📄 `api/ozone/moderationgetRecords.go`

- 📄 `api/ozone/moderationgetRepo.go`

- 📄 `api/ozone/moderationgetReporterStats.go`

- 📄 `api/ozone/moderationgetRepos.go`

- 📄 `api/ozone/moderationgetSubjects.go`

- 📄 `api/ozone/moderationlistScheduledActions.go`

- 📄 `api/ozone/moderationqueryEvents.go`

- 📄 `api/ozone/moderationqueryStatuses.go`

- 📄 `api/ozone/moderationscheduleAction.go`

- 📄 `api/ozone/moderationsearchRepos.go`

- 📄 `api/ozone/safelinkaddRule.go`

- 📄 `api/ozone/safelinkqueryEvents.go`

- 📄 `api/ozone/safelinkqueryRules.go`

- 📄 `api/ozone/safelinkremoveRule.go`

- 📄 `api/ozone/safelinkupdateRule.go`

- 📄 `api/ozone/servergetConfig.go`

- 📄 `api/ozone/setaddValues.go`

- 📄 `api/ozone/setdeleteSet.go`

- 📄 `api/ozone/setdeleteValues.go`

- 📄 `api/ozone/setgetValues.go`

- 📄 `api/ozone/setquerySets.go`

- 📄 `api/ozone/settingdefs.go`

- 📄 `api/ozone/settinglistOptions.go`

- 📄 `api/ozone/settingremoveOptions.go`

- 📄 `api/ozone/settingupsertOption.go`

- 📄 `api/ozone/setupsertSet.go`

- 📄 `api/ozone/signaturefindCorrelation.go`

- 📄 `api/ozone/signaturefindRelatedAccounts.go`

- 📄 `api/ozone/signaturesearchAccounts.go`

- 📄 `api/ozone/teamaddMember.go`

- 📄 `api/ozone/teamdeleteMember.go`

- 📄 `api/ozone/teamlistMembers.go`

- 📄 `api/ozone/teamupdateMember.go`

- 📄 `api/ozone/verificationdefs.go`

- 📄 `api/ozone/verificationgrantVerifications.go`

- 📄 `api/ozone/verificationlistVerifications.go`

- 📄 `api/ozone/verificationrevokeVerifications.go`

- 📄 `automod/consumer/firehose.go`

- 📄 `automod/engine/blobs.go`

- 📄 `automod/engine/ruleset.go`

- 📄 `automod/engine/ruletypes.go`

- 📄 `automod/rules/blobs.go`

- 📄 `automod/visual/abyss_api.go`

- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/abyss_rule.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `automod/visual/hiveai_rule.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/relay/stream/events.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/events.go`

- 📄 `fakedata/generators.go`

- 📄 `gen/main.go`

- 📄 `repo/repo.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/firehose.go`



### Определения локальных типов (best effort)


#### BlobSchema (struct)


*Определено в: `lex/util/lex_types.go:152`*


| Поле | Тип | JSON |

|------|-----|------|

| `LexiconTypeID` | `string` | `$type` |

| `Ref` | `LexLink` | `ref` |

| `MimeType` | `string` | `mimeType` |

| `Size` | `int64` | `size` |



#### CborChecker (struct)


*Определено в: `lex/util/util.go:23`*


| Поле | Тип | JSON |

|------|-----|------|

| `Type` | `string` | `$type` |



#### LegacyBlob (struct)


*Определено в: `lex/util/lex_types.go:147`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cid` | `string` | `cid` |

| `MimeType` | `string` | `mimeType` |



#### LexBlob (struct)


*Определено в: `lex/util/lex_types.go:141`*


| Поле | Тип | JSON |

|------|-----|------|

| `Ref` | `LexLink` | `Ref` |

| `MimeType` | `string` | `MimeType` |

| `Size` | `int64` | `Size` |



#### LexLink (type)


*Определено в: `lex/util/lex_types.go:21`*


```go

cid.Cid

```


#### LexiconTypeDecoder (struct)


*Определено в: `lex/util/decoder.go:96`*


| Поле | Тип | JSON |

|------|-----|------|

| `Val` | `unknown` | `Val` |




---


[import] path: github.com/bluesky-social/indigo/models type: local


### github.com/bluesky-social/indigo/models


- **Тип:** local

- **Алиасы:** `models`

- **Локальная директория пакета:** `models`



### Вызовы


`Uid`


### Кандидаты на типы


`DbCID`


### Селекторы (любое использование `pkg.X`)


`ActorInfo`, `DbCID`, `Uid`


### Используется в файлах


- 📄 `carstore/bs.go`

- 📄 `carstore/last_shard_cache.go`

- 📄 `carstore/meta_gorm.go`

- 📄 `carstore/nonarchive.go`

- 📄 `carstore/scylla.go`

- 📄 `carstore/sqlite_store.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `events/diskpersist/diskpersist.go`

- 📄 `events/events.go`

- 📄 `events/pebblepersist/pebblepersist.go`

- 📄 `events/persist.go`

- 📄 `events/yolopersist/yolopersist.go`

- 📄 `repomgr/repomgr.go`

- 📄 `splitter/ringbuf.go`

- 📄 `testing/pdsmodels/types.go`



### Определения локальных типов (best effort)


#### DbCID (struct)


*Определено в: `models/dbcid.go:12`*


| Поле | Тип | JSON |

|------|-----|------|

| `CID` | `unknown` | `CID` |




---


[import] path: github.com/bluesky-social/indigo/mst type: local


### github.com/bluesky-social/indigo/mst


- **Тип:** local

- **Алиасы:** `mst`

- **Локальная директория пакета:** `mst`



### Вызовы


`CBORTypes`, `DiffTrees`, `Get`, `LoadMST`, `NewEmptyMST`


### Кандидаты на типы


`DiffOp`, `MerkleSearchTree`


### Селекторы (любое использование `pkg.X`)


`Add`, `CBORTypes`, `DiffOp`, `DiffTrees`, `Get`, `LoadMST`, `MerkleSearchTree`, `NewEmptyMST`


### Используется в файлах


- 📄 `gen/main.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/repomgr.go`



### Определения локальных типов (best effort)


#### DiffOp (struct)


*Определено в: `mst/diff.go:12`*


| Поле | Тип | JSON |

|------|-----|------|

| `Depth` | `int` | `Depth` |

| `Op` | `string` | `Op` |

| `Rpath` | `string` | `Rpath` |

| `OldCid` | `unknown` | `OldCid` |

| `NewCid` | `unknown` | `NewCid` |



#### MerkleSearchTree (struct)


*Определено в: `mst/mst.go:134`*


| Поле | Тип | JSON |

|------|-----|------|

| `cst` | `unknown` | `cst` |

| `entries` | `[]nodeEntry` | `entries` |

| `layer` | `int` | `layer` |

| `pointer` | `unknown` | `pointer` |

| `validPtr` | `bool` | `validPtr` |




---


[import] path: github.com/bluesky-social/indigo/repo type: local


### github.com/bluesky-social/indigo/repo


- **Тип:** local

- **Алиасы:** `repo`

- **Локальная директория пакета:** `repo`



### Вызовы


`NewRepo`, `OpenRepo`, `ReadRepoFromCar`, `StreamRepoRecords`


### Кандидаты на типы


`Repo`, `SignedCommit`, `UnsignedCommit`


### Селекторы (любое использование `pkg.X`)


`Did`, `ErrDoneIterating`, `NewRepo`, `OpenRepo`, `ReadRepoFromCar`, `Repo`, `SignedCommit`, `StreamRepoRecords`, `UnsignedCommit`


### Используется в файлах


- 📄 `automod/consumer/firehose.go`

- 📄 `backfill/backfill.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/gosky/car.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/netsync/main.go`

- 📄 `cmd/sonar/sonar.go`

- 📄 `cmd/stress/main.go`

- 📄 `gen/main.go`

- 📄 `repomgr/repomgr.go`

- 📄 `search/firehose.go`

- 📄 `testing/utils.go`



### Определения локальных типов (best effort)


#### Repo (struct)


*Определено в: `repo/repo.go:45`*


| Поле | Тип | JSON |

|------|-----|------|

| `sc` | `SignedCommit` | `sc` |

| `cst` | `unknown` | `cst` |

| `bs` | `unknown` | `bs` |

| `repoCid` | `unknown` | `repoCid` |

| `mst` | `*mst.MerkleSearchTree` | `mst` |

| `dirty` | `bool` | `dirty` |

| `clk` | `*syntax.TIDClock` | `clk` |



#### SignedCommit (struct)


*Определено в: `repo/repo.go:28`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `did` |

| `Version` | `int64` | `version` |

| `Prev` | `*cid.Cid` | `prev` |

| `Data` | `unknown` | `data` |

| `Sig` | `[]byte` | `sig` |

| `Rev` | `string` | `rev` |



#### UnsignedCommit (struct)


*Определено в: `repo/repo.go:37`*


| Поле | Тип | JSON |

|------|-----|------|

| `Did` | `string` | `Did` |

| `Version` | `int64` | `Version` |

| `Prev` | `*cid.Cid` | `Prev` |

| `Data` | `unknown` | `Data` |

| `Rev` | `string` | `Rev` |




---


[import] path: github.com/bluesky-social/indigo/repo/carutil type: local


### github.com/bluesky-social/indigo/repo/carutil


- **Тип:** local

- **Алиасы:** `carutil`

- **Локальная директория пакета:** `repo/carutil`



### Вызовы


`NewReader`


### Кандидаты на типы


`BasicBlock`, `Reader`


### Селекторы (любое использование `pkg.X`)


`BasicBlock`, `NewReader`, `Reader`


### Используется в файлах


- 📄 `repo/repo.go`

- 📄 `repo/stream.go`



### Определения локальных типов (best effort)


#### BasicBlock (struct)


*Определено в: `repo/carutil/reader.go:99`*


| Поле | Тип | JSON |

|------|-----|------|

| `cid` | `unknown` | `cid` |

| `data` | `[]byte` | `data` |

| `base` | `[]byte` | `base` |



#### Reader (struct)


*Определено в: `repo/carutil/reader.go:14`*


| Поле | Тип | JSON |

|------|-----|------|

| `r` | `*bufio.Reader` | `r` |




---


[import] path: github.com/bluesky-social/indigo/repomgr type: local


### github.com/bluesky-social/indigo/repomgr


- **Тип:** local

- **Алиасы:** `repomgr`

- **Локальная директория пакета:** `repomgr`



### Вызовы


`EventKind`


### Селекторы (любое использование `pkg.X`)


`EventKind`, `EvtKindCreateRecord`, `EvtKindDeleteRecord`, `EvtKindUpdateRecord`


### Используется в файлах


- 📄 `automod/consumer/firehose.go`

- 📄 `backfill/backfill.go`

- 📄 `backfill/gormstore.go`

- 📄 `backfill/memstore.go`

- 📄 `cmd/beemo/firehose_consumer.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/sonar/sonar.go`




---


[import] path: github.com/bluesky-social/indigo/search type: local


### github.com/bluesky-social/indigo/search


- **Тип:** local

- **Алиасы:** `search`

- **Локальная директория пакета:** `search`



### Вызовы


`DoSearchPosts`, `DoSearchProfiles`, `DoSearchProfilesTypeahead`, `NewIndexer`, `NewServer`


### Кандидаты на типы


`ActorSearchParams`, `EsSearchResponse`, `IndexerConfig`, `PostSearchParams`, `ServerConfig`


### Селекторы (любое использование `pkg.X`)


`ActorSearchParams`, `DoSearchPosts`, `DoSearchProfiles`, `DoSearchProfilesTypeahead`, `EsSearchResponse`, `IndexerConfig`, `NewIndexer`, `NewServer`, `PostSearchParams`, `ServerConfig`, `db`


### Используется в файлах


- 📄 `cmd/palomar/main.go`



### Определения локальных типов (best effort)


#### ActorSearchParams (struct)


*Определено в: `search/query.go:69`*


| Поле | Тип | JSON |

|------|-----|------|

| `Query` | `string` | `Query` |

| `Typeahead` | `bool` | `Typeahead` |

| `Follows` | `[]syntax.DID` | `Follows` |

| `Viewer` | `*syntax.DID` | `Viewer` |

| `Offset` | `int` | `Offset` |

| `Size` | `int` | `Size` |



#### EsSearchResponse (struct)


*Определено в: `search/query.go:35`*


| Поле | Тип | JSON |

|------|-----|------|

| `Took` | `int` | `Took` |

| `TimedOut` | `bool` | `TimedOut` |

| `Hits` | `EsSearchHits` | `Hits` |



#### IndexerConfig (struct)


*Определено в: `search/indexing.go:52`*


| Поле | Тип | JSON |

|------|-----|------|

| `RelayHost` | `string` | `RelayHost` |

| `ProfileIndex` | `string` | `ProfileIndex` |

| `PostIndex` | `string` | `PostIndex` |

| `Logger` | `*slog.Logger` | `Logger` |

| `RelaySyncRateLimit` | `int` | `RelaySyncRateLimit` |

| `IndexMaxConcurrency` | `int` | `IndexMaxConcurrency` |

| `DiscoverRepos` | `bool` | `DiscoverRepos` |

| `IndexingRateLimit` | `int` | `IndexingRateLimit` |



#### PostSearchParams (struct)


*Определено в: `search/query.go:53`*


| Поле | Тип | JSON |

|------|-----|------|

| `Query` | `string` | `Query` |

| `Sort` | `string` | `Sort` |

| `Author` | `*syntax.DID` | `Author` |

| `Since` | `*syntax.Datetime` | `Since` |

| `Until` | `*syntax.Datetime` | `Until` |

| `Mentions` | `*syntax.DID` | `Mentions` |

| `Lang` | `*syntax.Language` | `Lang` |

| `Domain` | `string` | `Domain` |

| `URL` | `string` | `URL` |

| `Tags` | `[]string` | `Tags` |

| `Viewer` | `*syntax.DID` | `Viewer` |

| `Offset` | `int` | `Offset` |

| `Size` | `int` | `Size` |



#### ServerConfig (struct)


*Определено в: `search/server.go:30`*


| Поле | Тип | JSON |

|------|-----|------|

| `Logger` | `*slog.Logger` | `Logger` |

| `ProfileIndex` | `string` | `ProfileIndex` |

| `PostIndex` | `string` | `PostIndex` |

| `AtlantisAddresses` | `[]string` | `AtlantisAddresses` |




---


[import] path: github.com/bluesky-social/indigo/splitter type: local


### github.com/bluesky-social/indigo/splitter


- **Тип:** local

- **Алиасы:** `splitter`

- **Локальная директория пакета:** `splitter`



### Вызовы


`NewSplitter`


### Кандидаты на типы


`Splitter`, `SplitterConfig`


### Селекторы (любое использование `pkg.X`)


`NewSplitter`, `Splitter`, `SplitterConfig`


### Используется в файлах


- 📄 `cmd/rainbow/main.go`



### Определения локальных типов (best effort)


#### Splitter (struct)


*Определено в: `splitter/splitter.go:31`*


| Поле | Тип | JSON |

|------|-----|------|

| `erb` | `*EventRingBuffer` | `erb` |

| `pp` | `*pebblepersist.PebblePersist` | `pp` |

| `events` | `*events.EventManager` | `events` |

| `consumersLk` | `unknown` | `consumersLk` |

| `nextConsumerID` | `uint64` | `nextConsumerID` |

| `consumers` | `map[uint64]*SocketConsumer` | `consumers` |

| `conf` | `SplitterConfig` | `conf` |

| `logger` | `*slog.Logger` | `logger` |

| `upstreamClient` | `*http.Client` | `upstreamClient` |

| `peerClient` | `*http.Client` | `peerClient` |

| `nextCrawlers` | `[]url.URL` | `nextCrawlers` |



#### SplitterConfig (struct)


*Определено в: `splitter/splitter.go:50`*


| Поле | Тип | JSON |

|------|-----|------|

| `UpstreamHost` | `string` | `UpstreamHost` |

| `CollectionDirHost` | `string` | `CollectionDirHost` |

| `CursorFile` | `string` | `CursorFile` |

| `UserAgent` | `string` | `UserAgent` |

| `PebbleOptions` | `*pebblepersist.PebblePersistOptions` | `PebbleOptions` |

| `Logger` | `*slog.Logger` | `Logger` |




---


[import] path: github.com/bluesky-social/indigo/testing type: local


### github.com/bluesky-social/indigo/testing


- **Тип:** local

- **Алиасы:** `testing`

- **Локальная директория пакета:** `testing`



### Вызовы


`GenerateFakeRepo`


### Селекторы (любое использование `pkg.X`)


`GenerateFakeRepo`


### Используется в файлах


- 📄 `cmd/stress/main.go`




---


[import] path: github.com/bluesky-social/indigo/util type: local


### github.com/bluesky-social/indigo/util


- **Тип:** local

- **Алиасы:** `bsutil`, `util`

- **Локальная директория пакета:** `util`



### Вызовы


`CborStore`, `NewLoggingBstore`, `ParseAtUri`, `RobustHTTPClient`


### Кандидаты на типы


`FakeKeyManager`, `RobustHTTPClient`


### Селекторы (любое использование `pkg.X`)


`CborStore`, `FakeKeyManager`, `ISO8601`, `NewLoggingBstore`, `ParseAtUri`, `RobustHTTPClient`


### Используется в файлах


- 📄 `automod/visual/abyss_client.go`

- 📄 `automod/visual/hiveai_client.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/beemo/slack.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/hepa/server.go`

- 📄 `events/dbpersist/dbpersist.go`

- 📄 `fakedata/accounts.go`

- 📄 `mst/diff.go`

- 📄 `repo/repo.go`

- 📄 `repo/stream.go`

- 📄 `repomgr/repomgr.go`

- 📄 `splitter/splitter.go`

- 📄 `testing/utils.go`

- 📄 `xrpc/xrpc.go`



### Определения локальных типов (best effort)


#### FakeKeyManager (struct)


*Определено в: `util/fakekey.go:5`*



---


[import] path: github.com/bluesky-social/indigo/util/cliutil type: local


### github.com/bluesky-social/indigo/util/cliutil


- **Тип:** local

- **Алиасы:** `cliutil`

- **Локальная директория пакета:** `util/cliutil`



### Вызовы


`GetXrpcClient`, `LoadKeyFromFile`, `NewHttpClient`, `ReadAuth`, `SetupDatabase`


### Селекторы (любое использование `pkg.X`)


`GetXrpcClient`, `LoadKeyFromFile`, `NewHttpClient`, `ReadAuth`, `SetupDatabase`


### Используется в файлах


- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/account.go`

- 📄 `cmd/gosky/admin.go`

- 📄 `cmd/gosky/bsky.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/did.go`

- 📄 `cmd/gosky/handle.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/palomar/main.go`

- 📄 `cmd/relay/main.go`

- 📄 `cmd/relay/pull.go`

- 📄 `cmd/relay/testing/runner.go`

- 📄 `cmd/stress/main.go`




---


[import] path: github.com/bluesky-social/indigo/util/labels type: local


### github.com/bluesky-social/indigo/util/labels


- **Тип:** local

- **Алиасы:** `labels`

- **Локальная директория пакета:** `util/labels`



### Кандидаты на типы


`UnsignedLabel`


### Селекторы (любое использование `pkg.X`)


`UnsignedLabel`


### Используется в файлах


- 📄 `gen/main.go`



### Определения локальных типов (best effort)


#### UnsignedLabel (struct)


*Определено в: `util/labels/labels.go:10`*


| Поле | Тип | JSON |

|------|-----|------|

| `Cid` | `*string` | `cid` |

| `Cts` | `string` | `cts` |

| `Exp` | `*string` | `exp` |

| `Neg` | `*bool` | `neg` |

| `Src` | `string` | `src` |

| `Uri` | `string` | `uri` |

| `Val` | `string` | `val` |

| `Ver` | `*int64` | `ver` |




---


[import] path: github.com/bluesky-social/indigo/util/ssrf type: local


### github.com/bluesky-social/indigo/util/ssrf


- **Тип:** local

- **Алиасы:** `ssrf`

- **Локальная директория пакета:** `util/ssrf`



### Вызовы


`PublicOnlyDialer`, `PublicOnlyTransport`


### Селекторы (любое использование `pkg.X`)


`PublicOnlyDialer`, `PublicOnlyTransport`


### Используется в файлах


- 📄 `atproto/auth/oauth/resolver.go`

- 📄 `cmd/relay/relay/host_checker.go`

- 📄 `cmd/relay/relay/slurper.go`




---


[import] path: github.com/bluesky-social/indigo/util/svcutil type: local


### github.com/bluesky-social/indigo/util/svcutil


- **Тип:** local

- **Алиасы:** `svcutil`

- **Локальная директория пакета:** `util/svcutil`



### Вызовы


`ConfigLogger`


### Селекторы (любое использование `pkg.X`)


`ConfigLogger`, `MetricsMiddleware`


### Используется в файлах


- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/rainbow/main.go`

- 📄 `cmd/relay/service.go`

- 📄 `splitter/splitter.go`




---


[import] path: github.com/bluesky-social/indigo/xrpc type: local


### github.com/bluesky-social/indigo/xrpc


- **Тип:** local

- **Алиасы:** `xrpc`

- **Локальная директория пакета:** `xrpc`



### Кандидаты на типы


`AuthInfo`, `Client`, `Error`, `XRPCError`


### Селекторы (любое использование `pkg.X`)


`AuthInfo`, `Client`, `Error`, `XRPCError`


### Используется в файлах


- 📄 `automod/capture/fetch.go`

- 📄 `automod/consumer/ozone.go`

- 📄 `automod/engine/engine.go`

- 📄 `automod/engine/fetch_account_meta.go`

- 📄 `automod/engine/persisthelpers.go`

- 📄 `cmd/beemo/notify_reports.go`

- 📄 `cmd/collectiondir/crawl.go`

- 📄 `cmd/collectiondir/serve.go`

- 📄 `cmd/fakermaker/main.go`

- 📄 `cmd/gosky/bgs.go`

- 📄 `cmd/gosky/debug.go`

- 📄 `cmd/gosky/main.go`

- 📄 `cmd/gosky/sync.go`

- 📄 `cmd/hepa/server.go`

- 📄 `cmd/stress/main.go`

- 📄 `fakedata/accounts.go`

- 📄 `fakedata/generators.go`

- 📄 `models/models.go`

- 📄 `search/indexing.go`

- 📄 `splitter/handlers.go`

- 📄 `util/cliutil/util.go`



### Определения локальных типов (best effort)


#### AuthInfo (struct)


*Определено в: `xrpc/xrpc.go:43`*


| Поле | Тип | JSON |

|------|-----|------|

| `AccessJwt` | `string` | `AccessJwt` |

| `RefreshJwt` | `string` | `RefreshJwt` |

| `Handle` | `string` | `Handle` |

| `Did` | `string` | `Did` |



#### Client (struct)


*Определено в: `xrpc/xrpc.go:21`*


| Поле | Тип | JSON |

|------|-----|------|

| `Client` | `*http.Client` | `Client` |

| `Auth` | `*AuthInfo` | `Auth` |

| `AdminToken` | `*string` | `AdminToken` |

| `Host` | `string` | `Host` |

| `UserAgent` | `*string` | `UserAgent` |

| `Headers` | `map[string]string` | `Headers` |



#### Error (struct)


*Определено в: `xrpc/xrpc.go:59`*


| Поле | Тип | JSON |

|------|-----|------|

| `StatusCode` | `int` | `StatusCode` |

| `Wrapped` | `error` | `Wrapped` |

| `Ratelimit` | `*RatelimitInfo` | `Ratelimit` |



#### XRPCError (struct)


*Определено в: `xrpc/xrpc.go:50`*


| Поле | Тип | JSON |

|------|-----|------|

| `ErrStr` | `string` | `ErrStr` |

| `Message` | `string` | `Message` |




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

