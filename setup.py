from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup


setup(
    name='github-release',
    version='0.1',
    description='github release test',
    author='OpenDILab',
    license='Apache License, Version 2.0',
    keywords='github release test',
    packages=[
        'grelease',
        'grelease.sample',
    ],
    install_requires=[
        'trueskill'
    ]
)
