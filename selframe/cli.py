# -*- coding: utf8 -*-
import argparse
import os
import sys

from .exceptions import AppFileNotDefined

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


def main():
    current_path = os.getcwd()
    if args.keyword == "start":
        try:
            sys.path.append(os.path.abspath(current_path))
            from app import app
        except ModuleNotFoundError:
            raise AppFileNotDefined(
                """
                You must execute selframe command from your directory
                and you must define a file named app that contains your views
            """)

        from werkzeug.serving import run_simple
        run_simple(
            args.host or '127.0.0.1',
            args.port or 5000,
            app, use_reloader=True, use_debugger=True
        )

    if args.keyword == "build":
        target_path = current_path + '\\' + (args.name or 'sample')
        os.makedirs(target_path)
        with open(target_path + '\\app.py', "w") as f:
            from .sample import sample
            f.write(sample)


if __name__ == '__main__':
    main()
