#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import rectIntersect, intersect, getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer, Axis, RotationType
from decimal import Decimal
import decimal
import unittest
import numpy as np

"""
Black  Box Testing for Option 1, Jerry's Algorithm
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

    # BB Done
    def test_rectIntersect(self):
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")


                                        #                #
                                        # Positive Cases #
                                        #                #



        # 2 Items that intersect on all planes
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), True)

        # 2 Items that intersect on D & H planes
        #                     W   H  D
        testItem2.position = [30, 0, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), False)

        # 2 Items that intersect on D & W planes
        #                     W  H   D
        testItem2.position = [0, 30, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), True)

        # 2 Items that intersect on W & H planes
        #                     W  H  D
        testItem2.position = [0, 0, 30]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), False)

        # One Item Inside Another
        testItem2.position = [2.5, 5, 10]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)


                                        #                #
                                        #   Edge Cases   #
                                        #                #


        # 2 Items barely do not intersect at the edges
        testItem2.position = [10, 20, 30]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), False)

        # 2 Items barely intersect at the edges
        testItem2.position = [9, 19, 29]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), True)


                                        #                #
                                        # Negative Cases #
                                        #                #


        # 2 Items that do not intersect
        testItem2.position = [50, 50, 50]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), False)

        # Zero-Dimensional Item
        testItem1 = Item(1, 'test', 'cube', (0, 0, 0), 0.0, 1, 50, False, 'silver')
        testItem2.position = [0, 0, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)


        # Invalid Item types
        with self.assertRaises(AttributeError):
            # only objects of item class have the position attribute
            rectIntersect(32, testItem2, Axis.WIDTH, Axis.HEIGHT)
            rectIntersect('a', testItem2, Axis.WIDTH, Axis.HEIGHT)
            rectIntersect(False, testItem2, Axis.WIDTH, Axis.HEIGHT)
            rectIntersect(testItem1, 32, Axis.WIDTH, Axis.HEIGHT)
            rectIntersect(testItem1, 'a', Axis.WIDTH, Axis.HEIGHT)
            rectIntersect(testItem1, False, Axis.WIDTH, Axis.HEIGHT)

        # Invalid Dimension Values
        with self.assertRaises(IndexError):
            # position array holds 3 values, x, y and z. Any index above 2 is out of range
            rectIntersect(testItem1, testItem2, 11, Axis.HEIGHT)
            rectIntersect(testItem1, testItem2, -11, Axis.HEIGHT)
            rectIntersect(testItem1, testItem2, Axis.WIDTH, 11)
            rectIntersect(testItem1, testItem2, Axis.WIDTH, -11)

        # Invalid Dimension Types
        with self.assertRaises(TypeError):
            rectIntersect(testItem1, testItem2, "hello", Axis.HEIGHT)
            rectIntersect(testItem1, testItem2, Axis.WIDTH, "hello")

    # BB Done
    def test_intersect(self):
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [20,10,10], 25, 2, 400, False, "orange")

                                        #                #
                                        # Positive Cases #
                                        #                #

        # All 3 planes intersecting
        self.assertEqual(intersect(testItem1, testItem2), True)

        # Changing position of item 2 for all dimensions
        #                     W   H   D
        testItem2.position = [9, 19, 29]
        self.assertEqual(intersect(testItem1, testItem2), True)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Item 2 barely intersects with Item 1
        testItem2.position = [9,19,29]   
        self.assertEqual(intersect(testItem1, testItem2), True)

        # Item 2 barely does not intersect with Item 1
        testItem2.position = [10,20,30] 
        self.assertEqual(intersect(testItem1, testItem2), False)
                         

                                        #                #
                                        # Negative Cases #
                                        #                #

        # Item 2 does not intersect with Item 1
        testItem2.position = [10, 20, 30]
        self.assertEqual(intersect(testItem1, testItem2), False)

        # Invalid item types
        with self.assertRaises(AttributeError):
            # only objects of item class have the position attribute
            intersect(32, testItem2)
            intersect('a', testItem2)
            intersect(False, testItem2)
            intersect(testItem1, 32)
            intersect(testItem1, 'a')
            intersect(testItem1, False)
        
    # BB Done
    def test_getLimitNumberOfDecimals(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Positive number of decimals
        self.assertEqual(getLimitNumberOfDecimals(3), 1.000)

        # Zero decimals
        self.assertEqual(getLimitNumberOfDecimals(0), 1)

        # Large number of decimals
        self.assertEqual(getLimitNumberOfDecimals(20), 1.00000000000000000000)

        # Negative number of decimals
        self.assertEqual(getLimitNumberOfDecimals(-5), 1)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #
                        
        # Invalid type for number of decimals
        with self.assertRaises(TypeError):
            getLimitNumberOfDecimals(1.0)
            getLimitNumberOfDecimals(2.4)
            getLimitNumberOfDecimals('a')
            getLimitNumberOfDecimals(False)

    # BB Done
    def test_set2Decimal(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Integer value with default number of decimals
        self.assertEqual(set2Decimal(10), Decimal('10'))

        # Float value with default number of decimals
        self.assertEqual(set2Decimal(3.14159), Decimal('3'))

        # Negative value with default number of decimals
        self.assertEqual(set2Decimal(-7), Decimal('-7'))

        # Integer value with custom number of decimals
        self.assertEqual(set2Decimal(4, 3), Decimal('4.000'))

        # Float value with custom number of decimals
        self.assertEqual(set2Decimal(2.71828, 4), Decimal('2.7183'))

        # Negative value with custom number of decimals
        self.assertEqual(set2Decimal(-7, 2), Decimal('-7.00'))

        # Integer value with a large custom number of decimals
        self.assertEqual(set2Decimal(4, 20), Decimal('4.00000000000000000000'))

        # Integer value with a negative custom number of decimals
        self.assertEqual(set2Decimal(4, -5), Decimal('4'))

        # False value with a custom number of decimals
        self.assertEqual(set2Decimal(False, 1), Decimal('0.0'))

        # String integer value with a custom number of decimals
        self.assertEqual(set2Decimal("4", 1), Decimal('4.0'))

        # String float value with a custom number of decimals
        self.assertEqual(set2Decimal("4.64", 3), Decimal('4.640'))
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid number of decimals type
        with self.assertRaises(TypeError):
            set2Decimal(4, 1.5)
            set2Decimal(4, 'a')

        # Invalid value type
        with self.assertRaises(decimal.InvalidOperation):
            self.assertEqual(set2Decimal("Hello", 1), Decimal('Hello'))


    #                      #
    #  Item Class Methods  #
    #                      #

    # BB Done
    def test_itemConstructor(self):

                                        #                #
                                        # Positive Cases #
                                        #                #
                                        
        # Cube Item
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

        # Cylinder Item
        testItem = Item(2, 'Cup', 'cylinder', (8, 8, 4), 0.3, 1, 50, False, 'blue')
        assert testItem.partno == 2
        assert testItem.name == 'Cup'
        assert testItem.typeof == 'cylinder'
        assert testItem.width == 8
        assert testItem.height == 8
        assert testItem.depth == 4
        assert testItem.weight == 0.3
        assert testItem.level == 1
        assert testItem.loadbear == 50
        assert testItem.updown == False
        assert testItem.color == 'blue'

        # Random input types
        testItem = Item("¯\_(ツ)_/¯", False, 'Hexagon', (8.5, -34, 4.55), '0.3', (1,2,4,8), True, 'Maybe', 'blue')
        assert testItem.partno == "¯\_(ツ)_/¯"
        assert testItem.name == False
        assert testItem.typeof == 'Hexagon'
        assert testItem.width == 8.5
        assert testItem.height == -34
        assert testItem.depth == 4.55
        assert testItem.weight == '0.3'
        assert testItem.level == (1,2,4,8)
        assert testItem.loadbear == True
        assert testItem.updown == False
        assert testItem.color == 'blue'

                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid item dimensions array length
        with self.assertRaises(IndexError):
            testItem = Item(1,"test","cube", (10,20), 25, 2, 400, True, "orange")

        # Invalid item dimensions type
        with self.assertRaises(TypeError):
            testItem = Item(1,"test","cube", 10, 25, 2, 400, True, "orange")
            testItem = Item(1,"test","cube", False, 25, 2, 400, True, "orange")
            testItem = Item(1,"test","cube", "(10, 20, 30)", 25, 2, 400, True, "orange")

    # BB Done
    def test_itemFormatNumbers(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Integer number of decimals
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25., 2, 400, True, "orange")
        testItem.formatNumbers(3)
        self.assertEqual(testItem.width, Decimal('10.234'))
        self.assertEqual(testItem.height, Decimal('20.300'))
        self.assertEqual(testItem.depth, Decimal('30.000'))
        self.assertEqual(testItem.weight, Decimal('25.000'))
        self.assertEqual(testItem.number_of_decimals, 3)

        # Negative Integer number of decimals
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25., 2, 400, True, "orange")
        testItem.formatNumbers(-2)
        self.assertEqual(testItem.width, Decimal('10'))
        self.assertEqual(testItem.height, Decimal('20'))
        self.assertEqual(testItem.depth, Decimal('30'))
        self.assertEqual(testItem.weight, Decimal('25'))
        self.assertEqual(testItem.number_of_decimals, -2)

        # Large number of decimals
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25., 2, 400, True, "orange")
        testItem.formatNumbers(10)
        self.assertEqual(testItem.width, Decimal('10.2342300000'))
        self.assertEqual(testItem.height, Decimal('20.3000000000'))
        self.assertEqual(testItem.depth, Decimal('30.0000000000'))
        self.assertEqual(testItem.weight, Decimal('25.0000000000'))
        self.assertEqual(testItem.number_of_decimals, 10)

                                        #                #
                                        #   Edge Cases   #
                                        #                #
                                        
        # Number of decimals is 0
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25., 2, 400, True, "orange")
        testItem.formatNumbers(0)
        self.assertEqual(testItem.width, Decimal('10'))
        self.assertEqual(testItem.height, Decimal('20'))
        self.assertEqual(testItem.depth, Decimal('30'))
        self.assertEqual(testItem.weight, Decimal('25'))
        self.assertEqual(testItem.number_of_decimals, 0)

                                        #                #
                                        # Negative Cases #
                                        #                #
       
       # Invalid type of number of decimals
        with self.assertRaises(TypeError):
            testItem.formatNumbers(2.3)
            testItem.formatNumbers('a')

    # BB Done
    def test_itemString(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Valid Item construction
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.string(), "1(10.23423x20.3x30, weight: 25) pos([0, 0, 0]) rt(0) vol(6233)")

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Item construction with random values and datatypes (except dimensions)
        testItem = Item("1",34 ,33, [10.23423,20.3,30], False, True, "400", 22, "orange")
        self.assertEqual(testItem.string(), "1(10.23423x20.3x30, weight: False) pos([0, 0, 0]) rt(0) vol(6233)")
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Item construction with invalid dimension data types
        testItem = Item(1,"test","cube", ["10.23423", False, (1,23)], 25, 2, 400, True, "orange")
        with self.assertRaises(TypeError):
            testItem.string()

    # BB Done
    def test_itemGetVolume(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Item Construction
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getVolume(), 6000)

        # Item Construction Random Data Types (except Dimensions)
        testItem = Item("1",34 ,33, [10,20,30], False, True, "400", 22, "orange")
        self.assertEqual(testItem.getVolume(), 6000)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Item Construction with 0 dimensions
        testItem = Item("1",34 ,33, [0, 0, 0], False, True, "400", 22, "orange")
        self.assertEqual(testItem.getVolume(), 0)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #
        # Invalid Dimension Types
        testItem = Item(1,"test","cube", ["10", True, 30], 25, 2, 400, True, "orange")
        with self.assertRaises(decimal.InvalidOperation):
            testItem.getVolume()

    # BB Done
    def test_itemGetMaxArea(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Item Construction
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getMaxArea(), 600)

        # Large Item Dimensions
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        self.assertEqual(testItem.getMaxArea(), 200)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Item Construction with 0 dimensions
        testItem = Item(1,"test","cube", [0, 0, 0], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getMaxArea(), 0)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid Dimensions Data Types
        with self.assertRaises(TypeError):
            testItem = Item(1,"test","cube", ["10", True, 30], 25, 2, 400, True, "orange")
            testItem.getMaxArea()
            testItem = Item(1,"test","cube", ["10", True, 30], 25, 2, 400, False, "orange")
            testItem.getMaxArea()

    # BB Done
    def test_itemGetDimension(self):

                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Item Construction
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getDimension(), [10,20,30])

        # Small Dimensions
        testItem = Item(1,"test","cube", [1,2,3], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getDimension(), [1,2,3])

        # Large Dimensions
        testItem = Item(1,"test","cube", [150,2000,3320], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getDimension(), [150,2000,3320])


                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Invalid Dimension Data Types
        testItem = Item(1,"test","cube", ["10",False,30.3], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getDimension(), ["10",False,30.3])

    #                     #
    #  Bin Class Methods  #
    #                     #

    # BB Done
    def test_binConstructor(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Bin Construction using default values
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
      
        # Valid Bin Construction not using default values
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

        # Random input types
        testbin = Bin(1, ["100",13.4,False], [2232,54], False, "true")
        self.assertEqual(testbin.partno, 1)
        self.assertEqual(testbin.width, "100")
        self.assertEqual(testbin.height, 13.4)
        self.assertEqual(testbin.depth, False)
        self.assertEqual(testbin.max_weight, [2232,54])
        self.assertEqual(testbin.corner, False)
        self.assertEqual(testbin.put_type, "true")
        self.assertEqual(testbin.fit_items.tolist(), [['0', "100", '0', '13.4', '0', '0']])
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid Dimensions Length
        with self.assertRaises(IndexError):
            testbin = Bin(1, [100,200], 4000, False, "true")

        # Invalid Dimensions type
        with self.assertRaises(TypeError):
            testbin = Bin(1, 100, 4000, False, "true")
            testbin = Bin(1, "100", 4000, False, "true")

    # BB Done
    def test_binFormatNumbers(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Integer number of decimals
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        testbin.formatNumbers(3)
        self.assertEqual(testbin.width, 100.000)
        self.assertEqual(testbin.height, 200.000)
        self.assertEqual(testbin.depth, 100.000)
        self.assertEqual(testbin.max_weight, 5000.000)
        self.assertEqual(testbin.number_of_decimals, 3)

        # Negative number of decimals
        testbin.formatNumbers(-1)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.number_of_decimals, -1)

        # Large number of decimals
        testbin.formatNumbers(10)
        self.assertEqual(testbin.width, 100.0000000000)
        self.assertEqual(testbin.height, 200.0000000000)
        self.assertEqual(testbin.depth, 100.0000000000)
        self.assertEqual(testbin.max_weight, 5000.0000000000)
        self.assertEqual(testbin.number_of_decimals, 10)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Number of decimals is 0                     
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        testbin.formatNumbers(0)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.number_of_decimals, 0)

                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid number of decimals data type
        with self.assertRaises(TypeError):
            testbin.formatNumbers("potato")
            testbin.formatNumbers(False)
            testbin.formatNumbers(13.2)

    # BB Done
    def test_binString(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Item Construction
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        self.assertEqual(testbin.string(), "1(100x200x100, max_weight:5000) vol(2000000)")

                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #

        testbin = Bin("454", [100,200,100], False, "1")
        self.assertEqual(testbin.string(), "454(100x200x100, max_weight:False) vol(2000000)")    

                                        #                #
                                        # Negative Cases #
                                        #                #

        # Item construction with invalid dimension data types
        testbin = Bin(1, ["100",False,(2,33)], 5000, 1, 0)
        with self.assertRaises(TypeError):
            testbin.string()

    # BB Done
    def test_binGetVolume(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Valid Bin Construction
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        self.assertEqual(testbin.getVolume(), 2000000)

        # Bin Construction Random Data Types (except Dimensions)
        testbin = Bin("1", [100,200,100], False, "1", (22,0))
        self.assertEqual(testbin.getVolume(), 2000000)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Bin Construction with 0 dimensions
        testbin = Bin("1", [0, 0, 0], False, "1", (22,0))
        self.assertEqual(testbin.getVolume(), 0)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid Dimension Types
        testbin = Bin(1, ["100",False,(100, 22)], 5000, 1, 0)
        with self.assertRaises(TypeError):
            self.assertEqual(testbin.getVolume(), 2000000.000)

    # BB Done
    def test_binGetTotalWeight(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # 3 Light Items
        testbin = Bin(1, [2000,2000,2000], 5000, 1, 0)
        testItem1 = Item(1,"test1","cube", [10,20,30], 10, 2, 400, True, "orange")
        testItem2 = Item(2,"test2","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem3 = Item(3,"test3","cube", [10,20,30], 11, 2, 400, True, "orange")
        testbin.putItem(testItem1, [0,0,0])
        testbin.putItem(testItem2, [50,50,50])
        testbin.putItem(testItem3, [100,100,100])
        self.assertEqual(testbin.getTotalWeight(), 46)

        # 3 Heavy Items
        testbin = Bin(1, [2000,2000,2000], 5000, 1, 0)
        testItem1 = Item(1,"test1","cube", [10,20,30], 1000, 2, 400, True, "orange")
        testItem2 = Item(2,"test2","cube", [10,20,30], 500, 2, 400, True, "orange")
        testItem3 = Item(3,"test3","cube", [10,20,30], 2500, 2, 400, True, "orange")
        testbin.putItem(testItem1, [0,0,0])
        testbin.putItem(testItem2, [50,50,50])
        testbin.putItem(testItem3, [100,100,100])
        self.assertEqual(testbin.getTotalWeight(), 4000)
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #
                                        
        # Empty Bin
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        self.assertEqual(testbin.getTotalWeight(), 0)

        # 1 Item
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testbin.putItem(testItem, [0,0,0])
        self.assertEqual(testbin.getTotalWeight(), 25)

    # BB Done
    def test_binPutItem(self):

                                        #                #
                                        # Positive Cases #
                                        #                #

        # Item Fits
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testbin.putItem(testItem, [0,0,0])
        self.assertEqual(len(testbin.items), 1)

        # Item fits only after rotation
        testbin = Bin(3, (20, 20, 20), 100)
        testItem = Item(3, 'Item3', 'cube', (10, 5, 10), 1.5, 1, 50, True, 'green')
        testItem.formatNumbers(1)
        testbin.putItem(testItem, [5, 5, 5])
        assert len(testbin.items) == 1  # The item should be placed in the bin with a rotation
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Two items that barely fit together
        testbin = Bin(3, (20, 10, 10), 100)
        testItem1 = Item(2, 'testItem1', 'cube', [10, 10, 10], 2.0, 2, 75, True, 'blue')
        testItem2 = Item(2, 'testItem2', 'cube', [10, 10, 10], 2.0, 2, 75, True, 'red')
        testItem1.formatNumbers(1)
        testItem2.formatNumbers(1)
        testbin.putItem(testItem1, [0,0,0])
        testbin.putItem(testItem2, [10,0,0])
        self.assertEqual(len(testbin.items), 2)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Item doesn't fit
        testbin = Bin(3, (5, 5, 5), 100)
        testItem = Item(2, 'testItem', 'cube', [15, 15, 15], 2.0, 2, 75, True, 'blue')
        testItem.formatNumbers(1)
        testbin.putItem(testItem, [0, 0, 0])
        self.assertEqual(len(testbin.items), 0)

        # Item weight exceeds bin max weight
        testbin = Bin(1, (20, 20, 20), 2)
        testItem = Item(1, 'testItem', 'cube', (10, 10, 10), 3.0, 1, 50, True, 'purple')
        testItem.formatNumbers(1)
        testbin.putItem(testItem, [5, 5, 5])
        self.assertEqual(len(testbin.items), 0)

        # Invalid Pivot Type
        testItem = Item(2, 'testItem', 'cube', [15, 15, 15], 2.0, 2, 75, True, 'blue')
        testItem.formatNumbers(1)
        with self.assertRaises(TypeError):
            testbin.putItem(testItem, ["hello", 23, False])

        # Invalid Item Types
        testbin2 = Bin("testBin2", [100,200,100], 5000, 1, 0)
        with self.assertRaises(AttributeError):
            testbin.putItem("hello", [80, 90, 80])
            testbin.putItem(5, [80, 90, 80])
            testbin.putItem(testbin2, [80, 90, 80])

    # BB Done       
    def test_binCheckDepth(self):


                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid item and bin
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 10, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkDepth(unfix_point), 0.0)

        # Multiple items
        testItem1 = Item(1, 'testItem1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testItem2 = Item(2, 'testItem2', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'blue')
        testbin = Bin(3, (10, 10, 10), 100)
        testbin.items.append(testItem1)
        testbin.items.append(testItem2)
        unfix_point = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkDepth(unfix_point), 0.0)

        # Top depth exceeds available space
        testItem = Item(1, 'testItem', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(4, (10, 10, 10), 100)
        testbin.items.append(testItem)
        unfix_point4 = [0, 10, 0, 10, 0, 15]
        self.assertEqual(testbin.checkDepth(unfix_point4), 0.0)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Empty Bin
        testbin = Bin(1, (10, 10, 10), 100)
        unfix_point = [0, 5, 0, 5, 0, 5]
        self.assertEqual(testbin.checkDepth(unfix_point), 0.0)

                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid unfix_point data type
        testbin = Bin(8, (10, 10, 10), 100)
        unfix_point = "0 5 0 5 0 5"
        with self.assertRaises(ValueError):
            testbin.checkDepth(unfix_point)

        # Insufficient unfix_point elements
        testbin = Bin(8, (10, 10, 10), 100)
        unfix_point = [0, 5, 0, 5, 0]
        with self.assertRaises(IndexError):
            testbin.checkDepth(unfix_point)

    # BB Done
    def test_binCheckWidth(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Valid item and bin
        testitem = Item(1, 'testitem', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(5, (10, 10, 10), 100)
        testbin.items.append(testitem)
        unfix_point = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkWidth(unfix_point), 0)

        # Multiple items
        testItem1 = Item(1, 'testItem1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testItem2 = Item(2, 'testItem2', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'blue')
        testbin = Bin(6, (10, 10, 10), 100)
        testbin.items.extend([testItem1, testItem2])
        unfix_pounfix_pointint6 = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkWidth(unfix_point), 0)

        # Top Width Exceeds Available Space
        testitem = Item(1, 'testitem', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(7, (10, 10, 10), 100)
        testbin.items.append(testitem)
        unfix_point = [0, 10, 0, 10, 0, 15]
        self.assertEqual(testbin.checkWidth(unfix_point), 0)
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #
        # Empty Bin
        testbin = Bin(1, (10, 10, 10), 100)
        unfix_point = [0, 5, 0, 5, 0, 5]
        self.assertEqual(testbin.checkWidth(unfix_point), 0)
               
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid unfix_point data type
        testbin = Bin(3, (10, 10, 10), 100)
        unfix_point = "0 5 0 5 0 5"
        with self.assertRaises(ValueError):
            self.assertEqual(testbin.checkWidth(unfix_point), 0)

        # Insufficient unfix_point elements
        testbin = Bin(3, (10, 10, 10), 100)
        unfix_point = [0, 5, 0, 5]
        with self.assertRaises(IndexError):
            self.assertEqual(testbin.checkWidth(unfix_point), 0)

    # BB Done
    def test_binCheckHeight(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid item and bin
        testitem = Item(1, 'testitem', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(5, (10, 10, 10), 100)
        testbin.items.append(testitem)
        unfix_point = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkHeight(unfix_point), 0)

        # Multiple items
        testItem1 = Item(1, 'testItem1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testItem2 = Item(2, 'testItem2', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'blue')
        testbin = Bin(6, (10, 10, 10), 100)
        testbin.items.extend([testItem1, testItem2])
        unfix_pounfix_pointint6 = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkHeight(unfix_point), 0)

        # Top Height Exceeds Available Space
        testitem = Item(1, 'testitem', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(7, (10, 10, 10), 100)
        testbin.items.append(testitem)
        unfix_point = [0, 10, 0, 10, 0, 15]
        self.assertEqual(testbin.checkHeight(unfix_point), 0)

                                        #                #
                                        #   Edge Cases   #
                                        #                #
        # Empty Bin
        testbin = Bin(1, (10, 10, 10), 100)
        unfix_point = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkHeight(unfix_point), 0)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid unfix_point data type
        testbin = Bin(3, (10, 10, 10), 100)
        unfix_point = "0 5 0 5 0 5"
        with self.assertRaises(ValueError):
            self.assertEqual(testbin.checkHeight(unfix_point), 0)

        # Insufficient unfix_point elements
        testbin = Bin(3, (10, 10, 10), 100)
        unfix_point = [0, 5, 0, 5]
        with self.assertRaises(IndexError):
            self.assertEqual(testbin.checkHeight(unfix_point), 0)

    # BB Done
    def test_binAddCorner(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
                                
        # Valid Bin
        testbin = Bin(1, (10, 10, 10), 100, 2)
        corners = testbin.addCorner()
        self.assertEqual(len(corners), 8)
        for corner in corners:
            self.assertEqual(corner.width, 2)
            self.assertEqual(corner.height, 2)
            self.assertEqual(corner.depth, 2)


                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Adding a Corner to a Bin with Existing Items
        testitem = Item(1, 'testitem', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 10, 10), 100, 3)
        testbin.items.append(testitem)
        corners = testbin.addCorner()
        self.assertEqual(len(corners), 8)
        for corner in corners:
            self.assertEqual(corner.width, 3)
            self.assertEqual(corner.height, 3)
            self.assertEqual(corner.depth, 3)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Negative corner size
        testbin = Bin(2, (10, 10, 10), 100, -3)
        corners = testbin.addCorner()
        self.assertEqual(len(corners), 8)
        for corner in corners:
            self.assertEqual(corner.width, -3)
            self.assertEqual(corner.height, -3)
            self.assertEqual(corner.depth, -3)

        # Corner size is 0
        testbin = Bin(2, (10, 10, 10), 100, 0)
        corners = testbin.addCorner()
        self.assertEqual(corners, None)

    # BB Done
    def test_binPutCorner(self):

                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid bin and corners, place all corners
        testbin = Bin(1, (10, 10, 10), 100, 2)
        corners = testbin.addCorner()
        for corner in corners:
            testbin.putCorner(0, corner)
        self.assertEqual(len(testbin.items), 8)
        for count in range(len(corners)):
            self.assertEqual(testbin.items[count], corners[count])
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Valid bin and corners, place 1 corner
        testbin = Bin(1, (10, 10, 10), 100, 2)
        corner_item = Item(partno='corner', name='corner', typeof='cube', WHD=(2, 2, 2), weight=0, level=0, loadbear=0, updown=True, color='#000000')
        testbin.putCorner(0, corner_item)
        self.assertEqual(len(testbin.items), 1)
        self.assertEqual(testbin.items[0], corner_item)

        # Placing corner in bin with existing items
        testitem = Item(1, 'testitem', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 10, 10), 100, 3)
        testitem.formatNumbers(2)
        testbin.putItem(testitem, [0, 0, 0])
        corner_item = Item(partno='corner', name='corner', typeof='cube', WHD=(3, 3, 3), weight=0, level=0, loadbear=0, updown=True, color='#000000')
        testbin.putCorner(0, corner_item)
        self.assertEqual(len(testbin.items), 2)
        self.assertEqual(testbin.items[1], corner_item)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #
            
        # Info value too high
        testbin = Bin(3, (10, 10, 10), 100)
        corner_item = Item(partno='corner', name='corner', typeof='cube', WHD=(2, 2, 2), weight=0, level=0, loadbear=0, updown=True, color='#000000')
        with self.assertRaises(IndexError):
            testbin.putCorner(8, corner_item)

        # Invalid info value data type
        testbin = Bin(3, (10, 10, 10), 100)
        corner_item = Item(partno='corner', name='corner', typeof='cube', WHD=(2, 2, 2), weight=0, level=0, loadbear=0, updown=True, color='#000000')
        with self.assertRaises(TypeError):
            testbin.putCorner("hello world", corner_item)

        # corner size greater than bin size
        testbin = Bin(4, (10, 10, 10), 100, 15)
        testbin.corner = 15
        corner_item = Item(partno='corner', name='corner', typeof='cube', WHD=(15, 15, 15), weight=0, level=0, loadbear=0, updown=True, color='#000000')
        testbin.putCorner(0, corner_item)
        self.assertEqual(len(testbin.items), 1)

    # BB Done
    def test_binClearBin(self):

                                        #                #
                                        # Positive Cases #
                                        #                #
                    
        # Bin with multiple items
        testitem1 = Item(1, 'testitem1', 'cube', (4, 4, 4), 1.0, 1, 50, True, 'red')
        testitem2 = Item(2, 'testitem2', 'cube', (3, 3, 3), 1.0, 1, 50, True, 'blue')
        testbin = Bin(3, (10, 10, 10), 100)
        testitem1.formatNumbers(2)
        testitem2.formatNumbers(2)
        testbin.putItem(testitem1)
        testbin.putItem(testitem2)
        self.assertEqual(len(testbin.items), 2)
        testbin.clearBin()
        self.assertEqual(len(testbin.items), 0)

                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #
        # Empty Bin
        # Bin with multiple items
        testbin = Bin(3, (10, 10, 10), 100)
        self.assertEqual(len(testbin.items), 0)
        testbin.clearBin()
        self.assertEqual(len(testbin.items), 0)

        # Bin with 1 item
        testitem1 = Item(1, 'testitem1', 'cube', (4, 4, 4), 1.0, 1, 50, True, 'red')
        testbin = Bin(3, (10, 10, 10), 100)
        testitem1.formatNumbers(2)
        testbin.putItem(testitem1)
        self.assertEqual(len(testbin.items), 1)
        testbin.clearBin()
        self.assertEqual(len(testbin.items), 0)

    # Packer Class Methods
    def test_packerConstructor(self):
        # no input variables
        testPacker = Packer()

        self.assertEqual(testPacker.bins, [])
        self.assertEqual(testPacker.items, [])
        self.assertEqual(testPacker.unfit_items, [])
        self.assertEqual(testPacker.total_items, 0)
        self.assertEqual(testPacker.binding, [])

    def test_packerAddBin(self):
        testPacker = Packer()
        testbin1 = Bin("testbin1", [100,200,100], 5000, 1, 0)
        testbin2 = Bin("testbin2", [250,30,1000], 10000)

        testPacker.addBin(testbin1)
        testPacker.addBin(testbin2)

        #return string of bins
        def retStr(bins):
            ret = []
            for bin in bins:
                ret.append(bin.string())
            return ret

        self.assertEqual(retStr(testPacker.bins), ['testbin1(100x200x100, max_weight:5000) vol(2000000)', 'testbin2(250x30x1000, max_weight:10000) vol(7500000)'])

        testPacker2 = Packer()

        testItem1 = Item("testitem1","test","cube", [10,30,30], 25, 2, 400, True, "orange")

        testPacker2.addBin(testItem1)

        self.assertEqual(retStr(testPacker2.bins), ['testitem1(10x30x30, weight: 25) pos([0, 0, 0]) rt(0) vol(9000)'])

        self.assertEqual(testPacker2.addBin(True), None)

        self.assertEqual(testPacker2.addBin("testItem1"), None)

        self.assertEqual(testPacker2.addBin(45), None)

        self.assertEqual(testPacker2.addBin(None), None)

    def test_packerAddItem(self):
        testPacker = Packer()
        testItem1 = Item("testitem1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("testitem2","test","cube", [1,1,1], 5, 2, 20, True, "blue")
        testItem3 = Item("testitem3","test","cube", [60,10,10], 200, 2, 250, True, "grey")

        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)

        #func to return string of items
        def retStr(items):
            res = []
            for item in items:
                res.append(item.string())
            return res

        self.assertEqual(retStr(testPacker.items),['testitem1(10x30x30, weight: 25) pos([0, 0, 0]) rt(0) vol(9000)', 'testitem2(1x1x1, weight: 5) pos([0, 0, 0]) rt(0) vol(1)', 'testitem3(60x10x10, weight: 200) pos([0, 0, 0]) rt(0) vol(6000)'])

        self.assertEqual(testPacker.total_items, 3)

        testPacker2 = Packer()

        testbin1 = Bin("testbin1", [100,200,100], 5000, 1, 0)

        testPacker2.addItem(testbin1)

        self.assertEqual(retStr(testPacker2.items),['testbin1(100x200x100, max_weight:5000) vol(2000000)'])

        testPacker3 = Packer()

        testPacker3.addItem("testbin1")

        testPacker3.addItem(False)

        testPacker3.addItem(43)

        self.assertEqual(testPacker3.items,['testbin1', False, 43])

    # Not sure why this method has an error
    def test_packerPack2Bin(self):

        #print bin items
        def retStr(bin):
            res = []
            for item in bin.items:
                if item.name != 'corner':
                    res.append(item.partno)
            return res
        
        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 0)
        testItem1 = Item("testItem1","test","cube", [10,30,30], 25, 2, 400, True, "orange")


        testPacker1.addBin(testBin1)

        testPacker1.addItem(testItem1)

        # format bins
        for bin in testPacker1.bins:
            bin.formatNumbers(3)

        # format items
        for item in testPacker1.items:
            item.formatNumbers(3)

        testPacker1.pack2Bin(testBin1, testItem1, True, False, 0)

        # print(retStr(testBin1))





    def test_packerSortBinding(self):
        """
        Test to find out what sortBinding does and how it works
        """
        bin1 = Bin(partno='Bin', WHD=(589,243,259), max_weight=28080, corner=15, put_type= 1)
        item1 = Item(partno='toy1', name='toy', typeof='cube', WHD=(85, 60, 60), weight=10, level=1, loadbear=100, updown=True, color='#FFFF37')
        item2 = Item(partno='pencil1', name='pencil', typeof='cube', WHD=(85, 60, 60), weight=10, level=1, loadbear=100, updown=True, color='#FFFF37')
        item3 = Item(partno='spinner1', name='pencil', typeof='cube', WHD=(85, 60, 60), weight=10, level=1, loadbear=100, updown=True, color='#FFFF37')
        item4 = Item(partno='shoes1', name='shoes', typeof='cube', WHD=(85, 60, 60), weight=10, level=1, loadbear=100, updown=True, color='#FFFF37')
        testPacker = Packer()
        testPacker.addBin(bin1)
        testPacker.addItem(item1)
        testPacker.addItem(item2)
        testPacker.addItem(item3)
        testPacker.addItem(item4)

        bind = [('toy','shoes')]

        testPacker.binding = bind

        # for i in testPacker.items:
        #     print (i.string())

        testPacker.sortBinding(bind)

        # returns string of items
        def retStr(packer):
            ret = []
            for item in testPacker.items:
                ret.append(item.string())
            return ret

        self.assertEqual(retStr(testPacker), ['toy1(85x60x60, weight: 10) pos([0, 0, 0]) rt(0) vol(306000)', 'shoes1(85x60x60, weight: 10) pos([0, 0, 0]) rt(0) vol(306000)', 'pencil1(85x60x60, weight: 10) pos([0, 0, 0]) rt(0) vol(306000)', 'spinner1(85x60x60, weight: 10) pos([0, 0, 0]) rt(0) vol(306000)'])

        # for i in testPacker.items:
        #     print (i.string())

    def test_packerPutOrder(self):
        
        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)

        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [5,5,5], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1,100,2], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [10,2,10], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [3,20,42], 20, 2, 400, True, "green")

        testPacker1.addBin(testBin1)
        testPacker1.addItem(testItem1)
        testPacker1.addItem(testItem2)
        testPacker1.addItem(testItem3)
        testPacker1.addItem(testItem5)
        testPacker1.addItem(testItem4)
        testPacker1.addItem(testItem6)

        testPacker1.pack()
        

        #print bin items
        def retStr(bin):
            res = []
            for item in bin.items:
                if item.name != 'corner':
                    res.append(item.partno)
            return res

        self.assertEqual(retStr(testBin1), ['4', '2', '1', '5', '6', '3'])

        testBin1.put_type = 2

        testPacker1.putOrder()

        self.assertEqual(retStr(testBin1), ['2', '5', '6', '3', '4', '1'])
        
    def test_packerGravityCenter(self):
        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)

        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [5,50,5], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1,100,2], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [10,120,10], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")

        testPacker1.addBin(testBin1)
        testPacker1.addItem(testItem1)
        testPacker1.addItem(testItem2)
        testPacker1.addItem(testItem3)
        testPacker1.addItem(testItem5)
        testPacker1.addItem(testItem4)
        testPacker1.addItem(testItem6)

        # final input is variation, variation[0] determines if we use variation or not
        testPacker1.pack(False,True,True,True,0.75,[],0,[False, False])
        
        # #print bin items
        # def retStr(bin):
        #     res = []
        #     for item in bin.items:
        #         if item.name != 'corner':
        #             res.append(item.partno)
        #     return res

        # print item positions
        def retStr(bin):
            res = []
            for item in bin.items:
                if item.name != 'corner':
                    res.append(item.position)
            return res

        # no gravity distribution with as we stopped it from running
        self.assertEqual(testBin1.gravity, [96.48, 0.0, 3.52, 0.0])

        # remaking all of the items, bins and packer
        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)

        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [5,50,5], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1,100,2], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [10,120,10], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")

        testPacker1.addBin(testBin1)
        testPacker1.addItem(testItem1)
        testPacker1.addItem(testItem2)
        testPacker1.addItem(testItem3)
        testPacker1.addItem(testItem5)
        testPacker1.addItem(testItem4)
        testPacker1.addItem(testItem6)


        testPacker1.pack(False,True,True,True,0.75,[],0,[True,False])

        self.assertEqual(testBin1.gravity, [])

    def test_packerPack(self):
        
        # False,True,True,True,0.75,[],0
        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)

        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [5,50,5], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1,100,2], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [10,120,10], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")

        testPacker1.addBin(testBin1)
        testPacker1.addItem(testItem1)
        testPacker1.addItem(testItem2)
        testPacker1.addItem(testItem3)
        testPacker1.addItem(testItem5)
        testPacker1.addItem(testItem4)
        testPacker1.addItem(testItem6)

        testPacker1.pack(False, True, True, True, 0.75, [])

        #print bin items
        def retStr(bin):
            res = []
            for item in bin.items:
                if item.name != 'corner':
                    res.append(item.partno)
            return res
        
        self.assertEqual(retStr(testBin1), ['4', '2', '3', '1', '5'])

        # True,True,True,True,0.75,[],0
        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)

        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [5,50,5], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1,100,2], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [10,120,10], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")

        testPacker1.addBin(testBin1)
        testPacker1.addItem(testItem1)
        testPacker1.addItem(testItem2)
        testPacker1.addItem(testItem3)
        testPacker1.addItem(testItem5)
        testPacker1.addItem(testItem4)
        testPacker1.addItem(testItem6)

        testPacker1.pack(True,True,True,True,0.75,[])

        self.assertEqual(retStr(testBin1), ['6', '1', '4', '3', '2'])

        # False,False,True,True,0.75,[],0
        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)

        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [5,50,5], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1,100,2], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [10,120,10], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")

        testPacker1.addBin(testBin1)
        testPacker1.addItem(testItem1)
        testPacker1.addItem(testItem2)
        testPacker1.addItem(testItem3)
        testPacker1.addItem(testItem5)
        testPacker1.addItem(testItem4)
        testPacker1.addItem(testItem6)

        testPacker1.pack(False,False,True,True,0.75,[])

        self.assertEqual(retStr(testBin1), ['4', '2', '3', '1', '5'])

        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)

        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [5,50,5], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1,100,2], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [10,120,10], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")

        testPacker1.addBin(testBin1)
        testPacker1.addItem(testItem1)
        testPacker1.addItem(testItem2)
        testPacker1.addItem(testItem3)
        testPacker1.addItem(testItem5)
        testPacker1.addItem(testItem4)
        testPacker1.addItem(testItem6)

        testPacker1.pack(True,False,True,True,0.75,[])

        self.assertEqual(retStr(testBin1),['6', '1', '4', '3', '2'])

        # False,True,False,True,0.75,[],0
        testPacker1 = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)

        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [5,50,5], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1,100,2], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [10,120,10], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")

        testPacker1.addBin(testBin1)
        testPacker1.addItem(testItem1)
        testPacker1.addItem(testItem2)
        testPacker1.addItem(testItem3)
        testPacker1.addItem(testItem5)
        testPacker1.addItem(testItem4)
        testPacker1.addItem(testItem6)

        testPacker1.pack(False,True,False,True,0.75,[])

        self.assertEqual(retStr(testBin1), ['4', '2', '3', '1', '5'])


if __name__ == '__main__':
    unittest.main()