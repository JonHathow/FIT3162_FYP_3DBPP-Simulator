"""
Python Classes to represent a generic cuboidal object - Containers and SKU Items.

Creation Date: 13/8/2023
Authors: How Yu Chern

Classes Implemented (Ref: MCS15_Project_Proposal)
1. Cuboid - Represents any Cuboid Object
2. Container - Represents a generic container in a warehouse
3. SKU - Represents a generic item parcel.
"""

class Cuboid():

   def __init__(self, length: int, width: int, height: int, fragile: bool, category: str) -> None:
      self.length = length
      self.width = width
      self.height = height
      self.fragile = fragile
      self.category = category

   def __str__(self) -> str:
      print(("Cuboid of {} l x {} w x {} h, with category: {}, and fragility class = {}").format(self.length, self.width, self.height, self.fragile, self.category))
      


class Container(Cuboid):
   
   def __init__(self, length: int, width: int, height: int, fragile: bool, category: str, max_weight: int) -> None:

      super().__init__(length, width, height, fragile, category)

      # Container initially start of empty, so storage list is none for now.
      self.max_weight = max_weight
      self.storage = [None]

      # Container Metrics
      self.status = "Empty"
      self.no_of_items = 0
      self.occupied_weight = 0
      self.available_weight = 0
      self.occupied_volume = 0
      self.available_volume = 0

   def update():
      # To Do - Automatically Calculate Metrics
      pass

   def check_status():
      # To Do - Output Metrics
      pass

   def __str__(self) -> str:
      print("Container Dimensions: ({} l x {} w x {} h), Category: {}, Fragility Class: {}, Max Weight Capacity: {}").format(self.length, self.width, self.height, self.category, self.fragile, self.max_weight)


class SKU(Cuboid):

   def __init__(self, length: int, width: int, height: int, fragile: bool, category: str, weight: int) -> None:

      super().__init__(length, width, height, fragile, category)

      self.weight = weight


   def __str__(self) -> str:
      print("Item Dimensions: ({} l x {} w x {} h), Category: {}, Fragility Class: {}, Weight: {}").format(self.length, self.width, self.height, self.category, self.fragile, self.weight)

   

# Main
def main():
   print("This is not the main file. Please run warehouse_main.py instead.")
   return None

if __name__ == "__main__":
   main()