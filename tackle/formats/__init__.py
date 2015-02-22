import pkgutil
from importlib import import_module
import tackle.settings as settings
import sys

READER_FORMAT_DEFINITIONS = 'TACKLE_READER_FORMATS'
WRITER_FORMAT_DEFINITIONS = 'TACKLE_WRITER_FORMATS'

readers = {}
writers = {}

def _add_formatters(formats, storage):
    for format, fun in formats.iteritems():
        # TODO raise if fun is not a function
        # TODO warn if already exists
        storage[format] = fun


def _find_plugins(name=__name__, path=__path__):
    for importer, modname, ispkg in pkgutil.walk_packages(path=path,
                                                          prefix=name+'.',
                                                          onerror=lambda x: None):
        mod = import_module(modname)

        if READER_FORMAT_DEFINITIONS in dir(mod):
            formats = getattr(mod, READER_FORMAT_DEFINITIONS)
            _add_formatters(formats, readers)

        if WRITER_FORMAT_DEFINITIONS in dir(mod):
            formats = getattr(mod, WRITER_FORMAT_DEFINITIONS)
            _add_formatters(formats, writers)

_find_plugins()

plugin_dir = settings.plugin_dir()
if plugin_dir:
    sys.path.append(plugin_dir)
    _find_plugins('plugins', [plugin_dir + 'plugins'])

def getreader(format):
    if format in readers:
        return readers[format]
    else:
        raise Exception("Reader for format '%s' not found." % format)

def read(f, options):
    format = options["format"]
    if format is None:
        format = f.name.lower().split('.')[-1]
    else:
        format = format.lower()
    reader = getreader(format)
    return reader(f, options)

# TODO refactor reader and writer handling, so much code in common

def getwriter(format):
    if format in writers:
        return writers[format]
    else:
        raise Exception("Writer for format '%s' not found." % format)

def write(f, options):
    format = options["outputformat"]
    if format is None:
        format = f.name.lower().split('.')[-1]
    else:
        format = format.lower()
    writer = getwriter(format)
    return writer(f, options)
