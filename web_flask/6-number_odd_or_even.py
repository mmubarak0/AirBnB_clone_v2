#!/usr/bin/python3
"""Flask application."""
from flask import Flask, abort, render_template


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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """N template path."""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """N even or odd path."""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, t="even")
    return render_template('6-number_odd_or_even.html', n=n, t="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
