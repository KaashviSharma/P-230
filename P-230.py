import pandas as pd
dataset = pd.read_csv(r'country_vaccinations.csv')
print('shape of the given dataset:',dataset.shape)
prnt('count of column:',len(dataset.columns))
print('name of parameter used:',dataset.columns)
print('display empty row data:',dataset.loc[:,dataset.isna().any()])