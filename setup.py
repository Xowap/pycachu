#!/usr/bin/env python
# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# (c) 2015 ActivKonnect

import os
import codecs
from distutils.core import setup


with codecs.open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r') as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pycachu',
    version='0.1.1',
    packages=['pycachu'],
    include_package_data=True,
    license='WTFPL',
    description='A basic Python package to store files in a LRU cache.',
    long_description=README,
    url='https://github.com/Xowap/pycachu',
    author='Rémy Sanchez',
    author_email='remy.sanchez@activkonnect.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
