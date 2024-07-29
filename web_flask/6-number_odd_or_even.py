#!/usr/bin/python3
"""
This script starts a flask web app
"""
from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def number(n):
    """
    Argument passed must be a number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Html number template
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    Validate even or odd
    """
    even_or_odd = "even" if n % 2 == 0 else "odd"
    values = {
        "number": n,
        "even_or_odd": even_or_odd
    }
    return render_template('6-number_odd_or_even.html', values=values)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
