from flask import Flask #flaskのインポート

app = Flask(__name__, static_folder='../_pic') 
app.config.from_object('hima.config')

import hima.views.views