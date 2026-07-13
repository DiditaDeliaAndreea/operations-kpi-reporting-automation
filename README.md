# Process Quality KPI Reporting Automation

A production-inspired portfolio project that automates the extraction, preparation, and export of Process Quality task data for weekly KPI reporting.

The workflow uses **SQLite, SQL, Python, Pandas, OpenPyXL, and Excel formulas** to transform operational task records into structured team-level reports and performance insights.

All task records, employee names, team names, tags, and performance figures in this repository are fictional and were created for demonstration purposes.

---

## Project Overview

Process Quality teams often need to report on:

- completed task volumes;
- task volumes by task type;
- team performance;
- SLA performance;
- weekly performance changes;
- task distribution across operational teams.

The underlying task system may contain work completed by people from multiple teams, roles, or companies. This means that reporting cannot rely only on a task tag or only on the name of the person who completed the task.

This project recreates a reporting workflow in which:

1. completed tasks are extracted from a centralized data source;
2. task type is identified from task tags;
3. reporting team is identified using both the team tag and agent name;
4. SLA results are derived from a system-generated tag;
5. prepared task-level data is exported to Excel;
6. Excel formulas calculate weekly KPIs and week-over-week comparisons.

---

## Business Problem

The original reporting process required repeated manual work to:

- extract completed operational tasks;
- identify tasks completed during the reporting period;
- review team-specific tags;
- check which agent completed each task;
- separate tasks into team-level reports;
- classify tasks by type;
- identify SLA breaches;
- calculate weekly performance metrics;
- compare performance with the previous week.

A manual process can be:

- time-consuming;
- repetitive;
- vulnerable to inconsistent filtering;
- difficult to scale;
- prone to reporting errors.

The purpose of this project is to demonstrate how the data-preparation portion of that workflow can be automated while keeping KPI calculations visible and editable in Excel.

---

## Solution

The project separates the workflow into two parts.

### Python and SQL

Python and SQL are responsible for:

- creating a simulated operational database;
- extracting completed tasks;
- filtering the two most recently completed Monday-to-Sunday weeks;
- combining task tags;
- identifying task type;
- identifying the correct reporting team;
- classifying SLA results;
- preparing structured reporting data;
- exporting the data to Excel.

### Excel

Excel is responsible for:

- counting completed tasks;
- counting tasks by task type;
- calculating SLA compliance;
- calculating week-over-week changes;
- comparing team performance;
- presenting management-ready KPI summaries.

This matches the original workflow, where Excel formulas were used for the final KPI calculations.

---

## Workflow

```text
Simulated centralized task system
                ↓
SQLite database
                ↓
SQL extraction
                ↓
Two completed reporting weeks
                ↓
Pandas data preparation
                ↓
Task type identification
                ↓
Agent and team-tag filtering
                ↓
SLA classification
                ↓
Team-level Excel tabs
                ↓
Excel KPI formulas
                ↓
Weekly performance insights
```

---

## Reporting Period

The SQL query extracts tasks from the two most recently completed calendar weeks.

Each reporting week runs from:

```text
Monday 00:00
through
Sunday 23:59:59
```

The current incomplete week is excluded.

The reporting period is calculated directly in SQL, so the workflow returns the correct completed weeks regardless of which day it runs.

---

## Team Structure

The demonstration dataset contains:

- 5 Process Quality teams;
- 10 fictional agents;
- 2 agents assigned to each team.

| Team | Agents |
|---|---|
| Team Alpha | Alex Morgan, Jamie Lee |
| Team Beta | Taylor Smith, Jordan Patel |
| Team Gamma | Morgan Reed, Casey Brown |
| Team Delta | Riley Davis, Cameron Wilson |
| Team Epsilon | Avery Clark, Quinn Lewis |

Each team also has a team-specific task tag:

| Team | Task tag |
|---|---|
| Team Alpha | `team_alpha` |
| Team Beta | `team_beta` |
| Team Gamma | `team_gamma` |
| Team Delta | `team_delta` |
| Team Epsilon | `team_epsilon` |

A task is included in a team report only when both conditions are met:

1. the task contains the relevant team tag;
2. the agent who completed the task belongs to that team.

This helps exclude work completed by people from unrelated teams, roles, or companies.

---

## Task Types

Task type is identified from task tags.

The project uses four fictional Process Quality task types.

| Task-type tag | Reporting name |
|---|---|
| `task_type_quality_review` | Quality Review |
| `task_type_complex_case` | Complex Case Review |
| `task_type_process_exception` | Process Exception Investigation |
| `task_type_priority_escalation` | Priority Escalation Review |

These names are fictional but represent realistic categories of work that a Process Quality team may perform.

---

## SLA Logic

Only **Priority Escalation Review** tasks are subject to SLA tracking.

The simulated source system automatically applies the following tag when the SLA has been exceeded:

```text
sla_exceeded
```

The Python workflow does not recreate the internal SLA timing logic. It consumes the SLA result already recorded by the source system.

The exported `SLA Breached` field is classified as follows:

| Condition | SLA Breached |
|---|---|
| Priority Escalation Review with `sla_exceeded` | `Yes` |
| Priority Escalation Review without `sla_exceeded` | `No` |
| Any task type without an SLA | `N/A` |

---

## Demonstration Dataset

The SQLite database contains 100 fictional completed task records across two reporting weeks.

| Reporting period | Completed tasks |
|---|---:|
| Older completed week | 44 |
| Recent completed week | 56 |
| Total | 100 |

The dataset was intentionally designed to produce meaningful performance comparisons rather than identical weekly results.

### Task volumes

| Task type | Older week | Recent week | Change |
|---|---:|---:|---:|
| Quality Review | 11 | 15 | +4 |
| Complex Case Review | 10 | 13 | +3 |
| Process Exception Investigation | 9 | 12 | +3 |
| Priority Escalation Review | 14 | 16 | +2 |

### SLA results

| SLA metric | Older week | Recent week |
|---|---:|---:|
| SLA breaches | 7 | 5 |
| SLA met | 7 | 11 |
| SLA compliance | 50.0% | 68.8% |

---

## Key Insights Demonstrated

The sample report shows several positive week-over-week changes:

- total completed tasks increased from 44 to 56;
- overall task volume increased by 27.3%;
- Quality Reviews increased by 36.4%;
- Complex Case Reviews increased by 30.0%;
- Process Exception Investigations increased by 33.3%;
- Priority Escalation Reviews increased by 14.3%;
- SLA breaches decreased from 7 to 5;
- SLA-met tasks increased from 7 to 11;
- SLA compliance improved from 50.0% to 68.8%.

The workbook also supports team-level comparisons for:

- task volume;
- week-over-week volume change;
- SLA compliance;
- SLA compliance change.

---

## Excel Output

The generated workbook contains:

```text
Summary
All Data
Team Alpha
Team Beta
Team Gamma
Team Delta
Team Epsilon
```

### Team-tab columns

Each team tab contains the following task-level data:

| Column | Description |
|---|---|
| Team | Reporting team |
| Task Type | Task category derived from tags |
| Task ID | Unique task identifier |
| Created Date | Date and time the task was created |
| Completed Date | Date and time the task was closed |
| SLA Breached | `Yes`, `No`, or `N/A` |

### Excel KPI calculations

The example workbook uses formulas to calculate:

- total completed tasks;
- completed tasks by task type;
- completed tasks by team;
- SLA breaches;
- SLA-met tasks;
- SLA compliance percentage;
- Priority Escalation volume share;
- week-over-week task-volume change;
- week-over-week percentage change;
- team-level SLA change;
- recent task-type volume share.

The KPI calculations are intentionally completed in Excel rather than Python so that they remain visible, editable, and easy to review.

---

## Project Structure

```text
operations-kpi-reporting-automation/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── operations.db
│
├── sql/
│   ├── create_tables.sql
│   ├── seed_data.sql
│   └── extract_completed_tasks.sql
│
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── extract_tasks.py
│   ├── prepare_reporting_data.py
│   ├── team_mapping.py
│   ├── excel_report.py
│   └── run_workflow.py
│
├── output/
│   └── operations_kpi_report_<date-range>.xlsx
│
├── docs/
├── notebooks/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## File Responsibilities

### `sql/create_tables.sql`

Creates the SQLite tables used to store:

- task records;
- task tags.

### `sql/seed_data.sql`

Generates the fictional demonstration dataset.

The data includes:

- 100 completed tasks;
- two reporting weeks;
- five teams;
- ten agents;
- four task types;
- different team volumes;
- different weekly task volumes;
- different SLA outcomes.

### `sql/extract_completed_tasks.sql`

Extracts:

- closed tasks only;
- tasks completed during the two most recently completed weeks;
- task details;
- the agent who completed each task;
- all task tags combined into one field.

### `src/database.py`

Responsible for:

- creating the SQLite database;
- running the table-creation script;
- inserting the synthetic data;
- providing database connections.

### `src/extract_tasks.py`

Responsible for:

- reading the SQL extraction query;
- executing it against SQLite;
- loading the results into a Pandas DataFrame;
- parsing created and completed timestamps.

### `src/team_mapping.py`

Stores the workflow configuration for:

- five team names;
- ten agent names;
- team-specific tags;
- task-type tags;
- the SLA-eligible task type;
- the SLA breach tag.

### `src/prepare_reporting_data.py`

Responsible for:

- parsing task tags;
- identifying task type;
- identifying reporting team;
- checking both agent and team-tag conditions;
- classifying SLA results;
- creating reporting-week fields;
- preparing the final task-level dataset.

### `src/excel_report.py`

Responsible for:

- creating one final workbook;
- creating separate team tabs;
- writing task-level data;
- formatting headers;
- formatting dates;
- creating Excel tables;
- saving the report in the `output` folder.

### `src/run_workflow.py`

Runs the complete process:

```text
extract
→ prepare
→ filter
→ export
```

---

## Requirements

The project requires:

- Python 3.10 or later;
- Pandas;
- OpenPyXL;
- SQLite, included with Python.

Install the dependencies with:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
pandas
openpyxl
pytest
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/operations-kpi-reporting-automation.git
```

Open the project folder:

```bash
cd operations-kpi-reporting-automation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### 1. Create the database

```bash
python -m src.database
```

This creates:

```text
data/operations.db
```

### 2. Test the SQL extraction

```bash
python -m src.extract_tasks
```

This should return 100 completed task records.

### 3. Test the prepared data

```bash
python -m src.prepare_reporting_data
```

This applies:

- tag parsing;
- task-type identification;
- team filtering;
- SLA classification;
- reporting-period preparation.

### 4. Generate the Excel report

```bash
python -m src.run_workflow
```

The generated workbook will be saved in:

```text
output/
```

---

## Technologies Used

- Python
- SQL
- SQLite
- Pandas
- OpenPyXL
- Microsoft Excel
- Excel formulas
- Git
- GitHub
- Visual Studio Code

---

## Skills Demonstrated

This project demonstrates practical experience with:

- workflow automation;
- Process Quality reporting;
- KPI reporting;
- operational data analysis;
- SQL extraction;
- SQLite database design;
- relational data modelling;
- date-range filtering;
- Python modularization;
- Pandas data preparation;
- task-tag processing;
- team and agent mapping;
- business-rule implementation;
- SLA reporting;
- Excel report generation;
- Excel formulas;
- weekly performance reporting;
- week-over-week analysis;
- data visualization;
- Git version control;
- GitHub portfolio documentation.

---

## Data Privacy

This repository does not contain confidential company data.

The following were created specifically for this portfolio project:

- task records;
- task IDs;
- employee names;
- team names;
- task types;
- task tags;
- SLA results;
- reporting figures.

The workflow is inspired by professional reporting experience, but the implementation has been adapted into a fictional and portable demonstration.

---

## Potential Future Improvements

Potential future enhancements include:

- monthly KPI reporting;
- month-over-month comparisons;
- automated Excel charts;
- Power BI integration;
- duplicate-task validation;
- automated data-quality checks;
- unit tests;
- workflow logging;
- configurable reporting periods;
- scheduled execution;
- automated email delivery;
- report archiving.

---

## Author

**Delia Didita**

Portfolio project focused on:

- Python automation;
- SQL;
- data preparation;
- Process Quality;
- KPI reporting;
- operational reporting;
- continuous improvement.