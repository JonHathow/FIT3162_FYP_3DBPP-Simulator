#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import rectIntersect, intersect, getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer, Axis
from decimal import Decimal
import decimal
import unittest
import numpy as np

class TestAux(unittest.TestCase):
    
    def test_putItemVariation(self):
        return
    
    def test_pack2Bin(self):
        """
        variation = [if/elif swap]
        """

        #print bin items
        def retStr(bin):
            res = []
            for item in bin.items:
                if item.name != 'corner':
                    res.append(item.partno)
            return res
        
        # No variation
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
        print(retStr(testBin1))

        # Yes Variation
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
        testPacker1.pack2Bin(testBin1, testItem1, True, False, 0, [True])
        print(retStr(testBin1))
        

    def test_packVariation(self):
        """
        Variation = [gravityCenter, distribute_items]
        """

        #print bin items
        def retStr(bin):
            res = []
            for item in bin.items:
                if item.name != 'corner':
                    res.append(item.partno)
            return res
        
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

        # Variation default is false, this has gravity distribution
        testPacker1.pack(False,True,False,True,0.75,[])

        # print(retStr(testBin1))
        # self.assertEqual(retStr(testBin1), ['4', '2', '3', '1', '5'])

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

        # Variation is true, this ignores gravity distribution
        testPacker1.pack(False,True,False,True,0.75,[], True)

        # print(retStr(testBin1))
        # self.assertEqual(retStr(testBin1), ['4', '2', '3', '1', '5'])
    

if __name__ == '__main__':
    unittest.main()