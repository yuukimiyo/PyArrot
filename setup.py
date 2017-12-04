# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme_txt = f.read()

with open('LICENSE') as f:
    license_txt = f.read()

setup(
    name='pyarrot',
    version='0.1.0',
    description='Write with interactive mode for trial and error, Get the batch mode for cron or other automation.',
    long_description=readme_txt,
    author='yuuki miyoshi',
    author_email='yuuki.miyo@gmail.com',
    url='https://github.com/yuukimiyo/PyArrot',
    license=license_txt,
    packages=find_packages(exclude=('sample'))
)
