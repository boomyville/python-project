# Creating a flask app that links a python project to a (postgres/mariadb) database

## First steps
Create a directory for our project. Let's call it 'project'
Move into 'project' and create a virtual python environment. We are going with python3.7
We can use: **pipenv --python=$(which python3.7) install flask **
To activate a virtual environment we can run: **pipenv shell**

## Configure __init__.py
Mainly stolen from official (documentation)[https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/]
Set some environmental variables in shell: 
```
export FLASK_ENV=development
export FLASK_APP='.'
# flask run --host=0.0.0.0 --port=3000
# flask --app flaskr run --debug
```

## Database connection (postgres)
We use psycopg2 as a database adapter: pipenv install psycopg2 Flask-SQLAlchemy


