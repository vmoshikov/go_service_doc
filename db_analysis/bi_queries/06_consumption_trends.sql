-- =============================================================================
-- Дашборд: Тренды потребления
-- =============================================================================

-- Q1: Line — cpu_total, ram_total, nod_total по дням (update_ts)
-- Chart: Line
SELECT DATE(update_ts) AS day,
       SUM(cpu_total) AS cpu_total,
       SUM(ram_total) AS ram_total,
       SUM(nod_total) AS nod_total,
       SUM(cpu_running) AS cpu_running,
       SUM(ram_running) AS ram_running,
       SUM(nod_running) AS nod_running
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY DATE(update_ts)
ORDER BY day;

-- Q2: Line — cpu_running / ram_running по кластерам (топ-5)
-- Chart: Line
SELECT short_name, update_ts, cpu_running, ram_running, nod_running
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
  AND short_name IN (
    SELECT short_name FROM state.cluster_consumption
    WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
    GROUP BY short_name
    ORDER BY SUM(cpu_running) DESC NULLS LAST
    LIMIT 5
  )
ORDER BY short_name, update_ts;

-- Q3: Area — Потребление по environment во времени
-- Chart: Area / Stacked Area
SELECT DATE(update_ts) AS day, environment,
       SUM(cpu_total) AS cpu_total,
       SUM(ram_total) AS ram_total,
       SUM(nod_total) AS nod_total
FROM state.cluster_consumption
WHERE update_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND update_ts < COALESCE(:period_end, now())
GROUP BY DATE(update_ts), environment
ORDER BY day, environment;
