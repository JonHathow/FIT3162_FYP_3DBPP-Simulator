""" Functions to read from a CSV file of inputs for either bins or boxes. """
# TODO: Evaluate documentation.

import csv
from typing import Optional, List
from .constants import Option, File, PROMPT_CSVFILE_BIN, PROMPT_CSVFILE_BOX, CSVFILE_ERROR_NOTFOUND
from .prompts import prompt_integer
from .manage_lastfile import update_lastfile

def fetch_filename(filename: str, filetype: File) -> str:
    """
    The user is prompted for the integer identifier of the CSV file they
    wish to read from.

    For example, if you wish to read inputBoxes2.csv, you should enter "2".

    filename    - the name of the CSV file to be read from

    filetype    - specifies whether the CSV file being read is for bins or boxes,
                  determines which PROMPT_CSVFILE string is used when the user is
                  prompted for a file to read
    """
    prompt = PROMPT_CSVFILE_BIN if filetype == File.BIN.value else PROMPT_CSVFILE_BOX
    return f"{filename}{prompt_integer(prompt)}.csv"

def read_input(filename: str, filetype: File, option: Option, ui_flag: bool = False) -> Optional[List[str]]:
    """
    Reads from a CSV file of inputs for either bins or boxes.

    filename    - the name of the CSV file to be read from

    filetype    - specifies whether the CSV file being read is for bins or boxes,
                  determines which PROMPT_CSVFILE string is used when the user is
                  prompted for a file to read
    """

    # --- Fetch File Name --- #
    # Has ui_flag: true = UI in use, false then use fetch_filename() to get correct filepath
    if not ui_flag:
        filename = fetch_filename(filename, filetype)
    
    print("This is the format of filename: {}".format(filename))

    update_lastfile(filename, option, filetype)

    try:
        with open(filename, mode = 'r') as csvfile:
            item_params: Optional[List[str]] = []
            reader = csv.reader(csvfile)

            header = ', '.join(next(reader))
            print(f"\nRow headings: {header}")

            for row in reader:
                item_params.append(row)

        print(f"Read from file {filename} completed!\n")
        return item_params

    except FileNotFoundError:
        print(CSVFILE_ERROR_NOTFOUND)