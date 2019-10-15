# -*- coding: utf8 -*-
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

from .logging import logger
from .route import Router


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


def run(self,
        app,
        host='127.0.0.1',
        port=5000,
        use_reloader=False,
        use_debugger=True):
    """ Start a server instance.
        :param app: WSGI application.
        :param host: Server address to bind to. (default: 127.0.0.1)
        :param port: Server port to bind to. (default: 5000)
        :param use_reloader: Start auto-reloading server? (default: False)
        :param use_debugger: Auto-reloader interval in seconds (default: 1)
     """
    run_simple(
        host,
        port,
        app,
        use_reloader=use_reloader,
        use_debugger=use_debugger,
    )
