""" Handles writing and reading of CSV files for Option 2. """

from manage_csv.constants import File, Option, MENU_INPUT, MENU_INVALID, MENU_BIN_NOTLOADED, MENU_BOX_NOTLOADED, MENU_END, FILE_BIN_2, FILE_BOX_2
from manage_csv.write_input_bin import write_input_bin_func
from manage_csv.write_input_box import write_input_box_func
from manage_csv.read_input_csv import read_input
from write_output_option2 import output_master
from Option2_package import Packer, Bin, Item, Painter

# TODO: Check to see if rendering works for multiple boxes.

def O2_Input():

    bins_loaded = False
    boxes_loaded = False

    while True:

        response = input(MENU_INPUT)

        # Write a CSV file for bins.
        if response == "1":
            write_input_bin_func(Option.OPTION2.value)

        # Write a CSV file for boxes.
        elif response == "2":
            write_input_box_func(Option.OPTION2.value)

        # Read a CSV file for bins.
        elif response == "3":
            bin_params = read_input(FILE_BIN_2, File.BIN.value, Option.OPTION2.value)
            bins_loaded = True if bin_params is not None else False

        # Read a CSV file for boxes.
        elif response == "4":
            item_params = read_input(FILE_BOX_2, File.BOX, Option.OPTION2)
            boxes_loaded = True if item_params is not None else False

        elif response == "5":

            if not bins_loaded or not boxes_loaded:
                if not bins_loaded:
                    print(MENU_BIN_NOTLOADED)
                if not boxes_loaded:
                    print(MENU_BOX_NOTLOADED)

            else:
                # Initialize packing function.
                packer = Packer()

                # Initialize bins.
                for b in bin_params:
                    name = b[0]
                    width = float(b[1])
                    height = float(b[2])
                    depth = float(b[3])
                    capacity = float(b[4])
                    packer.add_bin(Bin(name, width, depth, height, capacity))
                
                # Initialize items.
                for item in item_params:
                    name = item[0]
                    width = float(item[1])
                    depth = float(item[2])
                    height = float(item[3])
                    weight = float(item[4])
                    color = item[5]
                    packer.add_item(Item(name, width, depth, height, weight, color))

                # Compute packing.
                packer.pack()
                for b in packer.bins:
                    painter = Painter(b)
                    fig = painter.plotBoxAndItems(
                            title = b.size,
                            alpha = 0.8,
                            write_num = False,
                            fontsize = 10
                        )
                fig.show()
                output_master(packer)

        elif response == "0":
            print(MENU_END)
            break

        else:
            print(MENU_INVALID)

# Test Run
if __name__ == "__main__":
   O2_Input()