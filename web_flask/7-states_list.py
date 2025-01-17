#!/usr/bin/python3
# File: 7-states_list.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

""""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:
            /states_list: Display HTML and state info from storage;
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    """After each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
       States are sorted by name.
    """
    states = storage.all(State).values()
    return(render_template("7-states_list.html", states=states))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
