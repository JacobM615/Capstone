import subprocess
import sys
import os
from pathlib import Path


def test_full_etl_pipeline_success():
    """E2E test: Complete ETL pipeline execution with output validation"""
    # Set test environment and log directory
    env = os.environ.copy()
    env["ENV"] = "test"

    # Get directories
    project_root = Path(__file__).parent.parent.parent
    test_logs_dir = Path(__file__).parent.parent / "logs"
    test_logs_dir.mkdir(exist_ok=True)
    env["LOG_BASE_PATH"] = str(test_logs_dir)

    # Run the ETL pipeline script
    result = subprocess.run(
        [sys.executable, "scripts/run_etl.py", "test"],
        cwd=str(project_root),
        env=env,
        capture_output=True,
        text=True,
    )

    # Verify pipeline executed successfully
    assert result.returncode == 0, f"ETL pipeline failed: {result.stderr}"

    # Verify log file was created and contains expected stages
    log_file = test_logs_dir / "logs" / "etl_pipeline.log"
    assert (
        log_file.exists()
    ), f"ETL pipeline log file not created at {log_file}"

    log_content = log_file.read_text()
    assert "Starting ETL pipeline" in log_content
    assert "Beginning data extraction phase" in log_content
    assert "Data extraction phase completed" in log_content
    assert "ETL pipeline completed successfully" in log_content

    # Verify final output file was created
    output_file = (
        project_root / "data" / "processed" / "high_value_customers.csv"
    )
    assert (
        output_file.exists()
    ), f"Expected output file not created: {output_file}"

    # Verify output file has data
    import pandas as pd

    result_df = pd.read_csv(output_file)
    assert len(result_df) > 0, "Output file is empty"
    assert (
        "customer_id" in result_df.columns
    ), "Missing expected column in output"
