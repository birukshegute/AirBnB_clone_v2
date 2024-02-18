#!/usr/bin/python3
"""Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()"""

from flask import Flask
from flask import render_template
from models import *
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ lists states in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """closes the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
