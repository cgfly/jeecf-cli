import click
import configparser
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import json
import os
import requests
from urllib.parse import urljoin
from .exceptions import *


def set_config(section, option, value):
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


def get_config(section, option):
    section, option = str(section), str(option)
    config_path = os.environ['HOME'] + "/.jeecf"
    config = configparser.ConfigParser()
    if not os.path.exists(config_path):
        raise JeecfNotLoginException()
    config.read(config_path)
    if config.has_section(section):
        if config.has_option(section, option):
            return config.get(section, option)
    raise JeecfNotLoginException()


class Jeecf:

    SERVER_ERROR_INFO = "Server Error"

    @property
    def base_url(self):
        return get_config("common", "path")

    @property
    def base_data(self):
        return {
            "username": get_config("common", "username"),
            "password": get_config("common", "password"),
        }

    @classmethod
    def login(cls, base_url, username, password):
        path = urljoin(base_url, "/cli/user/login")
        data = {
            "username": username,
            "password": password
        }
        req = requests.post(url=path, json=data)
        assert req.status_code == 200, cls.SERVER_ERROR_INFO
        resp = req.json()
        if resp['success']:
            set_config("common", "username", username)
            set_config("common", "password", password)
            set_config("common", "path", base_url)
            click.echo(f"Login Success!")
        else:
            click.echo(f"Login Failed: {resp['errorMessage']}")

    def get_current_namespace(self):
        path = urljoin(self.base_url, "/cli/namespace")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            return resp['data']
        else:
            return self._get_error_message(resp)

    def set_current_namespace(self, namespace):
        path = urljoin(self.base_url, f"/cli/namespace/effect/{namespace}")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            return resp['data']
        else:
            return self._get_error_message(resp)

    def get_namespace_list(self):
        path = urljoin(self.base_url, "/cli/namespace/list")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            current = self.get_current_namespace()
            for namespace in resp['data']:
                if namespace == current:
                    namespace += " √"
                click.echo(namespace)
        else:
            return self._get_error_message(resp)

    def get_dbsource_list(self):
        path = urljoin(self.base_url, "/cli/sysDbsource/list")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            current = self.get_current_dbsource()
            for dbsource in resp['data']:
                if dbsource == current:
                    dbsource += " √"
                click.echo(dbsource)
        else:
            return self._get_error_message(resp)

    def get_current_dbsource(self):
        path = urljoin(self.base_url, "/cli/sysDbsource")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            return resp['data']
        else:
            return self._get_error_message(resp)

    def set_current_dbsource(self, dbsource):
        path = urljoin(self.base_url, f"/cli/sysDbsource/effect/{dbsource}")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            return resp['data']
        else:
            return self._get_error_message(resp)

    def get_plugin_language(self):
        path = urljoin(self.base_url, "/cli/plugin/languages")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            for lang in resp['data']:
                click.echo(lang)
            return resp['data']
        else:
            return self._get_error_message(resp)

    def get_plugin_list(self):
        namespace = self.get_current_namespace()
        path = urljoin(self.base_url, f"/cli/plugin/plugins/{namespace}")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            plugin_list = resp.get('data', [])
            for plugin in plugin_list:
                click.echo(plugin)
        else:
            return self._get_error_message()

    def get_plugin_detail(self, plugin):
        namespace = self.get_current_namespace()
        path = urljoin(self.base_url, f"/cli/plugin/detail/{namespace}/{plugin}")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            click.echo(json.dumps(resp.get('data', {}),
                                  sort_keys=True,
                                  indent=4,
                                  separators=(',', ':'),
                                  ensure_ascii=False))
        else:
            return self._get_error_message(resp)

    def get_field_list(self):
        namespace = self.get_current_namespace()
        path = urljoin(self.base_url, f"/cli/field/list/{namespace}")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            fields = resp.get('data')
            for field in fields:
                click.echo(field)
        else:
            return self._get_error_message(resp)

    def get_field_detail(self, name):
        namespace = self.get_current_namespace()
        path = urljoin(self.base_url, f"/cli/field/detail/{namespace}/{name}")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            click.echo(json.dumps(resp.get('data', {}),
                                  sort_keys=True,
                                  indent=4,
                                  separators=(',', ":"),
                                  ensure_ascii=False))
        else:
            return self._get_error_message(resp)

    def get_template_list(self):
        namespace = self.get_current_namespace()
        path = urljoin(self.base_url, f"/cli/tmpl/list/{namespace}")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            template_list = resp.get('data')
            for template in template_list:
                click.echo(template)
        else:
            return self._get_error_message(resp)

    def pull_template(self, name):
        namespace = self.get_current_namespace()
        path = urljoin(self.base_url, f"/cli/tmpl/pull/{namespace}/{name}")
        resp = self._post_data(path, self.base_data)
        if resp['success']:
            uuid = resp.get('data')
            if uuid:
                click.echo(uuid)
                self.download_template(name, uuid)
        else:
            return self._get_error_message(resp)

    def download_template(self, name, uuid):
        path = urljoin(self.base_url, f"/cli/tmpl/download/{uuid}")
        resp = requests.get(url=path)
        file_name = f"{name}.zip"
        with open(file_name, 'wb') as f:
            f.write(resp.content)
        click.echo(f"File downloaded: {file_name}")

    def gen_code(self, file_path):
        with open(file_path, 'r') as file:
            try:
                genSingleModel = yaml.load(file, Loader=Loader)
                dbsource = genSingleModel.pop('dbsource')
                namespace = genSingleModel.pop('namespace')
                params = {}
                params.update(
                    genSingleModel=genSingleModel,
                    dbsource=dbsource,
                    namespace=namespace,
                    **self.base_data
                )
                path = urljoin(self.base_url, f"/cli/tmpl/gen")
                resp = self._post_data(path, data=params)
                if resp['success']:
                    uuid = resp.get('data')
                    click.echo(uuid)
                    self.download_code(uuid, file_path)
                else:
                    click.echo(resp['errorMessage'])
            except yaml.YAMLError as e:
                click.echo(f'Error when parse {file_path} \n{e}')

    def download_code(self, uuid, file_path):
        file = file_path.split('.')[0]
        path = urljoin(self.base_url, f"/cli/tmpl/download/code/{uuid}")
        file_name = f"{file}.zip"
        resp = requests.get(url=path)
        with open(file_name, 'wb') as f:
            f.write(resp.content)
        click.echo(f"Code downloaded: {file_name}")

    def push_template(self, file_path, **kwargs):
        path = urljoin(self.base_url, f"/cli/tmpl/push")
        kwargs.update(self.base_data)
        with open(file_path, 'rb') as file:
            resp = requests.post(url=path, params=kwargs, files={'file': file},
                headers={
                    # "Content-Type": "multipart/form-data;",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept": "*/*",
                    "X-Requested-With": "XMLHttpRequest",
                }, auth=('admin', '123456')
            )
            resp = resp.json()
            if resp['success']:
                click.echo(json.dumps(resp.get('data', {}),
                                      sort_keys=True,
                                      indent=4,
                                      separators=(',', ':'),
                                      ensure_ascii=False))
            else:
                click.echo(resp['errorMessage'])


    def _post_data(self, path, data):
        req = requests.post(url=path, json=data)
        assert req.status_code == 200, self.SERVER_ERROR_INFO
        return req.json()

    def _get_error_message(self, resp):
        click.echo(f"Error: {resp['errorMessage']}")
