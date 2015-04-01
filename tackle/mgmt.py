import click
import os

from . import settings
from .formats import readers, writers

def mkdir(path):
    try:
        os.mkdir(path)
    except OSError, e:
        raise click.ClickException("Coudn't create directory: %s" % e)

def touch(filename):
    try:
        f = open(filename, 'w')
        f.write('')
    except Exception, e:
        raise click.ClickException("Coudn't create file: %s" % e)

@click.group()
def mgmt():
    """Tackle management commands"""

@mgmt.command()
@click.option('--path', type=click.Path(exists=False),
              default=os.path.join(os.getenv('HOME'), '.tackle'))
def createdir(path):
    """Create tackle directory"""
    if os.path.exists(path):
        click.echo("Path %s already exists." % path)
    else:
        mkdir(path)
        click.echo("Created tackle directory %s" % path)

    pluginpath = os.path.join(path, "plugins")
    if not os.path.exists(pluginpath):
        mkdir(pluginpath)
    initpy = os.path.join(pluginpath, '__init__.py')
    if not os.path.exists(initpy):
        touch(os.path.join(initpy))
    click.echo("You can now place plugins in %s" % pluginpath)


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
