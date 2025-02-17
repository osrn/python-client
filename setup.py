import sys

import setuptools


# Utility function to read the README file.
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = ["requests", "backoff", "flatten_dict"]

tests_require = [
    "flake8==4.0.1",
    "flake8-import-order==0.18.1",
    "flake8-print==4.0.1",
    "flake8-quotes==3.3.1",
    "pytest==7.0.1; python_version < '3.7'",
    "pytest==7.1.2; python_version >= '3.7'",
    "isort==5.10.1",
    "pytest-cov==2.5.1",
    "pytest-responses>=0.3.0",
    "pytest-mock>=1.10.0",
    "black==22.3.0",
    "build==0.8.0",
    "twine==3.8.0",
]

extras_require = {"test": tests_require, "dev": requires + tests_require}

setup_requires = ["pytest-runner"] if {"pytest", "test", "ptr"}.intersection(sys.argv) else []

setuptools.setup(
    name="solar-client",
    description="A simple Python API client for the Solar Blockchain.",
    version="3.0.0",
    author="Solar Network",
    author_email="hello@solar.org",
    url="https://github.com/solar-network/python-client",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
    python_requires=">=3.6",
)
