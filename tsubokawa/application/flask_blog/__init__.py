# Flaskインポート
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flaskアプリケーション本体の作成
app = Flask(__name__)

# flask_blogフォルダ内,config.pyをconfigとして扱う
app.config.from_object('flask_blog.config')


db = SQLAlchemy(app)

from flask_blog.views.entries import entry

# ログインしたら/usersがつく
app.register_blueprint(entry, url_prefix='/users')


from flask_blog.views.views import view
app.register_blueprint(view)


# viewsファイルのインポート
from flask_blog.views import views, entries
