""" Contains various strings and enums used throughout the package and other dependent files. """

from enum import Enum

class Option(Enum):
    """
    Used as an argument in certain functions to specify which implementation
    (Option 1 or Option 2) is calling said function. The same function may
    be expected to behave differently to account for the variations between
    the two implementations.
    """
    OPTION1 = 1
    OPTION2 = 2

class File(Enum):
    """
    Used as an argument in certain functions to specify whether said function
    is working with an input file for bins, an input file for boxes, or an
    output file. The same function may be expected to behave differently
    depending on the purpose of the file in question.
    """
    BIN = 1
    BOX = 2
    OUT = 3

class Mode(Enum):
    """
    Used as an argument in certain functions to specify whether said function
    is handling fitted or unfitted boxes. The same function may be expected to
    behave differently depending on the type of boxes in question.
    """
    FITTED = 1
    UNFITTED = 2

# Menu navigation and feedback
MENU_INPUT = ("\n1: Generate bin CSV file"
               + "\n2: Generate box CSV file"
               + "\n3: Read from bin CSV file"
               + "\n4: Read from box CSV file"
               + "\n5: Compute packing and produce output files"
               + "\n0: Exit"
               + "\nRESPONSE: ")

MENU_INVALID = "Invalid menu input.\n"
MENU_BIN_NOTLOADED = "Bins have not been loaded. Please read from a bin CSV file first!\n"
MENU_BOX_NOTLOADED = "Boxes have not been loaded. Please read from a box CSV file first!\n"
MENU_END = "Exiting program...\n"

# Folder paths
FOLDER_OPTION1      = 'files_Option1'
FOLDER_OPTION2      = 'files_Option2'
FOLDER_INPUTS_1     = f'{FOLDER_OPTION1}\csv_inputs'
FOLDER_INPUTS_2     = f'{FOLDER_OPTION2}\csv_inputs'
FOLDER_OUTPUTS_1    = f'{FOLDER_OPTION1}\csv_outputs'
FOLDER_OUTPUTS_2    = f'{FOLDER_OPTION2}\csv_outputs'
FOLDER_BIN_1        = f'{FOLDER_INPUTS_1}\csv_bins'
FOLDER_BIN_2        = f'{FOLDER_INPUTS_2}\csv_bins'
FOLDER_BOX_1        = f'{FOLDER_INPUTS_1}\csv_boxes'
FOLDER_BOX_2        = f'{FOLDER_INPUTS_2}\csv_boxes'

# Input file names
FILE_BINCOUNT       = 'fileBinCount.txt'
FILE_BOXCOUNT       = 'fileBoxCount.txt'
FILE_BIN            = 'inputBins'
FILE_BOX            = 'inputBoxes'

# Input file paths
FILE_BINCOUNT_1     = f'{FOLDER_INPUTS_1}\{FILE_BINCOUNT}'
FILE_BINCOUNT_2     = f'{FOLDER_INPUTS_2}\{FILE_BINCOUNT}'
FILE_BOXCOUNT_1     = f'{FOLDER_INPUTS_1}\{FILE_BOXCOUNT}'
FILE_BOXCOUNT_2     = f'{FOLDER_INPUTS_2}\{FILE_BOXCOUNT}'
FILE_BIN_1          = f'{FOLDER_BIN_1}\{FILE_BIN}'
FILE_BIN_2          = f'{FOLDER_BIN_2}\{FILE_BIN}'
FILE_BOX_1          = f'{FOLDER_BOX_1}\{FILE_BOX}'
FILE_BOX_2          = f'{FOLDER_BOX_2}\{FILE_BOX}'

# Output file names
FILE_OUTCOUNT       = 'fileOutCount.txt'
FILE_LASTBIN        = 'lastBinFile.txt'
FILE_LASTBOX        = 'lastBoxFile.txt'
FILE_FITTED         = 'outputFitted'
FILE_UNFITTED       = 'outputUnfitted'
FILE_OUTBINS        = 'outputBins'
FILE_SUMMARY        = 'outputSummary'

# Output file paths
FILE_OUTCOUNT_1     = f'{FOLDER_OUTPUTS_1}\{FILE_OUTCOUNT}'
FILE_OUTCOUNT_2     = f'{FOLDER_OUTPUTS_2}\{FILE_OUTCOUNT}'
FILE_LASTBIN_1      = f'{FOLDER_OUTPUTS_1}\{FILE_LASTBIN}'
FILE_LASTBIN_2      = f'{FOLDER_OUTPUTS_2}\{FILE_LASTBIN}'
FILE_LASTBOX_1      = f'{FOLDER_OUTPUTS_1}\{FILE_LASTBOX}'
FILE_LASTBOX_2      = f'{FOLDER_OUTPUTS_2}\{FILE_LASTBOX}'
FILE_FITTED_1       = f'{FOLDER_OUTPUTS_1}\{FILE_FITTED}'
FILE_FITTED_2       = f'{FOLDER_OUTPUTS_2}\{FILE_FITTED}'
FILE_UNFITTED_1     = f'{FOLDER_OUTPUTS_1}\{FILE_UNFITTED}'
FILE_UNFITTED_2     = f'{FOLDER_OUTPUTS_2}\{FILE_UNFITTED}'
FILE_OUTBINS_1      = f'{FOLDER_OUTPUTS_1}\{FILE_OUTBINS}'
FILE_OUTBINS_2      = f'{FOLDER_OUTPUTS_2}\{FILE_OUTBINS}'
FILE_SUMMARY_1      = f'{FOLDER_OUTPUTS_1}\{FILE_SUMMARY}'
FILE_SUMMARY_2      = f'{FOLDER_OUTPUTS_2}\{FILE_SUMMARY}'

# Interchangeable prompts for bin inputs
PROMPT_QTY_BIN      = "# of bins"
PROMPT_WID_BIN      = "WIDTH of bins"
PROMPT_HEI_BIN      = "HEIGHT of bins"
PROMPT_DEP_BIN      = "DEPTH of bins"
PROMPT_WGT_BIN      = "maximum WEIGHT capacity of bins"

# Interchangeable prompts for box inputs
PROMPT_TYPE_BOX     = "# of types of boxes (each type has identical dimensions)"
PROMPT_QTY_BOX      = "QUANTITY of boxes per type"
PROMPT_DIM_BOX      = "DIMENSIONS of boxes"
PROMPT_WGT_BOX      = "WEIGHT of boxes"

# Interchangeable prompts for additional attributes exclusive to Option 1
PROMPT_LEVEL_VAR    = "variation in LOADING PRIORITY LEVEL"
PROMPT_UPDOWN_VAR   = "variation in LOADING ORIENTATION"
PROMPT_UPDOWN       = "boxes to be loaded UPSIDE-DOWN"

# Interchangeable prompts for locating specific files
PROMPT_CSVFILE_BIN      = f"the numeric identifier of a {FILE_BIN}#.csv file you wish to access"
PROMPT_CSVFILE_BOX      = f"the numeric identifier of a {FILE_BOX}#.csv file you wish to access"

# Input prompt error messages
ERROR_NUMBER    = "ERROR: Invalid numeric input."
ERROR_INTEGER   = "ERROR: Invalid integer input."
ERROR_STRING    = "ERROR: Invalid string input."
ERROR_BOOLEAN   = "ERROR: Invalid input. Y/N only."

# CSV file header with row names
HEADER_BIN_1        = ['partno', 'width', 'height', 'depth', 'max_weight']    
HEADER_BIN_2        = ['name', 'width', 'height', 'depth', 'max_weight']
HEADER_BOX_1        = ['partno', 'name', 'typeof', 'width', 'height', 'depth', 'weight', 'level', 'loadbear', 'updown', 'color']
HEADER_BOX_2        = ['name', 'width', 'height', 'depth', 'weight']
HEADER_OUT_1        = ['partno', 'name', 'color', 'width', 'height', 'depth', 'volume', 'weight', 'position', 'rotation_type']
HEADER_OUT_2        = ['name', 'width', 'height', 'depth', 'volume', 'weight', 'position', 'rotation_type' ]
HEADER_OUTBINS_1    = ['partno', 'volume', 'volume_utilised', 'residual_volume', 'space_utilisation', 'gravity_distribution']
HEADER_OUTBINS_2    = ['partno', 'volume', 'volume_utilised', 'residual_volume', 'space_utilisation']
HEADER_SUM          = ['input_bin_file', 'input_box_file', 'total_bin_volume', 'total_volume_utilised', 'total_residual_volume', 'total_space_utilisation', 'unpacked_volume']

# File I/O error messages
FILECOUNT_ERROR_VALUE       = "\nERROR: Valid integer value not found in given file. Creating new file..."
FILECOUNT_ERROR_NOTFOUND    = "\nERROR: File not found. Creating new file..."
CSVFILE_ERROR_NOTFOUND      = "\nERROR: File not found. Make sure you're entering a valid integer corresponding to an existing file."

# Colors for Option 1
COLORS              = ["red", "green", "blue", "white", "black"]
