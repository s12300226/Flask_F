# Flaskインポート
from flask import Flask


# Flaskアプリケーション本体の作成
app = Flask(__name__)

# flask_blogフォルダ内,config.pyをconfigとして扱う
app.config.from_object('calcsalary.config')

# viewsファイルのインポート
import calcsalary.views
