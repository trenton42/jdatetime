#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='jdatetime',
    version='0.1.0',
    description='A Julian date time replacement',
    long_description=readme + '\n\n' + history,
    author='Trenton Broughton',
    author_email='trenton@devpie.com',
    url='https://github.com/trenton42/jdatetime',
    packages=[
        'jdatetime',
    ],
    package_dir={'jdatetime': 'jdatetime'},
    include_package_data=True,
    install_requires=[
        'pytz'
    ],
    entry_points = {
        'console_scripts': ['jdate=jdatetime.command_line:main'],
    },
    license="BSD",
    zip_safe=False,
    keywords='jdatetime',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
