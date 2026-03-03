-- =============================================================================
-- Дашборд: Конфигурация
-- =============================================================================

-- Q1: Table — CR комбинации на кластер (resource_type + version)
-- Chart: Table
SELECT cluster_uid,
       STRING_AGG(DISTINCT resource_type || '@' || version, ', ' ORDER BY resource_type || '@' || version) AS cr_combinations
FROM conf.custom_resource
WHERE (deleted IS NULL OR deleted = false)
  AND modify_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND modify_ts < COALESCE(:period_end, now())
GROUP BY cluster_uid;

-- Q2: Bar — Топ комбинаций CR (частотный анализ)
-- Chart: Bar
SELECT resource_type || '@' || version AS combo, COUNT(DISTINCT cluster_uid) AS cluster_count
FROM conf.custom_resource
WHERE (deleted IS NULL OR deleted = false)
  AND modify_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND modify_ts < COALESCE(:period_end, now())
GROUP BY resource_type, version
ORDER BY cluster_count DESC
LIMIT 15;

-- Q3: Table — Операторная версионность: несовпадения operator.version vs cluster.operators_version
-- Chart: Table
SELECT o.name AS operator_name, o.version AS operator_version,
       c.operators_version AS cluster_version, o.cluster_uid
FROM state.operator o
JOIN conf.cluster c ON o.cluster_uid = c.uid
WHERE o.start_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND o.start_ts < COALESCE(:period_end, now())
  AND o.version IS DISTINCT FROM c.operators_version;

-- Q4: Table — Админы по кластерам
-- Chart: Table
SELECT cluster_uid, admins
FROM conf.admins
WHERE cluster_uid IS NOT NULL;
