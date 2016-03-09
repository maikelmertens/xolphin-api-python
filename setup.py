#!/usr/bin/env python

'''The setup and build script for the xilphin-api library.'''

import os

from setuptools import setup, find_packages

readme_file = open('readme.rst', 'r')
long_description = readme_file.read()
readme_file.close()

setup(
        name='xolphin-api',
        version='1.0.0',
        author='Roman Ragimoff',
        author_email='roma.ragimoff@gmail.com',
        license='MIT',
        url='https://github.com/bearburger/xolphin-api-python',
        keywords='xolphin',
        description='Python library for Xolphin API',
        long_description=long_description,
        packages=find_packages(exclude=['tests*']),
        install_requires=['future', 'requests'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Internet',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
        ],
)