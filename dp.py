import pandas as pd

data=pd.read_csv('dataset.csv')

data_wo_dp=data.drop_duplicates(subset='column_name',keep='first')

print(data_wo_dp)
