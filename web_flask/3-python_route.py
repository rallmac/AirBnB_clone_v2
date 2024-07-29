#!/usr/bin/python3
"""
This script starts a flask web app
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """
    Default response
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Returns HBNB only
    """
    return "HBNB"


@app.route('/c/<text>')
def c_with_params(text):
    """
    c with params
    """
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_params(text):
    """
    Text parameters of python
    """
    text_no_underscore = text.replace('_', ' ')
    return "Python {}".format(text_no_underscore)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
