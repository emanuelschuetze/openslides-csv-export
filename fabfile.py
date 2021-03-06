# -*- coding: utf-8 -*-

import sys

from fabric.api import local
from fabric.contrib import django


def check():
    """
    Checks for PEP 8 and other errors in openslides_csv_export and in tests.
    """
    local('flake8 --max-line-length=150 --statistics openslides_csv_export')
    local('flake8 --max-line-length=150 --statistics tests')


def test(module='tests'):
    """
    Runs the unit tests.
    """
    sys.path.insert(0, '')
    django.settings_module('tests.settings')
    sys.argv.pop()
    sys.argv.extend(['test', module])
    from django.core import management
    management.execute_from_command_line()


def prepare_commit():
    """
    Does everything that should be done before a commit.

    At the moment it is running the tests and checks for PEP 8 and other errors.
    """
    test()
    check()


def travis_ci():
    """
    Command that is run by Travis CI.
    """
    test()
    check()
