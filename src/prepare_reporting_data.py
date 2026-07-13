"""Prepare extracted tasks for KPI reporting."""

from typing import Any

import pandas as pd

from src.extract_tasks import extract_completed_tasks
from src.team_mapping import (
    SLA_EXCEEDED_TAG,
    SLA_TASK_TYPE,
    TASK_TYPE_TAG_MAPPING,
    TEAM_CONFIG,
)


OUTPUT_COLUMNS = [
    "task_id",
    "agent_name",
    "created_at",
    "completed_at",
    "team_name",
    "task_type",
    "sla_breached",
    "reporting_week",
    "reporting_month",
    "tags",
]


def parse_tags(tags: Any) -> set[str]:
    """Convert pipe-separated tags into a set."""

    if pd.isna(tags):
        return set()

    return {
        tag.strip()
        for tag in str(tags).split("|")
        if tag.strip()
    }


def identify_task_type(tags: set[str]) -> str:
    """Identify the task type using the task's tags."""

    matching_types = {
        task_type
        for tag, task_type in TASK_TYPE_TAG_MAPPING.items()
        if tag in tags
    }

    if not matching_types:
        return "Unknown"

    if len(matching_types) > 1:
        return "Multiple Task Types"

    return next(iter(matching_types))


def identify_reporting_team(
    agent_name: str,
    tags: set[str],
) -> str | None:
    """
    Identify the reporting team using the agent and team tag.

    The task is included only when:
    1. The task contains the team's tag.
    2. The agent belongs to that team.
    """

    for team_name, config in TEAM_CONFIG.items():
        team_tag = config["tag"]
        team_agents = config["agents"]

        if (
            team_tag in tags
            and agent_name in team_agents
        ):
            return team_name

    return None


def identify_sla_breached(
    task_type: str,
    tags: set[str],
) -> str:
    """
    Return the SLA breach result.

    Priority Escalation Review:
        Yes = sla_exceeded tag is present.
        No = sla_exceeded tag is not present.

    All other task types:
        N/A = the task type does not have an SLA.
    """

    if task_type != SLA_TASK_TYPE:
        return "N/A"

    if SLA_EXCEEDED_TAG in tags:
        return "Yes"

    return "No"


def prepare_reporting_data(
    tasks_df: pd.DataFrame,
) -> pd.DataFrame:
    """Prepare extracted tasks for team-level KPI reporting."""

    if tasks_df.empty:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)

    reporting_df = tasks_df.copy()

    reporting_df["tag_set"] = reporting_df["tags"].apply(
        parse_tags
    )

    reporting_df["task_type"] = reporting_df["tag_set"].apply(
        identify_task_type
    )

    reporting_df["team_name"] = reporting_df.apply(
        lambda row: identify_reporting_team(
            agent_name=row["agent_name"],
            tags=row["tag_set"],
        ),
        axis=1,
    )

    # Include tasks only when the agent and team tag both match.
    reporting_df = reporting_df[
        reporting_df["team_name"].notna()
    ].copy()

    reporting_df["sla_breached"] = reporting_df.apply(
        lambda row: identify_sla_breached(
            task_type=row["task_type"],
            tags=row["tag_set"],
        ),
        axis=1,
    )

    reporting_df["reporting_week"] = (
        reporting_df["completed_at"]
        .dt.to_period("W-SUN")
        .dt.start_time
        .dt.date
    )

    reporting_df["reporting_month"] = (
        reporting_df["completed_at"]
        .dt.to_period("M")
        .astype(str)
    )

    reporting_df = reporting_df.sort_values(
        by=[
            "team_name",
            "completed_at",
            "task_type",
            "task_id",
        ]
    ).reset_index(drop=True)

    return reporting_df[OUTPUT_COLUMNS]


if __name__ == "__main__":
    extracted_tasks_df = extract_completed_tasks()

    reporting_df = prepare_reporting_data(
        extracted_tasks_df
    )

    print(
        f"Tasks extracted: "
        f"{len(extracted_tasks_df)}"
    )

    print(
        f"Tasks included in reporting: "
        f"{len(reporting_df)}"
    )

    if reporting_df.empty:
        print(
            "No tasks were available for KPI reporting."
        )
    else:
        print(
            reporting_df.to_string(index=False)
        )