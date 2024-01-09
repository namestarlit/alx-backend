#!/usr/bin/env python3
"""A Flask application"""
from flask import Flask
from flask_babel import Babel
from flask import render_template


# Instantiate the flask object
app = Flask(__name__)
# Instantiate babel object
babel = Babel(app)


# Set configuration from Config class
class Config:
    """A configuration class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Set the configuration from Config class
app.config.from_object(Config)


@app.route("/")
def index():
    """returns the index page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
