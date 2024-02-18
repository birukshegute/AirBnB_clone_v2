#!/usr/bin/python3
""" It is the same as task 3,
Additional:  display “n is a number” only if n is an integer"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ hello world fuction """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ hbnb function"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ c is fun function """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_is_fun(text='is cool'):
    """ Python is fun function """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def n_is_a_number(n):
    """ n is a number function"""
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
