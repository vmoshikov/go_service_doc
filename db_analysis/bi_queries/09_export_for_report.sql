-- Экспорт данных для построения отчёта из CSV (отдельная задача от текущего процесса)
-- Использование: выполнить запросы, сохранить результаты в CSV, затем использовать CSV для генерации report.html

-- Параметры (подставить или использовать в BI):
-- :period_days — число дней (по умолчанию 7)
-- :from_date — начало периода YYYY-MM-DD (опционально)
-- :to_date — конец периода YYYY-MM-DD, включительно (опционально)

-- 1. Custom Resource (resource_type + version, deleted=False), сортировка по кол-ву живых кластеров
SELECT cr.resource_type, cr.version, COUNT(DISTINCT cr.cluster_uid) AS cluster_count
FROM conf.custom_resource cr
JOIN conf.cluster c ON c.uid = cr.cluster_uid AND c.delete_ts IS NULL
WHERE (cr.deleted IS NULL OR cr.deleted = false)
  AND cr.modify_ts > now() - interval '7 days'
GROUP BY cr.resource_type, cr.version
ORDER BY cluster_count DESC;

-- 2. Кластеры по статусу (только не удалённые)
SELECT cc.status, COUNT(*) AS cnt
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
GROUP BY cc.status;

-- 3. Ноды по статусу (только не удалённые кластеры)
SELECT nc.status, COUNT(*) AS cnt
FROM state.node_consumption nc
JOIN conf.cluster c ON c.uid = nc.cluster_uid AND c.delete_ts IS NULL
WHERE nc.update_ts > now() - interval '7 days'
GROUP BY nc.status;

-- 4. Версии K8s (только не удалённые кластеры)
SELECT cc.k8s_version, COUNT(*) AS cnt
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
GROUP BY cc.k8s_version;

-- 4a. CPU/RAM/NOD — суммарно по кластерам (только не удалённые)
SELECT SUM(cc.cpu_total) AS cpu_total, SUM(cc.ram_total) AS ram_total, SUM(cc.nod_total) AS nod_total,
  SUM(cc.cpu_running) AS cpu_running, SUM(cc.ram_running) AS ram_running, SUM(cc.nod_running) AS nod_running,
  SUM(cc.cpu_error) AS cpu_error, SUM(cc.ram_error) AS ram_error, SUM(cc.nod_error) AS nod_error
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days';

-- 4b. CPU по cluster_type_code (running / other / error)
SELECT cc.cluster_type_code,
  SUM(cc.cpu_running) AS cpu_running, SUM(cc.cpu_other) AS cpu_other, SUM(cc.cpu_error) AS cpu_error
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
GROUP BY cc.cluster_type_code;

-- 4c. RAM по cluster_type_code (running / other / error)
SELECT cc.cluster_type_code,
  SUM(cc.ram_running) AS ram_running, SUM(cc.ram_other) AS ram_other, SUM(cc.ram_error) AS ram_error
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
GROUP BY cc.cluster_type_code;

-- 4d. NOD по cluster_type_code (running / other / error)
SELECT cc.cluster_type_code,
  SUM(cc.nod_running) AS nod_running, SUM(cc.nod_other) AS nod_other, SUM(cc.nod_error) AS nod_error
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
GROUP BY cc.cluster_type_code;

-- 4e. Топ 15 кластеров по CPU
SELECT cc.short_name, cc.cpu_total, cc.cpu_running, cc.cpu_error
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
ORDER BY cc.cpu_total DESC NULLS LAST LIMIT 15;

-- 4f. Топ 15 кластеров по RAM
SELECT cc.short_name, cc.ram_total, cc.ram_running, cc.ram_error
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
ORDER BY cc.ram_total DESC NULLS LAST LIMIT 15;

-- 4g. Топ 15 кластеров по NOD
SELECT cc.short_name, cc.nod_total, cc.nod_running, cc.nod_error
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
ORDER BY cc.nod_total DESC NULLS LAST LIMIT 15;

-- 4h. CPU/RAM/Disk по нодам (flavor)
SELECT nc.flavor, SUM(nc.cpu) AS cpu_total, SUM(nc.ram) AS ram_total, SUM(nc.disk) AS disk_total
FROM state.node_consumption nc
JOIN conf.cluster c ON c.uid = nc.cluster_uid AND c.delete_ts IS NULL
WHERE nc.update_ts > now() - interval '7 days'
GROUP BY nc.flavor;

-- 5. Операции по статусу
SELECT state, COUNT(*) AS cnt
FROM operation_v2.operations
WHERE state_dt > now() - interval '7 days'
GROUP BY state;

-- 6. Операции по дням (успешные / неуспешные)
SELECT DATE(state_dt) AS day,
  SUM(CASE WHEN LOWER(state) IN ('success','completed','done') THEN 1 ELSE 0 END) AS success,
  SUM(CASE WHEN LOWER(state) NOT IN ('success','completed','done') THEN 1 ELSE 0 END) AS failed
FROM operation_v2.operations
WHERE state_dt > now() - interval '7 days'
GROUP BY DATE(state_dt)
ORDER BY day;

-- =============================================================================
-- Приоритет 1: Tasks (операции → задачи)
-- =============================================================================

-- 7. Tasks по action
SELECT COALESCE(action::text, 'null') AS action, COUNT(*) AS cnt
FROM operation_v2.tasks
WHERE state_dt > now() - interval '7 days'
GROUP BY action
ORDER BY cnt DESC;

-- 8. Tasks по operator
SELECT COALESCE(operator::text, 'null') AS operator, COUNT(*) AS cnt
FROM operation_v2.tasks
WHERE state_dt > now() - interval '7 days'
GROUP BY operator
ORDER BY cnt DESC;

-- 9. Failed tasks по operator
SELECT COALESCE(operator::text, 'null') AS operator, COUNT(*) AS failed_cnt
FROM operation_v2.tasks
WHERE state_dt > now() - interval '7 days'
  AND (error_type IS NOT NULL OR error_message IS NOT NULL)
GROUP BY operator
ORDER BY failed_cnt DESC;

-- 10. Tasks на операцию (распределение)
SELECT task_count, COUNT(*) AS operation_count
FROM (
  SELECT operation_id, COUNT(*) AS task_count
  FROM operation_v2.tasks
  WHERE state_dt > now() - interval '7 days'
  GROUP BY operation_id
) t
GROUP BY task_count
ORDER BY task_count;

-- 11. Avg duration по action (секунды)
SELECT COALESCE(action::text, 'null') AS action,
       COUNT(*) AS cnt,
       ROUND(AVG(EXTRACT(EPOCH FROM duration)), 2) AS avg_duration_sec
FROM operation_v2.tasks
WHERE state_dt > now() - interval '7 days'
  AND duration IS NOT NULL
GROUP BY action
ORDER BY avg_duration_sec DESC NULLS LAST;

-- =============================================================================
-- Приоритет 2: Nodepool + Node
-- =============================================================================

-- 12. Nodepool по кластерам (только не удалённые, cluster_ci из state.cluster_consumption)
SELECT c.uid AS cluster_uid, MAX(cc.cluster_ci) AS cluster_ci, c.short_name, MAX(cc.environment) AS env, c.di_area_id, COUNT(np.uid) AS nodepool_count
FROM conf.cluster c
LEFT JOIN conf.nodepool np ON np.cluster_uid = c.uid AND (np.deleted IS NULL OR np.deleted = false)
LEFT JOIN state.cluster_consumption cc ON cc.uid = c.uid AND cc.update_ts > now() - interval '7 days'
WHERE c.delete_ts IS NULL AND c.modify_ts > now() - interval '7 days'
GROUP BY c.uid, c.short_name, c.di_area_id
ORDER BY nodepool_count DESC;

-- 13. Node type distribution (только не удалённые nodepool)
SELECT COALESCE(np.node_type_code::text, 'null') AS node_type_code, COUNT(*) AS cnt
FROM conf.nodepool np
JOIN conf.cluster c ON c.uid = np.cluster_uid AND c.delete_ts IS NULL
WHERE (np.deleted IS NULL OR np.deleted = false)
  AND np.modify_ts > now() - interval '7 days'
GROUP BY np.node_type_code
ORDER BY cnt DESC;

-- 14. Nodes по nodepool
SELECT np.uid AS nodepool_uid, np.name AS nodepool_name, COUNT(n.uid) AS node_count
FROM conf.nodepool np
JOIN conf.cluster c ON c.uid = np.cluster_uid AND c.delete_ts IS NULL
LEFT JOIN state.node n ON n.nodepool_uid = np.uid
  AND (n.deleted IS NULL OR LOWER(COALESCE(n.deleted::text, '')) NOT IN ('true', '1', 'yes'))
WHERE (np.deleted IS NULL OR np.deleted = false)
  AND np.modify_ts > now() - interval '7 days'
GROUP BY np.uid, np.name
ORDER BY node_count DESC;

-- =============================================================================
-- Приоритет 3: Resource + Operator + Admins
-- =============================================================================

-- 15. Resources в ошибке по operator
SELECT o.name AS operator_name, o.operator_type,
       COUNT(*) AS resource_count, SUM(r.error_count) AS total_error_count
FROM state.resource r
JOIN state.operator o ON r.operator_uuid = o.uuid
WHERE r.operator_ts > now() - interval '7 days'
  AND (r.error_count > 0 OR r.status ILIKE '%error%' OR r.status ILIKE '%fail%')
GROUP BY o.name, o.operator_type
ORDER BY total_error_count DESC NULLS LAST;

-- 16. Operators по кластерам (только не удалённые)
SELECT o.cluster_uid, c.short_name, COUNT(*) AS operator_count
FROM state.operator o
JOIN conf.cluster c ON c.uid = o.cluster_uid AND c.delete_ts IS NULL
WHERE o.start_ts > now() - interval '7 days'
GROUP BY o.cluster_uid, c.short_name
ORDER BY operator_count DESC;

-- 17. Admins по кластерам (только непустые admins)
SELECT cluster_uid, admins
FROM conf.admins
WHERE cluster_uid IS NOT NULL
  AND admins IS NOT NULL
  AND TRIM(admins::text) != ''
ORDER BY cluster_uid;

-- 18. CR по кластерам (cluster_uid, cluster_ci, short_name, env, di_area_id, cr_list)
SELECT cr.cluster_uid, MAX(cc.cluster_ci) AS cluster_ci, MAX(c.short_name) AS short_name,
       MAX(cc.environment) AS env, MAX(c.di_area_id) AS di_area_id,
       STRING_AGG(DISTINCT cr.resource_type || ' @ ' || cr.version, ', ' ORDER BY cr.resource_type || ' @ ' || cr.version) AS cr_list
FROM conf.custom_resource cr
JOIN conf.cluster c ON c.uid = cr.cluster_uid AND c.delete_ts IS NULL
LEFT JOIN state.cluster_consumption cc ON cc.uid = cr.cluster_uid AND cc.update_ts > now() - interval '7 days'
WHERE (cr.deleted IS NULL OR cr.deleted = false)
  AND cr.modify_ts > now() - interval '7 days'
GROUP BY cr.cluster_uid
ORDER BY cr.cluster_uid;

-- 19. География (region × environment)
SELECT cc.region, cc.environment, COUNT(*) AS cluster_count
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
GROUP BY cc.region, cc.environment
ORDER BY cc.region, cc.environment;

-- 20. Узлы по region
SELECT nc.region, COUNT(*) AS node_count
FROM state.node_consumption nc
JOIN conf.cluster c ON c.uid = nc.cluster_uid AND c.delete_ts IS NULL
WHERE nc.update_ts > now() - interval '7 days'
GROUP BY nc.region
ORDER BY node_count DESC;

-- 21. Тренды потребления (CPU/RAM/NOD по дням)
SELECT DATE(cc.update_ts) AS day,
       SUM(cc.cpu_total) AS cpu_total, SUM(cc.ram_total) AS ram_total, SUM(cc.nod_total) AS nod_total
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
GROUP BY DATE(cc.update_ts)
ORDER BY day;

-- 22. Топ error_type (operations + tasks)
SELECT error_type, SUM(cnt) AS cnt FROM (
  SELECT COALESCE(error_type::text, 'null') AS error_type, COUNT(*) AS cnt
  FROM operation_v2.operations WHERE state_dt > now() - interval '7 days' AND error_type IS NOT NULL GROUP BY error_type
  UNION ALL
  SELECT COALESCE(error_type::text, 'null') AS error_type, COUNT(*) AS cnt
  FROM operation_v2.tasks WHERE state_dt > now() - interval '7 days' AND error_type IS NOT NULL GROUP BY error_type
) t GROUP BY error_type ORDER BY cnt DESC LIMIT 20;

-- 23. Dedicated vs Shared
SELECT COALESCE(nc.on_dedicated_resources::text, 'unknown') AS resource_type, COUNT(*) AS node_count
FROM state.node_consumption nc
JOIN conf.cluster c ON c.uid = nc.cluster_uid AND c.delete_ts IS NULL
WHERE nc.update_ts > now() - interval '7 days'
GROUP BY nc.on_dedicated_resources;

-- 24. По environment
SELECT cc.environment, COUNT(*) AS cluster_count
FROM state.cluster_consumption cc
JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
WHERE cc.update_ts > now() - interval '7 days'
GROUP BY cc.environment
ORDER BY cluster_count DESC;

-- Для явного диапазона дат замените:
--   update_ts > now() - interval '7 days'  →  update_ts >= ':from_date' AND update_ts < ':to_date'::date + 1
--   modify_ts > now() - interval '7 days'  →  modify_ts >= ':from_date' AND modify_ts < ':to_date'::date + 1
--   state_dt > now() - interval '7 days'  →  state_dt >= ':from_date' AND state_dt < ':to_date'::date + 1
--   operator_ts > now() - interval '7 days' → operator_ts >= ':from_date' AND operator_ts < ':to_date'::date + 1
--   start_ts > now() - interval '7 days'   →  start_ts >= ':from_date' AND start_ts < ':to_date'::date + 1
