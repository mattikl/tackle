from collections import namedtuple
import re

def make_alphanumeric(value):
    return re.sub(r'\W', '_', value)

def makerow(headers):
    return namedtuple('Row', map(make_alphanumeric, headers))
