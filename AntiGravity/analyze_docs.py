import pypdf
import pandas as pd
import os

pdf_path = r"c:\Users\akank\OneDrive\Documents\All_abt_AI\TestPlanwithAI\Product Requirements Document_ VWO Login Dashboard.pdf"
excel_path = r"c:\Users\akank\OneDrive\Documents\All_abt_AI\TestPlanwithAI\AntiGravity\VWO_Login_TestPlan.xlsx"
excel_path2 = r"c:\Users\akank\OneDrive\Documents\All_abt_AI\TestPlanwithAI\VS_GithubCopilot\VWO_Login_TestPlan.xlsx"

print("--- PDF CONTENT BEGIN ---")
try:
    reader = pypdf.PdfReader(pdf_path)
    for i, page in enumerate(reader.pages):
        print(f"Page {i+1}:")
        print(page.extract_text())
        print("-" * 20)
except Exception as e:
    print(f"Error reading PDF: {e}")
print("--- PDF CONTENT END ---")

print("--- EXCEL STRUCTURE BEGIN ---")
try:
    active_path = excel_path if os.path.exists(excel_path) else excel_path2
    xls = pd.ExcelFile(active_path)
    print("Sheets in", active_path, ":", xls.sheet_names)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(active_path, sheet_name=sheet_name, nrows=10)
        print(f"\nSheet '{sheet_name}' Header:", df.columns.tolist())
        if not df.empty:
            print("First row data:")
            row_dict = df.iloc[0].to_dict()
            for k, v in row_dict.items():
                print(f"  {k}: {v}")
except Exception as e:
    print(f"Error reading Excel: {e}")
print("--- EXCEL STRUCTURE END ---")
