# Flask app that links a python project to a mariaDB database

This app creates an API which we can use to connect a separate python app to a database

## First steps
Create a directory for our project. Let's call it 'project'

Move into 'project' and create a virtual python environment. We are going with python3.7

Make sure to move into the directory 'project' to store all files

We can use: **pipenv --python=$(which python3.7) install flask Flask-SQLAlchemy**

To activate a virtual environment we can run: **pipenv shell**

Also make sure mariaDB is installed
```
sudo apt-get install -y libmariadb-dev
```
Then in our virtual environment:

```
pip install mariadb
```

## Configure app.py
Mainly stolen from official [documentation](https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/)

Configure database connection; edit [SQLALCHEMY_DATABASE_URI](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) if not using MariaDB

```
user = 'boomy'
password = 'secret'
host = 'XXX.XXX.XXX.XXX'
port = '3306'
database = 'database_name'
```
Make sure there is a database called **guestbook** created and a table called **book**

Run the app using the following command:
```
# flask run --host=0.0.0.0 --port=3000
```

## Configuring the database

Create a database in MariaDB and give it a name

For this example we are creating a book dictionary with the following parameters:

```
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    msg = db.Column(db.String(100), nullable=False)

```

## Configuring the HTML

We wrap python variables with {% %}

The templates/index.html is our homepage

It loops through all entries in the database and spits out a list of them which are then shown in <div> blocks

Each block will show a name and a hyperlink to the actual comment

The templates/page.html is rendered when host/id is accessed (id being the database id of the guestbook page)

So for example flask.app:3000/5 will load the 5th database entry (well database.id == 5)

In this page we also render the message that the user left


