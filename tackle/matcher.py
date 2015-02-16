import re
from itertools import islice, ifilter, imap

def match_value(pattern):
    if pattern is None:
        return lambda x: x

    # implementing syntax column__regex to match to match a specific column
    column_specified = re.match('(\w+)__(.*)', pattern)
    if column_specified:
        column = column_specified.group(1)
        pattern = column_specified.group(2)
    else:
        column = None

    prog = re.compile(pattern)
    
    def fun(row):
        for key, val in row.iteritems():
            if column is not None and key != column:
                continue
            if prog.match(val):
                return True
        return False
    
    return fun

def select_columns(columnstr):
    if columnstr is None:
        return lambda x: x

    columns = columnstr.split(',')

    def fun(row):
        return {k: v for k, v in row.iteritems() if k in columns}

    return fun

def matcher(reader, options):
    sliced = islice(reader, options['first'], options['last'])
    matched = ifilter(match_value(options['match']), sliced)
    selected = imap(select_columns(options['selected']), matched)
    return selected