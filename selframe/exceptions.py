# -*- coding: utf8 -*-


class DuplicateRoute(Exception):

    def __init__(self, message):
        super(DuplicateRoute, self).__init__(message)


class AppFileNotDefined(Exception):

    def __init__(self, message):
        super(AppFileNotDefined, self).__init__(message)
