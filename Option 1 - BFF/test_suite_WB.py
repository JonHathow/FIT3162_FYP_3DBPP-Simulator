#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import rectIntersect, intersect, getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer, Axis
from decimal import Decimal
import decimal
import unittest
import numpy as np

"""
_summary_
Test suite to test and validate all the functions in this open source code

Author: Anson Lee
"""
'''
Option 1 Dimensions
    WIDTH = 0
    HEIGHT = 1
    DEPTH = 2

Option 2 Dimensions
    LENGTH = 0
    WIDTH = 1
    HEIGHT = 2
'''

class TestAux(unittest.TestCase):
    
    # Auxiliary Methods
    def test_rectIntersect(self):
        """
        rectIntersect is a straightforward function with only 2 conditions to test:

        'ix < (d1[x]+d2[x])/2' 
        'iy < (d1[y]+d2[y])/2'

        """
        #                                  W  H  D
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")

                                    #                     #
                                    # Conditional Testing #
                                    #                     #

        """
        2.5 < 7.5 ; True
        5 < 15    ; True
        """
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        
        """
        2.5 < 7.5 ; True
        140 < 60  ; False
        """
        testItem2 = Item(2,"test","cube", [5,100,10], 25, 2, 400, False, "orange")
        testItem2.position = [0, 100, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)


        """
        145 < 55  ; False
        5 < 15    ; True
        """

        testItem2 = Item(2,"test","cube", [100,10,10], 25, 2, 400, False, "orange")
        testItem2.position = [100, 0, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)


        """
        145 < 55  ; False
        140 < 60  ; False
        """
        testItem2 = Item(2,"test","cube", [100,100,10], 25, 2, 400, False, "orange")
        testItem2.position = [100, 100, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
 
 

if __name__ == '__main__':
    unittest.main()