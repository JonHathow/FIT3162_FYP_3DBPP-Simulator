""" Handles writing and reading of CSV files for Option 1. """

import time
from manage_csv.constants import File, Option, MENU_INPUT, MENU_INVALID, MENU_BIN_NOTLOADED, MENU_BOX_NOTLOADED, MENU_END, FILE_BIN_1, FILE_BOX_1
from manage_csv.write_input_bin import write_input_bin_func
from manage_csv.write_input_box import write_input_box_func
from manage_csv.read_input_csv import read_input
from write_output_option1 import output_master
from Option1_package import Packer, Bin, Item, Painter

# TODO: Check to see if rendering works for multiple boxes.

def O1_Input():
    
    # Fix Inascessible Local Variable Error
    global bin_params, bins_loaded, item_params, boxes_loaded 

    # Essential Params - Init
    bins_loaded = False
    boxes_loaded = False
    bin_params = None
    item_params = None

    while True:

        response = input(MENU_INPUT)

        # Write a CSV file for bins.
        if response == "1":
            write_input_bin_func(Option.OPTION1.value)

        # Write a CSV file for boxes.
        elif response == "2":
            write_input_box_func(Option.OPTION1.value)

        # Read a CSV file for bins.
        elif response == "3":
            bin_params = read_input(FILE_BIN_1, File.BIN.value, Option.OPTION1.value)
            bins_loaded = True if bin_params is not None else False

            print(bin_params)
            print(bins_loaded)

        # Read a CSV file for boxes.
        elif response == "4":
            item_params = read_input(FILE_BOX_1, File.BOX.value, Option.OPTION1.value)
            boxes_loaded = True if item_params is not None else False

            print(item_params)
            print(boxes_loaded)

        # Compute bin packing.
        elif response == "5":
            print(bin_params)
            print(bins_loaded)
            print(item_params)
            print(boxes_loaded)

            print("Compute")
            O1_compute(bin_params, item_params)
        
        elif response == "0":
            print(MENU_END)
            break

        else:
            print(MENU_INVALID)


# Compute Algorithm
def O1_compute(bin_params, item_params):
    
    # Check if Bin and Box CSVs are properly loaded
    bins_loaded = True if bin_params is not None else False
    boxes_loaded = True if item_params is not None else False
      
    if not bins_loaded or not boxes_loaded:
        if not bins_loaded:
            print(MENU_BIN_NOTLOADED)
        if not boxes_loaded:
            print(MENU_BOX_NOTLOADED)

    # If they are, run simulation
    else:
        # Initialize packing function.
        packer = Packer()

        # Initialize bins.
        for b in bin_params:
            partno = b[0]
            WHD = (float(b[1]), float(b[2]), float(b[3]))
            max_weight = b[4]
            packer.addBin(Bin(partno, WHD, max_weight))

        # Initialize items.
        for item in item_params:
            partno = item[0]
            name = item[1]
            typeof = item[2]
            WHD = (float(item[3]), float(item[4]), float(item[5]))
            weight = float(item[6])
            level = int(item[7])
            loadbear = int(item[8])
            updown = bool(item[9])
            color = item[10]
            packer.addItem(Item(partno, name, typeof, WHD, weight, level, loadbear, updown, color))

        #region Calculate packing
        start = time.time()                
        packer.pack(
            bigger_first=True,
            distribute_items=True,
            fix_point=True,
            check_stable=True,
            support_surface_ratio=0.75,
            number_of_decimals=0
        )
        stop = time.time()

        # print result
        print("***************************************************")
        for idx,b in enumerate(packer.bins) :
            print("**", b.string(), "**")
            print("***************************************************")
            print("FITTED ITEMS:")
            print("***************************************************")
            volume = b.width * b.height * b.depth
            volume_t = 0
            volume_f = 0
            unfitted_name = ''
            for item in b.items:
                print("partno : ",item.partno)
                print("color : ",item.color)
                print("position : ",item.position)
                print("rotation type : ",item.rotation_type)
                print("W*H*D : ",str(item.width) +' * '+ str(item.height) +' * '+ str(item.depth))
                print("volume : ",float(item.width) * float(item.height) * float(item.depth))
                print("weight : ",float(item.weight))
                volume_t += float(item.width) * float(item.height) * float(item.depth)
                print("***************************************************")
            
            print('space utilization : {}%'.format(round(volume_t / float(volume) * 100 ,2)))
            print('residual volume : ', float(volume) - volume_t )
            print("gravity distribution : ",b.gravity)
            print("***************************************************")
            # draw results
            painter = Painter(b)
            fig = painter.plotBoxAndItems(
                title=b.partno,
                alpha=0.8,
                write_num=False,
                fontsize=10
            )

        print("***************************************************")
        print("UNFITTED ITEMS:")
        for item in packer.unfit_items:
            print("***************************************************")
            print('name : ',item.name)
            print("partno : ",item.partno)
            print("color : ",item.color)
            print("W*H*D : ",str(item.width) +' * '+ str(item.height) +' * '+ str(item.depth))
            print("volume : ",float(item.width) * float(item.height) * float(item.depth))
            print("weight : ",float(item.weight))
            volume_f += float(item.width) * float(item.height) * float(item.depth)
            unfitted_name += '{},'.format(item.partno)
            print("***************************************************")
        print("***************************************************")
        print('unpack item : ',unfitted_name)
        print('unpack item volume : ',volume_f)

        print('used time : ',stop - start)

        fig.show()
        #endregion
        output_master(packer)

# Test Run
if __name__ == "__main__":
   O1_Input()