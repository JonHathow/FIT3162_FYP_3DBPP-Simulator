#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import rectIntersect, intersect, getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer, Axis, RotationType
from decimal import Decimal
import decimal
import unittest
import numpy as np

"""
Black  Box Testing for Option 1, Jerry's Algorithm
"""

class TestAux(unittest.TestCase):
    
    #                     #
    #  Auxiliary Methods  #
    #                     #

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
        self.assertEqual(testItem.partno, 2) 
        self.assertEqual(testItem.name, 'Cup') 
        self.assertEqual(testItem.typeof, 'cylinder')
        self.assertEqual(testItem.width, 8) 
        self.assertEqual(testItem.height, 8) 
        self.assertEqual(testItem.depth, 4) 
        self.assertEqual(testItem.weight, 0.3) 
        self.assertEqual(testItem.level, 1) 
        self.assertEqual(testItem.loadbear, 50) 
        self.assertEqual(testItem.updown, False) 
        self.assertEqual(testItem.color, 'blue') 

        # Random input types
        testItem = Item("¯\_(ツ)_/¯", False, 'Hexagon', (8.5, -34, 4.55), '0.3', (1,2,4,8), True, 'Maybe', 'blue')
        self.assertEqual(testItem.partno, "¯\_(ツ)_/¯")
        self.assertEqual(testItem.name, False)
        self.assertEqual(testItem.typeof, 'Hexagon')
        self.assertEqual(testItem.width, 8.5)
        self.assertEqual(testItem.height, -34)
        self.assertEqual(testItem.depth, 4.55)
        self.assertEqual(testItem.weight, '0.3') 
        self.assertEqual(testItem.level, (1,2,4,8))
        self.assertEqual(testItem.loadbear, True)
        self.assertEqual(testItem.updown, False)
        self.assertEqual(testItem.color, 'blue')

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

    def test_binClearBin(self):

                                        #                #
                                        # Positive Cases #
                                        #                #
                    
        # Bin with multiple items
        testitem1 = Item(1, 'testitem1', 'cube', (4, 4, 4), 1.0, 1, 50, True, 'red')
        testitem2 = Item(2, 'testitem2', 'cube', (3, 3, 3), 1.0, 1, 50, True, 'blue')
        testbin = Bin(3, (100, 100, 100), 100)
        testitem1.formatNumbers(2)
        testitem2.formatNumbers(2)
        testbin.putItem(testitem1, [0,0,0])
        testbin.putItem(testitem2, [5,5,5])
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
        testbin.putItem(testitem1, [0,0,0])
        self.assertEqual(len(testbin.items), 1)
        testbin.clearBin()
        self.assertEqual(len(testbin.items), 0)

    #                        #
    #  Packer Class Methods  #
    #                        #

    def test_packerConstructor(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Valid Construction
        testPacker = Packer()
        self.assertEqual(testPacker.bins, [])
        self.assertEqual(testPacker.items, [])
        self.assertEqual(testPacker.unfit_items, [])
        self.assertEqual(testPacker.total_items, 0)
        self.assertEqual(testPacker.binding, [])

    def test_packerAddBin(self):

                                        #                #
                                        # Positive Cases #
                                        #                #

        # Adding 1 Bin
        testPacker = Packer()
        testbin = Bin("testbin", [100,200,100], 5000, 1, 0)
        testPacker.addBin(testbin)
        self.assertEqual(len(testPacker.bins), 1)

        # Adding multiple bins
        testPacker = Packer()
        testbin1 = Bin("testbin1", [100,200,100], 5000, 1, 0)
        testbin2 = Bin("testbin1", [100,50,30], 1000)
        testPacker.addBin(testbin1)
        testPacker.addBin(testbin2)
        self.assertEqual(len(testPacker.bins), 2)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Adding invalid bin
        testPacker = Packer()
        testPacker.addBin("Not a Bin")
        self.assertEqual(len(testPacker.bins), 1)

    def test_packerAddItem(self):

                                        #                #
                                        # Positive Cases #
                                        #                #

        # Adding 1 Item
        testPacker = Packer()
        testItem = Item("testitem","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testPacker.addItem(testItem)
        self.assertEqual(len(testPacker.items), 1)

        # Adding multiple Item
        testPacker = Packer()
        testItem1 = Item("testitem1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("testitem2","test","cube", [1,1,1], 5, 2, 20, True, "blue")
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        self.assertEqual(len(testPacker.items), 2)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Adding invalid Item
        testPacker = Packer()
        testPacker.addItem("Not an Item")
        self.assertEqual(len(testPacker.items), 1)

    def test_packerPack2Bin(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid packing
        testpacker = Packer()
        testbin = Bin("testbin", [100,200,100], 5000, 0, 0)
        testItem = Item("testitem","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem.formatNumbers(3)
        testbin.formatNumbers(3)
        testpacker.pack2Bin(testbin, testItem, True, False, 0)
        self.assertEqual(len(testbin.unfitted_items), 0)
        self.assertEqual(len(testbin.items), 1)

        # Failed packing
        testpacker = Packer()
        testbin = Bin("testbin", [5,20,5], 200, 0, 0)
        testItem = Item("testitem","test","cube", [100,300,300], 25, 2, 400, True, "orange")
        testItem.formatNumbers(3)
        testbin.formatNumbers(3)
        testpacker.pack2Bin(testbin, testItem, True, False, 0)
        self.assertEqual(len(testbin.unfitted_items), 1)
        self.assertEqual(len(testbin.items), 0)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # 0 size item
        testpacker = Packer()
        testbin = Bin("testbin", [100,200,100], 5000, 0, 0)
        testItem = Item("testitem","test","cube", [0,0,0], 25, 2, 400, True, "orange")
        testItem.formatNumbers(3)
        testbin.formatNumbers(3)
        testpacker.pack2Bin(testbin, testItem, True, False, 0)
        self.assertEqual(len(testbin.unfitted_items), 0)
        self.assertEqual(len(testbin.items), 1)

        # Item barely fits
        testpacker = Packer()
        testbin = Bin("testbin", [100,200,100], 5000, 0, 0)
        testItem = Item("testitem","test","cube", [100,200,100], 25, 2, 400, True, "orange")
        testItem.formatNumbers(3)
        testbin.formatNumbers(3)
        testpacker.pack2Bin(testbin, testItem, True, False, 0)
        self.assertEqual(len(testbin.unfitted_items), 0)
        self.assertEqual(len(testbin.items), 1)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid Bin
        testpacker = Packer()
        testbin = "Not a Bin"
        testItem = Item("testitem","test","cube", [100,300,300], 25, 2, 400, True, "orange")
        testItem.formatNumbers(3)
        with self.assertRaises(AttributeError):
            testpacker.pack2Bin(testbin, testItem, True, False, 0)


        # Invalid Item
        testpacker = Packer()
        testbin = Bin("testbin", [100,200,100], 5000, 0, 0)
        testItem = "Not an Item"
        testbin.formatNumbers(3)
        with self.assertRaises(AttributeError):
            testpacker.pack2Bin(testbin, testItem, True, False, 0)

    def test_packerSortBinding(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid binding
        testPacker = Packer()
        testBin = Bin("B001", WHD=[10, 20, 30], max_weight=100)
        testItem1 = Item("1", "shoe", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem2 = Item("2", "book", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem3 = Item("3", "hat", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem4 = Item("4", "gloves", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem5 = Item("5", "shoe", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem6 = Item("6", "book", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testPacker.items = [testItem1, testItem2, testItem3, testItem4, testItem5, testItem6]
        testPacker.binding = [("shoe", "book")]
        testPacker.sortBinding(testBin)
        item_list = []
        for i in range(len(testPacker.items)):
            item_list.append(testPacker.items[i].name)
        self.assertEqual(item_list,  ['shoe', 'book', 'shoe', 'book', 'hat', 'gloves'])

                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # No Matching Binding
        packer = Packer()
        bin = Bin(partno="B001", WHD=[10, 20, 30], max_weight=100)
        testItem1 = Item("1", "hat", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem2 = Item("2", "gloves", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem3 = Item("3", "socks", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem4 = Item("4", "scarf", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem5 = Item("5", "shoes", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem6 = Item("6", "book", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testPacker.items = [testItem1, testItem2, testItem3, testItem4, testItem5, testItem6]
        packer.binding = [("shoe", "book")]
        packer.sortBinding(bin)
        item_list = []
        for i in range(len(testPacker.items)):
            item_list.append(testPacker.items[i].name)
        self.assertEqual(item_list,  ["hat", "gloves", "socks", "scarf", "shoes", "book"])

                                        #                #
                                        # Negative Cases #
                                        #                #
        # No Binding information
        testPacker = Packer()
        testBin = Bin("B001", WHD=[10, 20, 30], max_weight=100)
        testItem1 = Item("1", "shoe", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem2 = Item("2", "book", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem3 = Item("3", "hat", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem4 = Item("4", "gloves", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem5 = Item("5", "shoe", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testItem6 = Item("6", "book", 'cube', (85, 60, 60), 10, 1, 100, True, 'red')
        testPacker.items = [testItem1, testItem2, testItem3, testItem4, testItem5, testItem6]
        with self.assertRaises(ValueError):
            testPacker.sortBinding(testBin)
    
    def test_packerPutOrder(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        testItem1 = Item("1","testItem1","cube", [5, 5, 5], 25, 2, 400, True, "orange")
        testItem2 = Item("2","testItem2","cube", [5, 5, 5], 5, 2, 400, True, "red")
        testItem3 = Item("3","testItem3","cube", [5, 5, 5], 20, 2, 400, True, "blue")
        testPacker = Packer()
        
        

        # put_type = 1
        testBin = Bin("testBin1", [1000,1000,1000], 5000, 1, 1)
        testPacker.addBin(testBin)
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testItem3.formatNumbers(2)
        testBin.putItem(testItem1, [5, 10, 20])
        testBin.putItem(testItem2, [500, 500, 500])
        testBin.putItem(testItem3, [25, 5, 10])
        testPacker.putOrder()
        item_lst = []
        for item in testBin.items:
            if item.name != 'corner':
                item_lst.append(item.partno)
        self.assertEqual(item_lst,["1", "3", "2"])

        # put_type = 2
        testBin = Bin("testBin1", [1000,1000,1000], 5000, 1, 2)
        testPacker.addBin(testBin)
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testItem3.formatNumbers(2)
        testBin.putItem(testItem1, [5, 10, 20])
        testBin.putItem(testItem2, [500, 500, 500])
        testBin.putItem(testItem3, [25, 5, 10])
        testPacker.putOrder()
        item_lst = []
        for item in testBin.items:
            if item.name != 'corner':
                item_lst.append(item.partno)
        self.assertEqual(item_lst,["3", "1", "2"])
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # put_type = 3
        testBin = Bin("testBin1", [1000,1000,1000], 5000, 1, 3)
        testPacker.addBin(testBin)
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testItem3.formatNumbers(2)
        testBin.putItem(testItem1, [5, 10, 20])
        testBin.putItem(testItem2, [500, 500, 500])
        testBin.putItem(testItem3, [25, 5, 10])
        testPacker.putOrder()
        item_lst = []
        for item in testBin.items:
            if item.name != 'corner':
                item_lst.append(item.partno)
        self.assertEqual(item_lst,["1", "2", "3"])

    def test_packerGravityCenter(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Valid bin and single item
        testPacker = Packer()
        testBin = Bin("testBin", [300,200,300], 5000, 1, 1)
        testItem = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testPacker.addBin(testBin)
        testItem.formatNumbers(2)
        testBin.putItem(testItem, [0,0,0])
        testPacker.gravityCenter(testBin)
        self.assertEqual(testPacker.gravityCenter(testBin), [100.0, 0.0, 0.0, 0.0])

        # Valin bin and multiple items
        testPacker = Packer()
        testBin = Bin("testBin", [100,100,100], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [30,10,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [50,10,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [30,10,40], 20, 2, 400, True, "blue")
        testPacker.addBin(testBin)
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testItem3.formatNumbers(2)
        testBin.putItem(testItem1, [0, 0, 0])
        testBin.putItem(testItem2, [15, 15, 15])
        testBin.putItem(testItem3, [25, 30, 20])
        testPacker.gravityCenter(testBin)
        self.assertEqual(testPacker.gravityCenter(testBin), [91.87, 0.0, 8.13, 0.0]) 
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #
        
        # Small Dimensions
        testPacker = Packer()
        testBin = Bin("testBin", [20,20,20], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [2,2,2], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [1,1,2], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [2,5,5], 20, 2, 400, True, "blue")
        testPacker.addBin(testBin)
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testItem3.formatNumbers(2)
        testBin.putItem(testItem1, [0, 0, 0])
        testBin.putItem(testItem2, [2, 0, 0])
        testBin.putItem(testItem3, [1, 3, 2])
        testPacker.gravityCenter(testBin)
        self.assertEqual(testPacker.gravityCenter(testBin), [100.0, 0.0, 0.0, 0.0])

        # Large Dimensions
        testPacker = Packer()
        testBin = Bin("testBin", [300,200,300], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [100,50,150], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [200,100,100], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [50,40,200], 20, 2, 400, True, "blue")
        testPacker.addBin(testBin)
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testItem3.formatNumbers(2)
        testBin.putItem(testItem1, [0, 0, 0])
        testBin.putItem(testItem2, [50, 75, 50])
        testBin.putItem(testItem3, [0, 200, 0])
        testPacker.gravityCenter(testBin)
        self.assertEqual(testPacker.gravityCenter(testBin), [85.52, 2.15, 6.23, 6.11]) 
        
                                        #                #
                                        # Negative Cases #
                                        #                #
        # Empty bin
        testPacker = Packer()
        testBin = Bin("testBin", [300,200,300], 5000, 1, 1)
        testPacker.addBin(testBin)
        with self.assertRaises(ZeroDivisionError):
            testPacker.gravityCenter(testBin)


        # Invalid Bin Data Type                      
        testPacker = Packer()
        testBin = "Not a Bin"
        testPacker.addBin(testBin)
        with self.assertRaises(AttributeError):
            testPacker.gravityCenter(testBin)

    def test_packerPack(self):

        #print bin items
        def retStr(bin):
            res = []
            for item in bin.items:
                if item.name != 'corner':
                    res.append(item.partno)
            return res

                                        #                #
                                        # Positive Cases #
                                        #                #

        

        # Valin Input [False, False, False, False]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(False, False, False, False, 0.75, [])
        self.assertEqual(retStr(testBin1), ['3', '1'])
        self.assertEqual(retStr(testBin2), ['3', '1', '6', '2', '5'])

        # Valin Input [False, False, False, True]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(False, False, False, True, 0.75, [])
        self.assertEqual(retStr(testBin1), ['3', '1'])
        self.assertEqual(retStr(testBin2), ['3', '1', '6', '2', '5'])

        # Valin Input [False, False, True, False]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(False, False, True, False, 0.75, [])
        self.assertEqual(retStr(testBin1), ['3', '1'])
        self.assertEqual(retStr(testBin2), ['3', '1', '6', '2', '5'])

        # Valin Input [False, False, True, True]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(False, False, True, True, 0.75, [])
        self.assertEqual(retStr(testBin1), ['3', '1'])
        self.assertEqual(retStr(testBin2), ['3', '1', '6', '2', '5'])

        # Valin Input [False, True, False, False]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(False, True, False, False, 0.75, [])
        self.assertEqual(retStr(testBin1), ['3', '1'])
        self.assertEqual(retStr(testBin2), ['6', '2', '5'])

        # Valin Input [False, True, False, True]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(False, True, False, True, 0.75, [])
        self.assertEqual(retStr(testBin1), ['3', '1'])
        self.assertEqual(retStr(testBin2), ['6', '2', '5'])

        # Valin Input [False, True, True, False]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(False, True, True, False, 0.75, [])
        self.assertEqual(retStr(testBin1), ['3', '1'])
        self.assertEqual(retStr(testBin2), ['6', '2', '5'])

        # Valin Input [False, True, True, True]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(False, True, True, True, 0.75, [])
        self.assertEqual(retStr(testBin1), ['3', '1'])
        self.assertEqual(retStr(testBin2), ['6', '2', '5'])

        # Valin Input [True, False, False, False]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(True, False, False, False, 0.75, [])
        self.assertEqual(retStr(testBin1), ['6', '1', '3'])
        self.assertEqual(retStr(testBin2), ['5', '2', '6', '1', '3'])

        # Valin Input [True, False, False, True]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(True, False, False, True, 0.75, [])
        self.assertEqual(retStr(testBin1), ['6', '1', '3'])
        self.assertEqual(retStr(testBin2), ['5', '2', '6', '1', '3'])


        # Valin Input [True, False, True, False]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(True, False, True, False, 0.75, [])
        self.assertEqual(retStr(testBin1), ['6', '1', '3'])
        self.assertEqual(retStr(testBin2), ['5', '2', '6', '1', '3'])

        # Valin Input [True, False, True, True]
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        testPacker.pack(True, False, True, True, 0.75, [])
        self.assertEqual(retStr(testBin1), ['6', '1', '3'])
        self.assertEqual(retStr(testBin2), ['5', '2', '6', '1', '3'])
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Single Bin Single Item
        testPacker = Packer()
        testBin = Bin("testBin", [100,200,100], 5000, 1, 1)
        testItem = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testPacker.addBin(testBin)
        testPacker.addItem(testItem)
        testPacker.pack(False, True, False, False, 0.75, [])
        self.assertEqual(retStr(testBin), ['1'])

        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Single Bin No Item
        testPacker = Packer()
        testBin = Bin("testBin", [100,200,100], 5000, 1, 1)
        testPacker.addBin(testBin)
        with self.assertRaises(ZeroDivisionError):
            testPacker.pack(False, True, False, False, 0.75, [])
        self.assertEqual(retStr(testBin), [])

        # No Bin Single Item
        testPacker = Packer()
        testItem = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testPacker.addItem(testItem)
        with self.assertRaises(ValueError):
            testPacker.pack(False, True, False, False, 0.75, [])

        # No Bin No Item
        testPacker = Packer()
        with self.assertRaises(ValueError):
            testPacker.pack(False, True, False, False, 0.75, [])
                                        
                                
        """
        any combination of [True, True, ...] will not work
        """
        testPacker = Packer()
        testBin1 = Bin("testBin1", [100,200,100], 5000, 1, 1)
        testBin2 = Bin("testBin2", [1000,2000,3000], 5000, 1, 1)
        testItem1 = Item("1","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testItem2 = Item("2","test","cube", [500,600,50], 5, 2, 400, True, "red")
        testItem3 = Item("3","test","cube", [23,15,10], 20, 2, 400, True, "blue")
        testItem4 = Item("4","test","cube", [1200,1200,2320], 20, 2, 400, True, "yellow")
        testItem5 = Item("5","test","cube", [300,200,400], 20, 2, 400, True, "purple")
        testItem6 = Item("6","test","cube", [100,100,100], 20, 2, 400, True, "green")
        testPacker.addBin(testBin1)
        testPacker.addBin(testBin2)
        testPacker.addItem(testItem1)
        testPacker.addItem(testItem2)
        testPacker.addItem(testItem3)
        testPacker.addItem(testItem5)
        testPacker.addItem(testItem4)
        testPacker.addItem(testItem6)
        with self.assertRaises(ZeroDivisionError):
            testPacker.pack(True, True, True, True, 0.75, [])
        self.assertEqual(retStr(testBin1), [])
        self.assertEqual(retStr(testBin2), ['5', '2', '6', '1', '3'])


if __name__ == '__main__':
    unittest.main()