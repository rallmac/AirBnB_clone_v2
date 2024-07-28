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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
