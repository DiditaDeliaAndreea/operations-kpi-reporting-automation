"""Create and populate the team-level KPI Excel report."""

from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo

from src.extract_tasks import extract_completed_tasks
from src.prepare_reporting_data import prepare_reporting_data
from src.team_mapping import TEAM_CONFIG


BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "output"

DUBLIN_TIMEZONE = ZoneInfo("Europe/Dublin")


TEAM_HEADERS = [
    "Team",
    "Task Type",
    "Task ID",
    "Created Date",
    "Completed Date",
    "SLA Breached",
]


HEADER_FILL = PatternFill(
    fill_type="solid",
    fgColor="1F4E78",
)

HEADER_FONT = Font(
    color="FFFFFF",
    bold=True,
)

TITLE_FONT = Font(
    size=16,
    bold=True,
)

LABEL_FONT = Font(
    bold=True,
)


def format_header_row(worksheet) -> None:
    """Apply formatting to a team worksheet header."""

    for cell in worksheet[1]:
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(
            horizontal="center",
            vertical="center",
            wrap_text=True,
        )

    worksheet.freeze_panes = "A2"
    worksheet.row_dimensions[1].height = 30


def set_team_sheet_widths(worksheet) -> None:
    """Set readable widths for team worksheet columns."""

    widths = {
        "A": 18,
        "B": 34,
        "C": 16,
        "D": 21,
        "E": 21,
        "F": 16,
    }

    for column, width in widths.items():
        worksheet.column_dimensions[column].width = width


def set_summary_sheet_widths(worksheet) -> None:
    """Set readable widths for the Summary worksheet."""

    worksheet.column_dimensions["A"].width = 30
    worksheet.column_dimensions["B"].width = 22


def create_workbook() -> Workbook:
    """Create the complete KPI workbook in memory."""

    workbook = Workbook()

    summary_sheet = workbook.active
    summary_sheet.title = "Summary"

    summary_sheet["A1"] = "Operations KPI Report"
    summary_sheet["A1"].font = TITLE_FONT

    set_summary_sheet_widths(summary_sheet)

    for team_name in TEAM_CONFIG:
        worksheet = workbook.create_sheet(
            title=team_name
        )

        worksheet.append(TEAM_HEADERS)

        format_header_row(worksheet)
        set_team_sheet_widths(worksheet)

    return workbook


def convert_excel_value(value):
    """Convert Pandas values into Excel-compatible values."""

    if pd.isna(value):
        return None

    if isinstance(value, pd.Timestamp):
        return value.to_pydatetime()

    return value


def create_table_name(team_name: str) -> str:
    """Create a valid Excel table name."""

    cleaned_name = "".join(
        character
        for character in team_name
        if character.isalnum()
    )

    return f"{cleaned_name}Tasks"


def write_team_sheet(
    worksheet,
    team_df: pd.DataFrame,
    team_name: str,
) -> None:
    """Write one team's task records into its worksheet."""

    for row in team_df.itertuples(index=False):
        worksheet.append(
            [
                convert_excel_value(row.team_name),
                convert_excel_value(row.task_type),
                convert_excel_value(row.task_id),
                convert_excel_value(row.created_at),
                convert_excel_value(row.completed_at),
                convert_excel_value(row.sla_breached),
            ]
        )

    if worksheet.max_row > 1:
        table_reference = (
            f"A1:F{worksheet.max_row}"
        )

        table = Table(
            displayName=create_table_name(team_name),
            ref=table_reference,
        )

        table.tableStyleInfo = TableStyleInfo(
            name="TableStyleMedium2",
            showFirstColumn=False,
            showLastColumn=False,
            showRowStripes=True,
            showColumnStripes=False,
        )

        worksheet.add_table(table)

    for cell in worksheet["D"][1:]:
        cell.number_format = "yyyy-mm-dd hh:mm"

    for cell in worksheet["E"][1:]:
        cell.number_format = "yyyy-mm-dd hh:mm"

    for cell in worksheet["F"][1:]:
        cell.alignment = Alignment(
            horizontal="center",
        )


def get_reporting_weeks(
    reporting_df: pd.DataFrame,
) -> tuple:
    """Return the two reporting-week date ranges."""

    week_starts = sorted(
        pd.to_datetime(
            reporting_df["reporting_week"]
        )
        .dt.date
        .unique()
    )

    if len(week_starts) < 2:
        raise ValueError(
            "At least two reporting weeks are required."
        )

    older_week_start = week_starts[-2]
    recent_week_start = week_starts[-1]

    older_week_end = (
        older_week_start
        + timedelta(days=6)
    )

    recent_week_end = (
        recent_week_start
        + timedelta(days=6)
    )

    return (
        older_week_start,
        older_week_end,
        recent_week_start,
        recent_week_end,
    )


def write_summary_sheet(
    workbook: Workbook,
    reporting_df: pd.DataFrame,
) -> None:
    """Write basic report information without KPI formulas."""

    worksheet = workbook["Summary"]

    (
        older_week_start,
        older_week_end,
        recent_week_start,
        recent_week_end,
    ) = get_reporting_weeks(reporting_df)

    summary_values = [
        (
            "Older Reporting Week Start",
            older_week_start,
        ),
        (
            "Older Reporting Week End",
            older_week_end,
        ),
        (
            "Recent Reporting Week Start",
            recent_week_start,
        ),
        (
            "Recent Reporting Week End",
            recent_week_end,
        ),
        (
            "Generated At",
            datetime.now(
                DUBLIN_TIMEZONE
            ).replace(tzinfo=None),
        ),
        (
            "Total Tasks Included",
            len(reporting_df),
        ),
    ]

    for row_number, (
        label,
        value,
    ) in enumerate(
        summary_values,
        start=3,
    ):
        worksheet.cell(
            row=row_number,
            column=1,
            value=label,
        ).font = LABEL_FONT

        worksheet.cell(
            row=row_number,
            column=2,
            value=value,
        )

    for cell_reference in [
        "B3",
        "B4",
        "B5",
        "B6",
    ]:
        worksheet[cell_reference].number_format = (
            "yyyy-mm-dd"
        )

    worksheet["B7"].number_format = (
        "yyyy-mm-dd hh:mm"
    )


def remove_old_reports() -> None:
    """Remove previously generated KPI workbooks."""

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    for existing_report in OUTPUT_DIR.glob(
        "operations_kpi_report*.xlsx"
    ):
        try:
            existing_report.unlink()

        except PermissionError as error:
            raise PermissionError(
                "Close the existing Excel report before "
                "running the workflow again."
            ) from error


def export_kpi_report(
    reporting_df: pd.DataFrame,
) -> Path:
    """Create and save one final KPI workbook."""

    if reporting_df.empty:
        raise ValueError(
            "No reporting data is available to export."
        )

    (
        older_week_start,
        _,
        _,
        recent_week_end,
    ) = get_reporting_weeks(reporting_df)

    remove_old_reports()

    output_path = (
        OUTPUT_DIR
        / (
            "operations_kpi_report_"
            f"{older_week_start}_to_"
            f"{recent_week_end}.xlsx"
        )
    )

    workbook = create_workbook()

    for team_name in TEAM_CONFIG:
        worksheet = workbook[team_name]

        team_df = (
            reporting_df[
                reporting_df["team_name"]
                == team_name
            ]
            .sort_values(
                by=[
                    "completed_at",
                    "task_type",
                    "task_id",
                ]
            )
        )

        write_team_sheet(
            worksheet=worksheet,
            team_df=team_df,
            team_name=team_name,
        )

    write_summary_sheet(
        workbook=workbook,
        reporting_df=reporting_df,
    )

    workbook.save(output_path)

    return output_path


if __name__ == "__main__":
    extracted_tasks_df = extract_completed_tasks()

    reporting_df = prepare_reporting_data(
        extracted_tasks_df
    )

    if reporting_df.empty:
        print(
            "No tasks were available for Excel reporting."
        )
    else:
        report_path = export_kpi_report(
            reporting_df
        )

        print("Excel report created successfully:")
        print(report_path)