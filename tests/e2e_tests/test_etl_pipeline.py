import subprocess
import sys
import os
from pathlib import Path


def test_full_etl_pipeline_success():
    # Set test environment and log directory
    env = os.environ.copy()
    env["ENV"] = "test"

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

    # Get directory
    project_root = find_root()

    # Run the ETL pipeline script
    result = subprocess.run(
        [sys.executable, "scripts/run_etl.py", "test"],
        cwd=str(project_root),
        env=env,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"ETL pipeline failed: {result.stderr}"

    # Verify one final output file was created
    output_file = os.path.join(
        project_root, "data/output/merged/checkin_checkout__gyms__users.csv"
    )

    assert Path(
        output_file
    ).exists(), f"Expected output file not created: {output_file}"

    # Verify one output file has data
    import pandas as pd

    result_df = pd.read_csv(output_file)
    assert len(result_df) > 0, "Output file is empty"
    assert "user_id" in result_df.columns, "Missing expected column in output"
