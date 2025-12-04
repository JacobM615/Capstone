import pandas as pd

from src.etl.utils.file_utils import save_dataframe_to_csv
from src.etl.utils.cleaning_utils import remove_columns


def clean_gyms(
    gyms: pd.DataFrame, relative_output_dir: str, file_name: str
) -> tuple[pd.DataFrame, str]:

    gyms = remove_columns(gyms, ["facilities"])

    file_location = save_dataframe_to_csv(gyms, relative_output_dir, file_name)

    return gyms, file_location
