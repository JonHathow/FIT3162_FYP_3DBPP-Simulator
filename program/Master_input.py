""" 
Master Subroutine to help Warehouse Main manage the other Input Subroutines for the respective algorithms.
Creation Date: 7/9/2023
Authors: How Yu Chern

Master Subroutine Program Responsibilities:
1. Manage all UI Panels
2. Manage the Input Subroutines
"""
# Imports
from UI import Main_Window, MS_Window

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

def handle_option(chosen_option):
   
   return 

# Msster Input Main
"""
This is the Master Input Subroutine Program
Which is used to test and run the Master Subroutine
"""
def ms_main():

   # Run Main Window
   m_title = "Storage Optimization in Automated Fulfilment Centers"
   m_geometry = "600x400"
   c_algo, exit_flag = run_main_window(m_title, m_geometry)
   print("Exit: {} ".format(exit_flag))

   # Main Window Loop
   if not exit_flag:
      
      chosen_option, back_flag = run_ms_window(m_title, m_geometry, c_algo)

      # Master Subroutine Window Loop
      # Back Button Pressed - Return to Main Menu
      while back_flag and not exit_flag:
         c_algo, exit_flag = run_main_window(m_title, m_geometry)
         chosen_option, back_flag = run_ms_window(m_title, m_geometry, c_algo)

      # Retrieved Option and Call Other Relevant Windows
      print("Chosen Option: {}".format(chosen_option))
      print("Exit: {} ".format(exit_flag))

      handle_option(chosen_option)

   else:
      print("Exit was selected. Thank you for using the simulation.")
      print("==================================================================")
   
   return None

if __name__ == "__main__":
   ms_main()
