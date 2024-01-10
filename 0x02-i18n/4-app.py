#!/usr/bin/env python3
"""A Flask application"""
from flask import Flask
from flask import request
from flask_babel import Babel
from flask import render_template


class Config:
    """A configuration class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets the best match locale"""
    requested_locale = request.args.get("locale")
    supported_lang = app.config["LANGUAGES"]

    if requested_locale in supported_lang:
        return requested_locale
    else:
        return request.accept_languages.best_match(supported_lang)


@app.route("/")
def index():
    """returns the index page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
