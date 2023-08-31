"""
Main Program for Option 2 - CTC

Notes:
1. To Run Option 2's Algorithm
"""
from packer import Packer
from bin import Bin
from item import Item

def main():
   
   packer = Packer()

   bin1 = Bin("Bin1", 500, 500, 500, 500)
   packer.add_bin(bin1)
   
   item_list = []

   item1 = Item("Box1", 100, 100, 100, 50)
   item_list.append(item1)
   item2 = Item("Box2", 50, 50, 50, 100)
   item_list.append(item2)
   item3 = Item("Box3", 50, 80, 100, 70)
   item_list.append(item3)
   item4 = Item("Box4", 40, 70, 30, 30)
   item_list.append(item4)
   # item5 = Item("Full Box", 500, 500, 500, 500)
   # item_list.append(item5)
   item6 = Item("Oversized Box", 1000, 1000, 1000, 1000)
   item_list.append(item6)
   item7 = Item("Bigger Box", 400, 400, 400, 400)
   item_list.append(item7)

    # Add Items to Pack
   for item in item_list:
      packer.add_item(item)

   packer.pack()

   return None

if __name__ == "__main__":
   main()