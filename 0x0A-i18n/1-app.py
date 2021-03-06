#!/usr/bin/env python3
"""basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Class to config available languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """ return index.html
    """
    return render_template('1-index.html')
