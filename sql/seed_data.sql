DROP TABLE IF EXISTS seed_plan;
DROP TABLE IF EXISTS generated_seed_tasks;


CREATE TEMP TABLE seed_plan (
    week_number INTEGER NOT NULL,
    week_offset_days INTEGER NOT NULL,
    team_sort INTEGER NOT NULL,
    team_name TEXT NOT NULL,
    team_tag TEXT NOT NULL,
    agent_one TEXT NOT NULL,
    agent_two TEXT NOT NULL,
    task_sort INTEGER NOT NULL,
    task_type TEXT NOT NULL,
    task_type_tag TEXT NOT NULL,
    task_count INTEGER NOT NULL,
    sla_breach_count INTEGER NOT NULL
);


INSERT INTO seed_plan (
    week_number,
    week_offset_days,
    team_sort,
    team_name,
    team_tag,
    agent_one,
    agent_two,
    task_sort,
    task_type,
    task_type_tag,
    task_count,
    sla_breach_count
)
VALUES
    /*
    Older completed week: 44 tasks
    Team totals:
        Alpha   = 7
        Beta    = 8
        Gamma   = 9
        Delta   = 10
        Epsilon = 10
    */

    (
        1,
        -14,
        1,
        'Team Alpha',
        'team_alpha',
        'Alex Morgan',
        'Jamie Lee',
        1,
        'Quality Review',
        'task_type_quality_review',
        2,
        0
    ),
    (
        1,
        -14,
        1,
        'Team Alpha',
        'team_alpha',
        'Alex Morgan',
        'Jamie Lee',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        2,
        0
    ),
    (
        1,
        -14,
        1,
        'Team Alpha',
        'team_alpha',
        'Alex Morgan',
        'Jamie Lee',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        1,
        0
    ),
    (
        1,
        -14,
        1,
        'Team Alpha',
        'team_alpha',
        'Alex Morgan',
        'Jamie Lee',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        2,
        1
    ),

    (
        1,
        -14,
        2,
        'Team Beta',
        'team_beta',
        'Taylor Smith',
        'Jordan Patel',
        1,
        'Quality Review',
        'task_type_quality_review',
        2,
        0
    ),
    (
        1,
        -14,
        2,
        'Team Beta',
        'team_beta',
        'Taylor Smith',
        'Jordan Patel',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        1,
        0
    ),
    (
        1,
        -14,
        2,
        'Team Beta',
        'team_beta',
        'Taylor Smith',
        'Jordan Patel',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        2,
        0
    ),
    (
        1,
        -14,
        2,
        'Team Beta',
        'team_beta',
        'Taylor Smith',
        'Jordan Patel',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        3,
        1
    ),

    (
        1,
        -14,
        3,
        'Team Gamma',
        'team_gamma',
        'Morgan Reed',
        'Casey Brown',
        1,
        'Quality Review',
        'task_type_quality_review',
        2,
        0
    ),
    (
        1,
        -14,
        3,
        'Team Gamma',
        'team_gamma',
        'Morgan Reed',
        'Casey Brown',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        2,
        0
    ),
    (
        1,
        -14,
        3,
        'Team Gamma',
        'team_gamma',
        'Morgan Reed',
        'Casey Brown',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        2,
        0
    ),
    (
        1,
        -14,
        3,
        'Team Gamma',
        'team_gamma',
        'Morgan Reed',
        'Casey Brown',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        3,
        2
    ),

    (
        1,
        -14,
        4,
        'Team Delta',
        'team_delta',
        'Riley Davis',
        'Cameron Wilson',
        1,
        'Quality Review',
        'task_type_quality_review',
        3,
        0
    ),
    (
        1,
        -14,
        4,
        'Team Delta',
        'team_delta',
        'Riley Davis',
        'Cameron Wilson',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        2,
        0
    ),
    (
        1,
        -14,
        4,
        'Team Delta',
        'team_delta',
        'Riley Davis',
        'Cameron Wilson',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        2,
        0
    ),
    (
        1,
        -14,
        4,
        'Team Delta',
        'team_delta',
        'Riley Davis',
        'Cameron Wilson',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        3,
        1
    ),

    (
        1,
        -14,
        5,
        'Team Epsilon',
        'team_epsilon',
        'Avery Clark',
        'Quinn Lewis',
        1,
        'Quality Review',
        'task_type_quality_review',
        2,
        0
    ),
    (
        1,
        -14,
        5,
        'Team Epsilon',
        'team_epsilon',
        'Avery Clark',
        'Quinn Lewis',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        3,
        0
    ),
    (
        1,
        -14,
        5,
        'Team Epsilon',
        'team_epsilon',
        'Avery Clark',
        'Quinn Lewis',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        2,
        0
    ),
    (
        1,
        -14,
        5,
        'Team Epsilon',
        'team_epsilon',
        'Avery Clark',
        'Quinn Lewis',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        3,
        2
    ),

    /*
    Most recent completed week: 56 tasks
    Team totals:
        Alpha   = 12
        Beta    = 11
        Gamma   = 10
        Delta   = 11
        Epsilon = 12
    */

    (
        2,
        -7,
        1,
        'Team Alpha',
        'team_alpha',
        'Alex Morgan',
        'Jamie Lee',
        1,
        'Quality Review',
        'task_type_quality_review',
        3,
        0
    ),
    (
        2,
        -7,
        1,
        'Team Alpha',
        'team_alpha',
        'Alex Morgan',
        'Jamie Lee',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        3,
        0
    ),
    (
        2,
        -7,
        1,
        'Team Alpha',
        'team_alpha',
        'Alex Morgan',
        'Jamie Lee',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        3,
        0
    ),
    (
        2,
        -7,
        1,
        'Team Alpha',
        'team_alpha',
        'Alex Morgan',
        'Jamie Lee',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        3,
        1
    ),

    (
        2,
        -7,
        2,
        'Team Beta',
        'team_beta',
        'Taylor Smith',
        'Jordan Patel',
        1,
        'Quality Review',
        'task_type_quality_review',
        3,
        0
    ),
    (
        2,
        -7,
        2,
        'Team Beta',
        'team_beta',
        'Taylor Smith',
        'Jordan Patel',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        2,
        0
    ),
    (
        2,
        -7,
        2,
        'Team Beta',
        'team_beta',
        'Taylor Smith',
        'Jordan Patel',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        2,
        0
    ),
    (
        2,
        -7,
        2,
        'Team Beta',
        'team_beta',
        'Taylor Smith',
        'Jordan Patel',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        4,
        1
    ),

    (
        2,
        -7,
        3,
        'Team Gamma',
        'team_gamma',
        'Morgan Reed',
        'Casey Brown',
        1,
        'Quality Review',
        'task_type_quality_review',
        2,
        0
    ),
    (
        2,
        -7,
        3,
        'Team Gamma',
        'team_gamma',
        'Morgan Reed',
        'Casey Brown',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        3,
        0
    ),
    (
        2,
        -7,
        3,
        'Team Gamma',
        'team_gamma',
        'Morgan Reed',
        'Casey Brown',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        2,
        0
    ),
    (
        2,
        -7,
        3,
        'Team Gamma',
        'team_gamma',
        'Morgan Reed',
        'Casey Brown',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        3,
        1
    ),

    (
        2,
        -7,
        4,
        'Team Delta',
        'team_delta',
        'Riley Davis',
        'Cameron Wilson',
        1,
        'Quality Review',
        'task_type_quality_review',
        4,
        0
    ),
    (
        2,
        -7,
        4,
        'Team Delta',
        'team_delta',
        'Riley Davis',
        'Cameron Wilson',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        3,
        0
    ),
    (
        2,
        -7,
        4,
        'Team Delta',
        'team_delta',
        'Riley Davis',
        'Cameron Wilson',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        2,
        0
    ),
    (
        2,
        -7,
        4,
        'Team Delta',
        'team_delta',
        'Riley Davis',
        'Cameron Wilson',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        2,
        1
    ),

    (
        2,
        -7,
        5,
        'Team Epsilon',
        'team_epsilon',
        'Avery Clark',
        'Quinn Lewis',
        1,
        'Quality Review',
        'task_type_quality_review',
        3,
        0
    ),
    (
        2,
        -7,
        5,
        'Team Epsilon',
        'team_epsilon',
        'Avery Clark',
        'Quinn Lewis',
        2,
        'Complex Case Review',
        'task_type_complex_case',
        2,
        0
    ),
    (
        2,
        -7,
        5,
        'Team Epsilon',
        'team_epsilon',
        'Avery Clark',
        'Quinn Lewis',
        3,
        'Process Exception Investigation',
        'task_type_process_exception',
        3,
        0
    ),
    (
        2,
        -7,
        5,
        'Team Epsilon',
        'team_epsilon',
        'Avery Clark',
        'Quinn Lewis',
        4,
        'Priority Escalation Review',
        'task_type_priority_escalation',
        4,
        1
    );


CREATE TEMP TABLE generated_seed_tasks (
    seed_id INTEGER PRIMARY KEY AUTOINCREMENT,
    week_number INTEGER NOT NULL,
    team_sort INTEGER NOT NULL,
    team_name TEXT NOT NULL,
    team_tag TEXT NOT NULL,
    task_sort INTEGER NOT NULL,
    task_type TEXT NOT NULL,
    task_type_tag TEXT NOT NULL,
    item_number INTEGER NOT NULL,
    sla_breach_count INTEGER NOT NULL,
    agent_name TEXT NOT NULL,
    created_at TEXT NOT NULL,
    completed_at TEXT NOT NULL
);


WITH RECURSIVE numbers(n) AS (
    SELECT 1

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 10
),

current_week AS (
    SELECT
        date(
            'now',
            'localtime',
            '-' || (
                (
                    CAST(
                        strftime(
                            '%w',
                            'now',
                            'localtime'
                        ) AS INTEGER
                    ) + 6
                ) % 7
            ) || ' days'
        ) AS current_monday
)

INSERT INTO generated_seed_tasks (
    week_number,
    team_sort,
    team_name,
    team_tag,
    task_sort,
    task_type,
    task_type_tag,
    item_number,
    sla_breach_count,
    agent_name,
    created_at,
    completed_at
)

SELECT
    plan.week_number,
    plan.team_sort,
    plan.team_name,
    plan.team_tag,
    plan.task_sort,
    plan.task_type,
    plan.task_type_tag,
    numbers.n,
    plan.sla_breach_count,

    CASE
        WHEN numbers.n % 2 = 1
            THEN plan.agent_one
        ELSE plan.agent_two
    END AS agent_name,

    datetime(
        current_week.current_monday,
        printf(
            '%+d days',
            plan.week_offset_days
        ),
        printf(
            '+%d days',
            (
                plan.team_sort * 2
                + plan.task_sort
                + numbers.n * 3
                + plan.week_number
            ) % 7
        ),
        printf(
            '+%d hours',
            9 + (
                plan.team_sort
                + plan.task_sort * 2
                + numbers.n
            ) % 8
        ),
        printf(
            '+%d minutes',
            (
                7
                + plan.team_sort * 9
                + plan.task_sort * 11
                + numbers.n * 13
                + plan.week_number
            ) % 60
        ),
        printf(
            '-%d hours',
            18 + (
                plan.team_sort * 5
                + plan.task_sort * 9
                + numbers.n * 7
                + plan.week_number
            ) % 54
        )
    ) AS created_at,

    datetime(
        current_week.current_monday,
        printf(
            '%+d days',
            plan.week_offset_days
        ),
        printf(
            '+%d days',
            (
                plan.team_sort * 2
                + plan.task_sort
                + numbers.n * 3
                + plan.week_number
            ) % 7
        ),
        printf(
            '+%d hours',
            9 + (
                plan.team_sort
                + plan.task_sort * 2
                + numbers.n
            ) % 8
        ),
        printf(
            '+%d minutes',
            (
                7
                + plan.team_sort * 9
                + plan.task_sort * 11
                + numbers.n * 13
                + plan.week_number
            ) % 60
        )
    ) AS completed_at

FROM seed_plan AS plan

CROSS JOIN numbers

CROSS JOIN current_week

WHERE numbers.n <= plan.task_count

ORDER BY
    plan.week_number,
    plan.team_sort,
    plan.task_sort,
    numbers.n;


INSERT INTO tasks (
    task_id,
    task_status,
    created_at,
    completed_at,
    agent_name
)

SELECT
    printf(
        'TASK-%04d',
        2000 + seed_id
    ),
    'Closed',
    created_at,
    completed_at,
    agent_name

FROM generated_seed_tasks

ORDER BY seed_id;


-- Add each task's team-specific tag.
INSERT INTO task_tags (
    task_id,
    tag_name
)

SELECT
    printf(
        'TASK-%04d',
        2000 + seed_id
    ),
    team_tag

FROM generated_seed_tasks;


-- Add each task's task-type tag.
INSERT INTO task_tags (
    task_id,
    tag_name
)

SELECT
    printf(
        'TASK-%04d',
        2000 + seed_id
    ),
    task_type_tag

FROM generated_seed_tasks;


-- Add the SLA tag only to selected Priority Escalation tasks.
INSERT INTO task_tags (
    task_id,
    tag_name
)

SELECT
    printf(
        'TASK-%04d',
        2000 + seed_id
    ),
    'sla_exceeded'

FROM generated_seed_tasks

WHERE task_type = 'Priority Escalation Review'
  AND item_number <= sla_breach_count;


DROP TABLE generated_seed_tasks;
DROP TABLE seed_plan;