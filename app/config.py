try:
    from ConfigParser import ConfigParser
except ImportError as e:
    from configparser import ConfigParser

from os.path import join, abspath, dirname

config = ConfigParser()
config_path = join(abspath(dirname(dirname(__file__))), 'config', 'config.cfg')
config.read(config_path)


def parse_config(app_name="local"):
    '''Parse config for the given app name'''
    return dict(config.items(app_name))
