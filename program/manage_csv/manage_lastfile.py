# TODO: Evaluate documentation.

import os
from .constants import Option, File, FOLDER_OUTPUTS_1, FOLDER_OUTPUTS_2, FILE_LASTBIN_1, FILE_LASTBIN_2, FILE_LASTBOX_1, FILE_LASTBOX_2

def update_lastfile(filename: str, option: Option, filetype: File):
    
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