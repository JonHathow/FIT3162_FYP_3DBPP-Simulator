""" 
Functions to read/write to fileBinCount.txt and fileBoxCount.txt files. These
files ensure older CSV files are not overwritten upon the creation of new ones.
"""

from .constants import File, PROMPT_LASTFILE_BIN, PROMPT_LASTFILE_BOX, PROMPT_LASTFILE_OUT, FILECOUNT_ERROR_VALUE, FILECOUNT_ERROR_NOTFOUND
from .prompts import prompt_integer

def update_filecount(filename: str, filecount: int = -1) -> None:
    """
    Increment the integer stored in a given fileCount file by one.

    filename    - the name of the fileCount file to be modified

    filecount   - the number of bin or box files, stored as an integer in the
                  aforementioned file
    """

    with open(filename, mode = 'w') as file:
        file.write(str(filecount + 1))
    file.close()

def fix_filecount(filename: str, prompt: str) -> None:
    """
    Prompts the user for an integer equivalent to the number of CSV
    files of that type (bin or box) created so far, which will be
    use to fix the fileCount file (or create a new one).

    For example, if the last file created was inputBoxes2.csv, you
    should enter "2" when prompted. However, there is nothing
    stopping you from entering any other number in this case.

    If you wish to "reset" the file and do not mind potentially
    overwriting existing files, you should enter "0".

    filename    - the name of the fileCount file to be modified
    
    prompt      - string literal containing a prompt message
                  corresponing to the type of CSV file being
                  handled (bin or box)
    """
    update_filecount(filename, prompt_integer(prompt) - 1)

def fetch_filecount(filename: str, filetype: File) -> int:
    """
    Reads from a file that keep track of the number of CSV files (bin or box)
    that have been created for a particular Option, ensuring older files are
    not overwritten upon the creation of new ones.

    filename    - the name of the fileCount file to be modified

    mode        - specifies whether the fileCount file is for bins or boxes,
                  determines which PROMPT_LASTFILE string is used when the user
                  is prompted for a file count
    """

    if filetype == File.BIN.value:
        prompt = PROMPT_LASTFILE_BIN
    elif filetype == File.BOX.value:
        prompt = PROMPT_LASTFILE_BOX
    else:
        prompt = PROMPT_LASTFILE_OUT

    while True:
        try:
            with open(filename, mode = 'r') as file:
                try:
                    filecount =  int(file.readline())
                    break
                except ValueError:
                    # The file exists, but does NOT contain a valid integer.
                    print(FILECOUNT_ERROR_VALUE)
                    fix_filecount(filename, prompt)
                file.close()

        except FileNotFoundError:
            # The file does not exist.
            print(FILECOUNT_ERROR_NOTFOUND)
            fix_filecount(filename, prompt)

    return filecount