#!/usr/bin/env python
from setuptools import setup

INSTALL_REQUIRES = [
    "suds >= 0.4",
]

setup(
    name='turbosmsua',
    version='0.2dev',
    packages=['turbosmsua',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),

    install_requires = INSTALL_REQUIRES,
)