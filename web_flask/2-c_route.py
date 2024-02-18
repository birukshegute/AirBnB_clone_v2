#!/usr/bin/python3
""" /: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ hello world fuction """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ HBnb function """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ c is fun function """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
