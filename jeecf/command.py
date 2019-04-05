import argparse
import configparser
import getpass
import os
import requests
import sys
from urllib.parse import urljoin


def main():
    command = Command()
    options = sys.argv[1:]
    command(options)


class Command:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8801"

    def parse_arguments(self, options):
        parser = argparse.ArgumentParser()
        parser.add_argument('login')
        return parser.parse_args(options)

    def __call__(self, options):
        command = self.parse_arguments(options)
        if command.login:
            username = input("username:")
            password = getpass.getpass(prompt="password:")
            result = self.login(username, password)
            print(result)

    def login(self, username, password):
        path = urljoin(self.base_url, "/cli/user/login")
        data = {
            "username": username,
            "password": password
        }
        req = requests.post(url=path, json=data)
        assert req.status_code == 200, "Server Error"
        try:
            resp = req.json()
            if resp['success']:
                self.set_config("login", "username", username)
                self.set_config("login", "password", password)
                return "Login Success!"
            else:
                return f"Login Failed: {resp['errorMessage']}"
        except ValueError as e:
            return f"json value error: {e}"
        except Exception as e:
            return f"jeecf error: {e}"

    def set_config(self, section, option, value):
        section, option, value = str(section), str(option), str(value)
        config_path = os.environ['HOME'] + "/.jeecf"
        config = configparser.ConfigParser()
        if not os.path.exists(config_path):
            f = open(config_path, "w")
            f.close()
        config.read(config_path)
        if not config.has_section(section):
            config.add_section(section)
        config.set(section, option, value)
        config.write(open(config_path, "w"))
