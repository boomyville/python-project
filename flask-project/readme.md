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

Configure the login details
```
user = 'boomy'
password = 'secret'
host = '192.168.1.10'
port = '3306'
database = 'boomy_online'
```
Configure [SQLALCHEMY_DATABASE_URI](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) if not using MariaDB
Run the app using the following command:
```
# flask run --host=0.0.0.0 --port=3000
```

## Configuring the database

Create a database in MariaDB and give it a name



## Configuring the HTML

We wrap python variables with {% %}


