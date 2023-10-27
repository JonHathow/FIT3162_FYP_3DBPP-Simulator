" Functions to write a CSV file for boxes. "

import os
import csv
from .constants import (Option, File, PROMPT_TYPE_BOX, PROMPT_QTY_BOX, PROMPT_DIM_BOX, PROMPT_WGT_BOX,
                        PROMPT_LEVEL_VAR, PROMPT_UPDOWN_VAR, PROMPT_UPDOWN,
                        FOLDER_INPUTS_1, FOLDER_INPUTS_2, FOLDER_BOX_1, FOLDER_BOX_2, FILE_BOXCOUNT_1, FILE_BOXCOUNT_2, FILE_BOX_1, FILE_BOX_2,
                        HEADER_BOX_1, HEADER_BOX_2, COLORS)
from .manage_filecount import update_filecount, fetch_filecount
from .prompts import prompt_integer, prompt_range, prompt_boolean
from .input_parameters import InputBoxParameters
from random import randint, uniform
from UI import Box_Window_O1, Box_Window_O2

def prompt_input_boxes(option: Option) -> InputBoxParameters:
    """ 
    Prompts user for various inputs.
    Returns an InputBoxParameters object initialized with those values.
    
    option  - specifies whether the function is being called by
              Option 1 or Option 2, determines whether the user
              will be prompted for additional inputs required
              for Option 1
    """

    # Number of box types
    types = prompt_integer(PROMPT_TYPE_BOX)

    # Quantity of boxes
    qty_lo, qty_hi = prompt_range(PROMPT_QTY_BOX)   # type: (int, int)

    # Width, height, and depth of boxes
    # TODO: Allow users to specify lower/upper bounds for each dimension.
    dim_lo, dim_hi = prompt_range(PROMPT_DIM_BOX)   # type: (float, float)

    # Weight of boxes
    wgt_lo, wgt_hi = prompt_range(PROMPT_WGT_BOX)   # type (int, int)

    input_params = InputBoxParameters(types, min(qty_lo, qty_hi), max(qty_lo, qty_hi),
                           min(dim_lo, dim_hi), max(dim_lo, dim_hi), min(wgt_lo, wgt_hi), max(wgt_lo, wgt_hi))

    # Inputs specific to Option 1
    if option == Option.OPTION1.value:
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

        input_params.set_option1_params(level_var, updown_var, updown)
    
    return input_params

def write_input_box_func(option: Option, b_inputs:InputBoxParameters = None, ui_flag: bool = False) -> None:
    """
    Produce a CSV file with random values for boxes in the ranges specified by the user's inputs.

    option  - specifies whether the function is being called by
              Option 1 or Option 2, used to determine file path,
              file name, and the header to be printed
    """
    if option == Option.OPTION1.value:
        folder_path     = FOLDER_INPUTS_1
        folder_box_path = FOLDER_BOX_1
        file_boxcount   = FILE_BOXCOUNT_1
        filename        = FILE_BOX_1
        header          = HEADER_BOX_1
        
    else:
        folder_path     = FOLDER_INPUTS_2
        folder_box_path = FOLDER_BOX_2
        file_boxcount   = FILE_BOXCOUNT_2
        filename        = FILE_BOX_2
        header          = HEADER_BOX_2    

    # Make a new directory if it does not already exist.    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if not os.path.exists(folder_box_path):
        os.makedirs(folder_box_path)

    filecount: int = fetch_filecount(file_boxcount)

    # --- Fetching Box Information ---- #
    inputs = None
    print("UI Flag Status for write_input: {}".format(ui_flag))
    
    if ui_flag:
        inputs: InputBoxParameters = b_inputs
    else:
        inputs: InputBoxParameters = prompt_input_boxes(option)
    
    # Write File
    filename = f'{filename}{filecount + 1}.csv'

    with open(filename, mode = 'w', newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        # For each box type t
        for t in range(inputs.types):
            qty = randint(inputs.qty_lo, inputs.qty_hi)
            box_type = f"BoxType{t + 1}"

            # Randomly generate values for width, height, depth, and weight
            # within ranges specified by the user.

            width = uniform(inputs.dim_lo, inputs.dim_hi)
            height = uniform(inputs.dim_lo, inputs.dim_hi)
            depth = uniform(inputs.dim_lo, inputs.dim_hi)
            weight = uniform(inputs.wgt_lo, inputs.wgt_hi)
            color = COLORS[randint(0, len(COLORS) - 1)]

            if option == Option.OPTION1.value:
                # Attributes specific to Option 1
                shape = "cube"
                level = 1 if not inputs.level_var else randint(1, 3)
                loadbear = 100
                updown = inputs.updown if not inputs.updown_var else bool(randint(0, 1))

            for i in range(qty):    
                name = f"{box_type}_#{i + 1}"

                if option == Option.OPTION1.value:
                    writer.writerow([name, box_type, shape, width, height, depth, weight, level, loadbear, updown, color])

                else:
                    writer.writerow([name, width, height, depth, weight, color]) 
    
    csvfile.close()
    update_filecount(file_boxcount, filecount)
    print(f"\nFile {filename} created!\n")
