""" 
Functions to read/write to lastBinFile.txt and lastBoxFile.txt files. As their
names suggest, these files contain the name of the last bin and box CSV files
read as input so they can be listed in the output summary file.
"""

import os
from .constants import Option, File, FOLDER_OUTPUTS_1, FOLDER_OUTPUTS_2, FILE_LASTBIN_1, FILE_LASTBIN_2, FILE_LASTBOX_1, FILE_LASTBOX_2

def update_lastfile(filename: str, option: Option, filetype: File):
    """
    Overwrite the name of the last CSV file read from as recorded in
    a lastFile file.

    filename    - the name of the CSV file that was read from, to be
                  recorded in the corresponding lastFile file

    option      - specifies whether the function is being called by
                  Option 1 or Option 2, used to determine file and
                  folder paths

    filetype    - specifies whether the read file was for bins or boxes,
                  used to determine file path of lastFile file
    """

    if option == Option.OPTION1.value:
        folder_path = FOLDER_OUTPUTS_1
        file_path   = FILE_LASTBIN_1 if filetype == File.BIN.value else FILE_LASTBOX_1
    else:
        folder_path = FOLDER_OUTPUTS_2
        file_path   = FILE_LASTBIN_2 if filetype == File.BIN.value else FILE_LASTBOX_2

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, mode = 'w') as file:
        file.write(filename)
    file.close()

def fetch_lastfile(option: Option, filetype: File):
    """
    Fetch the name of the last CSV file read from, as recorded in a
    lastFile file.

    option      - specifies whether the function is being called by
                  Option 1 or Option 2, used to determine file and
                  folder paths

    filetype    - specifies whether the read file was for bins or boxes,
                  used to determine file path of lastFile file
    """

    if option == Option.OPTION1.value:
        file_path   = FILE_LASTBIN_1 if filetype == File.BIN.value else FILE_LASTBOX_1

    else:
        file_path   = FILE_LASTBIN_2 if filetype == File.BIN.value else FILE_LASTBOX_2

    with open(file_path, mode = 'r') as file:
        filename = str(file.readline())
    file.close()

    return filename