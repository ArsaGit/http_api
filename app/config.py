import configparser
import os

from .mylogger import get_mylogger

LOGGER = get_mylogger(__name__)


def get_cfg_dict(filename='config.ini', section='pg_remote'):
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.path.dirname(__file__), filename))

    d = {}
    if section in parser:
        for key in parser[section]:
            d[key] = parser[section][key]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return d


def get_pg_url(filename='config.ini', section='pg_remote'):
    d = get_cfg_dict(filename, section)

    pg_url = ""
    try:
        # pg_url = f"postgresql+psycopg2://{d['username']}:{d['password']}@{d['host']}:{d['port']}/{d['database']}"
        pg_url = f"postgresql://{d['username']}:{d['password']}@{d['host']}:{d['port']}/{d['database']}"
    except KeyError as e:
        LOGGER.error(f"Not enough arguments in config for url {e}")

    return pg_url
