"""
|=====[ Simulation Warehouse Main (SWM) ]====|
Creation Date: 11/8/2023
Authors: How Yu Chern, Cheryl Frances Lee, Anson Sameer Lee

Main Program Responsibilities:
1. Run Simulation
2. Allow user to select 3DBP Solution Algorithm
3. Output Results
"""
# Imports
from cuboids import Container, SKU

# Capture Input
def handle_input():
   index = input()
   flag = True

   if index == 1:
      print("# Placeholder: execute algorithm 1")
   elif index == 2:
      print("# Placeholder: execute algorithm 1")
   elif index == 3:
      print("# Placeholder: execute algorithm 1")
   else:
      print("Invalid algorithm selected. Please try again.")
      flag = False

   return flag

# Print Menu
def print_menu():
   print("Welcome to SimuMain for Storage Optimization in Automated Fulfillment Centers.")
   print("Please select an option (1, 2, 3) to choose your solution algorithm")

    # More code here . . .
    
   return None


# Main
def main():
   flag = True
   
   while not flag:
      print_menu()
      flag = handle_input()

   return None

if __name__ == "__main__":
   main()

