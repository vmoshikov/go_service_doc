-- =============================================================================
-- Дашборд: Операции и SLO
-- =============================================================================

-- Q1: Pie — Распределение operations по state
-- Chart: Pie
SELECT state, COUNT(*) AS operation_count
FROM operation_v2.operations
WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
  AND state_dt < COALESCE(:period_end, now())
GROUP BY state
ORDER BY operation_count DESC;

-- Q2: Line — Success rate по дням (тренд)
-- Chart: Line
SELECT DATE(state_dt) AS day,
       COUNT(*) AS total,
       SUM(CASE WHEN LOWER(state) IN ('success', 'completed', 'done') THEN 1 ELSE 0 END) AS success_count,
       ROUND(100.0 * SUM(CASE WHEN LOWER(state) IN ('success', 'completed', 'done') THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS success_rate_pct
FROM operation_v2.operations
WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
  AND state_dt < COALESCE(:period_end, now())
GROUP BY DATE(state_dt)
ORDER BY day;

-- Q3: Bar — Среднее время выполнения по type операции (минуты)
-- Chart: Bar
SELECT type,
       COUNT(*) AS operation_count,
       ROUND(AVG(EXTRACT(EPOCH FROM (state_dt - create_dt)) / 60), 2) AS avg_duration_min
FROM operation_v2.operations
WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
  AND state_dt < COALESCE(:period_end, now())
  AND state_dt IS NOT NULL AND create_dt IS NOT NULL
GROUP BY type
ORDER BY avg_duration_min DESC NULLS LAST;

-- Q4: Table — Топ проблемных кластеров (failed count)
-- Chart: Table
SELECT cluster_id, COUNT(*) AS failed_count
FROM operation_v2.operations
WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
  AND state_dt < COALESCE(:period_end, now())
  AND (LOWER(state) LIKE '%fail%' OR LOWER(state) LIKE '%error%')
GROUP BY cluster_id
ORDER BY failed_count DESC
LIMIT 15;

-- Q5: Gauge/KPI — Общий % успешных операций
-- Chart: Gauge/KPI
SELECT ROUND(100.0 * SUM(CASE WHEN LOWER(state) IN ('success', 'completed', 'done') THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS success_rate_pct,
       COUNT(*) AS total_operations
FROM operation_v2.operations
WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
  AND state_dt < COALESCE(:period_end, now());
