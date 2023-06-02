from flask import Flask #flaskのインポート
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../_pic') 
app.config.from_object('flask_blog.config')

db=SQLAlchemy(app)

import flask_blog.views