#!/usr/bin/env python3

import os, sys
import re
from distutils.core import setup

setup(
    name='chessbattle.ai',
    version='0.0.1',
    description='Write chess AIs to battle against each other.',
    author='William Findlay, Tri Do',
    author_email='william.findlay@carleton.ca, <Tri\'s email>',
    url='https://github.com/willfindlay/chessbattle.ai',
    packages=['chessbattle'],
    # include_package_data=True,
)
