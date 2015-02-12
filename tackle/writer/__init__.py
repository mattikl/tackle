import json

# as of now ignore format and just write json for testing
def write(data, format, object_name):
	if object_name is not None:
		output = {object_name: data}
	else:
		output = data
	return json.dumps(output, indent=True)