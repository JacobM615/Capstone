import pandas as pd

from src.utils.file_utils import save_dataframe_to_csv


def clean_checkin_checkout(
    checkin_checkout: pd.DataFrame, relative_output_dir: str, file_name: str
) -> pd.DataFrame:

    checkin_checkout = remove_nulls(checkin_checkout)

    checkin_checkout = correct_dtypes(checkin_checkout)

    checkin_checkout = remove_duplicates(checkin_checkout)

    checkin_checkout = remove_whitespace(checkin_checkout)

    checkin_checkout.reset_index(drop=True, inplace=True)

    save_dataframe_to_csv(checkin_checkout, relative_output_dir, file_name)

    return checkin_checkout


def remove_nulls(checkin_checkout: pd.DataFrame) -> pd.DataFrame:
    return checkin_checkout.dropna()


def correct_dtypes(checkin_checkout: pd.DataFrame) -> pd.DataFrame:

    checkin_checkout["checkin_time"] = checkin_checkout["checkin_time"].astype(
        "datetime64[ns]"
    )

    checkin_checkout["checkout_time"] = checkin_checkout[
        "checkout_time"
    ].astype("datetime64[ns]")

    checkin_checkout["calories_burned"] = checkin_checkout[
        "calories_burned"
    ].astype(int)

    return checkin_checkout


def remove_duplicates(checkin_checkout: pd.DataFrame) -> pd.DataFrame:
    return checkin_checkout.drop_duplicates()


def remove_whitespace(checkin_checkout: pd.DataFrame) -> pd.DataFrame:
    return checkin_checkout["user_id"].str.strip()
