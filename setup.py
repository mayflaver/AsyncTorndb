#!/usr/bin/env python
#
# Copyright 2014 Mayflower
#

from setuptools import setup, find_packages

version = "0.1"

setup(
    name="asynctorndb",
    version=version,
    author="Mayflower",
    author_email="fucongwang@gmail.com",
    url="https://github.com/mayflaver/AsyncTorndb",
    license="MIT",
    packages=find_packages(),
    description="async mysql client for tornado.",
    )
