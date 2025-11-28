import pandas as pd
import os

# import logging
# import timeit

from src.utils.logging_utils import setup_logger

# , successful extraction logger

# Logger setup and timer

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "checkin_checkout_history.csv",
)


def extract_checkin_checkout() -> pd.DataFrame:
    try:
        stuff

    except Exception as e:
        raise Exception(f"Data extraction error in {file_path}: {str(e)}")
