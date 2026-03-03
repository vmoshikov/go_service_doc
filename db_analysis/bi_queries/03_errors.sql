-- =============================================================================
-- Дашборд: Ошибки
-- =============================================================================

-- Q1: Bar — Топ error_type (operations + tasks + resource, объединённо)
-- Chart: Bar
SELECT error_type, SUM(cnt) AS cnt
FROM (
    SELECT COALESCE(error_type::text, 'null') AS error_type, COUNT(*) AS cnt
    FROM operation_v2.operations
    WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
      AND state_dt < COALESCE(:period_end, now())
      AND error_type IS NOT NULL
    GROUP BY error_type
    UNION ALL
    SELECT COALESCE(error_type::text, 'null') AS error_type, COUNT(*) AS cnt
    FROM operation_v2.tasks
    WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
      AND state_dt < COALESCE(:period_end, now())
      AND error_type IS NOT NULL
    GROUP BY error_type
    UNION ALL
    SELECT COALESCE(status::text, 'null') AS error_type, COUNT(*) AS cnt
    FROM state.resource
    WHERE operator_ts > COALESCE(:period_start, now() - interval '24 hours')
      AND operator_ts < COALESCE(:period_end, now())
      AND (status ILIKE '%error%' OR status ILIKE '%fail%')
    GROUP BY status
) t
GROUP BY error_type
ORDER BY cnt DESC
LIMIT 20;

-- Q2: Bar — Топ error_message (первые 20)
-- Chart: Bar (или Table)
SELECT error_message, COUNT(*) AS cnt
FROM (
    SELECT LEFT(error_message, 100) AS error_message FROM operation_v2.operations
    WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
      AND state_dt < COALESCE(:period_end, now())
      AND error_message IS NOT NULL
    UNION ALL
    SELECT LEFT(error_message, 100) AS error_message FROM operation_v2.tasks
    WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
      AND state_dt < COALESCE(:period_end, now())
      AND error_message IS NOT NULL
) t
GROUP BY error_message
ORDER BY cnt DESC
LIMIT 20;

-- Q3: Table — Ресурсы в ошибке по operator (status, error_count)
-- Chart: Table
SELECT o.name AS operator_name, r.operator_uuid,
       COUNT(*) AS resource_count, SUM(r.error_count) AS total_error_count
FROM state.resource r
JOIN state.operator o ON r.operator_uuid = o.uuid
WHERE r.operator_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND r.operator_ts < COALESCE(:period_end, now())
  AND (r.error_count > 0 OR r.status ILIKE '%error%')
GROUP BY o.name, r.operator_uuid
ORDER BY total_error_count DESC NULLS LAST;

-- Q4: Stacked Bar — Ошибки по источнику (operations / tasks / resource)
-- Chart: Stacked Bar
SELECT 'operations' AS source, COUNT(*) AS error_count
FROM operation_v2.operations
WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
  AND state_dt < COALESCE(:period_end, now())
  AND (error_type IS NOT NULL OR error_message IS NOT NULL)
UNION ALL
SELECT 'tasks' AS source, COUNT(*) AS error_count
FROM operation_v2.tasks
WHERE state_dt > COALESCE(:period_start, now() - interval '24 hours')
  AND state_dt < COALESCE(:period_end, now())
  AND (error_type IS NOT NULL OR error_message IS NOT NULL)
UNION ALL
SELECT 'resource' AS source, COUNT(*) AS error_count
FROM state.resource
WHERE operator_ts > COALESCE(:period_start, now() - interval '24 hours')
  AND operator_ts < COALESCE(:period_end, now())
  AND error_count > 0;
