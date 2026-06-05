import pandas as pd
import numpy as np


def dataset_summary(df):

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Duplicate Rows": df.duplicated().sum(),
        "Missing Values": df.isnull().sum().sum()
    }

    return summary


def missing_data(df):

    missing = (
        df.isnull()
        .sum()
        .reset_index()
    )

    missing.columns = ["Column", "Missing"]

    missing["Percent"] = (
        missing["Missing"] / len(df)
    ) * 100

    return missing.sort_values(
        by="Percent",
        ascending=False
    )


def numerical_columns(df):

    return df.select_dtypes(
        include=np.number
    ).columns.tolist()


def categorical_columns(df):

    return df.select_dtypes(
        exclude=np.number
    ).columns.tolist()
