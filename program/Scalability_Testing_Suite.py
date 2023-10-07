import unittest
import sys
import os
from io import StringIO
from Option1_input import O1_Input
from Option2_input import O2_Input
from unittest.mock import patch
import shutil

# Captures functions output
def capture_output(function, *args):
    captured_output = StringIO()
    sys.stdout = captured_output
    function(*args)
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()


class Test_Scalability_O1_small(unittest.TestCase):

    # def test_smthereadwad(self):
    #     O1_Input()

    @patch('builtins.input')
    def test_ss1(self, mock_input):
        """
        small scale tests where the number of bins and items do not exceed 10
        """
        
        mock_input.side_effect = ["1", "2", "100", "100", "100", "3000", "2", "1", "3", "1", "10", "10", "10", "10", "y", "y", "3", "1", "4", "1", "5", "0"]
        O1_Input()

    @patch('builtins.input')
    def test_ss2(self, mock_input):
        """
        small scale tests where the number of bins and items do not exceed 10
        """
        
        mock_input.side_effect = ["1", "3", "100", "100", "100", "3000", "2", "1", "10", "1", "10", "10", "10", "10", "y", "y", "3", "1", "4", "1", "5", "0"]
        O1_Input()

    @patch('builtins.input')
    def test_ss3(self, mock_input):
        """
        small scale tests where the number of bins and items do not exceed 10
        """
        
        mock_input.side_effect = ["1", "5", "100", "100", "100", "3000", "2", "2", "5", "1", "10", "10", "10", "10", "y", "y", "3", "1", "4", "1", "5", "0"]
        O1_Input()
    

class Test_Scalability_O1_medium(unittest.TestCase):

    @patch('builtins.input')
    def test_ms1(self, mock_input):
        """
        medium scale tests where the number of bins and items are between 10 and 50
        """
        
        mock_input.side_effect = ["1", "10", "100", "100", "100", "3000", "2", "3", "5", "1", "10", "10", "10", "10", "y", "y", "3", "1", "4", "1", "5", "0"]
        O1_Input()

    @patch('builtins.input')
    def test_ms2(self, mock_input):
        """
        medium scale tests where the number of bins and items are between 10 and 50
        """
        
        mock_input.side_effect = ["1", "25", "100", "100", "100", "3000", "2", "3", "10", "1", "10", "10", "10", "10", "y", "y", "3", "2", "4", "2", "5", "0"]
        O1_Input()

    @patch('builtins.input')
    def test_ms3(self, mock_input):
        """
        medium scale tests where the number of bins and items are between 10 and 50
        """
        
        mock_input.side_effect = ["1", "45", "100", "100", "100", "3000", "2", "5", "9", "1", "10", "10", "10", "10", "y", "y", "3", "2", "4", "2", "5", "0"]
        O1_Input()


class Test_Scalability_O1_large(unittest.TestCase):

    @patch('builtins.input')
    def test_ls1(self, mock_input):
        """
        large scale tests where the number of bins and items are between 50 and 100
        """
        
        mock_input.side_effect = ["1", "51", "100", "100", "100", "3000", "2", "4", "13", "1", "10", "10", "10", "10", "y", "y", "3", "1", "4", "1", "5", "0"]
        O1_Input()

    # @patch('builtins.input')
    # def test_ls2(self, mock_input):
    #     """
    #     large scale tests where the number of bins and items are between 50 and 100
    #     """
        
    #     mock_input.side_effect = ["1", "75", "100", "100", "100", "3000", "2", "5", "15", "1", "10", "10", "10", "10", "y", "y", "3", "3", "4", "3", "5", "0"]
    #     O1_Input()

    # @patch('builtins.input')
    # def test_ls3(self, mock_input):
    #     """
    #     large scale tests where the number of bins and items are between 50 and 100
    #     """
        
    #     mock_input.side_effect = ["1", "89", "100", "100", "100", "3000", "2", "15", "6", "1", "10", "10", "10", "10", "y", "y", "3", "3", "4", "3", "5", "0"]
    #     O1_Input()


class Test_Scalability_O2_small(unittest.TestCase):

    # def test_smthereadwad(self):
    #     O1_Input()

    @patch('builtins.input')
    def test_ss1(self, mock_input):
        """
        small scale tests where the number of bins and items do not exceed 10
        """
        
        mock_input.side_effect = ["1", "2", "100", "100", "100", "3000", "2", "1", "3", "1", "10", "10", "10", "10", "3", "1", "4", "1", "5", "0"]
        O2_Input()

    @patch('builtins.input')
    def test_ss2(self, mock_input):
        """
        small scale tests where the number of bins and items do not exceed 10
        """
        
        mock_input.side_effect = ["1", "3", "100", "100", "100", "3000", "2", "1", "10", "1", "10", "10", "10", "10", "3", "1", "4", "1", "5", "0"]
        O2_Input()

    @patch('builtins.input')
    def test_ss3(self, mock_input):
        """
        small scale tests where the number of bins and items do not exceed 10
        """
        
        mock_input.side_effect = ["1", "5", "100", "100", "100", "3000", "2", "2", "5", "1", "10", "10", "10", "10", "3", "1", "4", "1", "5", "0"]
        O2_Input()
    

class Test_Scalability_O2_medium(unittest.TestCase):

    @patch('builtins.input')
    def test_ms1(self, mock_input):
        """
        medium scale tests where the number of bins and items are between 10 and 50
        """
        
        mock_input.side_effect = ["1", "10", "100", "100", "100", "3000", "2", "3", "5", "1", "10", "10", "10", "10", "3", "2", "4", "2", "5", "0"]
        O2_Input()

    @patch('builtins.input')
    def test_ms2(self, mock_input):
        """
        medium scale tests where the number of bins and items are between 10 and 50
        """
        
        mock_input.side_effect = ["1", "25", "100", "100", "100", "3000", "2", "3", "10", "1", "10", "10", "10", "10", "3", "2", "4", "2", "5", "0"]
        O2_Input()

    @patch('builtins.input')
    def test_ms3(self, mock_input):
        """
        medium scale tests where the number of bins and items are between 10 and 50
        """
        
        mock_input.side_effect = ["1", "45", "100", "100", "100", "3000", "2", "5", "9", "1", "10", "10", "10", "10", "3", "2", "4", "2", "5", "0"]
        O2_Input()


class Test_Scalability_O2_large(unittest.TestCase):

    @patch('builtins.input')
    def test_ls1(self, mock_input):
        """
        large scale tests where the number of bins and items are between 50 and 100
        """
        
        mock_input.side_effect = ["1", "51", "100", "100", "100", "3000", "2", "10", "11", "1", "10", "10", "10", "10", "3", "3", "4", "3", "5", "0"]
        O2_Input()

    @patch('builtins.input')
    def test_ls2(self, mock_input):
        """
        large scale tests where the number of bins and items are between 50 and 100
        """
        
        mock_input.side_effect = ["1", "75", "100", "100", "100", "3000", "2", "5", "15", "1", "10", "10", "10", "10", "3", "3", "4", "3", "5", "0"]
        O2_Input()

    @patch('builtins.input')
    def test_ls3(self, mock_input):
        """
        large scale tests where the number of bins and items are between 50 and 100
        """
        
        mock_input.side_effect = ["1", "89", "100", "100", "100", "3000", "2", "15", "6", "1", "10", "10", "10", "10", "3", "3", "4", "3", "5", "0"]
        O2_Input()

    
if __name__ == '__main__':
    try:
        shutil.rmtree('files_Option1')
        shutil.rmtree('files_Option2')
    except OSError as e:
        pass

    suite = unittest.TestSuite()
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Scalability_O1_small))
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Scalability_O1_medium))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Scalability_O1_large))
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Scalability_O2_small))
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Scalability_O2_medium))
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Scalability_O2_large))
    runner = unittest.TextTestRunner()
    runner.run(suite)