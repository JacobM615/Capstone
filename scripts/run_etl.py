import sys

# import os

# from config.env_config import setup_env

from src.utils.logging_utils import setup_logger
from src.extract.extract import extract_data


def main():
    # Get the argument from the run_etl command and set up the environment
    # setup_env(sys.argv)

    logger = setup_logger("pipeline", "pipeline.log")

    try:
        # E
        logger.info("Starting Extraction")
        extracted_data = extract_data()
        logger.info("Extraction successful")

        print(
            "ETL pipeline run successfully"
            # f"{os.getenv('ENV', 'error')} environment!"
        )

    except Exception as e:
        logger.error(f"ETL error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
