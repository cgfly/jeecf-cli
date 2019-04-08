import click
import getpass
import sys
from .jeecf import Jeecf


@click.group()
def main():
    """
    jeecf client command toooool
    """


@main.command()
@click.argument("path", required=True)
@click.option("--username", type=click.STRING)
@click.option("--password", type=click.STRING)
def login(path, username, password):
    if path:
        if not path.startswith("http"):
            click.echo("Error:")
            sys.exit("The url should starts with http or https...")

    if not username:
        username = input("username:")
    if not password:
        password = getpass.getpass("password:")
    Jeecf.login(path, username, password)


@main.command()
@click.argument("command", required=False, type=click.Choice(['use']))
@click.argument("name", required=False)
def namespace(command, name):
    if command == 'use':
        click.echo(Jeecf().set_current_namespace(name))
    else:
        Jeecf().get_namespace_list()


@main.command()
@click.argument("command", required=False, type=click.Choice(['use']))
@click.argument("name", required=False)
def dbsource(command, name):
    if command == 'use':
        click.echo(Jeecf().set_current_dbsource(name))
    else:
        Jeecf().get_dbsource_list()


@main.command()
@click.argument("command", required=False, type=click.Choice(['detail', 'language']))
def plugin(command):
    if command == 'language':
        pass
    elif command == 'detail':
        pass
    else:
        pass
