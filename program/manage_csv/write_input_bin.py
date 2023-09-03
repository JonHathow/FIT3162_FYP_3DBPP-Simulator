" Functions to write a CSV file for bins. "

import os
import csv
from .constants import (Option, Mode, PROMPT_QTY_BIN, PROMPT_WID_BIN, PROMPT_HEI_BIN, PROMPT_DEP_BIN, PROMPT_WGT_BIN,
                        FOLDER_INPUTS_1, FOLDER_INPUTS_2, FILE_BINCOUNT_1, FILE_BINCOUNT_2, FILE_BIN_1, FILE_BIN_2,
                        HEADER_BIN_1, HEADER_BIN_2)

from .manage_filecount import update_filecount, fetch_filecount
from .prompts import prompt_number, prompt_integer
from .input_parameters import InputBinParameters

def prompt_input_bins() -> InputBinParameters:
    """
    Prompts user for various inputs for bin dimensions.
    Returns an InputBinParamters object initialized with those values.
    """

    # Quantity of bins
    qty = prompt_integer(PROMPT_QTY_BIN)

    # Width of bins
    wid = prompt_number(PROMPT_WID_BIN)

    # Height of bins
    hei = prompt_number(PROMPT_HEI_BIN)

    # Depth of bins
    dep = prompt_number(PROMPT_DEP_BIN)

    # Weight capacity of bins
    wgt = prompt_number(PROMPT_WGT_BIN)

    return InputBinParameters(qty, wid, hei, dep, wgt)

def write_input_bin_func(option: Option) -> None:
    """
    Produce a CSV file for bins specfied by the user's inputs.

    option  - specifies whether the function is being called by
              Option 1 or Option 2, used to determine file path,
              file name, and the header to be printed
    """

    #if option == Option.OPTION1:
    if option == Option.OPTION1.value:
        folder_path     = FOLDER_INPUTS_1
        file_bincount   = FILE_BINCOUNT_1
        filename        = FILE_BIN_1
        header          = HEADER_BIN_1
        
    else:
        folder_path     = FOLDER_INPUTS_2
        file_bincount   = FILE_BINCOUNT_2
        filename        = FILE_BIN_2
        header          = HEADER_BIN_2

    # Make a new directory if it does not already exist.
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filecount: int = fetch_filecount(file_bincount, Mode.BIN.value)
    inputs: InputBinParameters = prompt_input_bins()

    filename = f'{filename}{filecount + 1}.csv'

    with open(filename, mode = 'w', newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        # For each bin b
        for b in range(inputs.qty):
            name        = f"Bin_#{b + 1}"
            width       = inputs.width
            height      = inputs.height
            depth       = inputs.depth
            capacity    = inputs.capacity

            writer.writerow([name, width, height, depth, capacity])

    csvfile.close()
    update_filecount(file_bincount, filecount)
    print(f"\nFile {filename} created!\n")
