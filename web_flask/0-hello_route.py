#!/usr/bin/python3
# File: 0-hello_route.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /: Display "Hello HBNB!"
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
