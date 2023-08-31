from manage_input_csv import InputBinParameters, InputBoxParameters
import unittest

class TestAux(unittest.TestCase):
    
    # tests for input_parameters.py
    def test_inputBinParametersConstructor(self):
        testClass1 = InputBinParameters(4, 100, 200, 500, 10000)
        self.assertEqual(testClass1.qty, 4)
        self.assertEqual(testClass1.width, 100)
        self.assertEqual(testClass1.height, 200)
        self.assertEqual(testClass1.depth, 500)
        self.assertEqual(testClass1.max_weight, 10000)

        testClass2 = InputBinParameters("4", False, 200.24, InputBinParameters(0,0,0,0,0), 20000)
        self.assertEqual(testClass2.qty, "4")
        self.assertEqual(testClass2.width, False)
        self.assertEqual(testClass2.height, 200.24)
        self.assertEqual(testClass2.depth.__str__(), "\nwidth: 0\nheight: 0\ndepth: 0\nmax_weight: 0\n")
        self.assertEqual(testClass2.max_weight, 20000)

    # tests for prompts.py
    def test_inputBinParametersString(self):
        testClass1 = InputBinParameters(4, 100, 200, 500, 10000)
        self.assertEqual(testClass1.__str__(),  "\nwidth: 100\nheight: 200\ndepth: 500\nmax_weight: 10000\n")

        testClass2 = InputBinParameters("4", False, 200.24, InputBinParameters(0,0,0,0,0), 20000)
        self.assertEqual(testClass2.__str__(),  "\nwidth: False\nheight: 200.24\ndepth: \nwidth: 0\nheight: 0\ndepth: 0\nmax_weight: 0\n\nmax_weight: 20000\n")

    # tests for read_input_csv.py
    def test_pack2Bin(self):
        pass

    # tests for write_input_csv.py
    def test_pack2Bin(self):
        pass

    # tests for manage_input.py
    def test_pack2Bin(self):
        pass


if __name__ == '__main__':
    unittest.main()