from flask import make_response

from app import app


@app.route('/')
def index():
    old = str(app.config['DEBUG'])
    app.config['DEBUG'] = False
    return old

