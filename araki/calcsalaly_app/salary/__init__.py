from flask import Flask #flaskのインポート

app = Flask(__name__) 
app.config.from_object('salaly.config')

import salaly.views