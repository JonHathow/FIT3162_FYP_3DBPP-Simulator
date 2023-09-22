"""
Functions to extract relevant data items from a packer object
(as implemented in Option 1) and format them into rows to be
printed in a CSV file.
"""
# TODO: Validate correctness of extracting unpacked items from
# the packer object.

import os
from manage_csv.constants import (Option, File, Mode,
                                  FOLDER_OUTPUTS_1, FILE_OUTCOUNT_1,
                                  FILE_FITTED_1, FILE_UNFITTED_1, FILE_SUMMARY_1, FILE_OUTBINS_1,
                                  HEADER_OUT_1, HEADER_OUTBINS_1, HEADER_SUM)
from manage_csv.manage_filecount import fetch_filecount, update_filecount
from manage_csv.manage_lastfile import fetch_lastfile
from manage_csv.write_output import write_output
from Option1_package import Packer

def extract_boxes(packer: Packer, mode: Mode):
    """
    Extracts data items pertaining to boxes and formats
    them into rows to be printed in a CSV file.

    packer      - object that handles packing of boxes into
                  bins within the algorithm implemented in
                  Option 1

    mode        - specifies whether fitted or unfitted boxes
                  are being handled
    """

    rows = []

    for idx,b in enumerate(packer.bins):
        items = b.items if mode == Mode.FITTED.value else packer.unfit_items

        for item in items:
            rows.append([item.partno,
                         item.name,
                         item.color,
                         item.width,
                         item.height,
                         item.depth,
                         float(item.width) * float(item.height) * float(item.depth),
                         float(item.weight),
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
                  Option 1
    """

    rows_bins   = []
    rows_summ  = []

    volume_b = 0
    volume_f = 0
    volume_u = 0

    for idx,b in enumerate(packer.bins):
        vol_b       = b.width * b.height * b.depth
        volume_b    += vol_b

        for item in b.items:
            vol_f       = float(item.width) * float(item.height) * float(item.depth)
            volume_f    += vol_f

        rows_bins.append([b.partno,
                          vol_b,
                          vol_f,
                          float(vol_b) - vol_f,
                          round(vol_f / float(vol_b) * 100, 2),
                          b.gravity])
        
    for item in packer.unfit_items:
        volume_u += float(item.width) * float(item.height) * float(item.depth)

    rows_summ.append([fetch_lastfile(Option.OPTION1.value, File.BIN.value),
                      fetch_lastfile(Option.OPTION1.value, File.BOX.value),
                      volume_b,
                      volume_f,
                      float(volume_b) - volume_f,
                      round(volume_f / float(volume_b) * 100, 2),
                      volume_u])
    
    return rows_bins, rows_summ

def output_master(packer: Packer):
    """
    Calls various functions to extract relevant data items from
    packer and passes them into a function to write them into a
    CSV file.

    packer      - object that handles packing of boxes into
                  bins within the algorithm implemented in
                  Option 1
    """

    if not os.path.exists(FOLDER_OUTPUTS_1):
        os.makedirs(FOLDER_OUTPUTS_1)

    filecount = fetch_filecount(FILE_OUTCOUNT_1)

    rows_fitted             = extract_boxes(packer, Mode.FITTED.value)
    rows_unfitted           = extract_boxes(packer, Mode.UNFITTED.value)
    rows_bins, rows_summ    = extract_summary(packer)

    write_output(FILE_FITTED_1, filecount + 1, HEADER_OUT_1, rows_fitted)
    write_output(FILE_UNFITTED_1, filecount + 1, HEADER_OUT_1, rows_unfitted)
    write_output(FILE_OUTBINS_1, filecount + 1, HEADER_OUTBINS_1, rows_bins)
    write_output(FILE_SUMMARY_1, filecount + 1, HEADER_SUM, rows_summ)
    
    update_filecount(FILE_OUTCOUNT_1, filecount)
    