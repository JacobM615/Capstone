import pandas as pd
import os

from src.etl.transform.clean_checkin_checkout import clean_checkin_checkout
from src.etl.transform.clean_gyms import clean_gyms
from src.etl.transform.clean_sub_plans import clean_sub_plans
from src.etl.transform.clean_users import clean_users

from src.etl.transform.merge_two import merge_two


from src.etl.utils.logging_utils import setup_logger

logger = setup_logger("transform_data", "transform_data.log")


def transform_data(
    extracted_data: tuple[
        pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame
    ],
) -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
]:
    """
    Takes in extracted data
    Setup cleaning variables (output location and output names)
    Cleans and transforms each table with its own function (the function also saves it)
    Merge some of the clean tables so that insights can be answered
    Return transformed output data
    """
    try:
        logger.info("Data transforming started!")

        # Cleaning
        relative_output_dir_single = os.path.join(
            "data", "processed", "single_tables"
        )
        file_names_single = [
            "cleaned_checkin_checkout.csv",
            "cleaned_gyms.csv",
            "cleaned_subscriptions.csv",
            "cleaned_users.csv",
        ]

        logger.info("Checkin_checkout cleaning and transforming...")
        cleaned_checkin_checkout, file_location = clean_checkin_checkout(
            extracted_data[0], relative_output_dir_single, file_names_single[0]
        )
        logger.info(f"File saved to {file_location}")
        logger.info("Checkin_checkout cleaned, transformed and saved")

        logger.info("Gyms cleaning and transforming...")
        cleaned_gyms, file_location = clean_gyms(
            extracted_data[1], relative_output_dir_single, file_names_single[1]
        )
        logger.info(f"File saved to {file_location}")
        logger.info("Gyms cleaned, transformed and saved")

        logger.info("Subscription plans cleaning and transforming...")
        cleaned_sub_plans, file_location = clean_sub_plans(
            extracted_data[2], relative_output_dir_single, file_names_single[2]
        )
        logger.info(f"File saved to {file_location}")
        logger.info("Subscription plans cleaned, transformed and saved")

        logger.info("Users cleaning and transforming...")
        cleaned_users, file_location = clean_users(
            extracted_data[3], relative_output_dir_single, file_names_single[3]
        )
        logger.info(f"File saved to {file_location}")
        logger.info("Users cleaned, transformed and saved")

        # Merging
        relative_output_dir_merged = os.path.join(
            "data", "processed", "merged"
        )
        file_names_merged = [
            "merged_users__sub_plans.csv",
            "merged_checkin_checkout__gyms.csv",
            "merged_checkin_checkout__gyms__users.csv",
        ]

        keys = [
            "subscription_plan",
            "gym_id",
            "user_id",
        ]

        logger.info("Merging users and sub_plans...")
        users__sub_plans, file_location = merge_two(
            cleaned_users,
            cleaned_sub_plans,
            keys[0],
            relative_output_dir_merged,
            file_names_merged[0],
        )
        logger.info(f"File saved to {file_location}")
        logger.info("Merged users and sub_plans and saved")

        logger.info("Merging checkin_checkout and gyms...")
        checkin_checkout__gyms, file_location = merge_two(
            cleaned_checkin_checkout,
            cleaned_gyms,
            keys[1],
            relative_output_dir_merged,
            file_names_merged[1],
        )
        logger.info(f"File saved to {file_location}")
        logger.info("Merged checkin_checkout and gyms and saved")

        logger.info("Merging checkin_checkout__gyms and users...")
        checkin_checkout__gyms__users, file_location = merge_two(
            checkin_checkout__gyms,
            cleaned_users,
            keys[2],
            relative_output_dir_merged,
            file_names_merged[2],
        )
        logger.info(f"File saved to {file_location}")
        logger.info("Merged checkin_checkout__gyms and users and saved")

        logger.info("Data transformation completed!")

        return (
            cleaned_checkin_checkout,
            cleaned_users,
            users__sub_plans,
            checkin_checkout__gyms__users,
        )
    except Exception as e:
        logger.error(f"Data transforming error: {str(e)}")
        raise e
