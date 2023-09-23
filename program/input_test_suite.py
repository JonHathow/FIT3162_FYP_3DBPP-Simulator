#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from manage_csv import InputBinParameters, InputBoxParameters, prompt_range, prompt_number, prompt_boolean, prompt_integer, get_input, prompt_input_bins, write_input_bin_func
from manage_csv import Option, Mode, MENU_INPUT, MENU_INVALID, MENU_END, MENU_BIN_NOTLOADED, FILE_BIN_1, FILE_BOX_1, FILE_BOX_2, PROMPT_TYPE_BOX, FILE_BINCOUNT_1, FILE_BOXCOUNT_1
from manage_csv import PROMPT_LASTFILE_BIN, PROMPT_LASTFILE_BOX, FILE_BOXCOUNT_2
from manage_csv import prompt_input_boxes, write_input_box_func
from manage_csv import fetch_filename, read_input
from manage_csv import update_filecount, fix_filecount, fetch_filecount
from Option1_input import O1_input
from unittest.mock import patch
import shutil
import unittest
import csv
import os

class TestAux(unittest.TestCase):
    
    #                    #
    #  manage_csv tests  #
    #                    #

    # input_parameters.py
    def test_inputBinParametersConstructor(self):
        testClass1 = InputBinParameters(4, 100, 200, 500, 10000)
        self.assertEqual(testClass1.qty, 4)
        self.assertEqual(testClass1.width, 100)
        self.assertEqual(testClass1.height, 200)
        self.assertEqual(testClass1.depth, 500)
        self.assertEqual(testClass1.capacity, 10000)

        testClass2 = InputBinParameters("4", False, 200.24, InputBinParameters(0,0,0,0,0), 20000)
        self.assertEqual(testClass2.qty, "4")
        self.assertEqual(testClass2.width, False)
        self.assertEqual(testClass2.height, 200.24)
        self.assertEqual(testClass2.depth.__str__(), "\nqty: 0\nwidth: 0\nheight: 0\ndepth: 0\ncapacity: 0\n")
        self.assertEqual(testClass2.capacity, 20000)

    def test_inputBinParametersString(self):
        testClass1 = InputBinParameters(4, 100, 200, 500, 10000)
        self.assertEqual(testClass1.__str__(),  "\nqty: 4\nwidth: 100\nheight: 200\ndepth: 500\ncapacity: 10000\n")

        testClass2 = InputBinParameters("4", False, 200.24, InputBinParameters(0,0,0,0,0), 20000)
        self.assertEqual(testClass2.__str__(),  "\nqty: 4\nwidth: False\nheight: 200.24\ndepth: \nqty: 0\nwidth: 0\nheight: 0\ndepth: 0\ncapacity: 0\n\ncapacity: 20000\n")

    def test_inputBoxParametersConstructor(self):
        testClass1 = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        self.assertEqual(testClass1.types, 3)
        self.assertEqual(testClass1.qty_lo, 1)
        self.assertEqual(testClass1.qty_hi, 10)
        self.assertEqual(testClass1.dim_lo, 100)
        self.assertEqual(testClass1.dim_hi, 1000)
        self.assertEqual(testClass1.wgt_lo, 50)
        self.assertEqual(testClass1.wgt_hi, 300)

        # attributes not affected by constructor
        self.assertEqual(testClass1.level_var, False)
        self.assertEqual(testClass1.loadbear_var, False)
        self.assertEqual(testClass1.updown_var, False)
        self.assertEqual(testClass1.updown, False)

        # Other data types
        testClass2 = InputBoxParameters("3", False, 'c', 46.78, InputBoxParameters(0, 0, 0, 0, 0, 0, 0), 50, 300)
        self.assertEqual(testClass2.types, "3")
        self.assertEqual(testClass2.qty_lo, False)
        self.assertEqual(testClass2.qty_hi, 'c')
        self.assertEqual(testClass2.dim_lo, 46.78)
        self.assertEqual(testClass2.dim_hi.__str__(), "\ntypes: 0\nqty_lo: 0, qty_hi: 0\ndim_lo: 0, dim_hi: 0\nwgt_lo: 0, wgt_hi: 0\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n")
        self.assertEqual(testClass2.wgt_lo, 50)
        self.assertEqual(testClass2.wgt_hi, 300)

        # attributes not affected by constructor
        self.assertEqual(testClass2.level_var, False)
        self.assertEqual(testClass2.loadbear_var, False)
        self.assertEqual(testClass2.updown_var, False)
        self.assertEqual(testClass2.updown, False)

    def test_inputBoxParametersString(self):
        testClass1 = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        self.assertEqual(testClass1.__str__(),"\ntypes: 3\nqty_lo: 1, qty_hi: 10\ndim_lo: 100, dim_hi: 1000\nwgt_lo: 50, wgt_hi: 300\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n")

        testClass2 = InputBoxParameters("3", False, 'c', 46.78, InputBoxParameters(0, 0, 0, 0, 0, 0, 0), 50, 300)
        self.assertEqual(testClass2.__str__(),"\ntypes: 3\nqty_lo: False, qty_hi: c\ndim_lo: 46.78, dim_hi: \ntypes: 0\nqty_lo: 0, qty_hi: 0\ndim_lo: 0, dim_hi: 0\nwgt_lo: 0, wgt_hi: 0\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n\nwgt_lo: 50, wgt_hi: 300\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n")

    # prompts.py
    @patch('builtins.input')
    def test_getInput(self, mock_input):
        mock_input.return_value = "4"
        self.assertEqual(get_input("height"),"4")

        mock_input.return_value = "four"
        self.assertEqual(get_input("height"),"four")

        mock_input.return_value = "True"
        self.assertEqual(get_input("height"),"True")

    @patch('manage_csv.prompts.get_input')
    def test_promptNumber(self, mock_get_input):

        # input always return string

        mock_get_input.return_value = "4"
        self.assertEqual(prompt_number("dimension"), float(4))

        mock_get_input.return_value = "4.56"
        self.assertEqual(prompt_number("dimension"), float(4.56))

        mock_get_input.return_value = "-45"
        self.assertEqual(prompt_number("dimension"), float(45))

        #                         infinite loop
        # mock_get_input.return_value = "Four"
        # self.assertEqual(prompt_number("dimension"), "ERROR: Invalid numeric input.")

        #                         infinite loop
        # mock_get_input.return_value = "True"
        # self.assertEqual(prompt_number("dimension"), "ERROR: Invalid numeric input.")

        #                         infinite loop
        # mock_get_input.return_value = "[42]"
        # self.assertEqual(prompt_number("dimension"), "ERROR: Invalid numeric input.")

    @patch('manage_csv.prompts.get_input')
    def test_promptInteger(self, mock_get_input):

        # input always return string

        mock_get_input.return_value = "4"
        self.assertEqual(prompt_integer("dimension"), 4)

        mock_get_input.return_value = "-45"
        self.assertEqual(prompt_integer("dimension"), 45)

        """
                                Infinite Loop

                                possible fix:
                convert from string input to float, then to int
        """
        # mock_get_input.return_value = "4.56"
        # self.assertEqual(prompt_integer("dimension"), int(4.56))

        #                         infinite loop
        # mock_get_input.return_value = "Four"
        # self.assertEqual(prompt_integer("dimension"), "ERROR: Invalid numeric input.")

        #                         infinite loop
        # mock_get_input.return_value = "True"
        # self.assertEqual(prompt_integer("dimension"), "ERROR: Invalid numeric input.")

        #                         infinite loop
        # mock_get_input.return_value = "[42]"
        # self.assertEqual(prompt_integer("dimension"), "ERROR: Invalid numeric input.")

    @patch('manage_csv.prompts.get_input')
    def test_promptRange(self, mock_get_input1):

        mock_get_input1.side_effect = ["1", "10"]
        self.assertEqual(prompt_range("containers needed"), (1,10))

        #                       Infinite Loop
        # mock_get_input1.return_value = "1.5"
        # mock_get_input2.return_value = "10.9"
        # self.assertEqual(prompt_range("containers needed"), 'ERROR: Invalid integer input.')

        #                       Infinite Loop
        # mock_get_input1.return_value = "Yes"
        # mock_get_input2.return_value = "No"
        # self.assertEqual(prompt_range("containers needed"), 'ERROR: Invalid integer input.')

    @patch('manage_csv.prompts.get_input')
    def test_promptBoolean(self, mock_get_input):

        mock_get_input.return_value = "y"
        self.assertEqual(prompt_boolean("to pass fit3162"), True)

        mock_get_input.return_value = "Y"
        self.assertEqual(prompt_boolean("to pass fit3162"), True)

        mock_get_input.return_value = "n"
        self.assertEqual(prompt_boolean("to pass fit3162"), False)

        mock_get_input.return_value = "N"
        self.assertEqual(prompt_boolean("to pass fit3162"), False)

        #                       Infinite Loop
        # mock_get_input.return_value = "yes"
        # self.assertEqual(prompt_boolean("to pass fit3162"), 'ERROR: Invalid input. Y/N only.')

        #                       Infinite Loop
        # mock_get_input.return_value = "24"
        # self.assertEqual(prompt_boolean("to pass fit3162"), 'ERROR: Invalid input. Y/N only.')
        

    # write_input_bin.py
    @patch('manage_csv.write_input_bin.prompt_number')
    @patch('manage_csv.write_input_bin.prompt_integer')
    def test_promptIBin(self, mock_prompt_integer, mock_prompt_number):

        # func to return the string func of input_parameters
        def retstr(item):
            return item.__str__()

        mock_prompt_integer.return_value = 4
        mock_prompt_number.side_effect = [2, 3.5, 4, 5.66]
        self.assertEqual(retstr(prompt_input_bins()),"\nqty: 4\nwidth: 2\nheight: 3.5\ndepth: 4\ncapacity: 5.66\n")

        # would never happen
        mock_prompt_integer.return_value = 4.5
        mock_prompt_number.side_effect = [2.8, "3.5", -4.5, "hello"]
        self.assertEqual(retstr(prompt_input_bins()),"\nqty: 4.5\nwidth: 2.8\nheight: 3.5\ndepth: -4.5\ncapacity: hello\n")

    @patch('manage_csv.write_input_bin.fetch_filecount')
    @patch('manage_csv.write_input_bin.prompt_input_bins')
    def test_writeIBinFunc(self, mock_prompt_input_bins, mock_fetch_filecount):
        mock_prompt_input_bins.return_value = InputBinParameters(4, 100, 200, 500, 10000)
        mock_fetch_filecount.return_value = 0
        write_input_bin_func(1)
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\inputBins1.csv'), True)

        mock_prompt_input_bins.return_value = InputBinParameters(4, 100, 200, 500, 10000)
        mock_fetch_filecount.return_value = 1
        write_input_bin_func(1)
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\inputBins2.csv'), True)
        

        mock_prompt_input_bins.return_value = InputBinParameters(4, 100, 200, 500, 10000)
        mock_fetch_filecount.return_value = 0
        write_input_bin_func(2)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\inputBins1.csv'), True)
        
        
        mock_prompt_input_bins.return_value = InputBinParameters(4, 100, 200, 500, 10000)
        mock_fetch_filecount.return_value = 0
        write_input_bin_func(3)
        self.assertEqual(os.path.exists('files_Option3\csv_inputs\inputBins1.csv'), False)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\inputBins2.csv'), False)

    # write_input_box.py
    @patch('manage_csv.write_input_box.prompt_boolean')
    @patch('manage_csv.write_input_box.prompt_range')
    @patch('manage_csv.write_input_box.prompt_integer')
    def test_promptIBoxes(self, mock_prompt_integer, mock_prompt_range,mock_prompt_bool):

        def retstr(item):
            return item.__str__()
        
        # works but should never happen since prompt range always returns int
        mock_prompt_bool.side_effect = [False, False, False]
        mock_prompt_range.side_effect = [(1,10),(1.5,10.2),(1,10)]
        mock_prompt_integer.return_value = 3
        self.assertEqual(retstr(prompt_input_boxes(1)), "\ntypes: 3\nqty_lo: 1, qty_hi: 10\ndim_lo: 1.5, dim_hi: 10.2\nwgt_lo: 1, wgt_hi: 10\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n")

        mock_prompt_bool.side_effect = [True, True, True]
        mock_prompt_range.side_effect = [(1,10),(1,10),(1,10)]
        mock_prompt_integer.return_value = 4
        self.assertEqual(retstr(prompt_input_boxes(1)), "\ntypes: 4\nqty_lo: 1, qty_hi: 10\ndim_lo: 1, dim_hi: 10\nwgt_lo: 1, wgt_hi: 10\nlevel_var: True\nloadbear_var: False\nupdown_var: True\nupdown: False\n")

        mock_prompt_bool.side_effect = [False, True, False]
        mock_prompt_range.side_effect = [(1,10),(1,10),(1,10)]
        mock_prompt_integer.return_value = 5
        self.assertEqual(retstr(prompt_input_boxes(2)), "\ntypes: 5\nqty_lo: 1, qty_hi: 10\ndim_lo: 1, dim_hi: 10\nwgt_lo: 1, wgt_hi: 10\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n")


        mock_prompt_range.side_effect = [(1.2,10.2),(1.5,10.2),(1,10)]
        # Should give error, documentation shows quantity and weight should be int and dim is float
        # with self.assertRaises(TypeError):
        #     self.assertEqual(retstr(prompt_input_boxes(1)), "\ntypes: 3\nqty_lo: 1.2, qty_hi: 10.2\ndim_lo: 1.5, dim_hi: 10.2\nwgt_lo: 1, wgt_hi: 10\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n")
    
    @patch('manage_csv.write_input_box.fetch_filecount')
    @patch('manage_csv.write_input_box.prompt_input_boxes')
    def test_writeIBoxFunc(self, mock_prompt_input_boxes, mock_fetch_filecount):
        mock_prompt_input_boxes.return_value = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 0
        write_input_box_func(1)
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\inputBoxes1.csv'), True)

        mock_prompt_input_boxes.return_value = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 1
        write_input_box_func(1)
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\inputBoxes2.csv'), True)

        mock_prompt_input_boxes.return_value = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 0
        write_input_box_func(2)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\inputBoxes1.csv'), True)

        mock_prompt_input_boxes.return_value = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 0
        write_input_box_func(3)
        self.assertEqual(os.path.exists('files_Option3\csv_inputs\inputBoxes1.csv'), False)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\inputBoxes2.csv'), False)


    # read_input_csv.py
    @patch('manage_csv.read_input_csv.prompt_integer')
    def test_fetch_filename(self, mock_prompt_integer):
        mock_prompt_integer.return_value = 1
        self.assertEqual(fetch_filename(FILE_BOX_1, PROMPT_TYPE_BOX), "files_Option1\csv_inputs\inputBoxes1.csv")

        mock_prompt_integer.return_value = 123456
        self.assertEqual(fetch_filename("My IQ ----->", "Doesnt really matter"), "My IQ ----->123456.csv")

        mock_prompt_integer.return_value = 456
        self.assertEqual(fetch_filename(123, "Doesnt really matter"), "123456.csv")

        mock_prompt_integer.return_value = 1
        self.assertEqual(fetch_filename(True, "Doesnt really matter"), "True1.csv")
    

    @patch('manage_csv.read_input_csv.fetch_filename')
    def test_read_input(self, mock_fetch_filename):
        mock_fetch_filename.return_value = "files_Option2\csv_inputs\inputBoxes1.csv"
        self.assertNotEqual(read_input("files_Option2\csv_inputs\inputBoxes", 2), None)

        mock_fetch_filename.return_value = "files_Option1\csv_inputs\inputBins1.csv"
        self.assertNotEqual(read_input("files_Option1\csv_inputs\inputBins", 1), None)

        mock_fetch_filename.return_value = "files_Option2\csv_inputs\inputBins10.csv"
        self.assertEqual(read_input("files_Option2\csv_inputs\inputBins", 1), None)

    # manage_filecount.py
    def test_update_filecount(self):

        def retstr(filename):
            with open(filename, mode = 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    return row

        update_filecount(FILE_BINCOUNT_1 , 4)
        self.assertEqual(retstr(FILE_BINCOUNT_1), ['5'])

        update_filecount(FILE_BOXCOUNT_1 , 7)
        self.assertEqual(retstr(FILE_BOXCOUNT_1), ['8'])

    @patch('manage_csv.manage_filecount.prompt_integer')
    def test_fix_filecount(self, mock_prompt_integer):
        def retstr(filename):
            with open(filename, mode = 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    return row

        mock_prompt_integer.return_value = 4
        fix_filecount(FILE_BINCOUNT_1 , PROMPT_LASTFILE_BIN)
        self.assertEqual(retstr(FILE_BINCOUNT_1), ['4'])

        mock_prompt_integer.return_value = 7
        fix_filecount(FILE_BOXCOUNT_1 , PROMPT_LASTFILE_BOX)
        self.assertEqual(retstr(FILE_BOXCOUNT_1), ['7'])

    def test_fetch_filecount(self):
        self.assertEqual(fetch_filecount(FILE_BINCOUNT_1, 1), 2)
        self.assertEqual(fetch_filecount(FILE_BOXCOUNT_2, 2), 1)

if __name__ == '__main__':
    try:
        shutil.rmtree('files_Option1')
        shutil.rmtree('files_Option2')
    except OSError as e:
        pass
    unittest.main()