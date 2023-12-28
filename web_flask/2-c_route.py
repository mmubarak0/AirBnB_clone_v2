#!/usr/bin/python3
"""Flask application."""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """Root path."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Hbnb path."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """C text path."""
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
