import pandas as pd
import os
import logging

# import timeit

from src.utils.logging_utils import setup_logger

# Timer variables

logger = setup_logger(__name__, "extract.log", level=logging.DEBUG)


def extract_csv(file_name: str) -> pd.DataFrame:
    try:
        file_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "data",
            "raw",
            file_name,
        )

        df = pd.read_csv(file_path)
        logger.info(
            f"Successful data extraction: {file_name} (Shape: {df.shape})"
        )
        return df

    except Exception as e:
        logger.error(f"Extraction error for {file_path}: {str(e)}")
        raise Exception(f"Error for csv {file_path} extraction")
