-- =============================================================================
-- Дашборд: География
-- =============================================================================

-- Q1: Heatmap/Table — Region × Environment (количество кластеров)
-- Chart: Heatmap / Pivot Table
SELECT region, environment, COUNT(*) AS cluster_count
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY region, environment
ORDER BY region, environment;

-- Q2: Bar — Кластеры по geo_zone
-- Chart: Bar
SELECT geo_zone, COUNT(*) AS cluster_count
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY geo_zone
ORDER BY cluster_count DESC
LIMIT 15;

-- Q3: Bar — Узлы по region
-- Chart: Bar
SELECT region, COUNT(*) AS node_count
FROM state.node_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY region
ORDER BY node_count DESC
LIMIT 15;
