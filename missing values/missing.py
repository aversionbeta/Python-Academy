import janitor
import numpy as np
import pandas as pd
import missingno
from sklearn import datasets

df = pd.read_csv(r"C:\Users\juand\Dropbox\Profesional\7. Delphus Lab\5. Delphus Lab Academy\Python-Academy\missing values\amazon.csv")
df

df.shape
df.dtypes
df.rating_count.unique()

df.select_dtypes(object).apply(pd.unique)

df.replace(
        to_replace={
            'product_id':{
                "NA":np.nan
            }
        }
    )

implicit_to_explicit_df = pd.DataFrame.from_dict(
    data={
        "name": ["lynn", "lynn", "lynn", "zelda"],
        "time": ["morning", "afternoon", "night", "morning"],
        "value": [350, 310, np.nan, 320]
    }
)

implicit_to_explicit_df

implicit_to_explicit_df.pivot_wider(
        index="name",        # variable nombre como filas
        names_from="time",   # variable time como columnas
        values_from="value"  # variable value como valores de la tabla
    )

implicit_to_explicit_df.value_counts(
        subset=["name"]   # cuenta los valores asociados a los nombres
    ).reset_index(name="n").query("n < 3")  # asigna n como indice del conteo # condicion a cumplir por n para que se muestre en la tabla

implicit_to_explicit_df.complete( #Función complete con ayuda de Janitor
        "name",
        "time"
    )

implicit_to_explicit_df.complete( # formato diccionario con as variables y valores a mostrar
        {'name': ['lynn', 'zelda']},
        {'time': ['morning', 'afternoon']},
        sort=True) # ordena los valores de manera que primero muestra los pasados y luego el resto

implicit_to_explicit_df.complete(
        'name',
        'time',
        fill_value= np.nan  # puedes asignar el valor que desees. Por defecto asigna nan
    )

implicit_to_explicit_df.complete(
        'name',
        'time',
        fill_value=0,
        explicit=False
    )

diabetes = datasets.load_diabetes(as_frame=True).frame

diabetes[diabetes.columns[1:6]].replace(0,np.nan)

diabetes

missingno.matrix(diabetes)

diabetes.missing.sort_variables_by_missingness().pipe(missingno.matrix)  # muestra los datos en una matriz de sombra

diabetes.missing.sort_variables_by_missingness().sort_values(by='blood_pressure').pipe(missingno.matrix) # ordena los valores segun una columna

diabetes.missing.sort_variables_by_missingness().sort_values(by='insulin').pipe(missingno.matrix)  # ordena los valores segun una columna
    