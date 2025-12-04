import pandas as pd

from src.etl.utils.file_utils import save_dataframe_to_csv
from src.etl.utils.cleaning_utils import remove_columns


def clean_sub_plans(
    sub_plans: pd.DataFrame, relative_output_dir: str, file_name: str
) -> tuple[pd.DataFrame, str]:

    sub_plans = remove_columns(sub_plans, ["features"])

    file_location = save_dataframe_to_csv(
        sub_plans, relative_output_dir, file_name
    )

    return sub_plans, file_location
