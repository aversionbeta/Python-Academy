import janitor
import numpy as np
import pandas as pd
import missingno
from sklearn import datasets
import seaborn as sns

riskfactors_df = datasets.load_diabetes(as_frame=True).frame

riskfactors_df=riskfactors_df.isna().replace({ #reemplaza los valores booleanos por valores adecuados
        False:"Not missing",
        True:"Missing"
    }).add_suffix("_NA").pipe(
        lambda shadow_matrix: pd.concat(  # concatena los valores de la matriz de sombra a la derecha del dataframe
            [riskfactors_df, shadow_matrix],
            axis="columns"
        )
    )
    
riskfactors_df


riskfactors_df=riskfactors_df.missing.bind_shadow_matrix(only_missing=True).pipe(
        lambda df: (
            sns.boxenplot(
                data=df,
                x = 'weight_lbs_NA', #variables con datos faltantes
                y = 'age'  #variable de comparacion
            )
        )
    )


riskfactors_df=riskfactors_df.missing.bind_shadow_matrix(only_missing=True).pipe(
        lambda df: (
            sns.displot(
                data=df,
                x = 'age', #variable de distribucion
                hue = 'weight_lbs_NA',  #variable de comparacion
                kind= 'kde' #distribucion de densidad
            )
        )
    )


riskfactors_df=riskfactors_df.missing.bind_shadow_matrix(only_missing=True).pipe(
        lambda df: (
            sns.displot(
                data=df,
                x = 'age', #variable de distribucion
                col = 'weight_lbs_NA',  #variable de comparacion
                facet_kws={
                    'sharey': False
                }               
            )
        )
    )


riskfactors_df=riskfactors_df.missing.bind_shadow_matrix(only_missing=True).pipe(
        lambda df: (
            sns.displot(
                data=df,
                x = 'age', #variable de distribucion
                col = 'marital_NA',  #variable de comparacion
                row = 'weight_lbs_NA'               
            )
        )
    )

# funcion que añade valores aleatorios a las variables con valores faltantes
# para visualizarlos en un eje
def column_fill_with_dummies(
    column: pd.Series,
    proportion_below: float=0.10, #Proporcion de los datos en la grafica 
    jitter: float=0.075,  # evita el asolapamiento de los puntos en la grafica
    seed: int=42, #semilla para la aleatoriedad
) -> pd.Series: # la funcion retorna una serie

    #Copiar las columnas del dataframe
    column = column.copy(deep=True)

    #Extraer los valores de las variables
    missing_mask = column.isna() # matriz de booleanos
    number_missing_values = missing_mask.sum() #conteo de valores faltantes
    column_range = column.max() - column.min() #rango de las variables

    # shift data
    column_shift = column.min() - column.min() * proportion_below

    # crear un poco de ruido alrededor de los puntos 
    np.random.seed(seed)
    column_jitter = (np.random.rand(number_missing_values) - 2) * column_range * jitter

    #Guardar los nuevos datos aleatorios
    column[missing_mask] = column_shift + column_jitter

    return column