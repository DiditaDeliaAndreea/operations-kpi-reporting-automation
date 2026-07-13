"""Utilities for creating and accessing the reporting database."""

from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_PATH = BASE_DIR / "data" / "operations.db"
SQL_DIR = BASE_DIR / "sql"


def read_sql_file(filename: str) -> str:
    """Read a SQL file from the project's SQL directory."""

    sql_path = SQL_DIR / filename

    if not sql_path.exists():
        raise FileNotFoundError(
            f"SQL file not found: {sql_path}"
        )

    return sql_path.read_text(encoding="utf-8")


def initialise_database() -> None:
    """Create the database tables and insert sample records."""

    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    create_tables_sql = read_sql_file(
        "create_tables.sql"
    )
    seed_data_sql = read_sql_file(
        "seed_data.sql"
    )

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            "PRAGMA foreign_keys = ON;"
        )
        connection.executescript(create_tables_sql)
        connection.executescript(seed_data_sql)
        connection.commit()


def get_database_connection() -> sqlite3.Connection:
    """Return a connection to the SQLite database."""

    if not DATABASE_PATH.exists():
        raise FileNotFoundError(
            "The reporting database does not exist. "
            "Run 'python -m src.database' first."
        )

    connection = sqlite3.connect(DATABASE_PATH)
    connection.execute("PRAGMA foreign_keys = ON;")

    return connection


if __name__ == "__main__":
    initialise_database()

    print(
        "Database created successfully:"
    )
    print(DATABASE_PATH)