# -*- coding: utf8 -*-
sample = """# -*- coding: utf8 -*-
from orbata import WebApp

app = WebApp()


@app.map_urls.route("/home")
def home(request, response):
    # A a example of hello world.
    response.data = 'Hello world!'
    return response
"""
