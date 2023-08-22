# TODO: Evaluate documentation.

import os
import csv
from typing import Optional, List
from .constants import FILEBIN, FILEBOX, PROMPT_CSVFILE, CSVFILE_ERROR_NOTFOUND
from .prompts import prompt_integer

def read_input(filename: str) -> Optional[List[str]]:
    
    filename = f"{filename}{prompt_integer(PROMPT_CSVFILE)}.csv"

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