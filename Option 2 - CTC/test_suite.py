from test_folder import get_limit_number_of_decimals, set_to_decimal, rect_intersect, intersect, stack, Bin, Item, Packer, Axis
import unittest
from decimal import Decimal
import decimal

'''
OLD
    WIDTH = 0
    HEIGHT = 1
    DEPTH = 2

NEW
    LENGTH = 0
    WIDTH = 1
    HEIGHT = 2
'''

class TestAux(unittest.TestCase):

    # Testing Auxiliary Methods (Almost identical to option 1)
    def test_get_limit_number_of_decimals(self):
        self.assertEqual(get_limit_number_of_decimals(3), 1.000)
        self.assertEqual(get_limit_number_of_decimals(0), 1)
        self.assertEqual(get_limit_number_of_decimals(20), 1.00000000000000000000)
        self.assertEqual(get_limit_number_of_decimals(-5), 1)

        with self.assertRaises(TypeError):
            get_limit_number_of_decimals(1.5)
            get_limit_number_of_decimals('a')
            get_limit_number_of_decimals(False)
    
    def test_set_to_decimal(self):
        self.assertEqual(set_to_decimal(4, 3), 4.000)
        self.assertEqual(set_to_decimal(4, 0), 4)
        self.assertEqual(set_to_decimal(4, 20), 4.00000000000000000000)
        self.assertEqual(set_to_decimal(4, -5), 4)

        with self.assertRaises(TypeError):
            set_to_decimal(4, 1.5)
            set_to_decimal(4, 'a')
            set_to_decimal(4, True)
    
    def test_rect_intersect(self):
        #name, length, width, height, weight
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 5, 10, 10, 20)

        #default start position     
        START_POSITION = [0, 0, 0] 

        with self.assertRaises(AttributeError):
            # only objects of item class have the position attribute
            rect_intersect(32, testItem2, Axis.LENGTH, Axis.WIDTH)
            rect_intersect('a', testItem2, Axis.LENGTH, Axis.WIDTH)
            rect_intersect(False, testItem2, Axis.LENGTH, Axis.WIDTH)
            rect_intersect(testItem1, 32, Axis.LENGTH, Axis.WIDTH)
            rect_intersect(testItem1, 'a', Axis.LENGTH, Axis.WIDTH)
            rect_intersect(testItem1, False, Axis.LENGTH, Axis.WIDTH)

        with self.assertRaises(IndexError):
            # position array holds 3 values, x, y and z. Any index above 2 is out of range
            rect_intersect(testItem1, testItem2, 11, Axis.WIDTH)
            rect_intersect(testItem1, testItem2, -11, Axis.WIDTH)
            rect_intersect(testItem1, testItem2, Axis.LENGTH, 11)
            rect_intersect(testItem1, testItem2, Axis.LENGTH, -11)

        with self.assertRaises(TypeError):
            rect_intersect(testItem1, testItem2, "hello", Axis.WIDTH)
            rect_intersect(testItem1, testItem2, Axis.LENGTH, "hello")
            
        # All 3 planes intersecting
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.WIDTH), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), True)

        # Changing position of item 2 (1 plane intersecting)
        #                     W   H  D
        testItem2.position = [30, 0, 0]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.WIDTH), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), False)

        # Changing position of item 2 (1 plane intersecting)
        #                     W  H   D
        testItem2.position = [0, 30, 0]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), True)

        # Changing position of item 2 (1 plane intersecting)
        #                     W  H  D
        testItem2.position = [0, 0, 30]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), True)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), False)

        # Changing position of item 2 (no planes intersecting)
        #                     W   H   D
        testItem2.position = [50, 50, 50]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.WIDTH), False)
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.HEIGHT, Axis.LENGTH), False)
    
    def test_intersect(self):
        #name, length, width, height, weight
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 5, 10, 10, 20)

        #default start position     
        START_POSITION = [0, 0, 0] 

        with self.assertRaises(AttributeError):
            # only objects of item class have the position attribute
            intersect(32, testItem2)
            intersect('a', testItem2)
            intersect(False, testItem2)
            intersect(testItem1, 32)
            intersect(testItem1, 'a')
            intersect(testItem1, False)
            

        # All 3 planes intersecting
        self.assertEqual(intersect(testItem1, testItem2), True)


        # Changing position of item 2 width
        #                     W  H  D
        testItem2.position = [9, 0, 0]
        self.assertEqual(intersect(testItem1, testItem2), True)

        testItem2.position = [10, 0, 0]
        self.assertEqual(intersect(testItem1, testItem2), False)

        testItem2.position = [20, 0, 0]
        self.assertEqual(intersect(testItem1, testItem2), False)


        # Changing position of item 2 height
        #                     W  H   D
        testItem2.position = [0, 19, 0]
        self.assertEqual(intersect(testItem1, testItem2), True)

        testItem2.position = [0, 20, 0]
        self.assertEqual(intersect(testItem1, testItem2), False)

        testItem2.position = [0, 100, 0]
        self.assertEqual(intersect(testItem1, testItem2), False)


        # Changing position of item 2 depth
        #                     W  H  D
        testItem2.position = [0, 0, 29]
        self.assertEqual(intersect(testItem1, testItem2), True)

        testItem2.position = [0, 0, 30]
        self.assertEqual(intersect(testItem1, testItem2), False)

        testItem2.position = [0, 0, 100]
        self.assertEqual(intersect(testItem1, testItem2), False)


        # Changing position of item 2 for all dimensions
        #                     W   H   D
        testItem2.position = [9, 19, 29]
        self.assertEqual(intersect(testItem1, testItem2), True)

        testItem2.position = [10, 20, 30]
        self.assertEqual(intersect(testItem1, testItem2), False)

        testItem2.position = [100, 100, 100]
        self.assertEqual(intersect(testItem1, testItem2), False)
    
    def test_stack(self):
        # Both items identical
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 20, 30, 50)

        # Method to return string value of list of items
        def retStr(lst):
            if isinstance(lst, list):
                res = []
                for item in lst:
                    res.append(item.string())
                return res
            else:
                return lst.string()
            

        self.assertEqual(retStr(stack(testItem1,testItem2)), ['testItem1testItem2(20x20x30, weight: 100) pos([0, 0, 0]) rt(0) vol(12000.000)', 'testItem1testItem2(10x40x30, weight: 100) pos([0, 0, 0]) rt(0) vol(12000.000)', 'testItem1testItem2(10x20x60, weight: 100) pos([0, 0, 0]) rt(0) vol(12000.000)'])

        # Identical length and width
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 20, 20, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2(10x20x50, weight: 100) pos([0, 0, 0]) rt(0) vol(10000.000)')

        # Identical length and height
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 5, 30, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2(10x25x30, weight: 100) pos([0, 0, 0]) rt(0) vol(7500.000)')

        # Identical height and width
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 40, 20, 30, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2(50x20x30, weight: 100) pos([0, 0, 0]) rt(0) vol(30000.000)')

        # Identical length
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 70, 15, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1(10x20x30, weight: 50) pos([0, 0, 0]) rt(0) vol(6000.000)')

        # Identical width
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 40, 20, 100, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1(10x20x30, weight: 50) pos([0, 0, 0]) rt(0) vol(6000.000)')

        # Identical height
        testItem1 = Item('testItem1', 10, 23, 30, 50)
        testItem2 = Item('testItem2', 40, 20, 30, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1(10x23x30, weight: 50) pos([0, 0, 0]) rt(0) vol(6900.000)')

        # Nothing Identical
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 40, 50, 60, 50)

        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1(10x20x30, weight: 50) pos([0, 0, 0]) rt(0) vol(6000.000)')

        with self.assertRaises(AttributeError):
            stack('testItem1', testItem2)
            stack(testItem1, 'False')
            stack(True, testItem2)  
            stack(testItem1, False)  
            stack(1, testItem2)
            stack(testItem1, 2)
    
    # Testing Item Class Methods

    def test_itemConstructor(self):
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        self.assertEqual(testItem1.name, 'testItem1')
        self.assertEqual(testItem1.length, 10)
        self.assertEqual(testItem1.width, 20)
        self.assertEqual(testItem1.height, 30)
        self.assertEqual(testItem1.weight, 50)

        # Attributes not affected by constructor
        self.assertEqual(testItem1.rotation_type, 0)
        self.assertEqual(testItem1.position, [0,0,0])
        self.assertEqual(testItem1.number_of_decimals, 3)

        # Different name types
        testItem1 = Item(34, 10, 20, 30, 50)
        self.assertEqual(testItem1.name, 34)

        testItem1 = Item(False, 10, 20, 30, 50)
        self.assertEqual(testItem1.name, False)

        testItem2 = Item('testItem2', 30, 30, 30, 90)
        testItem1 = Item(testItem2, 10, 20, 30, 50)
        
        with self.assertRaises(AssertionError):
            # address of item always changes
            self.assertEqual(testItem1.name, '<test_folder.item.Item object at 0x000001B90D9E7EB0>(10x20x30')

        # Incorrect Data type measurements
        testItem1 = Item('testItem1', '10', 20, 30, 50)
        self.assertEqual(testItem1.length, '10')

        testItem1 = Item('testItem1', 10, '20', 30, 50)
        self.assertEqual(testItem1.width, '20')
        
        testItem1 = Item('testItem1', 10, 20, True, 50)
        self.assertEqual(testItem1.height, True)

        testItem1 = Item('testItem1', 10, 20, 30, False)
        self.assertEqual(testItem1.weight, False)
 
    def test_itemFormatNumbers(self):
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        
        testItem1.format_numbers(5)
        self.assertEqual(testItem1.length, 10.00000)
        self.assertEqual(testItem1.width, 20.00000)
        self.assertEqual(testItem1.height, 30.00000)
        self.assertEqual(testItem1.weight, 50.00000)
        self.assertEqual(testItem1.number_of_decimals, 5)

        testItem1.format_numbers(-5)
        self.assertEqual(testItem1.length, 10)
        self.assertEqual(testItem1.width, 20)
        self.assertEqual(testItem1.height, 30)
        self.assertEqual(testItem1.weight, 50)
        self.assertEqual(testItem1.number_of_decimals, -5)

        testItem1.format_numbers(0)
        self.assertEqual(testItem1.length, 10)
        self.assertEqual(testItem1.width, 20)
        self.assertEqual(testItem1.height, 30)
        self.assertEqual(testItem1.weight, 50)
        self.assertEqual(testItem1.number_of_decimals, 0)

        testItem1.format_numbers(20)
        self.assertEqual(testItem1.length, 10.00000000000000000000)
        self.assertEqual(testItem1.width, 20.00000000000000000000)
        self.assertEqual(testItem1.height, 30.00000000000000000000)
        self.assertEqual(testItem1.weight, 50.00000000000000000000)
        self.assertEqual(testItem1.number_of_decimals, 20)
    
    def test_itemGetVolume(self):
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        self.assertEqual(testItem1.get_volume(), 6000.000)

        # Non-integer values
        testItem1 = Item('testItem1', 10.5, 20.34, 30.5342, 50)
        self.assertEqual(testItem1.get_volume(), Decimal('6521.189'))

        # Non-numeric values
        testItem1 = Item('testItem1', '10', False, 30, 50)
        with self.assertRaises(decimal.InvalidOperation):
            self.assertEqual(testItem1.get_volume(), 6000.000)
    
    def test_itemGetDimension(self):
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        self.assertEqual(testItem1.get_dimension(), [10,20,30])

        testItem1 = Item('testItem1', 10.7, 20.65, 30.655, 50)
        self.assertEqual(testItem1.get_dimension(), [10.7,20.65,30.655])

        testItem1 = Item('testItem1', '10', False, 30, 50)
        self.assertEqual(testItem1.get_dimension(), ['10',False,30])

    def test_itemString(self):
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        self.assertEqual(testItem1.string(), 'testItem1(10x20x30, weight: 50) pos([0, 0, 0]) rt(0) vol(6000.000)')

        testItem1 = Item(43, 10.6, 204.5, 30.34, 5043)
        self.assertEqual(testItem1.string(), '43(10.6x204.5x30.34, weight: 5043) pos([0, 0, 0]) rt(0) vol(65768.018)')

        testItem1 = Item(True, 10, 20, 30, 50)
        self.assertEqual(testItem1.string(), 'True(10x20x30, weight: 50) pos([0, 0, 0]) rt(0) vol(6000.000)')

        # Invalid measurements
        testItem1 = Item('testItem1', '10', True, 30, 50)
        with self.assertRaises(decimal.InvalidOperation):
            self.assertEqual(testItem1.string(), 'testItem1(10x20x30, weight: 50) pos([0, 0, 0]) rt(0) vol(6000.000)')

    # Testing Bin Class Methods

    def test_binConstructor(self):
        testBin = Bin(300, 100, 110, 120, 400)

        self.assertEqual(testBin.size, 300) 
        self.assertEqual(testBin.length, 100)
        self.assertEqual(testBin.width, 110)
        self.assertEqual(testBin.height, 120)
        self.assertEqual(testBin.capacity, 400)

        # Not affected by constructor
        self.assertEqual(testBin.total_items, 0) 
        self.assertEqual(testBin.items, []) 
        self.assertEqual(testBin.unplaced_items, []) 
        self.assertEqual(testBin.unfitted_items, []) 
        self.assertEqual(testBin.number_of_decimals, 3) 

        testBin = Bin('300', 100, 110, 120, 400)
        self.assertEqual(testBin.size, '300') 

        testBin = Bin(300, False, 110, 120, 400)
        self.assertEqual(testBin.length, False) 

        testBin = Bin(300, 100, '110', 120, 400)
        self.assertEqual(testBin.width, '110') 

        testBin = Bin(300, 100, 110, True, 400)
        self.assertEqual(testBin.height, True) 

        testBin = Bin(300, 100, 110, 120, '400')
        self.assertEqual(testBin.capacity, '400') 
 
    def test_binFormatNumbers(self):
        testBin = Bin(300, 100, 110, 120, 400)
        
        testBin.format_numbers(5)
        self.assertEqual(testBin.size, 300.00000)
        self.assertEqual(testBin.length, 100.00000)
        self.assertEqual(testBin.width, 110.00000)
        self.assertEqual(testBin.height, 120.00000)
        self.assertEqual(testBin.capacity, 400.00000)
        self.assertEqual(testBin.number_of_decimals, 5)

        testBin.format_numbers(-5)
        self.assertEqual(testBin.size, 300)
        self.assertEqual(testBin.length, 100)
        self.assertEqual(testBin.width, 110)
        self.assertEqual(testBin.height, 120)
        self.assertEqual(testBin.capacity, 400)
        self.assertEqual(testBin.number_of_decimals, -5)

        testBin.format_numbers(0)
        self.assertEqual(testBin.size, 300)
        self.assertEqual(testBin.length, 100)
        self.assertEqual(testBin.width, 110)
        self.assertEqual(testBin.height, 120)
        self.assertEqual(testBin.capacity, 400)
        self.assertEqual(testBin.number_of_decimals, 0)

        testBin.format_numbers(20)
        self.assertEqual(testBin.size, 300.00000000000000000000)
        self.assertEqual(testBin.length, 100.00000000000000000000)
        self.assertEqual(testBin.width, 110.00000000000000000000)
        self.assertEqual(testBin.height, 120.00000000000000000000)
        self.assertEqual(testBin.capacity, 400.00000000000000000000)
        self.assertEqual(testBin.number_of_decimals, 20)
    
    def test_binGetVolume(self):
        testBin = Bin(300, 100, 110, 120, 400)
        self.assertEqual(testBin.get_volume(), 1320000)

        testBin = Bin(300, 10.5, 50.25, 25.75, 400)
        self.assertEqual(testBin.get_volume(), Decimal('13586.344'))

        with self.assertRaises(decimal.InvalidOperation):
            testBin = Bin(300, '100', 110, 120, 400)
            testBin.get_volume()

            testBin = Bin(300, 100, True, 120, 400)
            testBin.get_volume()

            testBin = Bin(300, 100, 110, '120', 400)
            testBin.get_volume()
    
    def test_binGetTotalWeight(self):
        testBin = Bin(300, 100, 110, 120, 400)

        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 20, 25, 15, 100)

        self.assertEqual(testBin.get_total_weight(), 0)

        testBin.items.append(testItem2)

        self.assertEqual(testBin.get_total_weight(), 100)

        testBin.items.append(testItem1)

        self.assertEqual(testBin.get_total_weight(), 150)

        testBin.items.append('testItem1')

        with self.assertRaises(AttributeError):
            testBin.get_total_weight()
  
    def test_binGetFillingRatio(self):
        testBin = Bin(300, 100, 110, 120, 400)

        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 20, 25, 15, 100)

        self.assertEqual(testBin.get_filling_ratio(), 0)

        testBin.items.append(testItem2)

        self.assertEqual(testBin.get_filling_ratio(), Decimal('0.006'))

        testBin.items.append(testItem1)

        self.assertEqual(testBin.get_filling_ratio(), Decimal('0.010'))

        testBin.items.append('testItem1')

        with self.assertRaises(AttributeError):
            testBin.get_filling_ratio()

    def test_binCanHoldItemWithRotation(self):
        testBin = Bin(300, 100, 110, 120, 400)

        testItem1 = Item('testItem1', 10, 120, 30, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem1, [0,0,0]), [1,5])

        testItem1 = Item('testItem1', 10, 3000, 30, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem1, [0,0,0]), [])

        testItem1 = Item('testItem1', 110, 100, 120, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem1, [0,0,0]), [4])

        testItem1 = Item('testItem1', 10, 10, 10, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem1, [0,0,0]), [0,1,2,3,4,5])

        with self.assertRaises(AttributeError):
            self.assertEqual(testBin.can_hold_item_with_rotation('testItem1', [0,0,0]), [0,1,2,3,4,5])
    
    def test_binPutItem(self):
        testBin = Bin(300, 100, 110, 120, 400)

        testItem1 = Item('testItem1', 10, 120, 30, 50)
        self.assertEqual(testBin.put_item(testItem1, [0,0,0], [0,0,0]), True)

        testItem2 = Item('testItem2', 10, 120, 30, 50)
        self.assertEqual(testBin.put_item(testItem2, [10,120,30], [10,120,30]), False)

        testItem3 = Item('testItem3', 430, 120, 243, 50)
        self.assertEqual(testBin.put_item(testItem3, [10,120,30], [0,0,0]), False)

        testItem4 = Item('testItem4', 430, 120, 243, 50)
        self.assertEqual(testBin.put_item(testItem4, [10,120,30], [430,120,243]), False)
    
    def test_binString(self):
        testBin = Bin(300, 300, 300, 300, 400)

        # Before adding any items
        self.assertEqual(testBin.string(), '300(300x300x300, max_weight:400) vol(27000000.000) item_number(0) filling_ratio(0.000)')

        testItem1 = Item('testItem1', 10, 120, 30, 300)

        testBin.put_item(testItem1, [0,0,0], [0,0,0])

        # After adding items
        self.assertEqual(testBin.string(), '300(300x300x300, max_weight:400) vol(27000000.000) item_number(1) filling_ratio(0.001)')


    # Testing Packer Class Methods

    def test_packerConstructor(self):
        testPacker = Packer()

        self.assertEqual(testPacker.bins,[])
        self.assertEqual(testPacker.unplaced_items,[])
        self.assertEqual(testPacker.placed_items,[])
        self.assertEqual(testPacker.unfit_items,[])
        self.assertEqual(testPacker.total_items,0)
        self.assertEqual(testPacker.total_used_bins,0)
        self.assertEqual(testPacker.used_bins,[])
    
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

    def test_packerPackToBin(self):
        testPacker = Packer()
        testBin = Bin(2000, 300, 400, 200, 4000)
        testItem1 = Item('testItem1', 10, 10, 30, 50)
        testItem2 = Item('testItem2', 100, 10, 40, 50)
        testItem3 = Item('testItem3', 55, 120, 30, 50)
        testItem4 = Item('testItem4', 500, 500, 500, 50)

        testPacker.add_bin(testBin)
        testPacker.add_item(testItem1)
        testPacker.add_item(testItem2)
        testPacker.add_item(testItem3)
        testPacker.add_item(testItem4)

        # Method to return string value of list of items
        def retStr(lst):
            if isinstance(lst, list):
                res = []
                for item in lst:
                    res.append(item.string())
                return res
            else:
                return lst.string()
        
        testPacker.pack_to_bin(testBin, testItem1)
        self.assertEqual(retStr(testBin.items), ['testItem1(10x10x30, weight: 50) pos([0, 0, 0]) rt(0) vol(3000.000)'])

        testPacker.pack_to_bin(testBin, testItem2)
        self.assertEqual(retStr(testBin.items), ['testItem1(10x10x30, weight: 50) pos([0, 0, 0]) rt(0) vol(3000.000)', 'testItem2(100x10x40, weight: 50) pos([10, 0, 0]) rt(2) vol(40000.000)'])

        testPacker.pack_to_bin(testBin, testItem3)
        self.assertEqual(retStr(testBin.items), ['testItem1(10x10x30, weight: 50) pos([0, 0, 0]) rt(0) vol(3000.000)', 'testItem2(100x10x40, weight: 50) pos([10, 0, 0]) rt(2) vol(40000.000)', 'testItem3(55x120x30, weight: 50) pos([0, 10, 0]) rt(5) vol(198000.000)'])

        # Item4 should not be fitted into bin (too big)
        testPacker.pack_to_bin(testBin, testItem4)
        self.assertEqual(retStr(testBin.items), ['testItem1(10x10x30, weight: 50) pos([0, 0, 0]) rt(0) vol(3000.000)', 'testItem2(100x10x40, weight: 50) pos([10, 0, 0]) rt(2) vol(40000.000)', 'testItem3(55x120x30, weight: 50) pos([0, 10, 0]) rt(5) vol(198000.000)'])
        self.assertEqual(retStr(testBin.unfitted_items), ['testItem4(500x500x500, weight: 50) pos([0, 10, 120]) rt(5) vol(125000000.000)'])
    
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