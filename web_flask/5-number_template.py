#!/usr/bin/python3
""" A flask web app that renders a template with dynamic content and
using the jinja template enging, running on 0.0.0.0 and port 5000
"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    # A view func that returns a string
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A view func that returns a string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text='is cool'):
    """A view function that reutrns a dynamic variable"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def pythontext(text='is cool'):
    """ A vie function that returns a dynamic variable"""
    return 'Python {)'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def numbern(n):
    """A view functionathat returns a dynamic variable"""
    if type(n) == int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def templaten(n):
    """A view function that renders a template"""
    if type(n) == int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
