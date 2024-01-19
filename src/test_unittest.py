import unittest
from unittest.mock import patch
from io import StringIO
import sys
import data_visualization
import Hypothesis_test
import pandas as pd


class TestCSVUpload(unittest.TestCase):

    def test_upload_and_read_csv(self):
        # Create a mock CSV file
        test_csv = StringIO("col1,col2\n1,2\n3,4")
        
        # Modify standard input to simulate user input for the file path
        sys.stdin = test_csv

        # Call the function
        result_df = data_visualization.upload_and_read_csv()

        # Create the expected DataFrame for comparison
        expected_df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})
        
        # Check if the result matches the expectation
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_file_not_found(self):
        # Test for the case where the file does not exist
        sys.stdin = StringIO("nonexistent.csv")
        result = data_visualization.upload_and_read_csv()
        self.assertIsNone(result)

class TestHypothesis(unittest.TestCase):

    @patch('builtins.input', side_effect=['10', '20'])
    def test_hypothesis_test_ROI(self, mock_inputs):
        # Create test data
        data = {'date': ['2021-01-01', '2021-01-02'],
                'ad Cost': [100, 150],
                'Buy': [10, 20]}
        df = pd.DataFrame(data)

        # Call the test function
        Hypothesis_test.hypothesis_test_ROI(df, df)
        # You can add assert statements to verify output or function state

    @patch('builtins.input', side_effect=['10', '20'])
    def test_hypothesis_test_Buy(self, mock_inputs):
        # Create test data
        data = {'date': ['2021-01-01', '2021-01-02'],
                'ad Cost': [100, 150],
                'Buy': [10, 20]}
        df = pd.DataFrame(data)

        # Call the test function
        Hypothesis_test.hypothesis_test_Buy(df, df)
        # You can add assert statements to verify output or function state

if __name__ == '__main__':
    unittest.main()
