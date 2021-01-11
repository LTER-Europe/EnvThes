from gsheets import Sheets
import pandas as pd
import os
import json


client = json.loads(os.environ["CLIENT"])
storage = json.loads(os.environ["STORAGE"])

with open("client.json", "w") as json_file:
    json.dump(client, json_file, indent=4)

with open("storage.json", "w") as json_file:
    json.dump(storage, json_file, indent=4)


file_name = os.environ["FILE_NAME"]
sheet_id = os.environ["SHEET_ID"]
sheet_obj = Sheets.from_files("client.json", "storage.json")
sheet = sheet_obj.get(sheet_id)
sheet.sheets[0].to_csv(file_name + ".csv", encoding="utf-8", dialect="excel")
txt_delimiter = ","

largest_column_count = 0
with open(file_name + ".csv", "r") as temp_f:
    lines = temp_f.readlines()
    for l in lines:
        column_count = len(l.split(txt_delimiter)) + 1
        largest_column_count = (
            column_count
            if largest_column_count < column_count
            else largest_column_count
        )
temp_f.close()


column_names = [i for i in range(0, largest_column_count)]
df = pd.read_csv(
    file_name + ".csv", header=None, delimiter=txt_delimiter, names=column_names
)
df.to_excel(file_name + ".xlsx", index=False, header=False)

os.remove("client.json")
os.remove("storage.json")
