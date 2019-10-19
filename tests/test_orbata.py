# -*- coding: utf8 -*-
import pytest

from wsgi import WebApp


@pytest.fixture
def app():
    return WebApp()


def test_basic_route(app):
    @app.map_urls.route("/home")
    def home(request, response):
        response.data = 'From Home Test'
        return response
