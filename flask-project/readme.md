# Flask app that links a python project to a (postgres/mariadb) database

This app creates an API which we can use to connect a separate python app to a database

## First steps
Create a directory for our project. Let's call it 'project'

Move into 'project' and create a virtual python environment. We are going with python3.7

Make sure to move into the directory 'project' to store all files

We can use: **pipenv --python=$(which python3.7) install flask**

To activate a virtual environment we can run: **pipenv shell**

Also make sure postgres is installed too (sudo apt-get install postgresql)

## Configure __init__.py
Mainly stolen from official [documentation](https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/)

Set some environmental variables in shell: 

```
export FLASK_ENV=development
export FLASK_APP='.'
# flask run --host=0.0.0.0 --port=3000
# flask --app flaskr run --debug
```

## Database connection (postgres)

We use psycopg2 as a database adapter: pipenv install psycopg2 Flask-SQLAlchemy

config.py has some parameters that need tweaking. This assumes postgres is already installed and running

```
db_host = os.environ.get('DB_HOST', default='< DB_PRIVATE_IP >')
db_name = os.environ.get('DB_NAME', default='dashboard')
db_password = os.environ.get('DB_PASSWORD', default='secure_password')
db_port = os.environ.get('DB_PORT', default='5432')
db_user = os.environ.get('DB_USERNAME', default='dashboard')
```

The method of us applying these config requires us altering the environmental variables in our virtual python environment

You could replace the defaults with the actual values in this script but then anyone has access to them...

## Creating out database

The models.py file contains the structure of our database

We use SQLAlchemy to map a python dictionary to SQL objects

```
pipenv install psycopg2 Flask-SQLAlchemy
```
