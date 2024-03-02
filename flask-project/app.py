import os, socket
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

# A summary of the packages we use
# OS is only used to determine path of this script
# socket is used to get ipaddress
# flask is used to connect HTML / database / python
# flask also includes a whole bunch of functions such as render_template, request, url_redirect
# sqlalchemy is used to connect to a database
# Inspired by this tutorial: https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application

# To do list:
# Implement @app.route('/<int:pageId>/')
# Show a single message

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
host = '127.0.0.1'
port = '3306'
database = 'guestbook'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# We create a book object 
# It will hold values we will store in the database

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.Integer)
    time = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    msg = db.Column(db.String(100), nullable=False)

    # This __repr__ (representation) will be returned when the above class is called
    def __repr__(self):
        return f'<Guest: {self.name}>'

# Flask uses @app.function to perform its actions
# route '/' will run when the user goes to url:port/
# This is effectively the 'main page'
# In this scenario we do a query to find all instances in the database and present it to the user

@app.route('/')
def index():
    guests = Book.query.all()
    return render_template('index.html', guests=guests)

# We also create a function that will create a new entry in our guestbook

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        msg = str(request.form['msg'])
	    # Grab IP address using sockets and time using SQLAlchemy func
        guest = Book(name=name, msg=msg, ip=socket.gethostbyname(socket.gethostname()), time=func.now()) 
        db.session.add(guest)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')
