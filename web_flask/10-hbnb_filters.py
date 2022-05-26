#!/usr/bin/python3
# File: 10-hbnb_filters.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

""""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:
            /hbnb_filters:        Display a HTML page like 6-index.html
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    """After each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters')
def states_and_cities():
    """Display html page with working city/state filters & amenities
       Runs with web static css files
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    dict = {"states": states, "amenities": amenities}
    return(render_template("10-hbnb_filters.html", **dict))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
