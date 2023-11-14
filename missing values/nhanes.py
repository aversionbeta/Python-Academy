# Import janitor, nhanes.load, numpy, pandas, and missingno
import janitor
import nhanes.load
import numpy as np
import pandas as pd
import missingno
import scipy

# Load NHANES data
nhanes_raw_df = nhanes.load.load_NHANES_data(year="2017-2018")

# Clean column names using janitor
nhanes_clean_df = nhanes_raw_df.clean_names(case_type="snake")

# Select and rename columns
nhanes_df = (
    nhanes_clean_df.select_columns(
        "general_health_condition",
        "age_in_years_at_screening",
        "gender",
        "current_selfreported_height_inches",
        "current_selfreported_weight_pounds",
        "doctor_told_you_have_diabetes",
        "60_sec_pulse30_sec_pulse2",
        "total_cholesterol_mgdl"
    ).rename_columns(
        {
            "age_in_years_at_screening": "age",
            "current_selfreported_height_inches": "height",
            "current_selfreported_weight_pounds": "weight",
            "doctor_told_you_have_diabetes": "diabetes",
            "60_sec_pulse30_sec_pulse2": "pulse",
            "total_cholesterol_mgdl": "total_cholesterol"
        }
    )
)

# Replace specified values with NaN
nhanes_df.replace(
    {
        "height": {9999: np.nan, 7777: np.nan},
        "weight": {9999: np.nan, 7777: np.nan},
        "diabetes": {"Borderline": np.nan}
    },
    inplace=True
)

# Drop rows with missing values in the "diabetes" column
nhanes_df.dropna(subset=["diabetes"], how="any", inplace=True)

# Convert "diabetes" column to integer
nhanes_df["diabetes"] = nhanes_df["diabetes"].astype(int)

# Display the shape of the cleaned DataFrame
print(nhanes_df.shape)

# Use missingno to visualize missing data
missingno.matrix(nhanes_df, sort="descending")

# Use missingno API for visualization
missingno.matrix(nhanes_df, sort="descending")

# Drop rows with missing values in specified columns
nhanes_df = (
    nhanes_df
    .dropna(
        subset=["pulse", "total_cholesterol", "general_health_condition", "weight", "height"],
        how="all"
    )
)

# Display the shape of the DataFrame after dropping missing values
print(nhanes_df.shape)

female_weight, male_weight =(
    nhanes_df
    .select_columns('gender','weight')
    .transform_column(
        'weight',
        lambda x: x.isna(),
        elementwise=False
    )
    .groupby('gender')
    .weight
    .pipe(
        lambda df: (
            df.get_group('Female'),
            df.get_group('Male')
        )
    )
)
scipy.stats.ttest_ind(
    a = female_weight,
    b= male_weight,
    alternative='two-sided',
)