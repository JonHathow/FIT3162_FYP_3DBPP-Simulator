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
from UI import Main_Window, MS_Window
from Option1_input import O1_Input

# Main Window
def run_main_window(m_title, m_geometry):

   # Create Main Window
   m_algorithms = ["Option 1 - Back Bottom Left Fill", "Option 2 - Best Match Fill"] # Can add more options here
   mw = Main_Window(m_title, m_geometry, m_algorithms)

   # Retrieve Chosen Algorithm
   data = mw.get_data()
   exit_flag = mw.get_exitflag()
   return data, exit_flag

# Master Subroutine Window
def run_ms_window(m_title, m_geometry, c_algo):
   
   # Initialize Variables
   chosen_option = None
   back_flag = False

   # Check if algorithm was chosen, else "Exit" was selected.
   if c_algo is not None:

      # Initialize Master Subroutine Window (MSW)
      print("Chosen Algorithm {}".format(c_algo))
      s_options = ["1. Create New Box (SKU)", "2. Create New Bin", "3. Load Existing Box (SKU)", "4. Load Existing Bin", "5. Compute Algorithm"] 
      msw = MS_Window(m_title, m_geometry, c_algo, s_options)

      # Retrieve Data and Status
      chosen_option = msw.get_data()
      back_flag = msw.get_backflag()
      print("Back Pressed: {}".format(back_flag))

   return chosen_option, back_flag

# Box Window
def run_box_window():
   pass

# Bin Window
def run_bin_window():
   pass

# Loading CSVs
def run_load_window():
   pass

# Main
def main():
   
   # Welcome Message
   print("==================================================================")
   print("Welcome to Warehouse simulation for Storage Optimization in Automated Fulfillment Centers.")
   print("Problem To Simulate: 3 Dimensional Bin Packing Problem")
   print("------------------------------------------------------------------")

   # Run Main Window
   m_title = "Storage Optimization in Automated Fulfilment Centers"
   m_geometry = "500x300"
   c_algo, exit_flag = run_main_window(m_title, m_geometry)
   print("Exit: {} ".format(exit_flag))

   # Invoke relevant Subroutines
   if not exit_flag:
      
      chosen_option, back_flag = run_ms_window(m_title, m_geometry, c_algo)

      # Feedback loop
      while back_flag and not exit_flag:
         c_algo, exit_flag = run_main_window(m_title, m_geometry)
         chosen_option, back_flag = run_ms_window(m_title, m_geometry, c_algo)

      print("Chosen Option: {}".format(chosen_option))
      print("Exit: {} ".format(exit_flag))

   else:
      print("Exit was selected. Thank you for using the simulation.")
      print("==================================================================")
   
   return None

if __name__ == "__main__":
   main()

