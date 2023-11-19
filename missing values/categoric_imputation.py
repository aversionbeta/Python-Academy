import pandas as pd
from sklearn import preprocessing
from sklearn import datasets
import missingno
import matplotlib.pyplot as plt
import sklearn.impute
import statsmodels.formula.api as smf
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge
import seaborn as sns

riskfactors_df = datasets.load_diabetes(as_frame=True).frame

label_encoder = preprocessing.LabelEncoder()

encoder_gender = label_encoder.fit_transform(riskfactors_df.gender)
riskfactors_df.gender = encoder_gender

riskfactors_df.head()

# Imputation by interpolation

plt.figure(figsize=(20, 10))

(
    riskfactors_df
    .select_dtypes(include='number')  # Assuming 'ozone' is a numerical column
    .pipe(
        lambda df: (
            df.interpolate(method='linear').plot(
                color='red',
                marker='o',
                alpha=6 / 9,
                linestyle='dashed'
            ),
            df.plot(
                color='#313638',
                marker='o'
            )
        )
    )
)

# Imputer with knn
knn_imputer = sklearn.impute.KNNImputer()

# Copy the dataframe, order variables by the amount of missing values in ascending order
riskfactors_df_knn = riskfactors_df.missing.sort_values(by='ozone', ascending=True).copy(deep=True)

# Add imputed values to the new dataframe, adjust data ordered by the amount of missing variables, round values
riskfactors_df_knn.iloc[:, :] = knn_imputer.fit_transform(
    riskfactors_df.missing.sort_values(by='ozone', ascending=True).copy(deep=True)
).round()

riskfactors_df_knn

# Shadow matrix
(
    pd.concat(
        [
            riskfactors_df_knn,
            riskfactors_df.missing.create_shadow_matrix2(True, False, suffix='_imp', only_missing=True)
        ],
        axis=1
    )
    .missing.scatter_imputation_plot(
        x='height',
        y='weight'
    )
)

# Imputation based on models

riskfactors_model_df = (
    riskfactors_df
    .select_columns('height', 'weight', 'gender', 'age')  # Select columns
    .sort_values(by='height')  # Sort by height
    .transform_column(
        'weight',  # Variable of interest
        lambda x: x.ffill(),
        elementwise=False
    )
    .missing.bind_shadow_matrix2(
        True,
        False,
        suffix='_imp',
        only_missing=False
    )
)

riskfactors_model_df

# Linear regression model
height_ols = (
    riskfactors_model_df
    .pipe(
        lambda df: smf.ols('height ~ weight + gender + age', data=df)
    )
    .fit()
)

# Get observations with missing values in the 'height' variable
(
    riskfactors_model_df
    .pipe(
        lambda df: df[df.height.isna()]
    )
)

# Use the model to generate imputed values
ols_imputed_values = (
    riskfactors_model_df
    .pipe(
        lambda df: df[df.height.isna()]
    )
    .pipe(
        lambda df: height_ols.predict(df).round()
    )
)

ols_imputed_values

# Replace the imputed values generated with the model in the associated variable
riskfactors_model_df.loc[riskfactors_model_df.height.isna(), ['height']] = ols_imputed_values

riskfactors_model_df

(
    riskfactors_model_df
    .missing
    .scatter_imputation_plot(
        x='weight',
        y='height'
    )
)

# Create copies, analyze them, and return a single dataset.
# You can also request to return all copies.

mice_imputer = IterativeImputer(
    estimator=BayesianRidge(),
    initial_strategy='mean',
    imputation_order='ascending'
)

# Create a copy of the transformed data
riskfactors_mice_df = riskfactors_df.copy(deep=True)

# Fit and transform the data
riskfactors_mice_df.iloc[:, :] = mice_imputer.fit_transform(riskfactors_df).round()

riskfactors_mice_df

# Shadow matrix for visualization
riskfactors_mice_df = pd.concat(
    [
        riskfactors_mice_df,
        riskfactors_df.missing.create_shadow_matrix2(
            True,
            False,
            only_missing=False,
            suffix='_imp',
        )
    ],
    axis=1
)

# Visualization of the 'height' and 'weight' variables
riskfactors_mice_df.missing.scatter_imputation_plot(
    x='height',
    y='weight'
)

sns.jointplot(
    data=riskfactors_df,
    x='height',
    y='weight',
    hue='gender',
    kind='scatter'
)
sns.jointplot(
    data=riskfactors_mice_df,
    x='height',
    y='weight',
    hue='gender',
    kind='scatter'
)
(
    riskfactors_mice_df
    .missing.scatter_imputation_plot(
        x='height',
        y='weight',
        show_marginal=True
    )
)

# Create a copy of the dataframe
riskfactors_imputed_df = riskfactors_mice_df.copy(deep=True)

# Check the named transformers
categorical_transformer.named_transformers_

--> {'ordinalencoder': OrdinalEncoder(), 'remainder': 'passthrough'}

# In this case, it is ordinal encoder
ordinalencoder_transformer = categorical_transformer.named_transformers_['ordinalencoder']

# Variables are stored in categorical_columns
categorical_columns = ['general_health_condition']  # replace this with your actual categorical columns

# Inverse transform using ordinal encoder
riskfactors_imputed_df[categorical_columns] = ordinalencoder_transformer.inverse_transform(
    X=riskfactors_mice_df[categorical_columns]
)

riskfactors_imputed_df

# Count for each category of the health condition. Values without imputation
riskfactors_df.general_health_condition.value_counts()

# Count for each category of the health condition. Imputed values
riskfactors_imputed_df.general_health_condition.value_counts()

riskfactors_imputed_df.missing.number_missing()
