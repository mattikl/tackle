"""builtin excel writer"""

def write_xls(data, options):
    """output xls"""

def write_xlsx(data, options):
    """output xls"""

TACKLE_WRITER_FORMATS = {
    'xls': write_xls,
    'xlsx': write_xlsx,
}
