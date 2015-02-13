import csv

TACKLE_READER_FORMAT = 'csv'

def reader(f, charset, headers):
    csv_reader = csv.reader(f)
    if headers is None:
        headers = next(csv_reader)
    # TODO if fewer columns than values, then strip remaining column
    # the other way around just return nulls
    return [dict(zip(headers, r)) for r in csv_reader if len(r) == len(headers)]
