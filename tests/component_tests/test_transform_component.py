import pandas as pd
import pytest
from unittest.mock import patch
from src.etl.transform.transform import transform_data


def normalize_nulls(df):
    """Normalize null values to avoid None vs NaN warnings
    in DataFrame comparisons."""
    return df.fillna(pd.NA).replace({pd.NA: None})


@pytest.fixture
def sample_input_data():
    CSV_FILES = [
        "data/raw/checkin_checkout_history.csv",
        "data/raw/gym_locations_data.csv",
        "data/raw/subscription_plans.csv",
        "data/raw/users_data.csv",
    ]
    checkin_checkout = pd.read_csv(CSV_FILES[0])
    gym_loc = pd.read_csv(CSV_FILES[1])
    sub_plans = pd.read_csv(CSV_FILES[2])
    users = pd.read_csv(CSV_FILES[3])

    return (
        checkin_checkout,
        gym_loc,
        sub_plans,
        users,
    )


@pytest.fixture
def expected_data_returned():
    CSV_FILES = [
        "tests/test_data/expected/checkin_checkout.csv",
        "tests/test_data/expected/users.csv",
        "tests/test_data/expected/users__sub_plans.csv",
        "tests/test_data/expected/checkin_checkout__gyms__users.csv",
    ]
    checkin_checkout = pd.read_csv(CSV_FILES[0]).astype(
        {
            "checkin_time": "datetime64[ns]",
            "checkout_time": "datetime64[ns]",
            "duration": "timedelta64[ns]",
            "calories_burned": int,
        }
    )
    users = pd.read_csv(CSV_FILES[1]).astype(
        {
            "age": int,
            "sign_up_date": "datetime64[ns]",
        }
    )
    users__sub_plans = pd.read_csv(CSV_FILES[2]).astype(
        {
            "age": int,
            "sign_up_date": "datetime64[ns]",
        }
    )
    checkin_checkout__gyms__users = pd.read_csv(CSV_FILES[3]).astype(
        {
            "checkin_time": "datetime64[ns]",
            "checkout_time": "datetime64[ns]",
            "duration": "timedelta64[ns]",
            "calories_burned": int,
            "age": int,
            "sign_up_date": "datetime64[ns]",
        }
    )

    return (
        checkin_checkout,
        users,
        users__sub_plans,
        checkin_checkout__gyms__users,
    )


def test_transform_data_returns_correct_structure(
    sample_input_data, expected_data_returned
):
    result = transform_data(sample_input_data)

    # Verify returned DataFrame
    i = 1
    while i < len(result):
        pd.testing.assert_frame_equal(
            result[i],
            expected_data_returned[i],
        )
        i += 1
