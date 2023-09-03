#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from manage_csv import InputBinParameters, InputBoxParameters, prompt_range, prompt_number, prompt_boolean, prompt_integer, get_input, prompt_input_bins, write_input_bin_func
from manage_csv import Option, Mode, MENU_INPUT, MENU_INVALID, MENU_END, MENU_BIN_NOTLOADED, FILE_BIN_1, FILE_BOX_1
from unittest.mock import patch
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
    def test_writeIBin_promptIBin(self, mock_prompt_integer, mock_prompt_number):

        # func to return the string func of input_parameters
        def retstr(item):
            return item.__str__()

        mock_prompt_integer.return_value = 4
        mock_prompt_number.side_effect = [2, 3.5, 4, 5.66]
        self.assertEqual(retstr(prompt_input_bins()),"\nqty: 4\nwidth: 2\nheight: 3.5\ndepth: 4\ncapacity: 5.66\n")

        # func to return the string func of input_parameters
        def retstr(item):
            return item.__str__()

        # would never happen
        mock_prompt_integer.return_value = 4.5
        mock_prompt_number.side_effect = [2.8, "3.5", -4.5, "hello"]
        self.assertEqual(retstr(prompt_input_bins()),"\nqty: 4.5\nwidth: 2.8\nheight: 3.5\ndepth: -4.5\ncapacity: hello\n")

    @patch('manage_csv.write_input_bin.fetch_filecount')
    @patch('manage_csv.write_input_bin.prompt_input_bins')
    def test_writeIBin_writeIBinFunc(self, mock_prompt_input_bins, mock_fetch_filecount):
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
    def test_writeInputBox(self):
        return
    
    # read_input_csv.py
    def test_readcsv(self):
        return
    
    # manage_filecount.py

    

    # Option1_input tests
    def test_pack2Bin(self):
        pass

    # Option2_input tests
    def test_pack2Bin(self):
        pass


if __name__ == '__main__':
    unittest.main()