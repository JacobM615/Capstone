import pandas as pd

from src.extract.extract_checkin_checkout import extract_checkin_checkout
from src.extract.extract_gym_loc import extract_gym_loc
from src.extract.extract_sub_plans import extract_sub_plans
from src.extract.extract_users import extract_users

from src.utils.logging_utils import setup_logger

# Logger setup


def extract_data() -> (
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
):
    try:
        # Logger info exacting started

        checkin_checkout = extract_checkin_checkout()
        gym_loc = extract_gym_loc()
        sub_plans = extract_sub_plans()
        users = extract_users()
        # ^^Getting all the dfs

        # Logger info successful??, df shapes??

        return (checkin_checkout, gym_loc, sub_plans, users)

    except Exception as e:
        raise Exception(f"Data extraction error in extract.py: {str(e)}")
