import json

TACKLE_READER_FORMAT = 'json'

# TODO fromdict
def reader(f, options):
	data = json.load(f)
	if type(data) != list:
		raise Exception("JSON data must be an array")
	return data