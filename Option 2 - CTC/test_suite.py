from test_folder import get_limit_number_of_decimals, set_to_decimal, rect_intersect, intersect, stack, Bin, Item, Packer, Axis
import unittest
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

    # Testing Bin Class Methods

    # Testing Packer Class Methods


if __name__ == '__main__':
    unittest.main()