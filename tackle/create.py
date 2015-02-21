import click
from . import settings

@click.group()
def create():
    """Create tackle directory or plugin"""

@create.command()
@click.option('--path', help='directory path')
def dir(path):
    """Create tackle directory"""
    click.echo('create dir')

@create.command()
def plugin():
    """Create tackle plugin"""
    click.echo('create plugin')
