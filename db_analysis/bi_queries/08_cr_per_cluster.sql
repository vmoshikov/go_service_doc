-- =============================================================================
-- Дашборд: CR установленные на каждый кластер
-- =============================================================================

-- Q1: Table — CR по кластерам (список CR на каждый кластер)
-- Chart: Table
SELECT c.cluster_uid, cl.short_name, cl.name,
       STRING_AGG(DISTINCT c.resource_type || ' @ ' || c.version, ', ' ORDER BY c.resource_type || ' @ ' || c.version) AS cr_list,
       COUNT(DISTINCT c.resource_type) AS cr_count
FROM conf.custom_resource c
LEFT JOIN conf.cluster cl ON c.cluster_uid = cl.uid
WHERE (c.deleted IS NULL OR c.deleted = false)
  AND c.modify_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND c.modify_ts < COALESCE(:period_end, now())
GROUP BY c.cluster_uid, cl.short_name, cl.name;

-- Q2: Table — Установки CR: тип и версия → кластеры
-- Chart: Table
SELECT resource_type, version,
       COUNT(DISTINCT cluster_uid) AS cluster_count,
       STRING_AGG(DISTINCT cluster_uid::text, ', ' ORDER BY cluster_uid::text) AS clusters
FROM conf.custom_resource
WHERE (deleted IS NULL OR deleted = false)
  AND modify_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND modify_ts < COALESCE(:period_end, now())
GROUP BY resource_type, version
ORDER BY cluster_count DESC;
