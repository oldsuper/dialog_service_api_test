__author__ = 'Administrator'
import ConfigParser
import os

class MCase:
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


class MScenario:
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

config_level_option_key = 'config_level'

class MConfig(ConfigParser):
    def __init__(self, config_file_path):
        if not os.path.exists(config_file_path):
            raise ValueError('ConfigFileNotExists')
        config = ConfigParser.ConfigParser()
        config.read(config_file_path)
        section_list = []
        total_options = []
        for section in config.options():
            if config.has_option(section):
                config.get(section, config_level_option_key)
            for option in config.options(section):
                total_options.append(option)

        setattr(self, )