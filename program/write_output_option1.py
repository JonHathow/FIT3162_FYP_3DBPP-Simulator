# TODO: Evaluate documentation.
# NOTE: Assumes we're only using 1 bin!!!

import os
import csv
from manage_csv.constants import Option, File, Mode, FOLDER_OUTPUTS_1, FILE_OUTCOUNT_1, FILE_FITTED_1, FILE_UNFITTED_1, FILE_METRICS_1, HEADER_OUT_1
from manage_csv.manage_filecount import fetch_filecount, update_filecount
from manage_csv.manage_lastfile import fetch_lastfile
from Option1_package import Packer, Item

def write_output_boxes(packer: Packer, fitting: Mode, filecount: int):

    if fitting == Mode.FITTED.value:
        filename = f'{FILE_FITTED_1}{filecount + 1}.csv'
    else:
        filename = f'{FILE_UNFITTED_1}{filecount + 1}.csv'

    with open(filename, mode = 'w', newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(HEADER_OUT_1)

        for idx,b in enumerate(packer.bins):
            items = b.items if fitting == Mode.FITTED.value else packer.unfit_items

            for item in items:
                writer.writerow([item.partno, item.name, item.color,
                                 item.width, item.height, item.depth, 
                                 float(item.width) * float(item.height) * float(item.depth),
                                 float(item.weight)])
                
            if Mode.UNFITTED.value:
                break

    csvfile.close()
    
def write_output_metrics(packer: Packer, filecount: int):
    filename = f'{FILE_METRICS_1}{filecount + 1}.txt'

    with open(filename, mode = 'w', newline = "") as file:
        volume = 0
        volume_f = 0
        volume_u = 0

        for idx,b in enumerate(packer.bins):
            volume += b.width * b.height * b.depth
            gravity = b.gravity

            for item in b.items:
                volume_f += float(item.width) * float(item.height) * float(item.depth)

        for item in packer.unfit_items:
            volume_u += float(item.width) * float(item.height) * float(item.depth)

        file.write(f'Bin input file:        {fetch_lastfile(Option.OPTION1.value, File.BIN.value)}\n')
        file.write(f'Box input file:        {fetch_lastfile(Option.OPTION1.value, File.BOX.value)}\n')
        file.write(f'Bin volume:            {volume}\n')
        file.write(f'Volume utilised:       {volume_f}\n')
        file.write(f'Residual volume:       {float(volume) - volume_f}\n')
        file.write(f'Space utilisation:     {round(volume_f / float(volume) * 100 ,2)}\n')
        file.write(f'Gravity distribution:  {gravity}\n')
        file.write(f'Unpacked volume:       {volume_u}\n')

def write_output(packer: Packer):

    if not os.path.exists(FOLDER_OUTPUTS_1):
        os.makedirs(FOLDER_OUTPUTS_1)

    filecount = fetch_filecount(FILE_OUTCOUNT_1)

    write_output_boxes(packer, Mode.FITTED.value, filecount)
    write_output_boxes(packer, Mode.UNFITTED.value, filecount)
    write_output_metrics(packer, filecount)

    update_filecount(FILE_OUTCOUNT_1, filecount)