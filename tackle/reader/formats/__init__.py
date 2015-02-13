import pkgutil
from importlib import import_module
import tackle.settings as settings
import sys

FORMAT_DEFINITION = 'TACKLE_READER_FORMAT'

readers = {}

def _find_readers(name=__name__, path=__path__):
    for importer, modname, ispkg in pkgutil.walk_packages(path=path,
                                                          prefix=name+'.',
                                                          onerror=lambda x: None):
        mod = import_module(modname)
        if FORMAT_DEFINITION in dir(mod):
            format = getattr(mod, FORMAT_DEFINITION)
            # TODO raise if mod.reader is not a function
            readers[format] = mod.reader

_find_readers()

plugin_dir = settings.plugin_dir()
if plugin_dir:
    sys.path.append(plugin_dir)
    _find_readers('plugins', [plugin_dir + 'plugins'])

def getreader(format):
    if format in readers:
        return readers[format]
    else:
        raise Exception("Reader for format '%s' not found." % format)