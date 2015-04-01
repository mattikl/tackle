import click
from . import settings
from .formats import readers, writers

@click.group()
def mgmt():
    """Tackle management commands"""

@mgmt.command()
@click.option('--path', help='directory path')
def createdir(path):
    """Create tackle directory"""
    click.echo('create dir')

@mgmt.command()
def createplugin():
    """Create tackle plugin"""
    click.echo('create plugin')

def firstline(obj):
    return obj.splitlines()[0] if isinstance(obj, str) and len(obj) else ""

@mgmt.command()
@click.option('-r', '--readers', 'showread', is_flag=True, help='show only readers')
@click.option('-w', '--writers', 'showwrite', is_flag=True, help='show only writers')
def show(showread, showwrite):
    """Show available formatters"""
    showall = showread == showwrite
    if showread or showall:
        click.echo("Readers:")
        for r, fun in readers.iteritems():
            click.echo("\t%s\t\t%s" % (r, firstline(fun.__doc__)))
    if showwrite or showall:
        click.echo("Writers:")
        for r, fun in writers.iteritems():
            click.echo("\t%s\t\t%s" % (r, fun.__doc__))
