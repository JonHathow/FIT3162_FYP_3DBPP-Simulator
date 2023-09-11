""" Handles writing and reading of CSV files for Option 2. """

from manage_csv.constants import Mode, Option, MENU_INPUT, MENU_INVALID, MENU_BIN_NOTLOADED, MENU_END, FILE_BIN_2, FILE_BOX_2
from manage_csv.write_input_bin import write_input_bin_func
from manage_csv.write_input_box import write_input_box_func
from manage_csv.read_input_csv import read_input
from Option2_package import Packer, Bin, Item

def O2_input():

    bins_loaded = False
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
            bin_params = read_input(FILE_BIN_2, Mode.BIN.value)

            if bin_params is not None:

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

                bins_loaded = True

        # Read a CSV file for boxes.
        elif response == "4":

            if not bins_loaded:
                print(MENU_BIN_NOTLOADED)

            else:
                item_params = read_input(FILE_BOX_2, Mode.BOX.value)

                if item_params is not None:
                    for item in item_params:
                        name = item[0]
                        width = float(item[1])
                        depth = float(item[2])
                        height = float(item[3])
                        weight = float(item[4])
                        packer.add_item(Item(name, width, depth, height, weight))

                packer.pack()

        elif response == "0":
            print(MENU_END)
            break

        else:
            print(MENU_INVALID)