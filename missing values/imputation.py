import janitor
import numpy as np
import pandas as pd
import missingno
from sklearn import datasets
import seaborn as sns


implicit_to_explicit_df = pd.DataFrame(
    data={
        "name": ["lynn", np.nan, "zelda", np.nan, "shadowsong", np.nan],
        "time": ["morning", "afternoon", "morning", "afternoon", "morning", "afternoon",],
        "value": [350, 310, 320, 350, 310, 320]
    }
)

implicit_to_explicit_df

implicit_to_explicit_df.ffill() #Rellena los nan con los valores de la celda de arriba
riskfactors_df = datasets.load_diabetes(as_frame=True).frame

riskfactors_df.select_columns("weight_lbs", "height_inch", "bmi").missing.bind_shadow_matrix(true_string=True, false_string=False).fillna(
        riskfactors_df.select_columns("weight_lbs", "height_inch", "bmi").astype("float64").mean().to_dict()
    )

riskfactors_df.select_columns('weight_lbs', 'height_inch', 'bmi').missing.bind_shadow_matrix(true_string=True, false_string=False).apply(
        axis = 'rows',
        func = lambda column: column.fillna(column.mean()) if '_NA' not in column.name else column
    )

riskfactors_df.select_columns('weight_lbs', 'height_inch', 'bmi').missing.bind_shadow_matrix(true_string=True, false_string=False).apply(
        axis = 'rows',
        func = lambda column: column.fillna(column.mean()) if '_NA' not in column.name else column
    ).pipe(
        lambda df: (
            sns.displot(
                data=df,
                x='weight_lbs',
                hue='weight_lbs_NA'
            )
        )
    )
    
riskfactors_df.select_columns("weight_lbs","height_inch","bmi").missing.bind_shadow_matrix(true_string=True,false_string=False).apply(
        axis="rows",
        func = lambda column : column.fillna(column.mean()) if "_NA" not in column.name else column
    ).pivot_longer(
        index="*_NA"
    ).pivot_longer(
        index=["variable","value"],
        names_to="variable_NA",
        values_to="value_NA"
    ).assign(
        valid=lambda df : df.apply(axis="columns", func= lambda column : column.variable in column.variable_NA)
    ).query("valid").pipe(
        lambda df:(
            sns.displot(
                data=df,
                x="value",
                hue="value_NA",
                col="variable",
                common_bins=False,
                facet_kws={
                    "sharex":False,
                    "sharey":False
                }
            )
        )
    )