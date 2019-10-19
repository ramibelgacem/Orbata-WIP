# Orbata
A web framework based on Werkzeug. 
The goal here is to learn how a web framework works
and apply best pratices along with OOP and design patterns (Hopefully).

This work is inspired by Jahongir Rahmonov [tutorial](http://rahmonov.me/posts/write-python-framework-part-one/) and [Flask](https://github.com/pallets/flask) web framework project.

## Installing
Clone the repos

```bash
git clone https://github.com/ramibelgacem/orbata.git
```
Move to orbata folder
```bash
cd orbata
```
Create a virtual environnement and execute it
```bash
python -m venv venv
venv\Scripts\activate.bat # windows
source <venv>/bin/activate # Linux
```
Install
```bash
pip3 install -r requirements.txt
python setup.py develop
```

## Quick start
Generate a sample
```bash
orbata build --name=project_name
```
Or Create a file called app.py in your new project folder
```python
# -*- coding: utf8 -*-
from orbata import WebApp

app = WebApp()


@app.map_urls.route("/home")
def home(request, response):
    # A a example of hello world.
    response.data = 'Hello world!'
    return response
```
Run the server
```bash
cd project_name
python app.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Done and to Improve
* WSGI
* Routing
* Exceptions
* Cli

## Todo
* Tests
* ORM
* Templating
* Logging
* Session
* Caching
* Middleware
* Security
* Restfull API
* Documentation (sphinx)
* Concurrency