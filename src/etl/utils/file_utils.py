import os
import pandas as pd


def find_root(maker_file: str = "README.md") -> str:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != os.path.dirname(current_dir):
        # print(current_dir)
        if maker_file in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    raise FileNotFoundError(
        f"Maker file {maker_file} not found in any parent directories"
    )


def save_dataframe_to_csv(
    df: pd.DataFrame, relative_output_dir: str, filename: str
) -> None:
    whole_output_dir = os.path.join(find_root(), relative_output_dir)
    os.makedirs(whole_output_dir, exist_ok=True)
    df.to_csv(os.path.join(whole_output_dir, filename), index=False)
    return os.path.join(whole_output_dir, filename)
