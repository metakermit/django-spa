#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'whitenoise==5.0.1'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='django-spa',
    version='0.3.5',
    description="Simple Django configuration to serve a single-page app",
    long_description=readme + '\n\n' + history,
    author="Dražen Lučanin",
    author_email='kermit666@gmail.com',
    url='https://github.com/metakermit/django-spa',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='django spa django-spa react angular yeoman heroku',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
