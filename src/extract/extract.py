import pandas as pd

from src.extract.extract_csv import extract_csv
from src.utils.logging_utils import setup_logger

logger = setup_logger("extract", "extract.log")

csv_files = [
    "checkin_checkout_history.csv",
    "gym_locations_data.csv",
    "subscription_plans.csv",
    "users_data.csv",
]


def extract_data() -> (
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
):
    try:
        logger.info("Data extraction started!")

        checkin_checkout = extract_csv(csv_files[0])
        gym_loc = extract_csv(csv_files[1])
        sub_plans = extract_csv(csv_files[2])
        users = extract_csv(csv_files[3])
        # ^^Getting all the dfs

        logger.info("Data extraction completed!")

        return (checkin_checkout, gym_loc, sub_plans, users)

    except Exception as e:
        logger.error(f"Data extraction error in extract.py: {str(e)}")
        raise Exception(f"Data extraction error in extract.py: {str(e)}")
