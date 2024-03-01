import os

# Runs a basic python script to initialise the flask app

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'))
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)  # Silent means nothing will be mentioned about this command 10     
    else:
        app.config.from_mapping(test_config)
    
    from models import db
    db.init_app(app)
    return app
