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

# Main Window - Warehouse Main UI
class Main_Window():
   
   #--- Constructor ---#
   # Init Window
   def __init__(self) -> None:
      
      # Create GUI Window
      self.window = Tk()
      self.window.title("Storage Optimization in Automated Fulfilment Centers")
      self.window.geometry("500x300")
      self.data = None
      
      # Frame for Content - Grid Layout
      self.content = Frame(self.window)

      # Algorithm Dropdow Menu
      self.approach_field, self.a_select = self.create_dropdown(["Option 1 - Back Bottom Left Fill", "Option 2 - Best Match Fill"], self.content)

      # Data
      self.data = []

      # Start input window
      self.content.pack()
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

      # Heading Label
      heading = Label(self.content, text="Warehouse 3DBPP Simulator", font=("Arial", 20), pady = 10)
      heading.grid(row=0, column=1)
   
      # Approach Label
      approach = Label(self.content, text="Approach", padx = 10, pady = 20)
      approach.grid(row=1, column=0)
      self.approach_field.grid(row=1, column=1, ipadx="100")

      # Buttons - Continue and Clear
      compute_exit = Frame(self.window, pady = 20)
      compute_exit.pack(side = 'bottom')
      compute_button = Button(compute_exit , text = "Continue" , command = self.fetch, bg = "lime")
      exit_button = Button(compute_exit, text = "Exit" , command = self.destroy_window, bg = "red", fg = "white")
      compute_button.pack(side = 'left')
      exit_button.pack(side = 'left', padx = 20)

      # Execute Tkinter
      self.window.mainloop()
      return None
   
   # Fetch Data from Input Fields
   def fetch(self):

      # Fetch Data from window
      approach = self.a_select.get()
      self.data = [approach]

      # Destroy window mainloop and pass control back to main
      self.destroy_window()
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
   
# Master Subroutine Window
class MS_Window():

     def __init__(self) -> None:
      
      # Create GUI Window
      self.window = Tk()
      self.window.title("3DBPP Warehouse Simulation")
      self.window.geometry("500x300")
      self.data = None

      clear_button = Button( self.window , text = "Exit" , command = self.clear )
      clear_button.grid(row=7, column = 2)
      # Clear entry fields

      def clear(self):
     
         # clear the content of text entry box
         self.r_seed_field.delete(0, END)
         self.no_sku_field.delete(0, END)
         self.batch_size_field.delete(0, END)

         return None

   
# Output Window UI
class Output_Window():

   def __init__(self) -> None:
      return None


# Main
def main():
   print("This function is to test the ui programs. ")
   print("This is not the main file. Please run warehouse_main.py instead.")

   iw = Main_Window()

   print("Data That Was Retrieved:")
   data = iw.get_data()
   print(data)

   return None

if __name__ == "__main__":
   main()