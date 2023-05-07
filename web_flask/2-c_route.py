#!/usr/bin/python3
"""A Flask web app that uses dynamic variable to display dynamic url routing
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return a strings"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return a string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def dynamic_text(text):
    """ Return the given variable"""

    return 'C {}'.format(text.replace("_", " ")4)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
