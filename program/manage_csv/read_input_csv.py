""" Functions to read from a CSV file of inputs for either bins or boxes. """
# TODO: Specify sample inputs.

import csv
from typing import Optional, List
from .constants import Mode, PROMPT_CSVFILE_BIN, PROMPT_CSVFILE_BOX, CSVFILE_ERROR_NOTFOUND
from .prompts import prompt_integer

def fetch_filename(filename: str, prompt: str) -> str:
    """
    The user is prompted for the integer identifier of the CSV file they
    wish to read from.

    For example, if you wish to read inputBoxes2.csv, you should enter "2".

    filename    - the name of the CSV file to be read from

    prompt      - string literal containing a prompt message
                  corresponing to the type of CSV file being
                  handled (bin or box)
    """
    return f"{filename}{prompt_integer(prompt)}.csv"

def read_input(filename: str, mode: Mode) -> Optional[List[str]]:
    """
    Reads from a CSV file of inputs for either bins or boxes.

    filename    - the name of the CSV file to be read from

    mode        - specifies whether the CSV file being read is for bins or boxes,
                  determines which PROMPT_CSVFILE string is used when the user is
                  prompted for a file to read
    """
    
    prompt = PROMPT_CSVFILE_BIN if mode == Mode.BIN.value else PROMPT_CSVFILE_BOX
    filename = fetch_filename(filename, prompt)

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