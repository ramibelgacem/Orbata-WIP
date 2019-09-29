# -*- coding: utf8 -*-


class DuplicateRoute(Exception):

    def __init__(self, message):
        super(DuplicateRoute, self).__init__(message)
