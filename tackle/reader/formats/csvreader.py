"""Builtin csv reader"""

import csv

TACKLE_READER_FORMAT = 'csv'

def reader(f, options):
    headers = options["columns"]
    charset = options["charset"]
    stream = decode(f, charset) if charset is not None else f

    csv_reader = csv.reader(stream)
    if headers is None:
        headers = next(csv_reader)

    for row in csv_reader:
        # TODO if fewer columns than values, then strip remaining column
        # the other way around just return nulls
        if len(row) == len(headers):
            yield dict(zip(headers, row))

def decode(stream, charset):
    for line in stream:
        yield line.decode(charset).encode('utf-8')