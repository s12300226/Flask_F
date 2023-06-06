from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('holiday.config')

db = SQLAlchemy(app)

# 最後に使用するファイルをインポートする
from holiday.views import list, input, maintenance_date