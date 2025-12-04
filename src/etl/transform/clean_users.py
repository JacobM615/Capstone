import pandas as pd

from src.etl.utils.file_utils import save_dataframe_to_csv
from src.etl.utils.cleaning_utils import (
    remove_nulls,
    remove_duplicates,
    remove_columns,
)


def clean_users(
    users: pd.DataFrame, relative_output_dir: str, file_name: str
) -> tuple[pd.DataFrame, str]:

    users = remove_nulls(users)

    users = correct_dtypes(users)

    users = remove_duplicates(users)

    users = remove_columns(users, ["birthdate"])

    users.reset_index(drop=True, inplace=True)

    file_location = save_dataframe_to_csv(
        users, relative_output_dir, file_name
    )

    return users, file_location


def correct_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    return df.astype(
        {
            "age": int,
            "sign_up_date": "datetime64[ns]",
        }
    )
