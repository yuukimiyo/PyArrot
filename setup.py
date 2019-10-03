# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='pyarrot',
    version='0.1.2',
    description='Helper functions for interactive mode.',
    long_description='Helper functions for interactive mode.',
    author='yuuki miyoshi',
    author_email='yuuki.miyo@gmail.com',
    url='https://github.com/yuukimiyo/PyArrot',
    license="MIT",
    keywords="interactive batch",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
