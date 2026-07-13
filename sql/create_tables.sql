DROP TABLE IF EXISTS task_tags;
DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    task_status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    completed_at TEXT,
    agent_name TEXT
);

CREATE TABLE task_tags (
    task_id TEXT NOT NULL,
    tag_name TEXT NOT NULL,

    PRIMARY KEY (task_id, tag_name),

    FOREIGN KEY (task_id)
        REFERENCES tasks(task_id)
        ON DELETE CASCADE
);