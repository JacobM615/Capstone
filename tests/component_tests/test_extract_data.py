import pandas as pd
import pytest

from unittest.mock import patch
from src.etl.extract.extract import extract_data


def normalise_nulls(df):
    return df.fillna(pd.NA).replace({pd.NA: None})


@pytest.fixture
def expected_df():
    df1 = normalise_nulls(pd.read_csv("data/raw/checkin_checkout_history.csv"))
    df2 = normalise_nulls(pd.read_csv("data/raw/gym_locations_data.csv"))
    df3 = normalise_nulls(pd.read_csv("data/raw/subscription_plans.csv"))
    df4 = normalise_nulls(pd.read_csv("data/raw/users_data.csv"))

    return [df1, df2, df3, df4]


def test_extract_data_returns_correct_data(expected_df):

    function_df = extract_data()

    assert isinstance(function_df, tuple)
    assert len(function_df) == 4
    assert isinstance(function_df[0], pd.DataFrame)
    assert isinstance(function_df[1], pd.DataFrame)
    assert isinstance(function_df[2], pd.DataFrame)
    assert isinstance(function_df[3], pd.DataFrame)

    pd.testing.assert_frame_equal(
        normalise_nulls(function_df[0]), expected_df[0]
    )
    pd.testing.assert_frame_equal(
        normalise_nulls(function_df[1]), expected_df[1]
    )
    pd.testing.assert_frame_equal(
        normalise_nulls(function_df[2]), expected_df[2]
    )
    pd.testing.assert_frame_equal(
        normalise_nulls(function_df[3]), expected_df[3]
    )


@patch("src.etl.extract.extract.extract_csv")
def test_extract_data_propagates_extract_csv_exceptions(mock_extract_csv):
    mock_extract_csv.side_effect = Exception("File Error")

    with pytest.raises(Exception, match="File Error"):
        extract_data()
