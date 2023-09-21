import csv

def write_output(filename: str, filecount: int, rows: [str], header: [str]):

    with open(f'{filename}{filecount}.csv', mode = 'w', newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for row in rows:
            writer.writerow(row)

    csvfile.close()