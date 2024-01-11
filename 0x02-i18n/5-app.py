#!/usr/bin/env python3
"""A Flask application"""
from flask import Flask
from flask import request, g
from flask_babel import Babel
from flask import render_template
from typing import Union, Dict


class Config:
    """A configuration class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Gets user's credentials"""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id), None)
    return None


@app.before_request
def before_request() -> None:
    """set the user to global variable"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Gets the best match locale"""
    requested_locale = request.args.get("locale")
    supported_lang = app.config["LANGUAGES"]

    if requested_locale in supported_lang:
        return requested_locale
    else:
        return request.accept_languages.best_match(supported_lang)


@app.route("/")
def index() -> str:
    """returns the index page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
