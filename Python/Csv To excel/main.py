import pandas as pd

read_file = pd.read_csv (r'test.csv')
read_file.to_excel (r'test.csv.xlsx', index = None, header=True)