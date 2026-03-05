-- =============================================================================
-- Дашборд: Успешные / неуспешные операции на временной шкале
-- =============================================================================

-- Stacked Bar — Успешные и неуспешные операции по дням
-- Chart: Stacked Bar
SELECT DATE(state_dt) AS day,
       SUM(CASE WHEN LOWER(state) IN ('success', 'completed', 'done') THEN 1 ELSE 0 END) AS success_count,
       SUM(CASE WHEN LOWER(state) NOT IN ('success', 'completed', 'done') OR state IS NULL THEN 1 ELSE 0 END) AS failed_count
FROM operation_v2.operations
WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
  AND state_dt < COALESCE(:period_end, now())
GROUP BY DATE(state_dt)
ORDER BY day;
