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
pass = 'secret'
host = '192.168.1.10'
port = '3306'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user}:{pass}@{host}:{port}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
