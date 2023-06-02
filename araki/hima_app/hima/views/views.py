from flask import request, redirect, url_for, render_template,flash,session #必要なもののインポート
from hima import app #

@app.route('/',methods=['GET','POST'])
def start():
    return render_template('title.html')


