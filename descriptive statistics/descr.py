import pandas as pd

df = pd.read_csv('descriptive statistics\datasetcars.csv')
print(df)
print(df.dtypes) 
print(df.describe())
print(df.median())