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

#Correlations

processed_df.corr()

sns.heatmap(
    processed_df.corr(),
    annot= True,
    cmap='coolwarm',
    center=0,
    vmin=-1,
    vmax=1,
    linewidths=0.5
)

plt.show()

sns.clustermap(
    processed_df.corr(),
    annot= True,
    cmap='coolwarm',
    center=0,
    vmin=-1,
    vmax=1,
    linewidths=0.5
)

plt.show()

processed_df= processed_df.assign(
    numeric_sex = lambda df: df.sex.replace(['female', 'male'],[0,1])
)

sns.clustermap(
    processed_df.corr(),
    annot= True,
    cmap='coolwarm',
    center=0,
    vmin=-1,
    vmax=1,
    linewidths=0.5
)

plt.show()

raw_df= palmerpenguins.load_penguins_raw()
processed_df=palmerpenguins.load_penguins()

np.random.seed(42)
x1 = np.linspace(0,100,100)
y1 = 0.1* x1 +3 + np.random.uniform(-2,2,size=x1.size)
x2 = np.linspace(0,100,100)
y2 = 0.5* x1 +1 + np.random.uniform(0,60,size=x2.size)

answ1=[]
answ2=[]
answ1 = sp.linregress( 
                            x=x1,
                            y=y1
                            )

answ2=sp.linregress(x=x2,y=y2
                            )

print(answ1,answ2, sep='\n')

sns.scatterplot(data=processed_df,
                x='bill_length_mm',
                y='bill_depth_mm')

plt.show()

answ_penguins = sp.linregress(
    x=processed_df.bill_length_mm,
    y=processed_df.bill_depth_mm
)

print(answ_penguins)
    
sns.lmplot(data=processed_df,
                x='bill_length_mm',
                y='bill_depth_mm',
                height=10)

plt.show()

x=processed_df.bill_length_mm,
y=processed_df.bill_depth_mm
answ_x_y=sp.linregress(x=x, y=y)
answ_y_x=sp.linregress(x=y, y=x)

print(answ_x_y, answ_y_x, sep='\n')

sns.lmplot(data=processed_df,
                x='bill_length_mm',
                y='bill_depth_mm')

sns.lmplot(data=processed_df,
                y='bill_length_mm',
                x='bill_depth_mm')


model_1 = (
    smf.ols(
        formula='body_mass_g ~ bill_length_mm',
        data=processed_df
    )
    .fit()
)

model_1.summary()

model_2 = (
    smf.ols(
        formula='body_mass_g ~ bill_length_mm + bill_depth_mm',
        data=processed_df
    )
    .fit()
)

model_2.summary()

model_3 = (
    smf.ols(
        formula='body_mass_g ~ bill_length_mm + bill_depth_mm + flipper_length_mm',
        data=processed_df
    )
    .fit()
)

model_3.summary()

model_4 = (
    smf.ols(
        formula='body_mass_g ~ bill_length_mm + bill_depth_mm + flipper_length_mm + C(sex)',
        data=processed_df
    )
    .fit()
)

model_4.summary()

model_5 = (
    smf.ols(
        formula='body_mass_g ~ flipper_length_mm + C(sex)',
        data=processed_df
    )
    .fit()
)

model_5.summary()

models_result = pd.DataFrame(
    dict(
        actual_value = processed_df.body_mass_g,
        prediction_model_1 = model_1.predict(),
        prediction_model_2 = model_2.predict(),
        prediction_model_3 = model_3.predict(),
        prediction_model_4 = model_4.predict(),
        prediction_model_5 = model_5.predict(),
        species=processed_df.species,
        sex=processed_df.sex
    )
)

models_result 

sns.ecdfplot(
    data=models_result
)

sns.ecdfplot(
    data=models_result.select_columns(['actual_value', 'prediction_model_5'])
)

sns.kdeplot(
    data=models_result,
    cumulative=True)

sns.lmplot(
    data=processed_df,
    x='flipper_length_mm',
    y='body_mass_g',
    hue='sex',
    height=10
)

smf.logit(
    formula='numeric_sex ~ flipper_length_mm + bill_length_mm + bill_depth_mm + C(island)',
    data=processed_df
).fit().summary()

(
    processed_df
    .value_counts(['island', 'sex'])
    .reset_index(name='count')
)

sns.pairplot(data=processed_df, hue='species')
plt.show()