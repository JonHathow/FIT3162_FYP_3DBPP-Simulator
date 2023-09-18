from test_folder import Bin, Item, Packer, Axis
from test_folder.auxiliary_methods import get_limit_number_of_decimals, set_to_decimal, rect_intersect, intersect, stack
import unittest
from decimal import Decimal
import decimal


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
    def test_aux_rect_intersect(self):
        testItem1 = Item("test1", 10, 20, 30, 25)
        testItem2 = Item("test2", 20, 10, 10, 25)


                                        #                #
                                        # Positive Cases #
                                        #                #

        # 2 Items that intersect on all planes
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), True)

        # 2 Items that intersect on W & H planes
        #                     L   W  H
        testItem2.position = [30, 0, 0]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), False)

        # 2 Items that intersect on L & H planes
        #                     L  W   H
        testItem2.position = [0, 30, 0]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), True)

        # 2 Items that intersect on L & W planes
        #                     L  W  H
        testItem2.position = [0, 0, 40]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), False)

        # One Item Inside Another
        #                     L    W  H
        testItem2.position = [2.5, 5, 10]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), True)


                                        #                #
                                        #   Edge Cases   #
                                        #                #


        # 2 Items barely do not intersect at the edges
        #                     L   W   H
        testItem2.position = [10, 20, 30]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), False)

        # 2 Items barely intersect at the edges
        #                     L  W   H
        testItem2.position = [9, 19, 29]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), True)


                                        #                #
                                        # Negative Cases #
                                        #                #


        # 2 Items that do not intersect
        #                     L   W   H
        testItem2.position = [50, 50, 50]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), False)

        # Zero-Dimensional Item
        testItem1 = Item('test1', 0, 0, 0, 0.0)
        #                     L  W  H
        testItem2.position = [0, 0, 0]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)


        # Invalid Item types
        with self.assertRaises(AttributeError):
            # only objects of item class have the position attribute
            rect_intersect(32, testItem2, Axis.WIDTH, Axis.HEIGHT)
            rect_intersect('a', testItem2, Axis.WIDTH, Axis.HEIGHT)
            rect_intersect(False, testItem2, Axis.WIDTH, Axis.HEIGHT)
            rect_intersect(testItem1, 32, Axis.WIDTH, Axis.HEIGHT)
            rect_intersect(testItem1, 'a', Axis.WIDTH, Axis.HEIGHT)
            rect_intersect(testItem1, False, Axis.WIDTH, Axis.HEIGHT)

        # Invalid Dimension Values
        with self.assertRaises(IndexError):
            # position array holds 3 values, x, y and z. Any index above 2 is out of range
            rect_intersect(testItem1, testItem2, 11, Axis.HEIGHT)
            rect_intersect(testItem1, testItem2, -11, Axis.HEIGHT)
            rect_intersect(testItem1, testItem2, Axis.WIDTH, 11)
            rect_intersect(testItem1, testItem2, Axis.WIDTH, -11)

        # Invalid Dimension Types
        with self.assertRaises(TypeError):
            rect_intersect(testItem1, testItem2, "hello", Axis.HEIGHT)
            rect_intersect(testItem1, testItem2, Axis.WIDTH, "hello")

    # BB Done
    def test_aux_intersect(self):
        testItem1 = Item("test1", 10, 20, 30, 25)
        testItem2 = Item("test2", 20, 10, 10, 25)

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
    def test_aux_get_limit_number_of_decimals(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Positive number of decimals
        self.assertEqual(get_limit_number_of_decimals(3), 1.000)

        # Zero decimals
        self.assertEqual(get_limit_number_of_decimals(0), 1)

        # Large number of decimals
        self.assertEqual(get_limit_number_of_decimals(20), 1.00000000000000000000)

        # Negative number of decimals
        self.assertEqual(get_limit_number_of_decimals(-5), 1)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #
                        
        # Invalid type for number of decimals
        with self.assertRaises(TypeError):
            get_limit_number_of_decimals(1.0)
            get_limit_number_of_decimals(2.4)
            get_limit_number_of_decimals('a')
            get_limit_number_of_decimals(False)

    # BB Done
    def test_aux_set_to_decimal(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Integer value 
        self.assertEqual(set_to_decimal(4, 3), Decimal('4.000'))

        # Float value 
        self.assertEqual(set_to_decimal(2.71828, 4), Decimal('2.7183'))

        # Negative value 
        self.assertEqual(set_to_decimal(-7, 2), Decimal('-7.00'))

        # Integer value with a large number of decimals
        self.assertEqual(set_to_decimal(4, 20), Decimal('4.00000000000000000000'))

        # Integer value with a negative number of decimals
        self.assertEqual(set_to_decimal(4, -5), Decimal('4'))

        # False value with a number of decimals
        self.assertEqual(set_to_decimal(False, 1), Decimal('0.0'))

        # String integer value
        self.assertEqual(set_to_decimal("4", 1), Decimal('4.0'))

        # String float value
        self.assertEqual(set_to_decimal("4.64", 3), Decimal('4.640'))
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid number of decimals type
        with self.assertRaises(TypeError):
            set_to_decimal(4, 1.5)
            set_to_decimal(4, 'a')

        # Invalid value type
        with self.assertRaises(decimal.InvalidOperation):
            self.assertEqual(set_to_decimal("Hello", 1), Decimal('Hello'))

    # BB Done
    def test_stack(self):
        
        # Method to return string value of list of items
        def retStr(lst):
            if isinstance(lst, list):
                res = []
                for item in lst:
                    res.append(item.name)
                return res
            else:
                return lst.name
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Identical Items
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 20, 30, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)), ['testItem1testItem2', 'testItem1testItem2', 'testItem1testItem2'])

        # Identical length and width
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 20, 20, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2')

        # Identical length and height
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 5, 30, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2')

        # Identical height and width
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 40, 20, 30, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2')

        # Identical length
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 70, 15, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1')

        # Identical width
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 40, 20, 100, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1')

        # Identical height
        testItem1 = Item('testItem1', 10, 23, 30, 50)
        testItem2 = Item('testItem2', 40, 20, 30, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1')

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Nothing Identical
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 40, 50, 60, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1')

                                        #                #
                                        # Negative Cases #
                                        #                #
        
        with self.assertRaises(AttributeError):
            stack('testItem1', testItem2)
            stack(testItem1, 'False')
            stack(True, testItem2)  
            stack(testItem1, False)  
            stack(1, testItem2)
            stack(testItem1, 2)
    
    #                      #
    #  Item Class Methods  #
    #                      #

    # BB Done
    def test_itemConstructor(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
                                        
        # Cylinder Item
        testItem = Item("testItem", 8, 8, 4, 0.3)
        self.assertEqual(testItem.name, 'testItem') 
        self.assertEqual(testItem.length, 8) 
        self.assertEqual(testItem.width, 8) 
        self.assertEqual(testItem.height, 4) 
        self.assertEqual(testItem.weight, 0.3) 
            # Attributes not affected by constructor
        self.assertEqual(testItem.rotation_type, 0)
        self.assertEqual(testItem.position, [0, 0, 0])
        self.assertEqual(testItem.number_of_decimals, 3)


        # Random input types
        testItem = Item(False, "WIDE", -34, 4.55, '0.3')
        self.assertEqual(testItem.name, False) 
        self.assertEqual(testItem.length, "WIDE") 
        self.assertEqual(testItem.width, -34) 
        self.assertEqual(testItem.height, 4.55) 
        self.assertEqual(testItem.weight, '0.3') 
            # Attributes not affected by constructor
        self.assertEqual(testItem.rotation_type, 0)
        self.assertEqual(testItem.position, [0, 0, 0])
        self.assertEqual(testItem.number_of_decimals, 3)
 
    # BB Done
    def test_itemFormatNumbers(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Integer number of decimals
        testItem = Item("testItem", 10.23423, 20.3, 30, 25)
        testItem.format_numbers(3)
        self.assertEqual(testItem.length, Decimal('10.234'))
        self.assertEqual(testItem.width, Decimal('20.300'))
        self.assertEqual(testItem.height, Decimal('30.000'))
        self.assertEqual(testItem.weight, Decimal('25.000'))
        self.assertEqual(testItem.number_of_decimals, 3)

        # Negative Integer number of decimals
        testItem = Item("testItem", 10.23423, 20.3, 30, 25)
        testItem.format_numbers(-2)
        self.assertEqual(testItem.length, Decimal('10'))
        self.assertEqual(testItem.width, Decimal('20'))
        self.assertEqual(testItem.height, Decimal('30'))
        self.assertEqual(testItem.weight, Decimal('25'))
        self.assertEqual(testItem.number_of_decimals, -2)

        # Large number of decimals
        testItem = Item("testItem", 10.23423, 20.3, 30, 25)
        testItem.format_numbers(10)
        self.assertEqual(testItem.length, Decimal('10.2342300000'))
        self.assertEqual(testItem.width, Decimal('20.3000000000'))
        self.assertEqual(testItem.height, Decimal('30.0000000000'))
        self.assertEqual(testItem.weight, Decimal('25.0000000000'))
        self.assertEqual(testItem.number_of_decimals, 10)

                                        #                #
                                        #   Edge Cases   #
                                        #                #
                                        
        # Number of decimals is 0
        testItem = Item("testItem", 10.23423, 20.3, 30, 25)
        testItem.format_numbers(0)
        self.assertEqual(testItem.length, Decimal('10'))
        self.assertEqual(testItem.width, Decimal('20'))
        self.assertEqual(testItem.height, Decimal('30'))
        self.assertEqual(testItem.weight, Decimal('25'))
        self.assertEqual(testItem.number_of_decimals, 0)

                                        #                #
                                        # Negative Cases #
                                        #                #
       
       # Invalid type of number of decimals
        testItem = Item("testItem", 10.23423, 20.3, 30, 25)
        with self.assertRaises(TypeError):
            testItem.format_numbers(2.3)
            testItem.format_numbers('a')

    # BB Done
    def test_itemGetVolume(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Item Construction
        testItem = Item("testItem", 10, 20, 30, 25)
        self.assertEqual(testItem.get_volume(), 6000)

        # Item Construction Random Data Types (except Dimensions)
        testItem = Item(34, 10, 20, 30, False)
        self.assertEqual(testItem.get_volume(), 6000)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Item Construction with 0 dimensions
        testItem = Item("testItem", 0, 0, 0, 25)
        self.assertEqual(testItem.get_volume(), 0)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #
        # Invalid Dimension Types
        testItem = Item("testItem", "10", True, 30, 25)
        with self.assertRaises(decimal.InvalidOperation):
            testItem.get_volume()
    
    # BB Done
    def test_itemGetDimension(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Item Construction
        testItem = Item("testItem", 10, 20, 30, 25)
        self.assertEqual(testItem.get_dimension(), [10,20,30])

        # Small Dimensions
        testItem = Item("testItem", 1, 2, 3, 25)
        self.assertEqual(testItem.get_dimension(), [1,2,3])

        # Large Dimensions
        testItem = Item("testItem", 150, 2000, 3320, 25)
        self.assertEqual(testItem.get_dimension(), [150,2000,3320])


                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Invalid Dimension Data Types
        testItem = Item("testItem", "10", False, 30.3, 25)
        self.assertEqual(testItem.get_dimension(), ["10",False,30.3])

    # BB Done
    def test_itemString(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Valid Item construction
        testItem = Item("testItem", 10.23423, 20.3, 30, 25)
        self.assertEqual(testItem.string(), "testItem(10.23423x20.3x30, weight: 25) pos([0, 0, 0]) rt(0) vol(6232.646)")

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Item construction with random values and datatypes (except dimensions)
        testItem = Item(34, 10.23423, 20.3, 30, False)
        self.assertEqual(testItem.string(), "34(10.23423x20.3x30, weight: False) pos([0, 0, 0]) rt(0) vol(6232.646)")
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Item construction with invalid dimension data types
        testItem = Item("testItem", "10.23423", False, (1,23), 25)
        with self.assertRaises(TypeError):
            testItem.string()

    #                     #
    #  Bin Class Methods  #
    #                     #

    # BB Done
    def test_binConstructor(self):

                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Bin Construction using default values
        testbin = Bin(300, 100, 200, 100, 5000)
        self.assertEqual(testbin.size, 300)
        self.assertEqual(testbin.length, 100)
        self.assertEqual(testbin.width, 200)
        self.assertEqual(testbin.height, 100)
        self.assertEqual(testbin.capacity, 5000)
            # Attributes not affected by constructor
        self.assertEqual(testbin.total_items, 0)
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unplaced_items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 3)

        # Random input types
        testbin = Bin(1, "100", 13.4, False, [2232,54])
        self.assertEqual(testbin.size, 1)
        self.assertEqual(testbin.length, "100")
        self.assertEqual(testbin.width, 13.4)
        self.assertEqual(testbin.height, False)
        self.assertEqual(testbin.capacity, [2232,54])
            # Attributes not affected by constructor
        self.assertEqual(testbin.total_items, 0)
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unplaced_items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 3)
                                        
    # BB Done
    def test_binFormatNumbers(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Integer number of decimals
        testbin = Bin(500, 100, 200, 100, 5000)
        testbin.format_numbers(3)
        self.assertEqual(testbin.size, Decimal('500.000'))
        self.assertEqual(testbin.length, Decimal('100.000'))
        self.assertEqual(testbin.width, Decimal('200.000'))
        self.assertEqual(testbin.height, Decimal('100.000'))
        self.assertEqual(testbin.capacity, Decimal('5000.000'))
        self.assertEqual(testbin.number_of_decimals, 3)

        # Negative number of decimals
        testbin.format_numbers(-1)
        self.assertEqual(testbin.size, Decimal('500'))
        self.assertEqual(testbin.length, Decimal('100'))
        self.assertEqual(testbin.width, Decimal('200'))
        self.assertEqual(testbin.height, Decimal('100'))
        self.assertEqual(testbin.capacity, Decimal('5000'))
        self.assertEqual(testbin.number_of_decimals, -1)

        # Large number of decimals
        testbin.format_numbers(10)
        self.assertEqual(testbin.size, Decimal('500.0000000000'))
        self.assertEqual(testbin.length, Decimal('100.0000000000'))
        self.assertEqual(testbin.width, Decimal('200.0000000000'))
        self.assertEqual(testbin.height, Decimal('100.0000000000'))
        self.assertEqual(testbin.capacity, Decimal('5000.0000000000'))
        self.assertEqual(testbin.number_of_decimals, 10)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Number of decimals is 0                     
        testbin.format_numbers(0)
        self.assertEqual(testbin.size, Decimal('500'))
        self.assertEqual(testbin.length, Decimal('100'))
        self.assertEqual(testbin.width, Decimal('200'))
        self.assertEqual(testbin.height, Decimal('100'))
        self.assertEqual(testbin.capacity, Decimal('5000'))
        self.assertEqual(testbin.number_of_decimals, 0)

                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid number of decimals data type
        with self.assertRaises(TypeError):
            testbin.format_numbers("potato")
            testbin.format_numbers(False)
            testbin.format_numbers(13.2)
    
    # BB Done
    def test_binGetVolume(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Valid Bin Construction
        testbin = Bin(300, 100, 200, 100, 5000)
        self.assertEqual(testbin.get_volume(), 2000000)

        # Bin Construction Random Data Types (except Dimensions)
        testbin = Bin("300", 100, 200, 100, False)
        self.assertEqual(testbin.get_volume(), 2000000)

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Bin Construction with 0 dimensions
        testbin = Bin(300, 0, 0, 0, 5000)
        self.assertEqual(testbin.get_volume(), 0)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid Dimension Types
        testbin = Bin(300, "100", False, (100, 22), 5000)
        with self.assertRaises(TypeError):
            testbin.get_volume()
    
    # BB Done
    def test_binGetTotalWeight(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # 3 Light Items
        testbin = Bin(300, 2000, 2000, 2000, 5000)
        testItem1 = Item("testItem1", 10, 20, 30, 10)
        testItem2 = Item("testItem2", 10, 20, 30, 25)
        testItem3 = Item("testItem3", 10, 20, 30, 11)
        testbin.items.append((testItem1))
        testbin.items.append((testItem2))
        testbin.items.append((testItem3))
        self.assertEqual(testbin.get_total_weight(), 46)

        # 3 Heavy Items
        testbin = Bin(300, 2000, 2000, 2000, 5000)
        testItem1 = Item("testItem1", 10, 20, 30, 1000)
        testItem2 = Item("testItem2", 10, 20, 30, 500)
        testItem3 = Item("testItem3", 10, 20, 30, 2500)
        testbin.items.append((testItem1))
        testbin.items.append((testItem2))
        testbin.items.append((testItem3))
        self.assertEqual(testbin.get_total_weight(), 4000)
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #
                                        
        # Empty Bin
        testbin = Bin(300, 2000, 2000, 2000, 5000)
        self.assertEqual(testbin.get_total_weight(), 0)

        # 1 Item
        testItem = Item("testItem", 10, 20, 30, 1000)
        testbin.items.append((testItem))
        self.assertEqual(testbin.get_total_weight(), 1000)
  
    # BB Done
    def test_binGetFillingRatio(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Multiple Large Items
        testBin = Bin(300, 4000, 2000, 10000, 400)
        testItem1 = Item('testItem1', 500, 1000, 3000, 200)
        testItem2 = Item('testItem2', 3000, 500, 5000, 400)
        testItem3 = Item('testItem3', 1000, 500, 1000, 100)
        testBin.items.append(testItem1)
        testBin.items.append(testItem2)
        testBin.items.append(testItem3)
        self.assertEqual(testBin.get_filling_ratio(), Decimal('0.119'))

        # Multiple Small Items
        testBin = Bin(300, 100, 110, 120, 400)
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 20, 25, 15, 100)
        testItem3 = Item('testItem2', 50, 5, 20, 35)
        testBin.items.append(testItem1)
        testBin.items.append(testItem2)
        testBin.items.append(testItem3)
        self.assertEqual(testBin.get_filling_ratio(), Decimal('0.014'))

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # 1 Item
        testBin = Bin(300, 100, 110, 120, 400)
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testBin.items.append(testItem1)
        self.assertEqual(testBin.get_filling_ratio(), Decimal('0.005'))

        # 0 Items
        testBin = Bin(300, 100, 110, 120, 400)
        self.assertEqual(testBin.get_filling_ratio(), Decimal('0'))

                                        #                #
                                        # Negative Cases #
                                        #                #

        # Invalid Item data types
        testBin.items.append('testItem1')
        with self.assertRaises(AttributeError):
            testBin.get_filling_ratio()

    # BB Done
    def test_binCanHoldItemWithRotation(self):

                                        #                #
                                        # Positive Cases #
                                        #                #

        testBin = Bin(300, 100, 110, 120, 400)

        # Item that can be placed with all orientations
        testItem1 = Item('testItem1', 10, 10, 10, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem1, [0,0,0]), [0,1,2,3,4,5])

        # Item that can be placed with multiple orientations
        testItem1 = Item('testItem1', 10, 120, 30, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem1, [0,0,0]), [1,5])

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Item that can be placed in 1 orientation
        testItem1 = Item('testItem1', 110, 100, 120, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem1, [0,0,0]), [4])

        # Item that can be placed in 0 orientations
        testItem1 = Item('testItem1', 10, 3000, 30, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem1, [0,0,0]), [])

                                        #                #
                                        # Negative Cases #
                                        #                #
        # Invalid Item Type
        with self.assertRaises(AttributeError):
            testBin.can_hold_item_with_rotation('testItem1', [0,0,0])
    
    # BB Done
    def test_binPutItem(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Item Fits
        testbin = Bin(300, 100, 200, 100, 5000)
        testItem = Item("testItem", 10, 20, 30, 25)
        testItem.format_numbers(3)
        testbin.put_item(testItem, [0,0,0], [0, 0, 0])
        self.assertEqual(testbin.total_items, 1)

        # Item fits only after rotation
        testbin = Bin(30, 30, 20, 20, 100)
        testItem = Item('testItem', 10, 25, 10, 1.5)
        testItem.format_numbers(3)
        testbin.put_item(testItem, [5, 5, 5], [0, 0, 0])
        self.assertEqual(testbin.total_items, 1) 
                                        
                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Two items that barely fit together
        testbin = Bin(3, 20, 10, 10, 100)
        testItem1 = Item('testItem1', 10, 10, 10, 2.0)
        testItem2 = Item('testItem2', 10, 10, 10, 2.0)
        testItem1.format_numbers(3)
        testItem2.format_numbers(3)
        testbin.put_item(testItem1, [0,0,0], [0, 0, 0])
        testbin.put_item(testItem2, [10,0,0], [0, 0, 0])
        self.assertEqual(testbin.total_items, 2)
                                        
                                        #                #
                                        # Negative Cases #
                                        #                #

        # Item doesn't fit
        testbin = Bin(3, 5, 5, 5, 100)
        testItem = Item('testItem', 15, 15, 15, 2.0)
        testItem.format_numbers(3)
        testbin.put_item(testItem, [0, 0, 0], [0, 0, 0])
        self.assertEqual(testbin.total_items, 0)

        # Item weight exceeds bin max weight
        testbin = Bin(1, 20, 20, 20, 2)
        testItem = Item('testItem', 10, 10, 10, 3.0)
        testItem.format_numbers(3)
        testbin.put_item(testItem, [5, 5, 5], [0, 0, 0])
        self.assertEqual(testbin.total_items, 0)

        # Invalid Pivot Type
        testItem = Item('testItem', 15, 15, 15, 2.0)
        testItem.format_numbers(3)
        with self.assertRaises(TypeError):
            testbin.put_item(testItem, ["hello", 23, False], [0, 0, 0])

        # Invalid distance_3d Type
        testItem = Item('testItem', 15, 15, 15, 2.0)
        testItem.format_numbers(3)
        with self.assertRaises(TypeError):
            testbin.put_item(testItem, [0, 0, 0], ["hello", 23, False])

        # Invalid Item Types
        testbin = Bin(300, 100, 200, 100, 5000)
        testItem.format_numbers(3)
        with self.assertRaises(AttributeError):
            testbin.put_item("hello", [80, 90, 80], [0, 0, 0])
            testbin.put_item(5, [80, 90, 80], [0, 0, 0])
            testbin.put_item(testbin, [80, 90, 80], [0, 0, 0])
    
    # BB Done
    def test_binString(self):
                                        #                #
                                        # Positive Cases #
                                        #                #

        # Valid Bin Construction
        testBin = Bin(300, 300, 300, 300, 400)
        self.assertEqual(testBin.string(), '300(300x300x300, max_weight:400) vol(27000000.000) item_number(0) filling_ratio(0.000)')

        # After adding two items
        testItem1 = Item('testItem1', 10, 10, 10, 20)
        testItem2 = Item('testItem2', 10, 10, 10, 20)
        testItem1.format_numbers(3)
        testItem2.format_numbers(3)
        testBin.put_item(testItem1, [0,0,0], [0,0,0])
        testBin.put_item(testItem2, [0,10,0], [0,0,0])
        self.assertEqual(testBin.string(), '300(300x300x300, max_weight:400) vol(27000000.000) item_number(2) filling_ratio(0.000)')

                                        #                #
                                        #   Edge Cases   #
                                        #                #

        # Random bin construction data types(except dimensions)
        testBin = Bin("454", 100, 200, 100, False)
        self.assertEqual(testBin.string(), '454(100x200x100, max_weight:False) vol(2000000.000) item_number(0) filling_ratio(0.000)')    

                                        #                #
                                        # Negative Cases #
                                        #                #

        # Item construction with invalid dimension data types
        testBin = Bin(1, "100", False, (2,33), 5000)
        with self.assertRaises(TypeError):
            testBin.string()

    #                        #
    #  Packer Class Methods  #
    #                        #

    # BB Done
    def test_packerConstructor(self):
                                        #                #
                                        # Positive Cases #
                                        #                #
        # Valid Construction
        testPacker = Packer()
        self.assertEqual(testPacker.bins,[])
        self.assertEqual(testPacker.unplaced_items,[])
        self.assertEqual(testPacker.placed_items,[])
        self.assertEqual(testPacker.unfit_items,[])
        self.assertEqual(testPacker.total_items,0)
        self.assertEqual(testPacker.total_used_bins,0)
        self.assertEqual(testPacker.used_bins,[])
        
    #
    def test_packerAddBin(self):
        testPacker = Packer()
        testBin = Bin(300, 300, 300, 300, 400)
        testPacker.add_bin(testBin)

        # Function to return string method of bin
        def retStr(bins):
            res = []
            for bin in bins:
                res.append(bin.string())
            return res
        
        self.assertEqual(retStr(testPacker.bins), ['300(300x300x300, max_weight:400) vol(27000000.000) item_number(0) filling_ratio(0.000)'])

        testBin2 = Bin(1000, 200, 500, 700, 20000)
        testPacker.add_bin(testBin2)
        self.assertEqual(retStr(testPacker.bins), ['300(300x300x300, max_weight:400) vol(27000000.000) item_number(0) filling_ratio(0.000)', '1000(200x500x700, max_weight:20000) vol(70000000.000) item_number(0) filling_ratio(0.000)'])
    
    #
    def test_packerAddItem(self):
        # Method to return string value of list of items
        def retStr(lst):
            if isinstance(lst, list):
                res = []
                for item in lst:
                    res.append(item.string())
                return res
            else:
                return lst.string()
            
        testPacker = Packer()
        testItem1 = Item('testItem1', 10, 120, 30, 120)
        testItem2 = Item('testItem2', 100, 10, 60, 100)
        self.assertEqual(testPacker.total_items, 0)
        self.assertEqual(retStr(testPacker.unplaced_items), [])

        testPacker.add_item(testItem1)
        self.assertEqual(testPacker.total_items, 1)
        self.assertEqual(retStr(testPacker.unplaced_items), ['testItem1(10x120x30, weight: 120) pos([0, 0, 0]) rt(0) vol(36000.000)'])
    
        testPacker.add_item(testItem2)
        self.assertEqual(testPacker.total_items, 2)
        self.assertEqual(retStr(testPacker.unplaced_items), ['testItem1(10x120x30, weight: 120) pos([0, 0, 0]) rt(0) vol(36000.000)', 'testItem2(100x10x60, weight: 100) pos([0, 0, 0]) rt(0) vol(60000.000)'])

        testPacker.add_item('testItem1')
        self.assertEqual(testPacker.total_items, 3)
        with self.assertRaises(AttributeError):
            retStr(testPacker.unplaced_items)

    #
    def test_packerPivotDict(self):
        testPacker = Packer()
        testBin = Bin(2000, 300, 400, 200, 4000)
        testItem1 = Item('testItem1', 10, 10, 30, 50)
        testItem2 = Item('testItem2', 10, 10, 30, 50)


        testPacker.add_bin(testBin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)

        self.assertEqual(testPacker.pivot_dict(testBin, testItem1), {})
        self.assertEqual(testPacker.pivot_dict(testBin, testItem2), {})

        testBin.put_item(testItem2, [0,0,0],[0,0,0])

        # There must be an item already in the bin
        self.assertEqual(testPacker.pivot_dict(testBin, testItem1), {(10, 0, 0): [290, 400, 200], (0, 10, 0): [300, 390, 200], (0, 0, 30): [300, 400, 170]})

        # Already in a bin
        self.assertEqual(testPacker.pivot_dict(testBin, testItem2), {})
     
    #
    def test_packerPivotList(self):
        testPacker = Packer()
        testBin = Bin(2000, 300, 400, 200, 4000)
        testItem1 = Item('testItem1', 10, 10, 30, 50)
        testItem2 = Item('testItem2', 10, 10, 30, 50)


        testPacker.add_bin(testBin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)

        self.assertEqual(testPacker.pivot_list(testBin, testItem1), [])
        self.assertEqual(testPacker.pivot_list(testBin, testItem2), [])

        testBin.put_item(testItem2, [0,0,0],[0,0,0])

        # There must be an item already in the bin
        self.assertEqual(testPacker.pivot_list(testBin, testItem1), [[10, 0, 0], [0, 10, 0], [0, 0, 30]])

        # Already in a bin
        self.assertEqual(testPacker.pivot_list(testBin, testItem2), [[10, 0, 0], [0, 10, 0], [0, 0, 30]])
    
    #
    def test_packerChoosePivotPoint(self):
        testPacker = Packer()
        testBin = Bin(2000, 300, 400, 200, 4000)
        testItem1 = Item('testItem1', 10, 10, 30, 50)
        testItem2 = Item('testItem2', 10, 10, 30, 50)


        testPacker.add_bin(testBin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)

        self.assertEqual(testPacker.choose_pivot_point(testBin, testItem1), False)
        self.assertEqual(testPacker.choose_pivot_point(testBin, testItem2), False)

        testBin.put_item(testItem2, [0,0,0],[0,0,0])

        # There must be an item already in the bin
        self.assertEqual(testPacker.choose_pivot_point(testBin, testItem1), [10, 0, 0])

        # Already in a bin
        self.assertEqual(testPacker.choose_pivot_point(testBin, testItem2), False)

    # def test_packerPackToBin(self):
    #     testPacker = Packer()
    #     testBin = Bin(2000, 300, 400, 200, 4000)
    #     testItem1 = Item('testItem1', 10, 10, 30, 50)
    #     testItem2 = Item('testItem2', 100, 10, 40, 50)
    #     testItem3 = Item('testItem3', 55, 120, 30, 50)
    #     testItem4 = Item('testItem4', 500, 500, 500, 50)

    #     testPacker.add_bin(testBin)
    #     testPacker.add_item(testItem1)
    #     testPacker.add_item(testItem2)
    #     testPacker.add_item(testItem3)
    #     testPacker.add_item(testItem4)

    #     # Method to return string value of list of items
    #     def retStr(lst):
    #         if isinstance(lst, list):
    #             res = []
    #             for item in lst:
    #                 res.append(item.string())
    #             return res
    #         else:
    #             return lst.string()
        
    #     testPacker.pack_to_bin(testBin, testItem1)
    #     self.assertEqual(retStr(testBin.items), ['testItem1(10x10x30, weight: 50) pos([0, 0, 0]) rt(0) vol(3000.000)'])

    #     testPacker.pack_to_bin(testBin, testItem2)
    #     self.assertEqual(retStr(testBin.items), ['testItem1(10x10x30, weight: 50) pos([0, 0, 0]) rt(0) vol(3000.000)', 'testItem2(100x10x40, weight: 50) pos([10, 0, 0]) rt(2) vol(40000.000)'])

    #     testPacker.pack_to_bin(testBin, testItem3)
    #     self.assertEqual(retStr(testBin.items), ['testItem1(10x10x30, weight: 50) pos([0, 0, 0]) rt(0) vol(3000.000)', 'testItem2(100x10x40, weight: 50) pos([10, 0, 0]) rt(2) vol(40000.000)', 'testItem3(55x120x30, weight: 50) pos([0, 10, 0]) rt(5) vol(198000.000)'])

    #     # Item4 should not be fitted into bin (too big)
    #     testPacker.pack_to_bin(testBin, testItem4)
    #     self.assertEqual(retStr(testBin.items), ['testItem1(10x10x30, weight: 50) pos([0, 0, 0]) rt(0) vol(3000.000)', 'testItem2(100x10x40, weight: 50) pos([10, 0, 0]) rt(2) vol(40000.000)', 'testItem3(55x120x30, weight: 50) pos([0, 10, 0]) rt(5) vol(198000.000)'])
    #     self.assertEqual(retStr(testBin.unfitted_items), ['testItem4(500x500x500, weight: 50) pos([0, 10, 120]) rt(5) vol(125000000.000)'])
    
    # def test_packerPack(self):
    #     #1 Bin
    #     testPacker = Packer()
    #     testBin = Bin(2000, 300, 400, 200, 4000)
    #     testItem1 = Item('testItem1', 10, 10, 30, 50)
    #     testItem2 = Item('testItem2', 100, 10, 40, 50)
    #     testItem3 = Item('testItem3', 55, 120, 30, 50)
    #     testItem4 = Item('testItem4', 500, 500, 500, 50)

    #     testPacker.add_bin(testBin)
    #     testPacker.add_item(testItem1)
    #     testPacker.add_item(testItem2)
    #     testPacker.add_item(testItem3)
    #     testPacker.add_item(testItem4)

    #     testPacker.pack()

    #     print("///////////////////////////////////////////////////////")

    #     # 2 Bins
    #     testPacker = Packer()
    #     testBin1 = Bin(2000, 300, 400, 200, 4000)
    #     testBin2 = Bin(2000, 1000, 600, 800, 4000)
    #     testItem1 = Item('testItem1', 10, 10, 30, 50)
    #     testItem2 = Item('testItem2', 100, 10, 40, 50)
    #     testItem3 = Item('testItem3', 55, 120, 30, 50)
    #     testItem4 = Item('testItem4', 500, 500, 500, 50)

    #     testPacker.add_bin(testBin1)
    #     testPacker.add_bin(testBin2)
    #     testPacker.add_item(testItem1)
    #     testPacker.add_item(testItem2)
    #     testPacker.add_item(testItem3)
    #     testPacker.add_item(testItem4)

    #     testPacker.pack()
    



if __name__ == '__main__':
    unittest.main()