"""Team, task-type, and SLA configuration."""

from typing import Final


TEAM_CONFIG: Final = {
    "Team Alpha": {
        "tag": "team_alpha",
        "agents": {
            "Alex Morgan",
            "Jamie Lee",
        },
    },
    "Team Beta": {
        "tag": "team_beta",
        "agents": {
            "Taylor Smith",
            "Jordan Patel",
        },
    },
    "Team Gamma": {
        "tag": "team_gamma",
        "agents": {
            "Morgan Reed",
            "Casey Brown",
        },
    },
    "Team Delta": {
        "tag": "team_delta",
        "agents": {
            "Riley Davis",
            "Cameron Wilson",
        },
    },
    "Team Epsilon": {
        "tag": "team_epsilon",
        "agents": {
            "Avery Clark",
            "Quinn Lewis",
        },
    },
}


TASK_TYPE_TAG_MAPPING: Final = {
    "task_type_quality_review": "Quality Review",
    "task_type_complex_case": "Complex Case Review",
    "task_type_process_exception": (
        "Process Exception Investigation"
    ),
    "task_type_priority_escalation": (
        "Priority Escalation Review"
    ),
}


SLA_TASK_TYPE: Final = "Priority Escalation Review"

SLA_EXCEEDED_TAG: Final = "sla_exceeded"