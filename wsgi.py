# -*- coding: utf8 -*-
import parse

from werkzeug.wrappers import Request, Response


class WebApp(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def response_404(self, request, response):
        response.data = "Oups this page is not found 404"
        return response

    def find_hundler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse.parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return False, False

    def build_response(self, handler, kwargs, request, response):
        if handler:
            return handler(request, response, **kwargs)
        else:
            return self.response_404(request, response)

    def hundle_request(self, request):
        response = Response()
        handler, kwargs = self.find_hundler(request.path)
        response = self.build_response(handler, kwargs, request, response)
        return response

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.hundle_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)