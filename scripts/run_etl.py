import sys

# import os

# from config.env_config import setup_env

from src.utils.logging_utils import setup_logger
from src.extract.extract import extract_data
from src.transform.transform import transform_data
from src.load.load import load_data


def main():
    # Get the argument from the run_etl command and set up the environment
    # setup_env(sys.argv)

    logger = setup_logger("pipeline", "pipeline.log")

    try:
        # E
        logger.info("Starting Extraction")
        extracted_data = extract_data()
        logger.info("Extraction successful")

        # T
        logger.info("Starting Transformation")
        transformed_data = transform_data(extracted_data)
        logger.info("Transformation successful")

        # L
        logger.info("Starting Load")
        load_data(transformed_data)
        logger.info("Load successful")

        print(
            "ETL pipeline run successfully"
            # f"{os.getenv('ENV', 'error')} environment!"
        )

    except Exception as e:
        logger.error(f"ETL error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
