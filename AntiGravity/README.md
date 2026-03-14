# VWO Login Dashboard — Enterprise Test Plan (AntiGravity / Gemini CLI)

## Overview
This folder contains an **enterprise-grade Test Plan** for the VWO Login Dashboard (`app.vwo.com`), generated using **Google Gemini CLI (AntiGravity)**. The Test Plan is strictly derived from the provided Product Requirements Document (PRD) with zero external assumptions.

## Output
| File | Description |
|------|-------------|
| `Test_Plan_app.vwo.com.xlsx` | Final Test Plan Excel with 12 color-coded tabs |

### Test Plan Tabs
| # | Tab Name | Tab Color |
|---|----------|-----------|
| 1 | Objective | 🟡 Yellow |
| 2 | Scope | 🟢 Green |
| 3 | Inclusions | 🟠 Orange |
| 4 | Exclusions | ⚪ Grey |
| 5 | Test Environments | 🔵 Blue |
| 6 | Defect Reporting Procedure | 🔴 Red |
| 7 | Test Strategy | 🟠 Orange |
| 8 | Test Schedule | 🔵 Blue |
| 9 | Test Deliverables | 🟢 Green |
| 10 | Entry and Exit Criteria | ⚪ White |
| 11 | Tools | 🟡 Yellow |
| 12 | Risks and Mitigations | 🔴 Red |

## Key Features
- **Headers**: Blue background with white bold text across all tabs.
- **Tab Colors**: Distinct color coding per tab for quick navigation.
- **Auto-sized Columns**: Columns auto-adjusted for readability.
- **PRD-Only Data**: All content strictly sourced from the VWO Login Dashboard PRD.

## Tools Used
- **JIRA** — Bug tracking
- **Screenshot/Snipping Tools** — Evidence capture
- **Word/Excel** — Documentation

## How It Was Generated
1. PRD text extracted via `pypdf` → `prd_text.txt`
2. Example Test Plan structure analyzed from `VWO_Login_TestPlan.xlsx`
3. Test Plan Excel generated and styled via `pandas` + `openpyxl`

## Helper Scripts
| Script | Purpose |
|--------|---------|
| `generate_styled_test_plan.py` | Generates the final styled Excel Test Plan |
| `analyze_docs.py` | Extracts text from PRD PDF and structure from example Excel |
| `get_colors.py` | Extracts tab/header colors from the example Excel |

## Prompt
The RICE-POT prompt used to generate this Test Plan is in `Prompt_RICE_POT_TestPlan.txt`.

## AI Tool
**Google Gemini CLI (AntiGravity)**
