import json

from .formats import sql # for testing

def write(data, format, object_name):
	return sql.write_sql(data, object_name)

# as of now ignore format and just write json for testing
def writex(data, format, object_name):
	# TODO must be a nicer way to serialize namedtuple as json?
	data = [r._asdict() for r in data]
	if object_name is not None:
		output = {object_name: data}
	else:
		output = data
	return json.dumps(output, indent=True)