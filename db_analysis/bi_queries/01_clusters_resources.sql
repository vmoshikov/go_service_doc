-- =============================================================================
-- Дашборд: Кластеры и ресурсы
-- =============================================================================

-- Q1: Bar — Распределение кластеров по версии K8s
-- Chart: Bar
SELECT k8s_version AS version, COUNT(*) AS cluster_count
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY k8s_version
ORDER BY cluster_count DESC
LIMIT 15;

-- Q2: Stacked Bar — CPU/RAM/NOD по cluster_type_code (total, running, other, error)
-- Chart: Stacked Bar
SELECT cluster_type_code,
       SUM(cpu_total) AS cpu_total,
       SUM(cpu_running) AS cpu_running,
       SUM(cpu_other) AS cpu_other,
       SUM(cpu_error) AS cpu_error,
       SUM(ram_total) AS ram_total,
       SUM(ram_running) AS ram_running,
       SUM(ram_other) AS ram_other,
       SUM(ram_error) AS ram_error,
       SUM(nod_total) AS nod_total,
       SUM(nod_running) AS nod_running,
       SUM(nod_other) AS nod_other,
       SUM(nod_error) AS nod_error
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY cluster_type_code;

-- Q3: Pie — Dedicated vs Shared (on_dedicated_resources)
-- Chart: Pie
SELECT COALESCE(on_dedicated_resources::text, 'unknown') AS resource_type, COUNT(*) AS node_count
FROM state.node_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY on_dedicated_resources;

-- Q4: Table — Топ кластеров по потреблению
-- Chart: Table
SELECT short_name, cpu_total, ram_total, nod_total, cpu_running, ram_running, nod_running
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
ORDER BY cpu_total DESC NULLS LAST
LIMIT 15;

-- Q5: Bar — Потребление по environment
-- Chart: Bar
SELECT environment, COUNT(*) AS cluster_count, SUM(cpu_total) AS cpu_total, SUM(ram_total) AS ram_total
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY environment
ORDER BY cluster_count DESC;
