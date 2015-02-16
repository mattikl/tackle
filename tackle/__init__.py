import click

from .reader import read
from .writer import write
from .matcher import matcher

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
def cli(source, format, charset, columns, outputformat, dest, name, first, last, match):
    """Convert tabular data into another format"""
    read_options = get_options(locals(), "format", "charset", "columns")

    try:
        reader = read(source, read_options)
    except Exception, e:
        raise click.ClickException(str(e))

    match_options = get_options(locals(), "first", "last", "match")
    filtered = matcher(reader, match_options)

    out = write(filtered, outputformat, name)
    click.echo(out)
