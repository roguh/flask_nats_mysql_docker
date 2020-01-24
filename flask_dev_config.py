import os
import random
import string
from datetime import timedelta

DEBUG = True

user = os.environ['MYSQL_USER']
pwd = os.environ['MYSQL_PASSWORD']
db = os.environ['MYSQL_DATABASE']
server = os.environ['MYSQL_URL']

# Example: 'sqlite:////tmp/test.db'
# mysql://username:password@server/db
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user}:{pwd}@{server}/{db}"

SQLALCHEMY_TRACK_MODIFICATIONS = False

secret_key = ''.join(random.choices(string.ascii_letters, k=20))
print('SECRET_KEY', secret_key)
SECRET_KEY = secret_key

JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
# TODO JWT SECRET
