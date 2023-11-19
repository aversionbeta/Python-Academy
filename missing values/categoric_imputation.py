from sklearn import preprocessing
from sklearn import datasets
import missingno
import matplotlib as plt
import pandas as pd

riskfactors_df = datasets.load_diabetes(as_frame=True).frame

label_encoder = preprocessing.LabelEncoder()

encoder_gender = label_encoder.fit_transform(riskfactors_df.gender)
riskfactors_df = encoder_gender

riskfactors_df.head()

#Imputation by interpolation

plt.figure(figsize=(20,10))

(
    airquality_df
    .select_columns('ozone')    # variable de interes
    .pipe(                      # graficamos los puntos del ozono
        lambda df: (
            df.ozone.interpolate(method = 'linear').plot(
                color='red',
                marker = 'o',
                alpha=6/9,
                linestyle='dashed'
            ),
            df.ozone.plot(
                color='#313638',
                marker='o'
            )
        )
    )
)

# imputador con knn
knn_imputer = sklearn.impute.KNNImputer()

# copia del df                        ordenamos las variables por la cantidad de missing de forma ascendente
nhanes_df_knn = nhanes_transformed_df.missing.sort_variables_by_missingness(ascending=True).copy(deep=True)

# agregamos los valores imputados al nuevo df         ajustamos los datos ordenados por la cantidad de variables faltantes                                                                              redondeamos valores   
nhanes_df_knn.iloc[:, :] = knn_imputer.fit_transform(nhanes_transformed_df.missing.sort_variables_by_missingness(ascending=True).copy(deep=True)).round()

nhanes_df_knn

(   # matriz de sombra
    pd.concat(
        [
            nhanes_df_knn,
            nhanes_df.missing.create_shadow_matrix2(True, False, suffix='_imp', only_missing=True)
        ],
        axis=1
    )   # visualizacion mediantes un scatterplot de dos variables numericas
    .missing.scatter_imputation_plot(
        x = 'height',
        y = 'weight'
    )
)

#Imputación  basada en modelos 

nhanes_model_df= (
    nhanes_df
    .select_columns('height', 'weight', 'gender', 'age')    # seleccionamos columnas
    .sort_values(by='height')   # ordenamos en funcion de height
    #   sustituir los valores faltantes con dummies
    .transform_column(  
        'weight',   # variable de interes
        lambda x: x.ffill(),
        elementwise = False
    )   #   matriz de sombra con el sufijo imp
    .missing.bind_shadow_matrix2(
        True,
        False,
        suffix='_imp',
        only_missing=False   # matriz de sombra para todas las variables
    )
)

nhanes_model_df

# para este ejemplo vamos a utilizar la regresion lineal como modelo

height_ols = (
    nhanes_model_df
    .pipe(
        lambda df: smf.ols('height ~ weight + gender + age', data=df)
    )
    .fit()
)

# obtener solo las observaciones con valores nulos en la variable height

(
    nhanes_model_df
    .pipe(
        lambda df: df[df.height.isna()]
    )
)

# utilizamos el modelo para generar los valores imputados

ols_imputed_values = (
    nhanes_model_df
    .pipe(
        lambda df: df[df.height.isna()]
    )
    # aplicamos el modelo. Los valores imputados se redondean debido a que son enteros
    .pipe( 
    lambda df: height_ols.predict(df).round()
    )
)

ols_imputed_values

# sustituimos los valores imputados generados con 
# el modelo en la variable asociada

nhanes_model_df.loc[nhanes_model_df.height.isna(), ['height']] = ols_imputed_values

nhanes_model_df

(
    nhanes_model_df
    .missing
    .scatter_imputation_plot(
        x = 'weight',   # variable independiente
        y = 'height'    # variable objetivo
    )
)