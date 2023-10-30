from manage_csv import InputBinParameters, InputBoxParameters, prompt_range, prompt_number, prompt_boolean, prompt_integer
from manage_csv import write_input_bin_func, prompt_input_bins
from manage_csv import write_input_box_func, prompt_input_boxes
from manage_csv import FILE_BIN_1, FILE_BIN_2, FILE_BOX_1, FILE_BOX_2, FILE_BINCOUNT_1, FILE_BINCOUNT_2, FILE_BOXCOUNT_1, FILE_BOXCOUNT_2
from manage_csv import FILE_FITTED_1, HEADER_OUT_1, FILE_LASTBIN, FILE_LASTBOX
from manage_csv import fetch_filename
from manage_csv import update_filecount, fetch_filecount
from manage_csv import update_lastfile, fetch_lastfile, read_input, write_output_func
from Option1_package import Item, Bin, Packer
from Option2_package import Item as ItemO2, Bin as BinO2, Packer as PackerO2
from manage_csv import Mode
from write_output_option1 import extract_boxes as extract_boxes_O1, extract_summary as extract_summary_O1, output_master as output_master_O1
from write_output_option2 import extract_boxes as extract_boxes_O2, extract_summary as extract_summary_O2, output_master as output_master_O2
from decimal import Decimal
from unittest.mock import patch
import shutil
import unittest
import csv
import os

"""
Unit tests covering all python files in manage_csv folder, as well as write_output_option1.py and write_output_option2.py
"""

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
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\csv_bins\inputBins1.csv'), True)

        mock_prompt_input_bins.return_value = InputBinParameters(4, 100, 200, 500, 10000)
        mock_fetch_filecount.return_value = 1
        write_input_bin_func(1)
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\csv_bins\inputBins2.csv'), True)
        
        # b_inputs not null, UI flag is true
        b_inputs = InputBinParameters(4, 100, 200, 500, 10000)
        mock_fetch_filecount.return_value = 2
        write_input_bin_func(1, b_inputs, True)
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\csv_bins\inputBins3.csv'), True)

        mock_prompt_input_bins.return_value = InputBinParameters(4, 100, 200, 500, 10000)
        mock_fetch_filecount.return_value = 0
        write_input_bin_func(2)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\csv_bins\inputBins1.csv'), True)
        
        # b_inputs not null, ui flag is true
        b_inputs = InputBinParameters(4, 100, 200, 500, 10000)
        mock_fetch_filecount.return_value = 1
        write_input_bin_func(2, b_inputs, True)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\csv_bins\inputBins2.csv'), True)
        
        # Invalid Option
        mock_fetch_filecount.return_value = 0
        write_input_bin_func(3)
        self.assertEqual(os.path.exists('files_Option3\csv_inputs\csv_bins\inputBins1.csv'), False)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\csv_bins\inputBins3.csv'), False)
        
        # Invalid b_inputs data type
        b_inputs = "Hello World"
        mock_fetch_filecount.return_value = 2
        with self.assertRaises(AttributeError):
            write_input_bin_func(2, b_inputs, ui_flag=True)
                 
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
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\csv_boxes\inputBoxes1.csv'), True)

        mock_prompt_input_boxes.return_value = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 1
        write_input_box_func(1)
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\csv_boxes\inputBoxes2.csv'), True)
        
        # b_inputs not null, ui flag is true
        b_inputs = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 2
        write_input_box_func(1, b_inputs, True)
        self.assertEqual(os.path.exists('files_Option1\csv_inputs\csv_boxes\inputBoxes3.csv'), True)

        mock_prompt_input_boxes.return_value = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 0
        write_input_box_func(2)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\csv_boxes\inputBoxes1.csv'), True)
        
        # b_inputs not null, ui flag is true
        b_inputs = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 1
        write_input_box_func(2, b_inputs, True)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\csv_boxes\inputBoxes2.csv'), True)

        # Invalid Option
        mock_prompt_input_boxes.return_value = InputBoxParameters(3, 1, 10, 100, 1000, 50, 300)
        mock_fetch_filecount.return_value = 0
        write_input_box_func(3)
        self.assertEqual(os.path.exists('files_Option3\csv_inputs\csv_boxes\inputBoxes1.csv'), False)
        self.assertEqual(os.path.exists('files_Option2\csv_inputs\csv_boxes\inputBoxes3.csv'), False)
        
        # Invalid b_inputs data type
        b_inputs = "Hello World"
        mock_fetch_filecount.return_value = 2
        with self.assertRaises(AttributeError):
            write_input_box_func(2, b_inputs, True)

class Test_Read_Input_CSV(unittest.TestCase):
    
    @patch('manage_csv.read_input_csv.prompt_integer')
    def test_fetch_filename(self, mock_prompt_integer):

        mock_prompt_integer.return_value = 1
        self.assertEqual(fetch_filename(FILE_BIN_1, 1), "files_Option1\csv_inputs\csv_bins\inputBins1.csv")

        mock_prompt_integer.return_value = 2
        self.assertEqual(fetch_filename(FILE_BIN_2, 1), "files_Option2\csv_inputs\csv_bins\inputBins2.csv")

        mock_prompt_integer.return_value = 1
        self.assertEqual(fetch_filename(FILE_BOX_1, 2), "files_Option1\csv_inputs\csv_boxes\inputBoxes1.csv")

        mock_prompt_integer.return_value = 2
        self.assertEqual(fetch_filename(FILE_BOX_2, 2), "files_Option2\csv_inputs\csv_boxes\inputBoxes2.csv")

        mock_prompt_integer.return_value = 123456
        self.assertEqual(fetch_filename("My IQ ----->", "Doesnt really matter"), "My IQ ----->123456.csv")

        mock_prompt_integer.return_value = 456
        self.assertEqual(fetch_filename(123, "Doesnt really matter"), "123456.csv")

        mock_prompt_integer.return_value = 1
        self.assertEqual(fetch_filename(True, "Doesnt really matter"), "True1.csv")
    
    
    @patch('builtins.input')
    def test_read_input(self, mock_input):

        mock_input.return_value = "1"
        self.assertEqual(read_input(FILE_BIN_1, 1, 1), [['Bin_#1', '100', '200', '500', '10000'], ['Bin_#2', '100', '200', '500', '10000'], ['Bin_#3', '100', '200', '500', '10000'], ['Bin_#4', '100', '200', '500', '10000']])

        mock_input.return_value = "2"
        self.assertEqual(read_input(FILE_BIN_2, 1, 2), [['Bin_#1', '100', '200', '500', '10000'], ['Bin_#2', '100', '200', '500', '10000'], ['Bin_#3', '100', '200', '500', '10000'], ['Bin_#4', '100', '200', '500', '10000']])

        # Boxes are randomly generated, cant test for exact values so test if output files were created
        mock_input.return_value = "1"
        self.assertNotEqual(read_input(FILE_BOX_1, 2, 1), None)

        mock_input.return_value = "2"
        self.assertNotEqual(read_input(FILE_BOX_2, 2, 2), None)
        
        mock_input.return_value = "200"
        self.assertEqual(read_input(FILE_BOX_2, 2, 2), None)

class Test_Manage_Last_File(unittest.TestCase):

    def test_update_lastfile(self):
        res = ""
        update_lastfile(FILE_LASTBIN, 2, 1)
        with open("files_Option2\csv_outputs\lastBinFile.txt", mode = 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                res = row
        self.assertEqual(res, ['lastBinFile.txt'])

        update_lastfile(FILE_LASTBOX, 1, 2)
        with open("files_Option1\csv_outputs\lastBoxFile.txt", mode = 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                res = row
        self.assertEqual(res, ['lastBoxFile.txt'])

        update_lastfile("I am not at all stressed", 1, 1)
        with open("files_Option1\csv_outputs\lastBinFile.txt", mode = 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                res = row
        self.assertEqual(res, ["I am not at all stressed"])

    def test_fetch_lastfile(self):
        update_lastfile(FILE_BIN_2, 2, 1)
        self.assertEqual(fetch_lastfile(2, 1), "files_Option2\csv_inputs\csv_bins\inputBins")

        update_lastfile(FILE_BOX_1, 1, 2)
        self.assertEqual(fetch_lastfile(1, 2), "files_Option1\csv_inputs\csv_boxes\inputBoxes")

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

class Test_Write_Output(unittest.TestCase):

    def test_write_output_func(self):
        rows = [
            ["Hello"],
            ["World"]
        ]
        write_output_func(FILE_FITTED_1, 30, HEADER_OUT_1, rows)
        path = FILE_FITTED_1 + "30.csv"
        self.assertTrue(os.path.exists(path))

class Test_Output_Option1(unittest.TestCase):

    def test_extract_boxes(self):

        # all items fitted
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")
        testbin = Bin(1, [100,200,100], 5000)
        testPacker = Packer()
        testPacker.addBin(testbin)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.pack(True, True, True, True, 0.75)

        expected_answer = [[1, 'test', 'orange', Decimal('10'), Decimal('20'), Decimal('30'), 6000.0, 25.0, [Decimal('0'), Decimal('0'), Decimal('0')], 0], [2, 'test', 'orange', Decimal('5'), Decimal('10'), Decimal('10'), 500.0, 25.0, [Decimal('10'), Decimal('0'), Decimal('0')], 0]]
        self.assertEqual(extract_boxes_O1(testPacker, Mode.FITTED.value), expected_answer)

        self.assertEqual(extract_boxes_O1(testPacker, Mode.UNFITTED.value), [])

        # all items unfitted
        testItem1 = Item(1,"test","cube", [520,520,530], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [350,530,510], 25, 2, 400, False, "orange")
        testbin = Bin(1, [200,100,300], 5000)
        testPacker = Packer()
        testPacker.addBin(testbin)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.pack(True, True, True, True, 0.75)

        self.assertEqual(extract_boxes_O1(testPacker, Mode.FITTED.value), [])

        expected_answer = [[1, 'test', 'orange', Decimal('520'), Decimal('520'), Decimal('530'), 143312000.0, 25.0, [0, 0, 0], 1], [2, 'test', 'orange', Decimal('350'), Decimal('530'), Decimal('510'), 94605000.0, 25.0, [0, 0, 0], 1]]
        self.assertEqual(extract_boxes_O1(testPacker, Mode.UNFITTED.value), expected_answer)

        # 1 item fitted 1 item unfitted
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [500,100,100], 25, 2, 400, False, "orange")
        testbin = Bin(1, [100,200,100], 5000)
        testPacker = Packer()
        testPacker.addBin(testbin)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.pack(True, True, True, True, 0.75)

        expected_answer = [[1, 'test', 'orange', Decimal('10'), Decimal('20'), Decimal('30'), 6000.0, 25.0, [Decimal('0'), Decimal('0'), Decimal('0')], 0]]
        self.assertEqual(extract_boxes_O1(testPacker, Mode.FITTED.value), expected_answer)

        expected_answer = [[2, 'test', 'orange', Decimal('500'), Decimal('100'), Decimal('100'), 5000000.0, 25.0, [0, 0, 0], 1]]
        self.assertEqual(extract_boxes_O1(testPacker, Mode.UNFITTED.value), expected_answer)

    def test_extract_summary(self):
        # all items fitted
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")
        testbin = Bin(1, [100,200,100], 5000)
        testPacker = Packer()
        testPacker.addBin(testbin)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.pack(True, True, True, True, 0.75)

        bins, sum = extract_summary_O1(testPacker)

        bins_exp = [[1, Decimal('2000000'), 500.0, 1999500.0, 0.03, []]]
        summ_exp = [['I am not at all stressed', 'lastBoxFile.txt', Decimal('2000000'), 6500.0, 1993500.0, 0.33, 0]]

        self.assertEqual(bins, bins_exp)
        self.assertEqual(sum, summ_exp)

    def test_output_master(self):
        # No existing files
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")
        testbin = Bin(1, [100,200,100], 5000)
        testPacker = Packer()
        testPacker.addBin(testbin)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.pack(True, True, True, True, 0.75)
        output_master_O1(testPacker)
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputBins1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputFitted1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputSummary1.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputUnfitted1.csv"))

        # With existing files
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")
        testbin = Bin(1, [100,200,100], 5000)
        testPacker = Packer()
        testPacker.addBin(testbin)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.pack(True, True, True, True, 0.75)

        output_master_O1(testPacker)
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputBins2.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputFitted2.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputSummary2.csv"))
        self.assertTrue(os.path.exists("files_Option1\csv_outputs\outputUnfitted2.csv"))

class Test_Output_Option2(unittest.TestCase):

    """
    Currently there is a bug with this part of O2 output
    """
    def test_extract_boxes(self):

        # all items fitted
        testItem1 = ItemO2("test1", 10, 20, 30, 25)
        testItem2 = ItemO2("test2", 20, 10, 10, 25)
        testbin = BinO2(300, 100, 200, 100, 5000)
        testPacker = PackerO2()
        testPacker.add_bin(testbin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)
        testPacker.pack()


        expected_answer = [['test1', Decimal('10.000'), Decimal('30.000'), Decimal('20.000'), Decimal('25.000'), Decimal('6000.000'), [0, 0, 0], 1]]
        self.assertEqual(extract_boxes_O2(testPacker, Mode.FITTED.value), expected_answer)

        exp_answer = [['test2', Decimal('20.000'), Decimal('10.000'), Decimal('10.000'), Decimal('25.000'), Decimal('2000.000'), [0, 0, 0], 0]]
        self.assertEqual(extract_boxes_O2(testPacker, Mode.UNFITTED.value), exp_answer)

        # all items unfitted
        testItem1 = ItemO2("test1", 1000, 2000, 3000, 25)
        testItem2 = ItemO2("test2", 2000, 1000, 1000, 25)
        testbin = BinO2(300, 100, 200, 100, 5000)
        testPacker = PackerO2()
        testPacker.add_bin(testbin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)
        testPacker.pack()

        self.assertEqual(extract_boxes_O2(testPacker, Mode.FITTED.value), [])

        expected_answer = [['test1', Decimal('1000.000'), Decimal('3000.000'), Decimal('2000.000'), Decimal('25.000'), Decimal('6000000000.000'), [0, 0, 0], 5], ['test2', Decimal('2000.000'), Decimal('1000.000'), Decimal('1000.000'), Decimal('25.000'), Decimal('2000000000.000'), [0, 0, 0], 5]]
        
        self.assertEqual(extract_boxes_O2(testPacker, Mode.UNFITTED.value), expected_answer)

        # 1 item fitted 1 item unfitted
        testItem1 = ItemO2("test1", 10, 20, 30, 25)
        testItem2 = ItemO2("test2", 2000, 1000, 1000, 25)
        testbin = BinO2(300, 100, 200, 100, 5000)
        testPacker = PackerO2()
        testPacker.add_bin(testbin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)
        testPacker.pack()

        

        expected_answer = [['test1', Decimal('10.000'), Decimal('30.000'), Decimal('20.000'), Decimal('25.000'), Decimal('6000.000'), [0, 0, 0], 1]]
        self.assertEqual(extract_boxes_O2(testPacker, Mode.FITTED.value), expected_answer)

        expected_answer = [['test2', Decimal('2000.000'), Decimal('1000.000'), Decimal('1000.000'), Decimal('25.000'), Decimal('2000000000.000'), [0, 0, 0], 5]]
        self.assertEqual(extract_boxes_O2(testPacker, Mode.UNFITTED.value), expected_answer)

    def test_extract_summary(self):
        
        testItem1 = ItemO2("test1", 10, 20, 30, 25)
        testItem2 = ItemO2("test2", 20, 10, 10, 25)
        testbin = BinO2(300, 100, 200, 100, 5000)
        testPacker = PackerO2()
        testPacker.add_bin(testbin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)
        testPacker.pack()

        bins, sum = extract_summary_O2(testPacker)

        bins_exp = [[300, Decimal('2000000.000'), Decimal('6000.000'), Decimal('1994000.000'), Decimal('0.30')]]
        summ_exp = [['lastBinFile.txt', 'files_Option2\\csv_inputs\\csv_boxes\\inputBoxes200.csv', Decimal('2000000.000'), Decimal('6000.000'), Decimal('1994000.000'), Decimal('0.30'), Decimal('2000.000')]]

        self.assertEqual(bins, bins_exp)
        self.assertEqual(sum, summ_exp)

    def test_output_master(self):
        # No existing files
        testItem1 = ItemO2("test1", 10, 20, 30, 25)
        testItem2 = ItemO2("test2", 20, 10, 10, 25)
        testbin = BinO2(300, 100, 200, 100, 5000)
        testPacker = PackerO2()
        testPacker.add_bin(testbin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)
        testPacker.pack()
        output_master_O2(testPacker)
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputBins1.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputFitted1.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputSummary1.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputUnfitted1.csv"))

        # With existing files
        testItem1 = ItemO2("test1", 10, 20, 30, 25)
        testItem2 = ItemO2("test2", 20, 10, 10, 25)
        testbin = BinO2(300, 100, 200, 100, 5000)
        testPacker = PackerO2()
        testPacker.add_bin(testbin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)
        testPacker.pack()
        output_master_O2(testPacker)
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputBins2.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputFitted2.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputSummary2.csv"))
        self.assertTrue(os.path.exists("files_Option2\csv_outputs\outputUnfitted2.csv"))


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
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Write_Output))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Output_Option1))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Output_Option2))

    runner = unittest.TextTestRunner()
    runner.run(suite)