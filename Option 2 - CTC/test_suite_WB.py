from test_folder import get_limit_number_of_decimals, set_to_decimal, rect_intersect, intersect, stack, Bin, Item, Packer, Axis
import unittest
from decimal import Decimal
import decimal

"""
White Box Testing for Option 2, Janet's Algorithm
"""
class TestAux(unittest.TestCase):

    #                     #
    #  Auxiliary Methods  #
    #                     #

    # WB Done
    def test_get_limit_number_of_decimals(self):
        """
        Conditional Testing:-
        0 Conditions: 
        
        Path Coverage Testing:-
        100% 
        """
        # Positive number of decimals
        self.assertEqual(get_limit_number_of_decimals(3), 1.000)
    
    # WB Done
    def test_set_to_decimal(self):
        """
        Conditional Testing:-
        0 Conditions
        
        100% path coverage
        """
        # Float value with a custom number of decimals
        self.assertEqual(set_to_decimal(9.4231, 2), Decimal('9.42'))
    
    # WB Done
    def test_rect_intersect(self):
        """
        Conditional Testing:-
        2 conditions:
        'ix < (d1[x]+d2[x])/2' 
        'iy < (d1[y]+d2[y])/2'

        Path Coverage Testing:-
        100%
        """
        #                             L   W   H
        testItem1 = Item("testItem1", 10, 20, 30, 25)
        testItem2 = Item("testItem2", 5, 10, 10, 25)

        """
        2.5 < 7.5 ; True
        5 < 15    ; True
        """
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), True)
        
        """
        2.5 < 7.5 ; True
        140 < 60  ; False
        """
        testItem2 = Item("testItem2", 5, 100, 10, 25)
        testItem2.position = [0, 100, 0]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)


        """
        145 < 55  ; False
        5 < 15    ; True
        """
        testItem2 = Item("testItem2", 100, 10, 10, 25)
        testItem2.position = [100, 0, 0]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)


        """
        145 < 55  ; False
        140 < 60  ; False
        """
        testItem2 = Item("testItem2", 100, 100, 10, 25)
        testItem2.position = [100, 100, 0]
        self.assertEqual(rect_intersect(testItem1, testItem2, Axis.LENGTH, Axis.WIDTH), False)
    
    # WB Done
    def test_stack(self):
        """
        Conditional Testing:-
        Conditions:
        if (
            item1.length == item2.length and
            item1.width == item2.width and
            item1.height == item2.height
        ):
        elif ( 
            item1.length == item2.length and
            item1.width == item2.width and
            item1.height != item2.height
        ):
        elif (
            item1.length == item2.length and 
            item1.height == item2.height and
            item1.width != item2.width
        ):
        elif (
            item1.width == item2.width and
            item1.height == item2.height and
            item1.length != item2.length
        ):
        else:

        Path Coverage Testing:-
        100%
        """
        # Method to return string value of list of items
        def retStr(lst):
            if isinstance(lst, list):
                res = []
                for item in lst:
                    res.append(item.name)
                return res
            else:
                return lst.name

        """
        if (
            item1.length == item2.length and
            item1.width == item2.width and
            item1.height == item2.height
        ):
        """
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 20, 30, 50)
        self.assertEqual(retStr(stack(testItem1,testItem2)), ['testItem1testItem2', 'testItem1testItem2', 'testItem1testItem2'])

        """
        elif ( 
            item1.length == item2.length and
            item1.width == item2.width and
            item1.height != item2.height
        ):
        """
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 20, 20, 50)
        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2')

        """
        elif (
            item1.length == item2.length and 
            item1.height == item2.height and
            item1.width != item2.width
        ):
        """
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 10, 5, 30, 50)
        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2')

        """
        elif (
            item1.width == item2.width and
            item1.height == item2.height and
            item1.length != item2.length
        ):
        """
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 40, 20, 30, 50)
        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1testItem2')

        """
        Else:
        """
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 40, 50, 60, 50)
        self.assertEqual(retStr(stack(testItem1,testItem2)),'testItem1')
    
    #                      #
    #  Item Class Methods  #
    #                      #

    # WB Done
    def test_itemConstructor(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        # Valid constructor
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

    # WB Done
    def test_itemFormatNumbers(self):
        """
        Conditional Testing:-
        0 Conditions:
        
        100% Path coverage
        """
        # Valid use case
        testItem = Item("testItem", 10.23423, 20.3, 30, 25)
        testItem.format_numbers(3)
        self.assertEqual(testItem.length, Decimal('10.234'))
        self.assertEqual(testItem.width, Decimal('20.300'))
        self.assertEqual(testItem.height, Decimal('30.000'))
        self.assertEqual(testItem.weight, Decimal('25.000'))
        self.assertEqual(testItem.number_of_decimals, 3)
    
    # WB Done
    def test_itemGetVolume(self):
        """
        Conditional Testing:-
        0 Conditions:
        
        100% Patch coverage
        """
        # Valid Item Construction
        testItem = Item("testItem", 10, 20, 30, 25)
        self.assertEqual(testItem.get_volume(), 6000)

    # WB Done  
    def test_itemGetDimension(self):
        """
        Conditional Testing:-
        7 Conditions:
        if self.rotation_type == RotationType.RT_LWH:
        elif self.rotation_type == RotationType.RT_HLW:
        elif self.rotation_type == RotationType.RT_HWL:
        elif self.rotation_type == RotationType.RT_WHL:
        elif self.rotation_type == RotationType.RT_WLH:
        elif self.rotation_type == RotationType.RT_LHW:
        else:
            dimension = []

        Path Coverage Testing:-
        100%
        """

        # if self.rotation_type == RotationType.RT_LWH:
        testItem = Item("testItem", 10, 20, 30, 25)
        testItem.rotation_type = 0
        self.assertEqual(testItem.get_dimension(), [10,20,30])

        # elif self.rotation_type == RotationType.RT_HLW:
        testItem = Item("testItem", 10, 20, 30, 25)
        testItem.rotation_type = 1
        self.assertEqual(testItem.get_dimension(), [30,10,20])

        # elif self.rotation_type == RotationType.RT_HWL:
        testItem = Item("testItem", 10, 20, 30, 25)
        testItem.rotation_type = 2
        self.assertEqual(testItem.get_dimension(), [30,20,10])

        # elif self.rotation_type == RotationType.RT_WHL:
        testItem = Item("testItem", 10, 20, 30, 25)
        testItem.rotation_type = 3
        self.assertEqual(testItem.get_dimension(), [20,30,10])

        # elif self.rotation_type == RotationType.RT_WLH:
        testItem = Item("testItem", 10, 20, 30, 25)
        testItem.rotation_type = 4
        self.assertEqual(testItem.get_dimension(), [20,10,30])

        # elif self.rotation_type == RotationType.RT_LHW:
        testItem = Item("testItem", 10, 20, 30, 25)
        testItem.rotation_type = 5
        self.assertEqual(testItem.get_dimension(), [10,30,20])

        # else:
        testItem = Item("testItem", 10, 20, 30, 25)
        testItem.rotation_type = 6
        self.assertEqual(testItem.get_dimension(), [])
    
    # WB Done
    def test_itemString(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """

        # Valid Item construction
        testItem = Item("testItem", 10.23423, 20.3, 30, 25)
        self.assertEqual(testItem.string(), "testItem(10.23423x20.3x30, weight: 25) pos([0, 0, 0]) rt(0) vol(6232.646)")

    #                     #
    #  Bin Class Methods  #
    #                     #

    # WB Done
    def test_binConstructor(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        # Valid Bin Construction
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

    # WB Done
    def test_binFormatNumbers(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        # Integer number of decimals
        testbin = Bin(500, 100, 200, 100, 5000)
        testbin.format_numbers(3)
        self.assertEqual(testbin.size, Decimal('500.000'))
        self.assertEqual(testbin.length, Decimal('100.000'))
        self.assertEqual(testbin.width, Decimal('200.000'))
        self.assertEqual(testbin.height, Decimal('100.000'))
        self.assertEqual(testbin.capacity, Decimal('5000.000'))
        self.assertEqual(testbin.number_of_decimals, 3)
    
    # WB Done
    def test_binGetVolume(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        # Valid Bin Construction
        testbin = Bin(300, 100, 200, 100, 5000)
        self.assertEqual(testbin.get_volume(), 2000000)
    
    # WB Done
    def test_binGetTotalWeight(self):
        """
        Conditional Testing:-
        0 Conditions:

        Loop Testing:-
        1 Loop:
        for item in self.items:
            total_weight += item.weight

        Path Coverage Testing:-
        100%
        """

        """
        for item in self.items:
            total_weight += item.weight
        """
        testbin = Bin(300, 2000, 2000, 2000, 5000)
        testItem1 = Item("testItem1", 10, 20, 30, 10)
        testItem2 = Item("testItem2", 10, 20, 30, 25)
        testItem3 = Item("testItem3", 10, 20, 30, 11)
        testbin.items.append((testItem1))
        testbin.items.append((testItem2))
        testbin.items.append((testItem3))
        self.assertEqual(testbin.get_total_weight(), 46)
  
    # WB Done
    def test_binGetFillingRatio(self):
        """
        Conditional Testing:-
        0 Conditions:

        Loop Testing:-
        1 Loop:
        for item in self.items:
            total_filling_volume += item.get_volume()

        Path Coverage Testing:-
        100%
        """

        """
        for item in self.items:
            total_filling_volume += item.get_volume()
        """
        testBin = Bin(300, 100, 110, 120, 400)
        testItem1 = Item('testItem1', 10, 20, 30, 50)
        testItem2 = Item('testItem2', 20, 25, 15, 100)
        testItem3 = Item('testItem2', 50, 5, 20, 35)
        testBin.items.append(testItem1)
        testBin.items.append(testItem2)
        testBin.items.append(testItem3)
        self.assertEqual(testBin.get_filling_ratio(), Decimal('0.014'))

    # WB Done
    def test_binCanHoldItemWithRotation(self):
        """
        Conditional Testing:-
        5 Conditions:
        if (
                pivot[0] + dimension[0] <= self.length and 
                pivot[1] + dimension[1] <= self.width and 
                pivot[2] + dimension[2] <= self.height    
            ):
            if intersect(current_item_in_bin, item):
            if fit:
                if self.get_total_weight() + item.weight > self.capacity:
                else: 

        Path Coverage Testing:-
        100%
        """

        testBin = Bin(300, 100, 110, 120, 400)

        """
        if (
                pivot[0] + dimension[0] <= self.length and 
                pivot[1] + dimension[1] <= self.width and 
                pivot[2] + dimension[2] <= self.height    
            ): 
            if intersect(current_item_in_bin, item):
            if fit:
                if self.get_total_weight() + item.weight > self.capacity:
                else: 
                
        False, -, -, -, -
        """
        testItem = Item('testItem', 110, 120, 130, 50)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem, [0,0,0]), [])


        """
        if (
                pivot[0] + dimension[0] <= self.length and 
                pivot[1] + dimension[1] <= self.width and 
                pivot[2] + dimension[2] <= self.height    
            ): 
            if intersect(current_item_in_bin, item):
            if fit:
                if self.get_total_weight() + item.weight > self.capacity:
                else: 
                
        True, False, True, False, True
        """
        testItem1 = Item('testItem1', 10, 10, 10, 50)
        testItem2 = Item('testItem1', 10, 10, 10, 50)
        testBin.items.append(testItem1)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem2, [0,10,0]), [0, 1, 2, 3, 4, 5])
        

        """
        if (
                pivot[0] + dimension[0] <= self.length and 
                pivot[1] + dimension[1] <= self.width and 
                pivot[2] + dimension[2] <= self.height    
            ): 
            if intersect(current_item_in_bin, item):
            if fit:
                if self.get_total_weight() + item.weight > self.capacity:
                else: 
                
        True, False, True, True, False
        """
        testItem1 = Item('testItem1', 10, 10, 10, 50)
        testItem2 = Item('testItem1', 10, 10, 10, 500)
        testBin.items.append(testItem1)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem2, [0,10,0]), [])
        

        """
        if (
                pivot[0] + dimension[0] <= self.length and 
                pivot[1] + dimension[1] <= self.width and 
                pivot[2] + dimension[2] <= self.height    
            ): 
            if intersect(current_item_in_bin, item):
            if fit:
                if self.get_total_weight() + item.weight > self.capacity:
                else: 
                
        True, True, False, -, -
        """
        testItem1 = Item('testItem1', 10, 10, 10, 50)
        testItem2 = Item('testItem1', 10, 10, 10, 50)
        testBin.items.append(testItem1)
        self.assertEqual(testBin.can_hold_item_with_rotation(testItem2, [0,0,0]), [])
    
    # WB Done
    def test_binPutItem(self):
        """
        Conditional Testing:-
        4 Conditions:
        if not rotation_type_list:
        else:
        
        if rotation_type_number == 1: 
        else:

        """

        """
        if not rotation_type_list:
        else:
        
        if rotation_type_number == 1: 
        else:
        
        True, -, -, -
        """
        testBin = Bin(300, 100, 110, 120, 400)
        testItem = Item('testItem', 110, 120, 130, 50)
        testBin.put_item(testItem, [0, 0, 0], [0, 0, 0])
        self.assertEqual(testBin.total_items, 0)


        """
        if not rotation_type_list:
        else:
        
        if rotation_type_number == 1: 
        else:
        
        False, True, True, -
        """
        testBin = Bin(300, 100, 110, 120, 400)
        testItem = Item('testItem', 110, 100, 120, 50)
        testBin.put_item(testItem, [0, 0, 0], [0, 0, 0])
        self.assertEqual(testBin.total_items, 1)


        """
        if not rotation_type_list:
        else:
        
        if rotation_type_number == 1: 
        else:
        
        False, True, False, True
        """
        testBin = Bin(300, 100, 110, 120, 400)
        testItem = Item('testItem', 10, 10, 10, 50)
        testBin.put_item(testItem, [0, 0, 0], [0, 0, 0])
        self.assertEqual(testBin.total_items, 1)
    
    # WB Done
    def test_binString(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        # Valid Bin Construction
        testBin = Bin(300, 300, 300, 300, 400)
        self.assertEqual(testBin.string(), '300(300x300x300, max_weight:400) vol(27000000.000) item_number(0) filling_ratio(0.000)')

    # #                        #
    # #  Packer Class Methods  #
    # #                        #

    #
    def test_packerConstructor(self):
        pass
    
    #
    def test_packerAddBin(self):
        pass

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
        pass
            
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
        pass
     
    #
    def test_packerPivotList(self):
        pass
    
    #
    def test_packerChoosePivotPoint(self):
        pass

    #
    def test_packerPackToBin(self):
        pass
    
    #
    # def test_packerPack(self):
    #     pass
    



if __name__ == '__main__':
    unittest.main()