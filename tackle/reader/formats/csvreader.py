import csv

TACKLE_READER_FORMAT = 'csv'

def reader(f, options):
    headers = options["columns"]
    csv_reader = csv.reader(f)
    if headers is None:
        headers = next(csv_reader)

    for row in csv_reader:
        # TODO if fewer columns than values, then strip remaining column
        # the other way around just return nulls
        if len(row) == len(headers):
            yield dict(zip(headers, row))

