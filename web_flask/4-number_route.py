#!/usr/bin/python3
""" A flask application that defines dynamic url routing with variables
listining on "0.0.0.0" and port 5000
"""

from flask import Flask


app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello():
    # A view function that dislplays a string
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # A view funciton that returns a string
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    # A view function that takes in parameters and return dynamic conten
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def pythontext(text="is cool"):
    # A view function that returns a dynamic content based on param passed
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def numbern(n):
    # A view function that returns a dynamic int value
    if type(n) == int:
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
