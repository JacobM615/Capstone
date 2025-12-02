import pandas as pd

from src.etl.utils.file_utils import save_dataframe_to_csv


def clean_checkin_checkout(
    checkin_checkout: pd.DataFrame, relative_output_dir: str, file_name: str
) -> tuple[pd.DataFrame, str]:

    checkin_checkout = remove_nulls(checkin_checkout)

    checkin_checkout = correct_dtypes(checkin_checkout)

    checkin_checkout = remove_duplicates(checkin_checkout)

    checkin_checkout = remove_whitespace(checkin_checkout)

    checkin_checkout.reset_index(drop=True, inplace=True)

    file_location = save_dataframe_to_csv(
        checkin_checkout, relative_output_dir, file_name
    )

    return checkin_checkout, file_location


def remove_nulls(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def correct_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    return df.astype(
        {
            "checkin_time": "datetime64[ns]",
            "checkout_time": "datetime64[ns]",
            "calories_burned": int,
        }
    )


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def remove_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    df["user_id"] = df["user_id"].str.strip()
    return df
