#!/usr/bin/env python
import logging
import os
import sys

import click

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pymorphy3
from benchmarks import speed

logger = logging.getLogger('pymorphy3.bench')
logger.addHandler(logging.StreamHandler())

@click.group()
@click.help_option('-h', '--help')
@click.version_option(version=pymorphy3.__version__, message='%(version)s')
def main():
    """ pymorphy3 benchmark utility. """

@main.command(context_settings={'show_default': True})
@click.option('-d', '--dict', 'DICT_PATH', metavar='DICT_PATH', help='Use dictionary from <DICT_PATH>')
@click.option('-r', '--repeats', default=5, help='Number of times to run each benchmarks')
@click.option('-v', '--verbose', is_flag=True, help='Be more verbose')
def run(DICT_PATH, repeats, verbose):
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    speed.bench_all(
        dict_path=DICT_PATH,
        repeats=int(repeats)
    )

    return 0


if __name__ == '__main__':
    sys.exit(main())
