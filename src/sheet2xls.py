import os
import requests
import sys
import pandas as pd

def getGoogleSheet(spreadsheet_id, spreadsheet_gid, outDir, outFile):
  
  if spreadsheet_gid is None:
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv'
  else:
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={spreadsheet_gid}'
  response = requests.get(url)
  if response.status_code == 200:
    filepath = os.path.join(outDir, outFile)
    with open(filepath, 'wb') as f:
      f.write(response.content)
      print('CSV file saved to: {}'.format(filepath))    
  else:
    print(f'Error downloading Google Sheet: {response.status_code}')
    sys.exit(1)


##############################################

file_name = os.environ['FILE_NAME']
sheet_id = os.environ["SHEET_ID"]
sheet_gid = os.getenv("SHEET_GID")

outDir = './'

os.makedirs(outDir, exist_ok = True)
filepath = getGoogleSheet(sheet_id, sheet_gid, outDir, file_name + ".csv")

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
print("column names = ", column_names)
df = pd.read_csv(
    file_name + ".csv", header=None, delimiter=txt_delimiter, names=column_names
)
df.to_excel(file_name + ".xlsx", index=False, header=False)

sys.exit(0); ## success
