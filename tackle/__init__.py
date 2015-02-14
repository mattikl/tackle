import click

from .reader import read
from .writer import write

@click.command()
@click.argument('source', type=click.File('rb'))
@click.option('--format', help='input format')
@click.option('--charset', help='input encoding')
@click.option('--columns', help='specify input columns (comma separated)')
@click.option('-a', '--as', 'outputformat', help='output format')
@click.option('-t', '--to', 'dest', help='output file, default stdout')
@click.option('-n', '--name', help='object name')
@click.option('-l', '--limit', type=click.INT, help='limit result set length')
@click.option('-m', '--match', help='only return results matching to query')
def cli(source, format, charset, columns, outputformat, dest, name, limit, match):
    """Convert tabular data into another format"""
    read_options = {}
    for option in ("format", "charset", "columns", "limit", "match"):
        read_options[option] = locals().get(option)
    
    try:
        data = read(source, read_options)
    except Exception, e:
        raise click.ClickException(str(e))
    out = write(data, outputformat, name)
    click.echo(out)
