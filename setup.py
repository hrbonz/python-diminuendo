# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

long_description = open(os.path.join(here, 'README.rst')).read()

# allow setup.py to be run from any path
#os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='python-diminuendo',
    version="0.0.1-alpha",
    author="Stefan \"hr\" Berder",
    author_email="hr@bonz.org",
    license="BSD 3-Clause",
    packages=find_packages(exclude=['docs', 'test*']),
    url='https://github.com/hrbonz/python-diminuendo',
    description='A generic HTML minifier for python',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet'
    ],
    keywords='minify',
)
