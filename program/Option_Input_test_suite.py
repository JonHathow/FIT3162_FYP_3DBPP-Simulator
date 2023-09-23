#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from manage_csv import InputBinParameters, InputBoxParameters, prompt_range, prompt_number, prompt_boolean, prompt_integer, get_input, prompt_input_bins, write_input_bin_func
from manage_csv import Option, Mode, MENU_INPUT, MENU_INVALID, MENU_END, MENU_BIN_NOTLOADED, FILE_BIN_1, FILE_BOX_1, FILE_BOX_2, PROMPT_TYPE_BOX, FILE_BINCOUNT_1, FILE_BOXCOUNT_1
from manage_csv import PROMPT_LASTFILE_BIN, PROMPT_LASTFILE_BOX, FILE_BOXCOUNT_2
from manage_csv import prompt_input_boxes, write_input_box_func
from manage_csv import fetch_filename, read_input
from manage_csv import update_filecount, fix_filecount, fetch_filecount
from Option1_input import O1_input
from Option2_input import O2_input
from unittest.mock import patch
import unittest
import csv
import os
import shutil

class TestAux(unittest.TestCase):

    @patch('builtins.input')
    def test_Option1_input(self, mock_input):
        mock_input.side_effect = ["1", "0", "3", "100", "200", "200", "1000", "2", "0", "3", "1", "5", "20", "500", "200", "10000", "n", "n", "n", "3", "1", "4", "1", "0"]
        O1_input()

    @patch('builtins.input')
    def test_Option2_input(self, mock_input):
        mock_input.side_effect = ["1", "0", "3", "100", "200", "200", "1000", "2", "0", "3", "1", "5", "20", "500", "200", "10000", "3", "1", "4", "1", "0"]
        O2_input()

if __name__ == '__main__':
    try:
        shutil.rmtree('files_Option1')
        shutil.rmtree('files_Option2')
    except OSError as e:
        pass
    
    unittest.main()