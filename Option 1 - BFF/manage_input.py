""" Derived from example#.py code provided in original repository. """

import os
import time
from manage_input_csv.constants import FILEBIN, FILEBOX
from manage_input_csv.write_input_csv import write_input_bin, write_input_box
from manage_input_csv.read_input_csv import read_input
from py3dbp import Packer, Bin, Item, Painter
os.chdir('Option 1 - BFF')

bins_loaded = False
while True:

    response = input("\n1: Generate bin CSV file" +
                     "\n2: Generate box CSV file" +
                     "\n3: Read from bin CSV file" +
                     "\n4: Read from box CSV file" +
                     "\n0: Exit" +
                     "\nRESPONSE: ")
    
    if response == "1":
        write_input_bin()

    elif response == "2":
        write_input_box()

    elif response == "3":
        bin_params = read_input(FILEBIN)

        if bin_params is not None:
            # Initialize backing function
            packer = Packer()

            # Initialize bins
            for b in bin_params:
                partno = b[0]
                WHD = (int(b[1]), int(b[2]), int(b[3]))
                max_weight = int(b[4])
                packer.addBin(Bin(partno, WHD, max_weight))

            bins_loaded = True

    elif response == "4":
        if bins_loaded == True:
            start = time.time()
            item_params = read_input(FILEBOX)

            if item_params is not None:
                for item in item_params:
                    partno = item[0]
                    name = item[1]
                    typeof = item[2]
                    WHD = (int(item[3]), int(item[4]), int(item[5]))
                    weight = int(item[6])
                    level = int(item[7])
                    loadbear = int(item[8])
                    updown = bool(item[9])
                    color = item[10]
                    packer.addItem(Item(partno, name, typeof, WHD, weight, level, loadbear, updown, color))

                #region Calculate packing
                packer.pack(
                    bigger_first=True,
                    distribute_items=False,
                    fix_point=True,
                    check_stable=True,
                    support_surface_ratio=0.75,
                    number_of_decimals=0
                )

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
                    print('residual volumn : ', float(volume) - volume_t )
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
                print('unpack item volumn : ',volume_f)

                stop = time.time()
                print('used time : ',stop - start)

                fig.show()
                #endregion

        else:
            print("Please load a CSV of bins first!\n")

    elif response == "0":
        print("End execution.\n")
        break

    else:
        print("Invalid input.\n")