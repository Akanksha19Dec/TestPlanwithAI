# TestPlanwithAI — VWO Login Test Plan Generator

This repository contains a small Python utility that generates an Excel test-plan workbook for the VWO Login Dashboard (app.vwo.com) using facts extracted from a product requirements document (PRD) and a simple test-plan template.

## Contents
- `generate_vwo_testplan_xlsx.py` — script that generates `VWO_Login_TestPlan.xlsx` with one sheet per test-plan section.
- `README_generate_testplan.md` — short usage notes and background on how the generator was created.

## Purpose
The generator produces a structured, human-readable test-plan workbook containing:
- Objective, Scope, Inclusions/Exclusions
- Test Environments and Tools
- Test Strategy, Schedule, Deliverables
- Verified Facts and a "Missing / Unknown Information" sheet that highlights gaps requiring inputs before executable test cases can be written.

The workbook is intended as a starting artefact for QA planning and stakeholder review.

## Prerequisites
- Python 3.8 or newer
- `openpyxl` (install via pip)

Install dependencies (PowerShell):
```powershell
python -m pip install --upgrade pip
pip install openpyxl
```

## Usage
1. Open a terminal and change to this repository folder.
2. Run the generator:
```powershell
python generate_vwo_testplan_xlsx.py
```
3. The script writes `VWO_Login_TestPlan.xlsx` to the current directory and prints the output path.

See the generator code for how sections and the "Missing / Unknown Information" sheet are populated.

## Output
- `VWO_Login_TestPlan.xlsx` — workbook with colored tabs for each test-plan section. It includes a `Verified Facts` sheet and a `Missing / Unknown Information` sheet that lists items required to create executable test cases (API docs, test accounts, SSO/MFA configuration, browser-version matrix, UI mocks, schedule, etc.).

## Next steps / How I can help
- If you provide the missing artifacts listed in the workbook (API endpoints, test credentials, password policy, SSO/MFA details, browser/OS matrix, UI mocks, timelines), I can extend the generator to produce:
  - Concrete test cases and steps
  - Automation-ready test scripts (skeleton)
  - A scheduled test run plan with owners and dates
- If you'd like, I can also convert the workbook into a CSV/Markdown test-case set or scaffold a simple automated test suite.

## References
- Generator script: [generate_vwo_testplan_xlsx.py](generate_vwo_testplan_xlsx.py)
- Additional notes: [README_generate_testplan.md](README_generate_testplan.md)

---
If you want me to proceed and populate test cases, tell me which missing items you can provide and I will update the generator accordingly.
