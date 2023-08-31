#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from manage_csv import InputBinParameters, InputBoxParameters
from decimal import Decimal
import unittest
import numpy as np

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

    # manage_filecount.py
    # need more time to research and implement tests for external files

    # prompts.py
    # need more time to research and implement tests for prompts

    # Option1_input tests
    def test_pack2Bin(self):
        pass

    # Option2_input tests
    def test_pack2Bin(self):
        pass


if __name__ == '__main__':
    unittest.main()