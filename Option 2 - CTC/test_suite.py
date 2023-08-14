from test_folder import get_limit_number_of_decimals, set_to_decimal, rect_intersect, intersect, Bin, Item, Packer,  Axis
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

    # Testing Auxiliary Methods
    def test_get_limit_number_of_decimals(self):
        return None
    
    def test_set_to_decimal(self):
        return None
    
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
        return None
    
    def test_stack(self):
        return None
    
    # Testing Item Class Methods

    # Testing Bin Class Methods

    # Testing Packer Class Methods


if __name__ == '__main__':
    unittest.main()