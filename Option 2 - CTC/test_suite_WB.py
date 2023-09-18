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

    def test_get_limit_number_of_decimals(self):
        pass
    
    def test_set_to_decimal(self):
        pass
    
    def test_rect_intersect(self):
        pass
    
    def test_stack(self):
        pass
    
    #                      #
    #  Item Class Methods  #
    #                      #

    def test_itemConstructor(self):
        pass
        
    def test_itemGetDimension(self):
        pass

    def test_itemString(self):
        pass

    #                     #
    #  Bin Class Methods  #
    #                     #

    def test_binConstructor(self):
        pass
        
    def test_binFormatNumbers(self):
        pass
    
    def test_binGetVolume(self):
        pass
    
    def test_binGetTotalWeight(self):
        pass
  
    def test_binGetFillingRatio(self):
       pass

    def test_binCanHoldItemWithRotation(self):
        pass
    
    def test_binPutItem(self):
        pass
    
    def test_binString(self):
        pass

    #                        #
    #  Packer Class Methods  #
    #                        #

    def test_packerConstructor(self):
        pass
    
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

    def test_packerPivotDict(self):
        pass
     
    def test_packerPivotList(self):
        pass
    
    def test_packerChoosePivotPoint(self):
        pass

    def test_packerPackToBin(self):
        pass
    
    def test_packerPack(self):
        pass
    



if __name__ == '__main__':
    unittest.main()