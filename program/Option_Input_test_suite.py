from Option1_input import O1_Input
from Option2_input import O2_Input
from unittest.mock import patch
import unittest
import shutil
import sys
import os
from io import StringIO


"""
Integration tests for option 1 and option 2 input functions

Each option interacts with:
- input CSV module
- The options code stored in Option1/2_pacakge folder
- output CSV module
"""

# 1 Bin 1 Box
class Test_O1_Inputs_1(unittest.TestCase):

    @patch('builtins.input')
    def test_Option1_input(self, mock_input):
        mock_input.side_effect = ["1", "1", "100", "100", "100", "3000", "2", "1", "1", "1", "10", "10", "10", "10", "y", "y", "3", "1", "4", "1", "5", "0"]
        O1_Input()
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputBins1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputFitted1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputSummary1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputUnfitted1.csv"))


# 1 Bin 3 Identical Boxes
class Test_O1_Inputs_2(unittest.TestCase):

    @patch('builtins.input')
    def test_Option1_input(self, mock_input):
        mock_input.side_effect = ["1", "1", "100", "100", "100", "3000", "2", "1", "3", "3", "10", "10", "10", "10", "y", "y", "3", "2", "4", "2", "5", "0"]
        O1_Input()
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputBins2.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputFitted2.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputSummary2.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputUnfitted2.csv"))


# 1 Bin 2 types of 2 boxes (total 4)
class Test_O1_Inputs_3(unittest.TestCase):

    @patch('builtins.input')
    def test_Option1_input(self, mock_input):
        mock_input.side_effect = ["1", "1", "100", "100", "100", "3000", "2", "2", "2", "2", "10", "50", "10", "50", "y", "y", "3", "3", "4", "3", "5", "0"]
        O1_Input()
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputBins3.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputFitted3.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputSummary3.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputUnfitted3.csv"))


# 2 Bins 5 types of 2 boxes (total 10)
class Test_O1_Inputs_4(unittest.TestCase):

    @patch('builtins.input')
    def test_Option1_input(self, mock_input):
        mock_input.side_effect = ["1", "2", "100", "100", "100", "3000", "2", "5", "2", "2", "5", "15", "5", "15", "y", "y", "3", "4", "4", "4", "5", "0"]
        O1_Input()
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputBins4.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputFitted4.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputSummary4.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputUnfitted4.csv"))


# 1 Bin 1 Box
class Test_O2_Inputs_1(unittest.TestCase):

    @patch('builtins.input')
    def test_Option2_input(self, mock_input):
        mock_input.side_effect = ["1", "1", "100", "100", "100", "3000", "2", "1", "1", "1", "10", "10", "10", "10", "3", "1", "4", "1", "5", "0"]
        O2_Input()
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputBins1.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputFitted1.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputSummary1.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputUnfitted1.csv"))


# 1 Bin 3 Identical Boxes
class Test_O2_Inputs_2(unittest.TestCase):

    @patch('builtins.input')
    def test_Option2_input(self, mock_input):
        mock_input.side_effect = ["1", "1", "100", "100", "100", "3000", "2", "1", "3", "3", "10", "10", "10", "10", "3", "2", "4", "2", "5", "0"]
        O2_Input()
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputBins2.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputFitted2.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputSummary2.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputUnfitted2.csv"))


# 1 Bin 2 types of 2 boxes (total 4)
class Test_O2_Inputs_3(unittest.TestCase):

    @patch('builtins.input')
    def test_Option2_input(self, mock_input):
        mock_input.side_effect = ["1", "1", "100", "100", "100", "3000", "2", "2", "2", "2", "10", "50", "10", "50", "3", "3", "4", "3", "5", "0"]
        O2_Input()
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputBins3.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputFitted3.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputSummary3.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputUnfitted3.csv"))


# 2 Bins 5 types of 2 boxes (total 10)
class Test_O2_Inputs_4(unittest.TestCase):

    @patch('builtins.input')
    def test_Option2_input(self, mock_input):
        mock_input.side_effect = ["1", "2", "100", "100", "100", "3000", "2", "5", "2", "2", "5", "15", "5", "15", "3", "4", "4", "4", "5", "0"]
        O2_Input()
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputBins4.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputFitted4.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputSummary4.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputUnfitted4.csv"))




if __name__ == '__main__':
    try:
        shutil.rmtree('files_Option1')
        shutil.rmtree('files_Option2')
    except OSError as e:
        pass
    
    suite = unittest.TestSuite()
    # Adding tests to test suite
    # This ensures tests are run in a certain order
    # Needed as some tests require the files to have been created by previous tests
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O1_Inputs_1))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O1_Inputs_2))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O1_Inputs_3))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O1_Inputs_4))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O2_Inputs_1))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O2_Inputs_2))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O2_Inputs_3))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O2_Inputs_4))
    runner = unittest.TextTestRunner()
    runner.run(suite)