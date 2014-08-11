#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

setup(
    name='text_histogram',
    version='0.0.1',
    description='Repackage Bit.ly\'s data_hacks for convenient use.',
    long_description=readme,
    author='Andy Kish',
    author_email='agkish@gmail.com',
    url='https://github.com/Kobold/text_histogram',
    py_modules=['text_histogram'],
    license='Apache License, Version 2.0',
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Terminals',
    ]
)