# Process Quality KPI Reporting Automation

A production-inspired portfolio project that automates the extraction, preparation, and weekly export of Process Quality task data for KPI reporting.

The workflow uses **SQLite, SQL, Python, Pandas, OpenPyXL, and Excel formulas** to transform operational task records into structured team-level reports and performance insights.

The solution is designed to run automatically every Monday at **12:00 PM Europe/Dublin time** through a notebook platform’s built-in scheduler.

All task records, employee names, team names, tags, and performance figures in this repository are fictional and were created specifically for demonstration purposes.

---

## Project Overview

Process Quality teams often need to report on:

- completed task volumes;
- task volumes by task type;
- team performance;
- SLA performance;
- weekly performance changes;
- task distribution across operational teams.

The underlying task system may contain work completed by people from several teams, roles, or companies. Reporting therefore cannot rely only on a task tag or only on the person who completed the task.

This project recreates a workflow in which:

1. completed tasks are extracted from a centralized data source;
2. task type is identified from task tags;
3. reporting team is identified using both the team tag and agent name;
4. SLA results are derived from a system-generated tag;
5. prepared task-level data is exported into team-specific Excel tabs;
6. existing Excel formulas calculate weekly KPIs and performance comparisons;
7. the workflow is scheduled to run automatically every Monday.

---

## Business Problem

The reporting process previously required repeated manual work to:

- extract completed operational tasks;
- identify tasks completed during the required reporting period;
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

This project demonstrates how the data-extraction and preparation stages can be automated while keeping KPI calculations visible and editable in Excel.

---

## Solution

The project separates the workflow into three parts.

### SQL

SQL is responsible for:

- querying the simulated centralized task system;
- selecting closed tasks;
- filtering the two most recently completed Monday-to-Sunday weeks;
- excluding the current incomplete week;
- joining tasks with their tags;
- combining multiple tags into one extracted field.

### Python

Python is responsible for:

- connecting to the SQLite database;
- executing the extraction query;
- preparing the results in Pandas;
- identifying task types from tags;
- identifying the correct reporting team;
- filtering tasks using both the team tag and agent name;
- classifying SLA results;
- updating the team-specific Excel tabs.

### Excel

Excel is responsible for:

- combining the team-level data;
- counting completed tasks;
- counting tasks by type;
- calculating SLA compliance;
- calculating week-over-week changes;
- comparing team performance;
- presenting management-ready KPI summaries.

The workbook’s `All Data` and `Summary` tabs contain manually maintained formulas. The Python workflow preserves these tabs and updates only the team-level task data.

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
Task-type identification
                ↓
Agent and team-tag filtering
                ↓
SLA classification
                ↓
Team-level Excel tabs updated
                ↓
Existing All Data formulas
                ↓
Existing Summary KPI formulas
                ↓
Weekly performance insights
```

---

## Automated Schedule

The workflow is intended to run automatically every:

```text
Monday at 12:00 PM
Timezone: Europe/Dublin
```

Scheduling is handled through the notebook platform’s built-in scheduler.

The scheduling logic is not implemented inside the Python modules. Instead:

1. the notebook imports and starts the workflow;
2. the notebook platform stores the weekly schedule;
3. the scheduler runs the notebook every Monday at 12:00 PM;
4. the notebook executes the same modular Python workflow used locally.

A notebook execution cell can call:

```python
from src.run_workflow import run_workflow

run_workflow()
```

This design keeps the reporting logic separate from the scheduling platform.

```text
Notebook scheduler
        ↓
Monday at 12:00 PM
        ↓
run_workflow()
        ↓
SQL extraction
        ↓
Python preparation
        ↓
Excel team-tab update
```

The reporting-period logic is calculated dynamically in SQL, so the workflow extracts the correct two completed reporting weeks regardless of the exact day or time it is executed.

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

For example, when the workflow runs on Monday, the extracted period contains:

- the full week that ended the previous day;
- the full week immediately before it.

This provides two complete weekly datasets for week-over-week comparison.

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

This prevents work completed by unrelated teams, roles, or companies from being included incorrectly.

---

## Task Types

Task type is identified from task tags.

The project uses four fictional Process Quality task types:

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

## Example Insights

The sample report demonstrates several week-over-week changes:

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
- SLA compliance change;
- task-type distribution.

---

## Excel Workbook

The existing Excel workbook contains:

```text
Summary
All Data
Team Alpha
Team Beta
Team Gamma
Team Delta
Team Epsilon
```

### Team tabs

Each team tab contains task-level data with the following columns:

| Column | Description |
|---|---|
| Team | Reporting team |
| Task Type | Task category derived from tags |
| Task ID | Unique task identifier |
| Created Date | Date and time the task was created |
| Completed Date | Date and time the task was closed |
| SLA Breached | `Yes`, `No`, or `N/A` |

### Protected formula tabs

The Python workflow does not write to:

```text
All Data
Summary
```

These tabs contain manually created Excel formulas and reporting logic.

The workflow:

- opens the existing workbook;
- preserves the `All Data` tab;
- preserves the `Summary` tab;
- updates only columns `A:F` in the team tabs;
- preserves content outside the team data area;
- saves the updated workbook back to the same output file.

The `All Data` formulas combine records from all team tabs.

The `Summary` formulas calculate metrics such as:

- total completed tasks;
- task volumes by type;
- task volumes by team;
- SLA breaches;
- SLA-met tasks;
- SLA compliance percentage;
- week-over-week task-volume change;
- week-over-week percentage change;
- team-level SLA change;
- task-type volume share.

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
├── notebooks/
│   └── kpi_reporting_workflow.ipynb
│
├── output/
│   └── operations_kpi_report_<date-range>.xlsx
│
├── docs/
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

- opening the existing KPI workbook;
- preserving `All Data`;
- preserving `Summary`;
- updating the five team tabs;
- clearing and replacing only columns `A:F`;
- maintaining team-level Excel tables;
- formatting task data;
- saving the updated workbook.

### `src/run_workflow.py`

Runs the complete process:

```text
extract
→ prepare
→ filter
→ update team tabs
→ save workbook
```

### `notebooks/kpi_reporting_workflow.ipynb`

Acts as the scheduled workflow entry point.

The notebook:

- imports the modular workflow;
- runs `run_workflow()`;
- is scheduled through the notebook platform;
- executes every Monday at 12:00 PM.

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

## Running the Project Locally

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

### 4. Update the Excel report

Close the existing Excel workbook before running:

```bash
python -m src.run_workflow
```

The workflow expects the completed workbook to already exist inside:

```text
output/
```

It updates the team tabs and preserves the workbook’s existing `All Data` and `Summary` formulas.

---

## Scheduled Execution

In the notebook environment, the workflow is started with:

```python
from src.run_workflow import run_workflow

run_workflow()
```

The notebook’s built-in scheduler is configured for:

```text
Frequency: Weekly
Day: Monday
Time: 12:00 PM
Timezone: Europe/Dublin
```

This demonstrates how the workflow can operate as a recurring reporting process rather than requiring a person to run each module manually every week.

---

## Technologies Used

- Python
- SQL
- SQLite
- Pandas
- OpenPyXL
- Microsoft Excel
- Excel formulas
- Scheduled notebooks
- Git
- GitHub
- Visual Studio Code

---

## Skills Demonstrated

This project demonstrates practical experience with:

- workflow automation;
- scheduled automation;
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
- Excel report maintenance;
- formula preservation;
- weekly performance reporting;
- week-over-week analysis;
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
- additional Excel charts;
- Power BI integration;
- duplicate-task validation;
- automated data-quality checks;
- unit tests;
- workflow logging;
- configurable reporting periods;
- automated email delivery;
- report archiving;
- failure notifications for scheduled runs.

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
- scheduled workflows;
- continuous improvement.