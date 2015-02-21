from collections import namedtuple

def makerow(columns):
	return namedtuple('Row', columns)
