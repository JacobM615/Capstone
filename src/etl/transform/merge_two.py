import pandas as pd

from src.etl.utils.file_utils import save_dataframe_to_csv


def merge_two(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    key: str,
    relative_output_dir: str,
    file_name: str,
) -> tuple[pd.DataFrame, str]:

    merged_data = pd.merge(df1, df2, on=key)
    file_location = file_location = save_dataframe_to_csv(
        merged_data, relative_output_dir, file_name
    )

    return merged_data, file_location
