#!/usr/bin/python3
""" A python Script that starts a Flask web app
    and listens on 0.0.0.0, port 5000
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ A route that displays "Hello HBNB" """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A route that displays 'HBNB' """
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
