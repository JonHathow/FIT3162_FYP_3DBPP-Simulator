import unittest
import sys
import time
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


class O1_Analysis(unittest.TestCase):

    # @patch('builtins.input')
    # def test_ts1(self, mock_input):
    #     """
    #     1 bins, 5 types of 30 boxes
    #     """
        
    #     mock_input.side_effect = ["3", "101", "4", "101", "5", "0"]
    #     start_time = time.time()
    #     O1_Input()
    #     end_time = time.time()
    #     elapsed_time = end_time - start_time
    #     print(f"Function execution time: {elapsed_time} seconds")
        

    # @patch('builtins.input')
    # def test_ts2(self, mock_input):
    #     """
    #     3 bins, 10 types of 30 boxes
    #     """
        
    #     mock_input.side_effect = ["3", "102", "4", "102", "5", "0"]
    #     start_time = time.time()
    #     O1_Input()
    #     end_time = time.time()
    #     elapsed_time = end_time - start_time
    #     print(f"Function execution time: {elapsed_time} seconds")

    @patch('builtins.input')
    def test_ts3(self, mock_input):
        """
        5 bins, 15 types of 30 boxes
        """
        
        mock_input.side_effect = ["3", "103", "4", "103", "5", "0"]
        start_time = time.time()
        O1_Input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function execution time: {elapsed_time} seconds")
        

class O2_Analysis(unittest.TestCase):

    # @patch('builtins.input')
    # def test_ts1(self, mock_input):
    #     """
    #     1 bins, 5 types of 30 boxes
    #     """
        
    #     mock_input.side_effect = ["3", "101", "4", "101", "5", "0"]
    #     start_time = time.time()
    #     O2_Input()
    #     end_time = time.time()
    #     elapsed_time = end_time - start_time
    #     print(f"Function execution time: {elapsed_time} seconds")

    # @patch('builtins.input')
    # def test_ts2(self, mock_input):
    #     """
    #     3 bins, 10 types of 30 boxes
    #     """
        
    #     mock_input.side_effect = ["3", "102", "4", "102", "5", "0"]
    #     start_time = time.time()
    #     O2_Input()
    #     end_time = time.time()
    #     elapsed_time = end_time - start_time
    #     print(f"Function execution time: {elapsed_time} seconds")

    @patch('builtins.input')
    def test_ts3(self, mock_input):
        """
        5 bins, 15 types of 30 boxes
        """
        
        mock_input.side_effect = ["3", "103", "4", "103", "5", "0"]
        start_time = time.time()
        O2_Input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function execution time: {elapsed_time} seconds")
        
    




if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(O1_Analysis))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(O2_Analysis))
    runner = unittest.TextTestRunner()
    runner.run(suite)