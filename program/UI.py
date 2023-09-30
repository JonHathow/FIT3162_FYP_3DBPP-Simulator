"""
Python Class to handle UI Inputs / Outputs.

Creation Date: 19/8/2023
Authors: How Yu Chern

Classes Implemented
1. Parent_Window (Parent Class)
2. Main_Window
3. MS_Window (Master Subroutine Window)
4. Bin_Input Window
5. Box_Input_O1 Window - Option 2 - Defined first as a parent to Option 1's Window
6. Box_Input_O1 Window - Option 1 - Has a few more perimeters than Option 2
7. Output Window
"""

# Imports
from tkinter import *
from manage_csv.input_parameters import InputBinParameters

##############################################################################
# 1. General Purpose - Parent Window
# Contains all common functionality of Windows
class Parent_Window():

   # --- Constructor --- #
   # Init Window
   def __init__(self, title, geometry) -> None:

      # ----- Create GUI Window ----- #
      self.window = Tk()
      self.window.title(title)
      self.window.geometry(geometry)
      self.data = None
      self.labels = None
      self.fields = None
      
      # ----- Section Frames ----- #
      # 1. Header - Title and Guides
      # 2. Body - Input Fields, etc.
      # 3. Footer - Buttons
      self.header = Frame(self.window)
      self.body = Frame(self.window)
      self.footer = Frame(self.window, pady = 20)
      return None
   
   # Create Window Content - Center Content is unique for each window
   def initialize_content(self):
      # To Override
      return None
   
   #--- Getters ---#
   # Extract Data
   def get_data(self):
      return self.data
   
   # Get Window
   def get_window(self):
      return self.window
   
   # --- Creation Methods --- #
   # Create Input Labels
   def create_input_labels(self, entries, col):
      
      labels = []

      for i in range(len(entries)):
         labels.append(Label(self.body, text = entries[i], padx = 10))
         labels[i].grid(row = i, column = col)

      return labels
   
   # Create Input Fields - To be used together with create_input_labels
   def create_input_fields(self, entries, col):
      
      fields = []

      for i in range(len(entries)):
         fields.append(Entry(self.body))
         fields[i].grid(row = i, column = col)

      return fields
   
   # Create Dropdown Menus - Approach, Run State, Termination Condition
   def create_dropdown(self, options, window):
      
      # Initial Menu Option
      select = StringVar()
      select.set(options[0])
  
      # Create Dropdown menu
      dropdown = OptionMenu( window , select , *options)

      return dropdown, select
   
   # --- Utility Methods --- #
   # Start Window
   def start_window(self):

      # Pack and publish
      self.header.pack()
      self.body.pack()
      self.footer.pack(side = 'bottom')

      # Place Window at Center of Screen
      self.window.eval('tk::PlaceWindow . center')
      self.window.mainloop()
      return None
   
   # Fetch Data from Input Fields
   def fetch(self):
      # To Override
      return None

   # Clear Fields
   def clear(self):

      # clear the content of all entry fields present
      if self.fields is not None:
         for i in range(len(self.fields)):
            self.fields[i].delete(0, END)

      return None
   
   # Destroy Window
   def destroy_window(self):
      self.window.destroy()
      return None
   
##############################################################################
# 2. Main Window - Warehouse Main UI
class Main_Window(Parent_Window):
   
   #--- Constructor ---#
   # Init Window
   def __init__(self, title, geometry, algorithms) -> None:
      
      # Create GUI Window
      super().__init__(title, geometry)

      # Algorithm Dropdow Menu and Exit Flag
      self.exitflag = False
      self.approach_field, self.a_select = self.create_dropdown(algorithms, self.body)

      # Initialize Window Content
      self.initialize_content()
      return None

   # Create Window Content
   def initialize_content(self):

      # Call Super - Method Override
      super().initialize_content()

      # ----- Header ----- #
      heading = Label(self.header, text="Warehouse 3DBPP Simulator", font=("Arial", 20), pady = 10)
      heading.grid(row=0, column=0)
   
      # ----- Body ----- #
      guide = Label(self.body, text="Select a Solution Algorithm to Continue", font=("Arial", 15))
      guide.grid(row=1, column=0)
      self.approach_field.grid(row=2, column=0, pady = "10")

      # ----- Footer ----- #
      # Buttons - Continue and Clear
      compute_button = Button(self.footer , text = "Continue" , command = self.fetch, bg = "lime")
      exit_button = Button(self.footer, text = "Exit" , command = self.exit, bg = "red", fg = "white")
      compute_button.pack(side = 'left')
      exit_button.pack(side = 'left', padx = 20)

      # Start Window
      self.start_window()
      return None
   
   #--- Getters ---#
   # Get Exit Flag
   def get_exitflag(self):
      return self.exitflag
   
   #--- Utility ---#
   # Fetch Algorithm - Override
   def fetch(self):

      # Method Override
      super().fetch()

      # Fetch Data from window
      self.data = self.a_select.get()

      # Destroy window mainloop and pass control back to main
      self.destroy_window()
      return None
   
   # Exit Program
   def exit(self):
      self.exitflag = True
      self.destroy_window()

##############################################################################
# 3. Master Subroutine Window
# To choose options - creating bin / box csv file, loading bin / box csv file, compute algorithm
class MS_Window(Parent_Window):
   
   #--- Constructor ---#
   # Init Window
   def __init__(self, title, geometry, chosen_algorithm, options) -> None:

      # Create GUI Window
      super().__init__(title, geometry)

      # Chosen Algorithm and Back Status
      self.c_algorithm = chosen_algorithm
      self.backflag = False

      # Options Dropdow Menu
      self.options_field, self.o_select = self.create_dropdown(options, self.body)

      # Initialize Window Content
      self.initialize_content()
      return None
   
   # Create Window Content
   def initialize_content(self):

      # Call Super - Method Override
      super().initialize_content()

      # ----- Header ----- #
      # Heading Label
      heading = Label(self.header, text="Chosen Algorithm:", font=("Arial", 20), pady = 10)
      heading.grid(row=0, column=0)

      # Chosen Algorithm (From Main Window)
      c_algorithm = Label(self.header, text=self.c_algorithm, font=("Arial", 15), bg = "Yellow")
      c_algorithm.grid(row=1, column=0)
      
      # ----- Body ----- #
      options_heading = Label(self.body, text="Select Option:", padx = 10, pady = 20)
      options_heading.grid(row=0, column=0)
      self.options_field.grid(row=0, column=1, padx=10)
   
      # ----- Footer ----- #
      compute_button = Button(self.footer , text = "Compute" , command = self.fetch, bg = "lime")
      exit_button = Button(self.footer, text = "Back" , command = self.back, bg = "red", fg = "white")
      compute_button.pack(side = 'left')
      exit_button.pack(side = 'left', padx = 20)

      # Start Window
      self.start_window()
      return None
   
   # --- Getters --- #
   # Check if "Back" button is pressed.
   def get_backflag(self):
      return self.backflag
   
   # --- Utility --- #
   # Back Button Function
   def back(self):
      self.backflag = True
      self.destroy_window()
      return None
   
   # Fetch Algorithm - Override
   def fetch(self):

      # Method Override
      super().fetch()

      # Fetch Data from window
      self.data = self.o_select.get()

      # Destroy window mainloop and pass control back to main
      self.destroy_window()
      return None
   
##############################################################################
# 4. Create New Bin UI - Same for both option 1 and 2
class Bin_Window(Parent_Window):

   # Init
   def __init__(self, title, geometry, entries) -> None:

      # Create GUI Window
      super().__init__(title, geometry)
      self.backflag = False
      self.entries = entries

      self.initialize_content()
      return None
   
    # Create Window Content
   def initialize_content(self):

      # Call Super - Method Override
      super().initialize_content()

      # ----- Header ----- #
      # Heading Label
      heading = Label(self.header, text="Create New Bin", font=("Arial", 20), pady = 10)
      heading.grid(row=0, column=0)
      heading = Label(self.header, text="Enter Bin Details (Positive Units):", font=("Arial", 15), pady = 5)
      heading.grid(row=1, column=0)

      # ----- Body ----- #
      # Bin Variables - Integer Types
      # Quantity, Width, Height, Depth, Capacity20
      self.labels = self.create_input_labels(self.entries, 0)
      self.fields = self.create_input_fields(self.entries, 1)

      # ----- Footer ----- #
      compute_button = Button(self.footer, text = "Create" , command = self.fetch, bg = "lime")
      clear_button = Button(self.footer, text = "Clear" , command = self.clear, bg = "yellow")
      exit_button = Button(self.footer, text = "Back" , command = self.back, bg = "red", fg = "white")
      compute_button.pack(side = 'left')
      clear_button.pack(side = 'left', padx = 20)
      exit_button.pack(side = 'left', padx = 20)

      # Start Window
      self.start_window()
      return None

   # --- Getters --- #
   # Get Data - Override
   def get_data(self):

      # Method Override
      super().get_data()

      # Return Data in New Format - Quantity, Width, Height, Depth, Capacity.
      print(self.data)
      return InputBinParameters(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4])

   # Check if "Back" button is pressed.
   def get_backflag(self):
      return self.backflag
   
   # --- Utility --- #
   # Fetch Algorithm - Override
   def fetch(self):

      # Method Override
      super().fetch()
      self.data = []

      # Fetch Data from window
      for i in range(len(self.fields)):
         
         # Field Ret Val is String Form
         field_val = self.fields[i].get()

         # Null Values Check
         if field_val == '':
            raise Exception("Input must be positive integer, not Null")
         
         # Positive Integers Only Check
         if field_val.isdigit():
            field_val = abs(int(field_val))
            self.data.append(field_val)
         else:
            raise Exception("Input must be positive integer, not negative integers, or other types like String")

      # Destroy window mainloop and pass control back to main
      self.destroy_window()
      return None
   
   # Back Button
   def back(self):
      self.backflag = True
      self.destroy_window()
      return None
   
##############################################################################
# 5. Create New Box UI - Option 2 
class Box_Window_O2(Parent_Window):

   # Init
   def __init__(self, title, geometry, chosen_algorithm, entries) -> None:

      # Create GUI Window
      super().__init__(title, geometry)

      # Chosen Algorithm and Back Status
      self.c_algorithm = chosen_algorithm
      self.backflag = False

      self.initialize_content
   
   # Create Window Content
   def initialize_content(self):

      # Call Super - Method Override
      super().initialize_content()

      # ----- Header ----- #
      # Heading Label
      heading = Label(self.body, text="Chosen Algorithm:", font=("Arial", 20), pady = 10)
      heading.grid(row=0, column=0)

      # Chosen Algorithm
      c_algorithm = Label(self.header, text=self.c_algorithm, font=("Arial", 15), bg = "Yellow")
      c_algorithm.grid(row=1, column=0)

      # ----- Body ----- #
      # Box Variables - Integer Types
      # Number of Boxes, quantity range = (qty_lo, qty_hi), dimensions range (WHD) = (dim_lo, dim_hi), weight range = (wgt_lo, wgt_hi)
      self.labels = self.create_input_labels(self.entries, 0)
      self.fields = self.create_input_fields(self.entries, 1)
   
      # ----- Footer ----- #
      compute_button = Button(self.footer, text = "Create" , command = self.fetch, bg = "lime")
      clear_button = Button(self.footer, text = "Clear" , command = self.clear, bg = "yellow")
      exit_button = Button(self.footer, text = "Back" , command = self.back, bg = "red", fg = "white")
      compute_button.pack(side = 'left')
      clear_button.pack(side = 'left', padx = 20)
      exit_button.pack(side = 'left', padx = 20)

      # Start Window
      self.start_window()
      return None
   
   # Back Button
   def back(self):
      self.backflag = True
      self.destroy_window()
      return None

# 6. Create New Box UI - Option 1 - Which has a few more parameters than Option 2
class Box_Window_O1(Box_Window_O2):
   
   # Init
   def __init__(self, title, geometry) -> None:

      # Create GUI Window
      super().__init__(self, title, geometry)

      # Box Details - Options 1 and 2 Differ

      return None

##############################################################################
# 7. Output_Window
class Output_Window(Parent_Window):

   # Init
   def __init__(self, title, geometry) -> None:

      # Create GUI Window
      super().__init__(self, title, geometry)
      return None

##############################################################################
# Main
def main():
   print("This function is to test the ui programs. ")
   print("This is not the main file. Please run warehouse_main.py instead.")

   """
   Test Program
   iw = Main_Window(title = "Storage Optimization in Automated Fulfilment Centers", geometry = "500x300")

   print("Data That Was Retrieved:")
   data = iw.get_data()
   print(data)
   """

   m_title = "Storage Optimization in Automated Fulfilment Centers"
   m_geometry = "500x300"
   bin_params = ["Quantity", "Width", "Height", "Depth", "Capacity"]

   # Box Param Option 1
   # These 3 are Boolean - "Allow Varying Priority Levels", "Allow Varying Loading Orientations", "Allow Upside Down Loading" - Only if No.2 is False.
   # If No. 2 is True, no. 3 is always False.
   b_params_O1 = ["Number of Boxes", "Quantity Range", "Dimensions Range", "Weight Range", "Allow Varying Priority Levels", "Allow Varying Loading Orientations", "Allow Upside Down Loading"]
   # Box Param Option 2
   b_params_O2 = ["Number of Boxes", "Quantity Range", "Dimensions Range", "Weight Range"]

   # Bin Window Test
   """
   bw = Bin_Window(m_title, m_geometry, bin_params)
   inputparam = bw.get_data()
   print(inputparam)
   """

   # Box Window Test - Option 2
   bw_O2 = Box_Window_O2(m_title, m_geometry, b_params_O2)

   return None

if __name__ == "__main__":
   main()