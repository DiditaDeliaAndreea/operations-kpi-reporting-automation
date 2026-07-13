"""Run the complete operations KPI reporting workflow."""

from src.excel_report import export_kpi_report
from src.extract_tasks import extract_completed_tasks
from src.prepare_reporting_data import prepare_reporting_data


def run_workflow() -> None:
    """Extract, prepare, and export the previous week's task data."""

    print("Operations KPI Reporting Workflow")
    print("-" * 40)

    extracted_tasks_df = extract_completed_tasks()

    print(
        f"Tasks extracted for the previous week: "
        f"{len(extracted_tasks_df)}"
    )

    reporting_df = prepare_reporting_data(
        extracted_tasks_df
    )

    print(
        f"Tasks included after team filtering: "
        f"{len(reporting_df)}"
    )

    if reporting_df.empty:
        print(
            "No valid tasks were found for "
            "the previous reporting week."
        )
        return

    report_path = export_kpi_report(
        reporting_df
    )

    print("\nExcel report created successfully:")
    print(report_path)


if __name__ == "__main__":
    run_workflow()