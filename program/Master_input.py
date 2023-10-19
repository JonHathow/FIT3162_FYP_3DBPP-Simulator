""" 
Master Subroutine to help Warehouse Main manage the other Input Subroutines for the respective algorithms.
Creation Date: 7/9/2023
Authors: How Yu Chern

Master Subroutine Program Responsibilities:
1. Manage all UI Panels
2. Manage the Input Subroutines
"""
# Imports
from manage_csv.constants import File, Option, MENU_INPUT, MENU_INVALID, MENU_BIN_NOTLOADED, MENU_BOX_NOTLOADED, MENU_END, FILE_BIN_1, FILE_BOX_1, FILE_BIN_2, FILE_BOX_2
from manage_csv.write_input_bin import write_input_bin_func
from manage_csv.write_input_box import write_input_box_func
from manage_csv.read_input_csv import read_input
from Option1_input import *
from Option2_input import *
from UI import *

# --- Global Variables: UI Details ---#
# Core Params
m_title = "Storage Optimization in Automated Fulfilment Centers"
m_geometry = "600x400"
bin_params = ["Quantity", "Width", "Height", "Depth", "Capacity"]

# Box Param Option 1 & Option 2
bparams_normal = ["Number of Boxes"]
bparams_ranges = ["Quantity Range", "Dimensions Range", "Weight Range"]
bparams_boolean = ["Allow Varying Priority Levels", "Allow Varying Loading Orientations", "Allow Upside Down Loading"]

# --- Run UI Functions --- #
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
def run_ms_window(m_title, m_geometry, c_algo, past_option = None, bin_filename = None, box_filename = None):
   
   # Initialize Variables
   chosen_option = None
   back_flag = False

   # Check if algorithm was chosen, else "Exit" was selected.
   if c_algo is not None:

      # Initialize Master Subroutine Window (MSW)
      print("Chosen Algorithm {}".format(c_algo))
      s_options = ["1. Create New Bin", "2. Create New Box (SKU)", "3. Load Existing Bin", "4. Load Existing Box (SKU)"] 

      if bin_filename is not None and box_filename is not None:
          s_options += ["5. Compute Algorithm"]

      msw = MS_Window(m_title, m_geometry, c_algo, s_options, past_option, bin_filename, box_filename)

      # Retrieve Data and Status
      chosen_option = msw.get_data()
      back_flag = msw.get_backflag()
      print("Back Pressed: {}".format(back_flag))

   return chosen_option, back_flag

# Run Bin Window
def run_bin_window():
   
   print("Bin Window")

   bw = Bin_Window(m_title, m_geometry, bin_params)
   bin_inputs = bw.get_data()
   backflag = bw.get_backflag()

   print("Details:")
   print(bin_inputs)
   print(backflag)
   
   return bin_inputs, backflag

# Run Box Window
def run_box_window(c_option):
   
   # Initialize Variables
   box_inputs = None
   back_flag = False

   # Box Window - Option 1
   if c_option == Option.OPTION1.value:
      print("Box Window - Option 1")
      box_w1 = Box_Window_O1(m_title, m_geometry, "Option 1 - Back Bottom Left Fill", bparams_normal, bparams_ranges, bparams_boolean)
      box_inputs = box_w1.get_data()
      back_flag = box_w1.get_backflag()
   # Box Window - Option 2
   elif c_option == Option.OPTION2.value:
      print("Box Window - Option 2")
      box_w2 = Box_Window_O2(m_title, m_geometry, "Option 2 - Best Match Fill", bparams_normal, bparams_ranges)
      box_inputs = box_w2.get_data()
      back_flag = box_w2.get_backflag()
   
   print("Details:")
   print(box_inputs)
   print(back_flag)

   return box_inputs, back_flag

# Run Load CSV Window
def run_load_window(c_option, filetype):
   
   # Initialize Variables
   filepath = None
   back_flag = False

   lcsv_window = Load_CSV_Window(c_option, filetype)
   filepath = lcsv_window.get_data()

   if filepath == None:
       back_flag = True
      
   print(filepath)
   print(back_flag)
   
   return filepath, back_flag

# --- Utility Functions --- #
# Utility Function to format the Master Subroutine Window's selected option.
def ms_format(response):
    if response is not None:
        response = response[0]
    return response

# Utility Function to format file name to get shortened file name.
def filename_format(filename):
    
    file_paths = filename.split("\\")
    # print(file_paths)
    file_short = file_paths[-1]
    # print(file_short)
    return file_short

# --- Master Subroutine - Common Functionality between O1 and O2 --- #
def master_sub(response, c_option, past_option,  bin_filename, box_filename, bin_params, item_params):
    
    # State Check
    print("==================================================================")
    print("Master Subroutine Entered")
    print("Response Selected: {}".format(response))
    
    # Status Params
    response_no = ms_format(response)
    terminate = False

    # Back Flag
    backflag = False

    # Check choosen algorithm
    if c_option == Option.OPTION1.value:
        filetype = File.BIN.value
        
    elif c_option == Option.OPTION2.value:
        filetype = File.BOX.value
   
    # Write a CSV file for bins.
    if response_no == "1":
         
         bin_inputs, backflag = run_bin_window()
         print("Bin Inputs {}".format(bin_inputs))

         if not backflag and bin_inputs is not None:
            write_input_bin_func(c_option, bin_inputs)
            past_option = "Bin CSV Created"

    # Write a CSV file for boxes.
    elif response_no == "2":
      
         box_inputs, backflag = run_box_window(c_option)
         print("Box Inputs {}".format(box_inputs))

         if not backflag  and box_inputs is not None:
            write_input_box_func(c_option, box_inputs)
            past_option = "Box CSV Created"

    # Read a CSV file for bins.
    elif response_no == "3":
         
         bin_filename, backflag = run_load_window(c_option, FILE_BIN)
         print("File Path {}".format(bin_filename))

         if not backflag:
            bin_params = read_input(bin_filename, filetype, c_option)
            bins_loaded = True if bin_params is not None else False
            past_option = "Bin CSV Loaded"

            print(bin_params)
            print(bins_loaded)

            # Format before return
            bin_filename = filename_format(bin_filename)
            print(bin_filename)

    # Read a CSV file for boxes.
    elif response_no == "4":
         
         box_filename, backflag = run_load_window(c_option, FILE_BOX)
         print("File Path {}".format(box_filename))

         if not backflag:
            item_params = read_input(box_filename, filetype, c_option)
            boxes_loaded = True if item_params is not None else False
            past_option = "Box CSV Loaded"

            print(item_params)
            print(boxes_loaded)

            # Format before return
            box_filename = filename_format(box_filename)
            print(box_filename)

    # Compute bin packing. - Enter Subroutine "n"
    elif response_no == "5":
         if c_option == Option.OPTION1.value:
            O1_compute(bin_params, item_params)
         elif c_option == Option.OPTION2.value:
            O2_compute(bin_params, item_params)

         terminate = True
    
    # Checks
    print(response_no)
    print(backflag)

    return past_option, bin_filename, box_filename, bin_params, item_params, terminate

# Master Input Main
"""
This is the Master Input Subroutine Program
Which is used to test and run the Master Subroutine
"""
def ms_main():

   # Essential Params - Init
   bin_params = None
   item_params = None
   bin_filename = None 
   box_filename = None

   # Status Params
   past_option = None
   exit_flag = False

   # Main Window Loop
   while not exit_flag:
       
      # Run Main Window
      c_algo, exit_flag = run_main_window(m_title, m_geometry)
      print("Exit: {} ".format(exit_flag))

      # Exit Condition
      if exit_flag:
          break
      
      # Call Master Subroutine
      back_flag = False

      while not back_flag:

         chosen_option, back_flag = run_ms_window(m_title, m_geometry, c_algo, past_option, bin_filename, box_filename)

         if c_algo == "Option 1 - Back Bottom Left Fill":
            c_option = Option.OPTION1.value
         elif c_algo == "Option 2 - Best Match Fill":
            c_option = Option.OPTION2.value

         past_option, bin_filename, box_filename, bin_params, item_params, terminate = master_sub(chosen_option, c_option, past_option, bin_filename, box_filename, bin_params, item_params)

         if terminate:
             break
   
           
   print("Simulation Exit. Thank you for using the simulation.")
   print("==================================================================")
   
   return None

if __name__ == "__main__":
   ms_main()
