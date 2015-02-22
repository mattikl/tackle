import json
from tackle.utils import makerow

TACKLE_READER_FORMAT = 'json'

def read_json(f, options):
	"""builtin json reader

You need to provide either an array of objects, or array or arrays and provide the column names
"""
	data = json.load(f)
	if type(data) != list:
		raise Exception("JSON data must be an array")
	headers = data[0].keys() # TODO or from options
	Row = makerow(headers)
	for r in data:
		yield Row(*r.values())

def write_json(data, options):
	object_name = options['name']
	# TODO must be a nicer way to serialize namedtuple as json?
	data = [r._asdict() for r in data]
	if object_name is not None:
		output = {object_name: data}
	else:
		output = data
	return json.dumps(output, indent=True)

TACKLE_READER_FORMATS = {
    'json': read_json,
}

TACKLE_WRITER_FORMATS = {
	'json': write_json,
}