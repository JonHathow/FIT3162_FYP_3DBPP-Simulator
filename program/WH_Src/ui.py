"""
Python Class to handle UI Inputs / Outputs.

Creation Date: 19/8/2023
Authors: How Yu Chern

Classes Implemented
1. Parent_Window (Parent Class)
2. Main_Window
3. MS_Window (Master Subroutine Window)
4. Bin_Input Window
5. Box_Input Window
6. Output Window
"""

#Imports
from tkinter import *

# General Purpose - Parent Window
# Contains all common functionality of Windows
class Parent_Window():

   #--- Constructor ---#
   # Init Window
   def __init__(self, title, geometry) -> None:

      # Create GUI Window
      self.window = Tk()
      self.window.title(title)
      self.window.geometry(geometry)
      self.data = None
      
      # Frame for Center Content - Grid Layout
      self.content = Frame(self.window)
      self.content.pack()
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
   
   #--- Utility Methods ---#
   # Start Window
   def start_window(self):
      self.content.pack()
      self.window.mainloop()
      return None
   
   # Fetch Data from Input Fields
   def fetch(self):
      # To Override
      return None

   # Destroy Window
   def destroy_window(self):
      self.window.destroy()
      return None
   
   # Create Dropdown Menus - Approach, Run State, Termination Condition
   def create_dropdown(self, options, window):
      
      # Initial Menu Option
      select = StringVar()
      select.set(options[0])
  
      # Create Dropdown menu
      dropdown = OptionMenu( window , select , *options)

      return dropdown, select
   

# Main Window - Warehouse Main UI
class Main_Window(Parent_Window):
   
   #--- Constructor ---#
   # Init Window
   def __init__(self, title, geometry, algorithms) -> None:
      
      # Create GUI Window
      super().__init__(title, geometry)

      # Algorithm Dropdow Menu
      self.approach_field, self.a_select = self.create_dropdown(algorithms, self.content)

      # Initialize Window Content
      self.initialize_content()
      return None

   # Create Window Content
   def initialize_content(self):

      # Call Super - Method Override
      super().initialize_content()

      # ----- Content Frame ----- #
      # Heading Label
      heading = Label(self.content, text="Warehouse 3DBPP Simulator", font=("Arial", 20), pady = 10)
      heading.grid(row=0, column=0)
      guide = Label(self.content, text="Select a Solution Algorithm to Continue", font=("Arial", 15))
      guide.grid(row=1, column=0)
   
      # Approach Label
      # Comment: First Column Size was mad big by "Guide" variable. Hence, other columns are pushed to the side.
      # approach = Label(self.content, text="Approach")
      # approach.grid(row=2, column=0)
      self.approach_field.grid(row=2, column=0, pady = "10")

      # Buttons - Continue and Clear
      compute_exit = Frame(self.window, pady = 20)
      compute_exit.pack(side = 'bottom')
      compute_button = Button(compute_exit , text = "Continue" , command = self.fetch, bg = "lime")
      exit_button = Button(compute_exit, text = "Exit" , command = self.destroy_window, bg = "red", fg = "white")
      compute_button.pack(side = 'left')
      exit_button.pack(side = 'left', padx = 20)

      # Start Window
      self.start_window()
      return None
   
   # Fetch Algorithm - Override
   def fetch(self):

      # Method Override
      super().fetch()

      # Fetch Data from window
      self.data = self.a_select.get()

      # Destroy window mainloop and pass control back to main
      self.destroy_window()
      return None
   
   
# Master Subroutine Window
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
      self.options_frame = Frame(self.window)
      self.options_field, self.o_select = self.create_dropdown(options, self.options_frame)

      # Initialize Window Content
      self.initialize_content()
      return None
   
   # Create Window Content
   def initialize_content(self):

      # Call Super - Method Override
      super().initialize_content()

      # ----- Content Frame ----- #
      # Heading Label
      heading = Label(self.content, text="Chosen Algorithm:", font=("Arial", 20), pady = 10)
      heading.grid(row=0, column=0)

      # Chosen Algorithm (From Main Window)
      c_algorithm = Label(self.content, text=self.c_algorithm, font=("Arial", 15), bg = "Yellow")
      c_algorithm.grid(row=1, column=0)
   
      # ----- Options Frame ----- #
      # Option Label
      options_heading = Label(self.options_frame, text="Select Option:", padx = 10, pady = 20)
      options_heading.grid(row=0, column=0)
      self.options_field.grid(row=0, column=1, padx=10)
      self.options_frame.pack()

      # Buttons - Compute and Back
      compute_exit = Frame(self.window, pady = 20)
      compute_exit.pack(side = 'bottom')
      compute_button = Button(compute_exit , text = "Compute" , command = self.fetch, bg = "lime")
      exit_button = Button(compute_exit, text = "Back" , command = self.back, bg = "red", fg = "white")
      compute_button.pack(side = 'left')
      exit_button.pack(side = 'left', padx = 20)

      # Start Window
      self.start_window()
      return None
   
   #--- Getters ---#
   # Check if "Back" button is pressed.
   def get_backflag(self):
      return self.backflag
   
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
   

# Create New Box UI
class Box_Window(Parent_Window):

   def __init__(self) -> None:
      return None
   
   def clear(self):
     
      # clear the content of text entry box
      self.r_seed_field.delete(0, END)
      self.no_sku_field.delete(0, END)
      self.batch_size_field.delete(0, END)

      return None


# Create New Bin UI
class Bin_Window(Parent_Window):

   def __init__(self) -> None:
      return None


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

   return None

if __name__ == "__main__":
   main()