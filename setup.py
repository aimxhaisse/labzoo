# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, find_packages


MODULE_NAME = 'labzoo'


def get_version():
    with open(os.path.join(
            os.path.dirname(__file__), MODULE_NAME, '__init__.py')
          ) as init:
        for line in init.readlines():
            res = re.match(r'__version__ *= *[\'"]([0-9\.]*)[\'"]$', line)
            if res:
                return res.group(1)


setup(
    name = MODULE_NAME,
    version = get_version(),
    author = u"Sébastien Rannou",
    author_email = "mxs@sbrk.org",
    description = ("An environment to write, run and visualize benchmarks and "
                   "tests on remote hosts."),
    license = "MIT",
    url = "http://mxs.sbrk.org/",
    packages=['labzoo'],
)
