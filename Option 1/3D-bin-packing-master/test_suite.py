#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer
import unittest

class TestAux(unittest.TestCase):
    def test_getLimitNumberOfDecimals(self):
        self.assertEqual(getLimitNumberOfDecimals(3), 1.000)
        self.assertEqual(getLimitNumberOfDecimals(0), 1)
        self.assertEqual(getLimitNumberOfDecimals(20), 1.00000000000000000000)
        self.assertEqual(getLimitNumberOfDecimals(-5), 1)

        # method has no way of dealing with float values
        # self.assertEqual(getLimitNumberOfDecimals(1.5), 1)

    def test_set2Decimal(self):
        self.assertEqual(set2Decimal(4, 4), 4.0000)

    def test_Item(self):
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")

        self.assertEqual(testItem.getMaxArea(), 200)
        self.assertEqual(testItem.getVolume(), 6000)

    def test_Packer(self):
        """
        Test to find out what sortBinding does and how it works
        """
        bin1 = Bin(partno='Bin', WHD=(589,243,259), max_weight=28080, corner=15, put_type= 1)
        item1 = Item(partno='toy', name='toy', typeof='cube', WHD=(85, 60, 60), weight=10, level=1, loadbear=100, updown=True, color='#FFFF37')
        item2 = Item(partno='pencil', name='pencil', typeof='cube', WHD=(85, 60, 60), weight=10, level=1, loadbear=100, updown=True, color='#FFFF37')
        item3 = Item(partno='shoes', name='shoes', typeof='cube', WHD=(85, 60, 60), weight=10, level=1, loadbear=100, updown=True, color='#FFFF37')
        testPacker = Packer()
        testPacker.addBin(bin1)
        testPacker.addItem(item1)
        testPacker.addItem(item2)
        testPacker.addItem(item3)

        bin = [('toy','shoes')]

        # add binding attribute REMOVE AFTERWARDS
        testPacker.binding = bin

        # Packer could have a proper string output
        # for i in testPacker.items:
        #     print (i.string())

        testPacker.sortBinding(bin)

        # for i in testPacker.items:
        #     print (i.string())



    
if __name__ == '__main__':
    unittest.main()