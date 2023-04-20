from setuptools import setup, find_packages

import os
from pathlib import Path
from setuptools import find_packages, setup

PKG_FOLDER = Path(os.path.abspath(os.path.dirname(__file__)))

with open(PKG_FOLDER / "README.md") as f:
    long_description = f.read()


setup(
    name="dnd-roller",
    version="0.0.1",
    author="Jeff Glass",
    author_email="glass.jeffrey@gmail.com",
    description="Python package to roll D&D dice in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/JeffersGlass/dnd-roller",
    include_package_data=True,
    packages=find_packages(exclude=[]),
    install_requires=["nomoji==0.0.5", "tabulate"],
)