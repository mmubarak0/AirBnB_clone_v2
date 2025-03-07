#!/usr/bin/python3
"""Flask application."""
from flask import Flask, abort, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """List all states."""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()

    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities,
    )


@app.teardown_appcontext
def downfunc(e):
    """Teardown appcontext."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
