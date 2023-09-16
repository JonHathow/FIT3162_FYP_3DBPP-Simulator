"""
|=====[ Simulation Warehouse Main (SWM) ]====|
Creation Date: 11/8/2023
Authors: How Yu Chern

Main Program Responsibilities:
1. Run Simulation
2. Allow user to select 3DBP Solution Algorithm
"""
# Imports
from cuboids import Container, SKU
from ui import Main_Window, MS_Window

"""
Old Code

class Warehouse():

   def __init__(self) -> None:
      self.container_details = None
      self.containers = []
      self.SKUs = []
      self.random_seed = 0
      self.batch_size = 0
      
   def set_random_seed(self, seed):
      self.random_seed = seed

   # To Do - Warehouse Containers can have different fragility class, categories, and max_weight.
   # Need to see how to standardize and regulate input better.

   def spawn_containers(self, quantity, length, width, height, fragile, category, max_weight):
      for i in range(quantity):
         self.containers += Container(length, width, height, fragile, category, max_weight)

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
"""
# Main Window
def main_window(m_title, m_geometry):

   # Create Main Window
   m_algorithms = ["Option 1 - Back Bottom Left Fill", "Option 2 - Best Match Fill"] # Can add more options here
   mw = Main_Window(m_title, m_geometry, m_algorithms)

   # Retrieve Chosen Algorithm
   data = mw.get_data()
   return data[0]

# Main
def main():
   
   # Welcome Message
   print("==================================================================")
   print("Welcome to Warehouse simulation for Storage Optimization in Automated Fulfillment Centers.")
   print("Problem To Simulate: 3 Dimensional Bin Packing Problem")

   # Run Main Window
   m_title = "Storage Optimization in Automated Fulfilment Centers"
   m_geometry = "500x300"
   c_algo = main_window(m_title, m_geometry)
   print(c_algo)

   # Invoke relevant Subroutines
   s_options = ["1. Create New Box (SKU)", "2. Create New Bin", "3. Load Existing Box (SKU)", "Load Existing Bin"] 
   # sw = MS_Window(m_title, m_geometry, c_algo, s_options)

   return None

if __name__ == "__main__":
   main()

