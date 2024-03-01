import os

# this config file has all our information to connect to the postgres database

cloud_host = '10.0.1.173' # Edit this to the local database IP

db_host = os.environ.get('DB_HOST', default=f'{cloud_host})
db_name = os.environ.get('DB_NAME', default='dashboard')
db_password = os.environ.get('DB_PASSWORD', default='secure_password')
db_port = os.environ.get('DB_PORT', default='5432')
db_user = os.environ.get('DB_USERNAME', default='dashboard')

SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
