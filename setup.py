#!/usr/bin/env python
"""
Flask Request ID
----------------

Adds Request ID inside your http requests to better identify what's happening on your app.
"""
from setuptools import setup

setup(
    name='flask-request-id-middleware',
    version='1.1',
    url='http://github.com/geoffreybauduin/flask-request-id',
    license='MIT',
    author='Geoffrey Bauduin',
    author_email='bauduin.geo@gmail.com',
    maintainer='Geoffrey Bauduin',
    maintainer_email='bauduin.geo@gmail.com',
    description="Adds Request ID inside your http requests to better identify what's happening on your app",
    long_description=__doc__,
    packages=['flask_request_id'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
