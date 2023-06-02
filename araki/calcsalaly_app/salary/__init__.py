from flask import Flask #flaskのインポート

app = Flask(__name__) 
app.config.from_object('salary.config')

import salary.views.views