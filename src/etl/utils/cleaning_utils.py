import pandas as pd


def remove_nulls(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def remove_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df.drop(columns, axis=1)
