#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='PyRunner API',
    version='0.1',
    description='REST API to run your code',
    author='Merlin Webster',
    author_email='mjftwebster@gmail.com',
    url='https://github.com/mjftw/pyrunner-api',
    license='GPLv3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'pytest',
        'flask'
    ]
)
