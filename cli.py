# -*- coding: utf8 -*-
import argparse

parser = argparse.ArgumentParser(
    prog="selframe",
    usage='%(prog)s [options] keyword',
    description="Selframe command line application",
    epilog="Code well!",
    allow_abbrev=False,
)

parser.add_argument(
    'keyword',
    type=str,
    choices=['build', 'start'],
    help="Build a project or start the server",
)

build_group = parser.add_argument_group('build', 'Build a project')
build_group.add_argument(
    '--name',
    type=str,
    help="The name of the new project",
)

start_group = parser.add_argument_group('start', 'Start the server')
start_group.add_argument(
    '--host',
    type=str,
    help="The host of the web server",
    action='store',
    default='127.0.0.1',
)
start_group.add_argument(
    '--port',
    type=int,
    help="The port of the web server",
    action='store',
    default='5000',
)

args = parser.parse_args()
