import pandas as pd

from src.etl.extract.extract_csv import extract_csv
from src.etl.utils.logging_utils import setup_logger

logger = setup_logger("extract", "extract.log")

CSV_FILES = [
    "checkin_checkout_history.csv",
    "gym_locations_data.csv",
    "subscription_plans.csv",
    "users_data.csv",
]


def extract_data() -> (
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
):
    """
    Call extract_csv for each raw file location
    Return a tuple of raw dataframes
    """
    try:
        logger.info("Data extraction started!")

        checkin_checkout = extract_csv(CSV_FILES[0])
        gym_loc = extract_csv(CSV_FILES[1])
        sub_plans = extract_csv(CSV_FILES[2])
        users = extract_csv(CSV_FILES[3])
        # ^^Getting all the dfs

        logger.info("Data extraction completed!")

        return (checkin_checkout, gym_loc, sub_plans, users)

    except Exception as e:
        logger.error(f"Data extraction error in extract.py: {e}")
        raise Exception(f"Data extraction error in extract.py: {e}")
