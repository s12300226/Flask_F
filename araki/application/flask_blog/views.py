from flask import request, redirect, url_for, render_template,flash,session #必要なもののインポート
from flask_blog import app #

@app.route('/')
def show_entries():
    return render_template('entries/index.html')