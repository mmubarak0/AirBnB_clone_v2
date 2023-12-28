#!/usr/bin/python3
"""Flask application."""
from flask import Flask, abort


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytext(text="is cool"):
    """Python text path."""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def numbern(n):
    """N number path."""
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
