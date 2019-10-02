# coding=utf-8

__author__ = 'Administrator'

import nose
from utils.struct import *
import yaml
from pprint import pprint
import json
import ConfigParser

def setup():
    pass


def teardown():
    pass


def test_generator():
    config = ConfigParser.ConfigParser()
    config.read('../conf/test.properties')
    total_options = []
    for section in ['default', 'global']:
        for option in config.options(section):
            total_options.append(option)


def test():
    cd = yaml.load(open('../case/case.yml'), Loader=yaml.Loader)
    for d in cd:
        tc = TestCase(**d)
        print tc.__dict__


if __name__ == '__main__':
    test_generator()
