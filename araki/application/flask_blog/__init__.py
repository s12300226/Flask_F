from flask import Flask #flaskのインポート

app = Flask(__name__) 
app = Flask(__name__, static_folder='../_pic') 
app.config.from_object('flask_blog.config')

import flask_blog.views