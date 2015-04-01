import click
from . import settings

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

@mgmt.command()
def show():
	"""Show plugins available plugins"""
	