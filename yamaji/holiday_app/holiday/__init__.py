from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app = Flask(__name__, static_folder='./templates/entries/imgs')

app.config.from_object('holiday.config')

db = SQLAlchemy(app)

from holiday.views import input, list, maintenance_data