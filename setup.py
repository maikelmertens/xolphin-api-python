#!/usr/bin/env python

'''The setup and build script for the xilphin-api library.'''

import os

from setuptools import setup, find_packages

def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
        name='xolphin-api',
        version='1.1.0',
        author='Roman Ragimoff',
        author_email='roma.ragimoff@gmail.com',
        license='MIT',
        url='https://github.com/bearburger/xolphin-api-python',
        keywords='xolphin',
        description='Python library for Xolphin API',
        long_description=(read('README.rst')),
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