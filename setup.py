import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("selframe/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="Selframe",
    version=version,
    project_urls={
        "Code": "https://github.com/ramibelgacem/Selframe",
    },
    license="BSD-3-Clause",
    author="Rami BELGACEM",
    author_email="ramibelgacem@gmail.com",
    maintainer="Rami Belgacem",
    maintainer_email="ramibelgacem@gmail.com",
    description="A simple framework for learning perpose.",
    long_description=readme,
    packages=find_packages("selframe"),
    package_dir={"": "selframe"},
    include_package_data=True,
    # python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=[
        "PyYAML==5.1.2"
        "Werkzeug==0.16.0"
        "argh==0.26.2"
        "atomicwrites==1.3.0"
        "attrs==19.1.0"
        "colorama==0.4.1"
        "entrypoints==0.3"
        "importlib-metadata==0.23"
        "mccabe==0.6.1"
        "more-itertools==7.2.0"
        "packaging==19.2"
        "parse==1.12.1"
        "pathlib2==2.3.5"
        "pathtools==0.1.2"
        "pluggy==0.13.0"
        "py==1.8.0"
        "pyparsing==2.4.2"
        "pytest==5.2.0"
        "scandir==1.10.0"
        "simplejson==3.16.0"
        "six==1.12.0"
        "termcolor==1.1.0"
        "typing==3.7.4.1"
        "watchdog==0.9.0"
        "wcwidth==0.1.7"
        "zipp==0.6.0"
    ],
    # extras_require={
    #     "dotenv": ["python-dotenv"],
    #     "dev": [
    #         "pytest",
    #         "coverage",
    #         "tox",
    #         "sphinx",
    #         "pallets-sphinx-themes",
    #         "sphinxcontrib-log-cabinet",
    #         "sphinx-issues",
    #     ],
    #     "docs": [
    #         "sphinx",
    #         "pallets-sphinx-themes",
    #         "sphinxcontrib-log-cabinet",
    #         "sphinx-issues",
    #     ],
    # },
    entry_points={
        "console_scripts": [
            "selframe = selframe.cli:main"
        ]
    },
)
