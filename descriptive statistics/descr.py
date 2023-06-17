import pandas as pd
df = []
df = pd.read_csv('descriptive statistics\datasetcars.csv')
print(df)
print(df.dtypes) 
print(df.describe())
print(df.median())

#Dispersion Meausures
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = []
df = pd.read_csv('descriptive statistics\datasetcars.csv')
df['price_usd'].std()
rango = df['price_usd'].max()-df['price_usd'].min()
print(rango)
Q1 = df['price_usd'].quantile(q=0.25)
print(Q1)
Q3 = df['price_usd'].quantile(q=0.75)
min_val = df['price_usd'].quantile(q=0)
print(min_val)
max_val = df['price_usd'].quantile(q=1)
print(max_val)
IQR = Q3 - Q1
print(IQR)
minlimit = Q1 - IQR
maxlimit = Q3 - IQR
print(minlimit, maxlimit)
sns.boxplot(df['price_usd'])
plt.show()
sns.histplot(df['price_usd'])
plt.show()
sns.boxplot(x= 'engine_fuel', y = 'price_usd', data = df)
plt.show()

#visualizations
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = []
iris = sns.load_dataset('iris')
print(iris.head())
sns.scatterplot(data=iris, x='sepal_length', y='petal_length', hue='species')
plt.show()
sns.jointplot(data=iris, x='sepal_length', y='petal_length', hue='species')
plt.show()
sns.boxplot(data=iris, x='sepal_length', hue='species')
plt.show()
sns.barplot(data=iris, x='species', y='petal_length')
plt.show()
