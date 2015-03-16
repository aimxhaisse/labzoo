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
    description = ("An environment to write, run and visualize checks "
                   "on remote hosts."),
    license = "MIT",
    url = "http://mxs.sbrk.org/",
    packages=['labzoo'],
    install_requires=[
        'DateTime == 4.0.1',
        'Flask == 0.10.1',
        'PyYAML == 3.11',
        'SQLAlchemy == 0.9.8',
    ],
    entry_points = {
        'console_scripts': [
            'labzoo-run = labzoo.bin.run:main',
            'labzoo-process = labzoo.bin.process:main',
            'labzoo-report = labzoo.bin.report:main',
        ],
    },
)
