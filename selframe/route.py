# -*- coding: utf8 -*-
import parse

from .exceptions import DuplicateRoute
from .logging import logger


class Router(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            if self.routes.get(path, False):
                raise DuplicateRoute(
                    "This route {} is duplicated".format(path))
            self.routes[path] = handler
            logger.info("Adding the route {}".format(path))
            return handler
        return wrapper

    def find_hundler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse.parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return False, False
