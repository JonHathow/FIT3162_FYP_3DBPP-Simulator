""" 
Functions to read/write to fileBinCount.txt and fileBoxCount.txt files. These
files ensure older CSV files are not overwritten upon the creation of new ones.
"""

from .constants import File, FILECOUNT_ERROR_VALUE, FILECOUNT_ERROR_NOTFOUND

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

def fetch_filecount(filename: str) -> int:
    """
    Reads from a file that keep track of the number of CSV files (bin or box)
    that have been created for a particular Option, ensuring older files are
    not overwritten upon the creation of new ones.

    filename    - the name of the fileCount file to be modified

    mode        - specifies whether the fileCount file is for bins or boxes,
                  determines which PROMPT_LASTFILE string is used when the user
                  is prompted for a file count
    """

    while True:
        try:
            with open(filename, mode = 'r') as file:
                try:
                    filecount =  int(file.readline())
                    break
                except ValueError:
                    # The file exists, but does NOT contain a valid integer.
                    print(FILECOUNT_ERROR_VALUE)
                    update_filecount(filename)
                file.close()

        except FileNotFoundError:
            # The file does not exist.
            print(FILECOUNT_ERROR_NOTFOUND)
            update_filecount(filename)

    return filecount