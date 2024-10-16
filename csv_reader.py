import csv


def read_csv_file(filename):
    data = []
    with open(filename, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)  # Append each row (a dictionary) to the list
    return data
