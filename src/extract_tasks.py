"""Extract tasks completed during the previous reporting week."""

import pandas as pd

from src.database import (
    get_database_connection,
    read_sql_file,
)


def extract_completed_tasks() -> pd.DataFrame:
    """
    Extract tasks completed during the previous Monday-to-Sunday week.

    The reporting-period calculation is performed directly in SQL.
    """

    query = read_sql_file(
        "extract_completed_tasks.sql"
    )

    with get_database_connection() as connection:
        tasks_df = pd.read_sql_query(
            query,
            connection,
            parse_dates=[
                "created_at",
                "completed_at",
            ],
        )

    return tasks_df


if __name__ == "__main__":
    completed_tasks_df = extract_completed_tasks()

    print(
        f"Completed tasks extracted: "
        f"{len(completed_tasks_df)}"
    )

    if completed_tasks_df.empty:
        print(
            "No completed tasks were found "
            "for the previous week."
        )
    else:
        print(
            completed_tasks_df.to_string(
                index=False
            )
        )