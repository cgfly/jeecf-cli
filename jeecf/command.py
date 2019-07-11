import click
import getpass
import sys
from .jeecf import Jeecf


@click.group()
def main():
    """
    Jeecf client commandline toooool.

    Documents: https://github.com/cgfly/jeecf-cli
    """


@main.command()
def version():
    click.echo("0.0.3")


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
@click.option("--language", required=False, is_flag=True)
@click.argument("name", required=False, type=click.STRING)
def plugin(language, name):
    if language:
        Jeecf().get_plugin_language()
    elif name:
        Jeecf().get_plugin_detail(name)
    else:
        Jeecf().get_plugin_list()


@main.command()
@click.argument("subcommand", required=False, type=click.Choice(['pull', 'push']))
@click.argument("name", required=False)
def template(subcommand, name):
    if subcommand == 'pull':
        Jeecf().pull_template(name)
    elif subcommand == 'push':
        Jeecf().push_template(
            name,
            field=click.prompt('field', default=''),
            language=click.prompt('language', default=''),
            version=click.prompt('version', default=''),
            tags=click.prompt('tags', default=''),
            namespace=click.prompt('namespace', default=''),
            description=click.prompt('description', default=''),
            wiki_uri=click.prompt('wiki_uri', default=''),
        )
    else:
        Jeecf().get_template_list()


@main.command()
@click.argument("name", required=True)
@click.option('--table_name',required=False, type=click.STRING)
@click.option('--namespace',required=False, type=click.STRING)
@click.option('--dbsource',required=False, type=click.STRING)
@click.option('--template',required=False, type=click.STRING)
def gen(name, table_name, namespace, dbsource, template):
    Jeecf().gen_code(name, table_name, namespace, dbsource, template)


@main.command()
def logout():
    Jeecf().logout()
