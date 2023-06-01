# Flaskインポート
from flask import Flask


# Flaskアプリケーション本体の作成
app = Flask(__name__)


# viewsファイルのインポート
import flask_blog.views