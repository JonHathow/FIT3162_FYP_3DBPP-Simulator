# Storage optimization in automated fulfilment centers


## Project Description
The 3DBPP Simulation Program was built as a Final Year Project, with the purpose of investigating the 3 Dimensional Bin Packing Problem, and for running and testing existing 3DBPP solution algorithms.

The 3DBPP Solution Algorihtms that we referenced are:

**Option 1 - Best-Fit Heuristic: Back Bottom Left Fill**

Dube, E., Kanavathy, L. R., & Za, O. C. (2006). Optimizing Three-Dimensional bin packing through simulation. In Proceedings of the Sixth IASTED International Conference on Modelling, Simulation, and Optimization. https://www.researchgate.net/publication/228974015_Optimizing_Three-Dimensional_Bin_Packing_Through_Simulation

**Option 2 - Genetic Algorithm with Best Match Fill (BMF) Heuristic**

Gonçalves, J. F., & Resende, M. G. C. (2012). A parallel multi-population biased random-key genetic algorithm for a container loading problem. Computers &amp; Operations Research, 39(2), 179–190. https://doi.org/10.1016/j.cor.2011.03.009 

## Project Packages

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

    write_output.py         - function that prints given array of
                              records detailing the output of the
                              program and prints them to a CSV file

(2) Option1_package

Contains functions and types from Option 1's implementation, exported
to an external folder for ease of access.

(3) Option2_package

Contains functions and types from Option 2's implementation, exported
to an external folder for ease of access.

## File Structure

Folders storing the relevant input files should be created within the
same parent directory as the repository folder. Accordingly, the file
structure should resemble something like this:

PARENT DIRECTORY

    -- files_Option1

        -- fileBinCount.txt
        -- fileBoxCount.txt

        -- csv_bins
            -- inputBins1.csv
            -- inputBins2.csv
            ...
        
        -- csv_boxes
            -- inputBoxes1.csv
            -- inputBoxes2.csv
            ...

    -- files_Option2

        -- fileBinCount.txt
        -- fileBoxCount.txt

        -- csv_bins
            -- inputBins1.csv
            -- inputBins2.csv
            ...
        
        -- csv_boxes
            -- inputBoxes1.csv
            -- inputBoxes2.csv
            ...

    -- program

        -- manage_csv
            ...

        -- Option1_package
            ...

        -- Option2_package
            ...

        -- Option1_input.py
        -- Option2_input.py

Keep in mind that files_Option1 and files_Option2 will be created
in the current directory as specified in the terminal. By default
this should be the path to the directory the repository is locally
saved in but may vary.

DO NOT include the generated text and CSV files when pushing to the
remote repository. However, do keep copies of files that result in
errors for debugging purposes.

## Project Back-End Subroutines

The Project is run using Main.py, but the communication between the user interface and the subroutines is managed by master_input.py, the master subroutine.
For more information about the master subroutine, you may refer to the comments in the code file.

The subroutines Option1_input.py and Option2_input.py handle the reading and writing
of CSV files used as the inputs of their respective implemantations.

    (1) constants.py
    (2) prompts.py
    (3) manage_filecountpy
    (4) input_parameters.py
    (5) read_input_csv.py
    (6) write_input_bin.py
    (7) write_input_box.py
    (8) write_output.py

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
    (8) write_output.py

The documentation of the following files should also be perused:

    (1) write_output_option1.py
    (2) write_output_option2.py

Despite their name, both Option1_input.py and Option2_input.py are
responsible for producing output files as well as parsing input.
They may be given a more suitable name should the need arise.

## Project Front-End

The Project Front-End Graphical User Interface, UI.py, has all the classes for all the UI windows in the simulation program.

The UI Windows are:

1. Parent_Window - Parent Window that is the foundation for all other windows.
2. Main_Window - Main Menu Windows
3. MS_Window (Master Subroutine Window) - The User Interface of the Master Subroutine
4. Bin_Input Window - Create Bin CSV Form
5. Box_Input_O2 Window - Create Box CSV Form for Option 2
6. Box_Input_O1 Window - Create Box CSV Form for Option 1
7. Load_CSV Window - Load CSV Window that opens File Explorer for loading a bin or box csv file into the program.
8. Output Window - Implementation Cancelled

## Additional Notes

To the best of our ability, we have separated functions that prompt for
user input from those that handle file I/O. This way, the "prompt"
functions used throughout the package can be switched out when it come
time to integrate the subroutines with the front-end.

## Support
For more information on how to set up and run the program, refer to the 3DBPP Simulation - User and Technical Guide PDF file.

## Authors and Acknowledgment
1. Cheryl Frances Lee - Project Manager and Back-End Developer
2. How Yu Chern - Technical Lead and Front-End Developer
3. Anson Sameer Lee - Quality Assurance Officer
