#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "geoapi",
    version = "1.0.1",
    url = 'https://github.com/ondrejsika/light-geo-api/',
    license = 'MIT',
    description = "Geo API",
    author = 'Ondrej Sika',
    author_email = 'ondrej@ondrejsika.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = ["flask", "psycopg2"],
)
