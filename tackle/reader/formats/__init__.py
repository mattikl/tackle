import pkgutil
from importlib import import_module

FORMAT_DEFINITION = 'TACKLE_READER_FORMAT'

readers = {}

def _find_readers(package):
    for importer, modname, ispkg in pkgutil.walk_packages(path=__path__,
                                                          prefix=__name__+'.',
                                                          onerror=lambda x: None):
        mod = import_module(modname)
        if FORMAT_DEFINITION in dir(mod):
            format = getattr(mod, FORMAT_DEFINITION)
            # TODO raise if mod.reader is not a function
            readers[format] = mod.reader

_find_readers(__package__)
# TODO _find_readers(settings.user_readers)

def getreader(format):
    if format in readers:
        return readers[format]
    else:
        raise Exception("Reader for format '%s' not found." % format)