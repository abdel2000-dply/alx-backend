#!/usr/bin/env python3
'''Parametrize templates
'''
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''Config class
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''Get locale from request
    '''
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''Main route
    '''
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
