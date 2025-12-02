import pandas as pd

from src.utils.logging_utils import setup_logger
from src.utils.file_utils import save_dataframe_to_csv

logger = setup_logger("load_data", "load_data.log")


def load_data(transformed_data) -> None:
    for df in transformed_data:
        if df is None or df.empty:
            logger.warning("transformed_data is empty -> no data to load")
            return

    try:
        logger.info("Data loading started!")

        relative_output_dir = "data\output"
        file_names = [
            "checkin_checkout.csv",
            "gyms.csv",
            "subscriptions.csv",
            "users.csv",
        ]

        i = 0
        while i < len(transformed_data):
            file_location = save_dataframe_to_csv(
                transformed_data[i], relative_output_dir, file_names[i]
            )
            logger.info(f"File saved to {file_location}")
            i += 1

        logger.info("Data loading completed!")

    except Exception as e:
        logger.error(f"Data loading error: {str(e)}")
        raise e
