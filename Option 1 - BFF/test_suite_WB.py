#Testing suite designed to test all of the methods in the auxiliary_methods.py folder in the py3dbp folder
from py3dbp import rectIntersect, intersect, getLimitNumberOfDecimals, set2Decimal, Item, Bin, Packer, Axis
from decimal import Decimal
import decimal
import unittest
import numpy as np

"""
White Box Testing
"""

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
    
    def test_rectIntersect(self):
        """
        Conditional Testing:-
        2 conditions:
        'ix < (d1[x]+d2[x])/2' 
        'iy < (d1[y]+d2[y])/2'

        """
        #                                  W  H  D
        testItem1 = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [5,10,10], 25, 2, 400, False, "orange")

        """
        2.5 < 7.5 ; True
        5 < 15    ; True
        """
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), True)
        
        """
        2.5 < 7.5 ; True
        140 < 60  ; False
        """
        testItem2 = Item(2,"test","cube", [5,100,10], 25, 2, 400, False, "orange")
        testItem2.position = [0, 100, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)


        """
        145 < 55  ; False
        5 < 15    ; True
        """

        testItem2 = Item(2,"test","cube", [100,10,10], 25, 2, 400, False, "orange")
        testItem2.position = [100, 0, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)


        """
        145 < 55  ; False
        140 < 60  ; False
        """
        testItem2 = Item(2,"test","cube", [100,100,10], 25, 2, 400, False, "orange")
        testItem2.position = [100, 100, 0]
        self.assertEqual(rectIntersect(testItem1, testItem2, Axis.WIDTH, Axis.HEIGHT), False)

        """
        100% path coverage
        """
 
    def test_intersect(self):
        """
        Conditional testing:-
        3 Conditions:
        rectIntersect(item1, item2, Axis.WIDTH, Axis.HEIGHT)
        rectIntersect(item1, item2, Axis.HEIGHT, Axis.DEPTH)
        rectIntersect(item1, item2, Axis.WIDTH, Axis.DEPTH)
        
        Not possible to get 2 True's and a False
        """
        #                                  W  H  D
        testItem1 = Item(1,"test","cube", [10,10,10], 25, 2, 400, False, "orange")
        testItem2 = Item(2,"test","cube", [10,10,10], 25, 2, 400, False, "orange")
        
        """
        True
        True
        True
        """
        self.assertEqual(intersect(testItem1, testItem2), True)
        
        """
        True
        False
        False
        """
        testItem1.position = [0, 0, 15]
        self.assertEqual(intersect(testItem1, testItem2), False)
        
        """
        False
        True
        False
        """
        testItem1.position = [15, 0, 0]
        self.assertEqual(intersect(testItem1, testItem2), False)
        
        """
        False
        False
        True
        """
        testItem1.position = [0, 15, 0]
        self.assertEqual(intersect(testItem1, testItem2), False)
        
        """
        False
        False
        False
        """
        testItem1.position = [0, 15, 15]
        self.assertEqual(intersect(testItem1, testItem2), False)
 
    def test_getLimitNumberOfDecimals(self):
        """
        No conditionals, 1 line of code, 100% Path Coverage
        """
        # Positive number of decimals
        self.assertEqual(getLimitNumberOfDecimals(3), 1.000)

    def test_set2Decimal(self):
        """
        Only difference is if default variable value is used
        
        100% path coverage
        """
        # Float value with default number of decimals
        self.assertEqual(set2Decimal(9.4231), Decimal('9'))
        
        # Float value with a custom number of decimals
        self.assertEqual(set2Decimal(9.4231, 2), Decimal('9.42'))

    #                      #
    #  Item Class Methods  #
    #                      #

    def test_itemConstructor(self):
        """
        Conditional testing:-
        1 Condition:
        self.updown = updown if typeof == 'cube' else False
        
        100% Path coverage
        """

                                        #                #
                                        # Positive Cases #
                                        #                #
                                        
        # typeof == 'cube'
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
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
        
        # typeof == 'apricot'
        testItem = Item(1,"test","apricot", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.partno, 1)
        self.assertEqual(testItem.name, "test")
        self.assertEqual(testItem.typeof, "apricot")
        self.assertEqual(testItem.width, 10)
        self.assertEqual(testItem.height, 20)
        self.assertEqual(testItem.depth, 30)
        self.assertEqual(testItem.weight, 25)
        self.assertEqual(testItem.level, 2)
        self.assertEqual(testItem.loadbear, 400)
        self.assertEqual(testItem.updown, False)
        self.assertEqual(testItem.color, "orange")
            # Attributes not affected by constructor
        self.assertEqual(testItem.rotation_type, 0)
        self.assertEqual(testItem.position, [0,0,0])
        self.assertEqual(testItem.number_of_decimals, 0)

    def test_itemFormatNumbers(self):
        """
        No conditionals
        
        100% Path coverage
        """
        # Integer number of decimals
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25., 2, 400, True, "orange")
        testItem.formatNumbers(3)
        self.assertEqual(testItem.width, Decimal('10.234'))
        self.assertEqual(testItem.height, Decimal('20.300'))
        self.assertEqual(testItem.depth, Decimal('30.000'))
        self.assertEqual(testItem.weight, Decimal('25.000'))
        self.assertEqual(testItem.number_of_decimals, 3)

    def test_itemString(self):
        """
        No conditionals
        
        100% Path coverage
        """
        # Valid Item construction
        testItem = Item(1,"test","cube", [10.23423,20.3,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.string(), "1(10.23423x20.3x30, weight: 25) pos([0, 0, 0]) rt(0) vol(6233)")

    def test_itemGetVolume(self):
        """
        No conditionals
        
        100% Patch coverage
        """
        # Valid Item Construction
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getVolume(), 6000)

    def test_itemGetMaxArea(self):
        """
        Conditional testing:-
        1 Condition:
        a = sorted([self.width,self.height,self.depth],reverse=True) if self.updown == True else [self.width,self.height,self.depth]
        
        100% path Coverage
        """
        # self.updown == True
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        self.assertEqual(testItem.getMaxArea(), 600)
        
        # self.updown == False
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, False, "orange")
        self.assertEqual(testItem.getMaxArea(), 200)

    def test_itemGetDimension(self):
        """
        Conditional Testing:-
        7 Conditions:
        if self.rotation_type == RotationType.RT_WHD
        if self.rotation_type == RotationType.RT_HWD
        if self.rotation_type == RotationType.RT_HDW
        if self.rotation_type == RotationType.RT_DHW
        if self.rotation_type == RotationType.RT_DWH
        if self.rotation_type == RotationType.RT_WDH
        else
        
        100% Path Coverage
        """
        #if self.rotation_type == RotationType.RT_WHD
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 0
        self.assertEqual(testItem.getDimension(), [10,20,30])
        
        #if self.rotation_type == RotationType.RT_HWD
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 1
        self.assertEqual(testItem.getDimension(), [20,10,30])
        
        #if self.rotation_type == RotationType.RT_HDW
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 2
        self.assertEqual(testItem.getDimension(), [20,30,10])
        
        #if self.rotation_type == RotationType.RT_DHW
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 3
        self.assertEqual(testItem.getDimension(), [30,20,10])
        
        #if self.rotation_type == RotationType.RT_DWH
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 4
        self.assertEqual(testItem.getDimension(), [30,10,20])
        
        #if self.rotation_type == RotationType.RT_WDH
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 5
        self.assertEqual(testItem.getDimension(), [10,30,20])
        
        #else
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.rotation_type = 6
        self.assertEqual(testItem.getDimension(), [])

    #                     #
    #  Bin Class Methods  #
    #                     #

    def test_binConstructor(self):
        """
        Conditional testing:-
        No Conditions
        
        100% Path Coverage
        """

        # Using default values for corner and put_type
        testbin = Bin(1, [100,200,100], 5000)
        self.assertEqual(testbin.partno, 1)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.corner, 0)
        self.assertEqual(testbin.put_type, 1)
        self.assertEqual(testbin.fit_items.tolist(), [[0, 100, 0, 200, 0, 0]])
            # Attributes not affected by constructor
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 0)
        self.assertEqual(testbin.fix_point, False)
        self.assertEqual(testbin.check_stable, False)
        self.assertEqual(testbin.support_surface_ratio, 0)
        self.assertEqual(testbin.gravity, [])
        
        # Using custom values for corner and put_type
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        self.assertEqual(testbin.partno, 1)
        self.assertEqual(testbin.width, 100)
        self.assertEqual(testbin.height, 200)
        self.assertEqual(testbin.depth, 100)
        self.assertEqual(testbin.max_weight, 5000)
        self.assertEqual(testbin.corner, 1)
        self.assertEqual(testbin.put_type, 0)
        self.assertEqual(testbin.fit_items.tolist(), [[0, 100, 0, 200, 0, 0]])
            # Attributes not affected by constructor
        self.assertEqual(testbin.items, [])
        self.assertEqual(testbin.unfitted_items, [])
        self.assertEqual(testbin.number_of_decimals, 0)
        self.assertEqual(testbin.fix_point, False)
        self.assertEqual(testbin.check_stable, False)
        self.assertEqual(testbin.support_surface_ratio, 0)
        self.assertEqual(testbin.gravity, [])

    def test_binFormatNumbers(self):
        """
        Conditional Testing:-
        No Conditions:
        
        100% Path coverage
        """
        # Integer number of decimals
        testbin = Bin(1, [100,200,49.64523], 5000, 1, 0)
        testbin.formatNumbers(3)
        self.assertEqual(testbin.width, Decimal('100.000'))
        self.assertEqual(testbin.height, Decimal('200.000'))
        self.assertEqual(testbin.depth, Decimal('49.645'))
        self.assertEqual(testbin.max_weight, Decimal('5000.000'))
        self.assertEqual(testbin.number_of_decimals, 3)

    def test_binString(self):
        """
        Conditional Testing:-
        No Conditions:
        
        100% Path Coverage
        """

        # Valid Item Construction
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        self.assertEqual(testbin.string(), "1(100x200x100, max_weight:5000) vol(2000000)")

    def test_binGetVolume(self):
        """
        Conditional Testing:-
        No Conditions:
        
        100% Path Coverage
        """
        # Valid Bin Construction
        testbin = Bin(1, [100,200,100], 5000, 1, 0)
        self.assertEqual(testbin.getVolume(), 2000000)

    def test_binGetTotalWeight(self):
        """
        Loop Testing:-
        1 Loop:
        for item in self.items:
            total_weight += item.weight
            
        Path Coverage Testing:-
        100%
        """
        # No items
        testbin = Bin(1, [2000,2000,2000], 5000, 1, 0)
        self.assertEqual(testbin.getTotalWeight(), 0)
        
        # 1 Item
        testbin = Bin(1, [2000,2000,2000], 5000, 1, 0)
        testItem = Item(1,"test","cube", [10,20,30], 10, 2, 400, True, "orange")
        testbin.putItem(testItem, [0,0,0])
        self.assertEqual(testbin.getTotalWeight(), 10)
        
        # Multiple Items
        testbin = Bin(1, [2000,2000,2000], 5000, 1, 0)
        testItem1 = Item(1,"test1","cube", [10,20,30], 10, 2, 400, True, "orange")
        testItem2 = Item(2,"test2","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem3 = Item(3,"test3","cube", [10,20,30], 11, 2, 400, True, "orange")
        testbin.putItem(testItem1, [0,0,0])
        testbin.putItem(testItem2, [50,50,50])
        testbin.putItem(testItem3, [100,100,100])
        self.assertEqual(testbin.getTotalWeight(), 46)

    # Delayed
    def test_binPutItem(self):
        """
        Conditional Testing:-
        8 Conditions:
        
        if (
        self.width < pivot[0] + dimension[0] or
        self.height < pivot[1] + dimension[1] or
        self.depth < pivot[2] + dimension[2]
        ) : else
            
        if intersect(current_item_in_bin, item)
        if self.getTotalWeight() + item.weight > self.max_weight
        if self.fix_point == True
        if self.check_stable == True
        
        Path Coverage Testing:-
        100% Path Coverage
        """

        """
        if (
        self.width < pivot[0] + dimension[0] or
        self.height < pivot[1] + dimension[1] or
        self.depth < pivot[2] + dimension[2]
        ) : else
        """
        # self.width < pivot[0] + dimension[0] == True
        testbin = Bin(1, [100,100,100], 5000, 1, 0)
        testItem = Item(1,"test","cube", [90,20,30], 25, 2, 400, True, "orange")
        testItem.formatNumbers(2)
        testbin.putItem(testItem, [100,0,0])
        self.assertEqual(len(testbin.items), 0)
        
        # self.height < pivot[1] + dimension[1] == True
        testbin = Bin(1, [100,100,100], 5000, 1, 0)
        testItem = Item(1,"test","cube", [10,90,30], 25, 2, 400, True, "orange")
        testItem.formatNumbers(2)
        testbin.putItem(testItem, [0,100,0])
        self.assertEqual(len(testbin.items), 0)

        # self.depth < pivot[2] + dimension[2] == True
        testbin = Bin(1, [100,100,100], 5000, 1, 0)
        testItem = Item(1,"test","cube", [10,20,90], 25, 2, 400, True, "orange")
        testItem.formatNumbers(2)
        testbin.putItem(testItem, [0,0,100])
        self.assertEqual(len(testbin.items), 0)
        
        # Else:
        testbin = Bin(1, [100,100,100], 5000, 1, 0)
        testItem = Item(1,"test","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem.formatNumbers(2)
        testbin.putItem(testItem, [0,0,0])
        self.assertEqual(len(testbin.items), 1)
        
        """
        if intersect(current_item_in_bin, item)
        """
        testbin = Bin(1, [500,500,500], 5000, 1, 0)
        testItem1 = Item(1,"test1","cube", [10,20,30], 25, 2, 400, True, "orange")
        testItem2 = Item(2,"test2","cube", [10,10,10], 25, 2, 400, True, "orange")
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testbin.putItem(testItem1, [0,0,0])
        testbin.putItem(testItem2, [5,5,5])
        self.assertEqual(len(testbin.items), 1)
        
        """
        if self.getTotalWeight() + item.weight > self.max_weight
        """
        testbin = Bin(1, [500,500,500], 100, 1, 0)
        testItem1 = Item(1,"test1","cube", [10,20,30], 75, 2, 400, True, "orange")
        testItem2 = Item(2,"test2","cube", [10,10,10], 50, 2, 400, True, "orange")
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testbin.putItem(testItem1, [0,0,0])
        testbin.putItem(testItem2, [100,100,100])
        self.assertEqual(len(testbin.items), 1)
        
        """
        if self.fix_point == True
        """
        testbin = Bin(1, [500,500,500], 100, 1, 0)
        testbin.fix_point = True
        testItem1 = Item(1,"test1","cube", [10,20,30], 75, 2, 400, True, "orange")
        testItem2 = Item(2,"test2","cube", [10,10,10], 50, 2, 400, True, "orange")
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testbin.putItem(testItem1, [0,0,0])
        testbin.putItem(testItem2, [100,100,100])
        self.assertEqual(len(testbin.items), 1)
        
        """
        if self.check_stable == True
        """
        testbin = Bin(1, [500,500,500], 100, 1, 0)
        testbin.check_stable = True
        testItem1 = Item(1,"test1","cube", [10,20,30], 75, 2, 400, True, "orange")
        testItem2 = Item(2,"test2","cube", [10,10,10], 50, 2, 400, True, "orange")
        testItem1.formatNumbers(2)
        testItem2.formatNumbers(2)
        testbin.putItem(testItem1, [0,0,0])
        testbin.putItem(testItem2, [100,100,100])
        self.assertEqual(len(testbin.items), 1)
        
    def test_binCheckDepth(self):
        """
        Condition Testing:-
        1 Condition:
        if len(x_bottom & x_top) != 0 and len(y_bottom & y_top) != 0 :

        Path Coverage Testing:-
        100%
        """

        """
        if len(x_bottom & x_top) != 0 and len(y_bottom & y_top) != 0 :
        
        for j in self.fit_items:
        x_bottom = set([i for i in range(int(j[0]),int(j[1]))]) # creates a list of every number from j[0] to j[1]
        x_top = set([i for i in range(int(unfix_point[0]),int(unfix_point[1]))])
        y_bottom = set([i for i in range(int(j[2]),int(j[3]))]) # creates a list of every number from j[2] to j[3]
        y_top = set([i for i in range(int(unfix_point[2]),int(unfix_point[3]))])

        """

        # True, True
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 10, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkDepth(unfix_point), 0.0)

        # True, False
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 0, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 10, 0, 0, 0, 10]
        self.assertEqual(testbin.checkDepth(unfix_point), 0.0)

        # False, True
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (0, 10, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 0, 0, 10, 0, 10]
        self.assertEqual(testbin.checkDepth(unfix_point), 0.0)

        # False, False
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (0, 0, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 0, 0, 0, 0, 10]
        self.assertEqual(testbin.checkDepth(unfix_point), 0.0)

    def test_binCheckWidth(self):
        """
        Condition Testing:-
        1 Condition:
        if len(z_bottom & z_top) != 0 and len(y_bottom & y_top) != 0 :

        Path Coverage Testing:-
        100%
        """

        """
        if len(z_bottom & z_top) != 0 and len(y_bottom & y_top) != 0 :
        
        for j in self.fit_items:
        z_bottom = set([i for i in range(int(j[4]),int(j[5]))])
        z_top = set([i for i in range(int(unfix_point[4]),int(unfix_point[5]))])
        y_bottom = set([i for i in range(int(j[2]),int(j[3]))])
        y_top = set([i for i in range(int(unfix_point[2]),int(unfix_point[3]))])

        """

        # True, True
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 10, 10), 100)
        testbin.items.append(testItem)
        testbin.fit_items = np.array([[0,10,0, 10,0,10]])
        unfix_point = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkWidth(unfix_point), 0.0)

        # True, False
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 0, 10), 100)
        testbin.items.append(testItem)
        testbin.fit_items = np.array([[0,10,0, 10,0,10]])
        unfix_point = [0, 10, 0, 0, 0, 10]
        self.assertEqual(testbin.checkWidth(unfix_point), 0.0)

        # False, True
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (0, 10, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 0, 0, 10, 0, 0]
        self.assertEqual(testbin.checkWidth(unfix_point), 0.0)

        # False, False
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (0, 0, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 0, 0, 0, 0, 0]
        self.assertEqual(testbin.checkWidth(unfix_point), 0.0)

    def test_binCheckWidth(self):
        """
        Condition Testing:-
        1 Condition:
        if len(x_bottom & x_top) != 0 and len(z_bottom & z_top) != 0 :

        Path Coverage Testing:-
        100%
        """

        """
        if len(z_bottom & z_top) != 0 and len(y_bottom & y_top) != 0 :
        
        for j in self.fit_items:
        x_bottom = set([i for i in range(int(j[0]),int(j[1]))])
        x_top = set([i for i in range(int(unfix_point[0]),int(unfix_point[1]))])
        z_bottom = set([i for i in range(int(j[4]),int(j[5]))])
        z_top = set([i for i in range(int(unfix_point[4]),int(unfix_point[5]))])
        """

        # True, True
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 10, 10), 100)
        testbin.items.append(testItem)
        testbin.fit_items = np.array([[0,10,0, 10,0,10]])
        unfix_point = [0, 10, 0, 10, 0, 10]
        self.assertEqual(testbin.checkWidth(unfix_point), 0.0)

        # True, False
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (10, 0, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 10, 0, 0, 0, 0]
        self.assertEqual(testbin.checkWidth(unfix_point), 0.0)

        # False, True
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (0, 10, 10), 100)
        testbin.items.append(testItem)
        testbin.fit_items = np.array([[0,10,0, 10,0,10]])
        unfix_point = [0, 0, 0, 10, 0, 0]
        self.assertEqual(testbin.checkWidth(unfix_point), 0.0)

        # False, False
        testItem = Item(1, 'Item1', 'cube', (5, 5, 5), 1.0, 1, 50, True, 'red')
        testbin = Bin(2, (0, 0, 10), 100)
        testbin.items.append(testItem)
        unfix_point = [0, 0, 0, 0, 0, 0]
        self.assertEqual(testbin.checkWidth(unfix_point), 0.0)

    def test_bin_addCorner(self):
        """
        Conditional Testing:-
        1 Condition:
        if self.corner != 0 :

        Path coverage testing:-
        100%
        """
        # self.corner == 0 :
        testbin = Bin(2, (10, 10, 10), 100, 0, 1)
        testbin.addCorner()
        self.assertEqual(testbin.addCorner(), None)

        # self.corner == 1 :
        testbin = Bin(2, (10, 10, 10), 100, 1, 1)
        testbin.addCorner()
        self.assertEqual(len(testbin.addCorner()), 8)

    def test_bin_putCorner(self):
        """
        Conditional testing:-
        0 Conditions:

        Path coverage testing:-
        100%
        """
        # Valid bin and corner creation
        testbin = Bin(1, (10, 10, 10), 100, 2)
        corners = testbin.addCorner()
        for corner in corners:
            testbin.putCorner(0, corner)
        self.assertEqual(len(testbin.items), 8)
        for count in range(len(corners)):
            self.assertEqual(testbin.items[count], corners[count])

    def test_bin_clearBin(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """

        # Valid bin and items
        testitem1 = Item(1, 'testitem1', 'cube', (4, 4, 4), 1.0, 1, 50, True, 'red')
        testitem2 = Item(2, 'testitem2', 'cube', (3, 3, 3), 1.0, 1, 50, True, 'blue')
        testbin = Bin(3, (100, 100, 100), 100)
        testitem1.formatNumbers(2)
        testitem2.formatNumbers(2)
        testbin.putItem(testitem1, [0,0,0])
        testbin.putItem(testitem2, [5,5,5])
        self.assertEqual(len(testbin.items), 2)
        testbin.clearBin()
        self.assertEqual(len(testbin.items), 0)

    #                        #
    #  Packer Class Methods  #
    #                        #

    def test_packer_constructor(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:
        100%
        """
        testPacker = Packer()
        self.assertEqual(testPacker.bins, [])
        self.assertEqual(testPacker.items, [])
        self.assertEqual(testPacker.unfit_items, [])
        self.assertEqual(testPacker.total_items, 0)
        self.assertEqual(testPacker.binding, [])

    def test_packer_addBin(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        # Adding 1 Bin
        testPacker = Packer()
        testbin = Bin("testbin", [100,200,100], 5000, 1, 0)
        testPacker.addBin(testbin)
        self.assertEqual(len(testPacker.bins), 1)

    def test_packer_addItem(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        # Adding 1 Item
        testPacker = Packer()
        testItem = Item("testitem","test","cube", [10,30,30], 25, 2, 400, True, "orange")
        testPacker.addItem(testItem)
        self.assertEqual(len(testPacker.items), 1)
        self.assertEqual(testPacker.total_items, 1)

    # Delayed
    def test_packer_pack2Bin(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        pass

        # Delayed
   
   # Delayed
    def test_packer_sortBinding(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        pass

    # Delayed
    def test_packer_putOrder(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        pass

    # Delayed
    def test_packer_gravityCenter(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        pass

    # Delayed
    def test_packer_pack(self):
        """
        Conditional Testing:-
        0 Conditions:

        Path Coverage Testing:-
        100%
        """
        pass












if __name__ == '__main__':
    unittest.main()