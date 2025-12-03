import pandas as pd
import pytest

from unittest.mock import patch
from src.etl.extract.extract_csv import extract_csv


@pytest.fixture
def mock_logger(mocker):
    return mocker.patch("src.etl.extract.extract_csv.logger")


mock_file_name = "mock.csv"


def test_extract_csv_to_df(mocker):

    mock_df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "another_test_column": ["testing1", "testing2", "testing3"],
        }
    )

    mocker.patch(
        "src.etl.extract.extract_csv.pd.read_csv", return_value=mock_df
    )

    function_df = extract_csv(mock_file_name)

    assert isinstance(function_df, pd.DataFrame)
    pd.testing.assert_frame_equal(function_df, mock_df)


@patch(
    "src.etl.extract.extract_csv.os.path.join", return_value="mock_file_path"
)
def test_extract_csv_errors_logged(mocker, mock_logger):

    file_path = "mock_file_path"

    mocker.patch(
        "src.etl.extract.extract_csv.pd.read_csv",
        side_effect=Exception(f"Error for csv, {file_path} extraction"),
    )

    with pytest.raises(
        Exception, match=f"Error for csv, {file_path} extraction"
    ):
        extract_csv(mock_file_name)

        mock_logger.error.assert_called_once_with(
            f"Extraction error for {file_path}: Error for csv, {file_path} extraction"
        )
