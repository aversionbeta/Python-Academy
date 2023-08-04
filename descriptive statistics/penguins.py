import empiricaldist
import janitor
import matplotlib.pyplot as plt
import numpy as np
import palmerpenguins
import pandas as pd
import scipy.stats as sp
import seaborn as sns
import sklearn.metrics
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats as ss
import session_info

penguin_color = {
    'Adelie': '#ff6602ff',
    'Gentoo': '#0f7175ff',
    'Chinstrap': '#c65dc9ff'
}

raw_df= palmerpenguins.load_penguins_raw()
processed_df=palmerpenguins.load_penguins()
raw_df.transpose()
processed_df.transpose()

adelie_df = processed_df.query("species == 'Adelie'")
gentoo_df = processed_df.query("species == 'Gentoo'")
chinstrap_df = processed_df.query("species == 'Chinstrap'")
specie = [adelie_df,gentoo_df,chinstrap_df]
specie

numeric_columns = processed_df.select_dtypes(include=np.number).columns
numeric_columns = numeric_columns.drop('year')
numeric_columns


species = processed_df.species.unique()
species

categories = processed_df.select_dtypes(include=object).keys()
categories

fig, axes = plt.subplots(3, 4, figsize= (12,9))
fig.suptitle('Normal distribution with Probability density distribution')
for i, i_col in enumerate(specie):
    for j, j_col in enumerate(numeric_columns):
        stats = i_col[j_col].describe()

        xs = np.linspace(stats['min'],stats['max']) 
        ys = sp.norm(stats['mean'], stats['std']).pdf(xs)

        axes[i][j].plot(xs,ys, color='black',linestyle='--')

        sns.kdeplot(
            ax = axes[i][j],
            data = i_col,
            x=j_col,
            hue='species',
            palette=penguin_color
        ) 
plt.show()
        
sns.jointplot(
data=processed_df,
x='bill_length_mm',
y='bill_depth_mm',
palette=penguin_color,
hue='species')

plt.show()

sns.scatterplot(
    data=processed_df,
    x='bill_length_mm',
    y='bill_depth_mm',
    alpha = 1/2, #transparencia
    s=100 #tamaño de los puntos
)
plt.show()

sns.displot(
    data= processed_df,
    x='bill_length_mm',
    y='bill_depth_mm',
    rug=True, #muestra una linea de distribucion para cada variable,
    kind='kde'
)
plt.show()

sns.displot(
    data= processed_df,
    x='bill_length_mm',
    y='bill_depth_mm',
    rug=True #muestra una linea de distribucion para cada variable
)
plt.show()

sns.scatterplot(
    data=processed_df,
    x='species',
    y='flipper_length_mm',
    hue='species',
    palette=penguin_color
)
plt.show()

sns.stripplot(
    data=processed_df,
    x='flipper_length_mm',
    y='species',
    color='.3'
)
sns.boxplot(
    data=processed_df,
    x='flipper_length_mm',
    y='species',
    hue='species',
    palette=penguin_color
)
plt.show()

sns.violinplot(
    data=processed_df,
    x='species',
    y='flipper_length_mm',
    color='.8'
)

sns.stripplot(
    data=processed_df,
    x='species',
    y='flipper_length_mm',
    palette=penguin_color
)

plt.show()

sns.swarmplot(
    data=processed_df,
    x='species',
    y='flipper_length_mm',
    palette=penguin_color
)

plt.show()

