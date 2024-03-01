import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

# __file__ is a special attribute
# Refers to absolute pathfile of current script
basedir = os.path.abspath(os.path.dirname(__file__))

# __name__ is a special attribute
# Refers to the name of the module
app = Flask(__name__)

# We will connect to our MariaDB server using the database_URI
# mysql://username:password@host:port
# https://docs.sqlalchemy.org/en/14/core/engines.html
user = 'boomy'
password = 'secret'
host = '192.168.1.10'
port = '3306'
database = 'boomy_online'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.Integer)
    time = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    score = db.Column(db.Integer)

    def __repr__(self):
        return f'<Player {self.name}>'
