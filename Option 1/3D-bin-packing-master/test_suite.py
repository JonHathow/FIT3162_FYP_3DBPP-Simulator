#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import rectIntersect, intersect, getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer, Axis
import unittest

class TestAux(unittest.TestCase):
    
    # Auxiliary Methods
    def test_rectIntersect(self):
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")

        #default start position     
        START_POSITION = [0, 0, 0] 

        with self.assertRaises(AttributeError):
            # only objects of item class have the position attribute
            rectIntersect(32, testItem2, Axis.WIDTH, Axis.HEIGHT)
            rectIntersect('a', testItem2, Axis.WIDTH, Axis.HEIGHT)
            rectIntersect(False, testItem2, Axis.WIDTH, Axis.HEIGHT)
            rectIntersect(testItem1, 32, Axis.WIDTH, Axis.HEIGHT)
            rectIntersect(testItem1, 'a', Axis.WIDTH, Axis.HEIGHT)
            rectIntersect(testItem1, False, Axis.WIDTH, Axis.HEIGHT)

        with self.assertRaises(IndexError):
            # position array holds 3 values, x, y and z. Any index above 2 is out of range
            rectIntersect(testItem1, testItem2, 11, Axis.HEIGHT)
            rectIntersect(testItem1, testItem2, -11, Axis.HEIGHT)
            rectIntersect(testItem1, testItem2, Axis.WIDTH, 11)
            rectIntersect(testItem1, testItem2, Axis.WIDTH, -11)

        with self.assertRaises(TypeError):
            rectIntersect(testItem1, testItem2, "hello", Axis.HEIGHT)
            rectIntersect(testItem1, testItem2, Axis.WIDTH, "hello")
            
        # All 3 planes intersecting
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), True)

        # Changing position of item 2 (1 plane intersecting)
        #                     W   H  D
        testItem2.position = [30, 0, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), False)

        # Changing position of item 2 (1 plane intersecting)
        #                     W  H   D
        testItem2.position = [0, 30, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), True)

        # Changing position of item 2 (1 plane intersecting)
        #                     W  H  D
        testItem2.position = [0, 0, 30]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), False)

        # Changing position of item 2 (no planes intersecting)
        #                     W   H   D
        testItem2.position = [50, 50, 50]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.HEIGHT), False)
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.DEPTH, Axis.WIDTH), False)

    def test_intersect(self):
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [20,10,10], 25, 2, 400, False, "orange")

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
        #                     W   H  D
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

    def test_getLimitNumberOfDecimals(self):
        self.assertEqual(getLimitNumberOfDecimals(3), 1.000)
        self.assertEqual(getLimitNumberOfDecimals(0), 1)
        self.assertEqual(getLimitNumberOfDecimals(20), 1.00000000000000000000)
        self.assertEqual(getLimitNumberOfDecimals(-5), 1)

        with self.assertRaises(TypeError):
            getLimitNumberOfDecimals(1.5)
            getLimitNumberOfDecimals('a')

    def test_set2Decimal(self):
        self.assertEqual(set2Decimal(4, 3), 4.000)
        self.assertEqual(set2Decimal(4, 0), 4)
        self.assertEqual(set2Decimal(4, 20), 4.00000000000000000000)
        self.assertEqual(set2Decimal(4, -5), 4)

        with self.assertRaises(TypeError):
            set2Decimal(4, 1.5)
            set2Decimal(4, 'a')

    # Main Methods
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