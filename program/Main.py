"""
|=====[ Simulation Warehouse Main (SWM) ]====|
Creation Date: 11/8/2023
Authors: How Yu Chern

Main Program Responsibilities:
1. Run Simulation
2. Allow user to select 3DBP Solution Algorithm
"""
# Imports
from Utilities import Cuboids
from Master_input import *

# Main
def main():
   
   # Welcome Message
   print("==================================================================")
   print("Welcome to Warehouse simulation for Storage Optimization in Automated Fulfillment Centers.")
   print("Problem To Simulate: 3 Dimensional Bin Packing Problem")
   print("------------------------------------------------------------------")

   # Run Warehouse - Master Subroutine
   ms_main()

   # Exit Message
   print("Simulation Exit. Thank you for using the simulation.")
   print("==================================================================")
   
   return None

if __name__ == "__main__":
   main()

