# -*- coding: utf8 -*-
sample = """# -*- coding: utf8 -*-
from orbata.wsgi import WebApp

app = WebApp()


@app.map_urls.route("/home")
def home(request, response):
    # An example of hello world.
    response.data = 'Hello world!!!!'
    return response


if __name__ == '__main__':
    app.run()
"""
