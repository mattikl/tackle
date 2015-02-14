from .formats import getreader

def read(f, options):
    format = options["format"]
    if format is None:
        format = f.name.lower().split('.')[-1]
    else:
        format = format.lower()
    reader = getreader(format)
    return reader(f, options)
