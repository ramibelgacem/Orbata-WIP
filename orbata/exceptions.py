# -*- coding: utf8 -*-
class SingletonInstance(Exception):
    def __init__(self, message):
        super().__init__(message)


class DuplicateRoute(Exception):
    def __init__(self, message):
        super().__init__(message)


class AppFileNotDefined(Exception):
    def __init__(self, message):
        super().__init__(message)
