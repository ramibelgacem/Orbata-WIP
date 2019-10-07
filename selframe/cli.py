# -*- coding: utf8 -*-
import argparse
import os
import sys
import importlib

from .logging import logger
from .exceptions import AppFileNotDefined


class CliBase(object):
    def __init__(self, args, path):
        self.args = args
        self.path = path


class CliBuild(CliBase):
    def _execute(self):
        logger.info("Building the project called {}".format(self.path))
        target_path = self.path + '\\' + (self.args.name or 'sample')
        os.makedirs(target_path)
        with open(target_path + '\\app.py', "w") as f:
            from .sample import sample
            f.write(sample)


class CliStart(CliBase):
    def _execute(self):
        logger.info("The server will begin")
        try:
            sys.path.append(os.path.abspath(self.path))
            from __discipline__ import VIEWS_DIR, MODELS_DIR, TEMPLATES_DIR, STATIC_DIR

            for views in VIEWS_DIR:
                importlib.import_module(views)
                # for root, dirs, files in os.walk(self.path + '\\' + views, topdown=True):
                #     for file_name in files:

        except ModuleNotFoundError:
            raise AppFileNotDefined(
                """
                You must execute selframe command from your directory
                and you must define a file named app that contains your views
            """)

        from werkzeug.serving import run_simple
        run_simple(
            self.args.host or '127.0.0.1',
            self.args.port or 5000,
            app, use_reloader=True, use_debugger=True
        )


cli_factory = {
    'build': CliBuild,
    'start': CliStart,
}


def build_commands():
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

    return parser.parse_args()


def main():
    args = build_commands()
    current_path = os.getcwd()
    if cli_factory.get(args.keyword, False):
        command = cli_factory[args.keyword](args, current_path)
        command._execute()


if __name__ == '__main__':
    main()
