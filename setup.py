#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(name='CoinigyREST',
      version='0.0.1',
      description='Python Coinigy REST API',
      author='William Phan',
      author_email='wphan@live.ca',
      url='http://github.com/wphan/CoinigyRESTPython',
      packages=find_packages(),
      scripts=['scripts.py'],
      )
