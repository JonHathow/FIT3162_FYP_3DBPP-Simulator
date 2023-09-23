import unittest
import sys
from io import StringIO
from program.Option1_input import O1_input, O1_input_test
from program.Option2_input import O2_input
from unittest.mock import patch
import shutil

# Captures functions output
def capture_output(function, *args):
    captured_output = StringIO()
    sys.stdout = captured_output
    function(*args)
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

class TestAux(unittest.TestCase):
    # Testing the interaction between Option1_input.py and Option 1
    @patch('builtins.input')
    def test_Option1_input(self, mock_input):
        mock_input.side_effect = ["1", "0", "1", "100", "200", "200", "1000", "2", "0", "2", "1", "1", "20", "100", "10", "200", "n", "n", "n", "3", "1", "4", "1", "0", "0"]
        # captured_output = capture_output(O1_input_test)
        O1_input_test()
        # self.assertEqual(captured_output, expected_output)
        
    # def test_Option1_input(self):
    #     O1_input()
    
if __name__ == '__main__':
    try:
        shutil.rmtree('files_Option1')
        shutil.rmtree('files_Option2')
    except OSError as e:
        pass
    unittest.main()