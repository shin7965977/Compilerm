import unittest
from unittest.mock import patch
import data_visualization
import Hypothesis_test
import pandas as pd


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
