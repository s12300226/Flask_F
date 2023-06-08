from flask import Flask #flaskのインポート

app = Flask(__name__) 
app.config.from_object('hima.config')

import hima.views.views