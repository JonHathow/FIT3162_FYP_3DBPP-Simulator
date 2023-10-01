from unittest.mock import patch
import shutil
import unittest

class Test_O1_Extract_Boxes(unittest.TestCase):

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

class Test_O1_Extract_Summary(unittest.TestCase):
    pass

class Test_O1_Output_Master(unittest.TestCase):
    pass


class Test_O2_Extract_Boxes(unittest.TestCase):
    pass

class Test_O2_Extract_Summary(unittest.TestCase):
    pass

class Test_O2_Output_Master(unittest.TestCase):
    pass




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
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O1_Extract_Boxes))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O1_Extract_Summary))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O1_Output_Master))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O2_Extract_Boxes))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O2_Extract_Summary))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_O2_Output_Master))

    runner = unittest.TextTestRunner()
    runner.run(suite)