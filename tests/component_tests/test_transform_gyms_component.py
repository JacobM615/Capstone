import os
import pandas as pd
import pytest
from unittest.mock import patch
from src.etl.transform.clean_gyms import clean_gyms


EXPECTED_CLEANED_GYMS_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "test_data",
    "expected",
    "cleaned_gyms.csv",
)

UNCLEAN_GYMS_DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "gym_locations_data.csv",
)


@pytest.fixture
def expected_cleaned_gyms():
    return pd.read_csv(EXPECTED_CLEANED_GYMS_DATA_PATH)


@pytest.fixture
def unclean_gyms():
    return pd.read_csv(UNCLEAN_GYMS_DATA_PATH)


def test_transform_gyms_returns_expected_data(
    expected_cleaned_gyms, unclean_gyms
):
    with patch(
        "src.etl.transform.clean_gyms.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        cleaned_gyms, file_location = clean_gyms(
            unclean_gyms,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    pd.testing.assert_frame_equal(cleaned_gyms, expected_cleaned_gyms)


def test_transform_gyms_handles_empty_dataframe():
    empty_df = pd.DataFrame()

    with patch(
        "src.etl.transform.clean_gyms.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        with pytest.raises(KeyError):
            clean_gyms(
                empty_df,
                "mock_relative_output_dir",
                "mock_file_name",
            )


def test_transform_gyms_handles_empty_rows_with_columns():

    empty_with_columns = pd.DataFrame(
        columns=["gym_id", "location", "gym_type", "facilities"]
    )

    with patch(
        "src.etl.transform.clean_gyms.save_dataframe_to_csv"
    ) as mock_save:
        mock_save.return_value = "mock_file_location"
        result, file_location = clean_gyms(
            empty_with_columns,
            "mock_relative_output_dir",
            "mock_file_name",
        )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0
    assert "facilities" not in result.columns
