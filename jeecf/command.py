import click
import getpass
import requests
import sys
from urllib.parse import urljoin
from .config import set_config, get_config


@click.group()
def main():
    pass


@main.command()
@click.argument("path", required=True)
@click.option("--username")
@click.option("--password")
def login(path, username, password):
    if not path:
        path = "http://127.0.0.1:8801"
    else:
        if not path.startswith("http"):
            click.echo("Error:", color="Red")
            sys.exit("The url should starts with http or https...")
    if not username:
        username = input("username:")
    if not password:
        password = getpass.getpass("password:")
    path = urljoin(path, "/cli/user/login")
    data = {
        "username": username,
        "password": password
    }
    req = requests.post(url=path, json=data)
    assert req.status_code == 200, "Server Error"
    try:
        resp = req.json()
        if resp['success']:
            set_config("login", "username", username)
            set_config("login", "password", password)
            click.echo("Login Success!")
        else:
            click.echo(f"Login Failed: {resp['errorMessage']}")
    except ValueError as e:
        click.echo(f"json value error: {e}")
    except Exception as e:
        click.echo(f"jeecf error: {e}")



