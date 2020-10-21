#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from pathlib import Path
from setuptools import find_packages, setup


ROOT_PATH = Path(__file__).parent

LICENSE_PATH = ROOT_PATH / 'LICENSE'

README_PATH = ROOT_PATH / 'README.md'

REQUIREMENTS_PATH = ROOT_PATH / 'requirements.txt'

#REQUIREMENTS_PATH = ROOT_PATH / 'requirement' / 'main.txt'

#REQUIREMENTS_TEST_PATH = ROOT_PATH / 'requirement' / 'test.txt'

#REQUIREMENTS_RQ_PATH = ROOT_PATH / 'requirement' / 'extras-rq.txt'

setup(
    name='covid_cdmx_daily',
    version='0.1.0',
    description='Paquetería para hacer análisis sobre SARS-CoV-2 en la ciudad de México',
    long_description=README_PATH.read_text(),
    long_description_content_type="text/markdown",
    author='Angel Rafael Ortega Ramírez',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    license='MIT License',
)
