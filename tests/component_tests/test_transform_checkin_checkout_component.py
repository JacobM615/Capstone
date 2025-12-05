import os
import pandas as pd
import pytest
from unittest.mock import patch
from src.etl.transform.clean_checkin_checkout import clean_checkin_checkout


EXPECTED_CLEANED_CHECKIN_CHECKOUT_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "expected",
    "checkin_checkout.csv",
)

UNCLEAN_CHECKIN_CHECKOUT_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "checkin_checkout_history.csv",
)


@pytest.fixture
def expected_cleaned_checkin_checkout():
    return pd.read_csv(EXPECTED_CLEANED_CHECKIN_CHECKOUT_DATA_PATH)


@pytest.fixture
def unclean_checkin_checkout():
    return pd.read_csv(UNCLEAN_CHECKIN_CHECKOUT_DATA_PATH)


def test_transform_checkin_checkout_returns_expected_data(
    expected_cleaned_checkin_checkout, unclean_checkin_checkout
):
    with patch(
        "src.etl.transform.clean_checkin_checkout.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        cleaned_checkin_checkout, file_location = clean_checkin_checkout(
            unclean_checkin_checkout,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    pd.testing.assert_frame_equal(
        cleaned_checkin_checkout,
        expected_cleaned_checkin_checkout.astype(
            {
                "checkin_time": "datetime64[ns]",
                "checkout_time": "datetime64[ns]",
                "calories_burned": int,
                "duration": "timedelta64[ns]",
            }
        ),
    )


def test_transform_checkin_checkout_handles_empty_dataframe():
    empty_df = pd.DataFrame()

    with patch(
        "src.etl.transform.clean_checkin_checkout.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(KeyError):
            clean_checkin_checkout(
                empty_df,
                "mock_relative_output_dir",
                "mock_file_name",
            )


def test_transform_checkin_checkout_handles_empty_rows_with_columns():

    empty_with_columns = pd.DataFrame(
        columns=[
            "user_id",
            "gym_id",
            "checkin_time",
            "checkout_time",
            "workout_type",
            "calories_burned",
        ]
    )

    with patch(
        "src.etl.transform.clean_checkin_checkout.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        result, file_location = clean_checkin_checkout(
            empty_with_columns,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0


def test_transform_checkin_checkout_handles_all_rows_filtered():

    all_invalid = pd.DataFrame(
        {
            "user_id": [None],
            "gym_id": [None],
            "checkin_time": [None],
            "checkout_time": [None],
            "workout_type": [None],
            "calories_burned": [None],
        }
    )

    with patch(
        "src.etl.transform.clean_checkin_checkout.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        result, file_location = clean_checkin_checkout(
            all_invalid,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0


def test_transform_checkin_checkout_missing_required_column():
    missing_checkout_time = pd.DataFrame(
        {
            "user_id": [1],
            "gym_id": [1],
            "checkin_time": [1],
            "workout_type": [1],
            "calories_burned": [1],
        }
    )

    with patch(
        "src.etl.transform.clean_checkin_checkout.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(KeyError):
            clean_checkin_checkout(
                missing_checkout_time,
                "mock_relative_output_dir",
                "mock_file_name",
            )
