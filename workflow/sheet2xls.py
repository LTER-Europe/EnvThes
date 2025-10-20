"""This file has been modified from its originally licensed version
by WillOnGit - see README.md at repository root for licence"""

from gsheets import Sheets
import pandas as pd
import os
import sys

# --- Environment variables ---
file_name = os.environ.get("FILE_NAME")
sheet_id = os.environ.get("SHEET_ID")
sheet_tab_name = os.environ.get("SHEET_TAB_NAME")  # new variable
google_api_key = os.environ.get("GOOGLE_API_KEY")

# --- Safety checks ---
if not all([file_name, sheet_id, google_api_key]):
    sys.exit("❌ Missing required environment variables (FILE_NAME, SHEET_ID, GOOGLE_API_KEY).")

sheets_service = Sheets.from_developer_key(google_api_key)
spreadsheet = sheets_service.get(sheet_id)

# --- Select sheet ---
selected_sheet = None
for s in spreadsheet.sheets:
    if s.title.strip().lower() == sheet_tab_name.strip().lower():
        selected_sheet = s
        break

if not selected_sheet:
    print(f"⚠️ Sheet tab '{sheet_tab_name}' not found in spreadsheet. Available tabs:")
    for s in spreadsheet.sheets:
        print(f" - {s.title}")
    sys.exit(1)

print(f"📄 Exporting tab '{selected_sheet.title}' from spreadsheet '{sheet_id}'")

# --- Export CSV ---
selected_sheet.to_csv(file_name + ".csv", encoding="utf-8", dialect="excel")

# --- Determine column count ---
txt_delimiter = ","
largest_column_count = 0
with open(file_name + ".csv", "r") as temp_f:
    for line in temp_f:
        column_count = len(line.split(txt_delimiter)) + 1
        largest_column_count = max(largest_column_count, column_count)

column_names = list(range(0, largest_column_count))
df = pd.read_csv(file_name + ".csv", header=None, delimiter=txt_delimiter, names=column_names)
df.to_excel(file_name + ".xlsx", index=False, header=False)

print(f"✅ Saved '{file_name}.xlsx' and '{file_name}.csv' successfully.")
