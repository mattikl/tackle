import json
from tackle.utils import makerow

TACKLE_READER_FORMAT = 'json'

# TODO fromdict
def reader(f, options):
	data = json.load(f)
	if type(data) != list:
		raise Exception("JSON data must be an array")
	headers = data[0].keys() # TODO or from options
	Row = makerow(headers)
	for r in data:
		yield Row(*r.values())