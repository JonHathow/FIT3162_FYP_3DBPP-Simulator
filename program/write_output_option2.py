"""
Functions to extract relevant data items from a packer object
(as implemented in Option 2) and format them into rows to be
printed in a CSV file.
"""
# TODO: Validate correctness of extracting unpacked items from
# the packer object.

import os
from manage_csv.constants import (Option, File, Mode,
                                  FOLDER_OUTPUTS_2, FILE_OUTCOUNT_2,
                                  FILE_FITTED_2, FILE_UNFITTED_2, FILE_SUMMARY_2, FILE_OUTBINS_2,
                                  HEADER_OUT_2, HEADER_OUTBINS_2, HEADER_SUM)
from manage_csv.manage_filecount import fetch_filecount, update_filecount
from manage_csv.manage_lastfile import fetch_lastfile
from manage_csv.write_output import write_output
from Option2_package import Packer

def extract_boxes(packer: Packer, mode: Mode):
    """
    Extracts data items pertaining to bins and the
    specific run of the simulation as a whole. Two
    lists are returned, one containing data items
    relevant to bins and the other relevant to the
    overall run of the simulation.

    packer      - object that handles packing of boxes into
                  bins within the algorithm implemented in
                  Option 2
    """

    rows = []

    for b in packer.bins:
        items = b.items if mode == Mode.FITTED.value else packer.unplaced_items
        
        for item in items:
            rows.append([item.name,
                         item.length,
                         item.height,
                         item.width,
                         item.weight,
                         item.get_volume(),
                         item.position,
                         item.rotation_type])

        # Skip remaining bins when handling unpacked items
        if mode == Mode.UNFITTED.value:
            break

    return rows

def extract_summary(packer: Packer):
    """
    Extracts data items pertaining to bins and the
    specific run of the simulation as a whole. Two
    lists are returned, one containing data items
    relevant to bins and the other relevant to the
    overall run of the simulation.

    packer      - object that handles packing of boxes into
                  bins within the algorithm implemented in
                  Option 2
    """

    rows_bins   = []
    rows_summ  = []

    volume_b = 0
    volume_f = 0
    volume_u = 0

    for b in packer.bins:
        vol_b       = b.get_volume()
        volume_b    += vol_b

        for item in b.items:
            vol_f       = item.get_volume()
            volume_f    += vol_f

        rows_bins.append([b.size,
                          vol_b,
                          vol_f,
                          vol_b - vol_f,
                          round(vol_f / vol_b * 100, 2)])
        
    for item in packer.unplaced_items:
        volume_u += item.get_volume()

    rows_summ.append([fetch_lastfile(Option.OPTION2.value, File.BIN.value),
                      fetch_lastfile(Option.OPTION2.value, File.BOX.value),
                      volume_b,
                      volume_f,
                      volume_b - volume_f,
                      round(volume_f / volume_b * 100, 2),
                      volume_u])
    
    return rows_bins, rows_summ

def output_master(packer: Packer):
    """
    Calls various functions to extract relevant data items from
    packer and passes them into a function to write them into a
    CSV file.

    packer      - object that handles packing of boxes into
                  bins within the algorithm implemented in
                  Option 2
    """

    if not os.path.exists(FOLDER_OUTPUTS_2):
        os.makedirs(FOLDER_OUTPUTS_2)

    filecount = fetch_filecount(FILE_OUTCOUNT_2)

    rows_fitted             = extract_boxes(packer, Mode.FITTED.value)
    rows_unfitted           = extract_boxes(packer, Mode.UNFITTED.value)
    rows_bins, rows_summ    = extract_summary(packer)

    write_output(FILE_FITTED_2, filecount + 1, HEADER_OUT_2, rows_fitted)
    write_output(FILE_UNFITTED_2, filecount + 1, HEADER_OUT_2, rows_unfitted)
    write_output(FILE_OUTBINS_2, filecount + 1, HEADER_OUTBINS_2, rows_bins)
    write_output(FILE_SUMMARY_2, filecount + 1, HEADER_SUM, rows_summ)
    
    update_filecount(FILE_OUTCOUNT_2, filecount)
