from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('game.config')

db = SQLAlchemy(app)

from game.views import start, play_game