  1 import os
  2
  3 from flask import Flask
  4
  5 def create_app(test_config=None):
  6     app = Flask(__name__)
  7     app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),)
  8     if test_config is None:
  9         app.config.from_pyfile('config.py', silent=True) # Silent means nothing will be mentioned about this command 10     else:
 11         app.config.from_mapping(test_config)
 12
 13     from .models import db
 14     db.init_app(app)
 15
 16     return app
