#!/usr/bin/python3
"""A Flask web application that listens on '0.0.0.0' and port '5000'
and displays a dynamic content based on the variable in the url routing
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """a view that returns a string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ a view that returns a string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """A view function that takes a dynamic variable and return the variable"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/<text>', strict_slashes=False)
def pythontext(text):
    """A view function that takes in a dynamic
    variable and return the variable
    """
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
