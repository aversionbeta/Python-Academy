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

#Numerical data scaling

import timeit as tm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model 

X,y = datasets.load_diabetes(return_X_y=True)
raw = X[:, None, 2]

#Scaling model

max_raw = max (raw)
min_raw = min (raw)
scaled = (2*raw - max_raw - min_raw) / (max_raw - min_raw)

fig, axs = plt.subplots(2,1, sharex=True)
axs[0].hist(raw)
axs[1].hist(scaled)
plt.show()

#Training model 
def train_raw():
    linear_model.LinearRegression().fit(raw,y)

def train_scaled():
    linear_model.LinearRegression().fit(scaled,y)

raw_time = tm.timeit(train_raw, number=100)
scaled_time = tm.timeit(train_scaled, number=100)
print('train raw : {}'.format(raw_time))
print('train raw : {}'.format(scaled_time))

#Non lineal transformations 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = []
df = pd.read_csv('descriptive statistics\datasetcars.csv')
df.price_usd.hist()
p=10000
plt.show()
df.price_usd.apply(lambda x: np.tanh(x/p)).hist()
plt.show()

#Categoric variables
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.preprocessing as skpre
df = []
df = pd.read_csv('descriptive statistics\datasetcars.csv')
pd.get_dummies(df['engine_type']) #onehot
encoder = skpre.OneHotEncoder(handle_unknown='ignore')
encoder.fit(df[['engine_type']].values)
encoder.transform([['gasoline'],['diesel'],['aceite']]).toarray()

#Covariance Matrix

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

iris = sns.load_dataset('iris')
iris.columns
scaler = StandardScaler()
scaled = scaler.fit_transform(iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
scaled.T
covariance_matrix = np.cov(scaled.T)
print(covariance_matrix)
plt.figure(figsize=(10,10))
sns.set(font_scale=1.5)
hm = sns.heatmap(covariance_matrix,
                    cbar=True,
                    annot=True,
                    square=True,
                    fmt='.2f',
                    annot_kws={'size':12},
                    yticklabels=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
                    xticklabels=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
plt.show()

#Principal Components Analysis PCA 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = sns.load_dataset('iris')
iris.columns
scaler = StandardScaler()
scaled = scaler.fit_transform(iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
scaled.T
covariance_matrix = np.cov(scaled.T)
print(covariance_matrix)
sns.jointplot(x=iris['petal_length'], y=iris['petal_width'])
sns.jointplot(x=scaled[:,2], y=scaled[:,3])
eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
print(eigen_values)
print(eigen_vectors)
variance_explained = []
for i in eigen_values:
    variance_explained.append((i/sum(eigen_values))*100)
print(variance_explained)

pca = PCA(n_components=2)
pca.fit(scaled)
pca.explained_variance_ratio_
reduced_scaled = pca.transform(scaled)
print(reduced_scaled)
iris['pca_1'] = scaled[:,0]
iris['pca_2'] = scaled[:,1]
sns.jointplot(iris['pca_1'],iris['pca_2'], hue = iris['species'])
plt.show()
