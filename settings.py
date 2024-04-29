from configparser import ConfigParser

CONFIG_FILE = "config.ini"
config_parser = ConfigParser()
config_parser.read_file(open(CONFIG_FILE))
default_config = dict(config_parser["default"])
consumer_config = dict(config_parser["consumer"])
producer_config = dict(config_parser["producer"])
