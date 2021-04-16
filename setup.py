import os
import re

from setuptools import find_packages, setup


def get_version(filename='__init__.py'):
    here = os.path.abspath(os.path.dirname(__file__))
    version_re = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')
    with open(os.path.join(here, 'bmc', filename)) as f:
        content = f.read()
    return version_re.search(content).group(1)


def get_requirements(filename='requirements.txt'):
    with open(filename) as f:
        _requirements = f.read().split('\n')
    return [req for req in _requirements if req]


def get_long_description(filename='README.md'):
    with open(filename) as f:
        long_description = f.read()
    return long_description

setup(
    name='bmc',
    version=get_version(),
    packages=find_packages(),
    author="BIGmama Technology",
    author_email="contact@big-mama.io",
    description="Python wrapper for Minio Admin",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    install_requires=get_requirements(),
    include_package_data=True,
    url='http://gitlab.com/big-mama-tech/bmc',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
    ],
    license="Proprietary", )
