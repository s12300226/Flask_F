from holiday import app
from flask import request, redirect, url_for, render_template, flash, session


@app.route('/')
def home():
    """
    祝日の入力画面に戻る処理
    """
    return render_template('input.html')