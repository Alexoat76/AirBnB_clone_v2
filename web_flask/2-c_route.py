#!/usr/bin/python3
# File: 2-c_route.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:         Display "Hello HBNB!"
            /hbnb:     Display "HBNB"
            /c/<text>: Display "C" + text (replace underscores with space)
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Displays 'C' followed by the value of <text>."""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
