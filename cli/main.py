import click
from .command import BaseCommand

@click.command(cls=BaseCommand)
def cli():
    pass