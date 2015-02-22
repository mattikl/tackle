"""builtin SQL writer"""

#
# very adhoc SQL writer, didn't find Python module to do this without too much hassle
#

from itertools import tee

def _stringify(value):
    return "'%s'" % value.replace("'", "''")

def _build_insert(table, columns, values):
    column_str = ",".join(["`%s`" % c for c in columns])
    value_str = ",".join(map(_stringify, values))
    return "INSERT INTO {table} ({column_str}) VALUES ({value_str});".format(**locals())

def _insert_statements(data, name):
    for r in data:
        yield _build_insert(name, r._fields, r)

def write_sqlinsert(data, options):
    return "\n".join(_insert_statements(data, options['name']))

# this syntax works with SQLite
def write_sqlcreate(data, name):
    """SQL create statement"""
    row = next(data)
    output = "CREATE TABLE %s (" % name
    output += ",".join(["`%s`" % c for c in row._fields])
    output += ");\n\n"
    return output

def write_sql(data, options):
    d1, d2 = tee(data) # very inefficient because we just need the first row from d1
    return write_sqlcreate(d1, options['name']) + write_sqlinsert(d2, options)

TACKLE_WRITER_FORMATS = {
    'sql': write_sql,
    'sqlinsert': write_sqlinsert,
}
