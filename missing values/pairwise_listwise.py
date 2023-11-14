import janitor
import numpy as np
import pandas as pd
import missingno
from sklearn import datasets
import seaborn as sns


riskfactors_df = datasets.load_diabetes(as_frame=True).frame

riskfactors_df.dropna(
        subset=['weight_lbs'], # indica la variable donde buscar los valores faltantes
        how='any' # any indica en cualquier registro que aparezca un valor faltante
    )

riskfactors_df.dropna(
        subset=['weight_lbs', 'height_inch'], # indica el parametro donde buscar los valores faltantes
        how='any' # algoritmo con el que eliminar los registros
    ).shape

riskfactors_df.dropna(
        subset=['weight_lbs', 'height_inch'], # indica el parametro donde buscar los valores faltantes
        how='all' # all indica los registros donde hayan valores faltantes en ambas variables
    ).shape

riskfactors_df.dropna(
        subset=['weight_lbs', 'height_inch'], # indica el parametro donde buscar los valores faltantes
        how='any' # any indica en cualquier registro que aparezca un valor faltante
    ).select_columns(['weight_lbs', 'height_inch']).pipe(missingno.matrix)

riskfactors_df.dropna(
        subset=['weight_lbs', 'height_inch'], # indica el parametro donde buscar los valores faltantes
        how='all' # algoritmo con el que eliminar los registros
    ).select_columns(['weight_lbs', 'height_inch']).pipe(missingno.matrix)