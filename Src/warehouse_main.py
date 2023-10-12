"""
|=====[ Simulation Warehouse Main (SWM) ]====|
Creation Date: 11/8/2023
Authors: How Yu Chern

Main Program Responsibilities:
1. Run Simulation
2. Allow user to select 3DBP Solution Algorithm

To Do - Capture and properly handle all Input Parameters - R1 from Requirement Tracability Matrix
"""
# Imports
import random
from cuboids import Container, SKU
from ui import Input_Window

class Warehouse():

   def __init__(self) -> None:
      self.container_details = None
      self.containers = []
      self.SKUs = []
      self.random_seed = 0
      self.batch_size = 0
      
   def set_random_seed(self, seed):
      self.random_seed = seed

   """
   # To Do - Warehouse Containers can have different fragility class, categories, and max_weight.
   # Need to see how to standardize and regulate input better.

   def spawn_containers(self, quantity, length, width, height, fragile, category, max_weight):
      for i in range(quantity):
         self.containers += Container(length, width, height, fragile, category, max_weight)
   """


# Capture Input
def handle_input():
   index = input()
   flag = True

   if index == "1":
      print("# Back Bottom-Left Fill Algorithm Selected")
      flag = True
   elif index == "2":
      print("# Corner To Center Algorithm Selected ")
      flag = True
   else:
      print("Invalid algorithm selected. Please try again.")
      flag = False

   return flag

# Print Menu
def print_menu():
   """
   print("==================================================================")
   print("Please select an option (1, 2) to choose your solution algorithm")
   print("1. Back Bottom-Left Fill Heuristic - Genetic Algorithm")
   print("2. Corner To Center Heuristic - Genetic Algorithm")
   """
   iw = Input_Window()

   print("Data Retrieved")
   data = iw.get_data()
   print(data)
    
   return data


# Main
def main():
   flag = False
   
   # Welcome Message
   print("==================================================================")
   print("Welcome to Warehouse simulation for Storage Optimization in Automated Fulfillment Centers.")
   print("Problem To Simulate: 3 Dimensional Bin Packing Problem")

   # Input Menu
   data = print_menu()
   random_seed = data[0]
   print(random_seed)

   return None

if __name__ == "__main__":
   main()

