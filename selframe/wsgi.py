# -*- coding: utf8 -*-
from werkzeug.wrappers import Request, Response

from .route import Router
from .logging import logger


class WebApp(object):
    def __init__(self):
        self.map_urls = Router()

    def response_404(self, request, response):
        response.data = "Oups this page is not found 404"
        return response

    def _build_response(self, handler, kwargs, request, response):
        if handler:
            logger.info("Calling route {}".format(handler.__name__))
            return handler(request, response, **kwargs)
        else:
            return self.response_404(request, response)

    def hundle_request(self, request):
        response = Response()
        handler, kwargs = self.map_urls.find_hundler(request.path)
        response = self._build_response(handler, kwargs, request, response)
        return response

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.hundle_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
