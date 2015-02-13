import os

PLUGIN_DIR_VAR = 'TACKLE_PLUGIN_DIR'

def plugin_dir():
	return os.environ.get(PLUGIN_DIR_VAR)
