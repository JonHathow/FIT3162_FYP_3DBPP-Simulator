from manage_csv import InputBinParameters, InputBoxParameters, prompt_range, prompt_number, prompt_boolean, prompt_integer
from manage_csv import write_input_bin_func, prompt_input_bins
from manage_csv import write_input_box_func, prompt_input_boxes
from manage_csv import FILE_BIN_1, FILE_BIN_2, FILE_BOX_1, FILE_BOX_2, FILE_BINCOUNT_1, FILE_BINCOUNT_2, FILE_BOXCOUNT_1, FILE_BOXCOUNT_2
from manage_csv import fetch_filename
from manage_csv import update_filecount, fetch_filecount
from manage_csv import update_lastfile, fetch_lastfile, read_input
from unittest.mock import patch
import shutil
import unittest
import csv
import os

class Test_Input_Parameters(unittest.TestCase):

    def test_inputParameters_Bin_Constructor(self):
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

    def test_inputParameters_Bin_String(self):
        testClass1 = InputBinParameters(4, 100, 200, 500, 10000)
        self.assertEqual(testClass1.__str__(),  "\nqty: 4\nwidth: 100\nheight: 200\ndepth: 500\ncapacity: 10000\n")

        testClass2 = InputBinParameters("4", False, 200.24, InputBinParameters(0,0,0,0,0), 20000)
        self.assertEqual(testClass2.__str__(),  "\nqty: 4\nwidth: False\nheight: 200.24\ndepth: \nqty: 0\nwidth: 0\nheight: 0\ndepth: 0\ncapacity: 0\n\ncapacity: 20000\n")

    def test_inputParameters_Box_Constructor(self):
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

    def test_inputParameters_Box_set_option1_params(self):
        testClass1 = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        testClass1.set_option1_params(True, True, True)
        self.assertEqual(testClass1.level_var, True)
        self.assertEqual(testClass1.updown_var, True)
        self.assertEqual(testClass1.updown, True)

        # Invalid Data types
        testClass1.set_option1_params("True", 1, (1.1, 20.45))
        self.assertEqual(testClass1.level_var, "True")
        self.assertEqual(testClass1.updown_var, 1)
        self.assertEqual(testClass1.updown, (1.1, 20.45))

    def test_inputParameters_Box_String(self):
        testClass1 = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        self.assertEqual(testClass1.__str__(),"\ntypes: 3\nqty_lo: 1, qty_hi: 10\ndim_lo: 100, dim_hi: 1000\nwgt_lo: 50, wgt_hi: 300\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n")

        testClass2 = InputBoxParameters("3", False, 'c', 46.78, InputBoxParameters(0, 0, 0, 0, 0, 0, 0), 50, 300)
        self.assertEqual(testClass2.__str__(),"\ntypes: 3\nqty_lo: False, qty_hi: c\ndim_lo: 46.78, dim_hi: \ntypes: 0\nqty_lo: 0, qty_hi: 0\ndim_lo: 0, dim_hi: 0\nwgt_lo: 0, wgt_hi: 0\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n\nwgt_lo: 50, wgt_hi: 300\nlevel_var: False\nloadbear_var: False\nupdown_var: False\nupdown: False\n")

class Test_Prompts(unittest.TestCase):

    @patch('builtins.input')
    def test_prompt_Number(self, mock_get_input):

        # input always return string

        mock_get_input.return_value = "4"
        self.assertEqual(prompt_number("dimension"), float(4))

        mock_get_input.return_value = "4.56"
        self.assertEqual(prompt_number("dimension"), float(4.56))

        mock_get_input.return_value = "-45"
        self.assertEqual(prompt_number("dimension"), float(45))

        mock_get_input.side_effect = ["Four", "11"]
        self.assertEqual(prompt_number("dimension"), float(11))

        mock_get_input.side_effect = ["True", "22"]
        self.assertEqual(prompt_number("dimension"), float(22))

        mock_get_input.side_effect = ["[42]", "-11.2"]
        self.assertEqual(prompt_number("dimension"), float(11.2))

    @patch('builtins.input')
    def test_prompt_Integer(self, mock_get_input):

        # input always return string

        mock_get_input.return_value = "4"
        self.assertEqual(prompt_integer("dimension"), 4)

        mock_get_input.return_value = "-45"
        self.assertEqual(prompt_integer("dimension"), 45)

        mock_get_input.side_effect = ["4.56", "4"]
        self.assertEqual(prompt_integer("dimension"), 4)

        mock_get_input.side_effect = ["Four", "-56"]
        self.assertEqual(prompt_integer("dimension"), 56)

        mock_get_input.side_effect = ["True", "32"]
        self.assertEqual(prompt_integer("dimension"), 32)

        mock_get_input.side_effect = ["[42]", "2"]
        self.assertEqual(prompt_integer("dimension"), 2)

    @patch('builtins.input')
    def test_prompt_Range(self, mock_get_input1):

        mock_get_input1.side_effect = ["1", "10"]
        self.assertEqual(prompt_range("containers needed"), (1,10))

        mock_get_input1.side_effect = ["-5", "10"]
        self.assertEqual(prompt_range("containers needed"), (5,10))

        mock_get_input1.side_effect = ["1", "-10"]
        self.assertEqual(prompt_range("containers needed"), (1,10))

        mock_get_input1.side_effect = ["-10", "-5"]
        self.assertEqual(prompt_range("containers needed"), (10,5))

        mock_get_input1.side_effect = ["1.5", "10.9", "1", "10"]
        self.assertEqual(prompt_range("containers needed"), (1,10))

        mock_get_input1.side_effect = ["Yes", "No", "1", "10"]
        self.assertEqual(prompt_range("containers needed"), (1,10))

    @patch('builtins.input')
    def test_prompt_Boolean(self, mock_get_input):

        mock_get_input.return_value = "y"
        self.assertEqual(prompt_boolean("to pass fit3162"), True)

        mock_get_input.return_value = "Y"
        self.assertEqual(prompt_boolean("to pass fit3162"), True)

        mock_get_input.return_value = "n"
        self.assertEqual(prompt_boolean("to pass fit3162"), False)

        mock_get_input.return_value = "N"
        self.assertEqual(prompt_boolean("to pass fit3162"), False)

        mock_get_input.side_effect = ["yes", "n"]
        self.assertEqual(prompt_boolean("to pass fit3162"), False)

        mock_get_input.side_effect = ["24", "y"]
        self.assertEqual(prompt_boolean("to pass fit3162"), True)

class Test_Write_Input_Bin(unittest.TestCase):

    @patch('builtins.input')
    def test_promptIBin(self, mock_input):

        mock_input.side_effect = [4, 100, 200, 500, 10000]

        testBin = prompt_input_bins()
        self.assertEqual(testBin.qty, 4)
        self.assertEqual(testBin.width, 100)
        self.assertEqual(testBin.height, 200)
        self.assertEqual(testBin.depth, 500)
        self.assertEqual(testBin.capacity, 10000)

    @patch('manage_csv.write_input_bin.fetch_filecount')
    @patch('manage_csv.write_input_bin.prompt_input_bins')
    def test_writeIBin(self, mock_prompt_input_bins, mock_fetch_filecount):
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

class Test_Write_Input_Box(unittest.TestCase):

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

class Test_Read_Input_CSV(unittest.TestCase):
    
    @patch('manage_csv.read_input_csv.prompt_integer')
    def test_fetch_filename(self, mock_prompt_integer):

        mock_prompt_integer.return_value = 1
        self.assertEqual(fetch_filename(FILE_BIN_1, 1), "files_Option1\csv_inputs\inputBins1.csv")

        mock_prompt_integer.return_value = 2
        self.assertEqual(fetch_filename(FILE_BIN_2, 1), "files_Option2\csv_inputs\inputBins2.csv")

        mock_prompt_integer.return_value = 1
        self.assertEqual(fetch_filename(FILE_BOX_1, 2), "files_Option1\csv_inputs\inputBoxes1.csv")

        mock_prompt_integer.return_value = 2
        self.assertEqual(fetch_filename(FILE_BOX_2, 2), "files_Option2\csv_inputs\inputBoxes2.csv")

        mock_prompt_integer.return_value = 123456
        self.assertEqual(fetch_filename("My IQ ----->", "Doesnt really matter"), "My IQ ----->123456.csv")

        mock_prompt_integer.return_value = 456
        self.assertEqual(fetch_filename(123, "Doesnt really matter"), "123456.csv")

        mock_prompt_integer.return_value = 1
        self.assertEqual(fetch_filename(True, "Doesnt really matter"), "True1.csv")
    

    """
    Needs to be fixed
    """
    @patch('builtins.input')
    def test_read_input(self, mock_input):

        mock_input.return_value = "1"
        self.assertNotEqual(read_input(FILE_BIN_1, 1, 1), None)

        mock_input.return_value = "2"
        self.assertEqual(read_input(FILE_BIN_2, 1, 2), None)

        mock_input.return_value = "1"
        self.assertNotEqual(read_input(FILE_BOX_1, 2, 1), None)

        mock_input.return_value = "2"
        self.assertEqual(read_input(FILE_BOX_2, 2, 2), None)

class Test_Manage_Last_File(unittest.TestCase):

    def test_update_lastfile(self):
        res = ""
        update_lastfile(FILE_BIN_2, 1, 1)
        with open("files_Option1\csv_outputs\lastBinFile.txt", mode = 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                res = row
        self.assertEqual(res, ["files_Option2\csv_inputs\inputBins"])

        update_lastfile(FILE_BOX_1, 1, 1)
        with open("files_Option1\csv_outputs\lastBinFile.txt", mode = 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                res = row
        self.assertEqual(res, ["files_Option1\csv_inputs\inputBoxes"])

        update_lastfile("I am not at all stressed", 1, 1)
        with open("files_Option1\csv_outputs\lastBinFile.txt", mode = 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                res = row
        self.assertEqual(res, ["I am not at all stressed"])

    def test_fetch_lastfile(self):
        update_lastfile(FILE_BIN_2, 1, 1)
        self.assertEqual(fetch_lastfile(1, 1), "files_Option2\csv_inputs\inputBins")

        update_lastfile(FILE_BOX_1, 1, 1)
        self.assertEqual(fetch_lastfile(1, 1), "files_Option1\csv_inputs\inputBoxes")

        update_lastfile("I am not at all stressed", 1, 1)
        self.assertEqual(fetch_lastfile(1, 1), "I am not at all stressed")

class Test_Manage_Filecount1(unittest.TestCase):

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

        update_filecount(FILE_BINCOUNT_2 , 5)
        self.assertEqual(retstr(FILE_BINCOUNT_2), ['6'])

        update_filecount(FILE_BOXCOUNT_2 , 8)
        self.assertEqual(retstr(FILE_BOXCOUNT_2), ['9'])

class Test_Manage_Filecount2(unittest.TestCase):

    def test_fetch_filecount(self):
        self.assertEqual(fetch_filecount(FILE_BINCOUNT_1), 5)
        self.assertEqual(fetch_filecount(FILE_BOXCOUNT_1), 8)
        self.assertEqual(fetch_filecount(FILE_BINCOUNT_2), 6)
        self.assertEqual(fetch_filecount(FILE_BOXCOUNT_2), 9)
    
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
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Input_Parameters))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Prompts))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Write_Input_Bin))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Write_Input_Box))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Read_Input_CSV))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Manage_Last_File))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Manage_Filecount1))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Manage_Filecount2))

    runner = unittest.TextTestRunner()
    runner.run(suite)