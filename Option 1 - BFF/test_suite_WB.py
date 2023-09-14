#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import rectIntersect, intersect, getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer, Axis
from decimal import Decimal
import decimal
import unittest
import numpy as np

"""
White Box Testing
"""

                                        #                #
                                        # Positive Cases #
                                        #                #
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

class TestAux(unittest.TestCase):
    
    #                     #
    #  Auxiliary Methods  #
    #                     #
    
    def test_rectIntersect(self):
        """
        Conditional Testing:-
        2 conditions:
        'ix < (d1[x]+d2[x])/2' 
        'iy < (d1[y]+d2[y])/2'

        """
        #                                  W  H  D
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")

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

        """
        100% path coverage
        """
 
    def test_intersect(self):
        """
        Conditional testing:-
        3 Conditions:
        rectIntersect(item1, item2, Axis.WIDTH, Axis.HEIGHT)
        rectIntersect(item1, item2, Axis.HEIGHT, Axis.DEPTH)
        rectIntersect(item1, item2, Axis.WIDTH, Axis.DEPTH)
        
        Not possible to get 2 True's and a False
        """
        #                                  W  H  D
        testItem1 = Item(1,"test","cube", [10,10,10], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [10,10,10], 25, 2, 400, False, "orange")
        
        """
        True
        True
        True
        """
        self.assertEqual(intersect(testItem1, testItem2), True)
        
        """
        True
        False
        False
        """
        testItem1.position = [0, 0, 15]
        self.assertEqual(intersect(testItem1, testItem2), False)
        
        """
        False
        True
        False
        """
        testItem1.position = [15, 0, 0]
        self.assertEqual(intersect(testItem1, testItem2), False)
        
        """
        False
        False
        True
        """
        testItem1.position = [0, 15, 0]
        self.assertEqual(intersect(testItem1, testItem2), False)
        
        """
        False
        False
        False
        """
        testItem1.position = [0, 15, 15]
        self.assertEqual(intersect(testItem1, testItem2), False)
 
    def test_getLimitNumberOfDecimals(self):
        """
        No conditionals, 1 line of code, 100% Path Coverage
        """
        # Positive number of decimals
        self.assertEqual(getLimitNumberOfDecimals(3), 1.000)

    def test_set2Decimal(self):
        """
        Only difference is if default variable value is used
        
        100% path coverage
        """
        # Float value with default number of decimals
        self.assertEqual(set2Decimal(9.4231), Decimal('9'))
        
        # Float value with a custom number of decimals
        self.assertEqual(set2Decimal(9.4231, 2), Decimal('9.42'))

    #                      #
    #  Item Class Methods  #
    #                      #

    def test_itemConstructor(self):
        """
        Conditional testing:-
        1 Condition:
        self.updown = updown if typeof == 'cube' else False
        
        100% Path coverage
        """

                                        #                #
                                        # Positive Cases #
                                        #                #
                                        
        # typeof == 'cube'
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.partno, 1)
        self.assertEqual(testItem.name, "test")
        self.assertEqual(testItem.typeof, "cube")
        self.assertEqual(testItem.width, 10)
        self.assertEqual(testItem.height, 20)
        self.assertEqual(testItem.depth, 30)
        self.assertEqual(testItem.weight, 25)
        self.assertEqual(testItem.level, 2)
        self.assertEqual(testItem.loadbear, 400)
        self.assertEqual(testItem.updown, True)
        self.assertEqual(testItem.color, "orange")
            # Attributes not affected by constructor
        self.assertEqual(testItem.rotation_type, 0)
        self.assertEqual(testItem.position, [0,0,0])
        self.assertEqual(testItem.number_of_decimals, 0)
        
        # typeof == 'apricot'
        testItem = Item(1,"test","apricot", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.partno, 1)
        self.assertEqual(testItem.name, "test")
        self.assertEqual(testItem.typeof, "apricot")
        self.assertEqual(testItem.width, 10)
        self.assertEqual(testItem.height, 20)
        self.assertEqual(testItem.depth, 30)
        self.assertEqual(testItem.weight, 25)
        self.assertEqual(testItem.level, 2)
        self.assertEqual(testItem.loadbear, 400)
        self.assertEqual(testItem.updown, False)
        self.assertEqual(testItem.color, "orange")
            # Attributes not affected by constructor
        self.assertEqual(testItem.rotation_type, 0)
        self.assertEqual(testItem.position, [0,0,0])
        self.assertEqual(testItem.number_of_decimals, 0)

    def test_itemFormatNumbers(self):
        """
        No conditionals
        
        100% Path coverage
        """
        # Integer number of decimals
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25., 2, 400, True, "orange")
        testItem.formatNumbers(3)
        self.assertEqual(testItem.width, Decimal('10.234'))
        self.assertEqual(testItem.height, Decimal('20.300'))
        self.assertEqual(testItem.depth, Decimal('30.000'))
        self.assertEqual(testItem.weight, Decimal('25.000'))
        self.assertEqual(testItem.number_of_decimals, 3)

    def test_itemString(self):
        """
        No conditionals
        
        100% Path coverage
        """
        # Valid Item construction
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.string(), "1(10.23423x20.3x30, weight: 25) pos([0, 0, 0]) rt(0) vol(6233)")

    def test_itemGetVolume(self):
        """
        No conditionals
        
        100% Patch coverage
        """
        # Valid Item Construction
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getVolume(), 6000)

    def test_itemGetMaxArea(self):
        """
        Conditional testing:-
        1 Condition:
        a = sorted([self.width,self.height,self.depth],reverse=True) if self.updown == True else [self.width,self.height,self.depth]
        
        100% path Coverage
        """
        # self.updown == True
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getMaxArea(), 600)
        
        # self.updown == False
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        self.assertEqual(testItem.getMaxArea(), 200)

    def test_itemGetDimension(self):
        """
        Conditional Testing:-
        7 Conditions:
        if self.rotation_type == RotationType.RT_WHD
        if self.rotation_type == RotationType.RT_HWD
        if self.rotation_type == RotationType.RT_HDW
        if self.rotation_type == RotationType.RT_DHW
        if self.rotation_type == RotationType.RT_DWH
        if self.rotation_type == RotationType.RT_WDH
        else
        
        100% Path Coverage
        """
        #if self.rotation_type == RotationType.RT_WHD
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 0
        self.assertEqual(testItem.getDimension(), [10,20,30])
        
        #if self.rotation_type == RotationType.RT_HWD
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 1
        self.assertEqual(testItem.getDimension(), [20,10,30])
        
        #if self.rotation_type == RotationType.RT_HDW
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 2
        self.assertEqual(testItem.getDimension(), [20,30,10])
        
        #if self.rotation_type == RotationType.RT_DHW
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 3
        self.assertEqual(testItem.getDimension(), [30,20,10])
        
        #if self.rotation_type == RotationType.RT_DWH
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 4
        self.assertEqual(testItem.getDimension(), [30,10,20])
        
        #if self.rotation_type == RotationType.RT_WDH
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 5
        self.assertEqual(testItem.getDimension(), [10,30,20])
        
        #else
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 6
        self.assertEqual(testItem.getDimension(), [])

    #                     #
    #  Bin Class Methods  #
    #                     #

    # BB Done
    def test_binConstructor(self):
        """
        Conditional testing:-
        No Conditions
        
        100% Path Coverage
        """

        # Using default values for corner and put_type
        testbin = Bin(1, [100,200,100], 5000)
        self.assertEqual(testbin.partno, 1)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.corner, 0)
        self.assertEqual(testbin.put_type, 1)
        self.assertEqual(testbin.fit_items.tolist(), [[0, 100, 0, 200, 0, 0]])
            # Attributes not affected by constructor
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 0)
        self.assertEqual(testbin.fix_point, False)
        self.assertEqual(testbin.check_stable, False)
        self.assertEqual(testbin.support_surface_ratio, 0)
        self.assertEqual(testbin.gravity, [])
        
        # Using custom values for corner and put_type
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        self.assertEqual(testbin.partno, 1)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.corner, 1)
        self.assertEqual(testbin.put_type, 0)
        self.assertEqual(testbin.fit_items.tolist(), [[0, 100, 0, 200, 0, 0]])
            # Attributes not affected by constructor
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 0)
        self.assertEqual(testbin.fix_point, False)
        self.assertEqual(testbin.check_stable, False)
        self.assertEqual(testbin.support_surface_ratio, 0)
        self.assertEqual(testbin.gravity, [])







if __name__ == '__main__':
    unittest.main()