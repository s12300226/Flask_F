from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('pokemon.config')

db = SQLAlchemy(app)

# 最後に使用するファイルをインポートする
from pokemon.views import home