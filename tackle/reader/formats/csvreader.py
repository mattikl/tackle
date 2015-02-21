"""Builtin csv reader"""

import csv
from tackle.utils import makerow

TACKLE_READER_FORMAT = 'csv'

def reader(f, options):
    headers = options["columns"]
    charset = options["charset"]
    stream = decode(f, charset) if charset is not None else f

    csv_reader = csv.reader(stream)
    if headers is None:
        headers = next(csv_reader)

    Row = makerow(headers)
    for r in csv_reader:
        # TODO if fewer columns than values, then strip remaining column
        # the other way around just return nulls
        if len(r) == len(headers):
            yield Row(*r)

def decode(stream, charset):
    for line in stream:
        yield line.decode(charset).encode('utf-8')