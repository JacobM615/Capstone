import pandas as pd

from src.etl.utils.logging_utils import setup_logger
from src.etl.utils.file_utils import save_dataframe_to_csv

logger = setup_logger("load_data", "load_data.log")


def load_data(
    transformed_data: tuple[
        pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame
    ],
) -> None:
    """
    Take in transformed data
    Check if any of the passed dataframes are empty
    Setup loading variables for single tables (output location and output names)
    Save single tables
    Setup loading variables for merged tables (output location and output names)
    Save merged tables
    """
    for df in transformed_data:
        if df is None or df.empty:
            logger.warning("transformed_data is empty -> no data to load")
            return

    try:
        logger.info("Data loading started!")

        relative_output_dir_single = "data/output/single_tables"
        file_names_single = [
            "checkin_checkout.csv",
            "users.csv",
        ]

        i = 0
        while i < len(file_names_single):
            file_location = save_dataframe_to_csv(
                transformed_data[i],
                relative_output_dir_single,
                file_names_single[i],
            )
            logger.info(f"File saved to {file_location}")
            i += 1

        relative_output_dir_merged = "data/output/merged"
        file_names_merged = [
            "users__sub_plans.csv",
            "checkin_checkout__gyms__users.csv",
        ]

        i = len(file_names_single)
        while i < (len(file_names_merged) + len(file_names_single)):
            file_location = save_dataframe_to_csv(
                transformed_data[i],
                relative_output_dir_merged,
                file_names_merged[i - len(file_names_single)],
            )
            logger.info(f"File saved to {file_location}")
            i += 1

        logger.info("Data loading completed!")

    except Exception as e:
        logger.error(f"Data loading error: {str(e)}")
        raise e
