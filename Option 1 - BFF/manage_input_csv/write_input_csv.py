# TODO: Evaluate documentation.

import os
import csv
from .constants import (FILECOUNT_ERROR_VALUE, FILECOUNT_ERROR_NOTFOUND, PROMPT_LASTFILE,
                        PROMPT_QTY_BIN, PROMPT_WID_BIN, PROMPT_HEI_BIN, PROMPT_DEP_BIN, PROMPT_WGT_BIN,
                        PROMPT_TYPE_BOX, PROMPT_QTY_BOX, PROMPT_DIM_BOX, PROMPT_WGT_BOX, PROMPT_LEVEL_VAR, PROMPT_UPDOWN_VAR, PROMPT_UPDOWN,
                        FOLDERCSVS, FILEBINCOUNT, FILEBOXCOUNT, FILEBIN, FILEBOX, ROW_HEADER_BIN, ROW_HEADER_BOX, COLORS)
from .prompts import prompt_integer, prompt_range, prompt_boolean
from .input_parameters import InputBinParameters, InputBoxParameters
from random import randint

def update_file_count(filename: str, filecount: int = -1) -> None:
    """
    Increment the integer stored in a given fileCount file by one.
    """

    with open(filename, mode = 'w') as file:
        file.write(str(filecount + 1))
    file.close()

def fetch_file_count(filename: str) -> int:
    """
    Reads from a file that keep track of the number of csv files that have been created by this module.
    This ensures writing a new file will not replace older files.
    """

    while True:
        try:
            with open(filename, mode = 'r') as file:
                try:
                    filecount =  int(file.readline())
                    break
                except ValueError:
                    print(FILECOUNT_ERROR_VALUE)
                    update_file_count(filename, prompt_integer(PROMPT_LASTFILE) - 1)
                file.close()

        except FileNotFoundError:
            print(FILECOUNT_ERROR_NOTFOUND)
            update_file_count(filename, prompt_integer(PROMPT_LASTFILE) - 1)

    return filecount

def prompt_input_bins() -> InputBinParameters:
    """ Prompts user for various inputs """

    qty = prompt_integer(PROMPT_QTY_BIN)
    wid = prompt_integer(PROMPT_WID_BIN)
    hei = prompt_integer(PROMPT_HEI_BIN)
    dep = prompt_integer(PROMPT_DEP_BIN)
    wgt = prompt_integer(PROMPT_WGT_BIN)

    return InputBinParameters(qty, wid, hei, dep, wgt)

def prompt_input_boxes() -> InputBoxParameters:
    """ Prompts user for various inputs. """

    # Prompt user for number of box types
    types: int = prompt_integer(PROMPT_TYPE_BOX)

    # Prompt user for range of quantity for a certain box type
    qty_lo, qty_hi = prompt_range(PROMPT_QTY_BOX)   # type: (int, int)

    # Prompt user for range of dimensions
    # TODO: Allow users to specify lower/upper bounds for each dimension.
    dim_lo, dim_hi = prompt_range(PROMPT_DIM_BOX)   # type: (int, int)

    # Prompt user for range of weight
    wgt_lo, wgt_hi = prompt_range(PROMPT_WGT_BOX)   # type (int, int)

    # Prompt user for whether they desire variation in loading priority level.
    level_var: bool = prompt_boolean(PROMPT_LEVEL_VAR)

    # TODO: Allow users to specify variation of loadbearing priority.

    # Prompt user for whether they desire variation in loading orientation.
    updown_var: bool = prompt_boolean(PROMPT_UPDOWN_VAR)

    # Ask user if they want boxes that can be loaded upside down. Relevant only if updown_var is False.
    if not updown_var:
        updown: bool = prompt_boolean(PROMPT_UPDOWN)
    else:
        updown = False

    # Return InputParameters object
    return InputBoxParameters(types, min(qty_lo, qty_hi), max(qty_lo, qty_hi),
                           min(dim_lo, dim_hi), max(dim_lo, dim_hi), min(wgt_lo, wgt_hi), max(wgt_lo, wgt_hi),
                           level_var, updown_var, updown)

def write_input_bin() -> None:
    """
    Produce a CSV file for bins specfied by the user's inputs.
    """
    
    if not os.path.exists(FOLDERCSVS):
        os.makedirs(FOLDERCSVS)

    filecount: int = fetch_file_count(FILEBINCOUNT)
    inputs: InputBinParameters = prompt_input_bins()

    filename = f'{FILEBIN}{filecount + 1}.csv'

    with open(filename, mode = 'w', newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(ROW_HEADER_BIN)

        # For each bin b
        for b in range(inputs.qty):
            partno = f"Bin_#{b + 1}"
            width = inputs.width
            height = inputs.height
            depth = inputs.depth
            max_weight = inputs.max_weight

            writer.writerow([partno, width, height, depth, max_weight])

    csvfile.close()
    update_file_count(FILEBINCOUNT, filecount)
    print(f"\nFile {filename} created!\n")

def write_input_box() -> None:
    """
    Produce a CSV file with random values for boxes in the ranges specified by the user's inputs.
    TODO: Allow users to specify variation of loadbearing priority.
    """
    
    if not os.path.exists(FOLDERCSVS):
        os.makedirs(FOLDERCSVS)

    filecount: int = fetch_file_count(FILEBOXCOUNT)
    inputs: InputBoxParameters = prompt_input_boxes()

    filename = f'{FILEBOX}{filecount + 1}.csv'

    with open(filename, mode = 'w', newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(ROW_HEADER_BOX)

        # For each box type t
        for t in range(inputs.types):
            qty = randint(inputs.qty_lo, inputs.qty_hi)

            for i in range(qty):
                name = f"BoxType{t + 1}"
                partno = f"{name}_#{i + 1}"
                typeof = "cube"

                width = randint(inputs.dim_lo, inputs.dim_hi)
                height = randint(inputs.dim_lo, inputs.dim_hi)
                depth = randint(inputs.dim_lo, inputs.dim_hi)
                weight = randint(inputs.wgt_lo, inputs.wgt_hi)
                
                level = 1 if not inputs.level_var else randint(1, 3)
                loadbear = 100
                updown = inputs.updown if not inputs.updown_var else bool(randint(0, 1))

                color = COLORS[randint(0, len(COLORS) - 1)]

                writer.writerow([partno, name, typeof, width, height, depth, weight, level, loadbear, updown, color])
    
    csvfile.close()
    update_file_count(FILEBOXCOUNT, filecount)
    print(f"\nFile {filename} created!\n")