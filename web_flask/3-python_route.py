#!/usr/bin/python3
""" task 1 for / and /hbnb
/c/<text>: display “C ”, followed by the value of the text variable.
/python/<text>: display Python {the value of the text variable}"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Hello world function """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Hbnb function """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_cool(text):
    """ C is fun function """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
