WITH current_week AS (
    SELECT
        date(
            'now',
            'localtime',
            '-' || (
                (
                    CAST(
                        strftime('%w', 'now', 'localtime')
                        AS INTEGER
                    ) + 6
                ) % 7
            ) || ' days'
        ) AS current_monday
),

reporting_period AS (
    SELECT
        date(current_monday, '-14 days') AS period_start,
        current_monday AS period_end
    FROM current_week
)

SELECT
    tasks.task_id,
    tasks.task_status,
    tasks.created_at,
    tasks.completed_at,
    tasks.agent_name,
    GROUP_CONCAT(
        task_tags.tag_name,
        '|'
    ) AS tags

FROM tasks

LEFT JOIN task_tags
    ON tasks.task_id = task_tags.task_id

CROSS JOIN reporting_period

WHERE tasks.task_status = 'Closed'
  AND tasks.completed_at >= reporting_period.period_start
  AND tasks.completed_at < reporting_period.period_end

GROUP BY
    tasks.task_id,
    tasks.task_status,
    tasks.created_at,
    tasks.completed_at,
    tasks.agent_name

ORDER BY
    tasks.completed_at,
    tasks.agent_name,
    tasks.task_id;