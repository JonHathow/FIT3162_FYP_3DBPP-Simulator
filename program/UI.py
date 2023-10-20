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
7. Load_CSV Window
8. Output Window
"""

# Imports
from tkinter import *
from tkinter import filedialog
from manage_csv.input_parameters import InputBinParameters
from manage_csv.input_parameters import InputBoxParameters
from manage_csv.constants import *

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

      if self.data is not None:
         return self.data
      else: 
         print("No data retrieved from user.")
         return None
         
   
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
   # Pack Window
   def pack_window(self):

      # Pack and publish
      self.header.pack()
      self.body.pack()
      self.footer.pack(side = 'bottom')
      return None

   # Start Window
   def start_window(self):

      # Place Window at Center of Screen
      self.pack_window()
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
   def __init__(self, title, geometry, algorithms, past_option = None, past_calgo = None, bin_filename = None, box_filename = None) -> None:
      
      # Create GUI Window
      super().__init__(title, geometry)

      # Algorithm Dropdow Menu and Exit Flag
      self.exitflag = False
      self.approach_field, self.a_select = self.create_dropdown(algorithms, self.body)

      # Previous Run State Parameters
      self.past_option = past_option
      self.past_calgo = past_calgo
      self.bin_filename = bin_filename
      self.box_filename = box_filename

      # Initialize Window Content
      self.initialize_content()
      return None

   # Create Window Content
   def initialize_content(self):

      # ----- Header ----- #
      heading = Label(self.header, text="Warehouse 3DBPP Simulator", font=("Arial", 20), pady = 10)
      heading.grid(row=0, column=0)
      desc = Label(self.header, text="This program simulates the solving of 3 Dimensional Bin Packing Problem", font=("Arial", 12))
      desc.grid(row=1, column=0)
      desc2 = Label(self.header, text="using existing Solution Algorithms", font=("Arial", 12))
      desc2.grid(row=2, column=0)
   
      # ----- Body ----- #
      guide = Label(self.body, text="Select a Solution Algorithm to Continue", font=("Arial", 15), pady = 5)
      guide.grid(row=1, column=0)
      self.approach_field.grid(row=2, column=0, pady = 5)

      # ----- Body - Previous Run Status ----- #
      if self.past_option is not None and self.past_calgo is not None and self.bin_filename is not None and self.box_filename is not None:
         pr_prompt = Label(self.body, text= "Previously Run: {}" .format(self.past_calgo), font=("Arial", 15))
         pr_prompt.grid(row=3, column=0)
         pr_status = Label(self.body, text= "On CSV files: {} and {}".format(self.bin_filename, self.box_filename), font=("Arial", 12))
         pr_status.grid(row=4, column=0)

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
   def __init__(self, title, geometry, chosen_algorithm, options, past_option = None, bin_filename = None, box_filename = None) -> None:

      # Create GUI Window
      super().__init__(title, geometry)

      # Chosen Algorithm and Back Status
      self.c_algorithm = chosen_algorithm
      self.backflag = False

      # Additional Frames
      self.body_second = Frame(self.window)
      self.body_third = Frame(self.window)

      # Additional Functionalities
      self.past_option = past_option
      self.bin_filename = bin_filename
      self.box_filename = box_filename

      # Options Dropdow Menu
      self.options_field, self.o_select = self.create_dropdown(options, self.body)

      # Initialize Window Content
      self.initialize_content()
      return None
   
   # Create Window Content
   def initialize_content(self):

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

      
      # ----- Body Second: Info of Last Selected Option ----- #
      # Recording of Past Options
      if self.past_option is None:
         options_prompt = "No Options Chosen Yet"
      else:
         options_prompt = self.past_option

      options_status = Label(self.body_second, text=options_prompt, font=("Arial", 15))
      options_status.grid(row=0, column=0)

      # CSV Files Tracker
      if self.bin_filename is None and self.box_filename is None:
         csv_prompt = "Load CSV Files to Continue"
      elif self.bin_filename is None:
         csv_prompt = "Please Load Bin CSV File"
      elif self.box_filename is None:
         csv_prompt = "Please Load Box CSV File"
      elif self.bin_filename is not None and self.box_filename is not None:
         csv_prompt = "You May run Compute Algorithm"

      csv_status = Label(self.body_second, text=csv_prompt, font=("Arial", 13))
      csv_status.grid(row=1, column=0)

      # ----- Body Third: Loaded CSVs Info ----- #
      bin_csv_label = Label(self.body_third, text="Loaded Bin CSV:", font=("Arial", 12))
      bin_csv_label.grid(row=0, column=0)
      box_csv_label = Label(self.body_third, text="Loaded Box CSV:", font=("Arial", 12))
      box_csv_label.grid(row=1, column=0)

      bin_csv_status = Label(self.body_third, text= self.bin_filename if self.bin_filename is not None else "None", font=("Arial", 12))
      bin_csv_status.grid(row=0, column=1)
      box_csv_status = Label(self.body_third, text= self.box_filename if self.box_filename is not None else "None", font=("Arial", 12))
      box_csv_status.grid(row=1, column=1)

   
      # ----- Footer ----- #
      compute_button = Button(self.footer , text = "Continue" , command = self.fetch, bg = "lime")
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

      # Fetch Data from window
      self.data = self.o_select.get()

      # Destroy window mainloop and pass control back to main
      self.destroy_window()
      return None
   
      # Pack Window
   def pack_window(self):

      # Pack and publish
      self.header.pack()
      self.body.pack(pady = 5)
      self.footer.pack(side = 'bottom')
      self.body_third.pack(side = 'bottom', pady = 3)
      self.body_second.pack(side = 'bottom', pady = 3)
      return None
   
##############################################################################
# 4. Create New Bin UI - Same for both option 1 and 2
class Bin_Window(Parent_Window):

   # --- Constructor --- #
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

      # ----- Header ----- #
      # Heading Label
      heading = Label(self.header, text="Create New Bin CSV", font=("Arial", 20), pady = 10)
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

      # Return Data in New Format - Quantity, Width, Height, Depth, Capacity.
      # But check if data was retrieved (is not nothing) first.
      if self.data is not None:
          return InputBinParameters(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4])
      else: 
         print("No data retrieved from user.")
         return None

   # Check if "Back" button is pressed.
   def get_backflag(self):
      return self.backflag
   
   # --- Utility --- #
   # Fetch Algorithm - Override
   def fetch(self):

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

   # --- Constructor --- #
   # Init
   def __init__(self, title, geometry, chosen_algorithm, entries, range_entries) -> None:

      # Create GUI Window
      super().__init__(title, geometry)

      # Chosen Algorithm and Back Status
      self.c_algorithm = chosen_algorithm
      self.backflag = False

      # Entries
      self.entries = entries
      self.range_entries = range_entries

      # Second Body for Ranges
      self.header_second = Frame(self.window, pady=5)
      self.body_second = Frame(self.window, pady=5)

      self.setup_content()
   
   # Create Window Content
   def setup_content(self):

      self.initialize_content()
      self.start_window()

   # Create Content Auxiliary Method
   def initialize_content(self):

      # Call Super - Method Override
      super().initialize_content()

      # ----- Header ----- #
      # Heading Label
      heading = Label(self.header, text="Chosen Algorithm: {}".format(self.c_algorithm), font=("Arial", 18), pady = 10)
      heading.grid(row=0, column=0)

      # Chosen Algorithm
      h_guide = Label(self.header, text= "Please Input Box Details (Positive Numbers):", font=("Arial", 15))
      h_guide.grid(row=1, column=0)

      # ----- Body ----- #
      # Box Variables - Integer Types
      # Number of Boxes
      self.labels = self.create_input_labels(self.entries, 0)
      self.fields = self.create_input_fields(self.entries, 1)

      # 2nd Body Guide Text
      self.b2_guide = Label(self.header_second, text = "Input Number Ranges (Low to High)", font=("Arial", 12))
      self.b2_guide.grid(row=0, column=0)

      # Range Variables - Integer Types
      # Ranges - quantity range = (qty_lo, qty_hi), dimensions range (WHD) = (dim_lo, dim_hi), weight range = (wgt_lo, wgt_hi)
      range_lab, range_field = self.range_input_fields(self.range_entries)
      self.labels += range_lab
      self.fields += range_field
   
      # ----- Footer ----- #
      compute_button = Button(self.footer, text = "Create" , command = self.fetch, bg = "lime")
      clear_button = Button(self.footer, text = "Clear" , command = self.clear, bg = "yellow")
      exit_button = Button(self.footer, text = "Back" , command = self.back, bg = "red", fg = "white")
      compute_button.pack(side = 'left')
      clear_button.pack(side = 'left', padx = 20)
      exit_button.pack(side = 'left', padx = 20)

      return None
    
   # --- Getters --- #
   # Get Data - Override
   def get_data(self):

      # Return Data in New Format
      # Number of Boxes, quantity range = (qty_lo, qty_hi), dimensions range (WHD) = (dim_lo, dim_hi), weight range = (wgt_lo, wgt_hi)
      if self.data is not None:
          return InputBoxParameters(self.data[0], min(self.data[1], self.data[2]), max(self.data[1], self.data[2]), min(self.data[3], self.data[4]), max(self.data[3], self.data[4]), min(self.data[5], self.data[6]), max(self.data[5], self.data[6]))
      else: 
         print("No data retrieved from user.")
         return None

   # Get Backflag - If Back Button is Pressed
   def get_backflag(self):
      return self.backflag

   # --- Creation Methods --- #
   # Unique Label and Field Creating Method - Creating Ranges (Low, High) Input
   def range_input_fields(self, range_entries):
      
      entries = []
      fields = []

      for i in range(len(range_entries)):

         # Labels
         entries.append(Label(self.body_second, text = range_entries[i], padx = 10))
         entries[i].grid(row = i, column = 0)

         # (Low , High) Tuple
         low = Entry(self.body_second)
         low.grid(row = i, column = 1)

         Label(self.body_second, text = " to ").grid(row = i, column = 2)

         high = Entry(self.body_second)
         high.grid(row = i, column = 3)

         fields.append(low)
         fields.append(high)

      return entries, fields
  
   # --- Utility Methods --- #
   # Back Button
   def back(self):
      self.backflag = True
      self.destroy_window()
      return None
   
   # Pack Window - Override
   def pack_window(self):
      
      # Pack and publish - With Second Body
      self.header.pack()
      self.body.pack()
      self.header_second.pack()
      self.body_second.pack()
      self.footer.pack(side = 'bottom')

      return None

   # Fetch Algorithm - Override
   def fetch(self):

      self.fetch_aux()
      print(self.data)

      # Destroy window mainloop and pass control back to main
      self.destroy_window()
   
   # Fetch Auxiliary Method
   def fetch_aux(self):

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

# 6. Create New Box UI - Option 1 - Which has a few more parameters than Option 2
class Box_Window_O1(Box_Window_O2):
   
   # --- Constructor --- #
   # Init
   def __init__(self, title, geometry, chosen_algorithm, entries, range_entries, bool_entries) -> None:

      # Boolean Variables
      self.bool_entries = bool_entries

      # Create GUI Window
      super().__init__(title, geometry, chosen_algorithm, entries, range_entries)

      return None
   
   # Setup Content - Override
   def setup_content(self):
      # Due to the way the command flow works in Box_Window_02, put new frames in the Setup Content Method.
      # Third Body - Boolean Variables
      self.body_third = Frame(self.window, pady = 10)
      self.initialize_content()
   
   # Initialize Content - Override
   def initialize_content(self):

      # Method Override
      super().initialize_content()

      # Boolean Variables - Integer Types
      # Booleans (Yes/No) - "Allow Varying Priority Levels", "Allow Varying Loading Orientations", "Allow Upside Down Loading"
      self.entries, self.bool_buttons = self.bool_input_fields(self.bool_entries)
      # print(self.bool_buttons[0].cget('text'))

      # 2nd Button - "Allow Varying Loading Orientations" makes it so that 3rd Button - "Allow Upside Down Loading" is default False if No.2 is True
      self.bool_buttons[1].config(command=self.toggle_activity)
      self.bool_buttons[2].config(state = DISABLED)
      self.bool_buttons[2].config(text = "Disabled")

      self.start_window()
   
   # --- Creation Methods --- #
   # Unique Boolean Field Create Method
   def bool_input_fields(self, bool_entries):

      entries = []
      bool_buttons = []

      for i in range(len(bool_entries)):

         # Labels
         entries.append(Label(self.body_third, text = bool_entries[i], padx = 10))
         entries[i].grid(row = i, column = 0)

         # Boolean Buttons - Have to be created manually for now since list[i].pack() or any other function does not work.
         bool_button = Button(self.body_third, text="Yes", width=12, relief="raised")
         bool_button['command']= lambda a=bool_button:self.flip(a)
         bool_button.grid(row = i, column = 1)

         bool_buttons.append(bool_button)
      
      return entries, bool_buttons
   
   # Toggle Button Activity - Allow 2nd button to toggle activity of 3rd button
   def toggle_activity(self):

      button1 = self.bool_buttons[1]
      button2 = self.bool_buttons[2]

      if button1.config('relief')[-1] == 'sunken':
        button2.config(state = DISABLED)
        button2.config(text = "Disabled")
      elif button1.config('relief')[-1] == 'raised':
        button2.config(state = NORMAL)
        button2.config(text = "Yes")

      self.flip(button1)

      pass

   # Flip Boolean Button - Yes/No
   def flip(self, button):
      
      if button.config('relief')[-1] == 'raised':
        button.config(relief="sunken")
        button.config(text="No")
      else:
        button.config(relief="raised")
        button.config(text="Yes")

      # print(button.cget('text'))

   # --- Getters --- #
   # Get Data - Override
   def get_data(self):

      # Return Data in New Format
      # Number of Boxes, quantity range = (qty_lo, qty_hi), dimensions range (WHD) = (dim_lo, dim_hi), weight range = (wgt_lo, wgt_hi)
      if self.data is not None:
          ibp = InputBoxParameters(self.data[0], min(self.data[1], self.data[2]), max(self.data[1], self.data[2]), min(self.data[3], self.data[4]), max(self.data[3], self.data[4]), min(self.data[5], self.data[6]), max(self.data[5], self.data[6]))
          
          # True / Falses - "Allow Varying Priority Levels", "Allow Varying Loading Orientations", "Allow Upside Down Loading" - False if No.2 is True
          if self.data[-2]: # updown_var
            self.data[-1] = False # updown
         
          ibp.set_option1_params(self.data[-3], self.data[-2], self.data[-1])
          return ibp
      else: 
         print("No data retrieved from user.")
         return None
   
   # --- Utility Methods --- #
   # Clear - Override
   def clear(self):
      # Call Super
      super().clear()

      # Reset Buttons
      for button in self.bool_buttons:
         button.config(relief="raised")
         button.config(text="Yes")

   # Fetch - Override
   def fetch(self):

      # Super Call Fetch Aux to not trigger "destroy window" early
      self.fetch_aux()

      # Fetch Button Bool Values
      print(self.bool_buttons)

      for i in range(len(self.bool_buttons)):

         b_val = self.bool_buttons[i].cget('text')

         if b_val == "Yes":
            self.data.append(True)
         elif b_val == "No":
            self.data.append(False)
      
      print(self.data)

      # Destroy Window
      self.destroy_window()

   # Fetch Auxiliary - Super Call
   def fetch_aux(self):
      return super().fetch_aux()
   
   # Pack Window - Override
   def pack_window(self):
      
      # Pack and publish - With Second Body
      self.header.pack()
      self.body.pack()
      self.header_second.pack()
      self.body_second.pack()
      self.body_third.pack()
      self.footer.pack(side = 'bottom')

      return None
      

##############################################################################
# 7. Load_CSV_Window
class Load_CSV_Window(Parent_Window):

   # --- Constructor --- #
   # Init - Override
   def __init__(self, choosen_algorithm, filetype) -> None:
      
      self.window = Tk()
      self.choosen_algorithm = choosen_algorithm
      self.filetype = filetype
      self.data = None
      self.load_csv()
      return None
   
   # Load CSV
   def load_csv(self):
      
      # Open Appropriate Directory
      self.dir = None 

      if self.choosen_algorithm == Option.OPTION1.value and self.filetype ==  FILE_BIN:
         self.dir = FOLDER_BIN_1  
      elif self.choosen_algorithm == Option.OPTION1.value and self.filetype ==  FILE_BOX:   
         self.dir = FOLDER_BOX_1
      elif self.choosen_algorithm == Option.OPTION2.value and self.filetype ==  FILE_BIN:
         self.dir = FOLDER_BIN_2
      elif self.choosen_algorithm == Option.OPTION2.value and self.filetype ==  FILE_BOX:
         self.dir = FOLDER_BOX_2
      else:
         raise Exception("Choosen Algorithm and File Type Provided is Incorrect Format / Non-Existent")

      # Load File
      prompt = "Open a {} CSV File from within This Directory or Select Cancel to Go Back".format(self.filetype)
      filename = ""

      while not self.filename_check(filename):
         filename = filedialog.askopenfilename(initialdir = self.dir,
                                             title = prompt,
                                             filetypes=[("CSV files", "*.csv")]
                                             ,parent = self.window)
      
         # Check if "Cancel" was selected
         if filename == "":
            filename = "Canceled"
            break
         
         if not self.filename_check(filename):
            prompt = "Incorrect {} File Selected. Open a {} CSV File from within This Directory or Select Cancel to Go Back".format(self.filetype, self.filetype)


      # Return filename status
      if filename != "Canceled":
         self.data = self.filename_shorten(filename)
         print(self.dir)

      self.destroy_window()
   
   # --- Utility Methods --- #
   # Verify Correct File Path - In Case User wanders to different directories in file explorer
   def filename_check(self, filename):

      flag = False

      # Parse File Paths
      dir = self.dir
      dir_paths = dir.split("\\")
      # print(dir_paths)
      
      file_paths = filename.split("/")
      file_paths = file_paths[-4:-1]
      # print(file_paths)

      # Check if Retrieved File Path matches original Dir
      if file_paths == dir_paths:
         flag = True

      # print (flag)
      return flag
   
   # Shorten File Path
   def filename_shorten(self, filename):

      file_paths = filename.split("/")
      file_paths = file_paths[-4:]

      f_short = ""

      for i in range(len(file_paths)):

         if i == 0:
            f_short += file_paths[i]
         else:
            f_short += "\\" + file_paths[i]
      
      return f_short

   
##############################################################################
# 8. Output_Window
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
   print("This is not the main file. Please run Main.py instead.")
   print("Reference: Methods of This Class used mainly in Mastet_Input.py")


   # --- Params --- #

   # Core Params
   m_title = "Storage Optimization in Automated Fulfilment Centers"
   m_geometry = "600x400"
   bin_params = ["Quantity", "Width", "Height", "Depth", "Capacity"]

   # Box Param Option 1 & Option 2
   # These 3 are Boolean - "Allow Varying Priority Levels", "Allow Varying Loading Orientations", "Allow Upside Down Loading" - Only if No.2 is False.
   # If No. 2 is True, no. 3 is always False.
   bparams_normal = ["Number of Boxes"]
   bparams_ranges = ["Quantity Range", "Dimensions Range", "Weight Range"]
   bparams_boolean = ["Allow Varying Priority Levels", "Allow Varying Loading Orientations", "Allow Upside Down Loading"]

   # --- Tests --- #
   # Main Window Test
   """
   print("Main Window Test")
   iw = Main_Window(title = "Storage Optimization in Automated Fulfilment Centers", geometry = "500x300")

   print("Data That Was Retrieved:")
   data = iw.get_data()
   print(data)
   """

   # Bin Window Test
   """
   print("Bin Window Test")
   bw = Bin_Window(m_title, m_geometry, bin_params)
   inputparam = bw.get_data()
   print(inputparam)
   """
 
   # Box Window Test - Option 2
   """
   print("Box Window Test - Option 2")
   bin_window_2 = Box_Window_O2(m_title, m_geometry, "Option 2 - Best Match Fill", bparams_normal, bparams_ranges)
   print(bin_window_2.get_data())
   print(bin_window_2.backflag)
   """

   # Box Window Test - Option 1
   """
   print("Box Window Test - Option 1")
   bin_window_1 = Box_Window_O1(m_title, m_geometry, "Option 1 - Back Bottom Left Fill", bparams_normal, bparams_ranges, bparams_boolean)
   print(bin_window_1.get_data())
   """

   # Load CSV Window Test
   """
   lw_filename = Load_CSV_Window(Option.OPTION2.value, FILE_BOX)
   print(lw_filename.get_data())
   """

   return None

if __name__ == "__main__":
   main()