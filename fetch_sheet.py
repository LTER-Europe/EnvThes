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




data_file = "taxonomy.csv"
sheet_id = '1zyEfkovkg66gWyzOgh8FucuE3CCVgHQCAjNEfx_kLmI'
sheet_obj = Sheets.from_files('client.json', 'storage.json')
sheet = sheet_obj.get(sheet_id)

sheet.sheets[0].to_csv(data_file, encoding='utf-8', dialect='excel')

data_file_delimiter = ','
largest_column_count = 0

with open(data_file, 'r') as temp_f:
    # Read the lines
    lines = temp_f.readlines()

    for l in lines:
        # Count the column count for the current line
        column_count = len(l.split(data_file_delimiter)) + 1

        # Set the new most column count
        largest_column_count = column_count if largest_column_count < column_count else largest_column_count

# Close file
temp_f.close()


column_names = [i for i in range(0, largest_column_count)]
df = pd.read_csv(data_file, header=None, delimiter=data_file_delimiter, names=column_names)
df.to_excel('taxonomy.xlsx',index=False)
