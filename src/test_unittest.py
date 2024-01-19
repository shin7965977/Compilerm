import unittest
from unittest.mock import patch
import data_visualization
import Hypothesis_test
import pandas as pd


class TestCSVUpload(unittest.TestCase):

    def test_upload_and_read_csv_with_real_file(self):
        # Specify the actual CSV file path
        csv_file_path = 'data/raw data 2.csv'

        # Call the function with the actual file
        result_df = data_visualization.upload_and_read_csv(csv_file_path)

        # Create the expected DataFrame for comparison
        expected_df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})

        # Check if the result matches the expectation
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_file_not_found(self):
        # Specify an invalid file path
        csv_file_path = 'data/nonexistent.csv'

        # Call the function which should handle the file not found case
        result_df = data_visualization.upload_and_read_csv(csv_file_path)

        # The result should be None if the file is not found
        self.assertIsNone(result_df)


class TestHypothesis(unittest.TestCase):

    @patch('builtins.input', side_effect=['10', '20'])
    def test_hypothesis_test_ROI(self, mock_inputs):
        data = {'date': ['2021-01-01', '2021-01-02'],
                'ad Cost': [100, 150],
                'Buy': [10, 20]}
        df = pd.DataFrame(data)

        Hypothesis_test.hypothesis_test_ROI(df, df)

    @patch('builtins.input', side_effect=['10', '20'])
    def test_hypothesis_test_Buy(self, mock_inputs):
        data = {'date': ['2021-01-01', '2021-01-02'],
                'ad Cost': [100, 150],
                'Buy': [10, 20]}
        df = pd.DataFrame(data)

        Hypothesis_test.hypothesis_test_Buy(df, df)


if __name__ == '__main__':
    unittest.main()
