# -*- coding: utf8 -*-
from werkzeug.serving import run_simple
from wsgi import WebApp

app = WebApp()


@app.route("/home")
def home(request, response):
    response.data = 'From Home'
    return response


@app.route("/product/{id}")
def home(request, response, id):
    response.data = 'Product with id: {}'.format(id)
    return response


run_simple('127.0.0.1', 5000, app, use_reloader=True, use_debugger=True)
