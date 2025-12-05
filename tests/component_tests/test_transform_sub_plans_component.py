import os
import pandas as pd
import pytest
from unittest.mock import patch
from src.etl.transform.clean_sub_plans import clean_sub_plans


EXPECTED_CLEANED_SUB_PLANS_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "expected",
    "cleaned_subscriptions.csv",
)

UNCLEAN_SUB_PLANS_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "subscription_plans.csv",
)


@pytest.fixture
def expected_cleaned_sub_plans():
    return pd.read_csv(EXPECTED_CLEANED_SUB_PLANS_DATA_PATH)


@pytest.fixture
def unclean_sub_plans():
    return pd.read_csv(UNCLEAN_SUB_PLANS_DATA_PATH)


def test_transform_sub_plans_returns_expected_data(
    expected_cleaned_sub_plans, unclean_sub_plans
):
    with patch(
        "src.etl.transform.clean_sub_plans.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        cleaned_sub_plans, file_location = clean_sub_plans(
            unclean_sub_plans,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    pd.testing.assert_frame_equal(
        cleaned_sub_plans, expected_cleaned_sub_plans
    )


def test_transform_sub_plans_handles_empty_dataframe():
    empty_df = pd.DataFrame()
    with patch(
        "src.etl.transform.clean_sub_plans.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(KeyError):
            clean_sub_plans(
                empty_df,
                "mock_relative_output_dir",
                "mock_file_name",
            )


def test_transform_sub_plans_handles_empty_rows_with_columns():

    empty_with_columns = pd.DataFrame(
        columns=["subscription_plan", "price_per_month", "features"]
    )
    with patch(
        "src.etl.transform.clean_sub_plans.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        result, file_location = clean_sub_plans(
            empty_with_columns,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0
    assert "features" not in result.columns
