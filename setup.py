# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


# local path
here = os.path.abspath(os.path.dirname(__file__))

long_description = open(os.path.join(here, 'README.rst')).read()

# list requirements for setuptools
requirements = [name.rstrip() for name in open(os.path.join(here,
                'requirements.txt')).readlines()]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(here))

setup(
    name='python-diminuendo',
    version="0.1.0",
    author="Stefan \"hr\" Berder",
    author_email="hr@bonz.org",
    license="BSD 3-Clause",
    packages=find_packages(exclude=['docs', 'test*']),
    url='https://github.com/hrbonz/python-diminuendo',
    description='A generic HTML minifier for python',
    long_description=long_description,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet'
    ],
    keywords='minify html',
)
