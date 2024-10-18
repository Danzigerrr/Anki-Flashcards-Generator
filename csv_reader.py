import csv


def read_csv_file(filename, delimiter=','):
    data = []
    with open(filename, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in csv_reader:
            data.append(row)
    return data
