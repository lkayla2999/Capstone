import pandas as pd

excel_file_path = 'Lengthofstay2.xls'

# pandas dataframe
df = pd.read_excel(excel_file_path)

# Print the contents of the dataframe
print(df.head(3))
