from flask import request, redirect, url_for, render_template,flash,session #必要なもののインポート
from salary import app #

@app.route('/')
def show_entries():
    return "Hello World!"