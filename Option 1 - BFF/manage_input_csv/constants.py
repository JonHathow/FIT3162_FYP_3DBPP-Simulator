# TODO: Evaluate documentation.

# File paths
FOLDERCSVS      = 'input_csv'
FILEBINCOUNT    = f'{FOLDERCSVS}\\fileBinCount.txt'
FILEBOXCOUNT    = f'{FOLDERCSVS}\\fileBoxCount.txt'
FILEBIN         = f'{FOLDERCSVS}\inputBins'
FILEBOX         = f'{FOLDERCSVS}\inputBoxes'

# Interchangeable prompts
PROMPT_QTY_BIN      = "# of bins"
PROMPT_WID_BIN      = "WIDTH of bins"
PROMPT_HEI_BIN      = "HEIGHT of bins"
PROMPT_DEP_BIN      = "DEPTH of bins"
PROMPT_WGT_BIN      = "maximum WEIGHT capacity of bins"
PROMPT_TYPE_BOX     = "# of types of boxes (each type has identical dimensions)"
PROMPT_QTY_BOX      = "QUANTITY of boxes per type"
PROMPT_DIM_BOX      = "DIMENSIONS of boxes"
PROMPT_WGT_BOX      = "WEIGHT of boxes"
PROMPT_LEVEL_VAR    = "variation in LOADING PRIORITY LEVEL"
PROMPT_UPDOWN_VAR   = "variation in LOADING ORIENTATION"
PROMPT_UPDOWN       = "boxes to be loaded UPSIDE-DOWN"
PROMPT_LASTFILE     = f"the numeric identifier of the last {FILEBIN}#.csv or {FILEBOX}#.csv file (enter 0 if you have no files)"
PROMPT_CSVFILE      = f"the numeric identifier of a {FILEBIN}#.csv or {FILEBOX}#.csv file you wish to access"

# Input prompt error messages
ERROR_INTEGER   = "ERROR: Invalid integer input."
ERROR_STRING    = "ERROR: Invalid string input."
ERROR_BOOLEAN   = "ERROR: Invalid input. Y/N only."

# CSV header with row names
ROW_HEADER_BIN  = ['partno', 'width', 'height', 'depth', 'max_weight', 'corner', 'put_type']
ROW_HEADER_BOX  = ['partno', 'name', 'typeof', 'width', 'height', 'depth', 'weight', 'level', 'loadbear', 'updown', 'color']

# File I/O error messages
FILECOUNT_ERROR_VALUE       = "\nERROR: Valid integer value not found in given file. Creating new file..."
FILECOUNT_ERROR_NOTFOUND    = "\nERROR: File not found. Creating new file..."
CSVFILE_ERROR_NOTFOUND      = "\nERROR: File not found. Make sure you're entering a valid integer corresponding to an existing file."

# TODO: Add more colors?
COLORS              = ["red", "green", "blue", "white", "black"]