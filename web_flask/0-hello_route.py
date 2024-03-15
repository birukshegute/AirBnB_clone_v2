#!/usr/bin/python3
"""  starts a Flask web application:
The web application listening on 0.0.0.0, port 5000 """

from flask import Flask


app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """ Hello world function """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
