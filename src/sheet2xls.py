import os
import requests
import sys
import pandas as pd

def getGoogleSeet(spreadsheet_id, outDir, outFile):
  
  url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv'
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

outDir = './'

os.makedirs(outDir, exist_ok = True)
filepath = getGoogleSeet(sheet_id, outDir, file_name + ".csv")

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
