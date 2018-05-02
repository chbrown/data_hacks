#!/usr/bin/env python

from distutils.core import setup

setup(
    name='data_hacks',
    version='0.3.1',
    description='Command line utilities for data analysis',
    author='Jehiah Czebotar',
    author_email='jehiah@gmail.com',
    url='https://github.com/bitly/data_hacks',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: System Administrators',
        'Topic :: Terminals',
    ],
    scripts=[
        'data_hacks/histogram.py',
        'data_hacks/ninety_five_percent.py',
        'data_hacks/run_for.py',
        'data_hacks/bar_chart.py',
        'data_hacks/sample.py',
    ]
)
