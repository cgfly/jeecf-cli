import argparse
import sys

from .jeecf import Jeecf
from .auth import Auth


def main():
    command = Command()
    options = sys.argv[1:]
    command(options)


class Command:

    def __init__(self, *args, **kwargs):
        self.base_url = "http://127.0.0.1:8801"

    def parse_arguments(self, options):
        parser = argparse.ArgumentParser()
        parser.add_argument('login')
        return parser.parse_args(options)

    def __call__(self, options):
        command = self.parse_arguments(options)
        if command.login:
            self.login()

    def login(self):
        print('login func', self.base_url)


if __name__ == '__main__':
    main()
