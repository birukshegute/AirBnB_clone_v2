#!/usr/bin/python3
""" The same as task 4:
Addition: display a HTML page only if n is an integer
H1 tag: “Number: n is even|odd” inside the tag BODY"""

from flask import Flask
from flask import render_template


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


@app.route('/number_template/<int:n>')
def number_template(n):
    """ displays template html if n is integer """
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """displays nis odd or n is even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
