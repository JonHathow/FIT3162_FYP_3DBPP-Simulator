--- INTRODUCTION ----------------------------------------------------

Option1_input.py and Option2_input.py handle the reading and writing
of CSV files used as the inputs of their respective implemantations.

To understand how these input subroutines work, it is recommended to
review the documenation of the Python scripts in the manage_csv
package in the following order:

    (1) constants.py
    (2) prompts.py
    (3) manage_filecountpy
    (4) input_parameters.py
    (5) read_input_csv.py
    (6) write_input_bin.py
    (7) write_input_box.py

--- PACKAGES --------------------------------------------------------

(1) manage_csv

Contains various functions and types for handling the reading and
writing of the CSV files to be used as inputs for the bin-packing
problem as implemented in Option 1 and Option 2.

    constants.py            - contains various strings and enums used
                              throughout the package and other files

    prompts.py              - functions to prompt users for inputs of
                              various types

    manage_filecount.py     - functions to read from and write to
                              fileBinCount.txt and fileBoxCount.txt
                              files

    input_parameters.py     - classes to instantiate objects that
                              store user inputs for further
                              processing

    read_input.py           - functions to read from a CSV file of
                              inputs for either bins or boxes

    write_input_bin.py      - functions to write a CSV file for bins

    write_input_box.py      - functions to write a CSV file for boxes

(2) Option1_package

Contains functions and types from Option 1's implementation, exported
to an external folder for ease of access.

(3) Option2_package

Contains functions and types from Option 2's implementation, exported
to an external folder for ease of access.

--- FILE STRUCTURE --------------------------------------------------

Folders storing the relevant input files should be created within the
same parent directory as the repository folder. Accordingly, the file
structure should look something like this:

PARENT DIRECTORY

    -- files_Option1

        -- fileBinCount.txt
        -- fileBoxCount.txt
        -- inputBins1.csv
        -- inputBoxes1.csv
        -- inputBoxes2.csv
        ...

    -- files_Option2

        -- fileBinCount.txt
        -- fileBoxCount.txt
        -- inputBins1.csv
        -- inputBoxes1.csv
        -- inputBoxes2.csv
        ...

    -- storage-optimization-in-automated-fulfilment-centers

        -- program

            -- manage_csv
                ...

            -- Option1_package
                ...

            -- Option2_package
                ...

            -- Option1_input.py
            -- Option2_input.py

Attempting to run the scripts locally on your device may result in
something that looks different from this. Please report to me if this
happens to be the case.

DO NOT include the generated text and CSV files when pushing to the
remote repository. However, do keep copies of files that result in
errors for debugging purposes.

--- ADDITIONAL NOTES ------------------------------------------------

To the best of my ability, I have separated functions that prompt for
user input from those that handle file I/O. This way, the "prompt"
functions I haved used throughout the package can be switched out
when it comes time to integrate the subroutines with the front-end.