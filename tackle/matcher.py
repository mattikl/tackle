import re

def matcher(reader, options):
    # TODO filter by first, last, match
    for row in reader:
        yield row
