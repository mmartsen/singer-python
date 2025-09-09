#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

setup(name="singer-python",
      version='6.1.1',
      description="Singer.io utility library",
      author="Stitch",
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      url="http://singer.io",
      install_requires=[
          'pytz>=2018.4',
          'jsonschema>=4.0.0,==4.*',
          'simplejson>=3.13.2,==3.*',
          'python-dateutil>=2.7.3,==2.*',
          'backoff>=2.2.1,==2.*',
          'ciso8601>=2.3.1,==2.*',
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipython',
              'ipdb',
              'pynose',
              'singer-tools @ git+https://github.com/mmartsen/singer-tools.git',
          ]
      },
      packages=find_packages(),
      package_data = {
          'singer': [
              'logging.conf'
              ]
          },
)
