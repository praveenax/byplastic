from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import constants
import config

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app, session_options={"autoflush": True, 'autocommit': True})

import backend_app.controllers
