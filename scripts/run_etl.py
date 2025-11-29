# import os
# import sys

# from config.env_config import setup_env
# from src.utils.logging_utils import setup_logger

from src.extract.extract import extract_data


def main():
    # Get the argument from the run_etl command and set up the environment
    # setup_env(sys.argv)

    # Logger setup

    try:
        # Logger

        # E
        extracted_data = extract_data()
        print(extracted_data)

        print(
            "ETL pipeline run successfully in "
            # f"{os.getenv('ENV', 'error')} environment!"
        )

    except Exception as e:
        raise Exception(f"Data extraction error in extract.py: {str(e)}")


if __name__ == "__main__":
    main()
