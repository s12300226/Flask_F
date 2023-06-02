from flask import Flask

app = Flask(__name__)
# app = Flask(__name__, static_folder='./templates/entries/imgs')

app.config.from_object('salary.config')

import salary.views.views