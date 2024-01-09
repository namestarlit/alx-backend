#!/usr/bin/env python3
"""A Flask application configuration class"""


class Config:
    """A configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "UTC"
    BABEL_DEFAULT_TIMEZONE = "en"
