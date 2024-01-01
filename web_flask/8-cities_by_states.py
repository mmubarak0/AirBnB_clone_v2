#!/usr/bin/python3
"""Flask application."""
from flask import Flask, abort, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states():
    """List all states."""
    states = storage.all(State).values()
    return render_template(
        '8-cities_by_states.html',
        states=states
    )


@app.teardown_appcontext
def downfunc(e):
    """Teardown appcontext."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
