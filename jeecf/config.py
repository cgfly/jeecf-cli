import os
import configparser


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


def get_config(section, option, value):
    section, option, value = str(section), str(option), str(value)
