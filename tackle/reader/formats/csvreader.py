import csv

TACKLE_READER_FORMAT = 'csv'

def reader(f):
	csv_reader = csv.reader(f)
	headers = next(csv_reader)
	return [dict(zip(headers, r)) for r in csv_reader]
