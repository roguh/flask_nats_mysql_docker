#!/usr/bin/env python3
import asyncio
import os

from database import Bookmark, Reader, db
from flask import Flask, jsonify, redirect, render_template, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from flask_security import Security, SQLAlchemyUserDatastore

if len(os.environ.get('FLASK_APPLICATION_SETTINGS', '')) == 0:
    os.environ['FLASK_APPLICATION_SETTINGS'] = './flask_dev_config.py'

app = Flask(__name__)
app.config.from_envvar('FLASK_APPLICATION_SETTINGS')

db.app = app
db.init_app(app)

db.create_all()
# b = Bookmark(name='Eduard Khil',
#              link='https://en.wikipedia.org/wiki/Eduard_Khil',
#              archived_version=None)
# r = Reader(name='Hugo', bookmarks=[b])
# db.session.add(b)
# db.session.add(r)
# db.session.commit()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Pocket but better')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
