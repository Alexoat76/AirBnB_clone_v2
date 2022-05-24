#!/usr/bin/python3
# File: 3-python_route.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:              Display "Hello HBNB!"
            /hbnb:          Display "HBNB"
            /c/<text>:      Display "C" + text (replace underscores with space)
            /python/<text>: Display "Python" + text (default is "is cool")
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


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Displays 'Python' followed by the value of <text>.
    first route statement ensures it works for:
    curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
    curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
