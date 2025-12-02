import pandas as pd

from src.transform.clean_checkin_checkout import clean_checkin_checkout

# from src.transform.clean_gym_loc import clean_gym_loc
# from src.transform.clean_sub_plans import clean_sub_plans
# from src.transform.clean_userss import clean_users
# from src.transform.merge_stuff import merge_stuff

from src.utils.logging_utils import setup_logger

logger = setup_logger("transform_data", "transform_data.log")

relative_output_dir = "data\proccessed"
file_names = [
    "cleaned_checkin_checkout.csv",
    "cleaned_gyms.csv",
    "cleaned_subscriptions.csv",
    "cleaned_users.csv",
]


def transform_data(
    extracted_data,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    try:
        transformed_data = extracted_data
        logger.info("Data loading started!")
        logger.info("Checkin_checkout cleaning...")
        cleaned_checkin_checkout = clean_checkin_checkout(
            extracted_data[0], relative_output_dir, file_names[0]
        )
        logger.info("Checkin_checkout cleaned")

        logger.info("Data loading completed!")
        transformed_data[0] = cleaned_checkin_checkout

        return transformed_data
    except Exception as e:
        logger.error(f"Data transforming error: {str(e)}")
        raise e
