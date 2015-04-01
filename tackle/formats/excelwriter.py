"""builtin excel writer"""

import tablib

def _build_tablib_object(data):
    dataset = None
    for row in data:
        if not dataset:
            dataset = tablib.Dataset(headers=row._fields)
        dataset.append(row)
    return dataset

def write_xls(data, options):
    """output xls"""
    return _build_tablib_object(data).xls

def write_xlsx(data, options):
    """output xls"""
    return _build_tablib_object(data).xlsx

TACKLE_WRITER_FORMATS = {
    'xls': write_xls,
    'xlsx': write_xlsx,
}
