"""
General use function to write a given set of rows into a specified
CSV output file. Usable by either option for producing all requisite
output files.
"""

import csv

def write_output(filename: str, filecount: int, header: [str], rows):
    """
    filename    - name of the CSV file to write to

    filecount   - numeric identifier of the file to prevent writing
                  over existing files

    row         - list of lists of strings containing data items to
                  write to the CSV file, one row is one entry

    header      - CSV file header containing labels for each field
    """

    with open(f'{filename}{filecount}.csv', mode = 'w', newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for row in rows:
            writer.writerow(row)

    csvfile.close()
