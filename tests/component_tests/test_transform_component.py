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
    with patch("src.etl.utils.file_utils.save_dataframe_to_csv") as mock_save:
        mock_save.return_value = "mock_file_location"
        result = transform_data(sample_input_data)

    # Verify returned DataFrame
    i = 0
    while i < len(result):
        pd.testing.assert_frame_equal(
            result[i],
            expected_data_returned[i],
        )
        i += 1


@patch("src.etl.transform.transform.clean_checkin_checkout")
def test_transform_data_propagates_checkin_checkout_cleaning_exceptions(
    mock_clean_checkin_checkout,
):
    mock_clean_checkin_checkout.side_effect = Exception(
        "Checkin_checkout cleaning failed"
    )

    input_data = (
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
    )

    with patch("src.etl.utils.file_utils.save_dataframe_to_csv") as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(
            Exception, match="Checkin_checkout cleaning failed"
        ):
            transform_data(input_data)


@patch("src.etl.transform.transform.clean_gyms")
@patch("src.etl.transform.transform.clean_checkin_checkout")
def test_transform_data_propagates_gyms_cleaning_exceptions(
    mock_clean_checkin_checkout, mock_clean_gyms
):

    mock_clean_checkin_checkout.return_value = (
        pd.DataFrame({"checkin_checkout": [1]}),
        "file_location",
    )
    mock_clean_gyms.side_effect = Exception("Gyms cleaning failed")

    input_data = (
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
    )

    with patch("src.etl.utils.file_utils.save_dataframe_to_csv") as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(Exception, match="Gyms cleaning failed"):
            transform_data(input_data)


@patch("src.etl.transform.transform.clean_sub_plans")
@patch("src.etl.transform.transform.clean_gyms")
@patch("src.etl.transform.transform.clean_checkin_checkout")
def test_transform_data_propagates_sub_plans_cleaning_exceptions(
    mock_clean_checkin_checkout, mock_clean_gyms, mock_clean_sub_plans
):

    mock_clean_checkin_checkout.return_value = (
        pd.DataFrame({"checkin_checkout": [1]}),
        "file_location",
    )
    mock_clean_gyms.return_value = (
        pd.DataFrame({"gyms": [1]}),
        "file_location",
    )
    mock_clean_sub_plans.side_effect = Exception("Sub_plans cleaning failed")

    input_data = (
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
    )

    with patch("src.etl.utils.file_utils.save_dataframe_to_csv") as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(Exception, match="Sub_plans cleaning failed"):
            transform_data(input_data)


@patch("src.etl.transform.transform.clean_users")
@patch("src.etl.transform.transform.clean_sub_plans")
@patch("src.etl.transform.transform.clean_gyms")
@patch("src.etl.transform.transform.clean_checkin_checkout")
def test_transform_data_propagates_users_cleaning_exceptions(
    mock_clean_checkin_checkout,
    mock_clean_gyms,
    mock_clean_sub_plans,
    mock_clean_users,
):

    mock_clean_checkin_checkout.return_value = (
        pd.DataFrame({"checkin_checkout": [1]}),
        "file_location",
    )
    mock_clean_gyms.return_value = (
        pd.DataFrame({"gyms": [1]}),
        "file_location",
    )
    mock_clean_sub_plans.return_value = (
        pd.DataFrame({"sub_plans": [1]}),
        "file_location",
    )
    mock_clean_users.side_effect = Exception("Users cleaning failed")

    input_data = (
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
    )

    with patch("src.etl.utils.file_utils.save_dataframe_to_csv") as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(Exception, match="Users cleaning failed"):
            transform_data(input_data)


@patch("src.etl.transform.transform.clean_gyms")
@patch("src.etl.transform.transform.clean_checkin_checkout")
def test_transform_data_handles_cleaning_checkin_checkout_exceptions_first(
    mock_clean_checkin_checkout, mock_clean_gyms
):

    mock_clean_checkin_checkout.side_effect = Exception(
        "Checkin_checkout cleaning failed"
    )

    input_data = (
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
    )

    with patch("src.etl.utils.file_utils.save_dataframe_to_csv") as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(
            Exception, match="Checkin_checkout cleaning failed"
        ):
            transform_data(input_data)

    mock_clean_gyms.assert_not_called()


@patch("src.etl.transform.transform.clean_sub_plans")
@patch("src.etl.transform.transform.clean_gyms")
@patch("src.etl.transform.transform.clean_checkin_checkout")
def test_transform_data_handles_cleaning_gyms_exceptions_second(
    mock_clean_checkin_checkout, mock_clean_gyms, mock_clean_sub_plans
):

    mock_clean_checkin_checkout.return_value = (
        pd.DataFrame({"checkin_checkout": [1]}),
        "file_location",
    )
    mock_clean_gyms.side_effect = Exception("Gyms cleaning failed")

    input_data = (
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
    )

    with patch("src.etl.utils.file_utils.save_dataframe_to_csv") as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(Exception, match="Gyms cleaning failed"):
            transform_data(input_data)

    mock_clean_sub_plans.assert_not_called()


@patch("src.etl.transform.transform.clean_users")
@patch("src.etl.transform.transform.clean_sub_plans")
@patch("src.etl.transform.transform.clean_gyms")
@patch("src.etl.transform.transform.clean_checkin_checkout")
def test_transform_data_handles_cleaning_sub_plans_exceptions_third(
    mock_clean_checkin_checkout,
    mock_clean_gyms,
    mock_clean_sub_plans,
    mock_clean_users,
):

    mock_clean_checkin_checkout.return_value = (
        pd.DataFrame({"checkin_checkout": [1]}),
        "file_location",
    )
    mock_clean_gyms.return_value = (
        pd.DataFrame({"gyms": [1]}),
        "file_location",
    )
    mock_clean_sub_plans.side_effect = Exception("Sub_plans cleaning failed")

    input_data = (
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
    )

    with patch("src.etl.utils.file_utils.save_dataframe_to_csv") as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(Exception, match="Sub_plans cleaning failed"):
            transform_data(input_data)

    mock_clean_users.assert_not_called()
