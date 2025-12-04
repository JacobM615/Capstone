import pandas as pd
import pytest

# timeit if I want to do performance testing later

from src.etl.extract.extract import CSV_FILES
from src.etl.extract.extract_csv import extract_csv


@pytest.fixture
def expected_df():
    return pd.read_csv("data/raw/checkin_checkout_history.csv")


def test_extract_csv_returns_df(expected_df):
    function_df = extract_csv(CSV_FILES[0])

    pd.testing.assert_frame_equal(function_df, expected_df)


def test_extract_csv_file_not_found():
    no_file = "no_file.csv"

    with pytest.raises(Exception, match="Error for csv,"):
        extract_csv(no_file)
