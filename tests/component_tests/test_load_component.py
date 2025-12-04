import pytest
import pandas as pd
from unittest.mock import patch, call
from src.etl.load.load import load_data


class TestLoadData:
    """Component tests for load_data function"""

    @pytest.fixture
    def sample_dataframe(self):
        """Sample DataFrame for testing"""
        return pd.DataFrame(
            {
                "customer_id": [1, 2, 3],
                "amount": [100.0, 200.0, 300.0],
                "transaction_date": ["2023-01-01", "2023-01-02", "2023-01-03"],
            }
        )

    @pytest.fixture
    def empty_dataframe(self):
        """Empty DataFrame for testing"""
        return pd.DataFrame()

    def test_load_data_success(self, sample_dataframe):
        """Test successful data loading with valid DataFrame"""
        with patch("src.etl.load.load.save_dataframe_to_csv") as mock_create:
            with patch("src.etl.load.load.logger") as mock_logger:
                load_data(
                    [
                        sample_dataframe,
                        sample_dataframe,
                        sample_dataframe,
                        sample_dataframe,
                    ]
                )

        # Verify component coordination
        calls = mock_create.call_args_list
        assert calls[0] == call(
            sample_dataframe,
            "data/output/single_tables",
            "checkin_checkout.csv",
        )
        assert calls[1] == call(
            sample_dataframe, "data/output/single_tables", "users.csv"
        )
        assert calls[2] == call(
            sample_dataframe,
            "data/output/merged",
            "users__sub_plans.csv",
        )
        assert calls[3] == call(
            sample_dataframe,
            "data/output/merged",
            "checkin_checkout__gyms__users.csv",
        )

        # Verify logging
        mock_logger.info.assert_any_call("Data loading started!")
        mock_logger.info.assert_any_call("Data loading completed!")

    def test_load_data_empty_dataframe(self, empty_dataframe):
        """Test handling of empty DataFrame"""
        df1 = empty_dataframe
        df2 = empty_dataframe
        df3 = empty_dataframe
        df4 = empty_dataframe
        with patch("src.etl.load.load.save_dataframe_to_csv") as mock_create:
            with patch("src.etl.load.load.logger") as mock_logger:
                load_data([df1, df2, df3, df4])

        # Verify early return behaviour
        mock_create.assert_not_called()
        mock_logger.warning.assert_called_once_with(
            "transformed_data is empty -> no data to load"
        )

    def test_load_data_none_in_input_dataframes(self):
        """Test handling of None input"""
        with patch("src.etl.load.load.save_dataframe_to_csv") as mock_create:
            with patch("src.etl.load.load.logger") as mock_logger:
                load_data([None])

        # Verify early return behaviour
        mock_create.assert_not_called()
        mock_logger.warning.assert_called_once_with(
            "transformed_data is empty -> no data to load"
        )

    def test_load_data_with_dataframe_containing_nulls(self):
        """Test handling of DataFrame with null values"""
        df_with_nulls = pd.DataFrame(
            {
                "customer_id": [1, 2, None],
                "amount": [100.0, None, 300.0],
                "transaction_date": ["2023-01-01", "2023-01-02", None],
            }
        )

        with patch("src.etl.load.load.save_dataframe_to_csv") as mock_create:
            with patch("src.etl.load.load.logger") as mock_logger:
                load_data(
                    [
                        df_with_nulls,
                        df_with_nulls,
                        df_with_nulls,
                        df_with_nulls,
                    ]
                )

        # Should still process (not considered empty)
        calls = mock_create.call_args_list
        assert calls[0] == call(
            df_with_nulls,
            "data/output/single_tables",
            "checkin_checkout.csv",
        )
        assert calls[1] == call(
            df_with_nulls, "data/output/single_tables", "users.csv"
        )
        assert calls[2] == call(
            df_with_nulls,
            "data/output/merged",
            "users__sub_plans.csv",
        )
        assert calls[3] == call(
            df_with_nulls,
            "data/output/merged",
            "checkin_checkout__gyms__users.csv",
        )
        mock_logger.info.assert_any_call("Data loading started!")

    def test_load_data_component_coordination(self, sample_dataframe):
        """Test that load_data properly coordinates with database component"""
        with patch("src.etl.load.load.save_dataframe_to_csv") as mock_create:
            # Simulate successful database operation
            mock_create.return_value = None

            with patch("src.etl.load.load.logger") as mock_logger:
                result = load_data(
                    [
                        sample_dataframe,
                        sample_dataframe,
                        sample_dataframe,
                        sample_dataframe,
                    ]
                )

        # Verify coordination
        assert result is None  # Function returns None on success
        calls = mock_create.call_args_list
        assert calls[0] == call(
            sample_dataframe,
            "data/output/single_tables",
            "checkin_checkout.csv",
        )
        assert calls[1] == call(
            sample_dataframe, "data/output/single_tables", "users.csv"
        )
        assert calls[2] == call(
            sample_dataframe,
            "data/output/merged",
            "users__sub_plans.csv",
        )
        assert calls[3] == call(
            sample_dataframe,
            "data/output/merged",
            "checkin_checkout__gyms__users.csv",
        )

        # Verify complete logging flow
        expected_calls = [
            "Data loading started!",
            "Data loading completed!",
        ]

        actual_calls = [
            call.args[0] for call in mock_logger.info.call_args_list
        ]
        assert all(expected in actual_calls for expected in expected_calls)
