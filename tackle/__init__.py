import click

from .reader import read

@click.command()
@click.argument('source', type=click.File('rb'))
@click.option('--format', help='input format')
@click.option('--charset', help='input encoding')
@click.option('-a', '--as', 'filetype', help='output format')
@click.option('-t', '--to', 'dest', help='output file, default stdout')
@click.option('-n', '--name', help='object name')
@click.option('-l', '--limit', type=click.INT, help='limit result set length')
@click.option('-m', '--match', help='only return results matching to query')
def cli(source, format, charset, filetype, dest, name, limit, match):
    """Convert tabular data into another format"""
    click.echo("convert from %s" % source.name)
    try:
    	data = read(source, format)
    except Exception, e:
    	raise click.ClickException(str(e))
    click.echo(data)
