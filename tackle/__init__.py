import click

from itertools import tee

from .formats import read, write
from .matcher import matcher

DEFAULT_OUTPUT_FORMAT = 'json'

def get_options(all_options, *names):
    return {k: v for k, v in all_options.items() if k in names}

@click.command()
@click.argument('source', type=click.File('rb'))
@click.option('--format', help='input format')
@click.option('--charset', help='input encoding, default utf-8')
@click.option('--columns', help='specify input columns (comma separated)')
@click.option('-a', '--as', 'outputformat', help='output format')
@click.option('-t', '--to', 'dest', help='output file, default stdout')
@click.option('-n', '--name', help='object name')
@click.option('--first', type=click.INT, help='index of first row returned')
@click.option('--last', type=click.INT, help='index of last row returned')
@click.option('-m', '--match', help='only return results matching to query')
@click.option('--selected', help='only return selected columns')
def cli(source, format, charset, columns, outputformat,
        dest, name, first, last, match, selected):
    """Convert tabular data into another format"""
    read_options = get_options(locals(), "format", "charset", "columns")
    match_options = get_options(locals(), "first", "last", "match", "selected")
    try:
        reader = read(source, read_options)
    except Exception, e:
        raise click.ClickException("Exception from reader: %s" % str(e))

    if dest is not None and outputformat is None:
        outputformat = dest.split('.')[-1]

    if outputformat is None:
        outputformat = DEFAULT_OUTPUT_FORMAT

    write_options = get_options(locals(), "outputformat", "name")
    filtered = matcher(reader, match_options)
    chartest, outstream = tee(filtered)

    # test that output stream is utf8
    # TODO doesn't test headers
    try:
        for row in chartest:
            for val in row:
                val.decode('utf-8')
    except UnicodeDecodeError, e:
        raise click.ClickException("Reader didn't return valid utf-8")

    try:
        output = write(outstream, write_options)
        if dest is None:
            click.echo(output)
        else:
            with open(dest, 'w') as f:
                f.write(output)
    except Exception, e:
        raise click.ClickException("Exception from writer: %s" % str(e))
