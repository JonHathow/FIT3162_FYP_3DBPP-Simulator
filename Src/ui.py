"""
Python Class to handle UI Inputs / Outputs.

Creation Date: 19/8/2023
Authors: How Yu Chern

Classes Implemented (Ref: MCS15_Project_Proposal)
1. Input_Window
2. Container_Window (To Do)
3. Output_Window (To Do)
"""

#Imports
from tkinter import *

# Input Window - Warehouse Main UI
class Input_Window():
   
   #--- Constructor ---#
   # Init Window
   def __init__(self) -> None:
      
      # Create GUI Window
      self.window = Tk()
      self.window.title("3DBPP Warehouse Simulation")
      self.window.geometry("500x300")
      self.data = None

      # Input Fields to Extract Values From
      self.r_seed_field = Entry(self.window)
      self.no_sku_field = Entry(self.window)
      self.batch_size_field = Entry(self.window)
      self.approach_field, self.a_select = self.create_dropdown(["Back Bottom Left Fill", "Corner To Center"])
      self.run_state_field, self.r_select = self.create_dropdown(["Immediate", "Iterate"])
      self.t_cond_field, self.t_select = self.create_dropdown(["Warehouse Full", "75 percent full", "50 percent full", "25 percent full"])

      # Data
      self.data = []

      # Start input window
      self.start_input_window()

   #--- Getters ---#
   # Extract Data
   def get_data(self):
      return self.data
   
   # Get Window
   def get_window(self):
      return self.window
   
   #--- Other Methods ---#
   # Create Input Window
   def start_input_window(self):

      # Create Labels
      heading = Label(self.window, text="Form")
      r_seed = Label(self.window, text="Random Seed")
      no_sku = Label(self.window, text="No. of SKUs")
      batch_size = Label(self.window, text="Batch Size")
      approach = Label(self.window, text="Approach")
      run_state = Label(self.window, text="Run State")
      t_cond = Label(self.window, text="Terminate When")

      # Label Grid Layout
      heading.grid(row=0, column=1)
      r_seed.grid(row=1, column=0)
      no_sku.grid(row=2, column=0)
      batch_size.grid(row=3, column=0)
      approach.grid(row=4, column=0)
      run_state.grid(row=5, column=0)
      t_cond.grid(row=6, column=0)

      # Input Field Grid Layout
      self.r_seed_field.grid(row=1, column=1, ipadx="100")
      self.no_sku_field.grid(row=2, column=1, ipadx="100")
      self.batch_size_field.grid(row=3, column=1, ipadx="100")
      self.approach_field.grid(row=4, column=1, ipadx="100")
      self.run_state_field.grid(row=5, column=1, ipadx="100")
      self.t_cond_field.grid(row=6, column=1, ipadx="100")

      # Buttons
      compute_button = Button( self.window , text = "Compute" , command = self.fetch )
      compute_button.grid(row=7, column = 1)

      clear_button = Button( self.window , text = "Clear" , command = self.clear )
      clear_button.grid(row=7, column = 2)

      # Execute Tkinter
      self.window.mainloop()

      return None
   
   # Fetch Data from Input Fields
   def fetch(self):

      if self.r_seed_field.get() != "" and self.no_sku_field.get() != "" and self.batch_size_field.get() != "":
         r_seed = self.r_seed_field.get()
         no_sku = self.no_sku_field.get()
         batch_size = self.batch_size_field.get()
         approach = self.a_select.get()
         r_state = self.r_select.get()
         t_cond = self.t_select.get()

         self.data = [r_seed, no_sku, batch_size, approach, r_state, t_cond]
         # print(self.data)

         # Destroy window mainloop and pass control back to main
         self.window.destroy()

      else:
         print("Input Fields Empty")
         self.data = "Error - Input Fields Empty"

      return self.data

   # Clear entry fields
   def clear(self):
     
      # clear the content of text entry box
      self.r_seed_field.delete(0, END)
      self.no_sku_field.delete(0, END)
      self.batch_size_field.delete(0, END)

      return None

   # Create Dropdown Menus - Approach, Run State, Termination Condition
   def create_dropdown(self, options):
      
      # Initial Menu Option
      select = StringVar()
      select.set(options[0])
  
      # Create Dropdown menu
      dropdown = OptionMenu( self.window , select , *options)

      return dropdown, select
   
# Container Window UI
class Container_Window():

   def __init__(self) -> None:
      return None
   
# Output Window UI
class Output_Window():

   def __init__(self) -> None:
      return None


# Main
def main():
   print("This function is to test the ui programs. ")
   print("This is not the main file. Please run warehouse_main.py instead.")

   iw = Input_Window()

   print("Data Retrieved")
   data = iw.get_data()
   print(data)

   return None

if __name__ == "__main__":
   main()