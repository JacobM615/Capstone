import os
import pandas as pd
import pytest
from unittest.mock import patch
from src.etl.transform.clean_users import clean_users


EXPECTED_CLEANED_USERS_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "expected",
    "users.csv",
)

UNCLEAN_USERS_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "users_data.csv",
)


@pytest.fixture
def expected_cleaned_users():
    return pd.read_csv(EXPECTED_CLEANED_USERS_DATA_PATH)


@pytest.fixture
def unclean_users():
    return pd.read_csv(UNCLEAN_USERS_DATA_PATH)


def test_transform_users_returns_expected_data(
    expected_cleaned_users, unclean_users
):
    with patch(
        "src.etl.transform.clean_users.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        cleaned_users, file_location = clean_users(
            unclean_users,
            "mock_relative_output_dir",
            "mock_file_name",
        )
        assert mock_save.called

    pd.testing.assert_frame_equal(
        cleaned_users,
        expected_cleaned_users.astype(
            {
                "age": int,
                "sign_up_date": "datetime64[ns]",
            }
        ),
    )


def test_transform_users_handles_empty_dataframe():
    empty_df = pd.DataFrame()

    with patch(
        "src.etl.transform.clean_users.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(KeyError):
            clean_users(
                empty_df,
                "mock_relative_output_dir",
                "mock_file_name",
            )


def test_transform_users_handles_empty_rows_with_columns():

    empty_with_columns = pd.DataFrame(
        columns=[
            "user_id",
            "first_name",
            "last_name",
            "age",
            "gender",
            "birthdate",
            "sign_up_date",
            "user_location",
            "subscription_plan",
        ]
    )
    with patch(
        "src.etl.transform.clean_users.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        result, file_location = clean_users(
            empty_with_columns,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0
    assert "birthdate" not in result.columns


def test_transform_users_handles_all_rows_filtered():

    all_invalid = pd.DataFrame(
        {
            "user_id": [None],
            "first_name": [None],
            "last_name": [None],
            "age": [None],
            "gender": [None],
            "birthdate": [None],
            "sign_up_date": [None],
            "user_location": [None],
            "subscription_plan": [None],
        }
    )
    with patch(
        "src.etl.transform.clean_users.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        result, file_location = clean_users(
            all_invalid,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0
    assert "birthdate" not in result.columns


def test_transform_users_missing_required_column():
    missing_age = pd.DataFrame(
        {
            "user_id": [1],
            "first_name": [1],
            "last_name": [1],
            "gender": [1],
            "birthdate": [1],
            "sign_up_date": [1],
            "user_location": [1],
            "subscription_plan": [1],
        }
    )
    with patch(
        "src.etl.transform.clean_users.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(KeyError):
            clean_users(
                missing_age,
                "mock_relative_output_dir",
                "mock_file_name",
            )
