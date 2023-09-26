""" 
Functions to read/write to fileBinCount.txt and fileBoxCount.txt files. These
files ensure older CSV files are not overwritten upon the creation of new ones.
"""

from .constants import FILECOUNT_ERROR_VALUE, FILECOUNT_ERROR_NOTFOUND

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
    Reads from a file that keep track of the number of CSV files (bin, box, or
    output) that have been created for a particular Option, ensuring older
    files are not overwritten upon the creation of new ones.

    A new file is created if one is not found or if the existing one has been
    corrupted in some form.

    filename    - the name of the fileCount file to be modified
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
