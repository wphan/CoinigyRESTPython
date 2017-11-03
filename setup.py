#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='coinigy REST API',
      version='0.0.1',
      description='Python Coinigy REST API',
      author='William Phan',
      author_email='wphan@live.ca',
      url='http://github.com/wphan/CoinigyRESTPython',
      packages=['coinigy'],
      scripts=['scripts.py'],
      )
