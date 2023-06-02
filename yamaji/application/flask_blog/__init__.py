from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app = Flask(__name__, static_folder='./templates/entries/imgs')

app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views import views, entries