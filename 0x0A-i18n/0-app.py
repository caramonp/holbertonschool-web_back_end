#!/usr/bin/env python3
"""basic Flask app

Returns:
    HTML with Hello word
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


@app.route('/')
def index():
    """ return index.html
    """
    return render_template('index.html')
