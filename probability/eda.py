import empiricaldist
import janitor
import matplotlib.pyplot as plt
import numpy as np
import palmerpenguins
import pandas as pd
import scipy.stats
import seaborn as sns
import sklearn.metrics
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats as ss
import session_info

#matplotlib inline
sns.set_style(style='whitegrid')
sns.set_context(context='notebook')
plt.rcParams['figure.figsize'] = (11, 9.4)

penguin_color = {
    'Adelie': '#ff6602ff',
    'Gentoo': '#0f7175ff',
    'Chinstrap': '#c65dc9ff'
}

df = palmerpenguins.load_penguins_raw()
    # preprocessed_df= palmerpenguins.load_penguins()
    # sns.load_dataset('penguins')
    # pd.read_csv('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv')


df.dtypes

df.dtypes.value_counts()

df.shape

df.isnull
df.isnull().any()
df.isnull().sum()
df.isnull().melt()
df.isnull().melt().pipe(lambda df: 
                        (sns.displot(
                            data=df,
                            y='variable',
                            hue='value',
                            multiple = 'fill'
                            )))

plt.show()

df.isnull().transpose()
df.dropna()
df.shape
df.info()
df.describe(include='all')
df.describe(include=[np.number])
df.describe(include=object)
df.Species.value_counts().plot(kind='bar')
plt.show()