# Flaskインポート
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flaskアプリケーション本体の作成
app = Flask(__name__)

# flask_blogフォルダ内,config.pyをconfigとして扱う
app.config.from_object('flask_blog.config')


db = SQLAlchemy(app)

# viewsファイルのインポート
from flask_blog.views import views, entries
