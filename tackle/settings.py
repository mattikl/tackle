import os

PLUGIN_DIR_VAR = 'TACKLE_PLUGIN_DIR'

def plugin_dir():
	return os.environ.get(PLUGIN_DIR_VAR)

plugin_template = '''"""describe your plugin here"""

from tackle.utils import rowsfromdict, rowsfromlist

def read_%(name)s(f, options):
	pass

TACKLE_READER_FORMATS = {
    'format': read_%(name)s,
}

# TACKLE_WRITER_FORMATS = {
#     'format': write%(name)s,
# }
'''