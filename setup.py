from setuptools import setup, find_packages

# Read version from the VERSION file
with open('VERSION', 'r') as version_file:
    version = version_file.read().strip()

setup(
name='lib-version',
version=version,
author='Nick Dubbeldam',
author_email='nick.dubbeldasm@live.nl',
description='A version-aware library designed to provide robust version management and utility functions',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)