import pandas as pd
import os

# import logging
# import timeit
# from src.utils.logging_utils import setup_logger

# +^^ , successful extraction logger and then include in try

# Logger setup and timer variables

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "users_data.csv",
)


def extract_users() -> pd.DataFrame:
    try:
        users_data = pd.read_csv(file_path)
        return users_data

    except Exception as e:
        raise Exception(f"Data extraction error in {file_path}: {str(e)}")
