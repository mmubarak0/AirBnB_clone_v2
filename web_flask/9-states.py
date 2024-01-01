#!/usr/bin/python3
"""Flask application."""
from flask import Flask, abort, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """List all states."""
    states = storage.all(State).values()
    return render_template(
        '9-states.html',
        states=states,
        detail_view=False
    )


@app.route("/states/<id>", strict_slashes=False)
def state_detail(id):
    """List all states."""
    key = f"State.{id}"
    state = storage.all(State).get(key, None)
    return render_template(
        '9-states.html',
        state=state,
        detail_view=True
    )


@app.teardown_appcontext
def downfunc(e):
    """Teardown appcontext."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
