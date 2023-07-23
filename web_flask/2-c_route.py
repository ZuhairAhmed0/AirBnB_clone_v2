#!/usr/bin/python3
"""
that starts a Flask web application
"""


from markupsafe import escape
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """ display “Hello HBNB!” """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display “HBNB” """
    return "HBNB"

@app.route("/c/<text>" strict_slashes=False)
def c_route(text):
    """ display “C ” followed by the value of the text variable """
    return "C {}".format(escape(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
