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

class Test_Integration(unittest.TestCase):

    def test_temp(self):
        O1_Input()

    @patch('builtins.input')
    def test_Dataflow_Interface(self, mock_input):
        """
        Data Flow Testing:
        This test verifies that data flows correctly between different modules or components, making it an integration test focused on data integration.

        Interface Testing:
        Testing the interfaces between different components to ensure they communicate effectively
        
        In order to do this we will compare data from the input csv and output csv.
        Currently, comparison must be done manually

        Both these tests are combined as the different components must communicate to share data. Therefore by performing data flow testing
        we are also performing interface testing at the same time.
        """
        
        mock_input.side_effect = ["1", "1", "100", "100", "100", "3000", "2", "1", "1", "1", "10", "10", "10", "10", "y", "y", "3", "1", "4", "1", "5", "0"]
        O1_Input()
        self.assertTrue(os.path.exists("files_Option1\csv_inputs\csv_boxes\inputBoxes1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputFitted1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputUnfitted1.csv"))

        self.assertTrue(os.path.exists("files_Option1\csv_inputs\csv_bins\inputBins1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputBins1.csv"))

        mock_input.side_effect = ["1", "1", "100", "100", "100", "3000", "2", "1", "1", "1", "10", "10", "10", "10", "3", "1", "4", "1", "5", "0"]
        O2_Input()
        self.assertTrue(os.path.exists("files_Option1\csv_inputs\csv_boxes\inputBoxes1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputFitted1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputUnfitted1.csv"))

        self.assertTrue(os.path.exists("files_Option1\csv_inputs\csv_bins\inputBins1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputBins1.csv"))

    
    
if __name__ == '__main__':
    try:
        shutil.rmtree('files_Option1')
        shutil.rmtree('files_Option2')
    except OSError as e:
        pass
    unittest.main()