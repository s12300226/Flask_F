from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('car_report.config')

db = SQLAlchemy(app)

# 最後に使用するファイルをインポートする
from car_report.views import input