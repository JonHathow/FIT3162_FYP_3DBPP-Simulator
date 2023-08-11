#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import rectIntersect, intersect, getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer, Axis
from decimal import Decimal
import decimal
import unittest
import numpy as np

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

    # Item Class Methods
    def test_itemConstructor(self):
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")

        '''
        self.partno = partno
        self.name = name
        self.typeof = typeof
        self.width = WHD[0]
        self.height = WHD[1]
        self.depth = WHD[2]
        self.weight = weight
        self.level = level
        self.loadbear = loadbear
        self.updown = updown if typeof == 'cube' else False
        self.color = color
        self.rotation_type = 0
        self.position = START_POSITION
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS
        '''
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

        # Testing if these attributes change correctly
        testItem.rotation_type = 5
        testItem.position = [-75,455,11]
        testItem.number_of_decimals = 4

        self.assertEqual(testItem.rotation_type, 5)
        self.assertEqual(testItem.position, [-75,455,11])
        self.assertEqual(testItem.number_of_decimals, 4)

    def test_itemFormatNumbers(self):
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25., 2, 400, True, "orange")

       
        with self.assertRaises(TypeError):
            testItem.formatNumbers(2.3)
            testItem.formatNumbers('a')

        testItem.formatNumbers(3)
        self.assertEqual(testItem.width, Decimal('10.234'))
        self.assertEqual(testItem.height, Decimal('20.300'))
        self.assertEqual(testItem.depth, Decimal('30.000'))
        self.assertEqual(testItem.weight, Decimal('25.000'))
        self.assertEqual(testItem.number_of_decimals, 3)

        testItem.formatNumbers(-2)
        self.assertEqual(testItem.width, Decimal('10'))
        self.assertEqual(testItem.height, Decimal('20'))
        self.assertEqual(testItem.depth, Decimal('30'))
        self.assertEqual(testItem.weight, Decimal('25'))
        self.assertEqual(testItem.number_of_decimals, -2)

    def test_itemString(self):
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25., 2, 400, True, "orange")

        # string should output more information ERROR
        # self.assertEqual(testItem.string(), 'partno:1, name:test, typeof:cube, dimensions:(10.23423x20.3x30), weight: 25.0, pos([0, 0, 0]), rt(0), vol(6233)')

        # Tests random data types of attributes
        testItem = Item("1",34 ,33, [10.23423,20.3,30], False, True, "400", 22, "orange")
        self.assertEqual(testItem.string(), "1(10.23423x20.3x30, weight: False) pos([0, 0, 0]) rt(0) vol(6233)")

    def test_itemGetVolume(self):
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getVolume(), 6000)

        testItem = Item(1,"test","cube", ["10",True,30], 25, 2, 400, True, "orange")

        with self.assertRaises(decimal.InvalidOperation):
            testItem.getVolume()

    def test_itemGetMaxArea(self):
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getMaxArea(), 600)

        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        self.assertEqual(testItem.getMaxArea(), 200)

        # incorrect dimensions
        with self.assertRaises(TypeError):
            testItem = Item(1,"test","cube", ["10",True,30], 25, 2, 400, True, "orange")
            testItem.getMaxArea()
            testItem = Item(1,"test","cube", ["10",True,30], 25, 2, 400, False, "orange")
            testItem.getMaxArea()

    def test_itemGetDimension(self):

        # rotation type must match as shown in constants.py
        #                                 W  H  D
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        #default rotation type is 0
        self.assertEqual(testItem.getDimension(), [10,20,30])

        testItem.rotation_type = 1  #HWD
        self.assertEqual(testItem.getDimension(), [20,10,30])

        testItem.rotation_type = 2  #HDW
        self.assertEqual(testItem.getDimension(), [20,30,10])

        testItem.rotation_type = 3  #DHW
        self.assertEqual(testItem.getDimension(), [30,20,10])

        testItem.rotation_type = 4  #DWH
        self.assertEqual(testItem.getDimension(), [30,10,20])

        testItem.rotation_type = 5  #WDH
        self.assertEqual(testItem.getDimension(), [10,30,20])

        testItem = Item(1,"test","cube", ["10",False,30.3], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getDimension(), ["10",False,30.3])

    # Bin Class Methods
    def test_binConstructor(self):
  
        testbin = Bin(1, [100,200,100], 5000)

        self.assertEqual(testbin.partno, 1)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.corner, 0)
        self.assertEqual(testbin.put_type, 1)

        # Attributes not affected by constructor
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 0)
        self.assertEqual(testbin.fix_point, False)
        self.assertEqual(testbin.check_stable, False)
        self.assertEqual(testbin.support_surface_ratio, 0)
        self.assertEqual(testbin.gravity, [])
      

        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        self.assertEqual(testbin.partno, 1)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.corner, 1)
        self.assertEqual(testbin.put_type, 0)

        # Attributes not affected by constructor
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 0)
        self.assertEqual(testbin.fix_point, False)
        self.assertEqual(testbin.check_stable, False)
        self.assertEqual(testbin.support_surface_ratio, 0)
        self.assertEqual(testbin.gravity, [])


        testbin = Bin(1, ["100",13.4,False], [2232,54], False, "true")

        self.assertEqual(testbin.partno, 1)
        self.assertEqual(testbin.width, "100")
        self.assertEqual(testbin.height, 13.4)
        self.assertEqual(testbin.depth, False)
        self.assertEqual(testbin.max_weight, [2232,54])
        self.assertEqual(testbin.corner, False)
        self.assertEqual(testbin.put_type, "true")

        # Attributes not affected by constructor
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 0)
        self.assertEqual(testbin.fix_point, False)
        self.assertEqual(testbin.check_stable, False)
        self.assertEqual(testbin.support_surface_ratio, 0)
        self.assertEqual(testbin.gravity, [])

        #just changing dimensions from array to int
        with self.assertRaises(TypeError):
            testbin = Bin(1, 100, [2232,54], False, "true")

    def test_binFormatNumbers(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        testbin.formatNumbers(3)
        self.assertEqual(testbin.width, 100.000)
        self.assertEqual(testbin.height, 200.000)
        self.assertEqual(testbin.depth, 100.000)
        self.assertEqual(testbin.max_weight, 5000.000)
        self.assertEqual(testbin.number_of_decimals, 3)

        testbin.formatNumbers(0)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.number_of_decimals, 0)

        testbin.formatNumbers(-1)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.number_of_decimals, -1)

        testbin.formatNumbers(10)
        self.assertEqual(testbin.width, 100.0000000000)
        self.assertEqual(testbin.height, 200.0000000000)
        self.assertEqual(testbin.depth, 100.0000000000)
        self.assertEqual(testbin.max_weight, 5000.0000000000)
        self.assertEqual(testbin.number_of_decimals, 10)

        with self.assertRaises(TypeError):
            testbin.formatNumbers("potato")
            testbin.formatNumbers(False)

    def test_binString(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        self.assertEqual(testbin.string(), "1(100x200x100, max_weight:5000) vol(2000000)")

        # does list items for some reason

        testbin = Bin("454", [100,200,100], False, "1")

        self.assertEqual(testbin.string(), "454(100x200x100, max_weight:False) vol(2000000)")

    def test_binGetVolume(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
    
        self.assertEqual(testbin.getVolume(), 2000000)

        testbin.formatNumbers(3)
        self.assertEqual(testbin.getVolume(), 2000000.000)

    def test_binGetTotalWeight(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        self.assertEqual(testbin.getTotalWeight(), 0)

        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testbin.putItem(testItem, [0,0,0])

        self.assertEqual(testbin.getTotalWeight(), 25)

        testItem2 = Item(2,"test","cube", [10,20,30], 75, 2, 400, False, "blue")
        testbin.putItem(testItem2, [50,0,50])

        self.assertEqual(testbin.getTotalWeight(), 100)

        testItem3 = Item(3,"test","cube", [10,20,30], 75, 2, 400, False, "red")
        testbin.putItem(testItem3, [0,0,0])
        #items cant overlap
        self.assertEqual(testbin.getTotalWeight(), 100)

    def test_binPutItem(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        self.assertEqual(testbin.items, [])

        testItem = Item("testItem1","test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testbin.putItem(testItem, [0,0,0])

        #func to print all items in bin
        def retItems(bin):
            final = []
            for item in bin.items:
                final.append(item.string())
            return final

        self.assertEqual(retItems(testbin), ['testItem1(10x20x30, weight: 25) pos([0, 0, 0]) rt(0) vol(6000)'])

        testItem2 = Item("testItem2","test","cube", [5,14,10], 50, 2, 400, True, "blue")
        testbin.putItem(testItem2, [50,50,50])

        self.assertEqual(retItems(testbin), ['testItem1(10x20x30, weight: 25) pos([0, 0, 0]) rt(0) vol(6000)', 'testItem2(5x14x10, weight: 50) pos([50, 50, 50]) rt(0) vol(700)'])


        testbin2 = Bin("testBin2", [100,200,100], 5000, 1, 0)
        with self.assertRaises(AttributeError):
            testbin.putItem("hello", [80, 90, 80])
            testbin.putItem(5, [80, 90, 80])
            testbin.putItem(testbin2, [80, 90, 80])


    # Honestly not sure what these next three functions do          
    def test_binCheckDepth(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        self.assertEqual(testbin.checkDepth([0,10,0,20,0,20]), 0.0)

    def test_binCheckWidth(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        self.assertEqual(testbin.checkWidth([0,10,0,20,0,20]), 0.0)

    def test_binCheckHeight(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        self.assertEqual(testbin.checkHeight([0,10,0,20,0,20]), 0.0)

    def test_binAddCorner(self):
        testbin = Bin(1, [100,200,100], 5000, 1, 0)

        # a function to return the contents of list and not the list object
        def retList(lst):
            res = []
            for item in lst:
                res.append(item.string())
            return res

        self.assertEqual(retList(testbin.addCorner()), ['corner0(1x1x1, weight: 0) pos([0, 0, 0]) rt(0) vol(1)', 'corner1(1x1x1, weight: 0) pos([0, 0, 0]) rt(0) vol(1)', 'corner2(1x1x1, weight: 0) pos([0, 0, 0]) rt(0) vol(1)', 'corner3(1x1x1, weight: 0) pos([0, 0, 0]) rt(0) vol(1)', 'corner4(1x1x1, weight: 0) pos([0, 0, 0]) rt(0) vol(1)', 'corner5(1x1x1, weight: 0) pos([0, 0, 0]) rt(0) vol(1)', 'corner6(1x1x1, weight: 0) pos([0, 0, 0]) rt(0) vol(1)', 'corner7(1x1x1, weight: 0) pos([0, 0, 0]) rt(0) vol(1)'])
        


        
        






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